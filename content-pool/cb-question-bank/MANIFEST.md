# Official College Board SAT Question Bank import

Source: the College Board question-bank PDF export the user is supplying in
parts (`READING_QUESTION_BANK__Part_1_p1657.pdf` = 100 pages / 84 questions,
`101199.pdf` = 99 pages / 86 questions, more expected).

## Why this source is different from everything else in content-pool/

Every other transcribed pool in this project came from third-party mock papers,
and CLAUDE.md records what that cost: 6 wrong keys in 81 Test 5 R&W questions
(7.4%), 44 wrong across Tests 3-4. That is why the standing rule is to author
R&W rather than transcribe it.

**This export does not have that problem.** Each question carries:

- a stable official `Question ID` (e.g. `f1bfbed3`)
- the official Domain, Skill and Difficulty
- the official `Correct Answer`
- the official `Rationale`, which explains the credited answer *and* why each
  distractor is wrong

So the key is authoritative rather than someone's transcription of a key, and
the rationale maps directly onto the existing `Explanation` model
(`whyCorrect` + `whyWrongJson`). The independent re-answer pass that Test 5
needed is not warranted here.

The taxonomy also maps 1:1 onto this project's existing domain/skill codes —
`Information and Ideas` → `INI`, `Command of Evidence` → `INI-CE`, and so on.

## `parse_bank.py`

    python3 parse_bank.py <file.pdf> <out.json>

Prints a validation summary and writes one JSON record per question. It
reports, and must show zero for, each of: parse errors, questions without
exactly 4 choices, a correct-answer letter not present among the choices,
empty stems or choices, and duplicate ids.

Current status — both supplied parts parse 100% clean:

| part | pages | questions | clean | need a rebuilt figure |
|---|---|---|---|---|
| 1 | 100 | 84 | 84 | 15 |
| 2 | 99 | 86 | 86 | 11 |

170 questions, 170 unique ids, all Information and Ideas
(Command of Evidence 84, Central Ideas and Details 48, Inferences 38).
Difficulty Hard 76 / Medium 56 / Easy 38. Keys fall A41 B51 C39 D39 — already
balanced, so `balance_rw.py`-style rotation is not needed.

## Three extraction traps, all found by running the parser rather than assuming

1. **Use `pdftotext -raw`, never `-layout`.** In `-layout` mode PDFium emits
   every typographic apostrophe on its own line *ahead of* the line it belongs
   to, so "photography's impact" becomes a bare `’` line followed by
   "photography s impact". That silently strips the apostrophe from every
   possessive and contraction in the bank — and any attempt to reattach it
   corrupts the `A. ` choice markers on the following line, which is exactly
   what broke 11 questions on the first attempt. `-raw` keeps the character
   inline and needs no repair.

2. **Strip form feeds.** `pdftotext` writes `\f` directly after the newline at
   a page boundary, so a marker landing at the top of a page arrives as
   `"\fCorrect Answer: D"` and a `^Correct Answer:` anchor no longer matches.
   One question per part was being dropped this way, with everything else about
   it perfectly intact.

3. **The charts are not images.** `pdfimages` reports **zero** image objects in
   the whole file: every bar and line graph is drawn as individually positioned
   glyphs. Text extraction shreds their axis labels into fragments like
   `ns e ry tiv e`. Those questions are flagged `needs_figure` and must have
   the figure rebuilt from a page render (`pdftoppm -r 110 -png`, which is
   fully legible) before they can ship — importing the shredded text would
   produce an unanswerable stem, the defect CLAUDE.md rule 3 exists to prevent.
   26 of the 170 so far are affected.

## Not yet done

- The `needs_figure` questions: rebuild each as a real `<table>` or a chart
  image on `Question.imageUrl`.
- Dedupe against the 4,560 questions already banked.
- The collection separation (`QuestionCollection`) was reverted after it took
  production down; it has to go back in together with its migration, which
  needs `PROD_URL`. See the schema rule at the top of CLAUDE.md.
