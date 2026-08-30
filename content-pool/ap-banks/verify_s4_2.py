"""Verify AP Statistics 4.2 Confidence Intervals for a Mean or Mean Difference.

Distribution: Student's t with df = n - 1 (for matched pairs, n is the number of
DIFFERENCES, so df = 12 - 1 = 11 in q10, not 22). Critical values come from
scipy.stats.t.ppf at 0.5 + C/2; standard errors are s/sqrt(n); intervals are
xbar +/- t* SE. The z* values that several distractors are built from come from
scipy.stats.norm.ppf and are computed here too, so each is confirmed to be a
different number from the key rather than assumed to be.
"""
import math
import statistics as st

from scipy import stats

import s4_2
from s_verify_util import Checker

c = Checker(s4_2)
T, N = stats.t, stats.norm


def tstar(conf, df):
    return T.ppf(0.5 + conf / 2, df)


def interval(xbar, s, n, conf):
    se = s / math.sqrt(n)
    me = tstar(conf, n - 1) * se
    return se, me, (xbar - me, xbar + me)


# q1, q10 -- degrees of freedom
c.check(1, 18 - 1)
c.check(10, 12 - 1)

# q2 -- t* with df = 17
c.check(2, round(tstar(0.95, 17), 3))
assert abs(N.ppf(0.975) - 1.960) < 5e-4, "the z* distractor in q2"

# q3 -- 95 percent interval, df = 24
se3, me3, ci3 = interval(24.6, 3.2, 25, 0.95)
assert abs(se3 - 0.64) < 1e-12 and abs(tstar(0.95, 24) - 2.0639) < 5e-5
c.check(3, [round(v, 3) for v in ci3])
zme3 = N.ppf(0.975) * se3
assert abs(24.6 - zme3 - 23.346) < 5e-4, "the z* distractor in q3"

# q4 -- standard error
c.check(4, 8.4 / math.sqrt(36))
assert abs(8.4 / 36 - 0.233) < 1e-3, "the divide-by-n distractor in q4"

# q5 -- margin of error, df = 11, 90 percent
se5, me5, _ = interval(0, 5.1, 12, 0.90)
assert abs(tstar(0.90, 11) - 1.7959) < 5e-5
c.check(5, round(me5, 3))
assert abs(se5 - 1.472) < 5e-4, "the SE-only distractor in q5"

# q13 -- matched pairs, 8 differences, df = 7
DIFFS = [4, 1, 5, 2, 6, 1, 4, 6]
assert st.mean(DIFFS) == 3.625 and abs(st.stdev(DIFFS) - 2.0659) < 5e-5
se13, me13, ci13 = interval(st.mean(DIFFS), st.stdev(DIFFS), len(DIFFS), 0.95)
assert abs(tstar(0.95, 7) - 2.3646) < 5e-5
c.check(13, [round(v, 3) for v in ci13])

# q14 -- 99 percent interval, df = 29
se14, me14, ci14 = interval(68.2, 9.4, 30, 0.99)
assert abs(tstar(0.99, 29) - 2.7564) < 5e-5
c.check(14, [round(v, 3) for v in ci14])
zme14 = N.ppf(0.995) * se14
assert abs(68.2 - zme14 - 63.779) < 1e-3, "the z* distractor in q14"
assert abs(68.2 - tstar(0.90, 29) * se14 - 65.284) < 1e-3, "the 90 percent distractor in q14"
assert abs(68.2 - se14 - 66.484) < 1e-3, "the SE-only distractor in q14"
assert abs(68.2 - tstar(0.99, 29) * (9.4 / 30) - 67.336) < 1e-3, "the s/n distractor in q14"

# q16 -- recover xbar and margin of error from the endpoints
lo, hi = 14.2, 19.8
c.check(16, [(lo + hi) / 2, (hi - lo) / 2])

# q17 -- 95 percent interval, df = 39
se17, me17, ci17 = interval(12.8, 2.9, 40, 0.95)
assert abs(tstar(0.95, 39) - 2.0227) < 5e-5
c.check(17, [round(v, 3) for v in ci17])
zme17 = N.ppf(0.975) * se17
assert abs(12.8 - zme17 - 11.901) < 1e-3, "the z* distractor in q17"

# q20 -- t* with df = 29 at 98 percent
c.check(20, round(tstar(0.98, 29), 3))
assert abs(N.ppf(0.99) - 2.326) < 5e-4, "the z* distractor in q20"

# q21 -- two margins of error from the same sample
se21 = 6.5 / math.sqrt(20)
c.check(21, [round(tstar(0.90, 19) * se21, 3), round(tstar(0.95, 19) * se21, 3)])
assert tstar(0.95, 19) * se21 > tstar(0.90, 19) * se21, "higher confidence must be wider"

# q25 -- z* in place of t* understates the margin of error
se25 = 7.2 / math.sqrt(16)
me_t = tstar(0.95, 15) * se25
me_z = N.ppf(0.975) * se25
assert abs(tstar(0.95, 15) - 2.1314) < 5e-5
assert me_z < me_t, "z* must be smaller than t* at the same confidence"
key25 = s4_2.QUESTIONS[24]["choices"][s4_2.QUESTIONS[24]["ans"]]
for value in (round(me_t - me_z, 3), round(me_t, 3), round(me_z, 3)):
    assert f"{value:.3f}" in key25, (value, key25)
c.conceptual(25, "df = 15 gives t* = 2.1314 against z* = 1.9600 on the same SE of 1.8, so the "
                 "correct margin of error is 3.837 and the student's is 3.528, understated by "
                 "0.309; all three values are computed above")

# q18 -- the 10 percent condition, computed rather than asserted
assert 20 > 0.10 * 150, "the 10 percent condition must actually fail here"
c.conceptual(18, "the condition is n <= 0.10N; 0.10 x 150 = 15 and the sample is 20, which is "
                 "13.3 percent of the club, so the condition fails -- randomness of the "
                 "selection does not rescue it")

# --- conceptual items, with the reasoning that fixes each key ----------------
c.conceptual(6, "before and after times come from the SAME athlete, so the two sets are "
                "dependent; CED 4.2.B.2 sends a matched-pairs design to a one-sample t "
                "procedure on the 20 differences")
c.conceptual(7, "CED 4.2.C.1.iii: with n = 15 < 30 the sample must be free from strong "
                "skewness and outliers, and this sample is neither; skewness is a property of "
                "the data, not of how the sample was drawn")
c.conceptual(8, "t is used precisely because sigma is unknown and s is substituted for it "
                "(CED 4.2.A.2); the extra estimation variability is what the fatter tails pay "
                "for")
c.conceptual(9, "CED 4.2.A.1: symmetric, bell-shaped, fatter-tailed than the standard normal, "
                "narrowing toward it as df increases; the standard deviation of a t "
                "distribution exceeds 1 for finite df, so 'mean 0 and SD 1 for every df' is "
                "false")
c.conceptual(11, "the standard error is fixed by the data, so raising confidence can only "
                 "raise t* and widen the interval -- precision and confidence trade against "
                 "each other")
c.conceptual(12, "the margin of error is t* s/sqrt(n); only n is under the researcher's "
                 "control among the listed changes, and increasing it shrinks both the "
                 "standard error and the critical value")
c.conceptual(15, "CED 4.2.B.3: the parameter is the POPULATION mean difference in context, "
                 "with the order of subtraction stated. An interval never estimates the "
                 "statistic for the participants actually studied")
c.conceptual(19, "the standard error is the estimated standard deviation of the sampling "
                 "distribution of xbar, so it describes sample-to-sample variation of the "
                 "statistic, not the spread of individual observations")
c.conceptual(22, "different plants in the two groups means the samples are independent; "
                 "pairing requires two measurements on the same unit, and pairing by recording "
                 "order would be arbitrary")
c.conceptual(23, "CED 4.2.C.1.iii gives three alternative routes; n = 45 >= 30 is one of them, "
                 "so moderate skew is not disqualifying")
c.conceptual(24, "for matched pairs the sample is the set of differences, so 42 >= 30 "
                 "satisfies the sample data condition on its own")

c.finish()
