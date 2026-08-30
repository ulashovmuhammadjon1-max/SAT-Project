"""Verification for AP STATISTICS 2.1, two-way tables and their displays.

Both tables are parsed out of the module and checked for internal consistency
first: every row must sum to its own row total, every column to its column
total, and both sets of margins to the same grand total. A two-way table that
does not balance would make several keys unanswerable at once, so this runs
before anything is checked against it.

Every count and proportion keyed in the module is then recomputed from the
parsed table. The association items are checked by computing both conditional
distributions and asserting they differ for table W and are equal for table Y --
so the contrast the module is built on is confirmed numerically, not assumed.

Run: python3 verify_s2_1.py
"""
import s_verify_util as U

import s2_1

c = U.Checker(s2_1)


def parse(table):
    """(cells, row_totals, col_totals, grand) from a module two-way table."""
    body = [r for r in table["rows"] if r[0].lower() != "total"]
    total_row = [r for r in table["rows"] if r[0].lower() == "total"][0]
    col_names = table["headers"][1:-1]

    cells = {}
    row_totals = {}
    for row in body:
        name = row[0]
        row_totals[name] = int(row[-1])
        for j, col in enumerate(col_names):
            cells[(name, col)] = int(row[j + 1])

    col_totals = {col: int(total_row[j + 1]) for j, col in enumerate(col_names)}
    grand = int(total_row[-1])

    # Internal consistency.
    for name in row_totals:
        s = sum(cells[(name, col)] for col in col_names)
        assert s == row_totals[name], f"row {name}: cells sum to {s}, total says {row_totals[name]}"
    for col in col_names:
        s = sum(cells[(name, col)] for name in row_totals)
        assert s == col_totals[col], f"column {col}: cells sum to {s}, total says {col_totals[col]}"
    assert sum(row_totals.values()) == grand, "row totals must sum to the grand total"
    assert sum(col_totals.values()) == grand, "column totals must sum to the grand total"
    return cells, row_totals, col_totals, grand


W, Wrow, Wcol, Wn = parse(s2_1.TABLE_W)
Y, Yrow, Ycol, Yn = parse(s2_1.TABLE_Y)

PET, NOPET = "Owns a pet", "Does not own a pet"
APT, HOUSE = "Apartment", "House"

# --- counts read straight from the table --------------------------------------
c.check(5, W[(APT, PET)])                       # 48
c.check(6, Wrow[HOUSE])                         # 300
c.check(7, Wcol[PET])                           # 210
c.check(13, W[(HOUSE, NOPET)])                  # 138
c.check(24, sum(W.values()))                    # 48+152+162+138 = 500

# --- joint, marginal and conditional proportions ------------------------------
c.check(8, W[(APT, PET)] / Wn)                  # joint       48/500 = 0.096
c.check(9, Wrow[APT] / Wn)                      # marginal   200/500 = 0.40
c.check(10, W[(APT, PET)] / Wrow[APT])          # cond.       48/200 = 0.24
c.check(11, W[(HOUSE, PET)] / Wrow[HOUSE])      # cond.      162/300 = 0.54
c.check(12, W[(APT, PET)] / Wcol[PET])          # cond.       48/210 = 0.229
c.check(14, Wcol[NOPET] / Wn)                   # marginal   290/500 = 0.58

# The two conditional directions are genuinely different questions, and q10 and
# q12 are keyed to different numbers precisely because of that.
assert W[(APT, PET)] / Wrow[APT] != W[(APT, PET)] / Wcol[PET], (
    "q10 and q12 condition on different variables and must not share an answer")
assert abs(Wcol[NOPET] / Wn + Wcol[PET] / Wn - 1.0) < 1e-12, (
    "q14: the two marginal proportions must complement to 1")


def association_contrast():
    """Table W shows association; table Y does not. Both are computed."""
    # W: the conditional distributions of pet ownership across housing type.
    cond_w = {row: W[(row, PET)] / Wrow[row] for row in Wrow}
    assert cond_w == {APT: 0.24, HOUSE: 0.54}, f"W conditionals are {cond_w}"
    assert abs(cond_w[HOUSE] - cond_w[APT]) > 0.25, (
        "q15: the two conditional proportions must differ substantially")

    # Y: identical conditional distributions despite unequal counts and sizes.
    cond_y = {row: Y[(row, "Yes")] / Yrow[row] for row in Yrow}
    assert set(cond_y.values()) == {0.30}, f"Y conditionals are {cond_y}"
    assert Y[("Group 2", "Yes")] == 2 * Y[("Group 1", "Yes")], (
        "q17: the raw yes counts differ by a factor of two")
    assert Yrow["Group 2"] == 2 * Yrow["Group 1"], (
        "q17: and the group sizes differ by the same factor, which is why the counts mislead")

    # q18: no association means every segmented bar has the same composition.
    for row in Yrow:
        segments = [Y[(row, col)] / Yrow[row] for col in ("Yes", "No")]
        assert abs(sum(segments) - 1.0) < 1e-12, "each bar's segments must sum to 1"
    bars = [tuple(round(Y[(row, col)] / Yrow[row], 10) for col in ("Yes", "No")) for row in Yrow]
    assert len(set(bars)) == 1, f"q18: with no association every bar is identical, got {bars}"

    # And under association the bars are NOT identical, which is the contrast.
    bars_w = [tuple(round(W[(row, col)] / Wrow[row], 10) for col in (PET, NOPET)) for row in Wrow]
    assert len(set(bars_w)) == 2, "q18/q15: table W's bars must differ from each other"


def claim_about_pet_owners():
    """q21: among pet owners, most live in a house."""
    share = W[(HOUSE, PET)] / Wcol[PET]
    assert abs(share - 162 / 210) < 1e-12
    assert share > 0.5, "q21: 'most' requires more than half"
    assert 0.76 < share < 0.78, f"q21: the key says about 77%, computed {share:.4f}"
    # The distractor reasoning '162 exceeds 152' compares cells from different
    # columns, which is not the comparison the claim is about.
    assert W[(HOUSE, PET)] == 162 and W[(APT, NOPET)] == 152


association_contrast()
claim_about_pet_owners()

# --- conceptual keys ---------------------------------------------------------
c.conceptual(1, "EK 2.1.A.1: a two-way, or contingency, table cross-classifies units by two categorical variables.")
c.conceptual(2, "EK 2.1.A.1: the cells of a two-way table may hold frequencies or relative frequencies.")
c.conceptual(3, "EK 2.1.A.2: side-by-side bar charts, segmented bar charts and mosaic plots display two categorical variables; a histogram displays one quantitative variable.")
c.conceptual(4, "EK 2.1.A.2: a segmented bar of relative frequencies pictures one conditional distribution, so its segments sum to 1.")
c.conceptual(15, "EK 2.1.A.3: computed above -- conditional proportions of 0.24 and 0.54 differ substantially, which is what association between two categorical variables looks like.")
c.conceptual(16, "EK 2.1.A.3: computed above -- both conditional proportions are exactly 0.30, so there is no apparent association despite the unequal counts.")
c.conceptual(17, "EK 2.1.A.3: computed above -- Group 2 is twice the size of Group 1, so twice as many yes answers is exactly what identical rates produce.")
c.conceptual(18, "EK 2.1.A.2 and 2.1.A.3: computed above -- with no association every segmented bar has the same composition, and table W's two bars differ.")
c.conceptual(19, "EK 2.1.A.2: side-by-side and segmented bar charts carry the same information and differ only in placing the bars alongside or stacking them.")
c.conceptual(20, "EK 2.1.A.2: a mosaic plot scales column width by the marginal relative frequency and height by the conditional distribution, so area is the joint relative frequency.")
c.conceptual(21, "EK 2.1.B.1: computed above -- 162 of the 210 pet owners, about 77%, live in a house, so 'most' is correct.")
c.conceptual(22, "EK 2.1.A.3 with 1.13.A.7: a two-way table shows association only; with no random assignment, confounders such as living space remain available explanations.")
c.conceptual(23, "EK 2.1.A.1: verified above for both tables -- each unit is counted in exactly one row and one column, so both sets of margins sum to the same grand total.")
c.conceptual(25, "EK 2.1.A.3: conditional distributions put levels of different sizes on the same footing, which is what makes them the fair basis for judging association.")

c.finish()
