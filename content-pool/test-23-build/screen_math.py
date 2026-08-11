#!/usr/bin/env python3
"""Pre-screen a candidate Math stem against the production bank BEFORE writing
it into math_test23.py.

The lesson from Tests 18-21: past ~1,386 banked Math stems a first draft is
more likely than not to repeat a template, and the Jaccard score is triage,
not a verdict — so this prints the nearest three banked stems in full and the
author reads them.

Usage:  python3 screen_math.py            # screens CANDIDATES below
        python3 screen_math.py "some stem text"
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def sig(text):
    tt = re.sub(r"<[^>]+>", " ", text)
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


PROD = json.load(open(os.path.join(HERE, "..", "prod_math_stems.json")))
BANK = [(q["label"], re.sub(r"<[^>]+>", " ", q["stem"]), sig(re.sub(r"<img[^>]*>", " ", q["stem"])))
        for q in PROD]


def screen(tag, stem, show=3):
    s0 = sig(stem)
    scored = sorted(((jac(s0, s), lab, txt) for lab, txt, s in BANK), reverse=True)
    print(f"\n### {tag}   top {show}")
    for sc, lab, txt in scored[:show]:
        print(f"  {sc:.2f}  {lab}: {txt[:230]}")
    return scored[0][0]


CANDIDATES = {}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        screen("cli", sys.argv[1], 5)
    else:
        for tag, stem in CANDIDATES.items():
            screen(tag, stem)
