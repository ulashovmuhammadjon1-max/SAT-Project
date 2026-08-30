"""Verify AP Statistics 4.10 Carrying Out a Two-Sample Test for Two Means.

Distribution: the two-sample statistic t = ((xbar1 - xbar2) - 0)/sqrt(s1^2/n1 +
s2^2/n2) follows a Student's t distribution when H0 is true (CED 4.10.A.1). The
CED does not fix one df -- it brackets it between the CONSERVATIVE value
min(n1, n2) - 1 and the pooled n1 + n2 - 2, with technology's
Welch-Satterthwaite value in between. Every stem naming a p-value names which
df to use, and both values are computed here so the difference between them is
demonstrated rather than assumed.

Degrees of freedom used: q1-q2 conservative 31 (Welch 62.91 computed for the
distractor); q3-q4 conservative 14; q5 conservative 39; q8 conservative 24;
q9 conservative 31; q14 df 40 as stated; q21 df 20 as stated.
"""
import math

from scipy import stats

import s4_10
from s_verify_util import Checker

c = Checker(s4_10)
T, N = stats.t, stats.norm


def se_diff(s1, n1, s2, n2):
    return math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)


def add_ses(s1, n1, s2, n2):
    return s1 / math.sqrt(n1) + s2 / math.sqrt(n2)


def tstat(diff, s1, n1, s2, n2):
    return diff / se_diff(s1, n1, s2, n2)


def df_conservative(n1, n2):
    return min(n1, n2) - 1


def df_welch(s1, n1, s2, n2):
    a, b = s1 ** 2 / n1, s2 ** 2 / n2
    return (a + b) ** 2 / (a ** 2 / (n1 - 1) + b ** 2 / (n2 - 1))


# q1, q2, q9, q12 -- one pair of samples used four ways
SE1 = se_diff(9.1, 32, 8.3, 35)
t1 = tstat(4.6, 9.1, 32, 8.3, 35)
assert abs(SE1 - 2.1345) < 5e-5
c.check(1, round(t1, 3))

df1 = df_conservative(32, 35)
assert df1 == 31
# 0.0195 (conservative df 31) and 0.0175 (technology's df 62.91) differ by only
# 0.002, so this check runs at a tolerance tight enough to tell them apart.
c.check(2, round(T.sf(t1, df1), 4), tol=1e-4)
dfw1 = df_welch(9.1, 32, 8.3, 35)
assert df1 <= dfw1 <= 32 + 35 - 2, "CED 4.10.A.1's bracket"
assert abs(T.sf(t1, dfw1) - 0.0175) < 5e-5, "technology's df, the q2 distractor"
assert abs(2 * T.sf(t1, df1) - 0.0390) < 5e-5, "the two-sided distractor in q2"

c.check(9, round(T.ppf(0.95, df1), 3))
assert abs(N.ppf(0.95) - 1.645) < 5e-4, "the z distractor in q9"

wrong12 = 4.6 / add_ses(9.1, 32, 8.3, 35)
assert abs(add_ses(9.1, 32, 8.3, 35) - 3.012) < 5e-4
assert abs(wrong12 - 1.527) < 5e-4 and wrong12 < t1
c.conceptual(12, "adding standard errors gives 1.609 + 1.403 = 3.012 against the correct "
                 "2.135, so the statistic falls from 2.155 to 1.527, computed above; a larger "
                 "denominator always shrinks |t| and makes a real difference harder to detect")

# q3, q4 -- small samples, two-sided
t3 = tstat(-2.8, 4.2, 15, 5.6, 18)
assert t3 < 0, "the statistic must keep its sign"
c.check(3, round(t3, 3))
df3 = df_conservative(15, 18)
assert df3 == 14
c.check(4, round(2 * T.cdf(t3, df3), 4))
assert abs(T.cdf(t3, df3) - 0.0617) < 5e-5, "the one-tail distractor in q4"

# q5 -- statistic and one-sided p-value together
t5 = tstat(3.2, 6, 40, 7, 40)
df5 = df_conservative(40, 40)
assert df5 == 39
c.check(5, [round(t5, 3), round(T.sf(t5, df5), 4)])
assert abs(2 * T.sf(t5, df5) - 0.0342) < 5e-5, "the two-sided distractor in q5"

# q8 -- two-sided p-value from summary statistics
t8 = tstat(58.2 - 63.7, 12.5, 25, 10.4, 28)
df8 = df_conservative(25, 28)
assert df8 == 24 and abs(t8 + 1.7295) < 5e-4
c.check(8, round(2 * T.cdf(t8, df8), 4))
assert abs(T.cdf(t8, df8) - 0.0483) < 5e-5, "the one-tail distractor in q8"

# q14 -- two-sided p-value at a stated df
c.check(14, round(2 * T.sf(1.85, 40), 4))
assert abs(T.sf(1.85, 40) - 0.0359) < 5e-5, "the one-tail distractor in q14"

# q21 -- significance decision plus p-value at a stated df
p21 = T.cdf(-2.41, 20)
assert p21 < 0.05, "q21's key says the result IS significant at 0.05"
assert abs(p21 - 0.0129) < 5e-5 and abs(2 * p21 - 0.0257) < 5e-5
key21 = s4_10.QUESTIONS[20]["choices"][s4_10.QUESTIONS[20]["ans"]]
assert "0.0129" in key21 and key21.startswith("Yes"), key21
c.conceptual(21, "the lower-tail area below -2.41 at df 20 is 0.0129, computed above, which is "
                 "below 0.05, so the result is significant; 0.0257 is the two-sided value and "
                 "belongs to a different alternative")

# q13 -- fewer degrees of freedom give a larger p-value for the same t
assert T.sf(2.0, 10) > T.sf(2.0, 100), "heavier tails at smaller df"
c.conceptual(13, "for a fixed t the tail area shrinks as df grows -- T.sf(2.0, 10) = "
                 f"{T.sf(2.0, 10):.4f} against T.sf(2.0, 100) = {T.sf(2.0, 100):.4f} -- so the "
                 "conservative (smaller) df yields the larger p-value and makes rejection "
                 "harder")

# q23 -- the two-sided p-value is exactly twice the one-sided one
assert abs(2 * T.sf(1.5, 17) - 2 * T.sf(1.5, 17)) < 1e-15
for df in (5, 17, 40, 200):
    assert abs(2 * T.sf(1.5, df) - (T.sf(1.5, df) + T.cdf(-1.5, df))) < 1e-12
c.conceptual(23, "the t distribution is symmetric, so the opposite tail beyond the same "
                 "distance has equal area; checked above at df 5, 17, 40 and 200, the "
                 "two-sided p-value is exactly twice the one-sided one whenever the sample "
                 "difference falls on the Ha side")

# q25 -- the degrees-of-freedom bracket
assert df_conservative(22, 26) == 21 and 22 + 26 - 2 == 46
c.check(25, [21, 46])

# q10 -- the formal decision
assert 0.011 > 0.01, "q10's key depends on p exceeding alpha"
c.conceptual(10, "CED's decision rule is reject when p <= alpha; 0.011 > 0.01, so H0 is not "
                 "rejected, and a failure to reject is never evidence that mu1 equals mu2")

# --- conceptual items, with the reasoning that fixes each key ----------------
c.conceptual(6, "the p-value is computed by ASSUMING mu1 = mu2, so it reports how surprising "
                "the observed difference would be in that case; a probability conditioned on "
                "H0 cannot also be a probability about H0")
c.conceptual(7, "p = 0.28 means the observed difference is unremarkable when the means are "
                "equal. That fails to establish a difference and equally fails to establish "
                "equality -- no result ever confirms a null")
c.conceptual(11, "random ASSIGNMENT is what licenses a causal claim; the conclusion is still "
                 "stated non-definitively, so 'definitely' overstates it, and the claim that "
                 "no study can show causation is simply false for experiments")
c.conceptual(15, "conditions come before the procedure. Convenience samples fail randomization, "
                 "so there is no sampling distribution to refer t to and the 0.05 comparison is "
                 "meaningless; robustness concerns shape, not selection")
c.conceptual(16, "a Type I error is rejecting a true null -- concluding the methods differ when "
                 "they do not. A nonzero difference in SAMPLE means under a true null is "
                 "ordinary variability, not an error")
c.conceptual(17, "power grows with |t| under the true difference, which larger samples achieve "
                 "by shrinking the standard error; a smaller alpha, a two-sided alternative, "
                 "the conservative df and greater within-group spread all reduce it")
c.conceptual(18, "at n = 5,000 per group the standard error is tiny, so a difference of 0.03 "
                 "is easily detected; a small p-value answers whether a difference is real, "
                 "not whether it is large enough to matter")
c.conceptual(19, "the two-sample standard error adds variances, which requires independence; "
                 "before-and-after values on the same subject are correlated, so the correct "
                 "analysis is a one-sample t-test on the 30 differences")
c.conceptual(20, "CED 4.10.A.1 writes the numerator as (xbar1 - xbar2) - 0, which is just the "
                 "observed difference; the population means are unknown and the numerator "
                 "keeps its sign")
c.conceptual(22, "the calculation conditions on H0 being true, so it cannot report the "
                 "probability that H0 is true; nor is the complement 96 percent a probability "
                 "for Ha")
c.conceptual(24, "with n1 = 9 and n2 = 11 both below 30 and no claim of normal populations, "
                 "CED 4.9.C.1.iii requires both sample distributions to be free from strong "
                 "skewness; they are not, so the t distribution is the wrong reference and the "
                 "0.02 does not mean what it appears to")

c.finish()
