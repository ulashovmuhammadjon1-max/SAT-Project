"""Verify AP Statistics 4.3 Justifying a Claim from a Confidence Interval.

Distribution: Student's t with df = n - 1 throughout; critical values from
scipy.stats.t.ppf, and the z* values behind two distractors from
scipy.stats.norm.ppf. Widths are 2 t* s/sqrt(n), and the CED's claim that width
is approximately proportional to 1/sqrt(n) is checked numerically in q11 rather
than asserted -- the ratio is close to but not exactly 1/2 because t* also
changes with df, which is why the CED says "approximately".

The interpretation items are conceptual; each carries the statement from CED
4.3.A that fixes its key.
"""
import math

from scipy import stats

import s4_3
from s_verify_util import Checker

c = Checker(s4_3)
T, N = stats.t, stats.norm


def tstar(conf, df):
    return T.ppf(0.5 + conf / 2, df)


def margin(s, n, conf):
    return tstar(conf, n - 1) * s / math.sqrt(n)


# q8 -- widths at 90 and 99 percent from the same sample (n = 20, s = 8)
w90, w99 = 2 * margin(8, 20, 0.90), 2 * margin(8, 20, 0.99)
assert w99 > w90, "a higher confidence level must widen the interval"
c.check(8, [round(w90, 3), round(w99, 3)])
assert abs(margin(8, 20, 0.90) - 3.093) < 5e-4 and abs(margin(8, 20, 0.99) - 5.118) < 5e-4

# q9, q10 -- width is proportional to 1/sqrt(n)
assert abs(1 / math.sqrt(4 * 1) - 0.5) < 1e-12, "n x 4 halves 1/sqrt(n)"
c.check(9, 4)
assert abs(1 / math.sqrt(9 * 1) - 1 / 3) < 1e-12, "n x 9 divides 1/sqrt(n) by 3"
c.check(10, 9)

# q11 -- widths at n = 36 and n = 144, same s and confidence level
w36, w144 = 2 * margin(12, 36, 0.95), 2 * margin(12, 144, 0.95)
c.check(11, [round(w36, 3), round(w144, 3)])
assert 0.47 < w144 / w36 < 0.50, ("approximately, not exactly, one half", w144 / w36)

# q12 -- rescale a margin of error from 90 to 95 percent on the same sample
se12 = 2.5 / tstar(0.90, 24)
c.check(12, round(tstar(0.95, 24) * se12, 3))

# q13 -- smallest n with a 95 percent t-margin of error at most 1 when s = 6
n13 = min(n for n in range(2, 5000) if margin(6, n, 0.95) <= 1)
assert n13 == 141, n13
c.check(13, n13)
n13z = min(n for n in range(2, 5000) if N.ppf(0.975) * 6 / math.sqrt(n) <= 1)
assert n13z == 139, ("the z*-based distractor in q13", n13z)

# q14 -- margin of error and width from the endpoints
lo, hi = 34.1, 41.9
c.check(14, [round((hi - lo) / 2, 1), round(hi - lo, 1)])
assert abs((lo + hi) / 2 - 38.0) < 1e-9, "the midpoint distractor in q14"

# q15 -- long-run capture rate over 200 intervals
c.check(15, 0.90 * 200)

# q24 -- the only value outside (14.8, 21.2)
outside = [v for v in (22.0, 15.0, 18.0, 20.5, 21.0) if not 14.8 <= v <= 21.2]
assert outside == [22.0], outside
c.check(24, 22.0)

# q25 -- halving n widens the interval through BOTH the SE and the critical value
se30, se15 = 1 / math.sqrt(30), 1 / math.sqrt(15)
assert se15 > se30 and tstar(0.95, 14) > tstar(0.95, 29)
assert abs(tstar(0.95, 29) - 2.045) < 5e-4 and abs(tstar(0.95, 14) - 2.145) < 5e-4
c.conceptual(25, "cutting n from 30 to 15 multiplies the standard error by sqrt(2) = 1.414 "
                 "and raises t* from 2.045 (df 29) to 2.145 (df 14); both factors widen the "
                 "interval, so it cannot be narrower")

# --- interpretation and justification items ----------------------------------
c.conceptual(1, "CED 4.3.A.3: the interpretation names the POPULATION mean. The sample mean is "
                "already known (it is the midpoint 21.0), and the interval describes neither "
                "the spread of individual commute times nor the distribution of sample means")
c.conceptual(2, "mu is a fixed constant and the interval is already computed, so it either "
                "contains mu or it does not -- there is no probability left. The 95 percent is "
                "the method's long-run capture rate, which is what the other four options say")
c.conceptual(3, "CED 4.3.A.2 verbatim in substance: in repeated random sampling with the same "
                "sample size from the same population, about C percent of the intervals "
                "constructed capture the parameter")
c.conceptual(4, "a confidence interval estimates an unknown population parameter; the sample "
                "mean is computed from the data with no uncertainty and is the interval's own "
                "center, so 'confident about the sample mean' is empty")
c.conceptual(5, "the interval is the set of plausible values for mu; 16 > 15.6 lies outside, "
                "so the data give evidence against the manager's claim")
c.conceptual(6, "0 lies inside (-0.4, 2.9), so no change remains plausible. Failing to rule "
                "out 0 is not evidence that the mean difference IS 0 -- every other value in "
                "the interval is equally plausible")
c.conceptual(7, "the entire interval (1.8, 4.6) is positive, so every plausible mean "
                "difference is an increase; the interval bounds the MEAN difference and says "
                "nothing about individual plants")
c.conceptual(16, "about 5 percent of 95 percent intervals miss by design; a single miss is "
                 "evidence of nothing wrong with the procedure, and the confidence level is a "
                 "property of the method rather than of one interval")
c.conceptual(17, "every value in (101.2, 108.8) exceeds 100, so mu > 100 is supported; the "
                 "interval does not single out its midpoint and does not describe individual "
                 "packages")
c.conceptual(18, "both intervals are centered at 50, so only t* differs; the higher confidence "
                 "level takes the larger critical value and yields the wider interval")
c.conceptual(19, "a larger n reduces s/sqrt(n) and so the width, but a new sample yields a new "
                 "xbar, so the center moves; and no individual interval is guaranteed to "
                 "capture mu")
c.conceptual(20, "the width is 2 t* s/sqrt(n): only a larger n reduces it legitimately. "
                 "Deleting extreme observations manipulates s, and rounding changes nothing")
c.conceptual(21, "with post minus pre as the order of subtraction and the whole interval below "
                 "0, every plausible mean difference is a decrease; the interval concerns the "
                 "mean difference, not individual participants")
c.conceptual(22, "CED 4.3.C.1: the standard error is fixed by the data, so a lower confidence "
                 "level lowers t* and narrows the interval")
c.conceptual(23, "an interval for a mean is narrower than the spread of the data by a factor "
                 "of about sqrt(n); it describes where mu plausibly lies, not where individual "
                 "scores lie")

c.finish()
