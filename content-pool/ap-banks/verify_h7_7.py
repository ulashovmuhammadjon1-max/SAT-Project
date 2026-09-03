"""Key audit for AP CHEMISTRY 7.7 Calculating Equilibrium Concentrations.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON. Two statements, and nothing else:

  7.7.A.1  the equilibrium amounts follow from the balanced reaction, the
           initial concentrations and K            items 1-3, 7-11, 15, 21, 22,
                                                   25, 26, 28, 30
  7.7.A.2  Q < K generates products, Q > K generates reactants, Q = K is
           dynamic equilibrium                     items 4-6, 12-14, 16-20, 23,
                                                   24, 27, 29

ARITHMETIC. Not one equilibrium amount or reaction quotient below is asserted.
Every one is recomputed from the balanced equation, the stated initial
condition and K -- in ``TABLE_CHECKS`` for the ten items carrying a table and
in ``NUMERIC`` for the twelve whose numbers are in the stem -- and the numeric
distractors are falsified against the same inputs. The two solvers are written
once, at the top, so a slip in one item cannot look like a different rule:

    ``one_to_one``  A to B from pure A: x/(a - x) = K, so x = Ka/(1 + K)
    ``two_to_two``  H2 + I2 to 2 HI from equal reactants: 2x/(a - x) = sqrt(K)

NEGATIVE CONTROL: ``python3 verify_h7_7.py --selftest`` corrupts a key, an
anchor, a table cell, a recomputed value and the notation on purpose and
confirms every gate fires.
"""
import math
import sys

import cg_check as cg
import h_check as h

import h7_7

A = "[A] (M)"
B = "[B] (M)"
H2 = "[H2] (M)"
I2 = "[I2] (M)"
HI = "[HI] (M)"
PA = "Partial pressure of A (atm)"
PB = "Partial pressure of B (atm)"


def one_to_one(a, k):
    """A to B starting from pure A at ``a``: returns (equilibrium A, equilibrium B)."""
    x = k * a / (1.0 + k)
    assert abs(x / (a - x) - k) < 1e-9, "solver disagrees with its own equilibrium ratio"
    return a - x, x


def two_to_two(a, k):
    """H2 + I2 to 2 HI from ``a`` of each reactant: returns (each reactant, HI)."""
    r = math.sqrt(k)
    x = r * a / (2.0 + r)
    assert abs((2 * x) ** 2 / ((a - x) ** 2) - k) < 1e-9, "solver disagrees with K"
    return a - x, 2 * x


# ------------------------------------------------------------------ table items

def _mix_q(table, row):
    return cg.cell(table, row, B) / cg.cell(table, row, A)


def q4(table, item):
    q = _mix_q(table, "1")
    assert abs(q - 0.50) < 1e-9, f"Q for mixture 1 is {q}"
    assert q < 2.0, "Q must be below K for the keyed forward direction"
    h.shows(item, "Net forward reaction, because Q is 0.50")
    return f"mixture 1 gives Q equal to {q:g}, which is below the stated K of 2.0"


def q5(table, item):
    q = _mix_q(table, "2")
    assert abs(q - 5.0) < 1e-9, f"Q for mixture 2 is {q}"
    assert q > 2.0, "Q must exceed K for the keyed reverse direction"
    h.shows(item, "Net reverse reaction, because Q is 5.0")
    return f"mixture 2 gives Q equal to {q:g}, which is above the stated K of 2.0"


def q6(table, item):
    q = _mix_q(table, "3")
    assert abs(q - 2.0) < 1e-9, f"Q for mixture 3 is {q}"
    assert cg.cell(table, "3", B) > cg.cell(table, "3", A), \
        "the two 'B is larger' distractors must be true of the table and still wrong"
    h.shows(item, "proceed at the same rate")
    return f"mixture 3 gives Q equal to {q:g}, exactly the stated K of 2.0"


def q11(table, item):
    # The table states the equilibrium row as 1.00 minus x and x, so the ratio is
    # x/(1 - x); K is 3.0 in the stem.
    assert cg.cell(table, "Initial", A) == 1.00, "the initial A must be 1.00 M"
    assert cg.cell(table, "Initial", B) == 0.0, "the initial B must be zero"
    left, x = one_to_one(1.00, 3.0)
    assert abs(x - 0.75) < 1e-9 and abs(left - 0.25) < 1e-9, f"solved x is {x}"
    h.shows(item, "0.75")
    return f"solving x over 1.00 minus x equal to 3.0 gives x of {x:g} and A of {left:g}"


def _hi_q(table, vessel):
    return (cg.cell(table, vessel, HI) ** 2
            / (cg.cell(table, vessel, H2) * cg.cell(table, vessel, I2)))


def q12(table, item):
    q = _hi_q(table, "W")
    assert abs(q - 8.0) < 1e-9, f"Q in vessel W is {q}"
    assert q > 4.0, "Q must exceed K for the keyed reverse direction"
    h.shows(item, "Net reverse reaction, because Q is 8.0")
    return f"vessel W gives Q equal to {q:g}, above the stated K of 4.0"


def q13(table, item):
    q = _hi_q(table, "X")
    assert abs(q - 16.0) < 1e-9, f"Q in vessel X is {q}"
    h.shows(item, "Q is 16 and the mixture reacts in reverse")
    return f"vessel X gives Q equal to {q:g}, well above the stated K of 4.0"


def q14(table, item):
    q = _hi_q(table, "Y")
    assert abs(q - 1.0) < 1e-9, f"Q in vessel Y is {q}"
    assert q < 4.0, "Q must be below K for the keyed forward direction"
    h.shows(item, "Q is 1.0, so the mixture reacts forward")
    return f"vessel Y gives Q equal to {q:g}, below the stated K of 4.0"


def _p_q(table, trial):
    return cg.cell(table, trial, PB) / cg.cell(table, trial, PA) ** 2


def q17(table, item):
    q = _p_q(table, "1")
    assert abs(q - 1.00) < 1e-9, f"Q for trial 1 is {q}"
    assert q < 2.0, "Q must be below K for the keyed forward direction"
    h.shows(item, "Q is 1.00, so there is net forward reaction")
    return f"trial 1 gives Q equal to {q:g} once the pressure of A is squared"


def q18(table, item):
    q = _p_q(table, "2")
    unsquared = cg.cell(table, "2", PB) / cg.cell(table, "2", PA)
    assert abs(q - 8.00) < 1e-9, f"Q for trial 2 is {q}"
    assert abs(unsquared - 4.00) < 1e-9, "the 4.00 distractor must be the unsquared ratio"
    h.shows(item, "8.00")
    return (f"trial 2 gives Q equal to {q:g} with the square, against {unsquared:g} "
            "without it")


def q19(table, item):
    q = _p_q(table, "3")
    assert abs(q - 0.125) < 1e-9, f"Q for trial 3 is {q}"
    assert q < 2.0, "Q must be below K for the keyed generation of B"
    h.shows(item, "Q is 0.125, which is below K, so B is generated")
    return f"trial 3 gives Q equal to {q:g}, far below the stated K of 2.0"


TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 11: q11, 12: q12, 13: q13, 14: q14,
                17: q17, 18: q18, 19: q19}


# ---------------------------------------------------------------- stem numerics

def n1(item):
    left, x = one_to_one(1.00, 4.0)
    assert abs(x - 0.80) < 1e-9 and abs(left - 0.20) < 1e-9
    h.shows(item, "0.80")
    return f"K of 4.0 from 1.00 M gives B of {x:g} M and A of {left:g} M"


def n2(item):
    left, x = one_to_one(1.00, 0.25)
    assert abs(left - 0.80) < 1e-9 and abs(x - 0.20) < 1e-9
    h.shows(item, "0.80")
    return f"K of 0.25 from 1.00 M leaves C at {left:g} M with D at {x:g} M"


def n3(item):
    each, hi = two_to_two(1.00, 36.0)
    assert abs(hi - 1.50) < 1e-9 and abs(each - 0.25) < 1e-9
    h.shows(item, "1.50")
    return f"K of 36 from 1.00 M of each reactant gives HI of {hi:g} M"


def n7(item):
    # A to 2 B, K = 4.0e-6, [A]0 = 1.00. Small K, so [A] stays 1.00.
    k, a0 = 4.0e-6, 1.00
    x = math.sqrt(k * a0 / 4.0)
    b = 2 * x
    assert abs(b - 2.0e-3) < 1e-12, f"B recomputes to {b}"
    assert (2 * x) ** 2 / (a0 - x) - k < 1e-9, "the approximation must reproduce K"
    h.shows(item, "2.0 \\times 10^{-3}")
    return f"four x squared equal to {k} gives x of {x:g} and B of {b:g} M"


def n8(item):
    k, a0 = 1.0e-8, 1.00
    x = math.sqrt(k * a0)
    assert abs(x - 1.0e-4) < 1e-12, f"F recomputes to {x}"
    h.shows(item, "1.0 \\times 10^{-4}")
    return f"x squared equal to {k} gives x of {x:g} M for each product"


def n10(item):
    left, x = one_to_one(2.00, 9.0)
    assert abs(left - 0.20) < 1e-9 and abs(x - 1.80) < 1e-9
    h.shows(item, "0.20")
    return f"K of 9.0 from 2.00 M leaves A at {left:g} M with B at {x:g} M"


def n15(item):
    each, hi = two_to_two(1.00, 4.0)
    assert abs(each - 0.50) < 1e-9 and abs(hi - 1.00) < 1e-9
    h.shows(item, "0.50")
    return f"K of 4.0 from 1.00 M of each reactant leaves H2 at {each:g} M"


def n21(item):
    left, x = one_to_one(0.50, 4.0)
    assert abs(x - 0.40) < 1e-9 and abs(left - 0.10) < 1e-9
    h.shows(item, "0.40")
    return f"K of 4.0 from 0.50 M gives B of {x:g} M with A at {left:g} M"


def n23(item):
    q = 0.90 / 0.10
    assert abs(q - 9.0) < 1e-9, f"Q recomputes to {q}"
    assert q > 4.0, "Q must exceed K for the keyed generation of A"
    h.shows(item, "Q is 9.0, so A is generated")
    return f"0.90 over 0.10 is {q:g}, above the stated K of 4.0"


def n26(item):
    d = 0.25
    c = 1.00 - d
    k = d / c
    assert abs(k - 1.0 / 3.0) < 1e-9, f"K recomputes to {k}"
    assert abs(d / 1.00 - 0.25) < 1e-12, "the 0.25 distractor must divide by the initial value"
    h.shows(item, "0.33")
    return f"{d} over {c} is {k:.4f}, against {d / 1.00:g} if the initial value is used"


def n28(item):
    left, x = one_to_one(4.00, 1.00)
    assert abs(left - 2.00) < 1e-9 and abs(x - 2.00) < 1e-9
    assert abs(left + x - 4.00) < 1e-9, "the total must be conserved at 4.00 M"
    h.shows(item, "Both A and B are 2.00 M")
    return f"K of exactly one from 4.00 M splits the total evenly at {left:g} M each"


def n30(item):
    left, x = one_to_one(1.00, 19.0)
    pct = 100.0 * left / 1.00
    assert abs(pct - 5.0) < 1e-9, f"the remaining fraction recomputes to {pct} percent"
    assert abs(100.0 * x - 95.0) < 1e-9, "the 95 percent distractor must be the fraction converted"
    h.shows(item, "5.0 percent")
    return f"K of 19 from 1.00 M leaves {left:g} M, which is {pct:g} percent of the start"


NUMERIC = {1: n1, 2: n2, 3: n3, 7: n7, 8: n8, 10: n10, 15: n15, 21: n21, 23: n23,
           26: n26, 28: n28, 30: n30}


CLAIMS = [
 ("0.80",
  "EK 7.7.A.1: the equilibrium amounts follow from the balanced reaction, the initial concentration and K. Recomputed in n1 by solving x over 1.00 minus x equal to 4.0."),
 ("0.80",
  "EK 7.7.A.1 with a constant smaller than one, which must leave more reactant than product. Recomputed in n2."),
 ("1.50",
  "EK 7.7.A.1 on a reaction whose product carries a coefficient of two, so the amount of HI is twice the amount reacted. Recomputed in n3."),
 ("Net forward reaction, because Q is 0.50",
  "EK 7.7.A.2: when Q is less than K the reaction proceeds with a net consumption of reactants and generation of products. Q recomputed from the table in q4."),
 ("Net reverse reaction, because Q is 5.0",
  "EK 7.7.A.2: when Q is greater than K the reaction proceeds with a net consumption of products and generation of reactants. Q recomputed from the table in q5."),
 ("proceed at the same rate",
  "EK 7.7.A.2, near verbatim: when Q equals K the system is at dynamic equilibrium, and both forward and reverse reactions proceed at the same rate. Dynamic equilibrium is continued reaction, not stopped reaction."),
 ("2.0 \\times 10^{-3}",
  "EK 7.7.A.1 with a very small K, where the reactant consumed is a negligible fraction of the initial amount. Recomputed in n7."),
 ("1.0 \\times 10^{-4}",
  "EK 7.7.A.1 on a reaction producing two different products in equal amounts. Recomputed in n8."),
 ("balanced reaction, the initial concentrations, and the appropriate value",
  "EK 7.7.A.1, verbatim: the concentrations or partial pressures of species at equilibrium can be predicted given the balanced reaction, initial concentrations, and the appropriate K."),
 ("0.20",
  "EK 7.7.A.1 with a starting concentration other than 1.00 M, so the answer cannot be read off the constant alone. Recomputed in n10."),
 ("0.75",
  "EK 7.7.A.1 read off a tabulated initial, change and equilibrium layout. Recomputed in q11 from the tabulated initial row and the stated K."),
 ("Net reverse reaction, because Q is 8.0",
  "EK 7.7.A.2 with an expression carrying a squared product term. Q recomputed from the tabulated concentrations in q12."),
 ("Q is 16 and the mixture reacts in reverse",
  "EK 7.7.A.2. Q recomputed from the tabulated concentrations in q13, where the squared numerator makes Q four times the value in the previous vessel."),
 ("Q is 1.0, so the mixture reacts forward",
  "EK 7.7.A.2, together with its statement that the system moves so as to bring the proportion into agreement with K. Q recomputed in q14."),
 ("0.50",
  "EK 7.7.A.1 on the same reaction as item 3 with a different constant, so the answer cannot be carried over. Recomputed in n15."),
 ("proportion of reactants and products stays constant",
  "EK 7.7.A.2, near verbatim: at Q equal to K both reactions proceed at the same rate and the proportion of reactants and products remains constant. Equal rates is not equal concentrations."),
 ("Q is 1.00, so there is net forward reaction",
  "EK 7.7.A.2 applied to partial pressures, which EK 7.7.A.1 places on the same footing as concentrations. Q recomputed in q17."),
 ("8.00",
  "EK 7.7.A.2 with the coefficient of two carried into the expression as a square. Recomputed in q18, which also recomputes the unsquared ratio to confirm the distractor."),
 ("Q is 0.125, which is below K, so B is generated",
  "EK 7.7.A.2: Q below K generates products, and B is the product in the written equation. Q recomputed in q19."),
 ("equilibrium concentration of reactant is nearly the initial concentration",
  "The approximation rests on EK 7.7.A.1: a small K makes the equilibrium proportion of product small, so only a small fraction of the reactant is converted. A small conversion is not a zero conversion."),
 ("0.40",
  "EK 7.7.A.1 from a starting concentration of 0.50 M. Recomputed in n21."),
 ("Almost all of the reactant has been converted",
  "EK 7.7.A.1 with a large K, which makes the product term far larger than the reactant term at equilibrium. Some of every species in the expression remains, since a concentration of zero would make the ratio undefined."),
 ("Q is 9.0, so A is generated",
  "EK 7.7.A.2: Q above K means net consumption of products and generation of reactants. Recomputed in n23."),
 ("value of the equilibrium constant",
  "K is fixed by the temperature, while EK 7.7.A.1 makes the equilibrium CONCENTRATIONS depend on the initial conditions as well, so those differ between two differently charged vessels."),
 ("change in B twice the magnitude",
  "EK 7.7.A.1 names the balanced reaction as one of the three required inputs, and the coefficients are what set the ratio of the changes: two B are formed for each A consumed."),
 ("0.33",
  "EK 7.7.A.1 read backwards, from a measured equilibrium amount to K. Recomputed in n26, which also recomputes the distractor formed by dividing by the initial value."),
 ("rises toward K",
  "EK 7.7.A.2: Q below K means products are generated and reactants consumed, which raises the numerator and lowers the denominator of the quotient until it equals K."),
 ("Both A and B are 2.00 M",
  "EK 7.7.A.1 with K exactly one, which forces equal product and reactant concentrations, and a one-to-one equation, which conserves the total. Recomputed in n28."),
 ("brings Q into agreement with the single value of K",
  "EK 7.7.A.2 makes the direction of net change depend on the comparison of Q with K, and K is set by the temperature rather than by the starting mixture, so a vessel of pure product reacts in reverse to the same constant."),
 ("5.0 percent",
  "EK 7.7.A.1 expressed as a fraction remaining rather than a concentration. Recomputed in n30, which also recomputes the fraction converted to confirm the 95 percent distractor."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[3]["table"] = dict(
            headers=h7_7._T_MIXTURES["headers"],
            rows=[[lab, a, ("0.90" if lab == "1" else b)]
                  for lab, a, b in h7_7._T_MIXTURES["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[0]["choices"])
        ch[0] = "[B] = 0.85 M"
        mod.QUESTIONS[0]["choices"] = ch
        cl[0] = ("0.85", cl[0][1])

    def drop_table_check(mod, cl):
        mod.QUESTIONS[8]["table"] = h7_7._T_MIXTURES

    return [("a table cell corrupted so the keyed Q is false", corrupt_table),
            ("a recomputed concentration no longer in the keyed choice", corrupt_numeric),
            ("a table added to an item with no recomputation for it", drop_table_check)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h.run(h7_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
