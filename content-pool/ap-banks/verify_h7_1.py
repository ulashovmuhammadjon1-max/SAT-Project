"""Key audit for AP CHEMISTRY 7.1 Introduction to Equilibrium.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  7.1.A.1  many observable processes are reversible, with evaporation and
           condensation, absorption and desorption, dissolution and
           precipitation, proton transfer and electron transfer as the
           framework's own examples            3, 4, 13, 14, 19, 23
  7.1.A.2  at equilibrium no observable change occurs, reactants and products
           are simultaneously present, and the concentrations or partial
           pressures of all species remain constant
                                        1, 5, 6, 7, 11, 15, 17, 18, 20, 24, 26, 28, 30
  7.1.A.3  the equilibrium state is dynamic: the forward and reverse processes
           continue at equal rates, giving no NET change
                                                2, 8, 9, 10, 21, 27, 29
  7.1.A.4  readings of concentration, partial pressure or rate against time
           show equilibrium being established     12, 16, 22, 25

THE FIGURE PROBLEM. EK 7.1.A.4 makes a graph against time the representation of
this topic and this bank cannot show one, so every one of them is a table of
readings against time. ``no_figure_language`` asserts that no stem or choice
refers to a picture -- the defect SCIENCE_BRIEF.md names and the project has
shipped once.

TWO SCOPE CHECKS. ``no_equilibrium_constant`` keeps K, Kc, Kp and the reaction
quotient out of this module: 7.3 owns their form, 7.4 owns computing one and 7.5
owns what its size means. ``equilibrium_is_not_equality`` asserts that every
tabulated equilibrium in this module is reached at UNEQUAL concentrations, which
is what stops the module from quietly teaching the misconception EK 7.1.A.2's
word "constant" exists to rule out.

ARITHMETIC. Every time at which equilibrium is first established, and every
tabulated change, is recomputed from the table alone.

NEGATIVE CONTROL: ``python3 verify_h7_1.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_1

TIME = "Time (min)"
CA = "[A] (M)"
CB = "[B] (M)"
TSEC = "Time (s)"
RF = "Rate of the forward reaction (M per s)"
RR = "Rate of the reverse reaction (M per s)"
PX = "Partial pressure of X (atm)"
PY = "Partial pressure of Y (atm)"
V20 = "[R] at 20 min (M)"
V30 = "[R] at 30 min (M)"
V40 = "[R] at 40 min (M)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|plotted above)(?![a-z])", re.I)

# 7.3, 7.4 and 7.5 own the equilibrium constant and the reaction quotient. A bare
# capital K or Q, with explicit lookarounds rather than \b, plus the spelled-out
# names.
_CONSTANT = re.compile(
    r"(?<![A-Za-z0-9])(?:K[cp]?|Q[cp]?)(?![A-Za-z0-9])"
    r"|(?<![a-z])equilibrium constant(?![a-z])"
    r"|(?<![a-z])reaction quotient(?![a-z])")


def _facing(item):
    """Every student-facing string on one question, including its table."""
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
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every reading "
                f"against time here is a table -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every set of readings against time is carried "
          "as a table.")


def no_equilibrium_constant(module):
    """K, Kc, Kp and Q belong to 7.3, 7.4 and 7.5, not to 7.1."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _CONSTANT.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: names {hit.group(0)!r}, which is 7.3 to 7.5's "
                f"material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item writes or evaluates an equilibrium "
          "constant or a reaction quotient.")


def equilibrium_is_not_equality(module):
    """EK 7.1.A.2 says CONSTANT, not EQUAL -- the module's data must say so too."""
    checked = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        t = item.get("table")
        if not t:
            continue
        heads = [cg.normalize(x) for x in t["headers"]]
        if cg.normalize(CA) in heads and cg.normalize(CB) in heads:
            a, b = cg.col(t, CA)[-1], cg.col(t, CB)[-1]
            assert abs(a - b) > 1e-9, (
                f"{module.TOPIC[0]} q{i}: the tabulated equilibrium is reached at EQUAL "
                f"concentrations ({a} and {b}), which is the misconception EK 7.1.A.2's "
                "word 'constant' exists to rule out"
            )
            checked += 1
    assert checked, f"{module.TOPIC[0]}: no concentration table found to check"
    print(f"OK  {module.TOPIC[0]} misconception: {checked} tabulated equilibrium/equilibria "
          "reached at unequal concentrations, so the data contradicts 'equal means "
          "equilibrium'.")


# ------------------------------------------------------------------ helpers

def first_constant(table, time_header, value_headers):
    """The first tabulated time after which no listed column changes again."""
    times = cg.col(table, time_header)
    cols = [cg.col(table, hdr) for hdr in value_headers]
    n = len(times)
    for i in range(n):
        if all(all(abs(c[j] - c[i]) < 1e-12 for j in range(i, n)) for c in cols):
            return times[i], i
    raise AssertionError(f"no tabulated time after which the readings stop changing: {cols}")


# ------------------------------------------------------------------ table items

def q5(table, item):
    t, i = first_constant(table, TIME, [CA, CB])
    assert abs(t - 6.0) < 1e-12, f"the readings first stop changing at {t} minutes"
    assert i > 0, "the readings must change at least once before settling"
    h.shows(item, "6 minutes")
    return f"the tabulated readings first stop changing at {t:g} minutes, row index {i}"


def q6(table, item):
    a, b = cg.col(table, CA)[-1], cg.col(table, CB)[-1]
    assert abs(a - b) > 1e-9, f"the settled concentrations are equal: {a} and {b}"
    a0, b0 = cg.col(table, CA)[-2], cg.col(table, CB)[-2]
    assert abs(a - a0) < 1e-12 and abs(b - b0) < 1e-12, "the last two rows must agree"
    h.shows(item, "not equal to each other")
    return f"the settled tabulated values {a:g} and {b:g} are constant and differ"


def q7(table, item):
    a = cg.col(table, CA)[-1]
    assert a > 0, f"the tabulated concentration of A settles at {a}, not above zero"
    b = cg.col(table, CB)[-1]
    assert b > 0, f"the tabulated concentration of B settles at {b}"
    h.shows(item, "simultaneously present at equilibrium")
    return f"the tabulated concentration of A settles at {a:g} M, with B present at {b:g} M"


def q8(table, item):
    f, r = cg.col(table, RF)[-1], cg.col(table, RR)[-1]
    assert abs(f - r) < 1e-12, f"the settled rates differ: {f} and {r}"
    assert f > 0, f"the settled rate is {f}, not greater than zero"
    h.shows(item, "both are greater than zero")
    return f"the two tabulated rates settle at the same nonzero value, {f:g} M per s"


def q9(table, item):
    times = cg.col(table, TSEC)
    fwd, rev = cg.col(table, RF), cg.col(table, RR)
    equal = [times[i] for i in range(len(times)) if abs(fwd[i] - rev[i]) < 1e-12]
    assert equal and abs(equal[0] - 20.0) < 1e-12, f"the rates first agree at {equal}"
    assert fwd[0] > rev[0], "the forward rate must start above the reverse rate"
    h.shows(item, "20 seconds")
    return f"the tabulated rates first agree at {equal[0]:g} seconds"


def q11(table, item):
    t, i = first_constant(table, TIME, [PX, PY])
    assert abs(t - 10.0) < 1e-12, f"the tabulated pressures first stop changing at {t}"
    assert i > 0, "the pressures must change at least once before settling"
    h.shows(item, "10 minutes")
    return f"the tabulated partial pressures first stop changing at {t:g} minutes"


def q12(table, item):
    px, py = cg.col(table, PX), cg.col(table, PY)
    fall, rise = px[0] - px[-1], py[-1] - py[0]
    assert abs(fall - 0.80) < 1e-12, f"the fall in the pressure of X recomputes to {fall}"
    assert abs(rise - 1.60) < 1e-12, f"the rise in the pressure of Y recomputes to {rise}"
    assert abs(rise - 2 * fall) < 1e-12, "the rise must be twice the fall for this reaction"
    h.shows(item, "fell by 0.80 atm while Y rose by 1.60 atm")
    return (f"the tabulated pressures give a fall of {fall:g} atm against a rise of "
            f"{rise:g} atm")


def q17(table, item):
    steady = [lab for lab in cg.labels(table)
              if len(set(round(cg.cell(table, lab, hdr), 9) for hdr in (V20, V30, V40))) == 1]
    assert steady == ["2"], f"the vessels whose three readings agree are {steady}"
    h.shows(item, "Vessel 2")
    return f"only vessel {steady[0]} has three identical tabulated readings"


def q18(table, item):
    falling = [lab for lab in cg.labels(table)
               if cg.cell(table, lab, V20) > cg.cell(table, lab, V30) >
               cg.cell(table, lab, V40)]
    assert sorted(falling) == ["1", "3"], f"the vessels still falling are {falling}"
    h.shows(item, "not yet reached equilibrium")
    return f"vessels {falling} show readings still falling from one time to the next"


def q22(table, item):
    sums = [a + b for a, b in zip(cg.col(table, CA), cg.col(table, CB))]
    assert len(set(round(s, 9) for s in sums)) == 1, f"the tabulated totals are {sums}"
    assert abs(sums[0] - 1.00) < 1e-12, f"the constant total recomputes to {sums[0]}"
    h.shows(item, "stays the same at every reading")
    return f"adding the two tabulated columns gives {sums[0]:g} M at every one of the {len(sums)} readings"


def q25(table, item):
    fwd, rev = cg.col(table, RF), cg.col(table, RR)
    assert fwd[1] < fwd[0], f"the forward rate rose from {fwd[0]} to {fwd[1]}"
    assert rev[1] > rev[0], f"the reverse rate fell from {rev[0]} to {rev[1]}"
    h.shows(item, "forward rate is falling while the reverse rate is rising")
    return (f"over the first interval the tabulated forward rate goes {fwd[0]:g} to "
            f"{fwd[1]:g} while the reverse goes {rev[0]:g} to {rev[1]:g}")


TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 11: q11, 12: q12,
                17: q17, 18: q18, 22: q22, 25: q25}

NUMERIC = {}


CLAIMS = [
 ("concentrations of all species remain constant",
  "EK 7.1.A.2, verbatim in substance: when equilibrium is reached, no observable changes occur and the concentrations or partial pressures of all species remain constant."),
 ("continue to occur at equal rates",
  "EK 7.1.A.3, verbatim in substance: the equilibrium state is dynamic, and the forward and reverse processes continue to occur at equal rates, resulting in no net observable change."),
 ("Evaporation and condensation",
  "EK 7.1.A.1 names evaporation and condensation of water first among its examples of reversible processes."),
 ("transfer of protons",
  "EK 7.1.A.1: important reversible chemical processes include the transfer of protons in acid-base reactions and the transfer of electrons in redox reactions."),
 ("6 minutes",
  "EK 7.1.A.2 makes constancy the signature of equilibrium. The first tabulated time after which nothing changes again is recomputed in q5."),
 ("not equal to each other",
  "EK 7.1.A.2 requires the concentrations to remain CONSTANT and both species to be present; it never says they become equal. q6 recomputes the settled values and asserts they differ."),
 ("simultaneously present at equilibrium",
  "EK 7.1.A.2 states that reactants and products are simultaneously present at equilibrium, and q7 checks the tabulated concentration of A settles above zero."),
 ("both are greater than zero",
  "EK 7.1.A.3 has both processes continuing at equal rates, so the shared rate is nonzero. q8 recomputes the settled rates from the table."),
 ("20 seconds",
  "EK 7.1.A.3 makes equality of the two rates the condition for equilibrium. The earliest tabulated time at which they agree is recomputed in q9."),
 ("equal rates that produce no net change",
  "EK 7.1.A.3 says the processes CONTINUE at equal rates; the absence of change is a balance between two ongoing processes rather than the absence of both."),
 ("10 minutes",
  "EK 7.1.A.2 extends constancy to partial pressures. The first tabulated time after which they stop changing is recomputed in q11."),
 ("fell by 0.80 atm while Y rose by 1.60 atm",
  "EK 7.1.A.4 licenses reading partial pressure against time. Both changes are recomputed from the table in q12, which also checks the rise is twice the fall."),
 ("continue at equal rates",
  "EK 7.1.A.1 names dissolution and precipitation of a salt as reversible and EK 7.1.A.3 makes the equilibrium state dynamic, so a constant mass of crystals is the absence of NET change."),
 ("Desorption",
  "EK 7.1.A.1 lists absorption and desorption of a gas as a reversible pair, each named process with its own reverse."),
 ("constant concentrations rather than equal ones",
  "EK 7.1.A.2 requires the concentrations to remain constant and says nothing about equality, so equality at one instant is no evidence of equilibrium."),
 ("partial pressure, or rate of reaction",
  "EK 7.1.A.4, verbatim in substance: graphs of concentration, partial pressure, or rate of reaction versus time can be used to understand the establishment of equilibrium."),
 ("Vessel 2",
  "EK 7.1.A.2 makes constancy the observable signature. q17 recomputes which of the three tabulated vessels has three identical readings and checks it is unique."),
 ("not yet reached equilibrium",
  "EK 7.1.A.2 requires constant concentrations at equilibrium, so a reading still falling shows the system has not got there. q18 recomputes which vessels are still falling."),
 ("continue to evaporate and to condense",
  "EK 7.1.A.1 gives evaporation and condensation as its example and EK 7.1.A.3 makes both continue at equal rates; the framework asserts equal RATES, not equal amounts of the phases."),
 ("Repeated measurements of every species",
  "EK 7.1.A.2 makes constancy of the concentrations of all species over time the observable signature; a single reading is consistent with a system still on its way."),
 ("how readily that species reacts",
  "EK 7.1.A.2 and EK 7.1.A.3 hold together: constant but different concentrations, with equal rates. Both can hold because a rate is not fixed by concentration alone."),
 ("stays the same at every reading",
  "A one-to-one conversion conserves the total, which q22 recomputes at every tabulated time. EK 7.1.A.4 licenses this reading of concentration against time."),
 ("transfer of electrons",
  "EK 7.1.A.1 names the transfer of electrons in redox reactions as an important reversible chemical process."),
 ("both processes continue",
  "EK 7.1.A.2 has both species present with constant concentrations and EK 7.1.A.3 has both processes continuing; a finished reaction would have no reverse process running."),
 ("forward rate is falling while the reverse rate is rising",
  "EK 7.1.A.4 licenses reading rate against time, and q25 recomputes the direction of each tabulated rate over the first interval."),
 ("partial pressure of a species is no longer changing",
  "EK 7.1.A.2 extends the constancy signature to partial pressures, and solid remains present, which is what distinguishes this from a reaction out of reactant."),
 ("the two changes cancel",
  "EK 7.1.A.3's word 'net' is doing the work: two ongoing changes of equal size in opposite directions leave every observable property fixed."),
 ("at several times and see whether the value stops changing",
  "EK 7.1.A.2 makes constancy over time the signature and EK 7.1.A.4 names concentration against time as the reading to take; the mass of a sealed flask is constant either way."),
 ("starts at zero and rises",
  "EK 7.1.A.3 has the two rates equal only at equilibrium, and with no product present at the start the reverse process has nothing to consume."),
 ("their amounts are unchanging",
  "EK 7.1.A.2 states in one sentence that reactants and products are simultaneously present and that the amounts of all species remain constant, with no claim of equality or of a coefficient ratio."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the graph above, what does an observer see?"
        no_figure_language(mod)

    def constant_creeps_in(mod, cl):
        mod.QUESTIONS[3]["q"] = mod.QUESTIONS[3]["q"] + " Assume Kc is 4.0."
        no_equilibrium_constant(mod)

    def equal_equilibrium(mod, cl):
        # The misconception this module exists to kill: an equilibrium reached at
        # EQUAL concentrations, behind a stem whose key says they are unequal.
        mod.QUESTIONS[5]["table"] = dict(
            headers=h7_1._T_TIMECOURSE["headers"],
            rows=[["0", "1.00", "0"], ["2", "0.75", "0.25"], ["4", "0.60", "0.40"],
                  ["6", "0.50", "0.50"], ["8", "0.50", "0.50"], ["10", "0.50", "0.50"]])
        equilibrium_is_not_equality(mod)

    def late_equilibrium(mod, cl):
        # The tabulated readings settle a reading later than the keyed time.
        mod.QUESTIONS[4]["table"] = dict(
            headers=h7_1._T_TIMECOURSE["headers"],
            rows=[["0", "1.00", "0"], ["2", "0.75", "0.25"], ["4", "0.65", "0.35"],
                  ["6", "0.62", "0.38"], ["8", "0.60", "0.40"], ["10", "0.60", "0.40"]])

    def broken_stoichiometry(mod, cl):
        # The pressure of Y no longer rises by twice the fall in X, so the keyed
        # pair of changes is false.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h7_1._T_PRESSURES["headers"],
            rows=[["0", "2.00", "0"], ["5", "1.40", "1.00"], ["10", "1.20", "1.20"],
                  ["15", "1.20", "1.20"], ["20", "1.20", "1.20"]])

    def second_steady_vessel(mod, cl):
        # A second vessel made steady, so "Vessel 2" is no longer the unique answer.
        mod.QUESTIONS[16]["table"] = dict(
            headers=h7_1._T_VESSELS["headers"],
            rows=[["1", "0.40", "0.40", "0.40"], ["2", "0.50", "0.50", "0.50"],
                  ["3", "0.60", "0.45", "0.38"]])

    return [("a stem referring to a graph the bank cannot show", figure_language),
            ("an equilibrium constant named, which is 7.3 to 7.5's material",
             constant_creeps_in),
            ("a tabulated equilibrium reached at EQUAL concentrations, behind a key "
             "that says they differ", equal_equilibrium),
            ("the readings settling one row later than the keyed time", late_equilibrium),
            ("the tabulated pressure changes no longer in the keyed two-to-one ratio",
             broken_stoichiometry),
            ("a second vessel made steady, so the keyed vessel is not unique",
             second_steady_vessel)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h7_1)
no_equilibrium_constant(h7_1)
equilibrium_is_not_equality(h7_1)
h.run(h7_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
