# Test 3 & Test 4 — built and inserted (DRAFT)

Both tests are now live in the production database as **`status: DRAFT`** (not visible to
students until published from the admin panel). 294 questions total: 147 per test (27+27+27
R&W, 22+22+22 Math).

- Test 3 id: `699d16aa-10d7-4edc-a2c6-3cfc0fdff966`
- Test 4 id: `98364c5d-c8ba-4710-943e-5103e603031f`

## What's in this directory
- `full_build.json` — the **exact** content that was inserted into the DB (passage HTML, stem
  HTML, choices, correct answers, domain/skill codes), grouped by test → module. This is the
  source of truth for what's live; if you need to re-verify or rebuild, start here.
- `build_rw.py` — applies the HTML formatting pass (tables, `<ul>` bullet lists, `<u>`
  underlines, Text 1/Text 2 splits) to the R&W content from
  `content-pool/test-3-4-5-reading-writing/test345_classified.json`, and folds in the 1
  borrowed Test 5 Transitions question that brings Test 4's Module 2 (Easy) from 26 to 27.
- `classify_math.py` — hand-classified Domain/Skill (by content, not automated) for all 165
  usable Math questions from `content-pool/new-source-transcripts/` (172 transcribed minus 4
  UNVERIFIED minus 3 confirmed duplicate-template pairs — see "Deduped" below). Also marks
  which questions were dropped.
- `mathify2.py` / `build_math_final.py` — converts the plain-text Math notation to `\( \)` /
  `\[ \]` LaTeX, applies the `pi`-word and fraction/sqrt/exponent fixes documented in
  `CLAUDE.md`, and wraps answer choices consistently. Includes a **safety fallback**: any stem
  where the auto-wrap would produce structurally broken LaTeX (unbalanced delimiters, a split
  number) reverts to plain unwrapped text instead of shipping broken rendering — see "Known
  gaps" below for which items that affected.
- `assemble_math3.py` — allocates the 165 classified Math questions across the 6 Math modules
  (22 each, ≤3 FR each), targeting Test 1's live domain proportions (~8 ALG / 6 ADV / 4 PSDA /
  4 GT per module; GT supply was exactly at capacity so all 24 available GT questions were
  used with zero slack).
- `insert.mjs` — the actual insertion script (Node + `@neondatabase/serverless`, since this
  session's sandbox blocks the raw Postgres port 5432 and only allows outbound HTTPS — Neon's
  HTTP query API was used instead of the normal Prisma/pg client). Idempotent: skips any
  Test/Module that already exists rather than duplicating it.

## Deduped before assembly
3 confirmed same-template-different-numbers duplicates were found across the 4 new source
PDFs (via a normalized-text similarity scan, not manual guessing) and one of each pair was
dropped:
- "Raheem bought 9 shirts..." — MayIntA and JuneV2 had the *exact same numbers*, a true
  duplicate, not just a similar template.
- "The cost of renting a piece of construction equipment for up to N days..." — JuneV2 (5
  days/$230/$115) vs DecIntB (10 days/$370/$185), same verbatim template.
- "A proposal for a construction project was included on a city election ballot..." — JuneV2
  (24,500 more) vs DecIntB (66,500 more), same verbatim template.

Many other near-matches flagged by the similarity scan were reviewed and kept as genuinely
different questions — generic SAT stem phrasing like "The function f is defined by f(x) = ...,
what is the value of f(N)?" recurs constantly across real, distinct SAT questions and is not
itself a duplicate signal.

## Known gaps / things to review before publishing
- **Test 4 Module 2 (Easy)** was short 1 question (26/27, missing a Transitions item); filled
  with 1 question borrowed from Test 5's EBRW pool (Nov2023 #23, Henry James), verified unique
  against everything already in Test 3/4.
- **4 R&W questions reference a real graph image not available in this environment**
  (`test4|RW_M2_EASY` idx10 line graph, `test4|RW_M2_HARD` idx10 bar graph, plus 2 more with
  fuller diagram-description text) — these were kept (not dropped) with the diagram's text
  description inserted as an italic note below the passage instead of a rendered chart. This
  preserves the question's answerability but is not a faithful visual reproduction of the
  original. Consider replacing with a real chart/image later.
- **~16 of 132 Math stems** fell back to plain (unstyled) text instead of full KaTeX
  rendering, because the automatic LaTeX-wrapping safety check judged the wrap attempt
  structurally risky for that specific stem (e.g. exponent expressions starting with a
  parenthesis, like `(x - 4)^2 + (y + 3)^2 = 16`) and intentionally backed off rather than
  risk shipping broken math rendering. The content and correct answers are unaffected — these
  just display as plain text instead of italicized math. Search `full_build.json` for stems
  without `\(` that contain digits to find the exact list.
- **4 Math questions carry an `APPROXIMATE` verification note** (graph/line reading done
  visually, not from precise pixel data) — inherited from `content-pool/new-source-transcripts/`.
  Search that directory's JSON files for `"APPROXIMATE"` to find them.
- **0 Explanation rows** exist for any Test 3/4 question (same known gap as Test 1) — not
  filled in this pass.
- Both tests are **DRAFT**, not PUBLISHED. Spot-check in the admin panel before flipping the
  status.
