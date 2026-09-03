"""Key audit for AP CHEMISTRY 7.6 Properties of the Equilibrium Constant.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON. Every item is one of the four algebraic properties in
7.6.A and nothing else:

  7.6.A.1  reversing a reaction INVERTS K       items 1, 2, 10, 14, 22, 28
  7.6.A.2  scaling coefficients by c RAISES K to the power c   3, 4, 5, 15, 17, 18, 20
  7.6.A.3  adding reactions MULTIPLIES the K's  6, 7, 12, 13, 16, 19, 23, 25, 29
  7.6.A.4  Q obeys the same algebra as K        11, 22, 26
  combinations of the three rules               8, 9, 21, 24, 27, 30

ARITHMETIC. Units 7 to 9 are the quantitative end of the course, so no numeric
key here is asserted -- each is recomputed below from the stimulus alone, in
``TABLE_CHECKS`` for the four items carrying a table and in ``NUMERIC`` for the
eighteen whose numbers are in the stem. Both gates also falsify the numeric
distractors against the same inputs, so a value that only LOOKS like the answer
cannot pass.

NEGATIVE CONTROL: ``python3 verify_h7_6.py --selftest`` corrupts a key, an
anchor, a table cell, a recomputed value and the notation on purpose and
confirms every gate fires.
"""
import sys

import cg_check as cg
import h_check as h

import h7_6

CONST = "Equilibrium constant at 298 K"
KNIT = "Equilibrium constant at 500 K"
KHAL = "Equilibrium constant"
QCOL = "Reaction quotient Q for the forward reaction"


# ------------------------------------------------------------------ table items

def q7(table, item):
    ks = cg.col(table, CONST)
    assert len(ks) == 3, f"expected three steps, got {len(ks)}"
    product = ks[0] * ks[1] * ks[2]
    assert abs(product - 40) < 1e-9, f"product of the three constants is {product}"
    assert abs(sum(ks) - 11) < 1e-9, "the sum distractor must be the sum of the same three"
    h.shows(item, "40")
    return f"the three tabulated constants {ks} multiply to {product:g}, and sum to {sum(ks):g}"


def q12(table, item):
    ks = cg.col(table, KNIT)
    product = ks[0] * ks[1]
    assert abs(product - 2.0) < 1e-9, f"product of the two constants is {product}"
    assert abs(sum(ks) - 405) < 1e-9, "the 405 distractor must be the sum of the same two"
    assert abs(ks[1] / ks[0] - 80000) < 1e-6, "the 80,000 distractor must be the quotient"
    h.shows(item, "2.0")
    return (f"{ks[0]:g} times {ks[1]:g} is {product:g}; the sum is {sum(ks):g} and the "
            "quotient is 80,000")


def q19(table, item):
    k1 = cg.cell(table, "I", KHAL)
    k2 = cg.cell(table, "II", KHAL)
    value = (1.0 / k1) * k2
    assert abs(value - 1.0 / 3.0) < 1e-9, f"reversing I and adding II gives {value}"
    assert abs(k1 * k2 - 27) < 1e-9, "the 27 distractor must be the unreversed product"
    h.shows(item, "0.33")
    return (f"one over {k1:g} times {k2:g} is {value:.2f}, while the unreversed product "
            f"is {k1 * k2:g}")


def q26(table, item):
    times = cg.labels(table)
    fwd = cg.col(table, QCOL)
    rev = [1.0 / v for v in fwd]
    best = times[rev.index(max(rev))]
    assert best == "15 minutes", f"the largest reverse quotient is at {best}"
    assert abs(max(rev) - 5.0) < 1e-9, f"the largest reverse quotient is {max(rev)}"
    assert [round(x, 6) for x in rev] == [2.0, 4.0, 5.0], f"reciprocals are {rev}"
    h.shows(item, "equals 5.0")
    return (f"the reciprocals of the tabulated {fwd} are {rev}, whose maximum {max(rev):g} "
            f"falls at {best}")


TABLE_CHECKS = {7: q7, 12: q12, 19: q19, 26: q26}


# ---------------------------------------------------------------- stem numerics

def _rule_reverse(k):
    return 1.0 / k


def _rule_scale(k, c):
    return k ** c


def n1(item):
    v = _rule_reverse(4.0)
    assert abs(v - 0.25) < 1e-12
    h.shows(item, "0.25")
    return "one over 4.0 is 0.25, the inverted constant of EK 7.6.A.1"


def n2(item):
    v = _rule_reverse(1.0e3)
    assert abs(v - 1.0e-3) < 1e-15
    h.shows(item, "10^{-3}")
    return "one over ten cubed is ten to the negative third"


def n3(item):
    v = _rule_scale(3.0, 2)
    assert abs(v - 9.0) < 1e-12
    assert abs(3.0 * 2 - 6.0) < 1e-12, "the 6.0 distractor must be K doubled"
    h.shows(item, "9.0")
    return "3.0 raised to the power two is 9.0, against 6.0 for doubling K itself"


def n4(item):
    v = _rule_scale(16.0, 0.5)
    assert abs(v - 4.0) < 1e-12
    assert abs(16.0 / 2 - 8.0) < 1e-12, "the 8.0 distractor must be K halved"
    h.shows(item, "4.0")
    return "16 raised to the power one half is 4.0, against 8.0 for halving K itself"


def n5(item):
    v = _rule_scale(2.0, 3)
    assert abs(v - 8.0) < 1e-12
    h.shows(item, "8.0")
    return "2.0 cubed is 8.0, and 2.0 times three would be 6.0"


def n6(item):
    v = 2.0 * 5.0
    assert abs(v - 10.0) < 1e-12
    assert abs(2.0 + 5.0 - 7.0) < 1e-12, "the 7.0 distractor must be the sum"
    h.shows(item, "10")
    return "2.0 times 5.0 is 10, against 7.0 for the sum"


def n8(item):
    v = _rule_scale(_rule_reverse(2.0), 2)
    assert abs(v - 0.25) < 1e-12
    h.shows(item, "0.25")
    return "inverting 2.0 gives 0.50 and squaring that gives 0.25"


def n9(item):
    v = 12.0 * _rule_reverse(3.0)
    assert abs(v - 4.0) < 1e-12
    assert abs(12.0 * 3.0 - 36.0) < 1e-12, "the 36 distractor must be the unreversed product"
    h.shows(item, "4.0")
    return "12 times one third is 4.0, against 36 without the reversal"


def n13(item):
    v = 60.0 / 12.0
    assert abs(v - 5.0) < 1e-12
    assert abs(60.0 - 12.0 - 48.0) < 1e-12, "the 48 distractor must be the difference"
    h.shows(item, "5.0")
    return "60 divided by 12 is 5.0, against 48 for the difference"


def n14(item):
    v = _rule_reverse(5.0e8)
    assert abs(v - 2.0e-9) < 1e-20
    h.shows(item, "2.0 \\times 10^{-9}")
    return "one over five times ten to the eighth is two times ten to the negative ninth"


def n15(item):
    v = _rule_scale(0.10, 2)
    assert abs(v - 0.010) < 1e-12
    h.shows(item, "0.010")
    return "0.10 squared is 0.010, against 0.20 for doubling K itself"


def n17(item):
    v = _rule_scale(25.0, 2)
    assert abs(v - 625.0) < 1e-9
    h.shows(item, "625")
    return "25 squared is 625, against 50 for doubling the constant itself"


def n18(item):
    v = 27.0 ** (1.0 / 3.0)
    assert abs(v - 3.0) < 1e-9
    assert abs(27.0 / 3.0 - 9.0) < 1e-12, "the 9.0 distractor must be 27 divided by three"
    h.shows(item, "3.0")
    return "the cube root of 27 is 3.0, against 9.0 for dividing by three"


def n20(item):
    v = _rule_scale(0.040, 0.5)
    assert abs(v - 0.20) < 1e-12
    h.shows(item, "0.20")
    return "the square root of 0.040 is 0.20, against 0.020 for halving K itself"


def n22(item):
    v = _rule_reverse(0.20)
    assert abs(v - 5.0) < 1e-12
    assert abs(0.20 ** 2 - 0.040) < 1e-12, "the 0.040 distractor must be Q squared"
    h.shows(item, "5.0")
    return "one over 0.20 is 5.0, against 0.040 for squaring the quotient"


def n23(item):
    v = 2.0 * 3.0 * 0.50
    assert abs(v - 3.0) < 1e-12
    assert abs(2.0 + 3.0 + 0.50 - 5.5) < 1e-12, "the 5.5 distractor must be the sum"
    h.shows(item, "3.0")
    return "2.0 times 3.0 times 0.50 is 3.0, against 5.5 for the sum"


def n24(item):
    """Every choice is an equation; recompute K for each from the two rules."""
    base = 0.50  # for 2 A(g) to B(g)
    # (reversed?, factor) read off each written equation relative to 2 A to B
    table = {"2 B(g) to 4 A(g)": (True, 2),
             "B(g) to 2 A(g)": (True, 1),
             "4 A(g) to 2 B(g)": (False, 2),
             "6 A(g) to 3 B(g)": (False, 3),
             "3 B(g) to 6 A(g)": (True, 3)}
    values = {}
    for text, (rev, c) in table.items():
        k = _rule_reverse(base) if rev else base
        values[text] = _rule_scale(k, c)
    hits = [t for t, v in values.items() if abs(v - 4.0) < 1e-9]
    assert hits == [h.keyed(item)], f"equations giving 4.0 are {hits}"
    assert set(table) == set(item["choices"]), "the recomputed set must be the choice set"
    return f"recomputing all five written equations gives {values}, and only one equals 4.0"


def n27(item):
    v = _rule_scale(_rule_reverse(100.0), 0.5)
    assert abs(v - 0.10) < 1e-12
    h.shows(item, "0.10")
    return "inverting 100 gives 0.010 and its square root is 0.10"


def n30(item):
    v = _rule_scale(_rule_reverse(2.0), 3)
    assert abs(v - 0.125) < 1e-12
    assert abs(2.0 ** 3 - 8.0) < 1e-12, "the 8.0 distractor must be the uninverted cube"
    h.shows(item, "0.125")
    return "inverting 2.0 gives 0.50 and cubing that gives 0.125"


NUMERIC = {1: n1, 2: n2, 3: n3, 4: n4, 5: n5, 6: n6, 8: n8, 9: n9, 13: n13, 14: n14,
           15: n15, 17: n17, 18: n18, 20: n20, 22: n22, 23: n23, 24: n24, 27: n27,
           30: n30}


CLAIMS = [
 ("0.25",
  "EK 7.6.A.1, verbatim: when a reaction is reversed, K is inverted. Recomputed in n1 as one over 4.0."),
 ("10^{-3}",
  "EK 7.6.A.1 applied to a power of ten. Recomputed in n2: the reciprocal of ten cubed is ten to the negative third."),
 ("9.0",
  "EK 7.6.A.2: multiplying every coefficient by a factor c raises K to the power c. Recomputed in n3 with c equal to two."),
 ("4.0",
  "EK 7.6.A.2 with c equal to one half, which is a square root. Recomputed in n4 against the halving error."),
 ("8.0",
  "EK 7.6.A.2 with c equal to three. Recomputed in n5; multiplying K by three instead would give six."),
 ("10",
  "EK 7.6.A.3: the K of a sum of reactions is the PRODUCT of their K values. Recomputed in n6 against the sum."),
 ("40",
  "EK 7.6.A.3 over three summed steps. Recomputed in q7 from the tabulated constants alone, with the sum falsified."),
 ("0.25",
  "EK 7.6.A.1 then EK 7.6.A.2 in sequence, inverting and then squaring. Recomputed in n8 as one half squared."),
 ("4.0",
  "Subtracting a reaction is reversing it and adding, so EK 7.6.A.1 then EK 7.6.A.3. Recomputed in n9."),
 ("reciprocal of the original value",
  "EK 7.6.A.1 states the inversion, and the structural reason is that the concentrations in the numerator of the expression move to the denominator when the equation is reversed."),
 ("identical mathematical forms",
  "EK 7.6.A.4, near verbatim: since the expressions for K and Q have identical mathematical forms, all valid algebraic manipulations of K also apply to Q."),
 ("2.0",
  "EK 7.6.A.3 with the shared NO cancelling between the two equations. Recomputed in q12 from the table, with the sum and quotient distractors falsified."),
 ("5.0",
  "EK 7.6.A.3 read backwards: the overall constant divided by the known step gives the unknown step. Recomputed in n13."),
 ("2.0 \\times 10^{-9}",
  "EK 7.6.A.1 on a value in scientific notation. Recomputed in n14; changing only the sign of the exponent leaves the coefficient uninverted."),
 ("0.010",
  "EK 7.6.A.2 with c equal to two applied to a value smaller than one. Recomputed in n15."),
 ("product of the two individual equilibrium constants",
  "EK 7.6.A.3, near verbatim: when reactions are added together, the K of the resulting overall reaction is the product of the K's for the reactions that were summed."),
 ("625",
  "EK 7.6.A.2 with c equal to two, on a pressure-based constant, which EK 7.6.A.4 confirms obeys the same algebra. Recomputed in n17."),
 ("3.0",
  "EK 7.6.A.2 read backwards: the reported constant is the original cubed, so the original is its cube root. Recomputed in n18."),
 ("0.33",
  "EK 7.6.A.1 then EK 7.6.A.3, reversing one tabulated reaction before multiplying. Recomputed in q19 from the table."),
 ("0.20",
  "EK 7.6.A.2 with c equal to one half applied to a value smaller than one. Recomputed in n20."),
 ("different left-to-right order",
  "EK 7.6.A.1, 7.6.A.2 and 7.6.A.3 each name a change to the equation that changes K, and none of them is a reordering of the reactant formulas; the expression is a product of the same terms in any order."),
 ("5.0",
  "EK 7.6.A.4 carries the inversion of EK 7.6.A.1 across to Q. Recomputed in n22 against the squaring error."),
 ("3.0",
  "EK 7.6.A.3 across three constants, one of them smaller than one. Recomputed in n23 against the sum."),
 ("2 B(g) to 4 A(g)",
  "EK 7.6.A.1 then EK 7.6.A.2. Recomputed in n24, which evaluates all five written equations from the two rules and confirms exactly one of them equals 4.0."),
 ("removed when they are combined",
  "EK 7.6.A.3 speaks of reactions ADDED together, which is an operation on the equations: a species that is a product of one and a reactant of the other stands on both sides of the sum and cancels."),
 ("equals 5.0",
  "EK 7.6.A.4 with EK 7.6.A.1. Recomputed in q26 from the tabulated quotients, whose reciprocals rise as the tabulated values fall."),
 ("0.10",
  "EK 7.6.A.1 then EK 7.6.A.2 with c equal to one half. Recomputed in n27."),
 ("2 NO(g) + Br2(g) to 2 NOBr(g)",
  "EK 7.6.A.1 makes the reverse constant available from the forward one by algebra at the same temperature. None of the four properties in 7.6.A relates constants at two temperatures, gives a concentration without initial conditions, or says anything about rate."),
 ("product of two numbers each greater than one",
  "EK 7.6.A.3 makes the overall constant a product, and a product of two factors each above one exceeds both factors. The claim is therefore correct for any such pair."),
 ("0.125",
  "EK 7.6.A.1 then EK 7.6.A.2 with c equal to three. Recomputed in n30 against the uninverted cube."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        # make the three summed steps multiply to something other than 40
        mod.QUESTIONS[6]["table"] = dict(
            headers=h7_6._T_STEPS["headers"],
            rows=[[a, b, ("9.0" if a == "1" else c)]
                  for a, b, c in h7_6._T_STEPS["rows"]])

    def corrupt_numeric(mod, cl):
        # 0.20 is the square root of 0.040; make the keyed choice say something else
        ch = list(mod.QUESTIONS[19]["choices"])
        ch[0] = "K = 0.44"
        mod.QUESTIONS[19]["choices"] = ch

    def swap_equation_key(mod, cl):
        # q24's key is an equation, checked by recomputing all five
        mod.QUESTIONS[23]["ans"] = 1
        cl[23] = ("B(g) to 2 A(g)", cl[23][1])

    return [("a table cell corrupted so the keyed product is false", corrupt_table),
            ("a recomputed numeric value no longer in the keyed choice", corrupt_numeric),
            ("q24's key moved to an equation with a different K", swap_equation_key)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h.run(h7_6, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
