#!/usr/bin/env python3
"""
Assemble Test 26 into insert-ready JSON.

    READING_WRITING  M1 STANDARD / M2 EASY / M2 HARD   27 each
    MATH             M1 STANDARD / M2 EASY / M2 HARD   22 each, 19 MC + 3 FR

Two structural rules are enforced by construction, then re-checked:

  * R&W block order. Every module sorts on block rank, so the reading domains
    run in the mandated sequence and the writing block opens at question 15 and
    never earlier. `report()` confirms the rank sequence is monotonic.

  * Per-question difficulty follows the module. This is the Test 1/2
    convention: an EASY module's questions are EASY, a HARD module's are HARD.
    Tests 3-6 left every question MEDIUM regardless of module, which is why
    their Question Bank difficulty badges and filters are wrong. Test 26 does
    not repeat that.

Nothing here is reused: the Math is authored in math_test26.py and verified
independently by verify_math_test26.py, and every R&W passage in
rw_test26.py was screened against the 1,295-passage corpus in
../rw_authored_corpus.json before it was drafted.

Three checks were added here for Test 26:

  * Provenance. Scaffolding this directory from test-20-build leaves TWO tags
    behind, and they do not look alike: the Math one is `AUTHORED/T20-` and the
    R&W one is `AUTHORED-T20:`. A substitution keyed on the hyphen fixes the
    Math tag and silently misses the R&W one, which is how Tests 19-21 nearly
    stamped Test 18's provenance on their own R&W questions. report() now
    asserts that no `T<n>` other than T26 survives anywhere in the JSON.

  * Cross-module scenes. A student sits Module 1 plus ONE Module 2 branch, so a
    Module 2 item that reuses a Module 1 setting shows the same scene twice to
    half the cohort. This is checked as passage-token Jaccard between every
    Module 1 item and every Module 2 item, NOT as a keyword match: a keyword
    list for this test would have to hold "bell", "ring", "peal", "stop",
    "pipe", "tone" and "round", every one of which has an ordinary English
    sense that would fire constantly. A boundary-free substring match in a
    checker is worse than no check, because it trains you to ignore the output.

  * Block quota. The quota below includes Cross-Text Connections, which the
    Test 20 quota this file was scaffolded from did not use.

Run:  python3 assemble_test26.py
Out:  test26.json
"""
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

from math_test26 import (MODULE_1 as MATH_M1, MODULE_2_EASY as MATH_M2E,      # noqa: E402
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
    "Words in Context": 5, "Text Structure and Purpose": 1, "Cross-Text Connections": 1,
    "Central Ideas and Details": 2, "Command of Evidence": 3, "Inferences": 2,
    "Boundaries": 4, "Form, Structure, and Sense": 3, "Transitions": 3,
    "Rhetorical Synthesis": 3,
}
assert sum(QUOTA.values()) == 27, "the quota must fill a 27-question module exactly"

MODULES = ["RW_M1", "RW_M2E", "RW_M2H"]
# Module difficulty -> the difficulty stamped on each of its questions.
QUESTION_DIFFICULTY = {
    "RW_M1": "MEDIUM", "RW_M2E": "EASY", "RW_M2H": "HARD",
    "MATH_M1": "MEDIUM", "MATH_M2E": "EASY", "MATH_M2H": "HARD",
}

random.seed(260026)


def load_rw_pool():
    """The authored, key-balanced pool, grouped by block."""
    with open(os.path.join(HERE, "rw_test26_balanced.json")) as fh:
        rows = json.load(fh)
    pool = defaultdict(list)
    for q in rows:
        item = dict(q)
        item["_ref"] = f"AUTHORED-T26:{q['num']}"
        pool[q["skill"]].append(item)
    for block in pool:
        random.shuffle(pool[block])
    return pool, set()


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
        out[mod] = picked
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
                "_ref": f"AUTHORED/T26-{mod_key}:{q['n']}",
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

    # Provenance. The R&W tag and the Math tag have different shapes, so a
    # substitution that fixes one can miss the other with nothing to show for it.
    strays = sorted({m for mod in test for q in test[mod]
                     for m in re.findall(r"T\d+", str(q["_ref"])) if m != "T26"})
    if strays:
        print(f"\n  !! foreign provenance tags survive in _ref: {strays}")
        ok = False
    else:
        print("\nprovenance: every _ref carries T26 and nothing else")

    # Cross-module scenes, measured on passage tokens rather than by keyword.
    stop = set("the a an and or of to in on at by for with from as is are was were be been it its "
               "that this which who not no than then so such can could will would may might must "
               "have has had one two three four five six seven eight nine ten more most some any "
               "all each every other same own very just only into out up down over under about "
               "after before during while because since until through between against among "
               "within without their they them there here he she his her him we us our you your"
               .split())

    def ptoks(q):
        t = re.sub(r"<[^>]+>", " ", q.get("passage") or "").lower()
        t = re.sub(r"&[a-z]+;", " ", t)
        return {w for w in re.findall(r"[a-z]+", t) if w not in stop and len(w) > 2}

    worst = (0.0, "", "")
    for m2 in ("RW_M2E", "RW_M2H"):
        for a in test["RW_M1"]:
            ta = ptoks(a)
            for b in test[m2]:
                tb = ptoks(b)
                j = len(ta & tb) / max(1, len(ta | tb))
                if j > worst[0]:
                    worst = (j, a["_ref"], f"{m2} {b['_ref']}")
    print(f"worst Module 1 / Module 2 scene overlap: {worst[0]:.2f}  "
          f"({worst[1]} vs {worst[2]})")
    if worst[0] >= 0.24:   # matches the calibrated threshold in ../validate_tests.py
        print("  !! a Module 2 item reuses a Module 1 setting")
        ok = False

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

    ok = report(test)
    with open(os.path.join(HERE, "test26.json"), "w") as fh:
        json.dump(test, fh, indent=1, ensure_ascii=False)
    print(f"\nwrote test26.json  —  {'OK' if ok else 'WITH FAILURES'}")
    raise SystemExit(0 if ok else 1)
