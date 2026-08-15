# SAToplam Math 2.0 and 3.0 — parsed, not yet imported

Two editions of the "Real Exam Questions Collection" Math book from the same
publisher as the R&W books already in the bank (`@satashkent`).

    python3 parse_math.py math_parsed.json ma2=<pdf> … ma3=<pdf> …

## What is in `math_parsed.json`

| | |
|---|---:|
| questions | **1,641** |
| — Math 2.0 (383pp, complete) | 1,223 |
| — Math 3.0 (132pp, complete) | 418 |
| with an answer from the book's key | 1,593 (97%) |
| multiple choice | 1,177 |
| free response | 464 |
| math survived text extraction | 755 |
| **math needs transcribing by eye** | **886** |

Each record carries `book`, `topic`, `num`, `exam` (the sitting it came from,
e.g. "March US 2025"), `page`, `domain`, `skill`, `body`, `choices`, `key`,
and `needs_vision`.

## Why 886 questions are not ready to import

The book is TeX-typeset, and `pdftotext` returns dependable **structure** and
undependable **mathematics**. An exponent lands on its own line, so `x^2 + y^2`
extracts as `x2` / `+ y2`; a fraction's numerator and denominator become two
lines with the rule dropped entirely, so `-w/(161x)` arrives as `w` then
`161x`.

The parser therefore does not try to rebuild the maths. CLAUDE.md is explicit
that a regex converter reverse-engineering author intent from noisy text was
the root cause of every Test 3/4 Math defect, that each fixing round found a
new edge case, and that the rule is to hand-write the LaTeX per question.
`needs_vision` marks the questions where that is required, detected
structurally: a stranded exponent line, a letter fused to a digit, or a lone
operator line where a fraction rule used to be.

The remaining 755 are ordinary prose-and-numbers questions whose text came out
intact, e.g. "The width of a rectangle is 8 centimeters…". Those can be
imported directly.

## Identity, and keeping these separate

Numbering restarts per topic **within a book**, so identity is
`(book, topic, number)` — both editions have a "Quadratics 1" and they are
different questions. Ids are `satmath-<book>-<topic>-<num>`, and the intended
`Question.source` prefix is `SATMATH:`, distinct from:

- `AUTHORED/…` — the 1,718 Math questions written for this project
- `CB:` — the College Board R&W bank
- `SAT:` — the SAToplam R&W books
- EliteXSAT paper labels — the transcribed Tests 1–5 material

So a query can always tell where a question came from.

## Known gaps and defects

- **30 Areas&Volumes answers missing in Math 2.0.** The key table for that
  section runs 1–42 on book page 381 and continues on page 382, which is one
  page past the last uploaded file. The questions themselves (43–72) are all
  present. 18 further stragglers across other sections bring the unkeyed total
  to 48.
- **11 questions have a key that contradicts their parsed type** — a
  multiple-choice question keyed `13`, or a free-response question keyed `C`.
  Both mean the choice block failed to parse, not that the key is wrong. They
  need reading.
- Book 3 renames three Geometry sections ("Lines and Angles", "Circle", "Area
  and Volume"). They are normalised to book 2's names so a query for "Circles"
  returns both editions. Its answer tables are aliased the same way — until
  they were, 53 keys silently failed to attach, because the key was filed under
  one topic name and the question under another.
- The contents page misspells "Trigonometry" as "Trignometry"; the section
  heading itself is correct, and the heading is what the parser matches.
- One section heading wraps across two printed lines, so what a line-oriented
  scan sees is `Research organizing(Margin of Error;`. That truncated string is
  used as the topic key deliberately, rather than papered over.

## Next step

Transcribe the 886 flagged questions from page images, hand-writing
`\( … \)` and `\frac{}{}` per question, and verify every answer independently
of the book's key — the same gate the explanations pipeline uses, for the same
reason. Then import all 1,641 under `SATMATH:`.
