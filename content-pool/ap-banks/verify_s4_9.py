"""Verify AP Statistics 4.9 Setting Up a Two-Sample Test for Two Means.

This topic sets a test up rather than carrying it out, so most items are
conceptual and each records the CED rule that fixes its key. What IS numeric --
the degrees-of-freedom bracket and every 10 percent-condition threshold -- is
computed here.

Distribution: Student's t. CED 4.10.A.1 says technology supplies the df and
that it lies between the smaller of n1 - 1 and n2 - 1 (the conservative value)
and n1 + n2 - 2. Both ends are computed for q9 and q23.
"""
import s4_9
from s_verify_util import Checker

c = Checker(s4_9)


def df_bracket(n1, n2):
    """CED 4.10.A.1: (conservative lower end, pooled upper end)."""
    return min(n1, n2) - 1, n1 + n2 - 2


def ten_percent_ok(n, N):
    return n <= 0.10 * N


# q9, q23 -- the degrees-of-freedom bracket
lo9, hi9 = df_bracket(18, 22)
assert (lo9, hi9) == (17, 38)
c.check(9, [lo9, hi9])
lo23, hi23 = df_bracket(30, 40)
assert (lo23, hi23) == (29, 68)
c.check(23, [hi23, lo23])

# q6 -- the 10 percent condition, one sample failing and one passing
assert not ten_percent_ok(90, 800) and ten_percent_ok(70, 1200)
assert 0.10 * 800 == 80.0 and 0.10 * 1200 == 120.0
c.conceptual(6, "0.10 x 800 = 80 and the student sample of 90 exceeds it, so that one fails; "
                "0.10 x 1,200 = 120 and the teacher sample of 70 is well inside it. Exactly "
                "one of the two fails, so only one option can be true")

# q17 -- both samples comfortably inside the 10 percent limit
assert ten_percent_ok(45, 5000) and ten_percent_ok(50, 6000) and 45 >= 30 and 50 >= 30
c.conceptual(17, "0.10 x 5,000 = 500 and 0.10 x 6,000 = 600, so 45 and 50 are far inside the "
                 "limit, and both sample sizes reach 30; all three conditions hold")

# --- conceptual items, with the CED rule that fixes each key -----------------
c.conceptual(1, "'differ' is two-sided, and CED 4.9.B.1 writes H0: mu1 = mu2 with "
                "Ha: mu1 != mu2 about the POPULATION means; mu_d is the parameter of a "
                "matched-pairs design, which this is not")
c.conceptual(2, "CED 4.9.A.1: two independent samples with unknown sigmas is the two-sample "
                "t-test. The one-sample mean-difference test is for matched pairs, z requires "
                "known sigmas, and pooling estimates a single combined mean instead")
c.conceptual(3, "'higher mean improvement for the drug' with the drug as population 1 is the "
                "one-sided Ha: mu1 > mu2; the sample means never appear in a hypothesis, and "
                "mu1 - mu2 = 0 is the null, not an alternative")
c.conceptual(4, "the same 40 patients supply both measurements, so the two sets are dependent "
                "and the two-sample procedure's independence assumption fails; CED 4.4.A.2 "
                "sends this to a one-sample t-test on the 40 differences")
c.conceptual(5, "CED 4.9.C.1.iii: once EITHER sample size is below 30 -- here 24 -- both "
                "sample distributions must be free from strong skewness and outliers, so the "
                "sample of 31 does not rescue the other")
c.conceptual(7, "CED 4.9.C.1.ii waives the 10 percent condition for a randomized experiment. "
                "Everything else still applies, and because 25 < 30 the freedom from strong "
                "skewness and outliers is still required of both groups")
c.conceptual(8, "CED 4.9.A.2: the parameters are the two POPULATION means, named with the "
                "response variable, its units and the two populations")
c.conceptual(10, "hypotheses are claims about unknown parameters. xbar1 and xbar2 were "
                 "computed from the data, so a hypothesis about them could be settled by "
                 "arithmetic rather than by inference")
c.conceptual(11, "twins are matched by design, so the pair is the unit; differencing within a "
                 "pair removes family-to-family variation, which is exactly the variation a "
                 "two-sample analysis would leave in the standard error")
c.conceptual(12, "evidence that region A is lower, with A as population 1, is Ha: mu1 < mu2, "
                 "equivalently mu1 - mu2 < 0; mu_d denotes a paired mean difference and does "
                 "not apply to independent samples")
c.conceptual(13, "neither group was randomly sampled and no treatment was randomly assigned, "
                 "so CED 4.9.C.1.i fails and there is no sampling distribution to refer the "
                 "statistic to; sample size cannot repair that")
c.conceptual(14, "CED 4.9.C.1.iii: both sample sizes reach 30, so moderate skewness in the "
                 "populations is not disqualifying, and equal population standard deviations "
                 "are never required by the two-sample t procedure")
c.conceptual(15, "the CED's three conditions are randomization, 10 percent per population, "
                 "and the sample data condition. Equal population standard deviations is not "
                 "among them -- the statistic keeps s1 and s2 separate so they may differ")
c.conceptual(16, "choosing the tail after seeing which sample mean was larger always selects "
                 "the more favorable half of a two-sided test, so the true Type I error rate "
                 "exceeds the stated alpha rather than falling below it")
c.conceptual(18, "only the two factories use two separate sets of bulbs, making the samples "
                 "independent; two test versions per student, each car tested twice, split "
                 "fields and before/after pulses all measure the same unit twice")
c.conceptual(19, "CED 4.9.B.1: H0 is mu1 - mu2 = 0, equivalently mu1 = mu2. Normality and "
                 "equal standard deviations are conditions or assumptions, never the null, "
                 "and no hypothesis mentions the observed difference")
c.conceptual(20, "CED 4.9.C.1.iii offers 'both populations approximately normal' as an "
                 "alternative to both n >= 30, and that route carries no sample-size "
                 "requirement, so 15 and 17 are fine")
c.conceptual(21, "random assignment satisfies randomization and waives the 10 percent "
                 "condition (CED 4.9.C.1.ii); with both n below 30 the sample data condition "
                 "is met by the stated symmetry and absence of outliers")
c.conceptual(22, "the two-sample standard error sqrt(s1^2/n1 + s2^2/n2) adds variances, which "
                 "is valid only for independent samples; correlated repeated measurements make "
                 "it the wrong standard error, and the paired analysis is correct instead")
c.conceptual(24, "CED 4.9.B.1 writes the null as mu1 - mu2 = 0, and CED 4.10.A.1's statistic "
                 "subtracts 0 in its numerator, so the standard procedure tests a null "
                 "difference of 0")
c.conceptual(25, "CED 4.9.C.1.iii: when n is below 30 and the population shape is unknown, the "
                 "requirement falls on the SAMPLE distributions, and both are free from strong "
                 "skewness and outliers here")

c.finish()
