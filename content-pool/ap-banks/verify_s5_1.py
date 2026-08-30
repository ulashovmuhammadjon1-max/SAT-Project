"""Verify AP Statistics 5.1 Graphical Representations of Two Quantitative Variables.

This topic is descriptive and carries no probability distribution, so no
critical value, p-value or degrees of freedom appears anywhere in it. What CAN
be computed is whether each stem's own data really has the direction, form and
strength its key claims, and that is what happens below: for every data set
given in a stem, numpy's correlation and scipy.stats.linregress supply r, r^2
and the fitted slope, and the key is accepted only if those numbers agree with
the description it asserts.

Strength thresholds used, and applied consistently: |r| >= 0.9 is strong,
0.5 <= |r| < 0.9 moderate, |r| < 0.5 weak. Form is judged from the SECOND
differences of y at equally spaced x -- constant first differences mean exactly
linear, and steadily growing ones mean curved -- because a high r alone does
not establish linearity (CED 5.2.A.3).
"""
import numpy as np
from scipy import stats

import s5_1
from s_verify_util import Checker

c = Checker(s5_1)

RISING = ([1, 2, 3, 4, 5, 6, 7, 8], [3, 5, 6, 8, 9, 11, 12, 14])
FALLING = ([2, 4, 6, 8, 10, 12], [95, 88, 80, 74, 66, 59])
SQUARES = ([1, 2, 3, 4, 5, 6, 7], [1, 4, 9, 16, 25, 36, 49])
NOISY = ([1, 2, 3, 4, 5, 6, 7, 8], [6, 4, 7, 5, 8, 5, 7, 6])
ZIGZAG = ([10, 12, 14, 16, 18, 20], [22, 19, 24, 21, 26, 23])
CARS = ([1, 2, 3, 4, 5, 6], [18, 16, 15, 13, 12, 10])
EXACT = ([3, 5, 7, 9, 11], [12, 17, 22, 27, 32])


def r_of(pair):
    return float(np.corrcoef(pair[0], pair[1])[0, 1])


def strength(pair):
    a = abs(r_of(pair))
    return "strong" if a >= 0.9 else "moderate" if a >= 0.5 else "weak"


def direction(pair):
    r = r_of(pair)
    return "positive" if r > 0.05 else "negative" if r < -0.05 else "none"


def first_differences(y):
    return [y[i + 1] - y[i] for i in range(len(y) - 1)]


def is_exactly_linear(pair):
    """Equally spaced x with constant first differences in y."""
    x, y = pair
    dx = set(first_differences(x))
    dy = set(first_differences(y))
    return len(dx) == 1 and len(dy) == 1


def form(pair):
    """Linear unless the first differences trend steadily in one direction."""
    d = first_differences(pair[1])
    if len(set(d)) == 1:
        return "linear"
    second = first_differences(d)
    if all(s > 0 for s in second) or all(s < 0 for s in second):
        return "non-linear"
    return "linear"


# q3 -- positive, linear, strong
assert direction(RISING) == "positive" and strength(RISING) == "strong"
assert form(RISING) == "linear" and abs(r_of(RISING) - 0.9976) < 5e-4
c.conceptual(3, f"r = {r_of(RISING):.4f} on the stem's own eight pairs, so the direction is "
                "positive and the strength is strong; the first differences in y are "
                "2,1,2,1,2,1,2 with no drift, so the form is linear")

# q4 -- negative, linear, strong
assert direction(FALLING) == "negative" and strength(FALLING) == "strong"
assert form(FALLING) == "linear" and abs(r_of(FALLING) + 0.9996) < 5e-4
c.conceptual(4, f"r = {r_of(FALLING):.4f}: negative and strong, with y falling by 7, 8, 6, 8, "
                "7 for each step of 2 in x, so the form is linear")

# q5 -- positive, NON-linear, strong pattern
assert direction(SQUARES) == "positive" and form(SQUARES) == "non-linear"
assert first_differences(SQUARES[1]) == [3, 5, 7, 9, 11, 13]
assert abs(r_of(SQUARES) - 0.9774) < 5e-4
c.conceptual(5, "the first differences are 3, 5, 7, 9, 11, 13 -- steadily increasing -- so the "
                f"form is curved even though r = {r_of(SQUARES):.4f} is high. CED 5.2.A.3 says "
                "exactly this: a high r does not establish that a line is appropriate")

# q6, q15 -- weak / moderate with heavy scatter
assert strength(NOISY) == "weak" and abs(r_of(NOISY) - 0.2673) < 5e-4
c.conceptual(6, f"r = {r_of(NOISY):.4f}, well below 0.5, so the association is weak; the "
                "y-values move up and down as x increases with only a slight upward drift")
assert strength(ZIGZAG) == "moderate" and direction(ZIGZAG) == "positive"
assert abs(r_of(ZIGZAG) - 0.5061) < 5e-4
c.conceptual(15, f"r = {r_of(ZIGZAG):.4f} -- positive but only moderate, so a mild upward "
                 "tendency with heavy scatter; the alternation does not remove the tendency")

# q12 -- justifying a claim from the data
fit = stats.linregress(*CARS)
assert fit.slope < 0 and abs(fit.slope + 1.5429) < 5e-4 and abs(fit.rvalue) > 0.99
c.conceptual(12, f"the fitted slope is {fit.slope:.2f} thousand per year with "
                 f"r = {fit.rvalue:.4f}, so value falls nearly linearly with age; a specific "
                 "value at age 7 would be an extrapolation and is not justified")

# q21 -- exactly linear
assert is_exactly_linear(EXACT) and abs(r_of(EXACT) - 1.0) < 1e-12
assert first_differences(EXACT[1]) == [5, 5, 5, 5]
c.conceptual(21, "x rises by exactly 2 each time and y by exactly 5, so all five points lie on "
                 "one line and r = 1.0000 exactly, computed above")

# --- conceptual items, with the CED rule that fixes each key -----------------
c.conceptual(1, "CED 5.1.A.2: the explanatory variable goes on the x-axis, and here hours "
                "studied is used to predict score")
c.conceptual(2, "CED 5.1.A.1: the ordered pairs must come from the same individuals, which is "
                "what makes pairing meaningful; equal units and equal means are irrelevant, "
                "and a categorical variable rules a scatterplot out")
c.conceptual(7, "CED 5.1.B.3 defines positive direction as a TENDENCY for y to increase with "
                "x -- not constant increments, not r = 1, and certainly not causation")
c.conceptual(8, "CED 5.1.B.4: strength is how closely the points follow the pattern. Slope, "
                "number of points and distance from the origin are all separate matters")
c.conceptual(9, "CED 5.1.B.5 counts points that do not fit the general pattern as unusual "
                "features to be described; they are reported, not deleted, and they do not "
                "reverse the direction of the rest of the data")
c.conceptual(10, "CED 5.1.B.5 names clusters explicitly as an unusual feature; two groups of "
                 "points signal a third variable at work, not an error")
c.conceptual(11, "a falling pattern gives negative direction, a straight pattern gives linear "
                 "form, and tight points give strength; a tightly followed CURVE is non-linear "
                 "however tight it is")
c.conceptual(13, "an upward pattern is positive, and substantial scatter rules out strong and "
                 "perfect; nothing about it is negative or directionless")
c.conceptual(14, "direction and strength are properties of the pairs and survive swapping the "
                 "axes, but which variable is explanatory -- and hence which least-squares "
                 "line is fitted -- does not")
c.conceptual(16, "form, direction, strength and unusual features are all readable from the "
                 "plot; causation is not, because an observational pattern can be produced by "
                 "a lurking variable")
c.conceptual(17, "months of high overall demand may bring both heavier advertising and higher "
                 "sales, so the pattern is consistent with a lurking variable; only assigning "
                 "spending levels at random would separate the two")
c.conceptual(18, "the response variable is the one being explained or predicted, so height is "
                 "the response and age the explanatory variable; units and measurement order "
                 "do not assign the roles")
c.conceptual(19, "CED 5.1.B.2 defines form as linear or non-linear. Rising or falling is "
                 "direction, tightness is strength, and stray points are unusual features")
c.conceptual(20, "slope and strength are independent: a steep pattern with wide scatter is "
                 "weak, and a shallow pattern with tight points is strong")
c.conceptual(22, "each axis needs a numerical scale for a point to be located on it; "
                 "categorical pairs are displayed with two-way tables and segmented bar charts")
c.conceptual(23, "a single straight line cannot follow a pattern whose rate of change shifts "
                 "partway through, so the form is non-linear; the direction stays positive")
c.conceptual(24, "CED 5.1.B.1 asks for form, direction, strength AND unusual features "
                 "together, so the stray point is reported alongside the strong linear "
                 "description rather than redefining it or being discarded")
c.conceptual(25, "with neither a direction nor a curve there is nothing for form or strength "
                 "to describe; a horizontal band means y does not tend to change with x")

c.finish()
