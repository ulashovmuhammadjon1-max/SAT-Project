#!/usr/bin/env python3
"""Pre-screen a candidate Math stem against the production bank BEFORE writing it out.

The Test 19-21 finding: a similarity threshold decides what to READ, not what to
accept. 48 Math questions across those three tests were genuine template repeats
and all but two scored below the 0.75 reject line. So this prints the top matches
for a draft so they can be read, rather than passing or failing anything.

Usage:
    python3 screen_math.py            # screen every stem in math_test29.py
    echo "<a draft stem>" | python3 screen_math.py -   # screen stdin, one per line
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.join(HERE, "..", "prod_math_stems.json")

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def sig(text):
    tt = re.sub(r"<img[^>]*>", " ", text)
    tt = re.sub(r"<[^>]+>", " ", tt)
    tt = re.sub(r"&[a-z]+;", " ", tt)
    math = []
    for mm in SPAN.findall(tt):
        sp = mm[0] or mm[1]
        if "\\frac" in sp:
            math.append("mathfrac")
        if "\\sqrt" in sp:
            math.append("mathsqrt")
        if "\\pi" in sp:
            math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp):
            math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp):
            math.append("mathexpvar")
    tt = re.sub(r"\\[a-zA-Z]+", " ", tt)
    tt = re.sub(r"[-+]?\d[\d,.]*", "#", tt)
    return set((re.sub(r"[^a-z#]+", " ", tt.lower()).strip()
                + " " + " ".join(sorted(set(math)))).split())


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def main():
    prod = json.load(open(PROD))
    others = [(p["label"], sig(p["stem"]), p["stem"]) for p in prod]

    if len(sys.argv) > 1 and sys.argv[1] == "-":
        drafts = [("stdin-%d" % i, ln.strip())
                  for i, ln in enumerate(sys.stdin.read().split("\n")) if ln.strip()]
    else:
        sys.path.insert(0, HERE)
        from math_test29 import ALL
        drafts = [(q["n"], q["stem"]) for q in ALL]

    show = float(os.environ.get("SHOW", "0.40"))
    for tag, stem in drafts:
        s0 = sig(stem)
        scored = sorted(((jaccard(s0, o), lab, full) for lab, o, full in others), reverse=True)
        top = scored[0]
        print(f"\n### {tag}   top={top[0]:.2f} vs {top[1]}")
        for sc, lab, full in scored[:4]:
            if sc < show:
                break
            print(f"   {sc:.2f}  {lab}")
            print("        " + re.sub(r"<[^>]+>", " ", full)[:260].replace("\n", " "))


if __name__ == "__main__":
    main()
