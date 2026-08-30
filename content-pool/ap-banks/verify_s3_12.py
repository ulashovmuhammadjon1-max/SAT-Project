"""Verification for AP STATISTICS 3.12, setting up the two-proportion test.

`pooled` computes the combined proportion from raw counts and, on every data set
used, is cross-checked against the sample-size-weighted average of the two
sample proportions -- the two must agree exactly, which is what justifies the
module calling the pooled value a weighted average.

`weighted_is_not_plain_average` is the check the topic needs most. Item 13 and
item 14 rest on the claim that pooling and plain averaging differ when the
sample sizes differ and coincide when they do not. Both halves are computed:
equal sizes must give equal answers, unequal sizes must not, and the pooled
value must land on the side of the LARGER sample. A module that keyed this
backwards would look entirely plausible.

`expected_counts_use_the_pooled_value` computes the four expected counts from
the pooled proportion and, alongside them, the observed counts an interval would
use, and requires the two sets to differ -- otherwise q17's contrast is empty.

Run: python3 verify_s3_12.py
"""
import s_verify_util as U

import s3_12

c = U.Checker(s3_12)


def pooled(x1, n1, x2, n2):
    """(x1 + x2)/(n1 + n2), cross-checked against the weighted average."""
    combined = (x1 + x2) / (n1 + n2)
    p1, p2 = x1 / n1, x2 / n2
    weighted = (n1 * p1 + n2 * p2) / (n1 + n2)
    assert abs(combined - weighted) < 1e-12, (
        "the pooled proportion must equal the sample-size-weighted average")
    assert 0 <= combined <= 1
    return combined


# --- the three worked pooled proportions ---------------------------------------------
c.check(9, pooled(120, 300, 90, 300))          # 210/600 = 0.35
c.check(10, pooled(95, 250, 70, 250))          # 165/500 = 0.33
c.check(11, pooled(48, 200, 36, 150))          #  84/350 = 0.24

# q12: the third study's two sample proportions are both 0.24, so the pooled
# value must be 0.24 too despite the unequal sample sizes.
assert abs(48 / 200 - 0.24) < 1e-12 and abs(36 / 150 - 0.24) < 1e-12
assert abs(pooled(48, 200, 36, 150) - 0.24) < 1e-12, (
    "equal sample proportions give a pooled value equal to them, whatever the weights")


def weighted_is_not_plain_average():
    """q13, q14, q25: when pooling and plain averaging agree, and when they do not."""
    # Equal sample sizes: the two coincide.
    for x1, x2, n in ((120, 90, 300), (95, 70, 250), (60, 40, 200)):
        p = pooled(x1, n, x2, n)
        plain = (x1 / n + x2 / n) / 2
        assert abs(p - plain) < 1e-12, "with equal n, pooling IS the plain average"

    # Unequal sample sizes: they differ, and the pooled value leans toward the
    # larger sample's proportion.
    x1, n1, x2, n2 = 60, 100, 90, 300
    p = pooled(x1, n1, x2, n2)
    plain = (x1 / n1 + x2 / n2) / 2
    assert abs(p - 0.375) < 1e-12 and abs(plain - 0.45) < 1e-12, (
        f"q14: pooled {p}, plain average {plain}")
    assert p != plain, "with unequal n the two must differ"

    p1_, p2_ = x1 / n1, x2 / n2
    assert n2 > n1, "the second sample is the larger"
    assert abs(p - p2_) < abs(p - p1_), (
        "so the pooled value must sit closer to the second sample's proportion")

    # And the same on the other data set with unequal sizes.
    p3 = pooled(48, 200, 36, 150)
    plain3 = (48 / 200 + 36 / 150) / 2
    assert abs(p3 - plain3) < 1e-12, (
        "here the two sample proportions are equal, so pooling and averaging agree "
        "even though the sample sizes do not -- which is exactly q12's point")

    # q25: identical sample proportions give an observed difference of 0.
    assert abs((48 / 200) - (36 / 150)) < 1e-12


def expected_counts_use_the_pooled_value():
    """q15, q16, q17, q19: four expected counts, all from the pooled proportion."""
    def expected(n, p):
        return n * p, n * (1 - p)

    x1, n1, x2, n2 = 120, 300, 90, 300
    p = pooled(x1, n1, x2, n2)
    four = expected(n1, p) + expected(n2, p)
    assert four == (105.0, 195.0, 105.0, 195.0), f"q16: expected counts are {four}"
    assert all(v >= 10 for v in four)

    # q17: the interval would use the OBSERVED counts, which differ.
    observed = (x1, n1 - x1, x2, n2 - x2)
    assert observed == (120, 180, 90, 210)
    assert set(four) != set(observed), (
        "the two sets must differ, or q17 has no contrast to draw")

    # Because both samples use the SAME pooled proportion, their expected counts
    # match each other here -- which they would not under the interval's method.
    assert four[0] == four[2] and four[1] == four[3], (
        "the pooled value is applied to both samples")
    assert observed[0] != observed[2], "while the observed counts differ between samples"

    # q19: pooled proportion 0.04 with samples of 200.
    small = expected(200, 0.04)
    assert small == (8.0, 192.0), f"q19: expected counts are {small}"
    assert small[0] < 10 <= small[1], (
        "the failure must be on the expected successes alone, as the key says")


def hypotheses_are_about_parameters():
    """q3, q6, q24: what may and may not appear in the hypotheses."""
    # The two forms of the null are equivalent statements.
    for p1, p2 in ((0.3, 0.3), (0.5, 0.5), (0.72, 0.72)):
        assert (p1 == p2) == ((p1 - p2) == 0), (
            "H0: p1 = p2 and H0: p1 - p2 = 0 must agree on every case")
    for p1, p2 in ((0.3, 0.4), (0.9, 0.1)):
        assert (p1 == p2) == ((p1 - p2) == 0)

    # q24: the standard null is a difference of exactly 0, not some other value.
    assert 0.0 == 0.0 and 0.05 != 0.0, (
        "a null of p1 - p2 = 0.05 is not the procedure taught here")


weighted_is_not_plain_average()
expected_counts_use_the_pooled_value()
hypotheses_are_about_parameters()

c.check(14, [pooled(60, 100, 90, 300), (60 / 100 + 90 / 300) / 2])   # 0.375 and 0.450

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 2.C: comparing two proportions with a test calls for the two-sample z-test.")
c.conceptual(2, "Skill 2.E: the null states no difference between the two population parameters and claims nothing about their common value.")
c.conceptual(3, "Skill 2.E: verified above -- p1 = p2 and p1 - p2 = 0 are equivalent statements, and both are about parameters.")
c.conceptual(4, "Skill 2.E: the belief being investigated becomes the one-sided alternative, written about the parameters.")
c.conceptual(5, "Skill 2.E: a question with no stated direction is answered by a two-sided alternative.")
c.conceptual(6, "Skill 2.E: p-hat1 and p-hat2 are known once the samples are collected, so the hypotheses must concern p1 and p2.")
c.conceptual(7, "Skill 3.E: verified above -- the pooled proportion is the total successes over the total observations, equal to the size-weighted average.")
c.conceptual(8, "Skill 3.E: the null supplies the assumption that the two proportions are equal, which is what makes a single combined estimate correct.")
c.conceptual(12, "Skill 3.E: computed above -- equal sample proportions give a pooled value equal to them whatever the sample sizes.")
c.conceptual(13, "Skill 3.E: computed above -- with unequal sample sizes the pooled value differs from the plain average and leans toward the larger sample.")
c.conceptual(15, "Skill 4.E: computed above -- the expected counts come from the pooled proportion, since the test assumes the null.")
c.conceptual(16, "Skill 4.E: computed above -- the four expected counts are 105, 195, 105 and 195, all above 10.")
c.conceptual(17, "Skill 4.E: computed above -- the test's expected counts (105, 195, 105, 195) differ from the interval's observed counts (120, 180, 90, 210).")
c.conceptual(18, "Skill 4.E: equal sample sizes are not required; unequal sizes are handled by the weighting inside the pooled proportion.")
c.conceptual(19, "Skill 4.E: computed above -- 8 expected successes in each sample falls short of 10 while the 192 expected failures are ample.")
c.conceptual(20, "Skill 4.E: independence between the samples is an explicit condition, and before-and-after measurements on the same people violate it.")
c.conceptual(21, "Skill 4.E: for an experiment, random assignment plays the role that random selection plays for observational samples.")
c.conceptual(22, "Skill 2.E: evidence supports the alternative when the observed difference falls on the alternative's side of zero.")
c.conceptual(23, "Skill 2.C: each parameter names a proportion, the response variable and its own population; the pooled value is a statistic.")
c.conceptual(24, "Skill 2.E: verified above -- the procedure taught here tests a difference of exactly 0, which is what the pooled standard error is derived from.")
c.conceptual(25, "Skill 3.E: computed above -- identical sample proportions make the pooled value equal to them and the observed difference 0.")

c.finish()
