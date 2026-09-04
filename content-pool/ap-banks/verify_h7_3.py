"""Key audit for AP CHEMISTRY 7.3 Reaction Quotient and Equilibrium Constant.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  7.3.A.1  Qc describes relative concentrations at ANY time; Qp is the pressure
           form for gas phase reactions; the quotient tends toward K so that at
           equilibrium Kc = Qc; and the law of mass action fixes the arrangement
                       1, 2, 3, 4, 5, 6, 13, 14, 15, 17, 19, 20, 22, 23, 24, 25,
                       27, 28, 29, 30
  7.3.A.2  solids and pure liquids are left out, because their concentrations are
           independent of the amount              7, 8, 9, 10, 16, 18, 21, 26
  the two exclusion statements                    11, 12

SCOPE. h7_6.py's header records the agreement that 7.3 owns the FORM of the
quotient and what is left out of it. 7.4 owns getting a value of K from
measurements at equilibrium; 7.7 and 7.10 own comparing Q with K to predict a
direction. ``no_direction_prediction`` asserts that no item here asks which way
a reaction will go.

THE EXCLUSION STATEMENTS ARE ENFORCED. ``no_kc_kp_conversion`` asserts that no
item pairs a numeric key with a stem naming both Kc and Kp, and
``no_dissolved_gas_equilibrium`` asserts that no reaction anywhere in the module
puts a species in solution in equilibrium with the same species as a gas.

THE OMISSION IS CHECKED STRUCTURALLY. ``solids_absent_from_keyed_expression``
reads the species the stem labels (s) or (l) and the species the keyed
expression actually contains, as exact formulas rather than as substrings, and
asserts they do not overlap. Substring matching would have reported the C in CO.

ARITHMETIC. Every quotient is recomputed from the tabulated concentrations and
the balanced equation alone -- including the heterogeneous case, where the
recomputation is what proves the solid was left out.

NEGATIVE CONTROL: ``python3 verify_h7_3.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_3

CONC = "Concentration at the moment of sampling (M)"
AMOUNT = "Amount present at the moment of sampling"
MN2O4 = "[N2O4] (M)"
MNO2 = "[NO2] (M)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

# 7.7 and 7.10 own the argument from Q to a direction of travel. "proceeds" on
# its own is ordinary English ("as the reaction proceeds"), so the pattern
# requires the directional continuation -- an under-matching check is worse than
# none, and so is an over-matching one.
_DIRECTION = re.compile(
    r"(?<![a-z])(?:shift|shifts|shifted|which direction|in which direction)(?![a-z])"
    r"|(?<![a-z])proceeds? (?:to the|toward|in the direction)(?![a-z])"
    r"|(?<![a-z])net conversion(?![a-z])", re.I)

_LABELLED = re.compile(r"(?<![A-Za-z0-9])([A-Z][A-Za-z0-9]*)\((s|l|g|aq)\)")
_MATHRM = re.compile(r"\\mathrm\{([^}]*)\}")


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


def no_direction_prediction(module):
    """7.7 and 7.10 own the argument from Q to which way a reaction goes."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _DIRECTION.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: says {hit.group(0)!r}, which is 7.7 and 7.10's "
                f"material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item predicts a direction of travel from the "
          "quotient.")


def no_kc_kp_conversion(module):
    """The first exclusion statement attached to EK 7.3.A.1."""
    named = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        stem = item["q"]
        if re.search(r"(?<![A-Za-z])Kc(?![A-Za-z])", stem) and \
           re.search(r"(?<![A-Za-z])Kp(?![A-Za-z])", stem):
            named += 1
            key = h.keyed(item)
            assert not re.search(r"\d", key), (
                f"{module.TOPIC[0]} q{i}: names both Kc and Kp and keys a number "
                f"({key!r}), which the exclusion statement puts outside the exam"
            )
    print(f"OK  {module.TOPIC[0]} exclusion: {named} item(s) name both Kc and Kp, and none "
          "keys a numerical conversion between them.")


def no_dissolved_gas_equilibrium(module):
    """The second exclusion statement attached to EK 7.3.A.1."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            labelled = {}
            for formula, state in _LABELLED.findall(text):
                labelled.setdefault(formula, set()).add(state)
            both = [f for f, states in labelled.items() if {"aq", "g"} <= states]
            assert not both, (
                f"{module.TOPIC[0]} q{i}: {both} appears both dissolved and as a gas, the "
                "case the second exclusion statement removes from the exam"
            )
    print(f"OK  {module.TOPIC[0]} exclusion: no species anywhere appears both dissolved "
          "and as a gas.")


def solids_absent_from_keyed_expression(module):
    """EK 7.3.A.2, checked on exact formulas rather than on substrings.

    A substring test would report the C of a solid carbon inside the CO of the
    keyed expression. Comparing the \\mathrm{...} arguments as whole formulas
    against the species the stem labels (s) or (l) is exact.
    """
    checked = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        key = h.keyed(item)
        present = {arg.replace("_", "").replace("{", "").replace("}", "")
                   for arg in _MATHRM.findall(key)}
        if not present:
            continue
        condensed = {f for f, state in _LABELLED.findall(item["q"]) if state in ("s", "l")}
        overlap = present & condensed
        assert not overlap, (
            f"{module.TOPIC[0]} q{i}: the keyed expression contains {sorted(overlap)}, "
            "which the stem labels a solid or a pure liquid and EK 7.3.A.2 leaves out"
        )
        if condensed:
            checked += 1
    assert checked >= 2, (
        f"{module.TOPIC[0]}: only {checked} keyed expression(s) had a condensed phase in "
        "the stem to check against"
    )
    print(f"OK  {module.TOPIC[0]} omission: {checked} keyed expression(s) checked against "
          "the solids and pure liquids named in their own stems; none contains one.")


# ------------------------------------------------------------------ arithmetic

def q_no2(no2, n2o4):
    """EK 7.3.A.1 for N2O4(g) to 2 NO2(g), written once."""
    return (no2 ** 2) / n2o4


def q_so3(so3, so2, o2):
    """EK 7.3.A.1 for 2 SO2(g) + O2(g) to 2 SO3(g), written once."""
    return (so3 ** 2) / ((so2 ** 2) * o2)


# ------------------------------------------------------------------ table items

def q14(table, item):
    no2 = cg.cell(table, "NO2(g)", CONC)
    n2o4 = cg.cell(table, "N2O4(g)", CONC)
    v = q_no2(no2, n2o4)
    assert abs(v - 0.80) < 1e-12, f"the quotient recomputes to {v}"
    assert abs(no2 / n2o4 - 2.0) < 1e-12, \
        "the unsquared value must be recomputable, since it is the standard error"
    h.shows(item, "0.80")
    return f"squaring the tabulated {no2:g} M and dividing by {n2o4:g} M gives {v:g}"


def q15(table, item):
    so2 = cg.cell(table, "SO2(g)", CONC)
    o2 = cg.cell(table, "O2(g)", CONC)
    so3 = cg.cell(table, "SO3(g)", CONC)
    v = q_so3(so3, so2, o2)
    assert abs(v - 0.50) < 1e-12, f"the quotient recomputes to {v}"
    h.shows(item, "0.50")
    return (f"the tabulated {so3:g} M squared, over {so2:g} M squared times {o2:g} M, "
            f"gives {v:g}")


def q16(table, item):
    h2o = cg.cell(table, "H2O(g)", AMOUNT)
    co = cg.cell(table, "CO(g)", AMOUNT)
    h2 = cg.cell(table, "H2(g)", AMOUNT)
    mass = cg.cell(table, "C(s)", AMOUNT)
    v = (co * h2) / h2o
    assert abs(v - 0.20) < 1e-12, f"the quotient recomputes to {v}"
    with_solid = v / mass
    assert abs(with_solid - 0.20 / 12.0) < 1e-12, "the solid-included value must recompute"
    assert abs(with_solid - v) > 1e-6, (
        "including the tabulated mass must change the answer, or the check proves nothing"
    )
    h.shows(item, "0.20")
    return (f"the two tabulated product concentrations over the tabulated reactant give "
            f"{v:g}, while dividing by the {mass:g} gram solid would give {with_solid:.4f}")


def q23(table, item):
    qs = {lab: q_no2(cg.cell(table, lab, MNO2), cg.cell(table, lab, MN2O4))
          for lab in cg.labels(table)}
    biggest = max(qs, key=qs.get)
    assert biggest == "2", f"the largest quotient is at mixture {biggest}: {qs}"
    assert len([v for v in qs.values() if abs(v - qs[biggest]) < 1e-12]) == 1, \
        "the largest quotient must be unique"
    no2s = [cg.cell(table, lab, MNO2) for lab in cg.labels(table)]
    assert len(set(no2s)) < len(no2s), (
        "two mixtures must share an NO2 concentration, or comparing that column alone "
        "would settle the item and the exponent rule would not be tested"
    )
    h.shows(item, "Mixture 2")
    return f"the three recomputed quotients are {qs}, whose unique maximum is at mixture {biggest}"


def q27(table, item):
    no2 = cg.cell(table, "NO2(g)", CONC)
    n2o4 = cg.cell(table, "N2O4(g)", CONC)
    unsquared = no2 / n2o4
    assert abs(unsquared - 2.0) < 1e-12, f"the unsquared value recomputes to {unsquared}"
    correct = q_no2(no2, n2o4)
    assert abs(correct - unsquared) > 1e-6, \
        "the correct and unsquared values must differ, or the item asks nothing"
    h.shows(item, "2.0")
    return (f"dividing the tabulated {no2:g} M by {n2o4:g} M without the exponent gives "
            f"{unsquared:g}, against the correct {correct:g}")


def q30(table, item):
    so2 = cg.cell(table, "SO2(g)", CONC)
    o2 = cg.cell(table, "O2(g)", CONC)
    so3 = cg.cell(table, "SO3(g)", CONC)
    correct = q_so3(so3, so2, o2)
    upside_down = ((so2 ** 2) * o2) / (so3 ** 2)
    assert abs(upside_down - 2.0) < 1e-12, f"the inverted value recomputes to {upside_down}"
    assert abs(upside_down * correct - 1.0) < 1e-12, \
        "the inverted value must be the reciprocal of the correct one"
    h.shows(item, "2.0")
    return (f"the tabulated concentrations give {correct:g} the right way up and "
            f"{upside_down:g} inverted, which are reciprocals")


TABLE_CHECKS = {14: q14, 15: q15, 16: q16, 23: q23, 27: q27, 30: q30}

NUMERIC = {}


CLAIMS = [
 ("relative concentrations of the reaction species at any time",
  "EK 7.3.A.1's opening sentence: the reaction quotient Qc describes the relative concentrations of reaction species at any time. The restriction to equilibrium belongs to the constant."),
 ("so that at equilibrium the two are equal",
  "EK 7.3.A.1: the reaction quotient tends toward the equilibrium constant such that at equilibrium Kc equals Qc and Kp equals Qp."),
 ("Partial pressures, written as Qp",
  "EK 7.3.A.1: for gas phase reactions the reaction quotient may instead be written in terms of partial pressures as Qp. A total pressure cannot distinguish the species."),
 ("\\frac{[\\mathrm{SO_3}]^{2}}{[\\mathrm{SO_2}]^{2}[\\mathrm{O_2}]}",
  "EK 7.3.A.1's law of mass action: products over reactants, each raised to the power of its coefficient. A coefficient is an exponent, never a multiplier."),
 ("\\frac{(P_{\\mathrm{SO_3}})^{2}}{(P_{\\mathrm{SO_2}})^{2}(P_{\\mathrm{O_2}})}",
  "EK 7.3.A.1's pressure form of the same expression, with each partial pressure raised to its own coefficient."),
 ("product concentrations in the numerator and the reactant concentrations in the denominator, each raised to its coefficient",
  "EK 7.3.A.1 writes the expression for (Kc, Qc) with C and D over A and B, each coefficient appearing as an exponent rather than as a multiplier or an added term."),
 ("Solids and pure liquids",
  "EK 7.3.A.2, verbatim in substance: the quotient does not include substances whose concentrations or partial pressures are independent of the amount, such as solids and pure liquids."),
 ("K_c = [\\mathrm{CO_2}]",
  "EK 7.3.A.2 removes both solids from the decomposition, leaving the gas alone; keeping a solid would make the constant depend on how much solid the flask held."),
 ("\\frac{[\\mathrm{CO}][\\mathrm{H_2}]}{[\\mathrm{H_2O}]}",
  "EK 7.3.A.1 puts products over reactants and EK 7.3.A.2 removes the solid carbon. Concentrations in the expression are multiplied, never added."),
 ("independent of the amount present",
  "EK 7.3.A.2 gives exactly this reason for the omission. A solid does take part in the reaction, which is why it is in the equation but not in the expression."),
 ("conceptual differences and attend to which one",
  "The first exclusion statement attached to EK 7.3.A.1: conversion between Kc and Kp will not be assessed, and students should be aware of the conceptual differences and pay attention to which is used."),
 ("dissolved species is in equilibrium with the same species",
  "The second exclusion statement attached to EK 7.3.A.1 names exactly that case; a solid with a gas is the ordinary heterogeneous equilibrium EK 7.3.A.2 handles."),
 ("defined at any time",
  "EK 7.3.A.1 defines the quotient at any time; what is reserved for equilibrium is its EQUALITY with the constant, not its existence."),
 ("0.80",
  "EK 7.3.A.1's law of mass action applied to the tabulated concentrations. Recomputed in q14, which also recomputes the unsquared value that is the standard error."),
 ("0.50",
  "EK 7.3.A.1 with two exponents, recomputed in q15 from the three tabulated concentrations."),
 ("0.20",
  "EK 7.3.A.2 removes the solid however much of it is present. q16 recomputes the quotient without the solid AND recomputes what including the tabulated mass would give, checking the two differ."),
 ("exponent on that species",
  "EK 7.3.A.1 raises each concentration to the power of its coefficient; a multiplier would give a different number for every mixture."),
 ("solid does not appear in the expression",
  "EK 7.3.A.2 leaves solids out because their concentrations are independent of the amount, so adding solid changes nothing in the expression."),
 ("\\frac{[\\mathrm{NH_3}]^{2}}{[\\mathrm{N_2}][\\mathrm{H_2}]^{3}}",
  "EK 7.3.A.1 with the coefficients of the ammonia synthesis; nitrogen's coefficient of one carries no written exponent."),
 ("\\frac{(P_{\\mathrm{NH_3}})^{2}}{(P_{\\mathrm{N_2}})(P_{\\mathrm{H_2}})^{3}}",
  "EK 7.3.A.1's pressure form mirrors the concentration form exactly; swapping the two exponents assigns each coefficient to the wrong species."),
 ("because a pure liquid is left out",
  "EK 7.3.A.2 names pure liquids alongside solids; the solvent's concentration is set by the liquid itself rather than by how much is in the flask."),
 ("evaluated at any moment",
  "EK 7.3.A.1 defines the quotient at any time and has it tend toward the constant, so the two words differ in WHEN they apply, not in which quantities they use."),
 ("Mixture 2",
  "EK 7.3.A.1's expression evaluated for three tabulated mixtures. q23 recomputes all three, checks the maximum is unique, and checks that the NO2 column alone would not settle it."),
 ("partial pressure of each species separately",
  "EK 7.3.A.1 writes Kp with one partial pressure per species; a single total pressure gives the same value for mixtures of quite different composition."),
 ("the quotient equals the constant",
  "EK 7.3.A.1: at equilibrium Kc equals Qc, and the constant belongs to the reaction and temperature rather than to how the vessel was charged."),
 ("dissolved solute and the gas only",
  "EK 7.3.A.2 removes solids and pure liquids and leaves everything whose amount can change; a solute and a gas both qualify."),
 ("2.0",
  "The value obtained by omitting the exponent EK 7.3.A.1 requires. Recomputed in q27 alongside the correct value, which is checked to differ."),
 ("reciprocal of the correct value",
  "EK 7.3.A.1 fixes which species go in the numerator, so exchanging the sides exchanges numerator and denominator. A concentration quotient is positive, so no sign change is available."),
 ("built from the supplied partial pressures",
  "EK 7.3.A.1 offers the pressure form for gas phase reactions, and its exclusion statement asks students to attend to which form is in use rather than to convert."),
 ("2.0",
  "The inverted arrangement of EK 7.3.A.1's expression. q30 recomputes it and checks it is the reciprocal of the correct value."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "The figure shows a quotient. What does it describe?"
        no_figure_language(mod)

    def direction_creeps_in(mod, cl):
        mod.QUESTIONS[12]["q"] = mod.QUESTIONS[12]["q"] + " In which direction will it go?"
        no_direction_prediction(mod)

    def kc_kp_conversion(mod, cl):
        mod.QUESTIONS[10]["q"] = "A reaction has Kc equal to 4.0 at 500 K. What is Kp?"
        ch = list(mod.QUESTIONS[10]["choices"])
        ch[0] = "160"
        mod.QUESTIONS[10]["choices"] = ch
        cl[10] = ("160", cl[10][1])
        no_kc_kp_conversion(mod)

    def dissolved_and_gas(mod, cl):
        mod.QUESTIONS[1]["q"] = ("For CO2(aq) to CO2(g), what does the quotient tend "
                                 "toward?")
        no_dissolved_gas_equilibrium(mod)

    def solid_kept_in_expression(mod, cl):
        ch = list(mod.QUESTIONS[8]["choices"])
        ch[0] = ("\\( K_c = \\frac{[\\mathrm{CO}][\\mathrm{H_2}]}"
                 "{[\\mathrm{C}][\\mathrm{H_2O}]} \\)")
        ch[1] = "\\( K_c = \\frac{[\\mathrm{CO}]}{[\\mathrm{H_2O}]} \\)"
        mod.QUESTIONS[8]["choices"] = ch
        cl[8] = ("\\frac{[\\mathrm{CO}][\\mathrm{H_2}]}{[\\mathrm{C}][\\mathrm{H_2O}]}",
                 cl[8][1])
        solids_absent_from_keyed_expression(mod)

    def solid_mass_used(mod, cl):
        # The tabulated solid mass changed to 1 gram, so including it or leaving
        # it out give the same number and the item stops testing EK 7.3.A.2.
        mod.QUESTIONS[15]["table"] = dict(
            headers=h7_3._T_HETERO["headers"],
            rows=[["C(s)", "1 gram of solid"], ["H2O(g)", "0.50 M"],
                  ["CO(g)", "0.20 M"], ["H2(g)", "0.50 M"]])

    def tied_largest_quotient(mod, cl):
        mod.QUESTIONS[22]["table"] = dict(
            headers=h7_3._T_MIXTURES["headers"],
            rows=[["1", "0.20", "0.40"], ["2", "0.20", "0.40"], ["3", "0.10", "0.20"]])

    return [("a stem referring to a figure the bank cannot show", figure_language),
            ("an item predicting a direction, which 7.7 and 7.10 own", direction_creeps_in),
            ("a numerical conversion between Kc and Kp, which the exclusion statement bars",
             kc_kp_conversion),
            ("a species placed both dissolved and as a gas, which the second exclusion "
             "statement bars", dissolved_and_gas),
            ("a keyed expression that keeps the solid EK 7.3.A.2 removes",
             solid_kept_in_expression),
            ("the tabulated solid mass set to one, so including it would change nothing",
             solid_mass_used),
            ("two mixtures tied for the largest quotient", tied_largest_quotient)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h7_3)
no_direction_prediction(h7_3)
no_kc_kp_conversion(h7_3)
no_dissolved_gas_equilibrium(h7_3)
solids_absent_from_keyed_expression(h7_3)
h.run(h7_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
