"""Key audit for AP CHEMISTRY 7.4 Calculating the Equilibrium Constant.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. This topic has one essential-knowledge statement --
EK 7.4.A.1, that equilibrium constants can be determined from experimental
measurements of the concentrations or partial pressures of the reactants and
products at equilibrium -- so almost every key is that statement applied, with
EK 7.3.A.1 supplying the form of the expression and EK 7.3.A.2 the omission of
condensed phases.

  the value, computed from equilibrium measurements
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 17, 18, 19, 20, 23, 24
  what the measurements must be, and when they must be taken
                    1, 11, 13, 14, 15, 16, 21, 22, 26, 29, 30
  the omission of solids and pure liquids (EK 7.3.A.2)
                    6, 18, 25, 27, 28

SCOPE. 7.3 owns the form, 7.5 the size, 7.6 the algebra of manipulating a K, 7.7
the reverse calculation. ``no_k_manipulation`` asserts that no item here
reverses a reaction, multiplies its coefficients or adds two reactions, and
``no_solving_for_concentration`` asserts that no item is handed a K and asked
for a concentration.

ARITHMETIC. Every constant is recomputed from the tabulated or stated
measurements and the balanced equation alone. Where a condensed phase is
present the value is recomputed BOTH ways, and the check asserts the two differ
-- otherwise the omission would be untested.

NEGATIVE CONTROL: ``python3 verify_h7_4.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_4

CONC = "Equilibrium concentration (M)"
PRESS = "Equilibrium partial pressure (atm)"
MOLES = "Moles present at equilibrium"
CA = "[A] (M)"
CB = "[B] (M)"
TA = "[A] at equilibrium (M)"
TB = "[B] at equilibrium (M)"
TEMP = "Temperature (K)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

# 7.6 owns the four algebraic properties of K. Explicit phrases, not bare words:
# "reverse" alone appears legitimately in "the reverse reaction".
_MANIPULATION = re.compile(
    r"(?<![a-z])(?:reversed reaction|when a reaction is reversed|reversing the reaction"
    r"|multiplying the coefficients|coefficients are multiplied|adding the two reactions"
    r"|sum of the two reactions|overall reaction is the product)(?![a-z])", re.I)

# 7.7 owns going from a known K to an unknown concentration.
_SOLVE = re.compile(
    r"(?<![a-z])(?:given that (?:kc|kp|k) (?:is|equals)"
    r"|the equilibrium constant is [0-9]"
    r"|kc is [0-9]|kp is [0-9])", re.I)


def _facing(item):
    out = [item["q"], item["why"]] + list(item["choices"])
    t = item.get("table")
    if t:
        out += [str(x) for x in t["headers"]]
        out += [str(c) for r in t["rows"] for c in r]
    return out


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_k_manipulation(module):
    """7.6 owns reversing, scaling and adding reactions."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _MANIPULATION.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: says {hit.group(0)!r}, which is 7.6's material "
                f"-- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item manipulates a constant algebraically.")


def no_solving_for_concentration(module):
    """7.7 owns going from a stated K to an unknown equilibrium amount."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _SOLVE.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: hands the student a value of K ({hit.group(0)!r}), "
            "which is 7.7's direction of travel"
        )
    print(f"OK  {module.TOPIC[0]} scope: every item ends at a constant rather than "
          "starting from one.")


# ------------------------------------------------------------------ arithmetic
# Each expression is written once, from the balanced equation, and used by every
# check that needs it.

def k_hi(h2, i2, hi):
    """H2(g) + I2(g) to 2 HI(g)."""
    return (hi ** 2) / (h2 * i2)


def k_so3(so2, o2, so3):
    """2 SO2(g) + O2(g) to 2 SO3(g)."""
    return (so3 ** 2) / ((so2 ** 2) * o2)


def k_nh3(n2, h2, nh3):
    """N2(g) + 3 H2(g) to 2 NH3(g)."""
    return (nh3 ** 2) / (n2 * (h2 ** 3))


def k_n2o4(n2o4, no2):
    """N2O4 to 2 NO2, in either concentrations or pressures."""
    return (no2 ** 2) / n2o4


def k_ratio(a, b):
    """A to B."""
    return b / a


# ------------------------------------------------------------------ table items

def q2(table, item):
    h2 = cg.cell(table, "H2(g)", CONC)
    i2 = cg.cell(table, "I2(g)", CONC)
    hi = cg.cell(table, "HI(g)", CONC)
    k = k_hi(h2, i2, hi)
    assert abs(k - 16.0) < 1e-12, f"the constant recomputes to {k}"
    assert abs((hi ** 2) / h2 - 3.2) < 1e-12, \
        "dividing by one reactant only must give the 3.2 distractor"
    h.shows(item, "16")
    return f"the tabulated {hi:g} M squared over {h2:g} M times {i2:g} M recomputes as {k:g}"


def q3(table, item):
    so2 = cg.cell(table, "SO2(g)", CONC)
    o2 = cg.cell(table, "O2(g)", CONC)
    so3 = cg.cell(table, "SO3(g)", CONC)
    k = k_so3(so2, o2, so3)
    assert abs(k - 40.0) < 1e-12, f"the constant recomputes to {k}"
    assert abs(so3 / (so2 * o2) - 20.0) < 1e-12, \
        "the first-powers value must be the 20 distractor"
    h.shows(item, "40")
    return f"the tabulated concentrations recompute the constant as {k:g}"


def q4(table, item):
    n2 = cg.cell(table, "N2(g)", CONC)
    h2 = cg.cell(table, "H2(g)", CONC)
    nh3 = cg.cell(table, "NH3(g)", CONC)
    k = k_nh3(n2, h2, nh3)
    assert abs(k - 200.0) < 1e-12, f"the constant recomputes to {k}"
    squared = (nh3 ** 2) / (n2 * (h2 ** 2))
    assert abs(squared - 20.0) < 1e-12, \
        "squaring hydrogen instead of cubing it must give the 20 distractor"
    h.shows(item, "200")
    return (f"cubing the tabulated {h2:g} M and squaring the tabulated {nh3:g} M "
            f"recomputes the constant as {k:g}")


def q5(table, item):
    n2o4 = cg.cell(table, "N2O4(g)", PRESS)
    no2 = cg.cell(table, "NO2(g)", PRESS)
    k = k_n2o4(n2o4, no2)
    assert abs(k - 0.10) < 1e-12, f"the constant recomputes to {k}"
    assert abs(no2 / n2o4 - 0.50) < 1e-12, \
        "the unsquared ratio must be the 0.50 distractor and must differ from the key"
    h.shows(item, "0.10")
    return (f"the tabulated {no2:g} atm squared over {n2o4:g} atm recomputes the constant "
            f"as {k:g}")


def q7(table, item):
    a0 = cg.cell(table, "Before any reaction", CA)
    aeq = cg.cell(table, "At equilibrium", CA)
    beq = a0 - aeq
    k = k_ratio(aeq, beq)
    assert abs(beq - 0.20) < 1e-12, f"the product concentration recomputes to {beq}"
    assert abs(k - 0.25) < 1e-12, f"the constant recomputes to {k}"
    assert abs(beq / a0 - 0.20) < 1e-12, \
        "using the initial concentration in the denominator must give the 0.20 distractor"
    h.shows(item, "0.25")
    return (f"the tabulated fall from {a0:g} M to {aeq:g} M makes {beq:g} M of product, "
            f"and the ratio recomputes as {k:g}")


def q8(table, item):
    b0 = cg.cell(table, "Before any reaction", CB)
    beq = cg.cell(table, "At equilibrium", CB)
    assert b0 == 0, f"the tabulated starting concentration of B is {b0}"
    a0 = 0.50                       # stated in the stem
    assert "0.50 M A(g)" in item["q"], "the stem must state the initial concentration used"
    aeq = a0 - beq / 2.0            # A to 2 B
    k = (beq ** 2) / aeq
    assert abs(aeq - 0.40) < 1e-12, f"the remaining A recomputes to {aeq}"
    assert abs(k - 0.10) < 1e-12, f"the constant recomputes to {k}"
    assert abs((beq ** 2) / a0 - 0.080) < 1e-12, \
        "using the initial A must give the 0.080 distractor"
    h.shows(item, "0.10")
    return (f"two of B per A consumed leaves {aeq:g} M of A, and the constant recomputes "
            f"as {k:g}")


def q9(table, item):
    vol = 2.0                       # stated in the stem
    assert "2.0 L" in item["q"], "the stem must state the volume used"
    a = cg.cell(table, "A(g)", MOLES) / vol
    b = cg.cell(table, "B(g)", MOLES) / vol
    c = cg.cell(table, "C(g)", MOLES) / vol
    k = c / (a * b)
    assert abs(k - 0.25) < 1e-12, f"the constant recomputes to {k}"
    raw = cg.cell(table, "C(g)", MOLES) / (cg.cell(table, "A(g)", MOLES) *
                                           cg.cell(table, "B(g)", MOLES))
    assert abs(raw - 0.125) < 1e-12, "using moles directly must give the 0.125 distractor"
    assert abs(raw - k) > 1e-6, "dividing by the volume must change the answer"
    h.shows(item, "0.25")
    return (f"dividing each tabulated mole figure by {vol:g} L recomputes the constant as "
            f"{k:g}, against {raw:g} from the moles themselves")


def q10(table, item):
    ks = [k_ratio(cg.cell(table, lab, TA), cg.cell(table, lab, TB))
          for lab in cg.labels(table)]
    assert len(set(round(k, 9) for k in ks)) == 1, f"the three trials give {ks}"
    assert abs(ks[0] - 0.25) < 1e-12, f"the common value recomputes to {ks[0]}"
    concs = [cg.cell(table, lab, TA) for lab in cg.labels(table)]
    assert len(set(concs)) == len(concs), \
        "the three trials must have different compositions, or they show nothing"
    h.shows(item, "0.25, the same in all three trials")
    return f"the three tabulated trials all recompute the constant as {ks[0]:g}"


def q11(table, item):
    ks = [k_ratio(cg.cell(table, lab, TA), cg.cell(table, lab, TB))
          for lab in cg.labels(table)]
    assert len(set(round(k, 9) for k in ks)) == 1, f"the three trials give {ks}"
    spread = max(cg.col(table, TA)) / min(cg.col(table, TA))
    assert spread >= 2.0, (
        f"the tabulated compositions span only a factor of {spread}, too little to show "
        "the value is independent of the charging"
    )
    h.shows(item, "does not depend on the amounts")
    return (f"the tabulated compositions span a factor of {spread:g} and still recompute "
            f"the same constant, {ks[0]:g}")


def q12(table, item):
    k300 = k_ratio(cg.cell(table, "300", TA), cg.cell(table, "300", TB))
    assert abs(k300 - 0.25) < 1e-12, f"the constant at 300 K recomputes to {k300}"
    h.shows(item, "0.25")
    return f"the 300 K row recomputes the constant as {k300:g}"


def q13(table, item):
    k300 = k_ratio(cg.cell(table, "300", TA), cg.cell(table, "300", TB))
    k500 = k_ratio(cg.cell(table, "500", TA), cg.cell(table, "500", TB))
    assert k500 > k300, f"the higher temperature gives {k500}, not larger than {k300}"
    assert abs(k500 - 2 * k300) > 1e-9, \
        "the ratio must not be two, or the 'exactly twice' distractor would be true"
    h.shows(item, "higher temperature is the larger")
    return f"the two rows recompute constants of {k300:g} at 300 K and {k500:g} at 500 K"


def q23(table, item):
    so2 = cg.cell(table, "SO2(g)", CONC)
    o2 = cg.cell(table, "O2(g)", CONC)
    so3 = cg.cell(table, "SO3(g)", CONC)
    first_powers = so3 / (so2 * o2)
    correct = k_so3(so2, o2, so3)
    assert abs(first_powers - 20.0) < 1e-12, f"the first-powers value recomputes to {first_powers}"
    assert abs(first_powers - correct) > 1e-6, \
        "the two values must differ, or the item asks nothing"
    h.shows(item, "20")
    return (f"the tabulated concentrations give {first_powers:g} with no exponents against "
            f"{correct:g} with them")


def q29(table, item):
    h2 = cg.cell(table, "H2(g)", CONC)
    i2 = cg.cell(table, "I2(g)", CONC)
    assert abs(h2 - i2) < 1e-12, (
        "the two tabulated reactant concentrations must be equal, since one distractor "
        "offers that as a reason the expression could be shortened"
    )
    assert h2 > 0 and i2 > 0, "both reactant concentrations must be present in the table"
    h.shows(item, "requires the two reactant concentrations")
    return (f"the expression divides by both tabulated reactant concentrations, {h2:g} M "
            f"and {i2:g} M, equal though they are")


TABLE_CHECKS = {2: q2, 3: q3, 4: q4, 5: q5, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11,
                12: q12, 13: q13, 23: q23, 29: q29}


# ---------------------------------------------------------------- stem numerics

def _stated(item, pattern, what):
    """Read a number out of the stem, so the check cannot drift from the item."""
    m = re.search(pattern, item["q"])
    assert m, f"the stem does not state {what}: {item['q'][:80]!r}"
    return float(m.group(1))


def n6(item):
    p_co2 = _stated(item, r"pressure is ([0-9.]+)\s*\n?\s*atm", "the carbon dioxide pressure")
    mass = _stated(item, r"([0-9.]+) grams of solid", "the mass of solid")
    assert abs(p_co2 - 0.25) < 1e-12, "the stated pressure is the constant itself"
    assert abs(p_co2 / mass - 0.03125) < 1e-9, \
        "dividing by the tabulated mass must give the 0.031 distractor"
    assert abs(p_co2 / mass - p_co2) > 1e-6, "including the mass must change the answer"
    h.shows(item, "0.25")
    return (f"both solids drop out, leaving the stated {p_co2:g} atm as the constant, "
            f"against {p_co2 / mass:.3f} if the {mass:g} gram solid were included")


def n17(item):
    k = k_n2o4(0.10, 0.20)
    assert abs(k - 0.40) < 1e-12, f"the constant recomputes to {k}"
    assert abs(0.20 / 0.10 - 2.0) < 1e-12, "the unsquared ratio must be the 2.0 distractor"
    h.shows(item, "0.40")
    return f"squaring the stated 0.20 M and dividing by 0.10 M recomputes the constant as {k:g}"


def n18(item):
    co2 = _stated(item, r"concentration of CO2 is ([0-9.]+) M", "the CO2 concentration")
    co = _stated(item, r"that of CO is ([0-9.]+) M", "the CO concentration")
    mass = _stated(item, r"([0-9.]+) grams of carbon", "the mass of carbon")
    k = (co ** 2) / co2
    assert abs(k - 0.80) < 1e-12, f"the constant recomputes to {k}"
    assert abs(k / mass - 0.16) < 1e-12, \
        "dividing by the stated mass would give a different number"
    assert abs(k / mass - k) > 1e-6, "including the solid must change the answer"
    h.shows(item, "0.80")
    return (f"the solid drops out and the stated concentrations recompute the constant as "
            f"{k:g}, against {k / mass:g} if the {mass:g} gram solid were divided in")


def n19(item):
    a, b = 0.20, 0.40
    k = b / (a ** 2)
    assert abs(k - 10.0) < 1e-12, f"the constant recomputes to {k}"
    assert abs(b / a - 2.0) < 1e-12, "the unsquared ratio must be the 2.0 distractor"
    h.shows(item, "10")
    return f"dividing the stated {b:g} M by the square of {a:g} M recomputes the constant as {k:g}"


def n20(item):
    so2, o2, so3 = 0.10, 0.20, 0.20
    k = k_so3(so2, o2, so3)
    assert abs(k - 20.0) < 1e-12, f"the constant recomputes to {k}"
    assert abs(so3 / (so2 * o2) - 10.0) < 1e-12, \
        "the first-powers value must be the 10 distractor"
    h.shows(item, "20")
    return f"the stated partial pressures recompute the constant as {k:g}"


def n24(item):
    a0 = 1.00
    aeq = a0 / 2.0
    beq = a0 - aeq
    k = k_ratio(aeq, beq)
    assert abs(k - 1.0) < 1e-12, f"the constant recomputes to {k}"
    assert abs(aeq - beq) < 1e-12, "half conversion must leave the two concentrations equal"
    h.shows(item, "1.0")
    return (f"half of {a0:g} M leaves {aeq:g} M of each species, so the constant recomputes "
            f"as {k:g}")


NUMERIC = {6: n6, 17: n17, 18: n18, 19: n19, 20: n20, 24: n24}


CLAIMS = [
 ("concentrations or partial pressures of the reactants and products at equilibrium",
  "EK 7.4.A.1, verbatim in substance. Measurements taken at mixing describe a system that has not arrived, and coefficients alone fix the form rather than the value."),
 ("16",
  "EK 7.4.A.1 with EK 7.3.A.1's expression. Recomputed in q2, which also recomputes the value obtained by dividing by one reactant only."),
 ("40",
  "EK 7.4.A.1 with two exponents. Recomputed in q3, which also recomputes the first-powers value that is the standard error."),
 ("200",
  "EK 7.4.A.1 with a cubed reactant. Recomputed in q4, which also recomputes the value obtained by squaring hydrogen instead of cubing it."),
 ("0.10",
  "EK 7.4.A.1 in the pressure form permitted by EK 7.3.A.1. Recomputed in q5, which checks the unsquared ratio is a different number and appears as a distractor."),
 ("0.25",
  "EK 7.3.A.2 removes both solids, so the constant is the stated gas pressure itself. n6 recomputes what including the stated mass would give and checks it differs."),
 ("0.25",
  "EK 7.4.A.1 from an initial and an equilibrium measurement, with stoichiometry supplying the rest. Recomputed in q7 along with the distractor formed from the initial concentration."),
 ("0.10",
  "Two product molecules per reactant consumed, then EK 7.4.A.1. Recomputed in q8, which also recomputes the value obtained by using the initial concentration."),
 ("0.25",
  "EK 7.4.A.1 speaks of concentrations, so each tabulated mole figure is divided by the volume. q9 recomputes both ways and checks the two differ."),
 ("0.25, the same in all three trials",
  "EK 7.4.A.1 makes the value follow from any equilibrium mixture. q10 recomputes all three tabulated trials, checks they agree, and checks their compositions differ."),
 ("does not depend on the amounts",
  "The three tabulated trials span a factor of four in composition and give one value, which q11 recomputes and whose spread it checks."),
 ("0.25",
  "EK 7.4.A.1 applied to the lower-temperature row alone. Recomputed in q12."),
 ("higher temperature is the larger",
  "EK 7.4.A.1 gives a value from each row and EK 7.10.A.2 makes temperature change K. q13 recomputes both and checks the ratio is not two, so the 'exactly twice' option is false."),
 ("the quotient equals the constant only once equilibrium",
  "EK 7.3.A.1 makes the quotient equal the constant only at equilibrium, which is why EK 7.4.A.1 specifies measurements taken there."),
 ("reaction quotient at that moment",
  "EK 7.3.A.1 defines the quotient at any time; the expression can be evaluated early, and what it returns is simply not the constant."),
 ("The volume of the vessel",
  "EK 7.4.A.1 asks for concentrations, and moles become concentrations only on division by the volume; temperature fixes which constant is measured but does not enter the arithmetic."),
 ("0.40",
  "EK 7.4.A.1 with the coefficient of two as an exponent. Recomputed in n17 alongside the unsquared ratio."),
 ("0.80",
  "EK 7.3.A.2 removes the solid carbon whatever its mass. n18 recomputes the constant without it and checks that dividing by the stated mass would give a different number."),
 ("10",
  "EK 7.3.A.1 squares the reactant because its coefficient is two. Recomputed in n19 alongside the plain ratio."),
 ("20",
  "EK 7.4.A.1 in the pressure form, with both exponents. Recomputed in n20 alongside the first-powers value."),
 ("after the system has stopped changing",
  "EK 7.1.A.2 makes a system that has stopped changing an equilibrium, and EK 7.4.A.1 asks for every species' concentration there. One species alone leaves the expression unknown."),
 ("amount of reactant consumed follows from the amount of product formed",
  "The balanced equation converts product formed into reactant consumed, giving the equilibrium concentration EK 7.4.A.1 requires; the coefficients supply any ratio."),
 ("20",
  "The value obtained by dropping the exponents EK 7.3.A.1 requires. q23 recomputes it alongside the correct value and checks the two differ."),
 ("1.0",
  "Half conversion leaves equal concentrations, so EK 7.4.A.1's ratio is one. n24 recomputes it and checks the equality that produces it."),
 ("left out of the expression entirely",
  "EK 7.3.A.2 removes substances whose concentrations are independent of the amount, naming pure liquids; a coefficient cannot bring back an omitted species."),
 ("different temperatures",
  "EK 7.10.A.2 makes a change in temperature change K, while EK 7.4.A.1 makes the value follow from the equilibrium measurements alone, as this topic's three tabulated trials show."),
 ("changes whenever a different amount of solid is used",
  "EK 7.3.A.2 omits solids precisely because their concentrations are independent of the amount; a value depending on the mass weighed out could not be a property of the reaction."),
 ("solid decomposing to another solid and a single gas",
  "EK 7.3.A.2 removes both solids and leaves one gas; the other cases leave two or three species, and the last is the case the exclusion statement on EK 7.3.A.1 removes."),
 ("requires the two reactant concentrations",
  "EK 7.4.A.1 asks for reactants AND products at equilibrium. q29 checks the two tabulated reactant concentrations are equal, which makes the arithmetic easy without removing them."),
 ("reaction and the temperature",
  "EK 7.4.A.1 gives the same value from any equilibrium mixture of the reaction, and EK 7.10.A.2 makes temperature the thing that changes it."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "The graph above reports equilibrium data. What is Kc?"
        no_figure_language(mod)

    def manipulation_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = ("When a reaction is reversed, what happens to the "
                                 "constant?")
        no_k_manipulation(mod)

    def solving_creeps_in(mod, cl):
        mod.QUESTIONS[13]["q"] = ("The equilibrium constant is 4.0. What is the "
                                  "equilibrium concentration of B?")
        no_solving_for_concentration(mod)

    def solid_mass_matters(mod, cl):
        # The stated mass changed to one gram, so including it or omitting it give
        # the same number and the item no longer tests EK 7.3.A.2.
        mod.QUESTIONS[5]["q"] = mod.QUESTIONS[5]["q"].replace("8.0 grams", "1.0 grams")

    def trials_disagree(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h7_4._T_TRIALS["headers"],
            rows=[["1", "0.80", "0.20"], ["2", "0.40", "0.20"], ["3", "0.20", "0.05"]])

    def trials_identical(mod, cl):
        # Three trials with the SAME composition would agree trivially and would
        # show nothing about independence from the charging.
        mod.QUESTIONS[10]["table"] = dict(
            headers=h7_4._T_TRIALS["headers"],
            rows=[["1", "0.80", "0.20"], ["2", "0.80", "0.20"], ["3", "0.80", "0.20"]])

    def volume_made_irrelevant(mod, cl):
        # A one litre vessel makes moles and concentrations identical, so the item
        # would no longer test the division EK 7.4.A.1 requires.
        mod.QUESTIONS[8]["q"] = mod.QUESTIONS[8]["q"].replace("2.0 L", "1.0 L")

    def temperature_ratio_two(mod, cl):
        # A ratio of exactly two would make the distractor true as well as the key.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h7_4._T_TEMPS["headers"],
            rows=[["300", "0.80", "0.20"], ["500", "0.80", "0.40"]])

    return [("a stem referring to a graph the bank cannot show", figure_language),
            ("an item manipulating a constant, which 7.6 owns", manipulation_creeps_in),
            ("an item handed a constant and asked for a concentration, which 7.7 owns",
             solving_creeps_in),
            ("the stated solid mass set to one, so omitting it would change nothing",
             solid_mass_matters),
            ("one tabulated trial no longer giving the common constant", trials_disagree),
            ("three tabulated trials of identical composition, which show nothing",
             trials_identical),
            ("a one litre vessel, so dividing by the volume would change nothing",
             volume_made_irrelevant),
            ("the two temperatures set to a ratio of exactly two, making a distractor true",
             temperature_ratio_two)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h7_4)
no_k_manipulation(h7_4)
no_solving_for_concentration(h7_4)
h.run(h7_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
