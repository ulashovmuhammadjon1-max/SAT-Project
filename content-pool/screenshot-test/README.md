# Screenshot practice test (in progress)

A full practice test transcribed from screenshots the user is sending module by
module. Watermarks ("[ Meo ]", "[ bluecorn.org ]") are stripped. Every answer is
solved independently before the printed key is read; a disagreement is flagged
in `disputes`, never silently resolved.

Target shape (CLAUDE.md, Test 1 reference): R&W 27/27/27, Math 22/22/22,
inserted as DRAFT. The user publishes from the admin panel.

## Status
- R&W Module 1: COMPLETE, 27/27, block order verified, 0 key disputes. Difficulty not yet assigned (target 3 E / 15 M / 9 H).
  Open: Q7 stem inferred; Q7 "resources" and Q9 "argued" are placeholders for words the watermark covered.
- R&W Module 2 Hard: COMPLETE, 27/27, block order verified, no passage overlaps with Module 1 (checked with a positive control). Two cross-text items at the user's request.
- Math Module 1: COMPLETE, 22/22 (4 free-response), every answer checked with sympy.
- Math Module 2 Hard: COMPLETE 22/22 (7 free-response, over the cap). Q22 is the user's own question, rebuilt because the original was unsolvable; awaiting OK.

## Assembled as SPECIAL TEST
- `build_special_test.py` -> `special_test.json` -> `insert_special.mjs` (DATABASE_URL=target, SOURCE_URL=production).
- Both Module 2 Easy sections are COPIES of existing published questions (`m2e_from_db.json`, chosen by
  `select_m2e_from_db.py`): only items whose key passed the explanation gate, none from Tests 3/4, no
  passage overlap with this test, lowest student exposure first. Every one was re-solved by hand; 4 were
  rejected (2 template repeats of Math M1, 1 contradictory rounding instruction, 1 wrong key "July Falk")
  and 4 repaired (`FIXES` in the build script).
- Routing (set by the user): Easy modules switched off, every student goes to Module 2 Hard (cut-off 0%). The Easy modules stay in the database because students already answered 98 questions in them.
- Pinned first in every test list by `isFeaturedTest` in `src/lib/tests/order.ts`.
- Verified locally: math rendering audit 0 errors (positive control fires), 117 KaTeX spans compile at
  throwOnError: true, all 147 questions walked in the real exam screen with no raw LaTeX, no broken images.
