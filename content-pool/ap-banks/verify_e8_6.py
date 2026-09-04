"""Key audit for AP ENVIRONMENTAL SCIENCE 8.6 Thermal Pollution.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.G.1  thermal pollution occurs when heat released into the water
             produces negative effects to the organisms in that ecosystem --
             items 1, 4, 5, 7, 11, 14, 17, 19, 20, 22, 23, 29;
  STB-3.G.2  variations in water temperature affect the concentration of
             dissolved oxygen because warm water does not contain as much
             oxygen as cold water -- items 2, 3, 6, 8, 9, 10, 12, 13, 15, 16,
             18, 21, 24, 26, 27, 28;
  STB-3.F.1  (topic 8.5, cited only to separate the two causes) eutrophication
             occurs when a body of water is enriched in nutrients -- item 25.
Item 30 joins both statements of this topic.

SCOPE. The oxygen sag curve and the oceanic dead zone are keyed in 8.2 under
STB-3.B.5 and STB-3.B.6, and the nutrient route to low oxygen in 8.5 under
STB-3.F.2. No key here attributes an oxygen change to nutrients; every key
turns on heat.

NOT KEYED: no numeric temperature threshold, no lethal oxygen concentration and
no named power station. The framework states none of them, so the data items
key only directions and rank orders, each recomputed below.

DATA ITEMS: 3, 4, 6, 8, 10 and 12 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_6.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_6

TEMP_SAT = "Water temperature (degrees Celsius)"
DO_SAT = "Dissolved oxygen the water can hold (milligrams per liter)"
TEMP_SITE = "Water temperature (degrees Celsius)"
DO_SITE = "Dissolved oxygen (milligrams per liter)"
FISH_SITE = "Cold water fish counted in one hour"
RISE_TOWER = "Temperature rise the discharge adds to the river (degrees Celsius)"
DO_TOWER = "Dissolved oxygen below the outfall (milligrams per liter)"
DEAD_TOWER = "Fish found dead below the outfall each year"
TEMP_SEA = "River temperature (degrees Celsius)"
DO_SEA = "Dissolved oxygen (milligrams per liter)"
RISE_RIV = "Temperature rise the discharge adds (degrees Celsius)"
FALL_RIV = "Fall in dissolved oxygen below the outfall (milligrams per liter)"
TOL = "Highest water temperature the species tolerates (degrees Celsius)"
COUNT_TOL = "Individuals counted at the warm outfall in one hour"


def q3(table, item):
    temp = cg.col(table, TEMP_SAT)
    do = cg.col(table, DO_SAT)
    pairs = sorted(zip(temp, do))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the oxygen the water can hold does not fall at every step: {pairs}"
    assert do[temp.index(max(temp))] == min(do), \
        "'the warmest row holds the most oxygen' must be false"
    assert len(set(do)) == len(do), "'the same at every temperature' must be false"
    return (f"sorted by temperature the oxygen values run {[d for _, d in pairs]} "
            "milligrams per liter, falling at every step")


def q4(table, item):
    sites = cg.labels(table)
    temp = cg.col(table, TEMP_SITE)
    do = cg.col(table, DO_SITE)
    fish = cg.col(table, FISH_SITE)
    hot = temp.index(max(temp))
    assert do[hot] == min(do), "the warmest site is not the lowest in dissolved oxygen"
    assert fish[hot] == min(fish), "the warmest site does not hold the fewest fish"
    up = [i for i, s in enumerate(sites) if s.lower().startswith("two kilometers above")][0]
    assert fish[up] == max(fish), "the upstream site does not hold the most fish"
    below = [i for i, s in enumerate(sites) if "below the outfall" in s.lower()]
    ordered = sorted(below, key=lambda i: temp[i], reverse=True)
    assert all(do[ordered[k]] < do[ordered[k + 1]] for k in range(len(ordered) - 1)), \
        "oxygen does not recover as the downstream sites cool"
    assert all(fish[ordered[k]] < fish[ordered[k + 1]] for k in range(len(ordered) - 1)), \
        "the fish counts do not recover as the downstream sites cool"
    assert len(set(temp)) == len(temp), "'the same temperature everywhere' must be false"
    return (f"the warmest site is {sites[hot]} at {temp[hot]} degrees with {do[hot]} "
            f"milligrams per liter and {fish[hot]:.0f} fish, both recovering downstream")


def q6(table, item):
    stages = cg.labels(table)
    rise = cg.col(table, RISE_TOWER)
    do = cg.col(table, DO_TOWER)
    dead = cg.col(table, DEAD_TOWER)
    n = len(stages)
    assert all(rise[i] > rise[i + 1] for i in range(n - 1)), \
        f"the temperature rise does not fall across the stages: {rise}"
    assert all(do[i] < do[i + 1] for i in range(n - 1)), \
        f"the dissolved oxygen does not rise across the stages: {do}"
    assert all(dead[i] > dead[i + 1] for i in range(n - 1)), \
        f"the yearly death count does not fall across the stages: {dead}"
    return (f"the temperature rise runs {rise} degrees while oxygen runs {do} and the "
            f"death count runs {dead}, falling, rising and falling in that order")


def q8(table, item):
    months = cg.labels(table)
    temp = cg.col(table, TEMP_SEA)
    do = cg.col(table, DO_SEA)
    hot, cold = temp.index(max(temp)), temp.index(min(temp))
    assert do[hot] == min(do), f"the warmest month is not the lowest in oxygen: {do}"
    assert do[cold] == max(do), f"the coldest month is not the highest in oxygen: {do}"
    assert len(set(do)) == len(do), "'identical in all four months' must be false"
    return (f"{months[hot]} is warmest at {temp[hot]} degrees with the smallest oxygen "
            f"value {do[hot]}, and {months[cold]} is coldest with the largest {do[cold]}")


def q10(table, item):
    rivers = cg.labels(table)
    rise = cg.col(table, RISE_RIV)
    fall = cg.col(table, FALL_RIV)
    order = [r for _, r in sorted(zip(rise, rivers))]
    assert order == [r for _, r in sorted(zip(fall, rivers))], \
        f"the order by temperature rise does not match the order by oxygen fall: {rise} {fall}"
    assert len(set(fall)) == len(fall), "'the same fall in all three' must be false"
    assert fall[rise.index(min(rise))] == min(fall), \
        "'the smallest rise gives the largest fall' must be false"
    return (f"ranking by temperature rise gives {order}, the same order as ranking by the "
            "fall in dissolved oxygen")


def q12(table, item):
    species = cg.labels(table)
    tol = cg.col(table, TOL)
    count = cg.col(table, COUNT_TOL)
    order = [s for _, s in sorted(zip(tol, species))]
    assert order == [s for _, s in sorted(zip(count, species))], \
        f"the order by tolerance does not match the order by abundance: {tol} {count}"
    assert count[tol.index(min(tol))] == min(count), \
        "the least tolerant species is not the least numerous"
    assert count[tol.index(max(tol))] == max(count) > 0, \
        "the most tolerant species is not the most numerous, or is absent"
    assert len(set(count)) == len(count), "'equally numerous' must be false"
    return (f"ranking the species by tolerance gives {order}, the same order as ranking "
            "them by the count at the outfall")


CLAIMS = [
 ("heat released into the water produces negative effects",
  "STB-3.G.1 verbatim: thermal pollution occurs when heat released into the water produces negative effects to the organisms in that ecosystem. Nutrient enrichment is STB-3.F.1, litter STB-3.B.8, sediment STB-3.B.9 and acidity STB-4.H.1."),
 ("does not contain as much oxygen as cold water",
  "STB-3.G.2 verbatim: variations in water temperature affect the concentration of dissolved oxygen because warm water does not contain as much oxygen as cold water. Every rejected option denies or reverses that."),
 ("falls at every step as the temperature rises",
  "Recomputed in q3 above: sorted by temperature, the oxygen values fall at every step and the warmest row holds the smallest value. That is the direction STB-3.G.2 states."),
 ("fewest cold water fish, and both recover as the river cools",
  "Recomputed in q4 above: the warmest site holds the smallest oxygen value and the smallest fish count, and both rise again at the cooler downstream sites. STB-3.G.1 makes negative effects on organisms the mark of thermal pollution and STB-3.G.2 supplies the oxygen link."),
 ("not on whether a substance is added",
  "STB-3.G.1 defines thermal pollution by the negative effects released heat produces on the organisms in that ecosystem, so the harm rather than the addition of a substance is what makes it pollution."),
 ("dissolved oxygen below the outfall rose and the number of dead fish fell",
  "Recomputed in q6 above: the temperature rise falls at every stage while the oxygen rises and the yearly death count falls at every stage. That is STB-3.G.1 and STB-3.G.2 run backward as the heat load is cut."),
 ("closer to the river's own temperature",
  "STB-3.G.1 attributes the harm to heat released into the water, so removing heat before discharge addresses the stated cause. A longer pipe, more frequent measurement and litter screens leave the heat load unchanged."),
 ("highest river temperature carries the lowest dissolved oxygen",
  "Recomputed in q8 above: the warmest month holds the smallest oxygen value and the coldest month the largest. STB-3.G.2 states that warm water does not contain as much oxygen as cold water."),
 ("so the warmed reach offers less oxygen as well as more heat",
  "STB-3.G.2 ties a temperature rise to a fall in dissolved oxygen, so the warmed water is unfavorable in two ways at once, and STB-3.G.1 defines the pollution by the negative effects on organisms."),
 ("the larger the fall in dissolved oxygen below the outfall",
  "Recomputed in q10 above: ranking the rivers by the temperature rise gives the same order as ranking them by the fall in dissolved oxygen, which is the dependence STB-3.G.2 states."),
 ("has lost species that lived there before",
  "STB-3.G.1 requires both released heat and negative effects on the organisms in that ecosystem, so a temperature difference alone does not meet the definition while a temperature difference plus a loss of resident species does."),
 ("least numerous at the outfall, and the most tolerant species is the most numerous",
  "Recomputed in q12 above: the order by temperature tolerance is the order by abundance at the outfall, from none for the least tolerant to the largest count for the most tolerant. STB-3.G.1 makes such effects on organisms the mark of thermal pollution."),
 ("sets how much oxygen the water can hold",
  "STB-3.G.2 makes the concentration of dissolved oxygen depend on water temperature, and STB-3.G.1 makes the negative effects on organisms the definition. The framework gives no salinity, depth or acidity role in this statement."),
 ("Heat released into the water can produce negative effects",
  "Cooling water returned from an industrial process carries waste heat, which is exactly the case STB-3.G.1 describes. The rejected statements are STB-3.F.2, STB-3.B.8, STB-3.B.9 and STB-3.B.10, which belong to other topics of this unit."),
 ("so a heated reach can leave organisms with less oxygen",
  "STB-3.G.2 states that warm water does not contain as much oxygen as cold water and STB-3.G.1 makes the resulting harm to organisms the definition of thermal pollution. Each rejected pairing reverses one half of that."),
 ("measured together above and below the outfall",
  "STB-3.G.2 links two quantities, so a test needs both measured where the discharge should have an effect and where it should not. A single downstream reading or an upstream temperature alone leaves one side unmeasured."),
 ("which is what thermal pollution means",
  "STB-3.G.1 defines thermal pollution by the negative effects released heat produces on the organisms in that ecosystem, and the loss of the resident cold water community is such an effect."),
 ("the oxygen it can hold is already lower",
  "STB-3.G.2 makes the oxygen a river can hold fall as its temperature rises, so a warm starting temperature leaves less oxygen before the discharge is added, and STB-3.G.1 attaches the harm to that heat."),
 ("so heat is still being released into the ecosystem",
  "STB-3.G.1 turns on heat released into the water and its negative effects on organisms, and redistributing the same heat does not remove it. The framework offers no statement making a discharge harmless by being spread out."),
 ("carry waste heat away from an industrial process",
  "STB-3.G.1 describes heat released into the water, and cooling water returned from an industrial process carries exactly that heat. Rain, cold groundwater, snowmelt and shade release no waste heat."),
 ("so a change in heat shows up as a change in oxygen",
  "STB-3.G.2 makes the concentration of dissolved oxygen depend on water temperature, so the oxygen record carries the signature of the heat. The discharge releases heat rather than oxygen."),
 ("there is no basis for negative effects from heat",
  "STB-3.G.1 makes released heat the cause and negative effects on organisms the consequence, so removing the heat removes the stated mechanism. The framework does not define the pollution by withdrawal or by volume."),
 ("same species at the same abundances as the reach above it",
  "STB-3.G.1 requires negative effects on the organisms, so an unchanged community below the outfall removes the harm the claim asserts. A temperature difference or a lower oxygen reading would support it instead."),
 ("raises its temperature less",
  "STB-3.G.2 makes the oxygen concentration follow the temperature, and a given quantity of heat produces a smaller temperature change in a larger volume, so the negative effects of STB-3.G.1 should be smaller."),
 ("while eutrophication begins with a body of water becoming enriched in nutrients",
  "STB-3.G.1 makes released heat the cause of thermal pollution while STB-3.F.1 makes nutrient enrichment the cause of eutrophication, so the two reach low oxygen by different routes and neither is defined by the type of water."),
 ("so it can hold the least oxygen",
  "STB-3.G.2 makes the oxygen the water can hold fall as temperature rises, so the hottest days start from the lowest oxygen and any added heat deepens the deficit."),
 ("recovers as the water cools downstream",
  "A pattern that tracks the warming in both place and time is what ties the oxygen change to the temperature dependence in STB-3.G.2. Uniformly low oxygen, litter and farmland point to other causes."),
 ("turns released heat into a negative effect",
  "STB-3.G.2 supplies the mechanism that STB-3.G.1's definition depends on, since the heat lowers the oxygen and the lowered oxygen is one of the negative effects on organisms. The relationship itself is a property of water, not of polluted water."),
 ("how much the discharge may raise the temperature of the receiving water",
  "STB-3.G.1 attributes the harm to heat released into the water, so a cap on the temperature rise bounds the stated cause. Staffing, color, pipe depth and operating hours do not."),
 ("because warm water cannot hold as much oxygen as cold water",
  "The keyed summary joins STB-3.G.1, which makes negative effects on organisms the definition, with STB-3.G.2, which supplies the oxygen mechanism. Each rejected summary reverses the oxygen relationship or substitutes a different pollutant."),
]

TABLE_CHECKS = {3: q3, 4: q4, 6: q6, 8: q8, 10: q10, 12: q12}

es.run(e8_6, CLAIMS, TABLE_CHECKS, sys.argv)
