"""Key audit for AP CHEMISTRY 9.10 Cell Potential Under Nonstandard Conditions.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  9.10.A.1  the potential varies with the concentrations of the active species,
            is a driving force toward equilibrium, and grows in magnitude with
            the distance from equilibrium    1, 2, 3, 13, 18, 24, 28, 29
  9.10.A.2  equilibrium arguments such as Le Chatelier's principle do not apply,
            because the systems are not in equilibrium      4, 26
  9.10.A.3  the standard potential sits at a reaction quotient of 1; the
            magnitude falls to zero at equilibrium, where the quotient equals the
            constant; a deviation further from equilibrium than a quotient of 1
            increases the magnitude and one closer decreases it; in concentration
            cells the direction of spontaneous electron flow is the direction
            needed to reach equilibrium
                    5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23,
                    25, 29, 30
  9.10.A.4  algorithmic Nernst calculations are insufficient; the qualitative use
            of \\( E = E^\\circ - \\frac{RT}{nF} \\ln Q \\) is what is asked for
                                             10, 11, 27, 28

EK 9.10.A.4 IS A FENCE, AND ``no_algorithmic_nernst`` IS THE GATE ON IT. The
framework calls an algorithmic Nernst calculation INSUFFICIENT, so no item may
produce a nonstandard potential as a number. The check bans a numeric voltage
anywhere in a student-facing string. What the items DO compute is a reaction
quotient and its position relative to 1 and to the equilibrium constant, which
is the comparison EK 9.10.A.3 is itself written in.

THE THREE-WAY VERDICT, and why the verifier decides it rather than reading it.
EK 9.10.A.3 gives four cases -- the standard point, equilibrium, a deviation
further from equilibrium than a quotient of 1, and one closer. Which case a set
of concentrations falls into is settled by comparing the distance from the
quotient to the constant against the distance from 1 to the constant, and
``quotient_verdict`` makes that comparison from the numbers alone. It refuses the
one ambiguous case it can meet -- a quotient that is not 1 but sits exactly as far
from the constant as 1 does -- rather than defaulting to a verdict.

``choice_consistency`` then applies the computed verdict to ALL FIVE choices of
each such item, together with the reason each choice gives, and requires exactly
the keyed one to survive. Three of the distractors in this module state the right
verdict for the wrong reason and two state the wrong verdict for the right
reason; a check that only read the key would pass all of them.

``concentration_cell_guard`` pins EK 9.10.A.3's last sentence, which is the other
statement in this topic whose opposite is equally sayable: electrons flow from
the DILUTE half-cell to the CONCENTRATED one, because that is the direction that
equalises the two.

``nernst_direction_guard`` pins EK 9.10.A.4's qualitative use: the equation
SUBTRACTS a term in the logarithm of the quotient, so the potential moves
opposite to the quotient. The direction of the quotient's change is declared per
item from the stem, and the key's two clauses must both agree with it.

SCOPE. 9.9 owns the standard potential and its arithmetic, 9.11 owns Faraday's
law. Neither a free energy change nor a current, charge or mass appears.

NEGATIVE CONTROL: ``python3 verify_h9_10.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h
import h9_check as h9

import h9_10

XCOL = "[X2+] (M)"
YCOL = "[Y2+] (M)"
ACOL = "Concentration in half-cell A (M)"
BCOL = "Concentration in half-cell B (M)"

# Explicit lookarounds, never \b: a digit and a letter are both word characters.
_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"shown here|the graph|graph above|graph below|the cell shown|illustrated)"
    r"(?![a-z])", re.I)

# EK 9.10.A.4's fence: no item may state a nonstandard potential as a number.
_NUMERIC_VOLTAGE = re.compile(r"(?<![A-Za-z])[+-]?\d+(?:\.\d+)?\s*(?:V|volts?)(?![A-Za-z])",
                              re.I)
# 9.11's material. "second" is deliberately absent -- an earlier draft of the
# sibling verifier banned it and the ban fired on the ordinal in "the first less
# the second", the same family as this project's \bpi own-goal.
_OUT_OF_SCOPE = re.compile(
    r"(?<![A-Za-z])(amperes?|coulombs?|electroplating|faraday's law|"
    r"free energy)(?![A-Za-z])", re.I)


# ------------------------------------------------------- EK 9.10.A.3's four cases

def quotient_verdict(q, k):
    """Which of EK 9.10.A.3's cases a reaction quotient falls into, given K.

    The distance from equilibrium is measured on the logarithmic scale the
    Nernst relationship uses, so "further from equilibrium than a quotient of 1"
    is a comparison of |log Q - log K| against |log 1 - log K|.

    Returns "zero" at equilibrium, "standard" at a quotient of 1, "greater"
    where the magnitude exceeds the standard one and "smaller" where it falls
    below it.
    """
    assert q > 0 and k > 0, f"a reaction quotient and a constant must be positive: {q}, {k}"
    here = abs(math.log10(q) - math.log10(k))
    at_standard = abs(math.log10(k))
    if here < 1e-12:
        return "zero"
    if abs(here - at_standard) < 1e-12:
        # A quotient of 1 IS the standard point. Anything else equidistant from
        # the constant would give the standard magnitude with the opposite sign,
        # a case EK 9.10.A.3 does not settle -- so it fails rather than defaults.
        assert abs(q - 1.0) < 1e-12, (
            f"a quotient of {q:g} sits exactly as far from a constant of {k:g} as 1 does "
            f"without being 1; the framework does not settle that case"
        )
        return "standard"
    return "greater" if here > at_standard else "smaller"


# What a choice ASSERTS. Each pattern is specific enough that no choice in this
# module matches two of them; the reader returns None rather than guessing when
# one does, which is what stops a silent default.
_VERDICT_PATTERNS = {
    "standard": re.compile(r"equals the standard cell potential", re.I),
    "zero": re.compile(r"already equals the equilibrium constant", re.I),
    "greater": re.compile(r"(?<![a-z])greater(?![a-z])", re.I),
    "smaller": re.compile(r"(?<![a-z])smaller(?![a-z])", re.I),
}
_REASON_PATTERNS = {
    "farther": re.compile(r"(?<![a-z])(?:farther|further)(?![a-z])", re.I),
    "closer": re.compile(r"(?<![a-z])(?:closer|nearer)(?![a-z])", re.I),
}
# EK 9.10.A.3: further from equilibrium means a larger magnitude.
_REASON_FOR = {"greater": "farther", "smaller": "closer"}


def _single(patterns, text):
    found = {name for name, pat in patterns.items() if pat.search(text)}
    return found.pop() if len(found) == 1 else None


def stated_verdict(text):
    return _single(_VERDICT_PATTERNS, text)


def stated_reason(text):
    return _single(_REASON_PATTERNS, text)


def _survivors(item, verdict):
    """The choices consistent with ``verdict`` AND with EK 9.10.A.3's reason for it."""
    out = []
    for k, choice in enumerate(item["choices"]):
        said = stated_verdict(choice)
        if said is None or said != verdict:
            continue
        reason = stated_reason(choice)
        if reason is not None and _REASON_FOR.get(verdict) not in (None, reason):
            continue
        out.append(k)
    return out


# ------------------------------------------------------------- stem arithmetic

_K = re.compile(r"equilibrium constant (?:of|is) (\d+(?:\.\d+)?)")
_X = re.compile(r"(\d+(?:\.\d+)?) M X2\+")
_Y = re.compile(r"(\d+(?:\.\d+)?) M Y2\+")
_Q_STATED = re.compile(r"reaction quotient of (\d+(?:\.\d+)?)")


def _only(pattern, text, what):
    hits = pattern.findall(text)
    assert len(hits) == 1, f"expected exactly one {what} in the stem, found {hits}"
    return float(hits[0])


def _q_and_k(stem):
    """The reaction quotient and the constant, read out of the stem.

    For X(s) + Y2+(aq) gives X2+(aq) + Y(s) the quotient is the product ion over
    the reactant ion; the solids do not appear in it.
    """
    k = _only(_K, stem, "equilibrium constant")
    if _X.search(stem):
        q = _only(_X, stem, "product ion concentration") / _only(
            _Y, stem, "reactant ion concentration")
    else:
        q = _only(_Q_STATED, stem, "reaction quotient")
    return q, k


def quotient_item(item):
    """Recompute the quotient, decide EK 9.10.A.3's case, and gate every choice."""
    q, k = _q_and_k(item["q"])
    verdict = quotient_verdict(q, k)
    survivors = _survivors(item, verdict)
    assert survivors == [item["ans"]], (
        f"a quotient of {q:g} against a constant of {k:g} is EK 9.10.A.3's {verdict!r} "
        f"case, which admits choices {survivors}, but the key is {item['ans']}"
    )
    return (f"the stem's concentrations give a reaction quotient of {q:g} against a "
            f"constant of {k:g}, which is EK 9.10.A.3's {verdict} case")


NUMERIC = {12: quotient_item, 13: quotient_item, 14: quotient_item, 15: quotient_item,
           29: quotient_item}


# ------------------------------------------------------------------ table items

def _trial_verdicts(table, k):
    return {lab: quotient_verdict(x / y, k)
            for lab, x, y in zip(cg.labels(table), cg.col(table, XCOL), cg.col(table, YCOL))}


def _unique(verdicts, wanted):
    hits = sorted(lab for lab, v in verdicts.items() if v == wanted)
    assert len(hits) == 1, f"exactly one tabulated row must be the {wanted!r} case: {hits}"
    return hits[0]


def q16(table, item):
    k = _only(_K, item["q"], "equilibrium constant")
    verdicts = _trial_verdicts(table, k)
    lab = _unique(verdicts, "standard")
    assert lab == "Trial 1", f"the tabulated standard-condition row is {lab}"
    h.shows(item, lab)
    return (f"dividing the two tabulated columns row by row against a constant of {k:g} "
            f"classifies the trials as {verdicts}")


def q17(table, item):
    k = _only(_K, item["q"], "equilibrium constant")
    verdicts = _trial_verdicts(table, k)
    lab = _unique(verdicts, "zero")
    assert lab == "Trial 4", f"the tabulated equilibrium row is {lab}"
    h.shows(item, lab)
    return (f"exactly one tabulated ratio equals the stated constant {k:g}, which EK "
            f"9.10.A.3 puts at a potential of zero: {verdicts}")


def q18(table, item):
    k = _only(_K, item["q"], "equilibrium constant")
    distance = {lab: abs(math.log10(x / y) - math.log10(k))
                for lab, x, y in zip(cg.labels(table), cg.col(table, XCOL),
                                     cg.col(table, YCOL))}
    farthest = max(distance, key=distance.get)
    ties = [lab for lab, d in distance.items() if abs(d - distance[farthest]) < 1e-12]
    assert ties == [farthest], f"the farthest tabulated row is not unique: {ties}"
    assert farthest == "Trial 2", f"the farthest tabulated row is {farthest}"
    h.shows(item, farthest)
    return (f"the tabulated distances from equilibrium are {distance}, whose unique maximum "
            f"is at {farthest}, and EK 9.10.A.1 makes that the largest magnitude")


def q19(table, item):
    k = _only(_K, item["q"], "equilibrium constant")
    verdicts = _trial_verdicts(table, k)
    lab = _unique(verdicts, "smaller")
    assert lab == "Trial 3", f"the tabulated closer-to-equilibrium row is {lab}"
    h.shows(item, lab)
    return (f"exactly one tabulated ratio lies between 1 and the constant {k:g} without "
            f"reaching it: {verdicts}")


def _conc_gaps(table):
    return {lab: abs(math.log10(a / b))
            for lab, a, b in zip(cg.labels(table), cg.col(table, ACOL), cg.col(table, BCOL))}


def q24(table, item):
    gaps = _conc_gaps(table)
    widest = max(gaps, key=gaps.get)
    ties = [lab for lab, g in gaps.items() if abs(g - gaps[widest]) < 1e-12]
    assert ties == [widest], f"the widest tabulated gap is not unique: {ties}"
    assert widest == "Cell 2", f"the widest tabulated concentration gap is at {widest}"
    h.shows(item, widest)
    return (f"a concentration cell reaches equilibrium at equal concentrations, and the "
            f"tabulated separations are {gaps}, whose unique maximum is at {widest}")


def q25(table, item):
    gaps = _conc_gaps(table)
    level = sorted(lab for lab, g in gaps.items() if g < 1e-12)
    assert level == ["Cell 3"], f"the tabulated rows already at equilibrium are {level}"
    h.shows(item, level[0])
    return (f"exactly one tabulated row has its two concentrations equal, which for a "
            f"concentration cell is equilibrium: {gaps}")


TABLE_CHECKS = {16: q16, 17: q17, 18: q18, 19: q19, 24: q24, 25: q25}


# -------------------------------------------------- EK 9.10.A.3's last sentence

_DILUTE_TO_CONC = re.compile(
    r"from the more dilute half-cell to the more concentrated", re.I)
_CONC_TO_DILUTE = re.compile(
    r"from the more concentrated half-cell to the more dilute", re.I)
_CONVERGE = re.compile(
    r"dilute solution grows more concentrated and the concentrated one grows more dilute",
    re.I)
_DIVERGE = re.compile(
    r"dilute solution grows more dilute and the concentrated one grows more concentrated",
    re.I)

FLOW_ITEM = 21
CONVERGE_ITEM = 22


def concentration_cell_guard(module, flow=FLOW_ITEM, converge=CONVERGE_ITEM):
    """Equilibrium for two identical half-cells is EQUAL concentrations.

    So the spontaneous direction, which EK 9.10.A.3 says is the direction needed
    to reach equilibrium, raises the dilute concentration and lowers the
    concentrated one. That puts the oxidation in the dilute half-cell, and EK
    9.8.A.3 sends the electrons away from it.
    """
    key = h.keyed(module.QUESTIONS[flow - 1])
    assert _DILUTE_TO_CONC.search(key), (
        f"{module.TOPIC[0]} q{flow}: the key does not send the electrons from the dilute "
        f"half-cell to the concentrated one -- {key!r}"
    )
    assert not _CONC_TO_DILUTE.search(key), (
        f"{module.TOPIC[0]} q{flow}: the key sends the electrons the other way as well -- "
        f"{key!r}"
    )
    key = h.keyed(module.QUESTIONS[converge - 1])
    assert _CONVERGE.search(key), (
        f"{module.TOPIC[0]} q{converge}: the key does not bring the two concentrations "
        f"together, which is the approach to equilibrium EK 9.10.A.3 describes -- {key!r}"
    )
    assert not _DIVERGE.search(key), (
        f"{module.TOPIC[0]} q{converge}: the key also drives the two concentrations apart "
        f"-- {key!r}"
    )
    print(f"OK  {module.TOPIC[0]} concentration cell: electrons run dilute to concentrated "
          "and the two concentrations converge, which is the direction that reaches "
          "equilibrium.")


# ---------------------------------------------- EK 9.10.A.4 used qualitatively

_E_MOVES = re.compile(r"^It (rises|falls)(?![a-z])", re.I)
_Q_MOVES = re.compile(r"reaction quotient (rises|falls)(?![a-z])", re.I)

# The direction the stem moves the reaction quotient. Declared, not read off the
# key, so the key has something to be checked against.
NERNST_ITEMS = {27: "rises", 28: "falls"}
_OPPOSITE = {"rises": "falls", "falls": "rises"}


def nernst_direction_guard(module, items=None):
    items = NERNST_ITEMS if items is None else items
    for i, q_moves in sorted(items.items()):
        key = h.keyed(module.QUESTIONS[i - 1])
        e_hit = _E_MOVES.search(key)
        assert e_hit, f"{module.TOPIC[0]} q{i}: the key does not open with a direction for " \
                      f"the potential -- {key!r}"
        q_hit = _Q_MOVES.search(key)
        assert q_hit, f"{module.TOPIC[0]} q{i}: the key does not say which way the reaction " \
                      f"quotient moves -- {key!r}"
        assert q_hit.group(1).lower() == q_moves, (
            f"{module.TOPIC[0]} q{i}: the stem moves the reaction quotient {q_moves} but the "
            f"key says it {q_hit.group(1).lower()} -- {key!r}"
        )
        # EK 9.10.A.4's equation SUBTRACTS the term in the logarithm of Q, so the
        # potential must move the other way. Named booleans, not two tuples read
        # by index.
        potential_moves = e_hit.group(1).lower()
        want = _OPPOSITE[q_moves]
        assert potential_moves == want, (
            f"{module.TOPIC[0]} q{i}: the reaction quotient {q_moves} and the key has the "
            f"potential {potential_moves} too, but the framework's equation subtracts the "
            f"logarithm term, so the potential {want} -- {key!r}"
        )
    print(f"OK  {module.TOPIC[0]} Nernst direction: {len(items)} key(s) moving the potential "
          "opposite to the reaction quotient, as the subtracted term requires.")


def no_figure_language(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _FIGURE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: refers to {hit.group(0)!r}, which this bank "
                f"cannot show -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} figures: no item points at a picture.")


def no_algorithmic_nernst(module):
    """EK 9.10.A.4's fence, gated rather than trusted."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in h9.facing(item):
            hit = _NUMERIC_VOLTAGE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: states the potential {hit.group(0)!r} as a number, "
                f"which is the algorithmic Nernst calculation EK 9.10.A.4 calls insufficient "
                f"-- {text[:70]!r}"
            )
            hit = _OUT_OF_SCOPE.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: mentions {hit.group(0)!r}, which belongs to 9.9 or "
                f"9.11 -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} fence: no numeric voltage anywhere, so nothing here is the "
          "algorithmic Nernst calculation EK 9.10.A.4 rules out.")


CLAIMS = [
 ("The concentrations of the active species",
  "EK 9.10.A.1: in a real system under nonstandard conditions the cell potential will vary depending on the concentrations of the active species."),
 ("A driving force toward equilibrium",
  "EK 9.10.A.1 calls the cell potential a driving force toward equilibrium, which is why its magnitude grows with the distance from equilibrium."),
 ("The farther the reaction is from equilibrium, the greater the magnitude",
  "EK 9.10.A.1 verbatim in substance, with EK 9.10.A.3 putting the magnitude at zero once equilibrium is reached."),
 ("do not apply, because such systems are not in equilibrium",
  "EK 9.10.A.2: equilibrium arguments such as Le Chatelier's principle do not apply to electrochemical systems, because the systems are not in equilibrium."),
 ("A reaction quotient of 1",
  "EK 9.10.A.3 opens by saying the standard cell potential corresponds to the standard conditions of a reaction quotient of 1."),
 ("It decreases, reaching zero at equilibrium",
  "EK 9.10.A.3: as the system approaches equilibrium the magnitude of the cell potential decreases, reaching zero at equilibrium."),
 ("It equals the equilibrium constant, so the system is at equilibrium",
  "EK 9.10.A.3 puts the potential at zero when the reaction quotient equals the equilibrium constant; a quotient of 1 is the standard point instead."),
 ("Its magnitude increases relative to the standard value",
  "EK 9.10.A.3: deviations taking the cell further from equilibrium than a reaction quotient of 1 increase the magnitude relative to the standard value."),
 ("Its magnitude decreases relative to the standard value",
  "EK 9.10.A.3's other clause: deviations taking the cell closer to equilibrium than a reaction quotient of 1 decrease the magnitude."),
 ("insufficient to demonstrate an understanding of cells under nonstandard conditions",
  "EK 9.10.A.4 says algorithmic calculations using the Nernst equation are insufficient, and asks for qualitative understanding and conceptual reasoning instead."),
 ("E = E^\\circ - \\frac{RT}{nF} \\ln Q",
  "EK 9.10.A.4's EQN, with the logarithm of the reaction quotient SUBTRACTED from the standard potential, which is what makes the potential fall as the quotient rises."),
 ("equals the standard cell potential, because the reaction quotient is 1",
  "EK 9.10.A.3 attaches the standard potential to a quotient of 1. quotient_item recomputes the quotient from the stem and gates all five choices with it."),
 ("greater in magnitude, because the deviation takes the cell farther from equilibrium",
  "EK 9.10.A.3's further-from-equilibrium clause with EK 9.10.A.1's reason. quotient_item recomputes the quotient and its distance from the stated constant."),
 ("smaller in magnitude, because the deviation takes the cell closer to equilibrium",
  "EK 9.10.A.3's closer-to-equilibrium clause. quotient_item recomputes the distance and rejects any choice giving this verdict the other reason."),
 ("Zero, because the reaction quotient already equals the equilibrium constant",
  "EK 9.10.A.3 puts the magnitude at zero at equilibrium. quotient_item recomputes the quotient from the stem and finds it equal to the stated constant."),
 ("Trial 1",
  "EK 9.10.A.3's standard point. q16 divides the two tabulated columns row by row and checks exactly one ratio is 1."),
 ("Trial 4",
  "EK 9.10.A.3's equilibrium point. q17 checks exactly one tabulated ratio equals the constant stated in the stem."),
 ("Trial 2",
  "EK 9.10.A.1 makes the magnitude grow with the distance from equilibrium. q18 recomputes every tabulated distance and checks the maximum is unique."),
 ("Trial 3",
  "EK 9.10.A.3's closer-to-equilibrium clause. q19 checks exactly one tabulated ratio lies between 1 and the constant without reaching it."),
 ("Zero, because the two half-reactions are the same and the standard condition makes the concentrations equal",
  "EK 9.10.A.3 ties the standard condition to a reaction quotient of 1, which for two identical half-cells means equal concentrations and so nothing to drive the cell."),
 ("From the more dilute half-cell to the more concentrated one",
  "EK 9.10.A.3: in concentration cells the direction of spontaneous electron flow is the direction needed to reach equilibrium, which here means equalising the two concentrations."),
 ("dilute solution grows more concentrated and the concentrated one grows more dilute",
  "The same statement read as the cell runs: reaching equilibrium means the two concentrations approach each other, which is EK 9.10.A.1's approach to equilibrium."),
 ("When the two concentrations have become equal",
  "Equilibrium for two identical half-cells is equal concentrations, and EK 9.10.A.3 puts the magnitude of the potential at zero once equilibrium is reached."),
 ("Cell 2",
  "EK 9.10.A.1 makes the magnitude grow with the distance from equilibrium. q24 recomputes each tabulated separation and checks the widest is unique."),
 ("Cell 3",
  "A concentration cell is at equilibrium when its two concentrations are equal. q25 checks exactly one tabulated row is already there."),
 ("does not apply here, because an operating cell is not at equilibrium",
  "EK 9.10.A.2 states exactly this, and EK 9.10.A.4 names the reasoning the framework wants in its place."),
 ("It falls, because the reaction quotient rises and the equation subtracts a term",
  "EK 9.10.A.4's equation subtracts a term proportional to the logarithm of the quotient, so adding product raises the quotient and lowers the potential."),
 ("It rises, because the reaction quotient falls and a smaller term is subtracted",
  "The same equation read the other way, and the same conclusion EK 9.10.A.1 gives from the cell having been moved farther from equilibrium."),
 ("greater, because a quotient of 100 is farther from the constant than a quotient of 1 is",
  "EK 9.10.A.3's comparison is made against the equilibrium constant, not against 1. quotient_item recomputes both distances from the numbers in the stem."),
 ("At a quotient of 1 the potential is the standard one, at the equilibrium constant it is zero, and farther from the constant than 1 is the magnitude is larger",
  "EK 9.10.A.3 states all three in one passage; any summary that exchanges the first two, or reverses the third, contradicts it."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the diagram, what does the cell potential vary with?"
        no_figure_language(mod)

    def numeric_voltage_creeps_in(mod, cl):
        ch = list(mod.QUESTIONS[11]["choices"])
        ch[4] = "It works out as 1.07 V once the concentrations are substituted"
        mod.QUESTIONS[11]["choices"] = ch
        no_algorithmic_nernst(mod)

    def free_energy_creeps_in(mod, cl):
        mod.QUESTIONS[0]["why"] = (mod.QUESTIONS[0]["why"]
                                   + " The free energy change follows from it.")
        no_algorithmic_nernst(mod)

    def stem_concentrations_swapped(mod, cl):
        # q13's key says the deviation takes the cell FARTHER from equilibrium.
        # Exchanging the two stated concentrations turns a quotient of 0.010
        # into one of 100, which is the equilibrium point for this constant.
        mod.QUESTIONS[12]["q"] = mod.QUESTIONS[12]["q"].replace(
            "0.010 M X2+ and 1.0 M Y2+", "1.0 M X2+ and 0.010 M Y2+")

    def stem_constant_changed(mod, cl):
        # q14's key says CLOSER to equilibrium. With a constant of 1 instead of
        # 100, a quotient of 10 is further from equilibrium than 1 is.
        mod.QUESTIONS[13]["q"] = mod.QUESTIONS[13]["q"].replace(
            "equilibrium constant of 100", "equilibrium constant of 1.0")

    def key_moved_to_the_right_verdict_wrong_reason(mod, cl):
        # q13's third choice states the keyed verdict with the OTHER reason. It
        # is the choice the framework rules out, and only the reason test sees it.
        mod.QUESTIONS[12]["ans"] = 2
        cl[12] = ("greater in magnitude, because the deviation takes the cell closer",
                  cl[12][1])

    def ambiguous_quotient(mod, cl):
        # A quotient of 10000 against a constant of 100 sits exactly as far from
        # equilibrium as 1 does, on the other side. quotient_verdict must refuse
        # it rather than call it the standard case.
        mod.QUESTIONS[11]["q"] = mod.QUESTIONS[11]["q"].replace(
            "0.50 M X2+ and 0.50 M Y2+", "1.0 M X2+ and 0.00010 M Y2+")

    def tabulated_standard_row_moved(mod, cl):
        mod.QUESTIONS[15]["table"] = dict(
            headers=h9_10._T_TRIALS["headers"],
            rows=[["Trial 1", "0.50", "0.050"], ["Trial 2", "0.010", "1.0"],
                  ["Trial 3", "1.0", "0.10"], ["Trial 4", "1.0", "0.010"]])

    def tabulated_equilibrium_row_moved(mod, cl):
        mod.QUESTIONS[16]["table"] = dict(
            headers=h9_10._T_TRIALS["headers"],
            rows=[["Trial 1", "0.50", "0.50"], ["Trial 2", "0.010", "1.0"],
                  ["Trial 3", "1.0", "0.10"], ["Trial 4", "1.0", "0.10"]])

    def tabulated_farthest_row_moved(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h9_10._T_TRIALS["headers"],
            rows=[["Trial 1", "0.50", "0.50"], ["Trial 2", "0.10", "1.0"],
                  ["Trial 3", "0.000010", "1.0"], ["Trial 4", "1.0", "0.010"]])

    def tabulated_closer_row_duplicated(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h9_10._T_TRIALS["headers"],
            rows=[["Trial 1", "0.50", "0.50"], ["Trial 2", "0.010", "1.0"],
                  ["Trial 3", "1.0", "0.10"], ["Trial 4", "1.0", "0.20"]])

    def widest_concentration_gap_moved(mod, cl):
        mod.QUESTIONS[23]["table"] = dict(
            headers=h9_10._T_CONC["headers"],
            rows=[["Cell 1", "0.000010", "1.0"], ["Cell 2", "0.0010", "1.0"],
                  ["Cell 3", "0.50", "0.50"]])

    def no_concentration_cell_at_equilibrium(mod, cl):
        mod.QUESTIONS[24]["table"] = dict(
            headers=h9_10._T_CONC["headers"],
            rows=[["Cell 1", "0.10", "1.0"], ["Cell 2", "0.0010", "1.0"],
                  ["Cell 3", "0.50", "0.20"]])

    def electron_flow_reversed(mod, cl):
        ch = list(mod.QUESTIONS[20]["choices"])
        ch[0] = "From the more concentrated half-cell to the more dilute one"
        ch[1] = "From the more dilute half-cell to the more concentrated half-cell"
        mod.QUESTIONS[20]["choices"] = ch
        concentration_cell_guard(mod)

    def concentrations_made_to_diverge(mod, cl):
        ch = list(mod.QUESTIONS[21]["choices"])
        ch[0] = ("The dilute solution grows more dilute and the concentrated one grows more "
                 "concentrated")
        ch[1] = ("The dilute solution grows more concentrated and the concentrated one "
                 "grows more dilute as well")
        mod.QUESTIONS[21]["choices"] = ch
        concentration_cell_guard(mod)

    def nernst_direction_reversed(mod, cl):
        ch = list(mod.QUESTIONS[26]["choices"])
        ch[0] = ("It rises, because the reaction quotient rises and the equation subtracts a "
                 "term proportional to its logarithm")
        ch[1] = ("It falls, because the reaction quotient rises and the equation adds a term "
                 "proportional to its logarithm")
        mod.QUESTIONS[26]["choices"] = ch
        nernst_direction_guard(mod)

    def nernst_stem_direction_changed(mod, cl):
        items = dict(NERNST_ITEMS)
        items[27] = "falls"
        nernst_direction_guard(mod, items=items)

    return [
        ("a stem pointing at a diagram the bank cannot show", figure_language),
        ("a choice stating a potential in volts, the calculation EK 9.10.A.4 bars",
         numeric_voltage_creeps_in),
        ("a free energy change, which is 9.9's material", free_energy_creeps_in),
        ("the stem's two concentrations exchanged under an unchanged key",
         stem_concentrations_swapped),
        ("the stem's equilibrium constant changed under an unchanged key",
         stem_constant_changed),
        ("the key moved to the choice giving the right verdict for the wrong reason",
         key_moved_to_the_right_verdict_wrong_reason),
        ("a quotient equidistant from the constant, which the framework does not settle",
         ambiguous_quotient),
        ("the tabulated standard-condition row moved", tabulated_standard_row_moved),
        ("the tabulated equilibrium row moved", tabulated_equilibrium_row_moved),
        ("the tabulated farthest row moved", tabulated_farthest_row_moved),
        ("a second tabulated row made closer to equilibrium than the standard point",
         tabulated_closer_row_duplicated),
        ("the widest tabulated concentration gap moved", widest_concentration_gap_moved),
        ("no tabulated concentration cell left at equilibrium",
         no_concentration_cell_at_equilibrium),
        ("the concentration cell's electron flow reversed", electron_flow_reversed),
        ("the concentration cell's two concentrations made to diverge",
         concentrations_made_to_diverge),
        ("the qualitative Nernst direction reversed", nernst_direction_reversed),
        ("the stem's direction of change declared the other way",
         nernst_stem_direction_changed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h9_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h9_10)
no_algorithmic_nernst(h9_10)
concentration_cell_guard(h9_10)
nernst_direction_guard(h9_10)
h.run(h9_10, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
