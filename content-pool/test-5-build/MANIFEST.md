# Test 5 build — in progress

## Status
| Module | Source | State |
|---|---|---|
| Math M2 **Easy** | **Original, authored here** | ✅ 22/22 written, sympy-verified, deduped |
| Math M1 | Oct IntB PDF (p51–72) | ⬜ not transcribed |
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

## Tooling kept here
- `dump_existing_questions.mjs` — dumps every question already in production so new content can
  be deduped against the whole database, not just the test being built. Reads the connection
  string from `PRODDB` in the environment; the string is never written to a file.
  `PRODDB='postgresql://...' node dump_existing_questions.mjs MATH out.json`

## Notes for the next session
- Two questions (Q8, Q18) carry a `table` field that must be rendered with the standard
  `<table>` style block from `CLAUDE.md` at insert time, not as prose.
- Nothing here is in the database yet. Test 5 does not exist as a `Test` row.
