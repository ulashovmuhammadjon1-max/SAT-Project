# Math transcription brief

You are converting real SAT questions from the SATashkent Math books into
database-ready records. Read this whole file before writing anything.

## What you are doing, per question

Four things, in this order, from the **page image** — never from the extracted
text:

1. **Transcribe** the stem and the answer choices, hand-writing the LaTeX.
2. **Solve it yourself** and record the answer you get.
3. **Assign a difficulty** — EASY, MEDIUM or HARD.
4. **Write an explanation** a stuck student can use.

## Rule 1: the extracted text is not the question

The books are TeX-typeset and text extraction mangles the mathematics.
`x^2 + y^2` comes out as `x2` / `+ y2`; a fraction becomes two lines with the
division rule dropped, so `-w/(161x)` arrives as `w` then `161x`. Four whole
choices routinely collapse onto one line.

So the page image is the source of truth. The extracted text is provided only
to help you find your place on the page. If they disagree, the image wins,
every time.

## Rule 2: the printed answer key is a claim, not the answer

The user reports **a lot of mistakes in these keys**. You are not shown the
key — that is deliberate. Solve the question, record your answer, and let the
verifier compare afterwards. A disagreement is a useful finding that goes to a
human; an explanation written to justify a wrong key teaches a student the
error, which is worse than no explanation at all.

Never reverse-engineer a justification. If your answer is not among the
choices, say so — that is a defective question, not a reason to pick the
closest one.

## Rule 3: LaTeX by hand, never by pattern

This project has been burned by regex-driven text-to-LaTeX conversion; it
caused every Test 3/4 Math defect and each fixing round found a new edge case.
Write the maths out as you read it.

- Inline `\( … \)`, display `\[ … \]`. Never `$…$`, never markdown.
- Fractions are `\frac{}{}` — never `3/5` inside a math span.
- Function names escape: `\sin`, `\cos`, `\tan`, `\log`, `\ln`. Bare `cos(A)`
  renders as three italic letters.
- Leave a space either side of an inline span: `the length of \(AB\) is`.
- Simple arithmetic stays plain text: `17h + 45 = 164`, not a math span.
  Reserve `\( \)` for fractions, exponents, radicals, subscripts.
- Never put prose inside math mode — KaTeX drops the spaces between words.
- `°` and similar go in as HTML entities (`&deg;`), not raw glyphs.
- Systems of equations stack with `<br/>`, never crammed onto one line.
- A real `<table>` for every data table, using the style block in CLAUDE.md.
- If the question depends on a figure you cannot reproduce as a table, do
  **not** describe it in prose — a prose description substitutes for the
  picture and usually leaks the answer. Flag the question as needing a figure
  and move on.

## Rule 4: difficulty

Hard Book questions are all HARD — do not re-judge them. For the other two
books, judge it:

- **EASY** — one step, or direct substitution into a stated relationship. A
  prepared student answers it without writing much down.
- **MEDIUM** — two or three steps, or one step plus a setup that has to be
  read carefully out of a word problem.
- **HARD** — several linked steps, a non-obvious setup, an unusual form, or a
  question where the common approach leads to a trap answer.

Judge the *work required*, not the topic. A quadratic can be easy and a ratio
question can be hard.

## Output

Append **one line per question** to your JSONL, after every single question.
Never batch — if you stop for any reason, everything already appended is safe
and a replacement resumes from the ids in your file.

```
{"id":"…","stem":"…","choices":[{"label":"A","content":"…"},…],
 "answerLabel":"B","answerValue":null,"difficulty":"MEDIUM",
 "whyCorrect":"…","whyWrong":{"A":"…","C":"…","D":"…"},
 "needsFigure":false,"note":""}
```

- `answerLabel` for multiple choice, `answerValue` (a string) for
  free-response. Exactly one of the two.
- `whyCorrect` — the step a stuck student is missing, not a restatement. 2-5
  sentences.
- `whyWrong` — every distractor, keyed by letter, naming the specific error
  that produces it. "This is incorrect" is useless. Omit for free-response.
- `needsFigure` — true if the question refers to a figure you could not
  reproduce.
- `note` — anything wrong with the question itself: two equivalent choices, a
  value that contradicts the stem, missing text. Leave empty otherwise.

## Voice

Direct and plain, addressing the student as "you". No praise, no filler.
Assume they got it wrong and want to know why — that is who reads this.
