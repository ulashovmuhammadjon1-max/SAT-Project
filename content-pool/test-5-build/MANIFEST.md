# Test 5 build — in progress

## Status
| Module | Source | State |
|---|---|---|
| Math M2 **Easy** | **Original, authored here** | ✅ 22/22 written, sympy-verified, deduped |
| Math M1 | Oct IntB PDF (p51–72) | ✅ 22/22 transcribed, 22/22 sympy-verified |
| Math M2 Hard | Oct USB PDF (p76–97) | ⬜ not transcribed |
| R&W M1 / M2E / M2H | `content-pool/test-3-4-5-reading-writing/` (74 banked) + Aug USC | ⬜ needs the HTML formatting pass |

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

## Tooling kept here
- `dump_existing_questions.mjs` — dumps every question already in production so new content can
  be deduped against the whole database, not just the test being built. Reads the connection
  string from `PRODDB` in the environment; the string is never written to a file.
  `PRODDB='postgresql://...' node dump_existing_questions.mjs MATH out.json`

## Notes for the next session
- Two questions (Q8, Q18) carry a `table` field that must be rendered with the standard
  `<table>` style block from `CLAUDE.md` at insert time, not as prose.
- Nothing here is in the database yet. Test 5 does not exist as a `Test` row.
