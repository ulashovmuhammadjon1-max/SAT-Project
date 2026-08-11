# Test 29 — progress

Territory: brickworks and kilns, tile making, plasterwork and lath, stonemasonry and
tracery, scaffolding and hoists. Structural template: `../test-17-build/`.

## Done
- **Math** — `math_test29.py`, 66 questions. `verify_math_test29.py` PASSES (highest Jaccard
  vs production 0.60, within-test 0.45, all sympy checks green). Do not rewrite.
- **`screen_topics.py`** — written. Pass 1 = each passage vs the 1,295-passage corpus
  (read >=0.45, reject >=0.50). Pass 2 = every internal pair, held to 0.24, using
  `validate_tests.py`'s own imported tokenizer. Assembler shuffles before dealing, so
  module assignment is unknown at authoring time and ALL pairs must clear 0.24, not just
  M1-vs-M2 pairs.

## R&W blocks (81 total; quota per module 4/2/1/2/3/2 reading + 4/3/3/3 writing)
| block | need | written |
|---|---|---|
| Words in Context | 12 | 12 (W1-W12) |
| Text Structure and Purpose | 6 | 6 (T1-T6) |
| Cross-Text Connections | 3 | 3 (X1-X3) |
| Central Ideas and Details | 6 | 0 |
| Command of Evidence | 9 | 0 |
| Inferences | 6 | 0 |
| Boundaries | 12 | 0 |
| Form, Structure, and Sense | 9 | 0 |
| Transitions | 9 | 0 |
| Rhetorical Synthesis | 9 | 0 |

## Sub-topics already spent (do not reuse — one sub-topic per item, 81 distinct)
W1 winter weathering of clay; W2 pug mill; W3 wire-cut vs moulded face; W4 hacks and
drying; W5 continuous ring kiln; W6 the frog; W7 headers tying a wall; W8 efflorescence;
W9 tile nib and batten; W10 inlaid floor tile; W11 mathematical tiles; W12 squaring a
block at the bench. T1 updraught vs downdraught kiln; T2 masons' marks; T3 putlog holes;
T4 the great wheel in a church roof; T5 moulded terracotta; T6 standard brick size.
X1 machine vs handmade tile; X2 the tracing floor; X3 the 1784 brick duty.

## Neighbouring builds — ground to stay off
- Test 18 quarrying (no stone is extracted here). Corpus `rw_test18:W4` is Portland
  limestone BEDS — so **face-bedding was dropped** as too close in vocabulary.
- Test 19 lime burning: no lime kiln, no quicklime, no lime-vs-cement mortar argument
  (`rw_test19:C3`, `F4`, `B1`, `R6`, `W11`).
- Test 16 pottery kilns, glaze faults, plaster slip-casting moulds (`rw_test16:B1`).
- Test 20 `R4` tunnelling shield with brickwork behind it.
- Tests 11/12 Great Zimbabwe mortarless coursing.

## Remaining
Author C1-C6, E1-E9, I1-I6, B1-B12, F1-F9, N1-N9, S1-S9. Then `balance_rw.py`,
`assemble_test29.py`, `../validate_tests.py 29`, local insert, math render audit.
