"""Verification for AP STATISTICS 2.9, the mean and standard deviation of a
discrete random variable.

Both distributions are parsed from the module and validated (legal
probabilities, totalling 1) before any parameter is computed from them, so a
mistyped probability fails here rather than producing a plausible-looking mean.

`mean_and_sd` implements EK 2.9.A.2 and 2.9.A.3 directly -- sum of x P(x), then
the square root of the sum of (x - mu) squared P(x) -- and every keyed value
comes from it. The variance and the standard deviation are BOTH computed for
each distribution and are checked to be different numbers, because each module
item offers the other as its distractor: q5 keys the variance with the standard
deviation among the choices, and q6 the reverse. If the two ever coincided
(variance 1) those pairs would become unanswerable.

The mean is also cross-checked against an independent route -- a large simulated
run of the distribution -- so a sign error in the weighted sum would not survive.

Run: python3 verify_s2_9.py
"""
import math
import random

import s_verify_util as U

import s2_9

c = U.Checker(s2_9)


def parse(table):
    return {float(value): float(p) for value, p in table["rows"]}


A = parse(s2_9.TABLE_A)          # defects
B = parse(s2_9.TABLE_B)          # net winnings
DIE = {float(k): 1 / 6 for k in range(1, 7)}
UNIF = {float(k): 0.2 for k in range(1, 6)}

for name, dist in (("A", A), ("B", B), ("die", DIE), ("uniform", UNIF)):
    assert all(0 <= p <= 1 for p in dist.values()), f"{name}: illegal probability"
    assert abs(sum(dist.values()) - 1.0) < 1e-9, (
        f"{name}: probabilities sum to {sum(dist.values())}")


def mean_and_sd(dist):
    """EK 2.9.A.2 and 2.9.A.3, implemented directly."""
    mu = sum(x * p for x, p in dist.items())
    var = sum((x - mu) ** 2 * p for x, p in dist.items())
    assert var >= 0, "a weighted sum of squared deviations cannot be negative"
    return mu, var, math.sqrt(var)


muA, varA, sdA = mean_and_sd(A)
muB, varB, sdB = mean_and_sd(B)
muD, varD, sdD = mean_and_sd(DIE)
muU, varU, sdU = mean_and_sd(UNIF)

# The variance and the standard deviation must be distinct, since each appears
# as the other's distractor.
for name, var, sd in (("A", varA, sdA), ("B", varB, sdB), ("die", varD, sdD)):
    assert abs(var - sd) > 1e-6, (
        f"{name}: variance and standard deviation coincide, so the distractor pairs collapse")

# --- distribution A: defects -----------------------------------------------------
c.check(4, muA)                       # 0.75
c.check(5, varA)                      # 0.7875
c.check(6, sdA, tol=0.001)            # 0.8874
assert abs(muA - 0.75) < 1e-12 and abs(varA - 0.7875) < 1e-12
assert muA not in A, "q7: the expected value must not be an attainable value of X"

# --- distribution B: a game ------------------------------------------------------
c.check(9, muB)                       # -0.10
c.check(11, sdB, tol=0.001)           # 3.0150
c.check(12, varB)                     # 9.09
assert muB < 0, "q10: a negative expected value means an average loss per play"
assert abs(varB - 9.09) < 1e-9

# --- a fair die -------------------------------------------------------------------
c.check(13, muD)                      # 3.5
c.check(14, sdD, tol=0.001)           # 1.7078
assert abs(muD - 3.5) < 1e-12 and muD not in DIE, (
    "q15: 3.5 is not a face of the die, which is the point of the item")
assert abs(varD - 35 / 12) < 1e-9, "the variance of a fair die is 35/12"

# --- a uniform variable on 1..5 ----------------------------------------------------
c.check(19, muU)                      # 3.0
c.check(20, sdU, tol=0.005)           # 1.41
assert abs(varU - 2.0) < 1e-12, "the variance is the average of (x-3) squared, which is 2"
assert abs(muU - sum(UNIF) / len(UNIF)) < 1e-12, (
    "with equal probabilities the expected value is the ordinary average")

# --- expected values in money ------------------------------------------------------
payout = {10000.0: 0.002, 0.0: 0.998}
assert abs(sum(payout.values()) - 1.0) < 1e-12
mu_payout, _, _ = mean_and_sd(payout)
assert abs(mu_payout - 20.0) < 1e-9, f"q21: expected payout is {mu_payout}"
c.check(21, mu_payout)                # 20

net = 2.20 - 3.00
assert abs(net - (-0.80)) < 1e-9, f"q22: expected net result is {net}"
c.check(22, net)                      # -0.80


def zero_spread():
    """q16: a degenerate variable has standard deviation 0."""
    degenerate = {7.0: 1.0}
    mu, var, sd = mean_and_sd(degenerate)
    assert (mu, var, sd) == (7.0, 0.0, 0.0), f"got {(mu, var, sd)}"


def mean_lies_within_the_range():
    """q23: a probability-weighted average cannot fall outside the values' range."""
    for dist in (A, B, DIE, UNIF, {10000.0: 0.002, 0.0: 0.998}):
        mu, _, _ = mean_and_sd(dist)
        assert min(dist) <= mu <= max(dist), (
            f"the mean {mu} must lie between {min(dist)} and {max(dist)}")
    # And it need not be attainable, positive, or whole -- each of which is a
    # distractor in q23.
    assert muA not in A, "not attainable"
    assert muB < 0, "not necessarily positive"
    assert muD != int(muD), "not necessarily whole"
    most_likely = max(A, key=lambda x: A[x])
    assert muA != most_likely, "not necessarily the most likely value"


def mean_matches_simulation():
    """Cross-check E(X) against a simulated long-run average, not just the formula."""
    rng = random.Random(20260830)
    for dist, mu in ((A, muA), (B, muB), (DIE, muD)):
        values = list(dist)
        weights = [dist[v] for v in values]
        draws = rng.choices(values, weights=weights, k=200000)
        average = sum(draws) / len(draws)
        spread = mean_and_sd(dist)[2] / math.sqrt(len(draws))
        assert abs(average - mu) < 5 * spread, (
            f"simulated average {average:.4f} is too far from the computed mean {mu}")


zero_spread()
mean_lies_within_the_range()
mean_matches_simulation()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.9.A.2: E(X) is the sum of x times P(x), a probability-weighted average rather than a plain one.")
c.conceptual(2, "EK 2.9.A.3: the weighted sum of squared deviations is the variance, and the standard deviation is its square root.")
c.conceptual(3, "EK 2.9.A.1: the mean and standard deviation of a distribution are parameters, single fixed values, not statistics that vary between samples.")
c.conceptual(7, "EK 2.9.A.2: verified above -- the computed mean 0.75 is not an attainable value, because an expected value is a long-run average.")
c.conceptual(8, "EK 2.9.B.1: an expected value is a long-run average per item in context, not a claim about a single item and not a percentage.")
c.conceptual(10, "EK 2.9.B.1: computed above -- the expected value is negative, so the long-run average is a loss per play, though no single play returns -0.10.")
c.conceptual(15, "EK 2.9.A.2: verified above -- 3.5 is not a face of the die, so the expected value is the balance point rather than an achievable outcome.")
c.conceptual(16, "EK 2.9.A.3: computed above -- with no variation every squared deviation is 0, so the standard deviation is 0.")
c.conceptual(17, "EK 2.9.A.3: an equal expected value fixes the centre, so a larger standard deviation means values further from that centre.")
c.conceptual(18, "EK 2.9.A.3: weighting the squared deviations by P(x) is what stops a rare extreme value from dominating the typical deviation.")
c.conceptual(23, "EK 2.9.A.2: verified above -- the mean lies within the range of the values, but need not be attainable, positive, whole, or the most likely value.")
c.conceptual(24, "EK 2.9.B.1: a standard deviation is a typical distance from the mean in the variable's own units, not a proportion of items.")
c.conceptual(25, "EK 2.9.A.3: verified above -- squared deviations and probabilities are both non-negative, so neither the variance nor its square root can be negative.")

c.finish()
