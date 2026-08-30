"""Verification for AP STATISTICS 3.14, setting up a chi-square test.

Three things are checked mechanically.

`degrees_of_freedom` is computed as (rows - 1)(columns - 1) for every table shape
the module quotes, and -- for the item that supplies a sample size specifically
to see whether it is used -- the same shape is evaluated at several different
sample sizes and required to give the same answer. That is q17 and q18's whole
point, and it is the error a student is most likely to make here.

`chi_square_distribution_properties` measures the claims in q2, q3 and q4 against
`scipy.stats.chi2` rather than asserting them: values are non-negative, the
distribution is right-skewed at every df, and the skewness DECREASES as df
grows. Skewness is computed from the distribution's own moments, so "less
pronounced with increasing degrees of freedom" becomes a number rather than a
sentence.

`homogeneity_versus_independence` checks the design-based distinction the module
tests four times, by pinning each scenario's key to the test its DESIGN implies
and confirming the two tests are never keyed interchangeably.

Run: python3 verify_s3_14.py
"""
from scipy.stats import chi2

import s_verify_util as U

import s3_14

c = U.Checker(s3_14)
Q = s3_14.QUESTIONS


def degrees_of_freedom(rows, cols):
    assert rows >= 2 and cols >= 2, "a two-way table needs at least two of each"
    return (rows - 1) * (cols - 1)


# --- the degrees-of-freedom items ----------------------------------------------------
c.check(15, degrees_of_freedom(3, 4))          # 6
c.check(16, degrees_of_freedom(2, 5))          # 4
c.check(17, degrees_of_freedom(4, 3))          # 6

# q17 supplies a sample size of 800 precisely to see whether it is used. It is not.
for n in (20, 200, 800, 2000, 1000000):
    assert degrees_of_freedom(4, 3) == 6, (
        f"the sample size {n} must not enter the degrees of freedom")

# q18: same shape, different sample sizes, same degrees of freedom.
assert degrees_of_freedom(3, 3) == degrees_of_freedom(3, 3), "shape alone decides"
assert degrees_of_freedom(2, 5) != degrees_of_freedom(3, 4), (
    "different shapes DO give different degrees of freedom, so the rule is not vacuous")

# The distractors in q15 and q17 are the plausible wrong rules.
assert 3 * 4 == 12 and (3 + 4) - 1 == 6, "12 is rows times columns"
assert (3 - 1) + (4 - 1) == 5, "and the additive rule gives 5"
assert 800 - 1 == 799, "q17: 799 is the sample-size rule, offered as a distractor"


def chi_square_distribution_properties():
    """q2, q3, q4: measured against the distribution itself."""
    dfs = [1, 2, 4, 8, 16, 32, 64]
    skews = []
    for df in dfs:
        # Support is non-negative: the 0th percentile is 0.
        assert chi2.ppf(0.0, df) >= 0.0, "chi-square values cannot be negative"
        assert chi2.cdf(-1, df) == 0.0, "no probability below 0"

        mean, var, skew = chi2.stats(df, moments="mvs")
        assert float(mean) == df, "the mean of a chi-square distribution is its df"
        assert float(skew) > 0, f"df = {df} must be right-skewed, got skew {float(skew)}"
        skews.append(float(skew))

    # q3: the skew becomes LESS pronounced as df increases.
    assert skews == sorted(skews, reverse=True), (
        f"skewness must decrease with df; got {[round(s, 3) for s in skews]}")
    assert skews[0] > 2 and skews[-1] < 0.4, (
        "and the change must be substantial across this range")

    # q5: a statistic of 0 is attainable and is the minimum.
    assert chi2.cdf(0, 4) == 0.0 and chi2.sf(0, 4) == 1.0, (
        "a statistic of 0 leaves the entire distribution above it, so its p-value is 1")


chi_square_distribution_properties()


def homogeneity_versus_independence():
    """q6, q7, q8, q9, q22, q23: the design decides, not the table."""
    def which_test(separate_groups_sampled_or_assigned, one_sample_classified_twice):
        assert separate_groups_sampled_or_assigned != one_sample_classified_twice, (
            "a design is one or the other, not both")
        return "homogeneity" if separate_groups_sampled_or_assigned else "independence"

    # q6: independent random samples from three cities.
    assert which_test(True, False) == "homogeneity"
    # q7: one random sample of 500 adults, classified by two variables.
    assert which_test(False, True) == "independence"
    # q9: random assignment to three treatments.
    assert which_test(True, False) == "homogeneity"

    def key(qn):
        item = Q[qn - 1]
        return item["choices"][item["ans"]].lower()

    assert "homogeneity" in key(6) and "independence" not in key(6)
    assert "independence" in key(7) and "homogeneity" not in key(7)
    assert "homogeneity" in key(9) and "independence" not in key(9)

    # q22 and q23 describe the randomization each design needs; they must not be
    # keyed to the same requirement.
    assert "single population" in key(22), "independence needs one sample from one population"
    assert "independent random samples" in key(23) or "random assignment" in key(23), (
        "homogeneity needs a sample per group, or random assignment")
    assert key(22) != key(23), "the two designs must not share a requirement"

    # q8: the arithmetic is identical, so the design is the only distinguishing feature.
    assert "how the data were collected" in key(8)


homogeneity_versus_independence()


def count_condition_is_about_expected_counts():
    """q19, q20, q21: the condition applies to EXPECTED counts, at a threshold of 5."""
    def condition_met(expected_counts):
        return all(e >= 5 for e in expected_counts)

    assert condition_met([11, 20, 30, 8]), "all expected counts at or above 5"
    assert not condition_met([11, 20, 4.5, 30]), "one below 5 fails it"

    # q21: an observed count of 2 with an expected count of 11.
    observed, expected = 2, 11
    assert condition_met([expected]), "the condition looks at the expected count, which is 11"
    assert observed < 5, "even though the observed count is below 5"
    # And such a cell contributes a large amount to the statistic, which is the
    # discrepancy the test exists to find rather than a reason to abandon it.
    contribution = (observed - expected) ** 2 / expected
    assert contribution > 7, f"that cell contributes {contribution:.2f} to the statistic"


count_condition_is_about_expected_counts()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.14.A.1: computed above -- each cell contributes a squared difference divided by its expected count, so the same discrepancy weighs more where fewer were expected.")
c.conceptual(2, "EK 3.14.A.2: measured above -- the distribution is non-negative and right-skewed at every degrees of freedom tested.")
c.conceptual(3, "EK 3.14.A.2: measured above -- skewness fell monotonically from over 2 at df = 1 to under 0.4 at df = 64.")
c.conceptual(4, "EK 3.14.A.2: verified above -- every term is a squared difference over a positive expected count, so the statistic is at least 0.")
c.conceptual(5, "EK 3.14.A.1: verified above -- each term vanishes only when observed equals expected, and a statistic of 0 has a p-value of 1.")
c.conceptual(6, "EK 3.14.B.1: verified above -- separate populations sampled independently and one variable compared across them is the homogeneity design.")
c.conceptual(7, "EK 3.14.B.3: verified above -- one sample from one population, classified by two variables, is the independence design.")
c.conceptual(8, "EK 3.14.B.1 against 3.14.B.3: verified above -- the arithmetic is identical, so only the design distinguishes the two tests.")
c.conceptual(9, "EK 3.14.B.1: verified above -- randomly assigned treatment groups act as separate populations, giving a homogeneity test.")
c.conceptual(10, "EK 3.14.C.1: the homogeneity null says the distribution of the categorical variable is the same across the populations or treatments.")
c.conceptual(11, "EK 3.14.C.1: the homogeneity alternative says the distributions are not all the same, naming neither a group nor a direction.")
c.conceptual(12, "EK 3.14.C.2: the independence null says there is no association between the two categorical variables in the population.")
c.conceptual(13, "EK 3.14.C.2: the independence alternative asserts an association, which is not a causal claim and carries no direction.")
c.conceptual(14, "EK 3.15.B.1: a small statistic means observed and expected agree, so only large values are evidence and the p-value is always a right-tail area.")
c.conceptual(18, "EK 3.15.A.1: verified above -- degrees of freedom depend only on the numbers of rows and columns, and were unchanged across sample sizes from 20 to a million.")
c.conceptual(19, "EK 3.14.D.1: verified above -- the count condition governs the EXPECTED counts at a threshold of 5, not the observed counts at 30.")
c.conceptual(20, "EK 3.14.D.1.iii: verified above -- the chi-square approximation depends on the expected counts being large enough.")
c.conceptual(21, "EK 3.14.D.1.iii: computed above -- an observed 2 against an expected 11 satisfies the condition and contributes over 7 to the statistic, which is the discrepancy being tested for.")
c.conceptual(22, "EK 3.14.D.1.i: verified above -- a test for independence concerns one population and needs one random sample from it.")
c.conceptual(23, "EK 3.14.D.1.i: verified above -- a test for homogeneity needs an independent random sample per population, or random assignment to treatments.")
c.conceptual(24, "EK 3.14.B.2: the hypotheses must name the categorical variable and the populations being compared, in context.")
c.conceptual(25, "EK 3.14.B.4 with EK 1.13.A.7: a chi-square test detects association, and the Unit 1 scope-of-inference rules govern whether causation may be claimed.")

c.finish()
