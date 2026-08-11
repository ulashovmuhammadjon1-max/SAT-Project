#!/usr/bin/env python3
"""
Mechanism search over the 1,386 banked production Math stems.

WHY THIS EXISTS, and why the Jaccard screen in verify_math_test27.py is not
enough on its own:

Test 25 replaced 34 of its 66 Math questions, and **19 of those were never
flagged by the similarity screen at all** — six scored below 0.30. The reason
is structural. Token-signature Jaccard measures *vocabulary* overlap. A
template repeat that keeps the mathematics and changes the setting words scores
LOW precisely because it changed the words, and a narrow thematic territory
guarantees the setting words are changed. So a score-only screen is blind to
exactly the failure it is supposed to catch.

This module searches by MECHANISM instead — the thing a template repeat
actually preserves. Four independent signals, none of which looks at the
setting nouns at all:

  numbers   The multiset of numerals in the stem, tags stripped first (a
            <table>'s inline style carries digits like 1 and 0.35 that would
            otherwise dominate every comparison). Shared *distinctive*
            numerals are weighted by inverse document frequency, so sharing
            "1,150 and 55.2" counts and sharing "2 and 3" does not. This is
            the signal that catches Test 20's `2x^2-12x+23` case, where the
            coefficients survived verbatim under a new setting.

  latex     Every math span normalised to a skeleton: whitespace gone, every
            variable letter collapsed to `v`, digits kept. `\\(2x^{2}-5\\)`
            and `\\(2y^{2}-5\\)` share a skeleton; so do two rearrangements of
            one identity. A second, weaker skeleton also collapses digits to
            `#`, which catches the same algebraic SHAPE under new numbers.

  phrase    A hand-written mechanism description per question — the sentence
            you would use to tell another author what the question *does*,
            with no setting nouns in it: "capacity minus tare over unit mass",
            "dilute a percentage with pure solvent", "mean of n then add one".
            Matched as an ordered bag of stemmed content words, so word order
            and inflection do not matter.

  regex     Free-form, for hunting a specific construction by hand.

USAGE
    python3 mechanism.py sweep            # all 66, every automatic signal
    python3 mechanism.py phrase "mean of n items then one more is added"
    python3 mechanism.py find "ratio.{0,40}after.{0,40}more"     # regex
    python3 mechanism.py nums 45 4.2 6 4.5                       # numeral hunt
    python3 mechanism.py show "Test 7 M2H Q21"                   # print a stem

The corpus is READ ONLY. Nothing in this file writes to it.
"""
import json
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MATH = os.path.join(ROOT, "prod_math_stems.json")

SPAN = re.compile(r"\\\((.*?)\\\)|\\\[(.*?)\\\]", re.S)

# Ordinary-English words carry no mechanism, and a stop list is cheaper than a
# stemmer here. "of", "the", "a" would otherwise dominate every phrase match.
STOP = set("""a an and are as at be been by can does each first for from
given how in into is it its many number of on one or per that the then there
this to total two value values what when where which with within after before
""".split())


def strip_tags(text):
    """Tags out FIRST. A table's inline style holds 1, 0.35, 0.6, 0.75 and a
    colour code; leaving them in makes every table question look alike."""
    tt = re.sub(r"<img[^>]*>", " ", text)
    tt = re.sub(r"<[^>]+>", " ", tt)
    return re.sub(r"&[a-z]+;", " ", tt)


def numerals(text):
    """Numbers as written, thousands separators removed, as a set of strings so
    12 and 12.0 stay distinct — a template repeat reuses the literal."""
    tt = strip_tags(text)
    out = set()
    for raw in re.findall(r"\d[\d,]*(?:\.\d+)?", tt):
        val = raw.replace(",", "")
        val = val.rstrip("0").rstrip(".") if "." in val else val
        out.add(val)
    return out


def skeletons(text, blind_digits=False):
    """Normalised math spans. Variables collapse to v; optionally digits to #."""
    out = set()
    for mm in SPAN.findall(text):
        sp = mm[0] or mm[1]
        sp = re.sub(r"\s+", "", sp)
        sp = re.sub(r"\\(left|right|cdot|,)", "", sp)
        sp = re.sub(r"(?<![\\a-zA-Z])[a-zA-Z](?![a-zA-Z])", "v", sp)
        if blind_digits:
            sp = re.sub(r"\d+", "#", sp)
        if len(sp) >= 5:
            out.add(sp)
    return out


def words(text):
    tt = strip_tags(text).lower()
    tt = re.sub(r"\\[a-zA-Z]+", " ", tt)
    ws = re.findall(r"[a-z]{3,}", tt)
    # crude suffix stripping so "hours"/"hour" and "dividing"/"divide" meet
    out = set()
    for wd in ws:
        if wd in STOP:
            continue
        for suf in ("ing", "ies", "ed", "es", "s"):
            if wd.endswith(suf) and len(wd) - len(suf) >= 3:
                wd = wd[: -len(suf)]
                break
        out.add(wd)
    return out


def load():
    return json.load(open(MATH))


BANK = load()
# inverse document frequency over numerals, so common small integers are cheap
_df = Counter()
for row in BANK:
    for nm in numerals(row["stem"]):
        _df[nm] += 1
_N = len(BANK)


def num_weight(nm):
    import math
    return math.log(_N / (1 + _df.get(nm, 0)))


def num_score(a, b):
    shared = a & b
    if not shared:
        return 0.0, shared
    tot = sum(num_weight(nm) for nm in (a | b))
    return (sum(num_weight(nm) for nm in shared) / tot if tot else 0.0), shared


def flat(text, width=200):
    return re.sub(r"\s+", " ", strip_tags(text)).strip()[:width]


# ------------------------------------------------------------------ commands
def cmd_sweep():
    from math_test27 import ALL
    for q in ALL:
        stem = q["stem"]
        mine_n = numerals(stem)
        mine_s = skeletons(stem)
        mine_b = skeletons(stem, blind_digits=True)
        hits = []
        for row in BANK:
            ns, shared = num_score(mine_n, numerals(row["stem"]))
            sk = mine_s & skeletons(row["stem"])
            bk = mine_b & skeletons(row["stem"], blind_digits=True)
            if sk:
                hits.append((3.0 + len(sk), row["label"], f"LATEX {sorted(sk)}", row["stem"]))
            elif bk and ns >= 0.12:
                hits.append((2.0 + ns, row["label"], f"SHAPE {sorted(bk)[:2]}", row["stem"]))
            elif ns >= 0.30 and len(shared) >= 3:
                hits.append((ns, row["label"], f"NUMS {sorted(shared)}", row["stem"]))
        hits.sort(reverse=True, key=lambda z: z[0])
        if hits:
            print(f"\n### {q['n']} :: {flat(stem, 150)}")
            for sc, lab, why, st in hits[:5]:
                print(f"   {sc:5.2f} {lab:22} {why}")
                print(f"          {flat(st, 190)}")


def cmd_phrase(text, n=12):
    mine = words(text)
    scored = []
    for row in BANK:
        ws = words(row["stem"])
        if not mine:
            continue
        scored.append((len(mine & ws) / len(mine), row["label"], row["stem"]))
    scored.sort(reverse=True)
    for sc, lab, st in scored[:n]:
        print(f"{sc:.2f}  {lab}\n      {flat(st, 230)}\n")


def cmd_find(pattern, n=25):
    rx = re.compile(pattern, re.I)
    found = 0
    for row in BANK:
        body = re.sub(r"\s+", " ", strip_tags(row["stem"]))
        if rx.search(body):
            found += 1
            if found <= n:
                print(f"{row['label']:22} {body[:220]}")
    print(f"-- {found} match(es)")


def cmd_nums(vals, n=20):
    want = set(v.replace(",", "") for v in vals)
    scored = []
    for row in BANK:
        got = numerals(row["stem"]) & want
        if len(got) >= max(2, len(want) - 1):
            scored.append((len(got), row["label"], sorted(got), row["stem"]))
    scored.sort(reverse=True)
    for sc, lab, got, st in scored[:n]:
        print(f"{sc}  {lab}  {got}\n      {flat(st, 230)}\n")


def cmd_show(label):
    for row in BANK:
        if row["label"].lower() == label.lower():
            print(row["label"])
            print(re.sub(r"\s+", " ", strip_tags(row["stem"])))
            return
    print("no such label")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    cmd = sys.argv[1]
    arg = " ".join(sys.argv[2:])
    {"sweep": lambda: cmd_sweep(),
     "phrase": lambda: cmd_phrase(arg),
     "find": lambda: cmd_find(arg),
     "nums": lambda: cmd_nums(sys.argv[2:]),
     "show": lambda: cmd_show(arg)}[cmd]()
