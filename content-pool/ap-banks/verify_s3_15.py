"""Verification for AP STATISTICS 3.15, carrying out a chi-square test.

Every table is parsed from the module and balance-checked first, then the whole
procedure is implemented FROM THE FORMULAS -- expected counts as row times
column over total, the statistic as the sum of (O - E) squared over E, the
degrees of freedom as (r - 1)(c - 1), the p-value as a right-tail area -- and
every result is cross-checked against `scipy.stats.chi2_contingency`. Two
independent routes must agree before anything is compared with a key, which is
what stops a hand-rolled formula and a hand-written answer from being wrong the
same way.

Two properties are asserted for every table beyond the numbers themselves:

* the expected counts reproduce the table's own margins exactly -- each row of
  expected counts sums to that row's total and each column to its column total.
  That is a strong check: it fails on almost any error in the expected-count
  formula, including the common one of dividing by the wrong total;

* the p-value is taken from the upper tail only. `right_tail_only` confirms on
  every table that doubling would give a different number, which is what makes
  q19 a real item rather than a restatement.

Run: python3 verify_s3_15.py
"""
import numpy as np
from scipy.stats import chi2, chi2_contingency

import s_verify_util as U

import s3_15

c = U.Checker(s3_15)


def parse(table):
    """Observed counts as a list of rows, with the Total row and column dropped."""
    body = [r for r in table["rows"] if r[0].lower() != "total"]
    total_row = [r for r in table["rows"] if r[0].lower() == "total"][0]

    observed = [[int(v) for v in row[1:-1]] for row in body]
    row_totals = [int(row[-1]) for row in body]
    col_totals = [int(v) for v in total_row[1:-1]]
    grand = int(total_row[-1])

    for i, row in enumerate(observed):
        assert sum(row) == row_totals[i], f"row {i} does not balance"
    for j, col_total in enumerate(col_totals):
        assert sum(row[j] for row in observed) == col_total, f"column {j} does not balance"
    assert sum(row_totals) == sum(col_totals) == grand, "margins must match the grand total"
    return observed, row_totals, col_totals, grand


def expected_counts(observed, row_totals, col_totals, grand):
    """EK 3.15.A.1, from the formula."""
    return [[row_totals[i] * col_totals[j] / grand for j in range(len(col_totals))]
            for i in range(len(row_totals))]


def chi_square(observed, expected):
    """EK 3.15.B.1, from the formula."""
    return sum((observed[i][j] - expected[i][j]) ** 2 / expected[i][j]
               for i in range(len(observed)) for j in range(len(observed[0])))


def analyse(table):
    """Everything about one table, by formula and by scipy, cross-checked."""
    observed, row_totals, col_totals, grand = parse(table)
    expected = expected_counts(observed, row_totals, col_totals, grand)
    stat = chi_square(observed, expected)
    df = (len(row_totals) - 1) * (len(col_totals) - 1)
    p = float(chi2.sf(stat, df))

    # The expected counts must reproduce the table's own margins.
    for i, row in enumerate(expected):
        assert abs(sum(row) - row_totals[i]) < 1e-9, (
            f"expected row {i} sums to {sum(row)}, not the row total {row_totals[i]}")
    for j, col_total in enumerate(col_totals):
        got = sum(row[j] for row in expected)
        assert abs(got - col_total) < 1e-9, (
            f"expected column {j} sums to {got}, not the column total {col_total}")
    assert abs(sum(sum(r) for r in expected) - grand) < 1e-9

    # Cross-check the whole thing against scipy.
    sp_stat, sp_p, sp_df, sp_expected = chi2_contingency(np.array(observed), correction=False)
    assert abs(stat - float(sp_stat)) < 1e-9, f"statistic: {stat} against scipy's {sp_stat}"
    assert df == int(sp_df), f"df: {df} against scipy's {sp_df}"
    assert abs(p - float(sp_p)) < 1e-12, f"p-value: {p} against scipy's {sp_p}"
    assert np.allclose(np.array(expected), sp_expected), "expected counts disagree with scipy"

    return observed, expected, stat, df, p


T1 = analyse(s3_15.TABLE_T1)
T2 = analyse(s3_15.TABLE_T2)
T3 = analyse(s3_15.TABLE_T3)

# --- table T1, 2 x 2 -----------------------------------------------------------------
obs1, exp1, stat1, df1, p1 = T1
c.check(4, exp1[0][0], tol=0.002)                                    # 52.5
c.check(5, exp1[0][1], tol=0.002)                                    # 47.5
c.check(6, (obs1[0][0] - exp1[0][0]) ** 2 / exp1[0][0], tol=0.002)   # 1.071
c.check(7, stat1, tol=0.002)                                         # 4.511
c.check(8, df1)                                                      # 1
c.check(9, p1, tol=0.0005)                                           # 0.0337
assert p1 <= 0.05, "q10: the null is rejected at the 5% level"
assert abs(exp1[0][0] - 100 * 105 / 200) < 1e-12

# --- table T2, 3 x 3 -----------------------------------------------------------------
obs2, exp2, stat2, df2, p2 = T2
c.check(11, exp2[0][1], tol=0.005)                                   # 36.67
c.check(12, exp2[2][0], tol=0.005)                                   # 30.00
c.check(13, df2)                                                     # 4
c.check(14, stat2, tol=0.002)                                        # 16.349
c.check(15, p2, tol=0.0005)                                          # 0.0026
# Every row total is 100, so every cell in a column shares an expected count.
assert len({round(exp2[i][1], 9) for i in range(3)}) == 1, (
    "with equal row totals, a column's expected counts are all equal")
assert abs(float(chi2.ppf(0.95, 4)) - 9.488) < 0.001, (
    "q14: 9.488 is the 5% critical value at df 4, offered as a distractor")

# --- table T3, 3 x 2 -----------------------------------------------------------------
obs3, exp3, stat3, df3, p3 = T3
c.check(16, exp3[0][0], tol=0.005)                                   # 23.33
c.check(17, [df3, stat3], tol=0.002)                                 # 2 and 9.375
c.check(18, p3, tol=0.0005)                                          # 0.0092
assert abs(float(chi2.ppf(0.95, 2)) - 5.991) < 0.001, (
    "q17: 5.992 is the 5% critical value at df 2, offered as a distractor")


def right_tail_only():
    """q3, q19: the p-value is an upper-tail area and is never doubled."""
    for stat, df, p in ((stat1, df1, p1), (stat2, df2, p2), (stat3, df3, p3)):
        assert abs(p - float(chi2.sf(stat, df))) < 1e-12, "the p-value is the right tail"
        assert abs(p - (1 - float(chi2.cdf(stat, df)))) < 1e-12, "equivalently 1 minus the cdf"
        assert 2 * p != p, "doubling would give a different number"
        assert 2 * p > p, "and a larger one, which is why the error matters"
        # A left-tail p-value would be nonsense here: it is large exactly when
        # the data agree with the null.
        left = float(chi2.cdf(stat, df))
        assert left > 0.9, "the left-tail area is large for these significant results"
        assert left != p


def zero_statistic_gives_p_one():
    """q25: perfect agreement gives a statistic of 0 and a p-value of 1."""
    for df in (1, 2, 4, 8):
        assert float(chi2.sf(0.0, df)) == 1.0, (
            "the whole chi-square distribution lies at or above 0")
    # Constructed: a table whose observed counts equal its expected counts.
    perfect = [[30, 30], [30, 30]]
    exp = expected_counts(perfect, [60, 60], [60, 60], 120)
    assert exp == [[30.0, 30.0], [30.0, 30.0]], f"expected counts are {exp}"
    assert chi_square(perfect, exp) == 0.0
    assert float(chi2.sf(0.0, 1)) == 1.0
    c.check(25, 1)


def doubling_the_counts():
    """q24: doubling every count doubles the statistic and leaves df alone."""
    observed, row_totals, col_totals, grand = parse(s3_15.TABLE_T1)
    doubled = [[2 * v for v in row] for row in observed]
    exp_d = expected_counts(doubled, [2 * t for t in row_totals],
                            [2 * t for t in col_totals], 2 * grand)
    stat_d = chi_square(doubled, exp_d)

    assert abs(stat_d - 2 * stat1) < 1e-9, (
        f"the statistic must double: {stat_d} against 2 x {stat1}")
    df_d = (len(row_totals) - 1) * (len(col_totals) - 1)
    assert df_d == df1, "the degrees of freedom are unchanged"
    assert float(chi2.sf(stat_d, df_d)) < p1, "so the p-value falls"

    # Each expected count doubles too, which is why each contribution doubles.
    for i in range(len(observed)):
        for j in range(len(observed[0])):
            assert abs(exp_d[i][j] - 2 * exp1[i][j]) < 1e-9


def largest_contribution():
    """q20: the cell contributing most is the largest (O - E)^2 / E, not the largest count."""
    contributions = {(i, j): (obs2[i][j] - exp2[i][j]) ** 2 / exp2[i][j]
                     for i in range(3) for j in range(3)}
    biggest_contrib = max(contributions, key=contributions.get)
    biggest_observed = max(((i, j) for i in range(3) for j in range(3)),
                           key=lambda ij: obs2[ij[0]][ij[1]])
    assert biggest_contrib != biggest_observed, (
        "on this table the largest contribution does NOT come from the largest observed "
        "count, which is exactly what makes the distractor wrong")
    assert abs(sum(contributions.values()) - stat2) < 1e-9, (
        "the contributions must sum to the statistic")


right_tail_only()
zero_statistic_gives_p_one()
doubling_the_counts()
largest_contribution()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 3.15.A.1: verified above -- the row-times-column-over-total formula reproduces every margin of every table exactly.")
c.conceptual(2, "EK 3.15.B.1: squaring stops discrepancies cancelling and dividing by the expected count makes each contribution relative to how many were expected.")
c.conceptual(3, "EK 3.15.B.2: verified above -- the p-value is the upper-tail area, and the left tail is large precisely when the data agree with the null.")
c.conceptual(10, "EK 3.15.D.1: computed above -- 0.0337 falls below 0.05, so the null is rejected.")
c.conceptual(19, "EK 3.15.B.2: verified above -- departures in any direction are squared and added, so all the evidence lies in one tail and doubling would give a different, wrong number.")
c.conceptual(20, "EK 3.15.B.1: computed above -- on table T2 the largest cell contribution does not come from the largest observed count.")
c.conceptual(21, "EK 3.15.C.1: the p-value is computed assuming the null is true and concerns statistics at least as large as the one observed, stated in context.")
c.conceptual(22, "EK 3.15.D.2: the test establishes that some difference exists, without identifying which groups differ, ranking them, or supporting causation.")
c.conceptual(23, "EK 3.15.D.1: a large p-value leaves the null unrejected, which is not the same as establishing that the distributions are identical.")
c.conceptual(24, "EK 3.15.B.1: computed above -- doubling every count doubles every expected count and every contribution, doubling the statistic while the degrees of freedom stay put.")

c.finish()
