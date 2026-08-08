# Tests 19, 20 and 21 — build record

All three are **PUBLISHED** in production, 147 questions each. This file covers all three; the
Test 20 and 21 directories point back here. The equivalent record for the previous group is
`../test-16-build/MANIFEST.md`, and the pipeline itself is unchanged from it.

| test | reference template | thematic territory |
|---|---|---|
| Test 19 | Test 16 | peat and turbary, tanning, mills, charcoal, basketry, thatching, lime burning, fen drainage |
| Test 20 | Test 17 | coal mining, gas works, telegraphy and cable laying, tramways, foundries, boilers, tunnelling |
| Test 21 | Test 18 | vineyards, sericulture, wheelwrighting, observatories, photographic plates, weather stations |

Every question is originally authored. Corpora at build time: **1,188** production Math stems
and **1,052** R&W passages (`../rw_authored_corpus.json`).

## Results

| | Test 19 | Test 20 | Test 21 |
|---|---|---|---|
| highest Math Jaccard vs production | 0.50 | 0.57 | 0.58 |
| highest Math Jaccard internal | 0.48 | 0.43 | 0.56 |
| sympy coverage | 65/66 | 64/66 | **66/66** |
| `MANUAL` items | 1 | 2 | 0 |
| highest R&W Jaccard vs corpus | 0.14 | 0.17 | 0.16 |
| R&W key before balancing | A72 B4 C5 D0 | A51 B19 C9 D2 | A71 B8 C2 D0 |
| R&W key after balancing | 21/20/20/20 | 21/20/20/20 | 21/20/20/20 |
| rationales locked by letter-naming | 0 | 0 | 0 |
| R&W topics dropped as collisions | 25 | 37 | 14 |
| Math questions rewritten as repeats | 19 | 11 | 18 |

Cross-sibling worst case: Math 0.53, R&W passages 0.17 — thresholds 0.75 and 0.50.

Post-publish, read back from production: 21 tests, all PUBLISHED at 147, **3,087 questions**;
per-question difficulty matching module difficulty at 1,029/1,029/1,029; every multiple-choice
question with exactly one key; all free-response answers JSON-array encoded; no answer choice
without a letter or digit; question order contiguous from 1 in every module; the DB-wide
rendering audit clean over all 1,386 Math questions.

## The finding this group establishes

**A similarity threshold does not decide originality — reading does.** Across the three tests,
**48 Math questions were rewritten as genuine template repeats, and all but two of them scored
below the 0.75 reject line.** Test 18 found this once; three independent agents have now
reproduced it. The most instructive cases:

- Test 20's `2x²−12x+23` scored 0.50 against a Test 6 item and shared its **exact
  coefficients**, only the constant differing.
- Test 19's `x²+bx+45=0` scored under threshold against Test 7 and was the **same equation with
  the same constant**.
- Test 21's mixture problem scored **0.42** and was the identical 20%/50% mixture as Test 7.
- Test 21's curve-tangent-to-a-line scored **0.41** and was Test 10's item with new numbers.

Token-signature Jaccard measures vocabulary overlap. A template repeat that changes the setting
words while keeping the mathematics scores *low* precisely because it changed the words. The
threshold is therefore a **triage device**: read every match above ~0.45 and judge it.

Two practices that fell out of this and are worth keeping:

1. **Pre-screen a replacement before writing it.** Test 20 discarded six replacement ideas
   (exterior angle, trapezium area, triangle base×height, parallelogram area, square-area-to-side,
   prism volume) by checking the bank first, avoiding a second rewrite pass on each. Test 19 and
   Test 21 did the same. As the bank grows past 1,300 Math questions, the ordinary skills are
   nearly exhausted and a first draft is *more likely than not* to collide.
2. **Convergence is real and reproducible.** Test 19's first two-stage composition independently
   reproduced Test 11's `g(x)=2x−5, f(x)=x²+x` exactly. Disjoint territories plus per-agent
   reference templates keep cross-sibling overlap at 0.53, but they do not prevent an agent
   colliding with the *bank* — only reading does.

## Verifier improvements made during this build

- **`latex_to_expr` ordering is not fixable by choosing an order.** A fraction can sit inside an
  exponent (`a^{\frac{7}{12}}`) as readily as an exponent inside a fraction
  (`\frac{4a^{3}}{b^{4}}`), and either fixed order fails one of them. Alternate the two rewrites
  in a loop iterated to a fixed point.
- **Split surviving multi-letter runs into implicit products.** Without it `\frac{uv}{u+v}`
  parses as a symbol named `uv` and the key silently fails to match.
- `Abs()` needs a symbol declared `real=True` or sympy refuses to solve it.
- A float-epsilon fallback so `1.8` matches `9/5`.

## Two boundary bugs, same family as the `\bpi` bug

Both were in *checking* code and both produced false positives:

- Test 19's setting check used `\bfen`, which matched the **"fen" inside "fence"**. It now
  requires a closing boundary. `ground` was dropped as a keyword entirely — it is the earth in
  one module and the past tense of *grind* in another.
- Test 21's setting matcher flagged `must` (the modal verb) and `moth` (inside *months*).

A third was mine: a tag-balance check counting `<u` matched `<ul` and reported nine false
unbalanced-tag findings. **A boundary-free substring match in a checker is worse than no check,
because it trains you to ignore it.**

## Two defects found and fixed in the harness

- **The R&W `_ref` prefix.** Scaffolding Tests 19–21 from Test 18 replaced the Math tag
  `AUTHORED/T18-` but not the R&W tag `AUTHORED-T18:`, because the substitution keyed on the
  hyphen. All three would have stamped Test 18 provenance onto their own R&W questions. Caught by
  the Test 21 R&W agent reading the assembler it feeds. Tests 16–18 were unaffected.
- **`audit_math_rendering.mjs` degree rule.** It flagged "75 degrees Brix". Spelling out a named
  scale is correct prose — the rule exists to catch an *angle* written as "35 degrees" — so the
  whitelist was widened (Brix, Baumé, Twaddell, proof) rather than the content changed. Verified
  the rule still fires on "an angle of 35 degrees" and "turned 90 degrees".

## Known gaps

No `Explanation` rows, consistent with every test from Test 1. No images: all figures are real
`<table>` markup, so geometry items are worded to be fully determined without a picture.
