#!/usr/bin/env python3
"""
Pre-screen a candidate idea against the shared corpora BEFORE it is written out.

The Test 19-21 group established the rule this exists to serve: a similarity
threshold decides what to READ, not what to accept. 48 Math questions across
those three tests were rewritten as genuine template repeats and all but two
scored BELOW the 0.75 reject line, because a repeat that changes the setting
words while keeping the mathematics scores low precisely because it changed the
words.  So the only defence is to look at the nearest banked items yourself,
and to look BEFORE drafting rather than after.

Usage:
    python3 screen.py math "a candidate stem or a bag of keywords"
    python3 screen.py rw   "a candidate passage or a bag of keywords"
    python3 screen.py kw   keyword [keyword ...]      # substring hunt, both corpora

Corpora are the ROOT copies (read-only):
    ../prod_math_stems.json     1,386 live production Math stems
    ../rw_authored_corpus.json  1,295 authored R&W passages
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MATH = os.path.join(ROOT, "prod_math_stems.json")
RW = os.path.join(ROOT, "rw_authored_corpus.json")

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def sig(text):
    """Token signature: markup and entities stripped, LaTeX structure reduced to
    a handful of marker tokens, every number collapsed to '#'."""
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


def load(kind):
    if kind == "math":
        return [(r["label"], r["stem"]) for r in json.load(open(MATH))]
    rows = json.load(open(RW))
    return [(f"{r.get('src')}:{r.get('num')} [{r.get('skill')}]", r.get("passage") or "")
            for r in rows]


def top(kind, text, n=8):
    s0 = sig(text)
    scored = [(jaccard(s0, sig(t)), lab, t) for lab, t in load(kind)]
    scored.sort(reverse=True, key=lambda z: z[0])
    return scored[:n]


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(2)
    mode = sys.argv[1]
    if mode == "kw":
        words = [w.lower() for w in sys.argv[2:]]
        for kind in ("math", "rw"):
            print(f"--- {kind}")
            for lab, t in load(kind):
                low = re.sub(r"<[^>]+>", " ", t).lower()
                hit = [w for w in words if w in low]
                if hit:
                    flat = re.sub(r"\s+", " ", low)[:150]
                    print(f"  {lab}  {hit}  {flat}")
        return
    text = " ".join(sys.argv[2:])
    for sc, lab, t in top(mode, text):
        body = re.sub(r"<[^>]+>", " ", t)
        body = re.sub(r"\s+", " ", body)[:230]
        print(f"{sc:.2f}  {lab}\n      {body}\n")


if __name__ == "__main__":
    main()
