#!/usr/bin/env python3
"""Pre-screen a candidate Math stem against the production bank BEFORE writing it.

    python3 screen.py "candidate stem text ..."          # top matches by Jaccard
    python3 screen.py --grep "inversely with the square" # literal survey of the bank

Reads ../prod_math_stems.json (READ ONLY).  The point of this tool is the lesson
from Tests 18-21: a template repeat that changes the setting words scores LOW,
so the number is triage, not a verdict — the matched stems get printed in full
so they can actually be read.
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
        if "\\frac" in sp: math.append("mathfrac")
        if "\\sqrt" in sp: math.append("mathsqrt")
        if "\\pi" in sp: math.append("mathpi")
        if re.search(r"\^\{?2\}?", sp): math.append("mathsq")
        if re.search(r"\^\{?[a-z]\}?", sp): math.append("mathexpvar")
    tt = re.sub(r"\\[a-zA-Z]+", " ", tt)
    tt = re.sub(r"[-+]?\d[\d,.]*", "#", tt)
    return set((re.sub(r"[^a-z#]+", " ", tt.lower()).strip()
                + " " + " ".join(sorted(set(math)))).split())


def jac(a, b):
    return len(a & b) / max(1, len(a | b))


def main():
    prod = json.load(open(PROD))
    if sys.argv[1] == "--grep":
        pat = re.compile(sys.argv[2], re.I)
        n = 0
        for row in prod:
            plain = re.sub(r"<[^>]+>", " ", re.sub(r"<img[^>]*>", " ", row["stem"]))
            if pat.search(plain):
                n += 1
                print(f"--- {row['label']}\n{' '.join(plain.split())[:400]}\n")
        print(f"{n} hit(s)")
        return
    for cand in sys.argv[1:]:
        s0 = sig(cand)
        scored = sorted(((jac(s0, sig(r["stem"])), r) for r in prod),
                        key=lambda z: -z[0])[:5]
        print(f"### {' '.join(cand.split())[:120]}")
        for sc, r in scored:
            plain = " ".join(re.sub(r"<[^>]+>", " ",
                                    re.sub(r"<img[^>]*>", " ", r["stem"])).split())
            print(f"  {sc:.2f}  {r['label']}: {plain[:300]}")
        print()


if __name__ == "__main__":
    main()
