"""Verify AP Statistics 4.1 Sampling Distributions for Sample Means.

Distribution used throughout: the sampling distribution of xbar is normal with
mean mu and standard deviation sigma/sqrt(n). No degrees of freedom appear in
this topic -- sigma is given in every stem, so the standard normal, not t, is
the reference distribution. Every probability below is scipy.stats.norm, and
every critical value is norm.ppf; none is recalled from a table.

The "wrong" values the distractors are built from (using sigma in place of
sigma/sqrt(n), dividing by n instead of sqrt(n)) are computed here as well, so
each distractor is confirmed to be a different number from the key.
"""
import math

from scipy import stats

import s4_1
from s_verify_util import Checker

c = Checker(s4_1)
Z = stats.norm


def sd_xbar(sigma, n):
    return sigma / math.sqrt(n)


# q1 -- mu_xbar = mu, sigma_xbar = sigma/sqrt(n)
c.check(1, [68, sd_xbar(12, 36)])
assert abs(12 / 36 - 0.3333) < 1e-3, "the divide-by-n distractor in q1"

# q2 -- normal population, n = 25, upper tail
se2 = sd_xbar(80, 25)
assert se2 == 16.0
c.check(2, round(Z.sf((520 - 500) / se2), 4))
assert abs(Z.sf((520 - 500) / 80) - 0.4013) < 5e-5, "the sigma-not-SE distractor in q2"

# q5 -- quadrupling n halves the standard deviation of xbar
assert sd_xbar(20, 25) == 4.0 and sd_xbar(20, 100) == 2.0
c.conceptual(5, "sigma/sqrt(n) with sigma = 20 gives 20/5 = 4 at n = 25 and 20/10 = 2 at "
                "n = 100: multiplying n by 4 divides the standard deviation by sqrt(4) = 2, "
                "not by 4")

# q6 -- smallest n with sigma/sqrt(n) <= 1.5
n6 = min(n for n in range(1, 1000) if sd_xbar(9, n) <= 1.5)
assert n6 == 36
c.check(6, n6)

# q7 -- CLT applies at n = 50 from a skewed population
se7 = sd_xbar(1.1, 50)
c.check(7, round(Z.cdf((3.0 - 3.2) / se7), 4))

# q8 -- z-score of a sample mean
c.check(8, round((63 - 60) / sd_xbar(8, 16), 2))
assert abs((63 - 60) / 8 - 0.375) < 1e-9, "the sigma-not-SE distractor in q8"

# q9 -- 90th percentile of the sampling distribution
c.check(9, round(250 + Z.ppf(0.90) * sd_xbar(40, 16), 1))
assert abs(250 + Z.ppf(0.90) * 40 - 301.3) < 0.05, "the sigma-not-SE distractor in q9"

# q13 -- sigma/sqrt(n) with n = 64
c.check(13, sd_xbar(2.5, 64))
assert abs(2.5 / 64 - 0.0391) < 1e-4, "the divide-by-n distractor in q13"

# q14 -- probability between two values
se14 = sd_xbar(15, 36)
assert se14 == 2.5
c.check(14, round(Z.cdf((124 - 120) / se14) - Z.cdf((118 - 120) / se14), 4))

# q15 -- recover sigma from sigma_xbar
c.check(15, 1.6 * math.sqrt(25))

# q16 -- normal population, n = 4
c.check(16, round(Z.sf((7.9 - 7.5) / sd_xbar(0.8, 4)), 4))
assert abs(Z.sf((7.9 - 7.5) / 0.8) - 0.3085) < 5e-5, "the sigma-not-SE distractor in q16"

# q17 -- the student's error: sigma in place of sigma/sqrt(n)
right17 = Z.sf((52 - 50) / sd_xbar(6, 9))
wrong17 = Z.sf((52 - 50) / 6)
assert abs(right17 - 0.1587) < 5e-5 and abs(wrong17 - 0.3694) < 5e-5, (right17, wrong17)
assert "0.1587" in s4_1.QUESTIONS[16]["choices"][s4_1.QUESTIONS[16]["ans"]]
assert "0.3694" in s4_1.QUESTIONS[16]["choices"][0]
c.conceptual(17, "the standard deviation of xbar is 6/sqrt(9) = 2, so z = 1.00 and the "
                 "probability is norm.sf(1.00) = 0.1587; the student's z = 2/6 = 0.333 gives "
                 "0.3694, and both values are computed above")

# q20 -- larger n makes a fixed margin more probable
se_25, se_100 = sd_xbar(20, 25), sd_xbar(20, 100)
p25 = Z.cdf(4 / se_25) - Z.cdf(-4 / se_25)
p100 = Z.cdf(4 / se_100) - Z.cdf(-4 / se_100)
c.check(20, [100, round(p100, 4), round(p25, 4), 25])

# q25 -- recover both parameters
c.check(25, [45, 3 * math.sqrt(49)])

# --- conceptual items, with the reasoning that fixes each key ----------------
c.conceptual(3, "CED 4.1.B.2/4.1.B.3: normality of the xbar distribution comes from a normal "
                "population (any n) or from n >= 30; a strongly skewed population with n = 12 "
                "has neither, so the normal model is not yet justified -- but a much larger n "
                "would justify it, which rules out the never-ever option")
c.conceptual(4, "the 10 percent condition is n <= 0.10N; here 100 > 0.10(800) = 80, so it "
                "fails. Randomization holds (a simple random sample), and large counts is a "
                "proportion condition, not a mean condition")
c.conceptual(10, "a sampling distribution is the distribution of a statistic over all possible "
                 "samples of a fixed size, which is neither the distribution of one sample nor "
                 "the distribution of the population")
c.conceptual(11, "CED 4.1.B.2: a normal population gives an exactly normal sampling "
                 "distribution for xbar at every sample size, so n = 5 is not an obstacle")
c.conceptual(12, "the central limit theorem is a statement about the sampling distribution of "
                 "the statistic, not about the population and not about any single sample")
c.conceptual(18, "the standard deviation of a sampling distribution measures sample-to-sample "
                 "variation of xbar about mu; it is not the spread of individual observations "
                 "and it guarantees nothing about one particular sample")
c.conceptual(19, "mu_xbar = mu for every n, so the center is fixed, while sigma_xbar = "
                 "sigma/sqrt(n) shrinks as n grows: same center, smaller spread")
c.conceptual(21, "n = 200 is random and 200 <= 0.10(15,000) = 1,500, so both conditions hold; "
                 "large counts (np >= 10, n(1-p) >= 10) is a condition for proportions, not "
                 "for means")
c.conceptual(22, "the CED lists randomization, the 10 percent condition, and normality (normal "
                 "population, or n >= 30, with more needed under extreme skew). Knowing sigma "
                 "is not among them; it decides z versus t, not the shape")
c.conceptual(23, "both sampling distributions center on mu; variance is sigma^2/n, so a "
                 "tenfold n divides the variance by 10 but the standard deviation only by "
                 "sqrt(10) = 3.16")
c.conceptual(24, "CED 4.1.B.3 states that an extremely skewed population may require a sample "
                 "size much larger than 30; also 30 <= 0.10(9,000) = 900, so the 10 percent "
                 "condition is not the problem")

c.finish()
