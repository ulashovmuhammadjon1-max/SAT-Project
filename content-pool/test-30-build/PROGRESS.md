# Test 30 — build progress

Updated: session start + inventory.

## Done
- `math_test30.py` — 66 questions. `verify_math_test30.py` **passes** (highest Jaccard vs
  production 0.55; within-test 0.53; key M1 A7/B4/C5/D3, M2E 5/5/5/4, M2H 5/6/4/4).
- `rw_test30.py` — 81 items present, all 4-choice, unique `num`s, block counts match the
  assembler quota exactly (WiC 15, TSP 6, CID 6, CoE 9, Inf 6, Bnd 12, FSS 9, Trn 9, Syn 9).
  Every key is currently `A` (author wrote correct-first); `balance_rw.py` rotates.
- `assemble_test30.py` already exists and is correctly de-Test-18'd (refs `AUTHORED-T30:` /
  `AUTHORED/T30-`, seed 300030, reads `rw_test30_balanced.json`, writes `test30.json`).

## Done (cont.)
- Writing correctness pass finished (Boundaries 12, FSS 9, Transitions 9). Defects fixed:
  - B2: trailing absolute phrase "each of them then rounded" could be read as a finite clause,
    making the semicolon defensible → now "each of them ready to be rounded".
  - B3: "Iron was less easily broken" was a non sequitur after the porcelain sentence →
    "Iron tainted acid preparations and fell out of use".
  - F5: choices were stay/stays/staying/to stay on a **press/blotter/ventilator** passage that
    duplicated W7's subject → rewritten as a plural-vs-possessive item on seed jars on racks.
  - F6: distractors "canned"/"could have"/"having" against a tail "be matched" were nonsense →
    blank now takes the whole verb phrase (can be matched / can be matching / being matched /
    to be matched).
  - **R5 (real defect)**: every choice began "A chromatograph, …" while the sentence continued
    "a gas chromatograph separates …" — double subject in all four. Choices are now bare
    transitions (By contrast / Likewise / For instance / In short).
  - R7: "By comparison," was arguably defensible next to the keyed "In short," → replaced with
    "For instance,".
  - W8: "The specimen is the label's attachment" read awkwardly → "The plant, on this
    accounting, is an _____ to its label" (appendage / objection / improvement / alternative).
  - S2: camera lucida duplicated `rw_test15:R4` (same device, 5 shared 5-grams) → retargeted to
    the spent charge left in a still.
- Corpus dedupe: highest Jaccard vs `rw_authored_corpus.json` now **0.180** (S1 ~ rw_test8:R4),
  zero flags at the 0.50/5-gram screen. Nothing reached the 0.45 read line.
- Within-test same-subject scan with `validate_tests._passage_jaccard`: worst pair **0.179**
  (E7/B9), zero pairs at or above the 0.24 threshold.

## Left
- Reading-item correctness pass (W done, C/E/I/S outstanding); balance; assemble; validate;
  local insert; math audit; MANIFEST.md.

## Decisions a successor would have to re-derive
- Reading per module = 14 of 27, writing opens at Q15. Fixed by the quota, do not change.
- Rationales must not name an option by letter or `balance_rw.py` locks the item at `A`.
