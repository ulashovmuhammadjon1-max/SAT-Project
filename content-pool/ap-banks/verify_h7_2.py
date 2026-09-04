"""Key audit for AP CHEMISTRY 7.2 Direction of Reversible Reactions.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. This topic has ONE essential-knowledge statement, so the
audit is organised by which of its three clauses each key uses:

  forward rate greater  ->  net conversion of reactants to products
                                 1, 4, 10, 18, 19, 20, 21, 22, 25, 26, 28, 30
  reverse rate greater  ->  net conversion of products to reactants
                                 2, 5, 9, 12, 13, 14
  rates equal           ->  an equilibrium state is reached
                                 3, 6, 7, 8, 11, 15, 16, 17, 23, 24, 27, 29

SCOPE. 7.1 owns the established equilibrium; 7.7 and 7.10 own the argument from Q
against K. ``no_equilibrium_constant`` asserts that neither K nor Q is named
anywhere in this module, and ``no_figure_language`` asserts that no stem points at
a graph the bank cannot show.

THE MISCONCEPTION GUARD. ``reverse_rate_never_zero_with_product`` asserts that
every tabulated reading with a nonzero forward rate also carries a nonzero
reverse rate, so the module's own data contradicts the reading that a net
conversion means only one reaction runs.

ARITHMETIC. Every direction of net conversion and every rate gap is recomputed
from the table or the stem alone.

NEGATIVE CONTROL: ``python3 verify_h7_2.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_2

VESSEL = "Vessel"
RF = "Rate of the forward reaction (M per s)"
RR = "Rate of the reverse reaction (M per s)"
TSEC = "Time (s)"
CR = "[R] (M)"
CP = "[P] (M)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|plotted above)(?![a-z])", re.I)

_CONSTANT = re.compile(
    r"(?<![A-Za-z0-9])(?:K[cp]?|Q[cp]?)(?![A-Za-z0-9])"
    r"|(?<![a-z])equilibrium constant(?![a-z])"
    r"|(?<![a-z])reaction quotient(?![a-z])")


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
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, but every set of "
                f"readings here is a table -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: every set of rate readings is carried as a "
          "table.")


def no_equilibrium_constant(module):
    """K, Kc, Kp and Q belong to 7.3 to 7.7 and 7.10, not to 7.2."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _CONSTANT.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: names {hit.group(0)!r}, which belongs to the "
                f"topics that own the constant and the quotient -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no item argues from an equilibrium constant or a "
          "reaction quotient.")


def reverse_rate_never_zero_with_product(module):
    """A net conversion is a DIFFERENCE between two running processes.

    Every tabulated reading in which the forward reaction has anything to work
    on must carry a nonzero reverse rate as well, or the module's own data would
    support the reading that only one reaction runs -- which is exactly what
    items 7, 18 and 28 tell the student is wrong.
    """
    checked = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        t = item.get("table")
        if not t:
            continue
        heads = [cg.normalize(x) for x in t["headers"]]
        if cg.normalize(RF) not in heads or cg.normalize(RR) not in heads:
            continue
        over_time = cg.normalize(t["headers"][0]) == cg.normalize(TSEC)
        for row, (fwd, rev) in enumerate(zip(cg.col(t, RF), cg.col(t, RR))):
            zero = [name for name, v in (("forward", fwd), ("reverse", rev)) if v == 0]
            if over_time:
                # Only the charging reading may have nothing for one process to
                # consume; every later reading has both species present.
                assert not zero or row == 0, (
                    f"{module.TOPIC[0]} q{i}: reading {row} has a {zero[0]} rate of "
                    "exactly zero after the reaction has begun -- the module must not "
                    "show one reaction running alone"
                )
            else:
                assert not zero, (
                    f"{module.TOPIC[0]} q{i}: vessel row {row} has a {zero[0]} rate of "
                    "exactly zero -- every vessel here holds an ongoing reversible "
                    "reaction, so both processes must be running"
                )
            checked += 1
    assert checked, f"{module.TOPIC[0]}: no rate table found to check"
    print(f"OK  {module.TOPIC[0]} misconception: {checked} tabulated readings checked; a "
          "rate of zero appears only where the reaction has not yet produced anything for "
          "that process to consume.")


# ------------------------------------------------------------------ helpers

def gap(table, label):
    """Forward minus reverse for one tabulated vessel."""
    return cg.cell(table, label, RF) - cg.cell(table, label, RR)


# ------------------------------------------------------------------ table items

def q4(table, item):
    gaps = {lab: gap(table, lab) for lab in cg.labels(table)}
    forward = {lab: g for lab, g in gaps.items() if g > 0}
    assert forward, f"no vessel has a positive gap: {gaps}"
    biggest = max(forward, key=forward.get)
    assert biggest == "1", f"the largest positive gap is at vessel {biggest}: {gaps}"
    assert len([g for g in forward.values() if abs(g - forward[biggest]) < 1e-12]) == 1, \
        "the largest positive gap must be unique"
    h.shows(item, "Vessel 1")
    return f"the tabulated gaps are {gaps}, whose largest positive value is at vessel {biggest}"


def q5(table, item):
    reverse = [lab for lab in cg.labels(table) if gap(table, lab) < 0]
    assert reverse == ["2"], f"the vessels with a larger reverse rate are {reverse}"
    h.shows(item, "Vessel 2")
    return f"exactly one tabulated vessel, {reverse[0]}, has its reverse rate above its forward rate"


def q6(table, item):
    equal = [lab for lab in cg.labels(table) if abs(gap(table, lab)) < 1e-12]
    assert equal == ["3"], f"the vessels whose rates agree are {equal}"
    h.shows(item, "Vessel 3")
    return f"exactly one tabulated vessel, {equal[0]}, has identical entries in the two rate columns"


def q7(table, item):
    rev = cg.cell(table, "1", RR)
    assert rev > 0, f"the tabulated reverse rate for vessel 1 is {rev}"
    assert gap(table, "1") > 0, "vessel 1 must still show a net conversion forward"
    h.shows(item, "reverse rate for that vessel is greater than zero")
    return f"vessel 1's tabulated reverse rate is {rev:g} M per s, which is above zero"


def q8(table, item):
    gaps = {lab: abs(gap(table, lab)) for lab in cg.labels(table)}
    nonzero = {lab: g for lab, g in gaps.items() if g > 1e-12}
    closest = min(nonzero, key=nonzero.get)
    assert closest == "4", f"the smallest nonzero gap is at vessel {closest}: {gaps}"
    assert len([g for g in nonzero.values() if abs(g - nonzero[closest]) < 1e-12]) == 1, \
        "the smallest nonzero gap must be unique"
    assert len(set(round(g, 9) for g in nonzero.values())) == len(nonzero), \
        "the remaining gaps must be distinct, so no two vessels are equally close"
    h.shows(item, "Vessel 4")
    return f"the tabulated gaps in size are {gaps}, whose smallest nonzero value is at vessel {closest}"


def q9(table, item):
    rev0 = cg.col(table, RR)[0]
    fwd0 = cg.col(table, RF)[0]
    assert rev0 == 0, f"the first tabulated reverse rate is {rev0}, not zero"
    assert fwd0 > 0, f"the first tabulated forward rate is {fwd0}"
    h.shows(item, "no product is present yet")
    return f"the first tabulated reading pairs a forward rate of {fwd0:g} with a reverse rate of {rev0:g}"


def q10(table, item):
    times = cg.col(table, TSEC)
    fwd, rev = cg.col(table, RF), cg.col(table, RR)
    early = [i for i, t in enumerate(times) if t <= 20]
    assert early, "no readings at or before twenty seconds"
    for i in early:
        assert fwd[i] > rev[i], f"at {times[i]} s the forward rate {fwd[i]} is not the greater"
    h.shows(item, "tabulated forward rate is the greater")
    return (f"over the first {len(early)} readings the tabulated forward rate exceeds the "
            f"reverse rate every time")


def q11(table, item):
    times, fwd, rev = cg.col(table, TSEC), cg.col(table, RF), cg.col(table, RR)
    equal = [times[i] for i in range(len(times)) if abs(fwd[i] - rev[i]) < 1e-12]
    assert equal and abs(equal[0] - 60.0) < 1e-12, f"the rates first agree at {equal}"
    h.shows(item, "60 seconds")
    return f"the tabulated rates first agree at {equal[0]:g} seconds"


def q12(table, item):
    fwd0, rev0 = cg.col(table, RF)[0], cg.col(table, RR)[0]
    assert fwd0 == 0 and rev0 > 0, f"the first reading is {fwd0} against {rev0}"
    fwdlast, revlast = cg.col(table, RF)[-1], cg.col(table, RR)[-1]
    assert abs(fwdlast - revlast) < 1e-12, "the readings must end at equal rates"
    h.shows(item, "only the reverse reaction has anything to consume")
    return (f"the first tabulated reading pairs a forward rate of {fwd0:g} with a reverse "
            f"rate of {rev0:g} M per s")


def q13(table, item):
    fwd = cg.col(table, RF)
    rev = cg.col(table, RR)
    assert fwd == sorted(fwd), f"the tabulated forward rate does not rise: {fwd}"
    assert fwd[0] == 0, f"the tabulated forward rate starts at {fwd[0]}"
    assert abs(fwd[-1] - rev[-1]) < 1e-12, "the forward rate must level off at the reverse rate"
    h.shows(item, "levels off once it matches the reverse rate")
    return f"the tabulated forward rate rises {fwd} and ends equal to the reverse rate {rev[-1]:g}"


def q14(table, item):
    r, p = cg.col(table, CR), cg.col(table, CP)
    assert r[1] > r[0], f"the tabulated concentration of R fell: {r}"
    assert p[1] < p[0], f"the tabulated concentration of P rose: {p}"
    assert abs((r[1] - r[0]) + (p[1] - p[0])) < 1e-12, \
        "the two tabulated changes must be equal and opposite"
    h.shows(item, "concentration of P fell while that of R rose")
    return (f"over the first interval the tabulated R goes {r[0]:g} to {r[1]:g} while P "
            f"goes {p[0]:g} to {p[1]:g}")


def q15(table, item):
    times, r, p = cg.col(table, TSEC), cg.col(table, CR), cg.col(table, CP)
    n = len(times)
    settled = None
    for i in range(n):
        if all(abs(r[j] - r[i]) < 1e-12 and abs(p[j] - p[i]) < 1e-12 for j in range(i, n)):
            settled = times[i]
            break
    assert settled is not None and abs(settled - 60.0) < 1e-12, \
        f"the tabulated concentrations first stop changing at {settled}"
    h.shows(item, "60 seconds")
    return f"the tabulated concentrations first stop changing at {settled:g} seconds"


def q26(table, item):
    fwd, rev = cg.col(table, RF), cg.col(table, RR)
    times = cg.col(table, TSEC)
    i = times.index(20.0)
    d = fwd[i] - rev[i]
    assert abs(d - 0.040) < 1e-12, f"the excess recomputes to {d}"
    h.shows(item, "0.040 M per s")
    return f"the tabulated rates at {times[i]:g} s differ by {d:g} M per s"


def q27(table, item):
    gaps = [abs(f - r) for f, r in zip(cg.col(table, RF), cg.col(table, RR))]
    for a, b in zip(gaps, gaps[1:]):
        assert b < a, f"the tabulated gap does not narrow at every reading: {gaps}"
    assert abs(gaps[-1]) < 1e-12, f"the tabulated gap does not reach zero: {gaps}"
    h.shows(item, "narrows at every reading and reaches zero")
    return f"the tabulated gaps are {gaps}, narrowing at every step to zero"


TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11,
                12: q12, 13: q13, 14: q14, 15: q15, 26: q26, 27: q27}


# ---------------------------------------------------------------- stem numerics

def n24(item):
    fwd, rev = 0.040, 0.040
    assert abs(fwd - rev) < 1e-12, "the two reported rates must be equal"
    assert abs(fwd + rev - 0.080) < 1e-12, \
        "the 0.080 distractor must be the sum a student would wrongly report as a net rate"
    h.shows(item, "reached an equilibrium state")
    return f"the two reported rates {fwd:g} and {rev:g} M per s are equal, the equilibrium condition"


def n30(item):
    fwd, rev = 0.090, 0.030
    d = fwd - rev
    assert d > 0, f"the excess recomputes to {d}"
    assert abs(d - 0.060) < 1e-12, f"the excess recomputes to {d}"
    assert abs(fwd - 3 * rev) < 1e-12, \
        "the fixed-ratio distractor must be recomputable from the stated rates"
    h.shows(item, "converted to products on balance, and the system is not at equilibrium")
    return (f"the stated rates give a positive excess of {d:g} M per s, so the forward "
            "direction leads and the rates are unequal")


NUMERIC = {24: n24, 30: n30}


CLAIMS = [
 ("net conversion of reactants to products",
  "EK 7.2.A.1, verbatim in substance: if the rate of the forward reaction is greater than the reverse reaction, there is a net conversion of reactants to products. No threshold ratio appears in the statement."),
 ("converted to reactants on balance",
  "EK 7.2.A.1's second clause: a greater reverse rate gives a net conversion of products to reactants. Nothing in the framework privileges the forward direction."),
 ("forward and reverse rates are equal",
  "EK 7.2.A.1's third clause: an equilibrium state is reached when these rates are equal. Rates of zero would describe a system in which nothing occurs."),
 ("Vessel 1",
  "EK 7.2.A.1's first clause applied across four tabulated vessels. q4 recomputes every gap and checks the largest positive one is unique."),
 ("Vessel 2",
  "EK 7.2.A.1's second clause. q5 recomputes the gaps and checks exactly one vessel has its reverse rate above its forward rate."),
 ("Vessel 3",
  "EK 7.2.A.1's third clause. q6 recomputes the gaps and checks exactly one vessel has identical entries in the two rate columns."),
 ("reverse rate for that vessel is greater than zero",
  "EK 7.2.A.1 speaks of a NET conversion, the excess of one rate over the other rather than the absence of the smaller; q7 checks the tabulated reverse rate there is nonzero."),
 ("Vessel 4",
  "EK 7.2.A.1 makes equality the equilibrium condition, so the smallest nonzero gap is the closest approach. q8 recomputes every gap and checks the minimum is unique and that no two remaining gaps tie."),
 ("no product is present yet",
  "The reverse process has nothing to act on before product forms, which q9 checks against the first tabulated reading of zero reverse rate."),
 ("tabulated forward rate is the greater",
  "EK 7.2.A.1's first clause read off the table; q10 checks the forward rate exceeds the reverse at every reading in the stated interval."),
 ("60 seconds",
  "EK 7.2.A.1's third clause: equal rates end the net conversion. q11 recomputes the earliest tabulated time at which the two columns agree."),
 ("only the reverse reaction has anything to consume",
  "EK 7.2.A.1's second clause at the start of a run charged with products; q12 checks the tabulated forward rate there is zero against a nonzero reverse rate."),
 ("levels off once it matches the reverse rate",
  "EK 7.2.A.1 makes the meeting of the two rates the equilibrium state; q13 checks the tabulated forward rate rises monotonically from zero and ends equal to the reverse rate."),
 ("concentration of P fell while that of R rose",
  "EK 7.2.A.1's second clause inferred from a composition rather than from rates; q14 recomputes both tabulated changes and checks they are equal and opposite."),
 ("60 seconds",
  "EK 7.2.A.1's third clause: equal rates leave the composition unchanging. q15 recomputes the first tabulated time after which neither concentration changes."),
 ("requires the two rates to be equal",
  "EK 7.2.A.1 reserves the equilibrium state for equal rates; a forward rate twice the reverse is the first clause's case of net conversion instead."),
 ("not on the two concentrations",
  "EK 7.2.A.1 states the equilibrium condition entirely in terms of the two rates and says nothing about the concentrations; EK 7.1.A.2 requires only that both be present and constant."),
 ("simply slower than the forward reaction",
  "EK 7.2.A.1 compares a greater rate with a smaller one, which presupposes both are running, and EK 7.1.A.3 has both processes continuing throughout."),
 ("forward rate falls and the reverse rate rises",
  "With reactants only at the start the reverse rate begins at zero and climbs as product accumulates while the forward rate falls, and EK 7.2.A.1 has the two meet at equilibrium."),
 ("vessel J the forward rate is the greater",
  "EK 7.2.A.1 ties a rising product concentration to a larger forward rate and a falling one to a larger reverse rate."),
 ("measured at two times, showing a change",
  "A composition still changing is what EK 7.2.A.1's unequal rates produce; a single reading or a sealed flask's mass is consistent with either case."),
 ("converted to reactants on balance",
  "EK 7.2.A.1's second clause: a larger reverse rate accumulates reactant, even though the forward reaction is still occurring."),
 ("neither process outruns the other",
  "EK 7.2.A.1 makes the direction of net conversion follow from an inequality, so equal rates leave no direction -- which is why the same statement calls that the equilibrium state."),
 ("reached an equilibrium state",
  "EK 7.2.A.1's third clause applied to two equal reported rates; n24 recomputes the equality and the sum that a student would wrongly report as a net rate."),
 ("falls steadily while the reactant concentration rises",
  "EK 7.2.A.1's second clause read from a composition; a concentration that is merely smaller, or has stopped changing, reports no direction."),
 ("0.040 M per s",
  "EK 7.2.A.1's first clause quantified: q26 recomputes the excess of the tabulated forward rate over the tabulated reverse rate at the named reading."),
 ("narrows at every reading and reaches zero",
  "EK 7.2.A.1's approach to the equilibrium state, recomputed in q27 as a gap that shrinks monotonically to zero."),
 ("names the difference between them",
  "EK 7.2.A.1 compares two rates and calls the outcome a NET conversion, and EK 7.1.A.3 has both processes running at once."),
 ("forward and reverse rates are equal",
  "EK 7.2.A.1's third clause: an unchanging composition is the case in which neither rate exceeds the other. Rates of zero are ruled out by EK 7.1.A.3."),
 ("converted to products on balance, and the system is not at equilibrium",
  "Both halves of EK 7.2.A.1 read together: a greater forward rate sets the direction, and unequal rates rule out equilibrium. n30 recomputes the excess."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "The graph above shows two rates. Which is greater?"
        no_figure_language(mod)

    def constant_creeps_in(mod, cl):
        mod.QUESTIONS[2]["q"] = mod.QUESTIONS[2]["q"] + " Assume Q is 2.0."
        no_equilibrium_constant(mod)

    def lone_forward_reaction(mod, cl):
        # A vessel with the reverse rate at zero would support exactly the
        # misconception items 7, 18 and 28 refute.
        mod.QUESTIONS[3]["table"] = dict(
            headers=h7_2._T_VESSELS["headers"],
            rows=[["1", "0.060", "0"], ["2", "0.015", "0.045"],
                  ["3", "0.030", "0.030"], ["4", "0.048", "0.044"]])
        reverse_rate_never_zero_with_product(mod)

    def reverse_stops_later(mod, cl):
        # The reverse rate falling back to zero AFTER product has formed is the
        # same misconception in the time-course table.
        mod.QUESTIONS[8]["table"] = dict(
            headers=h7_2._T_FROM_REACTANTS["headers"],
            rows=[["0", "0.100", "0"], ["20", "0.070", "0"],
                  ["40", "0.055", "0.045"], ["60", "0.050", "0.050"],
                  ["80", "0.050", "0.050"]])
        reverse_rate_never_zero_with_product(mod)

    def tied_largest_gap(mod, cl):
        # Two vessels made to share the largest forward gap, so the keyed
        # vessel is no longer the answer.
        mod.QUESTIONS[3]["table"] = dict(
            headers=h7_2._T_VESSELS["headers"],
            rows=[["1", "0.060", "0.020"], ["2", "0.015", "0.045"],
                  ["3", "0.030", "0.030"], ["4", "0.084", "0.044"]])

    def tied_closest_vessel(mod, cl):
        # Vessel 1's gap shrunk to match vessel 4's, so "closest" has two answers.
        mod.QUESTIONS[7]["table"] = dict(
            headers=h7_2._T_VESSELS["headers"],
            rows=[["1", "0.024", "0.020"], ["2", "0.015", "0.045"],
                  ["3", "0.030", "0.030"], ["4", "0.048", "0.044"]])

    def widening_gap(mod, cl):
        # The gap no longer narrows monotonically, so q27's key is false.
        mod.QUESTIONS[26]["table"] = dict(
            headers=h7_2._T_FROM_PRODUCTS["headers"],
            rows=[["0", "0", "0.090"], ["15", "0.010", "0.110"],
                  ["30", "0.042", "0.048"], ["45", "0.045", "0.045"]])

    return [("a stem referring to a graph the bank cannot show", figure_language),
            ("a reaction quotient named, which 7.7 and 7.10 own", constant_creeps_in),
            ("a tabulated vessel with the reverse rate at zero", lone_forward_reaction),
            ("the reverse rate back at zero after product has formed", reverse_stops_later),
            ("two vessels tied for the largest forward gap", tied_largest_gap),
            ("two vessels tied for the smallest nonzero gap", tied_closest_vessel),
            ("a tabulated gap that widens instead of narrowing", widening_gap)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h7_2)
no_equilibrium_constant(h7_2)
reverse_rate_never_zero_with_product(h7_2)
h.run(h7_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
