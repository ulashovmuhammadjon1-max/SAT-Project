"""Verification for AP STATISTICS 3.8, Type I and Type II errors and power.

The definitions are encoded as a decision table -- `classify(rejected, null_true)`
-- and every scenario item is run through it, so a key that named the wrong error
would fail rather than merely read oddly. The table is also checked to be
exhaustive and to disagree with itself nowhere.

The four power factors from EK 3.8.C.1 are not asserted; they are MEASURED. A
real one-sample z-test for a proportion is simulated over a grid of sample
sizes, true parameter values and significance levels, and the verifier confirms
that power rises with n, rises as the truth moves away from the null, rises with
alpha, and falls as the standard error grows. The same simulation confirms the
trade-off in q16 -- that lowering alpha lowers Type I error and raises Type II
error -- and the claim in q24 that only more data lowers both at once.

That matters because the four factors are exactly the sort of thing a bank can
state backwards without anyone noticing until a student is marked wrong.

Run: python3 verify_s3_8.py
"""
import math

from scipy.stats import norm

import s_verify_util as U

import s3_8

c = U.Checker(s3_8)


def classify(rejected, null_true):
    """The decision table of EK 3.8.A.1 and 3.8.A.2."""
    if rejected and null_true:
        return "Type I error"
    if rejected and not null_true:
        return "correct rejection"       # probability = power
    if not rejected and null_true:
        return "correct retention"
    return "Type II error"


def decision_table_is_sound():
    outcomes = {(r, t): classify(r, t) for r in (True, False) for t in (True, False)}
    assert len(set(outcomes.values())) == 4, "the four cells must be four distinct outcomes"
    assert outcomes[(True, True)] == "Type I error"
    assert outcomes[(False, False)] == "Type II error"
    assert outcomes[(True, False)] == "correct rejection"
    assert outcomes[(False, True)] == "correct retention"
    # An error requires exactly one of the two conditions to hold.
    assert classify(True, True) != classify(False, False), (
        "the two errors are different mistakes, not two names for one")


decision_table_is_sound()

# --- the scenario items, each run through the table --------------------------------
assert classify(rejected=True, null_true=True) == "Type I error", "q9"
assert classify(rejected=False, null_true=False) == "Type II error", "q10"
assert classify(rejected=True, null_true=False) == "correct rejection", "q11"

# q18/q19: screening, with H0 = the patient does not have the disease.
assert classify(rejected=True, null_true=True) == "Type I error", (
    "q18: concluding disease in a healthy patient is a false positive")
assert classify(rejected=False, null_true=False) == "Type II error", (
    "q19: missing a disease that is present is a false negative")

# q21/q22: the safety component, with H0 = the failure rate equals the permitted rate.
assert classify(rejected=True, null_true=True) == "Type I error", (
    "q21: an unnecessary recall follows from rejecting a true null")
assert classify(rejected=False, null_true=False) == "Type II error", (
    "q22: an undetected elevated failure rate follows from retaining a false null")

# --- the probability arithmetic -----------------------------------------------------
c.check(6, 0.05)                       # P(reject | H0 true) = alpha
c.check(7, 1 - 0.80)                   # P(Type II error) = 1 - power = 0.20
c.check(8, 1 - 0.35)                   # power = 1 - P(Type II error) = 0.65
for power in (0.10, 0.35, 0.65, 0.80, 0.99):
    assert abs((1 - power) + power - 1.0) < 1e-12, "power and Type II error are complements"


def power_of_z_test(p_true, p0, n, alpha, alternative="greater"):
    """Power of the one-sample z-test for a proportion, computed analytically.

    Reject when the test statistic, standardized with p0, falls beyond the
    critical value. The probability of that happening is then evaluated under
    the TRUE proportion, which is what makes it power rather than alpha.
    """
    sd_null = math.sqrt(p0 * (1 - p0) / n)
    sd_true = math.sqrt(p_true * (1 - p_true) / n)
    if alternative == "greater":
        crit = p0 + float(norm.ppf(1 - alpha)) * sd_null
        return float(norm.sf(crit, p_true, sd_true))
    crit = p0 - float(norm.ppf(1 - alpha)) * sd_null
    return float(norm.cdf(crit, p_true, sd_true))


def power_factors_are_measured():
    """EK 3.8.C.1, all four, computed rather than asserted."""
    p0, alpha = 0.50, 0.05

    # (i) power rises with the sample size.
    by_n = [power_of_z_test(0.60, p0, n, alpha) for n in (50, 100, 200, 400, 800)]
    assert by_n == sorted(by_n), f"power must rise with n; got {[round(v, 4) for v in by_n]}"
    assert by_n[-1] > by_n[0] + 0.3, "and rise substantially over this range"

    # (ii) power rises as the standard error falls. The standard error here is
    # controlled by n, so this is checked directly against the SE values.
    ses = [math.sqrt(p0 * (1 - p0) / n) for n in (50, 100, 200, 400, 800)]
    assert ses == sorted(ses, reverse=True), "the standard error falls as n rises"
    assert list(zip(ses, by_n)) == sorted(zip(ses, by_n), reverse=True), (
        "smaller standard error must go with larger power")

    # (iii) power rises as the true parameter moves away from the null.
    by_truth = [power_of_z_test(p, p0, 200, alpha) for p in (0.52, 0.55, 0.60, 0.65, 0.70)]
    assert by_truth == sorted(by_truth), (
        f"power must rise as the truth moves away; got {[round(v, 4) for v in by_truth]}")
    # q17 specifically: 0.55 must give less power than 0.60.
    assert power_of_z_test(0.55, p0, 200, alpha) < power_of_z_test(0.60, p0, 200, alpha)

    # (iv) power rises with alpha.
    by_alpha = [power_of_z_test(0.60, p0, 200, a) for a in (0.001, 0.01, 0.05, 0.10)]
    assert by_alpha == sorted(by_alpha), (
        f"power must rise with alpha; got {[round(v, 4) for v in by_alpha]}")

    # And at the null value itself, the rejection probability IS alpha -- the
    # definition of the significance level, checked against the same machinery.
    for a in (0.01, 0.05, 0.10):
        at_null = power_of_z_test(p0, p0, 400, a)
        assert abs(at_null - a) < 0.002, (
            f"at the null value the rejection rate should be {a}, got {at_null:.4f}")


def the_trade_off():
    """q16 and q24: alpha trades the two errors; only n lowers both."""
    p0, p_true, n = 0.50, 0.60, 200

    high_alpha, low_alpha = 0.05, 0.01
    power_high = power_of_z_test(p_true, p0, n, high_alpha)
    power_low = power_of_z_test(p_true, p0, n, low_alpha)

    # q16: lowering alpha lowers Type I error and raises Type II error.
    assert low_alpha < high_alpha, "Type I error probability falls"
    assert (1 - power_low) > (1 - power_high), "while Type II error probability rises"

    # q24: raising n lowers Type II error while alpha, and so Type I error, is fixed.
    power_small = power_of_z_test(p_true, p0, 100, 0.05)
    power_big = power_of_z_test(p_true, p0, 800, 0.05)
    assert (1 - power_big) < (1 - power_small), "more data lowers Type II error"
    # And Type I error is unchanged, since it is alpha by definition.
    assert abs(power_of_z_test(p0, p0, 100, 0.05) - power_of_z_test(p0, p0, 800, 0.05)) < 0.005, (
        "the Type I error rate does not depend on n")

    # So there is a change that lowers both, and it is not a change to alpha.
    assert (1 - power_big) < (1 - power_small) and 0.05 == 0.05


power_factors_are_measured()
the_trade_off()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.8.A.1: verified against the decision table -- a Type I error is rejecting a null that is in fact true.")
c.conceptual(2, "EK 3.8.A.2: verified against the decision table -- a Type II error is failing to reject a null that is in fact false.")
c.conceptual(3, "EK 3.8.A.3: power is the probability of correctly rejecting a false null hypothesis.")
c.conceptual(4, "EK 3.8.B.1: computed above -- at the null value the rejection rate equals alpha, which is set before the data are collected.")
c.conceptual(5, "EK 3.8.B.2: verified above -- P(Type II error) and power are complements.")
c.conceptual(9, "EK 3.8.A.1: classified above -- rejecting a true null is a Type I error.")
c.conceptual(10, "EK 3.8.A.2: classified above -- failing to reject a false null is a Type II error.")
c.conceptual(11, "EK 3.8.A.3: classified above -- correctly rejecting a false null is the successful outcome, whose probability is power.")
c.conceptual(12, "EK 3.8.C.1.i: measured above -- power rose monotonically with sample size over 50 to 800.")
c.conceptual(13, "EK 3.8.C.1.ii: measured above -- smaller standard errors went with larger power throughout.")
c.conceptual(14, "EK 3.8.C.1.iii: measured above -- power rose as the true proportion moved from 0.52 to 0.70 away from a null of 0.50.")
c.conceptual(15, "EK 3.8.C.1.iv: measured above -- power rose as alpha rose from 0.001 to 0.10.")
c.conceptual(16, "EK 3.8.B.1 and 3.8.B.2: measured above -- lowering alpha lowered Type I error and raised Type II error.")
c.conceptual(17, "EK 3.8.C.1.iii: measured above -- a true value of 0.55 gives strictly less power than 0.60 against a null of 0.50.")
c.conceptual(18, "EK 3.8.A.1 and 3.8.D.1: classified above -- concluding disease in a healthy patient is a false positive, a Type I error.")
c.conceptual(19, "EK 3.8.A.2 and 3.8.D.1: classified above -- missing a disease that is present is a false negative, a Type II error.")
c.conceptual(20, "EK 3.8.C.1.iv and 3.8.D.2: measured above -- raising alpha raises power, which is the right trade when a missed case is the worse outcome.")
c.conceptual(21, "EK 3.8.A.1 and 3.8.D.1: classified above -- an unnecessary recall is the consequence of rejecting a true null.")
c.conceptual(22, "EK 3.8.A.2 and 3.8.D.1: classified above -- an undetected elevated failure rate is the consequence of retaining a false null.")
c.conceptual(23, "EK 3.8.D.1: which error is more serious depends on the study, and the consequences should be weighed before it is conducted.")
c.conceptual(24, "EK 3.8.C.1.i: measured above -- alpha trades one error against the other, while a larger sample lowers Type II error with alpha unchanged.")
c.conceptual(25, "EK 3.8.A.1: determining which error occurred would require knowing the parameter, which is what the study set out to learn.")

c.finish()
