# Test 29 — build manifest

147 questions: R&W 27/27/27 (Module 1 Standard, Module 2 Easy, Module 2 Hard) and Math
22/22/22 (19 MC + 3 FR each). **All 147 are originally authored.** Inserted as **DRAFT**
into the local dev database only; production was not touched.

Territory: brickworks and kilns, tile making, plasterwork and lath, stonemasonry and
tracery, scaffolding and hoists. Structural template: `../test-17-build/`.

## Files
| file | what it is |
|---|---|
| `math_test29.py` | 66 authored Math questions (inherited, unchanged) |
| `verify_math_test29.py` | sympy verification + originality passes for the Math |
| `rw_test29.py` | 81 authored R&W items, with a `DROPPED` note at the foot |
| `screen_topics.py` | originality screen: vs the 1,295-passage corpus, and vs itself |
| `balance_rw.py` | rotates choice order to even the answer key → `rw_test29_balanced.json` |
| `assemble_test29.py` | deals the quota, sorts on block rank → `test29.json` |
| `insert_test.mjs` | inserter (writes per-question difficulty, not a hardcoded MEDIUM) |
| `prescreen.py`, `bankgrep.py`, `mechanism_scan.py`, `screen_math.py` | Math triage tools |

## Verification run, in order — all green
```
python3 verify_math_test29.py        # ALL CHECKS PASSED
python3 screen_topics.py             # 81 passages screened — clean
python3 balance_rw.py                # 81 questions, 0 locked
python3 assemble_test29.py           # wrote test29.json — OK
python3 ../validate_tests.py 29      # PASS
node insert_test.mjs test29.json "Test 29"        # 147 inserted, local, DRAFT
node ../test-6-7-build/audit_math_rendering.mjs   # 1914 questions, 0 errors
```

## Numbers
- **Math** (unchanged from the state inherited): highest Jaccard vs the production bank
  0.60, worst within-Test-29 pair 0.45; skills spread across all 12; keys per module
  roughly 5/5/5/5. Domains 7 ALG / 6 ADV / 5 PSDA / 4 GT in every module.
- **R&W vs the corpus**: highest 0.292 (`B2`, a 40-word Boundaries passage, against
  `rw_test8:F4`). Read-threshold is 0.45 and reject 0.50, so nothing came near either.
  Short writing passages carry few tokens and score high on noise alone; the top dozen are
  all writing items for that reason.
- **R&W within the test**: worst student-visible same-subject pair **0.188**
  (`S9` vs `S4`, both Rhetorical Synthesis, both about stonemasonry — one the modern
  banker shop, the other tooling marks and dating). `validate_tests.py` rejects at 0.24.
- **Answer key**: raw A 25 / B 24 / C 17 / D 15 → balanced **A 21 / B 20 / C 20 / D 20**.
  Nothing was locked: every `why` names its options by content, so all 81 could rotate.

## The two things the writing pass caught
Both were found by substituting each of the four choices into the blank and reading the
whole sentence, not by any regex.

1. **`B9` repeated a word across the blank.** The passage ran `the _____ rules on hours`
   while the options were `masons' rules` / `mason's rules` / …, so every choice produced
   "the masons' rules rules on hours". This is exactly the `quarter; yet the` + `the custom`
   failure a sibling build shipped. Fixed by deleting the second `rules` from the passage.
2. **`B8`'s keyed choice left an interrupter half-punctuated.** The passage supplied
   `however,` with a trailing comma only, so the key produced `the result however, is`
   rather than `the result, however, is`. Fixed by moving the whole `; however,` inside the
   options, which also made the near-miss distractor (`; however the result`) a real one.

## Topics screened out
Recorded in full in the `DROPPED` block at the foot of `rw_test29.py`. In brief: **face
bedding** (too close to `rw_test18:W4`, Portland limestone beds), **lime mortar in every
form** (Test 19's), **plaster slip-casting moulds and glazed ware** (Test 16's), **tunnel
brickwork** (`rw_test20:R4`), **snapped headers** (would have restated `W7`), **the
treadwheel crane** (already `T4`). One collision was internal and only appeared after
drafting: `B11` was first written about the centring struck from under a closed arch and
scored **0.286 against `F6`**, the keystone item — same arch, two questions. `B11` was
rewritten to the bricklayer's line and tingle, keeping the dash-pair convention it tests;
the pair now scores 0.07.

## Sizing note for the next build in a narrow territory
The topic list was sized to **81 distinct sub-topics, one per item**, not to the ten
blocks. That is what kept the internal worst case at 0.188. `screen_topics.py` holds
**every** pair to 0.24, which is stricter than the validator (which exempts M2E↔M2H),
because `assemble_test29.py` shuffles before dealing and so module assignment is not known
while the passages are being written.

## Known gaps
- **No `Explanation` rows** — same as every test from 1 onward. The `why` field on each
  R&W item and the `check` field on each Math item carry the reasoning and are inserted,
  but the `Explanation` table itself is not populated.
- **No images anywhere.** Every arch, gable, course and roof is worded so the question is
  fully determined without a picture; the four data items (`E1`, `E4`, `E6`, plus the Math
  data-interpretation questions) use real `<table>` markup in the house style.
- Test 29 is **DRAFT in local dev only**. It has never been written to production, and
  publishing is the user's call from the admin panel.
