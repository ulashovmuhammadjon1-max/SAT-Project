"""Verify AP Statistics 4.4 Setting Up a Test for a Mean or Mean Difference.

This topic sets a test up rather than carrying it out, so most items are
conceptual and each conceptual entry below states the CED rule that fixes its
key. The quantities that ARE numeric -- degrees of freedom for one-sample and
matched-pairs procedures, and the 10 percent condition thresholds -- are
computed here, not recalled.

Distribution for every test discussed: Student's t with df = n - 1, where for a
matched-pairs design n is the number of DIFFERENCES. That is why q4 is df 15
rather than 30 and q22 is df 40 rather than 80.
"""
import s4_4
from s_verify_util import Checker

c = Checker(s4_4)


def df_one_sample(n):
    return n - 1


def ten_percent_ok(n, N):
    """CED 4.4.C.1.ii: the sample must be at most 10 percent of the population."""
    return n <= 0.10 * N


def min_population(n):
    """Smallest N satisfying n <= 0.10 N."""
    return 10 * n


# q3, q22 -- degrees of freedom
c.check(3, df_one_sample(23))
c.check(22, df_one_sample(41))
assert df_one_sample(41) != 41 + 41 - 2, "a paired design never uses the two-sample df"

# q8 -- smallest population for the 10 percent condition at n = 45
assert min_population(45) == 450 and ten_percent_ok(45, 450)
assert not ten_percent_ok(45, 449)
c.check(8, min_population(45))

# q7 -- the 10 percent condition fails at n = 28 out of N = 250
assert not ten_percent_ok(28, 250), "q7 must actually fail the 10 percent condition"
assert 0.10 * 250 == 25.0 and 28 / 250 > 0.10
c.conceptual(7, "0.10 x 250 = 25 and the sample is 28, which is 11.2 percent of the club, so "
                "n <= 0.10N fails; n = 28 < 30 is not itself a failure, because the sample "
                "data condition can also be met by an absence of strong skewness and outliers")

# q4 -- matched pairs: one sample of 16 differences
assert df_one_sample(16) == 15
c.conceptual(4, "each student supplies both measurements, so the design is matched pairs: one "
                "sample of 16 differences with df = 16 - 1 = 15, computed above, and not the "
                "two-sample df of 30")

# --- conceptual items, with the CED rule that fixes each key -----------------
c.conceptual(1, "H0 takes the claimed value 40 and Ha states the suspicion, a decrease, so "
                "Ha: mu < 40. CED 4.4.B.1 writes both about mu, never about xbar")
c.conceptual(2, "xbar is observed data, not an unknown; a hypothesis has to be a claim about a "
                "parameter or there is nothing to infer")
c.conceptual(5, "CED 4.4.B.2: for a population mean difference the null is mu_d = 0 -- the "
                "population mean of the differences, not the observed mean difference and not "
                "a claim about every pair")
c.conceptual(6, "different volunteers in the two arms make the samples independent, so a "
                "two-sample procedure applies; equal group sizes create no pairing, and "
                "enrollment order is arbitrary")
c.conceptual(9, "a concern about a departure in either direction is two-sided: Ha: mu != 500, "
                "written about the population mean")
c.conceptual(10, "CED 4.4.C.1.iii: with n = 14 < 30 and no stated normal population, the "
                 "sample must be free from strong skewness and outliers, and it is neither; "
                 "t procedures are robust, but not to a strong skew at n = 14")
c.conceptual(11, "CED 4.4.A.3: the parameter names the population, the response variable and "
                 "its units. A parameter is never defined over only the sampled households")
c.conceptual(12, "the null takes the boundary value 8 and Ha states what the reporter wants "
                 "evidence for, so Ha: mu > 8")
c.conceptual(13, "with differences taken as before minus after, a drop in pressure makes each "
                 "difference positive, so 'the drug lowers pressure' is Ha: mu_d > 0. The "
                 "order of subtraction has to be read before the sign is chosen")
c.conceptual(14, "choosing the tail after seeing which way xbar fell always picks the more "
                 "favorable half, so the true Type I error rate exceeds the stated alpha; the "
                 "hypotheses must come from the question, not from the data")
c.conceptual(15, "CED 4.4.C.1.iii: n = 60 >= 30 satisfies the sample data condition on its "
                 "own, and skewness disqualifies only below 30")
c.conceptual(16, "for matched pairs the condition applies to the DIFFERENCES; 34 >= 30 "
                 "satisfies it without any judgement about their shape")
c.conceptual(17, "the CED's three conditions are randomization, 10 percent, and sample data. A "
                 "known sigma is not among them -- it would send the analysis to z instead of "
                 "t, which is a choice of procedure, not a condition")
c.conceptual(18, "'changed' is two-sided and the hypothesized value is the historical 72; the "
                 "observed 75.4 enters the test statistic and must never appear in a "
                 "hypothesis")
c.conceptual(19, "both measurements come from the same car, so differencing removes car-to-car "
                 "variation; the justification is the design, not the equal sample sizes, the "
                 "sample size, or a hoped-for p-value")
c.conceptual(20, "a convenience sample fails the randomization condition, and n = 50 does "
                 "nothing to repair it -- the sampling distribution the test uses assumes "
                 "randomization")
c.conceptual(21, "evidence that the mean rose above 100 is a one-sided upper-tail alternative, "
                 "Ha: mu > 100; mu_d belongs to a paired design, which this is not")
c.conceptual(23, "only the labeled-weight comparison has one measurement per unit against a "
                 "fixed claimed value; before/after baking, two recipes per taster and "
                 "pretest/posttest are all paired, and the two-oven comparison is independent "
                 "samples")
c.conceptual(24, "CED 4.4.C.1.iii lists an approximately normal population first, and that "
                 "route carries no sample-size requirement, so n = 9 is not an obstacle")
c.conceptual(25, "the paired analysis has one sample of 22 differences, so the below-30 branch "
                 "applies to the differences; counting the 44 raw measurements undoes the "
                 "pairing the design was built on")

c.finish()
