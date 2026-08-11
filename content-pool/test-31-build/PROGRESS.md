# Test 31 — build progress

Territory: poultry and egg grading, dovecotes, falconry and mews, decoy ponds,
eel traps and fish ponds. Structural template: `content-pool/test-19-build/`.

## Status

| step | state |
|---|---|
| `math_test31.py` (66 items) | DONE |
| `verify_math_test31.py` — 4 passes + choice-order rule | PASSING |
| hand-audit of all 66 stems against their derivations | DONE — 0 wrong answers |
| `mechanism_search.py` | DONE — 4 real repeats found, all replaced |
| `katex_check.mjs` | PASSING — 52 spans, 0 failures |
| `rw_test31.py` (81 items) | DONE |
| `verify_rw_test31.py` — 5 passes (NEW this run) | PASSING |
| F4 | verified correct; its rationale was already consistent |
| `balance_rw.py` | DONE — A21/B20/C20/D20 |
| `assemble_test31.py` | DONE — also re-balances each module's key to 7/7/7/6 |
| `test31.json` | DONE — 147 questions |
| `../validate_tests.py 31` | PASSING — zero problems |
| local DB insert + `audit_math_rendering.mjs` | DONE — 147 rows, audit clean |
| `MANIFEST.md` | DONE |

## Decisions a successor would otherwise have to re-derive

- `F4` is an **R&W** item (`rw_test31.py`, Form/Structure/Sense), not a Math
  item. The handover called it Math; it is not. Its "neither ... nor" proximity
  rationale reads correctly and was left alone.
- `verify_math_test31.py` was ALREADY passing when this run started, and every
  one of its 66 derivations models its stem independently. **No incorrect Math
  answer exists in this test — 0 of 66.** What the run found instead:
  - **9 items listed numeric answer choices out of order** (M1-04 read 1,299 /
    1,300 / 1,310 / 1,301). No sibling test does this — 85 purely numeric items
    across Tests 19 and 21, none out of order. Cause: the key LETTER was being
    picked for balance instead of the distractor VALUES. All 9 sorted; balance
    bought back by retuning distractors on 6 items; the verifier now enforces
    ascending order so it cannot come back.
  - **4 genuine template repeats, every one found by mechanism search and none
    by Jaccard**: M2E-21 = Test 5 M2E Q20 (cylinder r=3 h=10, scored 0.48);
    M2E-22 = Test 12 M2H Q18 (triangle XYZ, right angle at Y, legs 9 and 40);
    M2H-21 = Test 16 M2H Q21's ratio 8/17 AND hypotenuse 51, with Test 19 M2H
    Q21's ask; M2H-19 = Test 9 M2H Q21 with different percentages. All four
    replaced. The first drafted REPLACEMENT for M2E-22 was itself a repeat
    (Test 12 M2E Q22 already gives two legs and asks for tan) and was caught by
    pre-screening it before writing — always pre-screen the replacement.
- R&W defects found and fixed: **F8** choice C ended in "the" against a passage
  resuming "the gunner" → "with his hands the the gunner", exactly the sibling
  build's defect; **B1**'s four choices did not fill the blank consistently (two
  put the mark before the word, rendering "a goose ; simply lost"); **B7** had
  two defensible answers ("cadger:" is legal English); **B12** was the fifth of
  twelve Boundaries items answering with a full stop, and the set had no
  relative-clause comma; **B8** retold T5's decoy screens (0.22 on the
  same-subject tokenizer) and was moved to the loft trap; **W15**'s rationale
  rebutted the weakest distractor rather than "custom".
- Corpora at the content-pool ROOT are READ ONLY: `../prod_math_stems.json`
  (1,386), `../rw_authored_corpus.json` (1,295).
- `assemble_test19.py` is still present and is NOT this test's assembler. Use
  `assemble_test31.py`, which asserts no `T19` string survives into the JSON.
- Numbers worth keeping: highest Math Jaccard vs production 0.73; highest inside
  Test 31, 0.54. Highest R&W corpus similarity 0.21; highest same-subject pair
  inside the test 0.16 (validate_tests.py rejects at 0.24).

## Complete

Every step above passes. Nothing is outstanding. Full write-up in `MANIFEST.md`.
Not done and not attempted: opening the questions in `/exam/{attemptId}`.
Production untouched; no git commit.
