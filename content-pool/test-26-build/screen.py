#!/usr/bin/env python3
"""Pre-screening helper for Test 26 — used BEFORE a question is written out.

Two entry points:

    python3 screen.py math "candidate stem text ..."
    python3 screen.py rw   "candidate passage text ..."
    python3 screen.py kw   longwall "pit prop*" ...

The math signature is identical to the one verify_math_test26.py uses, so a
score printed here is the score the verifier will print. The point of running
it first is that a replacement written blind is more likely than not to collide
once the bank passes ~1,400 stems; screening the IDEA costs one command and
saves a whole rewrite pass.

Keyword matching is on WORD BOUNDARIES with an explicit closing boundary — a
raw substring match is worse than no check (\\bfen matched "fence", <u matched
<ul). A trailing * means whole-word-prefix.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MATH_CORPUS = os.path.join(HERE, "..", "prod_math_stems.json")
RW_CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def math_sig(text):
    tt = re.sub(r"<img[^>]*>", " ", text)
    tt = re.sub(r"<[^>]+>", " ", tt)
    tt = re.sub(r"&[a-z]+;", " ", tt)
    math = []
    for mo in SPAN.findall(tt):
        sp = mo[0] or mo[1]
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
    joined = re.sub(r"[^a-z#]+", " ", tt.lower()).strip() + " " + " ".join(sorted(set(math)))
    return set(joined.split())


STOP = set("""a an the and or but if of to in on at by for with from as is are was were be been
being it its this this that these those which who whom whose what when where how why not no than
then so such can could will would may might must shall should do does did done have has had
having one two three four five six seven eight nine ten first second more most less least many
much few some any all each every other another same own very just also only into out up down over
under about after before during while because since until through between against among within
without their they them there here he she his her him we us our you your i me my too s t""".split())
WORD = re.compile(r"[a-z]+")


def rw_toks(s):
    s = re.sub(r"<[^>]+>", " ", s or "").lower()
    s = re.sub(r"&[a-z]+;", " ", s)
    return [w for w in WORD.findall(s) if w not in STOP and len(w) > 2]


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def kw_regex(kw):
    if kw.endswith("*"):
        return re.compile(r"(?<![a-z])" + re.escape(kw[:-1]) + r"[a-z]*(?![a-z])")
    parts = [re.escape(p) for p in kw.split()]
    return re.compile(r"(?<![a-z])" + r"\s+".join(parts) + r"(?![a-z])")


def main():
    mode = sys.argv[1]
    if mode == "math":
        rows = json.load(open(MATH_CORPUS))
        sigs = [(r["label"], math_sig(r["stem"]), r["stem"]) for r in rows]
        for text in sys.argv[2:]:
            s0 = math_sig(text)
            scored = sorted(((jaccard(s0, s), lab, stem) for lab, s, stem in sigs), reverse=True)
            print(f"\n--- {text[:70]!r}")
            for sc, lab, stem in scored[:5]:
                flag = "  <== READ" if sc >= 0.45 else ""
                print(f"  {sc:.2f}  {lab}{flag}")
                if sc >= 0.45:
                    print("        " + re.sub(r"<[^>]+>", " ", stem)[:260])
    elif mode == "rw":
        rows = json.load(open(RW_CORPUS))
        sigs = [(f"{r.get('src')}:{r.get('num')}",
                 set(rw_toks((r.get("passage") or "") + " " + (r.get("stem") or ""))),
                 r.get("passage") or "") for r in rows]
        for text in sys.argv[2:]:
            s0 = set(rw_toks(text))
            scored = sorted(((jaccard(s0, s), lab, p) for lab, s, p in sigs), reverse=True)
            print(f"\n--- {text[:70]!r}")
            for sc, lab, p in scored[:5]:
                flag = "  <== READ" if sc >= 0.35 else ""
                print(f"  {sc:.2f}  {lab}{flag}")
                if sc >= 0.35:
                    print("        " + re.sub(r"<[^>]+>", " ", p)[:260])
    elif mode == "kw":
        rows = json.load(open(RW_CORPUS))
        blobs = [(f"{r.get('src')}:{r.get('num')}",
                  re.sub(r"<[^>]+>", " ", (r.get("passage") or "") + " " + (r.get("stem") or "")).lower())
                 for r in rows]
        mrows = json.load(open(MATH_CORPUS))
        mblobs = [(r["label"], re.sub(r"<[^>]+>", " ", r["stem"]).lower()) for r in mrows]
        for kw in sys.argv[2:]:
            rx = kw_regex(kw)
            hits = [lab for lab, b in blobs if rx.search(b)]
            mhits = [lab for lab, b in mblobs if rx.search(b)]
            print(f"{kw:<34} rw:{len(hits):>3} {hits[:6]}   math:{len(mhits):>3} {mhits[:4]}")
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
