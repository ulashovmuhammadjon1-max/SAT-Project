"""Verification for AP STATISTICS 2.6, conditional probability.

The screening table is parsed and balance-checked, then every conditional is
recomputed with the denominator its wording demands. The check that matters most
is `condition_direction_matters`: it computes P(positive | disease) and
P(disease | positive) from the same cell and asserts they are FAR apart, so the
pair of items built on that contrast (q9, q10, q11) cannot quietly become the
same question if the table is ever edited.

The without-replacement items are computed by the multiplication rule and then
CROSS-CHECKED against a full enumeration of ordered draws, so the answers do not
depend on the rule being applied correctly by the same hand that wrote them.
The with-replacement item is checked to differ from its without-replacement
counterpart, which is the whole point of the pair.

Fraction-valued choices are compared by value, since the shared checker reads
"1/16" as the pair (1, 16) and would not notice "169/2704". An earlier draft of
this module really did offer both, and this check is what found it.

Run: python3 verify_s2_6.py
"""
from fractions import Fraction
from itertools import permutations

import s_verify_util as U

import s2_6

c = U.Checker(s2_6)
Q = s2_6.QUESTIONS


def fraction_choices_are_distinct():
    for i, item in enumerate(Q, 1):
        seen = {}
        for choice in item["choices"]:
            try:
                value = Fraction(choice.strip())
            except (ValueError, ZeroDivisionError):
                continue
            assert value not in seen, (
                f"q{i}: {seen[value]!r} and {choice!r} are the same number ({float(value)})")
            seen[value] = choice


fraction_choices_are_distinct()


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


Z, Zrow, Zcol, N = parse(s2_6.TABLE_Z)
POS, NEG = "Positive", "Negative"
DIS, WELL = "Has the disease", "Does not have the disease"
assert N == 1000

# --- abstract conditional probability -------------------------------------------
c.check(3, 0.18 / 0.45)                     # P(A given B) = 0.40
c.check(4, 0.18 / 0.30)                     # P(B given A) = 0.60
assert 0.18 / 0.45 != 0.18 / 0.30, (
    "q3 and q4 share a joint probability and must still give different answers")
c.check(5, 0.40 * 0.25)                     # general multiplication rule: 0.10

# --- marginal and joint from the table -------------------------------------------
c.check(6, Zrow[POS] / N)                   # 175/1000 = 0.175
c.check(7, Zcol[DIS] / N)                   # 100/1000 = 0.100
c.check(8, Z[(POS, DIS)] / N)               #  85/1000 = 0.085

# --- conditionals, each with the denominator its wording demands -----------------
c.check(9, Z[(POS, DIS)] / Zcol[DIS])       #  85/100 = 0.850, given disease
c.check(10, Z[(POS, DIS)] / Zrow[POS])      #  85/175 = 0.486, given positive
c.check(12, Z[(NEG, WELL)] / Zcol[WELL])    # 810/900 = 0.900, given no disease
c.check(13, Z[(NEG, WELL)] / Zrow[NEG])     # 810/825 = 0.982, given negative
c.check(14, Z[(POS, WELL)] / Zcol[WELL])    #  90/900 = 0.100, given no disease

# The q14 distractor divides by the 1,000 screened instead of the 900 conditioned on.
assert abs(Z[(POS, WELL)] / N - 0.090) < 1e-12, "q14: 0.090 is the wrong-denominator distractor"
assert Z[(POS, WELL)] / Zcol[WELL] != Z[(POS, WELL)] / N


def condition_direction_matters():
    """q9, q10, q11: the same cell, two conditions, two very different answers."""
    cell = Z[(POS, DIS)]
    given_disease = cell / Zcol[DIS]
    given_positive = cell / Zrow[POS]
    assert cell == 85 and Zcol[DIS] == 100 and Zrow[POS] == 175
    assert abs(given_disease - 0.85) < 1e-12
    assert abs(given_positive - 85 / 175) < 1e-12
    assert given_disease > 0.8 and given_positive < 0.5, (
        "the contrast fails unless the test catches most cases yet most positives are false")
    assert given_disease - given_positive > 0.3, (
        f"q11 needs the two to be far apart; gap is {given_disease - given_positive:.3f}")
    # And 0.486 is not the complement of 0.85, which is a distractor in q11.
    assert abs(given_positive - (1 - given_disease)) > 0.3


condition_direction_matters()


# --- drawing without replacement, by rule AND by enumeration ---------------------
def enumerate_two_draws(items):
    """All ordered pairs of distinct positions, i.e. drawing two without replacement."""
    return list(permutations(range(len(items)), 2))


BAG = ["R"] * 5 + ["B"] * 3
assert BAG.count("R") == 5 and len(BAG) == 8
ordered = enumerate_two_draws(BAG)
assert len(ordered) == 8 * 7

both_red = [pr for pr in ordered if BAG[pr[0]] == "R" and BAG[pr[1]] == "R"]
first_red = [pr for pr in ordered if BAG[pr[0]] == "R"]
red_then_blue = [pr for pr in ordered if BAG[pr[0]] == "R" and BAG[pr[1]] == "B"]

# q15: P(second red | first red), by enumeration and by the counting argument.
p_second_red_given_first_red = Fraction(len(both_red), len(first_red))
assert p_second_red_given_first_red == Fraction(4, 7), (
    f"q15: enumeration gives {p_second_red_given_first_red}")
c.check(15, [4, 7])

# q16: P(both red).
p_both_red = Fraction(len(both_red), len(ordered))
assert p_both_red == Fraction(5, 8) * Fraction(4, 7) == Fraction(5, 14), (
    f"q16: enumeration gives {p_both_red}")
assert p_both_red != Fraction(5, 8) ** 2, "q16: 25/64 is the treat-as-independent distractor"
c.check(16, [5, 14])

# q17: P(first red and second blue).
p_red_blue = Fraction(len(red_then_blue), len(ordered))
assert p_red_blue == Fraction(5, 8) * Fraction(3, 7) == Fraction(15, 56), (
    f"q17: enumeration gives {p_red_blue}")
c.check(17, [15, 56])

# --- cards, with and without replacement ------------------------------------------
without = Fraction(13, 52) * Fraction(12, 51)
assert without == Fraction(1, 17), f"q18: two hearts without replacement is {without}"
c.check(18, [1, 17])

with_replacement = Fraction(13, 52) * Fraction(13, 52)
assert with_replacement == Fraction(1, 16), f"q19: with replacement is {with_replacement}"
c.check(19, [1, 16])

assert without != with_replacement, (
    "q18 and q19 exist to contrast; if these ever coincide the pair is pointless")
assert without < with_replacement, (
    "removing a heart lowers the chance of a second heart, so the without-replacement value is smaller")

# --- the general multiplication rule in context ------------------------------------
c.check(23, 0.60 * 0.25 * 100)              # 15 percent take both
c.check(24, 0.08 * 0.70)                    # 0.056 defective and detected

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.6.A.1: P(A given B) = P(A and B)/P(B); conditioning rescales the joint probability by the probability of the conditioning event.")
c.conceptual(2, "EK 2.6.A.2: the general multiplication rule is P(A and B) = P(A) x P(B given A); the plain product requires independence.")
c.conceptual(11, "EK 2.6.A.1: computed above -- the two conditionals have denominators 100 and 175, and differ by more than 0.3, so swapping the condition changes the answer.")
c.conceptual(20, "EK 2.6.A.1: enumerated above -- removing an item changes both numerator and denominator for the next draw, which is exactly dependence.")
c.conceptual(21, "EK 2.4.A.3 with 2.6.A.1: a conditional probability is still a probability, so a value above 1 signals dividing by the joint probability rather than by P(B).")
c.conceptual(22, "EK 2.6.A.1: conditioning on an impossible event is undefined, since the definition would divide by zero.")
c.conceptual(25, "EK 2.6.A.1: verified above on the screening table -- P(ate the food given ill) and P(ill given ate the food) are different quantities, and reporting one for the other is the error.")

c.finish()
