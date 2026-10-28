#!/usr/bin/env python3
"""Verify and apply a delivery zip to the repo, with every check before anything is committed.

Usage (from the repo root):
  python3 scripts/apply_delivery.py ~/Downloads/video2-delivery-9.zip              # verify, apply, stage, report
  python3 scripts/apply_delivery.py ~/Downloads/video2-delivery-9.zip --check-only   # verify only; touches nothing

The zip holds the delivery's files at their repo paths, plus MANIFEST.json (read from the zip; it is never
copied into the repo). If you ever unzip a delivery by hand, use:  unzip -o <zip> -x MANIFEST.json

What it checks, in this order (the first failure stops the run, and nothing is applied before check 7 passes):
  1  the folder is the repo root; the branch has an upstream
  2  after `git fetch`: the branch is in sync with its upstream, and the working tree is clean
  3  the manifest is present (its sha256 is printed: compare it with the one line in the chat message)
  4  HEAD against the commit the delivery was built on (a different HEAD is a NOTE, not a failure, if 6 passes)
  5  the zip lists exactly the manifest's files (and MANIFEST.json), with the manifest's sizes; no odd paths
  6  the base: every file the delivery replaces has the base hash; every new file does not exist yet
  7  the payload: each file inside the zip has the manifest's sha256 (checked in memory, before anything is written)
  8  apply: the files are copied into the repo
  9  git status shows exactly the manifest's files (` M` for replaced, `??` for new)
  10 the files in the repo have the manifest's sha256
  11 stage only those files; `git diff --cached --numstat` equals the manifest, file by file and in total
  12 the safety scan: no file of the listed types holds the key fragment (only the path is ever printed)
It prints one compact report to paste into the chat, and the commit command. It NEVER commits or pushes.

MANIFEST.json:
  {"delivery": "9", "built_on_head": "<40 hex>", "commit_message": "...",
   "files": [{"path": "docs/x.md", "size": 123, "sha256": "...", "base_sha256": "..." or null,
              "added": 10, "deleted": 2}],
   "totals": {"files": 1, "insertions": 10, "deletions": 2},
   "safety": {"include": ["*.md", "*.py"], "exclude_dirs": ["opentelemetry-demo", ".git"]}}
"""
import argparse, fnmatch, hashlib, json, os, subprocess, sys, zipfile

NEEDLE = b"OFQtLV9" + b"K"   # the key fragment; built from two parts so that this file never contains it


def run(args, cwd):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Report:
    def __init__(self):
        self.lines = []; self.failed = None

    def add(self, n, ok, name, detail=""):
        self.lines.append(f"[{'PASS' if ok else 'FAIL'}] {n:>2}  {name}" + (f": {detail}" if detail else ""))
        if not ok and self.failed is None:
            self.failed = f"{n} {name}"

    def note(self, text):
        self.lines.append(f"[NOTE]     {text}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("zip"); ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args()
    root = os.getcwd()
    rep = Report(); applied = []; manifest = None

    def finish(extra=None):
        print("=" * 72)
        if manifest:
            print(f"delivery {manifest.get('delivery')}   manifest sha256 {mhash}")
        for l in rep.lines: print(l)
        print("=" * 72)
        if rep.failed:
            print(f"RESULT: FAIL at check {rep.failed}.")
            if applied:
                mod = [p for p, base in applied if base]; new = [p for p, base in applied if not base]
                print("Files were already applied. To undo them (nothing is committed):")
                print("  git reset -q -- " + " ".join(p for p, _ in applied))
                if mod: print("  git checkout -- " + " ".join(mod))
                for p in new: print(f"  rm {p}")
            else:
                print("Nothing was applied: the repo is unchanged.")
            sys.exit(1)
        if a.check_only:
            print("RESULT: CHECK-ONLY OK. Nothing was applied. Run again without --check-only to apply and stage.")
        else:
            print("RESULT: PASS. The files are applied and staged. NOTHING is committed or pushed.")
            print("Commit and push when you are ready:")
            msg = manifest["commit_message"].replace('"', '\\"')
            print(f'  git commit -m "{msg}" && git push')
        sys.exit(0)

    # 1 repo root and upstream
    rc, out, _ = run(["git", "rev-parse", "--show-toplevel"], root)
    top = out.strip()
    if rc != 0 or os.path.realpath(top) != os.path.realpath(root):
        rep.add(1, False, "repo root", f"run this from the repo root (git says {top or 'not a repo'})")
        mhash = "n/a"; finish()
    rc, out, _ = run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"], root)
    if rc != 0:
        rep.add(1, False, "repo root and upstream", "the branch has no upstream"); mhash = "n/a"; finish()
    upstream = out.strip()
    rep.add(1, True, "repo root and upstream", f"{upstream}")

    # 2 in sync and clean
    rc, _, err = run(["git", "fetch"], root)
    if rc != 0:
        rep.add(2, False, "git fetch", err.strip()[:120]); mhash = "n/a"; finish()
    _, sb, _ = run(["git", "status", "-sb"], root)
    first = sb.splitlines()[0] if sb else ""
    _, por, _ = run(["git", "status", "--porcelain", "-uall"], root)
    in_sync = "[" not in first
    clean = por.strip() == ""
    rep.add(2, in_sync and clean, "in sync with upstream and clean tree",
            first + ("" if clean else f"; {len(por.splitlines())} changed or untracked path(s): {por.splitlines()[0][:60]}"))
    if rep.failed: mhash = "n/a"; finish()

    # 3 manifest
    try:
        z = zipfile.ZipFile(a.zip)
    except Exception as e:
        rep.add(3, False, "zip", f"cannot open {a.zip}: {e}"); mhash = "n/a"; finish()
    names = z.namelist()
    if "MANIFEST.json" not in names:
        rep.add(3, False, "manifest", "MANIFEST.json is not in the zip"); mhash = "n/a"; finish()
    mbytes = z.read("MANIFEST.json"); mhash = sha256_bytes(mbytes)
    try:
        manifest = json.loads(mbytes)
        files = manifest["files"]; _ = manifest["totals"]; _ = manifest["commit_message"]
    except Exception as e:
        rep.add(3, False, "manifest", f"unreadable: {e}"); manifest = None; finish()
    rep.add(3, True, "manifest", f"{len(files)} file(s)")

    # 4 HEAD
    _, head, _ = run(["git", "rev-parse", "HEAD"], root); head = head.strip()
    built = manifest.get("built_on_head", "")
    head_same = head == built
    rep.add(4, True, "HEAD", f"{head[:7]}" + ("" if head_same else f" (the delivery was built on {built[:7]}; see the NOTE)"))
    if not head_same:
        _, lg, _ = run(["git", "log", "--oneline", "-3"], root)
        rep.note("HEAD differs from the one the delivery was built on; the base check (6) decides. Recent history: " + " / ".join(lg.strip().splitlines()))

    # 5 listing
    want = {f["path"]: f for f in files}
    bad_paths = [n for n in names if n != "MANIFEST.json" and (n.startswith("/") or ".." in n.split("/") or n.endswith("/"))]
    listed = {n for n in names if n != "MANIFEST.json"}
    sizes_ok = all(z.getinfo(p).file_size == want[p]["size"] for p in listed & set(want))
    ok5 = (not bad_paths) and listed == set(want) and sizes_ok
    rep.add(5, ok5, "zip listing", f"{len(listed)} file(s), sizes match" if ok5 else
            f"extra: {sorted(listed - set(want))[:3]} missing: {sorted(set(want) - listed)[:3]} odd: {bad_paths[:2]} sizes_ok={sizes_ok}")
    if rep.failed: finish()

    # 6 base
    problems = []
    for f in files:
        p = os.path.join(root, f["path"])
        if f.get("base_sha256"):
            if not os.path.exists(p): problems.append(f"{f['path']} is missing")
            elif sha256_file(p) != f["base_sha256"]: problems.append(f"{f['path']} differs from the base")
        elif os.path.exists(p): problems.append(f"{f['path']} already exists")
    rep.add(6, not problems, "base files", f"{sum(1 for f in files if f.get('base_sha256'))} replaced file(s) match, "
            f"{sum(1 for f in files if not f.get('base_sha256'))} new file(s) absent" if not problems else "; ".join(problems[:4]))
    if rep.failed: finish()

    # 7 payload
    bad = [f["path"] for f in files if sha256_bytes(z.read(f["path"])) != f["sha256"]]
    rep.add(7, not bad, "payload hashes (checked before applying)", "all match" if not bad else ", ".join(bad[:4]))
    if rep.failed: finish()
    if a.check_only: finish()

    # 8 apply
    for f in files:
        dest = os.path.join(root, f["path"])
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as fh: fh.write(z.read(f["path"]))
        applied.append((f["path"], bool(f.get("base_sha256"))))
    rep.add(8, True, "apply", f"{len(applied)} file(s) copied")

    # 9 status
    _, por, _ = run(["git", "status", "--porcelain", "-uall"], root)
    got = {l[3:]: l[:2] for l in por.splitlines()}
    exp = {f["path"]: (" M" if f.get("base_sha256") else "??") for f in files}
    rep.add(9, got == exp, "git status shows exactly the delivery's files",
            f"{len(got)} path(s)" if got == exp else f"expected {sorted(exp.items())[:3]} got {sorted(got.items())[:3]}")
    if rep.failed: finish()

    # 10 after hashes
    bad = [f["path"] for f in files if sha256_file(os.path.join(root, f["path"])) != f["sha256"]]
    rep.add(10, not bad, "hashes of the files in the repo", "all match" if not bad else ", ".join(bad[:4]))
    if rep.failed: finish()

    # 11 stage and numstat
    rc, _, err = run(["git", "add", "--"] + [f["path"] for f in files], root)
    _, ns, _ = run(["git", "diff", "--cached", "--numstat"], root)
    gotn = {}
    for l in ns.splitlines():
        ad, de, path = l.split("\t", 2); gotn[path] = (ad, de)
    expn = {f["path"]: (str(f["added"]), str(f["deleted"])) for f in files}
    ti = sum(int(x[0]) for x in gotn.values() if x[0].isdigit()); td = sum(int(x[1]) for x in gotn.values() if x[1].isdigit())
    tot_ok = (len(gotn), ti, td) == (manifest["totals"]["files"], manifest["totals"]["insertions"], manifest["totals"]["deletions"])
    rep.add(11, rc == 0 and gotn == expn and tot_ok, "staged diff equals the manifest",
            f"{len(gotn)} file(s), {ti} insertions(+), {td} deletions(-)" if gotn == expn and tot_ok else
            f"got {len(gotn)} files {ti}/{td}, expected {manifest['totals']}")
    if rep.failed: finish()

    # 12 safety scan (paths only; never the matching text)
    safety = manifest.get("safety", {"include": ["*.yaml", "*.md", "*.sh", "*.py", "*.json"], "exclude_dirs": ["opentelemetry-demo", ".git"]})
    hits = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in safety["exclude_dirs"]]
        for n in fn:
            if any(fnmatch.fnmatch(n, pat) for pat in safety["include"]):
                p = os.path.join(dp, n)
                try:
                    with open(p, "rb") as fh:
                        if NEEDLE in fh.read(): hits.append(os.path.relpath(p, root))
                except OSError:
                    pass
    rep.add(12, not hits, "safety scan", "no file holds the key fragment" if not hits else "FOUND in " + ", ".join(hits[:4]) + " (the text is not shown)")
    finish()


if __name__ == "__main__":
    main()
