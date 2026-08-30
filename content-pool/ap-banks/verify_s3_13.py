"""Verification for AP STATISTICS 3.13, carrying out the two-proportion test.

`two_proportion_test` runs the procedure end to end from the four raw counts, so
the pooled proportion, standard error, test statistic and p-value in each
scenario all come from one derivation.

Three checks are specific to this topic.

`pooled_versus_unpooled_in_a_test` computes the statistic both ways for the same
data. The two standard errors differ by about 0.0002 on this data, so the
resulting statistics are very close -- which is precisely why q18 asks about the
DIRECTION of the error rather than offering the wrong value as a numeric choice.
The check pins that direction: the unpooled denominator is smaller here, so the
mistaken statistic is larger.

`zero_difference_gives_p_of_one` verifies the fourth scenario exactly. Both
sample proportions are 0.24, so the statistic is exactly 0 and the two-sided
p-value is exactly 1 -- not approximately. That is worth asserting exactly,
because a p-value of 1 is the kind of result an author might "correct" to 0.5.

`reversing_the_groups` confirms the sign flips, the magnitude does not, and the
two-sided p-value is untouched.

Run: python3 verify_s3_13.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_13

c = U.Checker(s3_13)


def two_proportion_test(x1, n1, x2, n2, alternative):
    p1, p2 = x1 / n1, x2 / n2
    pc = (x1 + x2) / (n1 + n2)
    se = math.sqrt(pc * (1 - pc) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    if alternative == "greater":
        p = float(norm.sf(z))
    elif alternative == "less":
        p = float(norm.cdf(z))
    elif alternative == "two-sided":
        p = 2 * float(norm.sf(abs(z)))
    else:
        raise AssertionError(alternative)
    assert 0 <= p <= 1, f"a p-value must lie in [0, 1]; got {p}"
    return p1, p2, pc, se, z, p


def reject(p, alpha):
    return p <= alpha


# --- study 1: 120/300 vs 90/300, two-sided ------------------------------------------
p1, p2, pc1, se1, z1, pv1 = two_proportion_test(120, 300, 90, 300, "two-sided")
assert (p1, p2) == (0.40, 0.30) and abs(pc1 - 0.35) < 1e-12
c.check(3, se1, tol=0.0005)                 # 0.0389
c.check(4, z1, tol=0.002)                   # 2.568
c.check(5, pv1, tol=0.0005)                 # 0.0102
assert reject(pv1, 0.05), "q6: 0.0102 is below 0.05"
assert p1 > p2, "and the observed difference is positive"

# --- study 2: 95/250 vs 70/250, one-sided -------------------------------------------
p1b, p2b, pc2, se2, z2, pv2 = two_proportion_test(95, 250, 70, 250, "greater")
assert abs(p1b - 0.38) < 1e-12 and abs(p2b - 0.28) < 1e-12
# Tight: the 0.0431 distractor sits only 0.001 from the key.
c.check(7, [pc2, se2], tol=0.0005)          # 0.3300 and 0.0421
c.check(8, z2, tol=0.002)                   # 2.378
c.check(9, pv2, tol=0.0005)                 # 0.0087
assert reject(pv2, 0.01), "q10: 0.0087 is below even 0.01"

# --- study 3: 140/400 vs 120/400, the near miss --------------------------------------
p1c, p2c, pc3, se3, z3, pv3 = two_proportion_test(140, 400, 120, 400, "greater")
assert abs(pc3 - 0.325) < 1e-12
c.check(11, z3, tol=0.002)                  # 1.510
c.check(12, pv3, tol=0.0005)                # 0.0656
assert not reject(pv3, 0.05), "q13: 0.0656 exceeds 0.05"
assert reject(pv3, 0.10), "q14: but it is below 0.10"
assert reject(pv3, 0.10) != reject(pv3, 0.05), (
    "q13 and q14 exist to show the same data giving opposite decisions")


def zero_difference_gives_p_of_one():
    """q15, q16, q17: identical sample proportions, exactly."""
    p1_, p2_, pc_, se_, z_, pv_ = two_proportion_test(48, 200, 36, 150, "two-sided")
    assert abs(p1_ - 0.24) < 1e-12 and abs(p2_ - 0.24) < 1e-12, (
        "both sample proportions must be exactly 0.24")
    assert p1_ == p2_, "so the observed difference is exactly 0"
    assert abs(z_) < 1e-12, f"the statistic must be exactly 0, got {z_}"
    assert abs(pv_ - 1.0) < 1e-12, f"the two-sided p-value must be exactly 1, got {pv_}"
    assert se_ > 0, "and this holds regardless of the standard error, which is positive"
    c.check(15, z_)                          # 0.000
    c.check(16, pv_)                         # 1.0000

    # A p-value of 1 is the maximum possible, not an error.
    assert pv_ >= two_proportion_test(120, 300, 90, 300, "two-sided")[5]


def pooled_versus_unpooled_in_a_test():
    """q2, q18: the direction of the error, since its size is negligible."""
    x1, n1, x2, n2 = 120, 300, 90, 300
    p1_, p2_ = x1 / n1, x2 / n2
    pc = (x1 + x2) / (n1 + n2)

    pooled_se = math.sqrt(pc * (1 - pc) * (1 / n1 + 1 / n2))
    unpooled_se = math.sqrt(p1_ * (1 - p1_) / n1 + p2_ * (1 - p2_) / n2)

    assert abs(pooled_se - 0.0389) < 0.0002 and abs(unpooled_se - 0.0387) < 0.0002, (
        f"pooled {pooled_se:.5f}, unpooled {unpooled_se:.5f}")
    assert unpooled_se < pooled_se, "here the unpooled denominator is the smaller"
    z_pooled = (p1_ - p2_) / pooled_se
    z_unpooled = (p1_ - p2_) / unpooled_se
    assert z_unpooled > z_pooled, (
        "so the mistaken statistic comes out LARGER, which is what q18 keys")
    assert abs(z_unpooled - z_pooled) < 0.05, (
        "and the difference is small, which is why the item asks for a direction "
        "rather than offering the wrong value as a numeric choice")


def reversing_the_groups():
    """q19, q20: sign flips, magnitude and two-sided p-value do not."""
    forward = two_proportion_test(120, 300, 90, 300, "two-sided")
    backward = two_proportion_test(90, 300, 120, 300, "two-sided")

    assert abs(forward[4] + backward[4]) < 1e-12, "the statistics must be negatives"
    assert abs(abs(forward[4]) - abs(backward[4])) < 1e-12, "with equal magnitude"
    assert abs(forward[2] - backward[2]) < 1e-12, "the pooled proportion is unchanged"
    assert abs(forward[3] - backward[3]) < 1e-12, "and so is the standard error"
    assert abs(forward[5] - backward[5]) < 1e-12, "so the two-sided p-value is identical"

    # A one-sided p-value, by contrast, does change -- which is why the key says
    # a one-sided alternative must be relabelled to match.
    fwd_one = two_proportion_test(120, 300, 90, 300, "greater")[5]
    bwd_one = two_proportion_test(90, 300, 120, 300, "greater")[5]
    assert abs(fwd_one - bwd_one) > 0.5, "the one-sided p-value flips to the other tail"


def sample_size_doubles_the_statistic():
    """q23: same proportions, four times the data, twice the statistic."""
    small = two_proportion_test(120, 300, 90, 300, "two-sided")
    big = two_proportion_test(480, 1200, 360, 1200, "two-sided")
    assert (small[0], small[1]) == (big[0], big[1]), "the sample proportions must match"
    assert abs(big[4] / small[4] - 2.0) < 1e-9, "the statistic must double"
    assert big[5] < small[5], "and the p-value must fall"


def test_and_interval_broadly_agree():
    """q24: a rejected null generally goes with an interval excluding 0."""
    x1, n1, x2, n2 = 120, 300, 90, 300
    _, _, _, _, _, pv = two_proportion_test(x1, n1, x2, n2, "two-sided")
    assert reject(pv, 0.05)

    p1_, p2_ = x1 / n1, x2 / n2
    se = math.sqrt(p1_ * (1 - p1_) / n1 + p2_ * (1 - p2_) / n2)
    z_star = float(norm.ppf(0.975))
    low, high = (p1_ - p2_) - z_star * se, (p1_ - p2_) + z_star * se
    assert not (low <= 0 <= high), "and the matching 95% interval excludes 0"

    # The two standard errors differ, so agreement is general, not exact.
    pc = (x1 + x2) / (n1 + n2)
    assert abs(se - math.sqrt(pc * (1 - pc) * (1 / n1 + 1 / n2))) > 1e-9


zero_difference_gives_p_of_one()
pooled_versus_unpooled_in_a_test()
reversing_the_groups()
sample_size_doubles_the_statistic()
test_and_interval_broadly_agree()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 3.E: the numerator is the observed difference of the sample proportions, measured against the 0 the null predicts.")
c.conceptual(2, "Skill 3.E: computed above -- the denominator uses the pooled proportion, since the null asserts a single common value.")
c.conceptual(6, "Skill 4.G: computed above -- 0.0102 falls below 0.05 with a positive observed difference.")
c.conceptual(10, "Skill 4.G: computed above -- 0.0087 falls below even the 1% standard.")
c.conceptual(13, "Skill 4.G: computed above -- 0.0656 exceeds 0.05, so the null is not rejected at that level.")
c.conceptual(14, "Skill 4.G: computed above -- the same 0.0656 falls below 0.10, so the decision reverses with the significance level.")
c.conceptual(17, "Skill 4.F: computed above -- a two-sided p-value of exactly 1 means the data are as unsurprising as possible under the null, not that the null is proved.")
c.conceptual(18, "Skill 3.E: computed above -- the unpooled denominator is smaller here, so the mistaken statistic is larger, though the method is wrong regardless of the size of the effect.")
c.conceptual(19, "Skill 3.E: computed above -- reversing the groups negates the statistic and leaves its magnitude and the standard error unchanged.")
c.conceptual(20, "Skill 3.E: computed above -- a two-sided p-value depends only on the magnitude, so it is identical either way round.")
c.conceptual(21, "Skill 4.G: a conclusion names the decision, the p-value against alpha, and what the evidence says about the two populations in context.")
c.conceptual(22, "Skill 4.G with EK 1.13.A.7: random assignment supports the causal claim, for subjects like those studied.")
c.conceptual(23, "Skill 3.E: computed above -- quadrupling both sample sizes halves the standard error and doubles the statistic.")
c.conceptual(24, "Skill 3.E: computed above -- the rejected null goes with an interval excluding 0, though the two use different standard errors so agreement is general.")
c.conceptual(25, "Skill 4.E: the p-value is an area under a normal null distribution, which is only correct when the conditions hold.")

c.finish()
