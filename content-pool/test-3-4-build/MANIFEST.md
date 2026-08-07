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
- **~16 of 132 Math stems** fell back to plain (unstyled) text instead of full KaTeX
  rendering, because the automatic LaTeX-wrapping safety check judged the wrap attempt
  structurally risky for that specific stem (e.g. exponent expressions starting with a
  parenthesis, like `(x - 4)^2 + (y + 3)^2 = 16`) and intentionally backed off rather than
  risk shipping broken math rendering. The content and correct answers are unaffected — these
  just display as plain text instead of italicized math. Search `full_build.json` for stems
  without `\(` that contain digits to find the exact list.
- **0 Explanation rows** exist for any Test 3/4 question (same known gap as Test 1) — not
  filled in this pass.
- Both tests are **DRAFT**, not PUBLISHED. Spot-check in the admin panel before flipping the
  status.

## Follow-up pass: real chart images + a live rendering check (this session, continued)
Set up a local dev environment (local Postgres via `apt install postgresql` — Docker's daemon
isn't available in this sandbox, so `docker-compose.yml` doesn't work here; Neon's HTTP driver
for the same reason on the production side, see above) seeded with the exact `full_build.json`
content, logged into the admin panel with Playwright, and visually confirmed rendering for a
KaTeX/image question, a table question, and a bullet-list question — all correct.

**Real chart images (not text descriptions) were generated and attached to `Question.imageUrl`**
for 7 questions where enough real data existed to build an accurate chart, via matplotlib,
embedded as base64 PNG data URIs (same convention Test 1 uses), applied to both the local dev
DB and production:
- Test 3: population-census exponential curve, shaded-inequality region, `y=f(x)-9` line,
  scatterplot with line of best fit.
- Test 4: y-intercept-12 line, population-growth exponential curve, and the lizard
  escaping-vs-pursuing-speed bar chart (built from the real approximate bin values already on
  record in `content-pool/new-source-transcripts/`).

Each chart was built from the specific equation/data already verified as correct for that
question (not a fresh guess) — e.g. the shaded-inequality chart plots exactly `y = -2x + 12`,
the same line used to verify `(8,0)` as the correct answer, so the image and the marked answer
are guaranteed consistent with each other.

**Important schema note found in the process**: the admin question editor's "Figure" upload
and the student preview both read `Question.imageUrl`, not `Passage.imageUrl` — an R&W
question's diagram must be attached to the *question*, not the passage that owns it, even
though conceptually a shared-passage diagram might seem passage-level. (`Passage.imageUrl`
exists in the schema but nothing in the app currently renders it.)

**Also fixed while reviewing rendering**: Test 3's March_IntB scatterplot question
("scatterplot ... line of best fit") had two identical answer choices (A and C both
`y = -2.6 + 1.9x`), a transcription defect flagged but not resolved when the content was
originally transcribed. The other 3 choices are exactly the 4 sign-permutations of
`(±2.6, ±1.9x)` — B and D are already 2 of the other 3 permutations — so the missing 4th
permutation (`y = 2.6 + 1.9x`, the `++` case) was used to replace the duplicate C rather than
guessing at unrelated wording. Also corrected the stem's `(0,3)` y-intercept description,
which contradicted the answer choices' actual `-2.6` intercept.

### Still not resolved — genuinely missing data, not a rendering problem
Two R&W questions reference a real graph/table with **no usable data on record** (the
`diagram` field for both is just a placeholder note like "needs image extraction/vision
check," not real transcribed values), so no accurate image could be built for them without
inventing numbers:
- **Test 3** — the Bologna urban-agriculture survey question ("Which choice best describes
  data in the table that support the city planner's conclusion?"). Source: `May`, R&W Module 2
  Hard, original num 14.
- **Test 4** — the science-fair submissions line graph ("Which choice most effectively uses
  data from the graph to support the underlined claim?"). Source: `Nov2023`, R&W Module 2
  Easy, original num 11. One data point is confirmed (~285 medicine/health submissions in
  2019, which is literally the correct choice's own text) but the other 3 topics' values
  across 2016-2019 are not on record, so a 4-line chart can't be built without fabricating 3 of
  4 series.

Both currently still show the plain-text diagram-description note (not an image) as a
placeholder. Fabricating plausible-looking chart data for either would risk shipping a chart
that's actually wrong or that doesn't uniquely support the marked correct answer — worse than
the current text note. These need either the original source PDF page image, or a decision to
drop/replace the question.

## Follow-up pass: 16 Math stems shipped as plain text instead of KaTeX (this session, continued)
User caught this live on production (screenshot of Test 3 Math Module 1 Q1 rendering
`(x - 4)^2 + (y + 3)^2 = 16` as literal plain text instead of styled math, unlike Test 1/2). Root
cause: these 16 stems fell through `mathify2.py`'s `_is_structurally_suspicious()` safety net
during the original build and were inserted with un-converted plain-text math syntax.

An initial broad regex ("any digit-containing stem lacking `\(`") returned 69 candidates, mostly
false positives (plain narrative word problems that never needed math wrapping, e.g. "Javier
deposits $45..."). Narrowed to a precise check for genuinely unconverted math syntax — unwrapped
`=`, `^\d`, `^{`, `sqrt(`, or `*` patterns sitting *outside* any existing `\(...\)` span — which
correctly isolated exactly 16 real cases, matching the user's screenshot.

Each of the 16 stems was hand-rewritten with `\(...\)` KaTeX delimiters (balance-verified) rather
than re-run through the auto-converter, per the rule above about not blindly regenerating stems.
Fixes were applied directly via three separate UPDATEs, all matched on a unique stem substring
(never `(source, num)`):
- Production DB, via the Neon HTTP driver, matched by question `id` (UUIDs) — confirmed
  "updated 16 questions."
- Local dev DB, via Prisma, matched by stem substring since local question IDs differ from
  production — confirmed "updated 16 of 16."
- `full_build.json` itself (this repo), matched by the same stem substrings — confirmed 16 of 16
  patched, so the source artifact now agrees with both live databases.

Affected questions (10 in Test 3, 6 in Test 4): circle-center and point-on-circle equations,
a projectile-height quadratic, two "equivalent expression" polynomial questions, an absolute-value
equation, an exponential y-intercept identity question, a linear ant-colony model, a triangle-area
equation, an isotope half-life exponential, a second absolute-value equation, a linear gas-tank
model, a proportional-relationship question, a solutions-count quadratic, a population exponential
model, and an equilateral-triangle side-length question.

Verified live in the exam-taking interface itself (not just the admin editor preview): seeded a
local `Attempt`/`ModuleAttempt` pointing at Test 3 Math Module 1 and loaded `/exam/{attemptId}` as
the student user — Q1's circle equation now renders as proper KaTeX (`.katex` elements present,
no literal `^2` in the stem), matching Test 1/2's exam styling.
