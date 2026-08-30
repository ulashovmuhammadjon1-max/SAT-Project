"""Verify AP Statistics 4.7 Confidence Interval for a Difference of Two Means.

Distribution: Student's t. The CED (4.7.C.2) does not fix a single df for the
two-sample interval -- it says technology supplies it and that it lies between
the smaller of n1 - 1 and n2 - 1 and n1 + n2 - 2. Both are computed here: the
CONSERVATIVE df, min(n1, n2) - 1, which every stem that asks for a numeric
interval names explicitly, and the Welch-Satterthwaite df that technology
reports. They give different intervals, which is exactly why the stems say
which one to use.

Standard errors are sqrt(s1^2/n1 + s2^2/n2). The wrong construction behind two
distractors -- adding the two standard errors -- is computed too.
"""
import math

from scipy import stats

import s4_7
from s_verify_util import Checker

c = Checker(s4_7)
T = stats.t


def se_diff(s1, n1, s2, n2):
    return math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def add_ses(s1, n1, s2, n2):
    return s1 / math.sqrt(n1) + s2 / math.sqrt(n2)


def df_conservative(n1, n2):
    return min(n1, n2) - 1


def df_welch(s1, n1, s2, n2):
    a, b = s1 ** 2 / n1, s2 ** 2 / n2
    return (a + b) ** 2 / (a ** 2 / (n1 - 1) + b ** 2 / (n2 - 1))


def interval(diff, s1, n1, s2, n2, conf, df):
    se = se_diff(s1, n1, s2, n2)
    me = T.ppf(0.5 + conf / 2, df) * se
    return se, me, (diff - me, diff + me)


# q1, q2, q3 -- one pair of samples, three questions
SE1 = se_diff(6.2, 25, 5.4, 30)
c.check(1, round(SE1, 3))
assert abs(6.2 ** 2 / 25 + 5.4 ** 2 / 30 - 2.510) < 5e-4, "the variance distractor in q1"
assert abs(add_ses(6.2, 25, 5.4, 30) - 2.226) < 5e-4, "the add-the-SEs value used in q1/q24"

df_c = df_conservative(25, 30)
assert df_c == 24
se2, me2, ci2 = interval(4.2, 6.2, 25, 5.4, 30, 0.95, df_c)
c.check(2, [round(v, 3) for v in ci2])
# and the narrower interval technology's df would give, which is a distractor
dfw = df_welch(6.2, 25, 5.4, 30)
_, _, ci2w = interval(4.2, 6.2, 25, 5.4, 30, 0.95, dfw)
assert abs(ci2w[0] - 1.015) < 1e-3 and abs(ci2w[1] - 7.385) < 1e-3, ci2w
assert ci2w[1] - ci2w[0] < ci2[1] - ci2[0], "the conservative df must give the wider interval"

c.check(3, [round(dfw, 2), df_conservative(25, 30), 25 + 30 - 2])
assert df_conservative(25, 30) <= dfw <= 25 + 30 - 2, "CED 4.7.C.2's bracket"

# q5, q6 -- second pair of samples
SE5 = se_diff(8.1, 40, 7.4, 36)
c.check(5, round(SE5, 3))
assert abs(8.1 ** 2 / 40 + 7.4 ** 2 / 36 - 3.161) < 5e-4, "the variance distractor in q5"
assert df_conservative(40, 36) == 35
_, _, ci6 = interval(3.5, 8.1, 40, 7.4, 36, 0.90, 35)
c.check(6, [round(v, 3) for v in ci6])

# q10, q11 -- third pair, small samples, interval straddling 0
SE10 = se_diff(12, 20, 15, 18)
c.check(10, round(SE10, 3))
assert abs(12 ** 2 / 20 + 15 ** 2 / 18 - 19.700) < 5e-4, "the variance distractor in q10"
assert abs(add_ses(12, 20, 15, 18) - 6.219) < 5e-4, "the add-the-SEs distractor in q10"
assert df_conservative(20, 18) == 17
_, me11, ci11 = interval(6.0, 12, 20, 15, 18, 0.95, 17)
c.check(11, [round(v, 3) for v in ci11])
assert ci11[0] < 0 < ci11[1], "q11's interval must contain 0 for its explanation to hold"

# q12 -- interval from a stated standard error and df
me12 = T.ppf(0.995, 44) * 1.003
assert abs(T.ppf(0.995, 44) - 2.6923) < 5e-4
c.check(12, [round(-2.3 - me12, 3), round(-2.3 + me12, 3)])

# q25 -- recover the point estimate and margin of error from the endpoints
lo, hi = 2.1, 9.7
c.check(25, [round((lo + hi) / 2, 2), round((hi - lo) / 2, 2)])

# q16 -- the 10 percent condition, one sample failing and one passing
assert 55 > 0.10 * 500 and 30 <= 0.10 * 400
c.conceptual(16, "0.10 x 500 = 50 and the first sample of 55 exceeds it, so that one fails; "
                 "0.10 x 400 = 40 and the second sample of 30 is inside it. Exactly one of "
                 "the two fails, so only one option can be true")

# q15 -- the conservative df always gives the wider interval
assert T.ppf(0.975, df_c) > T.ppf(0.975, dfw)
c.conceptual(15, "the point estimate and standard error do not depend on df; t*(24) = "
                 f"{T.ppf(0.975, df_c):.4f} exceeds t*(48.04) = {T.ppf(0.975, dfw):.4f}, so "
                 "the conservative df widens the interval -- which is what makes it "
                 "conservative")

# q19 -- the more variable sample dominates even at equal n
a19, b19 = 4 ** 2 / 25, 9 ** 2 / 25
assert abs(b19 - 3.24) < 1e-9 and abs(a19 + b19 - 3.88) < 1e-9 and b19 / (a19 + b19) > 0.83
c.conceptual(19, "the squared terms are 16/25 = 0.64 and 81/25 = 3.24, summing to 3.88, so "
                 "the s = 9 sample supplies 84 percent of the squared standard error despite "
                 "the equal sample sizes")

# q20 -- doubling both sample sizes
se_before = se_diff(1, 25, 1, 25)
se_after = se_diff(1, 50, 1, 50)
assert abs(se_after / se_before - 1 / math.sqrt(2)) < 1e-12
c.conceptual(20, "both squared terms halve, so the standard error is multiplied by "
                 "1/sqrt(2) = 0.707, verified above; the critical value also falls slightly "
                 "as df grows, so the margin of error shrinks a little more than that")

# q23 -- interval from a point estimate and a margin of error
lo23, hi23 = 3.5 - 4.1, 3.5 + 4.1
assert abs(lo23 + 0.6) < 1e-9 and abs(hi23 - 7.6) < 1e-9 and lo23 < 0 < hi23
c.conceptual(23, "3.5 +/- 4.1 gives (-0.6, 7.6), computed above, and 0 lies inside it, so no "
                 "difference between the population means remains plausible")

# q24 -- adding standard errors inflates the interval
wrong24, right24 = add_ses(6.2, 25, 5.4, 30), se_diff(6.2, 25, 5.4, 30)
assert abs(wrong24 - 2.226) < 5e-4 and abs(right24 - 1.584) < 5e-4 and wrong24 > right24
c.conceptual(24, "adding standard errors gives 1.240 + 0.986 = 2.226 against the correct "
                 "1.584; a sum of positive numbers always exceeds the root of the sum of "
                 "their squares, so the student's interval comes out too wide, not too narrow")

# --- conceptual items, with the reasoning that fixes each key ----------------
c.conceptual(4, "two independent samples with two unknown population standard deviations is "
                "the two-sample t-interval; the one-sample mean-difference procedure belongs "
                "to matched pairs, and separate one-sample intervals do not estimate a "
                "difference")
c.conceptual(7, "CED 4.7.A.2: the parameter is the difference in the two POPULATION means, "
                "named with the response variable and both populations; the sample difference "
                "is the estimate")
c.conceptual(8, "CED 4.7.B.1.iii: once either sample size falls below 30, BOTH sample "
                "distributions must be free from strong skewness and outliers, so one bad "
                "sample fails the condition")
c.conceptual(9, "CED 4.7.B.1.ii states the 10 percent condition is unnecessary for a "
                "randomized experiment, because no unit was sampled without replacement from "
                "a population; the other four still matter")
c.conceptual(13, "0 lies inside (-1.4, 5.8), so equality of the two means remains plausible; "
                 "that is a failure to find a difference, not evidence that the means are "
                 "equal")
c.conceptual(14, "Var(X - Y) = Var(X) + Var(Y) for independent X and Y, so the two "
                 "variabilities compound; the formula uses s1 and s2 separately and never "
                 "assumes they are equal")
c.conceptual(17, "CED 4.7.C.1: the center of the interval is the point estimate xbar1 - "
                 "xbar2. The parameter is the unknown being estimated, and a confidence "
                 "interval uses no null hypothesis")
c.conceptual(18, "the interval estimates a difference in POPULATION means; the sample "
                 "difference is already known, the interval describes no individual worker, "
                 "and 95 percent is the method's long-run capture rate rather than a "
                 "probability for this finished interval")
c.conceptual(21, "only the two age groups involve different people, so only there are the "
                 "samples independent; before/after coffee, two days, pretest/posttest and two "
                 "scales all measure the same units twice and are matched pairs")
c.conceptual(22, "CED 4.7.B.1.iii is met when BOTH sample sizes are at least 30, and 45 and "
                 "50 both are; the shape requirement applies only when a sample falls below 30")

c.finish()
