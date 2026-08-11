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
