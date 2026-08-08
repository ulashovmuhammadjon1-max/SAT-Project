# Test 7 — built, verified, NOT published

147 questions. R&W 27/27/27 + Math 22/22/22. Awaiting review of
`SATForge-Practice-Test-7-review.pdf`; nothing has been written to any database.

## The brief

> make one complete practice test without using any previous questions. but see
> all practice tests too see how you should structure and the difficulty ui
> should use. then send me the whole pdf before publishing

"No previous questions" is read as: nothing that appears in Tests 1–6, checked
programmatically rather than assumed.

## What the existing six tests actually do

Measured, not eyeballed. Two findings shaped this build.

**Every test is the same shape** — R&W 27/27/27, Math 22/22/22, 3 free-response
per Math module — and the domain mix across all 882 live questions is close to
the real blueprint:

| | | | |
|---|---|---|---|
| Math | ALG 33.3% | ADV 30.1% | PSDA 19.7% / GT 16.9% |
| R&W | INI 28.6% | CAS 25.3% | SEC 23.0% / EOI 23.0% |

Test 7 matches this: Math M1 is 8 ALG / 7 ADV / 4 PSDA / 3 GT, M2 Hard is
6 / 8 / 4 / 4.

**The difficulty field is broken in Tests 3–6.** Tests 1 and 2 stamp each
question's own `difficulty` to match its module — an EASY module's questions are
`EASY`, a HARD module's are `HARD`. Tests 3, 4, 5 and 6 left *every* question
`MEDIUM`, including all 132 questions sitting in Easy and Hard modules. That is
the difficulty UI leaking: the Question Bank shows a `MEDIUM` badge on those
questions and its difficulty filter cannot find them. Test 7 follows the Test 1/2
convention. **Tests 3–6 still carry the wrong values and would need a separate
backfill** — not done here, since it touches published content.

## Provenance — how "nothing reused" is enforced

| Module | Source | Count |
|---|---|---|
| Math M1 (Standard) | authored, `math_test7.py` | 22 |
| Math M2 (Hard) | authored, `math_test7.py` | 22 |
| Math M2 (Easy) | authored, `math_m2easy.TEST7` | 22 |
| R&W ×3 | pool never used by any published test | 79 |
| R&W | authored, `rw_test7_extra.py` | 2 |

Every R&W item is checked against the exact refs Test 6 consumed before it is
eligible. The pool held 98 unused items against a need for 81; the only block
that ran short was Command of Evidence, by one, so two were authored.

## Verification

`verify_math_test7.py` — three independent passes, all green:

1. **Answers re-derived with sympy** from the question itself, never read off the
   `check` note. A wrong note and a wrong key agree with each other; only an
   independent derivation separates them. This caught two real errors — a
   perpendicular-line intercept keyed to −3 when it is 3, and a radical equation
   whose extraneous root had not been discarded.
2. **House style** — the Test 1/2 rules plus the DB-wide rendering checks: no
   bare `^`, `sqrt(`, `*`-as-multiply, slash fraction, ASCII `!=`/`<=`, LaTeX
   macro outside a math span, prose inside math mode, or `<p>`-wrapped stem.
3. **Template dedupe against all 396 live Math stems**, on a signature that
   strips numbers and LaTeX so a template reused with new values is caught, not
   just an exact duplicate. **The first run rejected 16 of 44** — several at 1.00,
   including "which expression is equivalent to (x²−16)/(x+4)" against Test 2's
   (x²−9)/(x−3). Those were rewritten with genuinely different framings rather
   than by loosening the threshold. Highest remaining similarity: **0.73**,
   against a 0.75 limit.

`assemble_test7.py` re-checks the structure: 147 questions, no duplicate refs,
exactly one key per MC question, every `correctAnswerFR` a JSON array, 3
free-response per Math module, and for each R&W module a monotonic block
sequence with the writing block opening at question 15.

Two verifier bugs were found and fixed while it ran, worth recording because
both would have passed bad content silently:

- The LaTeX-to-sympy helper applied `\frac` before exponents, so
  `\frac{4a^{3}}{b^{4}}` — braces nested inside the numerator — never matched the
  non-recursive `\frac` pattern and fell through to a string comparison.
- `symbols("y", positive=True)` is a *different* symbol from `symbols("y")`, so
  a derivation and its answer choice compared unequal despite being identical.

## Files

| | |
|---|---|
| `math_test7.py` | 44 authored Math questions, M1 and M2 Hard |
| `rw_test7_extra.py` | 2 authored Command of Evidence items |
| `verify_math_test7.py` | the three verification passes |
| `assemble_test7.py` | pool selection, block ordering, structural report |
| `make_pdf.py` | renders `test7.json` to the review PDF via KaTeX |
| `test7.json` | the assembled test, insert-ready |
| `SATForge-Practice-Test-7-review.pdf` | 71 pages, every question with key and reasoning |

## Still to do

- Review the PDF and approve.
- Insert as `DRAFT`, run `audit_math_rendering.mjs` against local and
  production, verify in the real exam interface, then publish from the admin
  panel.
- Separately: backfill the per-question difficulty on Tests 3–6.
