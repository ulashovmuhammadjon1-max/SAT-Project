"""Verification for AP STATISTICS 1.9, comparing distributions and z-scores.

Every z-score item is recomputed from the stem's own mu, sigma and x with a
single `z` function, and the three items that invert the formula (solve for x,
for sigma, for mu) are checked by round-tripping: the recovered value is fed
back through `z` and must reproduce the z-score the stem states. That catches a
sign error, which is the realistic mistake here and which a one-way computation
would not notice.

The two cross-distribution comparison items (q13, q15) are checked on both
halves -- the z-scores AND the direction of the conclusion -- because q15 is
deliberately built so the higher raw score has the worse relative position, and
a verifier that only checked the arithmetic would pass a key pointing the wrong
way.

Run: python3 verify_s1_9.py
"""
import statistics as st

import s_verify_util as U

import s1_9

c = U.Checker(s1_9)


def z(x, mu, sigma):
    return (x - mu) / sigma


# --- straightforward z-scores --------------------------------------------------
c.check(5, z(84, 72, 8))                # 12/8  =  1.50
c.check(6, z(58, 70, 6))                # -12/6 = -2.00
c.check(7, z(158, 170, 8))              # -12/8 = -1.50
c.check(8, z(33, 25, 4))                # 8/4   =  2.00

# --- the formula inverted, each checked by round-tripping ----------------------
x9 = 500 + 1.8 * 100                    # solve for x
assert abs(z(x9, 500, 100) - 1.8) < 1e-12, "q9: the recovered value must have z = 1.8"
c.check(9, x9)                          # 680

x10 = 250 + (-0.75) * 40                # solve for x, negative z
assert abs(z(x10, 250, 40) - (-0.75)) < 1e-12, "q10: the recovered value must have z = -0.75"
assert x10 < 250, "q10: a negative z-score must land below the mean"
c.check(10, x10)                        # 220

sigma11 = (88 - 76) / 1.5               # solve for sigma
assert abs(z(88, 76, sigma11) - 1.5) < 1e-12, "q11: the recovered sigma must give z = 1.5"
c.check(11, sigma11)                    # 8

mu12 = 45 - (-0.5) * 6                  # solve for mu
assert abs(z(45, mu12, 6) - (-0.5)) < 1e-12, "q12: the recovered mu must give z = -0.5"
assert mu12 > 45, "q12: a negative z-score means the value sits below the mean"
c.check(12, mu12)                       # 48

# --- comparisons across distributions ------------------------------------------
za, zb = z(84, 72, 8), z(78, 65, 10)
assert (round(za, 2), round(zb, 2)) == (1.50, 1.30), f"q13: z-scores are {za}, {zb}"
assert za > zb, "q13: the key says Exam A is the stronger relative performance"
assert 84 > 78, "q13: here the higher raw score also wins, unlike q15"

# q14: lower is better, so the more negative z-score is the better performance.
zd, zp = z(52, 58, 4), z(47, 51, 5)
assert (round(zd, 2), round(zp, 2)) == (-1.50, -0.80), f"q14: z-scores are {zd}, {zp}"
assert zd < zp, "q14: Devon's z-score must be the more negative one"
assert 52 > 47, (
    "q14: Devon has the SLOWER raw time and still the better relative performance -- "
    "that inversion is the point of the item")

# q15: the higher raw score carries the WORSE relative position.
z1, z2 = z(90, 85, 2), z(95, 80, 10)
assert (z1, z2) == (2.5, 1.5), f"q15: z-scores are {z1}, {z2}"
assert 95 > 90 and z2 < z1, (
    "q15: Student 2 has the higher raw score and the lower z-score -- if this ever "
    "stops being true the key is wrong, not merely the rationale")

# q22: the same deviation divided by a smaller sigma gives the larger z-score.
big_sigma, small_sigma = 20.0, 4.0
assert z(5, 0, small_sigma) > z(5, 0, big_sigma), (
    "q22: the group with the smaller standard deviation gives the larger z-score")


def standardizing_a_data_set():
    """q17, q18: what standardizing does and does not change."""
    data = [4, 7, 8, 10, 11, 13, 14, 16, 18, 21, 24, 30]
    mu, sigma = st.mean(data), st.pstdev(data)
    zs = [z(x, mu, sigma) for x in data]

    # q17: the standardized data have mean 0 and standard deviation 1.
    assert abs(st.mean(zs)) < 1e-12, f"q17: standardized mean is {st.mean(zs)}"
    assert abs(st.pstdev(zs) - 1.0) < 1e-12, f"q17: standardized sd is {st.pstdev(zs)}"

    # q18: the shape is unchanged. Standardizing is strictly increasing, so the
    # ordering of the values is preserved, and the skew direction is preserved
    # too -- both are checked, since "shape unchanged" is the claim.
    assert zs == sorted(zs), "q18: standardizing preserves the ordering of the data"
    assert (st.mean(data) > st.median(data)) == (st.mean(zs) > st.median(zs)), (
        "q18: standardizing must preserve the direction of the skew")

    # q16: z-scores are unitless. Multiplying every value by any positive
    # constant -- a change of units -- leaves every z-score identical.
    for factor in (2.54, 100.0, 0.001):
        rescaled = [factor * x for x in data]
        rmu, rsigma = st.mean(rescaled), st.pstdev(rescaled)
        rzs = [z(x, rmu, rsigma) for x in rescaled]
        assert all(abs(a - b) < 1e-9 for a, b in zip(zs, rzs)), (
            f"q16: a change of units by {factor} must not change any z-score")


standardizing_a_data_set()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 1.9.D.1: a standardized score measures the number of standard deviations a value falls above or below the mean.")
c.conceptual(2, "EK 1.9.D.2: z = (x - mu)/sigma, the deviation from the mean divided by the standard deviation.")
c.conceptual(3, "EK 1.9.D.2: the sign of z is the sign of x - mu, so a negative z-score places the value below the mean.")
c.conceptual(4, "EK 1.9.D.2: z = 0 means x - mu = 0, so the value sits at the mean; whether it is also the median depends on the shape.")
c.conceptual(13, "EK 1.9.E.1: computed above -- z is 1.50 on Exam A against 1.30 on Exam B, so the relative standing is higher on Exam A.")
c.conceptual(14, "EK 1.9.E.1: computed above -- Devon's z is -1.50 against Priya's -0.80, and with lower times better the more negative z-score wins.")
c.conceptual(15, "EK 1.9.E.1: computed above -- Student 1's z is 2.5 against Student 2's 1.5, so the lower raw score carries the better relative position.")
c.conceptual(16, "EK 1.9.D.2: verified above -- numerator and denominator carry the same units, so a change of units leaves every z-score unchanged.")
c.conceptual(17, "EK 1.9.D.2: verified above -- standardizing a data set produces mean 0 and standard deviation 1.")
c.conceptual(18, "EK 1.9.D.2: verified above -- standardizing is a strictly increasing linear transformation, so ordering and skew direction, hence shape, are preserved.")
c.conceptual(19, "EK 1.9.A.1: a back-to-back stem-and-leaf plot shares one column of stems between two groups, so it is built for two-group comparison.")
c.conceptual(20, "EK 1.9.A.1: boxplots may be used to compare centre, variability, outliers and skewness, but they do not show sample size, modality, individual values or the mean.")
c.conceptual(21, "EK 1.9.A.1 and 1.9.B.1: both distributions centre near 40, while spans of 60 against 20 make the second far more variable.")
c.conceptual(22, "EK 1.9.E.1: verified above -- the same deviation divided by the smaller standard deviation gives the larger z-score.")
c.conceptual(23, "EK 1.9.C.1: a higher median is a higher typical month and a smaller IQR is greater consistency; staffing and outliers are not addressed by either summary.")
c.conceptual(24, "EK 1.9.A.1 and 1.9.B.1: a comparison covers shape, centre, variability and unusual features, stated comparatively rather than as two separate descriptions.")
c.conceptual(25, "EK 1.9.E.1: equal z-scores mean equal relative positions within each distribution and imply nothing about the raw values or the parameters.")

c.finish()
