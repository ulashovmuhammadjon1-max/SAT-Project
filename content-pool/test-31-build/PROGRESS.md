# Test 31 — build progress

Territory: poultry and egg grading, dovecotes, falconry and mews, decoy ponds,
eel traps and fish ponds. Structural template: `content-pool/test-19-build/`.

## Status

| step | state |
|---|---|
| `math_test31.py` (66 items) | DRAFTED, verifier passes |
| `verify_math_test31.py` 4 passes | PASSING |
| hand-audit of all 66 stems vs derivations | DONE — no math errors found |
| `mechanism_search.py` | in progress |
| `rw_test31.py` (81 items) | drafted, being validated |
| F4 rationale fix | pending |
| `balance_rw.py` | pending |
| `assemble_test31.py` | pending (must be created from ../test-19-build/) |
| `test31.json` | pending |
| `../validate_tests.py 31` | pending |
| local DB insert + math render audit | pending |

## Decisions a successor would otherwise have to re-derive

- `F4` is an **R&W** item (`rw_test31.py` ~line 964, Form/Structure/Sense), not a
  Math item. The handover called it a Math item; it is not.
- `verify_math_test31.py` was ALREADY passing when this run started. All 66
  derivations were read against their stems by hand this run; every one models
  the stem independently (no derivation quotes the `check` note). No incorrect
  Math answer was found.
- Corpora are at the content-pool ROOT and are READ ONLY:
  `../prod_math_stems.json` (1,386), `../rw_authored_corpus.json` (1,295).
- `assemble_test19.py` in this directory is the WRONG file; a Test 31 assembler
  must be written and the `_ref` tags must contain no `T19` string.
