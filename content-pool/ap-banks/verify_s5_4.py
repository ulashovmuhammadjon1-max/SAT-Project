"""Verify AP Statistics 5.4 Residuals.

Descriptive topic: no probability distribution, so no critical value, p-value
or degrees of freedom appears. Every residual quoted in a stem is recomputed
here as observed - predicted from that stem's own equation, and the two claims
that are easy to assert and hard to believe -- that a least-squares fit's
residuals sum to zero, and that least squares minimizes the SUM OF SQUARES
rather than the sum -- are demonstrated numerically on the stem's own six
points with scipy.stats.linregress.

The sign convention is checked in both directions: a positive residual must
correspond to underprediction and a negative one to overprediction (CED
5.4.B.1).
"""
from scipy import stats

import s5_4
from s_verify_util import Checker

c = Checker(s5_4)


def residual(observed, predicted):
    """CED 5.4.A.1."""
    return observed - predicted


def predict(a, b, x):
    return a + b * x


# --- residuals computed straight from the definition -------------------------
c.check(1, residual(47, 52.3))
assert abs(residual(52.3, 47) - 5.3) < 1e-9, "reversing the subtraction is the sign error in q1"

c.check(3, round(residual(40, predict(14.2, 2.6, 9)), 1))
assert abs(predict(14.2, 2.6, 9) - 37.6) < 1e-9

c.check(5, 61.2 + (-4.7))

c.check(19, residual(22.0, predict(42.0, -1.25, 16)))
assert abs(predict(42.0, -1.25, 16) - 22.0) < 1e-9, "q19's point lies exactly on the line"

c.check(23, [residual(9.0, predict(3.0, 1.5, 4)), residual(15.0, predict(3.0, 1.5, 8))])

# --- residuals plus the sign's meaning ---------------------------------------
r2 = residual(88, 81.6)
assert abs(r2 - 6.4) < 1e-9 and r2 > 0
c.conceptual(2, "88 - 81.6 = 6.4, computed above. CED 5.4.B.1: a POSITIVE residual puts the "
                "observation above the line, so the model underpredicted it")

r4 = residual(110, predict(200, -3.5, 24))
assert abs(predict(200, -3.5, 24) - 116.0) < 1e-9 and abs(r4 + 6.0) < 1e-9 and r4 < 0
c.conceptual(4, "the predicted value is 200 - 3.5(24) = 116 and the residual is 110 - 116 = "
                "-6.0, both computed above; a NEGATIVE residual means the model overpredicted")

# --- the six-point least-squares fit -----------------------------------------
X = [2, 4, 6, 8, 10, 12]
Y = [5, 11, 14, 21, 24, 30]
fit = stats.linregress(X, Y)
assert abs(fit.slope - 2.443) < 5e-4 and abs(fit.intercept - 0.4) < 5e-4
resids = [residual(y, predict(fit.intercept, fit.slope, x)) for x, y in zip(X, Y)]

c.check(9, round(residual(14, predict(0.4, 2.443, 6)), 2))
assert residual(14, predict(0.4, 2.443, 6)) < 0, "the model overpredicts at x = 6"

assert abs(sum(resids)) < 1e-9, sum(resids)
c.check(10, 0)

# least squares minimizes the SUM OF SQUARES: perturbing the slope must raise it
sse = sum(r ** 2 for r in resids)
for nudge in (-0.05, 0.05):
    alt = fit.slope + nudge
    alt_int = sum(Y) / len(Y) - alt * (sum(X) / len(X))
    alt_sse = sum((y - (alt_int + alt * x)) ** 2 for x, y in zip(X, Y))
    assert alt_sse > sse, (nudge, alt_sse, sse)
c.conceptual(18, "CED 5.5.A.1: the line minimizes the sum of SQUARED residuals. Verified above "
                 "on the six-point fit -- nudging the slope by +/-0.05 raises the sum of "
                 "squares -- while the plain sum is 0 for any least-squares line and so "
                 "cannot be what is minimized")
c.conceptual(11, f"the six residuals of the fitted line sum to {sum(resids):.1e}, zero to "
                 "machine precision, whatever the quality of the fit; positives and negatives "
                 "cancel exactly, which is why the squares are what get minimized")

# --- residual magnitudes ------------------------------------------------------
FIVE = [2.1, -3.4, 0.6, -1.2, 1.9]
most_over = min(FIVE)
assert most_over == -3.4, most_over
c.conceptual(13, "overprediction is a NEGATIVE residual, and the most negative of "
                 "2.1, -3.4, 0.6, -1.2, 1.9 is -3.4, so the model missed high by 3.4 there")

trio = [(10, 16.0), (20, 25.0), (30, 32.5)]
trio_res = [round(residual(y, predict(6.5, 0.9, x)), 4) for x, y in trio]
assert trio_res == [0.5, 0.5, -1.0], trio_res
assert max(trio_res, key=abs) == -1.0
c.conceptual(15, "the predicted values are 15.5, 24.5 and 33.5, giving residuals 0.5, 0.5 and "
                 "-1.0, computed above; the largest in MAGNITUDE is the -1.0 at x = 30")

A = [3, -2, 1, -3, 1]
B = [8, -7, 2, -6, 3]
assert sum(A) == 0 and sum(B) == 0
assert sum(abs(v) for v in A) < sum(abs(v) for v in B)
assert sum(v ** 2 for v in A) < sum(v ** 2 for v in B)
c.conceptual(20, "both sets of residuals sum to 0, so the sums cannot separate the two models; "
                 "the total absolute error is 10 against 26 and the sum of squares 24 against "
                 "162, both computed above, so Model A fits better")

# --- conceptual items, with the CED rule that fixes each key -----------------
c.conceptual(6, "CED 5.4.C.1: a residual plot graphs the RESIDUALS against the predicted "
                "values or against x -- not the observed values against anything")
c.conceptual(7, "CED 5.4.C.3: apparent randomness in the residual plot confirms the linear "
                "form and indicates the simple linear model is appropriate")
c.conceptual(8, "CED 5.4.C.4: curvature in the residual plot says the linear model is not the "
                "most appropriate one, however large r may be (CED 5.2.A.3)")
c.conceptual(12, "residuals that fan out without curving leave the FORM linear while showing "
                 "that the size of the prediction errors changes across x; that is a different "
                 "defect from the wrong form")
c.conceptual(14, "the residual is the vertical distance from the point to the line, so a point "
                 "on the line has observed equal to predicted and residual exactly 0")
c.conceptual(16, "a single zero residual describes one observation; CED 5.4.C.2 makes model "
                 "appropriateness a question about the PATTERN across the whole residual plot")
c.conceptual(17, "residuals running negative, positive, negative trace a curve, and CED "
                 "5.4.C.4 reads curvature as evidence that a line is the wrong form")
c.conceptual(21, "CED 5.4.A.1: the observed value is the recorded data point and the predicted "
                 "value is read off the fitted line; only the predicted value comes from the "
                 "line")
c.conceptual(22, "a large POSITIVE residual puts the observation far above the line, so the "
                 "model underpredicted it (CED 5.4.B.1); one stray point does not condemn the "
                 "form for the rest, and deleting it is not justified by inconvenience")
c.conceptual(24, "CED 5.4.C.2: the residual plot is the tool for judging appropriateness. A "
                 "high r does not establish linearity (5.2.A.3), and the residual sum is 0 for "
                 "every least-squares fit, as computed above")
c.conceptual(25, "CED 5.4.B.1: underprediction means observed exceeds predicted, so observed "
                 "minus predicted is +12; the predicted value and the slope are not needed")

c.finish()
