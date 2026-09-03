"""Key audit for AP ENVIRONMENTAL SCIENCE 7.2 Photochemical Smog.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
Items 1, 14, 19, 25 and 30 rest on STB-2.B.1, that photochemical smog forms
when nitrogen oxides and volatile organic hydrocarbons react with heat and
sunlight to produce a variety of pollutants.
Item 15 rests on STB-2.B.2, that many environmental factors affect its
formation.
Items 2, 3, 4, 13, 16, 18, 21, 24, 27 and 29 rest on STB-2.B.3: nitrogen oxide
is produced early in the day, and ozone peaks in the afternoon and is higher in
summer because it is produced by reactions between oxygen and sunlight.
Items 5, 6, 17 and 22 rest on STB-2.B.4, the definition of volatile organic
compounds, the examples formaldehyde and gasoline, and trees as a natural source.
Items 7 and 8 rest on STB-2.B.5, that smog often forms in urban areas because
of the large number of motor vehicles.
Items 9, 10, 23 and 26 rest on STB-2.B.6, reduction through the reduction of
nitrogen oxide and VOCs.
Items 11, 12 and 28 rest on STB-2.B.7, respiratory problems and eye irritation.

Item 20 chains STB-2.B.3 to STB-2.B.7: the framework supplies both the
afternoon peak and the irritation, and the item asks only that the two be put
together. Item 24 is a design item under suggested skill 5.B and turns on the
same afternoon peak.

NOTHING NAMED. The framework names no city, episode, statute or chemical
species beyond those quoted above, so neither does this module.

DATA ITEMS: 2, 4, 6, 8, 10, 12 and 16 carry tables and every keyed reading is
recomputed below from the table alone, with the rejected readings falsified
against the same numbers.

NEGATIVE CONTROL: `python3 verify_e7_2.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_2

NO = "Nitrogen oxide (parts per billion)"
O3 = "Ozone (parts per billion)"
SUN = "Average daily sunlight hours"
O3_PM = "Average afternoon ozone (parts per billion)"
VOC = "Volatile organic compounds released (kilograms per day)"
CARS = "Motor vehicles counted per hour on nearby roads"
O3_AFT = "Afternoon ozone (parts per billion)"
TEMP = "Afternoon air temperature (degrees Celsius)"
NOX_T = "Nitrogen oxides released (tons per day)"
VOC_T = "Volatile organic compounds released (tons per day)"
PEAK = "Peak afternoon ozone (parts per billion)"
BREATH = "Clinic visits for breathing difficulty per 100,000 residents"
EYES = "Clinic visits for eye irritation per 100,000 residents"


def q2(table, item):
    hours = cg.labels(table)
    nox = cg.col(table, NO)
    ozone = cg.col(table, O3)
    i_nox = nox.index(max(nox))
    i_o3 = ozone.index(max(ozone))
    assert i_nox == 0, f"nitrogen oxide peaks at {hours[i_nox]}, not the first hour"
    assert hours[i_o3] == "3 in the afternoon", f"ozone peaks at {hours[i_o3]}"
    assert i_nox != i_o3, "the two maxima must fall at different hours"
    assert not all(ozone[i] > ozone[i + 1] for i in range(len(ozone) - 1)), \
        "'ozone falls all afternoon' must be false"
    assert not all(nox[i] < nox[i + 1] for i in range(len(nox) - 1)), \
        "'nitrogen oxide climbs steadily' must be false"
    assert max(ozone) - min(ozone) > 10, "'neither changes appreciably' must be false"
    return (f"nitrogen oxide peaks at {hours[i_nox]} and ozone at {hours[i_o3]}, so the "
            f"maxima are at different hours and the ozone range is {max(ozone) - min(ozone):.0f}")


def q4(table, item):
    months = cg.labels(table)
    sun = cg.col(table, SUN)
    ozone = cg.col(table, O3_PM)
    by_sun = [m for _, m in sorted(zip(sun, months))]
    by_o3 = [m for _, m in sorted(zip(ozone, months))]
    assert by_sun == by_o3, f"sunlight order {by_sun} differs from ozone order {by_o3}"
    assert len(set(ozone)) == len(ozone), "'the same in all four months' must be false"
    return (f"ranking by sunlight gives {by_sun} and ranking by ozone gives the same "
            "order, so the two rise together and no two months share a value")


def q6(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, VOC)))
    human = vals["Fuel storage and refueling"] + vals["Solvent and paint use"]
    forest = vals["Forested hillside"]
    others = sum(v for k, v in vals.items() if k != "Forested hillside")
    assert human > others - human, "the two human uses must exceed the remaining sources"
    assert forest > 0, "the forested hillside must record a release"
    assert forest < others, "'the hillside releases more than all others combined' must be false"
    return (f"fuel and solvent use total {human:.0f} kilograms against {forest:.0f} from "
            f"the hillside and {others:.0f} from all non-forest sources together")


def q8(table, item):
    areas = cg.labels(table)
    cars = cg.col(table, CARS)
    ozone = cg.col(table, O3_AFT)
    assert [a for _, a in sorted(zip(cars, areas))] == \
           [a for _, a in sorted(zip(ozone, areas))], "the two rankings differ"
    assert areas[cars.index(max(cars))] == "City center", "the busiest area is not the city center"
    assert ozone[areas.index("Rural valley")] == min(ozone), \
        "'the rural valley recorded the highest' must be false"
    assert ozone[areas.index("Suburban edge")] < ozone[areas.index("City center")], \
        "'suburban above city center' must be false"
    return (f"ordering by vehicles and by ozone both give {[a for _, a in sorted(zip(cars, areas))]}, "
            "so the two increase together and the rural value is the smallest")


def q10(table, item):
    peak = dict(zip(cg.labels(table), cg.col(table, PEAK)))
    nox = dict(zip(cg.labels(table), cg.col(table, NOX_T)))
    voc = dict(zip(cg.labels(table), cg.col(table, VOC_T)))
    base = "No change"
    both = "Both cut by half"
    assert min(peak, key=peak.get) == both, f"the lowest peak belongs to {min(peak, key=peak.get)}"
    for single in ("Nitrogen oxides cut by half", "Volatile organic compounds cut by half"):
        assert peak[both] < peak[single] < peak[base], \
            f"{single} does not sit between the combined cut and the no-change case"
    assert nox["Nitrogen oxides cut by half"] * 2 == nox[base], "the nitrogen oxide cut is not a half"
    assert voc["Volatile organic compounds cut by half"] * 2 == voc[base], \
        "the volatile organic compound cut is not a half"
    return (f"peak ozone runs {peak[base]:.0f} with no change, {peak['Nitrogen oxides cut by half']:.0f} "
            f"and {peak['Volatile organic compounds cut by half']:.0f} for the single cuts, and "
            f"{peak[both]:.0f} for both, and each modeled cut is exactly half of the base release")


def q12(table, item):
    breath = cg.col(table, BREATH)
    eyes = cg.col(table, EYES)
    for series, name in ((breath, "breathing"), (eyes, "eye irritation")):
        assert all(series[i] < series[i + 1] for i in range(len(series) - 1)), \
            f"the {name} column does not rise with the ozone band: {series}"
    assert breath[0] == min(breath) and eyes[0] == min(eyes), \
        "'both highest in the lowest band' must be false"
    assert all(b != e for b, e in zip(breath, eyes)), "'equal in every band' must be false"
    return (f"breathing visits run {breath} and eye visits run {eyes} from the lowest ozone "
            "band to the highest; both rise throughout and no band has them equal")


def q16(table, item):
    temp = cg.col(table, TEMP)
    ozone = cg.col(table, O3_AFT)
    pairs = sorted(zip(temp, ozone))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"ozone does not rise with temperature: {pairs}"
    assert ozone[temp.index(min(temp))] == min(ozone), \
        "'highest on the coolest day' must be false"
    assert len(set(ozone)) == len(ozone), "'the same on all four days' must be false"
    return (f"sorted by temperature the ozone values are {[o for _, o in pairs]}, strictly "
            "increasing, and the coolest day carries the smallest value")


CLAIMS = [
 ("volatile organic hydrocarbons reacting with heat and sunlight",
  "STB-2.B.1, near verbatim: photochemical smog is formed when nitrogen oxides and volatile organic hydrocarbons react with heat and sunlight to produce a variety of pollutants. Sulfur chemistry in the dark, greenhouse gas accumulation, settling dust and stratospheric chemistry are different processes described elsewhere in the course."),
 ("climbs to its highest value in the afternoon",
  "Recomputed in q2 above: the tabulated nitrogen oxide is largest at the first sampling hour and the tabulated ozone is largest in mid-afternoon, so the maxima fall at different hours. STB-2.B.3 states that pattern -- nitrogen oxide produced early in the day, ozone peaking in the afternoon."),
 ("reactions between oxygen and sunlight",
  "STB-2.B.3 gives the reason in its own words: ozone is produced by chemical reactions between oxygen and sunlight, which is why the concentration builds through the sunlit hours. The framework does not have ozone emitted from tailpipes in the form measured, nor delivered from the stratosphere on cooling."),
 ("highest in the month with the most daily sunlight",
  "Recomputed in q4 above: ranking the four months by sunlight hours produces the same order as ranking them by afternoon ozone. STB-2.B.3 states that ozone concentrations are higher in the summer because ozone is produced by reactions between oxygen and sunlight."),
 ("evaporate or sublimate at room temperature",
  "STB-2.B.4, near verbatim: volatile organic compounds, such as formaldehyde and gasoline, evaporate or sublimate at room temperature. That is why they enter the air without combustion, and it distinguishes them from metals, from acids formed in cloud droplets, and from the inert constituents of clean air."),
 ("the forested hillside is a natural source as well",
  "Recomputed in q6 above: the two human uses together exceed every other entry while the forested hillside still records a substantial release. STB-2.B.4 states that trees are a natural source of volatile organic compounds, and these compounds evaporate at room temperature rather than requiring combustion."),
 ("large number of motor vehicles",
  "STB-2.B.5, near verbatim: photochemical smog often forms in urban areas because of the large number of motor vehicles there. Temperature, rainfall, tree cover and elevation are not the reason the framework gives."),
 ("rises with the number of motor vehicles counted nearby",
  "Recomputed in q8 above: ordering the three areas by vehicle count gives the same order as ordering them by afternoon ozone, and the city center holds both maxima. STB-2.B.5 ties urban smog to the large number of motor vehicles."),
 ("Reducing nitrogen oxide and reducing volatile organic compounds",
  "STB-2.B.6, near verbatim: photochemical smog can be reduced through the reduction of nitrogen oxide and VOCs. Those are the two reactants STB-2.B.1 puts into its formation; the rejected pairs name pollutants that are not ingredients of this reaction."),
 ("lowers peak ozone more than cutting either one alone",
  "Recomputed in q10 above: the combined scenario carries the lowest modeled peak and each single cut sits strictly between it and the no-change case. STB-2.B.6 names both reductions as methods of control, which is what a two-reactant formation implies."),
 ("Respiratory problems and eye irritation",
  "STB-2.B.7, near verbatim: photochemical smog can harm human health in several ways, including causing respiratory problems and eye irritation. No skeletal or dental harm is attributed to it, and the framework claims no health benefit from smog."),
 ("rise as the ozone band rises",
  "Recomputed in q12 above: both columns increase from the lowest ozone band to the highest and no band has them equal. STB-2.B.7 names respiratory problems and eye irritation as the harms of photochemical smog, which is what the two columns record."),
 ("before the sunlight-driven chemistry that builds ozone has had time to act",
  "STB-2.B.3 separates the two in time: nitrogen oxide is produced early in the day, while ozone is produced by reactions between oxygen and sunlight and peaks in the afternoon. So the two are not products of one reaction, and the framework gives no nighttime production, settling by weight, or tidal cycle."),
 ("hot, sunny weekday with heavy traffic",
  "STB-2.B.1 requires nitrogen oxides and volatile organic hydrocarbons together with heat and sunlight, and STB-2.B.5 supplies the vehicles as the urban source. Each rejected day removes at least one of those ingredients."),
 ("Many environmental factors affect the formation",
  "STB-2.B.2 verbatim. It is the framework's own explanation for why formation varies between days that look similar, and each rejected option contradicts STB-2.B.1, STB-2.B.4 or STB-2.B.5."),
 ("rises as the afternoon temperature rises",
  "Recomputed in q16 above: sorting the four days by temperature puts the ozone values in increasing order and the coolest day carries the smallest value. STB-2.B.1 names heat as one of the conditions under which the two reactants form smog."),
 ("since gasoline evaporates at room temperature",
  "STB-2.B.4 names gasoline as a volatile organic compound that evaporates at room temperature, so vapor-tight handling removes one of the two reactants named in STB-2.B.1. Nitrogen oxides are a combustion product rather than an evaporation product, and ozone is not stored in a tank."),
 ("by hour so that the afternoon peak is visible",
  "Suggested skill 5.B, describe relationships among variables in data represented, applied to the claim in STB-2.B.3 about when ozone peaks. A daily average conceals the time structure the claim is about, and further averaging, a daily minimum, coarse rounding and pre-dawn sampling all remove it as well."),
 ("produces a variety of pollutants",
  "STB-2.B.1 states that the reaction produces a variety of pollutants, which is why photochemical smog is a mixture rather than one substance. It is not a single gas, not warmed dust, not diluted nitrogen oxide and not condensed water."),
 ("sunnier region will tend to form more photochemical smog",
  "STB-2.B.1 puts sunlight and heat into the reaction and STB-2.B.3 attributes higher summer ozone to production by reactions between oxygen and sunlight. With the vehicle sources similar, the sunnier region is therefore the one expected to form more."),
 ("exercising earlier reduces exposure",
  "STB-2.B.3 places the ozone peak in the afternoon and STB-2.B.7 attributes respiratory problems and eye irritation to photochemical smog, so moving activity away from the peak lowers exposure. The rejected options invert the daily pattern or deny the harm the framework states."),
 ("trees are a natural source of them",
  "STB-2.B.4 names trees as a natural source of volatile organic compounds and STB-2.B.1 makes those compounds one of the two reactants. The framework attributes no nitrogen oxide or ozone emission to trees and no warming role of the kind described."),
 ("lowering either one can lower the amount of smog formed",
  "STB-2.B.6 names the reduction of nitrogen oxide and of VOCs as methods of reducing photochemical smog, and STB-2.B.1 makes both of them reactants. Limiting either reactant therefore limits how much can form, and no conversion of one into the other is described anywhere."),
 ("wind blows in from a large upwind urban area",
  "The competing explanation is transport of already formed pollution, so what bears on it is evidence tying the city's ozone to the arrival of air from another source region. Every other option describes a pattern STB-2.B.3 to STB-2.B.5 predict for locally formed smog, so none of them separates the two explanations."),
 ("produced in the air by reactions among substances the vehicles do release",
  "STB-2.B.1 with STB-2.B.5: the vehicles supply the nitrogen oxides and volatile organic compounds, and heat and sunlight drive the reaction that makes the product above the city. The framework gives no pavement, rainfall, instrument or pedestrian source."),
 ("release less nitrogen oxide and fewer volatile organic compounds",
  "STB-2.B.6 makes the reduction of those two the way to reduce photochemical smog, so a measured reduction in both is the evidence that supports the plan. Noise, maintenance cost, paint color and distance travelled speak to neither reactant."),
 ("season and at a time of day when the framework predicts ozone to be lowest",
  "STB-2.B.3 puts the ozone peak in the afternoon and makes concentrations higher in summer, so a single winter hour samples the conditions in which the lowest values are expected and cannot support a conclusion about summer. The units and the setting are not the flaw."),
 ("can cause eye irritation and respiratory problems",
  "STB-2.B.1 supplies the conditions -- heat and sunlight -- and STB-2.B.7 supplies exactly these two symptoms. Radon under STB-2.F.2 and noise under STB-2.J.1 are pollutants with different sources and different effects."),
 ("Hours of sunlight received and the ozone concentration",
  "Suggested skill 5.B applied to STB-2.B.3, which states the relationship between sunlight and ozone production. Each rejected pair omits one of the two variables in that stated relationship and so cannot describe it."),
 ("heat and sunlight drive reactions among them",
  "Each link is one of the framework's own statements: the large number of motor vehicles in urban areas under STB-2.B.5, the reaction of nitrogen oxides and volatile organic compounds with heat and sunlight under STB-2.B.1, and the respiratory problems and eye irritation under STB-2.B.7. Every rejected chain contradicts at least one of them."),
]

TABLE_CHECKS = {2: q2, 4: q4, 6: q6, 8: q8, 10: q10, 12: q12, 16: q16}

es.run(e7_2, CLAIMS, TABLE_CHECKS, sys.argv)
