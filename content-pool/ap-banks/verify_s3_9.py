"""Verification for AP STATISTICS 3.9, the difference between two sample proportions.

`sd_difference` implements the formula once -- the square root of the SUM of the
two variances -- and every keyed standard deviation comes from it.

Three checks are specific to this topic, and all three exist because the
add-versus-subtract question is where this material goes wrong:

* `variances_add_they_do_not_cancel` computes the correct value alongside the
  two wrong ones the module offers as distractors (subtracting the variances,
  and adding the standard deviations) and asserts the ORDERING among them --
  subtracting understates, adding standard deviations overstates. That ordering
  is a fact about square roots, so it is checked on many parameter pairs rather
  than on the one that happens to appear in a stem;

* the same function confirms the difference is MORE variable than either
  proportion alone, which is q8's key and the claim students find hardest;

* `conditions_check_all_four` evaluates the large counts condition on each of
  the four expected counts separately, so an item where exactly one of the four
  fails is confirmed to fail for the reason its key names.

Run: python3 verify_s3_9.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_9

c = U.Checker(s3_9)


def variance(p, n):
    return p * (1 - p) / n


def sd_difference(p1, n1, p2, n2):
    """sqrt(var1 + var2) -- the variances ADD."""
    total = variance(p1, n1) + variance(p2, n2)
    assert total > 0
    return math.sqrt(total)


# --- the three worked scenarios -----------------------------------------------------
c.check(4, 0.60 - 0.50)                                    # mean 0.10
c.check(5, sd_difference(0.60, 200, 0.50, 150), tol=0.002)  # 0.0535
c.check(6, sd_difference(0.40, 100, 0.30, 100), tol=0.002)  # 0.0671
c.check(7, [0.25 - 0.20, sd_difference(0.25, 400, 0.20, 500)], tol=0.005)  # 0.05, 0.0281
c.check(22, sd_difference(0.50, 100, 0.50, 100), tol=0.002)  # 0.0707


def variances_add_they_do_not_cancel():
    """q2, q3, q5, q8, q20, q21: the add-versus-subtract question, computed."""
    cases = [(0.60, 200, 0.50, 150), (0.40, 100, 0.30, 100),
             (0.25, 400, 0.20, 500), (0.50, 100, 0.50, 100),
             (0.80, 50, 0.20, 300)]

    for p1, n1, p2, n2 in cases:
        v1, v2 = variance(p1, n1), variance(p2, n2)
        correct = math.sqrt(v1 + v2)
        subtracted = math.sqrt(abs(v1 - v2))          # the q5 distractor
        added_sds = math.sqrt(v1) + math.sqrt(v2)     # the q21 error

        assert subtracted < correct, "subtracting the variances understates the variability"
        assert added_sds > correct, "adding the standard deviations overstates it"
        # q8: the difference is more variable than EITHER proportion alone.
        assert correct > math.sqrt(v1) and correct > math.sqrt(v2), (
            "the difference must vary more than either proportion on its own")

    # The specific distractor value quoted in q5's rationale.
    v1, v2 = variance(0.60, 200), variance(0.50, 150)
    assert abs(v1 - 0.0012) < 1e-9 and abs(v2 - 0.0016667) < 1e-6
    assert abs(math.sqrt(v1 + v2) - 0.0535) < 0.0005
    assert abs(math.sqrt(abs(v1 - v2)) - 0.0212) < 0.0005, (
        "0.0212 is the subtract-the-variances distractor")

    # q9/q10: equal parameters centre the difference at 0 but leave it variable.
    assert 0.5 - 0.5 == 0
    assert sd_difference(0.5, 100, 0.5, 100) > 0, (
        "equal proportions do not make the difference constant")


def conditions_check_all_four():
    """q12, q13, q14: four expected counts, checked one at a time."""
    def counts(p, n):
        return n * p, n * (1 - p)

    def all_four(p1, n1, p2, n2):
        return counts(p1, n1) + counts(p2, n2)

    four = all_four(0.60, 200, 0.50, 150)
    assert four == (120.0, 80.0, 75.0, 75.0), f"q13: counts are {four}"
    assert all(v >= 10 for v in four), "all four exceed 10"

    four = all_four(0.03, 250, 0.40, 250)
    assert four == (7.5, 242.5, 100.0, 150.0), f"q14: counts are {four}"
    failing = [v for v in four if v < 10]
    assert failing == [7.5], (
        "exactly one of the four counts must fail, which is what the key names")
    assert not all(v >= 10 for v in four)


def probabilities_of_the_difference():
    """q16, q17: normal probabilities for the difference."""
    mean = 0.60 - 0.50
    sd = sd_difference(0.60, 200, 0.50, 150)

    above = float(norm.sf(0.20, mean, sd))
    below_zero = float(norm.cdf(0.0, mean, sd))
    assert abs(above - 0.0309) < 0.0005, f"q16: computed {above:.4f}"
    assert abs(below_zero - 0.0309) < 0.0005, f"q17: computed {below_zero:.4f}"
    # They coincide here because 0 and 0.20 are equidistant from the mean of 0.10,
    # which is a property of the numbers chosen, not a general fact.
    assert abs((0.20 - mean) - (mean - 0.0)) < 1e-12
    c.check(16, above, tol=0.0005)
    c.check(17, below_zero, tol=0.0005)


def sample_size_narrows_it():
    """q18, q24: both sample sizes carry their own term."""
    base = sd_difference(0.60, 200, 0.50, 150)
    both = sd_difference(0.60, 800, 0.50, 600)
    one_only = sd_difference(0.60, 800, 0.50, 150)

    assert both < one_only < base, (
        "raising both helps most; raising only one leaves the other term untouched")
    assert abs(both - base / 2) < 1e-9, "quadrupling both halves the standard deviation"
    # The centre is untouched by either change.
    assert (0.60 - 0.50) == (0.60 - 0.50)


variances_add_they_do_not_cancel()
conditions_check_all_four()
probabilities_of_the_difference()
sample_size_narrows_it()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 3.D: the difference of two unbiased estimators is unbiased for the difference of the parameters.")
c.conceptual(2, "Skill 3.D: verified above -- variances of independent quantities add, so the sum is taken before the square root.")
c.conceptual(3, "Skill 3.D: verified above -- subtracting the variances understates the variability on every case tested.")
c.conceptual(8, "Skill 3.D: verified above -- the difference varies more than either proportion alone, on every case tested.")
c.conceptual(9, "Skill 3.D: computed above -- equal parameters put the centre at 0.")
c.conceptual(10, "Skill 3.D: computed above -- equal parameters still leave a positive standard deviation, which is why a test is needed.")
c.conceptual(11, "Skill 4.E: independence between the samples is what licenses adding the variances, and randomization is what makes each distribution behave as described.")
c.conceptual(12, "Skill 4.E: verified above -- the large counts condition is applied to each sample, giving four counts to check.")
c.conceptual(13, "Skill 4.E: computed above -- the four expected counts are 120, 80, 75 and 75, all above 10.")
c.conceptual(14, "Skill 4.E: computed above -- 7.5 is the only one of the four counts below 10, and one failure is enough.")
c.conceptual(15, "Skill 4.E: measurements on the same individuals are dependent by construction, so the variances may not simply be added.")
c.conceptual(18, "Skill 3.D: computed above -- both variances carry their own n, so raising both sample sizes narrows the distribution while the centre stays at p1 - p2.")
c.conceptual(19, "Skill 4.E: randomization and independence make the formulas apply, and the four large counts make the normal approximation trustworthy.")
c.conceptual(20, "Skill 3.D: verified above -- the sum is taken before the square root, since variances add and standard deviations do not.")
c.conceptual(21, "Skill 3.D: verified above -- adding the standard deviations overstates the variability on every case tested.")
c.conceptual(23, "Skill 3.D: reversing the order of subtraction negates the centre and leaves the standard deviation unchanged, since the variances add either way.")
c.conceptual(24, "Skill 3.D: computed above -- raising both sample sizes narrows the distribution more than raising only one.")
c.conceptual(25, "Skill 3.D: a sampling distribution describes how a statistic behaves across repeated sampling, not the data in one pair of samples.")

c.finish()
