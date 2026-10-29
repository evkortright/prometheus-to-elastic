#!/usr/bin/env python3
"""Fill the {{placeholders}} in Module 1, Video 1's narration from the take's numbers.

Added Oct 28, 2026 (author's request, made in the Video 2 chat): --dummy, --stage, --date, --review-out, --config, --out-narrative;
the original usage below is unchanged.

Usage:
  python3 fill_placeholders.py --narrative docs/module1/video1/module1-video1-narrative.md \
      --values take-values.json --out narration-final.txt

Review script without placeholders (added Oct 28; from the repo root; the review script is written outside the repo):
  python3 scripts/fill_placeholders.py --narrative docs/module1/video1/module1-video1-narrative.md --dummy \\
      --date "Oct 28, 2026" --review-out ~/module1-video1-review-DUMMY.txt
  python3 scripts/fill_placeholders.py --narrative docs/module1/video1/module1-video1-narrative.md \\
      --values ~/take-values.json --stage provisional --review-out ~/module1-video1-review-provisional.txt
  (--stage final after the take. Without --out, a --review-out run does not write narration-final.txt.)

Reads the nine spoken blocks (the nine fenced blocks) from the narrative, computes the derived
numbers (the digits the two rung 2 values share, the relative differences), formats every
number for speech, replaces each {{PLACEHOLDER}}, and writes the nine filled blocks.
It changes no repo file. It stops with an error if a placeholder has no value.
"""
import argparse, json, os, re, subprocess, sys, tempfile
from decimal import Decimal, InvalidOperation

NAMES = ["Opening (slide)", "Setup (Clip A)", "Rung 1, Prometheus (Clip B1)", "Rung 1, Elastic (Clip B2)",
         "Rung 2, Prometheus (Clip C1)", "Rung 2, Elastic (Clip C2)", "Rung 3, Prometheus (Clip D1)",
         "Rung 3, Elastic (Clip D2)", "Recap (slide)"]
KEYS = ["n_prom", "n_elastic", "prom_value", "elastic_value", "seconds_c",
        "rows_prom", "rows_elastic", "prom_frontend", "elastic_frontend", "seconds_d"]

# DUMMY values (added Oct 28, 2026, at the author's request): they let the narration be read, and a review
# script be built, without {{placeholders}}. They are NOT measurements; every output they feed is labelled.
DUMMY = {"_note": "DUMMY VALUES built into the helper, for wording review only. They are not measurements.",
         "n_prom": "41", "n_elastic": "41", "prom_value": "15.1234567891", "elastic_value": "15.1234567958",
         "seconds_c": "8", "rows_prom": "18", "rows_elastic": "18",
         "prom_frontend": "13.9216454", "elastic_frontend": "13.9216454", "seconds_d": "10"}
STATUS = {"provisional": "(Numbers are from the rehearsal{when} and will be replaced by the final recording's.)",
          "final": "(Numbers are from the final recording{when}.)",
          "dummy": "(The numbers in this script are DUMMY values, so that it reads without placeholders. They are not measurements; the recording's numbers replace them.)"}
FENCE = re.compile(r"(```\n)(.*?)(\n```)", re.S)

def die(msg):
    print("ERROR:", msg, file=sys.stderr); sys.exit(1)

def dec(s, name):
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
    n = 0
    for x, y in zip(da, db):
        if x != y: break
        n += 1
    return n

def rel(a, b):
    return abs(a - b) / abs(a) if a != 0 else Decimal(0)

def whole(d): return str(int(d.to_integral_value()))
def rate(d): return f"{d.quantize(Decimal('0.001')):f}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--narrative", required=True)
    ap.add_argument("--values", help="the take's values file (not needed with --dummy)")
    ap.add_argument("--out", default=None, help="the nine filled blocks (default narration-final.txt, unless --review-out is given)")
    ap.add_argument("--dummy", action="store_true", help="use the built-in DUMMY values (labelled; not measurements)")
    ap.add_argument("--review-out", help="also build the placeholder-free review script, using make_review_script.py")
    ap.add_argument("--config", default=None, help="review config (default: docs/module1/video1/review-config.video1.json)")
    ap.add_argument("--stage", choices=["provisional", "final", "dummy"], default=None, help="labels the review script (dummy is implied by --dummy)")
    ap.add_argument("--date", default="", help='e.g. "Oct 28, 2026"; goes into the review script header')
    ap.add_argument("--out-narrative", help="a copy of the whole narrative with the spoken blocks filled")
    a = ap.parse_args()
    if a.dummy: a.stage = "dummy"
    if not a.dummy and not a.values: die("give --values, or --dummy")
    if a.review_out and not a.stage: die("give --stage provisional or --stage final with --review-out (or use --dummy)")
    out_path = a.out or (None if a.review_out else "narration-final.txt")

    if a.dummy: raw = dict(DUMMY)
    else: raw = json.loads(open(a.values).read(), parse_float=str, parse_int=str)  # keep full precision as text
    for k in KEYS:
        if k not in raw: die(f"the values file has no '{k}'")
    v = {k: dec(raw[k], k) for k in KEYS}

    text = open(a.narrative).read()
    blocks = re.findall(r"```\n(.*?)\n```", text, flags=re.S)
    if len(blocks) != 9: die(f"expected 9 fenced blocks in the narrative, found {len(blocks)}")

    digits = shared_digits(v["prom_value"], v["elastic_value"])
    r2 = rel(v["prom_value"], v["elastic_value"])
    r3 = rel(v["prom_frontend"], v["elastic_frontend"])
    fill = {
        "N_PROM": whole(v["n_prom"]), "N_ELASTIC": whole(v["n_elastic"]),
        "PROM_VALUE": rate(v["prom_value"]), "ELASTIC_VALUE": rate(v["elastic_value"]),
        "SECONDS_C": whole(v["seconds_c"]), "DIGITS_C": str(digits),
        "ROWS_PROM": whole(v["rows_prom"]), "ROWS_ELASTIC": whole(v["rows_elastic"]),
        "PROM_FRONTEND": rate(v["prom_frontend"]), "ELASTIC_FRONTEND": rate(v["elastic_frontend"]),
        "SECONDS_D": whole(v["seconds_d"]),
    }

    warnings = []
    if digits < 4:
        warnings.append(f"The rung 2 values share only {digits} leading digits: rewrite the 'agree to N digits' sentence, don't fill it.")
    if r2 > Decimal("0.001"):
        warnings.append(f"Rung 2 relative difference is {r2:.2e}: a new scrape sample probably landed between the two runs. Consider retaking the pair inside one scrape minute.")
    if r3 > Decimal("0.001"):
        warnings.append(f"Rung 3 frontend relative difference is {r3:.2e}: same warning.")
    if v["n_prom"] != v["n_elastic"]:
        warnings.append("The rung 1 series counts differ: check the label sets before saying 'they're the same series'.")
    if v["rows_prom"] != v["rows_elastic"]:
        warnings.append("The rung 3 row counts differ: check before filling.")
    for k in ("seconds_c", "seconds_d"):
        if v[k] > 40: warnings.append(f"{k} is {whole(v[k])} s: the two runs may have straddled a scrape (the safe window is about 50 s).")

    out, used = [], set()
    for name, b in zip(NAMES, blocks):
        for ph in re.findall(r"\{\{([A-Z_]+)\}\}", b):
            if ph not in fill: die(f"the narrative uses {{{{{ph}}}}}, which this script does not know")
            used.add(ph)
        filled = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: fill[m.group(1)], b)
        out.append(f"== {name} ==\n{filled}\n")
    banner = "DUMMY NARRATION (placeholders filled with DUMMY values; not measurements)" if a.dummy else "FINAL NARRATION (placeholders filled from the take values)"
    if out_path:
        open(out_path, "w").write(banner + "\n\n" + "\n".join(out))
        print(f"Wrote {out_path}: 9 blocks, {sum(len(b.split()) for b in out)} words (headings included).\n")
    else:
        print(f"9 blocks filled ({sum(len(b.split()) for b in out)} words, headings included).\n")
    if a.dummy: print("DUMMY VALUES in use: nothing below is a measurement.\n")
    print(f"{'placeholder':18s}value")
    for k in sorted(used): print(f"{k:18s}{fill[k]}")
    print(f"\nrung 2 relative difference: {r2:.3e}   rung 3 frontend relative difference: {r3:.3e}")
    print(f"unused values (fine if intentional): {sorted(set(fill) - used) or 'none'}")
    for w in warnings: print("WARNING:", w)
    if not warnings: print("No warnings.")

    filled_text = FENCE.sub(lambda m: m.group(1) + re.sub(r"\{\{([A-Z_]+)\}\}", lambda x: fill[x.group(1)], m.group(2)) + m.group(3), text)
    if a.out_narrative:
        open(a.out_narrative, "w", encoding="utf-8").write(filled_text); print(f"Wrote {a.out_narrative}")
    if a.review_out:
        here = os.path.dirname(os.path.abspath(__file__)); builder = os.path.join(here, "make_review_script.py")
        cfg_path = a.config or os.path.join(here, "..", "docs", "module1", "video1", "review-config.video1.json")
        if not os.path.exists(builder): die(f"cannot find {builder}")
        cfg = json.load(open(cfg_path, encoding="utf-8"))
        when = f" of {a.date}" if a.date else ""
        hdr = []
        for l in cfg.get("header", []):
            if l.startswith("Voice-over script"): l = f"Voice-over script, review draft ({a.stage})" + (f", {a.date}" if a.date else "")
            if "{{double braces}}" in l: continue
            hdr.append(l)
        cfg["header"] = hdr + [STATUS[a.stage].format(when=when)]
        tmp_dir = tempfile.mkdtemp()
        try:
            narr_tmp = os.path.join(tmp_dir, "narrative-filled.md"); cfg_tmp = os.path.join(tmp_dir, "config.json")
            open(narr_tmp, "w", encoding="utf-8").write(filled_text); json.dump(cfg, open(cfg_tmp, "w", encoding="utf-8"))
            r = subprocess.run([sys.executable, builder, "--narrative", narr_tmp, "--config", cfg_tmp, "--out", a.review_out], capture_output=True, text=True)
            sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
            if r.returncode != 0: die("make_review_script.py failed")
        finally:
            for f in os.listdir(tmp_dir): os.remove(os.path.join(tmp_dir, f))
            os.rmdir(tmp_dir)
        outtxt = open(a.review_out, encoding="utf-8").read()
        if "{{" in outtxt: die("the review script still holds a placeholder")
        print(f"Review script has no placeholders. {a.stage.capitalize()} stage.")

if __name__ == "__main__":
    main()
