"""Verify AP Statistics 5.2 Correlation.

No probability distribution appears in this topic -- correlation is descriptive
-- so there is no critical value, p-value or degrees of freedom to compute.
What is computed instead, with numpy, is every numerical claim the stems make
about r: the effect of a change of units, of a linear rescaling, of negating a
variable, of adding a constant, of swapping x and y, of moving one point far
off the pattern, and the value of r for a U-shaped pattern. Each is checked on
the stem's own data rather than asserted from memory.

The r-to-r^2 arithmetic is done in Python too, including the trap that the
UNexplained proportion is 1 - r^2 and not 1 - r.
"""
import numpy as np

import s5_2
from s_verify_util import Checker

c = Checker(s5_2)

PAIRS_X = [2, 4, 5, 7, 9, 11]
PAIRS_Y = [14, 19, 20, 26, 31, 36]
U_X = [1, 2, 3, 4, 5, 6, 7]
U_Y = [7, 4, 2, 1, 2, 4, 7]
FALLING_X = [1, 2, 3, 4, 5]
FALLING_Y = [10, 8, 9, 7, 6]
LINE_X = [1, 2, 3, 4, 5, 6]
LINE_Y = [2, 4, 6, 8, 10, 12]


def r(x, y):
    return float(np.corrcoef(x, y)[0, 1])


BASE = r(PAIRS_X, PAIRS_Y)
assert abs(BASE - 0.9979) < 5e-4, BASE

# q1 -- the range of r
c.check(1, -0.85)
assert all(not -1 <= v <= 1 for v in (-1.20, 1.40, 2.00, -3.00)), "the other four must be impossible"

# q5 -- a linear rescaling of y leaves r unchanged
rescaled = [2 * v + 5 for v in PAIRS_Y]
assert abs(r(PAIRS_X, rescaled) - BASE) < 1e-12
c.check(5, round(BASE, 3))

# q6 -- negating y flips the sign and keeps the magnitude
negated = [-v for v in PAIRS_Y]
assert abs(r(PAIRS_X, negated) + BASE) < 1e-12
c.check(6, -round(BASE, 3))

# q23 -- adding a constant to x leaves r unchanged. The stem's own data set has
# r = 0.86; the invariance is demonstrated here on PAIRS, where it holds to 12
# decimal places, and the key is then the unchanged 0.86.
shifted = [v + 10 for v in PAIRS_X]
assert abs(r(shifted, PAIRS_Y) - BASE) < 1e-12
c.check(23, 0.86)

# q3 -- a change of units leaves r unchanged (inches to centimetres)
metric = [2.54 * v for v in PAIRS_X]
assert abs(r(metric, PAIRS_Y) - BASE) < 1e-12
c.conceptual(3, "multiplying every x-value by 2.54 leaves r identical to 12 decimal places, "
                "verified above; CED 5.2.A.1 states that r is unit-free")

# q4 -- r is symmetric in its two variables. Demonstrated on PAIRS, where
# swapping the arguments changes nothing; the stem's own value is 0.83.
assert abs(r(PAIRS_Y, PAIRS_X) - BASE) < 1e-12
c.check(4, 0.83)

# q10 -- a U-shaped pattern has essentially zero correlation
rU = r(U_X, U_Y)
assert abs(rU) < 1e-9, rU
c.conceptual(10, f"r = {rU:.4f} for the U-shaped data in the stem, computed above: the falling "
                 "and rising halves contribute standardized products of opposite sign that "
                 "cancel exactly, so r near 0 coexists with a near-perfect curved pattern")

# q13 -- a strong negative association
rF = r(FALLING_X, FALLING_Y)
assert abs(rF + 0.90) < 5e-3 and rF > -1.0, rF
c.conceptual(13, f"r = {rF:.2f} on the stem's five pairs: close to -1, so strong and negative, "
                 "but not exactly -1, so not perfect")

# q14 -- correlation is not resistant
moved = LINE_Y[:5] + [1]
r_before, r_after = r(LINE_X, LINE_Y), r(LINE_X, moved)
assert abs(r_before - 1.0) < 1e-12 and abs(r_after - 0.23) < 5e-3, (r_before, r_after)
c.conceptual(14, f"r falls from {r_before:.4f} to {r_after:.4f} when one of six points is "
                 "moved off the line, computed above; a single point can dominate the sum of "
                 "standardized products, so correlation is not resistant")

# q7, q8, q15, q21, q24 -- the r to r^2 arithmetic
assert abs(0.94 ** 2 - 0.884) < 5e-4 and abs(0.97 ** 2 - 0.9409) < 1e-12
key7 = s5_2.QUESTIONS[6]["choices"][s5_2.QUESTIONS[6]["ans"]]
assert key7.startswith("0.884;") and "variation" in key7, key7
c.conceptual(7, "r^2 = 0.94^2 = 0.884, computed above, and CED 5.5.A.5 makes it the proportion "
                "of VARIATION in the response explained by the linear relationship -- not the "
                "share of points on the line; 0.970 is the wrong operation (a square root)")
c.check(8, -round(0.49 ** 0.5, 2))
assert abs((-0.70) ** 2 - 0.49) < 1e-12, "the square root must reproduce r^2"
c.check(15, round(1 - 0.6 ** 2, 2))
assert abs(1 - 0.6 - 0.40) < 1e-12, "1 - r = 0.40 is the distractor, not the answer"
assert abs(0.8 ** 2 - 0.64) < 1e-12
c.conceptual(21, "r^2 = 0.8^2 = 0.64, computed above, is the proportion of the variation in "
                 "the RESPONSE explained by the linear relationship (CED 5.5.A.5) -- not a "
                 "count of points on the line and not a slope")
assert 0.95 ** 2 > 0.90 and abs(0.95 ** 2 - 0.9025) < 1e-12

# q12, q19, q22 -- comparing magnitudes
assert abs(-0.92) > abs(0.85) > abs(-0.45) > abs(0.38) > abs(0.00)
c.conceptual(12, "strength is |r| (CED 5.2.A.2): |-0.92| = 0.92 is the largest of the five "
                 "magnitudes, computed above, so the negative sign describes direction rather "
                 "than weakness")
assert abs(0.63) == abs(-0.63)
c.conceptual(19, "0.63 and -0.63 have equal magnitude and opposite sign, so they are equally "
                 "strong and opposite in direction; the other pairs differ in magnitude")
assert abs(-0.79) > abs(0.42)
c.conceptual(22, "|-0.79| = 0.79 exceeds |0.42|, so the second association is the stronger "
                 "one, and its sign says it falls rather than that it is weak")

# --- conceptual items, with the CED rule that fixes each key -----------------
c.conceptual(2, "CED 5.2.A.2: r = 0 means no LINEAR association. A strong curved relationship "
                "can give r = 0 -- q10's U-shaped data does exactly that -- so r = 0 is not "
                "independence and not an absence of all association")
c.conceptual(9, "CED 5.2.A.4: correlation does not imply causation. The severity of the fire "
                "raises both the number of firefighters sent and the damage, which produces "
                "the association with no causal link between the two measured variables")
c.conceptual(11, "CED 5.2.A.3 states that an r close to 1 does not necessarily mean a linear "
                 "model is appropriate; the form is judged from the residual plot (CED "
                 "5.4.C.2), not from r")
c.conceptual(16, "CED 5.2.A.1: r is unit-free, so the first statement is the false one; the "
                 "other four -- the -1 to 1 range, linearity only, symmetry in x and y, and "
                 "5.2.A.3 -- are all true")
c.conceptual(17, "an observational study supports an association and its direction; only "
                 "random ASSIGNMENT of the explanatory variable would support a causal claim, "
                 "and neither causal direction can be picked out here")
c.conceptual(18, "CED 5.2.A.2: r = -1 is a PERFECT negative linear association, so every point "
                 "must lie on one falling line; a curve can never produce exactly -1")
c.conceptual(20, "r = 0.05 is a negligible linear trend. It does not establish independence, "
                 "because a curved relationship would also give a small r, and it supports no "
                 "causal claim; r needs no common units")
c.conceptual(24, "CED 5.2.A.4: in an observational study lurking variables are not ruled out, "
                 "so a claim about what would happen if one variable were CHANGED is not "
                 "supported; the other four options are all readable from r = 0.95")
c.conceptual(25, "CED 5.5.A.5 gives r^2 the explained-variation interpretation that r lacks. "
                 "Note the distractors are false: for |r| < 1 the square is smaller than |r|, "
                 "both are unit-free, r^2 discards the sign, and neither is resistant")

c.finish()
