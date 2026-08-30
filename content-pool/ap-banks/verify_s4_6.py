"""Verify AP Statistics 4.6 Sampling Distributions for a Difference of Means.

Distribution: for two INDEPENDENT samples the difference x1bar - x2bar has mean
mu1 - mu2 and standard deviation sqrt(sigma1^2/n1 + sigma2^2/n2) (CED 4.6.A.1).
It is modeled as normal when both populations are normal (any n) or both
n >= 30, so every probability below is scipy.stats.norm -- no t and no degrees
of freedom, because the population standard deviations are given rather than
estimated. Topic 4.7 is where sigma becomes unknown and t appears.

The two wrong constructions the distractors are built from -- adding the two
standard errors, and taking sqrt(s/n) without squaring -- are computed here as
well, so each is confirmed to differ from the key.
"""
import math

from scipy import stats

import s4_6
from s_verify_util import Checker

c = Checker(s4_6)
Z = stats.norm


def sd_diff(s1, n1, s2, n2):
    """CED 4.6.A.1: variances add, standard deviations do not."""
    return math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def add_ses(s1, n1, s2, n2):
    """The classic wrong version: adding the two standard errors."""
    return s1 / math.sqrt(n1) + s2 / math.sqrt(n2)


def ten_percent_ok(n, N):
    return n <= 0.10 * N


# q1 -- the standard deviation of the difference, and both wrong versions
sd1 = sd_diff(6, 40, 8, 50)
c.check(1, round(sd1, 3))
assert abs(add_ses(6, 40, 8, 50) - 2.080) < 5e-4, "the add-the-SEs distractor in q1"
assert abs(math.sqrt(6 / 40 + 8 / 50) - 0.557) < 5e-4, "the unsquared distractor in q1"
assert abs(6 ** 2 / 40 + 8 ** 2 / 50 - 2.180) < 5e-4, "the variance distractor in q1"

# q2 -- the mean of the difference
c.check(2, 72 - 68)

# q3 -- upper-tail probability for the difference
c.check(3, round(Z.sf((6 - 4) / sd1), 4))

# q5, q7, q11, q18 -- more standard deviations and a variance
c.check(5, round(sd_diff(12, 36, 15, 25), 3))
assert abs(12 ** 2 / 36 + 15 ** 2 / 25 - 13.0) < 1e-12, "the variance distractor in q5"
c.check(7, round(sd_diff(2.5, 30, 3.1, 45), 3))
assert abs(add_ses(2.5, 30, 3.1, 45) - 0.919) < 5e-4, "the add-the-SEs distractor in q7"
assert abs(2.5 ** 2 / 30 + 3.1 ** 2 / 45 - 0.422) < 5e-4, "the variance distractor in q7"
c.check(11, round(sd_diff(10, 25, 10, 100), 3))
c.check(18, 20 ** 2 / 100 + 20 ** 2 / 100)
assert abs(math.sqrt(8) - 2.828) < 5e-4, "the SD-not-variance distractor in q18"

# q8 -- lower-tail probability
sd8 = sd_diff(4, 50, 5, 60)
c.check(8, round(Z.cdf((0 - 1.5) / sd8), 4))

# q12 -- two-tailed probability with equal population means
sd12 = sd_diff(9, 45, 7, 40)
c.check(12, round(2 * Z.sf(3 / sd12), 4))

# q6, q19 -- the 10 percent condition applied to EACH population separately
assert not ten_percent_ok(80, 600) and ten_percent_ok(50, 900)
c.conceptual(6, "0.10 x 600 = 60 and the village sample is 80, so that sample fails; "
                "0.10 x 900 = 90 and the town sample of 50 is well inside it. The condition "
                "is applied to each population on its own, not to the combined data")
assert not ten_percent_ok(120, 900) and ten_percent_ok(150, 20000)
c.conceptual(19, "0.10 x 900 = 90 and the employee sample of 120 exceeds it, so that one "
                 "fails; 150 <= 0.10 x 20,000 = 2,000, so the customer sample is fine")

# q14 -- where the variability actually comes from
v_small, v_large = 10 ** 2 / 20, 10 ** 2 / 200
assert v_small == 5.0 and v_large == 0.5 and v_small > 9 * v_large
c.conceptual(14, "the two variance terms are 100/20 = 5.0 and 100/200 = 0.5, computed above, "
                 "so the sample of 20 supplies ten elevenths of the variance and is where "
                 "extra observations do the most good")

# q20 -- unequal sigmas dominate even at equal sample sizes
t_small, t_large = 5 ** 2 / 30, 12 ** 2 / 30
total = t_small + t_large
assert abs(t_large - 4.8) < 1e-9 and abs(total - 5.6333) < 5e-4
assert t_large / total > 0.85
c.conceptual(20, "with equal n the variance terms are 25/30 = 0.833 and 144/30 = 4.8, summing "
                 "to 5.633, so the sigma = 12 population supplies 85 percent of the total; "
                 "equal sample sizes do not make equal contributions")

# q21 -- doubling both sample sizes
before = sd_diff(1, 10, 1, 10)
after = sd_diff(1, 20, 1, 20)
assert abs(after / before - 1 / math.sqrt(2)) < 1e-12
c.conceptual(21, "halving both variance terms halves the total variance, so the standard "
                 "deviation is multiplied by 1/sqrt(2) = 0.707 -- verified above on a concrete "
                 "pair of sample sizes")

# q23, q24 -- the arithmetic behind two misconceptions
assert add_ses(6, 40, 8, 50) > sd_diff(6, 40, 8, 50)
c.conceptual(23, "the student added standard errors; squaring, adding and taking the root "
                 "gives sqrt(0.9 + 1.28) = 1.477 against the student's 2.080, and a sum of "
                 "squares is always less than the square of the sum for positive terms")
assert abs(sd_diff(2, 50, 2, 50) / sd_diff(1, 50, 1, 50) - 2.0) < 1e-12
c.conceptual(24, "both variance terms carry sigma^2, so doubling sigma quadruples the total "
                 "variance and doubles the standard deviation -- checked above by doubling "
                 "sigma from 1 to 2 at n = 50")

# --- conceptual items, with the reasoning that fixes each key ----------------
c.conceptual(4, "Var(X - Y) = Var(X) + Var(Y) for independent X and Y: subtracting a quantity "
                "that varies does not remove its variability, it compounds with the other's")
c.conceptual(9, "CED 4.6.B.3/4.6.B.4 offer two routes -- both populations normal, or BOTH "
                "n >= 30. Pooling 18 and 22 into 40 is neither, and the samples' being random "
                "governs a different condition")
c.conceptual(10, "CED 4.6.B.2: for experimental data the random ASSIGNMENT of treatments meets "
                 "the randomization condition, and the 10 percent condition, which concerns "
                 "sampling without replacement from a population, does not apply")
c.conceptual(13, "the standard deviation of a sampling distribution describes how much the "
                 "STATISTIC x1bar - x2bar varies around mu1 - mu2 across repeated pairs of "
                 "samples, not how individual observations differ")
c.conceptual(15, "the sampling distribution of x1bar - x2bar is centered at mu1 - mu2, so -2.4 "
                 "is a statement about the two population means, not about the one pair of "
                 "samples that happened to be drawn")
c.conceptual(16, "the CED's conditions are independence of the samples, the 10 percent "
                 "condition per population, normality (both populations normal or both "
                 "n >= 30), and randomization. Equal population standard deviations is not "
                 "among them -- the formula keeps sigma1 and sigma2 separate precisely so "
                 "they may differ")
c.conceptual(17, "measuring the same 40 people twice makes the two sets of measurements "
                 "dependent, so adding the variances is wrong; the design is matched pairs and "
                 "reduces to one sample of differences")
c.conceptual(22, "CED 4.6.B.3: normal populations give a normal sampling distribution for the "
                 "difference at any sample sizes, so 8 and 11 are not obstacles")
c.conceptual(25, "independence between the two samples is exactly what licenses adding the "
                 "variances; repeated measurements on the same patients are correlated, and "
                 "the right analysis is one sample of within-patient differences")

c.finish()
