# Test 28 — progress

Territory: coaching routes, stage timetables, farriery, coach building, drovers' roads, toll gates.

## State
- Math: 66 questions drafted, `verify_math_test28.py` passing (inherited, untouched).
- R&W: 81 items drafted in `rw_test28.py` (WiC 15, TSP 6, CID 6, CoE 9, Inf 6, Bnd 12, FSS 9, Trn 9, Syn 9).
- Raw key distribution before balancing: A 72, C 9. `balance_rw.py` rotates to ~21/20/20/20.

## Current task: full correctness pass on the R&W WRITING block (Bnd 12 + FSS 9 + Trn 9 + Syn 9 = 39 items)
Method: substitute each of the four choices into the blank and read the whole sentence; confirm
exactly one choice is correct; fix the CHOICE text, not the key, where the key is right.

### Done
- [x] Boundaries B1-B12 read by substitution.

### Defects found so far
1. **B7 choice C** `"quarter; yet the"` — the passage already continues `"the custom was never..."`,
   so it rendered **"yet the the custom"**. Malformed distractor. (Confirmed by the parent.)
2. **B2 choice C** `"ground; the amended bill and"` — the passage continues `"was published in
   October"`, so it rendered **"the amended bill and was published"**. Stray trailing `and`.
   Same defect class: the choice ran past the blank and collided with the text after it.
3. **B2 rationale** calls a no-punctuation run-on "a comma splice of a different kind" — a fused
   sentence has no comma. Wording fix.

No Boundaries KEY was wrong; all 12 keys verified correct by substitution.

### Left
- [ ] Form, Structure and Sense F1-F9
- [ ] Transitions T1-T9
- [ ] Rhetorical Synthesis R1-R9
- [ ] Spot-check reading items (W*, S*, C*, E*, N*) for the same defect class
- [ ] Apply fixes to rw_test28.py
- [ ] verify_math_test28.py / balance_rw.py / assemble_test28.py / validate_tests.py 28
- [ ] local insert + audit_math_rendering.mjs
- [ ] MANIFEST.md

## Decisions a successor would otherwise re-derive
- The defect class to hunt is **a choice whose text overlaps the words the passage already supplies
  after the blank** (duplicated word) or leaves a stray connective. Reading the choice alone will
  never show it; only substitution does.
- Do NOT touch production. Do NOT git commit. Only edit inside `content-pool/test-28-build/`.
- Re-run `assemble_test28.py` after ANY edit to `rw_test28.py` — a previous run shipped a stale
  `test28.json`.
