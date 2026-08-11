#!/usr/bin/env python3
"""
Verify the 81 originally-authored Reading & Writing items for Test 31.

Five passes. Each exists because a real defect got past everything else:

 1. Shape — 81 items, the block counts the assembler's 27x3 quota needs, four
    distinct choices, one key, a rationale on every item, no sibling test's
    provenance tag surviving in any string.

 2. Substitution. Every choice is written into the blank and the resulting
    sentence is read back mechanically, looking for the junctions a human eye
    skips: a word repeated across the seam, a space before a punctuation mark,
    two marks in a row. A sibling build shipped a choice reading
    "quarter; yet the" against a passage continuing "the custom", giving
    "yet the the custom". THIS BUILD HAD THE SAME DEFECT — F8's third choice
    ended in "the" and the passage resumes "the gunner", so it rendered as
    "with his hands the the gunner". Nothing but substitution finds that.

 3. Rationales name options by CONTENT, never by letter, using the same
    LETTER_REF pattern balance_rw.py rotates on. A rationale that names a
    letter locks its question against rebalancing; the old pattern also
    matched the ARTICLE "A" starting a sentence, which silently locked three
    builds' worth of questions.

 4. Corpus dedupe against ../rw_authored_corpus.json (1,295 passages, READ
    ONLY): reject at 0.50, PRINT everything at or above 0.45, because the
    threshold decides what to read, not what to accept.

 5. Same-subject collision inside this test, at validate_tests.py's own 0.24
    threshold and with its own tokenizer — but over ALL 81 items rather than
    over one particular deal. The assembler deals randomly, so a pair that
    scores high must be fixed in the SOURCE; otherwise it passes today and
    fails the next time the seed changes.

Run:  python3 verify_rw_test31.py
"""
import json
import os
import re
from collections import Counter
from itertools import combinations

from rw_test31 import QUESTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []

BLOCK_QUOTA = {
    "Words in Context": 15, "Text Structure and Purpose": 6,
    "Central Ideas and Details": 6, "Command of Evidence": 9, "Inferences": 6,
    "Boundaries": 12, "Form, Structure, and Sense": 9, "Transitions": 9,
    "Rhetorical Synthesis": 9,
}

CORPUS_REJECT = 0.50
CORPUS_READ = 0.45
SAME_SUBJECT = 0.24


def check(cond, msg):
    if not cond:
        FAIL.append(msg)


# Same pattern balance_rw.py rotates on: an explicit marker, a parenthesis, or
# a bare letter used as the subject of a verb. Never a bare A-D plus space,
# which also matches the article "A" opening a sentence.
LETTER_REF = re.compile(
    r"\((?:[ABCD])\)"
    r"|\b(?:[Oo]ptions?|[Cc]hoices?|[Aa]nswers?)\s+([ABCD])\b"
    r"|(?:^|(?<=[\s(]))([ABCD])\s+(?:is|are|was|were|would|will|does|do|fails?|"
    r"states?|says?|gives?|makes?|describes?|names?|answers?|contradicts?|"
    r"reverses?|adds?|omits?|leaves?|treats?|asserts?|reads?|works?|"
    r"establishes?|supports?|overstates?|understates?|misses?)\b"
)


def text(html):
    tt = re.sub(r"<[^>]+>", " ", html or "")
    tt = (tt.replace("&ldquo;", '"').replace("&rdquo;", '"')
            .replace("&deg;", " degrees ").replace("&nbsp;", " "))
    tt = re.sub(r"&[a-z]+;", " ", tt)
    return re.sub(r"\s+", " ", tt).strip()


print("== pass 1: shape")
counts = Counter(q["skill"] for q in QUESTIONS)
check(len(QUESTIONS) == 81, f"{len(QUESTIONS)} items, expected 81")
for block, want in BLOCK_QUOTA.items():
    check(counts[block] == want,
          f"{block}: {counts[block]} items, the 27x3 quota needs {want}")
check(not set(counts) - set(BLOCK_QUOTA),
      f"unknown block(s): {set(counts) - set(BLOCK_QUOTA)}")

seen = set()
for q in QUESTIONS:
    tag = q["num"]
    check(tag not in seen, f"{tag}: duplicate item id")
    seen.add(tag)
    check(len(q["choices"]) == 4, f"{tag}: {len(q['choices'])} choices, expected 4")
    check(len(set(q["choices"])) == 4, f"{tag}: two identical choices")
    check(q["answer"] in "ABCD", f"{tag}: bad key {q['answer']!r}")
    check(bool(q.get("why")), f"{tag}: no rationale")
    check(bool(q.get("passage")), f"{tag}: no passage")
    check(bool(q.get("stem")), f"{tag}: no stem")
    blob = json.dumps(q)
    for sibling in ("T19", "T21", "AUTHORED-T1", "test19", "test21"):
        check(sibling not in blob, f"{tag}: carries a sibling test's tag {sibling!r}")
    # A choice with no letter or digit renders as an empty row in the exam.
    for i, cz in enumerate(q["choices"]):
        check(re.search(r"[A-Za-z0-9]", cz),
              f"{tag}: choice {'ABCD'[i]} has no letters or digits")
print(f"   {len(QUESTIONS)} items, blocks {dict(sorted(counts.items()))}")

print("== pass 2: substitution — every choice written into the blank")
subs = 0
for q in QUESTIONS:
    passage = q["passage"]
    if "_____" not in passage:
        continue
    for i, cz in enumerate(q["choices"]):
        subs += 1
        sentence = text(passage.replace("_____", cz))
        tagz = f"{q['num']} choice {'ABCD'[i]}"
        # A word repeated across the seam: "with his hands the" + "the gunner".
        for mo in re.finditer(r"(?<![A-Za-z])([A-Za-z]+)[,;:.]?\s+\1(?![A-Za-z])",
                              sentence):
            check(mo.group(1).lower() in ("had", "that", "who"),
                  f"{tagz}: repeats a word across the seam: {mo.group(0)!r}")
        check(not re.search(r"\s[,;:.]", sentence),
              f"{tagz}: a punctuation mark has a space in front of it")
        check(not re.search(r"[,;:]\s*[,;:]", sentence),
              f"{tagz}: two punctuation marks in a row")
        check(not re.search(r"\b(a|an|the)\s+(a|an|the)\b", sentence),
              f"{tagz}: two articles in a row")
print(f"   {subs} choice substitutions read back")

print("== pass 3: rationales name content, not letters")
locked = [q["num"] for q in QUESTIONS if LETTER_REF.search(q.get("why", ""))]
check(not locked, f"rationale names an option by letter, locking it: {locked}")
print(f"   {len(QUESTIONS)} rationales checked, {len(locked)} name a letter")

print("== pass 4: passage dedupe against the authored corpus")
corpus_path = os.path.join(HERE, "..", "rw_authored_corpus.json")


def sig(html):
    words = re.findall(r"[a-z]+", text(html).lower())
    return frozenset(w for w in words if len(w) > 3)


def jac(aa, bb):
    return len(aa & bb) / len(aa | bb) if aa and bb else 0.0


if os.path.exists(corpus_path):
    raw = json.load(open(corpus_path))
    rows = raw if isinstance(raw, list) else list(raw.values())
    others = []
    for row in rows:
        if isinstance(row, str):
            others.append(("corpus", sig(row)))
        else:
            label = (f"{row.get('src', 'corpus')}:{row.get('num', '?')}"
                     if row.get("src") else
                     (row.get("label") or row.get("num") or "corpus"))
            body = row.get("passage") or row.get("content") or row.get("text") or ""
            others.append((label, sig(body)))
    others = [(lab, sg) for lab, sg in others if sg]
    print(f"   comparing against {len(others)} corpus passages")
    worst = []
    for q in QUESTIONS:
        s0 = sig(q["passage"])
        score, label = max(((jac(s0, o), lab) for lab, o in others),
                           key=lambda z: z[0])
        worst.append((score, q["num"], label))
        check(score < CORPUS_REJECT,
              f"{q['num']}: passage similarity {score:.2f} to {label}")
    worst.sort(reverse=True)
    flagged = [rw for rw in worst if rw[0] >= CORPUS_READ]
    print(f"   {len(flagged)} at or above {CORPUS_READ:.2f} (read every one):")
    for sc, tag, lab in flagged:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
    print("   next closest:")
    for sc, tag, lab in [rw for rw in worst if rw[0] < CORPUS_READ][:6]:
        print(f"     {sc:.2f}  {tag}  vs {lab}")
else:
    check(False, "../rw_authored_corpus.json is missing — dedupe cannot run")

print("== pass 5: same-subject collision inside Test 31")
# validate_tests.py's tokenizer and threshold, applied to ALL 81 items rather
# than to one deal, because the assembler's deal is random: a pair fixed only
# for today's seed is not fixed.
STOP = {
    "this", "that", "then", "than", "with", "from", "they", "them", "their",
    "have", "been", "were", "which", "what", "when", "where", "would", "could",
    "there", "these", "those", "into", "only", "also", "such", "other", "more",
    "most", "some", "each", "over", "under", "after", "before", "about",
    "one", "two", "three", "out", "up", "down",
}


def vtokens(html):
    words = re.findall(r"[a-z]+", text(html).lower())
    return frozenset(w for w in words if len(w) > 3 and w not in STOP)


pairs = []
for qa, qb in combinations(QUESTIONS, 2):
    score = jac(vtokens(qa["passage"]), vtokens(qb["passage"]))
    pairs.append((score, qa["num"], qb["num"]))
    check(score < SAME_SUBJECT,
          f"{qa['num']} and {qb['num']} cover the same subject ({score:.2f})")
pairs.sort(reverse=True)
print(f"   {len(pairs)} pairs compared; closest:")
for sc, aa, bb in pairs[:6]:
    print(f"     {sc:.2f}  {aa}  vs {bb}")

print()
print(f"items: {len(QUESTIONS)}   key before balancing: "
      f"{dict(sorted(Counter(q['answer'] for q in QUESTIONS).items()))}")
if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for failure in FAIL:
        print("  -", failure)
    raise SystemExit(1)
print("\nALL CHECKS PASSED")
