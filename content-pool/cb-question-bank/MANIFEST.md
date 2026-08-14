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

## Current status — COMPLETE. 1,838 questions, zero defects

Twenty-four part files covering the whole export, book pages 1-1971 (one part
arrived twice as a straight re-send; several boundaries overlap by a page).

| | count |
|---|---|
| unique questions | 1,838 |
| duplicates across parts | 105 |
| already in the live bank | 55 |
| **new to import** | **1,783** |
| need a rebuilt figure | 73 |

Every check at zero: parse errors, questions without exactly 4 choices, keys
absent from their own choice list, duplicate choice text within a question,
missing rationales, empty stems, lost apostrophes, duplicate ids, and choice
labels out of A-B-C-D order. Rationales run 337 characters at the shortest,
1,135 at the median.

| domain | count |
|---|---|
| Information and Ideas | 554 |
| Craft and Structure | 469 |
| Standard English Conventions | 417 |
| Expression of Ideas | 398 |

By skill: Command of Evidence 268, Words in Context 252, Boundaries 207,
Rhetorical Synthesis 199, Form Structure and Sense 199, Transitions 184, Text
Structure and Purpose 141, Central Ideas and Details 136, Inferences 136,
Cross-Text Connections 61. Difficulty Easy 608 / Medium 591 / Hard 584. Keys
fall D471 A445 B445 C422 — balanced, so no rotation pass is needed.

Two long-standing constraints in this project disappear with this bank:

- Rhetorical Synthesis and Transitions were the chronically scarce domains in
  every previous build — the reason CLAUDE.md mandates pooling supply across
  tests with a largest-remainder split rather than per-test silos. At 199 and
  184, supply is no longer the binding constraint.
- Boundaries vs Form, Structure, and Sense could not be separated by any
  stem-only classifier, because the only signal is which punctuation differs
  between the four choices; both previously needed a by-eye pass. The official
  skill label is supplied here, so that step disappears.

Structural checks passing across the whole set: all Cross-Text questions carry
both Text 1 and Text 2; every Words in Context question either has a `_____`
blank or is the "as used in the text … most nearly mean" variant; every
Rhetorical Synthesis question references the notes or the given sentences;
every Standard English Conventions question has both a blank and the
"conventions of Standard English" phrasing.

## Remaining work before any of this ships

1. **The 73 figure questions.** All in Information and Ideas. Their bar and
   line graphs are vector glyphs that text extraction shreds, so each needs its
   figure rebuilt from a page render (`pdftoppm -r 110 -png`, fully legible) as
   either a real `<table>` or a chart image on `Question.imageUrl`.
2. **The collection separation.** `QuestionCollection` was reverted after it
   took production down, and has to go back in *together with* its migration —
   which needs `PROD_URL`. See the schema rule at the top of CLAUDE.md.
3. **Import.** Insert unpublished into its own collection, spot-check in the
   real exam interface, then publish.

## `overrides.json` — repairs to defects in the source export

One question so far. `e3bbf2bf` has its choice D typeset as a nested bullet
underneath choice C with no "D." label, so it parses as part of C; the
question's own rationale discusses "Choice D", confirming the choice exists,
and a render of the page shows the mis-typeset bullet. This is a flaw in
College Board's export, not in extraction.

Kept as data rather than as parser heuristics: these are one-off typesetting
flaws, not patterns, and a heuristic general enough to catch them would misfire
on correct questions. Every override asserts the text it expects to find before
changing anything, so a stale override fails loudly rather than silently
rewriting the wrong question.

## Five extraction traps, all found by running the parser rather than assuming

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

4. **The metadata row wraps.** A long skill name breaks across lines, so
   "…Craft and Structure Text Structure and" / "Purpose" / "Hard" arrives as
   three lines and reading only the first one fails. 103 questions in a single
   part were lost this way. The whole region between the table header and the
   `Question` marker is now collapsed and matched as one string. Matching is
   also case-insensitive, because the export writes both "Cross-text
   Connections" and "Cross-Text Connections".

5. **The charts are not images.** `pdfimages` reports **zero** image objects in
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
