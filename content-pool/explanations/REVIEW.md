# Answer-key review list — CLOSED

All 53 held-back questions have been adjudicated. Nothing remains on this list;
it is kept as the record of what was decided and why.

## Outcome

| verdict | count |
|---|---|
| key was wrong, key corrected | 51 |
| key was right, agent wrong — explanation rewritten by hand | 1 |
| defective item, rewritten so exactly one choice works | 1 |

The one where the key stood is **Test 2 R&W M2 Hard q22** (Transitions): the
keyed *However* is correct and the agent's *Therefore* was not. Both a cause and
a contrast are present in the sentence, and the transition has to match how the
writer is using it, not only how the facts connect. Its explanation is in
`manual.json`, written by hand because the agent's argued for the wrong answer.

The defective one is **Test 27 R&W M2 Easy q17**, which had two independent
clauses either side of the blank and so made both the full stop and comma-plus-
*and* correct. Recast around an appositive by `rewrite_questions.mjs`.

## Where the wrong keys were

| test | wrong keys | content origin |
|---|---|---|
| Test 3 | 24 | transcribed |
| Test 4 | 20 | transcribed |
| Test 1 | 4 | transcribed |
| Test 2 | 2 | transcribed |
| Test 10 | 1 | authored |

**50 of the 51 are in transcribed content.** Both adjudicating agents reached
the same diagnosis independently: the offsets are not a uniform shift (+1, +2,
−1, −2 all appear), which rules out an off-by-one in a parser and points at
answer choices being reordered during transcription while the source key letter
was carried across unchanged. One agent traced two of them back to
`content-pool/test-3-4-5-reading-writing/test345_classified.json`, which already
holds the wrong letters — so the fault is upstream of insertion.

Several of the keys were not merely arguable but impossible: *hew out* keyed as
*Vacate*; "few religious buildings can be said to **minimize** the astonishing
size" of one of the world's largest mosques; a Rhetorical Synthesis item whose
goal is to name the institution housing a fossil keyed to the one choice that
never names it; keys pointing at sentence fragments, at a comma splice, and at a
plural verb with a one-person subject.

## The consequence worth carrying forward

The disputed set was 100% wrong for Tests 3 and 4 — 44 for 44. Those keys were
only ever examined because an agent happened to disagree with them. **The rest of
Tests 3 and 4's R&W keys come from the same parse and should be assumed suspect
until re-answered.** The explanation run did derive an answer independently for
every question in both tests, and the ones that agreed are the ones not listed
here — so the coverage is better than it sounds, but the source file itself is
still wrong and should not be reused.

## How the fixes were applied

- `apply_verdicts.mjs verdicts-test3.json verdicts-test4.json --apply` — 44 keys
- `fix_keys.mjs --apply` — the 9 from Tests 1, 2, 10, 27, 29
- `resync_slices.mjs --apply` — **required after any key fix.** `insert.mjs`
  gates against the slice snapshot the agent worked from, not the live database,
  so a corrected key leaves a stale slice still rejecting the explanation.
- `insert.mjs --only <prefix> --apply` — ships the released explanations
