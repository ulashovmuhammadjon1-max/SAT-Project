# Test 22 — build record

147 questions: R&W 27/27/27, Math 22/22/22 (19 MC + 3 FR per Math module). Everything is
originally authored. Inserted **locally only**, as `DRAFT` — nothing in this build touched
production.

| | |
|---|---|
| structural template | `../test-16-build/` (`rw_test16.py`, `assemble_test16.py`) |
| thematic territory | beekeeping and apiaries, honey extraction, sugar refining, beet processing, confectionery boiling, beeswax and candle making |
| local test id | `de6bc6f1-3c40-4869-bc42-9b732fd5821f` |
| corpus at build time | 1,295 R&W passages (`../rw_authored_corpus.json`), 1,386 live Math stems |

## Results

| | Test 22 |
|---|---|
| highest R&W Jaccard vs corpus | **0.160** (F1 ~ `rw_test16:F2`) |
| highest R&W Jaccard within the test, before repair | 0.531 (S1 ~ R1) |
| highest R&W Jaccard within the test, after repair | **0.250** (S3 ~ N9) |
| worst *same-module* R&W Jaccard after placement search | **0.115** (RW_M1: R2 ~ R3) |
| R&W items flagged at ≥0.50 Jaccard or ≥3 shared 5-grams | **0** |
| R&W key before balancing | **A 80, B 1, C 0, D 0** |
| R&W key after balancing | **A 21, B 20, C 20, D 20** |
| rationales locked by letter-naming | **0** |
| R&W topics dropped as corpus collisions | **15** (at the planning stage, before drafting) |
| R&W items rewritten as internal repeats | **10** |
| highest Math Jaccard vs production | 0.67 |
| highest Math Jaccard within the test | 0.56 |
| Math verifier | `verify_math_test22.py` — ALL CHECKS PASSED, re-run unchanged |

Writing opens at question **15** in all three R&W modules; the block-rank sequence is
non-decreasing in each. `../validate_tests.py 22` passes.

## The finding this build adds: a corpus screen cannot catch a test plagiarising itself

`check_originality.py` compared all 81 passages against the 1,295-passage corpus and returned a
maximum of 0.160 — the cleanest R&W figure of any build so far. It was also, on its own,
misleading. Running the *same* measure between the test's own passages found that **all nine
Rhetorical Synthesis items had been written by restating a reading passage from earlier in the
same file** — the bee space behind S1, the soil tare behind S2, seeding behind W5, raffinose
behind C2, drone congregation areas behind C1, HMF behind I2, and so on — and that Command of
Evidence item E8 was a second treatment of W12's subject.

Six of those pairs scored **0.35–0.53**. For calibration, the same measure over Tests 16–21 gives
maxima of 0.15, 0.16, 0.14, 0.18, 0.16 and 0.23, and **zero** pairs at or above 0.35 across all
six. Whichever module a pair landed in would have shown one student the same topic twice inside
27 questions.

All ten were rewritten onto mechanisms that appear nowhere else in the test: the solar wax
extractor and slumgum, the clearer board, orientation flights and the rule for moving a hive,
robbing and the reduced entrance, the rushlight against tallow and beeswax, the wax seal and its
matrix, monogerm beet seed and singling, caramelisation as distinct from melting, wax moth in
stored comb, and boiling-point elevation as the confectioner's thermometer.

**For the next build: run the self-comparison as a first-class check, not an afterthought.** Its
natural failure mode is invisible to the corpus screen and it is most likely to bite exactly where
it bit here — Rhetorical Synthesis, whose bulleted notes are the easiest block to produce by
compressing a passage you have already written.

## The second placement rule, added to the assembler

`assemble_test22.py` now deals the R&W pool over a range of shuffle seeds and keeps the seed that
minimises the worst same-module passage Jaccard, reporting the figure it settled on. Rationale:
a student sits one module at a time, so a near-repeat split across two modules costs nothing while
a near-repeat inside one module is visible duplication. This is the R&W counterpart of the
cross-module setting check Tests 19–21 added for Math. It is a placement rule and cannot repair
content — the content-level fix above had to happen first; the search only moved the residual
0.250 pair down to 0.115.

The token set it measures on drops this territory's shared vocabulary (`bee`, `hive`, `colony`,
`comb`, `honey`, `wax`, `sugar`, `beet`, `syrup`, `boil`, `factory`). Left in, those words appear
in most of the 81 passages by construction, every pair looks related, and the measure stops
discriminating — the same lesson as dropping `ground` from Test 19's setting check.

## Both Rhetorical Synthesis stem shapes are now present

Six items use *"...uses relevant information from **the notes**..."* and three use
*"...uses information from **the given sentences**..."* (`given()` in `rw_test22.py`). CLAUDE.md
records that a classifier matching only the first phrasing silently misfiled every question of the
second kind, in Test 1 as well as Test 2. Tests 16–21 contain **only** the notes shape, so nothing
in the recent corpus could ever have surfaced that bug again. `assemble_test22.py` asserts both
shapes are present and that no Rhetorical Synthesis stem uses a third, unrecognised phrasing.

## The `_ref` provenance trap, checked rather than assumed

Scaffolding from `test-16-build` means two differently shaped tags must be rewritten: the Math tag
`AUTHORED/T16-` and the R&W tag `AUTHORED-T16:`. A substitution keyed on the hyphen rewrites the
first and misses the second — the defect that nearly put Test 18 provenance on Tests 19–21's R&W.
`report()` in `assemble_test22.py` now searches every assembled `_ref` for `T<n>` and fails on any
`n` other than 22, and `../validate_tests.py` checks the same thing independently. Both are clean;
`test22.json` contains no `T16` substring at all.

## Two content corrections found while re-deriving the answer keys

Every key was re-derived by hand — the standing rule after Test 5 shipped 6 wrong R&W answers in
81. No key was wrong, but two passages were:

- **B8** claimed maltose is a simple sugar. It is a disaccharide. The stem was reworded so no
  claim about sugar classes is made; the punctuation the item actually tests (a closing dash
  matching an opening one) is unchanged.
- **F2** put Achard's factory "fifty years" after Marggraf's 1747 paper. It opened in 1801, so the
  stem now reads "half a century afterwards".

## Verification run, in order

```
python3 verify_math_test22.py                       # ALL CHECKS PASSED, 66 questions
python3 check_originality.py ngrams                 # 0 flags; corpus 0.160, self 0.250
python3 balance_rw.py                               # A80/B1 -> 21/20/20/20, 0 locked
python3 assemble_test22.py                          # writes test22.json, all modules OK
python3 ../validate_tests.py 22                     # PASS
service postgresql start
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/sat_platform?schema=public' \
  node insert_test.mjs test22.json "Test 22"        # 147 inserted, DRAFT
DATABASE_URL='...' node ../test-6-7-build/audit_math_rendering.mjs
                                                    # 1,386 Math questions across 21 local
                                                    # tests incl. Test 22 — 0 errors
```

Read back from the local database afterwards: every one of the 81 R&W questions carries a
`passageId`; `Question.order` is contiguous 1..27 / 1..22 in all six modules with no duplicates;
per-question difficulty is a single value per module matching the module's own
(MEDIUM/EASY/HARD); the R&W key across the test is A21 B20 C20 D20.

A house-style pass over the assembled JSON confirms 81 distinct passages, 3 real `<table>` figures
(E4, E5, E6) in the house style block, every fill-in-the-blank exactly five underscores, every
"underlined" stem backed by a real `<u>`, no markdown asterisks and no raw `°`/curly-quote/dash
glyphs where an HTML entity belongs.

## Known gaps and what is unverified

- **No `Explanation` rows**, consistent with every test from Test 1 onward. The `why` field on each
  R&W question and `check` on each Math question hold the reasoning but are not inserted as
  `Explanation` records.
- **No images.** All three data figures are real `<table>` markup; no matplotlib PNG was produced,
  so any question needing a picture was instead worded to be fully determined without one.
- **Not verified in the exam interface.** The build was not loaded at `/exam/{attemptId}` via a
  seeded throwaway attempt — checks stopped at the assembled JSON and the database rows. Worth
  doing before this test is published.
- **Not inserted or published in production**, by instruction. Local `sat_platform` only.
- Two residual same-topic pairs remain in the pool at 0.25 (S3 ~ N9, both on the hydrometer;
  C5 ~ I1, both touching drone brood). Both are within the range Tests 16–21 already ship, and the
  placement search puts each pair in different modules.
