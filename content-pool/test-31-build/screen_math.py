#!/usr/bin/env python3
"""
Pre-screen a planned Math question against every Math stem live in production
BEFORE it is written into math_test31.py.

The lesson from Tests 18-21, reproduced by four independent agents: a token
Jaccard threshold does not decide originality, reading does. 57 questions were
rewritten as genuine template repeats and all but three scored BELOW the 0.75
reject line, because a template repeat that changes the *setting words* while
keeping the mathematics scores low precisely because it changed the words.

So this tool is deliberately a READING aid, not a gate. It prints the nearest
matches with their stems so the match can be judged by eye, and it is run on an
idea before the idea is drafted, which avoids a second rewrite pass on every
item.

Usage:
    python3 screen_math.py grep "egg"  "grade"      # bank search by keyword
    python3 screen_math.py idea "<candidate stem text>"
    python3 screen_math.py file ideas.txt           # one candidate per line
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROD = os.path.join(HERE, "..", "prod_math_stems.json")

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)


def sig(text):
    tx = re.sub(r"<img[^>]*>", " ", text)
    tx = re.sub(r"<[^>]+>", " ", tx)
    tx = re.sub(r"&[a-z]+;", " ", tx)
    math = []
    for mm in SPAN.findall(tx):
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
    tx = re.sub(r"\\[a-zA-Z]+", " ", tx)
    tx = re.sub(r"[-+]?\d[\d,.]*", "#", tx)
    tokens = (re.sub(r"[^a-z#]+", " ", tx.lower()).strip() + " "
              + " ".join(sorted(set(math)))).split()
    return set(tokens)


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def plain(text, n=240):
    t = re.sub(r"<[^>]+>", " ", text)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:n]


def load():
    rows = json.load(open(PROD))
    for r in rows:
        r["_sig"] = sig(r["stem"])
    return rows


def do_grep(terms):
    rows = load()
    pats = [re.compile(r"(?<![A-Za-z])" + re.escape(t) + r"(?![A-Za-z])", re.I)
            for t in terms]
    n = 0
    for r in rows:
        p = plain(r["stem"], 100000)
        if all(pt.search(p) for pt in pats):
            n += 1
            print(f"  {r['label']:<22} {plain(r['stem'], 200)}")
    print(f"-- {n} of {len(rows)} stems match all of {terms}")


def do_idea(text, rows=None, label="candidate", show=6):
    rows = rows or load()
    s0 = sig(text)
    scored = sorted(((jaccard(s0, r["_sig"]), r) for r in rows),
                    key=lambda z: z[0], reverse=True)
    print(f"\n### {label}: {plain(text, 160)}")
    for sc, r in scored[:show]:
        mark = "  <-- READ" if sc >= 0.45 else ""
        print(f"  {sc:.2f}  {r['label']:<20}{mark}")
        if sc >= 0.45:
            print(f"        {plain(r['stem'], 300)}")
    return scored[0][0]


if __name__ == "__main__":
    what = sys.argv[1]
    if what == "grep":
        do_grep(sys.argv[2:])
    elif what == "idea":
        do_idea(sys.argv[2])
    elif what == "file":
        rows = load()
        worst = 0.0
        for line in open(sys.argv[2]):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            lab, _, body = line.partition("|")
            sc = do_idea(body or lab, rows, lab.strip() if body else "candidate")
            worst = max(worst, sc)
        print(f"\nhighest: {worst:.2f}")
