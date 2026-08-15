# Adjudication brief — disputed Math answer keys

A question reaches you because **two sources already disagree about its
answer**: the book's printed key, and a transcriber who solved it without
seeing that key. You are the tiebreaker.

You will not be told either answer. That is the entire design. A key only
moves when two readings that could not see each other land on the same answer
against the book, so your reading is worthless the moment it is influenced.

## The one rule that matters

**Do not go looking for the answer.** Not in `disputes.json`, not in
`printed_keys.json`, not in `ready.json`, not in the `out/*.jsonl`
transcription files, not in the book's answer tables. Solve it yourself from
the question in front of you.

In the first round an adjudicator opened `disputes.json` while hunting for a
missing figure and saw both the first agent's answer and the printed key. It
volunteered this, and that one question had to be thrown out and re-read by
someone else. Everything else in its slice was fine. If it happens to you, say
so in the record's `note` — an honest disclosure costs one question, a silent
one corrupts the result.

## Working a question

    python3 dump_q.py --help            # not this one
    python3 dump_adj.py adj2-1 --todo 6

Run that from `content-pool/satoplam-math/` with your own slice name. It prints
the next few questions and nothing else.

1. **Solve it properly.** Use sympy where the mathematics allows it — that is
   an independent check, not a shortcut. Derive it by hand otherwise.
2. **If your answer is not among the choices, say so.** Record
   `"answer": "NONE"` and explain in `note` what the question would need to be
   answerable. A defective question is a real finding; picking the nearest
   choice destroys the evidence.
3. **Figures.** A question marked `needsFigure` carries the first
   transcriber's measured reading of the figure in `book_note` — that is
   deliberately shared, because you cannot re-measure a picture you have not
   been shown, and it describes the *figure*, not the answer. If the note is
   not enough to solve the question, record `"answer": null` and say why.

## Output — append one line per question, immediately

To `adj/<your-slice>.jsonl`. Never batch: if you stop, everything appended is
safe and a replacement resumes from the ids in your file.

```
{"id":"…","answer":"C","confidence":"high","reasoning":"…","note":""}
```

- `answer` — the letter for multiple choice, the value as a string for
  free-response, `"NONE"` if no choice works, `null` if unsolvable as printed.
- `confidence` — `high` when the mathematics is decisive, `medium` when the
  question is ambiguous but one reading is clearly better, `low` when you are
  genuinely unsure. Low confidence is useful information; false certainty is
  not.
- `reasoning` — two or three sentences: the step that settles it. Enough that
  a human comparing your reading against the other one can see *why* they
  differ, not just *that* they do.
- `note` — anything wrong with the question itself, or a disclosure.

## Voice

You are writing for the person who resolves the disagreement, not for a
student. Be terse and exact.
