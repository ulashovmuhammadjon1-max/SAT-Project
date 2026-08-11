#!/usr/bin/env python3
"""
Screen the 81 authored Reading & Writing items for Test 27.

Five passes. The third and fourth are the ones that matter, and they look for
different failures:

 3. AGAINST THE CORPUS — ../rw_authored_corpus.json, 1,295 passages, READ ONLY.
    Reject at 0.50, print everything at or above 0.45 so the nearest banked
    passage can be read and judged rather than waved through by a number.

 4. AGAINST ITSELF — every one of the 3,240 pairs among the 81 passages, using
    the EXACT tokenizer and threshold that ../validate_tests.py applies
    (0.24, stopword-filtered, words longer than three characters). This is the
    pass Test 23 needed and did not have: it had the lowest corpus overlap of
    any build, 0.14, and still failed on fifteen same-subject pairs internally.
    Because the assembler deals blocks to modules at random, ANY pair here can
    end up as an M1-to-M2 pair that one student meets, so every pair is checked
    rather than only the ones a particular deal would expose.

Pass 5 covers the harness traps: no `T21` provenance string surviving from the
scaffolding this build was copied from, no rationale naming an option by
letter (which would lock the question against balance_rw.py), no answer choice
that renders as an empty row, a raw degree glyph where `&deg;` belongs, and
unbalanced inline tags. Tag counting uses `<u>`/`</u>` with the closing angle
bracket required, because `<u` also matches `<ul` — the false-positive that
produced nine bogus findings in an earlier build.

Run:  python3 check_rw27.py
"""
import json
import os
import re
import sys
from collections import Counter
from itertools import combinations

from rw_test27 import QUESTIONS
from balance_rw import names_a_letter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CORPUS = os.path.join(ROOT, "rw_authored_corpus.json")

FAIL = []
def bad(msg):
    FAIL.append(msg)


# ------------------------------------------------------------------ tokenizer
# Lifted verbatim from validate_tests.py so this screen and the external
# validator cannot disagree about what "the same subject" means.
_PASSAGE_STOP = set("""
about above after again against because been before being below between both
cannot could does doing down during each even ever every from further have
having here hers herself himself into itself just more most much must myself
only other ours ourselves over same should some such than that their theirs
them themselves then there these they this those through under until very were
what when where which while will with would your yours yourself yourselves
""".split())


def _tokens(html):
    words = re.findall(r"[a-z]+", re.sub(r"<[^>]+>", " ", html).lower())
    return frozenset(w for w in words if len(w) > 3 and w not in _PASSAGE_STOP)


def jac(a, b):
    ta, tb = _tokens(a), _tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


# ---------------------------------------------------------------- pass 1: shape
print("== pass 1: block counts and item shape")
WANT = {"Words in Context": 15, "Text Structure and Purpose": 6,
        "Central Ideas and Details": 6, "Command of Evidence": 9, "Inferences": 6,
        "Boundaries": 12, "Form, Structure, and Sense": 9, "Transitions": 9,
        "Rhetorical Synthesis": 9}
got = Counter(q["skill"] for q in QUESTIONS)
for block, want in WANT.items():
    if got[block] != want:
        bad(f"block {block}: {got[block]} items, the assembler quota needs {want}")
extra = set(got) - set(WANT)
if extra:
    bad(f"unexpected blocks: {sorted(extra)}")
if len(QUESTIONS) != 81:
    bad(f"{len(QUESTIONS)} items, expected 81")
nums = [q["num"] for q in QUESTIONS]
dupe = [n for n, c in Counter(nums).items() if c > 1]
if dupe:
    bad(f"duplicate item ids: {dupe}")
for q in QUESTIONS:
    if len(q["choices"]) != 4:
        bad(f"{q['num']}: {len(q['choices'])} choices")
    if q["answer"] not in "ABCD":
        bad(f"{q['num']}: answer {q['answer']!r}")
    if not (q.get("why") or "").strip():
        bad(f"{q['num']}: no rationale, so nothing verifies the key")
    if len(set(q["choices"])) != 4:
        bad(f"{q['num']}: two answer choices are identical")
print(f"   {len(QUESTIONS)} items   {dict(sorted(got.items()))}")

# ------------------------------------------------------- pass 2: house style
print("== pass 2: house style")
for q in QUESTIONS:
    html = (q.get("passage") or "") + " " + q["stem"] + " " + " ".join(q["choices"])
    if "°" in html:
        bad(f"{q['num']}: raw degree glyph; CLAUDE.md requires &deg;")
    if re.search(r"(?<![\w*])\*(?!\*)[^*]+\*(?![\w*])", html):
        bad(f"{q['num']}: markdown asterisks; italics must be <em>")
    for tag in ("u", "em", "strong", "ul", "li", "table", "tr"):
        # `<u` also matches `<ul`, so the closing bracket is required on the
        # opening tag too. A boundary-free substring match here is worse than
        # no check at all.
        op = len(re.findall(rf"<{tag}(?:\s[^>]*)?>", html))
        cl = len(re.findall(rf"</{tag}>", html))
        if op != cl:
            bad(f"{q['num']}: {op} <{tag}> vs {cl} </{tag}>")
    for c in q["choices"]:
        if not re.search(r"[A-Za-z0-9]", c):
            bad(f"{q['num']}: an answer choice renders as an empty row: {c!r}")
    if q["skill"] == "Words in Context" and "most nearly mean" not in q["stem"]:
        if "_____" not in (q.get("passage") or ""):
            bad(f"{q['num']}: a fill-in Words in Context item with no literal _____ blank")
    if q["skill"] in ("Boundaries", "Form, Structure, and Sense", "Transitions"):
        if "_____" not in (q.get("passage") or ""):
            bad(f"{q['num']}: a writing item with no literal _____ blank")
    if q["skill"] == "Rhetorical Synthesis" and "<ul>" not in (q.get("passage") or ""):
        bad(f"{q['num']}: synthesis notes are not real <ul><li> markup")
print(f"   {len(QUESTIONS)} items style-checked")

# ---------------------------------------------------- pass 3: against the corpus
print("== pass 3: passage dedupe against the shared corpus")
rows = json.load(open(CORPUS))
print(f"   comparing against {len(rows)} banked passages ({CORPUS})")
bank = [(f"{r.get('src')}:{r.get('num')}", r.get("passage") or "") for r in rows]
scored = []
for q in QUESTIONS:
    p = q.get("passage") or ""
    best, lab = max(((jac(p, t), l) for l, t in bank), key=lambda z: z[0])
    scored.append((best, q["num"], lab))
    if best >= 0.50:
        bad(f"{q['num']}: passage similarity {best:.2f} to {lab}")
scored.sort(reverse=True)
worst_corpus = scored[0][0]
flagged = [r for r in scored if r[0] >= 0.45]
print(f"   {len(flagged)} at or above 0.45 — read each one:")
for sc, num, lab in flagged:
    print(f"     {sc:.2f}  {num}  vs {lab}")
print("   next closest:")
for sc, num, lab in [r for r in scored if r[0] < 0.45][:8]:
    print(f"     {sc:.2f}  {num}  vs {lab}")

# ------------------------------------------------- pass 4: against itself
print("== pass 4: within-test same-subject pairs (validate_tests.py rules)")
THRESH = 0.24
pairs = []
for a, b in combinations(QUESTIONS, 2):
    pa, pb = a.get("passage") or "", b.get("passage") or ""
    if not pa or not pb:
        continue
    sc = jac(pa, pb)
    pairs.append((sc, a["num"], b["num"]))
    if sc >= THRESH:
        bad(f"{a['num']} and {b['num']} cover the same subject ({sc:.2f}); "
            "the assembler could put them in Module 1 and a Module 2 branch")
pairs.sort(reverse=True)
worst_self = pairs[0][0]
print(f"   {len(pairs)} pairs compared; closest:")
for sc, x, y in pairs[:8]:
    print(f"     {sc:.2f}  {x}  vs {y}")

# ------------------------------------------------------------ pass 5: traps
print("== pass 5: harness traps")
lettered = [q["num"] for q in QUESTIONS if names_a_letter(q.get("why", ""))]
if lettered:
    bad(f"rationales naming an option by letter (balance_rw.py cannot rotate these): {lettered}")
src = open(os.path.join(HERE, "rw_test27.py")).read()
stray = re.findall(r"T21", src)
if stray:
    bad(f"{len(stray)} 'T21' provenance strings survive from the Test 21 scaffolding")
keys = Counter(q["answer"] for q in QUESTIONS)
print(f"   0 letter-naming rationales, 0 stray T21 strings")
print(f"   raw key distribution (before balancing): {dict(sorted(keys.items()))}")

print()
print(f"highest Jaccard vs corpus: {worst_corpus:.2f}   worst within-test pair: {worst_self:.2f}")
if FAIL:
    print(f"\n{len(FAIL)} FAILURES:")
    for f in FAIL:
        print("  -", f)
    sys.exit(1)
print("\nALL CHECKS PASSED")
