#!/usr/bin/env python3
"""Pre-screen candidate Math stems against the bank BEFORE they are written up.

Reads a JSON list of {"id": ..., "text": ...} on stdin or from a path and
prints, for each candidate, the closest banked stem under all three signals
used in this build: the verifier's token signature (vocabulary), the
mechanism skeleton (setting-blind), and shared numeric literals.

Screening a candidate first is cheaper than writing it, discovering the
collision, and rewriting: Tests 19-21 each discarded several ideas this way.
"""
import json
import re
import sys

from mechanism import load, plain, skeleton, numbers, jac, numshare

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


def main():
    rows = load()
    pre = [(r, sig(r["stem"]), skeleton(r["stem"]), numbers(r["stem"])) for r in rows]
    cands = json.load(open(sys.argv[1]))
    for c in cands:
        s0, k0, n0 = sig(c["text"]), skeleton(c["text"]), numbers(c["text"])
        vs = sorted(((jac(s0, s), r) for r, s, k, n in pre), key=lambda z: -z[0])[:3]
        ks = sorted(((jac(k0, k), r) for r, s, k, n in pre), key=lambda z: -z[0])[:3]
        ns = sorted(((numshare(n0, n), r) for r, s, k, n in pre), key=lambda z: -z[0])[:2]
        print(f"### {c['id']}  vocab {vs[0][0]:.2f}  mech {ks[0][0]:.2f}  nums {ns[0][0]}")
        for sc, r in vs:
            print(f"   V {sc:.2f} {r['label']}: {plain(r['stem'])[:150]}")
        for sc, r in ks:
            print(f"   M {sc:.2f} {r['label']}: {plain(r['stem'])[:150]}")
        for sc, r in ns:
            if sc >= 3:
                print(f"   N {sc}    {r['label']}: {plain(r['stem'])[:150]}")
        print()


if __name__ == "__main__":
    main()
