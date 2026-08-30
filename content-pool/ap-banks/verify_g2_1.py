"""Key audit for AP HUMAN GEOGRAPHY 2.1 Population Distribution.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-2.A, PSO-2.B and PSO-2.C between them print four
essential-knowledge statements:

    PSO-2.A.1  Physical factors (e.g., climate, landforms, water bodies) and
               human factors (e.g., culture, economics, history, politics)
               influence the distribution of population.
    PSO-2.A.2  Factors that illustrate patterns of population distribution vary
               according to the scale of analysis.
    PSO-2.B.1  The three methods for calculating population density are
               arithmetic, physiological, and agricultural.
    PSO-2.C.1  The method used to calculate population density reveals different
               information about the pressure the population exerts on the land.

PSO-2.B.1 names the three methods but does NOT define them, so every key that
turns on a formula rests on the standard definitions, recorded in the module
header and repeated here because they are what a reader must audit against:

    arithmetic     = population / total land area
    physiological  = population / arable land area
    agricultural   = farmers    / arable land area

The consequence students reverse, and the reason items 7, 18, 19 and 27 exist:
a LOW agricultural density means few farmers working a large area, which is
mechanization -- not scarcity of farmland and not a small population. Nothing in
the CED says this, so those claims are argued from the formula rather than
cited.

Items citing PSO-2.A.1 (physical/human split): 1, 2, 3, 11, 12, 22, 23.
Items citing PSO-2.A.2 (scale): 4, 13, 16.
Items citing PSO-2.B.1 or PSO-2.C.1 (methods and what they reveal): 5, 6, 8, 9,
10, 20, 24, 25, 26.
Items arguing from the formulas without a citation: 7, 14, 15, 17, 18, 19, 21,
27, 28, 29, 30.

The five table items (26-30) are the computational gate, and three of them exist
to force the reader past the obvious column:

  26  changing the denominator to arable land REVERSES which of two countries
      looks crowded -- the recompute asserts the reversal is real
  27  the country with the most farmers is not the one with the highest labour
      intensity, and the mechanized one is the one with the fewest farmers
  28  the most populous region is not the region under the greatest pressure,
      and neither is the region with the least arable land

REVIEW NOTE, written while building the tables. Item 28's first draft offered
"the region with the least arable land" as a distractor, but in that draft the
keyed region actually HAD the least arable land, so the distractor was
accidentally true of the answer. The fourth row was rewritten so the smallest
arable area belongs to a region that is not the key, and the recompute below
asserts that separation. Item 30's keyed choice originally said the ratio had
"doubled" when it had gone from 250 to 600, which is more than double; the
wording was corrected. No key was changed in either case.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_1


def q26_two_denominators(table):
    """Arithmetic and physiological density rank the two countries oppositely."""
    arith, phys = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        pop = num(d["Population (millions)"]) * 1e6
        total = num(d["Total land area (thousand km2)"]) * 1e3
        arable = num(d["Arable land (thousand km2)"]) * 1e3
        arith[d["Country"]] = pop / total
        phys[d["Country"]] = pop / arable
    assert arith["Country A"] == 100 and arith["Country B"] == 80, arith
    assert phys["Country A"] == 250 and phys["Country B"] == 800, phys
    # The reversal is the whole point of the item.
    assert max(arith, key=arith.get) != max(phys, key=phys.get), (arith, phys)
    return "100 per km2"


def q27_agricultural_density(table):
    """Farmers per unit of arable land; the lowest value is the mechanized one."""
    dens, farmers = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        farmers[d["Country"]] = num(d["Farmers (thousands)"])
        dens[d["Country"]] = farmers[d["Country"]] / num(d["Arable land (thousand km2)"])
    assert dens == {"Country P": 20, "Country Q": 2, "Country R": 15}, dens
    lowest = min(dens, key=dens.get)
    assert lowest == "Country Q", dens
    # The country with the most farmers must NOT be the mechanized one.
    assert max(farmers, key=farmers.get) != lowest, farmers
    return "2 farmers per square kilometre"


def q28_pressure(table):
    """Physiological density by region, with both false maxima checked."""
    dens, pop, arable = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        pop[d["Region"]] = num(d["Population (thousands)"]) * 1e3
        arable[d["Region"]] = num(d["Arable land (km2)"])
        dens[d["Region"]] = pop[d["Region"]] / arable[d["Region"]]
    worst = max(dens, key=dens.get)
    assert worst == "Region 2", dens
    assert dens["Region 2"] == 1500 and dens["Region 1"] == 800, dens
    # Neither the biggest population nor the smallest arable area may be the key.
    assert max(pop, key=pop.get) != worst, pop
    assert min(arable, key=arable.get) != worst, arable
    return "1,500 people per square kilometre"


def q29_concentration(table):
    """Share of population against share of land, zone by zone."""
    pop, land = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        pop[d["Zone"]] = num(d["Population (millions)"])
        land[d["Zone"]] = num(d["Land area (thousand km2)"])
    tp, tl = sum(pop.values()), sum(land.values())
    assert tp == 100 and tl == 1000, (tp, tl)
    pshare = 100 * pop["River valley"] / tp
    lshare = 100 * land["River valley"] / tl
    assert pshare == 72 and lshare == 4, (pshare, lshare)
    # The desert distractor's premise must be true so the item tests the reading.
    assert 100 * pop["Desert interior"] / tp == 10, pop
    assert 100 * land["Desert interior"] / tl == 90, land
    return "72 percent of the population lives on 4 percent"


def q30_rising_pressure(table):
    """Both terms move, and in opposite directions, so the ratio more than doubles."""
    series = []
    for row in table["rows"]:
        d = rowdict(table, row)
        pop = num(d["Population (millions)"]) * 1e6
        arable = num(d["Arable land (thousand km2)"]) * 1e3
        series.append((num(d["Year"]), pop, arable, pop / arable))
    series.sort()
    dens = [s[3] for s in series]
    assert dens == [250, 400, 600], dens
    assert all(series[i][1] < series[i + 1][1] for i in range(len(series) - 1)), \
        "population does not rise throughout"
    assert all(series[i][2] > series[i + 1][2] for i in range(len(series) - 1)), \
        "arable land does not fall throughout"
    assert dens[-1] > 2 * dens[0], dens
    return "from 250 to 600 people"


CLAIMS = [
 ("Growing-season length is physical",
  "EK PSO-2.A.1 divides the influences on distribution into physical factors such as climate and landforms and human factors such as history, economics and politics. A growing season is fixed by climate while a port sited by an imperial administration is a historical and political decision."),

 ("availability of water for irrigation and settlement",
  "EK PSO-2.A.1 names water bodies among the physical factors influencing distribution. Where rainfall cannot support cultivation the river is the only place agriculture and dense settlement are possible, so the population narrows to the strip the water reaches."),

 ("chosen to serve an export economy",
  "EK PSO-2.A.1 lists history among the human factors influencing population distribution. Ports founded to move goods outward accumulated infrastructure, administration and population that outlasted the trade which created them."),

 ("vary according to the scale of analysis",
  "This restates EK PSO-2.A.2 directly. Climate barely varies across a single city so it cannot explain variation there, while it varies enormously across the globe and explains a great deal of the worldwide pattern."),

 ("Total population divided by total land area",
  "EK PSO-2.B.1 names arithmetic as one of the three methods and it is the simplest: everyone divided by all the land. It reports how crowded a territory is on paper and says nothing about the quality of the land being shared."),

 ("each unit of farmable land must support many people",
  "EK PSO-2.C.1 states that the method used reveals different information about the pressure the population exerts on the land. Dividing by arable land rather than by all land isolates the resource that produces food, so the ratio measures demand on that resource."),

 ("few workers cultivate a large area",
  "With farmers in the numerator and farmland in the denominator, a low ratio means few workers per unit of land, which is what machinery and capital substitution produce. The measure describes labour intensity rather than output, and the CED does not define it, so this is argued from the formula."),

 ("much smaller share of its land in arable use",
  "Equal arithmetic densities fix population against total area, so any difference in physiological density must come from the denominator that changed, which is arable land. EK PSO-2.C.1's point is exactly that the choice of denominator is what each method reveals."),

 ("How much human labour is applied to each unit of farmland",
  "EK PSO-2.C.1 says each method reveals different information about pressure on the land, and agricultural density puts farmers over farmland. That ratio is a statement about labour intensity, while mouths per hectare is what the physiological measure reports."),

 ("Most of its territory is unfarmable",
  "A low arithmetic figure means few people per unit of all land while a high physiological figure means many per unit of arable land, and only a small arable share can produce both at once. EK PSO-2.C.1 treats that divergence as informative rather than contradictory."),

 ("Aridity",
  "EK PSO-2.A.1 lists climate among the physical factors influencing distribution. Where precipitation cannot support crops or households, settlement depends on transported water and energy, which is why desert interiors hold isolated points rather than a spread of population."),

 ("a state decision redirected population",
  "EK PSO-2.A.1 names politics among the human factors influencing the distribution of population. Relocating the machinery of government carries employment, services and migrants with it, which is how a siting decision becomes a demographic fact."),

 ("conceals extreme internal concentration",
  "EK PSO-2.A.2 makes the informative factors depend on the scale of analysis, and one national ratio is the coarsest scale available. Averaging a crowded delta together with an empty desert produces a figure that no part of the country resembles."),

 ("Salinization and urban expansion removing land from cultivation",
  "Physiological density is population over arable land, so with population held fixed only a fall in the denominator can raise it. Yields, mechanization and the size of the farm workforce change output and labour intensity without changing how much land is classified arable."),

 ("Distribution describes where people are arranged",
  "A distribution is a pattern -- clustered, dispersed, linear -- while a density is a computed value for a defined unit. Two countries can share a density and have entirely different distributions, which is why the framework treats them under separate learning objectives."),

 ("The type of housing permitted and built",
  "EK PSO-2.A.2 makes the explanatory factor depend on scale, and within one city latitude, continent and climate are constants that cannot explain variation. Building form varies block by block and is what actually sets residents per hectare."),

 ("High physiological density and high agricultural density",
  "Intensive subsistence farming means many people fed from limited farmland, a high people-per-hectare figure, worked by large numbers of hand labourers, a high farmers-per-hectare figure. The pair together is the signature the two measures were built to produce."),

 ("Low agricultural density with a moderate physiological density",
  "Few farmers spread across a large cultivated area gives a low farmers-per-hectare ratio, while a moderate population divided by ample arable land keeps people-per-hectare unremarkable. The low labour ratio is the diagnostic figure for mechanization."),

 ("Physiological and agricultural densities both fall",
  "Arable land is the denominator of two of the three measures and appears nowhere in the third. Enlarging it therefore lowers both ratios that use it and leaves population over total land exactly where it was."),

 ("relates the population to the land that can actually produce food",
  "EK PSO-2.C.1 is explicit that different methods reveal different information about pressure on the land. A food self-sufficiency question is about the productive resource, and dividing by deserts and ice sheets tells the planner nothing about it."),

 ("because the share of land that is arable differs",
  "Arithmetic density is fixed by the two quantities the provinces share, so it has to be identical for both. The arable denominator is what the terrain changes, and it appears only in the physiological and agricultural measures."),

 ("employment created by an industrial economy",
  "EK PSO-2.A.1 lists economics among the human factors influencing the distribution of population. Elevation, rivers, temperature and harbour depth are landforms, water bodies and climate, which the same statement places on the physical side."),

 ("both physical and human advantages coincide",
  "EK PSO-2.A.1 lists physical and human factors side by side without ranking them, and the great clusters are where the two reinforce one another. Climate permits agriculture, flat land permits farming and building, and navigable water permits the trade that sustains cities."),

 ("averages over land that may be uninhabitable",
  "EK PSO-2.C.1 exists because the three methods answer different questions, and the arithmetic figure divides by every square kilometre whether it is farmable, frozen or vertical. Judging capacity requires the measure whose denominator is the usable land."),

 ("same population data with different denominators",
  "EK PSO-2.B.1 names three methods and EK PSO-2.C.1 says the method chosen reveals different information about pressure on the land. Two of the three change the denominator to arable land and one also replaces the numerator with the farming population."),

 ("100 per km2",
  "Recomputed from the table: arithmetic densities are 100 and 80 per square kilometre while physiological densities are 250 and 800, so changing the denominator to arable land reverses which country looks crowded. The verifier asserts that reversal separately, since it is the whole point of the item.",
  q26_two_denominators),

 ("2 farmers per square kilometre",
  "Recomputed from the table: farmers per thousand square kilometres of arable land are 20, 2 and 15, so the country applying the least labour per unit of land is the one with the fewest farmers rather than the one with the most land. Low labour intensity is the signature of capital substitution.",
  q27_agricultural_density),

 ("1,500 people per square kilometre",
  "Recomputed from the table: physiological densities are 800, 1,500, 600 and 400 people per square kilometre of arable land. The verifier confirms separately that neither the most populous region nor the region with the least arable land is the answer, so both distractors name real but irrelevant extremes.",
  q28_pressure),

 ("72 percent of the population lives on 4 percent",
  "Recomputed from the table: the valley holds 72 of 100 million people on 40 of 1,000 thousand square kilometres, so 72 percent of the population occupies 4 percent of the land. The national arithmetic density of 100 per square kilometre describes none of the three zones.",
  q29_concentration),

 ("from 250 to 600 people",
  "Recomputed from the table: dividing each year's population by that year's arable land gives 250, 400 and 600 people per square kilometre, so the ratio has more than doubled. The verifier also confirms that population rises throughout while arable land falls throughout, which is why the population figure alone does not account for the rise.",
  q30_rising_pressure),
]

hg_check.check(g2_1, CLAIMS, per_topic=30, n_choices=5)
