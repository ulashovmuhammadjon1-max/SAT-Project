"""Key audit for AP CHEMISTRY 7.8 Representations of Equilibrium.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON. A single essential knowledge statement, 7.8.A.1:
particulate representations can be used to describe the relative numbers of
reactant and product particles present prior to and at equilibrium, and the
value of the equilibrium constant. Because the whole topic rests on one
sentence, the items are separated by WHAT IS ASKED OF THE COUNTS rather than by
subject matter, and the separation is checked here:

  value of K from equilibrium counts        1, 3, 5, 8, 10, 21, 23, 29
  before-and-at comparison of counts        2, 4, 6, 11, 25, 26, 27
  which counts are consistent with a K      9, 15, 16, 17, 18, 20
  what counts CANNOT establish              13, 14, 19, 22, 24, 28, 30
  reaching equilibrium over time            7, 12

FIGURES. This bank cannot show a picture, so every particulate representation
is a table of particle COUNTS with the stem fixing 1.0 mol per particle in a
1.0 L container. ``no_figure_language`` below asserts that no stem or choice
refers to a diagram, image or figure, which is the defect SCIENCE_BRIEF.md
names and this project has shipped once.

ARITHMETIC. Every constant, ratio and count is recomputed from the tabulated or
stated counts alone -- in ``TABLE_CHECKS`` for the twelve items carrying a table
and in ``NUMERIC`` for the seven whose counts are in the stem.

NEGATIVE CONTROL: ``python3 verify_h7_8.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_8

PA = "Particles of A"
PB = "Particles of B"
PX = "Particles of X"
PY = "Particles of Y"
PA2 = "Particles of A2"
PB2 = "Particles of B2"
PAB = "Particles of AB"
BEFORE = "Before any reaction"
EQ = "At equilibrium"

# The defect this project has shipped once: a stem that describes a picture the
# student cannot see. No \b -- explicit lookarounds only.
_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|drawing|as shown|shown below|"
    r"the graph)(?![a-z])", re.I)


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in [item["q"]] + list(item["choices"]):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but this bank "
                f"cannot show one -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item refers to a picture it cannot show.")


# ------------------------------------------------------------------ table items

def q1(table, item):
    a = cg.cell(table, EQ, PA)
    b = cg.cell(table, EQ, PB)
    k = b / a
    assert abs(k - 3.0) < 1e-9, f"K recomputes to {k}"
    assert abs(a / b - 1.0 / 3.0) < 1e-9, "the 0.33 distractor must be the inverted ratio"
    h.shows(item, "3.0")
    return f"{b:g} particles of product over {a:g} of reactant recomputes K as {k:g}"


def q2(table, item):
    start = cg.cell(table, BEFORE, PA)
    left = cg.cell(table, EQ, PA)
    frac = (start - left) / start
    assert abs(frac - 0.75) < 1e-9, f"the converted fraction recomputes to {frac}"
    assert abs(left / start - 0.25) < 1e-9, "the one-quarter distractor must be the fraction left"
    h.shows(item, "Three quarters of them")
    return f"{start:g} falling to {left:g} is a converted fraction of {frac:g}"


def q3(table, item):
    x = cg.cell(table, EQ, PX)
    y = cg.cell(table, EQ, PY)
    k = y / x ** 2
    assert abs(k - 0.25) < 1e-9, f"K recomputes to {k}"
    assert abs(y / x - 1.0) < 1e-9, "the 1.0 distractor must be the unsquared ratio"
    h.shows(item, "0.25")
    return f"{y:g} over the square of {x:g} recomputes K as {k:g}, against {y / x:g} unsquared"


def q4(table, item):
    dx = cg.cell(table, BEFORE, PX) - cg.cell(table, EQ, PX)
    dy = cg.cell(table, EQ, PY) - cg.cell(table, BEFORE, PY)
    assert abs(dx / dy - 2.0) < 1e-9, f"the consumed-to-formed ratio is {dx / dy}"
    h.shows(item, "Two particles of X for each particle of Y")
    return f"{dx:g} particles of X consumed for {dy:g} of Y formed is a ratio of {dx / dy:g}"


def q5(table, item):
    a2 = cg.cell(table, EQ, PA2)
    b2 = cg.cell(table, EQ, PB2)
    ab = cg.cell(table, EQ, PAB)
    k = ab ** 2 / (a2 * b2)
    assert abs(k - 16.0) < 1e-9, f"K recomputes to {k}"
    assert abs(ab / (a2 * b2) - 2.0) < 1e-9, "the unsquared value must be a listed distractor"
    h.shows(item, "16")
    return f"the square of {ab:g} over {a2:g} times {b2:g} recomputes K as {k:g}"


def q6(table, item):
    before = sum(cg.cell(table, BEFORE, c) for c in (PA2, PB2, PAB))
    after = sum(cg.cell(table, EQ, c) for c in (PA2, PB2, PAB))
    assert before == after == 12, f"totals are {before} before and {after} at equilibrium"
    h.shows(item, "Twelve diatomic particles are present before reaction")
    return f"the totals recompute to {before:g} before and {after:g} at equilibrium"


def q7(table, item):
    times = cg.labels(table)
    a = cg.col(table, PA)
    b = cg.col(table, PB)
    steady = [i for i in range(1, len(times)) if a[i] == a[i - 1] and b[i] == b[i - 1]]
    assert steady, "no pair of consecutive rows is unchanged"
    first = times[steady[0] - 1]
    assert first == "2 minutes", f"the counts first stop changing at {first}"
    h.shows(item, "At 2 minutes")
    return f"the counts {list(zip(a, b))} first repeat between {first} and the next row"


def q8(table, item):
    a = cg.col(table, PA)
    b = cg.col(table, PB)
    k = b[-1] / a[-1]
    assert abs(k - 1.0) < 1e-9, f"K recomputes to {k}"
    early = b[1] / a[1]
    assert abs(early - 0.60) < 1e-9, "the 0.60 distractor must be the quotient at one minute"
    h.shows(item, "1.0")
    return f"the settled counts give K as {k:g}, against a quotient of {early:g} at one minute"


def q9(table, item):
    ratios = {lab: cg.cell(table, lab, PB) / cg.cell(table, lab, PA)
              for lab in cg.labels(table)}
    hits = [lab for lab, r in ratios.items() if abs(r - 2.0) < 1e-9]
    assert hits == ["P"], f"containers matching K of 2.0 are {hits}"
    h.shows(item, "Container P")
    return f"the four containers give ratios {ratios}, of which only one equals 2.0"


def q10(table, item):
    ratios = {lab: cg.cell(table, lab, PB) / cg.cell(table, lab, PA)
              for lab in cg.labels(table)}
    best = max(ratios, key=ratios.get)
    assert best == "S", f"the largest ratio belongs to container {best}"
    assert len(set(ratios.values())) == 4, "the 'all the same' distractor must be false"
    h.shows(item, "Container S")
    return f"the ratios {ratios} have a single maximum, at container {best}"


def q11(table, item):
    x = cg.cell(table, EQ, PX)
    y = cg.cell(table, EQ, PY)
    k = y ** 2 / x
    assert abs(k - 2.0) < 1e-9, f"K recomputes to {k}"
    assert abs(y / x - 0.50) < 1e-9, "the 0.50 distractor must be the unsquared ratio"
    h.shows(item, "2.0")
    return f"the square of {y:g} over {x:g} recomputes K as {k:g}"


def q12(table, item):
    dx = cg.cell(table, BEFORE, PX) - cg.cell(table, EQ, PX)
    dy = cg.cell(table, EQ, PY) - cg.cell(table, BEFORE, PY)
    assert (dx, dy) == (2.0, 4.0), f"the changes recompute to {dx} and {dy}"
    assert abs(dy / dx - 2.0) < 1e-9, "the changes must be in the two-to-one ratio"
    total_before = cg.cell(table, BEFORE, PX) + cg.cell(table, BEFORE, PY)
    total_after = cg.cell(table, EQ, PX) + cg.cell(table, EQ, PY)
    assert total_after > total_before, "the 'total conserved' distractor must be false"
    h.shows(item, "ratio of the coefficients")
    return (f"X falls by {dx:g} while Y rises by {dy:g}, and the total goes from "
            f"{total_before:g} to {total_after:g}")


TABLE_CHECKS = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9,
                10: q10, 11: q11, 12: q12}


# ---------------------------------------------------------------- stem numerics

def _split(total, k):
    """One-to-one reaction: counts summing to ``total`` in the ratio ``k``."""
    reactant = total / (1.0 + k)
    product = total - reactant
    assert abs(product / reactant - k) < 1e-9, "the split must reproduce K"
    return reactant, product


def n15(item):
    a, b = _split(20, 4.0)
    assert (a, b) == (4.0, 16.0), f"the split recomputes to {a} and {b}"
    h.shows(item, "16 particles of B")
    return f"twenty particles split four to sixteen at a ratio of 4.0, giving {b:g} of B"


def n16(item):
    c, d = _split(15, 0.50)
    assert (c, d) == (10.0, 5.0), f"the split recomputes to {c} and {d}"
    h.shows(item, "10 particles of C")
    return f"fifteen particles split at a ratio of 0.50 leave {c:g} of C and {d:g} of D"


def n21(item):
    x, y = 2.0, 8.0
    k = y / x ** 2
    assert abs(k - 2.0) < 1e-9, f"K recomputes to {k}"
    assert abs(y / x - 4.0) < 1e-9, "the 4.0 distractor must be the unsquared ratio"
    h.shows(item, "2.0")
    return f"{y:g} over the square of {x:g} recomputes K as {k:g}"


def n23(item):
    a0, b0, a_eq = 10.0, 10.0, 5.0
    b_eq = b0 + (a0 - a_eq)
    k = b_eq / a_eq
    assert abs(k - 3.0) < 1e-9, f"K recomputes to {k}"
    h.shows(item, "3.0")
    return f"A falling from {a0:g} to {a_eq:g} raises B to {b_eq:g}, giving K of {k:g}"


def n24(item):
    first = 8.0 / 4.0
    second = 16.0 / 8.0
    assert abs(first - second) < 1e-9, f"the two quotients are {first} and {second}"
    h.shows(item, "Both have the same reaction quotient")
    return f"the two containers give quotients of {first:g} and {second:g}, which agree"


def n27(item):
    start, left = 12.0, 6.0
    consumed = start - left
    formed = consumed / 2.0
    assert formed == 3.0, f"the formed count recomputes to {formed}"
    h.shows(item, "the six consumed give three of B")
    return f"{consumed:g} particles of X consumed at two per B give {formed:g} of B"


def n29(item):
    start, left = 24.0, 6.0
    k = (start - left) / left
    assert abs(k - 3.0) < 1e-9, f"K recomputes to {k}"
    assert abs(start / left - 4.0) < 1e-9, "the 4.0 distractor must use the starting count"
    h.shows(item, "3.0")
    return f"{start - left:g} of product over {left:g} of reactant recomputes K as {k:g}"


NUMERIC = {15: n15, 16: n16, 21: n21, 23: n23, 24: n24, 27: n27, 29: n29}


CLAIMS = [
 ("3.0",
  "EK 7.8.A.1: a particulate representation can describe the value of the equilibrium constant. Recomputed in q1 from the tabulated equilibrium counts."),
 ("Three quarters of them",
  "EK 7.8.A.1 covers the relative numbers of particles present PRIOR TO and at equilibrium, which is what makes the two rows comparable. Recomputed in q2."),
 ("0.25",
  "EK 7.8.A.1 with a stoichiometric coefficient of two, which enters the expression as a square. Recomputed in q3, which also recomputes the unsquared distractor."),
 ("Two particles of X for each particle of Y",
  "EK 7.8.A.1: the change in the counts between the two rows is fixed by the coefficients of the balanced equation. Recomputed in q4."),
 ("16",
  "EK 7.8.A.1 on a reaction with a product coefficient of two. Recomputed in q5 from the tabulated equilibrium counts."),
 ("Twelve diatomic particles are present before reaction",
  "EK 7.8.A.1 makes the counts before and at equilibrium the content of the representation. Both totals are recomputed in q6 and agree at twelve, as an equation making two particles from two requires."),
 ("At 2 minutes",
  "EK 7.8.A.1 makes constant relative numbers the mark of equilibrium in a particulate account. The first pair of unchanged consecutive rows is located in q7."),
 ("1.0",
  "EK 7.8.A.1 ties the value of the constant to the counts once they have stopped changing. Recomputed in q8, which also recomputes the earlier quotient as a distractor."),
 ("Container P",
  "EK 7.8.A.1 makes a set of counts testable against a stated equilibrium constant. All four ratios are recomputed in q9 and exactly one matches."),
 ("Container S",
  "EK 7.8.A.1 makes the relative numbers comparable across containers. All four ratios are recomputed in q10 and the maximum is unique."),
 ("2.0",
  "EK 7.8.A.1 with a product coefficient of two, so the product count is squared. Recomputed in q11."),
 ("ratio of the coefficients",
  "EK 7.8.A.1 makes the before-and-at counts comparable, and the balanced equation fixes their ratio of change at one to two. Recomputed in q12, which also falsifies the conserved-total distractor."),
 ("particles continue to react in both directions",
  "EK 7.8.A.1 describes the relative numbers AT equilibrium, which are constant because the opposing processes proceed at equal rates. Equal counts are a special case fixed by the value of K rather than a general feature."),
 ("ratio of product particles to reactant particles required by the equilibrium constant",
  "EK 7.8.A.1 links the value of the constant to the RELATIVE numbers of particles, so two containers at the same temperature must share the ratio while their absolute counts follow from how much was charged."),
 ("16 particles of B",
  "EK 7.8.A.1 read backwards, from a stated constant to the counts. Recomputed in n15 from the total of twenty and the required ratio."),
 ("10 particles of C",
  "EK 7.8.A.1 with a constant below one, which must leave more reactant than product. Recomputed in n16."),
 ("undefined, so some reactant must remain",
  "The equilibrium expression divides by the reactant term, so a count of zero leaves no value of K to attach to the representation, and EK 7.8.A.1 ties a representation of equilibrium to such a value."),
 ("2 particles of A and 18 particles of B",
  "EK 7.8.A.1 states that a particulate representation can describe the value of the equilibrium constant, and a constant far above one is a product count far exceeding the reactant count."),
 ("Both containers are at equilibrium",
  "EK 7.8.A.1 attaches the constant to the relative numbers of particles, so two containers of the same reaction at the same temperature that share the ratio share the equilibrium condition."),
 ("reverse reaction speeds up as product accumulates",
  "A particulate account of the approach to equilibrium has product particles accumulating and the reverse process quickening until the two rates match, which is when the relative numbers of EK 7.8.A.1 stop changing."),
 ("2.0",
  "EK 7.8.A.1 with the reactant coefficient of two entering as a square. Recomputed in n21 against the unsquared distractor."),
 ("say nothing about the time taken",
  "EK 7.8.A.1 assigns the representation the relative numbers of particles and the value of the constant. A composition at one moment contains no information about the interval that produced it, so no rate can be read from it."),
 ("3.0",
  "EK 7.8.A.1 where both species are present before reaction, so the change in one must be added to the starting count of the other. Recomputed in n23."),
 ("Both have the same reaction quotient",
  "EK 7.8.A.1 ties the constant to the relative numbers, so scaling every count by the same factor leaves the quotient unchanged. Recomputed in n24."),
 ("A(g) + B(g) to C(g) + D(g)",
  "The total particle count is preserved only when the equation has equal numbers of particles on the two sides, which is true of exactly one of the five written equations."),
 ("Only a few reactant particles have been replaced",
  "EK 7.8.A.1 carries the value of K in the before-and-at comparison: a small constant makes the product term small at equilibrium, so most reactant particles are still present."),
 ("the six consumed give three of B",
  "EK 7.8.A.1 makes the two rows of counts comparable through the coefficients: two particles of A give one of B. Recomputed in n27."),
 ("equilibrium constant is larger at the higher temperature",
  "EK 7.8.A.1 ties the relative numbers at equilibrium to the value of the constant, so a larger product-to-reactant ratio at equilibrium is a larger constant. It is a statement about position, not about speed."),
 ("3.0",
  "EK 7.8.A.1 from a starting count and a remaining count. Recomputed in n29, which also recomputes the distractor formed from the starting count."),
 ("left out of the expression",
  "A pure solid has a concentration independent of how much is present and so is absent from the equilibrium expression, which limits what a count of its particles can contribute to the value EK 7.8.A.1 assigns to a representation."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[0]["table"] = dict(
            headers=h7_8._T_AB["headers"],
            rows=[[lab, a, ("6" if lab == "At equilibrium" else b)]
                  for lab, a, b in h7_8._T_AB["rows"]])

    def figure_language(mod, cl):
        mod.QUESTIONS[13]["q"] = "In the diagram shown, which counts are at equilibrium?"
        no_figure_language(mod)

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[14]["choices"])
        ch[0] = "15 particles of B"
        mod.QUESTIONS[14]["choices"] = ch
        cl[14] = ("15 particles of B", cl[14][1])

    return [("a table cell corrupted so the keyed K is false", corrupt_table),
            ("a stem referring to a diagram the bank cannot show", figure_language),
            ("a recomputed count no longer in the keyed choice", corrupt_numeric)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h7_8)
h.run(h7_8, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
