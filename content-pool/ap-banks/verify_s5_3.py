"""Verify AP Statistics 5.3 Linear Regression Models.

Descriptive topic: no probability distribution, so no critical value, p-value
or degrees of freedom is involved anywhere. The Fall 2026 framework contains no
inference for a regression slope at all, so nothing in this module asks for a
standard error of b or a t statistic -- a deliberate consequence of the CED,
not an omission.

Every predicted value is recomputed here from the stem's own equation, the
line quoted in q6/q7 is refitted from the stem's own six points with
scipy.stats.linregress, and the interpolation/extrapolation judgements are made
by comparing the prediction's x against the fitted range rather than by eye.
"""
from scipy import stats

import s5_3
from s_verify_util import Checker

c = Checker(s5_3)


def predict(a, b, x):
    return a + b * x


def is_extrapolation(x, xmin, xmax):
    """CED 5.3.A.3/5.3.A.4: inside the fitted interval, endpoints included."""
    return not (xmin <= x <= xmax)


# --- straightforward predicted values ----------------------------------------
c.check(1, predict(12.4, 3.7, 8))
assert abs(3.7 * 8 - 29.6) < 1e-9, "the no-intercept distractor in q1"
c.check(2, predict(85.2, -1.6, 15))
assert abs(85.2 + 1.6 * 15 - 109.2) < 1e-9, "the wrong-sign distractor in q2"
c.check(3, predict(-2.5, 0.45, 20))
assert abs(0.45 * 20 - 9.0) < 1e-9, "the no-intercept distractor in q3"
c.check(12, predict(48.6, 2.15, 7))
c.check(16, predict(210, -3.4, 35))
assert abs(3.4 * 35 - 119.0) < 1e-9, "the amount-subtracted distractor in q16"
c.check(21, predict(52, 4.5, 6))

# q6, q7 -- the line is refitted from the stem's own data
X = [3, 5, 8, 10, 12, 15]
Y = [21, 26, 34, 39, 44, 51]
fit = stats.linregress(X, Y)
assert abs(fit.slope - 2.518) < 5e-4 and abs(fit.intercept - 13.594) < 5e-4
c.check(6, round(predict(13.594, 2.518, 9), 2))
assert not is_extrapolation(9, min(X), max(X)), "q6's prediction must be an interpolation"

xbar, ybar = sum(X) / len(X), sum(Y) / len(Y)
assert abs(xbar - 8.833) < 5e-4 and abs(ybar - 35.833) < 5e-4
# CED 5.5.A.1: the least-squares line passes through (xbar, ybar)
assert abs(predict(fit.intercept, fit.slope, xbar) - ybar) < 1e-9
c.check(7, round(ybar, 2))

# --- changes in the predicted value ------------------------------------------
c.check(8, 3.7 * 5)
c.check(9, -1.6 * 10)
c.check(18, predict(5.0, 1.25, 16) - predict(5.0, 1.25, 4))
assert abs(1.25 * 12 - 15.0) < 1e-9, "slope times the change in x"
c.check(24, [round(predict(18.0, 0.75, 24), 2), round(predict(18.0, 0.75, 25), 2)])
assert abs(predict(18.0, 0.75, 25) - predict(18.0, 0.75, 24) - 0.75) < 1e-12

# --- solving for x -----------------------------------------------------------
c.check(10, round((100 - 12.4) / 3.7, 2))
assert abs(100 / 3.7 - 27.03) < 5e-3, "the forgot-the-intercept distractor in q10"
c.check(23, (0 - 100) / -2.5)

# q14 -- a prediction plus an interpolation judgement
assert abs(predict(3.2, 0.85, 12) - 13.40) < 1e-9
assert not is_extrapolation(12, 1, 20)
c.conceptual(14, "3.2 + 0.85(12) = 13.40, computed above, and 12 lies inside the fitted range "
                 "1 to 20, so the prediction is an interpolation")

# q20 -- a prediction plus an extrapolation warning
assert predict(40, 12, 30) == 400 and is_extrapolation(30, 1, 10)
c.conceptual(20, "40 + 12(30) = 400 exactly, but year 30 is 20 years beyond the last year used "
                 "to fit the line, so CED 5.3.A.3's warning applies and the number must be "
                 "reported with it")

# --- interpolation versus extrapolation --------------------------------------
assert is_extrapolation(45, 5, 30) and not is_extrapolation(18, 5, 30)
c.conceptual(4, "45 lies beyond the largest fitted x of 30, so it is an extrapolation; CED "
                "5.3.A.3 says reliability falls the further out the prediction goes")
c.conceptual(5, "18 lies between 5 and 30, so it is an interpolation whether or not 18 was one "
                "of the observed x-values (CED 5.3.A.4)")

far = [(900, 500), (410, 10)]
assert all(is_extrapolation(x, 100, 400) for x, _ in far)
assert all(not is_extrapolation(x, 100, 400) for x in (250, 380, 105))
assert far[0][1] > far[1][1]
c.conceptual(15, "only 900 and 410 lie outside the range 100 to 400, and 900 is 500 units "
                 "beyond the top against 410's 10, so 900 is by far the least reliable")

assert not is_extrapolation(60, 20, 60) and is_extrapolation(65, 20, 60)
assert all(not is_extrapolation(x, 20, 60) for x in (21, 40, 55))
c.conceptual(25, "the fitted interval 20 to 60 includes its endpoints, so only x = 65 is an "
                 "extrapolation; 60, 55, 40 and 21 are all interpolations")
c.conceptual(19, "CED 5.3.A.4: the interval used to fit the line includes its endpoints, so "
                 "predicting at the largest observed x is still an interpolation")

assert is_extrapolation(0, 2, 12) and is_extrapolation(40, 2, 12)
assert (40 - 12) > (2 - 0), "age 40 is much further outside the range than age 0"
c.conceptual(11, "both age 0 and age 40 lie outside the fitted range of 2 to 12, but 40 is 28 "
                 "years past the top while 0 is only 2 years below the bottom, computed above; "
                 "CED 5.3.A.3 grades reliability by distance, not by a yes/no rule")

# --- remaining conceptual items ----------------------------------------------
c.conceptual(13, "CED 5.3.A.2 and 5.5.B.3: a is the y-intercept, the predicted response at "
                 "x = 0; the per-unit change is the slope b, and neither is the correlation")
c.conceptual(17, "a fitted line summarizes only the observed range of x; continuing it outward "
                 "assumes a pattern the data never showed, which is how a model can predict a "
                 "negative weight while fitting the data well")
c.conceptual(22, "CED 5.4.C.3: a linear model should only be fitted when the data show a "
                 "linear trend. The line yields PREDICTED values, both variables must be "
                 "quantitative, and no common units are required")

c.finish()
