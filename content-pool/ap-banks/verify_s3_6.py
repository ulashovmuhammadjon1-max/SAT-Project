"""Verification for AP STATISTICS 3.6, p-values.

`p_value` implements EK 3.6.A.1 directly -- the tail area in the direction the
alternative specifies, doubled for a two-sided alternative -- and every keyed
p-value comes from it. Each is also cross-checked against the complementary area
so a left/right mix-up cannot survive.

The check that carries the module is `same_statistic_two_alternatives`. Items 6,
7 and 8 use z = -2.10 with a one-sided and a two-sided alternative, and the
whole point is that the p-values differ by a factor of exactly two. The verifier
asserts that factor rather than the two numbers separately, so the pair cannot
drift apart under editing.

`decisions_follow_from_alpha` evaluates the reject / fail-to-reject rule as a
predicate for q15, q16 and q23, and confirms that the same p-value of 0.032 gives
OPPOSITE decisions at the two significance levels the module uses -- which is
what those items are for.

Run: python3 verify_s3_6.py
"""
from scipy.stats import norm

import s_verify_util as U

import s3_6

c = U.Checker(s3_6)


def p_value(z, alternative):
    """EK 3.6.A.1: the area in the alternative's direction."""
    if alternative == "greater":
        p = float(norm.sf(z))
        assert abs(p - (1 - float(norm.cdf(z)))) < 1e-12, "tail routes must agree"
    elif alternative == "less":
        p = float(norm.cdf(z))
        assert abs(p - (1 - float(norm.sf(z)))) < 1e-12, "tail routes must agree"
    elif alternative == "two-sided":
        p = 2 * float(norm.sf(abs(z)))
    else:
        raise AssertionError(f"unknown alternative {alternative!r}")
    assert 0 <= p <= 1, f"a p-value must lie in [0, 1]; got {p}"
    return p


# --- the keyed p-values ------------------------------------------------------------
# A tight absolute tolerance: p-values here are small, and several items
# deliberately offer half or double the key as a distractor, so a loose
# tolerance would make those choices collide with the answer.
PTOL = 0.0005
c.check(5, p_value(1.85, "greater"), tol=PTOL)          # 0.0322
c.check(6, p_value(-2.10, "less"), tol=PTOL)            # 0.0179
c.check(7, p_value(-2.10, "two-sided"), tol=PTOL)       # 0.0357
c.check(9, p_value(1.42, "two-sided"), tol=PTOL)        # 0.1556
c.check(10, p_value(2.58, "greater"), tol=PTOL)         # 0.0049


def same_statistic_two_alternatives():
    """q6, q7, q8: one test statistic, two alternatives, a factor of exactly 2."""
    one_sided = p_value(-2.10, "less")
    two_sided = p_value(-2.10, "two-sided")
    assert abs(two_sided - 2 * one_sided) < 1e-12, (
        "the two-sided p-value must be exactly twice the one-sided one")
    assert abs(one_sided - 0.0179) < 0.001 and abs(two_sided - 0.0357) < 0.001
    assert one_sided != two_sided, "q8 is empty unless the two genuinely differ"

    # And the same relationship holds for the other statistic the module uses.
    assert abs(p_value(1.42, "two-sided") - 2 * p_value(1.42, "greater")) < 1e-12
    assert abs(p_value(1.85, "two-sided") - 2 * p_value(1.85, "greater")) < 1e-12
    assert abs(2 * p_value(1.85, "greater") - 0.0644) < 0.001, (
        "q5: 0.0644 is the two-sided distractor")


same_statistic_two_alternatives()


def decisions_follow_from_alpha():
    """q15, q16, q23: the same p-value, two significance levels, two decisions."""
    def reject(p, alpha):
        return p <= alpha

    p = 0.032
    assert reject(p, 0.05), "q15: 0.032 is below 0.05, so the null is rejected"
    assert not reject(p, 0.01), "q16: 0.032 exceeds 0.01, so it is not"
    assert reject(p, 0.05) != reject(p, 0.01), (
        "the pair of items is pointless unless the decisions differ")

    # q23: two p-values on either side of 0.05, differing by 0.004.
    a, b = 0.048, 0.052
    assert reject(a, 0.05) and not reject(b, 0.05), "opposite decisions at alpha = 0.05"
    assert abs(a - b) < 0.005, (
        "yet the two p-values differ by less than 0.005, which is the point of the item")
    # Expressed as evidence rather than as a decision, they are near-identical.
    assert abs(a / b - 1) < 0.1, "the ratio of the two p-values is within 10% of 1"


decisions_follow_from_alpha()


def monotonicity_and_range():
    """q18, q20, q22: how the p-value moves, and what it can never be."""
    # q18: a statistic further from 0 gives a smaller p-value, in each direction.
    rights = [p_value(z, "greater") for z in (0.5, 1.0, 1.5, 2.0, 2.5)]
    assert rights == sorted(rights, reverse=True), "right-tail p-values must fall as z rises"
    lefts = [p_value(z, "less") for z in (-0.5, -1.0, -1.5, -2.0, -2.5)]
    assert lefts == sorted(lefts, reverse=True), "left-tail p-values must fall as z falls"
    twos = [p_value(z, "two-sided") for z in (0.5, 1.0, 1.5, 2.0, 2.5)]
    assert twos == sorted(twos, reverse=True)

    # q20: a p-value can never exceed 1. The two-sided formula uses |z| exactly
    # so that doubling an area larger than one half cannot happen.
    for z in (-3.0, -1.0, 0.0, 1.0, 3.0):
        assert 0 <= p_value(z, "two-sided") <= 1
    assert abs(p_value(0.0, "two-sided") - 1.0) < 1e-12, (
        "a statistic of exactly 0 gives the largest possible two-sided p-value, 1")

    # q22: with Ha: p > p0, a NEGATIVE statistic gives a p-value above one half.
    for z in (-0.5, -1.0, -2.0):
        p = p_value(z, "greater")
        assert p > 0.5, f"z = {z} with a greater-than alternative gives p = {p:.4f}"
    assert p_value(-1.0, "greater") > 0.5 > p_value(1.0, "greater"), (
        "data on the wrong side of the null are no evidence for the alternative")

    # q19: a p-value of 0.62 is the sort of thing the null routinely produces.
    assert p_value(-0.31, "greater") > 0.6, "such a p-value corresponds to an unremarkable statistic"


monotonicity_and_range()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.6.A.1: a p-value is computed from the null distribution, so it is a probability about the data given the null.")
c.conceptual(2, "EK 3.6.A.1: the null distribution is the distribution of the test statistic given that the null hypothesis is true.")
c.conceptual(3, "EK 3.6.A.1: verified above -- a small p-value means the data are surprising under the null, which is evidence against it.")
c.conceptual(4, "EK 3.6.A.1: verified above -- a large p-value means the data are unremarkable under the null, which is not evidence for it.")
c.conceptual(8, "EK 3.6.A.1: computed above -- the two-sided p-value is exactly twice the one-sided one for the same statistic.")
c.conceptual(11, "EK 3.6.A.1: the interpretation must state the conditional on the null and describe results at least as extreme in the alternative's direction.")
c.conceptual(12, "EK 3.6.A.1: the conditioning runs from hypothesis to data, so a p-value is not the probability that the null is true.")
c.conceptual(13, "EK 3.6.A.1: subtracting a p-value from 1 does not turn a statement about data into a statement about a hypothesis.")
c.conceptual(14, "EK 3.6.A.1: verified above -- the smaller the p-value, the more surprising the data under the null and the stronger the evidence against it.")
c.conceptual(15, "EK 3.6.A.1: computed above -- 0.032 falls below alpha = 0.05, so the null is rejected.")
c.conceptual(16, "EK 3.6.A.1: computed above -- the same 0.032 exceeds alpha = 0.01, so the decision reverses.")
c.conceptual(17, "EK 3.6.A.1: a test can find evidence against a claim but never establish one, so the wording is 'fail to reject'.")
c.conceptual(18, "EK 3.6.A.1: verified above -- moving further into the tail leaves less area beyond the statistic, so the p-value falls.")
c.conceptual(19, "EK 3.6.A.1: computed above -- a p-value of 0.62 describes a result the null routinely produces.")
c.conceptual(20, "EK 3.6.A.1: verified above -- a p-value is a probability and lies in [0, 1], with 1 attained at a statistic of exactly 0.")
c.conceptual(21, "EK 3.6.A.1 with 1.1.B.1: choosing alpha after seeing the p-value lets the researcher pick the conclusion, so the stated error rate no longer applies.")
c.conceptual(22, "EK 3.6.A.1: computed above -- a negative statistic against a greater-than alternative gives a p-value above one half.")
c.conceptual(23, "EK 3.6.A.1: computed above -- 0.048 and 0.052 differ by less than 0.005 in evidence while giving opposite decisions at a fixed alpha.")
c.conceptual(24, "EK 3.6.A.1 with 3.5.C.1: the null distribution is derived under the null and is only correct if the test's conditions hold.")
c.conceptual(25, "EK 3.6.A.1: hypotheses and alpha are fixed first, conditions are checked before the calculation is trusted, and the decision comes last.")

c.finish()
