#!/usr/bin/env python3
"""
Assemble Test 31 into insert-ready JSON.

    READING_WRITING  M1 STANDARD / M2 EASY / M2 HARD   27 each
    MATH             M1 STANDARD / M2 EASY / M2 HARD   22 each, 19 MC + 3 FR

Two structural rules are enforced by construction, then re-checked:

  * R&W block order. Every module sorts on block rank, so the reading domains
    run in the mandated sequence and the writing block opens at question 15 and
    never earlier. `report()` confirms the rank sequence is monotonic.

  * Per-question difficulty follows the module. This is the Test 1/2
    convention: an EASY module's questions are EASY, a HARD module's are HARD.
    Tests 3-6 left every question MEDIUM regardless of module, which is why
    their Question Bank difficulty badges and filters are wrong. Test 31 does
    not repeat that.

Nothing here is reused: the Math is authored in math_test31.py and verified
independently by verify_math_test31.py, and every R&W passage in
rw_test31.py was screened against the 1,295-passage corpus in
../rw_authored_corpus.json before it was drafted, and re-checked by
verify_rw_test31.py, which also substitutes every choice into its blank and
reads the result back.

The `_ref` prefixes are the test's own: AUTHORED-T31 for R&W and AUTHORED/T31
for Math. This file was created from ../test-19-build/assemble_test19.py, and a
leftover T19 in either prefix would tag every one of Test 31's 147 rows with a
sibling test's provenance — so an assertion below fails the build if the string
"T19" survives anywhere in the assembled JSON.

Run:  python3 assemble_test31.py
Out:  test31.json
"""
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

from math_test31 import (MODULE_1 as MATH_M1, MODULE_2_EASY as MATH_M2E,      # noqa: E402
                        MODULE_2_HARD as MATH_M2H)

HERE = os.path.dirname(os.path.abspath(__file__))

BLOCK_ORDER = [
    "Words in Context", "Text Structure and Purpose", "Cross-Text Connections",
    "Central Ideas and Details", "Command of Evidence", "Inferences",
    "Boundaries", "Form, Structure, and Sense", "Transitions", "Rhetorical Synthesis",
]
RANK = {s: i for i, s in enumerate(BLOCK_ORDER)}
FIRST_WRITING_RANK = 6

SKILL_CODE = {
    "Words in Context": ("CAS", "CAS-WV"),
    "Text Structure and Purpose": ("CAS", "CAS-TS"),
    "Cross-Text Connections": ("CAS", "CAS-CT"),
    "Central Ideas and Details": ("INI", "INI-CI"),
    "Command of Evidence": ("INI", "INI-CE"),
    "Inferences": ("INI", "INI-IE"),
    "Boundaries": ("SEC", "SEC-BS"),
    "Form, Structure, and Sense": ("SEC", "SEC-FS"),
    "Transitions": ("EOI", "EOI-TR"),
    "Rhetorical Synthesis": ("EOI", "EOI-RS"),
}

# 14 reading + 13 writing, so the writing block opens at question 15.
QUOTA = {
    "Words in Context": 5, "Text Structure and Purpose": 2, "Central Ideas and Details": 2,
    "Command of Evidence": 3, "Inferences": 2,
    "Boundaries": 4, "Form, Structure, and Sense": 3, "Transitions": 3,
    "Rhetorical Synthesis": 3,
}

MODULES = ["RW_M1", "RW_M2E", "RW_M2H"]
# Module difficulty -> the difficulty stamped on each of its questions.
QUESTION_DIFFICULTY = {
    "RW_M1": "MEDIUM", "RW_M2E": "EASY", "RW_M2H": "HARD",
    "MATH_M1": "MEDIUM", "MATH_M2E": "EASY", "MATH_M2H": "HARD",
}

random.seed(310031)


def load_rw_pool():
    """The authored, key-balanced pool, grouped by block."""
    with open(os.path.join(HERE, "rw_test31_balanced.json")) as fh:
        rows = json.load(fh)
    pool = defaultdict(list)
    for q in rows:
        item = dict(q)
        item["_ref"] = f"AUTHORED-T31:{q['num']}"
        pool[q["skill"]].append(item)
    for block in pool:
        random.shuffle(pool[block])
    return pool, set()


def rebalance_module(items):
    """Even the answer key out WITHIN one module, which is what a student sees.

    balance_rw.py evens out the 81-item pool, but the assembler then deals that
    pool into three modules at random, and an even pool deals into uneven
    modules: this build's first deal put B on 12 of Module 1's 27 questions
    (44%) and A on 10 of Module 2 Easy's, against a worst case of 9 anywhere in
    Tests 19, 20, 21 and 30. A student takes ONE module, so the module is the
    unit that has to be balanced.

    Rotating a question's choices moves its key without touching its content.
    That is only safe because no rationale in rw_test31.py names an option by
    letter — verify_rw_test31.py checks that with the same pattern balance_rw.py
    uses, and the assertion below re-checks that the key still sits on the same
    option text after every rotation.

    The target letters are shuffled rather than dealt in order: dealing A, B, C,
    D round-robin balances perfectly and produces a visible repeating pattern
    down the answer key, which is worse than the imbalance it fixes. Runs of
    four or more of the same letter are rejected for the same reason.
    """
    letters = "ABCD"
    n = len(items)
    target = [letters[i % 4] for i in range(n)]      # 7/7/7/6 over 27
    for _ in range(2000):
        random.shuffle(target)
        if not any(target[i] == target[i + 1] == target[i + 2] == target[i + 3]
                   for i in range(n - 3)):
            break
    out = []
    for item, want in zip(items, target):
        cur = letters.index(item["answer"])
        shift = (cur - letters.index(want)) % 4
        moved = dict(item)
        moved["choices"] = item["choices"][shift:] + item["choices"][:shift]
        moved["answer"] = want
        assert moved["choices"][letters.index(want)] == item["choices"][cur], item["num"]
        out.append(moved)
    return out


def build_rw(pool):
    """Deal the quota per module, then sort each module on block rank."""
    out = {}
    shortfall = Counter()
    for mod in MODULES:
        picked = []
        for block, want in QUOTA.items():
            have = pool[block]
            take = min(want, len(have))
            if take < want:
                shortfall[block] += want - take
            picked += [have.pop() for _ in range(take)]
        # Block rank first, then a stable shuffle inside the block.
        picked.sort(key=lambda q: RANK[q["skill"]])
        out[mod] = rebalance_module(picked)
    return out, shortfall


def build_math():
    def conv(items, mod_key):
        # The Math source writes "MC"/"FR"; older authored files write the full
        # enum names. Accept both rather than editing the older file.
        out = []
        for q in items:
            domain, skill = q["domain"], q["skill"]
            is_fr = q["type"] in ("FR", "FREE_RESPONSE")
            row = {
                "_ref": f"AUTHORED/T31-{mod_key}:{q['n']}",
                "type": "FREE_RESPONSE" if is_fr else "MULTIPLE_CHOICE",
                "domain": domain, "skill": skill,
                "stem": q["stem"],
                "difficulty": QUESTION_DIFFICULTY[mod_key],
                "check": q.get("check", ""),
            }
            if not is_fr:
                row["choices"] = [
                    {"label": "ABCD"[i], "content": c, "isCorrect": "ABCD"[i] == q["correct"]}
                    for i, c in enumerate(q["choices"])
                ]
            else:
                row["correctAnswerFR"] = json.dumps(q["answers"])
            out.append(row)
        return out

    return {
        "MATH_M1": conv(MATH_M1, "MATH_M1"),
        "MATH_M2E": conv(MATH_M2E, "MATH_M2E"),
        "MATH_M2H": conv(MATH_M2H, "MATH_M2H"),
    }


def convert_rw(items, mod_key):
    out = []
    for q in items:
        domain, skill = SKILL_CODE[q["skill"]]
        row = {
            "_ref": q["_ref"],
            "type": "MULTIPLE_CHOICE",
            "domain": domain, "skill": skill, "block": q["skill"],
            "stem": q["stem"],
            "passage": q.get("passage"),
            "difficulty": QUESTION_DIFFICULTY[mod_key],
            "why": q.get("why", ""),
            "choices": [
                {"label": "ABCD"[i], "content": c, "isCorrect": "ABCD"[i] == q["answer"]}
                for i, c in enumerate(q["choices"])
            ],
        }
        if q.get("table"):
            row["table"] = q["table"]
        out.append(row)
    return out


def report(test):
    ok = True
    print(f"{'module':<10}{'n':>4}{'read':>6}{'write':>7}{'w@':>5}  {'monotonic':>10}  difficulty")
    for mod in MODULES:
        items = test[mod]
        ranks = [RANK[q["block"]] for q in items]
        monotonic = all(a <= b for a, b in zip(ranks, ranks[1:]))
        writing = [i for i, r in enumerate(ranks) if r >= FIRST_WRITING_RANK]
        first_w = writing[0] + 1 if writing else None
        reading = len(items) - len(writing)
        diffs = set(q["difficulty"] for q in items)
        good = monotonic and len(items) == 27 and first_w is not None and 14 <= first_w <= 16
        ok &= good
        print(f"{mod:<10}{len(items):>4}{reading:>6}{len(writing):>7}{first_w or 0:>5}  "
              f"{str(monotonic):>10}  {','.join(sorted(diffs))}"
              f"{'' if good else '   <-- FAIL'}")

    for mod in ("MATH_M1", "MATH_M2E", "MATH_M2H"):
        items = test[mod]
        fr = sum(1 for q in items if q["type"] == "FREE_RESPONSE")
        diffs = set(q["difficulty"] for q in items)
        good = len(items) == 22 and fr == 3 and len(diffs) == 1
        ok &= good
        print(f"{mod:<10}{len(items):>4}{'':>6}{'':>7}{'':>5}{'':>12}  "
              f"{','.join(sorted(diffs))}  ({fr} free-response)"
              f"{'' if good else '   <-- FAIL'}")

    # A choice with no letters or digits renders as an empty row. Test 8 shipped
    # 12 Boundaries questions whose options were bare punctuation (", " / "; ")
    # before this check existed; the real test always repeats the words either
    # side of the blank inside every option.
    wordless = [
        f"{mod} Q{i}"
        for mod in test
        for i, q in enumerate(test[mod], 1)
        for c in q.get("choices", [])
        if not re.search(r"[A-Za-z0-9]", c["content"])
    ]
    if wordless:
        print(f"  !! {len(wordless)} answer choices render as empty: {wordless[:6]}")
        ok = False

    for mod in MODULES:
        keys = Counter(c["label"] for q in test[mod]
                       for c in q["choices"] if c["isCorrect"])
        spread = dict(sorted(keys.items()))
        worst = max(keys.values())
        print(f"  {mod} key spread {spread}"
              f"{'' if worst <= 9 else '   <-- one letter dominates'}")
        ok &= worst <= 9

    refs = [q["_ref"] for mod in test for q in test[mod]]
    dupes = [r for r, n in Counter(refs).items() if n > 1]
    print(f"\ntotal questions: {len(refs)}   duplicate refs: {len(dupes)}")
    ok &= not dupes

    for mod in test:
        for q in test[mod]:
            keys = [c for c in q.get("choices", []) if c["isCorrect"]]
            if q["type"] == "MULTIPLE_CHOICE" and len(keys) != 1:
                print(f"  !! {q['_ref']}: {len(keys)} correct choices")
                ok = False
            if q["type"] == "FREE_RESPONSE":
                try:
                    val = json.loads(q["correctAnswerFR"])
                    if not isinstance(val, list) or not val:
                        raise ValueError
                except Exception:
                    print(f"  !! {q['_ref']}: correctAnswerFR is not a JSON array")
                    ok = False
    return ok


if __name__ == "__main__":
    pool, used = load_rw_pool()
    print(f"R&W pool available: {sum(len(v) for v in pool.values())}\n")

    rw, shortfall = build_rw(pool)
    if shortfall:
        print(f"!! short on: {dict(shortfall)}\n")

    test = {mod: convert_rw(rw[mod], mod) for mod in MODULES}
    test.update(build_math())

    blob = json.dumps(test)
    for sibling in ("T19", "T21", "test19"):
        if sibling in blob:
            print(f"  !! assembled JSON still carries the sibling tag {sibling!r}")
            raise SystemExit(1)

    ok = report(test)
    with open(os.path.join(HERE, "test31.json"), "w") as fh:
        json.dump(test, fh, indent=1, ensure_ascii=False)
    print(f"\nwrote test31.json  —  {'OK' if ok else 'WITH FAILURES'}")
    raise SystemExit(0 if ok else 1)
