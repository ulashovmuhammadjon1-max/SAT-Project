"""Key audit for AP ENVIRONMENTAL SCIENCE 8.9 Solid Waste Disposal.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.K.1  solid waste is any discarded material that is not a liquid or gas,
             generated in domestic, industrial, business and agricultural
             sectors -- items 1, 2, 3, 18;
  STB-3.K.2  solid waste is most often disposed of in landfills, which can
             contaminate groundwater and release harmful gases -- items 4, 5,
             6, 16, 19, 25, 27, 28;
  STB-3.K.3  e-waste is composed of discarded electronic devices including
             televisions, cell phones and computers -- items 8, 17;
  STB-3.K.4  a sanitary municipal landfill consists of a bottom liner, a storm
             water collection system, a leachate collection system, a cap and a
             methane collection system -- items 7, 15, 22;
  STB-3.L.1  factors in landfill decomposition include the composition of the
             trash and the conditions needed for microbial decomposition --
             items 11, 13, 26;
  STB-3.L.2  incineration burns waste at high temperatures, significantly
             reducing volume but releasing air pollutants -- items 9, 10, 20,
             29;
  STB-3.L.3  items not accepted in sanitary landfills may be dumped illegally,
             as with tire piles that breed disease-carrying mosquitoes --
             items 12, 21, 24;
  STB-3.L.4  ocean dumping, with other plastic sources, has produced large
             floating islands of trash, and wildlife become entangled in the
             waste and ingest it -- items 14, 23.
Item 30 joins all eight.

SCOPE. Recycling, composting, e-waste reduction and landfill mitigation are
keyed in 8.10 under STB-3.M.1 to STB-3.M.6, and litter's harm to aquatic
wildlife in 8.2 under STB-3.B.8. No key here states a reduction method, and
item 23 rests on STB-3.L.4's own wording rather than on the litter statement.

NOT KEYED: no national waste statistic, no landfill lifetime, no emission limit
and no named site. The framework states none of them, so the data items key
only sums, ratios, rank orders and ranges recomputed below.

DATA ITEMS: 3, 6, 9, 13, 17 and 21 carry tables and every keyed reading is
recomputed here from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_9.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_9

TONS = "Solid waste generated in one region each year (thousands of tons)"
CL = "Chloride measured in the groundwater (milligrams per liter)"
VOL_BEFORE = "Volume of waste before burning (cubic meters)"
VOL_ASH = "Volume of ash remaining after burning (cubic meters)"
AIR = "Air pollutants released (kilograms)"
PCT = "Percent of the material decomposed after five years"
ITEMS = "Number of items received"
TIRES = "Discarded tires left in the pile"
LARVAE = "Mosquito larvae counted in a standard sample"

FRAMEWORK_SECTORS = {"domestic", "industrial", "business", "agricultural"}
EWASTE_ROWS = {"televisions", "cell phones", "computers"}


def q3(table, item):
    sectors = [s.strip().lower() for s in cg.labels(table)]
    tons = cg.col(table, TONS)
    assert set(sectors) == FRAMEWORK_SECTORS, \
        f"the rows are not the four sectors STB-3.K.1 names: {sectors}"
    top = sectors[tons.index(max(tons))]
    assert top == "industrial", f"the largest row is {top}, not industrial"
    assert sectors[tons.index(min(tons))] != "agricultural", \
        "'agricultural is the smallest' must be false"
    assert len(set(tons)) == len(tons), "'all four the same' must be false"
    return (f"the four rows are the sectors STB-3.K.1 names and the largest figure "
            f"{max(tons):.0f} belongs to the industrial row")


def q6(table, item):
    wells = cg.labels(table)
    pos = [str(r[1]).strip().lower() for r in table["rows"]]
    cl = cg.col(table, CL)
    unlined = [i for i, p in enumerate(pos) if "unlined" in p]
    lined = [i for i, p in enumerate(pos) if "bottom liner" in p]
    up = [i for i, p in enumerate(pos) if p.startswith("upgradient")]
    assert len(unlined) == 1 and len(lined) == 1 and len(up) == 1, \
        f"the three positions are not each present exactly once: {pos}"
    u, l, a = unlined[0], lined[0], up[0]
    assert cl[u] > 10 * cl[l], \
        f"the unlined well is not far above the lined well: {cl[u]} against {cl[l]}"
    assert cl[u] == max(cl), "the unlined well is not the most contaminated"
    assert cl[a] < cl[u] and cl[l] < cl[u], "'the wells below are cleaner than above' must be false"
    assert max(cl[l], cl[a]) < 2 * min(cl[l], cl[a]), \
        f"the lined well {cl[l]} is not close to the upgradient value {cl[a]}"
    return (f"{wells[u]} below the unlined section reads {cl[u]} against {cl[l]} at "
            f"{wells[l]} below the lined section and {cl[a]} upgradient")


def q9(table, item):
    batches = cg.labels(table)
    before = cg.col(table, VOL_BEFORE)
    ash = cg.col(table, VOL_ASH)
    air = cg.col(table, AIR)
    fracs = [a / b for a, b in zip(ash, before)]
    for name, b, a, f in zip(batches, before, ash, fracs):
        assert a < b, f"{name}: the ash volume {a} is not smaller than {b}"
        assert 0.05 <= f <= 0.15, f"{name}: the remaining fraction {f:.3f} is not about a tenth"
    assert all(p > 0 for p in air), f"some batch released no air pollutants: {air}"
    biggest = before.index(max(before))
    assert ash[biggest] != min(ash), \
        "'the largest starting volume left the smallest ash' must be false"
    return (f"the ash fractions are {[round(f, 3) for f in fracs]}, about a tenth in every "
            f"batch, and the air pollutant figures {air} are all positive")


def q13(table, item):
    materials = cg.labels(table)
    pct = cg.col(table, PCT)
    assert max(pct) > 80, f"no material decomposed nearly completely: {pct}"
    assert min(pct) < 5, f"no material resisted decomposition: {pct}"
    assert len(set(pct)) == len(pct), "'all five the same' must be false"
    food = [i for i, m in enumerate(materials) if m.strip().lower() == "food scraps"][0]
    plastic = [i for i, m in enumerate(materials) if "plastic" in m.lower()][0]
    glass = [i for i, m in enumerate(materials) if "glass" in m.lower()][0]
    assert pct[food] > pct[plastic] and pct[food] > pct[glass], \
        "'plastic and glass decomposed more than the food scraps' must be false"
    assert pct[food] == max(pct) and pct[glass] == min(pct), \
        f"the food scraps are not the highest or the glass the lowest: {pct}"
    return (f"across the same landfill the values run from {max(pct):.0f} percent down to "
            f"{min(pct):.0f} percent, so the material is what differs")


def q17(table, item):
    names = [n.strip().lower() for n in cg.labels(table)]
    counts = cg.col(table, ITEMS)
    ew = [c for n, c in zip(names, counts) if n in EWASTE_ROWS]
    other = [c for n, c in zip(names, counts) if n not in EWASTE_ROWS]
    assert len(ew) == 3, f"the three device rows STB-3.K.3 names are not all present: {names}"
    assert other, "there is no non-electronic row, so 'every item is e-waste' would be true"
    assert sum(ew) > sum(other), \
        f"the three device rows {sum(ew):.0f} do not outnumber the rest {sum(other):.0f}"
    phones = [c for n, c in zip(names, counts) if n == "cell phones"][0]
    assert phones < sum(counts) - phones, \
        "'the cell phones alone outnumber everything else' must be false"
    return (f"the televisions, cell phones and computers total {sum(ew):.0f} against "
            f"{sum(other):.0f} for the yard clippings and food scraps")


def q21(table, item):
    sites = cg.labels(table)
    tires = cg.col(table, TIRES)
    larvae = cg.col(table, LARVAE)
    order = [s for _, s in sorted(zip(tires, sites))]
    assert order == [s for _, s in sorted(zip(larvae, sites))], \
        f"the order by tires does not match the order by larvae: {tires} {larvae}"
    assert larvae[tires.index(min(tires))] == min(larvae), \
        "'the site with no tires had the most larvae' must be false"
    assert len(set(larvae)) == len(larvae), "'the same count at every site' must be false"
    return (f"ranking the sites by tires gives {order}, the same order as ranking them by "
            "the larvae counted")


CLAIMS = [
 ("Any discarded material that is not a liquid or a gas",
  "STB-3.K.1 verbatim: solid waste is any discarded material that is not a liquid or gas. The definition turns on the state of the material rather than on its destination or its recyclability."),
 ("Domestic, industrial, business and agricultural",
  "STB-3.K.1 states that solid waste is generated in domestic, industrial, business and agricultural sectors. Each rejected option drops at least two of the four."),
 ("industrial sector generates the largest amount in this region",
  "Recomputed in q3 above: the four row labels are exactly the four sectors STB-3.K.1 names, and the industrial row carries the largest figure. The framework does not rank the sectors, so the ranking comes from the table alone."),
 ("In landfills",
  "STB-3.K.2 states that solid waste is most often disposed of in landfills. Incineration is STB-3.L.2 and ocean dumping STB-3.L.4, described as other routes rather than the most common one."),
 ("contaminate groundwater and release harmful gases",
  "STB-3.K.2 verbatim: landfills can contaminate groundwater and release harmful gases. The rejected options belong to ocean warming, ocean acidification, biomagnification and ozone depletion."),
 ("far more contaminated than the well below the section that has a bottom liner",
  "Recomputed in q6 above: the well below the unlined section reads more than ten times the well below the lined section, which sits close to the upgradient value. STB-3.K.2 names groundwater contamination and STB-3.K.4 lists a bottom liner and leachate collection."),
 ("bottom liner, a storm water collection system, a leachate collection system, a cap and a methane collection system",
  "STB-3.K.4 lists exactly those five components for a sanitary municipal landfill. The rejected options describe an incinerator, a sewage plant and a materials recovery line."),
 ("Discarded electronic devices including televisions, cell phones and computers",
  "STB-3.K.3 verbatim: electronic waste, or e-waste, is composed of discarded electronic devices including televisions, cell phones and computers. Food and yard waste belong to STB-3.M.3 and tires to STB-3.L.3."),
 ("about a tenth of the volume before it in every batch",
  "Recomputed in q9 above: every batch's ash volume divided by its starting volume falls between five and fifteen percent, and every row carries a positive air pollutant figure. That is the trade STB-3.L.2 states."),
 ("significantly reduces the volume of solid waste but releases air pollutants",
  "STB-3.L.2 verbatim: incineration significantly reduces the volume of solid waste but releases air pollutants. Each rejected option denies one half of that trade."),
 ("composition of the trash and the conditions needed for microbial decomposition",
  "STB-3.L.1 verbatim: factors in landfill decomposition include the composition of the trash and conditions needed for microbial decomposition of the waste. Bag color, distance, truck counts and fencing appear nowhere in the framework."),
 ("Used rubber tires, which when left in piles can become breeding grounds for mosquitoes",
  "STB-3.L.3 names used rubber tires as its example of an item not accepted in sanitary landfills that may be disposed of illegally, and states that piles of them can become breeding grounds for mosquitoes that can spread disease."),
 ("depends strongly on what the material is",
  "Recomputed in q13 above: within one landfill the five materials span from above eighty percent decomposed to below five percent, and the food scraps exceed both the plastic and the glass. STB-3.L.1 names the composition of the trash as a factor."),
 ("Large floating islands of trash in the oceans",
  "STB-3.L.4 states that ocean dumping, along with other sources of plastic, has led to large floating islands of trash in the oceans and that wildlife can become entangled in the waste as well as ingest it."),
 ("bottom liner of plastic or clay",
  "STB-3.K.4 lists a bottom liner of plastic or clay among the components of a sanitary municipal landfill, and it is the component beneath the waste. STB-3.K.2 names groundwater contamination as the problem a base barrier addresses."),
 ("collection system captures gas that would otherwise escape",
  "STB-3.K.2 states that landfills can release harmful gases and STB-3.K.4 lists a methane collection system among the components, so the component matches the stated problem rather than the groundwater one."),
 ("televisions, cell phones and computers together outnumber the remaining items",
  "Recomputed in q17 above: the three device rows STB-3.K.3 names sum to more than the two rows of yard clippings and food scraps, and no single row outweighs the rest. The organic rows are the material of STB-3.M.3 rather than electronic devices."),
 ("Used oil drained from an engine",
  "STB-3.K.1 defines solid waste as any discarded material that is not a liquid or gas, and used oil is a liquid. The four rejected items are discarded materials in the solid state."),
 ("manage the rainfall that runs off the site",
  "STB-3.K.4 lists a storm water collection system among the components of a sanitary municipal landfill and lists methane collection separately, and STB-3.K.2 names groundwater contamination as the problem water management addresses."),
 ("waste is transformed rather than erased",
  "STB-3.L.2 states that incineration significantly reduces the volume of solid waste but releases air pollutants, so it changes the form and the location of the problem rather than removing it."),
 ("more tires left at a site, the more mosquito larvae were counted",
  "Recomputed in q21 above: ranking the sites by tires gives the same order as ranking them by larvae, and the site with none has the fewest. STB-3.L.3 states that tire piles can become breeding grounds for mosquitoes."),
 ("Groundwater sampled below the unlined part of the site is far more contaminated",
  "STB-3.K.2 names groundwater contamination as a landfill problem and STB-3.K.4 lists a bottom liner and a cap among the components of a sanitary municipal landfill, so a measured lined against unlined difference is the evidence that bears on the proposal."),
 ("Becoming entangled in the waste and ingesting it",
  "STB-3.L.4 states that wildlife can become entangled in the waste as well as ingest it. The framework names no salt, noise, shading or heating effect for ocean waste in that statement."),
 ("dumping it outside a regulated site is what leads to the problems",
  "STB-3.L.3 states that some items are not accepted in sanitary landfills and may be disposed of illegally, leading to environmental problems, and gives tire piles breeding mosquitoes as the example."),
 ("bottom liner together with the leachate collection system",
  "STB-3.K.4 lists a bottom liner and a leachate collection system as separate components and STB-3.K.2 names groundwater contamination as a landfill problem. Each rejected option attaches a listed component to the wrong function or denies the stated problem."),
 ("conditions needed for microbial decomposition of the waste",
  "STB-3.L.1 names both the composition of the trash and the conditions needed for microbial decomposition; with the material held constant the conditions are what remain. The rejected statements are definitions or other disposal routes."),
 ("Landfilling, paired with the possibility of contaminated groundwater",
  "STB-3.K.2 attaches groundwater contamination and harmful gas release to landfills, STB-3.L.2 attaches volume reduction and air pollutants to incineration, STB-3.L.4 attaches floating trash to ocean dumping and STB-3.L.3 attaches mosquitoes to tire piles. Each rejected pairing crosses two of those."),
 ("concentration of methane measured in the air",
  "STB-3.K.2 states that landfills can release harmful gases, so a gas measured in the air is the direct evidence. A well concentration bears on the groundwater half of that same statement instead."),
 ("volume of waste each route would leave behind and the air pollutants each would release",
  "STB-3.L.2 states the incineration trade as a large reduction in volume against the release of air pollutants, and STB-3.K.2 names groundwater and gas problems for landfills, so those two quantities are what the comparison turns on."),
 ("liners, collection systems and a cap because they can contaminate groundwater",
  "Each clause of the keyed summary is one of STB-3.K.1 through STB-3.L.4. Every rejected summary contradicts the definition, denies a stated landfill problem, recommends a practice the framework describes as harmful, or denies the role of trash composition."),
]

TABLE_CHECKS = {3: q3, 6: q6, 9: q9, 13: q13, 17: q17, 21: q21}

es.run(e8_9, CLAIMS, TABLE_CHECKS, sys.argv)
