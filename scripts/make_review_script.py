#!/usr/bin/env python3
"""Build the plain-text voice-over REVIEW SCRIPT for a Module 1 video from its narrative.

Usage:
  python3 make_review_script.py --narrative docs/module1-video1-narrative.md \
      --config review-config.video1.json --out module1-video1-voiceover-script.txt

The narrative's spoken text is the fenced blocks, grouped under "## Heading" sections.
The config says which headings go on which slide, and holds the title-slide narration.
Nothing in the repo is changed. Every block is copied character for character.

Config (JSON):
  header:           list of lines printed at the top
  title_narration:  the spoken text for the title slide ("Welcome to ... In this lesson, you will ...")
  slides:           list of {"name": "OPENING", "headings": ["Hook"], "labels": [optional list, one per block]}
  include_optional: true to include sections whose heading starts with "OPTIONAL" (default false)
"""
import argparse, json, re, sys

BAR = "=" * 72
ROLE = re.compile(r"^(Prometheus|Elastic|Question|Answer)\b[^:]{0,15}:")

def die(m): print("ERROR:", m, file=sys.stderr); sys.exit(1)

def parse(text):
    """-> ordered list of (heading, [(note, block), ...]) for each '## ' section."""
    sections, cur, note = [], None, None
    lines = text.split("\n"); i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("## "):
            cur = (l[3:].strip(), []); sections.append(cur); note = None
        elif cur is not None and l.startswith("*") and l.endswith("*") and not l.startswith("**"):
            note = l.strip("*").strip()
        elif cur is not None and l.strip() == "```":
            j = i + 1; buf = []
            while j < len(lines) and lines[j].strip() != "```": buf.append(lines[j]); j += 1
            cur[1].append((note, "\n".join(buf))); note = None; i = j
        i += 1
    return sections

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--narrative", required=True); ap.add_argument("--config", required=True)
    ap.add_argument("--out", default="voiceover-script.txt")
    a = ap.parse_args()
    cfg = json.load(open(a.config)); text = open(a.narrative).read()
    sections = {h: b for h, b in parse(text)}
    include_opt = bool(cfg.get("include_optional", False))
    out = list(cfg.get("header", [])) + [""]
    def sec(n, name, body): out.extend([BAR, f"SLIDE {n}: {name}", BAR, "", body.strip(), ""])
    n = 1; sec(n, "TITLE", cfg["title_narration"]); used = set(); counts = {"TITLE": len(cfg["title_narration"].split())}
    for s in cfg["slides"]:
        pieces = []
        for h in s["headings"]:
            if h not in sections: die(f"no section '## {h}' in the narrative. Sections found: {list(sections)}")
            if h.upper().startswith("OPTIONAL") and not include_opt: continue
            used.add(h)
            for note, block in sections[h]:
                role = ROLE.match(note).group(1).lower() if note and ROLE.match(note) else None
                pieces.append((h, role, block))
        if not pieces: die(f"slide {s['name']} has no blocks")
        labels = s.get("labels")
        if labels is not None and len(labels) != len(pieces):
            die(f"slide {s['name']}: {len(labels)} labels for {len(pieces)} blocks")
        if len(pieces) == 1 and labels is None: body = pieces[0][2]
        else:
            parts = []
            for k, (h, role, block) in enumerate(pieces):
                lab = labels[k] if labels else f"[{h}{' (' + role + ')' if role else ''}]"
                parts.append(f"{lab}\n{block}")
            body = "\n\n".join(parts)
        n += 1; sec(n, s["name"], body); counts[s["name"]] = sum(len(p[2].split()) for p in pieces)
    result = "\n".join(out).rstrip("\n") + "\n"
    for h, blocks in sections.items():
        for _, b in blocks:
            if h in used and b not in result: die(f"a block under '{h}' was not copied verbatim")
    unmapped = [h for h, b in sections.items() if b and h not in used and not h.upper().startswith("OPTIONAL")
                and h not in ("Placeholders", "Claims to confirm", "Listening notes (fill in)", "Still open", "How to read this")]
    open(a.out, "w").write(result)
    print(f"Wrote {a.out}: {sum(counts.values())} spoken words ({', '.join(f'{k} {v}' for k, v in counts.items())}).")
    skipped = [h for h in sections if h.upper().startswith("OPTIONAL") and not include_opt]
    if skipped: print("Optional sections left out (set include_optional to add them):", skipped)
    if unmapped: print("WARNING: sections with spoken blocks that are on no slide:", unmapped)
    ph = sorted(set(re.findall(r"\{\{([A-Z_]+)\}\}", result)))
    print(f"Placeholders left in the script ({len(ph)}): {ph}")

if __name__ == "__main__":
    main()
