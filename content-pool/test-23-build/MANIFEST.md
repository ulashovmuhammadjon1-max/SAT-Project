# Test 23 — build record

147 questions: R&W 27/27/27, Math 22/22/22 (19 MC + 3 FR per Math module). Everything is
originally authored. **Inserted into the local dev database only, as `DRAFT`**
(`42c058fa-ead4-4fbc-b484-a66b875f7a57`). Production was not touched.

| | |
|---|---|
| thematic territory | canal locks and pounds, barge haulage, aqueducts, dredging, towpaths, wharves and quays, canal toll keeping |
| structural template | `../test-17-build/` |
| corpus at build time | 1,295 banked R&W passages (`../rw_authored_corpus.json`) |

## Results

| | |
|---|---|
| Math sympy verification | **66/66**, `verify_math_test23.py` re-run and passing |
| highest Math Jaccard vs production | 0.72 |
| highest Math Jaccard within Test 23 | 0.61 |
| **highest R&W Jaccard vs corpus** | **0.14** (passage-only; nothing at or above 0.45) |
| R&W items sharing a 5-gram with the bank | 0 |
| **R&W key before balancing** | **A 78, B 1, C 2, D 0** |
| **R&W key after balancing** | **A 21, B 20, C 20, D 20** |
| **rationales locked by letter-naming** | **0** — every `why` names options by content |
| **R&W topics dropped as collisions** | **19** (listed as `DROPPED` at the foot of `rw_test23.py`) |
| R&W subjects rewritten for intra-test overlap | 24 (see below) |
| max intra-test passage Jaccard | 0.196, against the validator's 0.24 |
| `../validate_tests.py 23` | PASS |
| `../test-6-7-build/audit_math_rendering.mjs` | clean over all 1,452 Math questions in the local DB |

Per-module R&W shape: 15 reading + 12 writing, writing opening at question 16, block sequence
non-decreasing in all three modules. Quota per module: Words in Context 5, Text Structure and
Purpose 2, **Cross-Text Connections 1**, Central Ideas and Details 2, Command of Evidence 3,
Inferences 2, Boundaries 3, Form/Structure/Sense 3, Transitions 3, Rhetorical Synthesis 3.
Unlike Test 17 this test carries a Cross-Text item in every module; the block is optional in
the mandated sequence but it is a real domain and 15 reading questions leave room for it.

## The finding this build adds: a narrow territory collides with ITSELF, not with the bank

Test 23's territory is one subject — canals — where earlier tests had fifteen. The consequence is
the opposite of what the accumulated findings predict. Against the 1,295-passage bank the whole
test scored **0.14**, the lowest of any build so far, because no banked passage is about canals.
Against *itself* the first draft failed `validate_tests.py` on **15 same-subject pairs**, three of
them above 0.50:

- `W11` and `N5` at **0.56** — a Words in Context item and a Transitions item that both argued
  a horse leaves the bank alone while a propeller's wash carries clay away. The same paragraph
  twice.
- `C3` and `R3` at **0.55** — stop gates explained as a reading passage and then again as a set
  of synthesis notes.
- `W6` and `N9` at **0.53** — the 1792 subscription lists, verbatim in both.

The mechanism is worth stating plainly, because it is not the one the earlier manifests describe.
With 27 sub-topics and 81 items, each sub-topic gets used three times, and the third use is
almost always a Rhetorical Synthesis note-set restating a reading passage it was written next to.
**Seven of the nine synthesis items restated another item in the test.** The notes format invites
it: bullet points are the passage with the prose removed.

Two rules follow:

1. **A build needs roughly as many distinct subjects as it has R&W items**, not as many as it has
   blocks. Sizing the topic list to 27 guaranteed the failure before a word was written.
2. **Never draft a Rhetorical Synthesis note-set beside the reading passage on the same subject.**
   Give the synthesis block its own subjects from the start.

The fix was to re-subject 24 items — all nine synthesis items and fifteen writing-domain items
(N2, N3, N5, N7, N9, B2, B5, B7, B8, F1, F4, F5, F7, F9, W10) — onto sub-topics used nowhere else:
winding holes, compensation water owed to millers, bridge numbering, day boats, tunnel ventilation
shafts, canal constables, the lengthsman, stop planks, the horse boy's trip money, frost in lock
masonry, towpath milestones, cutting versus tunnel, warehouse hand cranes, windlasses, bonded
warehouses, the horse-marine, roses-and-castles painting, families aboard and the 1877 Act, wide
versus narrow locks, reservoirs sold to a waterworks, aqueduct expansion joints, the stop lock at
a company boundary, and gauging. Every one was keyword-screened against the bank before drafting
and all came back clean. Result: **0 pairs at or above 0.20**, against a 0.24 threshold and the
0.207 that six shipped tests reach.

Note that `validate_tests.py` gained this same-subject check *during* this build. It caught a real
and substantial defect that no per-build verifier here would have found, since every one of the 15
pairs scored far below the 0.50 corpus threshold and the corpus check only ever looks outward.

## Grammar items repeat as templates, exactly as Math questions do

The Test 18-21 finding — read every match near the threshold rather than trusting the number —
reproduced on the R&W writing domains, which the earlier manifests had not tested it against.
Five Form/Structure items were rewritten after reading matches that scored **0.32 to 0.44**:

- `F1` was `The record of the tolls … _____ in the county archive` against `rw_authored A-F1`'s
  `The collection of woodblock prints … _____ views` — the same "singular collective noun of
  plural, in an archive" template.
- `F2` was `By the time the surveyor reached …, the frost _____` against thirteen banked `By the
  time` items, one of which (`rw_test13 F3`) is itself about a **lock** being rebuilt.
- `F3` was `Each of the four companies … _____ payment` against `rw_test8 F4`'s `Each of the three
  prototypes _____ its own control board`.
- `F5` was `The number of boats legged … _____ every year` against `rw_test9 F1`'s `The number of
  applicants … _____ risen every year`.
- `F7` used `along with` as its agreement trap, as `rw_test8 F2` and `rw_test18 F1` already do.

The bank now holds 115 Form/Structure items and the standard conventions are close to exhausted.
Before writing one, grep the corpus for the *construction* (`Each of the`, `The number of`, `By
the time`, `along with`, `Neither … nor`, `Among … _____`) rather than for the subject matter.
`Neither … nor` was dropped outright: 22 banked passages use it.

## Two bugs in checking code, both mine

Same family as `\bpi` and `<u` matching `<ul`.

- `screen_topics.py final` folded the **stem** into the token set. Every writing-domain stem is
  the identical mandated sentence, so all 63 writing items reported a shared 5-gram with the bank,
  and Jaccard was inflated to 0.44 on the one-sentence grammar passages. Passage-only comparison
  drops the true maximum to 0.14 and the 5-gram hits to 0. The Rhetorical Synthesis opener
  (`While researching a topic…`) is stripped for the same reason — left in, it makes all nine
  synthesis items report a hit against every synthesis item ever banked.
- A hand check asserting that Boundaries options differ only in punctuation reported two failures.
  Both were false: `B1`'s full-stop option correctly capitalises the following word, and `B5`'s
  dash option contains `&mdash;`, whose entity name matched as a word. Fold case and strip
  entities before comparing.

Keyword screening deliberately avoids `lock`, `pound`, `reach`, `gate`, `lift` and `tow` as bare
terms — every one is ordinary English or a prefix of one (`block`, `compound`, `town`), and on a
canal all six carry a technical sense as well. They are used only inside multi-word phrases.

## Provenance trap

Scaffolding the assembler from Test 17 required replacing **two** differently-spelled tags:
`AUTHORED-T17:` on R&W and `AUTHORED/T17-` on Math. A substitution keyed on the hyphen catches
only the Math one. Both are replaced explicitly in the copy step and `test23.json` is asserted to
contain no `T17` string; `validate_tests.py` re-checks it independently.

## Pipeline

```
python3 verify_math_test23.py                     # 66/66
python3 screen_topics.py keywords                 # screen a topic BEFORE writing it
python3 screen_topics.py final                    # screen finished passages
python3 balance_rw.py                             # -> rw_test23_balanced.json
python3 assemble_test23.py                        # -> test23.json
python3 ../validate_tests.py 23                   # independent structural check
service postgresql start
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/sat_platform?schema=public' \
  node insert_test.mjs test23.json "Test 23"
DATABASE_URL='postgresql://postgres:postgres@localhost:5432/sat_platform?schema=public' \
  node ../test-6-7-build/audit_math_rendering.mjs
```

Add `--publish` to the inserter to publish; it was **not** used. `insert_test.mjs` is idempotent
and skips a Test or Module that already exists.

## Known gaps

- No `Explanation` rows, consistent with every test from Test 1 onward.
- No images. All three data questions are real `<table>` markup in the exact CLAUDE.md style
  block; no question depends on a picture.
- Not verified in the real exam interface (`/exam/{attemptId}`). Content was checked from the
  assembled JSON and read back from the database, but no attempt was seeded and no page was
  rendered.
- Not inserted into production and not published.
