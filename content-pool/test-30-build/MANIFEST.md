# Test 30 — build manifest

Territory: physic gardens, essential-oil distilling, apothecary dispensing and weights,
herbarium pressing, seed drying and storage. Structural template: `test-18-build/`.
Test 18 holds brewing, so nothing here touches malt, hops, fermentation or casks; the
distilling in this test is of plant oils only.

147 questions: R&W 27/27/27 (Module 1 / Module 2 Easy / Module 2 Hard), Math 22/22/22
(19 MC + 3 FR each). All content is originally authored.

## Files
| file | what it is |
|---|---|
| `math_test30.py` | 66 authored Math questions (inherited, unchanged) |
| `verify_math_test30.py` | sympy verification + dedupe passes for the Math; **passes** |
| `rw_test30.py` | 81 authored R&W items, keyed and rationalised |
| `check_originality.py` | corpus/self screen (`keywords`, `ngrams`) |
| `balance_rw.py` | rotates the key; writes `rw_test30_balanced.json` |
| `assemble_test30.py` | deals the quota per module, sorts on block rank; writes `test30.json` |
| `insert_test.mjs` | inserter (writes per-question difficulty; do not use the Test 6 one) |
| `test30.json` | the assembled test, 147 questions |
| `PROGRESS.md` | running checkpoint state |

## Verification actually run
- `python3 verify_math_test30.py` — ALL CHECKS PASSED. Highest Math Jaccard vs production
  0.55, within-test 0.53; keys M1 A7/B4/C5/D3, M2E 5/5/5/4, M2H 5/6/4/4.
- `python3 check_originality.py ngrams` — highest R&W passage Jaccard vs
  `../rw_authored_corpus.json` (1,295 passages) **0.180** (S1 ~ `rw_test8:R4`); nothing reached
  the 0.45 read line, nothing near the 0.50 reject line; 0 flagged on shared 5-grams.
- Within-test same-subject scan using `validate_tests._passage_jaccard`: worst pair **0.156**
  (S1/S2) against a 0.24 threshold; zero pairs at or above it.
- Hand correctness pass over every writing item: each of the four choices substituted into the
  blank and the whole sentence read. Defects found and fixed are listed below.
- `python3 balance_rw.py` — 81 items, 0 locked by a letter-naming rationale,
  key A21/B20/C20/D20 (was A81/B0/C0/D0 as drafted).
- `python3 assemble_test30.py` — 27/27/27 R&W, 14 reading + 13 writing per module, writing
  opens at Q15 in all three, block rank monotonic, 0 duplicate refs.
- `python3 ../validate_tests.py 30` — **PASS**, zero problems.
- Local insert: `Test 30` = `230d1be8-1529-4741-bb7b-e9f910fe64f3`, DRAFT, 147 rows, one
  difficulty per module (MEDIUM / EASY / HARD).
- `node ../test-6-7-build/audit_math_rendering.mjs` against local — 1,782 Math questions across
  27 tests, **0 rendering errors, 0 style-only**.
- No `T18` string survives in `rw_test30.py`, `assemble_test30.py` or `test30.json`; refs are
  `AUTHORED-T30:` (R&W) and `AUTHORED/T30-MATH_*:` (Math).

## Defects found in the inherited R&W draft and fixed
1. **R5 (Transitions) — the real one.** All four choices began "A chromatograph, …" while the
   sentence continued "a gas chromatograph separates a sample…", so every option produced a
   double subject. Choices are now bare transitions (By contrast / Likewise / For instance /
   In short). This is the same family of defect the brief warned about ("quarter; yet the" +
   "the custom").
2. **F5** had stay/stays/staying/to stay on a press/blotter/ventilator passage that restated
   W7's subject almost sentence for sentence. Rewritten as a plural-vs-possessive item on
   sealed seed jars, which also diversified a block that was six-ninths subject-verb agreement.
3. **F6** used the tail "…_____ be matched to a field notebook entry", with distractors
   "canned", "could have", "having" — three non-words in context and no plausible second
   reading. The blank now takes the whole verb phrase (can be matched / can be matching /
   being matched / to be matched).
4. **B2** ended "…equal _____ each of them then rounded between the palms": "rounded" reads as
   a finite past-tense verb as easily as a participle, which made the semicolon defensible.
   Now "each of them ready to be rounded between the palms" — unambiguously a phrase.
5. **B3** keyed a full stop before "Iron was less easily broken", a non sequitur after a
   sentence about porcelain becoming the usual material. Continuation is now "Iron tainted acid
   preparations and fell out of use".
6. **B9** restated E7's subject (screening / winnowing / gravity table) in prose. Retargeted to
   an apothecary's apprenticeship, keeping the same series-then-semicolon lesson.
7. **S2** was a camera lucida note list; `rw_test15:R4` is also a camera lucida note list
   (5 shared 5-grams). Retargeted to the spent charge left in a still after a run.
8. **W8** ended "The specimen is the label's _____" with the key "attachment", which reads
   awkwardly in that frame. Now "The plant, on this accounting, is an _____ to its label"
   (appendage / objection / improvement / alternative).
9. **R7** offered "By comparison," beside the keyed "In short," for a sentence that does
   compare two arrangements — two defensible options. Replaced with "For instance,".

## Notes for a successor
- Reading is 14 of 27 in every module and writing opens at Q15; that is fixed by `QUOTA` in
  `assemble_test30.py` and must not be edited without re-running the validator.
- No rationale in `rw_test30.py` names an option by letter, which is why `balance_rw.py` was
  able to rotate all 81 items. Keep it that way.
- Test 30 is **DRAFT in local dev only**. Nothing was written to production, and nothing was
  committed to git — the parent session does that.
