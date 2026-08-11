#!/usr/bin/env python3
"""Query helper over the production Math stem bank.

Two modes, both used *before* a question is written rather than after:

    python3 bank.py grep <regex>          # print every banked stem matching
    python3 bank.py near "<candidate>"    # top Jaccard matches, full text

Reads ../prod_math_stems.json (READ ONLY — the shared corpus at the
content-pool root, never modified from here).
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "prod_math_stems.json")

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


def plain(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text)).strip()


def main():
    rows = json.load(open(BANK))
    mode = sys.argv[1]
    arg = sys.argv[2]
    if mode == "grep":
        pat = re.compile(arg, re.I)
        n = 0
        for r in rows:
            p = plain(r["stem"])
            if pat.search(p):
                n += 1
                print(f"--- {r['label']}\n{p[:420]}\n")
        print(f"{n} of {len(rows)} banked stems match")
    else:
        s0 = sig(arg)
        scored = sorted(((jac(s0, sig(r["stem"])), r) for r in rows),
                        key=lambda z: -z[0])[:int(sys.argv[3]) if len(sys.argv) > 3 else 5]
        for sc, r in scored:
            print(f"--- {sc:.2f}  {r['label']}\n{plain(r['stem'])[:420]}\n")


if __name__ == "__main__":
    main()
