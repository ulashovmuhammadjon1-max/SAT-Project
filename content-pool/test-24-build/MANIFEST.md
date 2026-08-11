# Test 24 — build record

147 originally-authored questions: R&W 27/27/27, Math 22/22/22 (19 MC + 3 FR per Math module).
Inserted into the **local** database as `DRAFT` (`Test 24`, local id
`f4d1ce52-8a32-4a8b-ba5f-8b7493cea77f`). **Not published, and production was never touched** —
this session had no production `DATABASE_URL`.

| | |
|---|---|
| structural template | `../test-18-build/` |
| Math thematic territory | the rope and canvas trades |
| corpora (READ ONLY, at the content-pool root) | `../prod_math_stems.json` 1,386 Math stems; `../rw_authored_corpus.json` 1,295 R&W passages |

## Territory, and how it is split across the adaptive boundary

A student sees Module 1 and exactly one Module 2 branch, so a setting used on both sides of that
boundary shows the same scene twice in one sitting. The Math territory is therefore divided:

| | settings |
|---|---|
| Math Module 1 | ropewalks and cordage, hemp dressing and hackling, twine spinning, strand and hawser laying, the tar kettle |
| Math Module 2 (both branches) | net making and mesh gauges, sailmaking lofts, canvas and tarpaulin, rigging, splices, blocks and thimbles |

`verify_math_test24.py` pass 4 enforces the split, and it also asserts the reverse direction
(no Module 2 keyword in Module 1 and none of Module 1's in Module 2). Result: **0 shared
keywords**, 10 keywords in Module 1 and 11 in Module 2.

Deliberately kept off Test 16's maritime/textile ground — no ships, voyages, cargo, looms,
weaving or cloth mills anywhere in the test — and off Test 30's physic-garden list.

## Results

| | |
|---|---|
| highest Math Jaccard vs production | **0.70** (`H2H-11` vs Test 2 M1S Q16) |
| highest Math Jaccard internal | **0.62** (`H2E-08` vs `H2E-09`) |
| sympy coverage | **66/66** |
| `MANUAL` items | **0** |
| highest R&W Jaccard vs corpus | **0.250** (`R5` vs `rw_test8:R4`) |
| highest R&W Jaccard internal | **0.378** (`C4` vs `R6`) |
| R&W items flagged (≥0.50 Jaccard or ≥3 shared 5-grams) | **0** |
| R&W key before balancing | A 81, B 0, C 0, D 0 |
| R&W key after balancing | **21 / 20 / 20 / 20** |
| rationales locked by letter-naming | **0** |
| Math questions rewritten as template repeats | **17** (2 of them twice) |
| R&W topics dropped as collisions before drafting | **12** |

Math answer key per module (19 MC each): M1 A4 B6 C4 D5 · M2E A4 B6 C6 D3 · M2H A4 B6 C4 D5.
Domain mix is 7 ALG / 6 ADV / 5 PSDA / 4 GT in every Math module, with 1 GT-TR item each.

R&W block order verified programmatically, not by eye: the block-rank sequence is monotonic in
all three modules and the writing block opens at question 15 in each, with 14 reading and 13
writing questions per module.

## Verification that was run and passed

```
python3 verify_math_test24.py          # 4 passes, exits non-zero on any finding
python3 check_originality.py ngrams    # R&W dedupe + structural checks
python3 balance_rw.py
python3 assemble_test24.py
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/sat_platform?schema=public' \
  node insert_test.mjs test24.json "Test 24"
DATABASE_URL='...localhost...' node ../test-6-7-build/audit_math_rendering.mjs   # exit 0
```

The DB-wide audit came back **clean over 1,320 Math questions across 20 tests**, Test 24
included. Post-insert SQL checks: 6 modules, 147 questions, every MC question with exactly one
key, every `correctAnswerFR` a JSON array, every R&W question with a passage, no answer choice
without a letter or digit, `Question.order` contiguous from 1 in every module, no raw degree
glyph, per-question difficulty matching module difficulty in all six modules.

Every one of the **69 KaTeX spans** in the test was additionally pushed through the app's own
render path (`katex.renderToString` with the same options `renderMathContent` uses in
`src/components/shared/math-content.tsx`) — **0 produced a `katex-error` node**.

## What was NOT verified

**The test was not loaded in the real exam interface.** CLAUDE.md asks for a
`/exam/{attemptId}` screenshot pass, and that was not possible here: no Playwright browsers are
installed in this container (`~/.cache/ms-playwright` is absent) and installing them was out of
scope for a local-only DRAFT insert. The KaTeX render pass above exercises the same function the
exam page calls, so a malformed span would have shown up, but the visual layout of the tables and
the `<br/>`-stacked system in `H2H-01` has not been seen rendered. That is the one check left
open, and it is worth doing before this test is ever published.

## The finding this build adds: read below 0.45 when the *phrasing* is boilerplate

The standing rule — a similarity threshold decides what to READ, not what to accept — held again,
and sharpened. Of the 17 Math questions rewritten as genuine template repeats, **13 scored below
the 0.75 reject line**, and the interesting part is the tail:

| item | score | what it actually was |
|---|---|---|
| `H2E-12` | 0.92 | `f(x)=7x-6`, find `f(4)` — Test 5 M2E Q3 is `f(x)=9x+4`, find `f(3)` |
| `H2H-20` | 0.86 | DE ∥ BC with AD/DB/DE given — Test 9 M2H Q18, same three quantities |
| `H2E-21` | 0.80 | two angles of a triangular **sail**, find the third — Test 8 M2E Q19, same setting |
| `H2H-01` | 0.70 | system with a constant, no solution — Test 6 M1S Q3, same template |
| `H2E-19` | 0.53 | rectangle 14 by 9, find the area — Test 8 M2E Q20 uses **the same two numbers** |
| `H2E-20` | 0.56 | rectangular box volume — Test 15 M2E Q21 is 4 × 3 × 5 to my 4 × 3 × 2 |
| `H1-22` | 0.46 | corresponding angles `(4x+15)` / `(6x-25)` on a **stay** crossing two parallels — Test 20 M2H Q19 is the same sentence with different coefficients |
| `H2E-01` | **0.44** | "uses the equation `8n+17=121` to find the number n of …" — Test 16 M2E Q6 is "uses the equation `14p+35=203` to work out the number p of panels" |
| `H2E-04` | **0.44** | same, `5(t-3)=40` |

The last two matter most. They sat **below the 0.45 read threshold**, in the "next closest" list
the verifier prints only as a courtesy, and they are the most literal repeats in the whole set —
identical stem *phrasing*, identical template, different numbers. They scored low because the
setting nouns differ ("panels" vs "meshes") and because the signature normalises every number to
`#`, which throws away exactly the thing that distinguishes them.

**Practical rule for the next build: print the top ~10 below the threshold as well, and read them
whenever the stem uses a stock phrasing frame** ("uses the equation X to find the number of Y",
"what is the value of f(k)", "what is the area of the rectangle"). Those frames are where the
bank is most saturated and where Jaccard is least able to see it.

Second observation, more structural: **Module 2 (Easy) is where the bank is exhausted, not
Module 2 (Hard).** 12 of the 17 rewrites were easy items. A one-step question has almost no room
to be original — the skill *is* the template — so the freshness has to come from choosing a
less-worked corner of the same skill. Screening before writing found several such corners with
**zero** precedent in 1,386 stems: factoring out a greatest common factor, a monomial × monomial
product, expanding a product of two binomials, the mode of a list, and a quadrilateral's angles
given as a ratio. All five were used. Templates that came back saturated and were avoided:
median of a short list (14), rectangular-prism volume (15), cube volume or edge (12), completing
the square / vertex form (11), triangle third angle (7), circumference (6).

## Traps that were live in this build

- **The `_ref` prefix.** Scaffolding from Test 18 has two different provenance tags — the Math
  one `AUTHORED/T18-` and the R&W one `AUTHORED-T18:` — and a substitution keyed on the hyphen
  updates only the first. Both were updated, and the verifier asserts no `T18` or `Test 18`
  string survives in any question; `test24.json` contains zero occurrences of `T18`.
- **Word boundaries in the checker.** The cross-module setting check lists `tarpaulin` and
  `tar kettle` **separately**, because a bare `tar` prefix matches both and would have reported a
  false collision between Module 1's tar kettle and Module 2's tarpaulin. `net`, `knot`, `yarn`,
  `line` and `block` were dropped as keywords entirely — all have everyday senses, and a
  boundary-free substring match in a checker is worse than no check.
- **`latex_to_expr` rewrite order.** The exponent and fraction rewrites alternate in a loop to a
  fixed point rather than running in a fixed order. Surviving multi-letter runs are split into
  implicit products, which is what makes `\frac{pq}{p+q}` in `H2H-09` parse as a product instead
  of a symbol named `pq`. One rule had to be **added** for this build: an implicit `*` between a
  closing parenthesis and a following letter, without which `\(5a^{3}\sqrt{2a}\)` in `H2H-11`
  fell through to a string comparison and reported a false failure.
- **Two answer choices both correct.** The first draft of Boundaries item `B10` offered a dash
  and a comma before an appositive phrase; both are correct English. It was rewritten so the
  material after the blank is a complete statement, which makes the semicolon the only fit.
- **Transition choices written as full clauses.** Two Transitions items (`N3`, `N7`) were first
  drafted with options that repeated the words after the blank, so every choice produced a
  doubled clause. Caught by reading the assembled sentence, not by any check — worth adding a
  check that concatenates passage and choice and looks for a repeated bigram.
- **A raw `<` outside a math span** is invalid HTML, but `&lt;` *inside* one is worse: the exam
  page pulls math out of the raw string with a regex before anything is parsed as HTML, so KaTeX
  would receive the literal ampersand. Two production questions (Test 5 M2H Q11, Test 6 M2H Q12)
  have that defect today. `H2E-05` writes its inequality as `\(4w+5<33\)`, and pass 2 now checks
  both directions.

## R&W

All 81 items authored. Fifteen subject territories, chosen after screening the 1,295-passage
corpus: ropewalks and cordage, sailmaking lofts and canvas, wire rope and bridge cable spinning,
netting and mesh in engineering, the mathematics of knots, fibre science and tensile strength,
bookbinding and sewn structures, eyewitness memory, mycorrhizal networks, braille and tactile
reading, lava flow behaviour, antibiotic resistance, machine translation and corpus linguistics,
the dating of cave art, hoisting gear and safety brakes.

Twelve candidate topics were dropped **before drafting** rather than paraphrased around: the Inca
khipu (already `rw_test10/W3`), the chip log and its knotted line (`rw_test16/T2`), carpet knot
counts (`rw_test12/W8`), cellulose decay in paper and timber (`rw_test16/E4`, `I2`), spider
dragline silk, lichen symbiosis (12 corpus passages), origami folding (14), urban tree canopy
(13), hydrothermal vents (7), ice cores (6), salt marshes and estuaries (9), beaver dams (27).

Three items were retopiced *after* drafting because they duplicated a sibling item of my own
rather than anything banked: `R6` (was a second braille passage overlapping `W9` by three
5-grams), `R7` (was a second lava-tube passage at 0.476 against `C5`), and `M2` (had followed
`R7` onto the hoist brake). Internal worst fell from 0.476 to 0.378.

Every rationale names options by their **content**, so `balance_rw.py` rotated all 81 and none
was locked. Boundaries options always repeat the words on either side of the blank, so no choice
renders as an empty row.

## Files

| file | what it is |
|---|---|
| `math_test24.py` | the 66 Math questions, three modules, LaTeX typed by hand |
| `verify_math_test24.py` | 4 passes; exits non-zero on any finding |
| `rw_test24.py` | the 81 R&W items with a `why` on every one |
| `check_originality.py` | R&W topic screen (`keywords`) and finished-pool dedupe (`ngrams`) |
| `screen.py` | pre-screen one candidate idea against either corpus before writing it |
| `balance_rw.py` | rotates the R&W key to 21/20/20/20 |
| `assemble_test24.py` | deals the R&W quota, sorts on block rank, emits `test24.json` |
| `insert_test.mjs` | idempotent inserter; writes `q.difficulty` through, `--publish` to publish |
| `test24.json` | exactly what was inserted |
| `rw_test24_balanced.json` | the key-balanced R&W pool the assembler reads |

## Known gaps

No `Explanation` rows, consistent with every test from Test 1 onward. No images: every figure is
real `<table>` markup, and the geometry items are worded so they are fully determined without a
picture.

---

# Repair pass — same-subject R&W passages a single student would meet twice

`validate_tests.py 24` reported **eight** pairs of R&W passages covering one subject where a
single student sees both sides. A student takes Module 1 plus exactly one Module 2 branch, so
M1↔M2E and M1↔M2H pairs count, as does any pair inside one module; only M2E↔M2H is safe. The
original build screened R&W topics against the 1,295-passage corpus and against its own pool for
*duplication*, but never asked whether two different questions on the same subject could land on
the same side of the adaptive boundary — and the pool is organised one topic per block, so the
assembler's per-block deal spread each subject across all three modules by construction.

Test 24 is PUBLISHED in production. This repair changed the source, the assembled JSON and the
**local** database only; production was not touched.

## Which side of each pair was rewritten, and onto what

The writing-domain item was rewritten wherever a pair had one, because a Transitions, Rhetorical
Synthesis, Boundaries or Form/Structure/Sense passage exists to host a grammar or transition test
and its subject is incidental, whereas a reading passage is the substance of its own question.
Where both sides were writing items, the one whose rewrite also cleared a second near-threshold
pair was chosen. All eight replacements stay inside Test 24's territory — the rope and canvas
trades — and every one lands on a corner of it used nowhere else in the test.

| flagged pair | score | rewritten | why that side | new subject |
|---|---|---|---|---|
| RW_M2H Q8 (`C4`, Central Ideas) ↔ RW_M2H Q26 (`R6`, Rhet. Synthesis) | 0.38 | **`R6`** | writing item; `C4`'s braille passage is its own question's substance | retting and hackling hemp — why the soak is judged, not timed |
| RW_M1 Q5 (`W9`, Words in Context) ↔ RW_M2E Q22 (`N6`, Transitions) | 0.30 | **`N6`** | writing item | a rope's size stated round it vs straight across |
| RW_M1 Q23 (`N2`, Transitions) ↔ RW_M2E Q25 (`R2`, Rhet. Synthesis) | 0.30 | **`R2`** | both writing; rewriting `R2` also cleared `W2`↔`R2` at 0.204 | tarred against white (untarred) cordage |
| RW_M1 Q17 (`B9`, Boundaries) ↔ RW_M2H Q23 (`N5`, Transitions) | 0.28 | **`N5`** | both writing; rewriting `N5` also cleared `C3`↔`N5` at 0.220 | serving standing rigging with tarred twine against chafe |
| RW_M2H Q22 (`N8`, Transitions) ↔ RW_M2H Q27 (`R8`, Rhet. Synthesis) | 0.27 | **`N8`** | both writing; rewriting `N8` also cleared `F8`↔`N8` at 0.217 | new canvas shrinking the first time it is wetted |
| RW_M1 Q14 (`I4`, Inferences) ↔ RW_M2E Q23 (`N9`, Transitions) | 0.27 | **`N9`** | writing item; also cleared `F9`↔`N9` at 0.174 | a netmaker's flat gauge and even meshes |
| RW_M1 Q26 (`R9`, Rhet. Synthesis) ↔ RW_M2H Q3 (`W12`, Words in Context) | 0.27 | **`R9`** | writing item | a knotted join against a spliced one |
| RW_M1 Q16 (`B6`, Boundaries) ↔ RW_M2E Q21 (`F5`, Form/Structure) | 0.25 | **`F5`** | both writing; `F5` sits in a Module 2 branch, so its replacement has one fewer module to stay clear of | a tarpaulin lashed over open crates |

Each question still tests exactly what it tested before:

- **`N5`, `N8`** keep their consequence relation and their four unchanged options, so `As a
  result,` / `Accordingly,` remain the only fits and the concessive distractors remain wrong for
  the same reason.
- **`N6`** keeps its contrast relation (two conventions set against each other) and **`N9`** its
  concessive one (measures nothing, yet every mesh matches).
- **`F5`** keeps the tested structure exactly: singular head noun, a plural noun in the relative
  clause sitting nearer the blank, and a verb that must agree with the head — `A tarpaulin that is
  lashed down over several open crates **shields** …`.
- **`R2`** keeps the trade-off shape its goal depends on (one kind wins in one place and loses in
  another), so the key is still the only option combining both halves, and the "names a single
  winner" distractor still fails for the stated reason.
- **`R6`, `R9`** keep the one-option-only structure: the key supplies the causal chain or the
  trade-off, and the three distractors restate a single note, define a term, or restate the very
  practice the student was asked to explain.

`N6`'s arithmetic was checked: a three-inch circumference is 3/π ≈ 0.955 inches across, so "just
under an inch" is right. `N6` deliberately avoids the word *diameter* so it shares no vocabulary
with `E8`'s sheave table in Module 1.

## Results after the repair

| | before | after |
|---|---|---|
| `validate_tests.py 24` | FAIL, 8 same-subject pairs | **PASS**, zero problems |
| worst student-visible same-subject pair | 0.375 (`C4`↔`R6`) | **0.225** (`T2`↔`B2`, untouched, threshold 0.24) |
| worst pair involving a rewritten item | — | 0.196 (`R9`↔`R1`: splices vs the Chatham ropewalk — different subjects) |
| R&W key distribution | A21/B20/C20/D20 | **A21/B20/C20/D20** |
| questions whose key letter moved | — | **0** |
| highest R&W Jaccard vs the 1,295-passage bank | 0.39 (`T1`) | 0.39 (`T1`); highest for a rewritten item is 0.32 (`R6`) |
| `check_originality.py ngrams` | 0 flagged | **0 flagged**, 0 structural problems |
| Math questions touched | — | **0** (byte-identical in `test24.json`) |

The key distribution survived by construction rather than by luck: `balance_rw.py` deals target
letters round-robin by position in `QUESTIONS`, so as long as a rewritten item keeps its source
`answer` (all 81 are authored with the key first, at `"A"`) and its `why` names options by
content rather than by letter, every question's final letter is unchanged. Verified by diffing
the assembled JSON against the previous one: exactly 8 R&W questions differ, no Math question
differs, and no correct-choice label moved anywhere in the test.

## Local database

Test 24 already existed locally and `insert_test.mjs` skips modules that exist, so the rows were
deleted first — scoped by `testId`, after asserting the row's title is `Test 24` and that it had
no `Response` rows — and the test re-inserted. It came back as a new local id
**`67e769f1-5ff1-4d0a-9ad0-33485cbc5ffc`**, `DRAFT`, 6 modules / 147 questions, per-question
difficulty matching module difficulty in all six modules, and the R&W key counted straight out of
the database as 21/20/20/20. `audit_math_rendering.mjs` re-run over the whole local database:
**1,452 Math questions across 22 tests, 0 rendering errors**.

Production was deliberately left alone — the eight replacements are in `rw_test24.py` and
`test24.json` for the user to apply.

## Still not verified

The same gap the original build recorded: no `/exam/{attemptId}` screenshot pass, because
Playwright browsers are still absent from this container (`~/.cache/ms-playwright` does not
exist). The eight rewritten passages are plain prose and `<ul>` note lists with no math spans, no
tables and no images, so there is nothing in them a renderer can fail on that the assembled HTML
does not already show.
