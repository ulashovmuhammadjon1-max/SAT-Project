"""Verification for AP STATISTICS 3.3, confidence intervals for a proportion.

Every interval is built by one function, `z_interval`, that returns the critical
value, standard error, margin of error and both endpoints together, and each is
then checked against the module. Interval choices are compared endpoint by
endpoint, which the shared checker does automatically for a choice written
"(0.3033, 0.3967)".

Three properties are asserted for every interval rather than only the endpoints,
because an interval can have the right width and the wrong location or vice
versa:

  * it is centred exactly on p-hat;
  * its half-width equals the margin of error;
  * its full width is twice the margin of error -- which is what makes the
    "full width" distractor in q11 demonstrably a different number.

The sample-size items check the ROUNDING DIRECTION explicitly. Rounding 1067.07
down to 1067 would leave the achieved margin of error above the 0.03 requested,
and the verifier confirms that by computing the margin of error at both 1067 and
1068 and requiring only the latter to satisfy the constraint.

Run: python3 verify_s3_3.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_3

c = U.Checker(s3_3)


def z_star(confidence):
    return float(norm.ppf(1 - (1 - confidence) / 2))


def z_interval(phat, n, confidence):
    """(z*, SE, ME, (low, high)) for a one-sample z-interval for a proportion."""
    se = math.sqrt(phat * (1 - phat) / n)
    z = z_star(confidence)
    me = z * se
    low, high = phat - me, phat + me

    # Structural properties every interval must have.
    assert abs((low + high) / 2 - phat) < 1e-12, "the interval must centre on p-hat"
    assert abs((high - low) / 2 - me) < 1e-12, "half the width must equal the margin of error"
    assert abs((high - low) - 2 * me) < 1e-12, "the full width is twice the margin of error"
    return z, se, me, (low, high)


def observed_counts_ok(successes, n):
    """EK 3.3.B.1.iii: the OBSERVED counts, not expected ones."""
    return successes >= 10 and (n - successes) >= 10


# --- critical values ---------------------------------------------------------------
c.check(8, z_star(0.95), tol=0.002)          # 1.960
c.check(9, z_star(0.90), tol=0.002)          # 1.645
c.check(10, z_star(0.99), tol=0.002)         # 2.576
assert z_star(0.90) < z_star(0.95) < z_star(0.99), (
    "a higher confidence level requires a larger critical value")

# --- 140 of 400 adults, 95% ---------------------------------------------------------
phat_a = 140 / 400
assert phat_a == 0.35
c.check(6, phat_a)                           # 0.35
assert observed_counts_ok(140, 400), "140 successes and 260 failures both exceed 10"
assert (140, 400 - 140) == (140, 260)

z_a, se_a, me_a, ci_a = z_interval(phat_a, 400, 0.95)
c.check(7, se_a, tol=0.005)                  # 0.0238
c.check(11, me_a, tol=0.005)                 # 0.0467
c.check(12, list(ci_a), tol=0.005)           # (0.3033, 0.3967)
assert abs((ci_a[1] - ci_a[0]) - 0.0935) < 0.001, (
    "q11: 0.0935 is the full width, offered as a distractor against the margin of error")
assert abs(se_a - me_a) > 0.01, (
    "q7: the standard error and the margin of error must be visibly different numbers")

# --- 300 of 500 voters, 90% ----------------------------------------------------------
phat_b = 300 / 500
assert phat_b == 0.60
z_b, se_b, me_b, ci_b = z_interval(phat_b, 500, 0.90)
c.check(13, se_b, tol=0.005)                 # 0.0219
c.check(14, list(ci_b), tol=0.005)           # (0.5640, 0.6360)
assert observed_counts_ok(300, 500)

# --- 160 of 250 items, 99% -----------------------------------------------------------
phat_c = 160 / 250
assert phat_c == 0.64
z_c, se_c, me_c, ci_c = z_interval(phat_c, 250, 0.99)
c.check(15, list(ci_c), tol=0.005)           # (0.5618, 0.7182)
assert observed_counts_ok(160, 250)


def confidence_and_n_move_the_width():
    """q18, q19, q20, q25: which input changes what."""
    # q18: raising the confidence level widens the interval; the SE is unchanged.
    _, se_low, me_low, ci_low = z_interval(0.5, 400, 0.90)
    _, se_high, me_high, ci_high = z_interval(0.5, 400, 0.99)
    assert abs(se_low - se_high) < 1e-15, "the standard error does not depend on the confidence level"
    assert me_high > me_low and (ci_high[1] - ci_high[0]) > (ci_low[1] - ci_low[0])

    # q19: raising n narrows the interval; the critical value is unchanged.
    z_small, se_small, _, ci_small = z_interval(0.5, 100, 0.95)
    z_big, se_big, _, ci_big = z_interval(0.5, 900, 0.95)
    assert z_small == z_big, "the critical value does not depend on n"
    assert se_big < se_small
    assert (ci_big[1] - ci_big[0]) < (ci_small[1] - ci_small[0])

    # q20 and q25: the margin of error scales as 1/sqrt(n).
    _, _, me_200, _ = z_interval(0.5, 200, 0.95)
    _, _, me_800, _ = z_interval(0.5, 800, 0.95)
    assert abs(me_200 / me_800 - 2.0) < 1e-9, "quadrupling n halves the margin of error"
    _, _, me_4n, _ = z_interval(0.5, 4 * 200, 0.95)
    assert abs(me_4n - me_200 / 2) < 1e-12


confidence_and_n_move_the_width()
c.check(20, 4)                               # multiply n by 4 to halve the margin of error


def sample_size_rounds_up():
    """q21, q23: the rounding direction is the whole point."""
    z = z_star(0.95)
    target = 0.03
    exact = (z / target) ** 2 * 0.25
    assert abs(exact - 1067.07) < 0.05, f"the exact requirement is {exact:.4f}"

    def me_at(n):
        return z * math.sqrt(0.25 / n)

    assert me_at(1067) > target, (
        "rounding DOWN leaves the margin of error above the requirement")
    assert me_at(1068) <= target, "rounding up satisfies it"
    c.check(21, math.ceil(exact))            # 1068

    # q23: the same rule applied to a stated 546.2.
    assert math.ceil(546.2) == 547
    # A tight tolerance here: the distractors 546 and 546.2 are deliberately
    # within one unit of the key, since the item is about rounding direction.
    c.check(23, math.ceil(546.2), tol=1e-6)

    # q22: p* = 0.5 maximizes p(1-p) and so the required n.
    requirement = {p: (z / target) ** 2 * p * (1 - p)
                   for p in (0.1, 0.25, 0.5, 0.75, 0.9)}
    assert max(requirement, key=requirement.get) == 0.5, (
        "0.5 must give the largest requirement, which is what makes it conservative")
    assert requirement[0.5] >= max(requirement.values())


sample_size_rounds_up()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.3.A.1: estimating one population proportion with an interval calls for the one-sample z-interval.")
c.conceptual(2, "EK 3.3.A.1: a confidence interval is an interval estimate for a parameter, not a description of the sample.")
c.conceptual(3, "EK 3.3.B.1: the three conditions are randomization, the 10% condition and the observed-count normality check; nothing is assumed about the population's shape.")
c.conceptual(4, "EK 3.3.B.1.iii against 3.2.B.2: for an interval p is unknown, so the check uses the OBSERVED successes and failures rather than expected counts.")
c.conceptual(5, "EK 3.3.B.1.iii: computed above -- the observed counts are 140 and 260, both far above 10.")
c.conceptual(16, "EK 3.3.D.2: the standard error estimates the typical amount by which a statistic varies from the parameter.")
c.conceptual(17, "EK 3.3.D.3: verified above -- the margin of error is z* times the standard error and equals HALF the interval's width.")
c.conceptual(18, "EK 3.3.C.1: computed above -- the critical value rises from 1.645 to 2.576 while the standard error is unchanged, so the interval widens.")
c.conceptual(19, "EK 3.3.D.1: computed above -- the critical value is fixed by the confidence level, and it is the standard error that shrinks as n grows.")
c.conceptual(22, "EK 3.3.D.3: computed above -- p(1-p) peaks at 0.5, so using it gives the largest required n and guarantees the margin of error is not exceeded.")
c.conceptual(24, "EK 3.3.A.2: the parameter names the proportion, the response variable and the population, so it is about all adults in the city rather than the 400 sampled.")
c.conceptual(25, "EK 3.3.D.3: computed above -- quadrupling the sample size halves the margin of error and so halves the width.")

c.finish()
