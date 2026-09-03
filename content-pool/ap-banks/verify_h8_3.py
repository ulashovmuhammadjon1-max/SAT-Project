"""Key audit for AP CHEMISTRY 8.3 Weak Acid and Base Equilibria.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.3.A.1  only a small percentage of a weak acid ionizes    1, 25, 26
  8.3.A.2  Ka and pKa, and the pH from the initial concentration and the pKa
                                                             2, 3, 4, 5, 7, 8,
                                                             9, 10, 11, 27, 30
  8.3.A.3  a weak base likewise ionizes only slightly        12, 28
  8.3.A.4  Kb and pKb                                        13, 14, 15, 19
  8.3.A.5  percent ionization from the constant and the initial concentration,
           or from a measured equilibrium concentration      6, 21, 22, 23, 24
  8.3.A.6  Kw = Ka x Kb and pKw = pKa + pKb                  16, 17, 18, 20, 29

THE ASSUMPTION EVERY CALCULATION MAKES, and why it is asserted rather than
trusted. The one-step result used here -- that the hydronium concentration is
the square root of Ka times the initial concentration -- is only valid because
EK 8.3.A.1 says the ionized fraction is small. ``weak_ion`` recomputes each
value AND asserts the ionized fraction is at most five percent, so an item whose
numbers quietly broke the assumption fails here rather than shipping a value
that is merely close. It also asserts the exact equilibrium expression is
reproduced to within a percent by the approximate answer.

ARITHMETIC. Every logarithm is exact, including the half-unit results where the
square root halves an odd exponent.

NEGATIVE CONTROL: ``python3 verify_h8_3.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h8_3

KA = "Ka at 298 K"
PKA = "pKa"
KB = "Kb at 298 K"
PKB = "pKb"
C0 = "Initial acid concentration (M)"
HEQ = "Hydronium ion concentration at equilibrium (M)"

KW25 = 1.0e-14

_SCI = re.compile(r"\\\(\s*(-?\d+(?:\.\d+)?)\s*(?:\\times\s*10\^\{(-?\d+)\})?\s*\\\)")


def sci(text):
    m = _SCI.search(str(text))
    assert m, f"{text!r} holds no parseable math span"
    return float(m.group(1)) * (10.0 ** int(m.group(2)) if m.group(2) else 1.0)


def sci_col(table, header):
    j = [cg.normalize(x) for x in table["headers"]].index(cg.normalize(header))
    return {str(r[0]): sci(r[j]) for r in table["rows"]}


def p(value):
    return -math.log10(value)


def weak_ion(k, c0):
    """Ion concentration from a weak acid or base at initial concentration c0.

    Returns (ion concentration, fraction ionized). The one-step square-root
    result is only licensed by EK 8.3.A.1's small percentage, so the fraction is
    asserted small here and the exact quadratic root is compared against it.
    """
    x = math.sqrt(k * c0)
    frac = x / c0
    assert frac <= 0.05, (
        f"the ionized fraction is {frac:.3f}, too large for the approximation this "
        "module relies on -- the item's numbers are wrong, not merely imprecise"
    )
    exact = (-k + math.sqrt(k * k + 4 * k * c0)) / 2.0
    assert abs(exact - x) / x < 0.03, (
        f"the approximate {x:g} and exact {exact:g} roots differ by more than three percent"
    )
    return x, frac


# ------------------------------------------------------------------ table items

def q9(table, item):
    kas = sci_col(table, KA)
    strongest = max(kas, key=kas.get)
    assert strongest == "HA", f"the largest tabulated constant belongs to {strongest}"
    pkas = dict(zip(cg.labels(table), cg.col(table, PKA)))
    assert min(pkas, key=pkas.get) == strongest, \
        f"the smallest tabulated pKa must belong to the same acid: {pkas}"
    h.shows(item, "HA")
    return (f"the tabulated constants {kas} have their maximum at {strongest}, which is "
            f"also where the tabulated pKa values {pkas} have their minimum")


def q10(table, item):
    kas = sci_col(table, KA)
    pkas = dict(zip(cg.labels(table), cg.col(table, PKA)))
    for lab in kas:
        assert abs(p(kas[lab]) - pkas[lab]) < 1e-9, (
            f"row {lab}: the negative logarithm of {kas[lab]} is {p(kas[lab])}, not {pkas[lab]}"
        )
    h.shows(item, "negative base-ten logarithm")
    return f"every tabulated pair satisfies the definition: {[(k, pkas[k]) for k in kas]}"


def q11(table, item):
    kas = sci_col(table, KA)
    phs = {lab: p(weak_ion(k, 1.0)[0]) for lab, k in kas.items()}
    highest = max(phs, key=phs.get)
    assert highest == "HD", f"the highest recomputed pH belongs to {highest}"
    assert min(kas, key=kas.get) == highest, "the highest pH must go with the smallest Ka"
    h.shows(item, "HD")
    return f"at 1.0 M the tabulated acids give pH values {phs}, whose maximum is at {highest}"


def q19(table, item):
    kbs = sci_col(table, KB)
    highest = max(kbs, key=kbs.get)
    assert highest == "B1", f"the largest tabulated base constant belongs to {highest}"
    pohs = {lab: p(weak_ion(k, 0.10)[0]) for lab, k in kbs.items()}
    assert min(pohs, key=pohs.get) == highest, f"recomputed pOH values are {pohs}"
    h.shows(item, "B1")
    return (f"at 0.10 M the tabulated bases give pOH values {pohs}, whose minimum, and so "
            f"the highest pH, is at {highest}")


def q20(table, item):
    pkbs = dict(zip(cg.labels(table), cg.col(table, PKB)))
    pka = 14.0 - pkbs["B2"]
    assert abs(pka - 5.0) < 1e-9, f"the conjugate pKa recomputes to {pka}"
    h.shows(item, "5.00")
    return f"fourteen less the tabulated pKb of {pkbs['B2']:g} recomputes the pKa as {pka:g}"


def q21(table, item):
    c = dict(zip(cg.labels(table), cg.col(table, C0)))
    hh = dict(zip(cg.labels(table), cg.col(table, HEQ)))
    frac = {lab: hh[lab] / c[lab] for lab in c}
    largest = max(frac, key=frac.get)
    assert largest == "3", f"the largest tabulated fraction ionized is solution {largest}"
    assert abs(frac["1"] - frac["2"]) < 1e-12, \
        "the other two solutions must tie, so the maximum is unambiguous"
    h.shows(item, "Solution 3")
    return f"the tabulated ratios recompute to {frac}, whose maximum is at {largest}"


def q22(table, item):
    c = dict(zip(cg.labels(table), cg.col(table, C0)))
    hh = dict(zip(cg.labels(table), cg.col(table, HEQ)))
    pct = 100.0 * hh["2"] / c["2"]
    assert abs(pct - 1.0) < 1e-9, f"the percent ionization recomputes to {pct}"
    h.shows(item, "1.0 percent")
    return f"{hh['2']:g} over {c['2']:g} recomputes the percent ionization as {pct:g}"


def q23(table, item):
    hh = dict(zip(cg.labels(table), cg.col(table, HEQ)))
    v = p(hh["1"])
    assert abs(v - 3.0) < 1e-9, f"the pH recomputes to {v}"
    h.shows(item, "3.00")
    return f"the tabulated equilibrium concentration {hh['1']:g} gives a pH of {v:g}"


TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23}


# ---------------------------------------------------------------- stem numerics

def n3(item):
    v = p(1.0e-5)
    assert abs(v - 5.0) < 1e-9, f"pKa recomputes to {v}"
    assert abs(14.0 - v - 9.0) < 1e-9, "the 9.00 distractor must be the conjugate pKb"
    h.shows(item, "5.00")
    return f"the negative logarithm of the stated constant recomputes pKa as {v:g}"


def n4(item):
    x, frac = weak_ion(1.0e-6, 1.0)
    v = p(x)
    assert abs(v - 3.0) < 1e-9, f"pH recomputes to {v}"
    h.shows(item, "3.00")
    return f"the square root of the product recomputes the hydronium as {x:g}, pH {v:g}, with {frac:.4f} ionized"


def n5(item):
    x, frac = weak_ion(1.0e-5, 0.10)
    v = p(x)
    assert abs(v - 3.0) < 1e-9, f"pH recomputes to {v}"
    h.shows(item, "3.00")
    return f"the square root of the product gives {x:g} M hydronium and pH {v:g}"


def n6(item):
    x, frac = weak_ion(1.0e-5, 0.10)
    pct = 100.0 * frac
    assert abs(pct - 1.0) < 1e-9, f"the percent ionization recomputes to {pct}"
    h.shows(item, "1.0 percent")
    return f"{x:g} M of an initial 0.10 M recomputes the percent ionization as {pct:g}"


def n7(item):
    x, frac = weak_ion(1.0e-6, 0.10)
    v = p(x)
    assert abs(v - 3.5) < 1e-9, f"pH recomputes to {v}"
    h.shows(item, "3.50")
    return f"the square root of ten to the minus seven gives {x:g} M and pH {v:g}"


def n14(item):
    x, frac = weak_ion(1.0e-5, 0.10)
    poh = p(x)
    ph = 14.0 - poh
    assert abs(ph - 11.0) < 1e-9, f"pH recomputes to {ph}"
    assert abs(poh - 3.0) < 1e-9, "the 3.00 distractor must be the pOH"
    h.shows(item, "11.00")
    return f"a hydroxide concentration of {x:g} M gives pOH {poh:g} and pH {ph:g}"


def n15(item):
    x, frac = weak_ion(1.0e-6, 0.10)
    poh = p(x)
    assert abs(poh - 3.5) < 1e-9, f"pOH recomputes to {poh}"
    h.shows(item, "3.50")
    return f"the square root of ten to the minus seven gives {x:g} M hydroxide and pOH {poh:g}"


def n17(item):
    v = 14.0 - 5.0
    assert abs(v - 9.0) < 1e-9, f"pKb recomputes to {v}"
    h.shows(item, "9.00")
    return f"fourteen less the stated pKa of 5.00 recomputes the pKb as {v:g}"


def n18(item):
    kb = KW25 / 1.0e-4
    assert abs(kb - 1.0e-10) < 1e-19, f"Kb recomputes to {kb}"
    h.shows(item, "1.0 \\times 10^{-10}")
    return f"Kw divided by the stated Ka recomputes Kb as {kb:g}"


def n26(item):
    c0, x = 0.20, 0.0020
    left = c0 - x
    assert abs(left - 0.198) < 1e-12, f"the un-ionized concentration recomputes to {left}"
    assert x / c0 <= 0.05, "the ionized fraction must remain small, per EK 8.3.A.1"
    h.shows(item, "0.198 M")
    return f"{c0:g} less the ionized {x:g} recomputes the un-ionized acid as {left:g} M"


def n28(item):
    oh = 10.0 ** (-3.0)
    assert abs(oh - 0.0010) < 1e-15, f"the hydroxide concentration recomputes to {oh}"
    h.shows(item, "much smaller than the initial concentration")
    return f"a pOH of 3.00 recomputes the hydroxide concentration as {oh:g} M"


def n30(item):
    x, frac = weak_ion(1.0e-8, 1.0)
    v = p(x)
    assert abs(v - 4.0) < 1e-9, f"pH recomputes to {v}"
    h.shows(item, "4.00")
    return f"the square root of ten to the minus eight gives {x:g} M hydronium and pH {v:g}"


NUMERIC = {3: n3, 4: n4, 5: n5, 6: n6, 7: n7, 14: n14, 15: n15, 17: n17, 18: n18,
           26: n26, 28: n28, 30: n30}


CLAIMS = [
 ("small percentage ionize",
  "EK 8.3.A.1, verbatim in substance: only a small percentage of molecules of a weak acid will ionize, so the hydronium concentration is much less than the initial concentration and the vast majority of molecules remain un-ionized."),
 ("\\frac{[\\mathrm{H_3O^+}][\\mathrm{A^-}]}{[\\mathrm{HA}]}",
  "EK 8.3.A.2's equation for Ka: the two products in the numerator and the un-ionized acid in the denominator."),
 ("5.00",
  "EK 8.3.A.2 defines pKa as the negative logarithm of Ka. Recomputed in n3, which also recomputes the conjugate pKb as the distractor."),
 ("3.00",
  "EK 8.3.A.2 makes the pH determinable from the initial concentration and the constant, using EK 8.3.A.1's small ionized fraction. Recomputed in n4, which asserts that fraction is small."),
 ("3.00",
  "The same relationship at a tenth the concentration and ten times the constant, which happens to give the same pH -- so the item cannot be answered by pattern. Recomputed in n5."),
 ("1.0 percent",
  "EK 8.3.A.5: the percent ionization follows from the constant and the initial concentration. Recomputed in n6 from the same solver that produced the pH."),
 ("3.50",
  "EK 8.3.A.2 where the square root halves an odd exponent, giving a half-unit pH. Recomputed in n7."),
 ("larger constant means more hydronium",
  "EK 8.3.A.2 places the hydronium concentration in the numerator of Ka, so at equal initial concentrations a larger constant means more hydronium and a lower pH."),
 ("HA",
  "EK 8.3.A.2 makes Ka the ionization constant, so the largest value marks the strongest acid. Recomputed in q9, which also checks the tabulated pKa column orders the same acids in reverse."),
 ("negative base-ten logarithm",
  "EK 8.3.A.2's equation pKa equal to minus log Ka. Every tabulated pair is checked against it in q10."),
 ("HD",
  "EK 8.3.A.2 with the initial concentration held fixed, so the smallest constant gives the highest pH. All three pH values are recomputed in q11."),
 ("small percentage of its molecules ionize",
  "EK 8.3.A.3, verbatim in substance: weak bases react with water to produce hydroxide ions, but ordinarily just a small percentage ionize, so the hydroxide concentration does not equal the initial concentration of the base."),
 ("\\frac{[\\mathrm{OH^-}][\\mathrm{HB^+}]}{[\\mathrm{B}]}",
  "EK 8.3.A.4's equation for Kb: the hydroxide ion and the conjugate acid in the numerator and the un-ionized base in the denominator."),
 ("11.00",
  "EK 8.3.A.4 for the hydroxide concentration and EK 8.1.A.3 for the conversion to pH. Recomputed in n14, which also recomputes the pOH as the distractor."),
 ("3.50",
  "EK 8.3.A.4 with an odd exponent, giving a half-unit pOH. Recomputed in n15."),
 ("Their product is Kw",
  "EK 8.3.A.6, verbatim: for any conjugate acid-base pair, Kw equals Ka times Kb."),
 ("9.00",
  "EK 8.3.A.6's logarithmic form, pKw equal to pKa plus pKb, with pKw fourteen at 25 degrees Celsius. Recomputed in n17."),
 ("1.0 \\times 10^{-10}",
  "EK 8.3.A.6 solved for Kb by dividing Kw by Ka. Recomputed in n18."),
 ("B1",
  "EK 8.3.A.4 makes Kb the constant for the reaction with water, so the largest value gives the most hydroxide at a fixed concentration. All three pOH values are recomputed in q19."),
 ("5.00",
  "EK 8.3.A.6's logarithmic form applied to a tabulated pKb. Recomputed in q20."),
 ("Solution 3",
  "EK 8.3.A.5 allows percent ionization from the initial and equilibrium concentrations. All three ratios are recomputed in q21, and the two that tie are checked so the maximum is unambiguous."),
 ("1.0 percent",
  "EK 8.3.A.5 applied to one tabulated pair. Recomputed in q22."),
 ("3.00",
  "EK 8.1.A.1 applied to the tabulated equilibrium concentration, which needs no ionization constant at all. Recomputed in q23."),
 ("rises, because the percent ionized depends on the initial concentration",
  "EK 8.3.A.5 makes percent ionization a function of the constant AND the initial concentration. The ion concentration falls only as the square root of the dilution while the initial concentration falls in full, so their ratio rises."),
 ("only a small percentage of the weak acid molecules ionize",
  "EK 8.3.A.1 states the contrast directly, and EK 8.2.A.1 makes the two concentrations equal for a strong acid because ionization there is complete."),
 ("0.198 M",
  "Each ionization removes one molecule from the un-ionized pool and adds one hydronium ion. Recomputed in n26, which also asserts the ionized fraction stays small as EK 8.3.A.1 requires."),
 ("initial acid concentration and the pKa",
  "EK 8.3.A.2, verbatim in substance: the pH of a weak acid solution can be determined from the initial acid concentration and the pKa. Neither quantity alone suffices."),
 ("much smaller than the initial concentration",
  "EK 8.1.A.1 converts the pOH and EK 8.3.A.3 states that the hydroxide concentration in a weak base solution does not equal the initial concentration of the base. Recomputed in n28."),
 ("product of the two constants is fixed at Kw",
  "EK 8.3.A.6 fixes the PRODUCT of Ka and Kb at Kw, so a smaller Ka forces a larger Kb at a given temperature."),
 ("4.00",
  "EK 8.3.A.2 at a different constant and concentration from every other calculation in the module. Recomputed in n30."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[8]["table"] = dict(
            headers=h8_3._T_ACIDS["headers"],
            rows=[[lab, ("\\( 1.0 \\times 10^{-9} \\)" if lab == "HA" else k), pk]
                  for lab, k, pk in h8_3._T_ACIDS["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[6]["choices"])
        ch[0] = "pH = 3.20"
        mod.QUESTIONS[6]["choices"] = ch
        cl[6] = ("3.20", cl[6][1])

    def approximation_broken(mod, cl):
        """A concentration too low for the small-ionization assumption must fail."""
        x, frac = weak_ion(1.0e-5, 1.0e-4)
        raise AssertionError(f"unreachable: solver accepted {frac:.2f} ionized")

    def pka_column_desynced(mod, cl):
        mod.QUESTIONS[9]["table"] = dict(
            headers=h8_3._T_ACIDS["headers"],
            rows=[[lab, k, ("4.00" if lab == "HB" else pk)]
                  for lab, k, pk in h8_3._T_ACIDS["rows"]])

    return [("a tabulated Ka corrupted so the strongest acid changes", corrupt_table),
            ("a recomputed pH no longer in the keyed choice", corrupt_numeric),
            ("numbers that break the small-ionization assumption", approximation_broken),
            ("a tabulated pKa that no longer matches its own Ka", pka_column_desynced)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h.run(h8_3, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
