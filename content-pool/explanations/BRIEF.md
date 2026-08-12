# Explanation authoring brief

You are writing student-facing explanations for real SAT practice questions on
a live platform. Read this whole file before writing anything.

## The one rule that matters

**Work the question yourself before you look at the marked key.** Then record
the answer *you* derived — not the one the database says is correct.

If they disagree, still write your own. The verifier compares the two and
rejects the mismatch, which sends it to a human review list. That is the
intended behaviour: this project has already found wrong answer keys in its own
content (Test 5 had 6 wrong answers in 81 banked R&W items), and an explanation
that confidently argues for a wrong key teaches a student the error. A
mismatch is a useful finding, not a failure.

Never reverse-engineer a justification for the marked answer.

## Durability — read carefully

Append **one line to your JSONL file after every single question**. Do not
batch, do not hold results in memory to write at the end. If you stop for any
reason — context, usage limit, error — everything already appended is safe and
a replacement agent resumes from the ids in your file.

Before starting, read your existing `.jsonl` and skip any `questionId` already
in it. Restarting must never duplicate work.

## Input and output

- Your questions: `content-pool/explanations/out/<agent>.slice.json`
- Your output:    `content-pool/explanations/out/<agent>.jsonl`  (append-only)

One JSON object per line, no pretty-printing:

```
{"questionId":"…","answerLabel":"B","whyCorrect":"…","whyWrong":{"A":"…","C":"…","D":"…"},"commonMistakes":"…","tips":"…"}
```

- `answerLabel` — the letter you derived. Free-response questions use
  `answerValue` instead, holding the value as a string.
- `whyCorrect` — the reasoning that gets there. Show the step a stuck student
  is missing, not a restatement of the answer. 2–5 sentences.
- `whyWrong` — **every** distractor gets an entry keyed by its letter. Name the
  specific error that produces it ("subtracts before distributing", "true of
  the passage but not what the question asks"). "This is incorrect" is useless.
- `commonMistakes`, `tips` — optional, one sentence, omit rather than pad.

## House style — matches the question content already in the database

- Inline math is `\( … \)`; display math is `\[ … \]`. Never `$…$`.
- Simple arithmetic stays plain text: write `17h + 45 = 164`, not a math span.
  Reserve `\( \)` for fractions, exponents, radicals, subscripts.
- Fractions are `\frac{}{}` — never `3/5` inside a math span.
- Function names are escaped: `\cos`, `\sin`, `\log`. Bare `cos(A)` renders as
  three italic variables.
- Leave a space either side of an inline span: `the length of \(AB\) is`.
- Never put prose inside math mode — KaTeX drops the spaces between words.
- Italics are `<em>…</em>`. Never markdown asterisks.
- No LaTeX macro outside a math span; `2\pi` in prose renders as literal
  backslash-p-i.

## Voice

Direct and plain. Address the student as "you". No praise, no filler, no
"Great question!". Assume they got it wrong and want to know why — that is who
reads an explanation.

## When you finish

Run `node content-pool/explanations/verify.mjs` and fix anything it reports
against your own file. Report your final counts: written, and any answer
mismatches you found.
