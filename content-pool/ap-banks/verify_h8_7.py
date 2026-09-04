"""Key audit for AP CHEMISTRY 8.7 pH and pKa.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.7.A.1  the protonation state follows from comparing solution pH with acid
           pKa: pH below pKa leaves the acid form dominant, pH above it leaves
           the base form dominant
                       1, 2, 3, 5, 6, 8, 16, 17, 18, 19, 20, 28, 30
  8.7.A.2  an indicator's property, such as colour, differs between its
           protonated and deprotonated states     9, 10, 14, 15, 25, 26, 27
  8.7.A.3  select an indicator whose pKa is close to the equivalence pH
                       11, 12, 13, 21, 22, 23, 24, 29
  8.5.A.3  pH equals pKa exactly where the pair is equal        4, 7

SCOPE. h8_5.py contains no indicator item and its verifier asserts that, because
EK 8.7.A.3 belongs here. In the other direction, h8_4.py's header records that
8.9 owns the Henderson-Hasselbalch arithmetic, so ``no_buffer_arithmetic``
asserts that no item here takes a logarithm, names that equation, or is handed a
pair of concentrations to work from.

THE ERROR THIS MODULE EXISTS TO PREVENT. ``seven_is_not_the_comparison`` asserts
that the tabulated acids include at least one row where comparing the pH with 7
gives the OPPOSITE answer to comparing it with the pKa. Without such a row the
module could be answered correctly by the wrong rule, and would teach it.

ARITHMETIC. Every pH-against-pKa comparison and every closest-pKa selection is
recomputed from the table or the stem alone.

NEGATIVE CONTROL: ``python3 verify_h8_7.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h8_7

PKA = "pKa of the acid"
PH = "pH of the solution it is dissolved in"
IPKA = "pKa of the indicator"
CPROT = "Colour of the protonated form"
CDEP = "Colour of the deprotonated form"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|titration curve)(?![a-z])", re.I)

# 8.9 owns the arithmetic. A logarithm, the equation by name, or a stem carrying
# two molar concentrations would all be that topic's work.
_HH = re.compile(
    r"\\log|(?<![a-z])logarithm(?![a-z])|(?<![a-z])henderson(?![a-z])", re.I)
_MOLAR = re.compile(r"(?<![A-Za-z0-9])\d+(?:\.\d+)?\s*M(?![A-Za-z])")


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
    print(f"OK  {module.TOPIC[0]} figures: no item points at a curve or a picture; every "
          "equivalence pH is supplied in words.")


def no_buffer_arithmetic(module):
    """8.9 owns the Henderson-Hasselbalch arithmetic; this topic is qualitative."""
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _HH.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is 8.9's material "
                f"-- {text[:70]!r}"
            )
        molars = _MOLAR.findall(item["q"])
        assert len(molars) < 2, (
            f"{module.TOPIC[0]} q{i}: the stem states {len(molars)} concentrations "
            f"({molars}), which is the setup 8.9 owns rather than a pH-against-pKa "
            "comparison"
        )
    print(f"OK  {module.TOPIC[0]} scope: no logarithm, no named buffer equation and no "
          "item handed a pair of concentrations.")


def seven_is_not_the_comparison(module):
    """EK 8.7.A.1 compares pH with pKa, and the data must make that visible.

    A module whose every tabulated row happened to agree with the pH-against-7
    rule could be answered correctly by that wrong rule, and would teach it. So
    at least one row must be a case where the two rules DISAGREE.
    """
    disagreeing = []
    for i, item in enumerate(module.QUESTIONS, 1):
        t = item.get("table")
        if not t or cg.normalize(PKA) not in [cg.normalize(x) for x in t["headers"]]:
            continue
        for lab, pka, ph in zip(cg.labels(t), cg.col(t, PKA), cg.col(t, PH)):
            by_pka = "base" if ph > pka else ("acid" if ph < pka else "equal")
            by_seven = "base" if ph > 7.0 else ("acid" if ph < 7.0 else "equal")
            if by_pka != by_seven and by_pka != "equal":
                disagreeing.append((i, lab, pka, ph, by_pka, by_seven))
    assert disagreeing, (
        f"{module.TOPIC[0]}: no tabulated acid distinguishes the pH-against-pKa rule from "
        "the pH-against-7 rule, so the module could be answered by the wrong one"
    )
    print(f"OK  {module.TOPIC[0]} misconception: {len(disagreeing)} tabulated row(s) where "
          "comparing the pH with 7 gives the opposite answer to comparing it with the pKa.")


# ------------------------------------------------------------------ helpers

def margin(table, label):
    """Solution pH minus acid pKa: positive means the base form predominates."""
    return cg.cell(table, label, PH) - cg.cell(table, label, PKA)


def closest(table, target):
    """The tabulated indicator whose pKa is nearest ``target``."""
    gaps = {lab: abs(cg.cell(table, lab, IPKA) - target) for lab in cg.labels(table)}
    best = min(gaps, key=gaps.get)
    assert len([g for g in gaps.values() if abs(g - gaps[best]) < 1e-12]) == 1, \
        f"the closest indicator is not unique: {gaps}"
    return best, gaps


def colour(table, label, ph):
    """Which tabulated colour EK 8.7.A.1 and EK 8.7.A.2 give at this pH."""
    pka = cg.cell(table, label, IPKA)
    assert abs(ph - pka) > 0.5, (
        f"the stated pH {ph} is too close to the tabulated pKa {pka} for one form to "
        "predominate cleanly"
    )
    j = [cg.normalize(x) for x in table["headers"]].index(
        cg.normalize(CPROT if ph < pka else CDEP))
    i = cg.labels(table).index(label)
    return str(table["rows"][i][j]), ("protonated" if ph < pka else "deprotonated")


# ------------------------------------------------------------------ table items

def q5(table, item):
    ms = {lab: margin(table, lab) for lab in cg.labels(table)}
    positive = {lab: m for lab, m in ms.items() if m > 0}
    assert len(positive) >= 2, (
        f"at least two rows must have the base form predominant, or 'largest margin' asks "
        f"nothing: {ms}"
    )
    biggest = max(positive, key=positive.get)
    assert biggest == "HJ", f"the largest positive margin is at {biggest}: {ms}"
    assert len([m for m in positive.values() if abs(m - positive[biggest]) < 1e-12]) == 1, \
        "the largest positive margin must be unique"
    h.shows(item, "Acid HJ")
    return f"the tabulated pH-minus-pKa margins are {ms}, whose largest positive value is {biggest}"


def q6(table, item):
    acidic = [lab for lab in cg.labels(table) if margin(table, lab) < 0]
    assert acidic == ["HL"], f"the rows with pH below pKa are {acidic}"
    h.shows(item, "Acid HL")
    return f"exactly one tabulated row has its pH below its own pKa: {acidic[0]}"


def q7(table, item):
    equal = [lab for lab in cg.labels(table) if abs(margin(table, lab)) < 1e-12]
    assert equal == ["HM"], f"the rows with pH equal to pKa are {equal}"
    h.shows(item, "Acid HM")
    return f"exactly one tabulated row has its pH equal to its own pKa: {equal[0]}"


def q8(table, item):
    hits = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, PH) < 7.0 and margin(table, lab) > 0]
    assert hits == ["HN"], f"the acidic-but-deprotonated rows are {hits}"
    h.shows(item, "Acid HN")
    return (f"exactly one tabulated row sits below pH 7 and above its own pKa: {hits[0]}, "
            f"with a margin of {margin(table, hits[0]):g}")


def q12(table, item):
    best, gaps = closest(table, 9.0)
    assert best == "Y", f"the closest indicator to pH 9.0 is {best}: {gaps}"
    h.shows(item, "Indicator Y")
    return f"the tabulated pKa values sit {gaps} from the stated equivalence pH of 9.0"


def q13(table, item):
    best, gaps = closest(table, 5.2)
    assert best == "X", f"the closest indicator to pH 5.2 is {best}: {gaps}"
    assert gaps[best] > 0, (
        "the closest indicator must not match the equivalence pH exactly, since one "
        "distractor turns on the framework asking only for CLOSE"
    )
    h.shows(item, "Indicator X")
    return f"the tabulated pKa values sit {gaps} from the stated equivalence pH of 5.2"


def q14(table, item):
    col, state = colour(table, "X", 2.0)
    assert state == "protonated", f"at pH 2.0 indicator X is {state}"
    assert col, "the tabulated protonated colour must be present"
    h.shows(item, "protonated colour, because the solution pH is below its pKa")
    return (f"pH 2.0 sits below indicator X's tabulated pKa of "
            f"{cg.cell(table, 'X', IPKA):g}, giving its {state} colour, {col}")


def q15(table, item):
    col, state = colour(table, "W", 6.0)
    assert state == "deprotonated", f"at pH 6.0 indicator W is {state}"
    assert cg.normalize(col) == "yellow", f"the tabulated deprotonated colour is {col}"
    h.shows(item, "Yellow, because the solution pH is above its pKa and the deprotonated form")
    return (f"pH 6.0 sits above indicator W's tabulated pKa of "
            f"{cg.cell(table, 'W', IPKA):g}, giving its tabulated {state} colour, {col}")


def q24(table, item):
    gaps = {lab: abs(cg.cell(table, lab, IPKA) - 3.5) for lab in cg.labels(table)}
    worst = max(gaps, key=gaps.get)
    assert worst == "Z", f"the furthest indicator from pH 3.5 is {worst}: {gaps}"
    assert len([g for g in gaps.values() if abs(g - gaps[worst]) < 1e-12]) == 1, \
        "the furthest indicator must be unique"
    h.shows(item, "Indicator Z")
    return f"the tabulated pKa values sit {gaps} from the stated equivalence pH of 3.5"


def q27(table, item):
    col, state = colour(table, "Z", 12.0)
    assert state == "deprotonated", f"at pH 12.0 indicator Z is {state}"
    assert cg.normalize(col) == "green", f"the tabulated deprotonated colour is {col}"
    h.shows(item, "Green, because the pH is above its pKa so the deprotonated form")
    return (f"pH 12.0 sits above indicator Z's tabulated pKa of "
            f"{cg.cell(table, 'Z', IPKA):g}, giving its tabulated {state} colour, {col}")


TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 12: q12, 13: q13, 14: q14, 15: q15,
                24: q24, 27: q27}


# ---------------------------------------------------------------- stem numerics

def n16(item):
    pka, ph = 5.0, 3.0
    assert ph < pka, "the stem's pH must sit below its pKa"
    assert ph < 7.0, "the solution is also acidic, which is the distractor's wrong reason"
    h.shows(item, "protonated form, because the pH is below the pKa")
    return f"the stated pH {ph:g} sits below the stated pKa {pka:g}, so the acid form leads"


def n17(item):
    pka, ph = 4.0, 6.0
    assert ph > pka, "the stem's pH must sit above its pKa"
    assert ph < 7.0, (
        "the solution must still be acidic, or the item would not separate the "
        "pH-against-pKa rule from the pH-against-7 rule"
    )
    h.shows(item, "deprotonated form, because the pH is above the pKa")
    return (f"the stated pH {ph:g} is above the stated pKa {pka:g} while remaining below "
            "7, which is exactly where the two rules disagree")


def n18(item):
    ph, low, high = 6.0, 4.0, 8.0
    assert low < ph < high, "the solution pH must lie between the two stated pKa values"
    h.shows(item, "pKa of 4.0, since the solution pH is above it")
    return (f"the stated pH {ph:g} lies above {low:g} and below {high:g}, so the two acids "
            "fall on opposite sides of EK 8.7.A.1's comparison")


def n29(item):
    target, a, b = 7.0, 6.8, 9.0
    assert abs(a - target) < abs(b - target), "the first stated pKa must be the closer"
    assert abs(abs(a - target) - 0.2) < 1e-9, "the closer gap must recompute to 0.2"
    assert abs(abs(b - target) - 2.0) < 1e-9, "the further gap must recompute to 2.0"
    h.shows(item, "pKa of 6.8")
    return (f"the two stated pKa values sit {abs(a - target):g} and {abs(b - target):g} "
            f"from the stated equivalence pH of {target:g}")


NUMERIC = {16: n16, 17: n17, 18: n18, 29: n29}


CLAIMS = [
 ("relative concentrations of HA and A-",
  "EK 8.7.A.1, verbatim in substance: the protonation state, meaning the relative concentrations of HA and A-, is predicted by comparing solution pH with acid pKa."),
 ("The acid form",
  "EK 8.7.A.1: when solution pH is less than the acid pKa, the acid form has the higher concentration. The order of addition does not enter the statement."),
 ("The base form",
  "EK 8.7.A.1: when solution pH is greater than the acid pKa, the base form has the higher concentration."),
 ("conjugate pair are present in equal concentrations",
  "EK 8.5.A.3 puts equal concentrations of the pair exactly where pH equals pKa, the boundary between EK 8.7.A.1's two cases; it says nothing about the pH being 7.00."),
 ("Acid HJ",
  "EK 8.7.A.1's second clause across four tabulated rows. q5 recomputes every pH-minus-pKa margin, checks two rows are positive and that the largest is unique."),
 ("Acid HL",
  "EK 8.7.A.1's first clause. q6 recomputes the margins and checks exactly one tabulated row has its pH below its pKa."),
 ("Acid HM",
  "EK 8.5.A.3's equality case. q7 recomputes the margins and checks exactly one row has the two numbers identical."),
 ("Acid HN",
  "EK 8.7.A.1 compares pH with pKa, not with 7. q8 recomputes which tabulated row is below pH 7 and still above its own pKa, and checks it is unique."),
 ("differ between its protonated and deprotonated states",
  "EK 8.7.A.2, verbatim in substance: indicators exhibit different properties, such as colour, in their protonated versus deprotonated state."),
 ("pH fixes which of its two states predominates",
  "EK 8.7.A.2 attaches the colour to the state and EK 8.7.A.1 makes the pH relative to the pKa decide the state; the two statements together are the mechanism."),
 ("pKa is close to the pH at the equivalence point",
  "EK 8.7.A.3, verbatim in substance. A pKa fixed at seven would suit only titrations whose equivalence pH is seven."),
 ("Indicator Y",
  "EK 8.7.A.3 applied to four tabulated indicators. q12 recomputes every gap from the stated equivalence pH and checks the minimum is unique."),
 ("Indicator X",
  "EK 8.7.A.3 asks for CLOSE, not equal. q13 recomputes the gaps, checks the minimum is unique, and checks it is not zero."),
 ("protonated colour, because the solution pH is below its pKa",
  "EK 8.7.A.1 makes the acid form dominant below the pKa and EK 8.7.A.2 attaches the colour to that form. q14 recomputes which tabulated column applies."),
 ("Yellow, because the solution pH is above its pKa and the deprotonated form",
  "EK 8.7.A.1 and EK 8.7.A.2 together, read off the table. q15 recomputes the state and reads the tabulated colour for it."),
 ("protonated form, because the pH is below the pKa",
  "EK 8.7.A.1's first clause. n16 checks the stated pH is below the stated pKa and that the solution is also acidic, which is the distractor's wrong reason."),
 ("deprotonated form, because the pH is above the pKa",
  "EK 8.7.A.1's second clause in a solution that is nonetheless acidic; n17 checks both facts, which is what separates the right rule from the wrong one."),
 ("pKa of 4.0, since the solution pH is above it",
  "EK 8.7.A.1 applied to each acid separately against the same pH; n18 checks the pH lies between the two stated pKa values."),
 ("against the pKa of that acid",
  "EK 8.7.A.1 states the rule in terms of solution pH against acid pKa in both clauses; comparing with seven answers a different question."),
 ("mostly deprotonated even in an acidic solution",
  "EK 8.7.A.1's comparison is with the pKa, so an acid of low pKa in a mildly acidic solution has its base form dominant -- the case this topic's own table contains."),
 ("well before or well after the equivalence point",
  "EK 8.7.A.2 has the colour flip when the pH passes the indicator's pKa, which is why EK 8.7.A.3 asks for a pKa close to the equivalence pH."),
 ("pKa is above 7, close to that basic equivalence pH",
  "EK 8.5.A.4 puts a weak acid titration's equivalence point on the basic side and EK 8.7.A.3 asks for a pKa close to it."),
 ("pKa is below 7, close to that acidic equivalence pH",
  "EK 8.5.A.4 puts a weak base titration's equivalence point on the acidic side and EK 8.7.A.3 asks for a pKa close to it; vividness is not the criterion."),
 ("Indicator Z",
  "EK 8.7.A.3 read the other way. q24 recomputes every gap from the stated equivalence pH and checks the maximum is unique."),
 ("intermediate colour appears",
  "EK 8.5.A.3 makes the pair equal where pH equals pKa and EK 8.7.A.2 gives each form its own colour, so both are present at once."),
 ("property other than colour could serve",
  "EK 8.7.A.2 says properties SUCH AS colour, so the example is illustrative and the requirement is that the property differ between the states."),
 ("Green, because the pH is above its pKa so the deprotonated form",
  "EK 8.7.A.1 and EK 8.7.A.2 read off the table at a stated pH. q27 recomputes the state and the tabulated colour."),
 ("the pH of the solution is compared with that pKa",
  "Learning objective 8.7.A covers a weak acid OR base in relation to the pKa of the conjugate acid, and EK 8.7.A.1 gives that comparison against solution pH."),
 ("pKa of 6.8",
  "EK 8.7.A.3 applied to two stated indicators. n29 recomputes both gaps from the stated equivalence pH, and EK 8.5.A.4 makes a neutral equivalence pH possible."),
 ("relative to that acid's pKa",
  "EK 8.7.A.1 gives both clauses in terms of solution pH against acid pKa; nothing in it refers to the amount dissolved or the order of addition."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "From the titration curve above, which form predominates?"
        no_figure_language(mod)

    def logarithm_creeps_in(mod, cl):
        mod.QUESTIONS[3]["q"] = mod.QUESTIONS[3]["q"] + " Use \\( \\log \\) to decide."
        no_buffer_arithmetic(mod)

    def two_concentrations(mod, cl):
        mod.QUESTIONS[15]["q"] = ("A buffer holds 0.20 M of the acid and 0.40 M of its "
                                  "conjugate base. Which form predominates?")
        no_buffer_arithmetic(mod)

    def seven_rule_would_serve(mod, cl):
        # Every tabulated row made to agree with the pH-against-7 rule, so the
        # module could be answered by the wrong rule and would teach it.
        for idx in (4, 5, 6, 7):
            mod.QUESTIONS[idx]["table"] = dict(
                headers=h8_7._T_ACIDS["headers"],
                rows=[["HJ", "4.0", "9.0"], ["HL", "7.0", "6.0"],
                      ["HM", "6.0", "6.0"], ["HN", "8.0", "9.5"]])
        seven_is_not_the_comparison(mod)

    def tied_indicator(mod, cl):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h8_7._T_INDICATORS["headers"],
            rows=[["W", "3.5", "red", "yellow"], ["X", "5.0", "colourless", "pink"],
                  ["Y", "8.9", "colourless", "blue"], ["Z", "9.1", "yellow", "green"]])

    def indicator_matches_exactly(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h8_7._T_INDICATORS["headers"],
            rows=[["W", "3.5", "red", "yellow"], ["X", "5.2", "colourless", "pink"],
                  ["Y", "8.9", "colourless", "blue"], ["Z", "10.5", "yellow", "green"]])

    def colour_columns_swapped(mod, cl):
        mod.QUESTIONS[14]["table"] = dict(
            headers=h8_7._T_INDICATORS["headers"],
            rows=[["W", "3.5", "yellow", "red"], ["X", "5.0", "colourless", "pink"],
                  ["Y", "8.9", "colourless", "blue"], ["Z", "10.5", "yellow", "green"]])

    def single_positive_margin(mod, cl):
        # Only one row left with the base form predominant, so "largest margin"
        # would be asking nothing.
        mod.QUESTIONS[4]["table"] = dict(
            headers=h8_7._T_ACIDS["headers"],
            rows=[["HJ", "4.0", "9.0"], ["HL", "7.0", "6.0"],
                  ["HM", "6.0", "6.0"], ["HN", "6.5", "5.0"]])

    return [("a stem referring to a titration curve the bank cannot show", figure_language),
            ("a logarithm, which is 8.9's material", logarithm_creeps_in),
            ("a stem handed two concentrations, which is 8.9's setup", two_concentrations),
            ("a table on which the pH-against-7 rule would give every answer correctly",
             seven_rule_would_serve),
            ("two indicators tied for closest to the equivalence pH", tied_indicator),
            ("an indicator whose pKa matches the equivalence pH exactly, so the item no "
             "longer tests 'close'", indicator_matches_exactly),
            ("the two tabulated colour columns swapped", colour_columns_swapped),
            ("only one tabulated row left with the base form predominant",
             single_positive_margin)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_7)
no_buffer_arithmetic(h8_7)
seven_is_not_the_comparison(h8_7)
h.run(h8_7, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
