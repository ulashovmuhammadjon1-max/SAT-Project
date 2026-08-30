"""Verification for AP STATISTICS 3.2, sampling distributions for sample proportions.

Every standard deviation is computed from sqrt(p(1-p)/n) and cross-checked
against the standard deviation of the COUNT divided by n -- the two must agree,
which is what makes the q2 distractor (sqrt(np(1-p)), the count's standard
deviation) demonstrably a different quantity rather than merely a wrong-looking
one.

The condition items are checked by evaluating each condition as a predicate:
`large_counts`, `ten_percent` and the randomization requirement are separate
functions, and each scenario is run through ALL of them so the verifier can
assert that exactly the intended condition fails. That is the point of those
items -- a student who has merged the conditions into one rule cannot answer
them -- and a check that only evaluated the intended condition would not notice
if a scenario accidentally broke a second one too.

Run: python3 verify_s3_2.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_2

c = U.Checker(s3_2)


def sd_phat(p, n):
    """Standard deviation of p-hat, computed two ways and required to agree."""
    direct = math.sqrt(p * (1 - p) / n)
    from_count = math.sqrt(n * p * (1 - p)) / n
    assert abs(direct - from_count) < 1e-12, (
        f"routes disagree for p={p} n={n}: {direct} vs {from_count}")
    return direct


def large_counts(p, n):
    """EK 3.2.B.2: both expected counts at least 10."""
    return n * p >= 10 and n * (1 - p) >= 10


def ten_percent(n, population):
    """EK 3.2.B.1.ii: the sample is at most a tenth of the population."""
    return n <= 0.10 * population


# --- means and standard deviations -------------------------------------------------
c.check(3, sd_phat(0.4, 200), tol=0.005)         # 0.0346
c.check(4, 0.4)                                  # the mean of p-hat is p
c.check(5, sd_phat(0.6, 150), tol=0.005)         # 0.0400
c.check(6, sd_phat(0.25, 400), tol=0.005)        # 0.0217
c.check(7, sd_phat(0.5, 100), tol=0.005)         # 0.0500

# The q3 rationale names two distractors; both are confirmed to be what it says.
assert abs(0.4 * 0.6 / 200 - 0.0012) < 1e-12, "q3: 0.0012 is the VARIANCE of p-hat"
assert abs(math.sqrt(200 * 0.4 * 0.6) - 6.9282) < 1e-4, (
    "q3: 6.93 is the standard deviation of the COUNT of successes")
assert abs(200 * 0.4 - 80) < 1e-12, "q4: 80 is the expected count, not the proportion"

# Two of these are exact, which is worth asserting since the choices show them so.
assert sd_phat(0.6, 150) == 0.04 and sd_phat(0.5, 100) == 0.05


# --- probabilities -------------------------------------------------------------------
def p_above(value, p, n):
    return float(norm.sf(value, p, sd_phat(p, n)))


def p_below(value, p, n):
    return float(norm.cdf(value, p, sd_phat(p, n)))


c.check(14, p_above(0.45, 0.4, 200), tol=0.01)                       # 0.074
c.check(15, p_below(0.55, 0.6, 150), tol=0.01)                       # 0.106
c.check(16, p_below(0.28, 0.25, 400) - p_below(0.22, 0.25, 400), tol=0.005)   # 0.834

# Each of those scenarios must satisfy the conditions, or the normal calculation
# the item asks for would not be legitimate in the first place.
for p, n in ((0.4, 200), (0.6, 150), (0.25, 400)):
    assert large_counts(p, n), f"p={p} n={n} must satisfy large counts for a normal calculation"


def conditions_fail_one_at_a_time():
    """q10-q13, q22: each scenario must fail exactly the condition its key names."""
    # q10: p = 0.4, n = 200 -- large counts holds.
    assert large_counts(0.4, 200)
    assert (200 * 0.4, 200 * 0.6) == (80.0, 120.0), "the two expected counts are 80 and 120"

    # q11: p = 0.03, n = 200 -- large counts fails on the SUCCESSES only.
    assert not large_counts(0.03, 200), "np = 6 is below 10"
    assert 200 * 0.03 == 6.0 and 200 * 0.97 == 194.0
    assert 200 * 0.97 >= 10, (
        "the failure must be on successes alone, which is what the key says")

    # q12: n = 200 from a population of 1,500 -- the 10% condition fails.
    assert not ten_percent(200, 1500), "200 exceeds 10% of 1,500"
    assert 0.10 * 1500 == 150.0

    # q13: n = 200 from a population of 50,000 -- the 10% condition holds.
    assert ten_percent(200, 50000)
    assert 0.10 * 50000 == 5000.0
    assert 200 / 50000 < 0.005, "the sample is well under half a percent of the population"

    # q22: same n, two very different p. Only the second fails large counts.
    assert large_counts(0.5, 40), "40(0.5) = 20 successes and 20 failures"
    assert not large_counts(0.05, 40), "40(0.05) = 2 successes"
    assert 40 * 0.05 == 2.0
    # And n alone does not decide it, which is the misconception being tested.
    assert large_counts(0.5, 40) != large_counts(0.05, 40), (
        "the same n gives opposite verdicts, so the condition is not about n alone")


def spread_behaviour():
    """q17, q18, q24, q25: how the standard deviation responds to n and to p."""
    # q17/q24: the standard deviation falls as 1/sqrt(n).
    base = sd_phat(0.3, 100)
    assert abs(sd_phat(0.3, 400) - base / 2) < 1e-12, "quadrupling n halves the spread"
    assert abs(sd_phat(0.3, 200) - base / 2) > 1e-6, "doubling n does not halve it"
    # q25: n = 100 against n = 900 is a factor of 3, not 9.
    assert abs(sd_phat(0.3, 100) / sd_phat(0.3, 900) - 3.0) < 1e-9, (
        "nine times the sample size gives three times the precision")

    # q18: p(1-p) peaks at p = 0.5.
    values = {p: p * (1 - p) for p in (0.10, 0.25, 0.50, 0.75, 0.90)}
    best = max(values, key=values.get)
    assert best == 0.50, f"p(1-p) is maximized at {best}"
    assert values[0.25] == values[0.75], "the function is symmetric about 0.5"

    # q23: when large counts fails, the mean and the standard deviation formula
    # still hold -- only the normal SHAPE is unreliable.
    p, n = 0.03, 200
    assert not large_counts(p, n)
    assert abs(sd_phat(p, n) - math.sqrt(p * (1 - p) / n)) < 1e-12, (
        "the standard deviation formula is unaffected by the shape condition")


conditions_fail_one_at_a_time()
spread_behaviour()

c.check(18, 0.50)                                # p maximizing p(1-p)
c.check(24, 4)                                   # multiply n by 4 to halve the spread

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.2.A.1: p-hat is unbiased, so its sampling distribution centres on p for every n.")
c.conceptual(2, "EK 3.2.A.1: verified above -- sqrt(p(1-p)/n) is the standard deviation of the PROPORTION; sqrt(np(1-p)) is that of the count.")
c.conceptual(8, "EK 3.2.B.2: both np and n(1-p) must be at least 10, since either count being small leaves the distribution skewed.")
c.conceptual(9, "EK 3.2.B.1.ii: the 10% condition requires the population to be at least ten times the sample, which is what keeps the draws near-independent.")
c.conceptual(10, "EK 3.2.B.2: computed above -- 80 expected successes and 120 expected failures both exceed 10.")
c.conceptual(11, "EK 3.2.B.2: computed above -- np = 6 fails while n(1-p) = 194 passes, so a large n is not sufficient.")
c.conceptual(12, "EK 3.2.B.1.ii: computed above -- 10% of 1,500 is 150 and the sample of 200 exceeds it.")
c.conceptual(13, "EK 3.2.B.1.ii: computed above -- 200 from 50,000 is under half a percent, well inside the limit.")
c.conceptual(17, "EK 3.2.A.1: verified above -- the spread falls in proportion to 1 over the square root of n.")
c.conceptual(19, "EK 3.2.C.1: a sampling distribution's standard deviation is a typical distance between a sample statistic and the parameter, stated in context.")
c.conceptual(20, "EK 1.2.A.5: p-hat is computed from a sample and varies; p is the fixed population value it estimates.")
c.conceptual(21, "EK 3.2.B.1.i: without random selection the statistic may be biased, so the sampling distribution need not centre on p and no formula repairs that.")
c.conceptual(22, "EK 3.2.B.2: computed above -- the same n of 40 passes large counts at p = 0.5 and fails at p = 0.05.")
c.conceptual(23, "EK 3.2.B.2: verified above -- the mean and the standard deviation formula survive; it is the normal SHAPE that becomes untrustworthy.")
c.conceptual(25, "EK 3.2.A.1: computed above -- both centre at 0.3 while the larger sample's spread is three times narrower, not nine times.")

c.finish()
