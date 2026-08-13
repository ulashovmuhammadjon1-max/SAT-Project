# Broken questions found while authoring explanations

Structural defects in **live** questions, found by the authoring agents and
then confirmed directly against production. These need the *question* repaired
— a key change does not fix any of them.

Kept separate from REVIEW.md because `review_report.mjs` rewrites that file
from the JSONL on every run, and would erase anything hand-written in it.

## Unanswerable as it stands

- **Test 7 · Math M2 Easy q17** (`060a8be5`) — the stem begins with the literal
  placeholder token `TABLE_B` and the question asks "how many more tickets were
  sold for the screening with the greatest number…". There is **no `<table>`
  markup and no image**: the table it refers to does not exist. The key says 92,
  but nothing on screen lets a student reach it. This is live.

## Two correct answers

- **Test 6 · Math M1 q6** (`b4f10f7d`) — the relationship is `p = 35c + 6`.
  Choice A is `35c - p = -6` (keyed) and choice D is `p - 35c = 6`. Rearranged,
  both are `p = 35c + 6` — the same equation. A student choosing D is marked
  wrong for a correct answer.
- **Test 2 · Math M1 q16** (`lismstoib…`) — "Which expression is equivalent to
  \(\sqrt{48}\)?" Key is A `\(4\sqrt{3}\)`; choice C is `\(2\sqrt{12}\)`.
  Both equal 6.9282…, verified arithmetically. C is only "wrong" for not being
  in simplest radical form, which the stem never asks for.

## Duplicate-value choices (grading unaffected, choice set redundant)

- **Test 6 · Math M2 Easy q12** (`04294af7`) — A is `\(\frac{49}{2}\)` and B is
  `24.5`: the same number twice. Key C (7) is unaffected.
- **Test 1 · Math M2 Easy q21** — A is `\(36\pi\)` (keyed) and D is
  `36π (approx)`, with D using a raw π glyph outside a math span.
- **Test 2 · Math M2 Easy q21** — B is `\(3\pi\)` (keyed) and D is
  `3π (approx)`. Choice A is `\(3π/2\)` — raw glyph and slash fraction inside
  a math span.

## The same question in two different tests

A full exact-duplicate scan over all 4,557 published questions (signature =
passage + stem, so a reordered choice set still matches) found **14 duplicate
groups covering 28 questions**, and they are overwhelmingly one pair:

| tests | shared items |
|---|---|
| **Test 6 + Test 7** | **11** |
| Test 4 + Test 5 | 1 |
| Test 5 + Test 6 | 1 |
| Test 4 + Test 6 | 1 |

Test 7 recycles eleven R&W items from Test 6 verbatim. A student who sits both
meets the same question twice. Worse, **five of the eleven land in a different
difficulty branch** — an Easy-branch student in one test meets the identical
item on the Hard branch in the other:

- Test 6 M1 q20 → Test 7 M2 **Hard** q21
- Test 6 M1 q24 → Test 7 M2 **Easy** q22
- Test 6 M2 Easy q4 → Test 7 M2 **Hard** q2
- Test 6 M2 Easy q26 → Test 7 M2 **Hard** q26
- Test 6 M2 Hard q26 → Test 7 M2 **Easy** q26

The remaining six sit in comparable positions: M1 q1→q2, M1 q18→q17,
M2E q5→M2E q1, M2H q21→q20, M2H q22→q24, M2H q23→q22.

## Near-duplicates within one module

The scan above matches only *exact* passage+stem pairs and returns zero
within-test hits. These two were found by agents reading the questions, and
differ by a few words in the passage, so a strict signature misses them:



- **Test 3 · R&W M1 q9 and q10** — identical stems (similarity 1.00).
- **Test 4 · R&W M2 Hard q9 and q10** — identical lake-ice table and stem.

## Identical distractors

- **Test 2 · R&W M2 Hard q17** — choices B and D are byte-identical
  ("advocate, Ernesto Hernandez-Lopez,"). Key is C, so it still grades, but two
  of four options are the same string.

## Rendering defects

- **Test 3 · M1 q6, q19** — a whole prose sentence wrapped in `\( … \)`; KaTeX
  drops the spaces and it renders as run-on text.
- **Test 3 · M1 q3** — `cos(A)` unescaped inside math mode, rendering as three
  italic variables instead of the function.
- **Test 3 · M2 Hard q12** — carries `[Graph/figure not available]` where its
  table should be.
- **Test 1 · M2 Easy q14, M2 Hard q27** — raw markdown asterisks around titles
  instead of `<em>`.
- **Test 3 · M1 q7, M2 Hard q17/q22** — the stem describes the figure in prose
  alongside the real image (the answer leak CLAUDE.md rule 3 warns about).

## Coverage gap (a content decision, not a bug)

- **Tests 8 and 9** contain **no Command of Evidence — Graph/Table** questions
  at all. All 18 `INI-CE` items across their six modules are the
  "which finding, if true, would support/weaken" type. That is block 7 of the
  mandated R&W domain-block sequence, empty in both tests.


## Same scenario reused across sibling tests (Tests 14 / 15)

Found by `t12-rw-b` while authoring, and **not caught by the exact-duplicate
scan**, because the passages differ by a few words. The exact scan matches
passage+stem verbatim; these are rewrites of the same material.

The one that is effectively a duplicate — verified against production:

| | Test 14 M2 Hard q1 | Test 15 M2 Hard q4 |
|---|---|---|
| passage | "A male sandgrouse may nest fifty kilometres from the nearest water…" | same scenario, near-identical wording |
| skill | Words in Context | Words in Context |
| branch | M2 Hard | M2 Hard |
| **key** | **vessel** | **a container** |

Same passage material, same skill, same slot type, same difficulty branch, and
the two correct answers are synonyms of each other. This is one question
shipped twice; one of the pair needs replacing.

Nine further scenarios appear once in each test, in different skills or slots —
Nicaraguan deaf children, gecko toe hairs, railway time zones, gold tesserae,
Exchequer tally sticks, the Athenian allotment machine, bar-headed geese,
sundial vs clock, and a contrast-transition template landing at q22 in both.
A student sitting both tests meets each scenario twice.

None of these collide *within* a single test, so the CLAUDE.md rule about a
Module 2 item reusing a Module 1 setting is not violated in either package.
The cause is the documented one: sibling authoring agents that were not steered
onto disjoint thematic territory. It is the same failure that cost Tests 13 and
14 a repair pass during the original build.


## Tests 14 and 15 share Math templates too — same slot, same numbers

`t12-math-b` found the collision running through Math as well, question-for-
question in matching slots. Verified against production:

| | Test 14 M2 Easy **q16** | Test 15 M2 Easy **q16** |
|---|---|---|
| stem | "The price of a season ticket fell from **$250 to $210**" | "A cycle shop's stock of helmets fell from **250 to 210**" |
| answer | **16%** | **16%** |

Identical numbers, identical answer, identical slot number — only the setting
words differ. Seven more pairs behave the same way:

- **M2 Hard q1** — `6x-4y=10 / 9x+cy=15` against `6x-4y=14 / 9x+ky=21`, the same
  four choices (-6 / -4 / 4 / 6).
- **M1 q10** — the same decay function `6250(1/5)^d` in the same "tracer"
  framing, target 10 against 2.
- **M2 Easy q22** — a 9-12-15 right triangle in both (guy wire / batten).
- **M1 q12** — solve `(5c-12)/3` for c against `(5g-8)/3` for g.
- **M2 Hard q3** — the same "at least 3 of item B per item A, capped resource"
  optimisation.
- **M1 q3 / q4** — the same grant-minus-licence-fee-then-divide setup.
- Kiln / percent-cracked data tables at Test 14 M2 Hard q15 and Test 15 M1 q17.

**Why the existing dedupe missed all of this.** These score *low* on token
Jaccard precisely because the setting words changed — the exact trap CLAUDE.md
records under "a similarity threshold decides what to READ, not what to
accept". The numbers survived; only the nouns moved.

Combined with the ten R&W scenario pairs above, **Tests 14 and 15 are close to
parallel forms of one another.** A student sitting both meets the same
mathematics and the same passages twice. This needs a decision: rebuild one of
the two, or accept them as an intentional pair and say so.

## Found during the Tests 18-23 and review-list passes

### Test 7 R&W M2 Hard q10 is unanswerable — no graph
`97278a56-e5a3-4704-9af0-224bac8e42fe`. The stem reads "Which choice most
effectively uses data from the graph to complete the example?" and asks the
student to pick between percentages for individual 9 and individual 12. There is
no graph: `Question.imageUrl` is null, the passage carries no image, and the
passage contains no `<table>`. Every choice is a bare pair of numbers with
nothing to check them against.

This is the second question of this shape in Test 7, after M2 Easy q17 (stem
opens with the literal token `TABLE_B`, no table). Both need the missing figure
supplied or the question replaced; neither can be repaired with an explanation,
which is why both are still uncovered.

### Test 23 R&W Module 1 leaks its own answer
Reported by the agent covering Tests 22-23, confirmed as a content problem
rather than a rendering one. Module 1 q6's passage prints the sentence
"Weed cutting takes off what has grown in the water this season; dredging takes
out what has settled on the bed over many." Module 1 **q17** then asks the
student to punctuate that same sentence — and the semicolon they must supply is
already on screen eleven questions earlier in the same module.

### Test 23 repeats content across modules a single student sees
A student takes Module 1 plus one Module 2 branch, so a Module 2 item reusing
Module 1 material shows the same passage twice to half the cohort.
- M1 q8 (Cross-Text) states the statutory rate ceiling; **M2 Hard q14** is an
  Inference item whose answer is that same proposition, and **M2 Easy q24** is a
  Transitions item built from a near-verbatim restatement of it.
- M2 Easy q8's Text 1 and M2 Easy q23 are the same two clauses, about fifteen
  questions apart in one module.

### Test 22 and Test 23 share a trigonometry template
Test 22 M2 Hard q21 (`508c39f6-1970-4e23-a6af-6747ccafe90c`) and Test 23 M2 Hard
q19 (`59425706-9db9-4346-a631-4045fd17c91b`) are the same 5-12-13 triangle with
the same given ratio; only which angle's tangent is requested differs. Both are
correct as written.

## Answer keys corrected on the review list

Seven of the 53 held-back questions were adjudicated and the key was found
wrong. `fix_keys.mjs` carries the full reasoning for each; the agents' own
explanations then shipped through the normal pipeline.

| question | was | now | why |
|---|---|---|---|
| Test 1 R&W M1 q7 | D | A | The underlined portion is the refutation; the explanation it overturns sits before the underline. |
| Test 1 Math M1 q8 | A | B | Line n passes through (0, 3) and hits y = 12 at x = 1.5, so its slope is 6 and the perpendicular is -1/6. |
| Test 1 R&W M1 q16 | D | B | Both sides of the blank are independent clauses; the keyed comma is a splice. |
| Test 1 R&W M2 Hard q7 | C | D | The next sentence says the Comanche center "employs a similar strategy", so the sentence cannot be distinguishing this center from other tribal centers. |
| Test 2 R&W M1 q22 | A | C | The sentence restates the one before it rather than exemplifying it. |
| Test 2 R&W M2 Hard q3 | B | C | "unique, rapidly evolving local conditions" defines the blank as "distinctive to"; "prohibitive in" contradicts the advantage being described. |
| Test 10 R&W M2 Easy q14 | A | D | Only the ring inference is supported by the passage; lifespan is never mentioned, and choices B and C are the two reversals of the density sentence. |

One was adjudicated the other way — **Test 2 R&W M2 Hard q22**, where the key
"However" is correct and the agent's "Therefore" was wrong. Its explanation was
written by hand (`manual.json`) because the agent's argued for the wrong answer.

Six of these seven are in Tests 1 and 2, both transcribed. That is the same
pattern the original audit found, now confirmed a level deeper: the errors are
in the transcribed keys, not in the agents.
