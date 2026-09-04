"""Key audit for AP CHEMISTRY 7.5 Magnitude of the Equilibrium Constant.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. EK 7.5.A.1 has two clauses and learning objective 7.5.A
frames them, so every key is one of three things:

  very large K -> proceeds essentially to completion, products predominate
                       1, 3, 5, 9, 15, 17, 19, 20, 21, 23, 27
  very small K -> barely proceeds at all, reactants predominate
                       2, 4, 6, 7, 11, 12, 14, 22, 24, 25, 28
  what the statement does NOT say -- nothing about a K near one, nothing about
  rate, and no claim that a large K empties the flask of reactant
                       8, 10, 13, 16, 18, 26, 29, 30

SCOPE. h7_6.py's header records the agreement that 7.5 owns what a large or
small K says about extent. ``no_value_of_k_question`` asserts that no item asks
for the VALUE of a constant, which is 7.4's job, and
``no_solving_for_concentration`` asserts that none is handed a K and asked for a
concentration, which is 7.7's.

THE CLAIM THE DATA HAS TO SUPPORT. ``magnitudes_are_extreme`` asserts that every
constant this module calls very large is at least a thousand and every one it
calls very small is at most a thousandth. Without it a table could quietly call
2.0 "very large" and the module would teach the opposite of EK 7.5.A.1.

ARITHMETIC. Scientific notation is PARSED out of the hand-written spans, never
restated, and every ordering and every product-to-reactant ratio is recomputed
from the table alone.

NEGATIVE CONTROL: ``python3 verify_h7_5.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h7_5

KCOL = "Equilibrium constant at 298 K"
KCOL2 = "Equilibrium constant at 500 K"
CA = "[A] at equilibrium (M)"
CB = "[B] at equilibrium (M)"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below)(?![a-z])", re.I)

# 7.4 owns "what is the value of Kc". Explicit phrases only.
_VALUE_Q = re.compile(
    r"(?<![a-z])(?:what is the value of|calculate (?:the value of )?k[cp]?"
    r"|value of k[cp]? is)(?![a-z])", re.I)

# 7.7 owns going from a stated K to an unknown equilibrium amount.
_SOLVE = re.compile(
    r"(?<![a-z])(?:what is the equilibrium concentration"
    r"|find the equilibrium concentration"
    r"|calculate the equilibrium concentration)(?![a-z])", re.I)

# ``\( 1 \times 10^{15} \)`` or a plain ``\( 2.0 \)``.
_SCI = re.compile(
    r"\\\(\s*(-?\d+(?:\.\d+)?)\s*(?:\\times\s*10\^\{(-?\d+)\})?\s*\\\)")


def sci(cell):
    """Parse a hand-written span such as ``\\( 1 \\times 10^{-12} \\)``."""
    m = _SCI.fullmatch(str(cell).strip())
    assert m, f"cell {cell!r} is not a hand-written number span"
    mantissa = float(m.group(1))
    return mantissa * (10.0 ** int(m.group(2))) if m.group(2) else mantissa


def sci_col(table, header):
    j = [cg.normalize(x) for x in table["headers"]].index(cg.normalize(header))
    return [sci(r[j]) for r in table["rows"]]


def sci_cell(table, row_label, header):
    labels = cg.labels(table)
    rows = [i for i, lab in enumerate(labels) if cg.normalize(lab) == cg.normalize(row_label)]
    assert len(rows) == 1, f"row {row_label!r} appears {len(rows)} times"
    return sci_col(table, header)[rows[0]]


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


def no_value_of_k_question(module):
    """7.4 owns computing a constant from measurements."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _VALUE_Q.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: asks for {hit.group(0)!r}, which is 7.4's material"
        )
    print(f"OK  {module.TOPIC[0]} scope: no item asks for the value of a constant.")


def no_solving_for_concentration(module):
    """7.7 owns going from a constant to an equilibrium amount."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _SOLVE.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: asks for {hit.group(0)!r}, which is 7.7's material"
        )
    print(f"OK  {module.TOPIC[0]} scope: no item solves for an equilibrium concentration.")


def magnitudes_are_extreme(module, big=1e3, small=1e-3):
    """A constant this module calls very large or very small must be one.

    EK 7.5.A.1's two clauses are about VERY large and VERY small values. A table
    whose 'very large' constant were 2.0 would teach the opposite of the
    statement while every other check still passed, so the data itself is
    gated: the largest constant in each table must clear ``big`` and the
    smallest must fall below ``small``.
    """
    checked = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        t = item.get("table")
        if not t:
            continue
        for header in (KCOL, KCOL2):
            if cg.normalize(header) not in [cg.normalize(x) for x in t["headers"]]:
                continue
            values = sci_col(t, header)
            assert max(values) >= big or min(values) <= small, (
                f"{module.TOPIC[0]} q{i}: no tabulated constant is extreme "
                f"({values}), so the item cannot illustrate EK 7.5.A.1"
            )
            if max(values) >= 1.0:
                assert max(values) >= big, (
                    f"{module.TOPIC[0]} q{i}: the largest tabulated constant is "
                    f"{max(values)}, which is not 'very large'"
                )
            assert min(values) <= small, (
                f"{module.TOPIC[0]} q{i}: the smallest tabulated constant is "
                f"{min(values)}, which is not 'very small'"
            )
            checked += 1
    assert checked >= 2, f"{module.TOPIC[0]}: only {checked} constant table(s) checked"
    print(f"OK  {module.TOPIC[0]} magnitudes: {checked} tabulated set(s) of constants span "
          "a genuinely extreme range, so the module's language matches its data.")


# ------------------------------------------------------------------ table items

def q5(table, item):
    ks = dict(zip(cg.labels(table), sci_col(table, KCOL)))
    biggest = max(ks, key=ks.get)
    assert biggest == "W", f"the largest tabulated constant is {biggest}: {ks}"
    others = [v for lab, v in ks.items() if lab != biggest]
    assert ks[biggest] >= 1e3 * max(others), (
        f"the largest constant {ks[biggest]} is not far above the next, {max(others)}"
    )
    h.shows(item, "Reaction W")
    return f"the tabulated constants are {ks}, whose largest by orders of magnitude is {biggest}"


def q6(table, item):
    ks = dict(zip(cg.labels(table), sci_col(table, KCOL)))
    smallest = min(ks, key=ks.get)
    assert smallest == "X", f"the smallest tabulated constant is {smallest}: {ks}"
    assert ks[smallest] <= 1e-3, f"the smallest tabulated constant is {ks[smallest]}"
    h.shows(item, "Reaction X")
    return f"the tabulated constants are {ks}, whose smallest is {smallest} at {ks[smallest]:g}"


def q7(table, item):
    ks = dict(zip(cg.labels(table), sci_col(table, KCOL)))
    smallest = min(ks, key=ks.get)
    assert smallest == "X", f"the smallest tabulated constant is {smallest}: {ks}"
    assert len(set(ks.values())) == len(ks), \
        "the four tabulated constants must be distinct, so no two mixtures share a ratio"
    h.shows(item, "Reaction X")
    return (f"the smallest tabulated constant, {ks[smallest]:g}, belongs to the mixture "
            "with the least product relative to reactant")


def q8(table, item):
    ks = dict(zip(cg.labels(table), sci_col(table, KCOL)))
    near_one = [lab for lab, v in ks.items() if 0.1 <= v <= 10.0]
    assert near_one == ["Y"], f"the constants near one are {near_one}: {ks}"
    h.shows(item, "Neither clause applies")
    return f"exactly one tabulated constant, {ks['Y']:g}, lies within a factor of ten of one"


def q9(table, item):
    ks = dict(zip(cg.labels(table), sci_col(table, KCOL2)))
    bigger = max(ks, key=ks.get)
    assert bigger == "J", f"the larger tabulated constant is {bigger}: {ks}"
    assert all(v < 1.0 for v in ks.values()), (
        "both tabulated constants must be below one, or the distractor about both being "
        "less than one would not be the trap it is meant to be"
    )
    h.shows(item, "Reaction J")
    return f"the tabulated constants are {ks}, of which {bigger} is the larger"


def ratio(table, label):
    """Product over reactant for one tabulated equilibrium mixture."""
    return cg.cell(table, label, CB) / cg.cell(table, label, CA)


def q11(table, item):
    rs = {lab: ratio(table, lab) for lab in cg.labels(table)}
    biggest = max(rs, key=rs.get)
    assert biggest == "P", f"the largest product-to-reactant ratio is at {biggest}: {rs}"
    assert rs[biggest] > 100, f"the largest ratio is only {rs[biggest]}"
    assert len(set(round(v, 9) for v in rs.values())) == len(rs), \
        "the three tabulated ratios must be distinct"
    h.shows(item, "Mixture P")
    return f"the tabulated ratios are {rs}, whose unique maximum is at mixture {biggest}"


def q12(table, item):
    rs = {lab: ratio(table, lab) for lab in cg.labels(table)}
    smallest = min(rs, key=rs.get)
    assert smallest == "R", f"the smallest ratio is at {smallest}: {rs}"
    assert rs[smallest] < 0.01, f"the smallest ratio is only {rs[smallest]}"
    assert cg.cell(table, smallest, CB) > 0, (
        "some product must be present, since EK 7.1.A.2 requires it and one distractor "
        "turns on that"
    )
    h.shows(item, "Mixture R")
    return f"mixture {smallest} holds product at {rs[smallest]:.4g} times its reactant"


def q13(table, item):
    rs = {lab: ratio(table, lab) for lab in cg.labels(table)}
    middling = [lab for lab, v in rs.items() if 0.1 <= v <= 10.0]
    assert middling == ["S"], f"the mixtures with a ratio near one are {middling}: {rs}"
    h.shows(item, "Mixture S")
    return f"exactly one tabulated mixture has a product-to-reactant ratio near one: {rs}"


TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 11: q11, 12: q12, 13: q13}


# ---------------------------------------------------------------- stem numerics

def _spans(item):
    """Every number written as a span in the stem, parsed."""
    return [sci("\\( " + m + " \\)") for m in
            re.findall(r"\\\((.*?)\\\)", item["q"])]


def n14(item):
    k, = _spans(item)
    assert k <= 1e-3, f"the stated constant is {k}, not very small"
    assert k > 0, "an equilibrium constant is positive, so a trace of product does form"
    h.shows(item, "Almost no product")
    return f"the stated constant {k:g} is far below one, EK 7.5.A.1's barely-proceeding case"


def n15(item):
    k, = _spans(item)
    assert k >= 1e3, f"the stated constant is {k}, not very large"
    h.shows(item, "trace of reactant left")
    return f"the stated constant {k:g} is far above one, EK 7.5.A.1's completion case"


def n21(item):
    values = [sci(c) for c in item["choices"]]
    biggest = max(values)
    assert abs(biggest - 5e8) < 1e-6 * 5e8, f"the largest choice recomputes to {biggest}"
    assert values.index(biggest) == item["ans"], (
        f"the largest value sits at choice {values.index(biggest)}, not at the key"
    )
    assert len([v for v in values if v > 1.0]) == 1, (
        f"exactly one choice must exceed one, so the key is unambiguous: {values}"
    )
    h.shows(item, "5 \\times 10^{8}")
    return f"the five choices recompute to {values}, of which only {biggest:g} exceeds one"


def n22(item):
    values = [sci(c) for c in item["choices"]]
    smallest = min(values)
    assert abs(smallest - 2e-16) < 1e-6 * 2e-16, f"the smallest choice recomputes to {smallest}"
    assert values.index(smallest) == item["ans"], (
        f"the smallest value sits at choice {values.index(smallest)}, not at the key"
    )
    assert len([v for v in values if v < 1.0]) == 1, (
        f"exactly one choice must fall below one, so the key is unambiguous: {values}"
    )
    h.shows(item, "2 \\times 10^{-16}")
    return f"the five choices recompute to {values}, of which only {smallest:g} falls below one"


def n25(item):
    a, b = _spans(item)
    assert a > b, f"the first stated constant {a} is not the larger"
    assert a <= 1e-3 and b <= 1e-3, f"both stated constants must be very small: {a}, {b}"
    assert a / b >= 1e3, f"the two constants differ by only a factor of {a / b}"
    h.shows(item, "the first proceeds further than the second")
    return (f"the stated constants {a:g} and {b:g} are both far below one, with the first "
            f"larger by a factor of {a / b:g}")


def n26(item):
    k, = _spans(item)
    assert k >= 1e3, f"the stated constant is {k}, not very large"
    assert k < float("inf"), "a finite constant leaves a finite amount of reactant"
    h.shows(item, "small but nonzero fraction")
    return (f"the stated constant {k:g} is finite, so EK 7.1.A.2 leaves a small but nonzero "
            "amount of reactant")


NUMERIC = {14: n14, 15: n15, 21: n21, 22: n22, 25: n25, 26: n26}


CLAIMS = [
 ("proceed essentially to completion",
  "EK 7.5.A.1, verbatim: some equilibrium reactions have very large K values and proceed essentially to completion. The statement is about extent, not speed or energy."),
 ("barely proceed at all",
  "EK 7.5.A.1, verbatim: others have very small K values and barely proceed at all. Barely proceeding is a statement about how far, not how slowly."),
 ("products, since the reaction has proceeded nearly to completion",
  "Learning objective 7.5.A links the size of K to the relative concentrations, and EK 7.5.A.1 puts a very large K at the completion end of that scale."),
 ("Reactants, since the reaction has barely proceeded",
  "EK 7.5.A.1's second clause leaves most of the reactant unconverted; EK 7.1.A.2 keeps some product present, so 'only reactants' overstates it."),
 ("Reaction W",
  "EK 7.5.A.1's first clause applied to four tabulated constants. q5 recomputes them and checks the largest is orders of magnitude above the next."),
 ("Reaction X",
  "EK 7.5.A.1's second clause. q6 recomputes the tabulated constants and checks the smallest really is at most a thousandth."),
 ("Reaction X",
  "Learning objective 7.5.A: the smallest constant belongs to the mixture with the least product relative to reactant. q7 checks the four tabulated values are distinct."),
 ("Neither clause applies",
  "EK 7.5.A.1 describes only very large and very small constants; q8 recomputes which tabulated constant lies within a factor of ten of one and checks it is unique."),
 ("Reaction J",
  "Learning objective 7.5.A: the larger of two constants gives the mixture richer in product. q9 recomputes both and checks both are below one, which is the trap."),
 ("how far the reaction proceeds, not how quickly",
  "EK 7.5.A.1 speaks of extent -- proceeding essentially to completion or barely at all -- while EK 9.4.A.1 separately allows a favoured process not to occur at a measurable rate."),
 ("Mixture P",
  "Learning objective 7.5.A read from a composition. q11 recomputes all three product-to-reactant ratios and checks the maximum is unique and large."),
 ("Mixture R",
  "EK 7.5.A.1's second clause read from a composition. q12 recomputes the ratios and checks some product is nonetheless present, as EK 7.1.A.2 requires."),
 ("Mixture S",
  "EK 7.5.A.1 covers only the two extremes; q13 recomputes which tabulated mixture has a ratio near one and checks it is unique."),
 ("Almost no product",
  "EK 7.5.A.1's second clause for a stated constant, parsed and checked below a thousandth in n14; the value is positive, so a trace does form."),
 ("trace of reactant left",
  "EK 7.5.A.1's first clause with EK 7.1.A.2's requirement that both species be present, so the reactant is reduced to a trace rather than eliminated."),
 ("very small amount of reactant remains",
  "EK 7.5.A.1 says ESSENTIALLY to completion, and EK 7.1.A.2 has reactants and products simultaneously present at equilibrium."),
 ("proceeded further toward products",
  "Learning objective 7.5.A ties magnitude to composition; a ratio of constants says nothing about time, which EK 9.4.A.1 treats separately."),
 ("concentrations have become constant",
  "EK 7.1.A.2 makes constancy the signature of equilibrium, and EK 7.5.A.1 explains the sparse product: the reaction barely proceeds."),
 ("very large, and at equilibrium the products predominate",
  "EK 7.5.A.1's first clause with learning objective 7.5.A's link between the value of K and the relative concentrations."),
 ("very large equilibrium constant",
  "EK 7.5.A.1: reactions with very large K values proceed essentially to completion, which is the near-total conversion the chemist wants."),
 ("5 \\times 10^{8}",
  "EK 7.5.A.1's first clause applied to five stated constants. n21 parses all five and checks exactly one exceeds one, so the key is unambiguous."),
 ("2 \\times 10^{-16}",
  "EK 7.5.A.1's second clause applied to five stated constants. n22 parses all five and checks exactly one falls below one."),
 ("much greater than one",
  "Learning objective 7.5.A with EK 7.3.A.1's arrangement of products over reactants, so a product-rich mixture means a large constant; a ratio of concentrations is never negative."),
 ("so its constant is very small",
  "EK 7.5.A.1's second clause; EK 7.4.A.1 makes the constant independent of how the vessel was charged."),
 ("the first proceeds further than the second",
  "Both stated constants fall under EK 7.5.A.1's second clause, and learning objective 7.5.A still orders them. n25 parses both and checks the gap is large."),
 ("small but nonzero fraction",
  "EK 7.5.A.1's word 'essentially' with EK 7.1.A.2's simultaneous presence; how small depends on the reaction, so no universal fraction can be quoted."),
 ("mixture richer in products",
  "Learning objective 7.5.A stated directly. Temperature fixes the value of the constant, which is a separate matter from what the value then reports."),
 ("only a trace of product can be detected",
  "EK 7.5.A.1's 'barely proceed at all' is about extent, so the observable consequence is a mixture holding almost none of the product."),
 ("holds mostly products or mostly reactants",
  "Learning objective 7.5.A makes the relative concentrations the thing the magnitude reports; EK 9.4.A.1 separates extent from rate."),
 ("reach equilibrium with both species present",
  "EK 7.1.A.2 applies to both of EK 7.5.A.1's cases alike: reactants and products simultaneously present with constant concentrations."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "In the figure above, which reaction goes furthest?"
        no_figure_language(mod)

    def value_question(mod, cl):
        mod.QUESTIONS[2]["q"] = "What is the value of Kc for this reaction at 298 K?"
        no_value_of_k_question(mod)

    def solving_question(mod, cl):
        mod.QUESTIONS[2]["q"] = ("What is the equilibrium concentration of the product in "
                                 "this reaction?")
        no_solving_for_concentration(mod)

    def not_actually_extreme(mod, cl):
        # A table whose "very large" constant is 2.0 would teach the opposite of
        # EK 7.5.A.1 while every structural check still passed.
        mod.QUESTIONS[4]["table"] = dict(
            headers=h7_5._T_K["headers"],
            rows=[["W", "\\( 2.0 \\)"], ["X", "\\( 0.5 \\)"],
                  ["Y", "\\( 1.0 \\)"], ["Z", "\\( 1.5 \\)"]])
        magnitudes_are_extreme(mod)

    def largest_not_far_ahead(mod, cl):
        mod.QUESTIONS[4]["table"] = dict(
            headers=h7_5._T_K["headers"],
            rows=[["W", "\\( 1 \\times 10^{15} \\)"], ["X", "\\( 1 \\times 10^{-12} \\)"],
                  ["Y", "\\( 2.0 \\)"], ["Z", "\\( 5 \\times 10^{14} \\)"]])

    def two_mixtures_near_one(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h7_5._T_COMPS["headers"],
            rows=[["P", "0.0010", "0.9990"], ["R", "0.4000", "0.6000"],
                  ["S", "0.5000", "0.5000"]])

    def two_choices_above_one(mod, cl):
        ch = list(mod.QUESTIONS[20]["choices"])
        ch[2] = "\\( 5 \\times 10^{3} \\)"
        mod.QUESTIONS[20]["choices"] = ch

    return [("a stem referring to a figure the bank cannot show", figure_language),
            ("an item asking for the value of a constant, which 7.4 owns", value_question),
            ("an item solving for an equilibrium concentration, which 7.7 owns",
             solving_question),
            ("a table calling 2.0 a very large constant", not_actually_extreme),
            ("the largest tabulated constant no longer far above the next",
             largest_not_far_ahead),
            ("two tabulated mixtures with a ratio near one, so the key is not unique",
             two_mixtures_near_one),
            ("a second choice above one, so the largest-constant key is not unique",
             two_choices_above_one)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h7_5)
no_value_of_k_question(h7_5)
no_solving_for_concentration(h7_5)
magnitudes_are_extreme(h7_5)
h.run(h7_5, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
