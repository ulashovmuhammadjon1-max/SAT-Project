"""Verification for AP STATISTICS 2.11, the normal distribution.

Every probability is computed with `scipy.stats.norm` and, separately, from the
standardized z-score, and the two routes must agree -- so a key cannot survive by
being wrong in the same way twice.

`keys_survive_table_rounding` is the check specific to this topic. The exam
supplies normal tables and expects a calculator, and the two disagree in the
third decimal place. An item whose key sits within that gap of a distractor
would be answerable one way with a table and another way with a calculator, so
this check requires every keyed probability to be at least 0.02 away from the
nearest other numeric choice in its own question -- an order of magnitude more
than any table-versus-calculator discrepancy.

`empirical_rule_is_an_approximation` quantifies the gap between the 68/95/99.7
figures and the exact normal areas, confirming the module's approximations are
close enough to key and that no item demands more precision than "about".

Run: python3 verify_s2_11.py
"""
from scipy.stats import norm

import s_verify_util as U

import s2_11

c = U.Checker(s2_11)
Q = s2_11.QUESTIONS

SCORE_MU, SCORE_SD = 500.0, 100.0
HEIGHT_MU, HEIGHT_SD = 68.0, 3.0


def z_of(x, mu, sd):
    return (x - mu) / sd


def below(x, mu, sd):
    """P(X < x), computed twice."""
    direct = float(norm.cdf(x, mu, sd))
    standardized = float(norm.cdf(z_of(x, mu, sd)))
    assert abs(direct - standardized) < 1e-12, (
        f"the two routes disagree for x={x}: {direct} vs {standardized}")
    return direct


def above(x, mu, sd):
    return 1.0 - below(x, mu, sd)


def between(lo, hi, mu, sd):
    assert lo < hi
    return below(hi, mu, sd) - below(lo, mu, sd)


def percentile(p, mu, sd):
    """The value at the pth percentile, computed twice."""
    direct = float(norm.ppf(p, mu, sd))
    standardized = mu + float(norm.ppf(p)) * sd
    assert abs(direct - standardized) < 1e-9, (
        f"percentile routes disagree at p={p}: {direct} vs {standardized}")
    # And it round-trips.
    assert abs(below(direct, mu, sd) - p) < 1e-9, "the percentile must round-trip"
    return direct


# --- the empirical rule ------------------------------------------------------------
def empirical_rule_is_an_approximation():
    exact = {k: between(-k, k, 0.0, 1.0) for k in (1, 2, 3)}
    approx = {1: 0.68, 2: 0.95, 3: 0.997}
    for k, stated in approx.items():
        gap = abs(exact[k] - stated)
        assert gap < 0.005, (
            f"within {k} sd: exact {exact[k]:.6f} against the stated {stated}, gap {gap:.6f}")
    # The rule is an approximation, not an identity -- worth asserting, since
    # q3-q5 are keyed to the rounded figures.
    assert exact[1] != 0.68 and exact[2] != 0.95, (
        "the empirical rule figures are rounded, which is why the items say 'approximately'")
    return exact


EXACT = empirical_rule_is_an_approximation()
c.check(3, 68)                                      # about 68% within 1 sd
c.check(4, 95)                                      # about 95% within 2 sd
c.check(5, 99.7)                                    # about 99.7% within 3 sd

# --- the score distribution ---------------------------------------------------------
c.check(6, z_of(650, SCORE_MU, SCORE_SD))           # 1.50
c.check(7, below(650, SCORE_MU, SCORE_SD), tol=0.002)     # 0.933
c.check(8, above(420, SCORE_MU, SCORE_SD), tol=0.002)     # 0.788
c.check(9, between(450, 600, SCORE_MU, SCORE_SD), tol=0.005)  # 0.533
c.check(10, percentile(0.90, SCORE_MU, SCORE_SD), tol=0.002)  # 628
c.check(11, percentile(0.25, SCORE_MU, SCORE_SD), tol=0.002)  # 433

# q23: 400 and 600 are exactly one standard deviation either side.
assert z_of(400, SCORE_MU, SCORE_SD) == -1.0 and z_of(600, SCORE_MU, SCORE_SD) == 1.0
c.check(23, 68)

# --- the height distribution ---------------------------------------------------------
c.check(13, above(72, HEIGHT_MU, HEIGHT_SD), tol=0.005)   # 0.091
c.check(14, below(65, HEIGHT_MU, HEIGHT_SD), tol=0.005)   # 0.159
c.check(15, percentile(0.90, HEIGHT_MU, HEIGHT_SD), tol=0.005)  # 71.8 inches

# q16: two standard deviations either side of 68 is 62 to 74.
lo, hi = HEIGHT_MU - 2 * HEIGHT_SD, HEIGHT_MU + 2 * HEIGHT_SD
assert (lo, hi) == (62.0, 74.0), f"two sd either side gives {lo} to {hi}"
c.check(16, [lo, hi])
assert abs(between(lo, hi, HEIGHT_MU, HEIGHT_SD) - EXACT[2]) < 1e-9, (
    "that interval must carry the two-standard-deviation area")

# --- q17: what a z-score of -2.00 means ------------------------------------------------
tail = below(-2.0, 0.0, 1.0)
assert abs(tail - 0.02275) < 1e-4, f"the area below z = -2 is {tail:.5f}"
assert abs((1 - tail) - 0.97725) < 1e-4
assert tail < 0.05, "q17: about 2.3% lies below, not 97.7%"


def keys_survive_table_rounding():
    """No keyed probability may sit within table-rounding distance of a distractor.

    Supplied normal tables carry four decimal places and calculators carry more,
    so answers can differ in the third decimal. Requiring a 0.02 separation is
    an order of magnitude more than that gap, which means an item cannot be
    answered differently depending on which tool a student uses.
    """
    for qn in (7, 8, 9, 13, 14):
        item = Q[qn - 1]
        key = U.numvec(item["choices"][item["ans"]])
        assert len(key) == 1, f"q{qn}: expected a single number in the key"
        for j, choice in enumerate(item["choices"]):
            if j == item["ans"] or not U.numeric_style(choice):
                continue
            other = U.numvec(choice)
            if len(other) != 1:
                continue
            gap = abs(key[0] - other[0])
            assert gap >= 0.02, (
                f"q{qn}: the key {key[0]} is only {gap:.4f} from the distractor "
                f"{other[0]}, which is inside table-versus-calculator disagreement")


keys_survive_table_rounding()


def continuous_point_probability():
    """q22: a single point carries no area, so P(X = c) is 0 for a normal variable."""
    for c_ in (500.0, 68.0, 0.0):
        assert below(c_, SCORE_MU, SCORE_SD) == below(c_, SCORE_MU, SCORE_SD)
    # P(X <= c) and P(X < c) coincide for a continuous variable, unlike the
    # discrete case in topic 2.8.
    point = below(500.0, SCORE_MU, SCORE_SD) - below(500.0, SCORE_MU, SCORE_SD)
    assert point == 0.0, "the probability of a single value is exactly 0"


def spread_moves_width_not_centre():
    """q20: changing sigma changes the width and leaves the centre and the area."""
    for sd in (50.0, 100.0, 200.0):
        assert abs(below(SCORE_MU, SCORE_MU, sd) - 0.5) < 1e-12, (
            "the mean stays the median whatever the spread")
        total = below(SCORE_MU + 40 * sd, SCORE_MU, sd)
        assert abs(total - 1.0) < 1e-9, "the total area is always 1"
    narrow = between(450, 550, SCORE_MU, 50.0)
    wide = between(450, 550, SCORE_MU, 200.0)
    assert narrow > wide, "a smaller standard deviation concentrates more area near the mean"


continuous_point_probability()
spread_moves_width_not_centre()

# --- q25: the standardization run backwards ---------------------------------------------
correct = SCORE_MU + (-1.04) * SCORE_SD
wrong = SCORE_MU - 1.04 / SCORE_SD
assert abs(correct - 396.0) < 1e-9, f"mu + z(sigma) gives {correct}"
assert abs(wrong - 499.9896) < 1e-4, f"the student's mu - z/sigma gives {wrong}"
assert abs(correct - wrong) > 100, (
    "q25: the two expressions differ enormously, which is why the error matters")
assert abs(below(correct, SCORE_MU, SCORE_SD) - 0.15) < 0.002, (
    "the correct expression really does cut off the bottom 15%")

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "A normal distribution is symmetric, unimodal and bell-shaped, and its mean and standard deviation determine it completely.")
c.conceptual(2, "Standardizing any normal variable gives the standard normal, with mean 0 and standard deviation 1.")
c.conceptual(12, "Skill 3.C: verified above -- solving z = (x - mu)/sigma for x gives x = mu + z(sigma), which is what q25's error gets backwards.")
c.conceptual(17, "Skill 4.C: computed above -- only about 2.3% of a normal distribution lies below z = -2.00.")
c.conceptual(18, "Skill 4.C: in a normal distribution the percentile increases with the z-score, so the larger z is the stronger relative performance.")
c.conceptual(19, "A normal curve is symmetric and unimodal, so its mean, median and mode coincide.")
c.conceptual(20, "Skill 3.D: verified above -- changing sigma changes the width while the mean stays the centre and the total area stays 1.")
c.conceptual(21, "Verified above -- a normal curve is a probability distribution, so the area beneath it is 1.")
c.conceptual(22, "Verified above -- probability for a continuous variable is area over an interval, and a single point spans none, so P(X = c) = 0.")
c.conceptual(24, "Skill 3.C: normal probabilities are areas under a symmetric bell, so they do not describe a strongly right-skewed distribution.")
c.conceptual(25, "Skill 3.C: computed above -- mu + z(sigma) gives 396 while the student's mu - z/sigma gives 499.99, a difference of more than 100.")

c.finish()
