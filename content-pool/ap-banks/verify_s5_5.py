"""Verify AP Statistics 5.5 Least-Squares Regression.

Descriptive topic: there is no probability distribution here, so no critical
value, p-value or degrees of freedom appears anywhere in this module. The
Fall 2026 framework removed inference for a regression slope from the course
entirely, which is why the two computer-output items ask only for the
coefficients and never for a standard error of b, a t statistic or df = n - 2.

Every coefficient, prediction and r^2 below is recomputed with numpy and
scipy.stats.linregress from the stem's own numbers. Three structural facts the
stems rely on are demonstrated rather than asserted: the least-squares line
passes through (xbar, ybar); it minimizes the sum of SQUARED residuals; and
b = r(s_y/s_x) reproduces the slope technology reports.
"""
import numpy as np
from scipy import stats

import s5_5
from s_verify_util import Checker

c = Checker(s5_5)

X = [4, 7, 9, 12, 15, 18, 20]
Y = [31, 38, 43, 50, 58, 64, 69]
fit = stats.linregress(X, Y)
xbar, ybar = float(np.mean(X)), float(np.mean(Y))
sx, sy = float(np.std(X, ddof=1)), float(np.std(Y, ddof=1))

# The line passes through the point of averages (CED 5.5.A.1).
assert abs(fit.intercept + fit.slope * xbar - ybar) < 1e-9

# b = r(s_y/s_x) reproduces what linregress reports.
assert abs(fit.rvalue * sy / sx - fit.slope) < 1e-9

# Least squares really does minimize the SUM OF SQUARES, not the sum.
resid = [y - (fit.intercept + fit.slope * x) for x, y in zip(X, Y)]
assert abs(sum(resid)) < 1e-9, "the plain sum is 0 for any least-squares line"
sse = sum(r ** 2 for r in resid)
for nudge in (-0.1, 0.1):
    alt_b = fit.slope + nudge
    alt_a = ybar - alt_b * xbar
    assert sum((y - (alt_a + alt_b * x)) ** 2 for x, y in zip(X, Y)) > sse, nudge

# q3 -- intercept from the slope and the two means
c.check(3, 68 - 2.4 * 15)
assert abs(2.4 * 15 - 36.0) < 1e-9, "the b*xbar distractor in q3"

# q8, q9 -- the seven-point fit
assert abs(fit.slope - 2.381) < 5e-4 and abs(xbar - 12.143) < 5e-4 and abs(ybar - 50.429) < 5e-4
c.check(8, round(ybar - 2.381 * xbar, 2))
assert abs(fit.rvalue - 0.9997) < 5e-5
r2 = round(fit.rvalue ** 2, 4)
assert abs(r2 - 0.9993) < 5e-5, r2
key9 = s5_5.QUESTIONS[8]["choices"][s5_5.QUESTIONS[8]["ans"]]
assert key9.startswith("0.9993;") and "variation" in key9, key9
c.conceptual(9, f"r^2 = {fit.rvalue:.4f}^2 = {r2}, computed above, and CED 5.5.A.5 makes it the "
                "proportion of VARIATION in the response explained by the linear relationship "
                "-- not the share of points lying on the line")

# q10, q20 -- r to r^2 and back
c.check(10, round(0.88 ** 2, 4))
assert abs(0.88 ** 0.5 - 0.9381) < 5e-5, "the square-root distractor in q10"
assert abs(1 - 0.88 ** 2 - 0.2256) < 5e-5, "the unexplained-proportion distractor in q10"
assert abs(0.36 ** 0.5 - 0.6) < 1e-12 and abs(0.36 ** 2 - 0.1296) < 1e-12
c.conceptual(20, "sqrt(0.36) = 0.6 exactly, computed above, so |r| = 0.6; squaring discards "
                 "the sign, so only the direction of the association -- the sign of the slope "
                 "-- can restore it, and r could equally be -0.6")

# q12 -- prediction from the computer output's coefficients
c.check(12, 12.85 + 3.42 * 6)
assert abs(3.42 * 6 - 20.52) < 1e-9, "the no-intercept distractor in q12"

# q14 -- b = r(s_y/s_x) on the stem's own numbers
b14 = -0.6 * (8 / 5)
assert abs(b14 + 0.96) < 1e-9 and b14 < 0
c.check(14, round(b14, 2))
assert abs(-0.6 * (5 / 8) + 0.375) < 1e-9, "the inverted-ratio distractor in q14"

# q15 -- sign of the slope and r^2 together
assert 0.75 > 0 and abs(0.75 ** 2 - 0.5625) < 1e-12
c.conceptual(15, "r = 0.75 > 0, and b = r(s_y/s_x) with both standard deviations positive, so "
                 "the slope is positive; r^2 = 0.5625, computed above, is about 56 percent. "
                 "The slope equals r only if s_y happens to equal s_x")

# q17 -- prediction plus an interpolation judgement
pred17 = 25.6 + 2.15 * 14
assert abs(pred17 - 55.70) < 1e-9 and 1 <= 14 <= 20
c.conceptual(17, "25.6 + 2.15(14) = 55.70, computed above, and 14 lies inside the fitted range "
                 "of 1 to 20, so the prediction is an interpolation (CED 5.3.A.4)")

# q22 -- the unit conversion the stem hides
pred22 = 48.2 - 6.4 * 3.5
assert abs(pred22 - 25.80) < 1e-9
assert abs(48.2 - 6.4 * 3500 + 22351.8) < 1e-6, "the unconverted-units distractor in q22"
c.check(22, round(pred22, 2))

# q24 -- comparing two r^2 values
assert 0.81 > 0.49
c.conceptual(24, "CED 5.5.A.5 makes r^2 the proportion of variation explained, so 0.81 against "
                 "0.49 compares explained variation only; it says nothing about the two slopes, "
                 "about the sign of the second correlation, or about any single residual")

# --- conceptual items, with the CED rule that fixes each key -----------------
c.conceptual(1, "CED 5.5.A.1: the fit minimizes the sum of the SQUARES of the residuals, "
                "demonstrated above by nudging the slope and watching the sum of squares rise; "
                "the plain sum of residuals is 0 for any least-squares line")
c.conceptual(2, "CED 5.5.A.1: the line passes through (xbar, ybar), verified above to 1e-9 on "
                "the seven-point fit")
c.conceptual(4, "CED 5.5.B.2: the slope is the PREDICTED change in the response per one-unit "
                "increase in x, in context. The reversed reading swaps the roles of the "
                "variables, and observational regression supports no causal claim")
c.conceptual(5, "CED 5.5.B.3: the intercept is the PREDICTED response at x = 0, in context; it "
                "promises nothing exact about any individual home")
c.conceptual(6, "the slope is negative, so the interpretation must say the predicted time "
                "DECREASES by 1.8 minutes per extra kilometer per week; and the study is "
                "observational, so 'causes' is not supported")
c.conceptual(7, "CED 5.5.B.3 names both failure modes and this stem triggers both: x = 0 is "
                "far outside the fitted range of 20 to 45 cm, and a predicted weight of -180 "
                "grams is impossible for the response variable")
c.conceptual(11, "in computer regression output the Constant row is the y-intercept and the "
                 "row named for the explanatory variable is its slope, so the equation is "
                 "yhat = 12.85 + 3.42x")
c.conceptual(13, "the coefficient on the explanatory variable is the slope, so it reports a "
                 "predicted DECREASE of 2.75 units of fuel per additional degree; a statement "
                 "about temperature 0 would use the Constant row, and the data are "
                 "observational so 'causes' is unsupported")
c.conceptual(16, "rounding the reported equation changes nothing about the fit. Adding or "
                 "removing an observation changes the data, changing the response's units "
                 "rescales the slope, and swapping the roles fits a different line entirely")
c.conceptual(18, "CED 5.5.B.2 phrases the slope as a PREDICTED change because the line "
                 "summarizes an average relationship; individual observations sit off it by "
                 "their residuals")
c.conceptual(19, "regression on observational data describes how the predicted response varies "
                 "with x; ruling out lurking variables would require random assignment, so the "
                 "causal wording overstates the model")
c.conceptual(21, "r is unit-free (CED 5.2.A.1) and so survives the conversion, but the slope "
                 "is measured in response units per explanatory unit, so predicted growth per "
                 "MONTH is one twelfth of predicted growth per year")
c.conceptual(23, "squaring discards the sign and maps every r into [0, 1]. For |r| < 1 the "
                 "square is SMALLER than |r|, r^2 is not a slope, and it counts explained "
                 "variation rather than points on the line")
c.conceptual(25, "least squares weights a large residual heavily, so removing that observation "
                 "moves both coefficients and usually raises r^2; the point of averages itself "
                 "moves, because dropping a point changes both sample means")

c.finish()
