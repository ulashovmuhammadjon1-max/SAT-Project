"""Verification for AP STATISTICS 2.2, joint, marginal and conditional relative frequencies.

Table X is parsed and balance-checked before anything is keyed off it, then all
three families of summary are recomputed with the denominator each definition
requires:

    joint       cell / grand total
    marginal    margin total / grand total
    conditional cell / that row's or that column's total

The distinguishing check is on q15: the same cell, 144, is required to give
three DIFFERENT answers as a joint, a row-conditional and a column-conditional,
and the verifier asserts all three are pairwise distinct. If a future edit made
any two of them coincide the item would lose its point, and this fails.

The expected-count items (q20, q21) are computed as row total x marginal
proportion, and the direction of the discrepancy is asserted, not just its size.

Run: python3 verify_s2_2.py
"""
import s_verify_util as U

import s2_2

c = U.Checker(s2_2)


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
    assert sum(rows.values()) == sum(colt.values()) == grand, "margins must match the grand total"
    return cells, rows, colt, grand


X, Xrow, Xcol, N = parse(s2_2.TABLE_X)
FC, RR, PASS, FAIL = "Flashcards", "Rereading", "Passed", "Failed"

# --- joint --------------------------------------------------------------------
c.check(6, X[(FC, PASS)] / N)            # 144/300 = 0.48
c.check(7, X[(RR, FAIL)] / N)            #  54/300 = 0.18

# --- marginal -----------------------------------------------------------------
c.check(8, Xrow[FC] / N)                 # 180/300 = 0.60
c.check(9, Xcol[PASS] / N)               # 210/300 = 0.70
c.check(17, Xcol[FAIL] / N)              #  90/300 = 0.30

# --- conditional --------------------------------------------------------------
c.check(10, X[(FC, PASS)] / Xrow[FC])    # 144/180 = 0.80
c.check(11, X[(RR, PASS)] / Xrow[RR])    #  66/120 = 0.55
c.check(12, X[(FC, PASS)] / Xcol[PASS])  # 144/210 = 0.686
c.check(13, X[(FC, FAIL)] / Xcol[FAIL])  #  36/90  = 0.40
c.check(14, X[(FC, FAIL)] / Xrow[FC])    #  36/180 = 0.20

# --- the sums -----------------------------------------------------------------
joint = [X[(r, col)] / N for r in Xrow for col in (PASS, FAIL)]
assert abs(sum(joint) - 1.0) < 1e-12, f"the four joint relative frequencies sum to {sum(joint)}"
assert sorted(round(j, 2) for j in joint) == [0.12, 0.18, 0.22, 0.48], (
    f"q16: the four joint relative frequencies should be 0.48, 0.12, 0.22, 0.18; got {joint}")
c.check(16, sum(joint))                  # 1.00


def same_cell_three_ways():
    """q15: one numerator, three denominators, three different answers."""
    cell = X[(FC, PASS)]
    as_joint = cell / N
    as_row_conditional = cell / Xrow[FC]
    as_col_conditional = cell / Xcol[PASS]
    values = [as_joint, as_row_conditional, as_col_conditional]

    assert len(set(round(v, 10) for v in values)) == 3, (
        f"q15 loses its point unless all three differ; got {values}")
    assert abs(as_joint - 0.48) < 1e-12
    assert abs(as_row_conditional - 0.80) < 1e-12
    assert abs(as_col_conditional - 144 / 210) < 1e-12
    # And the numerator really is the same in all three.
    assert cell == 144


def conditional_sums():
    """q23, q24: conditionals sum to 1 within a level, not across levels."""
    within_fc = [X[(FC, col)] / Xrow[FC] for col in (PASS, FAIL)]
    within_rr = [X[(RR, col)] / Xrow[RR] for col in (PASS, FAIL)]
    assert abs(sum(within_fc) - 1.0) < 1e-12, "passing and failing exhaust the flashcards group"
    assert abs(sum(within_rr) - 1.0) < 1e-12, "and the rereading group"
    assert within_fc == [0.80, 0.20] and within_rr == [0.55, 0.45]

    # Across levels there is no reason to sum to 1, and here the sum exceeds it.
    across = X[(FC, PASS)] / Xrow[FC] + X[(RR, PASS)] / Xrow[RR]
    assert abs(across - 1.35) < 1e-12, f"q23: 0.80 + 0.55 = {across}"
    assert across > 1.0, "q23: the key explains why a sum above 1 is not an error here"

    # q24: the only pair among the options that genuinely sums to 1.
    assert abs(sum(within_fc) - 1.0) < 1e-12
    assert abs(Xrow[FC] / N + Xcol[PASS] / N - 1.0) > 0.2, (
        "q24: 'used flashcards' and 'passed' come from different variables and must not sum to 1")


def expected_counts_under_no_association():
    """q19, q20, q21: what independence would predict, and which way it misses."""
    marginal_pass = Xcol[PASS] / N
    assert abs(marginal_pass - 0.70) < 1e-12

    # q19: under no association every group's passing rate equals the marginal.
    for r in Xrow:
        expected_rate = marginal_pass
        assert 0 < expected_rate < 1
    assert abs(X[(FC, PASS)] / Xrow[FC] - marginal_pass) > 0.05, (
        "q19: the observed rate must differ from the marginal, or there is no association to see")

    # q20: expected count = row total x marginal proportion.
    expected = Xrow[FC] * marginal_pass
    assert abs(expected - 126.0) < 1e-9, f"q20: expected count is {expected}"

    # q21: the observed count exceeds the expected count.
    assert X[(FC, PASS)] > expected, "q21: 144 must exceed the 126 expected"
    assert abs((X[(FC, PASS)] - expected) - 18.0) < 1e-9, "q21: the excess is 18 students"

    # The same conclusion must follow from the conditional proportions, or the
    # module would be telling two different stories about one table.
    assert (X[(FC, PASS)] / Xrow[FC]) > (X[(RR, PASS)] / Xrow[RR]), (
        "q18 and q21 must agree on the direction of the association")


expected_counts_under_no_association()
same_cell_three_ways()
conditional_sums()
c.check(20, Xrow[FC] * (Xcol[PASS] / N))   # 126

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.2.A.1: a joint relative frequency is a cell frequency divided by the grand total.")
c.conceptual(2, "EK 2.2.A.2: a marginal relative frequency is a row or column total divided by the grand total.")
c.conceptual(3, "EK 2.2.A.3: a conditional relative frequency restricts to one row or column and divides by that level's total.")
c.conceptual(4, "EK 2.2.A.1: verified above -- the four joint relative frequencies of this table sum to exactly 1.")
c.conceptual(5, "EK 2.2.A.3: verified above -- within the flashcards row the conditionals 0.80 and 0.20 sum to 1.")
c.conceptual(15, "EK 2.2.A.1 through 2.2.A.3: verified above -- the same numerator 144 over three different denominators gives three distinct values.")
c.conceptual(18, "EK 2.2.B.1: computed above -- the conditional passing rate changes from 0.80 to 0.55 across study methods, which is evidence of association, not of causation.")
c.conceptual(19, "EK 2.2.B.1: under no association each group's conditional distribution equals the overall marginal distribution, which here is 0.70.")
c.conceptual(21, "EK 2.2.B.1: computed above -- 144 observed against 126 expected is an excess of 18, so the cell is over-represented relative to independence.")
c.conceptual(22, "EK 2.2.A.3: the phrase 'of flashcard users' names the conditioning group, which fixes the denominator at 180 rather than 300.")
c.conceptual(23, "EK 2.2.A.3: computed above -- 0.80 and 0.55 belong to two different conditional distributions, so their sum of 1.35 carries no meaning.")
c.conceptual(24, "EK 2.2.A.3: verified above -- only passing and failing within the flashcards group exhaust one whole, giving 0.80 + 0.20 = 1.")
c.conceptual(25, "EK 2.2.C.1 with 1.13.A.7: the data show a higher pass rate among flashcard users, but with no random assignment the groups may differ in ability.")

c.finish()
