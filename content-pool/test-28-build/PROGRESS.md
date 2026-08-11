# Test 28 — progress

Territory: coaching routes, stage timetables, farriery, coach building, drovers' roads, toll gates.

## State
- Math: 66 questions, `verify_math_test28.py` passing (inherited, untouched this pass).
- R&W: 81 items in `rw_test28.py` (WiC 15, TSP 6, CID 6, CoE 9, Inf 6, Bnd 12, FSS 9, Trn 9, Syn 9).
- **Correctness pass on the writing block: COMPLETE.** All 39 writing items (Bnd 12, FSS 9, Trn 9,
  Syn 9) read by substituting each of the four choices into the blank. All 42 reading items
  spot-checked the same way.

## Defects found and fixed (8)

### Seam collisions — a choice running past the blank into the words after it (4)
Found by `check_substitution.py`, which is new in this directory. **Two were not visible by
reading the option list, and one was in a KEY, not a distractor.**
1. **B7 choice C** `"quarter; yet the"` + passage `"the custom was never..."` -> **"yet the the
   custom"**. Replaced with `"quarter, however,"` (a comma splice, unambiguously wrong).
2. **B2 choice C** `"ground; the amended bill and"` + `"was published in October"` -> **"the
   amended bill and was published"**. Replaced with `"ground, the amended bill"` (comma splice).
3. **B3 — the KEY was malformed.** All four choices ended in `in` (`"wall; in"`) and the passage
   continued `"in the loose boxes"` -> **"wall; in in the loose boxes"**. Fixed by deleting the
   duplicated `in` from the PASSAGE, so the choices supply it. Key unchanged and still correct.
4. **B12 — the KEY was malformed.** All four choices ended in `the` (`"years; the"`) and the
   passage continued `"the remaining five"` -> **"years; the the remaining"**. Same fix: the
   duplicated `the` deleted from the passage.

### Two-correct-answer risks (2)
5. **F1 choice C** was `"have been"` — PLURAL, so it agreed in number just as the key `"were"`
   does, and the rationale's claim that the wrong options are singular was false. Changed to
   `"has been"`. Key unchanged.
6. **W5** `"handed the bidder the whole of the _____"` — `profit` was as defensible as the key
   `risk` (a fixed sum to the trust, the residual to the bidder is a real reading). Passage now
   adds `"A wet season that kept the wagons off the road fell on him and not on the trust"`, which
   only `risk` completes. Rationale rewritten.
7. **W9** `"not a fashion but a _____"` — `convenience` was live, because the passage justified the
   angled room by a keeper seeing "without rising", which is convenience, not necessity. Rewritten
   to "nothing could reach the bar from either road without having been seen from that window".

### Typography / wording (2, counted as one defect above plus one)
8. **Seven passages wrote the blank as `_____ .`** with a space before the full stop — renders as
   "stayed constant ." No other build in `content-pool/` does this (checked all of 20-29). Fixed.
9. **T6** put `Thus,` two sentences after `A line was therefore divided` — the passage handed the
   answer away. `therefore` -> `instead`. Rationale also called the conclusion a "restatement",
   which argues for `In other words` rather than the key; reworded to "follows directly from".
   Same for **B2**'s rationale, which called a no-punctuation run-on "a comma splice", though a
   fused sentence has no comma.

**No answer key was wrong.** Every one of the 81 keys is the correct option; the defects were all
in distractors, passages or rationales. B3 and B12 are the closest calls — the key OPTION was
malformed there, but the option it named was still the right one.

## New tool: check_substitution.py
Runs over all four options of all 48 blank-bearing items. Reports DOUBLE / DANGLE only when the
match **straddles the edge of the inserted choice** — one word from the option, one from the
passage. That precision matters: a first cut that scanned the whole substituted passage reported
97 findings, 93 of them ordinary compound predicates. Currently **0 findings**; a regression test
re-injecting the four original defects confirms it still fires on them.

## Left
- [ ] verify_math_test28.py / balance_rw.py / assemble_test28.py / validate_tests.py 28
- [ ] local insert + audit_math_rendering.mjs
- [ ] MANIFEST.md

## Decisions a successor would otherwise re-derive
- The defect class to hunt is a choice whose text overlaps what the passage supplies on the other
  side of the blank. Reading the option list will never show it; only substitution does. Run
  `python3 check_substitution.py`.
- Rationales must name options by CONTENT, never by letter, or `balance_rw.py` refuses to rotate
  them. Verified: 0 of 81 name a letter, so all 81 are rotatable.
- Do NOT touch production. Do NOT git commit. Only edit inside `content-pool/test-28-build/`.
- Re-run `assemble_test28.py` after ANY edit to `rw_test28.py` — a previous run shipped a stale
  `test28.json`.
