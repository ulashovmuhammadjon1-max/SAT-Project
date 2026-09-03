"""Key audit for AP ENVIRONMENTAL SCIENCE 7.6 Reduction of Air Pollutants.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
Items 1, 9, 10, 16, 20, 23, 27 and 30 rest on STB-2.G.1, the three categories
of method: regulatory practices, conservation practices, and alternative fuels.
Items 2, 8, 15, 24 and 19 rest on STB-2.G.2, the vapor recovery nozzle as a
device on a gasoline pump that prevents fumes escaping when fueling.
Items 3, 4, 11, 12, 17, 28 and 29 rest on STB-2.G.3, the catalytic converter
and the conversion of CO, NOx and hydrocarbons into CO2, N2, O2 and H2O.
Items 5, 13, 18 and 21 rest on STB-2.G.4, wet and dry scrubbers removing
particulates and gases from industrial exhaust streams.
Items 6, 7 and 26 rest on STB-2.G.5, scrubbers and electrostatic precipitators
as methods for coal-burning power plants.
Item 14 rests on STB-2.G.1's alternative fuels category, read off the table.
Items 15, 18, 22, 25 and 28 are also skill 7.D items: use data and evidence to
support a potential solution.

WHAT IS NOT CLAIMED. The framework gives no removal efficiency, no cost, no
statutory limit and no internal mechanism for an electrostatic precipitator, so
no key states one. Every efficiency in this module is supplied by its own stem
or table as that question's data. Item 21's key says only that a device
capturing solid particles need not remove a gas, which is the distinction the
framework itself draws between what its devices remove; it does not describe
how a precipitator works.

Item 29's key rests on the framework's own choice of the words LESS HARMFUL
together with CO2 appearing in the product list, and CO2 is treated as a
pollutant of concern in STB-2.A.1 and throughout unit 9. It does not claim any
harm figure.

DATA ITEMS: 4, 7, 8, 9, 12 and 14 carry tables and every keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e7_6.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_6

NO_CAT = "Without a catalytic converter (grams per kilometer)"
CAT = "With a catalytic converter (grams per kilometer)"
SO2 = "Sulfur dioxide released (tons per year)"
PM = "Particulates released (tons per year)"
VAPOR = "Hydrocarbon vapor escaping per 1,000 liters dispensed (grams)"
FALL = "Modeled fall in city-wide pollutant releases (percent)"
SO2_KM = "Sulfur dioxide released per 1,000 kilometers (grams)"
PM_KM = "Particulates released per 1,000 kilometers (grams)"
SHARE = "Share of the vehicle fleet fitted with catalytic converters (percent)"
CO_TOWN = "Carbon monoxide measured downtown (parts per million)"


def q4(table, item):
    before = dict(zip(cg.labels(table), cg.col(table, NO_CAT)))
    after = dict(zip(cg.labels(table), cg.col(table, CAT)))
    targets = ["Carbon monoxide", "Hydrocarbons", "Nitrogen oxides"]
    for t in targets:
        assert after[t] < 0.5 * before[t], f"{t} does not fall sharply: {before[t]} to {after[t]}"
    assert after["Carbon dioxide"] >= before["Carbon dioxide"], \
        "'all four fall' must be false, so carbon dioxide must not fall"
    changed = [t for t in targets if after[t] != before[t]]
    assert len(changed) == 3, "'only carbon monoxide changes' must be false"
    return (f"the three named pollutants fall to {[after[t] for t in targets]} from "
            f"{[before[t] for t in targets]}, while carbon dioxide moves from "
            f"{before['Carbon dioxide']:.0f} to {after['Carbon dioxide']:.0f}")


def q7(table, item):
    plants = cg.labels(table)
    kit = {r[0]: r[1] for r in table["rows"]}
    so2 = dict(zip(plants, cg.col(table, SO2)))
    pm = dict(zip(plants, cg.col(table, PM)))
    both = [p for p in plants if kit[p] == "scrubber and precipitator"][0]
    none = [p for p in plants if kit[p] == "none"][0]
    scrub = [p for p in plants if kit[p] == "scrubber only"][0]
    prec = [p for p in plants if kit[p] == "electrostatic precipitator only"][0]
    assert so2[both] == min(so2.values()) and pm[both] == min(pm.values()), \
        "the plant with both devices is not lowest in both columns"
    assert so2[scrub] < 0.5 * so2[none] and pm[scrub] > 0.5 * pm[none], \
        "the scrubber-only plant should be far lower in sulfur dioxide and little changed in particulates"
    assert pm[prec] < 0.5 * pm[none] and so2[prec] > 0.5 * so2[none], \
        "the precipitator-only plant should be far lower in particulates and little changed in sulfur dioxide"
    assert so2[both] < so2[none], "'both devices raise sulfur dioxide' must be false"
    return (f"with both devices the plant reads {so2[both]:.0f} and {pm[both]:.0f}, the smallest "
            f"in each column, while the single devices cut one pollutant by more than half and "
            "leave the other above half its uncontrolled value")


def q8(table, item):
    stations = cg.labels(table)
    fitted = {r[0]: r[1] for r in table["rows"]}
    vapor = dict(zip(stations, cg.col(table, VAPOR)))
    assert set(fitted.values()) <= {"yes", "no"}, f"the fitted column is not yes or no: {fitted}"
    with_n = [s for s in stations if fitted[s] == "yes"]
    without = [s for s in stations if fitted[s] == "no"]
    assert len(with_n) == 2 and len(without) == 2, "two stations of each kind are required"
    assert max(vapor[s] for s in with_n) < 0.2 * min(vapor[s] for s in without), \
        f"the fitted stations are not far below the unfitted: {vapor}"
    return (f"the fitted stations lose {[vapor[s] for s in with_n]} grams against "
            f"{[vapor[s] for s in without]} at the unfitted stations, under a fifth in every pairing")


def q9(table, item):
    measures = cg.labels(table)
    cat = {r[0]: r[1] for r in table["rows"]}
    fall = dict(zip(measures, cg.col(table, FALL)))
    assert set(cat.values()) == {"regulatory practice", "conservation practice", "alternative fuel"}, \
        f"the three categories are not each present exactly once: {cat}"
    top = max(fall, key=fall.get)
    assert cat[top] == "regulatory practice", f"the largest modeled fall is the {cat[top]}"
    assert min(fall.values()) > 0, "'no reduction at all' must be false"
    assert len(set(fall.values())) == 3, "'identical reductions' must be false"
    return (f"the table carries one measure in each of the three categories and the modeled "
            f"falls are {[fall[m] for m in measures]}, the largest belonging to the {cat[top]}")


def q12(table, item):
    share = cg.col(table, SHARE)
    co = cg.col(table, CO_TOWN)
    assert all(share[i] < share[i + 1] for i in range(len(share) - 1)), \
        f"the fitted share does not rise through the program: {share}"
    assert all(co[i] > co[i + 1] for i in range(len(co) - 1)), \
        f"carbon monoxide does not fall through the program: {co}"
    return (f"the fitted share runs {share} percent while carbon monoxide runs {co} parts per "
            "million, one rising at every step and the other falling at every step")


def q14(table, item):
    so2 = dict(zip(cg.labels(table), cg.col(table, SO2_KM)))
    pm = dict(zip(cg.labels(table), cg.col(table, PM_KM)))
    base = "High-sulfur diesel"
    for fuel in so2:
        if fuel == base:
            continue
        assert so2[fuel] < so2[base] and pm[fuel] < pm[base], \
            f"{fuel} does not lower both pollutants against the base fuel"
    cng = "Compressed natural gas"
    assert so2[cng] == min(so2.values()) and pm[cng] == min(pm.values()), \
        "compressed natural gas is not the smallest in both columns"
    return (f"against {so2[base]:.0f} and {pm[base]:.0f} for the base fuel, both alternatives are "
            f"lower in each column and compressed natural gas is lowest at {so2[cng]:.0f} and {pm[cng]:.0f}")


CLAIMS = [
 ("Regulatory practices, conservation practices, and alternative fuels",
  "STB-2.G.1 verbatim: methods to reduce air pollutants include regulatory practices, conservation practices, and alternative fuels. The rejected groupings belong to other units, and dilution and burial are offered nowhere as reduction methods."),
 ("prevents fumes from escaping into the atmosphere while a motor vehicle is being fueled",
  "STB-2.G.2 near verbatim: a vapor recovery nozzle is an air pollution control device on a gasoline pump that prevents fumes from escaping into the atmosphere when fueling a motor vehicle. Converting exhaust is STB-2.G.3 and removing particulates from an industrial stream is STB-2.G.4."),
 ("into carbon dioxide, nitrogen, oxygen, and water",
  "STB-2.G.3 near verbatim: a catalytic converter converts pollutants (CO, NOx, and hydrocarbons) in exhaust into less harmful molecules (CO2, N2, O2, and H2O). The rejected conversions run the reaction backwards or assign substances the framework does not give to this device."),
 ("while carbon dioxide does not fall",
  "Recomputed in q4 above: the three pollutants named in STB-2.G.3 each fall to less than half their uncontrolled value while the carbon dioxide reading does not fall. That is what a device converting those three into CO2, N2, O2 and H2O would produce."),
 ("remove particulates and gases from industrial exhaust streams",
  "STB-2.G.4 near verbatim: wet and dry scrubbers are air pollution control devices that remove particulates and/or gases from industrial exhaust streams. Vapor capture at a pump is STB-2.G.2, exhaust conversion is STB-2.G.3, and a monitor removes nothing."),
 ("Scrubbers and electrostatic precipitators",
  "STB-2.G.5 verbatim: methods to reduce air pollution from coal-burning power plants include scrubbers and electrostatic precipitators. The vapor recovery nozzle is defined for a gasoline pump and the catalytic converter for an internal combustion engine."),
 ("each single device lowers one pollutant much more than the other",
  "Recomputed in q7 above: the plant with both devices holds the smallest value in each column, the scrubber-only plant is below half the uncontrolled sulfur dioxide but above half the uncontrolled particulates, and the precipitator-only plant is the reverse. Both devices are those named in STB-2.G.5."),
 ("lose far less hydrocarbon vapor per volume dispensed",
  "Recomputed in q8 above: each fitted station loses under a fifth of what either unfitted station loses per volume dispensed. STB-2.G.2 describes the nozzle as preventing fumes from escaping when a vehicle is fueled."),
 ("regulatory measure is modeled to achieve the largest reduction here",
  "Recomputed in q9 above: the table carries one measure in each of the three categories STB-2.G.1 names, the three modeled falls are distinct and positive, and the largest belongs to the regulatory measure. The claim is about these modeled data, not about regulation in general."),
 ("Reducing the number of vehicle trips taken",
  "STB-2.G.1 lists conservation practices as one of the three kinds of method, and a conservation practice reduces the activity that releases the pollutant. A legal limit and an equipment mandate are regulatory practices, a scrubber is the device of STB-2.G.4, and changing the fuel is the alternative fuel category."),
 ("into less harmful molecules before they leave",
  "STB-2.G.3 has the converter change CO, NOx and hydrocarbons into CO2, N2, O2 and H2O, so what leaves the tailpipe is a different mixture. The framework does not have it store exhaust, stop combustion, or merely measure."),
 ("fell as the share of the fleet fitted with catalytic converters rose",
  "Recomputed in q12 above: the fitted share rises at every step of the record and the measured carbon monoxide falls at every step. Carbon monoxide is one of the pollutants STB-2.G.3 has the converter convert."),
 ("A scrubber, which removes particulates and gases from industrial exhaust streams",
  "STB-2.G.4 assigns exactly that removal to wet and dry scrubbers. The nozzle of STB-2.G.2 is defined for a fuel pump and the converter of STB-2.G.3 for an engine; a thermal inversion under STB-2.C is a condition of the atmosphere and a fan relocates air."),
 ("compressed natural gas is lowest in both",
  "Recomputed in q14 above: both alternatives read below the high-sulfur base fuel in each column and compressed natural gas holds the smallest value in both. Alternative fuels are one of the three categories in STB-2.G.1."),
 ("release far less fuel vapor per volume dispensed",
  "Suggested skill 7.D, use data and evidence to support a potential solution, applied to STB-2.G.2. The evidence that supports the device is a measured difference in escaping vapor with and without it; sales volume, appearance, vapor density and vehicle range measure nothing the nozzle acts on."),
 ("law setting a maximum allowable release",
  "STB-2.G.1 names regulatory practices as one of the three methods, and a rule imposed by law is what makes a measure regulatory. Walking and inflating tires are conservation choices, a voluntary installation is not a rule, and changing fuel is the alternative fuel category."),
 ("same amount of driving releases less carbon monoxide",
  "STB-2.G.3 makes the converter change what leaves the tailpipe rather than how much driving occurs, and it is defined for internal combustion engines, so it applies to vehicles that do burn fuel. Nothing in the framework has it stop an engine or wait on a reduction in driving."),
 ("before and after the scrubber was installed, with production held steady",
  "Suggested skill 7.D. Attributing a change to the device requires readings bracketing its installation with the activity held constant, so that the difference is not a change in output. A single later reading, employment, price and a distant city leave that comparison unmade."),
 ("before it enters the wider atmosphere",
  "The three devices act at the point of release: STB-2.G.2 at the pump, STB-2.G.3 in the engine's exhaust and STB-2.G.4 in the industrial exhaust stream. None of them retrieves pollution that has already dispersed, which is what reduction at the source means."),
 ("control device fitted to an exhaust stream and the other is a regulatory practice",
  "A scrubber is the device of STB-2.G.4 and one of the coal plant methods of STB-2.G.5, and a legal limit on fuel composition is a regulatory practice under STB-2.G.1. Neither reduces the activity itself, so neither is a conservation practice."),
 ("captures solid particles from the stream does not by itself remove a gas",
  "The framework distinguishes its devices by what they remove: STB-2.G.4 gives scrubbers particulates and gases, and STB-2.G.5 names precipitators separately among the coal plant methods. So equipment aimed at solid particles need not affect a gas in the same stream. No internal mechanism is claimed here."),
 ("Measured releases per kilometer travelled",
  "Suggested skill 7.D applied to the alternative fuels category of STB-2.G.1. Comparing releases per kilometer for the current and the proposed fuel is what shows whether the same service is delivered with less pollution; capacity, appearance, depot location and route count measure no release."),
 ("regulation can require a device to be used",
  "STB-2.G.1 gives the three broad methods and STB-2.G.2 to STB-2.G.5 give particular devices, so a rule mandating a device is a regulatory practice carried out through a device. The framework applies its devices to pumps, engines, industrial streams and coal plants alike, so no split between indoor and outdoor or between plants and vehicles holds."),
 ("same as at nearby stations without the nozzles",
  "STB-2.G.2 makes the nozzle's purpose the prevention of escaping fumes during fueling, so an escape rate no lower than at unfitted stations is what undercuts the claim. Volume dispensed, location, installation date and fuel brand bear on none of that."),
 ("two situations with different amounts of activity to be compared fairly",
  "Suggested skill 7.D. A yearly total mixes how clean each unit of activity is with how much activity occurred, so a rate per unit of activity is what isolates the device's effect. The size of the number and the state of the pollutant are irrelevant."),
 ("so the plant addresses more than one pollutant",
  "STB-2.G.5 names scrubbers and electrostatic precipitators together as methods for coal-burning power plants, and STB-2.G.4 has scrubbers remove particulates and gases. The framework has no device disable another and does not make the fuel unnecessary."),
 ("changes where the pollution goes rather than reducing the amount released",
  "Every method in STB-2.G.1 to STB-2.G.5 either reduces the activity, changes the fuel, imposes a rule, or removes or converts pollutants before release. A taller stack does none of those, since the same material still enters the atmosphere."),
 ("both recorded over the same years",
  "Suggested skill 7.D applied to STB-2.G.3. Tying the program to the outcome requires the fitted share and the measured pollutant over the same period; national sales, foreign fuel prices, manufacturing counts and mismatched periods break the link."),
 ("include carbon dioxide, which the course treats as a pollutant of concern",
  "STB-2.G.3 says less harmful molecules, not harmless ones, and its own product list contains CO2, which STB-2.A.1 lists among the releases of coal combustion and which unit 9 treats as a greenhouse gas. The products are not the original pollutants and are not retained in the vehicle."),
 ("Three broad kinds of method, together with named devices",
  "STB-2.G.1 supplies the three categories and STB-2.G.2 to STB-2.G.5 supply the devices for the pump, the engine, the industrial exhaust stream and the coal plant. Both halves are part of the framework's structure, and every device acts before release rather than after it."),
]

TABLE_CHECKS = {4: q4, 7: q7, 8: q8, 9: q9, 12: q12, 14: q14}

es.run(e7_6, CLAIMS, TABLE_CHECKS, sys.argv)
