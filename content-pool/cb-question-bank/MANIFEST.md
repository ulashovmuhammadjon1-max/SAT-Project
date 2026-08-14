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

## Current status — all four R&W domains parsed, 1,767 questions, zero defects

Twenty-three part files covering book pages 1-1900 (one part arrived twice as a
straight re-send; several boundaries overlap by a page).

| | count |
|---|---|
| unique questions | 1,767 |
| duplicates across parts | 104 |
| already in the live bank | 53 |
| **new to import** | **1,714** |
| need a rebuilt figure | 73 |

Every check at zero: parse errors, questions without exactly 4 choices, keys
absent from their own choice list, duplicate choice text within a question,
missing rationales, empty stems, lost apostrophes, duplicate ids.

| domain | count |
|---|---|
| Information and Ideas | 554 |
| Craft and Structure | 469 |
| Expression of Ideas | 398 |
| Standard English Conventions | 346 |

By skill: Command of Evidence 268, Words in Context 252, Rhetorical Synthesis
199, Transitions 184, Boundaries 173, Form Structure and Sense 164, Text
Structure and Purpose 141, Central Ideas and Details 136, Inferences 136,
Cross-Text Connections 61. Difficulty Easy 582 / Medium 572 / Hard 560. Keys
fall D448 B433 A429 C404 — balanced, so no rotation pass is needed.

**All four Reading and Writing domains are now present**, which makes this a
complete R&W bank rather than a partial one. Two consequences worth noting:

- Rhetorical Synthesis and Transitions were the two chronically scarce domains
  in every previous test build — the reason CLAUDE.md mandates pooling supply
  across tests with a largest-remainder split. At 199 and 184 that constraint
  is gone.
- Boundaries vs Form, Structure, and Sense previously had to be told apart by
  reading each question's choices by eye, because a stem-only classifier
  cannot distinguish them. Here the official skill label is supplied, so that
  hand-classification step disappears entirely.

Structural checks passing across the whole set: all Cross-Text questions carry
both Text 1 and Text 2; every Words in Context question either has a `_____`
blank or is the "as used in the text … most nearly mean" variant; every
Rhetorical Synthesis question references the notes or the given sentences; all
346 Standard English Conventions questions have both a `_____` blank and the
"conventions of Standard English" phrasing.

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
