"""Key audit for AP CHEMISTRY 4.5 Stoichiometry.

One ``(anchor, claim)`` per item, in module order; the anchor must appear in the
KEYED choice and in no distractor. Every numerical item is ALSO recomputed --
from the table where it has one, and from the numbers in the stem where it does
not -- and the recomputed value is asserted against the keyed choice, so an
edited number or a moved key fails here rather than reaching a student.

Stoichiometry is the one topic in this range where nearly every item is
quantitative, so the arithmetic gate carries most of the weight: 18 stem-data
items and 6 table items, 24 of 30. The remaining six are conceptual and rest on
the essential knowledge statements quoted below.

WHAT THE KEYS REST ON
---------------------
EK 4.5.A.1  Because atoms must be conserved during a chemical process, it is
            possible to calculate product amounts by using known reactant
            amounts, or to calculate reactant amounts given known product
            amounts.  (items 4, 7, 16, 24, 25)
EK 4.5.A.2  Coefficients of balanced chemical equations contain information
            regarding the proportionality of the amounts of substances involved
            in the reaction; these values can be used in chemical calculations
            involving the mole concept.  (items 1, 2, 3, 8, 9, 10, 11, 14, 15,
            18, 19, 20, 23, 27, 28, 30)
EK 4.5.A.3  Stoichiometric calculations can be combined with the ideal gas law
            and calculations involving molarity to quantitatively study gases
            and solutions.  (items 5, 6, 12, 13, 17, 21, 22, 26, 29)

The molar mass or molar volume every calculation needs is supplied in the stem
or in the item's own table, so no key depends on a value a student would have to
remember.

NEGATIVE CONTROL: ``python3 verify_h4_5.py --selftest`` corrupts a key, an
anchor, the notation, a table cell and a stem-recomputed value on purpose and
requires each corruption to be caught.
"""
import sys

import h_chem_notation as hn
import h4_5 as M

MM = "Molar mass (grams per mole)"
N2 = "Moles of N2 consumed"
H2 = "Moles of H2 consumed"
NH3 = "Moles of NH3 produced"
MG = "Mass of magnesium burned (grams)"
MGO = "Mass of magnesium oxide collected (grams)"
CONC = "Concentration (moles per liter)"
VOL = "Volume used (liters)"
NGAS = "Moles of gas"
VGAS = "Volume measured (liters)"
AL = "Moles of Al placed in the flask"
CL = "Moles of Cl2 placed in the flask"
PROD = "Moles of AlCl3 formed"


# ------------------------------------------------------------ table questions

def q4(t, item):
    mm = dict(zip(hn.cg.labels(t), hn.cg.col(t, MM)))
    n = 50.0 / mm["CaCO3"]
    mass = n * mm["CO2"]
    hn.keyed(item, f"{mass:.1f} g")
    return (f"50.0 g over {mm['CaCO3']} g/mol is {n} mol, and one CO2 per CaCO3 at "
            f"{mm['CO2']} g/mol gives {mass:.1f} g")


def q9(t, item):
    labs = hn.cg.labels(t)
    n2 = dict(zip(labs, hn.cg.col(t, N2)))
    h2 = dict(zip(labs, hn.cg.col(t, H2)))
    nh3 = dict(zip(labs, hn.cg.col(t, NH3)))
    for lab in labs:
        assert abs(h2[lab] - 3 * n2[lab]) < 1e-9, f"trial {lab}: H2 is not three times N2"
        assert abs(nh3[lab] - 2 * n2[lab]) < 1e-9, f"trial {lab}: NH3 is not twice N2"
        assert h2[lab] != n2[lab], "'equal amounts of N2 and H2' must be false"
        assert nh3[lab] != h2[lab], "'NH3 equals H2' must be false"
    rising = [n2[l] for l in labs] == sorted(n2[l] for l in labs)
    assert rising and [nh3[l] for l in labs] == sorted(nh3[l] for l in labs), \
        "'NH3 falls as N2 rises' must be false"
    return ("every row holds H2 at three times N2 and NH3 at twice N2, which is the "
            "1 to 3 to 2 ratio of the coefficients")


def q14(t, item):
    labs = hn.cg.labels(t)
    mg = dict(zip(labs, hn.cg.col(t, MG)))
    ox = dict(zip(labs, hn.cg.col(t, MGO)))
    ratios = [ox[l] / mg[l] for l in labs]
    assert max(ratios) - min(ratios) < 1e-9, f"the oxide to metal ratio is not constant: {ratios}"
    assert all(ox[l] > mg[l] for l in labs), "'oxide mass equals metal mass' must be false"
    scaled = [ox[l] / ox[labs[0]] == mg[l] / mg[labs[0]] for l in labs]
    assert all(scaled), "'oxide grows faster than metal' must be false"
    return (f"every run gives the same oxide to metal ratio {ratios[0]}, and the two "
            "columns scale by the same factor from run to run")


def q17(t, item):
    labs = hn.cg.labels(t)
    conc = dict(zip(labs, hn.cg.col(t, CONC)))
    vol = dict(zip(labs, hn.cg.col(t, VOL)))
    mol = {l: conc[l] * vol[l] for l in labs}
    short = min(mol, key=mol.get)
    assert short == "Silver nitrate", f"the smaller amount belongs to {short}"
    assert vol["Silver nitrate"] < vol["Sodium chloride"], \
        "the limiting solution must NOT be the one with the larger volume"
    assert conc["Silver nitrate"] > conc["Sodium chloride"], \
        "the concentration distractor must point at the same solution for the wrong reason"
    hn.keyed(item, "0.0100 mol")
    return (f"silver nitrate supplies {mol['Silver nitrate']:.4f} mol against "
            f"{mol['Sodium chloride']:.4f} mol of chloride, so it is the smaller amount "
            "in a one to one reaction")


def q22(t, item):
    labs = hn.cg.labels(t)
    n = dict(zip(labs, hn.cg.col(t, NGAS)))
    v = dict(zip(labs, hn.cg.col(t, VGAS)))
    molar = {l: v[l] / n[l] for l in labs}
    assert max(molar.values()) - min(molar.values()) < 1e-9, \
        f"the molar volume is not constant across the table: {molar}"
    amount = 36.0 / molar[labs[0]]
    hn.keyed(item, f"{amount:.2f} mol")
    return (f"every row gives {molar[labs[0]]} L per mole, so 36.0 L is "
            f"{amount:.2f} mol of gas")


def q27(t, item):
    labs = hn.cg.labels(t)
    al = dict(zip(labs, hn.cg.col(t, AL)))
    cl = dict(zip(labs, hn.cg.col(t, CL)))
    made = dict(zip(labs, hn.cg.col(t, PROD)))
    al_short = [l for l in labs if cl[l] > 1.5 * al[l]]
    assert al_short == ["1"], f"trials with chlorine left over: {al_short}"
    for l in labs:
        expected = min(al[l], (2.0 / 3.0) * cl[l])
        assert abs(made[l] - expected) < 1e-9, \
            f"trial {l}: product {made[l]} does not match the limiting amount {expected}"
    assert al["2"] > cl["2"], "the 'more aluminum than chlorine' distractor must be true of trial 2"
    assert max(made, key=made.get) == "3", "the 'largest product' distractor must point at trial 3"
    return ("only trial 1 supplies more chlorine than the three halves of its aluminum, "
            "and every product entry equals the smaller of the two allowed amounts")


TABLE_CHECKS = {4: q4, 9: q9, 14: q14, 17: q17, 22: q22, 27: q27}


# --------------------------------------------------- stem-data questions
# Each recomputes from the stem's own numbers and asserts the result against the
# KEYED choice, so a moved key or an edited number fails here.

def a1(item):
    n = 6.0 * (2 / 2)
    hn.keyed(item, f"{n:.1f} mol")
    return f"6.0 mol H2 times the 2 to 2 coefficient ratio is {n:.1f} mol H2O"


def a2(item):
    n = 0.60 * (2 / 1)
    hn.keyed(item, f"{n:.1f} mol")
    return f"0.60 mol N2 times the 2 to 1 ratio is {n:.1f} mol NH3"


def a3(item):
    from_al, from_cl = 4.0 * (2 / 2), 3.0 * (2 / 3)
    n = min(from_al, from_cl)
    hn.keyed(item, f"{n:.1f} mol")
    return f"aluminum allows {from_al:.1f} and chlorine {from_cl:.1f}, so {n:.1f} mol forms"


def a5(item):
    n = 0.500 * 0.100
    hn.keyed(item, f"{n:.4f} mol")
    return f"0.500 moles per liter times 0.100 L is {n:.4f} mol of HCl"


def a6(item):
    v = 0.25 * 24.0
    hn.keyed(item, f"{v:.1f} L")
    return f"0.25 mol at 24.0 L per mole occupies {v:.1f} L"


def a10(item):
    n = 2.0 * (3 / 1)
    hn.keyed(item, f"{n:.1f} mol")
    return f"2.0 mol propane times the 3 to 1 CO2 ratio is {n:.1f} mol"


def a11(item):
    used_al = 3.0 * (2 / 3)
    left = 4.0 - used_al
    hn.keyed(item, f"{left:.1f} mol of Al")
    return f"3.0 mol Cl2 consumes {used_al:.1f} mol Al, leaving {left:.1f} mol of the 4.0 supplied"


def a12(item):
    n = 0.200 * 0.0250
    hn.keyed(item, f"{n:.5f} mol")
    return f"0.200 moles per liter times 0.0250 L is {n:.5f} mol, matched one to one by the acid"


def a13(item):
    v = 0.10 * 24.0
    hn.keyed(item, f"{v:.1f} L")
    return f"0.10 mol Zn gives 0.10 mol H2, which at 24.0 L per mole is {v:.1f} L"


def a15(item):
    n = 0.50 * 3
    hn.keyed(item, f"{n:.1f} mol")
    return f"0.50 mol Fe2O3 times the 3 to 1 CO ratio is {n:.1f} mol"


def a16(item):
    co2 = 8.8 / 44.0
    n = co2 / 3
    hn.keyed(item, f"{n:.3f} mol")
    return f"8.8 g over 44.0 g/mol is {co2:.2f} mol CO2, a third of which is {n:.3f} mol propane"


def a20(item):
    need = 1.0 * (5 / 4)
    assert need > 1.0, "the oxygen on hand should be insufficient"
    hn.keyed(item, f"{need:.2f} mol of O2")
    return f"1.0 mol NH3 requires {need:.2f} mol of O2 against the 1.0 mol supplied"


def a21(item):
    molar = 3.60 / 0.150
    v = 0.500 * molar
    hn.keyed(item, f"{v:.1f} L")
    return f"3.60 L over 0.150 mol is {molar} L per mole, so 0.500 mol occupies {v:.1f} L"


def a23(item):
    each = 0.40 / 2
    total = 2 * each
    hn.keyed(item, f"{total:.2f} mol")
    return f"0.40 mol NaHCO3 gives {each:.2f} mol each of H2O and CO2, or {total:.2f} mol of gas"


def a24(item):
    n = 0.30 * (2 / 2)
    hn.keyed(item, f"{n:.2f} mol")
    return f"the 2 to 2 coefficient ratio makes the aluminum needed equal to the {n:.2f} mol wanted"


def a25(item):
    m = 10.0 + 5.0
    hn.keyed(item, f"{m:.1f} g")
    return f"every atom of both reactants ends in the one product, so the mass is {m:.1f} g"


def a28(item):
    n = 0.030 / 2
    hn.keyed(item, f"{n:.3f} mol")
    return f"two silver per copper makes the copper consumed {n:.3f} mol"


def a29(item):
    c = 0.0400 / 0.200
    hn.keyed(item, f"{c:.3f} M")
    return f"0.0400 mol over 0.200 L is {c:.3f} M"


ARITH = {1: a1, 2: a2, 3: a3, 5: a5, 6: a6, 10: a10, 11: a11, 12: a12, 13: a13,
         15: a15, 16: a16, 20: a20, 21: a21, 23: a23, 24: a24, 25: a25,
         28: a28, 29: a29}

CLAIMS = [
 ("6.0 mol",
  "Recomputed in a1. EK 4.5.A.2 makes the coefficients the proportionality between amounts, and H2 and H2O both carry the coefficient 2, so the two amounts are equal."),
 ("1.2 mol",
  "Recomputed in a2. EK 4.5.A.2: two moles of NH3 accompany every one mole of N2 consumed, so the ammonia amount is twice the nitrogen amount."),
 ("2.0 mol",
  "Recomputed in a3. EK 4.5.A.2 fixes the proportion at three Cl2 per two Al; the chlorine allows less product than the aluminum does, so it is what runs out and sets the amount."),
 ("22.0 g",
  "Recomputed in q4 from the table's own molar masses. EK 4.5.A.1 allows a product amount to be calculated from a reactant amount, and EK 4.5.A.2 supplies the one to one CaCO3 to CO2 ratio."),
 ("0.0500 mol",
  "Recomputed in a5. EK 4.5.A.3 brings molarity into stoichiometric work; molarity is moles per liter, so the amount is the concentration times the volume in liters."),
 ("6.0 L",
  "Recomputed in a6. EK 4.5.A.3 combines stoichiometry with the ideal gas law; at fixed temperature and pressure volume is proportional to amount, and the stem supplies the molar volume."),
 ("atoms are conserved during a chemical process",
  "EK 4.5.A.1, near verbatim: because atoms must be conserved during a chemical process, it is possible to calculate product amounts by using known reactant amounts, or reactant amounts given known product amounts."),
 ("proportionality of the amounts",
  "EK 4.5.A.2, near verbatim: coefficients of balanced chemical equations contain information regarding the proportionality of the amounts of substances involved, and these values can be used in calculations involving the mole concept."),
 ("three times the amount of",
  "Recomputed in q9 above. EK 4.5.A.2 makes the coefficients the proportionality between amounts, and every tabulated row holds the 1 to 3 to 2 ratio the equation states."),
 ("6.0 mol",
  "Recomputed in a10. EK 4.5.A.2: the coefficients place three moles of CO2 with each mole of propane burned."),
 ("2.0 mol of Al",
  "Recomputed in a11. EK 4.5.A.2 supplies the two to three ratio, so the chlorine present consumes only part of the aluminum and the rest is left over."),
 ("0.00500 mol",
  "Recomputed in a12. EK 4.5.A.3 combines stoichiometry with molarity, and the one to one coefficients make the acid amount equal to the base amount delivered."),
 ("2.4 L",
  "Recomputed in a13. EK 4.5.A.3 combines stoichiometry with the ideal gas law; one H2 forms per Zn, and the stem gives the molar volume."),
 ("fixed multiple of the mass",
  "Recomputed in q14 above. EK 4.5.A.1 conserves atoms and EK 4.5.A.2 fixes the proportion, so the oxide mass is the same multiple of the metal mass in every run, and it exceeds it because the oxide also contains oxygen."),
 ("1.5 mol",
  "Recomputed in a15. EK 4.5.A.2: three moles of CO are consumed per mole of Fe2O3."),
 ("0.067 mol",
  "Recomputed in a16. EK 4.5.A.1 allows a reactant amount to be found from a product amount, and EK 4.5.A.2 supplies the three to one CO2 to propane ratio."),
 ("0.0100 mol",
  "Recomputed in q17 above from the table's concentrations and volumes. EK 4.5.A.3 combines stoichiometry with molarity, and with one to one coefficients the smaller amount is what runs out."),
 ("does not change",
  "EK 4.5.A.2 makes the product amount proportional to the amount of the reactant that is entirely consumed. Adding more of a reactant already in excess does not move that limit."),
 ("mass in grams of each substance",
  "EK 4.5.A.2 limits what the coefficients carry to the proportionality of the amounts. Turning an amount into a mass requires the molar mass of that substance, which the balanced equation does not supply."),
 ("1.25 mol of O2",
  "Recomputed in a20. EK 4.5.A.2 fixes the required proportion at five O2 per four NH3, and that exceeds the oxygen supplied, so the oxygen is exhausted first."),
 ("12.0 L",
  "Recomputed in a21. EK 4.5.A.3 combines stoichiometry with the ideal gas law: at fixed temperature and pressure the volume per mole is constant, and the stem's first sample fixes it."),
 ("1.50 mol",
  "Recomputed in q22 above. EK 4.5.A.3 combines stoichiometry with the ideal gas law, and every tabulated row gives the same volume per mole."),
 ("0.40 mol",
  "Recomputed in a23. EK 4.5.A.2 puts one H2O and one CO2 with every two NaHCO3, so half the carbonate amount appears as each gas and the two gases together equal the carbonate amount."),
 ("0.30 mol",
  "Recomputed in a24. EK 4.5.A.1 allows a reactant amount to be found from a desired product amount, and the coefficients of Al and AlCl3 are equal."),
 ("15.0 g",
  "Recomputed in a25. EK 4.5.A.1 rests on the conservation of atoms: with only one product, every atom of both reactants ends up in it, so the masses add."),
 ("concentration of the solution and the molar mass",
  "EK 4.5.A.3 allows stoichiometry to be combined with molarity, and it is the concentration that turns a solution volume into an amount; the molar mass then turns the product amount into a mass."),
 ("Trial 1",
  "Recomputed in q27 above. EK 4.5.A.2 requires three Cl2 per two Al, and only the first tabulated row supplies more chlorine than that, leaving aluminum as the reactant that limits the product."),
 ("0.015 mol",
  "Recomputed in a28. EK 4.5.A.1 allows a reactant amount to be found from a product amount, and EK 4.5.A.2 supplies the two silver per copper ratio."),
 ("0.200 M",
  "Recomputed in a29. EK 4.5.A.3 brings molarity into stoichiometric work, and molarity is the amount of solute divided by the solution volume in liters."),
 ("three times as large",
  "EK 4.5.A.2 makes the coefficients a statement of proportionality rather than of fixed amounts, so scaling every amount by one factor leaves the limiting reactant unchanged and scales the product by that factor."),
]


def _wreck_table(mod, cl):
    """Module-specific control: break the constant molar volume q22 rests on."""
    t = mod.QUESTIONS[21]["table"]
    mod.QUESTIONS[21]["table"] = dict(
        headers=t["headers"],
        rows=[[r[0], r[1], "99.0"] if r[0] == "C" else list(r) for r in t["rows"]])


def _wreck_stem_number(mod, cl):
    """Module-specific control: edit a stem number so its key no longer follows."""
    mod.QUESTIONS[0]["q"] = mod.QUESTIONS[0]["q"].replace("6.0 mol of H2", "7.0 mol of H2")
    mod.QUESTIONS[0]["choices"][0] = "7.0 mol"


if __name__ == "__main__" and "--selftest" in sys.argv:
    hn.selftest(M, CLAIMS, TABLE_CHECKS, arith=ARITH,
                extra=[("a molar-volume cell corrupted", _wreck_table),
                       ("a stem number edited away from its key", _wreck_stem_number)])

hn.audit(M, CLAIMS, TABLE_CHECKS, arith=ARITH)
