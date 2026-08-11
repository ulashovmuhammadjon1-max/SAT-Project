#!/usr/bin/env python3
"""Grep the READ-ONLY production Math bank by regex, printing tag-stripped stems.

Jaccard triage finds vocabulary neighbours; it does NOT find a template repeat
that reuses the mathematics under different setting words. This is the second
tool: search the bank for the MECHANISM ("vertex", "without replacement",
"true for all", "surface area") before writing a replacement, and read what
comes back.

    python3 bankgrep.py "surface area"
    python3 bankgrep.py "vertex" "x\\^\\{2\\}"      # every pattern must match
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.join(HERE, "..", "prod_math_stems.json")


def flat(s):
    s = re.sub(r"<img[^>]*>", " ", s)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def main():
    pats = [re.compile(p, re.I) for p in sys.argv[1:]]
    hits = 0
    for row in json.load(open(PROD)):
        txt = flat(row["stem"])
        if all(p.search(txt) for p in pats):
            hits += 1
            print(f"{row['label']:>18}  {txt[:300]}")
    print(f"-- {hits} hit(s)")


if __name__ == "__main__":
    main()
