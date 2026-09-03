"""Key audit for AP CHEMISTRY 7.11 Introduction to Solubility Equilibria.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  7.11.A.1  dissolution is a reversible process described by Ksp   1, 18, 26
  7.11.A.2  solubility is calculable from Ksp, and relative solubility
            predictable from it                       3, 4, 8, 11, 12, 15, 19,
                                                      21, 22, 24, 25, 30
  7.11.A.3  Ksp greater than one marks a soluble salt  10, 23, 27
  7.11.A.4  molar solubility gives Ksp                 5, 9, 13, 14, 16, 17, 20, 28
  the form of the expression itself                    2, 6, 7, 29

THE ONE PLACE THIS TOPIC CAN TEACH SOMETHING FALSE. EK 7.11.A.2 licenses
predicting relative solubility from Ksp, and the shortcut "larger Ksp means
more soluble" holds only between salts of the same formula type. Item 19 pairs
a one-to-one salt of larger Ksp against a one-to-two salt of smaller Ksp, and
``n19`` recomputes BOTH solubilities and asserts the shortcut fails on them;
item 25 states the limitation and item 12 states the condition under which the
comparison is sound. If any of those three ever contradicts the arithmetic,
this file fails.

ARITHMETIC. Every solubility and every Ksp is recomputed from the stated value
alone, through two solvers written once at the top so an error cannot look like
a different rule:

    ``s_from_ksp(ksp, kind)``   kind 1 gives sqrt(Ksp); kind 2 gives cbrt(Ksp/4)
    ``ksp_from_s(s, kind)``     the inverse of each

The tables carry their Ksp values as hand-written math spans, because a student
should read scientific notation rather than a row of zeros; ``sci`` parses a
span back to a float, so the checks still read the table rather than a constant
retyped here.

NEGATIVE CONTROL: ``python3 verify_h7_11.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h7_11

KSP = "Ksp at 298 K"
SOL = "Molar solubility in pure water (M)"

_SCI = re.compile(
    r"\\\(\s*(-?\d+(?:\.\d+)?)\s*(?:\\times\s*10\^\{(-?\d+)\})?\s*\\\)")


def sci(cell):
    """Parse a hand-written span such as ``\\( 1.8 \\times 10^{-10} \\)``."""
    m = _SCI.fullmatch(str(cell).strip())
    assert m, f"cell {cell!r} is not a parseable math span"
    mantissa = float(m.group(1))
    return mantissa * (10.0 ** int(m.group(2)) if m.group(2) else 1.0)


def sci_col(table, header):
    j = [cg.normalize(x) for x in table["headers"]].index(cg.normalize(header))
    return {str(r[0]): sci(r[j]) for r in table["rows"]}


def s_from_ksp(ksp, kind):
    """Molar solubility from Ksp. kind 1 is one-to-one, kind 2 is one-to-two."""
    if kind == 1:
        s = math.sqrt(ksp)
    elif kind == 2:
        s = (ksp / 4.0) ** (1.0 / 3.0)
    else:
        raise AssertionError(f"unknown formula type {kind}")
    assert abs(ksp_from_s(s, kind) - ksp) / ksp < 1e-9, "the two solvers disagree"
    return s


def ksp_from_s(s, kind):
    return s * s if kind == 1 else 4.0 * s ** 3


# ------------------------------------------------------------------ table items

def q11(table, item):
    ks = sci_col(table, KSP)
    least = min(ks, key=ks.get)
    assert least == "AgI", f"the smallest tabulated constant belongs to {least}"
    sols = {lab: s_from_ksp(v, 1) for lab, v in ks.items()}
    assert min(sols, key=sols.get) == "AgI", f"recomputed solubilities are {sols}"
    h.shows(item, "AgI")
    return (f"the tabulated constants {ks} give solubilities {sols}, whose minimum is "
            f"{least}")


def q12(table, item):
    ions = {str(r[0]): str(r[1]) for r in table["rows"]}
    assert len(set(ions.values())) == 1 or all("one silver ion and one" in v
                                               for v in ions.values()), \
        f"the three salts must share a formula type for the ranking to carry over: {ions}"
    h.shows(item, "same number of ions per formula unit")
    return ("every tabulated salt releases one cation and one anion, so the same "
            "function of Ksp gives each solubility")


def q13(table, item):
    s = cg.cell(table, "Salt J", SOL)
    k = ksp_from_s(s, 1)
    assert abs(k - 1.0e-6) < 1e-15, f"Ksp for salt J recomputes to {k}"
    h.shows(item, "1.0 \\times 10^{-6}")
    return f"the tabulated solubility {s:g} squared recomputes Ksp as {k:g}"


def q14(table, item):
    s = cg.cell(table, "Salt L", SOL)
    k = ksp_from_s(s, 2)
    assert abs(k - 4.0e-9) < 1e-18, f"Ksp for salt L recomputes to {k}"
    assert cg.cell(table, "Salt J", SOL) == s, \
        "salts J and L must share a solubility, which is the point of the pair"
    h.shows(item, "4.0 \\times 10^{-9}")
    return (f"four times the cube of the tabulated {s:g} recomputes Ksp as {k:g}, "
            "against a different value for the same solubility in salt J")


def q15(table, item):
    kj = ksp_from_s(cg.cell(table, "Salt J", SOL), 1)
    kl = ksp_from_s(cg.cell(table, "Salt L", SOL), 2)
    assert cg.cell(table, "Salt J", SOL) == cg.cell(table, "Salt L", SOL)
    assert abs(kj - kl) > 1e-12, f"the two constants must differ: {kj} and {kl}"
    h.shows(item, "depends on how many ions the formula unit releases")
    return (f"equal tabulated solubilities give constants {kj:g} and {kl:g}, which "
            "differ only through the formula type")


def q16(table, item):
    ks = {"Salt J": ksp_from_s(cg.cell(table, "Salt J", SOL), 1),
          "Salt L": ksp_from_s(cg.cell(table, "Salt L", SOL), 2),
          "Salt M": ksp_from_s(cg.cell(table, "Salt M", SOL), 1)}
    largest = max(ks, key=ks.get)
    assert largest == "Salt M", f"the largest recomputed constant belongs to {largest}"
    h.shows(item, "Salt M")
    return f"the three recomputed constants are {ks}, whose maximum is {largest}"


def q21(table, item):
    ks = sci_col(table, KSP)
    s = s_from_ksp(ks["Salt P"], 1)
    assert abs(s - 1.0e-4) < 1e-12, f"the solubility of salt P recomputes to {s}"
    h.shows(item, "0.00010 M")
    return f"the square root of the tabulated {ks['Salt P']:g} recomputes the solubility as {s:g}"


def q22(table, item):
    ks = sci_col(table, KSP)
    s = s_from_ksp(ks["Salt R"], 2)
    assert abs(s - 1.0e-3) < 1e-12, f"the solubility of salt R recomputes to {s}"
    wrong = math.sqrt(ks["Salt R"])
    assert abs(wrong - 6.32e-5) < 1e-6, "the 0.000063 distractor must be the square root"
    h.shows(item, "0.0010 M")
    return (f"the cube root of a quarter of {ks['Salt R']:g} recomputes the solubility as "
            f"{s:g}, against {wrong:.2g} for a square root")


def q23(table, item):
    ks = sci_col(table, KSP)
    soluble = [lab for lab, v in ks.items() if v > 1.0]
    assert soluble == ["Salt T"], f"tabulated constants above one: {soluble}"
    h.shows(item, "Salt T")
    return f"of the tabulated constants {ks}, exactly one exceeds one"


TABLE_CHECKS = {11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                21: q21, 22: q22, 23: q23}


# ---------------------------------------------------------------- stem numerics

def n3(item):
    s = s_from_ksp(4.0e-10, 1)
    assert abs(s - 2.0e-5) < 1e-12, f"solubility recomputes to {s}"
    h.shows(item, "2.0 \\times 10^{-5}")
    return f"the square root of 4.0 times ten to the minus ten recomputes as {s:g}"


def n4(item):
    s = s_from_ksp(9.0e-12, 1)
    assert abs(s - 3.0e-6) < 1e-14, f"solubility recomputes to {s}"
    h.shows(item, "3.0 \\times 10^{-6}")
    return f"the square root of 9.0 times ten to the minus twelve recomputes as {s:g}"


def n5(item):
    k = ksp_from_s(1.0e-4, 1)
    assert abs(k - 1.0e-8) < 1e-18, f"Ksp recomputes to {k}"
    h.shows(item, "1.0 \\times 10^{-8}")
    return f"the square of ten to the minus four recomputes Ksp as {k:g}"


def n8(item):
    s = s_from_ksp(3.2e-11, 2)
    assert abs(s - 2.0e-4) < 1e-12, f"solubility recomputes to {s}"
    root = math.sqrt(3.2e-11)
    assert abs(root - 5.66e-6) < 1e-7, "the 5.7 distractor must be the square root"
    h.shows(item, "2.0 \\times 10^{-4}")
    return f"the cube root of a quarter of 3.2 times ten to the minus eleven is {s:g}"


def n9(item):
    k = ksp_from_s(2.0e-3, 2)
    assert abs(k - 3.2e-8) < 1e-16, f"Ksp recomputes to {k}"
    assert abs((2.0e-3) ** 3 - 8.0e-9) < 1e-18, "the 8.0 distractor must omit the four"
    h.shows(item, "3.2 \\times 10^{-8}")
    return f"four times the cube of 2.0 times ten to the minus three recomputes Ksp as {k:g}"


def n17(item):
    k = ksp_from_s(5.0e-5, 1)
    assert abs(k - 2.5e-9) < 1e-18, f"Ksp recomputes to {k}"
    h.shows(item, "2.5 \\times 10^{-9}")
    return f"the square of 5.0 times ten to the minus five recomputes Ksp as {k:g}"


def n19(item):
    """The whole point of the item: the naive Ksp shortcut FAILS on this pair."""
    kv, kw = 1.0e-10, 4.0e-12
    sv, sw = s_from_ksp(kv, 1), s_from_ksp(kw, 2)
    assert kv > kw, "salt V must hold the larger constant"
    assert sw > sv, f"salt W must be the more soluble: {sw} against {sv}"
    assert abs(sw / sv - 10.0) < 1e-6, f"the ratio of solubilities recomputes to {sw / sv}"
    h.shows(item, "Salt W, even though its constant is the smaller")
    return (f"the larger constant {kv:g} gives solubility {sv:g} while the smaller "
            f"{kw:g} gives {sw:g}, so the shortcut fails by a factor of ten")


def n20(item):
    anion = 4.0e-3
    s = anion / 2.0
    assert abs(s - 2.0e-3) < 1e-12, f"solubility recomputes to {s}"
    h.shows(item, "2.0 \\times 10^{-3}")
    return f"an anion concentration of {anion:g} at two per formula unit gives {s:g}"


def n24(item):
    ratio = math.sqrt(100.0)
    assert abs(ratio - 10.0) < 1e-9, f"the solubility ratio recomputes to {ratio}"
    h.shows(item, "The first is ten times as soluble")
    return f"a hundredfold ratio of constants gives a {ratio:g}-fold ratio of solubilities"


def n27(item):
    ksp = 2.5e-1
    assert ksp < 1.0, f"the stated constant is {ksp}, which must be below one"
    h.shows(item, "sparingly soluble, since the constant is below one")
    return f"the stated constant {ksp:g} lies below the value of one that EK 7.11.A.3 names"


NUMERIC = {3: n3, 4: n4, 5: n5, 8: n8, 9: n9, 17: n17, 19: n19, 20: n20,
           24: n24, 27: n27}


CLAIMS = [
 ("reversible process whose extent is described by the solubility-product",
  "EK 7.11.A.1, verbatim in substance: the dissolution of a salt is a reversible process whose extent can be described by Ksp, the solubility-product constant."),
 ("K_{sp} = [\\mathrm{Pb^{2+}}][\\mathrm{I^-}]^{2}",
  "The dissolution equation releases one lead ion and two iodide ions, so each concentration is raised to its own coefficient, and the pure solid is omitted because its concentration does not depend on how much is present."),
 ("2.0 \\times 10^{-5}",
  "EK 7.11.A.2: the solubility is calculable from Ksp. Recomputed in n3 for a one-to-one salt, where Ksp is the square of the solubility."),
 ("3.0 \\times 10^{-6}",
  "EK 7.11.A.2 on a second one-to-one salt, so the answer cannot be carried over from the previous item. Recomputed in n4."),
 ("1.0 \\times 10^{-8}",
  "EK 7.11.A.4: the molar solubility in a saturated solution can be used to calculate Ksp. Recomputed in n5."),
 ("K_{sp} = [\\mathrm{Ca^{2+}}]^{3}[\\mathrm{PO_4^{3-}}]^{2}",
  "Three calcium ions and two phosphate ions are released per formula unit, so each concentration carries its own coefficient as an exponent. The ionic charges set the formula rather than the exponents."),
 ("4s^{3}",
  "For a salt releasing one cation and two anions, dissolving s gives s of the cation and twice s of the anion, so the product is s times the square of two s."),
 ("2.0 \\times 10^{-4}",
  "EK 7.11.A.2 for a one-to-two salt, where the solubility is the cube root of a quarter of Ksp. Recomputed in n8 against the square-root distractor."),
 ("3.2 \\times 10^{-8}",
  "EK 7.11.A.4 for a one-to-two salt. Recomputed in n9, which also recomputes the value obtained by omitting the factor of four."),
 ("greater than one",
  "EK 7.11.A.3, verbatim in substance: the solubility rules can be quantitatively related to Ksp, in which Ksp values greater than one correspond to soluble salts."),
 ("AgI",
  "EK 7.11.A.2 licenses ranking relative solubility from Ksp where the formula type is shared. Both the constants and the recomputed solubilities are ranked in q11."),
 ("same number of ions per formula unit",
  "EK 7.11.A.2 relates solubility to Ksp through the stoichiometry of the dissolution, so a ranking by Ksp carries over to solubility only when that stoichiometry is shared. The shared type is checked in q12."),
 ("1.0 \\times 10^{-6}",
  "EK 7.11.A.4 applied to the tabulated solubility of a one-to-one salt. Recomputed in q13."),
 ("4.0 \\times 10^{-9}",
  "EK 7.11.A.4 applied to the tabulated solubility of a one-to-two salt. Recomputed in q14, which also confirms the two salts share a solubility."),
 ("depends on how many ions the formula unit releases",
  "EK 7.11.A.2 routes the relationship between Ksp and solubility through the dissolution stoichiometry. The two constants are recomputed from equal tabulated solubilities in q15 and differ."),
 ("Salt M",
  "EK 7.11.A.4 across three salts of two formula types, so the constants must be computed rather than read off the solubilities. Recomputed in q16."),
 ("2.5 \\times 10^{-9}",
  "EK 7.11.A.4 from a measured ion concentration in a saturated solution. Recomputed in n17."),
 ("concentration that does not depend on how much of it is present",
  "An equilibrium expression omits a species whose concentration is fixed however much is present, which is why the undissolved solid does not appear in the constant EK 7.11.A.1 defines."),
 ("Salt W, even though its constant is the smaller",
  "EK 7.11.A.2 makes solubility calculable from Ksp through the stoichiometry, so the shortcut of ranking by Ksp fails across formula types. Both solubilities are recomputed in n19 and the failure is asserted there."),
 ("2.0 \\times 10^{-3}",
  "EK 7.11.A.4 says the molar solubility of ONE OR MORE species can be used, and the balanced equation converts an anion concentration into the solubility. Recomputed in n20."),
 ("0.00010 M",
  "EK 7.11.A.2 for a one-to-one salt, from the tabulated constant. Recomputed in q21."),
 ("0.0010 M",
  "EK 7.11.A.2 for a one-to-two salt, from the tabulated constant. Recomputed in q22 against the square-root distractor."),
 ("Salt T",
  "EK 7.11.A.3 makes a constant above one the mark of a soluble salt. The tabulated constants are compared against one in q23."),
 ("The first is ten times as soluble",
  "EK 7.11.A.2 makes the solubility of a one-to-one salt the square root of Ksp, so a ratio of constants is not the ratio of solubilities. Recomputed in n24."),
 ("salt releasing more ions can be more soluble",
  "EK 7.11.A.2 relates the two quantities through the dissolution stoichiometry, so a ranking on constants alone can invert the true order; item 19's pair is the worked case, recomputed in n19."),
 ("Nothing measurable changes",
  "EK 7.11.A.1 fixes the extent of dissolution by Ksp at a given temperature, and a saturated solution already satisfies it. A pure solid's concentration does not enter the expression, so adding more changes nothing."),
 ("sparingly soluble, since the constant is below one",
  "EK 7.11.A.3 sets the dividing line at one rather than at zero. Recomputed in n27 against the stated value."),
 ("stoichiometry of the dissolution fixes the ratio",
  "EK 7.11.A.4 allows the molar solubility of one or more species to be used, and the balanced equation supplies the ratio that converts one ion concentration into the solubility."),
 ("4s^{3}",
  "For a salt releasing two cations and one anion, the cation term is squared and the anion term is not, so the product is the square of two s multiplied by s."),
 ("larger at the higher temperature",
  "EK 7.11.A.2 makes solubility an increasing function of Ksp for a fixed formula type, and comparing one salt with itself holds the formula type fixed, which is the case where reading Ksp directly is sound."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[10]["table"] = dict(
            headers=h7_11._T_ONE_TO_ONE["headers"],
            rows=[[lab, ions, ("\\( 9.9 \\times 10^{-2} \\)" if lab == "AgI" else k)]
                  for lab, ions, k in h7_11._T_ONE_TO_ONE["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[2]["choices"])
        ch[0] = "\\( 2.0 \\times 10^{-6} \\) M"
        mod.QUESTIONS[2]["choices"] = ch
        cl[2] = ("2.0 \\times 10^{-6}", cl[2][1])

    def break_the_trap(mod, cl):
        # If item 19's pair ever stopped falsifying the naive Ksp shortcut, the
        # item would be teaching the shortcut instead of its limit.
        ch = list(mod.QUESTIONS[18]["choices"])
        ch[0] = "Salt W, because its constant is the larger of the two"
        mod.QUESTIONS[18]["choices"] = ch
        cl[18] = ("Salt W, because its constant is the larger", cl[18][1])

    return [("a tabulated constant corrupted so the least soluble salt changes", corrupt_table),
            ("a recomputed solubility no longer in the keyed choice", corrupt_numeric),
            ("item 19 rewritten so it no longer states the limit it exists to state",
             break_the_trap)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h.run(h7_11, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
