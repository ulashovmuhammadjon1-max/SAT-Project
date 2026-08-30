"""Verify AP Statistics 4.5 Carrying Out a Test for a Mean or Mean Difference.

Distribution: the one-sample t statistic t = (xbar - mu0)/(s/sqrt(n)) follows a
Student's t distribution with df = n - 1 when H0 is true (CED 4.5.A.1). Every
p-value below is an actual tail area from scipy.stats.t at the stated df -- an
upper tail for Ha: mu > mu0, a lower tail for Ha: mu < mu0, and twice the tail
area on the side the sample mean falls for a two-sided Ha. Critical values come
from t.ppf. The z values behind two distractors are computed from
scipy.stats.norm so that each is confirmed to differ from the t answer.

Degrees of freedom used, stated explicitly: q1-q2 df 35; q3-q4 df 19;
q5-q6 and q25 df 24; q7-q8 df 9 (ten paired DIFFERENCES); q18-q19 df 41;
q20 df 48; q21 df 35; q22 df 15.
"""
import math
import statistics as st

from scipy import stats

import s4_5
from s_verify_util import Checker

c = Checker(s4_5)
T, N = stats.t, stats.norm


def tstat(xbar, mu0, s, n):
    return (xbar - mu0) / (s / math.sqrt(n))


def p_upper(t, df):
    return T.sf(t, df)


def p_lower(t, df):
    return T.cdf(t, df)


def p_two(t, df):
    return 2 * T.sf(abs(t), df)


# q1, q2 -- n = 36, df = 35, upper tail
t1 = tstat(51.3, 50, 4.2, 36)
c.check(1, round(t1, 3))
c.check(2, round(p_upper(t1, 35), 4))
assert abs((51.3 - 50) / 4.2 - 0.310) < 5e-4, "the s-not-SE distractor in q1"
assert abs(2 * p_upper(t1, 35) - 0.0717) < 5e-5, "the two-sided distractor in q2"

# q3, q4 -- n = 20, df = 19, lower tail
t3 = tstat(27.4, 30, 6.1, 20)
assert t3 < 0, "the statistic must keep its sign"
c.check(3, round(t3, 3))
c.check(4, round(p_lower(t3, 19), 4))
assert abs(2 * p_lower(t3, 19) - 0.0719) < 5e-5, "the two-sided distractor in q4"
assert abs(1 - p_lower(t3, 19) - 0.9641) < 5e-5, "the complement distractor in q4"

# q5, q6 -- n = 25, df = 24, two-sided
t5 = tstat(104.2, 100, 9.5, 25)
c.check(5, round(t5, 3))
c.check(6, round(p_two(t5, 24), 4))
assert abs(p_upper(t5, 24) - 0.0184) < 5e-5, "the one-tail distractor in q6"

# q7, q8 -- matched pairs: ten DIFFERENCES, df = 9
DIFFS = [3, -1, 4, 2, 5, 0, 3, 6, 1, 2]
assert len(DIFFS) == 10 and st.mean(DIFFS) == 2.5 and abs(st.stdev(DIFFS) - 2.1731) < 5e-5
t7 = tstat(st.mean(DIFFS), 0, st.stdev(DIFFS), len(DIFFS))
c.check(7, round(t7, 3))
c.check(8, round(p_upper(t7, 9), 4))
assert abs(p_two(t7, 9) - 0.0054) < 5e-5, "the two-sided distractor in q8"

# q18, q20, q22 -- statistic and p-value together
t18 = tstat(8.6, 9.0, 1.4, 42)
c.check(18, [round(t18, 3), round(p_two(t18, 41), 4)])
assert abs(p_lower(t18, 41) - 0.0356) < 5e-5, "the one-tail distractor in q18"
assert p_two(t18, 41) > 0.05, "q19's decision depends on this p-value exceeding 0.05"

t20 = tstat(212, 200, 28, 49)
assert abs(t20 - 3.0) < 1e-12
c.check(20, [round(t20, 3), round(p_upper(t20, 48), 4)])
assert abs(p_two(t20, 48) - 0.0043) < 5e-5, "the two-sided distractor in q20"

t22 = tstat(3.42, 3.5, 0.35, 16)
c.check(22, [round(t22, 3), round(p_lower(t22, 15), 4)])
assert abs(p_two(t22, 15) - 0.3750) < 5e-5, "the two-sided distractor in q22"

# q21 -- one-sided critical value at alpha = 0.05, df = 35
c.check(21, round(T.ppf(0.95, 35), 3))
assert abs(N.ppf(0.95) - 1.645) < 5e-4, "the z distractor in q21"

# q25 -- the two-sided p-value is exactly twice the one-sided one
one, two = p_upper(t5, 24), p_two(t5, 24)
assert abs(two - 2 * one) < 1e-12, "symmetry of the t distribution"
key25 = s4_5.QUESTIONS[24]["choices"][s4_5.QUESTIONS[24]["ans"]]
assert f"{one:.4f}" in key25 and f"{two:.4f}" in key25, key25
c.conceptual(25, "the t distribution is symmetric, so the opposite tail contributes an equal "
                 "area: one-sided 0.0184 and two-sided 0.0368, both computed above at df 24, "
                 "and the factor of 2 holds at any df when xbar falls on the Ha side")

# q11 -- the formal decision against two significance levels
assert 0.031 <= 0.05 and 0.031 > 0.01
c.conceptual(11, "CED 4.5.C.1: reject when p <= alpha. 0.031 <= 0.05 rejects; 0.031 > 0.01 "
                 "does not, so the same evidence gives opposite decisions at the two levels")

# --- conceptual items, with the reasoning that fixes each key ----------------
c.conceptual(9, "CED 4.5.B.1: the p-value is P(a statistic at least this extreme in the "
                "direction of Ha GIVEN H0 true). It conditions on H0 and therefore cannot be "
                "a probability about H0, about Ha, or about the conclusion being wrong")
c.conceptual(10, "H0 is either true or false; the p-value assumes it true and measures how "
                 "unusual the data would be under that assumption, so P(H0 true) is not "
                 "something a p-value reports")
c.conceptual(12, "CED 4.5.C.3: the conclusion is in terms of Ha, in context, non-definitive, "
                 "and about the POPULATION parameter -- not about the sampled bottles, not "
                 "'definitely', and never a conclusion in favor of H0")
c.conceptual(13, "a large p-value means the data are consistent with mu = 45, which leaves "
                 "many other values equally consistent; failing to reject H0 is not evidence "
                 "FOR H0")
c.conceptual(14, "a Type I error is rejecting a true H0. A sample mean above 100 when mu = 100 "
                 "is ordinary sampling variability, not an error, and a non-random sample is a "
                 "design flaw rather than a Type I error")
c.conceptual(15, "a Type II error is failing to reject H0 when Ha is true. A p-value above "
                 "alpha is a decision, not an error -- it is an error only if Ha happens to be "
                 "true")
c.conceptual(16, "alpha IS the Type I error rate, so lowering it to 0.01 lowers that rate; "
                 "with the same data and the same true mu, a stricter rejection rule fails to "
                 "detect a real difference more often, so beta rises and power falls")
c.conceptual(17, "power rises with the magnitude of |t| under the true mu; only a larger n "
                 "does that here, by shrinking s/sqrt(n). A smaller alpha, a larger sigma and "
                 "a two-sided alternative each reduce power")
c.conceptual(19, "the p-value 0.0713 computed above exceeds alpha = 0.05, so H0 is not "
                 "rejected -- and a failure to reject is never evidence that mu equals 9.0")
c.conceptual(23, "the standard error shrinks like 1/sqrt(n), so at n = 40,000 a difference of "
                 "0.05 is easily detectable; statistical significance says a difference is "
                 "real, not that it is large enough to matter")
c.conceptual(24, "conditions are checked BEFORE the procedure. A convenience sample fails "
                 "randomization, and n = 18 with strong skew and an outlier fails the sample "
                 "data condition, so the t distribution does not describe this statistic and "
                 "the 0.03 is not a trustworthy p-value")

c.finish()
