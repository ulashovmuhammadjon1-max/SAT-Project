"""Key audit for AP CHEMISTRY 3.4 Ideal Gas Law.

One (anchor, claim) per item, in module order.

WHAT THE KEYS REST ON.

  3.4.A.1  the macroscopic properties of ideal gases are related through
           PV = nRT                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20, 21,
                                   22, 23, 24, 25
  3.4.A.2  each component's partial pressure is independent of the others, is
           proportional to its mole fraction, and the total is their sum
                                   11, 12, 13, 14, 15, 16, 17, 18, 26, 27, 29, 30
  3.4.A.3  graphical representations of the P, V, T and n relationships are
           useful to describe gas behavior                            28

ARITHMETIC IS THE GATE HERE. This is the most quantitative topic in the unit, so
every number a key asserts is recomputed from the stimulus alone -- thirteen
stem items in ``NUMERIC`` and six tabulated ones in ``TABLE_CHECKS``. Several
checks also recompute the DISTRACTOR, so an item claiming to punish a particular
mistake provably does.

THE CELSIUS TRAP. Item 6 is 27 to 327 degrees Celsius, which doubles the Kelvin
temperature and multiplies the Celsius reading by roughly twelve; ``n6``
recomputes both and asserts the twelve-fold value is a distractor and not the
key. ``no_celsius_proportionality`` then asserts that no key anywhere in the
module makes a quantity proportional to a Celsius temperature.

TWO HALF-SWAPS. Item 16 pairs an UNCHANGED partial pressure with a RISING total,
and item 25 pairs DIRECT proportionality with a constant RATIO. Each keeps a
distractor carrying exactly one of the two clauses, so
``swap_anchors_carry_both_clauses`` requires the anchor to carry both and proves
the ambiguity is real by finding the one-clause distractor.

SCOPE. 3.5 owns the kinetic molecular theory and 3.6 owns every departure from
ideal behaviour, so ``no_other_topic`` asserts neither appears here.

FIGURES. EK 3.4.A.3 is about graphs and this bank cannot show one, so every
relationship is tabulated and ``no_figure_language`` asserts no item points at a
picture.

NEGATIVE CONTROL: ``python3 verify_h3_4.py --selftest``.
"""
import re
import sys

import cg_check as cg
import h_check as h

import h3_4

MOLES = "Moles present"
VOL = "Volume (L)"
PRESS = "Pressure (atm)"
KELVIN = "Kelvin temperature (K)"
NMOL = "Moles of gas"

R = 0.08206  # L atm per mole per kelvin, the value the stem quotes to 3 figures

_FIGURE = re.compile(
    r"(?<![a-z])(diagram|figure|image|picture|as shown|shown below|shown above|"
    r"the graph|graph above|graph below|plotted above|plotted below|the curve)(?![a-z])",
    re.I)

# 3.5 owns the kinetic molecular theory; 3.6 owns every departure from ideality;
# 3.13 owns Beer-Lambert. None of them belong in a topic about the equation.
_OTHER_TOPIC = re.compile(
    r"(?<![A-Za-z])(kinetic molecular theory|Maxwell-Boltzmann|van der Waals|"
    r"deviation|deviations|deviate|deviates|real gas|real gases|Beer-Lambert|"
    r"molar absorptivity)(?![A-Za-z])", re.I)

# A key that makes anything proportional to a CELSIUS temperature is wrong, and
# it is the mistake this topic exists to punish.
_CELSIUS_KEY = "Celsius temperature"


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
    print(f"OK  {module.TOPIC[0]} figures: EK 3.4.A.3's graphical relationships are all "
          "carried as tables; no item points at a picture.")


def no_other_topic(module):
    for i, item in enumerate(module.QUESTIONS, 1):
        for text in _facing(item):
            hit = _OTHER_TOPIC.search(text)
            assert not hit, (
                f"{module.TOPIC[0]} q{i}: uses {hit.group(0)!r}, which is 3.5's or 3.6's "
                f"material -- {text[:70]!r}"
            )
    print(f"OK  {module.TOPIC[0]} scope: no kinetic molecular theory and no departure from "
          "ideality; the topic stays on the equation itself.")


def no_celsius_proportionality(module):
    """No key may make a quantity follow a Celsius reading. EK 3.4.A.1 is in kelvins."""
    seen = 0
    for i, item in enumerate(module.QUESTIONS, 1):
        if cg.contains_phrase(h.keyed(item), _CELSIUS_KEY):
            raise AssertionError(
                f"{module.TOPIC[0]} q{i}: the key makes a quantity follow a Celsius "
                f"temperature -- {h.keyed(item)!r}. EK 3.4.A.1's equation is written in "
                "the Kelvin temperature."
            )
        seen += sum(1 for c in item["choices"] if cg.contains_phrase(c, _CELSIUS_KEY))
    assert seen, (
        "no distractor anywhere offers the Celsius mistake, so this check has nothing to "
        "distinguish and proves nothing"
    )
    print(f"OK  {module.TOPIC[0]} Kelvin guard: {seen} Celsius distractor(s) present and "
          "none of them keyed.")


# Items whose distractor set contains the HALF-SWAP of the key: one of the two
# clauses right and the other wrong. An anchor naming only one clause would
# match that distractor too, which is the ambiguity anchors exist to prevent.
SWAP_ITEMS = {
    16: ("unchanged", "total pressure rises"),
    25: ("directly proportional", "ratio of pressure to Kelvin temperature"),
}


def swap_anchors_carry_both_clauses(module, claims):
    for i, (clause_a, clause_b) in sorted(SWAP_ITEMS.items()):
        anchor = claims[i - 1][0]
        item = module.QUESTIONS[i - 1]

        has_a = cg.contains_phrase(anchor, clause_a)
        has_b = cg.contains_phrase(anchor, clause_b)
        assert has_a and has_b, (
            f"{module.TOPIC[0]} q{i}: the anchor {anchor!r} carries "
            f"{'the first' if has_a else 'the second' if has_b else 'neither'} clause only; "
            f"it must name both {clause_a!r} and {clause_b!r} or a half-swapped key would "
            "match it"
        )

        # Prove the ambiguity is real rather than assumed: some distractor must
        # carry exactly one of the two clauses, which is what a one-clause
        # anchor would have matched.
        half = []
        for k, choice in enumerate(item["choices"]):
            if k == item["ans"]:
                continue
            in_a = cg.contains_phrase(choice, clause_a)
            in_b = cg.contains_phrase(choice, clause_b)
            if in_a != in_b:
                half.append(k)
        assert half, (
            f"{module.TOPIC[0]} q{i}: no distractor carries exactly one of {clause_a!r} and "
            f"{clause_b!r}, so this item is not the half-swap case the check is for"
        )
    print(f"OK  {module.TOPIC[0]} swap guard: {len(SWAP_ITEMS)} anchor(s) carry both "
          "clauses, each with a half-swapped distractor present to make the requirement "
          "bite.")


# ------------------------------------------------------------------ arithmetic

def combined(v1, p1, p2, t1, t2):
    """EK 3.4.A.1: the new volume when pressure and Kelvin temperature both move."""
    return v1 * (p1 / p2) * (t2 / t1)


def n2(item):
    p2 = 2.0 * 6.0 / 2.0
    assert abs(p2 - 6.0) < 1e-12, f"the new pressure recomputes to {p2}"
    inverted = 2.0 * 2.0 / 6.0
    assert abs(inverted - 0.6667) < 1e-3, "the 0.67 atm distractor must be the inverted ratio"
    h.shows(item, f"{p2:.1f} atm")
    return (f"holding the product of pressure and volume fixed gives {p2:g} atm, with the "
            f"inverted volume ratio giving the {inverted:.2f} atm distractor")


def n3(item):
    v2 = 4.0 * 400.0 / 200.0
    assert abs(v2 - 8.0) < 1e-12, f"the new volume recomputes to {v2}"
    h.shows(item, f"{v2:.1f} L")
    return f"volume proportional to the Kelvin temperature gives {v2:g} L from 4.0 L"


def n4(item):
    p2 = 1.5 * 900.0 / 300.0
    assert abs(p2 - 4.5) < 1e-12, f"the new pressure recomputes to {p2}"
    h.shows(item, f"{p2:.1f} atm")
    return f"pressure proportional to the Kelvin temperature gives {p2:g} atm in a rigid vessel"


def n5(item):
    v2 = 3.0 * 1.5 / 0.50
    assert abs(v2 - 9.0) < 1e-12, f"the new volume recomputes to {v2}"
    h.shows(item, f"{v2:.1f} L")
    return f"volume proportional to the amount of gas gives {v2:g} L from 3.0 L"


def n6(item):
    kelvin = 1.00 * (327.0 + 273.0) / (27.0 + 273.0)
    celsius = 1.00 * 327.0 / 27.0
    assert abs(kelvin - 2.00) < 1e-12, f"the Kelvin ratio recomputes to {kelvin}"
    assert abs(celsius - 12.11) < 5e-3, f"the Celsius ratio recomputes to {celsius}"
    assert abs(kelvin - celsius) > 1.0, (
        "the two routes must differ, or the item punishes nothing"
    )
    h.shows(item, f"{kelvin:.2f} atm")
    # The Celsius mistake must be OFFERED and must not be the key.
    wrong = [k for k, c in enumerate(item["choices"])
             if cg.contains_phrase(c, f"{celsius:.1f} atm")]
    assert wrong and item["ans"] not in wrong, (
        f"the Celsius-ratio value {celsius:.1f} atm must appear as a distractor and not as "
        f"the key; it appears at {wrong} with the key at {item['ans']}"
    )
    return (f"the Kelvin ratio 600 to 300 gives {kelvin:.2f} atm while the Celsius ratio 327 "
            f"to 27 gives {celsius:.1f} atm, which is offered as a distractor")


def n7(item):
    factor = combined(1.0, 1.0, 2.0, 1.0, 2.0)
    assert abs(factor - 1.0) < 1e-12, f"the volume factor recomputes to {factor}"
    h.shows(item, "unchanged")
    return (f"doubling pressure and Kelvin temperature together multiplies the volume by "
            f"{factor:g}, so it does not move")


def n8(item):
    v2 = combined(6.0, 3.0, 1.0, 400.0, 200.0)
    assert abs(v2 - 9.0) < 1e-12, f"the new volume recomputes to {v2}"
    h.shows(item, f"{v2:.1f} L")
    return (f"tripling the volume for the pressure drop and halving it for the temperature "
            f"drop gives {v2:g} L")


def n9(item):
    n = 1.00 * 44.8 / (R * 273.0)
    assert abs(n - 2.00) < 5e-3, f"the amount recomputes to {n}"
    h.shows(item, f"{n:.2f} mol")
    return (f"dividing 44.8 L atm by the product of the gas constant and 273 K, which is "
            f"{R * 273.0:.1f} L atm per mole, gives {n:.2f} mol")


def n11(item):
    total = 0.25 + 0.45 + 0.30
    assert abs(total - 1.00) < 1e-12, f"the total pressure recomputes to {total}"
    h.shows(item, f"{total:.2f} atm")
    return f"summing the three stated partial pressures gives {total:.2f} atm"


def n12(item):
    x = 2.0 / (2.0 + 6.0)
    assert abs(x - 0.25) < 1e-12, f"the mole fraction recomputes to {x}"
    wrong = 2.0 / 6.0
    assert abs(wrong - 0.3333) < 1e-3, "the 0.33 distractor must be the ratio to the OTHER gas"
    h.shows(item, f"{x:.2f}")
    return (f"two moles over a total of eight gives {x:g}, with the ratio to the other "
            f"component alone giving the {wrong:.2f} distractor")


def n18(item):
    x = 1.2 / 6.0
    assert abs(x - 0.20) < 1e-12, f"the mole fraction recomputes to {x}"
    inverted = 6.0 / 1.2
    assert inverted > 1.0, "the inverted distractor must exceed one, which no mole fraction can"
    h.shows(item, f"{x:.2f}")
    return (f"the partial pressure over the total gives {x:g}, with the inverted ratio "
            f"giving {inverted:g}, larger than one")


def n26(item):
    third = 3.0 - 1.5 - 0.8
    assert abs(third - 0.7) < 1e-9, f"the third partial pressure recomputes to {third}"
    summed = 1.5 + 0.8
    assert abs(summed - 2.3) < 1e-9, "the 2.30 atm distractor must be the sum of the two given"
    h.shows(item, f"{third:.2f} atm")
    return (f"the total less the two stated partial pressures gives {third:.2f} atm, with "
            f"their sum giving the {summed:.2f} atm distractor")


def n27(item):
    p = 10.0 * (1.0 / (1.0 + 4.0))
    assert abs(p - 2.0) < 1e-12, f"the partial pressure recomputes to {p}"
    other = 10.0 * (4.0 / 5.0)
    assert abs(other - 8.0) < 1e-12, "the 8.0 atm distractor must be the OTHER component's share"
    h.shows(item, f"{p:.1f} atm")
    return (f"a mole fraction of one fifth times the 10.0 atm total gives {p:g} atm, with the "
            f"other component taking {other:g} atm")


NUMERIC = {2: n2, 3: n3, 4: n4, 5: n5, 6: n6, 7: n7, 8: n8, 9: n9, 11: n11,
           12: n12, 18: n18, 26: n26, 27: n27}


# ----------------------------------------------------------------- table items

def _mole_fractions(table):
    ns = dict(zip(cg.labels(table), cg.col(table, MOLES)))
    total = sum(ns.values())
    assert total > 0, f"the tabulated amounts sum to {total}"
    return {lab: n / total for lab, n in ns.items()}, ns, total


def q13(table, item):
    xs, ns, total = _mole_fractions(table)
    p = 4.0 * xs["Gas B"]
    assert abs(p - 1.5) < 1e-12, f"the partial pressure recomputes to {p}"
    h.shows(item, f"{p:.1f} atm")
    return (f"the tabulated amounts {ns} total {total:g} mol, making that component's mole "
            f"fraction {xs['Gas B']:g} and its share of the 4.0 atm total {p:g} atm")


def q14(table, item):
    xs, ns, total = _mole_fractions(table)
    richest = max(xs, key=xs.get)
    assert richest == "Gas C", f"the most abundant tabulated component is {richest}: {ns}"
    assert len([v for v in ns.values() if abs(v - ns[richest]) < 1e-12]) == 1, (
        "the most abundant component must be unique, or the item has no single answer"
    )
    h.shows(item, richest)
    return (f"the tabulated amounts {ns} have a unique maximum at {richest}, which EK "
            f"3.4.A.2 gives the largest mole fraction and so the largest partial pressure")


def q15(table, item):
    xs, ns, total = _mole_fractions(table)
    x = xs["Gas A"]
    assert abs(x - 0.125) < 1e-12, f"the mole fraction recomputes to {x}"
    h.shows(item, f"{x:.3f}")
    return (f"one mole out of the tabulated total of {total:g} mol gives a mole fraction of "
            f"{x:g}")


def q19(table, item):
    vs, ps = cg.col(table, VOL), cg.col(table, PRESS)
    products = [round(v * p, 9) for v, p in zip(vs, ps)]
    assert len(set(products)) == 1, f"the tabulated products of pressure and volume are {products}"
    sums = [round(v + p, 9) for v, p in zip(vs, ps)]
    assert len(set(sums)) > 1, (
        "the tabulated sums must NOT be constant, or the 'sum is constant' distractor is "
        "true as well"
    )
    ratios = [round(p / v, 9) for v, p in zip(vs, ps)]
    assert len(set(ratios)) > 1, (
        "the tabulated ratios must NOT be constant, or the 'directly proportional' "
        "distractor is true as well"
    )
    h.shows(item, "product of pressure and volume is constant")
    return (f"every tabulated row gives the same product {products[0]:g} while the sums "
            f"{sums} and the ratios {ratios} both vary")


def q20(table, item):
    ts, vs = cg.col(table, KELVIN), cg.col(table, VOL)
    ratios = [round(v / t, 9) for t, v in zip(ts, vs)]
    assert len(set(ratios)) == 1, f"the tabulated volume-to-temperature ratios are {ratios}"
    products = [round(v * t, 9) for t, v in zip(ts, vs)]
    assert len(set(products)) > 1, (
        "the tabulated products must NOT be constant, or the 'product' distractor is true too"
    )
    diffs = [round(t - v, 9) for t, v in zip(ts, vs)]
    assert len(set(diffs)) > 1, (
        "the tabulated differences must NOT be constant, or the 'difference' distractor is "
        "true too"
    )
    h.shows(item, "ratio of volume to Kelvin temperature")
    return (f"every tabulated row shares the ratio {ratios[0]:g} L per kelvin while the "
            f"products {products} and differences {diffs} both vary")


def q21(table, item):
    ns, ps = cg.col(table, NMOL), cg.col(table, PRESS)
    slopes = [round(p / n, 9) for n, p in zip(ns, ps)]
    assert len(set(slopes)) == 1, f"the tabulated pressure-per-mole values are {slopes}"
    p = 0.50 * slopes[0]
    assert abs(p - 2.50) < 1e-12, f"the pressure at half a mole recomputes to {p}"
    h.shows(item, f"{p:.2f} atm")
    return (f"the tabulated rows share {slopes[0]:g} atm per mole, so half a mole gives "
            f"{p:.2f} atm")


TABLE_CHECKS = {13: q13, 14: q14, 15: q15, 19: q19, 20: q20, 21: q21}


CLAIMS = [
 ("PV = nRT",
  "EK 3.4.A.1, verbatim: the macroscopic properties of ideal gases are related through the ideal gas law, given as that equation."),
 ("6.0 atm",
  "EK 3.4.A.1 with amount and Kelvin temperature fixed holds the product of pressure and volume constant. Recomputed in n2, which also recomputes the inverted-ratio distractor."),
 ("8.0 L",
  "EK 3.4.A.1 with amount and pressure fixed makes volume proportional to the Kelvin temperature. Recomputed in n3."),
 ("4.5 atm",
  "EK 3.4.A.1 in a rigid vessel makes pressure proportional to the Kelvin temperature. Recomputed in n4."),
 ("9.0 L",
  "EK 3.4.A.1 with pressure and Kelvin temperature fixed makes volume proportional to the amount of gas. Recomputed in n5."),
 ("2.00 atm",
  "EK 3.4.A.1's equation is written in the Kelvin temperature. Recomputed in n6, which also recomputes the Celsius ratio and asserts that value is offered as a distractor rather than keyed."),
 ("unchanged",
  "EK 3.4.A.1 makes volume proportional to the Kelvin temperature and inversely proportional to pressure, so doubling both cancels. Recomputed in n7."),
 ("9.0 L",
  "EK 3.4.A.1 combining both changes at fixed amount. Recomputed in n8 through the same helper used for every combined-change item."),
 ("2.00 mol",
  "EK 3.4.A.1 rearranged for amount. Recomputed in n9 from the stated pressure, volume, Kelvin temperature and gas constant."),
 ("\\frac{nRT}{P}",
  "EK 3.4.A.1 divided through by pressure isolates volume, leaving the amount, gas constant and Kelvin temperature above the line."),
 ("1.00 atm",
  "EK 3.4.A.2: the total pressure of the sample is the sum of the partial pressures. Recomputed in n11."),
 ("0.25",
  "EK 3.4.A.2 defines the mole fraction as moles of that component over TOTAL moles. Recomputed in n12, which also recomputes the ratio-to-the-other-component distractor."),
 ("1.5 atm",
  "EK 3.4.A.2 makes each partial pressure the total times that component's mole fraction. Recomputed in q13 from the tabulated amounts."),
 ("Gas C",
  "EK 3.4.A.2 makes the partial pressure follow the mole fraction, which follows the amount present. q14 recomputes the tabulated amounts and checks the maximum is unique."),
 ("0.125",
  "EK 3.4.A.2's definition of mole fraction applied to the tabulated amounts. Recomputed in q15."),
 ("is unchanged and the total pressure rises",
  "EK 3.4.A.2 makes each component's pressure independent of the others, so the original gas's partial pressure does not move, while the same statement makes the total a sum to which a term has been added. Both clauses are pinned because a half-swapped distractor is present."),
 ("\\frac{n_A}{n_{\\mathrm{total}}}",
  "EK 3.4.A.2 gives the mole fraction as moles A over total moles, a ratio of amounts carrying no pressure, volume or temperature term."),
 ("0.20",
  "EK 3.4.A.2 makes the partial pressure the total times the mole fraction, so the ratio of the two recovers the fraction. Recomputed in n18, which checks the inverted ratio exceeds one."),
 ("product of pressure and volume is constant",
  "EK 3.4.A.1 with amount and Kelvin temperature fixed. q19 recomputes the product for every tabulated row and checks the sums and the ratios both vary, so no other option is true as well."),
 ("ratio of volume to Kelvin temperature",
  "EK 3.4.A.1 with amount and pressure fixed makes volume directly proportional to the Kelvin temperature, and a directly proportional pair keeps a constant ratio. q20 recomputes the ratios, products and differences."),
 ("2.50 atm",
  "EK 3.4.A.1 with volume and Kelvin temperature fixed makes pressure proportional to the amount. q21 recomputes the shared pressure-per-mole from the table and applies it to the new amount."),
 ("no term for the identity of the gas",
  "EK 3.4.A.1 relates pressure, volume, amount and Kelvin temperature and nothing else, so two samples agreeing in the other three must agree in pressure whatever the substances are."),
 ("same number of moles",
  "EK 3.4.A.1's equation fixes the amount once pressure, volume and Kelvin temperature are fixed; equal mass would additionally need molar masses, which the equation does not contain."),
 ("Doubling the Kelvin temperature",
  "EK 3.4.A.1 makes pressure proportional to the Kelvin temperature at fixed volume and amount. A doubled Celsius reading is not a doubled Kelvin temperature, and a rigid container cannot change volume."),
 ("Directly proportional, so the ratio of pressure to Kelvin temperature is constant",
  "EK 3.4.A.1 with volume and amount fixed leaves pressure equal to a constant times the Kelvin temperature. The anchor carries both clauses because distractors offer each half separately."),
 ("0.70 atm",
  "EK 3.4.A.2 makes the total the sum of the partial pressures, so the unknown is the total less the two given. Recomputed in n26, which also recomputes the sum-of-the-two distractor."),
 ("2.0 atm",
  "EK 3.4.A.2 makes each partial pressure the total times its mole fraction. Recomputed in n27, which also recomputes the other component's share."),
 ("useful to describe gas behavior",
  "EK 3.4.A.3, verbatim in substance: graphical representations of the relationships between pressure, volume, temperature and amount are useful to describe gas behavior."),
 ("independent of the other components",
  "EK 3.4.A.2 opens with exactly that: the pressure exerted by each component, its partial pressure, is independent of the other components."),
 ("The mole fraction of that gas",
  "EK 3.4.A.2 states that the partial pressure of a gas within the mixture is proportional to its mole fraction, and defines that fraction as its moles over the total moles."),
]


def _extra_mutations():
    def figure_language(mod, cl):
        mod.QUESTIONS[18]["q"] = "In the graph above, what do the plotted points show?"
        no_figure_language(mod)

    def kmt_creeps_in(mod, cl):
        mod.QUESTIONS[0]["q"] = (mod.QUESTIONS[0]["q"]
                                 + " Use the kinetic molecular theory to decide.")
        no_other_topic(mod)

    def celsius_key(mod, cl):
        # The mistake the topic exists to punish, promoted to the key.
        mod.QUESTIONS[23]["ans"] = 1
        cl[23] = ("Doubling the Celsius temperature", cl[23][1])
        no_celsius_proportionality(mod)

    def celsius_distractor_removed(mod, cl):
        # A control on the CONTROL: with no Celsius distractor anywhere, the
        # guard above would pass over an empty set and prove nothing.
        for item in mod.QUESTIONS:
            item["choices"] = [c.replace("Celsius temperature", "container volume")
                               for c in item["choices"]]
        no_celsius_proportionality(mod)

    def swap_anchor_halved(mod, cl):
        # Only the first clause. The half-swapped distractor -- an unchanged
        # TOTAL with a fallen partial pressure -- carries "unchanged" too.
        cl[15] = ("unchanged", cl[15][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def proportionality_anchor_halved(mod, cl):
        cl[24] = ("Directly proportional", cl[24][1])
        swap_anchors_carry_both_clauses(mod, cl)

    def celsius_ratio_keyed(mod, cl):
        # n6 must reject an item whose key is the Celsius-ratio value.
        mod.QUESTIONS[5]["ans"] = 1
        cl[5] = ("12.1 atm", cl[5][1])

    def pv_table_no_longer_constant(mod, cl):
        mod.QUESTIONS[18]["table"] = dict(
            headers=h3_4._T_PV["headers"],
            rows=[["1.0", "12.0"], ["2.0", "7.0"], ["3.0", "4.0"], ["4.0", "3.0"]])

    def pv_table_made_proportional(mod, cl):
        # Pressure equal to volume in every row: the product is NOT constant and
        # the "directly proportional" distractor becomes the true statement.
        mod.QUESTIONS[18]["table"] = dict(
            headers=h3_4._T_PV["headers"],
            rows=[["1.0", "1.0"], ["2.0", "2.0"], ["3.0", "3.0"], ["4.0", "4.0"]])

    def tv_table_products_also_constant(mod, cl):
        # One row repeated makes every derived quantity constant, so the
        # "product" and "difference" distractors are true as well and the item
        # no longer has a single answer.
        mod.QUESTIONS[19]["table"] = dict(
            headers=h3_4._T_TV["headers"],
            rows=[["100", "2.0"], ["100", "2.0"], ["100", "2.0"], ["100", "2.0"]])

    def np_table_not_proportional(mod, cl):
        mod.QUESTIONS[20]["table"] = dict(
            headers=h3_4._T_NP["headers"],
            rows=[["0.10", "0.50"], ["0.20", "1.10"], ["0.30", "1.50"], ["0.40", "2.00"]])

    def mixture_amounts_tied(mod, cl):
        # Two components tied at the top: the "which is greatest" item loses its
        # single answer.
        mod.QUESTIONS[13]["table"] = dict(
            headers=h3_4._T_MIX["headers"],
            rows=[["Gas A", "1.0"], ["Gas B", "4.0"], ["Gas C", "4.0"]])

    def mixture_amounts_changed(mod, cl):
        # The partial-pressure item recomputes against the table, so changing the
        # amounts falsifies the key even though the stem is untouched.
        mod.QUESTIONS[12]["table"] = dict(
            headers=h3_4._T_MIX["headers"],
            rows=[["Gas A", "1.0"], ["Gas B", "1.0"], ["Gas C", "6.0"]])

    return [
        ("a stem referring to a graph the bank cannot show", figure_language),
        ("the kinetic molecular theory creeping in from 3.5", kmt_creeps_in),
        ("the Celsius mistake promoted to a key", celsius_key),
        ("every Celsius distractor removed, so the Kelvin guard would run over an empty set",
         celsius_distractor_removed),
        ("the partial-pressure anchor cut to one clause, which the half-swapped distractor "
         "also carries", swap_anchor_halved),
        ("the proportionality anchor cut to one clause", proportionality_anchor_halved),
        ("the Celsius-ratio value keyed instead of offered as a distractor", celsius_ratio_keyed),
        ("the pressure-volume table given a row whose product differs", pv_table_no_longer_constant),
        ("the pressure-volume table made directly proportional, so a distractor becomes true",
         pv_table_made_proportional),
        ("the temperature-volume table flattened to one repeated row, so every distractor "
         "becomes true as well", tv_table_products_also_constant),
        ("the amount-pressure table given a row off the proportional line", np_table_not_proportional),
        ("two tabulated components tied for the largest amount", mixture_amounts_tied),
        ("the tabulated amounts changed under an unchanged stem", mixture_amounts_changed),
    ]


if __name__ == "__main__" and "--selftest" in sys.argv:
    h.selftest(h3_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC,
               mutations=_extra_mutations())

no_figure_language(h3_4)
no_other_topic(h3_4)
no_celsius_proportionality(h3_4)
swap_anchors_carry_both_clauses(h3_4, CLAIMS)
h.run(h3_4, CLAIMS, table_checks=TABLE_CHECKS, numeric_checks=NUMERIC)
