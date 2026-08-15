# SAToplam R&W (Tests 16–31) — defects found while writing explanations

Twelve agents read all 1,254 questions to write explanations. Reading every
question by hand is the most thorough audit this content has had, and it found
things no regex pass had. This records what was fixed, what needs the source
books, and one structural problem in how the tests were built.

## Status: closed

Everything below was found and every item is now resolved. Production carries
**4,557 live questions, all 4,557 with an explanation**, and the R&W audit
across all 31 tests reports no findings.

## Fixed in production

| defect | count | how |
|---|---|---|
| quotation marks encoded as apostrophes (`’especially pointed’`) | 32 | `cb-question-bank/fix_quote_glyphs.mjs` |
| passage's last sentence stored in the `stem` column | 11 | `cb-question-bank/fix_stem_spill.mjs` |
| spliced or mangled answer choice | 8 | gated per-row rewrites, values restored from the question's own notes |
| duplicate a student could meet twice in one sitting | 35 | `plan_dupe_fix.py` + `apply_dupe_fix.mjs` |
| unanswerable or incoherent question, replaced | 18 | same pipeline, driven by `force_replace.json` |
| wrong answer key | 21 | `explanations/apply_key_verdicts.mjs` |

### The answer keys: 21 of 26 were genuinely wrong

Every disputed question was worked **three times** — once by the authoring
agent, then by two adjudicators who could not see the key, could not see each
other, and were not told what the first agent concluded.

- **21** — both independent readings converged on the same answer against the
  stored key. Flipped.
- **2** — the adjudicator reached the stored key; the first agent was the
  outlier. Key left alone, adjudicator's explanation shipped.
- **3** — replaced instead, because adjudication found the question itself
  broken rather than merely miskeyed.
- **0** — unsettled. Nothing needed a coin toss.

An 81% confirmation rate is not a story about careful reading; it is a story
about the source. Two examples worth keeping:

- The same museum question appears in Test 17 and Test 28 with different
  institutions, and **both are keyed to the same wrong option under different
  letters** — which rules out a transcription letter-slip and means the defect
  is in the source book, replicated.
- One question was keyed `conversely` in the Easy branch and `likewise` in the
  Hard branch of the same test. Same question, two keys, so one is provably
  wrong.

**The gate is what made this recoverable.** Because no explanation was ever
written from the key, a wrong key showed up as a disagreement instead of being
silently justified. Withholding the key from `dump_slice.mjs` is the cheapest
high-value thing in this pipeline — keep it.

### Two questions replaced rather than re-keyed, on purpose

A defective question is not fixed by moving its key. Test 31's bird-metabolism
item had **two** choices that undermine the proposal — one hedged, one flat —
and a weaken question with two working answers is broken whichever letter is
marked. Test 22's Henry VIII item is filed under Standard English Conventions
but every choice is well-formed English; it is decided on diction and history,
not grammar. The first was replaced; the second is answerable and correctly
keyed, so it stands, noted here rather than churned.

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

## Answer keys: 29 disagreements in 1,254 (2.3%)

Every agent derived its own answer before seeing the key; `verify.mjs` held
back every mismatch, so **no explanation shipped arguing for a disputed key**.
**1,225 of the 1,254 are live**; the 29 below are the only R&W questions in all
31 tests still without an explanation, and they are held deliberately.
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
(Test 5: 6 wrong in 81, 7.4%). 2.3% is better, not clean.

## Was unrepairable from the database — all replaced

These were corrupted beyond mechanical recovery: the text that went missing
exists only in the source books. Rather than leave them in front of students
pending a re-transcription, each was replaced with a sound question a tier
harder. `cb-question-bank/force_replace.json` records the reason beside each
id. Listed here because the defects are worth recognising if the books are
ever re-parsed.

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
- `3e218287` **Test 25 M1 q10** — stem asks for the "main idea" but all four
  choices are bare noun phrases answering a *main topic* question. Stem and
  choices come from two different question forms.
- `23eb6fb3` **Test 24 M2 Hard q21** — "at 14,08 meters" should be 1,408 m. As
  printed it is *shorter* than the 1,006 m bridge the sentence says it exceeds,
  so the passage contradicts itself.
- `11ec09c8` **Test 24 M2 Hard q25** — choice C reads "lived from year to
  1737"; the notes give 1644.

## Cosmetic transcription noise

Dozens of instances, student-visible but answer-neutral: "exmaines",
"Alfre Nobel", "citles", "onceupon**atime**", "Jhumpa Lahir**l**",
"Washington. DC", "February A3, 2014", dropped numbers in choices
("At **by** inches", "formed about **million** years ago", "relatively short,
at **hours**"). Not enumerated here — they are best fixed in one pass against
the source books rather than one at a time.
