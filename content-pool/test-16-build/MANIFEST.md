# Tests 16, 17 and 18 — build record

All three are **PUBLISHED** in production, 147 questions each. This file covers all three
builds; the Test 17 and Test 18 directories point back here.

| test | Math | R&W | reference template | thematic territory |
|---|---|---|---|---|
| Test 16 | `math_test16.py` | `rw_test16.py` | Test 13 | maritime shipping, textiles and dyeing, beekeeping, printing, glassmaking |
| Test 17 | `math_test17.py` | `rw_test17.py` | Test 11 | mountaineering and survey, dairying, railways, kilns, forestry |
| Test 18 | `math_test18.py` | `rw_test18.py` | Test 15 | aviation and ballooning, brewing, watchmaking, quarrying, orchards |

Every question is originally authored. No transcribed source material was used — those pools
were spent by Test 8.

## Shape

Per test: R&W 27/27/27 (Standard, M2 Easy, M2 Hard), Math 22/22/22 with exactly 19
multiple-choice + 3 free-response per module. Math domain spread is ALG 7 / ADV 6 / PSDA 5 /
GT 4 in every module of every test. R&W block quota is 14 reading + 13 writing, so the writing
block opens at question 15; the assembler sorts on block rank and re-checks that the rank
sequence is monotonic.

Difficulty follows the module, as Tests 1 and 2 do: an EASY module's questions are EASY, a HARD
module's are HARD. Math Module 1 is deliberately upper-medium — nearly every item makes a
constant, a rate or an unknown be recovered before it can be used. Module 2 Easy is strictly
one operation. Module 2 Hard works in parameters and structural answers.

## Build order

```
python3 verify_math_testN.py                          # four passes, exits non-zero on failure
python3 balance_rw.py                                 # -> rw_testN_balanced.json
python3 assemble_testN.py                             # -> testN.json
DATABASE_URL=<local>  node insert_test.mjs testN.json "Test N"
DATABASE_URL=<local>  node ../test-6-7-build/audit_math_rendering.mjs
DATABASE_URL=<prod>   node insert_test.mjs testN.json "Test N" --publish
DATABASE_URL=<prod>   node ../test-6-7-build/audit_math_rendering.mjs
```

`insert_test.mjs` is idempotent — an existing Test or Module is skipped rather than duplicated,
so a failed run can simply be re-run. It writes each question's own `difficulty` rather than
hardcoding `MEDIUM`, which is the defect that left Tests 3-6 misreporting their level.

## Dedupe corpora

- `../rw_authored_corpus.json` — 809 R&W passages: every authored pool from Tests 7-15 plus the
  transcribed October and August pools Tests 3-6 consumed.
- `prod_math_stems.json` — the 990 Math stems live in production at build time. Gitignored, as
  a derived snapshot; regenerate from the database if it is missing.

Both are screened with token-signature Jaccard, not exact matching, because a repeat with new
numbers is still a repeat.

## What the verifiers actually check

`verify_math_testN.py`, four passes:

1. **Independent sympy re-derivation** of the answer from the question itself, never from the
   `check` note — a wrong `check` and a wrong key agree with each other. Also asserts no
   distractor equals the derived value. Coverage: 65/66, 65/66 and 64/66; the rest are prose-choice
   interpretation items listed in `MANUAL` with a written justification.
2. **House style** on all stems and choices, `<img>` stripped first because base64 payloads match
   every pattern. No bare `^`, `sqrt(`, `*`-as-multiply, slash fractions, `!=`/`<=`/`>=`,
   spelled-out Greek, or LaTeX macro outside a math span; escaped `\cos`/`\sin`; no prose inside
   math mode; any stem naming a table/graph/figure must carry real markup.
3. **Template dedupe** against production at a 0.75 threshold.
4. **Self-collision** among the test's own 66 questions.

R&W has no equivalent script; it was checked directly — block counts, non-empty rationales, no
rationale naming an option by letter, four distinct choices with the key in ABCD, no choice
without a letter or digit, balanced table markup, the literal five-underscore blank.

## Results

| | Test 16 | Test 17 | Test 18 |
|---|---|---|---|
| highest Math Jaccard vs production | 0.67 | 0.62 | 0.57 |
| highest Math Jaccard internal | 0.37 | 0.42 | 0.42 |
| highest R&W Jaccard vs corpus | 0.24 | 0.31 | 0.16 |
| R&W key before balancing | A45 B22 C13 D1 | A42 B29 C9 D1 | A70 B8 C3 D0 |
| R&W key after balancing | 21/20/20/20 | 21/20/20/20 | 21/20/20/20 |
| rationales locked by letter-naming | 0 | 0 | 0 |
| topics dropped as collisions | 29 | 23 | 19 |

Cross-sibling overlap, the check the per-test production pass cannot make because the siblings
are not shipped yet: Math peaks at 0.56 (T16/T17), R&W passages at 0.18 (T17/T18).

## Questions rewritten rather than accepted

- **Test 16** — the first `H2H-01` scored 0.82 against Test 11: an independently reinvented
  "two loading constraints, find k so no pair satisfies both", a template already banked eight
  times over. The first `H2E-22` scored 0.81 against Test 14's guy-wire item.
- **Test 17** — the first `H2H-09` scored 0.76 against Test 10's "parabola tangent to a line".
- **Test 18** — **nine** questions scored *below* the threshold and were still genuine template
  repeats when the nearest banked stem was read: a linear `f(x+3)−f(x)`, a guy-wire Pythagoras,
  a shadow similar-triangles, a "no solution, find k" system, a circle-equation radius, a
  triangle third angle, a circle circumference, a cube volume, a composed-function chain.
- **Test 16 R&W** — three items were rewritten despite scoring well under threshold because the
  *template* was a clone rather than the wording: the first `F3` reproduced Test 11's and Test
  13's `F3` move for move on a silting harbour, and `F1` echoed Test 15's "neither the curator
  nor the two conservators" frame.

## Two findings worth carrying forward

**A similarity number decides what to read, not what to accept.** Test 18's nine sub-threshold
repeats are the evidence. Read every match above roughly 0.45.

**Check settings across modules, not just stems.** Two Test 18 Module 2 Easy items had
genuinely distinct maths from their Module 1 counterparts — a rational equation against an
exponential evaluation, a two-step rate recovery against a one-step evaluation — but reused
their settings. A student sees Module 1 plus one Module 2 branch, so the Easy branch would have
shown the same hop kiln and the same sundial twice. Reskinned to an airship mooring line and a
fermenting wort; internal similarity fell from 0.53 to 0.42.

## Post-publish state, read back from production

18 tests, all PUBLISHED at 147 questions, 2,646 questions total. Per-question difficulty matches
module difficulty at 882/882/882 across STANDARD/EASY/HARD. Every multiple-choice question
carries exactly one key; all free-response answers are JSON-array encoded; no answer choice
lacks a letter or digit; the DB-wide rendering audit is clean over all 1,188 Math questions.

## Known gaps

No `Explanation` rows, consistent with every test from Test 1 on. No question carries an image —
all figures are real `<table>` markup, because the authoring agents could not produce diagrams.
Geometry items are therefore worded to be fully determined without a picture.
