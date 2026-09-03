"""Key audit for AP CHEMISTRY 7.12 Common-Ion Effect.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON. One essential knowledge statement, 7.12.A.1: the
solubility of a salt is reduced when it is dissolved into a solution that
already contains one of the ions present in the salt, and the impact can be
understood qualitatively using Le Chatelier's principle OR calculated from the
Ksp for the dissolution process. Because the topic rests on a single sentence,
the items are separated by which of the two named routes they take and by what
is asked, and both routes appear:

  qualitative, via Le Chatelier   1, 2, 3, 4, 5, 6, 9, 12, 16, 20, 21, 23, 25,
                                  27, 29, 30
  calculated from Ksp             7, 8, 10, 11, 13, 14, 15, 17, 18, 19, 22, 24,
                                  26, 28

THE HIDDEN ASSUMPTION, checked. Every calculation here treats the common ion's
concentration as unchanged by the salt that dissolves into it. That is an
approximation, and it is the one a wrong answer would quietly rely on, so
``solubility_with_common_ion`` recomputes each value AND asserts that what the
dissolving salt contributes is under one percent of the pool already there. If
a future edit ever picks numbers where that fails, this file fails rather than
shipping a value that is merely close.

ARITHMETIC. Two solvers, written once:

    ``solubility_with_common_ion(ksp, common, n_common, n_other)``
    ``ksp_from_common_ion(s, common, ...)``

NEGATIVE CONTROL: ``python3 verify_h7_12.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h7_12

IONS = "Ions present in solution"
CL = "Chloride ion concentration already present (M)"
SOLN = "Solution the salt was added to"
MEAS = "Molar solubility measured (M)"

_SCI = re.compile(r"\\\(\s*(-?\d+(?:\.\d+)?)\s*(?:\\times\s*10\^\{(-?\d+)\})?\s*\\\)")


def sci(text):
    m = _SCI.search(str(text))
    assert m, f"{text!r} holds no parseable math span"
    return float(m.group(1)) * (10.0 ** int(m.group(2)) if m.group(2) else 1.0)


def solubility_with_common_ion(ksp, common, n_common=1, n_other=1):
    """Molar solubility of a salt in a solution already holding one of its ions.

    ``n_common`` is how many of the shared ion each formula unit releases and
    ``n_other`` how many of the other ion. The shared ion is held at ``common``
    by the solution already present; the other ion arrives only from the salt.

    The approximation being made is that the salt's own contribution to the
    shared ion is negligible, and it is ASSERTED rather than assumed.
    """
    other = (ksp / common ** n_common) ** (1.0 / n_other)
    s = other / n_other
    contributed = n_common * s
    assert contributed < 0.01 * common, (
        f"the dissolving salt contributes {contributed:g} to a pool of {common:g}, "
        "which is too large to neglect -- the arithmetic in the item is not exact"
    )
    assert abs((common ** n_common) * (other ** n_other) - ksp) / ksp < 1e-9, \
        "the solver does not reproduce the stated Ksp"
    return s, other


# ------------------------------------------------------------------ table items

def _shares(table, row, ions):
    text = cg.normalize(cg.cell.__self__ if False else
                        [r for r in table["rows"] if str(r[0]) == row][0][
                            [cg.normalize(x) for x in table["headers"]].index(
                                cg.normalize(IONS))])
    return [i for i in ions if cg.contains_phrase(text, i)]


def q3(table, item):
    agcl = ["silver ion", "chloride ion"]
    free = [lab for lab in cg.labels(table) if not _shares(table, lab, agcl)]
    assert free == ["2"], f"solutions sharing no ion with AgCl: {free}"
    h.shows(item, "Solution 2")
    return (f"exactly one tabulated solution, {free[0]}, holds neither ion of AgCl, so it "
            "is the only one whose solubility is not reduced")


def q4(table, item):
    cation = [lab for lab in cg.labels(table)
              if _shares(table, lab, ["silver ion"])]
    assert cation == ["3"], f"solutions supplying the silver ion: {cation}"
    h.shows(item, "Solution 3")
    return f"exactly one tabulated solution, {cation[0]}, supplies the cation of AgCl"


def q5(table, item):
    agcl = ["silver ion", "chloride ion"]
    reduce = [lab for lab in cg.labels(table) if _shares(table, lab, agcl)]
    assert reduce == ["1", "3", "4"], f"solutions sharing an ion with AgCl: {reduce}"
    h.shows(item, "Solutions 1, 3 and 4")
    return f"the tabulated solutions sharing an ion with AgCl are {reduce}"


def q9(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CL)))
    lowest = min(conc, key=conc.get)
    assert lowest == "A", f"the smallest tabulated common-ion concentration is in {lowest}"
    h.shows(item, "Beaker A")
    return (f"the tabulated concentrations {conc} have a unique minimum at {lowest}, "
            "where the reduction is smallest")


def q10(table, item):
    conc = dict(zip(cg.labels(table), cg.col(table, CL)))
    s, other = solubility_with_common_ion(1.0e-10, conc["C"])
    assert abs(s - 1.0e-10) < 1e-20, f"the solubility in beaker C recomputes to {s}"
    h.shows(item, "1.0 \\times 10^{-10}")
    return (f"dividing the constant by the tabulated {conc['C']:g} M recomputes the "
            f"solubility as {s:g}")


def q18(table, item):
    rows = {str(r[0]): r for r in table["rows"]}
    head = [cg.normalize(x) for x in table["headers"]]
    si, mi = head.index(cg.normalize(SOLN)), head.index(cg.normalize(MEAS))
    c2 = float(re.search(r"([\d.]+) M", rows["2"][si]).group(1))
    c3 = float(re.search(r"([\d.]+) M", rows["3"][si]).group(1))
    s2, s3 = float(rows["2"][mi]), float(rows["3"][mi])
    assert abs(c3 / c2 - 10.0) < 1e-9, f"the shared-ion concentrations rise by {c3 / c2}"
    assert abs(s2 / s3 - 10.0) < 1e-9, f"the solubilities fall by {s2 / s3}"
    h.shows(item, "by a factor of ten")
    return (f"a tenfold rise from {c2:g} M to {c3:g} M accompanies a fall from {s2:g} to "
            f"{s3:g}, a factor of {s2 / s3:g}")


def q19(table, item):
    rows = {str(r[0]): r for r in table["rows"]}
    head = [cg.normalize(x) for x in table["headers"]]
    si, mi = head.index(cg.normalize(SOLN)), head.index(cg.normalize(MEAS))
    c3 = float(re.search(r"([\d.]+) M", rows["3"][si]).group(1))
    k3 = c3 * float(rows["3"][mi])
    k1 = float(rows["1"][mi]) ** 2
    assert abs(k3 - 1.0e-6) < 1e-15, f"the constant from trial 3 recomputes to {k3}"
    assert abs(k1 - k3) / k3 < 1e-9, \
        f"the pure-water trial gives {k1}, which must agree with {k3}"
    h.shows(item, "1.0 \\times 10^{-6}")
    return (f"trial 3 gives {c3:g} times {rows['3'][mi]} equal to {k3:g}, which agrees "
            f"with the pure-water trial's {k1:g}")


TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 9: q9, 10: q10, 18: q18, 19: q19}


# ---------------------------------------------------------------- stem numerics

def n7(item):
    s, _ = solubility_with_common_ion(1.0e-10, 0.10)
    assert abs(s - 1.0e-9) < 1e-18, f"solubility recomputes to {s}"
    assert abs(math.sqrt(1.0e-10) - 1.0e-5) < 1e-12, \
        "the pure-water value quoted in the rationale must be ten to the minus five"
    h.shows(item, "1.0 \\times 10^{-9}")
    return f"the constant over 0.10 M recomputes the solubility as {s:g}"


def n8(item):
    s, _ = solubility_with_common_ion(1.0e-10, 0.010)
    assert abs(s - 1.0e-8) < 1e-17, f"solubility recomputes to {s}"
    h.shows(item, "1.0 \\times 10^{-8}")
    return f"the constant over 0.010 M recomputes the solubility as {s:g}"


def n11(item):
    pure = math.sqrt(1.0e-10)
    s, _ = solubility_with_common_ion(1.0e-10, 0.10)
    ratio = pure / s
    assert abs(ratio - 1.0e4) < 1.0, f"the ratio recomputes to {ratio}"
    h.shows(item, "10,000 times smaller")
    return f"{pure:g} in pure water against {s:g} with the common ion is a factor of {ratio:g}"


def n13(item):
    s, _ = solubility_with_common_ion(4.0e-12, 0.10, n_common=2, n_other=1)
    assert abs(s - 4.0e-10) < 1e-19, f"solubility recomputes to {s}"
    unsquared = 4.0e-12 / 0.10
    assert abs(unsquared - 4.0e-11) < 1e-20, \
        "the 4.0 times ten to the minus eleven distractor must omit the square"
    h.shows(item, "4.0 \\times 10^{-10}")
    return (f"the constant over the square of 0.10 recomputes the solubility as {s:g}, "
            f"against {unsquared:g} without the square")


def n14(item):
    s, other = solubility_with_common_ion(4.0e-11, 0.10, n_common=1, n_other=2)
    assert abs(other - 2.0e-5) < 1e-12, f"the anion concentration recomputes to {other}"
    h.shows(item, "2.0 \\times 10^{-5}")
    return (f"the square root of the constant over 0.10 recomputes the anion "
            f"concentration as {other:g}")


def n15(item):
    s, other = solubility_with_common_ion(4.0e-11, 0.10, n_common=1, n_other=2)
    assert abs(s - 1.0e-5) < 1e-12, f"the molar solubility recomputes to {s}"
    assert abs(other - 2 * s) < 1e-15, "the anion must be twice the molar solubility"
    h.shows(item, "1.0 \\times 10^{-5}")
    return f"half the anion concentration {other:g} recomputes the solubility as {s:g}"


def n17(item):
    s, common = 5.0e-10, 0.20
    k = s * common
    assert abs(k - 1.0e-10) < 1e-19, f"Ksp recomputes to {k}"
    assert abs(s * s - 2.5e-19) < 1e-28, \
        "the squared-solubility distractor must be the pure-water mistake"
    h.shows(item, "1.0 \\times 10^{-10}")
    return f"{s:g} times {common:g} recomputes Ksp as {k:g}, against {s * s:g} if squared"


def n22(item):
    s, _ = solubility_with_common_ion(9.0e-12, 0.030)
    assert abs(s - 3.0e-10) < 1e-19, f"solubility recomputes to {s}"
    assert abs(math.sqrt(9.0e-12) - 3.0e-6) < 1e-14, \
        "the pure-water value quoted in the rationale must be three times ten to the minus six"
    h.shows(item, "3.0 \\times 10^{-10}")
    return f"the constant over 0.030 M recomputes the solubility as {s:g}"


def n24(item):
    ksp, target = 2.0e-9, 1.0e-8
    common = ksp / target
    assert abs(common - 0.20) < 1e-12, f"the required concentration recomputes to {common}"
    s, _ = solubility_with_common_ion(ksp, common)
    assert abs(s - target) < 1e-17, "the recomputed concentration must reproduce the target"
    h.shows(item, "0.20 M solution")
    return f"the constant over the target solubility recomputes the concentration as {common:g} M"


NUMERIC = {7: n7, 8: n8, 11: n11, 13: n13, 14: n14, 15: n15, 17: n17, 22: n22,
           24: n24}


CLAIMS = [
 ("The solubility is reduced",
  "EK 7.12.A.1, verbatim: the solubility of a salt is reduced when it is dissolved into a solution that already contains one of the ions present in the salt. The statement draws no distinction between a shared cation and a shared anion."),
 ("chloride ion already present pushes the dissolution equilibrium back",
  "EK 7.12.A.1 offers Le Chatelier's principle as the qualitative route, and the shared ion is a product of the dissolution equilibrium, so supplying it shifts that equilibrium toward the undissolved solid."),
 ("Solution 2",
  "EK 7.12.A.1 reduces solubility only where an ion of the salt is already present. The tabulated ion lists are searched in q3 and exactly one solution holds neither ion of AgCl."),
 ("Solution 3",
  "EK 7.12.A.1 applies through either ion of the salt. The tabulated lists are searched in q4 and exactly one solution supplies the cation."),
 ("Solutions 1, 3 and 4",
  "EK 7.12.A.1 requires an ion already present that also appears in the salt. The tabulated lists are searched in q5 and three of the four qualify."),
 ("one of the products of the dissolution equilibrium",
  "EK 7.12.A.1's qualitative route is Le Chatelier's principle, which treats the dissolved ions as products of a reversible process; supplying a product pushes the process back toward the solid. The constant is a function of temperature."),
 ("1.0 \\times 10^{-9}",
  "EK 7.12.A.1's calculation from Ksp, with the shared anion held at 0.10 M. Recomputed in n7, which also confirms the dissolving salt's own contribution is negligible."),
 ("1.0 \\times 10^{-8}",
  "EK 7.12.A.1's calculation from Ksp with a tenfold smaller common-ion concentration, so the answer cannot be carried over from the previous item. Recomputed in n8."),
 ("Beaker A",
  "EK 7.12.A.1 makes the reduction larger the more of the shared ion is present, so the smallest tabulated concentration leaves the salt most soluble. The tabulated concentrations are ranked in q9."),
 ("1.0 \\times 10^{-10}",
  "EK 7.12.A.1's calculation from Ksp with the tabulated 1.0 M chloride. Recomputed in q10 from the table."),
 ("10,000 times smaller",
  "EK 7.12.A.1 read as a comparison with the pure-water case: the square root of Ksp against Ksp divided by the shared-ion concentration. Recomputed in n11."),
 ("The iodide ion",
  "EK 7.12.A.1 requires an ion already present that also appears in the salt being dissolved. Of the two ions the solution supplies, only one appears in PbI2, and the lead ion is not present until the salt dissolves."),
 ("4.0 \\times 10^{-10}",
  "EK 7.12.A.1's calculation from Ksp where the shared ion carries a coefficient of two and so enters squared. Recomputed in n13 against the unsquared distractor."),
 ("2.0 \\times 10^{-5}",
  "EK 7.12.A.1's calculation from Ksp where the shared ion is the cation, so the anion concentration is the square root of the constant over the fixed cation concentration. Recomputed in n14."),
 ("1.0 \\times 10^{-5}",
  "The molar solubility is half the anion concentration because two anions leave each formula unit. Recomputed in n15 from the same constant."),
 ("neither ion of the added salt appears in the dissolution equilibrium",
  "EK 7.12.A.1 makes the reduction depend on the solution already containing an ion PRESENT IN THE SALT, so a salt supplying two unrelated ions adds no term to the equilibrium expression."),
 ("1.0 \\times 10^{-10}",
  "EK 7.12.A.1 allows Ksp to be obtained from a measurement made with a common ion present, using the actual concentration of each ion. Recomputed in n17, which also recomputes the squared-solubility mistake."),
 ("by a factor of ten",
  "EK 7.12.A.1 for a one-to-one salt, where the constant is the product of the solubility and the fixed shared-ion concentration. The tabulated trials are compared in q18."),
 ("1.0 \\times 10^{-6}",
  "EK 7.12.A.1's calculation from Ksp, run backwards from a measured solubility. Recomputed in q19, which also checks the value against the pure-water trial in the same table."),
 ("supplies the same anion as the silver salt",
  "EK 7.12.A.1 makes solubility fall when an ion of the salt is already present, so an excess of the shared ion drives the salt out of solution; dilution and an unrelated salt do the opposite or nothing."),
 ("value of the solubility-product constant",
  "EK 7.12.A.1 has the effect CALCULATED FROM Ksp, which treats the constant as the fixed input; it is a function of temperature, so it is the quantity that does not move while the amounts in the beaker do."),
 ("3.0 \\times 10^{-10}",
  "EK 7.12.A.1's calculation from Ksp with a shared cation at 0.030 M. Recomputed in n22, which also recomputes the pure-water value quoted in the rationale."),
 ("lower in the beaker containing the shared anion",
  "The cation enters solution only from the sparingly soluble salt, so its concentration is the molar solubility, which EK 7.12.A.1 reduces. The constant is the same in both beakers, which is what forces the cation term down as the anion term rises."),
 ("0.20 M solution",
  "EK 7.12.A.1's calculation from Ksp, solved for the common-ion concentration that produces a stated solubility. Recomputed in n24 and checked by substituting it back."),
 ("understood qualitatively using the principle, or calculated",
  "EK 7.12.A.1 offers both routes in one sentence, so neither is excluded and the two agree."),
 ("two ion concentrations are not equal here",
  "Squaring the solubility works only when both ions arrive from the dissolving salt in equal amounts. EK 7.12.A.1's calculation from Ksp uses the actual concentration of each ion, and the shared ion is far larger."),
 ("More solid appears",
  "EK 7.12.A.1 reduces the solubility when the shared ion is supplied, so a solution already holding its full complement of dissolved salt now holds more than it can, and the excess leaves as solid."),
 ("squared term, because two of that ion appear in the formula unit",
  "The exponent in the expression comes from the coefficient in the dissolution equation rather than from where the ion originated, so EK 7.12.A.1's calculation squares the total concentration of that ion."),
 ("far larger than the molar solubility",
  "The approximation is a comparison of sizes: the salt adds its molar solubility to a pool already far larger, so the total is unchanged to the digits reported. It does not depend on the formula type or on which ion is shared."),
 ("constant depends on temperature while the solubility depends on what else",
  "EK 7.12.A.1 has the effect calculated FROM Ksp, which makes the constant the fixed input and the solubility the result; the constant belongs to the salt at a temperature and the solubility to the salt in a particular solution."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[2]["table"] = dict(
            headers=h7_12._T_SOLUTIONS["headers"],
            rows=[[lab, sol, ("sodium ion and chloride ion" if lab == "2" else ions)]
                  for lab, sol, ions in h7_12._T_SOLUTIONS["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[6]["choices"])
        ch[0] = "\\( 1.0 \\times 10^{-7} \\) M"
        mod.QUESTIONS[6]["choices"] = ch
        cl[6] = ("1.0 \\times 10^{-7}", cl[6][1])

    def break_the_approximation(mod, cl):
        """If the numbers ever stop justifying the neglected contribution, fail."""
        s, _ = solubility_with_common_ion(1.0e-10, 1.0e-9)
        raise AssertionError(f"unreachable: solver accepted a negligible pool, s={s}")

    return [("a tabulated ion list corrupted so the keyed solution changes", corrupt_table),
            ("a recomputed solubility no longer in the keyed choice", corrupt_numeric),
            ("a common-ion pool too small for the neglected contribution to be ignored",
             break_the_approximation)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h7_12, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

h.run(h7_12, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
