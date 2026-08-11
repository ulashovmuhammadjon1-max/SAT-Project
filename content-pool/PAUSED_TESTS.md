# Tests 28–31 — paused mid-build

Eight builds were stopped deliberately part-way through. This file records exactly where each
one stopped, so the work can be resumed without re-deriving what state it is in.

**Nothing here is finished, and nothing here has been inserted into any database.**

## What every paused test has

All eight completed their Math authoring: **66 questions each** (22 per module across
`MODULE_1`, `MODULE_2_EASY`, `MODULE_2_HARD`), written by hand into `math_testN.py`.

None of them started Reading & Writing. There is no `rw_testN.py`, no `balance_rw.py` output,
no `assemble_testN.py` and no assembled `testN.json` in any of these directories. Each test is
therefore **66 of 147 questions — roughly 45% complete**.

## Where each one stopped

| test | Math authored | verifier | state when stopped |
|---|---|---|---|
| 23 | 66/66 | written | Math complete. Was about to begin the 81 R&W items. |
| 25 | 66/66 | written | **Mid-rewrite.** Reading the flagged similarity matches found **24 genuine template repeats**; it was replacing them with pre-screened alternatives when it stopped. |
| 26 | 66/66 | written | Math complete and passing. Was about to begin the 81 R&W items. |
| 27 | 66/66 | written | **Mid-rewrite.** Had found several genuine template repeats by reading flagged matches and was screening replacements before writing them. |
| 28 | 66/66 | written | Was updating the verifier's sympy derivations and LaTeX parser to cover newly written items. |
| 29 | 66/66 | written | Math verified and passing. Was screening candidate R&W topics against the 1,295-passage corpus. |
| 30 | 66/66 | written | All 66 verified. Was reading every flagged similarity match, per the rule that the threshold is triage rather than a verdict. |
| 31 | 66/66 | partial | Was still writing the verifier. Math is unverified. |

## Read this before resuming any of them

**Tests 25 and 27 stopped in the middle of a rewrite.** Their `math_testN.py` still contains
questions that had already been *identified as template repeats* and were queued for
replacement. Do not treat those files as verified content — re-run the similarity screen and
finish the rewrite before trusting them. Test 25's count of 24 repeats is the largest any single
build has reported, which is consistent with the recorded finding that past roughly 1,386 banked
Math stems a first draft is more likely than not to collide.

**Test 31's Math has never been verified** — its verifier was incomplete when it stopped. Every
answer still needs an independent sympy derivation.

**Tests 23, 26, 29 and 30 are the cleanest resume points**: Math authored and verified, R&W not yet
started.

## To resume

Each directory keeps its own `math_testN.py`, `verify_math_testN.py`, and the screening helper
the agent wrote for itself. The shared inputs are unchanged and live at the `content-pool` root:

- `prod_math_stems.json` — 1,386 Math stems (rebuildable with `build_corpora.py`)
- `rw_authored_corpus.json` — 1,295 R&W passages
- `validate_tests.py` — structural validation of an assembled `testN.json`
- `sweep_similarity.py` — cross-test similarity, with the length-aware `shape` signal that
  catches template repeats plain word-overlap misses

Territories and structural templates as originally assigned:

| test | template | territory |
|---|---|---|
| 23 | Test 17 | canal locks and pounds, barge haulage, aqueducts, dredging, towpaths, wharves, canal tolls |
| 25 | Test 19 | papermaking, pulp mills, dye works, ink and pigment grinding, bookbinding, marbling |
| 26 | Test 20 | bell founding, campanology, organ building, pipe voicing, carillons, tuning |
| 27 | Test 21 | ice houses, ice harvesting, salt pans, fish curing, smokehouses, cheese caves |
| 28 | Test 16 | coaching routes, stage timetables, farriery, coach building, drovers' roads, toll gates |
| 29 | Test 17 | brickworks and kilns, tile making, plasterwork, stonemasonry, scaffolding and hoists |
| 30 | Test 18 | physic gardens, essential-oil distilling, apothecary dispensing, herbaria, seed drying |
| 31 | Test 19 | poultry and egg grading, dovecotes, falconry, decoy ponds, eel traps, fish ponds |

---

# Second pass: Tests 27–31 (11 August)

Five agents resumed these; all five were killed by an account session limit, not by
an error in the work. Test 27 was finished and **published**. The rest stopped at
these points.

| test | Math | R&W | assembled | state |
|---|---|---|---|---|
| 27 | 66 | 81 | yes | **PUBLISHED.** Its agent believed the Math key `D=9/57` was worse than any shipped test; it is not — Test 17 ships `A=9` and Test 25 `D=10`, spreads of 9 against Test 27's 8. No change was needed. |
| 28 | 66 | 81 | yes | **Held. Do not publish as-is.** Its agent reported finding a real key error in the writing items and was fixing that plus "several weak Boundaries items" when it died. Reading six Boundaries items found one confirmed defect: `RW_M2E Q16` choice C is `"quarter; yet the"` against a passage continuing `"the custom was never written"`, giving **"yet the the custom"**. The whole writing block needs a correctness pass before this ships. |
| 29 | 66 | ~partial (458 lines) | no | R&W barely started — it had just begun the first chunk. |
| 30 | 66 | 81 drafted (1,223 lines) | no | R&W drafted but never balanced or assembled. |
| 31 | 66 | 81 drafted (1,288 lines) | no | R&W drafted, not assembled. **Its Math has still never been fully verified**, and its agent was fixing a self-contradictory rationale on item `F4` when it stopped. |

Note the assembled JSON for a paused build can be **older than its source** — Test 28's was
written 2m16s before its last source edit, so it did not contain the final fixes. Re-run the
assembler before trusting any `testN.json` from an interrupted build.

Each directory also now carries the mechanism-search helper its agent wrote
(`mechanism.py`, `bankgrep.py`, `mechanism_search.py`, `mechanism_scan.py`) — searching the
banked stems by mechanism rather than vocabulary is what found the repeats Jaccard missed, and
those are worth keeping.
