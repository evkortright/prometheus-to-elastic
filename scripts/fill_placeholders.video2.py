#!/usr/bin/env python3
"""Fill the {{placeholders}} in Module 1, Video 2's narrative from a values file, and (optionally)
build the placeholder-free review script with the root's make_review_script.py.

Usage (one command, values file to review script):
  python3 scripts/fill_placeholders.video2.py --narrative docs/module1-video2-narrative.md \\
      --values take-values.video2.json --stage provisional --date "Oct 30, 2026" \\
      --review-out ~/module1-video2-review-provisional.txt

Dummy mode (for a wording review before any measurement exists):
  python3 scripts/fill_placeholders.video2.py --narrative docs/module1-video2-narrative.md --dummy \
      --date "Oct 28, 2026" --review-out ~/module1-video2-review-DUMMY.txt
  The built-in DUMMY values are not measurements; the review script says so in its header.

Other outputs (any combination):
  --out-narrative PATH   a copy of the whole narrative with the spoken blocks filled
  --out-blocks PATH      the spoken blocks only, named, for the speech engine
  --check-only           validate the values and print the table; write nothing

What it does
  * Reads the values file (full precision kept as text; keys that start with "_" are notes).
  * Computes DIGITS_B, DIGITS_C and DIGITS_D: the leading significant digits the two full-precision
    values share (register row 64). No percent form is ever produced.
  * Formats every number for speech: counts and seconds whole; rates, per-minute values and the
    ratio to three decimals (the ratio's decimals are --ratio-decimals; the form is still open).
  * Replaces {{PLACEHOLDER}} only inside the fenced spoken blocks. Tables and notes keep theirs.
  * Stops with an error if a value is missing or null, or if the narrative uses a placeholder it
    does not know. It warns about the things that need a person (few digits, a likely straddled
    scrape minute, differing counts, a zero ratio).
It changes no repo file. Run it from the repo root, with the values file outside the repo.
"""
import argparse, json, os, re, subprocess, sys, tempfile
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# value key -> how it is spoken
COUNTS = ["a_frontend_prom", "a_frontend_elastic", "a_err_frontend_prom", "a_err_frontend_elastic",
          "d_rows_prom", "d_rows_elastic"]
SECONDS = ["seconds_a", "seconds_a_base", "seconds_b", "seconds_c", "seconds_d"]
RATES = ["b_prom", "b_elastic", "c_frontend_prom", "c_frontend_elastic"]
RATIOS = ["d_payment_prom", "d_payment_elastic"]
KEYS = COUNTS + SECONDS + RATES + RATIOS

# placeholder -> (kind, value key[s])
PLACEHOLDERS = {
    "A_FRONTEND_PROM": ("count", "a_frontend_prom"), "A_FRONTEND_ELASTIC": ("count", "a_frontend_elastic"),
    "SECONDS_A": ("seconds", "seconds_a"),
    "A_ERR_FRONTEND_PROM": ("count", "a_err_frontend_prom"), "A_ERR_FRONTEND_ELASTIC": ("count", "a_err_frontend_elastic"),
    "SECONDS_A_BASE": ("seconds", "seconds_a_base"),
    "B_PROM": ("rate", "b_prom"), "B_ELASTIC": ("rate", "b_elastic"),
    "SECONDS_B": ("seconds", "seconds_b"), "DIGITS_B": ("digits", ("b_prom", "b_elastic")),
    "C_FRONTEND_PROM": ("rate", "c_frontend_prom"), "C_FRONTEND_ELASTIC": ("rate", "c_frontend_elastic"),
    "SECONDS_C": ("seconds", "seconds_c"), "DIGITS_C": ("digits", ("c_frontend_prom", "c_frontend_elastic")),
    "D_ROWS_PROM": ("count", "d_rows_prom"), "D_ROWS_ELASTIC": ("count", "d_rows_elastic"),
    "D_PAYMENT_PROM": ("ratio", "d_payment_prom"), "D_PAYMENT_ELASTIC": ("ratio", "d_payment_elastic"),
    "SECONDS_D": ("seconds", "seconds_d"), "DIGITS_D": ("digits", ("d_payment_prom", "d_payment_elastic")),
}

def die(msg):
    print("ERROR:", msg, file=sys.stderr); sys.exit(1)

def dec(s, name):
    if s is None: die(f"'{name}' is null: fill every value from the take log")
    try: return Decimal(str(s))
    except InvalidOperation: die(f"'{name}' is not a number: {s!r}")

def sci(d):
    """(digit string without leading zeros, decimal exponent of the first digit)."""
    sign, digits, exp = d.normalize().as_tuple()
    ds = "".join(map(str, digits)).lstrip("0")
    if not ds: return "", 0
    return ds, len(digits) + exp - 1

def shared_digits(a, b):
    da, ea = sci(a); db, eb = sci(b)
    if not da or not db or ea != eb: return 0
    m = max(len(da), len(db))                     # an exact value such as 0.03125 has implicit zeros after it
    da, db = da.ljust(m, "0"), db.ljust(m, "0")
    n = 0
    for x, y in zip(da, db):
        if x != y: break
        n += 1
    return n

def rel(a, b):
    return abs(a - b) / abs(a) if a != 0 else Decimal(0)

def whole(d): return str(int(d.to_integral_value()))
def fixed(d, places): return f"{d.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP):f}"

FENCE = re.compile(r"(```\n)(.*?)(\n```)", re.S)

# DUMMY values, for wording review only. They are NOT measurements, and every output they feed is labelled.
DUMMY = {"_note": "DUMMY VALUES built into the helper, for wording review only. They are not measurements.",
         "a_frontend_prom": "36", "a_frontend_elastic": "36", "seconds_a": "14",
         "a_err_frontend_prom": "14", "a_err_frontend_elastic": "14", "seconds_a_base": "9",
         "b_prom": "46.37547088", "b_elastic": "46.37547091", "seconds_b": "15",
         "c_frontend_prom": "767.31394283", "c_frontend_elastic": "767.31394277", "seconds_c": "7",
         "d_rows_prom": "8", "d_rows_elastic": "8", "d_payment_prom": "0.31251234", "d_payment_elastic": "0.31251239", "seconds_d": "9"}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--narrative", required=True)
    ap.add_argument("--values", help="the values file (not needed with --dummy)")
    ap.add_argument("--dummy", action="store_true", help="use the built-in DUMMY values (labelled; not measurements)")
    ap.add_argument("--out-narrative"); ap.add_argument("--out-blocks"); ap.add_argument("--review-out")
    ap.add_argument("--config", default=None, help="review config (default: review-config.video2.json next to this script)")
    ap.add_argument("--stage", choices=["provisional", "final", "dummy"], default="provisional")
    ap.add_argument("--date", default="", help='e.g. "Oct 30, 2026"; goes into the review script header')
    ap.add_argument("--ratio-decimals", type=int, default=3)
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()

    if a.dummy: a.stage = "dummy"
    if not a.dummy and not a.values: die("give --values, or --dummy")
    if a.dummy: raw = dict(DUMMY); print("DUMMY VALUES in use: nothing below is a measurement.\n")
    else: raw = json.loads(open(a.values).read(), parse_float=str, parse_int=str)  # full precision as text
    for k in KEYS:
        if k not in raw: die(f"the values file has no '{k}'")
    v = {k: dec(raw[k], k) for k in KEYS}
    for k in COUNTS + SECONDS:
        if v[k] != v[k].to_integral_value() or v[k] < 0: die(f"'{k}' must be a whole number, not {raw[k]!r}")

    text = open(a.narrative, encoding="utf-8").read()
    used = set(re.findall(r"\{\{([A-Z_]+)\}\}", "".join(m.group(2) for m in FENCE.finditer(text))))
    unknown = sorted(used - set(PLACEHOLDERS))
    if unknown: die(f"the narrative uses placeholders this script does not know: {unknown}")

    fill = {}
    for name, (kind, key) in PLACEHOLDERS.items():
        if kind == "count" or kind == "seconds": fill[name] = whole(v[key])
        elif kind == "rate": fill[name] = fixed(v[key], 3)
        elif kind == "ratio": fill[name] = fixed(v[key], a.ratio_decimals)
        elif kind == "digits": fill[name] = str(shared_digits(v[key[0]], v[key[1]]))

    # ---- warnings: things that need a person
    warnings = []
    for label, (k1, k2), ph in [("idea 2", ("b_prom", "b_elastic"), "DIGITS_B"),
                                ("idea 3", ("c_frontend_prom", "c_frontend_elastic"), "DIGITS_C"),
                                ("idea 4", ("d_payment_prom", "d_payment_elastic"), "DIGITS_D")]:
        if v[k1] == 0 and v[k2] == 0:
            warnings.append(f"{label}: both values are 0, so the digits sentence cannot be filled. For idea 4, check that the flag is on and has settled.")
            continue
        n = int(fill[ph])
        if n < 4: warnings.append(f"{label}: the two values share only {n} leading digit(s): rewrite the 'agree to N digits' sentence, don't fill it (register row 64).")
        r = rel(v[k1], v[k2])
        if r > Decimal("0.001"): warnings.append(f"{label}: relative difference {r:.2e}: a new scrape sample probably landed between the two runs. Consider retaking the pair inside one scrape minute.")
    if v["a_frontend_prom"] != v["a_frontend_elastic"]: warnings.append("idea 1, first pair: the series counts differ: check before saying the numbers agree.")
    if v["a_err_frontend_prom"] != v["a_err_frontend_elastic"]: warnings.append("idea 1, second pair: the series counts differ: check before saying the numbers agree.")
    if v["a_err_frontend_prom"] == 0 or v["a_err_frontend_elastic"] == 0: warnings.append("idea 1, second pair: the error row has 0 series, so the pair would not show it.")
    if v["d_rows_prom"] != v["d_rows_elastic"]: warnings.append("idea 4: the row counts differ: check before filling.")
    for k in SECONDS:
        if v[k] > 40: warnings.append(f"{k} is {whole(v[k])} s: the two runs may have straddled a scrape (the safe window is about 50 s).")

    # ---- fill only inside the fenced spoken blocks
    def sub(block): return re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: fill[m.group(1)], block)
    filled = FENCE.sub(lambda m: m.group(1) + sub(m.group(2)) + m.group(3), text)
    left = [m.group(2) for m in FENCE.finditer(filled) if "{{" in m.group(2)]
    if left: die("a placeholder is left inside a spoken block after filling")

    print(f"{'placeholder':24s}value")
    for k in sorted(used): print(f"{k:24s}{fill[k]}")
    print(f"\nplaceholders in the spoken blocks: {len(used)} (all filled)   unused: {sorted(set(PLACEHOLDERS) - used) or 'none'}")
    for w in warnings: print("WARNING:", w)
    if not warnings: print("No warnings.")
    note = str(raw.get("_note", ""))
    if note: print("values file note:", note)
    if a.check_only: return

    if a.out_narrative:
        open(a.out_narrative, "w", encoding="utf-8").write(filled); print(f"Wrote {a.out_narrative}")
    if a.out_blocks:
        parts, head = [], ("DUMMY NARRATION (placeholders filled with DUMMY values; not measurements)" if a.dummy
                           else "FILLED NARRATION (" + a.stage + "; placeholders filled from the values file)")
        sections = re.split(r"(?m)^## ", filled)[1:]
        for sec in sections:
            title = sec.split("\n", 1)[0].strip()
            for i, m in enumerate(FENCE.finditer(sec), 1):
                parts.append(f"== {title} [{i}] ==\n{m.group(2)}\n")
        open(a.out_blocks, "w", encoding="utf-8").write(head + "\n\n" + "\n".join(parts)); print(f"Wrote {a.out_blocks}: {len(parts)} blocks")

    if a.review_out:
        here = os.path.dirname(os.path.abspath(__file__))
        builder = os.path.join(here, "make_review_script.py")
        cfg_path = a.config or os.path.join(here, "review-config.video2.json")
        if not os.path.exists(builder): die(f"cannot find {builder}")
        cfg = json.load(open(cfg_path, encoding="utf-8"))
        when = f" of {a.date}" if a.date else ""
        status = {"provisional": f"(Numbers are from the rehearsal{when} and will be replaced by the final recording's.)",
                  "final": f"(Numbers are from the final recording{when}.)",
                  "dummy": "(The numbers in this script are DUMMY values, so that it reads without placeholders. They are not measurements; the recording's numbers replace them.)"}[a.stage]
        if str(cfg.get("title_narration", "")).startswith("WRITE THE TITLE NARRATION HERE"):
            die("the title narration in the review config is still the marker: write it (and have the author approve it) first")
        hdr = []
        for l in cfg.get("header", []):
            if l.startswith("Voice-over script"): l = f"Voice-over script, review draft ({a.stage})" + (f", {a.date}" if a.date else "")
            if "{{double braces}}" in l: continue
            hdr.append(l)
        cfg["header"] = hdr + [status]
        tmp_dir = tempfile.mkdtemp()
        try:
            narr_tmp = os.path.join(tmp_dir, "narrative-filled.md"); cfg_tmp = os.path.join(tmp_dir, "config.json")
            open(narr_tmp, "w", encoding="utf-8").write(filled); json.dump(cfg, open(cfg_tmp, "w", encoding="utf-8"))
            r = subprocess.run([sys.executable, builder, "--narrative", narr_tmp, "--config", cfg_tmp, "--out", a.review_out],
                               capture_output=True, text=True)
            sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
            if r.returncode != 0: die("make_review_script.py failed")
        finally:
            for f in os.listdir(tmp_dir): os.remove(os.path.join(tmp_dir, f))
            os.rmdir(tmp_dir)
        out = open(a.review_out, encoding="utf-8").read()
        if "{{" in out: die("the review script still holds a placeholder: " + sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", out)))[0])
        print(f"Review script has no placeholders. {a.stage.capitalize()} stage.")

if __name__ == "__main__":
    main()
