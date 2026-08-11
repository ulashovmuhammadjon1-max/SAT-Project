#!/usr/bin/env python3
"""
Rebuild the two dedupe corpora that every content build depends on.

    python3 build_corpora.py

Writes `prod_math_stems.json` and `rw_authored_corpus.json` at this directory.

## Why this script exists

`prod_math_stems.json` is in `.gitignore` — production snapshots are kept out
of git deliberately. The consequence went unnoticed: the working copy carrying
1,188 Math stems lived only in one container's working tree, untracked and
unbackupable. Losing that container would have left the next build with no way
to check a new question against the bank, and duplicate questions are the one
defect this project has spent the most effort preventing.

Nothing here reads the production database. Every source below is tracked in
git, so a fresh clone can rebuild both corpora offline:

  * `test-8-build/prod_math_stems.json` — a tracked snapshot covering Tests 1-7,
    which is the only record of Tests 1 and 2, whose build directories predate
    the current pipeline.
  * `test-N-build/testN.json` — the assembled content for every later test.

That means the corpora are reproducible rather than precious. If it ever
disagrees with production, production wins — but it will not silently vanish.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

BASELINE = os.path.join(HERE, "test-8-build", "prod_math_stems.json")
MATH_MODULES = {"MATH_M1": "M1S", "MATH_M2E": "M2E", "MATH_M2H": "M2H"}
RW_MODULES = ("RW_M1", "RW_M2E", "RW_M2H")


def assembled_tests():
    """Every `test-N-build/testN.json`, in test-number order."""
    found = []
    for entry in os.listdir(HERE):
        m = re.fullmatch(r"test-(\d+)-build", entry)
        if not m:
            continue
        n = int(m.group(1))
        path = os.path.join(HERE, entry, f"test{n}.json")
        if os.path.exists(path):
            found.append((n, path))
    return sorted(found)


def main():
    math, seen_math = [], set()

    with open(BASELINE) as fh:
        for entry in json.load(fh):
            if entry["stem"] not in seen_math:
                math.append(entry)
                seen_math.add(entry["stem"])
    print(f"baseline (Tests 1-7): {len(math)} Math stems")

    rw, seen_rw = [], set()
    tests = assembled_tests()

    for n, path in tests:
        with open(path) as fh:
            test = json.load(fh)
        added_m = added_r = 0
        for key, tag in MATH_MODULES.items():
            for i, q in enumerate(test.get(key, []), 1):
                stem = q.get("stem", "")
                if stem and stem not in seen_math:
                    math.append({"label": f"Test {n} {tag} Q{i}", "stem": stem})
                    seen_math.add(stem)
                    added_m += 1
        for key in RW_MODULES:
            for q in test.get(key, []):
                passage = (q.get("passage") or "").strip()
                if passage and passage not in seen_rw:
                    rw.append({
                        "src": f"rw_test{n}",
                        "num": str(q.get("_ref", "")).split(":")[-1],
                        "skill": q.get("skill", ""),
                        "passage": passage,
                    })
                    seen_rw.add(passage)
                    added_r += 1
        print(f"  Test {n:>2}: +{added_m:>3} Math, +{added_r:>3} R&W")

    math_path = os.path.join(HERE, "prod_math_stems.json")
    rw_path = os.path.join(HERE, "rw_authored_corpus.json")

    # The R&W corpus IS tracked and holds passages from transcribed pools that
    # never went through an assembled testN.json, so merge rather than replace.
    if os.path.exists(rw_path):
        with open(rw_path) as fh:
            existing = json.load(fh)
        merged, seen = [], set()
        for entry in existing + rw:
            p = entry.get("passage", "").strip()
            if p and p not in seen:
                merged.append(entry)
                seen.add(p)
        rw = merged

    with open(math_path, "w") as fh:
        json.dump(math, fh, ensure_ascii=False, indent=1)
    with open(rw_path, "w") as fh:
        json.dump(rw, fh, ensure_ascii=False, indent=1)

    print(f"\nwrote {len(math)} Math stems -> {os.path.relpath(math_path, HERE)}")
    print(f"wrote {len(rw)} R&W passages -> {os.path.relpath(rw_path, HERE)}")
    print("\nThese cover every test with an assembled JSON in git. A test that is")
    print("live in production but has no tracked JSON will be missing — check the")
    print("count against production before trusting it for a new build.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
