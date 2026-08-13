# Cross-Text Connections top-up for the Question Bank

## Why this exists

Cross-Text Connections (`CAS-CT`) was the starved skill in the bank. Counted
against the other nine Reading & Writing skills in production:

| skill | published questions before this build |
|---|---|
| **CAS-CT Cross-Text Connections** | **16** |
| CAS-TS Text Structure and Purpose | 181 |
| INI-IE Inferences | 187 |
| INI-CI Central Ideas and Details | 193 |
| SEC-FS Form, Structure, and Sense | 275 |
| EOI-RS Rhetorical Synthesis | 280 |
| EOI-TR Transitions | 282 |
| INI-CE Command of Evidence | 284 |
| SEC-BS Boundaries | 359 |
| CAS-WV Words in Context | 454 |

Sixteen is not enough to build a practice session on, which is what a student
filtering the bank by this skill was running into. The shortage is structural
rather than accidental: the real SAT places at most one Cross-Text item in a
27-question module, so a bank assembled entirely from assembled tests can never
hold many. That is why these are authored **outside** the tests.

## What was built

48 questions across `batch1.json` … `batch4.json`, taking the skill from 16 to
64. Each carries a paired Text 1 / Text 2 passage, four choices, and a full
explanation with a separate reason for every distractor.

They are **standalone bank questions**: `moduleId` is null, which the schema
permits (`Question.moduleId String?`) and which the bank's filters accommodate,
since `question-bank.ts` gates on `isPublished` alone and never joins `Module`.
No assembled test is touched, and no test's question count changes.

## Topics, and why they are all new

Every existing Cross-Text passage was pulled from production first and its
subject recorded, so nothing here repeats one. The sixteen already live cover
UNESCO gastronomy cities (twice — Buenaventura and Arequipa), poetry economics,
canal tugs and railway competition, canal restoration, equal temperament, ice
cores, organ restoration, cathedral tracing floors, the brick tax, machine-made
roof tiles, mycorrhizal nutrient transfer, Asimov's prose, entrepreneurship
courses, and hawk–lemming predation.

The 48 new ones take disjoint territory: urban beekeeping, Roman marine
concrete, octopus cognition, museum repatriation, the four-day week, Yellowstone
wolves, handwriting versus typing, machine translation, urban tree canopy,
sourdough microbiology, adaptive optics, libraries as social infrastructure,
fire-stick farming, Sardinian nuraghi, ocean iron fertilization, cave-art dating,
induced demand for cycling, amber taphonomy, subglacial lakes, birdsong dialects,
vertical farming, audiobooks, sponge cities, craft guilds, lighthouses versus
satellite navigation, tulip mania, self-healing concrete, oral tradition and sea
level, plastic-digesting enzymes, platform work, antivenom, germ-free mice,
open-access publishing, Namibian conservancies, map projections, night-shift
handover, seed vaults, dazzle camouflage, pension defaults, mangrove replanting,
face recognition benchmarks, marathon shoes, desalination brine, school break
time, permafrost thaw, painting attribution, dam removal, and the spy novel.

## Question design

Real Cross-Text items ask about the *relationship* between two texts, not about
either one alone, and the four recurring shapes are all represented:

- how the author of Text 2 would respond to a claim in Text 1
- what relationship holds between the texts
- which assumption or step in Text 1 the evidence in Text 2 challenges
- how Text 2 qualifies, refines, or limits Text 1

The distractors are built from the errors students actually make on this type —
most often reading any critical second text as a flat denial of the first, when
the real relationship is a concession plus a limit. Several explanations say so
directly, because that is the transferable lesson.

Difficulty is spread across `EASY`, `MEDIUM` and `HARD` and written through to
`Question.difficulty` by the inserter, so the bank's difficulty filter and badge
report it correctly (see the difficulty-backfill note in CLAUDE.md for what goes
wrong when an inserter hardcodes it).

## Running it

```
PROD_URL=… node insert_ct.mjs batch1.json batch2.json batch3.json batch4.json           # report
PROD_URL=… node insert_ct.mjs batch1.json batch2.json batch3.json batch4.json --apply
```

Idempotent by `ref`: each question stores `CT-AUTHORED:<ref>` in `Question.source`
and the script skips any ref already present, so a re-run after an interruption
inserts only what is missing.

The validation pass runs **before** any write and refuses the whole batch on any
finding — both texts present in the passage, exactly four choices, exactly one
key, no duplicate choice text, a `whyWrong` entry for every distractor, a valid
difficulty, no LaTeX macro loose in prose, no markdown asterisks. A batch that
fails writes nothing rather than landing half of itself in a live bank.

## Still short

64 is a working pool, not parity. Four more batches of this size would bring
Cross-Text level with Text Structure and Purpose, the next-scarcest skill.
