# Test 5 build — SHIPPED (published to production)

## Status
| Module | Source | State |
|---|---|---|
| Math M2 **Easy** | **Original, authored here** | ✅ 22/22 written, sympy-verified, deduped |
| Math M1 | Oct IntB PDF (p51–72) | ✅ 22/22 transcribed, 22/22 sympy-verified |
| Math M2 Hard | Oct USB PDF (p76–97) | ✅ 22 transcribed, 19 usable (3 rejected) |
| R&W M1 / M2E / M2H | banked pool + October top-ups | ✅ 27/27/27 — all 81 answers verified by hand |

**Live in production as `Test 5` (`5537a8d3-602e-43ab-b973-1bc607d3f37c`), status `PUBLISHED`.**
147 questions: R&W 27/27/27, Math 22/22/22.

## `t5_math_m2easy.json` — 22 original questions
Written by hand per the standing rules in `CLAUDE.md` (Test 1/2 house style, no
auto-converter). Every one carries a `check` field recording how its answer was derived.

**Verification performed:**
- All 22 answers independently re-derived with sympy — all agree with the recorded answer.
- House-style audit clean: no `<p>` wrappers, no bare `sin`/`cos`/`log` inside math mode, no
  prose wrapped in math mode, no missing spaces around inline spans, no raw `/` division, and
  every question that mentions a table actually has one.
- 3 free-response (the cap), 19 multiple-choice.
- Domain mix 8 ALG / 6 ADV / 4 PSDA / 4 GT, matching Test 1's live proportions.

**Duplicate check** against all 264 Math questions in Tests 1–4 (production). String similarity
alone is useless here — short SAT stems share so much boilerplate ("what is the value of…",
"which expression is equivalent to…") that unrelated questions score 1.00 once digits are
stripped. Every flagged pair was read by eye. Three were genuine same-template-different-numbers
repeats and were **replaced**:
- Q5 was "Line k has slope -2 and passes through (0,7); which equation defines line k?" —
  the same template as Test 3 M2H Q16 *and* as Oct IntB Math M1 Q1, which is still to be
  transcribed. Now: "For the linear function g, g(0)=9 and g(1)=14, what is g(4)?"
- Q19 was "In triangle ABC, angle A is 40° and angle B is 75°, find angle C" — Test 2 M1S Q21
  is the same sentence with 42° and 65°. Now an isosceles-triangle question.
- Q9 was `x^7/x^3`, which reduces to `x^4` — the same concept *and the same answer* as
  Test 2 M2H Q11 (`x^-3 * x^7`). Now `12x^5/(4x^2)`, which also exercises the coefficient.

## `octintb_math_m1.json` — 22 questions from the Oct IntB source
Transcribed page by page from the screenshot images (the PDF has no text layer, and OCR mangles
every expression — `y = -8x + 60` comes out as `y = —82 + 60` — so each page was read visually).

**Verification: 22/22.** For every question the recorded answer, an independent sympy
re-derivation, and the PDF's own official answer key all agree. That is a much better result
than the earlier EliteXSAT sources, where one module had 10 of 22 answers conflicting with
verification — this source's key is trustworthy.

Transcribing also resolved an ambiguity in the key page: the entry `21.340.8` is Q21 = 340.8
(the ramp question), not two separate values.

**Figures.** Two questions carry a real figure, cropped from the source page rather than
described in prose (`figures/q08_scatterplot.png`, `figures/q21_ramp.png`). The scatterplot
crop independently confirms Q8's answer: the line runs from about (0,27) to (4,4), a slope of
-5.75, closest to -6.

**One flagged item.** Q17's choice D sits below the page fold and is not captured in the
source. It is recorded as `0.50` because the arithmetic is forced (22/44) and the official key
says D, but the `FLAG` field marks it for confirmation before publishing.

**Free-response balance.** This source module has 6 FR and 16 MC. The standing rules cap a
module at 3 FR (Test 1 ships 19 MC + 3 FR), so Test 5's Math M1 cannot be this module verbatim
— drop 3 FR and top up with MC items from the Oct USB / Oct USC Math M1 pools.

## `octusb_math_m2.json` — 22 questions from the Oct USB source, **19 usable**

Transcribed the same way (visual read per page). Unlike the Oct IntB module, this source's
answer key is **not** fully reliable — three questions were rejected rather than shipped:

- **Q4 (parallel lines cut by a transversal) — CONFLICT.** The key says A (26), which needs
  y=61. Zooming the figure shows 61° at the **upper-right** angle of line q and y° at the
  **upper-left** angle of line r. Those are supplementary, not equal, so y=119 and x=55
  (choice C). The student who sat the test also chose C. Rejected.
- **Q17 (graph of y = f(x)+2) — CONFLICT.** The key says D. Reading the plotted curve at four
  lattice points gives y(0)=4, y(1)=3, y(2)=1, y(3)=-3, x-intercept ≈2.35 — exactly
  `-2^x + 5`. Since the plotted curve *is* y=f(x)+2, f(x) = `-2^x + 3` (choice B). Choice D
  would need a y-intercept of 6; the graph plainly shows 4. Rejected.
- **Q10 (stamp-age frequency table) — INCOMPLETE.** The test-taker had scrolled, so only the
  last table rows survive. The missing rows cannot be reconstructed, so the answer cannot be
  verified. Rejected.

The other 19 all verify: recorded answer, independent re-derivation, and the official key agree.

**A resolution worth recording.** Q22's equation reads `1/(cx) = x/76 + 1/c`. At the capture's
native resolution the 76 is indistinguishable from 70, and 70 would give c = -17.5 and appear
to contradict the key. Zooming 7× showed 76, which gives exactly the key's -19. Every
expression in these screenshot sources needs to be read at zoom, not at page scale.

**Reliability note for future builds:** Oct IntB's key was 22/22 correct. Oct USB's key has at
least two errors. Trust neither blindly — verify every answer independently.

## `test5_math.json` — the assembled Math side (66 questions), built by `assemble_math.py`

| Module | Shape | Sources |
|---|---|---|
| Math M1 | 19 MC + 3 FR | Oct IntB (17) + Oct USC (5) |
| Math M2 Hard | 19 MC + 3 FR | Oct USB (14) + Oct USC (8) |
| Math M2 Easy | 19 MC + 3 FR | **all 22 originally authored** |

**Duplicate rejections.** The first assembly was checked against all 264 Math questions live in
Tests 1–4 and four picks were thrown out and replaced:
- Oct IntB M1 Q12 (ant-colony larvae model) scored **1.00** — an *exact* duplicate of
  Test 3 M2E Q22.
- Oct USB M2 Q1 (`f(x)=10x²-38x-150`, find `f(0)`) vs Test 3 M2H Q12 (`10x²-40x-150`) — the
  same question with one digit changed.
- Oct IntB M1 Q1 (line with slope m through a point) vs Test 3 M2E Q19 — same template.
- Oct USC M2 Q2 ("how many distinct real solutions") vs Test 4 M2E Q10 — same template.

Three more Oct USC questions were rejected before they ever entered the pool for the same
reason (see `rejectedAsTemplateRepeats` in `octusc_supplement.json`).

After replacement: **0 pairs at ≥0.96** either internally or against Tests 1–4. The residual
0.93–0.95 scores are unrelated mathematics sharing SAT boilerplate ("Which expression is
equivalent to…", "The function f is defined by…") and were each read by eye.

**Audit at assembly time is clean**: no `<p>`-wrapped stems, no bare `sin`/`cos`/`log` in math
mode, no prose in math mode, no missing spaces around inline spans, no raw `/` division, every
`correctAnswerFR` a JSON array string, every question that mentions a figure or table actually
has one (6 figures cropped from the source pages, 4 real data tables).

**Known deviation:** Math M2 Hard's domain mix is ALG 10 / ADV 7 / GT 3 / PSDA 2, more
algebra-heavy than Test 1's ~8/6/4/4. That is what the verified hard-module supply allowed
after the duplicate rejections; the other two modules match Test 1's proportions closely.

## `format_rw.py` / `test5_rw_formatted.json` — the R&W formatting pass

Converts the banked pool's raw text into the markup Test 1/2 use: bulleted student notes become
real `<ul><li>`, data tables become real `<table>` with the standard style block,
`[UNDERLINED: …]` becomes `<u>`, `*italics*` becomes `<em>`.

**The five data tables are hand-written, not parsed.** The source stores them on a single line
with implicit row breaks — `… | Fungi | Insects Lithuania | 8 | …`, where `Insects Lithuania` is
the last header cell running straight into the first row label. No regex can split that
reliably, so all five tables and the prose that follows them are written out explicitly and each
one's answer was re-checked against the data (e.g. Poland is indeed the only country in the
tree-threat table with more insect than fungus species).

**Four questions dropped as unshippable**, with reasons recorded in `UNUSABLE`:
- two Command-of-Evidence questions whose line graph exists only as a prose description because
  the source PDF was not kept — shipping them would violate the no-prose-figures rule;
- a Boundaries question whose choices A and B differ only by a comma that a watermark obscured;
- a question whose choice D was hidden behind a cursor icon and transcribed by inference.

**Ordering check:** none of the three modules leaks a reading-domain question after the writing
block has started — the hard rule in CLAUDE.md holds. Within-block ordering is re-sorted to the
mandated sequence at assembly time.

**Still outstanding:** 11 top-up questions (4 / 6 / 1) to reach 27 per module. These will come
from the October sources, which carry reliable answer keys, rather than the August PDFs, whose
only answer marking is an inline highlight that appears to be the crossed-out state rather than
the selected one.

## R&W answer audit — resolved, and what it found

The blocker that held this build back was that the banked R&W pool's recorded answers come from
source answer keys that had already proved unreliable. All 81 were therefore re-answered by
hand, from the question text alone, before the recorded answer was looked at. Full detail and
per-question reasoning: `rw_answer_audit.md`.

**6 of 81 recorded answers were wrong** (7.4%), all corrected in `ANSWER_FIXES`:

| Module | Order | Recorded | Correct |
|---|---|---|---|
| RW_M1 | 10 | D | **B** (tree species — D contradicts its own table) |
| RW_M1 | 15 | C | **A** (`however. All` — C and D are comma splices) |
| RW_M2_EASY | 8 | B | **C** (hyperpop — B says the opposite of the text) |
| RW_M2_HARD | 11 | A | **B** (lake ice — A is a decrease, the claim is an increase) |
| RW_M2_HARD | 14 | A | **C** (net CO₂ — A's two effects pull in opposite directions) |
| RW_M2_HARD | 16 | C | **B** (`measurement used` — C strands a fragment) |

Only 2 of the 6 (RW_M1 10, RW_M2_HARD 11) were catchable from a printed data table. The other 4
required reading and reasoning the question — i.e. the mechanical check alone would have shipped
four wrong answers, which is exactly why the full pass was worth doing.

**Two more questions were dropped as unrepairable and replaced** (both are in `UNUSABLE` with
the reason; replacements are hand-transcribed from the October IntB page images, each carrying
the same skill so the modules' domain mix and ordering are unchanged):
- RW_M1 Nov2023 16 (theremin) — the stem was mistranscribed from a neighbouring Transitions
  question while all four choices are punctuation variants. Replaced by OctIntB M1 Q21
  (Boundaries, answer D).
- RW_M2_HARD Nov2023 13 (Persad) — asks which choice "best describes data from the table", but
  no table survives and the transcript kept none of its numbers. Replaced by OctIntB M2 Q9
  (Command of Evidence, answer C).

That makes 6 dropped of 87 banked, all backfilled; every module ships at a full 27.

**One skill mislabel corrected** (`SKILL_FIXES`): RW_M2_HARD order 9 was filed as Central Ideas
and Details, but its stem is "It can most reasonably be inferred from the text that…" — the
canonical Inferences phrasing. This matters twice: skill drives the question bank's filters, and
module ordering is derived from the skill.

**Reliability note for future builds.** The October papers' *Math* keys were fine (Oct IntB
scored 22/22). Their *R&W* keys were not, and neither was the banked R&W pool. Treat an R&W
answer key as a hint, not an authority; the Math side of this build had all 66 answers
independently re-derived and rejected the ones whose key disagreed.

## Verification performed before publishing

- Local DB: deleted and re-inserted the full 147, then swept every question of R&W M1 and Math
  M1 in the real `/exam/{attemptId}` interface via Playwright — zero raw-markup hits (no stray
  `\(`, `\frac`, `&deg;`, `<p>`, markdown asterisks), zero console errors, figures and KaTeX
  rendering correctly.
- Production DB after insert: every MC question has exactly 4 choices and exactly 1 marked
  correct; all 9 `correctAnswerFR` values are JSON-encoded arrays; every R&W question has a
  passage; 6 questions carry an image; module time limits and `adaptiveThresholdPct` match
  Test 1's shape.
- All 6 corrected answers and both replacements re-checked in production **by content
  substring**, not by hardcoded position — the two dropped questions confirmed absent.
- satforge.org itself: Test 5 lists on `/tests` (147 questions, ~201 min, Adaptive), and a
  throwaway attempt confirmed both an R&W and a Math question render end to end on the live
  site (KaTeX server-rendered, base64 figures present). The attempt was deleted afterwards.

## Tooling kept here
- `dump_existing_questions.mjs` — dumps every question already in production so new content can
  be deduped against the whole database, not just the test being built. Reads the connection
  string from `PRODDB` in the environment; the string is never written to a file.
  `PRODDB='postgresql://...' node dump_existing_questions.mjs MATH out.json`
- `format_rw.py` → `test5_rw_formatted.json`, `assemble_rw.py` → `test5_rw.json`,
  `assemble_math.py` → `test5_math.json` — the three build steps, each re-runnable.
- `insert_test5.mjs` — idempotent insert (skips any Test/Module that already exists). Picks the
  driver from the URL: `pg` for a localhost dry run, Neon's HTTP API for production, because the
  sandbox blocks port 5432. `--publish` flips the status; without it the test lands as DRAFT.
- `seed_attempt.mjs` — seeds a throwaway Attempt so a built test can be walked in the real
  `/exam/{attemptId}` interface, which CLAUDE.md requires before shipping.

## Notes for the next session
- Test 5 is live and PUBLISHED in production; `insert_test5.mjs` is idempotent, so re-running it
  is a no-op rather than a duplicate.
- `dump_rw.py "<module>" <lo> <hi>` renders R&W questions readable for an answer audit. Use it
  before shipping any future R&W module — it is what caught 4 of this build's 6 wrong answers.
- Test 5 ships 0 `Explanation` rows, same as Tests 1–4. Still a real content gap across the
  whole platform.
- Two Math questions carry a `table` field rendered with the standard `<table>` style block from
  `CLAUDE.md` at insert time.
