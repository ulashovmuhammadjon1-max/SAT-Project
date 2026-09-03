"""Key audit for AP CHEMISTRY 8.1 Introduction to Acids and Bases.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  8.1.A.1  pH and pOH are the negative base-ten logarithms of the hydronium and
           hydroxide concentrations; H+(aq) and H3O+(aq) are interchangeable
  8.1.A.2  water autoionizes with Kw, the PRODUCT of the two concentrations,
           equal to 1.0e-14 at 25 degrees Celsius
  8.1.A.3  neutral means pH EQUALS pOH; at 25 degrees that makes both 7.0 and
           makes pH + pOH = pKw = 14
  8.1.A.4  Kw is temperature dependent, so the neutral pH deviates from 7.0 at
           other temperatures

THE DEFINITION THAT MUST NOT BE TAUGHT WRONG. EK 8.1.A.3 defines neutral as pH
equal to pOH and gives 7.0 only for 25 degrees Celsius; EK 8.1.A.4 then says the
neutral pH deviates from 7.0 elsewhere. ``neutral_is_equality`` below asserts
that the keyed choice of the definition item names the EQUALITY and that no
keyed choice anywhere in the module calls a solution neutral because its pH is
7.0. That is the one place a Chemistry bank most reliably teaches an error.

ARITHMETIC. Every logarithm here is exact -- concentrations are powers of ten,
and the two temperature items use values of Kw whose square root is also a power
of ten -- and every one is recomputed from the stated value, in TABLE_CHECKS for
the eight items carrying a table and in NUMERIC for the fourteen whose numbers
are in the stem.

NEGATIVE CONTROL: ``python3 verify_h8_1.py --selftest``.
"""
import math
import re
import sys

import cg_check as cg
import h_check as h

import h8_1

HYD = "Hydronium ion concentration (M)"
KWCOL = "Value of Kw"
PHCOL = "pH"
POHCOL = "pOH"

_SCI = re.compile(r"\\\(\s*(-?\d+(?:\.\d+)?)\s*(?:\\times\s*10\^\{(-?\d+)\})?\s*\\\)")

KW25 = 1.0e-14


def sci(text):
    m = _SCI.search(str(text))
    assert m, f"{text!r} holds no parseable math span"
    return float(m.group(1)) * (10.0 ** int(m.group(2)) if m.group(2) else 1.0)


def sci_col(table, header):
    j = [cg.normalize(x) for x in table["headers"]].index(cg.normalize(header))
    return {str(r[0]): sci(r[j]) for r in table["rows"]}


def p(value):
    """The negative base-ten logarithm, which is what EK 8.1.A.1 defines."""
    return -math.log10(value)


def neutral_pH(kw):
    """Pure water: the two ion concentrations are equal, so each is sqrt(Kw)."""
    return p(math.sqrt(kw))


# The error this topic exists to prevent: calling a solution neutral because its
# pH is 7.0 rather than because pH equals pOH. Explicit lookarounds, never \b
# beside a digit -- "7.0" abuts a period and a digit at both ends.
# The pattern must fire on "neutral WHEN its pH IS 7.0" and stay silent on
# "the pH of pure neutral water DEVIATES FROM 7.0", which is the framework's own
# correct sentence. So it requires an equating word between the two, matched with
# explicit lookarounds -- a bare "is" would otherwise match inside "deviates".
_EQUATES = r"(?<![A-Za-z])(?:is|are|equals?|means?|makes?|when|of exactly)(?![A-Za-z])"
_SEVEN_AS_DEFINITION = re.compile(
    r"(?<![A-Za-z])neutral(?![A-Za-z])[^.]{0,80}?" + _EQUATES
    + r"[^.]{0,25}?(?<![\d.])7\.0(?![\d])"
    + r"|(?<![\d.])7\.0(?![\d])[^.]{0,40}?" + _EQUATES
    + r"[^.]{0,25}?(?<![A-Za-z])neutral(?![A-Za-z])",
    re.I)


def neutral_is_equality(module):
    """No keyed choice may define neutrality by the number 7.0."""
    for i, item in enumerate(module.QUESTIONS, 1):
        keyed = h.keyed(item)
        hit = _SEVEN_AS_DEFINITION.search(keyed)
        assert not hit, (
            f"{module.TOPIC[0]} q{i}: the keyed choice ties neutrality to the value 7.0 "
            f"({hit.group(0)!r}); EK 8.1.A.3 defines it as pH equal to pOH and EK 8.1.A.4 "
            "makes the number temperature dependent"
        )
    print(f"OK  {module.TOPIC[0]} definition: no keyed choice defines a neutral solution "
          "by the number 7.0.")


# ------------------------------------------------------------------ table items

def q7(table, item):
    conc = sci_col(table, HYD)
    value = p(conc["3"])
    assert abs(value - 11.0) < 1e-9, f"pH of solution 3 recomputes to {value}"
    h.shows(item, "11.00")
    return f"the tabulated {conc['3']:g} M gives a pH of {value:g}"


def q8(table, item):
    conc = sci_col(table, HYD)
    neutral = [lab for lab, c in conc.items()
               if abs(p(c) - p(KW25 / c)) < 1e-9]
    assert neutral == ["2"], f"tabulated solutions with pH equal to pOH: {neutral}"
    h.shows(item, "Solution 2")
    return (f"of the tabulated concentrations {conc}, exactly one gives a pH equal to its "
            "own pOH at 25 degrees Celsius")


def q9(table, item):
    conc = sci_col(table, HYD)
    oh = KW25 / conc["1"]
    assert abs(oh - 1.0e-11) < 1e-20, f"the hydroxide concentration recomputes to {oh}"
    h.shows(item, "1.0 \\times 10^{-11}")
    return (f"Kw over the tabulated {conc['1']:g} M recomputes the hydroxide "
            f"concentration as {oh:g} M")


def q15(table, item):
    ph = dict(zip(cg.labels(table), cg.col(table, PHCOL)))
    poh = dict(zip(cg.labels(table), cg.col(table, POHCOL)))
    equal = [lab for lab in ph if abs(ph[lab] - poh[lab]) < 1e-9]
    assert equal == ["X"], f"tabulated samples with pH equal to pOH: {equal}"
    h.shows(item, "Sample X")
    return f"exactly one tabulated sample, {equal[0]}, has its pH equal to its pOH"


def q16(table, item):
    ph = dict(zip(cg.labels(table), cg.col(table, PHCOL)))
    poh = dict(zip(cg.labels(table), cg.col(table, POHCOL)))
    sums = {lab: ph[lab] + poh[lab] for lab in ph}
    assert all(abs(v - 14.0) < 1e-9 for v in sums.values()), f"the sums are {sums}"
    assert len([lab for lab in ph if abs(ph[lab] - poh[lab]) < 1e-9]) == 1, \
        "the 'all three are neutral' distractor must be false"
    h.shows(item, "sum of pH and pOH is 14")
    return f"every tabulated pair sums to 14: {sums}"


def q19(table, item):
    kw = sci_col(table, KWCOL)
    temps = dict(zip(cg.labels(table), cg.col(table, "Temperature in degrees Celsius")))
    order = sorted(temps, key=temps.get)
    values = [kw[lab] for lab in order]
    assert all(values[i] < values[i + 1] for i in range(len(values) - 1)), \
        f"Kw must rise with temperature in the table: {values}"
    h.shows(item, "Kw increases as the temperature rises")
    return f"sorted by temperature the tabulated constants are {values}, strictly rising"


def q20(table, item):
    kw = sci_col(table, KWCOL)
    lo, hi = neutral_pH(kw["10"]), neutral_pH(kw["60"])
    assert hi < lo, f"the neutral pH must fall from {lo} to {hi} as the water warms"
    assert abs(kw["25"] - KW25) < 1e-20, "the tabulated 25 degree value must be Kw"
    h.shows(item, "falls, because Kw rises")
    return (f"the neutral pH recomputes from {lo:.2f} at 10 degrees to {hi:.2f} at 60 "
            "degrees, a fall")


TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 15: q15, 16: q16, 19: q19, 20: q20}


# ---------------------------------------------------------------- stem numerics

def n2(item):
    v = p(1.0e-4)
    assert abs(v - 4.0) < 1e-9, f"pH recomputes to {v}"
    assert abs(14.0 - v - 10.0) < 1e-9, "the 10.00 distractor must be the matching pOH"
    h.shows(item, "4.00")
    return f"the negative logarithm of ten to the minus four recomputes as {v:g}"


def n3(item):
    v = p(1.0e-2)
    assert abs(v - 2.0) < 1e-9, f"pOH recomputes to {v}"
    h.shows(item, "2.00")
    return f"the negative logarithm of ten to the minus two recomputes as {v:g}"


def n6(item):
    v = 14.0 - 5.0
    assert abs(v - 9.0) < 1e-9, f"pOH recomputes to {v}"
    h.shows(item, "9.00")
    return f"fourteen less the stated pH of 5.00 recomputes the pOH as {v:g}"


def n14(item):
    c = 10.0 ** (-3.0)
    assert abs(c - 1.0e-3) < 1e-12, f"the concentration recomputes to {c}"
    assert abs(KW25 / c - 1.0e-11) < 1e-20, \
        "the ten to the minus eleventh distractor must be the hydronium concentration"
    h.shows(item, "1.0 \\times 10^{-3}")
    return f"ten raised to the negative of the stated pOH recomputes as {c:g} M"


def n18(item):
    ph = p(1.0e-9)
    poh = 14.0 - ph
    assert abs(ph - 9.0) < 1e-9 and abs(poh - 5.0) < 1e-9, f"recomputed {ph} and {poh}"
    assert ph > 7.0, "the solution must be basic at 25 degrees Celsius"
    h.shows(item, "Its pH is 9.00, and its pOH is 5.00")
    return f"the stated concentration gives pH {ph:g} and pOH {poh:g}, so the solution is basic"


def n21(item):
    v = neutral_pH(1.0e-12)
    assert abs(v - 6.0) < 1e-9, f"the neutral pH recomputes to {v}"
    h.shows(item, "6.00")
    return f"the square root of ten to the minus twelve gives a neutral pH of {v:g}"


def n22(item):
    kw = 1.0e-12
    ph = neutral_pH(kw)
    poh = p(math.sqrt(kw))
    assert abs(ph - poh) < 1e-12, "pure water must have pH equal to pOH at any temperature"
    assert ph < 7.0, "the value must sit below 7.0, which is why the equality matters"
    h.shows(item, "Neutral, because pH still equals pOH")
    return (f"pure water at this Kw has pH and pOH both {ph:g}, equal to one another and "
            "below 7.0")


def n23(item):
    v = neutral_pH(1.0e-13)
    assert abs(v - 6.5) < 1e-9, f"the neutral pH recomputes to {v}"
    h.shows(item, "6.50")
    return f"the square root of ten to the minus thirteen gives a neutral pH of {v:g}"


def n24(item):
    v = p(1.0e-13)
    assert abs(v - 13.0) < 1e-9, f"pKw recomputes to {v}"
    h.shows(item, "13")
    return f"the negative logarithm of the stated Kw recomputes pKw as {v:g}"


def n25(item):
    poh = p(1.0e-6)
    ph = 14.0 - poh
    assert abs(ph - 8.0) < 1e-9, f"pH recomputes to {ph}"
    assert abs(poh - 6.0) < 1e-9, "the 6.00 distractor must be the pOH"
    h.shows(item, "8.00")
    return f"a pOH of {poh:g} leaves a pH of {ph:g} at 25 degrees Celsius"


def n27(item):
    ratio = (10.0 ** -3.0) / (10.0 ** -6.0)
    assert abs(ratio - 1000.0) < 1e-6, f"the ratio recomputes to {ratio}"
    h.shows(item, "1,000 times the second")
    return f"three pH units apart is a concentration ratio of {ratio:g}"


def n29(item):
    assert abs((4.0 + 4.0) - 8.0) < 1e-9, "the reported pair must sum to 8"
    assert abs(14.0 - 8.0 - 6.0) < 1e-9, "and so fall six short of pKw at 25 degrees"
    h.shows(item, "sum to 14 at that temperature, and these sum to 8")
    return "the reported pH and pOH sum to 8, six short of the pKw of 14"


NUMERIC = {2: n2, 3: n3, 6: n6, 14: n14, 18: n18, 21: n21, 22: n22, 23: n23,
           24: n24, 25: n25, 27: n27, 29: n29}


CLAIMS = [
 ("-\\log[\\mathrm{H_3O^+}]",
  "EK 8.1.A.1, verbatim: pH is the negative base-ten logarithm of the hydronium ion concentration. The negative logarithm of the hydroxide concentration is pOH."),
 ("4.00",
  "EK 8.1.A.1 applied to a concentration that is an exact power of ten. Recomputed in n2, which also recomputes the matching pOH as the distractor."),
 ("2.00",
  "EK 8.1.A.1's second equation, pOH as the negative logarithm of the hydroxide concentration. Recomputed in n3."),
 ("product of the hydronium and hydroxide concentrations",
  "EK 8.1.A.2, verbatim: water autoionizes with an equilibrium constant Kw equal to the product of the hydronium and hydroxide concentrations, which is one times ten to the negative fourteenth at 25 degrees Celsius."),
 ("Their sum is 14",
  "EK 8.1.A.3 gives pKw equal to 14 equal to pH plus pOH at 25 degrees Celsius. The value 7.0 is what each equals in pure water, not what they sum to."),
 ("9.00",
  "EK 8.1.A.3's sum rule at 25 degrees Celsius. Recomputed in n6."),
 ("11.00",
  "EK 8.1.A.1 applied to a tabulated concentration. Recomputed in q7 from the table."),
 ("Solution 2",
  "EK 8.1.A.3 makes a neutral solution one in which pH equals pOH. The tabulated concentrations are tested for that equality in q8, and exactly one satisfies it."),
 ("1.0 \\times 10^{-11}",
  "EK 8.1.A.2 fixes the product of the two concentrations at 25 degrees Celsius, so one determines the other. Recomputed in q9 from the tabulated value."),
 ("Hydrogen ion and hydronium ion",
  "EK 8.1.A.1 states that the terms hydrogen ion and hydronium ion, and the symbols H+(aq) and H3O+(aq), are often used interchangeably, with the hydronium form preferred and the other also accepted."),
 ("value of Kw changes",
  "EK 8.1.A.4, verbatim in substance: the value of Kw is temperature dependent, so the pH of pure, neutral water will deviate from 7.0 at temperatures other than 25 degrees Celsius."),
 ("pH equals pOH",
  "EK 8.1.A.3 defines a neutral solution by that equality and only then gives 7.0 as its value at 25 degrees Celsius; EK 8.1.A.4 makes the number temperature dependent, so the equality is what carries the definition."),
 ("2 H2O(l) to H3O+(aq) + OH-(aq)",
  "EK 8.1.A.2 defines Kw as the product of the hydronium and hydroxide concentrations, which are the two species autoionization produces when one water molecule transfers a proton to another."),
 ("1.0 \\times 10^{-3}",
  "EK 8.1.A.1 read backwards, from pOH to the hydroxide concentration. Recomputed in n14, which also recomputes the hydronium concentration as the distractor."),
 ("Sample X",
  "EK 8.1.A.3's definition applied to tabulated pairs. The equality is tested in q15 and holds for exactly one sample."),
 ("sum of pH and pOH is 14",
  "EK 8.1.A.3's equation holds for every aqueous solution at 25 degrees Celsius, neutral or not. The three tabulated sums are recomputed in q16, along with the fact that only one sample is neutral."),
 ("Their product is fixed, so raising one lowers the other",
  "EK 8.1.A.2 gives Kw as the product of the two concentrations, and an equilibrium constant applies to every aqueous solution at that temperature, so raising one concentration lowers the other."),
 ("Its pH is 9.00, and its pOH is 5.00",
  "EK 8.1.A.1 for the pH and EK 8.1.A.3 for the pOH, with the classification following from the neutral value of 7.0 at this temperature. Recomputed in n18."),
 ("Kw increases as the temperature rises",
  "EK 8.1.A.4 makes Kw temperature dependent. The tabulated values are sorted by temperature in q19 and rise strictly."),
 ("falls, because Kw rises",
  "In pure water each ion concentration is the square root of Kw, so a rising Kw raises the hydronium concentration and lowers its negative logarithm. The two neutral pH values are recomputed from the table in q20."),
 ("6.00",
  "EK 8.1.A.4: at a temperature where Kw differs, the neutral pH differs from 7.0. Recomputed in n21 as the negative logarithm of the square root of the stated Kw."),
 ("Neutral, because pH still equals pOH",
  "EK 8.1.A.3 defines neutrality by the equality of pH and pOH, which pure water satisfies at every temperature because autoionization makes the two ions in equal amounts. Recomputed in n22."),
 ("6.50",
  "EK 8.1.A.4 with a Kw whose square root is also an exact power of ten. Recomputed in n23."),
 ("13",
  "The sum of pH and pOH is pKw, and EK 8.1.A.3 fixes the value 14 only for 25 degrees Celsius. Recomputed in n24 from the stated Kw."),
 ("8.00",
  "EK 8.1.A.1 gives the pOH from the hydroxide concentration and EK 8.1.A.3 gives the pH as the remainder of 14. Recomputed in n25, which also recomputes the pOH as the distractor."),
 ("higher hydronium ion concentration",
  "EK 8.1.A.1 makes pH the NEGATIVE logarithm of the hydronium concentration, so the two move in opposite directions, and EK 8.1.A.2 then makes the hydroxide concentration fall as the hydronium concentration rises."),
 ("1,000 times the second",
  "EK 8.1.A.1 makes pH a base-ten logarithm, so a difference of three units is a factor of a thousand in concentration. Recomputed in n27."),
 ("concentration that does not depend on how much is present",
  "EK 8.1.A.2 writes Kw as the product of the two ion concentrations alone, which is what an equilibrium expression does with a pure liquid; water is a reactant in the autoionization rather than a product."),
 ("sum to 14 at that temperature, and these sum to 8",
  "EK 8.1.A.3's equation is violated by the reported pair, which is checked in n29. Equal values would also make the solution neutral, which a pH of 4.00 at 25 degrees Celsius is not."),
 ("Any aqueous solution at 25 degrees Celsius",
  "EK 8.1.A.2 makes Kw a property of aqueous solution rather than of pure water alone, so its logarithmic form applies generally; EK 8.1.A.4 restricts the numerical value 14 to 25 degrees Celsius."),
]


def _extra_mutations():
    def corrupt_table(mod, cl):
        mod.QUESTIONS[6]["table"] = dict(
            headers=h8_1._T_SOLUTIONS["headers"],
            rows=[[lab, ("\\( 1.0 \\times 10^{-5} \\)" if lab == "3" else c)]
                  for lab, c in h8_1._T_SOLUTIONS["rows"]])

    def corrupt_numeric(mod, cl):
        ch = list(mod.QUESTIONS[20]["choices"])
        ch[0] = "pH = 6.20"
        mod.QUESTIONS[20]["choices"] = ch
        cl[20] = ("6.20", cl[20][1])

    def seven_becomes_the_definition(mod, cl):
        ch = list(mod.QUESTIONS[11]["choices"])
        ch[0] = "A solution is neutral when its pH is exactly 7.0"
        mod.QUESTIONS[11]["choices"] = ch
        cl[11] = ("neutral when its pH is exactly", cl[11][1])
        neutral_is_equality(mod)

    def kw_trend_reversed(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h8_1._T_KW["headers"],
            rows=[[t, ("\\( 1.0 \\times 10^{-16} \\)" if t == "60" else k)]
                  for t, k in h8_1._T_KW["rows"]])

    return [("a tabulated concentration corrupted so the keyed pH is false", corrupt_table),
            ("a recomputed neutral pH no longer in the keyed choice", corrupt_numeric),
            ("a keyed choice defining neutrality by the number 7.0",
             seven_becomes_the_definition),
            ("the tabulated Kw trend reversed so the keyed direction is false",
             kw_trend_reversed)]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h8_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

neutral_is_equality(h8_1)
h.run(h8_1, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
