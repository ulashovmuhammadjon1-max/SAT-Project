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

## Follow-up pass: prose "tables"/"graphs", a spacing bug, and real content defects (this session, continued)
User reported "large texts written without spacing," "incorrect numbers," and "lack of graphs" in
the Math sections specifically. A full audit of all 132 Test 3/4 Math questions (not just the 16
already fixed) turned up several distinct, real problems, all now fixed in both DBs and this JSON:

**1. A systemic KaTeX spacing bug — 30 answer choices across Test 3/4 Math (0 in Test 1/2).**
`mathify2.py`'s whole-string-wrap trigger (any digit/operator) fired on ordinary English
interpretation sentences that merely *contained* a number, e.g.
`"The mean of the 14 data points is greater than..."`. Wrapped in `\( ... \)`, KaTeX renders
consecutive words with no spacing (math mode doesn't preserve whitespace between bare tokens),
producing exactly the "words jammed together" the user described —
`Themeanofthe14datapointsisgreater...`. Fix: detect any choice that's fully wrapped in `\( \)`
but contains 5+ real English words plus a common function word (the/is/of/and/etc.) — that's
prose, not math — and strip the wrapper back to plain `<p>` text. Found and fixed identically on
both local and production (30 on each, exact same set, confirming it's a build-time defect, not
drift between environments).

**2. 9 questions describing real tabular data as run-on prose instead of a `<table>`.** E.g. "The
table shows the frequency of values in a data set: Value 13 freq 8; Value 20 freq 1; Value 27
freq 8; Value 34 freq 6." Converted all 9 to real `<table>` HTML using the standard style block
(cars/passengers linear-relationship data, rectangle area/perimeter, quadratic x/f(x) triples, age
distribution, value/frequency, pole-vault exponential x/h(x), and 5-task timing data). Two of
these ("which table..." questions) needed their **answer choices** converted to small tables too
— those had been mathify'd into a broken `\(x:0,1,\frac{2}{y}:0,45,47\)`, where the auto-converter
mistook a literal `x-col / y-col` separator for a fraction bar. Now real per-choice tables.

**3. 4 questions describing a graph/figure with zero image anywhere** (distinct from the 7 images
already added in the prior pass — these are 4 *additional* ones that prior pass missed): a dot
plot (orbital periods + outlier), a scatterplot (y-intercept -2.6, slope 1.9), a line+parabola
system (y=3x, y=x²-6), and a 30-60-90 triangle. Built matplotlib images for all 4, consistent with
the already-verified correct answers. The 30-60-90 triangle's stem was also confusingly worded
("the side adjacent to the 30 degree angle (opposite the right angle vertex)") — rewrote it
plainly once the actual geometry was worked out (the leg adjacent to 30°, i.e. opposite the 60°
angle, is 66 — not the hypotenuse; solving that way is the only reading that matches answer B).

**4. Real correctness defects found while checking the math, not just formatting:**
- **Test 3 Math Module 1 Q16** (cars/passengers linear equation) — choices A (`35c - p = -6`) and
  D (`p - 35c = 6`) were algebraically identical (both reduce to `p = 35c + 6`), so two of the four
  "different" answer choices were actually the same equation. Replaced D with a genuine (wrong)
  distractor.
- **Test 4 Math Module 2 Easy Q6** (age-distribution probability) — choices C and D were shipped
  as the literal string `"[cut off in source PDF]"`, i.e. a 4-choice question with only 2 real
  choices. Added two original, verification-consistent distractor values (0.28, 0.38 — plausible
  results of common conditioning/numerator errors); A (0.21) and B (0.29, correct) were already
  real.
- **Test 3 Math Module 1 Q2** (similar-triangles area) — the transcript's own verification note
  flagged this as unresolvable: sympy on the transcribed area (170) gives 170/9, but the parsed
  official key implies 149/9, and the transcriber suspected the area value itself may have been
  misread with no independent source (no circled selection, no PDF image on file) to break the
  tie. Rather than ship a coinflip FREE_RESPONSE answer, replaced it with a fresh, sympy-verified
  similar-triangles question (side ratio 4, area 15 → 240) testing the identical skill.
- **Test 3 Math Module 2 Easy Q15** (`4(x+3) = 3(x+3) + 56`) — the transcript's own note already
  flagged this as likely mistranscribed: solving the equation as given yields x+3=56, but both the
  official key and the source's own circled student answer independently say 53 — and since
  `4(x+3) = 3(x+3) + D` reduces to exactly `x+3 = D`, the stem's "56" is inconsistent with its own
  corroborated answer. Corrected the stem's constant to 53, making the equation self-consistent
  with the answer already in place.
  (Caught and self-corrected mid-fix: this question sits immediately next to a different, unrelated
  question that also happens to be of the form "4(x+3) = 3(x+3) + N" — Module 2 Easy Q14, the
  exponential-y-intercept question from the earlier 16-question fix. An initial pass targeted Q14
  by a hardcoded position instead of Q15, briefly overwriting the already-correct Q14 content in
  both DBs. Caught immediately via a content-substring re-check against the source, and both
  questions were restored/fixed correctly before this JSON was synced or anything was committed.)

All fixes were verified in the actual exam-taking interface (not just the admin preview) via a
seeded local `Attempt` across all 6 affected Math modules, screenshotted question-by-question,
then applied identically to production (matched by `(test title, subject, module order,
difficulty, question order)` via the Neon HTTP driver — production question IDs differ from
local, so nothing here is matched on `(source, num)` per the standing rule) and spot-verified by
re-fetching each updated stem and confirming it contains the expected content before this file was
saved.

**Still not resolved, unrelated to this pass**: the 2 genuinely data-less R&W questions (Bologna
survey table, science-fair line graph — see above), Test 5's content gaps, and 0 Explanation rows
across Test 1-4.

## Follow-up pass: unconverted fractions/exponents and crammed systems of equations (this session, continued again)
User pointed at specific questions across Test 3/4 Math (Module 1 Q9/Q13, Module 2 Easy Q17/Q21,
plus several in Test 4 Module 1) reporting bad LaTeX and systems of equations "written in one big
line" instead of stacked. A full regex sweep of all 132 Math questions (stems + choices, images
excluded to avoid false positives on base64 data) for raw un-converted `/` division and `^`
exponents outside any `\(...\)` span, plus a separate sweep for stems containing 2+ separate
`\(...\)` equation spans, found 20 more real defects on top of everything already fixed above —
`mathify2.py` had still more edge cases than the two rounds before this one caught:

- **9 stems/choice-sets with a raw `/` instead of `\frac{}{}`**: a slope "1/8", a triangle-ratio
  "4/3" (appeared twice in one stem), an angle "(k/2) degrees" not even wrapped in math mode at
  all, `25 · pi/2`-style trig choices, `8(cx+3)/5` in an equation, 4 answer choices expressing a
  variable as a raw-slash ratio, 3 more answer choices with the same pattern, a triangle cosine
  "60/61", and a compound fraction equation `6(7-x)/5` / `4(7-x)/3`. All converted to real
  `\frac{}{}`.
- **1 badly broken math wrapper**: `\(f(x) = 3\),000(0.75)^x` — the auto-converter closed the
  `\(...\)` span right after "3" (before the thousands-comma), leaving `,000(0.75)^x` as
  unrendered plain text with a literal caret. Rewrapped as `\(f(x) = 3{,}000(0.75)^x\)`.
- **1 more instance of the "which table" broken-fraction bug** from the previous pass
  (`\(x:3,5,\frac{8}{y}:14,32,59\)`) that the first sweep missed because that pass only checked
  questions whose stem literally said "table" — this one's stem says "inequality," not "table."
  Converted all 4 choices to real per-choice tables, same as the earlier fix.
- **2 short prose-in-math fragments** the previous 30-choice sweep's 5-word threshold missed:
  `\(-1 and 4\)` and `\(0 and 9\)` as answer choices — same class of bug as the spacing fix above,
  just too short to trip the word-count filter. Unwrapped to plain text.
- **7 "crammed" systems of equations** — stems presenting two full equations separated by `; ` on
  a single line (e.g. `\(y = -4x^2 - 47\); \(y = qx - 43\).`) instead of the real SAT's stacked,
  one-equation-per-line layout. Reformatted all 7 (6 stems + 1 question's 4 answer choices, each of
  which was itself a 2-equation system) using `<br/>` between the equations, e.g.
  `\(y = -4x^2 - 47\)<br/>\(y = qx - 43\)`. Only stems containing the literal `"system of"` phrase
  were treated as genuine systems — several other stems matched the "2+ equation spans" scan but
  were ordinary sentences stating two separate facts (e.g. "QR = 16 and TU = 12"), not a system to
  stack, and were correctly left alone.

No correctness/answer-key issues were found in this pass (unlike the previous one) — this batch
was pure rendering/formatting, and every choice's marked-correct answer was re-verified against
its own math (e.g. Q21's `1/x + 1/(x-9) = 4/(x^2-9x)` reduces to `x = 13/2`, matching the
already-correct D) before touching anything.

All 20 fixes were verified in the exam-taking interface via a fresh seeded `Attempt` per module
(screenshotted individually), then applied to production using the same
`(test title, subject, module order, difficulty, question order)` matching as before, with each
production write additionally gated on a content-substring assertion against the fetched row
before update (not just before the whole batch) — every one passed on the first attempt, so
nothing here required an in-flight correction like the digit-fix mix-up in the previous pass.
