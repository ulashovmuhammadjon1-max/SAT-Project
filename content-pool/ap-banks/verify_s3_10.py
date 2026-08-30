"""Verification for AP STATISTICS 3.10, the two-sample z-interval for a difference.

`two_sample_interval` builds the interval from the raw counts, returning the two
sample proportions, the difference, the unpooled standard error, the critical
value, the margin of error and both endpoints, and asserts the structural
properties every interval must have (centred on the difference, half-width equal
to the margin of error).

Two checks are specific to this topic.

`unpooled_is_not_pooled` computes BOTH standard errors for the same data and
records how close they are. They differ by about 0.0002 here, which is why the
module does NOT offer the pooled value as a numeric distractor -- an item whose
key and distractor round to nearly the same figure would let the wrong method
reach the right choice. The distinction is tested conceptually instead, in q3
and q4, and this check pins the numbers that justify that decision.

`contains_zero_drives_the_conclusion` evaluates "does the interval contain 0"
for each of the three worked intervals and asserts the verdict its key states.
The third interval is deliberately built to contain 0, and the check confirms
it does; if that ever stopped being true, q13's key would become wrong and
nothing else in the module would notice.

Run: python3 verify_s3_10.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_10

c = U.Checker(s3_10)


def two_sample_interval(x1, n1, x2, n2, confidence):
    p1, p2 = x1 / n1, x2 / n2
    diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    z = float(norm.ppf(1 - (1 - confidence) / 2))
    me = z * se
    low, high = diff - me, diff + me
    assert abs((low + high) / 2 - diff) < 1e-12, "the interval must centre on the difference"
    assert abs((high - low) / 2 - me) < 1e-12, "half the width is the margin of error"
    return p1, p2, diff, se, z, me, (low, high)


def pooled_se(x1, n1, x2, n2):
    """The TEST's standard error -- not used by an interval."""
    pc = (x1 + x2) / (n1 + n2)
    return math.sqrt(pc * (1 - pc) * (1 / n1 + 1 / n2))


# --- study 1: 120 of 300 against 90 of 300, 95% -------------------------------------
p1, p2, d1, se1, _, me1, ci1 = two_sample_interval(120, 300, 90, 300, 0.95)
assert (p1, p2) == (0.40, 0.30)
c.check(5, d1)                                   # 0.10
c.check(6, se1, tol=0.0005)                      # 0.0387
c.check(7, list(ci1), tol=0.002)                 # (0.0241, 0.1759)

# --- study 2: 168 of 240 against 144 of 240, 90% ------------------------------------
p1b, p2b, d2, se2, _, me2, ci2 = two_sample_interval(168, 240, 144, 240, 0.90)
assert abs(p1b - 0.70) < 1e-12 and abs(p2b - 0.60) < 1e-12
c.check(9, se2, tol=0.0005)                      # 0.0433
c.check(10, list(ci2), tol=0.002)                # (0.0288, 0.1712)

# --- study 3: 90 of 200 against 70 of 200, 99% --------------------------------------
p1c, p2c, d3, se3, _, me3, ci3 = two_sample_interval(90, 200, 70, 200, 0.99)
assert abs(p1c - 0.45) < 1e-12 and abs(p2c - 0.35) < 1e-12
c.check(11, se3, tol=0.0005)                     # 0.0487
c.check(12, list(ci3), tol=0.002)                # (-0.0255, 0.2255)


def unpooled_is_not_pooled():
    """q3, q4, q6: the interval's standard error is not the test's."""
    for x1, n1, x2, n2 in ((120, 300, 90, 300), (168, 240, 144, 240),
                           (90, 200, 70, 200), (45, 150, 30, 150)):
        p1_, p2_ = x1 / n1, x2 / n2
        unpooled = math.sqrt(p1_ * (1 - p1_) / n1 + p2_ * (1 - p2_) / n2)
        pooled = pooled_se(x1, n1, x2, n2)
        assert abs(unpooled - pooled) > 1e-9, (
            "the two standard errors must be genuinely different quantities")
        assert abs(unpooled - pooled) < 0.01, (
            "and close enough that the pooled value is a plausible distractor")

    # The specific pair quoted in q6.
    p1_, p2_ = 0.40, 0.30
    unpooled = math.sqrt(p1_ * 0.6 / 300 + p2_ * 0.7 / 300)
    pooled = pooled_se(120, 300, 90, 300)
    assert abs(unpooled - 0.0387) < 0.0002 and abs(pooled - 0.0389) < 0.0002, (
        f"unpooled {unpooled:.5f}, pooled {pooled:.5f}")


def contains_zero_drives_the_conclusion():
    """q8, q13, q14, q15: what an interval containing 0 does and does not say."""
    def contains_zero(interval):
        return interval[0] <= 0 <= interval[1]

    assert not contains_zero(ci1), "q8: study 1's interval must exclude 0"
    assert all(v > 0 for v in ci1), "and lie entirely above it, so p1 is the larger"

    assert not contains_zero(ci2), "study 2's interval also excludes 0"

    assert contains_zero(ci3), (
        "q13: study 3's interval must CONTAIN 0, or the item has no contrast to draw")
    assert ci3[0] < 0 < ci3[1]

    # q15: a wholly negative interval would place p2 above p1. Constructed here
    # by reversing the order of subtraction on study 1, which q22 also describes.
    reversed_ci = (-ci1[1], -ci1[0])
    assert all(v < 0 for v in reversed_ci), "reversing the order gives a wholly negative interval"
    assert not contains_zero(reversed_ci), "and it still excludes 0, so the conclusion is unchanged"
    assert abs((reversed_ci[1] - reversed_ci[0]) - (ci1[1] - ci1[0])) < 1e-12, (
        "q22: the width is unchanged by the order of subtraction")


def observed_counts_and_width():
    """q18, q19, q20, q21, q25."""
    # q18: the four OBSERVED counts for study 1.
    counts = (120, 300 - 120, 90, 300 - 90)
    assert counts == (120, 180, 90, 210), f"counts are {counts}"
    assert all(v >= 10 for v in counts)

    # q19: a higher confidence level widens.
    _, _, _, se, _, me_low, ci_low = two_sample_interval(120, 300, 90, 300, 0.90)
    _, _, _, se_hi, _, me_hi, ci_hi = two_sample_interval(120, 300, 90, 300, 0.99)
    assert abs(se - se_hi) < 1e-15, "the standard error does not depend on the confidence level"
    assert me_hi > me_low and (ci_hi[1] - ci_hi[0]) > (ci_low[1] - ci_low[0])

    # q20 and q25: larger samples narrow it.
    _, _, _, _, _, _, small = two_sample_interval(120, 300, 90, 300, 0.95)
    _, _, _, _, _, _, big = two_sample_interval(480, 1200, 360, 1200, 0.95)
    assert (big[1] - big[0]) < (small[1] - small[0]), "four times the data halves the width"
    assert abs((big[1] - big[0]) - (small[1] - small[0]) / 2) < 1e-9

    # q25: with a real difference, larger samples eventually exclude 0.
    _, _, _, _, _, _, wide = two_sample_interval(90, 200, 70, 200, 0.99)
    _, _, _, _, _, _, narrow = two_sample_interval(360, 800, 280, 800, 0.99)
    assert wide[0] <= 0 <= wide[1], "the small-sample interval contains 0"
    assert not (narrow[0] <= 0 <= narrow[1]), "the large-sample interval does not"

    # q21: recovering the centre and margin of error from endpoints.
    low, high = 0.02, 0.18
    centre, me = (low + high) / 2, (high - low) / 2
    assert abs(centre - 0.10) < 1e-12 and abs(me - 0.08) < 1e-12
    c.check(21, [centre, me])


unpooled_is_not_pooled()
contains_zero_drives_the_conclusion()
observed_counts_and_width()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Estimating a difference of two proportions with an interval calls for the two-sample z-interval.")
c.conceptual(2, "The interval is built around the difference of the two sample proportions, which estimates the difference of the parameters.")
c.conceptual(3, "Verified above -- an interval uses each sample's own proportion, adding the two variances, rather than a pooled estimate.")
c.conceptual(4, "Verified above -- a test assumes equal proportions under its null and so pools; an interval assumes nothing and keeps the samples apart.")
c.conceptual(8, "Computed above -- study 1's interval excludes 0 and lies entirely above it, so p1 is convincingly the larger.")
c.conceptual(13, "Computed above -- study 3's interval contains 0, so 'no difference' remains plausible and equality is not established.")
c.conceptual(14, "Computed above -- 0 is the value 'no difference', and an interval containing it has merely failed to rule it out.")
c.conceptual(15, "Computed above -- a wholly negative interval for p1 minus p2 places every plausible value where p2 exceeds p1.")
c.conceptual(16, "The counts are checked in each sample separately, and independence between the samples is what licenses adding the variances.")
c.conceptual(17, "An interval has no hypothesized value, so the normality condition uses the observed counts, as in the one-sample interval of topic 3.3.")
c.conceptual(18, "Computed above -- the four observed counts for study 1 are 120, 180, 90 and 210, all above 10.")
c.conceptual(19, "Computed above -- a larger critical value multiplies an unchanged standard error, so the interval widens.")
c.conceptual(20, "Computed above -- each variance carries its own sample size, so raising both narrows the interval.")
c.conceptual(22, "Computed above -- reversing the order negates both endpoints and leaves the width, and so the conclusion, unchanged.")
c.conceptual(23, "The interpretation names the confidence level, the interval, and the parameter, which is the difference between the two population proportions.")
c.conceptual(24, "Independence between the samples is what licenses adding the variances, and before-and-after measurements on the same people violate it.")
c.conceptual(25, "Computed above -- larger samples narrowed an interval containing 0 into one excluding it, while a higher confidence level would have widened it.")

c.finish()
