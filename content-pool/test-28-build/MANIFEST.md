# Test 28 — build record

147 questions: R&W 27/27/27, Math 22/22/22 (19 MC + 3 FR per Math module). Everything is
originally authored. Inserted **local only**, as `DRAFT`
(`1631a6c4-ff5b-4da0-a0bc-de610cd3f192`). **Production was not touched.**

Thematic territory: coaching routes and stage timetables, farriery and horseshoeing, coach
building, drovers' roads, toll gates and turnpikes. Wheelwrighting, felloes, spokes and harness
belong to Test 21; railways to Test 17 and tramways to Test 20, so everything here stays on the
horse-drawn road.

## Results

| | Test 28 |
|---|---|
| Math questions / verified | 66 / 66, `verify_math_test28.py` ALL CHECKS PASSED |
| highest Math Jaccard vs production | 0.67 |
| highest Math Jaccard internal | 0.46 |
| Module 1 / Module 2 shared Math settings | 0 |
| **highest R&W Jaccard vs corpus (passage + stem)** | **0.250** (F2 ~ rw_test8:F9) |
| highest R&W Jaccard within Test 28 | 0.235 (B12 ~ F2) |
| max shared 5-grams, either direction | 2 |
| R&W pairs at or above 0.5 Jaccard | 0 |
| **R&W key before balancing** | **A 72, B 0, C 9, D 0** |
| **R&W key after balancing** | **A 21, B 20, C 20, D 20** |
| rationales locked by letter-naming | 0 of 81 |
| **writing items with a defect (this pass)** | **8** — see below |
| answer keys found wrong | **0** |
| math rendering audit | 1,782 questions across 27 tests, 0 errors, 0 style-only |

## The correctness pass — what this build is actually a record of

Math and R&W were both drafted and passing `validate_tests.py` when this pass began. The pass
substituted **each of the four choices into the blank** for all 39 writing items (Boundaries 12,
Form/Structure/Sense 9, Transitions 9, Rhetorical Synthesis 9) and read the resulting sentence,
then spot-checked the 42 reading items the same way. It found eight defects.

### Seam collisions — a choice running past the blank into the words after it (4)

The defect class: the option is well formed **in isolation**, so reading the option list will
never show it. Only substitution does. Two of the four were in a **key**, not a distractor.

| item | option | passage continues | rendered | fix |
|---|---|---|---|---|
| B7 (RW_M2E q16) | `quarter; yet the` | `the custom was never...` | "yet **the the** custom" | option -> `quarter, however,` (a comma splice) |
| B2 (RW_M1 q15) | `ground; the amended bill and` | `was published in October` | "the amended bill **and was published**" | option -> `ground, the amended bill` (a comma splice) |
| B3 (RW_M2E q18) | **all four** ended `in` | `in the loose boxes` | "wall; **in in** the loose boxes" | duplicated `in` deleted from the PASSAGE |
| B12 (RW_M2E q15) | **all four** ended `the` | `the remaining five` | "years; **the the** remaining" | duplicated `the` deleted from the PASSAGE |

B3 and B12 were the serious ones: every option was malformed, so the item was unanswerable as
drafted. The key OPTION was broken; the option it named was still the right answer, so the key
letter did not move.

### Two-correct-answer risks (3)

- **F1** offered `have been` as a distractor. That is **plural**, so it agreed in number exactly
  as the key `were` does, and the rationale's claim that the wrong options were singular was
  false. Changed to `has been`; the rationale now says "every other option is singular".
- **W5** `handed the bidder the whole of the _____` — `profit` was as defensible as the key
  `risk`, since a fixed sum to the trust and the residual to the bidder is a real reading of an
  auctioned toll lease. The passage now adds "A wet season that kept the wagons off the road fell
  on him and not on the trust", which only `risk` completes.
- **W9** `not a fashion but a _____` — `convenience` was live, because the passage justified the
  angled room by a keeper seeing both roads "without rising", which *is* a convenience. Rewritten
  to "nothing could reach the bar from either road without having been seen from that window", so
  the shape is forced on the house rather than merely easier.

### Wording and typography (1 + rationale repairs)

- **Seven passages wrote the blank as `_____ .`**, with a space before the full stop, rendering as
  "one that stayed constant ." No other build in `content-pool/` does this — checked every
  `rw_test*.py` from 20 to 29, all zero. Fixed.
- **T6** put `Thus,` two sentences after "A line was **therefore** divided", handing the answer
  away; `therefore` -> `instead`. Its rationale also called the conclusion a "restatement", which
  argues for *In other words* rather than for the key, and was reworded to "follows directly
  from". **B2**'s rationale called a no-punctuation run-on "a comma splice of a different kind",
  though a fused sentence has no comma.

**No answer key was wrong.** All 81 R&W keys are the correct option. Every defect was in a
distractor, a passage, or a rationale.

## New in this directory: `check_substitution.py`

Substitutes all four options into all 48 blank-bearing items and reports doubled words, dangling
connectives, doubled punctuation and identical substitutions. Currently **0 findings**, and a
regression test that re-injects the four original defects confirms it still fires on them.

The precision matters more than the checks do. A first cut scanned the whole substituted passage
and reported **97 findings, 93 of them ordinary compound predicates** ("stood tied and faced",
"walks steadily and will make") that had nothing to do with the blank. Narrowing to a window
around the insert was still not enough. The version kept here requires the match to **straddle the
edge of the inserted text** — one word from the option, one from the passage — which is the defect
stated exactly, and drops the false positives to zero. This is the same lesson CLAUDE.md already
records under word-boundary bugs: *a checker that over-matches is worse than no checker, because
it trains you to ignore its output.*

One further trap, worth repeating because the tool fell into it itself: stripping the head and
tail of the passage separately and rejoining them with spaces **invents whitespace that is not in
the source**, and produced 28 phantom `SPACEDOT` findings against passages that were already
fixed. Mark the blank, normalise once, then split on the mark.

## Files

`math_test28.py` and `verify_math_test28.py` were inherited complete and are unmodified; the
verifier was re-run and still passes. `rw_test28.py` carries the corrections above.
`screen_topics.py` was copied from `../test-16-build` and its `final` mode still imported
`rw_test16`, so it screened the wrong test from whatever directory it ran in — retargeted to
`rw_test28`.

Pipeline, in order:

```
python3 check_substitution.py         # 0 findings
python3 verify_math_test28.py         # ALL CHECKS PASSED
python3 screen_topics.py final        # 0 pairs at or above 0.5
python3 balance_rw.py                 # A 21, B 20, C 20, D 20
python3 assemble_test28.py            # -> test28.json
python3 ../validate_tests.py 28       # PASS
service postgresql start
DATABASE_URL=... node insert_test.mjs test28.json "Test 28"
DATABASE_URL=... node ../test-6-7-build/audit_math_rendering.mjs
```

A stale Test 28 from the killed previous run was already in the local DB, and `insert_test.mjs`
is idempotent — it skipped every module and reported "inserted this run: 0". The old row was
deleted and the test re-inserted, or local would still be serving the defective content while
every check passed against the file.

## Verified from the database, not from the JSON

All three R&W modules: 27 questions, writing opens at question 15, sequence

```
CAS-WV x5 -> CAS-TS x2 -> INI-CI x2 -> INI-CE x3 -> INI-IE x2
          -> SEC-BS x4 -> SEC-FS x3 -> EOI-TR x3 -> EOI-RS x3
```

identical and monotonic in all three. All 81 R&W questions carry their own `Passage` row. All 9
free-response answers are JSON-array encoded. Per-question difficulty matches module difficulty in
all six modules. The three fixed Boundaries items were re-read out of the DB with each choice
substituted into the passage by SQL, and a DB-side sweep for a doubled word at any seam across
every blank-bearing R&W question returns **0**.

## Status and what is left

`DRAFT`, local only. Not published, not inserted to production, nothing committed — the parent
commits. Before publishing: insert to production with the same script and re-run
`audit_math_rendering.mjs` against production.

Not verified: the R&W content was not opened in the real exam interface (`/exam/{attemptId}`) this
pass. Every check here is against the file and the local database.
