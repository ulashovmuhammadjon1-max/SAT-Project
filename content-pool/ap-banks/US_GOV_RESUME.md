# AP U.S. Government and Politics — bank state and how to resume

This file is the US Gov bank's own record. `SOCIAL_RESUME.md` covers all three
social science subjects and is owned by the run that created it; this one covers
only US Gov and is kept current by whoever is authoring it.

## State

| unit | topics | status |
|---|---|---|
| 1 Foundations of American Democracy | 1.1 – 1.9 | **complete**, 9 of 9 |
| 2 Interactions Among Branches | 2.1 – 2.15 | **complete**, 15 of 15 |
| 3 Civil Liberties and Civil Rights | 3.1, 3.2, 3.3 | 3 of 13 |
| 4 American Political Ideologies and Beliefs | — | 0 of 10 |
| 5 Political Participation | — | 0 of 13 |

**27 of 60 topics, 810 questions, every one behind a passing verifier.**

Resume at **3.4 Freedom of the Press** and work in CED order.

## How to author one topic

1. `zcat ced-source/US_GOV_ced.txt.gz > /tmp/usgov.txt` and read the topic's
   own pages. `AP_US_GOV_CED.md` has the exam format, the thirteen required
   documents, the fourteen required cases with the CED's own statement of every
   holding, and twelve numbered notes recording places where the CED
   contradicts what general knowledge of this course would assume. Read the
   notes; several of them have already prevented defects in this bank.
2. Write `v<unit>_<n>.py`: a module header that quotes the essential-knowledge
   statements verbatim and says what the topic's trap is, then
   `TOPIC = (code, verbatim CED title, unit)` and exactly 30 questions, five
   choices, key written first (`ans=0`), a `why` that gives the reason.
3. Write `verify_v<unit>_<n>.py`. See the next section.
4. Run it, run `export_units.py`, commit and push. **After every topic.**

## What a verifier must contain

Units 1 and 2 use `usgov_check`; Units 3 to 5 use `gov345_check`, which is the
convention `verify_v3_1.py` established and which adds the digit-hyphen and
LETTER_REF rules. **Every module, in either half, also runs the four helpers in
`usgov_anchor.py`:**

- `ua.shape(module)` — the question dict holds exactly `q/choices/ans/why` plus
  an optional `table`. This exists because a stray walrus expression once sat
  inside a question dict, imported cleanly, and passed every content check in
  the bank. Nothing that reads MEANING can see a defect that is syntactically
  valid and semantically inert.
- `ua.check(module, ANCHORS, GROUNDING)` — an anchor per question (a substring
  in the keyed choice and in no distractor) and a grounding per question (the
  CED statement, required case, foundational document or constitutional
  provision the key traces to). **Writing thirty groundings IS the review.**
  Every wrong number and misstated claim found in this bank was found doing it.
- `ua.notation(module)` — no digit-hyphen-digit and no digit-slash-digit
  anywhere, because `export_units.py` runs every string through
  `mathfmt.convert`, which reads both as arithmetic. Write "five to four",
  "two-thirds", "the September 2001 attacks".
- plus a per-topic check for whatever that topic's specific trap is, and
  arithmetic recomputed from every table.

## Traps this bank has already paid for

- **A NOT-question needs its distractors verified as carefully as its key.**
  If one distractor is not actually on the list, the item has two defensible
  answers and the best-prepared student is the one who hesitates. See
  `_four_purposes` in `verify_v2_6.py`, `_five_restrictions` in
  `verify_v2_11.py`, `_seven_agencies` in `verify_v2_13.py`.
- **A number that appears only in prose is a number nothing is checking.**
  Four defects so far, all of them a rationale asserting something false about
  the table directly above it (v1_2 twice, v1_3, v1_7, v2_1, v2_6, v2_9).
  Recompute every claim from the table, including the ones the key does not
  make.
- **A stimulus table has to be true in the ways nobody asks about.** v2_2's
  budget table needed mandatory plus discretionary to equal total outlays; no
  question asserts it, every reader assumes it, and nothing would have caught it.
- **An over-matching checker is worse than none.** Rebuilt four times this
  session alone: `_pocket_veto` fired on eight correct distractors,
  `_quantifiers` fired on two rationales whose job was to state the correction,
  `_definitions` fired on a sentence that gets libel and slander right. Scope a
  content check to the KEY and the WHY — the text a student is told is true —
  and never to the choice list, whose distractors exist to be wrong.
- **The CED's own wording is sometimes the wrong thing to copy.** It writes
  "2/3 vote"; shipping that typesets a fraction. Write "two-thirds".
- **Off-syllabus content is what a well-informed author reaches for.** 2.10 is
  titled "The Court in Action" and contains nothing about certiorari, the rule
  of four or oral argument — the CED never mentions any of them. See
  `_on_syllabus` in `verify_v2_10.py`.
- **The framework states the access-point claim three times** (EK 1.6.B.1 for
  separation of powers, EK 1.9.A.1 for federalism, EK 2.15.B.1 for the three
  branches). Each module is pinned to a different multiplier and
  `_branches_not_levels` in `verify_v2_15.py` enforces the boundary.

## Files

- `v1_1.py` … `v3_3.py` — the modules. `verify_v*.py` — one per module.
- `usgov_check.py`, `gov345_check.py` — the two shared structural checkers.
  Libraries, not scripts: running one prints nothing.
- `usgov_anchor.py` — the shared anchor/grounding/notation/shape gate.
- `export_units.py v1_1 v1_2 … --subject US_GOV --out /tmp/usgov.json` —
  enforces 30 per topic, redistributes keys across A–E, warns on near-duplicate
  stems. Warnings on items that share one stimulus are expected.
