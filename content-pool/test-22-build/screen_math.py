#!/usr/bin/env python3
"""Pre-screen a Math idea against the production bank BEFORE writing it out.

The lesson from Tests 18-21: a template repeat that changes the setting words
scores LOW on token Jaccard precisely because it changed the words, so the
number is triage, not a verdict. This tool therefore offers two modes:

    python3 screen_math.py sig  "candidate stem text ..."
        token-signature Jaccard against all 1,386 banked stems, top 8 printed.

    python3 screen_math.py grep "regex"
        every banked stem matching a regex — use this for the MATHEMATICS
        (e.g. "one real solution", "\\\\frac\\{k\\}\\{d\\^\\{2\\}\\}") rather
        than for the setting words.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = json.load(open(os.path.join(HERE, "..", "prod_math_stems.json")))

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


def cmd_sig(text):
    s0 = sig(text)
    rows = sorted(((jac(s0, sig(q["stem"])), q["label"], q["stem"]) for q in BANK),
                  reverse=True)
    for sc, lab, stem in rows[:8]:
        flat = re.sub(r"<[^>]+>", " ", stem)
        print(f"{sc:.2f}  {lab}\n      {flat[:300]}\n")


def cmd_grep(pattern):
    rx = re.compile(pattern, re.I)
    n = 0
    for q in BANK:
        flat = re.sub(r"<[^>]+>", " ", q["stem"])
        if rx.search(flat) or rx.search(q["stem"]):
            n += 1
            print(f"{q['label']}\n      {flat[:300]}\n")
    print(f"{n} of {len(BANK)} banked stems match {pattern!r}")


if __name__ == "__main__":
    {"sig": cmd_sig, "grep": cmd_grep}[sys.argv[1]](sys.argv[2])
