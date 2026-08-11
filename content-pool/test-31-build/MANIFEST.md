# Test 31 — build manifest

147 questions: R&W 27/27/27 (Module 1 Standard, Module 2 Easy, Module 2 Hard),
Math 22/22/22 (19 MC + 3 FR each). Every question is originally authored.

**Territory**: poultry and egg grading, dovecotes and pigeon lofts, falconry and
the mews, decoy ponds and wildfowling, eel traps and fish ponds.
**Structural template**: `../test-19-build/`.

## Files

| file | what it is |
|---|---|
| `math_test31.py` | 66 authored Math questions, 3 modules |
| `verify_math_test31.py` | 4 passes + the choice-order rule; **must exit 0** |
| `katex_check.mjs` | typesets all 52 math spans with the exam's own KaTeX |
| `mechanism_search.py` | asks what mathematical MOVE a stem makes, and counts how many banked stems make it |
| `rw_test31.py` | 81 authored R&W items, one sub-topic each |
| `verify_rw_test31.py` | 5 passes, written this run; **must exit 0** |
| `balance_rw.py` | evens the 81-item pool → `rw_test31_balanced.json` |
| `assemble_test31.py` | deals the modules, re-balances each module's key, writes `test31.json` |
| `test31.json` | the 147 rows the inserter writes |
| `insert_test.mjs` | inserter (`--publish` to publish) |
| `PROGRESS.md` | running state, kept current in case the session is killed |

`assemble_test19.py` is still in this directory and is **not** this test's
assembler. `assemble_test31.py` fails the build if the string `T19` survives
anywhere in the assembled JSON.

## Build order

```
python3 verify_math_test31.py           # must pass
node katex_check.mjs                    # after the verifier writes math_spans.json
python3 verify_rw_test31.py             # must pass
python3 balance_rw.py
python3 assemble_test31.py
python3 ../validate_tests.py 31         # must pass, zero problems
service postgresql start
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/sat_platform?schema=public' \
  node insert_test.mjs test31.json "Test 31"
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/sat_platform?schema=public' \
  node ../test-6-7-build/audit_math_rendering.mjs
```

Status: all of the above pass. Inserted into **local dev only**, as DRAFT
(`aa5bba96-1c61-4617-a2a2-8350e84b2a58` on the local database — production was
not touched). The DB-wide math rendering audit reports 0 errors across all
1,914 Math questions in 29 local tests.

## What the first full verification of this test found

The Math had never been verified end to end before this run.

**Wrong answers: none.** All 66 answers were re-derived with sympy from the
question itself — 66/66, nothing in MANUAL — and every derivation was then read
by hand against its stem to confirm it models the question rather than quoting
the author's `check` note. Every distractor is asserted to differ from the
derived value. Two questions key something that is not a value (a prose
comparison of two data sets, and an ordered pair); for those the derivation
evaluates all four printed claims and asserts exactly one is true.

**What was wrong instead — four classes:**

1. **Nine items listed their numeric answer choices out of order.** M1-04 read
   1,299 / 1,300 / 1,310 / 1,301. The cause was choosing the key LETTER to
   balance the answer key rather than choosing the distractor VALUES. No sibling
   build does this: across Tests 19 and 21, 85 purely numeric MC items, none out
   of order. All nine sorted; the balance was bought back by retuning
   distractors on six items, and every module now keys 5/5/5/4.
   `verify_math_test31.py` now enforces ascending numeric choices, exempting
   anything symbolic, an ordered pair, an inequality or prose, which have no
   canonical order.

2. **Four genuine template repeats, all four found by mechanism search and none
   by the Jaccard screen:**

   | item | repeated | Jaccard |
   |---|---|---|
   | M2E-21 | Test 5 M2E Q20 — cylinder, radius 3, height 10, volume | 0.48 |
   | M2E-22 | Test 12 M2H Q18 — triangle XYZ, right angle at Y, legs 9 and 40 | below 0.45 |
   | M2H-21 | Test 16 M2H Q21 — the same ratio 8/17 **and** the same hypotenuse 51; and Test 19 M2H Q21's ask (area) | 0.65 |
   | M2H-19 | Test 9 M2H Q21 — radius up and height down by stated percentages | 0.40 |

   Replacements: a trapezium area, a leg recovered from a cosine and the
   hypotenuse, a hypotenuse recovered from a tangent and a leg, and a
   displacement volume (a mechanism with zero instances in the 1,386-stem bank).
   The three trigonometry items now use the disjoint triples 12-35-37, 20-21-29
   and 33-56-65, none of which any banked trigonometry question uses.

   **The transferable lesson: pre-screen the REPLACEMENT before writing it.**
   The first replacement drafted for M2E-22 gave two legs and asked for tan —
   which is Test 12 M2E Q22. The same search that found the repeat rejected its
   obvious successor.

3. **R&W: six defects.**
   - **F8** choice C ended in the word "the" and its passage resumes "the
     gunner", so it rendered as "with his hands the the gunner" — exactly the
     defect a sibling build shipped ("yet the the custom"). Found by
     substitution, which is now pass 2 of `verify_rw_test31.py`.
   - **B1**'s four choices did not fill the blank consistently: two put the mark
     *before* the word, rendering "a goose ; simply lost". Rewritten as a
     subject-verb separation item.
   - **B7** had two defensible answers — "cadger:" is legal English, a complete
     statement followed by a colon introducing an elaboration, alongside the
     keyed comma-plus-conjunction. The colon option was replaced.
   - **B12** was the fifth of twelve Boundaries items whose answer is a full
     stop, and the set contained no relative-clause comma at all. Rewritten as
     one.
   - **B8** retold the decoy-pipe screens that T5 already describes: 0.22 on
     `validate_tests.py`'s own same-subject tokenizer, under its 0.24 gate but
     plainly the same scene twice. Moved to the loft trap. The highest
     same-subject pair inside the test is now 0.16.
   - **W15**'s rationale rebutted "rehearsal" when the distractor a student
     actually weighs is "custom".

   `F4`, which the handover flagged, is an **R&W** item, not a Math one, and its
   "neither ... nor" proximity rationale reads correctly and consistently. It
   needed no change.

4. **The answer key was even across the pool and uneven inside each module.**
   `balance_rw.py` evens the 81-item pool (A21/B20/C20/D20), but the assembler
   then deals that pool into three modules at random, and the first deal put B
   on 12 of Module 1's 27 questions — worse than any module in Tests 19, 20, 21
   or 30, which top out at 9. A student sits ONE module, so the module is the
   unit that must be balanced. `assemble_test31.py` now re-balances each module
   to 7/7/7/6 by rotating choices, shuffling the target letters rather than
   dealing them round-robin (which balances perfectly and leaves a visible
   repeating pattern down the key) and rejecting runs of four.

## Numbers

- Math: 66/66 sympy-derived, 0 in MANUAL. Highest template similarity to the
  1,386 live stems **0.73**; highest inside Test 31 **0.54**; 31 matches at or
  above 0.45, all read.
- Math key: 5/5/5/4 in each of the three modules. 52 KaTeX spans, 0 failures.
- R&W: highest similarity to the 1,295-passage corpus **0.21** — nothing reached
  even the 0.45 read line. Highest same-subject pair inside the test **0.16**
  (rejected at 0.24). 196 choice substitutions read back. 0 rationales name an
  option by letter.
- R&W key: A21/B20/C20/D20 across the pool, 7/7/7/6 in every module.

## Not verified

The questions were not opened in the exam interface (`/exam/{attemptId}`). Every
static check the pipeline has was run — including the DB-wide rendering audit
against the inserted rows and a KaTeX typeset of every math span — but nothing
was screenshotted in the student view.

Production was not touched: no production insert, no publish, no git commit.
