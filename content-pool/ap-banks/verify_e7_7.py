"""Key audit for AP ENVIRONMENTAL SCIENCE 7.7 Acid Rain.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
Items 1, 16 and 23 rest on STB-2.H.1, that acid rain and deposition is due to
nitrogen oxides and sulfur oxides from anthropogenic and natural sources.
Items 2, 3, 14 and 27 rest on STB-2.H.2, which assigns the nitric oxides to
motor vehicles and coal-burning power plants and the sulfur dioxides to
coal-burning power plants.
Items 4, 5, 13, 19, 20, 22 and 25 rest on STB-2.I.1, that acid deposition
mainly affects communities downwind from coal-burning power plants.
Items 6, 9, 12, 17 and 21 rest on STB-2.I.2, the acidification of soils and
bodies of water and the corrosion of human-made structures.
Items 7, 8, 15, 18, 24 and 26 rest on STB-2.I.3, that regional differences in
soils and bedrock affect the impact, with limestone's ability to neutralize as
the framework's own example.
Items 10, 11, 28 and 29 are measurement and design items under suggested skill
4.B, identify a research method, design, and/or measure used. Item 30 joins all
five statements.

THE ONE CONVENTION PRESUPPOSED is the direction of the pH scale: a lower pH is
more acidic. The framework uses that convention itself in STB-4.H.1, where
ocean acidification is defined as the DECREASE in pH of the oceans. No item
asks for a pH value to be recalled and every comparison is recomputed below.

WHAT IS NOT CLAIMED. No region, statute, pH threshold or species is named, and
no key states a neutralization reaction or a formula -- the framework gives
limestone's ability to neutralize and nothing further.

DATA ITEMS: 5, 7, 9, 11, 12 and 14 carry tables and every keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e7_7.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e7_7

DIST = "Distance from the plant (kilometers)"
PH_RAIN = "Average pH of rainfall"
PH_IN = "Average pH of rainfall reaching the lake"
PH_LAKE = "Average pH of the lake water"
PH_SOL = "pH of the solution"
LOSS = "Mass lost by the chips (milligrams)"
COAL = "Coal-burning generating capacity (gigawatts)"
CARS = "Motor vehicles registered (millions)"
SOX = "Sulfur oxides released (thousand tons per year)"
NOX = "Nitrogen oxides released (thousand tons per year)"
PH_START = "Soil pH at the start"
PH_END = "Soil pH at the end"
SOX_T = "Sulfur oxides released by regional power plants (thousand tons per year)"
PH_STN = "Average pH of rainfall at a downwind station"


def q5(table, item):
    sites = cg.labels(table)
    dist = dict(zip(sites, cg.col(table, DIST)))
    ph = dict(zip(sites, cg.col(table, PH_RAIN)))
    down = [s for s in sites if s.startswith("Downwind")]
    up = [s for s in sites if s.startswith("Upwind")]
    assert down and up, "the table must carry downwind and upwind sites"
    ordered = sorted(down, key=lambda s: dist[s])
    assert all(ph[ordered[i]] < ph[ordered[i + 1]] for i in range(len(ordered) - 1)), \
        f"pH does not rise with distance downwind: {[ph[s] for s in ordered]}"
    assert ph[ordered[0]] == min(ph.values()), "the nearest downwind site is not the most acidic"
    assert ph[up[0]] == max(ph.values()), "the upwind site is not the least acidic"
    assert ph[up[0]] != ph[ordered[0]], "'upwind equals nearest downwind' must be false"
    return (f"downwind pH runs {[ph[s] for s in ordered]} with distance, rising throughout, "
            f"against {ph[up[0]]} upwind, the largest value and so the least acidic")


def q7(table, item):
    lakes = cg.labels(table)
    rock = {r[0]: r[1] for r in table["rows"]}
    rain = dict(zip(lakes, cg.col(table, PH_IN)))
    lake = dict(zip(lakes, cg.col(table, PH_LAKE)))
    lime = [k for k in lakes if rock[k] == "limestone"]
    gran = [k for k in lakes if rock[k] == "granite"]
    assert lime and gran, "both bedrock types must appear"
    assert max(rain.values()) - min(rain.values()) <= 0.3, \
        f"the rainfall must be similarly acidic at all four lakes: {rain}"
    assert min(lake[k] for k in lime) > max(lake[k] for k in gran), \
        f"the limestone lakes are not all less acidic: {lake}"
    for k in lime:
        assert lake[k] > rain[k] + 2, f"{k} is not buffered well above its rainfall"
    most_acid_rain = min(rain, key=rain.get)
    assert lake[most_acid_rain] != max(lake.values()), \
        "'the lake with the most acidic rainfall holds the least acidic water' must be false"
    return (f"the limestone lakes hold {[lake[k] for k in lime]} against "
            f"{[lake[k] for k in gran]} in granite, while the rainfall reaching all four "
            f"spans only {max(rain.values()) - min(rain.values()):.1f} of a pH unit")


def q9(table, item):
    ph = cg.col(table, PH_SOL)
    loss = cg.col(table, LOSS)
    pairs = sorted(zip(ph, loss))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"mass loss does not fall as pH rises: {pairs}"
    assert loss[ph.index(min(ph))] == max(loss), "the lowest pH does not carry the greatest loss"
    assert min(loss) > 0, "'the chips gained mass' must be false"
    assert len(set(loss)) == len(loss), "'the same mass in all four' must be false"
    return (f"sorted by pH the mass losses are {[l for _, l in pairs]}, falling as pH rises, "
            f"with the greatest loss {max(loss):.0f} milligrams at pH {min(ph)}")


def q11(table, item):
    sox = cg.col(table, SOX_T)
    ph = cg.col(table, PH_STN)
    assert all(sox[i] > sox[i + 1] for i in range(len(sox) - 1)), \
        f"the released sulfur oxides do not fall across the periods: {sox}"
    assert all(ph[i] < ph[i + 1] for i in range(len(ph) - 1)), \
        f"the rainfall pH does not rise across the periods: {ph}"
    return (f"releases run {sox} thousand tons, falling at every step, while rainfall pH runs "
            f"{ph}, rising at every step, so the rain becomes less acidic as releases fall")


def q12(table, item):
    plots = cg.labels(table)
    start = dict(zip(plots, cg.col(table, PH_START)))
    end = dict(zip(plots, cg.col(table, PH_END)))
    shelter = [p for p in plots if "sheltered" in p.lower()]
    exposed = [p for p in plots if p not in shelter]
    assert len(shelter) == 1 and len(exposed) == 2, "one sheltered plot and two exposed are required"
    for p in exposed:
        assert start[p] - end[p] > 0.5, f"{p} did not acidify appreciably"
    s = shelter[0]
    assert abs(start[s] - end[s]) < 0.2, "the sheltered plot must be close to unchanged"
    assert end[s] > max(end[p] for p in exposed), \
        "'the sheltered plot became the most acidic' must be false"
    return (f"the exposed plots fell by {[round(start[p] - end[p], 1) for p in exposed]} pH units "
            f"against {round(start[s] - end[s], 1)} for the sheltered plot")


def q14(table, item):
    regions = cg.labels(table)
    coal = dict(zip(regions, cg.col(table, COAL)))
    cars = dict(zip(regions, cg.col(table, CARS)))
    sox = dict(zip(regions, cg.col(table, SOX)))
    nox = dict(zip(regions, cg.col(table, NOX)))
    assert max(sox, key=sox.get) == max(coal, key=coal.get), \
        "the most sulfur oxides do not belong to the region with the most coal capacity"
    assert max(nox, key=nox.get) == max(cars, key=cars.get), \
        "the most nitrogen oxides do not belong to the region with the most vehicles"
    assert max(sox, key=sox.get) != max(nox, key=nox.get), \
        "'the coal region also releases the most nitrogen oxides' must be false"
    assert min(sox, key=sox.get) == min(coal, key=coal.get), \
        "the region with no coal capacity should hold the smallest sulfur figure"
    return (f"sulfur oxides peak in {max(sox, key=sox.get)}, which holds the most coal capacity, "
            f"and nitrogen oxides in {max(nox, key=nox.get)}, which holds the most vehicles")


CLAIMS = [
 ("Nitrogen oxides and sulfur oxides in the atmosphere",
  "STB-2.H.1 near verbatim: acid rain and deposition is due to nitrogen oxides and sulfur oxides from anthropogenic and natural sources in the atmosphere. Carbon dioxide, chlorofluorocarbons, radon and ozone are treated in other topics and are not given as the cause of acid deposition."),
 ("Motor vehicles and coal-burning power plants",
  "STB-2.H.2, first sentence, verbatim: nitric oxides that cause acid deposition come from motor vehicles and coal-burning power plants. Volcanic vents alone, fertilizer, radioactive decay and evaporation are not assigned that role anywhere in the framework."),
 ("Coal-burning power plants",
  "STB-2.H.2, second sentence: sulfur dioxides that cause acid deposition come from coal-burning power plants. Motor vehicles are named for the nitric oxides rather than the sulfur, and limestone appears in STB-2.I.3 as a neutralizer rather than a source."),
 ("Communities downwind from coal-burning power plants",
  "STB-2.I.1 near verbatim: acid deposition mainly affects communities that are downwind from coal-burning power plants. Position over a coal seam, a coastal location, or the absence of any plant is not the pattern the framework gives."),
 ("most acidic at the nearest downwind site",
  "Recomputed in q5 above: the smallest pH is at the nearest downwind site, pH rises with distance downwind, and the upwind site holds the largest value of all. That is the downwind pattern of STB-2.I.1, read with the convention that lower pH is more acidic."),
 ("acidification of bodies of water, and corrosion of human-made structures",
  "STB-2.I.2 near verbatim: acid rain and deposition can lead to the acidification of soils and bodies of water and corrosion of human-made structures. The rejected lists belong to unit 9, to the health effects of other pollutants, or to land use in unit 5."),
 ("lakes in limestone basins hold much less acidic water",
  "Recomputed in q7 above: the rainfall reaching all four lakes spans a third of a pH unit, while each limestone lake sits more than two pH units above its rainfall and above both granite lakes. STB-2.I.3 gives limestone's ability to neutralize as its example of regional differences."),
 ("neutralize the effect of acid rain on lakes and ponds",
  "STB-2.I.3 near verbatim: regional differences in soils and bedrock affect the impact acid deposition has on the region, such as limestone bedrock's ability to neutralize the effect of acid rain on lakes and ponds. The framework gives limestone no role as a source and no effect on rainfall itself."),
 ("greatest loss in the solution of lowest pH",
  "Recomputed in q9 above: ordering the solutions by pH puts the largest mass loss at the lowest pH and the smallest at the highest, and every chip lost mass. STB-2.I.2 names corrosion of human-made structures among the effects of acid deposition."),
 ("pH of the collected rainwater",
  "Suggested skill 4.B, identify a measure used. Acidity is what pH reports, so it is the measure that answers the question asked; volume, temperature, frequency of rainfall and distance to a source describe the sample or the setting instead."),
 ("rainfall at the downwind station became less acidic",
  "Recomputed in q11 above: the released sulfur oxides fall at every step while the rainfall pH rises at every step, which is a fall in acidity. STB-2.H.2 attributes the sulfur dioxides causing acid deposition to coal-burning power plants."),
 ("while the sheltered plot barely changed",
  "Recomputed in q12 above: each exposed plot fell by more than half a pH unit and the sheltered plot by less than two tenths, and the sheltered plot ends the least acidic. STB-2.I.2 names acidification of soils among the effects of acid deposition."),
 ("varies distance and direction from a suspected source",
  "Suggested skill 4.B, identify a research design. Sites placed at different distances along and against the prevailing wind are what make the downwind pattern of STB-2.I.1 visible; holding position constant or measuring something other than rainfall would not."),
 ("while the region with the most vehicles releases the most nitrogen oxides",
  "Recomputed in q14 above: the largest sulfur figure belongs to the region with the most coal capacity and the largest nitrogen figure to the region with the most vehicles, and they are different regions. That is the split STB-2.H.2 draws between the two oxides."),
 ("one region's bedrock can neutralize the acid",
  "STB-2.I.3 states that regional differences in soils and bedrock affect the impact acid deposition has, with limestone's neutralizing ability as the example. Rainfall amount, lake depth and upwind position are not what the framework names."),
 ("from human activities and from processes that occur without them",
  "STB-2.H.1 places nitrogen oxides and sulfur oxides in the atmosphere from anthropogenic AND natural sources, which is exactly what both kinds of origin means. The framework does not describe acids being released ready-made or restrict natural sources to acids."),
 ("corrosion of human-made structures",
  "STB-2.I.2 lists corrosion of human-made structures among the effects of acid deposition, and a stone monument is such a structure. The rejected statements concern water, geography or sources rather than damage to a built object."),
 ("compared with the pH of the lake water itself",
  "STB-2.I.3's buffering shows as a difference between the acidity arriving in rainfall and the acidity of the water that results, so those two pH values are the comparison that reveals it. Temperature, volume, stream count and a distant reading leave it unmade."),
 ("Less acidic rainfall downwind",
  "STB-2.H.2 makes coal-burning power plants the source of the sulfur dioxides that cause acid deposition and STB-2.I.1 places the affected communities downwind of them, so a large cut in that release should reduce the acidity arriving downwind. Nothing in the framework makes a sulfur cut raise nitrogen oxides."),
 ("travel through the atmosphere and are deposited downwind",
  "STB-2.I.1 locates the affected communities downwind of coal-burning power plants, which requires the released oxides to travel from the plant to them. The absence of a local plant is therefore no protection, and the framework gives no indoor or naturally acidic alternative for this."),
 ("pH of the soil, measured over time at the same plots",
  "Suggested skill 4.B with STB-2.I.2: acidification of soils is one of the named effects and soil pH is its measure, taken repeatedly at fixed plots so a change can be seen. Tree height, visitor numbers, distance and temperature measure nothing about soil acidity."),
 ("downwind of the plant than at comparable sites upwind",
  "STB-2.I.1's downwind pattern is precisely what a paired downwind and upwind comparison over the same period tests. Building size, rainfall amount, a single measurement and fuel type elsewhere bear on none of it."),
 ("both are attributed to the same oxides",
  "STB-2.H.1 treats acid rain and deposition together and attributes both to nitrogen oxides and sulfur oxides from anthropogenic and natural sources. The framework does not split them by land use, by bedrock, or by pollutant."),
 ("limestone can neutralize the effect of the acid",
  "STB-2.I.3's own example is limestone bedrock's ability to neutralize the effect of acid rain on lakes and ponds, so the limestone basin is the buffered one. Hardness is not a property the framework mentions, and it does not claim bedrock prevents all acidification."),
 ("wind direction identifies which sites should show the effect",
  "Suggested skill 4.B with STB-2.I.1. Because the framework's pattern is a downwind one, the wind direction is what determines which sites are expected to be affected and which serve as comparisons; it does not change the scale, the bedrock or the fuel burned."),
 ("Regional differences in soils and bedrock",
  "STB-2.I.3 is the framework's own denial that the impact is uniform across regions, with limestone's neutralizing ability as the example. The rejected statements concern the sources or the effects rather than variation between regions."),
 ("Motor vehicles and coal-burning power plants",
  "STB-2.H.2 names motor vehicles and coal-burning power plants as the sources of the nitric oxides that cause acid deposition. Refrigerators, quarries, landfills, sewage plants and irrigation are given no such role anywhere in the framework."),
 ("One storm at one site cannot show whether acidic rainfall is typical",
  "Suggested skill 4.B. A single sample at a single place cannot establish that the value represents the region, which is what the conclusion claims. The measure itself is the appropriate one and can be taken during a storm."),
 ("three effects the framework lists",
  "Acidified lakes, damaged building stone and falling soil pH are the acidification of bodies of water, the corrosion of human-made structures and the acidification of soils named in STB-2.I.2, and the community's position is the downwind one of STB-2.I.1. The rejected options belong to other topics with different effects."),
 ("with the local bedrock affecting how severe the impact is",
  "Each clause is one of the framework's statements: STB-2.H.1 for the oxides and their sources, STB-2.H.2 for the plants and vehicles, STB-2.I.1 for the downwind communities, STB-2.I.2 for the three effects and STB-2.I.3 for the regional differences. Every rejected summary contradicts at least one of them."),
]

TABLE_CHECKS = {5: q5, 7: q7, 9: q9, 11: q11, 12: q12, 14: q14}

es.run(e7_7, CLAIMS, TABLE_CHECKS, sys.argv)
