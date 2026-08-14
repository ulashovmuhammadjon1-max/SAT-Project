# SAToplam R&W (Tests 16–31) — defects found while writing explanations

Twelve agents read all 1,254 questions to write explanations. Reading every
question by hand is the most thorough audit this content has had, and it found
things no regex pass had. This records what was fixed, what needs the source
books, and one structural problem in how the tests were built.

## Fixed in production

| defect | count | how |
|---|---|---|
| quotation marks encoded as apostrophes (`’especially pointed’`) | 32 | `cb-question-bank/fix_quote_glyphs.mjs` |
| passage's last sentence stored in the `stem` column | 11 | `cb-question-bank/fix_stem_spill.mjs` |
| spliced tail on an answer choice | 2 | truncated at the join, gated on the exact current text |

The stem-spill one was the worst of the three for a student: the sentence that
went missing is usually the study's conclusion, which is the sentence the
question is about, so the passage stopped mid-argument and the question opened
mid-sentence. Five agents reported it independently.

## Structural: the source bank recycles templates, and the allocator did not check

`cb-question-bank/scan_satoplam_defects.mjs` scores every pair of questions on
a passage+stem token signature. Across Tests 16–31:

- **33 near-duplicate pairs inside a single test**, two of them scoring 1.00 —
  byte-identical questions shipped twice in one test.
- **443 pairs across tests** at ≥0.60.

A student sees Module 1 plus one Module 2 branch, so a repeat inside one test
shows half the cohort the same question twice in one sitting. Worked examples:

- Test 18 M1 q6 and M2 Easy q7 are the same question, verbatim; M2 Easy q9 is
  the same passage a third time with "rusty-spotted cat" swapped for
  "flat-headed cat".
- Test 24 M2 Easy q13 and M2 Hard q13 score 1.00.
- Test 16 M2 Hard q25 and q26 are the same Rhetorical Synthesis template
  **back to back in one module** — "refute a claim that [fruit] is a better
  source of vitamin C than [vegetable]".
- The "price of vintage X rose dramatically … counterintuitive effect of ___
  demand" item appears three times (Test 16 twice, Test 17 once).

This is the same finding CLAUDE.md already records for the EliteXSAT corpus —
"the corpus recycles heavily" — reproduced for SAToplam. The build deduped on
exact content, which is what missed it: a template repeat that swaps the
setting words is not an exact match.

**The fix is not a threshold.** CLAUDE.md's rule already says a similarity
score decides what to *read*, not what to accept. What was missing here is that
the allocator never scored candidate pairs at all. Any future build from this
bank must screen each module's picks against every other question **in the same
test** before assembling it.

## Answer keys: 29 disagreements in 1,233 (2.4%)

Every agent derived its own answer before seeing the key; `verify.mjs` held
back every mismatch, so **no explanation shipped arguing for a disputed key**.
The full list is reproducible with:

    node content-pool/explanations/verify.mjs 2>&1 | grep "! sat-"

Two things make these worth taking seriously rather than treating as agent
error:

1. **They cluster on repeated positions** — INI q11–q13, EOI q22–q27,
   CAS q6–q7, SEC q17–q18. That is the duplicate-template problem again: the
   same item carries the same wrong key into several tests.
2. **Independent agents converged.** sat-02 and sat-03 hit the same
   dog-language-exposure template in Tests 18 and 19 and both derived B against
   a keyed A, without seeing each other's work. sat-01 and sat-10 both hit the
   Aristophanes *Clouds* item (Tests 16 and 29) and both rejected the key.
   sat-10 found the ekphrastic-poem transition item keyed `conversely` in one
   branch and `likewise` in the other — the same question, two different keys,
   so at least one is provably wrong.

This is consistent with CLAUDE.md's measured rate for transcribed R&W keys
(Test 5: 6 wrong in 81, 7.4%). 2.4% is better, not clean.

## Needs the source books — cannot be repaired from what is in the database

These are corrupted beyond mechanical recovery. Each needs the SAToplam page
re-read, or the question replaced.

- `f8f1a61c` **Test 16 M1 q12** — choice C is text from an unrelated
  music-recommendation question, and the stem is truncated mid-sentence ("as
  seen when the character.") so the cue naming the character is gone.
- `eaac4a9f` **Test 16 M2 Easy q26** — the goal sentence ("emphasize a
  similarity between the two countries") belongs to a different question; the
  notes are about Elizabeth Catlett's linocut and no countries appear anywhere.
- `5ea5ddb9` **Test 17 M1 q26** — same defect: goal asks for "a dinosaur fossil
  specimen's nickname", notes and all four choices are about chromium mass
  fraction.
- `5a7f57b3` **Test 27 M2 Hard q26** — notes open on Oahu plants then list
  Indus River facts; the two plants named in every choice appear nowhere.
- `03046302` **Test 25 M2 Easy q9** — the correct choice has words dropped:
  "It appears in the Gershwin opera Porgy and Bess**an** adaptation by Davis
  and Evans."
- `1db6a792` **Test 28 M2 Hard q10** — choice C is the literal string "None of
  the above", which is not an SAT choice format; a real choice was dropped.
- `aa2e92cb` **Test 18 M2 Easy q14** — the lead-in verb was dropped, so no
  choice fits grammatically.
- `c20bd30a` **Test 18 M2 Easy q1** — "not as ______ finding seems to suggest"
  is missing the second "as".
- `b3562fdf` **Test 20 M2 Easy q7** — stem says "undeclined portion" (typo for
  underlined) and the passage carries no `<u>` markup.
- `5b61af59` **Test 27 M1 q22** — stem asks which choice "conforms to the
  conventions of Standard English" while all four choices are transitions.

## Cosmetic transcription noise

Dozens of instances, student-visible but answer-neutral: "exmaines",
"Alfre Nobel", "citles", "onceupon**atime**", "Jhumpa Lahir**l**",
"Washington. DC", "February A3, 2014", dropped numbers in choices
("At **by** inches", "formed about **million** years ago", "relatively short,
at **hours**"). Not enumerated here — they are best fixed in one pass against
the source books rather than one at a time.
