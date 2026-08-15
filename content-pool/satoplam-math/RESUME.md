# RESUME — Math rebuild of Tests 6-31. Read this first.

## Status: SHIPPED for Tests 6-19. Tests 20-31 Math is unchanged.

924 SATashkent questions are live in production across Tests 6-19 Math
(14 tests x 66). The old Math in those modules was retired, not deleted.
Tests 1-5 and 20-31 keep their previously authored Math — 1,122 questions.

    live Math by source:  SATMATH 671   SATHARD 253   authored/other 1,122
    total live questions: 4,557, all 4,557 with an explanation
    rendering audit:      0 errors, 6 style-only ("degrees" spelled out)

## Why 14 tests and not 26

Supply, after every gate:

    verified transcriptions       1,953
    figure never built             -139
    duplicate clusters collapsed   -289
    blocked defects                  -6
    POOL                          1,519

HARD is the binding tier: 443 against 26 needed per test. That alone allows
17 tests, but the allocator stops at 14 on a **domain cap**. Past 14 the
algebra and advanced-maths HARD supply is spent and only geometry is left —
tests 20-22 came out with Module 2 Hard at 14 of 22 geometry and zero
problem-solving. A module that lopsided is not a Digital SAT module. No
module in the 14 shipped exceeds 8 of one domain.

To go further you need more HARD content in ALG/ADV/PSDA, not a looser
threshold.

## What the key verification found

**102 of 110 disputed keys were confirmed wrong**, across 1,999 questions.

| wave | checked | disputed | confirmed wrong |
|---|---:|---:|---:|
| first (needed transcribing) | 1,102 | 72 | 67 |
| second (extracted cleanly) | 897 | 38 | 35 |

Every question was solved by a transcriber who could not see the printed key;
every disagreement was re-solved by a second reader who could see neither the
key nor the first reading. A key moved only when both agreed against the book.
**About 1 keyed answer in 18 in these books is wrong in print.**

Residue: 1 unsettled (three different answers), 4 broken, 1 held for a
contaminated reading, 14 unanswerable, 25 with no usable printed key. All are
out of the pool.

## The pipeline, in order — every stage is re-runnable

    parse_math.py / parse_hard.py   ->  math_parsed.json, hard_parsed.json
    slices.py -> agents             ->  out/mx-*.jsonl, out/my-*.jsonl
    verify_keys.py --write          ->  ready.json, disputes.json
    build_adj.py -> agents          ->  adj/adj*-*.jsonl
    resolve_keys.py --write         ->  key_verdicts.json  (merges rounds)
    build_pool.py                   ->  pool.json
    allocate.py --tests N           ->  allocation.json
    verify_allocation.py            ->  exits non-zero on any ERROR
    insert_math.mjs [--apply]       ->  production

`verify_keys.py` carries prior verdicts forward, so a flipped key never
resurfaces as a fresh dispute. `resolve_keys.py` merges rounds rather than
replacing the file.

## Traps hit here — do not repeat any of these

- **`head` closes the pipe.** `python3 verify_keys.py --write | head` dies of
  SIGPIPE before the write block runs, silently leaving the old file in place.
  It cost a round of adjudication built on a stale dispute list once, and it
  caught me a second time in the same file. Redirect to a log, never pipe.
- **Two briefs, two field names.** Round 1 adjudicators wrote
  `answerLabel`/`answerValue`; round 2's brief asked for `answer`.
  `resolve_keys.py` read only the first shape, so 38 clean readings looked
  like refusals and it reported all 38 as broken questions. The same mismatch
  in the writer left every flip target null and dropped 35 corrected keys out
  of the pool. **A checker that does not error is the dangerous kind.**
- **Bag-of-words Jaccard does not work on Math.** Stems are short and heavily
  boilerplated, so after stopword removal two entirely different questions can
  share their whole remaining vocabulary and score 1.00 — "If 6/7 p + 12 = 54,
  what is 7p?" against "If (x-16)/27 = (x-16)/9, what is x+16?" did exactly
  that. `sim.py` uses 4-gram shingles over the normalised token stream, which
  keeps word order, plus a distinctive-constants channel for the repeat that
  keeps the mathematics and changes the setting.
- **The article "A"** came back in `parse_hard.py` and swallowed 63 question
  bodies. CLAUDE.md already documented it as `LETTER_REF`.
- **Two over-matching checkers in `verify_allocation.py`**, both caught by
  reading the output rather than acting on it: the "stem promises a visual"
  check fired on 110 sound questions because "the graph of y = f(x) passes
  through (-3, 0)" names a mathematical object, not a picture; and it only
  read the stem, so eight "for which of the following tables..." questions
  were flagged while carrying four real tables in their CHOICES.
- **Run positive AND negative controls on any style checker before believing
  a clean result.** 924 questions passing with zero findings is only
  meaningful because all ten defect patterns were shown to fire on a planted
  example and none fires on correct LaTeX or on a dollar amount.

## Thresholds, and how they were set

Read off a band survey of every pair in the pool, never guessed:

- **>= 0.60 is the same question**, not merely the same skill — `1/(cx) =
  x/76 + 1/c` against `x/96` against `x/152`. 209 clusters absorbed 289
  questions.
- **0.45-0.60 is the same question with the numbers changed** — a polygon of
  83 sides against 87, `w = 150` against `w = 128`.
- **0.35-0.45 still holds real template repeats** — `x^2+kx+14=(x+n)(x+7)`
  against `x^2+kx+55=(x+n)(x+11)` scored 0.44. Hence the co-visible reject
  line at 0.35.

Highest co-visible similarity in the 14 shipped tests: **0.32**.

## Co-visibility, the thing the R&W build skipped

A student sits Module 1 plus exactly ONE Module 2 branch. So M1-M2E, M1-M2H
and within-module pairs are screened; M2E-M2H is not, because no student sees
both. The R&W build scored nothing and shipped 33 same-test duplicates, two of
them byte-identical.

## Placement rules the user set

- Hard Book questions are Module 2 Hard questions, and **never** go into
  Module 2 Easy.
- The user extended this so the Hard Book may also fill Module 1's nine hard
  slots. Keeping it out of Module 1 caps the build at 11 tests, because
  Module 1's 9 and Module 2 Easy's 3 would both have to come from the two
  regular books' 139 HARD questions.

## Still open

- **Tests 20-31 Math is untouched** and still carries authored questions.
  Finishing them needs more HARD content in Algebra, Advanced Math and
  Problem-Solving specifically.
- **139 questions were dropped for want of a figure** (81 MEDIUM, 58 EASY —
  no HARD). Building those figures returns them to the pool.
- **The real exam interface was not walked.** The DB-wide rendering audit is
  clean and `verify_allocation.py` passes, but CLAUDE.md also asks for a pass
  through `/exam/{attemptId}` with Playwright, and that was not run.
- **1 unsettled key** (`satmath-ma2-triangles-5`) and the blocked defects in
  `blocked.json` are recorded for a human.
- Rotate the Neon database password, the Resend API key and the Gmail
  password — all three were pasted into the session that produced this work.
