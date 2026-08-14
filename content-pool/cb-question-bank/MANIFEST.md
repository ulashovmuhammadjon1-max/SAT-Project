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

## `combine_parts.py`

    DATABASE_URL=… python3 combine_parts.py <out.json> <part1.json> …

Dedupes across parts on the official question id, flags anything whose stem
already matches a banked question, and writes `bank_parsed.json`.

## Current status — pages 1-657 complete, 552 questions, zero defects

Nine part files covering book pages 1-657 (one part arrived twice as a
straight re-send; several boundaries overlap by a page).

| | count |
|---|---|
| unique questions | 552 |
| duplicates across parts | 91 |
| already in the live bank | 14 |
| **new to import** | **538** |
| need a rebuilt figure | 73 |

Zero parse errors, zero questions without exactly 4 choices, zero keys absent
from their own choice list, zero missing rationales, zero empty stems, zero
lost apostrophes.

All 552 are **Information and Ideas** — Command of Evidence 268, Central Ideas
and Details 136, Inferences 134. Difficulty Hard 231 / Medium 174 / Easy 133.
Keys fall A148 B137 C121 D132, already balanced, so `balance_rw.py`-style
rotation is not needed.

Craft and Structure, Expression of Ideas and Standard English Conventions are
still to come — those are separate exports.

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

3. **A question can straddle a part boundary.** One question's stem sits at the
   end of one file while its `Correct Answer` and `Rationale` are in the next,
   so it parses as an error in the earlier part and cleanly in the later one.
   `combine_parts.py` therefore keeps the *most complete* record for an id, not
   the first one seen — keying on first-seen silently preferred the truncated
   copy.

4. **The charts are not images.** `pdfimages` reports **zero** image objects in
   the whole file: every bar and line graph is drawn as individually positioned
   glyphs. Text extraction shreds their axis labels into fragments like
   `ns e ry tiv e`. Those questions are flagged `needs_figure` and must have
   the figure rebuilt from a page render (`pdftoppm -r 110 -png`, which is
   fully legible) before they can ship — importing the shredded text would
   produce an unanswerable stem, the defect CLAUDE.md rule 3 exists to prevent.
   73 of the 552 are affected.

## Not yet done

- The `needs_figure` questions: rebuild each as a real `<table>` or a chart
  image on `Question.imageUrl`.
- Dedupe against the 4,560 questions already banked.
- The collection separation (`QuestionCollection`) was reverted after it took
  production down; it has to go back in together with its migration, which
  needs `PROD_URL`. See the schema rule at the top of CLAUDE.md.
