# Test 26 — build record

147 questions: R&W 27/27/27, Math 22/22/22 (19 MC + 3 FR per Math module). Everything is
originally authored. Inserted **local only**, as `DRAFT`
(`66747946-2e72-485c-a9d1-57a7c63c7e03`). Production was not touched.

Thematic territory: bell founding, campanology and change ringing, organ building, pipe voicing,
carillons, tuning and temperament. Test 20 holds foundries, so the metalwork here is about bells
and never about ironfounding in general. Structural template: `../test-20-build/`.

## Results

| | Test 26 |
|---|---|
| Math questions / verified | 66 / 66, `verify_math_test26.py` ALL CHECKS PASSED |
| highest Math Jaccard vs production | 0.69 (read; see below) |
| highest Math Jaccard internal | 0.59 |
| **highest R&W Jaccard vs corpus, passage + stem** | **0.47** |
| **highest R&W Jaccard vs corpus, passage only** | **0.17** |
| highest R&W within-test overlap | 0.20 (validator threshold 0.24) |
| worst Module 1 / Module 2 scene overlap | 0.20 |
| **R&W key before balancing** | **A 81, B 0, C 0, D 0** |
| **R&W key after balancing** | **A 21, B 20, C 20, D 20** |
| **rationales locked by letter-naming** | **0** |
| R&W topics dropped as collisions | 6 before drafting, 5 after |
| R&W items rewritten after first draft | 14 of 81 |

Corpus at build time: **1,295** banked R&W passages, **1,436** production Math stems.

## Files

`math_test26.py` and `verify_math_test26.py` were inherited complete and are unmodified — the
verifier was re-run once and still passes. Everything else in this directory was written or
retargeted for this build: `rw_test26.py` (81 items), `verify_rw_test26.py`, `balance_rw.py`,
`assemble_test26.py`, `insert_test.mjs`, `rw_test26_balanced.json`, `test26.json`.

Pipeline, in order:

```
python3 verify_math_test26.py
python3 verify_rw_test26.py
python3 balance_rw.py
python3 assemble_test26.py            # -> test26.json
python3 ../validate_tests.py 26       # PASS
service postgresql start
DATABASE_URL=... node insert_test.mjs test26.json "Test 26"
DATABASE_URL=... node ../test-6-7-build/audit_math_rendering.mjs
```

The rendering audit read **1,518 Math questions across 23 tests: 0 errors, 0 style-only.**

## Verified from the database, not from the JSON

Block order was re-derived from the inserted `Skill.code` values rather than from the file that
produced them. All three R&W modules: 27 questions, rank sequence non-decreasing, writing opens
at question 15, sequence
`CAS-WV ×5 → CAS-TS → CAS-CT → INI-CI ×2 → INI-CE ×3 → INI-IE ×2 → SEC-BS ×4 → SEC-FS ×3 →
EOI-TR ×3 → EOI-RS ×3`. Every one of the 81 R&W questions carries its own `Passage` row; question
order is contiguous from 1 in all six modules; every free-response answer is JSON-array encoded;
per-question difficulty matches module difficulty in all six modules; the R&W key reads
21/20/20/20 from the `AnswerChoice` table; no `T20` string survives in any stem or passage.

## The finding this build adds: a Rhetorical Synthesis item collides with its own test

`../validate_tests.py` grew a **0.24 within-test subject-repeat check** (added by a sibling agent,
calibrated against six shipped tests that top out at 0.207 and one confirmed defect at 0.278). It
failed Test 26 on the first assembly with two pairs, at 0.29 and 0.26.

Both were a **Words in Context item and a Rhetorical Synthesis item on the same territory**, and
the cause is structural rather than careless. A synthesis item's note list *is* the core facts of
its subject, stated plainly; a Words-in-Context passage on the same subject states the same facts
to set up its blank. With fourteen territories carrying 81 items, one Words-in-Context item and
one synthesis item land on each territory by construction, so the collision is the default
outcome, not an accident. Five items (`W1`, `W3`, `W4`, `W12`, `C3`) were retargeted to a
different *aspect* of the same territory — bell founding moved from the sweep board to the
clapper, organ building from the tracker action to the swell box, voicing from flue pipes to
reeds, stained glass from lead lines to fired paint, falconry from flying weight to the moult.
Internal maximum fell from 0.29 to 0.20.

**For the next build: pick the synthesis item's aspect first, then author the Words-in-Context
item on a different one.** It costs nothing at drafting time and it is a rewrite pass afterwards.

## The threshold-is-triage lesson reproduces in R&W

Tests 18-21 established it for Math: a template repeat that changes the setting words scores
*low* precisely because it changed the words. **It holds for R&W passages too, and it cost this
build nine rewritten items, none of which came anywhere near the 0.50 reject line.**

- **The platinum-iridium kilogram.** `rw_test14:I1` is that passage — the cylinder, its drift
  against its own copies, and the point that an artefact cannot be said to have gained or lost
  mass because it defines the unit. Three items here (`W15`, `E8`, `B11`) were built on exactly
  that argument. Highest score: **0.31**. All three moved to tide gauges and the vertical datum.
- **Deaf children at a new school, each cohort regularising what it inherited.** `rw_test9:W9` is
  that passage; `W14` scored **0.37** against it and `E5` made the identical claim about
  successive cohorts supplying consistency their models lacked. `W14` moved to birdsong learning,
  `E5` to shorthand and gallery reporting.
- **Volcanic ash layers tying distant ice cores together.** `rw_test10:B6`, scored **0.20** —
  which is below everything a shipped test does — and was `N8`'s entire premise. `N8` moved to
  shorthand.
- Two grammar items were template repeats with the nouns swapped: `rw_test9:F2`
  "Neither the copper pipes nor the boiler _____" was `F3`, and `rw_test8:F4` "Each of the three
  prototypes _____ its own control board" was `F5`'s frame. Both reframed.

Every one of these was found by **reading the printed match**, never by the score. The scores
would all have passed silently.

### Corollary: screen the CLAIM, not the topic word

`screen.py kw kilogram*` returned four R&W hits at the start of this build and they were not
read, because "kilogram" looked like an ordinary unit that would appear anywhere. One of those
four was the entire metrology passage. The keyword pass is worth nothing unless the hits are
opened; a count is not a screen. The same pass *did* work where it was used properly — six topics
were dropped before a word of them was written, including **railway time replacing local noon**,
which `rw_test14:B7` and `rw_test15:C2` both already hold almost verbatim.

## Why the headline corpus number is 0.47 and the real one is 0.17

The four highest scores against the corpus (0.30–0.47) are all short writing items matched against
other short writing items, and every one of them comes from the **formulaic stem**. `F2`'s passage
is nine words; its stem is "Which choice completes the text so that it conforms to the conventions
of Standard English?", which every Boundaries and Form/Structure item in the bank shares word for
word. Against `rw_test8:F4` — a completely unrelated item about circuit-board prototypes — the
shared stem alone carries the pair to 0.47.

`verify_rw_test26.py` therefore prints **both** numbers, and the passage-only one (0.17) is the
one worth reading. A future build should not chase the passage+stem figure down; it cannot go
much lower while the stems remain correct.

## Inherited Math: all eight matches above 0.45 were read

The brief said the Math was complete and not to be rewritten, so nothing was changed, but the
standing rule is to read every match above ~0.45 and the inherited verifier prints eight. All
eight are token-signature artefacts of short algebraic stems, and none is a template repeat:

| | mine | banked | verdict |
|---|---|---|---|
| 0.69 | `x²=3x`, x≠0, find x | Test 1 M2H Q5: `(x+3)²=30`, find `x²+6x` | different problem |
| 0.53 | circle `x²+y²=45` meets `y=2x`, **product of x-coordinates** | Test 17 M2H Q9: parabola meets a line, **sum of y-coordinates** | different curve, different quantity |
| 0.55 | `f(g(x))` as an **expression** | Test 7 M2H Q7: `f(g(2))` as a **value** | different task and functions |
| 0.56 / 0.54 / 0.53 / 0.53 / 0.52 | — | — | short-stem artefacts, unrelated problems |

## Two checker bugs found in my own code

Both in *checking* code, both producing false findings — the recurring own-goal.

- The Boundaries-option check demanded **four distinct punctuation profiles and identical words**
  across the four options. That is not what a Boundaries item is: real ones routinely offer
  `". The"` against `", the"` against `" and the"`, or pair a comma with *which* against no comma
  with *that*. It reported **seven findings on seven correct items**. Relaxed to "the options
  differ in punctuation at all", which is the property that actually distinguishes Boundaries
  from Form/Structure.
- The assembler's cross-module scene check was written at a 0.35 threshold, picked by feel. The
  shared validator's 0.24 — calibrated against real shipped tests at one end and a confirmed
  defect at the other — caught two pairs that 0.35 waved through. The assembler now uses 0.24.

The cross-module check is deliberately **not** a keyword match. A keyword list for this test would
have to contain "bell", "ring", "peal", "stop", "pipe", "tone" and "round", every one of which has
an ordinary English sense that would fire constantly — the `\bfen`-matching-"fence" family of bug.
It measures passage-token Jaccard between every Module 1 item and every Module 2 item instead, so
there is no boundary to get wrong.

## Known gaps

- **No `Explanation` rows** — consistent with every test since Test 1, and still a real content
  gap rather than a convention.
- **No images.** Every figure is real `<table>` markup in the house style block, so the three
  data items (`E1` hall reverberation, `E4` paper acidity, `E7` organ wind pressure) are fully
  determined without a picture.
- The test is **`DRAFT` in local dev only**. It has not been inserted into production and has not
  been opened in the real exam interface at `/exam/{attemptId}` — the last verification step in
  CLAUDE.md is still outstanding and should be done before publishing.
