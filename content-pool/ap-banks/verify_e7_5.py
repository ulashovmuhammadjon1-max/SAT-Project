"""Key audit for AP ENVIRONMENTAL SCIENCE 7.5 Indoor Air Pollutants.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
Items 1 and 26 rest on STB-2.E.1, carbon monoxide as an indoor air pollutant
classified as an asphyxiant. The only content presupposed is what an asphyxiant
is -- an agent that interferes with the oxygen the body needs -- which is what
the classification means and is why the framework uses it in place of a bare
name.
Item 2 rests on STB-2.E.2, the indoor particulates asbestos, dust and smoke.
Items 3 and 18 rest on STB-2.E.3, the three kinds of indoor source.
Items 4 and 21 rest on STB-2.E.4 and STB-2.E.5, the natural and the human-made
lists; items 5, 23 and 28 rest on STB-2.E.5 alone; items 6, 19 and 24 on
STB-2.E.6, the combustion list.
Items 7, 11 and 22 rest on STB-2.E.7, radon-222 as a naturally occurring
radioactive gas produced by the decay of uranium found in some rocks and soils.
Items 8, 9, 10, 16, 17, 20, 25 and 27 rest on STB-2.F.1, the routes by which
radon infiltrates a home: up through the soil and in via the basement or cracks
in the walls or foundation, and dissolved in groundwater entering through a
well.
Items 12 and 29 rest on STB-2.F.2, radon-induced lung cancer as the second
leading cause of lung cancer in America.
Items 13, 14 and 15 read data under suggested skill 5.C against the combustion
and human-made lists.
Item 30 states the two learning objectives themselves.

DUST APPEARS TWICE in the framework -- as an indoor particulate in STB-2.E.2 and
as a natural source pollutant in STB-2.E.4 -- so no item asks a student to
assign it to one list to the exclusion of the other.

WHAT IS NOT CLAIMED. No action level, no safe concentration, no ventilation
rate, no half-life and no named product or statute; the framework states none.
The only quantity it gives is the ranking in STB-2.F.2, and that is quoted
rather than computed.

DATA ITEMS: 8, 9, 11, 13, 14, 15 and 16 carry tables and every keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e7_5.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_5

HEIGHT = "Height above the soil surface (meters)"
RN_HOUSE = "Radon measured (picocuries per liter)"
RN_BASE = "Radon measured in the basement (picocuries per liter)"
URANIUM = "Uranium in the underlying rock (parts per million)"
RN_AVG = "Average indoor radon (picocuries per liter)"
CO = "Carbon monoxide after two hours (parts per million)"
HCHO = "Formaldehyde measured indoors (parts per billion)"
PM = "Fine particulates measured (micrograms per cubic meter)"
RN_WATER = "Radon in the water (picocuries per liter)"
RN_AIR = "Radon in the bathroom air after showering (picocuries per liter)"


def q8(table, item):
    levels = cg.labels(table)
    height = cg.col(table, HEIGHT)
    radon = cg.col(table, RN_HOUSE)
    pairs = sorted(zip(height, radon))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"radon does not fall with height: {pairs}"
    assert levels[radon.index(max(radon))] == "Basement", "the maximum is not in the basement"
    assert levels[radon.index(min(radon))] == "Attic", "'highest in the attic' must be false"
    assert len(set(radon)) == len(radon), "'the same on every level' must be false"
    return (f"sorted by height above the soil the readings are {[r for _, r in pairs]}, "
            "strictly decreasing, with the largest at the basement and the smallest in the attic")


def q9(table, item):
    houses = cg.labels(table)
    sealed = {r[0]: r[1] for r in table["rows"]}
    radon = dict(zip(houses, cg.col(table, RN_BASE)))
    assert set(sealed.values()) <= {"yes", "no"}, f"the treatment column is not yes or no: {sealed}"
    treated = [h for h in houses if sealed[h] == "yes"]
    untreated = [h for h in houses if sealed[h] == "no"]
    assert treated and untreated, "both kinds of house must appear"
    assert max(radon[h] for h in treated) < min(radon[h] for h in untreated), \
        f"the treated homes are not all below the untreated: {radon}"
    assert radon[min(radon, key=radon.get)] == min(radon.values()) and \
        sealed[min(radon, key=radon.get)] == "yes", \
        "'the lowest reading came from an unsealed home' must be false"
    return (f"the sealed and vented homes read {[radon[h] for h in treated]} against "
            f"{[radon[h] for h in untreated]} in the untreated homes, every treated value lower")


def q11(table, item):
    hoods = cg.labels(table)
    ura = cg.col(table, URANIUM)
    radon = cg.col(table, RN_AVG)
    assert [h for _, h in sorted(zip(ura, hoods))] == \
           [h for _, h in sorted(zip(radon, hoods))], "the two rankings differ"
    assert radon[ura.index(max(ura))] == max(radon), "the most uranium does not carry the most radon"
    assert radon[ura.index(min(ura))] == min(radon), "'highest where uranium is lowest' must be false"
    assert len(set(radon)) == len(radon), "'the same in all four' must be false"
    return (f"ranking by uranium and by indoor radon both give "
            f"{[h for _, h in sorted(zip(ura, hoods))]}, so the two rise together")


def q13(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, CO)))
    unvented = vals["Unvented fuel-burning heater running"]
    vented = vals["Same heater running with the flue open to the outside"]
    off = vals["Heater switched off"]
    assert unvented > 3 * vented, f"venting does not reduce the reading sharply: {unvented} to {vented}"
    assert vented > off, "the vented condition should still exceed the heater switched off"
    assert off == min(vals.values()), "'highest when switched off' must be false"
    assert len(set(vals.values())) == 3, "'the same in all three conditions' must be false"
    return (f"the unvented condition reads {unvented:.0f} parts per million against "
            f"{vented:.0f} vented and {off:.0f} with the heater off")


def q14(table, item):
    vals = cg.col(table, HCHO)
    ages = cg.labels(table)
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)), \
        f"formaldehyde does not fall as the furnishings age: {vals}"
    assert ages[0].startswith("New"), "the rows must run from newest to oldest"
    assert vals[0] == max(vals) and vals[-1] == min(vals), \
        "the newest room must hold the largest value and the oldest the smallest"
    return (f"from newest to oldest the readings are {vals}, falling at every step, so the "
            "newest furnishings carry the largest value")


def q15(table, item):
    rooms = cg.labels(table)
    smoked = {r[0]: r[1] for r in table["rows"]}
    pm = dict(zip(rooms, cg.col(table, PM)))
    assert set(smoked.values()) <= {"yes", "no"}, f"the smoking column is not yes or no: {smoked}"
    with_s = [r for r in rooms if smoked[r] == "yes"]
    without = [r for r in rooms if smoked[r] == "no"]
    assert len(with_s) == 2 and len(without) == 2, "two rooms of each kind are required"
    assert min(pm[r] for r in with_s) > max(pm[r] for r in without), \
        f"not every smoking room exceeds every other room: {pm}"
    return (f"the smoking rooms read {[pm[r] for r in with_s]} against "
            f"{[pm[r] for r in without]} in the rooms without smoking, every value higher")


def q16(table, item):
    water = dict(zip(cg.labels(table), cg.col(table, RN_WATER)))
    air = dict(zip(cg.labels(table), cg.col(table, RN_AIR)))
    well, town = "Private well", "Treated municipal supply"
    assert water[well] > water[town], "the well supply must carry more radon in its water"
    assert air[well] > air[town], "the well supply must carry more radon in its bathroom air"
    assert water[well] != water[town] and air[well] != air[town], "'the same in both' must be false"
    return (f"the well home reads {water[well]:.0f} in water and {air[well]:.1f} in air against "
            f"{water[town]:.0f} and {air[town]:.1f} on the municipal supply, larger in both columns")


CLAIMS = [
 ("delivery of oxygen the body needs",
  "STB-2.E.1 states that carbon monoxide is an indoor air pollutant classified as an asphyxiant, and an asphyxiant is an agent that deprives the body of the oxygen it needs. Carbon monoxide is a gas rather than a particulate under STB-2.E.2, it is not radioactive as radon is under STB-2.E.7, and the framework attributes no skin or eye effect to it."),
 ("Asbestos, dust, and smoke",
  "STB-2.E.2 verbatim: indoor air pollutants that are classified as particulates include asbestos, dust, and smoke. Carbon monoxide, radon and formaldehyde are gases, the third list is clean air, and the fourth belongs to the outdoor chemistry of STB-2.A and STB-2.B."),
 ("Natural sources, human-made sources, and combustion",
  "STB-2.E.3 verbatim, and STB-2.E.4 to STB-2.E.6 populate exactly those three categories. The point-source and primary-secondary groupings belong to STB-3.A and STB-2.A.5 and are not the indoor classification."),
 ("Radon, mold, and dust",
  "STB-2.E.4 verbatim: common natural source indoor air pollutants include radon, mold, and dust. The rejected lists are drawn from the human-made examples of STB-2.E.5 and the combustion examples of STB-2.E.6."),
 ("Insulation, formaldehyde from building materials, and lead from paints",
  "STB-2.E.5 near verbatim: common human-made indoor air pollutants include insulation, VOCs from furniture, paneling and carpets, formaldehyde from building materials, furniture, upholstery and carpeting, and lead from paints. The rejected options are the natural list, the combustion list, and two settings for radon."),
 ("nitrogen oxides, sulfur dioxide, particulates, and tobacco smoke",
  "STB-2.E.6 verbatim: common combustion air pollutants include carbon monoxide, nitrogen oxides, sulfur dioxide, particulates, and tobacco smoke. Radon and mold belong to STB-2.E.4, formaldehyde and insulation to STB-2.E.5, and ores and allergens appear in no list."),
 ("decay of uranium found in some rocks and soils",
  "STB-2.E.7 near verbatim: radon-222 is a naturally occurring radioactive gas produced by the decay of uranium found in some rocks and soils. Combustion, solvent evaporation, mold growth and asbestos wear are separate indoor sources of other pollutants."),
 ("highest at the level closest to the soil",
  "Recomputed in q8 above: sorted by height above the soil the readings fall at every step, with the maximum in the basement and the minimum in the attic. STB-2.F.1 has radon move up through the soil and enter via the basement."),
 ("sealed foundations and vented basements recorded lower radon",
  "Recomputed in q9 above: every treated home reads below every untreated home. STB-2.F.1 gives the basement and cracks in the walls or foundation as the entry routes, so closing them is expected to reduce what accumulates."),
 ("in through the basement or cracks in the walls or foundation",
  "STB-2.F.1 near verbatim: radon gas infiltrates homes as it moves up through the soil and enters via the basement or cracks in the walls or foundation. The framework gives no route through the roof, through a shared wall, or through wiring."),
 ("rises with the amount of uranium in the underlying rock",
  "Recomputed in q11 above: ranking the neighborhoods by uranium in the rock gives the same order as ranking them by indoor radon. STB-2.E.7 makes the decay of uranium in rocks and soils the source of the gas."),
 ("second leading cause of lung cancer in America",
  "STB-2.F.2 verbatim: exposure to radon gas can lead to radon-induced lung cancer, which is the second leading cause of lung cancer in America. Fiber-related disease belongs to EIN-3.C.3, asphyxiation to STB-2.E.1, and no hearing or skin effect is attributed to radon."),
 ("runs without venting and falls sharply",
  "Recomputed in q13 above: the unvented condition exceeds the vented condition several fold and the heater switched off is the smallest of the three. STB-2.E.6 lists carbon monoxide among the common combustion air pollutants."),
 ("highest where the pressed-wood furniture is newest",
  "Recomputed in q14 above: the readings fall at every step from the newest furnishings to the oldest. STB-2.E.5 names formaldehyde from building materials, furniture, upholstery and carpeting among the human-made indoor pollutants."),
 ("rooms where tobacco was smoked carry higher particulate concentrations",
  "Recomputed in q15 above: both smoking rooms read above both rooms without smoking. Tobacco smoke is in the combustion list of STB-2.E.6 and smoke is in the particulate list of STB-2.E.2."),
 ("more radon in its water and more radon in its bathroom air",
  "Recomputed in q16 above: the well-supplied home carries the larger value in both columns. STB-2.F.1 states that radon is also dissolved in groundwater that enters homes through a well, a second route alongside soil gas."),
 ("Radon entering from the soil beneath the house",
  "STB-2.F.1 makes the basement and cracks in the walls or foundation the entry routes for radon moving up through the soil, so sealing and venting address exactly that pollutant. Formaldehyde, lead, asbestos and mold originate inside the building."),
 ("natural sources and from human-made materials in the building",
  "STB-2.E.3 gives three kinds of indoor source, so removing combustion leaves the natural sources of STB-2.E.4 and the human-made materials of STB-2.E.5. Nothing in the framework confines indoor pollution to combustion or seals a building from outdoor air."),
 ("list of common combustion air pollutants",
  "STB-2.E.6 lists carbon monoxide, nitrogen oxides, sulfur dioxide, particulates and tobacco smoke together, so all three named in the stem belong to that one list. None of the three is radioactive, released from paint, or produced by mold."),
 ("basement air with the radon concentration in the water",
  "STB-2.F.1 gives two routes, soil gas through the foundation and radon dissolved in well water, so distinguishing them requires measuring both. Counting cracks without measuring radon, a distant outdoor reading and a paint analysis test neither route."),
 ("released by the furnishings",
  "STB-2.E.5 names volatile organic compounds from furniture, paneling and carpets and formaldehyde from furnishings among the human-made indoor pollutants, and the furnishings are the only difference the stem leaves between the rooms. Radon, carbon monoxide, sulfur dioxide and mold have sources the stem holds equal."),
 ("moves into the building",
  "STB-2.E.7 places the production of radon in the decay of uranium in rocks and soils, outside the building, and STB-2.F.1 describes it infiltrating the home from there. It is not manufactured, not a combustion product, not a paint constituent, and no indoor photochemical route is given for it."),
 ("with paints as its source",
  "STB-2.E.5 names lead from paints among the common human-made indoor air pollutants, so deteriorating paint is the source at issue. Radon comes from soil under STB-2.F.1, carbon monoxide and nitrogen oxides from combustion under STB-2.E.6, and mold is a natural source under STB-2.E.4."),
 ("Combustion inside the home is one source",
  "STB-2.E.6 lists particulates among the common combustion air pollutants and STB-2.E.2 lists smoke among the indoor particulates, so burning things indoors is a source of them. Radon and formaldehyde are gases and are not what a particulate monitor records."),
 ("rises while the appliance is running",
  "STB-2.E.6 attributes carbon monoxide and particulates to combustion, and a concentration that tracks the operation of an appliance is what ties a pollutant to it. The basement gradient, the uranium-rich rock and the private well are the radon patterns of STB-2.E.7 and STB-2.F.1."),
 ("rather than by irritating tissue",
  "STB-2.E.1 classifies carbon monoxide as an asphyxiant, which describes how it harms rather than where it comes from; its combustion origin is stated separately in STB-2.E.6. The framework does not make it a particulate, a radioactive substance, or harmless."),
 ("differ in how readily soil gas can enter",
  "STB-2.F.1 has radon move up through the soil and enter via the basement or cracks in the walls or foundation, so differences in those openings bear directly on how much enters. It is not produced by furnishings, is not a combustion product, and is not described as entering through the roof."),
 ("falls steadily over the years after the furnishings are installed",
  "STB-2.E.5 names formaldehyde from building materials, furniture, upholstery and carpeting, so a decline as those furnishings age points to them as the source. A basement gradient and a well supply are the radon patterns of STB-2.F.1, and an appliance effect points to STB-2.E.6."),
 ("second leading cause of lung cancer",
  "STB-2.F.2 is the framework's own statement of the health consequence of radon exposure, which is what a message about health consequences rests on. The rejected options state sources rather than effects, or concern a different pollutant."),
 ("describe the effects they have on people",
  "The topic carries two learning objectives, STB-2.E identify indoor air pollutants and STB-2.F describe the effects of indoor air pollutants, with STB-2.E.3 supplying the three source categories. Dangerous concentrations, national rankings, outdoor smog chemistry and engineering design are not stated anywhere in the topic."),
]

TABLE_CHECKS = {8: q8, 9: q9, 11: q11, 13: q13, 14: q14, 15: q15, 16: q16}

es.run(e7_5, CLAIMS, TABLE_CHECKS, sys.argv)
