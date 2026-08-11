#!/usr/bin/env python3
"""Originality screen for Test 29's R&W passages.

Two questions, and they are not the same question:

  1. Does a passage repeat something already in the 1,295-passage bank?
     Reject at 0.50, READ everything at or above 0.45. The threshold is triage,
     not a verdict — a repeat that changes the setting words scores low
     precisely because it changed the words.

  2. Does a passage repeat ANOTHER PASSAGE IN THIS FILE? This is the failure
     mode a narrow territory produces on its own. Test 29 owns five trades that
     share a vocabulary, so two items can land on one sub-topic without either
     of them touching the bank at all. validate_tests.py enforces 0.24 on the
     pairs a single student can meet (Module 1 against either Module 2 branch),
     and because the assembler shuffles before it deals, WHICH module a passage
     lands in is not known here. So this holds every pair in the file to 0.24 —
     stricter than the validator, and the only way to be sure before assembly.

The internal pass deliberately uses validate_tests.py's own tokenizer, imported
rather than re-implemented, so a passage that clears this cannot fail there on
a wording difference between two copies of the same function.

    python3 screen_topics.py            # both passes
    python3 screen_topics.py internal   # pass 2 only (fast)
"""
import json
import os
import re
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

from validate_tests import _passage_jaccard, _passage_tokens  # noqa: E402

from rw_test29 import QUESTIONS  # noqa: E402

CORPUS = os.path.join(HERE, "..", "rw_authored_corpus.json")

CORPUS_READ = 0.45
CORPUS_REJECT = 0.50
INTERNAL_LIMIT = 0.24


def flat(html):
    return " ".join(re.sub(r"<[^>]+>", " ", html or "").split())


def corpus_pass():
    with open(CORPUS) as fh:
        rows = json.load(fh)
    banked = [(f"{r['src']}:{r['num']}", (r.get("passage") or ""), (r.get("stem") or ""))
              for r in rows]
    banked = [(lab, p, _passage_tokens(p + " " + s)) for lab, p, s in banked if p]

    print(f"== pass 1: {len(QUESTIONS)} passages vs {len(banked)} banked")
    worst = []
    for q in QUESTIONS:
        mine = _passage_tokens((q.get("passage") or "") + " " + (q.get("stem") or ""))
        if not mine:
            continue
        best = sorted(
            ((len(mine & t) / len(mine | t), lab, p) for lab, p, t in banked if t),
            reverse=True, key=lambda z: z[0])[:3]
        worst.append((best[0][0], q["num"], best))

    worst.sort(reverse=True)
    fails = 0
    for score, num, best in worst[:14]:
        flag = ""
        if score >= CORPUS_REJECT:
            flag = "   <<< REJECT"
            fails += 1
        elif score >= CORPUS_READ:
            flag = "   <<< READ IT"
        print(f"  {score:.3f}  {num:<4} vs {best[0][1]}{flag}")
        if score >= CORPUS_READ:
            for sc, lab, p in best:
                print(f"          {sc:.3f} {lab}: {flat(p)[:150]}")
    print(f"  highest vs corpus: {worst[0][0]:.3f}")
    return fails


def internal_pass():
    items = [(q["num"], q["skill"], q.get("passage") or "") for q in QUESTIONS]
    items = [i for i in items if i[2]]
    pairs = []
    for (na, sa, pa), (nb, sb, pb) in combinations(items, 2):
        pairs.append((_passage_jaccard(pa, pb), na, sa, nb, sb))
    pairs.sort(reverse=True)

    print(f"\n== pass 2: {len(pairs)} internal pairs, limit {INTERNAL_LIMIT}")
    fails = 0
    for score, na, sa, nb, sb in pairs[:14]:
        flag = ""
        if score >= INTERNAL_LIMIT:
            flag = "   <<< COLLIDES"
            fails += 1
        print(f"  {score:.3f}  {na} ({sa[:22]})  vs  {nb} ({sb[:22]}){flag}")
    print(f"  worst internal pair: {pairs[0][0]:.3f}")
    return fails


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else ""
    fails = 0
    if only != "internal":
        fails += corpus_pass()
    fails += internal_pass()
    print(f"\n{len(QUESTIONS)} passages screened — {'FAIL' if fails else 'clean'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
