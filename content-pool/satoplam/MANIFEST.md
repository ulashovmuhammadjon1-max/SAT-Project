# SAToplam 2.0 Reading book — parsed and compared against the College Board bank

Source: "SAToplam 2.0" by @satashkent, a topic-organised compilation that
states its questions come from real digital SATs administered March 2023 to
August 2025. Supplied in parts covering book pages 1-450 plus 550-555.

## What came out

| | count |
|---|---|
| parsed | 680 |
| already present in the College Board export | 70 |
| **contributed as new** | **610** |

Every parsed question has a key and exactly 4 choices. 46 carry square-bracket
editorial reconstructions (see below).

By skill: Command of Evidence 229, Inferences 138, Text Structure and Purpose
133, Central Ideas and Details 91, Cross-Text Connections 19.

## The overlap is small, and that is the useful finding

Both books claim to reproduce real SAT questions, so heavy duplication looked
likely. It is not: only **70 of 680** appear in the College Board export.
The two sources are largely complementary rather than redundant.

## Never compare answer LETTERS across two sources

Of the 70 overlapping questions, **33 carry a different letter while crediting
the identical choice text** — the two books simply order the choices
differently. A first comparison keyed on the letter reported a ~50 % "key
disagreement" rate that was almost entirely an artefact of that reordering.

Correctness has to be compared on the **text of the credited choice**. This is
the same failure mode CLAUDE.md already records from the Tests 3-4 audit, where
non-uniform offsets (+1, +2, -1, -2) revealed choices reordered during
transcription rather than an off-by-one parser.

Matching also has to require the **stem** to agree, not just the passage:
several SAT passages are near-identical templates about different subjects, and
a passage-only key pairs unrelated questions.

After both corrections, 8 genuine answer conflicts remain, listed in
`key_conflicts.json`. In every one the College Board key is the authoritative
side — it ships with an official rationale — so College Board wins all
collisions and SAToplam contributes only what College Board lacks.

## Two limitations that gate how these can be used

1. **No difficulty label.** The book is organised by topic, not difficulty. All
   610 import with `difficulty: null`, so they cannot fill a per-module
   difficulty quota until labelled. That is the direct blocker on using them
   for the Test 6+ rebuild, whose whole premise is a difficulty mix.
2. **No rationale, and a transcribed key.** Unlike the College Board export
   these carry no explanation, and the key is someone's transcription. CLAUDE.md
   measures transcribed R&W keys at 6 wrong in 81 (7.4 %) and 44 wrong across
   Tests 3-4. Every one is flagged `key_is_transcribed: true` and needs an
   independent answer pass before it reaches a student.

37 of the 610 also carry bracketed text such as
`delivered by [a confident orator, it may be] ignored` — the book's own
editorial reconstruction of damaged source text. Flagged `bracketed_text`;
these want a human read before shipping.

## Running it

    python3 parse_satoplam.py <out.json> <part1.pdf> <part2.pdf> …
    python3 merge_into_bank.py <cb_bank.json> <satoplam.json> <merged.json>

Parts must be parsed as one stream, not individually: a topic's questions and
its answer table can fall in different parts (Inference starts in part 1, its
key is in part 2), and a per-file parse silently drops every question whose key
it cannot see — 52 in the first attempt.
