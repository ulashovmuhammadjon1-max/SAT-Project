# Test 29 — progress

**COMPLETE.** All 147 questions authored, verified, assembled, validated and inserted into
the local dev database as DRAFT. Production untouched, nothing committed. Full detail is in
`MANIFEST.md`; this file is the checkpoint log only.

## State
| stage | status |
|---|---|
| Math — 66 questions (`math_test29.py`) | inherited, unchanged, `verify_math_test29.py` PASSES |
| R&W — 81 items (`rw_test29.py`) | **all 81 written** |
| `screen_topics.py` | clean: corpus max 0.292, internal max 0.188 |
| `balance_rw.py` | A21/B20/C20/D20, 0 locked |
| `assemble_test29.py` → `test29.json` | 147, block order monotonic, writing opens at Q15 |
| `../validate_tests.py 29` | PASS, zero problems |
| local insert + `audit_math_rendering.mjs` | 147 inserted DRAFT; 1914 Math questions, 0 errors |

## R&W blocks — all written
Words in Context 12 (W1-W12) · Text Structure 6 (T1-T6) · Cross-Text 3 (X1-X3) · Central
Ideas 6 (C1-C6) · Command of Evidence 9 (E1-E9) · Inferences 6 (I1-I6) · Boundaries 12
(B1-B12) · Form/Structure/Sense 9 (F1-F9) · Transitions 9 (N1-N9) · Rhetorical Synthesis 9
(S1-S9). Per-module quota 4/2/1/2/3/2 reading + 4/3/3/3 writing = 27.

## Decisions a successor would otherwise have to re-derive
- **81 distinct sub-topics, one per item.** Sizing the topic list to the block count is what
  makes a narrow territory collide with itself; the `DROPPED` block at the foot of
  `rw_test29.py` lists what was abandoned and why.
- **`screen_topics.py` holds every internal pair to 0.24**, not just the M1↔M2 pairs the
  validator checks, because the assembler shuffles before dealing and module assignment is
  unknown while passages are being written.
- **Defects found by the substitution proofread**, not by any checker: `B9` repeated the
  word "rules" across the blank; `B8`'s key left "however" with only a trailing comma. Both
  fixed. Re-run that read for any future edit to a writing item.
- **Test 29 has three Cross-Text Connections items**, which Test 17 (the structural
  template) does not — `assemble_test29.py`'s QUOTA carries a line for that block, and
  asserts both that no block runs short and that no authored item goes undealt.
