"""Key audit for AP CHEMISTRY 8.9 Henderson- Hasselbalch Equation.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. EK 8.9.A.1 is the topic's only statement and it carries
four separable claims:

  the pH depends on the pKa and the RATIO, through the stated equation
        1, 2, 3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 30
  small additions do not significantly change the ratio, and so do not
  significantly change the pH                              4, 5, 29
  the change is much less than it would have been without the buffer     6
  the two exclusion statements                             7, 8

SCOPE, from the four-way buffer split recorded in h8_4.py's header. 8.4 owns
which case a mixture is, 8.8 the mechanism and its net ionic equations, 8.10 the
capacity. ``no_other_buffer_topic`` asserts that no stem asks for a net ionic
equation and that no KEYED choice is about capacity -- a distractor may name
capacity, since ruling it out is part of knowing what this equation does.

THE EXCLUSIONS ARE ENFORCED. ``no_ph_change_computation`` asserts that any item
whose stem describes an addition to a buffer keys a qualitative answer, never a
number, which is exactly what the first exclusion statement removes.
``no_derivation_task`` asserts that no stem asks the student to derive the
equation.

ARITHMETIC. Every ratio in the module is a power of ten, so every logarithm is
exact. ``hh`` implements the equation once and every pH and every ratio is
recomputed through it from the tabulated or stated values alone.

NEGATIVE CONTROL: ``python3 verify_h8_9.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h8_9

PKA = "pKa of the acid"
CB = "[A-] (M)"
CA = "[HA] (M)"
MPH = "Measured pH"
RPKA = "pKa of the acid it was made from"

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|titration curve)(?![a-z])", re.I)

_NET_IONIC = re.compile(r"(?<![a-z])net ionic(?![a-z])", re.I)
_CAPACITY = re.compile(r"(?<![a-z])capacity(?![a-z])", re.I)
_ADDITION = re.compile(
    r"(?<![a-z])(?:after adding|is added to|on adding|on addition of"
    r"|adding a small amount|adding small amounts)(?![a-z])", re.I)
_DERIVE = re.compile(r"(?<![a-z])(?:derive|derivation of the henderson)(?![a-z])", re.I)


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


def no_other_buffer_topic(module):
    """8.8 owns the net ionic equations; 8.10 owns capacity."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _NET_IONIC.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: asks for a net ionic equation, which is 8.8's material"
        )
        hit = _CAPACITY.search(h.keyed(item))
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: keys an answer about capacity, which is 8.10's "
            f"material -- {h.keyed(item)!r}"
        )
    print(f"OK  {module.TOPIC[0]} scope: no net ionic equation asked for, and no key rests "
          "on buffer capacity.")


def no_ph_change_computation(module):
    """The first exclusion statement attached to EK 8.9.A.1.

    An item whose stem describes acid or base being added to a buffer may ask
    what happens QUALITATIVELY -- EK 8.9.A.1 says it plainly -- but may not key
    a number, because putting a number on that change is exactly what the
    exclusion statement removes from the exam.
    """
    checked = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        if not _ADDITION.search(item["q"]):
            continue
        checked += 1
        key = h.keyed(item)
        assert not re.search(r"\d", key), (
            f"{module.TOPIC[0]} q{i}: the stem describes an addition to a buffer and the "
            f"key states a number ({key!r}), which the exclusion statement removes"
        )
    assert checked >= 3, (
        f"{module.TOPIC[0]}: only {checked} item(s) describe an addition, too few for the "
        "check to mean anything"
    )
    print(f"OK  {module.TOPIC[0]} exclusion: {checked} item(s) describe an addition to a "
          "buffer, and every one keys a qualitative answer rather than a computed change.")


def no_derivation_task(module):
    """The second exclusion statement attached to EK 8.9.A.1."""
    for i, item in enumerate(module.QUESTIONS, 1):
        hit = _DERIVE.search(item["q"])
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the stem says {hit.group(0)!r}, and derivation of the "
            "equation is excluded from the exam"
        )
    print(f"OK  {module.TOPIC[0]} exclusion: no stem asks the student to derive the "
          "equation.")


# ------------------------------------------------------------------ arithmetic

def hh(pka, base, acid):
    """EK 8.9.A.1's equation, written once and used by every check below."""
    return pka + math.log10(base / acid)


def ratio_from(ph, pka):
    """The same equation rearranged: the base-to-acid ratio from pH and pKa."""
    return 10.0 ** (ph - pka)


# ------------------------------------------------------------------ table items

def _buffer_ph(table, label):
    return hh(cg.cell(table, label, PKA), cg.cell(table, label, CB),
              cg.cell(table, label, CA))


def q9(table, item):
    ph = _buffer_ph(table, "1")
    assert abs(ph - 4.00) < 1e-12, f"the pH recomputes to {ph}"
    assert abs(cg.cell(table, "1", CB) - cg.cell(table, "1", CA)) < 1e-12, \
        "the two tabulated concentrations must be equal for the logarithm to vanish"
    h.shows(item, "4.00")
    return f"equal tabulated concentrations leave the pH at the tabulated pKa, {ph:.2f}"


def q10(table, item):
    ph = _buffer_ph(table, "2")
    assert abs(ph - 5.00) < 1e-12, f"the pH recomputes to {ph}"
    r = cg.cell(table, "2", CB) / cg.cell(table, "2", CA)
    assert abs(r - 10.0) < 1e-12, f"the tabulated ratio recomputes to {r}"
    h.shows(item, "5.00")
    return f"a tabulated ratio of {r:g} puts the pH one unit above the pKa, at {ph:.2f}"


def q11(table, item):
    ph = _buffer_ph(table, "3")
    assert abs(ph - 3.00) < 1e-12, f"the pH recomputes to {ph}"
    r = cg.cell(table, "3", CB) / cg.cell(table, "3", CA)
    assert abs(r - 0.10) < 1e-12, f"the tabulated ratio recomputes to {r}"
    h.shows(item, "3.00")
    return f"a tabulated ratio of {r:g} puts the pH one unit below the pKa, at {ph:.2f}"


def q12(table, item):
    ph = _buffer_ph(table, "4")
    assert abs(ph - 10.00) < 1e-12, f"the pH recomputes to {ph}"
    r = cg.cell(table, "4", CB) / cg.cell(table, "4", CA)
    assert abs(r - 10.0) < 1e-12, f"the tabulated ratio recomputes to {r}"
    assert cg.cell(table, "4", CB) != cg.cell(table, "2", CB), (
        "this buffer must use different concentrations from the earlier one, so the item "
        "shows that only the ratio enters"
    )
    h.shows(item, "10.00")
    return (f"different tabulated concentrations with the same ratio {r:g} put the pH at "
            f"{ph:.2f}, one unit above the tabulated pKa")


def q13(table, item):
    equal = [lab for lab in cg.labels(table)
             if abs(_buffer_ph(table, lab) - cg.cell(table, lab, PKA)) < 1e-12]
    assert equal == ["1"], f"the buffers whose pH equals their pKa are {equal}"
    h.shows(item, "Buffer 1")
    return f"exactly one tabulated buffer recomputes a pH equal to its own pKa: {equal[0]}"


def q18(table, item):
    r = ratio_from(cg.cell(table, "B", MPH), cg.cell(table, "B", RPKA))
    assert abs(r - 10.0) < 1e-9, f"the ratio recomputes to {r}"
    h.shows(item, "base is ten times the acid")
    return (f"the tabulated pH exceeds the tabulated pKa by "
            f"{cg.cell(table, 'B', MPH) - cg.cell(table, 'B', RPKA):g}, so the ratio "
            f"recomputes as {r:g}")


def q19(table, item):
    ones = [lab for lab in cg.labels(table)
            if abs(ratio_from(cg.cell(table, lab, MPH), cg.cell(table, lab, RPKA)) - 1.0)
            < 1e-9]
    assert ones == ["A"], f"the solutions with a ratio of one are {ones}"
    h.shows(item, "Solution A")
    return f"exactly one tabulated solution recomputes a base-to-acid ratio of one: {ones[0]}"


def q20(table, item):
    r = ratio_from(cg.cell(table, "C", MPH), cg.cell(table, "C", RPKA))
    assert abs(r - 0.01) < 1e-9, f"the ratio recomputes to {r}"
    h.shows(item, "acid is one hundred times the base")
    return (f"the tabulated pH falls {cg.cell(table, 'C', RPKA) - cg.cell(table, 'C', MPH):g} "
            f"below the tabulated pKa, so the ratio recomputes as {r:g}")


TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 18: q18, 19: q19, 20: q20}


# ---------------------------------------------------------------- stem numerics

def n14(item):
    ph = hh(6.00, 1.0, 1.0)
    assert abs(ph - 6.00) < 1e-12, f"the pH recomputes to {ph}"
    h.shows(item, "6.00")
    return f"equal concentrations give a logarithm of zero, leaving the pH at {ph:.2f}"


def n15(item):
    ph = hh(4.50, 10.0, 1.0)
    assert abs(ph - 5.50) < 1e-12, f"the pH recomputes to {ph}"
    assert abs(hh(4.50, 1.0, 10.0) - 3.50) < 1e-12, \
        "the mirrored ratio must give the 3.50 distractor"
    h.shows(item, "5.50")
    return f"a ratio of ten adds one to the pKa, recomputing the pH as {ph:.2f}"


def n16(item):
    ph = hh(4.50, 1.0, 10.0)
    assert abs(ph - 3.50) < 1e-12, f"the pH recomputes to {ph}"
    h.shows(item, "3.50")
    return f"a ratio of one tenth subtracts one from the pKa, recomputing the pH as {ph:.2f}"


def n17(item):
    ph = hh(3.00, 100.0, 1.0)
    assert abs(ph - 5.00) < 1e-12, f"the pH recomputes to {ph}"
    assert abs(hh(3.00, 10.0, 1.0) - 4.00) < 1e-12, \
        "a ratio of ten must give the 4.00 distractor, one unit lower"
    h.shows(item, "5.00")
    return f"a ratio of one hundred adds two to the pKa, recomputing the pH as {ph:.2f}"


def n21(item):
    r = ratio_from(5.00, 5.00)
    assert abs(r - 1.0) < 1e-12, f"the ratio recomputes to {r}"
    h.shows(item, "present in equal concentrations")
    return f"a pH equal to the pKa recomputes the ratio as {r:g}"


def n22(item):
    r = ratio_from(1.0, 0.0)       # the stem states a difference of one unit
    assert abs(r - 10.0) < 1e-12, f"the ratio recomputes to {r}"
    assert abs(ratio_from(2.0, 0.0) - 100.0) < 1e-12, \
        "two units would be a hundredfold, which is what makes the factor of ten specific"
    h.shows(item, "base is ten times the acid")
    return f"a difference of one pH unit recomputes the ratio as {r:g}, not as two"


def n24(item):
    high = hh(0.0, 10.0, 1.0)
    low = hh(0.0, 1.0, 10.0)
    assert abs((high - low) - 2.0) < 1e-12, f"the gap recomputes to {high - low}"
    assert high > low, "the larger ratio must give the higher pH"
    h.shows(item, "larger ratio, by two units")
    return (f"the two stated ratios sit {high:+g} and {low:+g} units from the shared pKa, "
            f"a gap of {high - low:g}")


def n27(item):
    r = ratio_from(5.00, 4.00)
    assert abs(r - 10.0) < 1e-9, f"the required ratio recomputes to {r}"
    assert abs(hh(4.00, r, 1.0) - 5.00) < 1e-9, "the recomputed ratio must reach the target pH"
    h.shows(item, "Ten parts conjugate base to one part acid")
    return (f"reaching a pH one unit above the stated pKa needs a base-to-acid ratio of "
            f"{r:g}")


def n28(item):
    target = 9.00
    assert abs(hh(target, 1.0, 1.0) - target) < 1e-12, \
        "equal concentrations must leave the pH at the pKa"
    assert abs(hh(5.00, 1.0, 1.0) - target) > 1e-9, \
        "the 5.00 distractor must not reach the target pH at equal concentrations"
    h.shows(item, "pKa of 9.00")
    return (f"with equal concentrations the equation reduces to pH equals pKa, so the "
            f"target of {target:.2f} fixes the pKa")


NUMERIC = {14: n14, 15: n15, 16: n16, 17: n17, 21: n21, 22: n22, 24: n24,
           27: n27, 28: n28}


CLAIMS = [
 ("concentration ratio of the conjugate acid-base pair",
  "EK 8.9.A.1's opening sentence: the pH of the buffer is related to the pKa of the acid and the concentration ratio of the pair. A ratio is unchanged by the volume."),
 ("p}K_a + \\log\\frac{[\\mathrm{A^-}]}{[\\mathrm{HA}]}",
  "EK 8.9.A.1's stated equation, with the pKa plus the logarithm of the base-to-acid ratio. Inverting the ratio or changing the sign would move the pH the wrong way."),
 ("equilibrium expression associated with the dissociation of a weak acid",
  "EK 8.9.A.1 states that the relation is a consequence of exactly that equilibrium expression."),
 ("It does not change it significantly",
  "EK 8.9.A.1: adding small amounts of acid or base does not significantly change the ratio of the pair, because EK 8.8.A.1 puts both members there in large concentration."),
 ("pH does not change significantly either",
  "EK 8.9.A.1: the ratio does not significantly change and THUS the solution pH does not significantly change."),
 ("buffered solution is much less",
  "EK 8.9.A.1: the change in pH on addition to a buffered solution is much less than it would have been in the absence of the buffer. Much less is not none."),
 ("change in pH resulting from adding an acid or a base to a buffer",
  "The first exclusion statement attached to EK 8.9.A.1 names exactly that computation; using the equation on a stated composition remains in scope."),
 ("Deriving the Henderson-Hasselbalch equation",
  "The second exclusion statement attached to EK 8.9.A.1 excludes derivation; using the equation is the topic's learning objective."),
 ("4.00",
  "EK 8.9.A.1's equation with equal tabulated concentrations. q9 recomputes the pH and checks the two concentrations are equal, which is why the logarithm vanishes."),
 ("5.00",
  "EK 8.9.A.1's equation with a tabulated ratio of ten. q10 recomputes both the ratio and the pH."),
 ("3.00",
  "EK 8.9.A.1's equation with a tabulated ratio of one tenth, which puts the pH below the pKa. Recomputed in q11."),
 ("10.00",
  "EK 8.9.A.1's equation with different concentrations but the same ratio as an earlier row. q12 recomputes both and checks the concentrations really do differ."),
 ("Buffer 1",
  "EK 8.9.A.1's equation leaves pH equal to pKa only when the logarithm vanishes. q13 recomputes every row and checks exactly one satisfies it."),
 ("6.00",
  "EK 8.9.A.1's equation with equal concentrations; n14 recomputes it. A buffer's pH is set by its acid, not by neutrality."),
 ("5.50",
  "EK 8.9.A.1's equation with a tenfold excess of the base form. n15 recomputes it and also recomputes the mirrored case that is the distractor."),
 ("3.50",
  "EK 8.9.A.1's equation with a tenfold excess of the acid form, one unit below the pKa. Recomputed in n16."),
 ("5.00",
  "EK 8.9.A.1's equation with a hundredfold ratio, two units above the pKa. n17 recomputes it and the tenfold value one unit lower."),
 ("base is ten times the acid",
  "EK 8.9.A.1's equation rearranged: the logarithm of the ratio is the tabulated pH minus the tabulated pKa. Recomputed in q18."),
 ("Solution A",
  "The ratio is one exactly where pH equals pKa. q19 recomputes every tabulated row and checks exactly one qualifies."),
 ("acid is one hundred times the base",
  "A tabulated pH two units below the pKa gives a ratio of one hundredth. Recomputed in q20."),
 ("present in equal concentrations",
  "EK 8.9.A.1 rearranged with a zero difference; n21 recomputes the ratio as one, so it certainly can be determined."),
 ("base is ten times the acid",
  "A difference of one pH unit is a factor of ten in the ratio. n22 recomputes it and recomputes the two-unit case to show the factor is not two."),
 ("differ by the difference between the two pKa values",
  "EK 8.9.A.1's equation adds the same logarithm term to each pKa when the ratios agree, so the two pH values are displaced equally."),
 ("larger ratio, by two units",
  "One buffer sits a unit above the shared pKa and the other a unit below. n24 recomputes both displacements and their gap."),
 ("ratio of base to acid is less than one",
  "EK 8.9.A.1's equation makes the logarithm of the ratio the pH minus the pKa, and a negative logarithm belongs to a ratio below one; a concentration ratio is never negative."),
 ("present in equal concentrations",
  "EK 8.9.A.1's logarithm term vanishes only for a ratio of one, and the pKa may be any value, so no particular pH is required."),
 ("Ten parts conjugate base to one part acid",
  "EK 8.9.A.1's equation solved for the ratio that makes up a one-unit difference. n27 recomputes the ratio and checks it reaches the target pH."),
 ("pKa of 9.00",
  "With equal concentrations EK 8.9.A.1's equation reduces to pH equals pKa, so the target fixes the acid. n28 recomputes both that and the failure of the distractor."),
 ("present in large concentration, so a small addition",
  "EK 8.8.A.1 puts a large concentration of both members in a buffer and EK 8.9.A.1 concludes that small additions do not significantly change the ratio."),
 ("or the ratio from the pH and the pKa",
  "Learning objective 8.9.A identifies the pH from the pair, and rearranging EK 8.9.A.1's equation runs the same relation the other way; the change on addition is excluded."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[0]["q"] = "From the titration curve above, what is the buffer pH?"
        no_figure_language(mod)

    def net_ionic_creeps_in(mod, cl):
        mod.QUESTIONS[2]["q"] = "Which net ionic equation describes the buffer's response?"
        no_other_buffer_topic(mod)

    def capacity_key(mod, cl):
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[0] = "The capacity of the buffer to absorb added base"
        mod.QUESTIONS[2]["choices"] = ch
        cl[2] = ("capacity of the buffer", cl[2][1])
        no_other_buffer_topic(mod)

    def computed_change(mod, cl):
        ch = list(mod.QUESTIONS[3]["choices"])
        ch[0] = "The ratio falls by 0.04 units"
        mod.QUESTIONS[3]["choices"] = ch
        cl[3] = ("falls by 0", cl[3][1])
        no_ph_change_computation(mod)

    def derivation_task(mod, cl):
        mod.QUESTIONS[2]["q"] = "Derive the Henderson-Hasselbalch equation from Ka."
        no_derivation_task(mod)

    def ratio_flipped(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h8_9._T_BUFFERS["headers"],
            rows=[["1", "4.00", "0.10", "0.10"], ["2", "4.00", "0.10", "1.00"],
                  ["3", "4.00", "0.10", "1.00"], ["4", "9.00", "0.50", "0.050"]])

    def same_concentrations_twice(mod, cl):
        # Buffer 4 given the same concentrations as buffer 2, so the item would
        # no longer show that only the ratio enters.
        mod.QUESTIONS[11]["table"] = dict(
            headers=h8_9._T_BUFFERS["headers"],
            rows=[["1", "4.00", "0.10", "0.10"], ["2", "4.00", "1.00", "0.10"],
                  ["3", "4.00", "0.10", "1.00"], ["4", "9.00", "1.00", "0.10"]])

    def second_equal_row(mod, cl):
        mod.QUESTIONS[12]["table"] = dict(
            headers=h8_9._T_BUFFERS["headers"],
            rows=[["1", "4.00", "0.10", "0.10"], ["2", "4.00", "1.00", "1.00"],
                  ["3", "4.00", "0.10", "1.00"], ["4", "9.00", "0.50", "0.050"]])

    def measured_ph_moved(mod, cl):
        mod.QUESTIONS[17]["table"] = dict(
            headers=h8_9._T_RATIOS["headers"],
            rows=[["A", "5.00", "5.00"], ["B", "7.00", "5.00"], ["C", "3.00", "5.00"]])

    return [("a stem referring to a titration curve the bank cannot show", figure_language),
            ("an item asking for a net ionic equation, which 8.8 owns", net_ionic_creeps_in),
            ("a key resting on buffer capacity, which 8.10 owns", capacity_key),
            ("a computed pH change on addition, which the exclusion statement removes",
             computed_change),
            ("a stem asking the student to derive the equation", derivation_task),
            ("a tabulated ratio inverted, so the keyed pH is wrong", ratio_flipped),
            ("the fourth buffer given the same concentrations as the second, so the item "
             "no longer shows that only the ratio matters", same_concentrations_twice),
            ("a second tabulated row whose pH equals its pKa", second_equal_row),
            ("a tabulated pH moved, so the keyed ratio is wrong", measured_ph_moved)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h8_9)
no_other_buffer_topic(h8_9)
no_ph_change_computation(h8_9)
no_derivation_task(h8_9)
h.run(h8_9, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
