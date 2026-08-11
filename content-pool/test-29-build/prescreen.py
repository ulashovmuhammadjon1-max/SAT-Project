#!/usr/bin/env python3
"""
Pre-screen a Math question idea against the production bank BEFORE writing it.

The lesson every previous build re-learns: a token-signature Jaccard score is a
triage device, not a verdict. A template repeat that changes the setting words
while keeping the mathematics scores LOW precisely because it changed the words.
So this prints the nearest banked stems in full, and the judgement is made by
reading them.

Usage:
    python3 prescreen.py ideas.txt        # one candidate per line (blank-separated ok)
    echo "..." | python3 prescreen.py -
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


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def main():
    prod = json.load(open(PROD))
    others = [(p["label"], p["stem"], sig(p["stem"])) for p in prod]

    src = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1]).read()
    cands = [ln.strip() for ln in src.split("\n") if ln.strip() and not ln.startswith("#")]

    for cand in cands:
        s0 = sig(cand)
        scored = sorted(((jaccard(s0, s), lab, stem) for lab, stem, s in others),
                        reverse=True, key=lambda z: z[0])[:4]
        print("=" * 78)
        print("CAND:", cand[:160])
        for sc, lab, stem in scored:
            mark = "  <<< READ" if sc >= 0.45 else ""
            print(f"  {sc:.2f} {lab}{mark}")
            print(f"       {re.sub(r'<[^>]+>', ' ', stem)[:230]}")
    print("=" * 78)


if __name__ == "__main__":
    main()
