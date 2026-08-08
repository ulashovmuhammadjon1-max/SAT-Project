#!/usr/bin/env python3
"""
Even out the answer-key distribution of the authored Reading & Writing pool.

Written by hand, the correct option tends to land in the same place — here it
was B 42, A 26, C 13, D 0, which a student would notice within one module.

Rotating a question's choices moves its key, but it also silently invalidates
any rationale that refers to an option *by letter* ("A is consistent with
either explanation"). That exact breakage happened during the Test 6 build, so
this only rotates questions whose `why` names no letter, and re-checks
afterwards that no rationale points at the wrong option.

Out: rw_test9_balanced.json
"""
import json
import re
from collections import Counter

from rw_test9 import QUESTIONS

LETTERS = "ABCD"
# A standalone option letter: "A is consistent", "Option D would support".
LETTER_REF = re.compile(r"(?:^|[\s(])(?:[Oo]ptions?\s+)?([ABCD])(?=[\s,.;:)']|$)")


def names_a_letter(why):
    return bool(LETTER_REF.search(why or ""))


def rotate(q, target):
    """Move the key to `target` by rotating the choice list."""
    cur = LETTERS.index(q["answer"])
    want = LETTERS.index(target)
    shift = (cur - want) % 4
    ch = q["choices"]
    q = dict(q)
    q["choices"] = ch[shift:] + ch[:shift]
    q["answer"] = target
    return q


def main():
    out = []
    locked = 0
    counts = Counter()
    # Deal keys round-robin so the distribution stays even as we go, taking the
    # locked questions' existing keys into account first.
    for q in QUESTIONS:
        if names_a_letter(q.get("why", "")):
            counts[q["answer"]] += 1
            locked += 1

    for q in QUESTIONS:
        if names_a_letter(q.get("why", "")):
            out.append(q)
            continue
        target = min(LETTERS, key=lambda L: (counts[L], LETTERS.index(L)))
        moved = rotate(q, target)
        counts[target] += 1
        out.append(moved)

    # The key must still sit on the option it started on.
    for before, after in zip(QUESTIONS, out):
        assert before["choices"][LETTERS.index(before["answer"])] == \
               after["choices"][LETTERS.index(after["answer"])], before["num"]

    final = Counter(q["answer"] for q in out)
    print(f"{len(out)} questions   {locked} locked by a letter-naming rationale")
    print(f"key distribution: {dict(sorted(final.items()))}")
    worst = max(final.values()) / len(out)
    print(f"most common answer: {worst:.0%}")
    assert worst <= 0.32, "still unbalanced"

    with open("rw_test9_balanced.json", "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    print("wrote rw_test9_balanced.json")


if __name__ == "__main__":
    main()
