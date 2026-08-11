#!/usr/bin/env python3
"""
Assemble Test 22 into insert-ready JSON.

    READING_WRITING  M1 STANDARD / M2 EASY / M2 HARD   27 each
    MATH             M1 STANDARD / M2 EASY / M2 HARD   22 each, 19 MC + 3 FR

Two structural rules are enforced by construction, then re-checked:

  * R&W block order. Every module sorts on block rank, so the reading domains
    run in the mandated sequence and the writing block opens at question 15 and
    never earlier. `report()` confirms the rank sequence is monotonic.

  * Per-question difficulty follows the module. This is the Test 1/2
    convention: an EASY module's questions are EASY, a HARD module's are HARD.
    Tests 3-6 left every question MEDIUM regardless of module, which is why
    their Question Bank difficulty badges and filters are wrong. Test 22 does
    not repeat that.

Nothing here is reused: the Math is authored in math_test22.py and verified
independently by verify_math_test22.py, and every R&W passage in
rw_test22.py was screened against the 1,295-passage corpus in
../rw_authored_corpus.json before it was drafted.

A third rule this assembler adds, which the Test 16 original did not have:

  * Two R&W passages on the same subject must not land in the SAME module.
    A student sits one module at a time, so a near-repeat split across two
    modules costs nothing while a near-repeat inside one module is a visible
    duplication. The dealing is therefore run over a range of shuffle seeds and
    the seed minimising the worst same-module passage Jaccard is kept. This is
    the R&W counterpart of the cross-module setting check Tests 19-21 added for
    Math, and it is a placement rule, not a content rule — the content-level
    self-screen lives in rw_test22.py and check_originality.py.

Provenance: scaffolding this file from test-16-build means every Test 16 tag
has to be rewritten, and there are TWO of them in different shapes — the Math
tag `AUTHORED/T16-` and the R&W tag `AUTHORED-T16:`. A substitution keyed on
the hyphen rewrites the first and silently misses the second; that is exactly
how Tests 19-21 nearly shipped Test 18 provenance on their R&W. `report()`
asserts that no `T<n>` other than T22 survives anywhere in the output.

Run:  python3 assemble_test22.py
Out:  test22.json
"""
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict

from math_test22 import (MODULE_1 as MATH_M1, MODULE_2_EASY as MATH_M2E,      # noqa: E402
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

random.seed(220022)

# Words that carry no topical signal inside THIS test's territory. "bee",
# "honey", "wax", "sugar" and "beet" appear in most of the 81 passages by
# construction, so leaving them in the token set makes every pair look related
# and the measure stops discriminating. This is the same lesson as dropping
# "ground" from Test 19's setting check: a keyword that is ordinary vocabulary
# in context is worse than no keyword.
TERRITORY_STOP = set("""
bee bees beekeeper beekeepers hive hives colony colonies comb combs honey wax
sugar sugars beet syrup boil boiled boiling factory
""".split())

STOP = set("""
a an the and or but of in on at to for with from by as is are was were be been
being it its this that these those which who whom whose what when where while
how not no nor so than then there here their they them he she his her him you
your we our us my one two three into over under about between during after
before again more most much many few some any all each both other another such
own same very can will just should now has have had do does did having doing up
down out off above below only also because if though however thus therefore per
cent percent year years first second new old made make makes making use used
uses using take takes taken took give gives given gave get got put set well back
even still
""".split())


def topic_tokens(html):
    """Content words of a passage, minus this territory's shared vocabulary."""
    text = re.sub(r"<[^>]+>", " ", html or "")
    text = re.sub(r"&[a-z]+;", " ", text)
    words = re.findall(r"[a-z]+", text.lower())
    return set(w for w in words
               if len(w) > 2 and w not in STOP and w not in TERRITORY_STOP)


def load_rw_pool(seed):
    """The authored, key-balanced pool, grouped by block."""
    rng = random.Random(seed)
    with open(os.path.join(HERE, "rw_test22_balanced.json")) as fh:
        rows = json.load(fh)
    pool = defaultdict(list)
    for q in rows:
        item = dict(q)
        item["_ref"] = f"AUTHORED-T22:{q['num']}"
        item["_topic"] = topic_tokens(q.get("passage", ""))
        pool[q["skill"]].append(item)
    for block in pool:
        rng.shuffle(pool[block])
    return pool, set()


def worst_same_module_pair(rw):
    """Highest passage Jaccard between two questions dealt to one module."""
    worst = (0.0, None, None, None)
    for mod, items in rw.items():
        for i, a in enumerate(items):
            for b in items[i + 1:]:
                ta, tb = a["_topic"], b["_topic"]
                if not ta or not tb:
                    continue
                j = len(ta & tb) / len(ta | tb)
                if j > worst[0]:
                    worst = (j, mod, a["num"], b["num"])
    return worst


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


def deal_rw(seeds=range(400)):
    """Deal the R&W pool under many shuffles; keep the least self-similar one.

    The deal itself is trivial; what is being searched for is a placement in
    which no module contains two passages on the same subject. Every seed
    produces a structurally valid test, so this can only improve the result and
    can never fail — if no seed separates a pair, the best available is used and
    reported rather than silently accepted.
    """
    best = None
    for seed in seeds:
        pool, _ = load_rw_pool(seed)
        rw, shortfall = build_rw(pool)
        score = worst_same_module_pair(rw)
        if best is None or score[0] < best[0][0]:
            best = (score, rw, shortfall, seed)
        if score[0] == 0.0:
            break
    score, rw, shortfall, seed = best
    print(f"R&W placement: seed {seed}, worst same-module passage Jaccard "
          f"{score[0]:.3f}" + (f"  ({score[1]}: {score[2]} ~ {score[3]})" if score[1] else ""))
    return rw, shortfall


def build_math():
    def conv(items, mod_key):
        # The Math source writes "MC"/"FR"; older authored files write the full
        # enum names. Accept both rather than editing the older file.
        out = []
        for q in items:
            domain, skill = q["domain"], q["skill"]
            is_fr = q["type"] in ("FR", "FREE_RESPONSE")
            row = {
                "_ref": f"AUTHORED/T22-{mod_key}:{q['n']}",
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

    # Provenance. This file was scaffolded from test-16-build, which stamps two
    # differently shaped tags — `AUTHORED/T16-` on Math and `AUTHORED-T16:` on
    # R&W. Substituting on the hyphen rewrites one and misses the other, which
    # is how Tests 19-21 nearly shipped Test 18's tag on their own R&W. Assert
    # on the assembled output rather than trusting the substitution.
    foreign = sorted({
        m.group(0)
        for mod in test for q in test[mod]
        for m in [re.search(r"T(\d+)", str(q.get("_ref", "")))]
        if m and m.group(1) != "22"
    })
    if foreign:
        print(f"  !! foreign test provenance in _ref: {foreign}")
        ok = False
    else:
        print("provenance: every _ref is T22, no scaffold tag survived")

    # Rhetorical Synthesis has two real stem shapes and the assembled test must
    # contain both, because a classifier keyed only on "the notes" misfiles
    # every question of the other kind and nothing catches it if only one shape
    # is ever produced.
    rs = [q for mod in MODULES for q in test[mod] if q["block"] == "Rhetorical Synthesis"]
    notes = sum(1 for q in rs if "information from the notes" in q["stem"])
    givens = sum(1 for q in rs if "information from the given sentences" in q["stem"])
    print(f"rhetorical synthesis: {notes} 'from the notes', {givens} 'from the given sentences'")
    if notes + givens != len(rs) or not notes or not givens:
        print("  !! a Rhetorical Synthesis stem uses neither recognised phrasing")
        ok = False
    return ok


if __name__ == "__main__":
    rw, shortfall = deal_rw()
    print(f"R&W dealt: {sum(len(v) for v in rw.values())}\n")
    if shortfall:
        print(f"!! short on: {dict(shortfall)}\n")

    test = {mod: convert_rw(rw[mod], mod) for mod in MODULES}
    test.update(build_math())

    ok = report(test)
    with open(os.path.join(HERE, "test22.json"), "w") as fh:
        json.dump(test, fh, indent=1, ensure_ascii=False)
    print(f"\nwrote test22.json  —  {'OK' if ok else 'WITH FAILURES'}")
    raise SystemExit(0 if ok else 1)
