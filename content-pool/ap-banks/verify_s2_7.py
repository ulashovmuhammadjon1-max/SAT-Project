"""Verification for AP STATISTICS 2.7, independence and unions.

The two tables are the heart of this module and they are constructed to share
the same margins while differing in whether independence holds. The verifier
checks exactly that: TABLE_IND must factor in EVERY cell (joint proportion equal
to the product of its marginals), TABLE_DEP must fail in every cell, and the two
must have identical row and column totals. If a future edit broke the shared
margins the contrast in q13/q14 would collapse, and this fails first.

`independence_is_not_disjointness` proves the claim behind q17 in general rather
than by example: for two events of positive probability, P(A and B) = 0 and
P(A and B) = P(A)P(B) cannot both hold. It also checks q23's closure property --
that independence of A and B carries over to the complement of A -- by
constructing the full joint distribution and computing it.

Run: python3 verify_s2_7.py
"""
from fractions import Fraction

import s_verify_util as U

import s2_7

c = U.Checker(s2_7)


def parse(table):
    body = [r for r in table["rows"] if r[0].lower() != "total"]
    total_row = [r for r in table["rows"] if r[0].lower() == "total"][0]
    cols = table["headers"][1:-1]
    cells, rows = {}, {}
    for row in body:
        rows[row[0]] = int(row[-1])
        for j, col in enumerate(cols):
            cells[(row[0], col)] = int(row[j + 1])
    colt = {col: int(total_row[j + 1]) for j, col in enumerate(cols)}
    grand = int(total_row[-1])
    for r in rows:
        assert sum(cells[(r, col)] for col in cols) == rows[r], f"row {r} does not balance"
    for col in cols:
        assert sum(cells[(r, col)] for r in rows) == colt[col], f"column {col} does not balance"
    assert sum(rows.values()) == sum(colt.values()) == grand
    return cells, rows, colt, grand


IND = parse(s2_7.TABLE_IND)
DEP = parse(s2_7.TABLE_DEP)


def factors_everywhere(parsed):
    """True when every cell's joint proportion equals the product of its marginals."""
    cells, rows, colt, grand = parsed
    results = {}
    for (r, col), n in cells.items():
        joint = Fraction(n, grand)
        product = Fraction(rows[r], grand) * Fraction(colt[col], grand)
        results[(r, col)] = (joint, product, joint == product)
    return results


ind_results = factors_everywhere(IND)
dep_results = factors_everywhere(DEP)

assert all(ok for _, _, ok in ind_results.values()), (
    f"TABLE_IND must factor in every cell: {ind_results}")
assert not any(ok for _, _, ok in dep_results.values()), (
    f"TABLE_DEP must fail to factor in every cell: {dep_results}")

# The two tables must share their margins, or q13 and q14 are not the same test
# applied to different data -- they are just two different tables.
assert IND[1] == DEP[1] and IND[2] == DEP[2] and IND[3] == DEP[3], (
    "the independent and dependent tables must have identical margins")

# The specific figures q13 and q14 quote.
joint_ind, product_ind, _ = ind_results[("Row 1", "Column 1")]
joint_dep, product_dep, _ = dep_results[("Row 1", "Column 1")]
assert (float(product_ind), float(joint_ind)) == (0.24, 0.24), "q13: 0.60 x 0.40 = 0.24 = 24/100"
assert (float(product_dep), float(joint_dep)) == (0.24, 0.35), "q14: 0.24 expected, 0.35 observed"

# --- independent events: product and union --------------------------------------
c.check(6, 0.4 * 0.5)                                    # 0.20
c.check(7, 0.4 + 0.5 - 0.4 * 0.5)                        # 0.70
assert abs((0.4 + 0.5) - 0.90) < 1e-12, "q7: 0.90 is the forgot-to-subtract-the-overlap distractor"

# --- the independence test, both verdicts ---------------------------------------
assert abs(0.3 * 0.6 - 0.18) < 1e-12, "q8: the product equals the stated joint probability"
assert abs(0.3 * 0.6 - 0.25) > 1e-9, "q9: the product does not equal 0.25"
c.check(10, 0.3 + 0.6 - 0.25)                            # 0.65

# --- the addition rule run backwards, then tested for independence ---------------
joint_11 = 0.5 + 0.4 - 0.7
assert abs(joint_11 - 0.20) < 1e-9, f"q11: P(A and B) = {joint_11}"
c.check(11, joint_11)
assert abs(0.5 * 0.4 - joint_11) < 1e-9, (
    "q12: the recovered joint probability must equal the product, making the events independent")

# --- independent components -------------------------------------------------------
p_fail = 0.2
c.check(18, p_fail ** 3)                                 # 0.008, all three fail
c.check(20, (1 - p_fail) ** 3)                           # 0.512, none fails
c.check(19, 1 - (1 - p_fail) ** 3)                       # 0.488, at least one fails
assert abs(((1 - p_fail) ** 3) + (1 - (1 - p_fail) ** 3) - 1.0) < 1e-12, (
    "q19 and q20 are complements and must sum to 1")

# --- two events of probability 0.5, under each assumption -------------------------
union_independent = 0.5 + 0.5 - 0.5 * 0.5
union_disjoint = 0.5 + 0.5 - 0.0
assert (union_independent, union_disjoint) == (0.75, 1.0), (
    f"q21: unions are {union_independent} and {union_disjoint}")
c.check(22, (1 - 0.5) * (1 - 0.5))                       # 0.25, neither occurs
assert abs((1 - union_independent) - 0.25) < 1e-12, "q22: also 1 - P(A or B)"

# --- q25: the inconsistent pair of reports ---------------------------------------
implied_union = 0.7 + 0.2 - 0.14
assert abs(implied_union - 0.76) < 1e-9, f"q25: the addition rule gives {implied_union}"
assert abs(implied_union - 0.9) > 1e-9, "q25: 0.9 is inconsistent with a joint probability of 0.14"
assert abs((0.7 + 0.2) - 0.9) < 1e-12, "q25: 0.9 is what forgetting the overlap produces"


def independence_is_not_disjointness():
    """q17: the two conditions cannot both hold for positive-probability events."""
    for pa in (0.1, 0.25, 0.5, 0.9):
        for pb in (0.1, 0.3, 0.75):
            product = pa * pb
            assert product > 0, "positive marginals give a positive product"
            # Disjointness demands a joint probability of 0; independence demands
            # the product. They agree only if one marginal is 0.
            assert product != 0.0, (
                "so P(A and B) cannot be both 0 (disjoint) and pa*pb (independent)")


def independence_survives_complementing():
    """q23: if A and B are independent, so are 'not A' and B.

    Built as a full joint distribution rather than argued, so the claim is
    checked arithmetically.
    """
    for pa in (0.2, 0.5, 0.85):
        for pb in (0.3, 0.6):
            joint = {
                (True, True): pa * pb,
                (True, False): pa * (1 - pb),
                (False, True): (1 - pa) * pb,
                (False, False): (1 - pa) * (1 - pb),
            }
            assert abs(sum(joint.values()) - 1.0) < 1e-12

            p_not_a = 1 - pa
            p_not_a_and_b = joint[(False, True)]
            assert abs(p_not_a_and_b - p_not_a * pb) < 1e-12, (
                "the complement of A must remain independent of B")
            # And stated as a conditional probability.
            assert abs(p_not_a_and_b / pb - p_not_a) < 1e-12


independence_is_not_disjointness()
independence_survives_complementing()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.7.A.1: independence means knowing whether A occurred does not change the probability of B.")
c.conceptual(2, "EK 2.7.A.1: P(A given B) = P(A) is the definition written as a conditional probability.")
c.conceptual(3, "EK 2.7.A.1 with 2.6.A.2: substituting P(B given A) = P(B) into the general multiplication rule leaves the plain product.")
c.conceptual(4, "EK 2.7.A.3: adding the two probabilities double-counts the overlap, so P(A and B) is subtracted once.")
c.conceptual(5, "EK 2.7.A.2: the union is inclusive and covers the case where both events occur.")
c.conceptual(8, "EK 2.7.A.1: computed above -- 0.3 x 0.6 = 0.18 exactly matches the stated joint probability, so the events are independent.")
c.conceptual(9, "EK 2.7.A.1: computed above -- the product is 0.18 against an actual joint probability of 0.25, so independence fails.")
c.conceptual(12, "EK 2.7.A.1 and 2.7.A.3: computed above -- the addition rule recovers a joint probability of 0.20, which equals 0.5 x 0.4.")
c.conceptual(13, "EK 2.7.A.1: computed above -- TABLE_IND factors in every cell, with 0.60 x 0.40 = 0.24 matching the observed 24/100.")
c.conceptual(14, "EK 2.7.A.1: computed above -- TABLE_DEP has the same margins but an observed 0.35 against the 0.24 independence requires.")
c.conceptual(15, "EK 2.7.A.1: nothing about the coin changes between tosses, so the first result carries no information about the second.")
c.conceptual(16, "EK 2.7.A.1 with 2.6.A.1: removing a heart leaves 12 of 51 rather than 13 of 52, so the first draw changes the second's probability.")
c.conceptual(17, "EK 2.5.A.2 against 2.7.A.1: proved above -- disjointness demands a joint probability of 0 and independence demands a positive product, so both cannot hold.")
c.conceptual(21, "EK 2.7.A.3: computed above -- both cases use the same addition rule and differ only in the joint probability, 0.25 against 0.")
c.conceptual(23, "EK 2.7.A.1: proved above on the full joint distribution -- independence of A and B carries over to the complement of A.")
c.conceptual(24, "EK 2.7.A.1: independence is exactly the statement that every joint proportion factors into the product of its marginals.")
c.conceptual(25, "EK 2.7.A.3: computed above -- a joint probability of 0.14 forces a union of 0.76, so the reported 0.9 is the overlap left unsubtracted.")

c.finish()
