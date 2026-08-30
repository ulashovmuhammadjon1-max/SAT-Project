"""Verify AP Statistics 4.8 Justifying a Claim from a Two-Sample Interval.

Distribution: Student's t with the CONSERVATIVE degrees of freedom,
min(n1, n2) - 1, which q4 names in its stem; critical values from
scipy.stats.t.ppf. Every endpoint, midpoint, width and expected count below is
computed rather than recalled, and each conceptual item records the reasoning
that fixes its key -- including, where the key turns on whether 0 is inside an
interval, an assertion that 0 really is (or is not) inside it.
"""
import math

from scipy import stats

import s4_8
from s_verify_util import Checker

c = Checker(s4_8)
T = stats.t


def se_diff(s1, n1, s2, n2):
    return math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def interval(diff, se, conf, df):
    me = T.ppf(0.5 + conf / 2, df) * se
    return me, (diff - me, diff + me)


# q4 -- two confidence levels from one pair of samples, conservative df = 29
SE = se_diff(5, 30, 6, 30)
assert abs(SE - 1.4259) < 5e-5
me95, ci95 = interval(4, SE, 0.95, 29)
me90, ci90 = interval(4, SE, 0.90, 29)
assert me90 < me95, "the lower confidence level must give the shorter interval"
c.check(4, [round(v, 3) for v in ci95] + [round(v, 3) for v in ci90])
_, ci99 = interval(4, SE, 0.99, 29)
assert abs(ci99[0] - 0.070) < 1e-3 and abs(ci99[1] - 7.930) < 1e-3, ci99

# q5 -- long-run capture rate
c.check(5, 0.95 * 200)

# q6 -- point estimate and margin of error from the endpoints
lo, hi = -8.2, -1.6
c.check(6, [round((lo + hi) / 2, 1), round((hi - lo) / 2, 1)])

# q10, q14 -- which value is (not) inside a stated interval
outside10 = [v for v in (1.5, 2.5, 4.0, 6.0, 7.5) if not 2.0 <= v <= 8.0]
assert outside10 == [1.5], outside10
c.check(10, 1.5)
inside14 = [v for v in (-1.0, -6.0, 0.0, 0.5, 1.0) if -5.0 <= v <= -0.2]
assert inside14 == [-1.0], inside14
c.check(14, -1.0)

# q16 -- reversing the order of subtraction
lo16, hi16 = 1.1, 4.9
c.check(16, [-hi16, -lo16])

# q18 -- quadrupling both sample sizes roughly halves the margin of error
mid18, me18 = (1.2 + 8.8) / 2, (8.8 - 1.2) / 2
assert abs(mid18 - 5.0) < 1e-9 and abs(me18 - 3.8) < 1e-9
# quadrupling n1 and n2 halves sqrt(s1^2/n1 + s2^2/n2) exactly; t* falls a little too
assert abs(se_diff(5, 4 * 30, 6, 4 * 30) / se_diff(5, 30, 6, 30) - 0.5) < 1e-12
c.check(18, [round(mid18 - me18 / 2, 2), round(mid18 + me18 / 2, 2)])

# q22 -- interval from a point estimate and a margin of error
lo22, hi22 = 3.1 - 2.7, 3.1 + 2.7
assert abs(lo22 - 0.4) < 1e-9 and abs(hi22 - 5.8) < 1e-9
assert not (lo22 <= 0 <= hi22), "0 must lie OUTSIDE this interval"
c.conceptual(22, "3.1 +/- 2.7 = (0.4, 5.8), computed above, and 0 < 0.4 lies outside it, so a "
                 "zero difference is not a plausible value")

# q19 -- a wider interval can straddle 0 when a narrower one does not
me90b, ci90b = interval(2.0, 1.0, 0.90, 29)
me99b, ci99b = interval(2.0, 1.0, 0.99, 29)
assert not (ci90b[0] <= 0 <= ci90b[1]) and ci99b[0] <= 0 <= ci99b[1], (ci90b, ci99b)
c.conceptual(19, "constructed above with a point estimate of 2.0 and SE 1.0 at df 29: the "
                 "90 percent interval is (0.30, 3.70) and the 99 percent interval is "
                 "(-0.76, 4.76). Same center, and only the wider one reaches past 0")

# q25, q12, q2, q20 -- intervals that contain 0
for qn, (a, b), reason in [
    (2, (-2.4, 6.1), "0 is inside (-2.4, 6.1), so equality remains plausible; failing to rule "
                     "out equality is not evidence for it"),
    (12, (-0.9, 3.7), "0 is inside (-0.9, 3.7), so a girls' advantage is as plausible as a "
                      "boys' advantage; a positive point estimate alone is not evidence"),
    (20, (-1.2, 0.4), "0 is inside (-1.2, 0.4), but so are -1.0 and 0.3; an interval that "
                      "fails to exclude 0 does not single 0 out"),
    (25, (-0.4, 5.6), "0 is inside (-0.4, 5.6), so the plausible values include both a "
                      "program 1 advantage and a small program 2 advantage"),
]:
    assert a <= 0 <= b, f"q{qn}: 0 must lie inside {(a, b)}"
    c.conceptual(qn, reason)

# q1, q3, q9, q21 -- intervals that exclude 0, and what side they fall on
for qn, (a, b), reason in [
    (1, (3.2, 11.8), "the whole interval is above 0, so every plausible value of mu1 - mu2 is "
                     "positive and region 1 has the larger mean; the midpoint is not singled "
                     "out and individual years are not described"),
    (3, (-8.2, -1.6), "the whole interval is below 0 with A minus B as the order of "
                      "subtraction, so mu_A < mu_B and A has the shorter mean recovery time"),
    (9, (1.4, 6.0), "the whole interval is above 0, and because the units were randomly "
                    "ASSIGNED the difference can be attributed to the treatment"),
    (21, (3.4, 3.6), "the interval excludes 0, so a difference is supported, and its width of "
                     "0.2 makes it a precise estimate -- which comes from large samples or "
                     "small within-sample variability, not from small ones"),
]:
    assert not (a <= 0 <= b), f"q{qn}: 0 must lie OUTSIDE {(a, b)}"
    c.conceptual(qn, reason)

# q17 -- a short interval excluding 0 from very large samples
assert not (0.02 <= 0 <= 0.06)
c.conceptual(17, "the interval (0.02, 0.06) excludes 0, so the difference is real; at n = "
                 "5,000 per group the standard error is small enough to resolve a difference "
                 "of a few hundredths of a kilogram, which need not matter in practice")

# --- remaining conceptual items ----------------------------------------------
c.conceptual(7, "a confidence interval estimates the difference in POPULATION means; the "
                "difference in sample means is already known and is the midpoint, here 3.0")
c.conceptual(8, "mu1 - mu2 is a fixed constant and the endpoints are already computed, so no "
                "probability remains; 95 percent is the method's capture rate over repeated "
                "pairs of samples")
c.conceptual(11, "the margin of error is t* sqrt(s1^2/n1 + s2^2/n2); larger samples shrink it, "
                 "while a higher confidence level and the conservative df both raise t*, and "
                 "pooling the samples estimates a different parameter")
c.conceptual(13, "width is t* sqrt(s1^2/n1 + s2^2/n2), which depends on sample sizes, sample "
                 "standard deviations and the critical value -- not on how far apart the "
                 "population means happen to be, and two intervals for one parameter need not "
                 "agree")
c.conceptual(15, "the interpretation names both populations, the response variable and the "
                 "parameter, and says 'confident' rather than 'probability'; it describes "
                 "neither individual commuters nor the sample difference")
c.conceptual(23, "with n1 = 8 and n2 = 9 both below 30, CED 4.7.B.1.iii requires both sample "
                 "distributions to be free from strong skewness and outliers; when they are "
                 "not, the interval's stated capture rate is not the one it actually has")
c.conceptual(24, "a higher confidence level raises t*, which widens the interval and raises "
                 "the long-run capture rate; the two always move together, and the capture "
                 "rate is not a statement about one particular sample")

c.finish()
