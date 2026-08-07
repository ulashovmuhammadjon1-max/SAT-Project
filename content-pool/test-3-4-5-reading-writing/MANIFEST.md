# Reserved Reading & Writing content for Test 3, Test 4, Test 5

Built and verified in a prior session, persisted here so it survives past that session's
ephemeral scratchpad (per the environment: only what's committed to git survives). This is
**Reading & Writing only** — no Math content exists for these three tests yet (see "Math
status" below).

## What's in this directory
- `test345_classified.json` — the actual content, one array per `{testKey}|{moduleKey}`
  (e.g. `test3|RW_M1`). Each question object has `source`, `num`, `passage`, `stem`, `choices`,
  `correct`, plus `domain`/`skill` already assigned. This is the direct input for an
  `insert_test3.mjs`-style script modeled on the one used for Test 2 (see
  `CLAUDE.md`'s "Test 1 — reference structure & schema conventions" section for the exact
  schema/HTML conventions to follow).
- `classify_test345.py`, `classify_test1.py`, `classify2.py` — the classification scripts that
  produced it, kept for reproducibility/traceability, not meant to be re-run blindly (they read
  from a scratchpad path from the session that built them, which no longer exists — treat them
  as reference, not runnable as-is without repointing the file paths and providing a fresh
  `final_allocation_5tests.json`-equivalent source).

## Verified before saving
- **Question counts**: Test 3 is a full 27/27/27. Test 4 is 27/26/27 (short 1 in Module 2
  Easy). Test 5 is 26/22/26 (short 1/5/1 — short 7 total). None of these are full 27-question
  modules per the CLAUDE.md rule for Test 4/5 — top up with more real content or original
  questions before publishing either.
- **R&W domain-block order**: monotonic in all 9 modules (verified programmatically against
  the same fine-grained 12-block order used for Test 1/2 — see CLAUDE.md).
- **Deduplication**: zero content overlap against Test 1, Test 2, each other, and internally
  within each test (checked by full stem+passage+choices content, not stem alone — a bare-stem
  check gives false positives since many R&W stems are boilerplate reused verbatim across
  unrelated questions).
- **Domain/skill classification**: Standard English Conventions was manually split into
  Boundaries vs. Form/Structure/Sense by reading each of the 54 SEC questions' actual answer
  choices (the classifier can't do this from stem text alone — see CLAUDE.md). Rhetorical
  Synthesis correctly includes the "given sentences" phrasing variant.

## Still needed before this can ship (not done yet — do this when actually building the test)
Same content-formatting pass Test 2 got (HTML tables, bullet lists, Text 1/Text 2 splits,
`[UNDERLINED: ...]` → `<u>`, `*italics*` → `<em>`) — none of that has been applied yet, this
file still has the raw pre-formatting text. Specifically:

- **~24 Rhetorical Synthesis questions** need their `"Bulleted notes: - ..."` passages
  converted to `<ul><li>` markup.
- **5 Cross-Text Connections questions** need Text 1 / Text 2 passage splitting.
- **4 questions** have `[UNDERLINED: ...]` brackets needing `<u>` conversion.
- **13 questions have a real data table** already transcribed as text (pipe-delimited or
  otherwise) that needs HTML `<table>` conversion — same technique as Test 1/2's tables:
  `test3|RW_M1` idx11, `test3|RW_M2_HARD` idx11, `test4|RW_M1` idx10 & idx11,
  `test4|RW_M2_EASY` idx8 & idx9, `test4|RW_M2_HARD` idx8, `test5|RW_M1` idx8 & idx9,
  `test5|RW_M2_EASY` idx8, `test5|RW_M2_HARD` idx8 & idx9 & idx10.
- **4 questions reference a real line/bar graph** with no source image available in this
  environment — the original source PDFs (Dec2023, Nov2023, March2024) were not kept, only
  their transcribed text. These need either the original PDF re-sent to extract the real
  figure, or the question dropped/replaced: `test4|RW_M2_EASY` idx10 (line graph),
  `test4|RW_M2_HARD` idx10 (bar graph), `test5|RW_M1` idx10 (line graph), `test5|RW_M2_EASY`
  idx7 (line graph).
- **3 questions have a transcription-ambiguity flag** in their `diagram` field noting the
  source image had a watermark/cursor obscuring some text, with the transcribed value being
  an inference — should be re-verified against the original PDF before shipping, not assumed
  correct: `test4|RW_M2_HARD` idx9, `test5|RW_M1` idx15, `test5|RW_M1` idx18.

## Math status
**Zero Math content exists for Test 3, 4, or 5.** Confirmed in the session that built this: the
4 new source files the user provided (March2024B, Dec2023E, Dec2023_12A, Nov2023) are R&W-only
transcripts (verified against their own answer keys — 2 modules of 27 each, no Math section).
The old pool's real transcribed Math (March/May/JuneV1/JuneV2) was already fully consumed
building Test 1 and Test 2. Test 3/4/5 cannot be published until Math content exists — either
more source PDFs (with a Math section) arrive, or original SAT-style Math questions get
written and sympy-verified per the CLAUDE.md rule for when real supply runs short.
