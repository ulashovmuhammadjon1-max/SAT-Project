"""Key audit for AP ENVIRONMENTAL SCIENCE 8.2 Human Impacts on Ecosystems.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
Items 1, 2, 20 and 27 rest on STB-3.B.1, the range of tolerance, the optimum
range in which homeostasis is maintained, and the stress, limited growth,
reduced reproduction and death outside it.
Items 3, 4 and 28 rest on STB-3.B.2, the factors damaging coral reefs.
Items 5 and 21 rest on STB-3.B.3, the three harms of an oil spill; items 7 and
22 on STB-3.B.4, the economic consequences for fishing and tourism.
Items 8, 9 and 23 rest on STB-3.B.5, dead zones as areas of low oxygen caused
by increased nutrient pollution; items 10, 11 and 24 on STB-3.B.6, the oxygen
sag curve as a plot of dissolved oxygen against distance from a source.
Items 12, 13 and 29 rest on STB-3.B.7, heavy metals from industry, especially
mining and burning fossil fuels, reaching groundwater and the drinking supply.
Item 14 rests on STB-3.B.8, the harms of litter.
Items 15, 16 and 25 rest on STB-3.B.9, sediment reducing light infiltration and
settling to disrupt habitats.
Items 17, 18 and 26 rest on STB-3.B.10, bacterial conversion of elemental
mercury to highly toxic methylmercury.
Items 6 and 19 are the quantitative items under suggested skill 6.B, and item
30 joins all ten statements.

WHAT IS NOT KEYED HERE. The algal-bloom-and-decomposition mechanism belongs to
STB-3.F.2 in topic 8.5, thermal effects on dissolved oxygen to STB-3.G.2 in
8.6, biomagnification to STB-3.I in 8.8, and coral bleaching by warming to
STB-4.G.3 in 9.6. The dead zone is keyed only as an area of low oxygen caused
by nutrient pollution, and mercury only as far as the conversion in the water.

ARITHMETIC. Items 6 and 19 are one-step conversions recomputed below from the
table alone, and each rejected value is checked to differ from the recomputed
answer, so a decimal slip or an addition in place of a multiplication cannot
match the key.

DATA ITEMS: 2, 4, 6, 9, 11, 16, 18 and 19 carry tables and every keyed reading
is recomputed below.

NEGATIVE CONTROL: `python3 verify_e8_2.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_2

DOSE = "Concentration of a pollutant in the tank (milligrams per liter)"
SURV = "Fish surviving after 30 days (out of 40)"
EGGS = "Eggs laid per surviving female"
DIST = "Distance downstream from the outfall (kilometers)"
DO = "Dissolved oxygen (milligrams per liter)"
NITRO = "Nitrogen carried down the river in spring (thousand tons)"
ZONE = "Area of the low-oxygen zone that summer (square kilometers)"
SED = "Suspended sediment (milligrams per liter)"
LIGHT = "Depth reached by 1 percent of surface light (meters)"
ALGAE = "Algal growth measured on plates at 3 meters (milligrams per day)"
VALUE = "Value"
SED_REEF = "Sediment reaching the reef (grams per square meter per day)"
CORAL = "Live coral cover (percent)"
MINE = "Distance from the abandoned mine (kilometers)"
HG = "Mercury in the water (nanograms per liter)"
MEHG = "Methylmercury in the water (nanograms per liter)"


def q2(table, item):
    dose = cg.col(table, DOSE)
    surv = cg.col(table, SURV)
    eggs = cg.col(table, EGGS)
    assert dose == sorted(dose), "the treatments must be listed in increasing order"
    for series, name in ((surv, "survival"), (eggs, "egg production")):
        assert all(series[i] >= series[i + 1] for i in range(len(series) - 1)), \
            f"{name} does not fall as the concentration rises: {series}"
        assert series[-1] == 0, f"{name} does not reach zero in the strongest treatment"
        assert series[0] == max(series), f"{name} is not largest at the lowest concentration"
    return (f"survival runs {surv} and egg production {eggs} across concentrations {dose}, "
            "both falling to zero at the strongest treatment")


def q4(table, item):
    sed = cg.col(table, SED_REEF)
    coral = cg.col(table, CORAL)
    pairs = sorted(zip(sed, coral))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"coral cover does not fall as sediment rises: {pairs}"
    assert coral[sed.index(max(sed))] == min(coral), \
        "'the most sediment holds the most coral' must be false"
    assert len(set(coral)) == len(coral), "'the same in all four' must be false"
    return (f"sorted by sediment the coral cover runs {[c for _, c in pairs]} percent, falling "
            "at every step, with the least coral where the sediment is greatest")


def q6(table, item):
    vals = {r[0]: cg.num(r[1]) for r in table["rows"]}
    barrels = vals["Volume of oil released (barrels)"]
    per = vals["Volume of one barrel (liters)"]
    litres = barrels * per
    assert abs(litres - 640000) < 1e-6, f"the product recomputes to {litres}"
    for wrong in (64000, 6400000, barrels + per):
        assert abs(litres - wrong) > 1, f"a rejected value {wrong} equals the recomputed answer"
    return (f"{barrels:.0f} barrels times {per:.0f} liters per barrel is {litres:.0f} liters, "
            f"which is not {barrels + per:.0f}, the sum of the two quantities")


def q9(table, item):
    years = cg.labels(table)
    nitro = dict(zip(years, cg.col(table, NITRO)))
    zone = dict(zip(years, cg.col(table, ZONE)))
    assert max(nitro, key=nitro.get) == max(zone, key=zone.get), \
        "the largest nitrogen year is not the largest zone year"
    assert min(nitro, key=nitro.get) == min(zone, key=zone.get), \
        "the smallest nitrogen year is not the smallest zone year"
    assert [y for _, y in sorted(zip(nitro.values(), years))] == \
           [y for _, y in sorted(zip(zone.values(), years))], "the two rankings differ"
    assert len(set(zone.values())) == len(zone), "'the same in all four years' must be false"
    return (f"ranking by nitrogen and by zone area both give "
            f"{[y for _, y in sorted(zip(nitro.values(), years))]}, so the two rise together")


def q11(table, item):
    dist = cg.col(table, DIST)
    do = cg.col(table, DO)
    assert dist == sorted(dist), "the samples must be listed in order of distance"
    low = do.index(min(do))
    assert 0 < low < len(do) - 1, f"the minimum must lie between the ends, found at index {low}"
    assert all(do[i] > do[i + 1] for i in range(low)), "oxygen must fall to the minimum"
    assert all(do[i] < do[i + 1] for i in range(low, len(do) - 1)), "oxygen must recover after it"
    assert do[0] == max(do) or do[-1] == max(do), "the ends should carry the highest values"
    return (f"dissolved oxygen runs {do} with distance {dist}, falling to {min(do)} at "
            f"{dist[low]:.0f} kilometers and recovering to {do[-1]} beyond it")


def q16(table, item):
    sed = cg.col(table, SED)
    light = cg.col(table, LIGHT)
    algae = cg.col(table, ALGAE)
    assert sed == sorted(sed), "the stretches must be listed in increasing sediment order"
    for series, name in ((light, "light penetration"), (algae, "algal growth")):
        assert all(series[i] > series[i + 1] for i in range(len(series) - 1)), \
            f"{name} does not fall as sediment rises: {series}"
    assert light[sed.index(max(sed))] == min(light), \
        "'the most sediment gives the deepest light' must be false"
    return (f"as sediment runs {sed} the light depth runs {light} meters and the algal growth "
            f"{algae} milligrams per day, both falling at every step")


def q18(table, item):
    sites = cg.labels(table)
    dist = dict(zip(sites, cg.col(table, MINE)))
    hg = dict(zip(sites, cg.col(table, HG)))
    me = dict(zip(sites, cg.col(table, MEHG)))
    ordered = sorted(sites, key=lambda s: dist[s])
    for series, name in ((hg, "mercury"), (me, "methylmercury")):
        assert all(series[ordered[i]] > series[ordered[i + 1]] for i in range(len(ordered) - 1)), \
            f"{name} does not fall with distance from the mine: {series}"
        assert min(series.values()) > 0, f"{name} must be present in every sample"
    assert me[ordered[0]] == max(me.values()), "methylmercury is not greatest nearest the mine"
    ref = [s for s in sites if "Reference" in s][0]
    assert hg[ref] == min(hg.values()) and me[ref] == min(me.values()), \
        "'both highest at the reference site' must be false"
    return (f"from the mine outward mercury runs {[hg[s] for s in ordered]} and methylmercury "
            f"{[me[s] for s in ordered]}, both falling and both present in every sample")


def q19(table, item):
    vals = {r[0]: cg.num(r[1]) for r in table["rows"]}
    litres = vals["Water flowing past the town each day (million liters)"] * 1e6
    conc = vals["Dissolved metal concentration (milligrams per liter)"]
    kilograms = litres * conc / 1e6
    assert abs(kilograms - 600) < 1e-6, f"the load recomputes to {kilograms}"
    for wrong in (60, 6000, vals["Water flowing past the town each day (million liters)"] + conc):
        assert abs(kilograms - wrong) > 1, f"a rejected value {wrong} equals the recomputed answer"
    return (f"{litres:.0f} liters times {conc:.0f} milligrams per liter is {litres * conc:.0f} "
            f"milligrams, which is {kilograms:.0f} kilograms per day")


CLAIMS = [
 ("optimum range in which the organism can maintain homeostasis",
  "STB-3.B.1 near verbatim: organisms have a range of tolerance, an optimum range for each factor where they can maintain homeostasis, and outside it may experience physiological stress, limited growth, reduced reproduction and in extreme cases death. Neither immunity nor immediate death at any exposure is stated."),
 ("reaching zero at the highest concentration",
  "Recomputed in q2 above: survival and egg production both fall as the concentration rises and both reach zero in the strongest treatment. Reduced reproduction and death outside the range of tolerance are two of the outcomes named in STB-3.B.1."),
 ("Increasing ocean temperature, sediment runoff, and destructive fishing practices",
  "STB-3.B.2 verbatim: coral reefs have been suffering damage due to a variety of factors, including increasing ocean temperature, sediment runoff, and destructive fishing practices. Cooling water, rising oxygen and the remaining options appear nowhere in that statement."),
 ("falls as the sediment reaching the reef rises",
  "Recomputed in q4 above: ordering the sections by sediment delivery puts coral cover in decreasing order, with the least coral where sediment is greatest. Sediment runoff is one of the factors named in STB-3.B.2."),
 ("sinking components kill some bottom-dwelling organisms",
  "STB-3.B.3 near verbatim: oil spills cause organisms to die from the hydrocarbons in oil, floating oil can coat the feathers of birds and fur of marine mammals, and some components sink to the ocean floor killing some bottom-dwelling organisms. None of the rejected descriptions appears in the framework."),
 ("released 640,000 liters",
  "Recomputed in q6 above: four thousand barrels times one hundred and sixty liters per barrel is six hundred and forty thousand liters, and each rejected value is checked to differ from that product, including the sum of the two quantities. Suggested skill 6.B."),
 ("fishing and tourism industries",
  "STB-3.B.4 near verbatim: oil that washes up on the beach can have economic consequences on the fishing and tourism industries. No such consequence is attached to mining, forestry, electricity generation or rainfall."),
 ("area of low oxygen in the world's oceans caused by increased nutrient pollution",
  "STB-3.B.5 verbatim. Depth, legal closure, an oil slick and low temperature are not part of the definition the framework gives for an oceanic dead zone."),
 ("largest in the year the river carried the most nitrogen",
  "Recomputed in q9 above: ranking the years by nitrogen carried gives the same order as ranking them by zone area, so the extremes coincide. STB-3.B.5 attributes oceanic dead zones to increased nutrient pollution."),
 ("plot of dissolved oxygen levels against distance from a source of pollution",
  "STB-3.B.6 near verbatim: an oxygen sag curve is a plot of dissolved oxygen levels versus the distance from a source of pollution, usually excess nutrients and biological refuse. The rejected options plot other quantities against other variables."),
 ("falls to a minimum a few kilometers below the outfall and then recovers",
  "Recomputed in q11 above: the values fall from the outfall to an interior minimum and rise again beyond it. That shape is what STB-3.B.6 defines the oxygen sag curve to plot."),
 ("Industry, especially mining and the burning of fossil fuels",
  "STB-3.B.7 near verbatim: heavy metals used for industry, especially mining and burning of fossil fuels, can reach the groundwater, impacting the drinking water supply. Rainfall, photosynthesis, decomposition and evaporation are not given as their source."),
 ("Groundwater is a drinking water supply",
  "STB-3.B.7's own wording makes the concern the impact on the drinking water supply, which is a route from an industrial source to the people who use the water. It does not depend on the metals being altered underground, and the framework does not have them become harmless."),
 ("Intestinal blockage and choking hazards for wildlife",
  "STB-3.B.8 near verbatim: litter that reaches aquatic ecosystems, besides being unsightly, can create intestinal blockage and choking hazards for wildlife and introduce toxic substances to the food chain. None of the rejected effects is attributed to litter."),
 ("reduces light infiltration, affecting primary producers and visual predators",
  "STB-3.B.9 near verbatim: increased sediment in waterways can reduce light infiltration, which can affect primary producers and visual predators, and sediment can also settle, disrupting habitats. The rejected options reverse the light effect or borrow another statement's role."),
 ("light penetrates less deeply and the algal growth measured at a fixed depth falls",
  "Recomputed in q16 above: both the depth reached by light and the algal growth fall at every step as sediment rises. Reduced light infiltration affecting primary producers is exactly the effect named in STB-3.B.9."),
 ("Bacteria in the water convert the mercury to highly toxic methylmercury",
  "STB-3.B.10 near verbatim: when elemental sources of mercury enter aquatic environments, bacteria in the water convert it to highly toxic methylmercury. No evaporation, permanent settling or neutralizing role is described for mercury."),
 ("methylmercury is present wherever mercury is",
  "Recomputed in q18 above: both columns are largest at the site nearest the mine, both fall at every step with distance, and every sample carries some methylmercury. STB-3.B.10 supplies the conversion by bacteria in the water."),
 ("600 kilograms of the dissolved metal past the town each day",
  "Recomputed in q19 above: two hundred million liters times three milligrams per liter is six hundred million milligrams, or six hundred kilograms, and each rejected value is checked to differ. Suggested skill 6.B, with STB-3.B.7 supplying the industrial metal."),
 ("range of tolerance with an optimum range",
  "STB-3.B.1 describes exactly this: an optimum range for each factor in which homeostasis is maintained, with physiological stress, limited growth and reduced reproduction outside it. The rejected options name unrelated statements from the same topic."),
 ("Floating oil coats the feathers of birds and the fur of marine mammals",
  "STB-3.B.3 places harm at both levels of the water column, assigning the coating of feathers and fur to oil at the surface and the killing of bottom dwellers to components that sink. Neither part is described as harmless."),
 ("economic consequences on the fishing and tourism industries",
  "STB-3.B.4 attaches economic consequences for fishing and tourism to oil washing up on a beach, which is what lost fleet and hotel income is. The rejected statements describe ecological or health effects rather than economic ones."),
 ("reduction in the nutrient pollution reaching that part of the ocean",
  "STB-3.B.5 attributes oceanic dead zones to increased nutrient pollution, so reducing that pollution addresses the stated cause. Litter under STB-3.B.8, mercury under STB-3.B.10 and light under STB-3.B.9 are given other effects."),
 ("how dissolved oxygen changes with position downstream",
  "STB-3.B.6 defines the curve as a plot against the distance from a source of pollution, so distance is the variable by construction. The rejected options change the plotted quantity or deny that oxygen varies."),
 ("visual predator depends on being able to see its prey",
  "STB-3.B.9 attributes to increased sediment a reduction in light infiltration that affects primary producers and visual predators, so the harm runs through the loss of light rather than through toxicity."),
 ("convert elemental mercury entering an aquatic environment into highly toxic methylmercury",
  "STB-3.B.10 makes the change one of chemical form, carried out by bacteria in the water, rather than a change in concentration. The framework gives no other route by which mercury becomes more toxic."),
 ("physiological stress, limited growth and reduced reproduction while remaining alive",
  "STB-3.B.1 lists those three for conditions outside the optimum range and reserves death for extreme cases, so sublethal harm is what it predicts just outside the range. It does not describe organisms as unaffected up to a lethal level."),
 ("variety of factors, and all three of these are among them",
  "STB-3.B.2 states that reefs have been suffering damage due to a variety of factors and names these three among them, without ranking them or limiting how many may act at once."),
 ("especially mining, can reach the groundwater",
  "STB-3.B.7 names mining among the industrial uses whose heavy metals can reach groundwater and impact the drinking water supply, which is the pollutant and the setting in the stem. The rejected statements concern different pollutants in different settings."),
 ("mercury is converted to a more toxic form",
  "Each clause of the summary is one of the ten statements STB-3.B.1 to STB-3.B.10, which together cover organisms, habitats, coastal economies and drinking water. Every rejected summary omits or denies most of them."),
]

TABLE_CHECKS = {2: q2, 4: q4, 6: q6, 9: q9, 11: q11, 16: q16, 18: q18, 19: q19}

es.run(e8_2, CLAIMS, TABLE_CHECKS, sys.argv)
