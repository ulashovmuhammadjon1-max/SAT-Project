# Test 25 — build record

**Status: assembled, validated and inserted into LOCAL dev only, as DRAFT. Nothing was
published and production was never written to.** Local test id
`c11d3ca9-9a3b-4de2-9f81-80ebf5f0aaa1`, 147 questions (R&W 27/27/27, Math 22/22/22 with 19 MC +
3 FR per module).

Territory: papermaking and pulp mills, dye works, ink and pigment grinding, bookbinding, paper
marbling, and the colour science behind them. Structural template: `../test-19-build/`.

| | |
|---|---|
| Math questions re-derived with sympy | **66 / 66** (0 in `MANUAL`) |
| highest Math Jaccard vs production, after repair | **0.67** (was 0.72 before) |
| highest Math Jaccard within Test 25 | 0.56 |
| Math questions rewritten as template repeats | **34 of 66** |
| highest R&W Jaccard vs the 1,295-passage corpus | **0.175** |
| highest R&W self-pair | 0.143, with **0** pairs sharing any 5-gram |
| R&W key before balancing | A 81, B 0, C 0, D 0 |
| R&W key after balancing | **21 / 20 / 20 / 20**, 0 questions locked |
| Math key (M1 / M2E / M2H) | A3 B6 C5 D5 / A5 B4 C7 D3 / A3 B7 C7 D2 |
| DB-wide Math rendering audit | clean over all **1,584** Math questions in 24 tests |

---

## Task 1 — the interrupted Math repair

The build was halted mid-rewrite. `PAUSED_TESTS.md` recorded that it had found **24** genuine
template repeats, but not *which* 24, so the screen was re-run from scratch and every judgement
made independently.

**34 of the 66 were replaced.** The count is higher than 24 because the reading pass was pushed
below the flag line: only 15 of the 34 were ever flagged at 0.45 or above.

### What the Jaccard screen flagged (25 items at ≥ 0.45) — 15 replaced, 10 kept

Replaced: `M1-10 M1-12 M1-21 M2E-06 M2E-16 M2E-20 M2H-01 M2H-03 M2H-05 M2H-10 M2H-12 M2H-18
M2H-20 M2H-21 M2H-22`.

Kept, with the reason:

| item | score | nearest banked stem | why it stays |
|---|---|---|---|
| M1-08 | 0.48 | Test 21 M2E Q9 factoring an area | mine turns on recognising a **perfect square** and then asking for a perimeter; `bankgrep "perfect square"` returns 0 hits, and Test 13's square-area-to-perimeter item is purely numeric |
| M1-09 | 0.52 | Test 4 M1S Q12 (unrelated) | axis of symmetry recovered from a **table of equal values**; every banked vertex item hands the vertex or the equation over directly |
| M2E-10 | 0.59 | Test 6 M2E Q3 (unrelated) | substituting one point into `y = x² + k`; the top match is a linear item and the score is inflated by short abstract stems |
| M2E-19 | 0.60 | Test 14 M2E Q20 allotment **area** | surface area of a box; the bank has cube surface area (Test 2 M2E Q22) but no three-dimension box |
| M2E-22 | 0.51 | Test 19 M2H Q21 (a sine-ratio item) | 45-45-90 with the adjacent leg given; a different figure and a different route |
| M2H-02 | 0.46 | Test 19 M2H Q7 (two-fraction equation) | substituting a **given solution** back to recover a constant; no bank hit for that direction |
| M2H-07 | 0.60 | Test 2 M2E Q14 (unrelated) | optimising `(x−y)/y` over two ranges; the four banked "greatest possible value" items all solve an inequality |
| M2H-08 | 0.67 | Test 1 M2E Q11 (minimum of a quadratic) | `f(2x−1) = 6x+5`; the composed-argument definition has no bank instance, and 0.67 is the metric's ceiling for a short abstract function stem |
| M2H-09 | 0.56 | Test 1 M1S Q21 (exponent quotient) | `a+b+c` of an expanded difference; `bankgrep "value of a\+b\+c"` returns 0 hits |
| M2H-13 | 0.58 | Test 8 M1S Q21 (one real solution → \|k\|) | one root given, other root asked; `bankgrep "the other solution\|one solution of"` returns 0 hits |

### The 19 the screen never flagged — found by grepping the bank for the MECHANISM

This is the finding this build adds. Jaccard measures vocabulary; **19 of the 34 repeats scored
below 0.45, and six of them below 0.30**, because the words had all been changed. They were found
by writing `bankgrep.py` (in this directory) and searching the 1,386 banked stems for the
*mechanism* — "without replacement", "true for every value", "surface area", "does this model
give", "in the ratio N to M" — instead of for the vocabulary.

| item | score | the twin it was hiding from | what was identical |
|---|---|---|---|
| M1-02 | 0.40 | Test 18 M2H Q5 | linear cost from two data points, evaluated at a third |
| M1-04 | **<0.30** | Test 20 M1S Q5 | capacity limit minus a fixed tare, divided by a unit mass |
| M1-05 | **<0.30** | Test 18 M2H Q4 | dilute a percentage by adding pure solvent, find the volume added |
| M1-06 | **<0.30** | Test 13 M1S Q3 | linear interpolation from two readings to a third value |
| M1-11 | 0.44 | Test 19 M1S Q10 | "the distance between those two points" = difference of two roots |
| M1-13 | **<0.30** | Test 9 M1S Q13 | a fixed percentage removed repeatedly, value after n steps |
| M1-15 | **<0.30** | Test 8 M2H Q15 | mean of n, one more value added, new mean given, find it |
| M1-16 | **<0.30** | Test 20 M1S Q15 | table of count × unit, "for which row is the total greatest" |
| M1-17 | 0.35 | Test 13 M1S Q16 | two successive percent changes, recover the original price |
| M1-20 | <0.30 | Test 11 M2H Q16 / Test 14 M2H Q16 / Test 15 M2E Q22 | the altitude to the hypotenuse of a 9-12-15 triangle, three ways |
| M2E-02 | 0.37 | Test 6 M2E Q7 | `7(k−3)=42` against `7(k−2)=63` — same coefficient, same variable |
| M2E-05 | 0.35 | Test 6 M2E Q8 | "which listed value satisfies this inequality", same coefficient 5 |
| M2E-08 | **<0.30** | Test 19 M2E Q12 | product of two monomial powers, "which expression is equivalent" |
| M2E-12 | 0.35 | Test 19 M2E Q13 | evaluate an exponential model at a given input |
| M2E-15 | 0.43 | Test 9 M2E Q15 | "at that rate", unit price recovered then applied |
| M2E-17 | 0.37 | Test 18 M2E Q16 (+ Tests 11, 16) | table, "how many more X than Y" |
| M2H-11 | <0.30 | Test 20 M2H Q9 | exponential with an unknown coefficient, later value given, find it |
| M2H-14 | 0.39 | Test 14 M2H Q14 | **the same 5-to-2 ratio** limited by stock, greatest mixture |
| M2H-19 | 0.44 | Test 18 M1S Q22 | pour one cylinder into a wider one, find the new depth |

### Replacements were pre-screened before they were written

Every replacement went through `prescreen.py` (and `bankgrep.py` for its mechanism) *before* it
was drafted. **Eight first ideas were discarded that way**, which is eight second rewrites
avoided:

- `f(g(4))` composition — Test 7 M2H Q7 is the same item (0.88).
- `(2x²+5x−12)/(x+4)` polynomial division — Test 2 M1S Q13 (0.85) and Test 15 M1S Q8.
- sphere volume `288π` → radius — Test 8 M2H Q17 has the identical numbers and answer.
- `sin A = 20/29` → `cos A` — Test 8 M2H Q18 is the same identity with 8-15-17.
- `5π/6` radians → degrees — Test 5 M1S Q11 uses **the same angle**.
- two pumps working together — Test 9 M2H Q6, same template and the same 6 hours.
- "sum of three consecutive whole numbers" — Test 7 M1S Q21.
- `x⁴ − 13x² + 36 = 0` — Test 19 M1S Q13, verbatim.

Two more were discarded on the threshold alone: any bare `If …, what is the value of x?` stem
scores **0.75–1.00** against Test 1 M2H Q3 and its siblings, because stripping LaTeX and mapping
every number to `#` leaves those stems with nearly identical token sets. Short abstract stems
therefore need a context clause, which is house style here anyway.

### Verifier

`verify_math_test25.py` passes all four passes. Every one of the 66 answers is re-derived from the
question with sympy — never read off the `check` note — and no distractor equals a derived value.
Pass 4 confirms the cross-module setting rule: **0 setting keywords shared** between Module 1
(15 keywords: papermaking, pulp, beater, couching, ream, quire, grammage, guillotine, bindery,
reel, …) and either Module 2 branch (19 keywords: dye, skein, madder, alum, indigo, pigment, ink,
vermilion, ochre, muller, marbling, …). One replacement tripped it and was fixed: an "ink **mill**"
in M2H-12 collided with Module 1's paper mill.

---

## Task 2 — the 81 R&W items

All 81 authored. Blocks: Words in Context 15 (3 of them the underlined-word variant), Text
Structure and Purpose 6, Central Ideas and Details 6, Command of Evidence 9, Inferences 6,
Boundaries 12, Form/Structure/Sense 9, Transitions 9, Rhetorical Synthesis 9. Block order is
non-decreasing in every module and the writing block opens at question 15 in all three.

Rhetorical Synthesis is written in **both** real shapes — six items quote "the notes" and R2, R5
and R8 quote "the given sentences" — because a pipeline that knows only the first misfiles the
second (that bug was live in Test 1).

### Test 16 is the dangerous neighbour, and keyword screening found it first

`screen_topics.py topics` ran before a word was drafted. Test 16 (printing) already holds most of
the obvious ground in this trade, and **21 planned topics were dropped at the planning stage**
rather than written and discovered later: the hand mould and deckle against the Fourdrinier web
(rw_test16:T1); sizing with gelatine (W2); iron gall ink (W3, and rw_test13:C6); a mordant such as
alum linking dye to fibre (W7); lead white over vinegar (W10); lake-pigment lightfastness measured
in units (E8); orchil from lichen (R5); rag paper against wood pulp and the acid left in the sheet
(N7, I2); a binder resewing sections onto cords (F4); two dyehouses working the same weld under a
north light (F5); fastness at the window and in the wash (W14); long paper-mulberry fibres
(rw_test18:I5); woad against indigo by yield (rw_test14:T7); murex priced by the labour of
collection (rw_test14:E5); cochineal from Oaxaca (rw_test8:R7); Prussian blue in woodblock prints
(rw_test11:R7); synthetic ultramarine dating a panel (rw_test9:I5); a watermark dating a
manuscript (rw_test8:B10, rw_test10:B10); and suminagashi, where a surfactant makes each ring
spread inside the last (rw_test15:B6) — which is why **no item here explains ox gall**.

rw_test16:F5 also rules out a whole *item shape*: no comparative item here takes the form "deeper
than _____ in the other house". rw_test14:E5 rules out the claim shape "the price was set by the
labour rather than by any secret".

### Five items were rewritten after drafting — all of them for repeating **my own** facts

`screen_topics.py passages` scores each passage against the corpus *and against every other
passage in this file*. The corpus scores were never a problem (0.175 worst). The self-pairs were:

- **T5 / B11** 0.225 — both had the marbler dropping colour on the bath to test its thickness.
  B11 moved to sorting white rags by grade.
- **W4 / E6** 0.208 — both were foxing. W4 moved to a reversible conservation mend.
- **W1 / C1** 0.170 — both turned on beating, fibre contact and sheet strength. C1 moved to the
  collapsible paint tube.
- **W9 / N3** 0.156 — both had verdigris eating through the page. N3's example became orpiment.
- **B6 / N9** 0.148 — both were ochre needing nothing but washing and grinding. B6 moved to an
  apprentice's indenture.

Every replacement topic was screened against the corpus first: "colourman", "paint tube",
"wheat-starch mend" and "orpiment" return 0 relevant hits.

### Key balance

Hand-authored, all 81 keys landed on A. `balance_rw.py` rotated to **21/20/20/20** with **0**
questions locked, because every `why` names options by their content.

---

## Three checker bugs found this build

All three are the recurring family: a check that matches more, or less, than it means to.

1. **`LETTER_REF` matched data-table row labels.** Two Command of Evidence rationales began "Ink B
   is inside both limits" and "the difference for paper C", and `balance_rw.py` read `B is` and
   `C is` as references to *options* B and C and refused to rotate them. The rationales were
   innocent; the *content* was the problem, since a table with rows labelled A–D sitting beside
   answer choices labelled A–D is confusing for a student too. The rows were renamed (Ink 1–4,
   and four mills), which fixed the lock and the ambiguity at once. **Do not "fix" this by
   loosening `LETTER_REF`** — it is the pattern that already cost three builds.
2. **`screen_topics.py` stripped only one Rhetorical Synthesis boilerplate.** `BOILER` removed
   "While researching a topic, a student has taken the following notes" but not the
   given-sentences template, so R2, R5 and R8 appeared to share 5-grams with one another. The
   shared text was the stem template, not the content. `BOILER` now strips both — any build that
   uses the second shape needs this.
3. **The keyword split in the Math verifier is only as good as its word list.** It caught "ink
   mill" straight away. Words with an everyday sense — "ink", "size", "leaf", "board",
   "gathering", "ground", "press", "sheet", "laid", "weld" — are deliberately *absent* from that
   list and must stay absent.

## Files

`math_test25.py` (repaired) · `verify_math_test25.py` (derivations rewritten for the 34
replacements) · `bankgrep.py` (**new** — regex search over the read-only bank, the tool that found
the 19 hidden repeats) · `prescreen.py` · `rw_test25.py` (new, 81 items) · `screen_topics.py`
(BOILER fixed) · `balance_rw.py` (retargeted from T19) · `rw_test25_balanced.json` ·
`assemble_test25.py` (copied from T19; **both** provenance tags retargeted — `AUTHORED-T25:` for
R&W and `AUTHORED/T25-` for Math — and asserted: `test25.json` contains 0 occurrences of "T19") ·
`insert_test.mjs` · `test25.json`.

## Known gaps

No `Explanation` rows, consistent with every test since Test 1. No images: all figures are real
`<table>` markup (5 Math questions, 3 R&W), so the geometry items are worded to be fully
determined without a picture. Test 25 has **not** been opened in the exam interface at
`/exam/{attemptId}` — the DB-wide rendering audit and the database content QA are the only
rendering checks run.
