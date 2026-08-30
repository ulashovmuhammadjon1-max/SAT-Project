"""Verification for AP STATISTICS 3.7, carrying out a test for a proportion.

`z_test` runs the whole procedure from the raw counts -- p-hat, the null
standard deviation, the test statistic, the p-value in the alternative's
direction -- so every keyed number in a scenario comes from one derivation
rather than from four separate ones that might disagree.

The check this topic most needs is `wrong_denominator_is_a_distractor`. The
characteristic error here is standardizing with p-hat instead of p0, and the
module offers the resulting value as a distractor in q5 and describes it in q20.
The verifier computes BOTH statistics for the same data and asserts that they
are close but distinct -- close enough that a student would not notice by eye,
which is what makes the item worth asking, and distinct enough that the keyed
choice is unambiguous.

Every decision item is evaluated through one `reject` predicate, and q13 and q16
are confirmed to be cases where the p-value exceeds alpha only narrowly, since
those items exist to show that a near miss is still a miss.

Run: python3 verify_s3_7.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_7

c = U.Checker(s3_7)


def z_test(successes, n, p0, alternative):
    """The full one-sample z-test for a proportion, from the counts up."""
    phat = successes / n
    sd_null = math.sqrt(p0 * (1 - p0) / n)
    z = (phat - p0) / sd_null
    if alternative == "greater":
        p = float(norm.sf(z))
    elif alternative == "less":
        p = float(norm.cdf(z))
    elif alternative == "two-sided":
        p = 2 * float(norm.sf(abs(z)))
    else:
        raise AssertionError(alternative)
    assert 0 <= p <= 1
    return phat, sd_null, z, p


def reject(p, alpha):
    return p <= alpha


# --- scenario A: 92 of 200, H0 p = 0.40, Ha p > 0.40 --------------------------------
phat_a, sd_a, z_a, p_a = z_test(92, 200, 0.40, "greater")
# The distractors in this topic are deliberately near-misses -- each is the
# value the wrong-denominator error produces -- so the tolerances are tight
# enough that the mistaken value cannot also match the key.
c.check(3, phat_a)                          # 0.46
c.check(4, sd_a, tol=0.0002)                # 0.0346 against the wrong 0.0352
c.check(5, z_a, tol=0.002)                  # 1.732 against the wrong 1.703
c.check(6, p_a, tol=0.001)                  # 0.0416
assert reject(p_a, 0.05), "q7: 0.0416 is below 0.05"

# --- scenario B: 178 of 400, H0 p = 0.50, two-sided ---------------------------------
phat_b, sd_b, z_b, p_b = z_test(178, 400, 0.50, "two-sided")
assert abs(phat_b - 0.445) < 1e-12 and abs(sd_b - 0.025) < 1e-12
c.check(8, z_b, tol=0.002)                  # -2.200 against the wrong -2.209
c.check(9, p_b, tol=0.001)                  # 0.0278
assert abs(p_b - 2 * float(norm.cdf(z_b))) < 1e-12, "the two-sided p-value doubles one tail"
assert reject(p_b, 0.05), "q10: 0.0278 is below 0.05"

# --- scenario C: 63 of 300, H0 p = 0.25, Ha p < 0.25 --------------------------------
phat_c, sd_c, z_c, p_c = z_test(63, 300, 0.25, "less")
assert abs(phat_c - 0.21) < 1e-12 and abs(sd_c - 0.025) < 1e-12
c.check(11, z_c, tol=0.002)                 # -1.600 against the wrong -1.643
c.check(12, p_c, tol=0.001)                 # 0.0548
assert not reject(p_c, 0.05), "q13: 0.0548 exceeds 0.05, so the null is NOT rejected"
assert 0.05 < p_c < 0.06, (
    "q13 exists to show a NARROW miss, so the p-value must sit just above alpha")

# --- scenario D: 340 of 500, H0 p = 0.65, Ha p > 0.65 -------------------------------
phat_d, sd_d, z_d, p_d = z_test(340, 500, 0.65, "greater")
assert abs(phat_d - 0.68) < 1e-12
c.check(14, z_d, tol=0.002)                 # 1.406 against the wrong 1.398
c.check(15, p_d, tol=0.001)                 # 0.0798
assert not reject(p_d, 0.05), "q16: 0.0798 exceeds 0.05"


def wrong_denominator_is_a_distractor():
    """q5 and q20: standardizing with p-hat instead of p0.

    Both statistics are computed for the same data. They must be CLOSE, since
    that is what makes the error hard to spot, and DISTINCT, since the module
    offers one as the key and the other as a distractor.
    """
    successes, n, p0 = 92, 200, 0.40
    phat = successes / n

    correct_sd = math.sqrt(p0 * (1 - p0) / n)
    wrong_sd = math.sqrt(phat * (1 - phat) / n)
    correct_z = (phat - p0) / correct_sd
    wrong_z = (phat - p0) / wrong_sd

    assert abs(correct_sd - 0.0346) < 0.0005 and abs(wrong_sd - 0.0352) < 0.0005, (
        f"standard deviations are {correct_sd:.4f} and {wrong_sd:.4f}")
    assert wrong_sd > correct_sd, (
        "p-hat here is further from 0.5 than p0 is... no: 0.46 is CLOSER to 0.5 than 0.40, "
        "so p-hat(1-p-hat) is the larger product and the wrong denominator is bigger")
    assert phat * (1 - phat) > p0 * (1 - p0), "which is why the wrong denominator is larger"
    assert wrong_z < correct_z, "so the mistaken statistic comes out smaller"
    assert abs(correct_z - 1.732) < 0.005 and abs(wrong_z - 1.703) < 0.005, (
        f"statistics are {correct_z:.4f} and {wrong_z:.4f}")
    assert 0.01 < abs(correct_z - wrong_z) < 0.10, (
        "the two must be close enough to be a plausible error and far enough apart to key")

    # The same error on scenario D, to confirm it is not an accident of one data set.
    phat_d2 = 340 / 500
    w = (phat_d2 - 0.65) / math.sqrt(phat_d2 * (1 - phat_d2) / 500)
    correct = (phat_d2 - 0.65) / math.sqrt(0.65 * 0.35 / 500)
    assert abs(w - correct) > 0.001 and abs(w - correct) < 0.1


wrong_denominator_is_a_distractor()


def sample_size_scales_the_statistic():
    """q23: same p-hat, nine times the sample, three times the statistic."""
    _, sd_small, z_small, p_small = z_test(46, 100, 0.40, "greater")
    _, sd_big, z_big, p_big = z_test(414, 900, 0.40, "greater")
    assert abs(46 / 100 - 414 / 900) < 1e-12, "both samples must give p-hat = 0.46"
    assert abs(sd_small / sd_big - 3.0) < 1e-9, "the standard deviation falls by a factor of 3"
    assert abs(z_big / z_small - 3.0) < 1e-9, "so the statistic grows by a factor of 3"
    assert p_big < p_small, "and the p-value falls"


def zero_statistic():
    """q24: z = 0 exactly when p-hat equals p0."""
    _, _, z, p = z_test(80, 200, 0.40, "greater")
    assert 80 / 200 == 0.40
    assert abs(z) < 1e-12, "matching the null value gives a statistic of 0"
    assert abs(p - 0.5) < 1e-12, "and a one-sided p-value of exactly one half"


def interval_and_test_broadly_agree():
    """q25: a value rejected by the two-sided test generally falls outside the interval.

    'Generally' is the right word and the item says so: the test standardizes
    with p0 and the interval with p-hat, so the two do not agree exactly for
    proportions. Both facts are checked here.
    """
    successes, n, p0 = 178, 400, 0.50
    phat = successes / n
    _, _, _, p = z_test(successes, n, p0, "two-sided")
    assert reject(p, 0.05), "the test rejects p0 = 0.50 at the 5% level"

    z_star = float(norm.ppf(0.975))
    se_interval = math.sqrt(phat * (1 - phat) / n)
    low, high = phat - z_star * se_interval, phat + z_star * se_interval
    assert not (low <= p0 <= high), "and 0.50 falls outside the 95% interval, as expected"

    # But the two standard errors genuinely differ, so exact agreement is not
    # guaranteed -- which is why the key says "generally".
    se_test = math.sqrt(p0 * (1 - p0) / n)
    assert abs(se_test - se_interval) > 1e-6, (
        "the test and interval use different standard errors")


sample_size_scales_the_statistic()
zero_statistic()
interval_and_test_broadly_agree()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 3.E: a test statistic is the distance from the hypothesized value measured in standard deviations of the null distribution.")
c.conceptual(2, "Skill 3.E: computed above -- the denominator uses p0 because a test assumes H0; an interval has no such value and must use p-hat.")
c.conceptual(7, "Skill 4.G: computed above -- the p-value 0.0416 falls below alpha = 0.05, so H0 is rejected.")
c.conceptual(10, "Skill 4.G: computed above -- 0.0278 falls below 0.05, giving convincing evidence that p differs from 0.50.")
c.conceptual(13, "Skill 4.G: computed above -- 0.0548 exceeds 0.05, so however narrow the miss, the null is not rejected.")
c.conceptual(16, "Skill 4.G: computed above -- 0.0798 exceeds 0.05, so the data are not surprising enough under the null.")
c.conceptual(17, "Skill 4.G: a conclusion states the decision, the p-value against alpha, and the evidence about the alternative in context.")
c.conceptual(18, "Skill 4.G: the correct conclusion compares p-value with alpha, states the decision, and names the population, without claiming proof.")
c.conceptual(19, "Skill 4.G: failing to reject leaves the claim unestablished in either direction, which is why 'accept H0' is never used.")
c.conceptual(20, "Skill 3.E: computed above -- using p-hat gives a denominator of 0.0352 instead of 0.0346 and a statistic of 1.703 instead of 1.732.")
c.conceptual(21, "Skill 4.G with EK 3.6.A.1: rejecting at alpha = 0.05 means the result would occur less than 5% of the time under the null, not that the null is disproved.")
c.conceptual(22, "EK 3.5.C.1: the p-value is an area under a normal null distribution, which is only the correct distribution when the conditions hold.")
c.conceptual(23, "Skill 3.E: computed above -- nine times the sample size divides the standard deviation by 3 and so triples the statistic.")
c.conceptual(24, "Skill 3.E: computed above -- p-hat equal to p0 gives z = 0 and a one-sided p-value of exactly 0.5, the least surprising possible result.")
c.conceptual(25, "Skill 3.E: computed above -- the rejected value falls outside the interval, though the two use different standard errors so agreement is general rather than exact.")

c.finish()
