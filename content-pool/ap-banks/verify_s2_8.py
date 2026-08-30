"""Verification for AP STATISTICS 2.8, random variables and probability distributions.

The pet distribution is parsed from the module and validated as a distribution
before anything is keyed off it: every probability legal, and the total exactly
1. Then each keyed probability is recomputed by summing the relevant values.

Two structural checks are specific to this topic.

`cumulative_table_matches` confirms TABLE_PETS_CUM is genuinely the cumulative
version of TABLE_PETS -- built by running totals, non-decreasing, ending at 1.
The module asks questions off both tables and asserts, in q15 and q16, that an
individual probability is the JUMP in the cumulative table, so the two tables
have to agree or those items are wrong in a way no single-table check would see.

`strict_versus_inclusive` checks the boundary items. For a discrete variable
P(X <= 2) and P(X < 2) differ by exactly P(X = 2), and q9 and q25 both turn on
that; the check requires the two to be genuinely different numbers here, since
an item distinguishing them is pointless if they happen to coincide.

Run: python3 verify_s2_8.py
"""
import s_verify_util as U

import s2_8

c = U.Checker(s2_8)


def parse(table):
    """value -> probability, skipping any entry written as '?'."""
    out = {}
    for value, p in table["rows"]:
        if p.strip() == "?":
            out[int(value)] = None
        else:
            out[int(value)] = float(p)
    return out


PETS = parse(s2_8.TABLE_PETS)
CUM = parse(s2_8.TABLE_PETS_CUM)
CALLS = parse(s2_8.TABLE_CALLS)

# --- the pet distribution must be a distribution --------------------------------
assert set(PETS) == {0, 1, 2, 3, 4}
assert all(0 <= p <= 1 for p in PETS.values()), "every probability must be legal"
assert abs(sum(PETS.values()) - 1.0) < 1e-12, f"pet probabilities sum to {sum(PETS.values())}"


def P(pred, dist):
    return sum(p for x, p in dist.items() if pred(x))


# --- individual and accumulated probabilities -----------------------------------
c.check(7, PETS[2])                                   # 0.25
c.check(8, P(lambda x: x <= 2, PETS))                 # 0.82
c.check(9, P(lambda x: x < 2, PETS))                  # 0.57
c.check(10, P(lambda x: x >= 2, PETS))                # 0.43
c.check(11, P(lambda x: x > 2, PETS))                 # 0.18
c.check(12, PETS[1] + PETS[2])                        # 0.60
c.check(13, 1 - PETS[0])                              # 0.78
c.check(14, sum(PETS.values()))                       # 1.00

# Complementary pairs must be consistent.
assert abs(P(lambda x: x <= 2, PETS) + P(lambda x: x > 2, PETS) - 1.0) < 1e-12
assert abs(P(lambda x: x < 2, PETS) + P(lambda x: x >= 2, PETS) - 1.0) < 1e-12


def cumulative_table_matches():
    """TABLE_PETS_CUM must be the running total of TABLE_PETS."""
    running = 0.0
    for x in sorted(PETS):
        running += PETS[x]
        assert abs(CUM[x] - running) < 1e-9, (
            f"cumulative table says P(X <= {x}) = {CUM[x]}, running total is {running}")
    values = [CUM[x] for x in sorted(CUM)]
    assert values == sorted(values), "a cumulative distribution must be non-decreasing"
    assert abs(values[-1] - 1.0) < 1e-12, "a cumulative distribution must end at 1"


cumulative_table_matches()

# --- reading individual probabilities back out of the cumulative table ------------
c.check(15, CUM[3] - CUM[2])                          # P(X = 3) = 0.13
c.check(16, CUM[1] - CUM[0])                          # P(X = 1) = 0.35
c.check(17, 1 - CUM[3])                               # P(X > 3) = 0.05
assert abs((CUM[3] - CUM[2]) - PETS[3]) < 1e-9, "the jump must equal the individual probability"
assert abs((CUM[1] - CUM[0]) - PETS[1]) < 1e-9


def strict_versus_inclusive():
    """q9 and q25: the two boundary probabilities differ by exactly P(X = 2)."""
    inclusive = P(lambda x: x <= 2, PETS)
    strict = P(lambda x: x < 2, PETS)
    assert abs((inclusive - strict) - PETS[2]) < 1e-12, (
        "the difference must be exactly the probability at the boundary value")
    assert inclusive != strict, (
        "q9 is pointless unless the two genuinely differ, which requires P(X = 2) > 0")
    assert PETS[2] > 0


strict_versus_inclusive()

# --- the distribution with a missing probability ---------------------------------
known = {x: p for x, p in CALLS.items() if p is not None}
missing_values = [x for x, p in CALLS.items() if p is None]
assert missing_values == [3], f"exactly one probability should be missing, got {missing_values}"
missing = 1 - sum(known.values())
assert abs(missing - 0.18) < 1e-9, f"the missing probability is {missing}"
assert 0 <= missing <= 1, "the recovered value must itself be a legal probability"
c.check(19, missing)                                  # 0.18

CALLS_FULL = dict(known)
CALLS_FULL[3] = missing
assert abs(sum(CALLS_FULL.values()) - 1.0) < 1e-12, "the completed distribution must total 1"

c.check(20, P(lambda x: x <= 1, CALLS_FULL))          # 0.34, uses none of the missing value
assert abs(P(lambda x: x <= 1, CALLS_FULL) - (CALLS[0] + CALLS[1])) < 1e-12
c.check(21, P(lambda x: x >= 3, CALLS_FULL))          # 0.35, uses the recovered value

# --- invalid distributions --------------------------------------------------------
short = [0.30, 0.25, 0.20, 0.15]
assert abs(sum(short) - 0.90) < 1e-12, "q22: these total 0.90, not 1"
assert all(0 <= v <= 1 for v in short), (
    "q22: each value is individually legal, so the sum is the only objection")

negative = [0.5, 0.4, -0.1]
assert any(v < 0 for v in negative), "q23: a negative probability is not legal"
assert abs(sum(negative) - 0.8) < 1e-12, (
    "q23: these also fail to sum to 1, which is why the key names the negative value "
    "as the decisive objection rather than the only one")

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.8.A.1: a random variable takes numerical values that come from a random phenomenon.")
c.conceptual(2, "EK 2.8.A.2: verified above -- the probabilities over all possible values sum to 1.")
c.conceptual(3, "EK 2.8.A.4: a discrete distribution may be shown as a graph, a table or a function.")
c.conceptual(4, "EK 2.8.A.5: a cumulative distribution gives P(X <= x) at each value.")
c.conceptual(5, "EK 2.8.A.1 with 1.2.C.1: a count of cars is discrete; times, masses, temperatures and lengths are continuous.")
c.conceptual(6, "EK 2.8.A.1 with 1.2.C.2: rainfall can take any value in an interval, while the alternatives are all counts.")
c.conceptual(18, "EK 2.8.A.5: verified above -- by the largest value all the probability has accumulated, so the last entry is 1.")
c.conceptual(22, "EK 2.8.A.2: computed above -- the four probabilities total 0.90, leaving 0.10 unaccounted for.")
c.conceptual(23, "EK 2.4.A.3 with 2.8.A.2: computed above -- a negative value is not a legal probability at all, which settles it before the sum is even considered.")
c.conceptual(24, "EK 2.8.A.3: a discrete distribution may be determined with the rules of probability or estimated by simulation.")
c.conceptual(25, "EK 2.8.A.5: verified above -- the two events differ by the single outcome X = 2, so the probabilities differ by exactly P(X = 2).")

c.finish()
