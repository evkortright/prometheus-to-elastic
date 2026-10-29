#!/usr/bin/env python3
"""Build a delivery zip with a MANIFEST.json that scripts/apply_delivery.py can verify.

This is the chat-side tool: it runs where the delivery is prepared (a chat's sandbox), not on the author's laptop.
The baseline is the repo as it was pushed: a plain folder is enough (for example the unzipped repo archive, with
the deliveries already applied on top of it). No git repo is needed.

Usage:
  python3 scripts/build_delivery.py --baseline DIR --source DIR --paths docs/a.md scripts/b.py \\
      --delivery 9 --message "commit message" --built-on <40-hex HEAD> --out ~/video2-delivery-9.zip

  --baseline  the pushed state (files the delivery replaces are read from here; paths absent here are new files)
  --source    the folder holding the delivery's finished files, at their repo paths
  --paths     the repo paths of the files in the delivery (every one must exist under --source)
  --built-on  the commit the baseline corresponds to. For a repo archive made with `git archive`, it is the
              archive's comment: `unzip -z repo.zip`. If other commits have been pushed since, the author's
              apply_delivery.py reports the difference as a NOTE and lets the base hashes decide.

It prints the manifest's sha256 (give that one line in the chat message; the author compares it with the line the
apply script prints) and the expected totals. The manifest holds, for every file: its size, its sha256, the sha256
of the file it replaces (null for a new file) and the added and deleted line counts, from `git diff --no-index`.
"""
import argparse, hashlib, json, os, subprocess, sys, zipfile


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def numstat(old, new):
    """(added, deleted) between two files; old may be None for a new file."""
    r = subprocess.run(["git", "diff", "--no-index", "--numstat", "--", old or os.devnull, new],
                       capture_output=True, text=True)
    if r.returncode not in (0, 1) or not r.stdout.strip():
        if r.returncode == 0:
            return (0, 0)
        sys.exit(f"git diff failed for {new}: {r.stderr.strip()}")
    ad, de, _ = r.stdout.splitlines()[0].split("\t", 2)
    if not (ad.isdigit() and de.isdigit()):
        sys.exit(f"{new} looks like a binary file; deliveries are for text files")
    return int(ad), int(de)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", required=True); ap.add_argument("--source", required=True)
    ap.add_argument("--paths", nargs="+", required=True); ap.add_argument("--delivery", required=True)
    ap.add_argument("--message", required=True); ap.add_argument("--built-on", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if len(a.built_on) != 40 or any(c not in "0123456789abcdef" for c in a.built_on):
        sys.exit("--built-on must be the full 40-character commit hash")
    files = []
    for p in a.paths:
        if p.startswith("/") or ".." in p.split("/"): sys.exit(f"bad path: {p}")
        src = os.path.join(a.source, p); base = os.path.join(a.baseline, p)
        if not os.path.isfile(src): sys.exit(f"missing in --source: {p}")
        if os.path.exists(base) and sha(base) == sha(src):
            sys.exit(f"{p} is identical to the baseline: remove it from the delivery")
        added, deleted = numstat(base if os.path.exists(base) else None, src)
        files.append({"path": p, "size": os.path.getsize(src), "sha256": sha(src),
                      "base_sha256": sha(base) if os.path.exists(base) else None, "added": added, "deleted": deleted})
    man = {"delivery": a.delivery, "built_on_head": a.built_on, "commit_message": a.message, "files": files,
           "totals": {"files": len(files), "insertions": sum(f["added"] for f in files), "deletions": sum(f["deleted"] for f in files)},
           "safety": {"include": ["*.yaml", "*.md", "*.sh", "*.py", "*.json"], "exclude_dirs": ["opentelemetry-demo", ".git"]}}
    mbytes = json.dumps(man, indent=2).encode()
    if os.path.exists(a.out): os.remove(a.out)
    with zipfile.ZipFile(a.out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in a.paths: z.write(os.path.join(a.source, p), p)
        z.writestr("MANIFEST.json", mbytes)
    print(json.dumps({"zip": a.out, "manifest_sha256": hashlib.sha256(mbytes).hexdigest(), "totals": man["totals"],
                      "files": [(f["path"], "new" if not f["base_sha256"] else "replaced", f["added"], f["deleted"]) for f in files]}, indent=1))


if __name__ == "__main__":
    main()
