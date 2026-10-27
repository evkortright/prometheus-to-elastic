#!/usr/bin/env python3
"""Fill the {{placeholders}} in Module 1, Video 1's narration from the take's numbers.

Usage:
  python3 fill_placeholders.py --narrative docs/module1-video1-narrative.md \
      --values take-values.json --out narration-final.txt

Reads the nine spoken blocks (the nine fenced blocks) from the narrative, computes the derived
numbers (the digits the two rung 2 values share, the relative differences), formats every
number for speech, replaces each {{PLACEHOLDER}}, and writes the nine filled blocks.
It changes no repo file. It stops with an error if a placeholder has no value.
"""
import argparse, json, re, sys
from decimal import Decimal, InvalidOperation

NAMES = ["Opening (slide)", "Setup (Clip A)", "Rung 1, Prometheus (Clip B1)", "Rung 1, Elastic (Clip B2)",
         "Rung 2, Prometheus (Clip C1)", "Rung 2, Elastic (Clip C2)", "Rung 3, Prometheus (Clip D1)",
         "Rung 3, Elastic (Clip D2)", "Recap (slide)"]
KEYS = ["n_prom", "n_elastic", "prom_value", "elastic_value", "seconds_c",
        "rows_prom", "rows_elastic", "prom_frontend", "elastic_frontend", "seconds_d"]

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
    ap.add_argument("--values", required=True)
    ap.add_argument("--out", default="narration-final.txt")
    a = ap.parse_args()

    raw = json.loads(open(a.values).read(), parse_float=str, parse_int=str)  # keep full precision as text
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
    open(a.out, "w").write("FINAL NARRATION (placeholders filled from the take values)\n\n" + "\n".join(out))

    print(f"Wrote {a.out}: 9 blocks, {sum(len(b.split()) for b in out)} words (headings included).\n")
    print(f"{'placeholder':18s}value")
    for k in sorted(used): print(f"{k:18s}{fill[k]}")
    print(f"\nrung 2 relative difference: {r2:.3e}   rung 3 frontend relative difference: {r3:.3e}")
    print(f"unused values (fine if intentional): {sorted(set(fill) - used) or 'none'}")
    for w in warnings: print("WARNING:", w)
    if not warnings: print("No warnings.")

if __name__ == "__main__":
    main()
