"""Verification for AP STATISTICS 2.10, the binomial distribution.

Every probability is computed TWICE by independent routes and the two are
required to agree before either is compared with a key:

  * `scipy.stats.binom.pmf` / `.cdf`, and
  * the closed form C(n, k) p^k (1-p)^(n-k) built from `math.comb`, summed by
    hand for the cumulative cases.

That matters because a binomial key is the kind of number nobody can check by
eye, so a single library call verifying a value the author took from the same
library call would be circular. Means and standard deviations are likewise
computed both from the np / sqrt(np(1-p)) formulas and from the full
distribution by its definition, and the two must match.

The distribution used for each item is stated in a comment, and every one is
confirmed to be a valid distribution (probabilities summing to 1 across all
k from 0 to n) before it is used.

Run: python3 verify_s2_10.py
"""
import math

from scipy.stats import binom

import s_verify_util as U

import s2_10

c = U.Checker(s2_10)


def pmf_formula(k, n, p):
    """C(n, k) p^k (1-p)^(n-k), from first principles."""
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def pmf(k, n, p):
    """Both routes, required to agree."""
    a = float(binom.pmf(k, n, p))
    b = pmf_formula(k, n, p)
    assert abs(a - b) < 1e-12, f"pmf routes disagree for n={n} p={p} k={k}: {a} vs {b}"
    return b


def cdf(k, n, p):
    a = float(binom.cdf(k, n, p))
    b = sum(pmf_formula(j, n, p) for j in range(k + 1))
    assert abs(a - b) < 1e-12, f"cdf routes disagree for n={n} p={p} k<={k}: {a} vs {b}"
    return b


def parameters(n, p):
    """(mean, sd) from the formulas AND from the distribution's definition."""
    mean_formula = n * p
    sd_formula = math.sqrt(n * p * (1 - p))

    ks = list(range(n + 1))
    probs = [pmf_formula(k, n, p) for k in ks]
    assert abs(sum(probs) - 1.0) < 1e-9, (
        f"n={n} p={p}: the pmf must sum to 1 over k = 0..n, got {sum(probs)}")
    mean_def = sum(k * q for k, q in zip(ks, probs))
    var_def = sum((k - mean_def) ** 2 * q for k, q in zip(ks, probs))

    assert abs(mean_formula - mean_def) < 1e-9, (
        f"n={n} p={p}: np gives {mean_formula}, the definition gives {mean_def}")
    assert abs(sd_formula - math.sqrt(var_def)) < 1e-9, (
        f"n={n} p={p}: sqrt(np(1-p)) gives {sd_formula}, the definition gives {math.sqrt(var_def)}")
    return mean_formula, sd_formula


# --- n = 10, p = 0.3 --------------------------------------------------------------
mean_10, sd_10 = parameters(10, 0.3)
c.check(8, pmf(3, 10, 0.3), tol=0.002)          # 0.267
c.check(9, mean_10)                             # 3.0
c.check(10, sd_10, tol=0.002)                   # 1.449
c.check(11, cdf(2, 10, 0.3), tol=0.002)         # 0.383
assert abs(sd_10 ** 2 - 2.1) < 1e-9, "q10: 2.1 is the variance distractor"
# The rationale for q8 names two distractors; both are confirmed to be what it says.
assert abs(cdf(2, 10, 0.3) - 0.383) < 0.001, "q8: 0.383 is P(X <= 2)"
assert abs(0.3 ** 3 - 0.027) < 1e-12, "q8: 0.027 is p cubed with no coefficient"

# --- n = 8, p = 0.25 --------------------------------------------------------------
mean_8, sd_8 = parameters(8, 0.25)
c.check(12, pmf(2, 8, 0.25), tol=0.002)         # 0.311
c.check(13, cdf(1, 8, 0.25), tol=0.002)         # 0.367
c.check(14, mean_8)                             # 2.00
c.check(15, sd_8, tol=0.002)                    # 1.225
assert abs(sd_8 ** 2 - 1.5) < 1e-9, "q15: 1.5 is the variance distractor"
assert abs(pmf(0, 8, 0.25) - 0.100) < 0.001 and abs(pmf(1, 8, 0.25) - 0.267) < 0.001, (
    "q13: the rationale's two terms must be 0.100 and 0.267")

# --- n = 12, p = 0.6 --------------------------------------------------------------
mean_12, sd_12 = parameters(12, 0.6)
c.check(16, mean_12)                            # 7.2
c.check(17, sd_12, tol=0.002)                   # 1.697
c.check(18, pmf(8, 12, 0.6), tol=0.002)         # 0.213
assert abs(sd_12 ** 2 - 2.88) < 1e-9, "q17: 2.88 is the variance distractor"
assert abs(12 * 0.4 - 4.8) < 1e-9, "q16: 4.8 is the expected number MISSED"

# --- n = 5, p = 0.4, via the complement --------------------------------------------
p_none = pmf(0, 5, 0.4)
assert abs(p_none - 0.6 ** 5) < 1e-12, "P(no failures) must equal 0.6^5"
c.check(19, 1 - p_none, tol=0.002)              # 0.922

# --- n = 6, p = 1/6 ----------------------------------------------------------------
mean_6, sd_6 = parameters(6, 1 / 6)
c.check(20, mean_6)                             # 1.000
c.check(21, pmf(2, 6, 1 / 6), tol=0.002)        # 0.201

# --- n = 20, p = 0.5 ----------------------------------------------------------------
mean_20, sd_20 = parameters(20, 0.5)
c.check(22, sd_20, tol=0.002)                   # 2.236
assert abs(sd_20 ** 2 - 5.0) < 1e-9 and abs(mean_20 - 10.0) < 1e-9, (
    "q22: 5 is the variance and 10 the mean, both offered as distractors")


def failures_are_binomial_too():
    """q24: counting failures instead of successes is binomial with p -> 1 - p."""
    n, p = 12, 0.6
    for k in range(n + 1):
        assert abs(pmf_formula(k, n, p) - pmf_formula(n - k, n, 1 - p)) < 1e-12, (
            "the distribution of failures must mirror that of successes")
    mean_f, sd_f = parameters(n, 1 - p)
    assert abs(mean_f - n * 0.4) < 1e-9 and abs(sd_f - sd_12) < 1e-9, (
        "the failure count has mean n(1-p) and the SAME standard deviation")


def n_grows():
    """q25: raising n with p fixed raises both the mean and the standard deviation."""
    p = 0.3
    previous = None
    for n in (10, 20, 40, 80):
        mean, sd = parameters(n, p)
        if previous is not None:
            assert mean > previous[0], "the mean must increase with n"
            assert sd > previous[1], "the standard deviation must increase with n"
        previous = (mean, sd)
    # The mean grows in proportion to n and the sd in proportion to sqrt(n),
    # which is why the sd grows more slowly but still grows.
    m10, s10 = parameters(10, p)
    m40, s40 = parameters(40, p)
    assert abs(m40 / m10 - 4.0) < 1e-9, "the mean quadruples when n quadruples"
    assert abs(s40 / s10 - 2.0) < 1e-9, "the standard deviation only doubles"


def without_replacement_is_not_binomial():
    """q7 and q23: a constant p is what the binomial model needs.

    Drawing 20 from 30 changes the success probability a great deal; drawing 20
    from 300,000 changes it negligibly. Both are computed rather than asserted.
    """
    def drift(population, successes, draws):
        """How much p moves if every draw so far was a success."""
        start = successes / population
        end = (successes - (draws - 1)) / (population - (draws - 1))
        return abs(end - start)

    small = drift(30, 15, 20)
    large = drift(300000, 150000, 20)
    assert small > 0.3, f"20 of 30 moves p a lot: {small:.4f}"
    assert large < 0.0001, f"20 of 300,000 barely moves p: {large:.8f}"
    assert small > 1000 * large, "the two situations must differ by orders of magnitude"

    # q7: 10 cards from 52 without replacement -- p really does change.
    assert abs(13 / 52 - 12 / 51) > 0.004, "removing a heart changes the probability of the next"


failures_are_binomial_too()
n_grows()
without_replacement_is_not_binomial()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "Skill 3.C: the binomial requirements are a fixed n, two outcomes, independence and a constant p; nothing is required of the observed number of successes.")
c.conceptual(2, "Skill 3.C: the binomial coefficient counts the orderings of k successes, each with probability p^k (1-p)^(n-k).")
c.conceptual(3, "Skill 3.D: verified above against the definition -- the mean of a binomial is np.")
c.conceptual(4, "Skill 3.D: verified above against the definition -- the standard deviation is sqrt(np(1-p)).")
c.conceptual(5, "Skill 3.C: only the with-replacement selection of a fixed 12 items has a fixed n, two outcomes, independence and a constant p.")
c.conceptual(6, "Skill 3.C: rolling until the first six satisfies every requirement except the fixed number of trials, which is why it is not binomial.")
c.conceptual(7, "Skill 3.C: computed above -- dealing without replacement moves the success probability from 13/52 to 12/51, so p is not constant.")
c.conceptual(23, "Skill 3.C: computed above -- 20 drawn from 30 moves p by more than 0.3, while 20 from 300,000 moves it by less than 0.0001.")
c.conceptual(24, "Skill 3.C: verified above -- relabelling successes as failures leaves a binomial with the same n and probability 1 - p.")
c.conceptual(25, "Skill 3.D: computed above -- quadrupling n quadruples the mean and doubles the standard deviation, so both increase.")

c.finish()
