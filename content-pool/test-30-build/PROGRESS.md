# Test 30 — build progress

**STATUS: COMPLETE.** Everything in the brief has been run and passes. See `MANIFEST.md` for
the full record; this file is the short checkpoint.

## Done
- `math_test30.py` (inherited, unchanged) — `verify_math_test30.py` **ALL CHECKS PASSED**.
- `rw_test30.py` — 81 items finished and checked. Nine defects found in the inherited draft and
  fixed (R5 double subject in every choice; F5 duplicated W7's subject; F6 nonsense distractors;
  B2 ambiguous participle; B3 non sequitur; B9 duplicated E7's subject; S2 duplicated
  `rw_test15:R4`'s camera lucida; W8 awkward frame; R7 two defensible transitions).
- Corpus dedupe: highest Jaccard vs `../rw_authored_corpus.json` **0.180**; nothing at 0.45.
- Within-test same-subject: worst pair **0.156**, threshold 0.24, zero pairs at or above it.
- `balance_rw.py` — key A81/B0/C0/D0 → **A21/B20/C20/D20**, 0 items locked.
- `assemble_test30.py` → `test30.json`, 147 questions, block order monotonic, writing at Q15.
- `python3 ../validate_tests.py 30` → **PASS**, zero problems.
- Local insert OK: `Test 30` = `230d1be8-1529-4741-bb7b-e9f910fe64f3`, DRAFT.
- `audit_math_rendering.mjs` (local) → 1,782 Math questions, **0 errors**.
- No `T18` string anywhere in the deliverables.

## Not done, deliberately
- No production write, no git commit, no publish. Test 30 is DRAFT in local dev only.
- Not screenshot-verified in `/exam/{attemptId}`; the rendering audit and the validator were
  the checks run instead.

## If you have to redo anything
Order is: `verify_math_test30.py` → `balance_rw.py` → `assemble_test30.py` →
`../validate_tests.py 30` → `insert_test.mjs` → `../test-6-7-build/audit_math_rendering.mjs`.
Re-run `balance_rw.py` **and** `assemble_test30.py` after any edit to `rw_test30.py`, or
`test30.json` goes stale against the source.
