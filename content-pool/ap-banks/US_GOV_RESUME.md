# AP U.S. Government and Politics — bank state and how to resume

This file is the US Gov bank's own record. `SOCIAL_RESUME.md` covers all three
social science subjects and is owned by the run that created it; this one covers
only US Gov and is kept current by whoever is authoring it.

## State

| unit | topics | status |
|---|---|---|
| 1 Foundations of American Democracy | 1.1 – 1.9 | **complete**, 9 of 9 |
| 2 Interactions Among Branches | 2.1 – 2.15 | **complete**, 15 of 15 |
| 3 Civil Liberties and Civil Rights | 3.1 – 3.13 | **complete**, 13 of 13 |
| 4 American Political Ideologies and Beliefs | 4.1 – 4.10 | **complete**, 10 of 10 |
| 5 Political Participation | 5.1 – 5.13 | **complete**, 13 of 13 |

**60 of 60 topics, 1,800 questions, every one behind a passing verifier.
THE SUBJECT IS FINISHED.**

Nothing to resume. What is left is insertion, and the scan below before it.

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
- **A required case can be attached to a topic it says nothing about.** The CED
  attaches United States v. Lopez to 3.5 Second Amendment, and Lopez holds
  nothing about the right to bear arms -- its holding is a Commerce Clause one.
  A student who reads the topic heading and the case name together writes a
  false holding into an FRQ. Check what the CED says the case HELD, never what
  the case was about. See `_lopez_is_commerce` in `verify_v3_5.py`.
- **Do not supply a list the framework declines to supply.** 3.7 says SELECT
  protections have been incorporated and names no roster. A list assembled from
  outside the CED would be content the exam cannot ask about, presented with the
  authority of content it can. Every specific guarantee in that module arrives
  through a required case holding, and its timeline table counts guarantees in a
  hypothetical system so an item can teach the GAP without asserting which seven.
- **Where the framework says DEBATE, the bank takes no side.** 3.6's three
  subjects -- the death penalty, firearms regulation, metadata collection -- are
  live controversies the CED identifies as contested and resolves none of.
  Every item there asks what the debate consists of, what would count as
  evidence, or what a required case held. See `_no_position` in
  `verify_v3_6.py`.
- **Where the framework supplies no test, the bank supplies none either.** 3.5
  gives one sentence about interpretation and one holding about applicability,
  and no standard for evaluating any regulation. Items 27 and 28 there make the
  ABSENCE the thing tested rather than inventing content that sounds
  authoritative about a contested question.
- **The framework states the access-point claim three times** (EK 1.6.B.1 for
  separation of powers, EK 1.9.A.1 for federalism, EK 2.15.B.1 for the three
  branches). Each module is pinned to a different multiplier and
  `_branches_not_levels` in `verify_v2_15.py` enforces the boundary.

## Files

- `v1_1.py` … `v5_13.py` — the modules. `verify_v*.py` — one per module.
- `usgov_check.py`, `gov345_check.py` — the two shared structural checkers.
  Libraries, not scripts: running one prints nothing.
- `usgov_anchor.py` — the shared anchor/grounding/notation/shape gate.
- `export_units.py v1_1 v1_2 … --subject US_GOV --out /tmp/usgov.json` —
  enforces 30 per topic, redistributes keys across A–E, warns on near-duplicate
  stems. Warnings on items that share one stimulus are expected.

## Unit 5's last three topics, and the two boundaries they turn on

5.11, 5.12 and 5.13 close the subject. Two of them rest on a single framework
word, and in both cases the word is one a student already has an opinion about:

- **5.11 keys nothing the CED does not state.** The framework gives no
  contribution limit, no dollar figure, no definition of soft money beyond the
  word, no taxonomy of PACs beyond "different types", and no verdict on the 2002
  act or on `Citizens United`. `verify_v5_11.py`'s `_no_invented_numbers` refuses
  any digit in a key outside the data items unless it is one of the eight years
  the topic names, and `_holding` refuses any key that enlarges the CED's
  one-sentence holding — in particular the standard misstatement that the case
  permitted unlimited direct contributions, which is a claim about
  CONTRIBUTIONS where the CED's sentence is about SPENDING.
- **5.12's verb is CAN AFFECT and 5.13's is AFFECTED.** EK 5.12.A.2 says horse
  race coverage CAN AFFECT elections; EK 5.13.A.3 says democratic debate and
  political knowledge ARE AFFECTED, with no direction. Neither states an
  outcome. `_modal` and `_uncommitted` enforce both, and `_uncommitted` also
  refuses any key settling EK 5.13.A.2's bias debate in either direction.
- **The course defines AGENDA SETTING twice.** EK 2.7.A.1.ii makes it a
  president's influence over which policies the public sees as most important;
  EK 5.12.A.1 makes it media influence over how citizens routinely acquire
  political information. `_agenda` in `verify_v5_12.py` refuses a key that
  imports the earlier definition, and 5.12 item 6 makes the difference the
  question rather than leaving a student to collide with it.

Every gate in the three verifiers carries an executable negative control: the
gate is run against a deliberately corrupted copy of the module and must fail.
Sixteen controls across the three files, all firing. One of them earned its keep
immediately — 5.12 item 28's key said poll coverage took the largest share ONLY
IN THE FINAL WEEK, and the table's own arithmetic says it passes the platforms
column a period earlier. The item was structurally impeccable and read as true.
