#!/usr/bin/env python3
"""Pre-screen a candidate idea against the banked corpora BEFORE drafting it.

Two modes:

    python3 screen.py math  "keyword keyword ..."   # grep prod_math_stems.json
    python3 screen.py rw    "keyword keyword ..."   # grep rw_authored_corpus.json

Both corpora live at the content-pool ROOT and are READ ONLY.

The point of this tool is the lesson from Tests 18-21: a Jaccard score decides
what to READ, not what to accept, and past ~1,386 banked Math questions a first
draft is more likely than not to repeat a template. Screening a candidate by
its mathematical skeleton (the keywords, not the setting) before writing it
avoids a second rewrite pass on every item.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")


def load(kind):
    if kind == "math":
        return [(r["label"], r["stem"]) for r in
                json.load(open(os.path.join(ROOT, "prod_math_stems.json")))]
    rows = json.load(open(os.path.join(ROOT, "rw_authored_corpus.json")))
    return [(f"{r.get('src')}/{r.get('num')}", r.get("passage") or "") for r in rows]


def main():
    kind = sys.argv[1]
    words = [w.lower() for w in sys.argv[2].split()]
    hits = []
    for label, text in load(kind):
        flat = re.sub(r"<[^>]+>", " ", text).lower()
        n = sum(1 for w in words if re.search(r"(?<![a-z])" + re.escape(w), flat))
        if n:
            hits.append((n, label, re.sub(r"\s+", " ", flat)[:220]))
    hits.sort(reverse=True)
    print(f"{len(hits)} hit(s) for {words}")
    for n, label, snip in hits[:14]:
        print(f"  [{n}] {label}: {snip}")


if __name__ == "__main__":
    main()
