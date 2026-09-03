"""Key audit for AP CHEMISTRY 8.2 pH and pOH of Strong Acids and Bases.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.2.A.1  a strong acid ionizes COMPLETELY, so [H3O+] equals the stated acid
           concentration                     1, 2, 3, 4, 8, 9, 10, 11, 15, 18,
                                             19, 21, 22, 27, 28, 30
  8.2.A.2  a strong base dissociates completely, so [OH-] equals the stated
           concentration for a GROUP I hydroxide and DOUBLE it for a GROUP II
           hydroxide                         5, 6, 7, 12, 13, 14, 16, 17, 20,
                                             23, 24, 25, 26, 29, 30

THE FACTOR OF TWO IS THE TOPIC. ``group_rule`` below is the only place the rule
is written, and every calculation goes through it, so an item that quietly
forgot to double could not pass. Each base item also states its group in the
stem or the table, so no key depends on remembering which block a metal sits in.

H2SO4 IS DELIBERATELY ABSENT FROM EVERY CALCULATION. The framework lists it as a
strong acid but only its first ionization is complete, and the framework says
nothing about the second. ``no_sulfuric_arithmetic`` asserts it appears in no
item that computes a pH, so the bank cannot ship a value resting on an
assumption the CED does not make.

ARITHMETIC. Every logarithm is exact, including after the doubling. Recomputed
in TABLE_CHECKS for the nine items carrying a table and in NUMERIC for the
thirteen whose numbers are in the stem.

NEGATIVE CONTROL: ``python3 verify_h8_2.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h8_2

CONC = "Initial concentration (M)"
SOLUTE = "Solute"
GROUP = "Group of the metal"

KW25 = 1.0e-14

# Explicit lookarounds, never \b: the formula abuts a digit at its end.
_SULFURIC = re.compile(r"(?<![A-Za-z0-9])H2SO4(?![A-Za-z0-9])")
_COMPUTES_PH = re.compile(r"(?<![A-Za-z])p(?:H|OH)\s*=\s*\d")


def no_sulfuric_arithmetic(module):
    """H2SO4 may be identified but never used in a computed pH."""
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(c) for r in t["rows"] for c in r]
        if any(_SULFURIC.search(x) for x in texts):
            assert not any(_COMPUTES_PH.search(x) for x in texts), (
                f"{module.TOPIC[0]} q{i}: names H2SO4 in an item that computes a pH; only "
                "its first ionization is complete and the framework does not treat the "
                "second, so no such value may be shipped"
            )
    print(f"OK  {module.TOPIC[0]} scope: H2SO4 appears in no item that computes a pH.")


def p(value):
    return -math.log10(value)


def group_rule(conc, group):
    """[OH-] from the stated concentration -- EK 8.2.A.2's asymmetry, written once."""
    g = cg.normalize(group)
    if g in ("group i", "i", "1"):
        return conc
    if g in ("group ii", "ii", "2"):
        return 2.0 * conc
    raise AssertionError(f"unknown group {group!r}")


# ------------------------------------------------------------------ table items

def q9(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CONC)))
    lowest = max(conc, key=conc.get)          # largest [H3O+] gives lowest pH
    assert lowest == "3", f"the largest tabulated concentration is solution {lowest}"
    phs = {lab: p(c) for lab, c in conc.items()}
    assert min(phs, key=phs.get) == "3", f"recomputed pH values are {phs}"
    h.shows(item, "Solution 3")
    return f"the tabulated concentrations give pH values {phs}, whose minimum is at {lowest}"


def q10(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CONC)))
    v = p(conc["2"])
    assert abs(v - 3.0) < 1e-9, f"the pH of solution 2 recomputes to {v}"
    h.shows(item, "3.00")
    return f"the tabulated {conc['2']:g} M gives a pH of {v:g}"


def q11(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CONC)))
    oh = KW25 / conc["1"]
    assert abs(oh - 1.0e-12) < 1e-21, f"the hydroxide concentration recomputes to {oh}"
    h.shows(item, "1.0 \\times 10^{-12}")
    return f"Kw over the tabulated {conc['1']:g} M gives {oh:g} M hydroxide"


def _base_oh(table, label):
    head = [cg.normalize(x) for x in table["headers"]]
    row = [r for r in table["rows"] if str(r[0]) == label][0]
    conc = cg.num(row[head.index(cg.normalize(CONC))])
    group = row[head.index(cg.normalize(GROUP))]
    return group_rule(conc, group), conc, group


def q12(table, item):
    oh, conc, group = _base_oh(table, "5")
    v = p(oh)
    assert abs(oh - 0.010) < 1e-12 and abs(v - 2.0) < 1e-9, f"pOH recomputes to {v}"
    assert abs(p(conc) - 2.30) < 0.01, "the undoubled value must give the 2.30 distractor"
    h.shows(item, "2.00")
    return (f"the tabulated {conc:g} M of a {group} hydroxide doubles to {oh:g} M, giving "
            f"pOH {v:g}, against {p(conc):.2f} undoubled")


def q13(table, item):
    oh, conc, group = _base_oh(table, "6")
    ph = 14.0 - p(oh)
    assert abs(oh - conc) < 1e-15, "a group I hydroxide must not be doubled"
    assert abs(ph - 11.0) < 1e-9, f"the pH recomputes to {ph}"
    h.shows(item, "11.00")
    return f"the tabulated {conc:g} M of a {group} hydroxide gives pOH {p(oh):g} and pH {ph:g}"


def q14(table, item):
    ohs = {lab: _base_oh(table, lab)[0] for lab in cg.labels(table)}
    pairs = [(a, b) for i, a in enumerate(ohs) for b in list(ohs)[i + 1:]
             if abs(ohs[a] - ohs[b]) < 1e-15]
    assert pairs == [("4", "5")], f"tabulated solutions with equal hydroxide: {pairs}"
    h.shows(item, "Solutions 4 and 5")
    return f"the recomputed hydroxide concentrations are {ohs}, and exactly one pair agrees"


def q22(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CONC)))
    v = p(conc["P"])
    assert abs(v - 3.0) < 1e-9, f"the pH of sample P recomputes to {v}"
    h.shows(item, "3.00")
    return f"the tabulated {conc['P']:g} M of a strong acid gives a pH of {v:g}"


def q23(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CONC)))
    oh = group_rule(conc["Q"], "group II")
    v = p(oh)
    assert abs(v - 3.0) < 1e-9, f"the pOH of sample Q recomputes to {v}"
    assert abs(p(conc["Q"]) - 3.30) < 0.01, "the undoubled value must give the 3.30 distractor"
    h.shows(item, "3.00")
    return (f"the tabulated {conc['Q']:g} M doubles to {oh:g} M, giving pOH {v:g}, against "
            f"{p(conc['Q']):.2f} undoubled")


def q24(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CONC)))
    oh_q = group_rule(conc["Q"], "group II")
    oh_r = group_rule(conc["R"], "group I")
    assert oh_r > oh_q, f"the group I sample must supply more hydroxide: {oh_r} against {oh_q}"
    ph = {"P": p(conc["P"]), "Q": 14.0 - p(oh_q), "R": 14.0 - p(oh_r)}
    assert max(ph, key=ph.get) == "R", f"recomputed pH values are {ph}"
    h.shows(item, "Sample R")
    return f"the three recomputed pH values are {ph}, whose maximum is at sample R"


TABLE_CHECKS = {9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                22: q22, 23: q23, 24: q24}


# ---------------------------------------------------------------- stem numerics

def n2(item):
    v = p(0.010)
    assert abs(v - 2.0) < 1e-9, f"pH recomputes to {v}"
    h.shows(item, "2.00")
    return f"complete ionization of 0.010 M strong acid gives a pH of {v:g}"


def n3(item):
    v = p(0.0010)
    assert abs(v - 3.0) < 1e-9, f"pH recomputes to {v}"
    h.shows(item, "3.00")
    return f"complete ionization of 0.0010 M strong acid gives a pH of {v:g}"


def n5(item):
    oh = group_rule(0.010, "group I")
    v = p(oh)
    assert abs(oh - 0.010) < 1e-15 and abs(v - 2.0) < 1e-9, f"pOH recomputes to {v}"
    h.shows(item, "2.00")
    return f"a group I hydroxide at 0.010 M gives {oh:g} M hydroxide and pOH {v:g}"


def n6(item):
    oh = group_rule(0.0050, "group II")
    assert abs(oh - 0.010) < 1e-15, f"the hydroxide concentration recomputes to {oh}"
    h.shows(item, "0.010 M")
    return f"doubling the stated 0.0050 M gives {oh:g} M hydroxide"


def n7(item):
    oh = group_rule(0.0050, "group II")
    v = p(oh)
    assert abs(v - 2.0) < 1e-9, f"pOH recomputes to {v}"
    assert abs(p(0.0050) - 2.30) < 0.01, "the undoubled value must be the 2.30 distractor"
    h.shows(item, "2.00")
    return f"doubling gives pOH {v:g}, against {p(0.0050):.2f} without the doubling"


def n18(item):
    v = p(0.10)
    assert abs(v - 1.0) < 1e-9, f"pH recomputes to {v}"
    assert abs(14.0 - v - 13.0) < 1e-9, "the 13.00 distractor must be the matching pOH"
    h.shows(item, "1.00")
    return f"complete ionization of 0.10 M strong acid gives a pH of {v:g}"


def n19(item):
    diluted = 0.10 / 10.0
    v = p(diluted)
    assert abs(diluted - 0.010) < 1e-15 and abs(v - 2.0) < 1e-9, f"pH recomputes to {v}"
    assert abs(v - p(0.10) - 1.0) < 1e-9, "a tenfold dilution must raise the pH by one unit"
    h.shows(item, "2.00")
    return f"tenfold dilution to {diluted:g} M raises the pH from {p(0.10):g} to {v:g}"


def n20(item):
    oh = group_rule(0.050, "group II")
    v = p(oh)
    assert abs(oh - 0.10) < 1e-15 and abs(v - 1.0) < 1e-9, f"pOH recomputes to {v}"
    assert abs(p(0.050) - 1.30) < 0.01, "the undoubled value must be the 1.30 distractor"
    h.shows(item, "1.00")
    return f"doubling 0.050 M gives {oh:g} M hydroxide and pOH {v:g}"


def n26(item):
    oh = group_rule(0.00050, "group II")
    needed = oh  # a group I hydroxide is not doubled, so its concentration IS [OH-]
    assert abs(needed - 0.0010) < 1e-15, f"the required concentration recomputes to {needed}"
    h.shows(item, "0.0010 M")
    return (f"the group II solution supplies {oh:g} M hydroxide, which a group I hydroxide "
            f"matches only at {needed:g} M")


def n28(item):
    c = 10.0 ** (-2.0)
    assert abs(c - 0.010) < 1e-15, f"the concentration recomputes to {c}"
    h.shows(item, "0.010 M")
    return f"ten raised to the negative of the stated pH recomputes the concentration as {c:g} M"


def n29(item):
    oh = 10.0 ** (-2.0)
    conc = oh / 2.0
    assert abs(conc - 0.0050) < 1e-15, f"the solute concentration recomputes to {conc}"
    assert abs(group_rule(conc, "group II") - oh) < 1e-15, \
        "the recomputed concentration must reproduce the stated pOH"
    h.shows(item, "0.0050 M")
    return f"a pOH of 2.00 is {oh:g} M hydroxide, which is double a solute concentration of {conc:g} M"


def n30(item):
    acid_ph = p(0.0010)
    base_ph = 14.0 - p(group_rule(0.0010, "group I"))
    total = acid_ph + base_ph
    assert abs(total - 14.0) < 1e-9, f"the sum recomputes to {total}"
    h.shows(item, "14.00")
    return f"the acid gives pH {acid_ph:g} and the base pH {base_ph:g}, summing to {total:g}"


NUMERIC = {2: n2, 3: n3, 5: n5, 6: n6, 7: n7, 18: n18, 19: n19, 20: n20,
           26: n26, 28: n28, 29: n29, 30: n30}


CLAIMS = [
 ("completely ionize, producing hydronium ions and the conjugate base",
  "EK 8.2.A.1, verbatim: molecules of a strong acid will completely ionize in aqueous solution to produce hydronium ions and the conjugate base of the acid."),
 ("2.00",
  "EK 8.2.A.1 makes the hydronium concentration equal to the stated acid concentration. Recomputed in n2."),
 ("3.00",
  "EK 8.2.A.1 with a tenfold smaller concentration, so the answer cannot be carried over. Recomputed in n3."),
 ("complete ionization makes the hydronium concentration equal",
  "EK 8.2.A.1 says exactly this: because ionization is complete, the hydronium concentration equals the initial concentration of the strong acid, and thus the pH is easily calculated."),
 ("2.00",
  "EK 8.2.A.2's group I rule: the hydroxide concentration equals the initial concentration. Recomputed in n5 through the same solver that doubles for group II."),
 ("0.010 M",
  "EK 8.2.A.2, verbatim: the hydroxide concentration is DOUBLE the initial concentration of a group II hydroxide. Recomputed in n6."),
 ("2.00",
  "EK 8.2.A.2's doubling carried through to a pOH. Recomputed in n7, which also recomputes the undoubled value as the distractor."),
 ("HClO4",
  "EK 8.2.A.1 gives the examples HCl, HBr, HI, HClO4, H2SO4 and HNO3. EK 8.6.A.1 names carboxylic acids as one common class of WEAK acid."),
 ("Solution 3",
  "EK 8.2.A.1 makes each hydronium concentration the tabulated one, so the largest concentration gives the lowest pH. Recomputed in q9."),
 ("3.00",
  "EK 8.2.A.1 applied to a tabulated concentration. Recomputed in q10."),
 ("1.0 \\times 10^{-12}",
  "EK 8.2.A.1 fixes the hydronium concentration and EK 8.1.A.2's Kw then fixes the hydroxide concentration. Recomputed in q11."),
 ("2.00",
  "EK 8.2.A.2's group II doubling, with the group read from the table rather than remembered. Recomputed in q12 against the undoubled distractor."),
 ("11.00",
  "EK 8.2.A.2's group I rule with EK 8.1.A.3's sum. Recomputed in q13, which also asserts the group I value was not doubled."),
 ("Solutions 4 and 5",
  "EK 8.2.A.2's asymmetry: a group I hydroxide at 0.010 M and a group II hydroxide at 0.0050 M supply the same hydroxide. Recomputed in q14."),
 ("strong acid, so ionization is complete and no equilibrium",
  "EK 8.2.A.1 lists HBr among the strong acids and makes their ionization complete, which is what removes the need for an equilibrium calculation."),
 ("completely dissociate to produce hydroxide ions",
  "EK 8.2.A.2, verbatim: when dissolved in solution, strong bases completely dissociate to produce hydroxide ions."),
 ("group II solution has twice the hydroxide concentration",
  "EK 8.2.A.2 makes the hydroxide concentration equal to the stated concentration for a group I hydroxide and double it for a group II hydroxide."),
 ("1.00",
  "EK 8.2.A.1 with a strong acid at 0.10 M. Recomputed in n18, which also recomputes the matching pOH as the distractor."),
 ("2.00",
  "EK 8.2.A.1 after a tenfold dilution, which raises the pH by exactly one unit. Recomputed in n19."),
 ("1.00",
  "EK 8.2.A.2's doubling on a more concentrated group II hydroxide. Recomputed in n20 against the undoubled distractor."),
 ("Chloride ion, at the same concentration as the hydronium ion",
  "EK 8.2.A.1 has complete ionization produce hydronium ion together with the conjugate base, one of each per molecule, so essentially no molecular acid remains and the two ions are equal."),
 ("3.00",
  "EK 8.2.A.1 applied to a tabulated strong acid. Recomputed in q22."),
 ("3.00",
  "EK 8.2.A.2's group II doubling applied to a tabulated concentration. Recomputed in q23 against the undoubled distractor."),
 ("Sample R",
  "EK 8.2.A.2 ranks the two tabulated bases by the hydroxide each supplies after the group rule is applied. Recomputed in q24 across all three samples."),
 ("far larger than the amount water supplies",
  "EK 8.2.A.2 sets the hydroxide from the base at the stated concentration, while EK 8.1.A.2 leaves water contributing near ten to the negative seventh, so the larger term dominates."),
 ("0.0010 M",
  "EK 8.2.A.2's asymmetry read backwards: equal pOH means equal hydroxide, which the group II solution reaches at half the group I concentration. Recomputed in n26."),
 ("HF",
  "EK 8.2.A.1's list of strong acids is HCl, HBr, HI, HClO4, H2SO4 and HNO3, and hydrofluoric acid is not among them."),
 ("0.010 M",
  "EK 8.2.A.1 read backwards, from pH to the acid concentration, which complete ionization makes identical to the hydronium concentration. Recomputed in n28."),
 ("0.0050 M",
  "EK 8.2.A.2's doubling read backwards: the hydroxide concentration is twice the solute concentration for a group II hydroxide. Recomputed in n29 and checked by substitution."),
 ("14.00",
  "EK 8.2.A.1 for the acid and EK 8.2.A.2 with EK 8.1.A.3 for the base. Recomputed in n30."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[11]["table"] = dict(
            headers=h8_2._T_BASES["headers"],
            rows=[[lab, sol, ("group I" if lab == "5" else grp), c]
                  for lab, sol, grp, c in h8_2._T_BASES["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[5]["choices"])
        ch[0] = "0.0050 M"
        mod.QUESTIONS[5]["choices"] = ch
        cl[5] = ("0.0050 M", cl[5][1])

    def sulfuric_creeps_into_a_calculation(mod, cl):
        mod.QUESTIONS[1]["q"] = "A solution is 0.010 M in H2SO4. What is its pH?"
        no_sulfuric_arithmetic(mod)

    return [("a tabulated group changed so the doubling rule no longer applies", corrupt_table),
            ("a recomputed hydroxide concentration no longer in the keyed choice",
             corrupt_numeric),
            ("H2SO4 used in an item that computes a pH", sulfuric_creeps_into_a_calculation)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_sulfuric_arithmetic(h8_2)
h.run(h8_2, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
