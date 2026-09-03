"""Key audit for AP ENVIRONMENTAL SCIENCE 8.4 Human Impacts on Wetlands and Mangroves.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-3.E.1  wetlands are areas where water covers the soil, either part or all
             of the time  -- items 1, 14, 20, 27;
  STB-3.E.2  wetlands provide a variety of ecological services, including water
             purification, flood protection, water filtration, and habitat --
             items 2, 4, 5, 7, 8, 11, 12, 16, 17, 22, 24, 25, 26, 29;
  STB-3.E.3  threats to wetlands and mangroves include commercial development,
             dam construction, overfishing, and pollutants from agriculture and
             industrial waste -- items 3, 6, 9, 10, 13, 15, 18, 19, 21, 23, 28.
Item 30 joins all three.

MANGROVES. The framework mentions mangroves only in STB-3.E.3, and only as
sharing the list of threats. It states no service, definition or distinctive
property for them, so no key here attributes a service to mangroves -- not
storm buffering, not nursery habitat, not carbon storage. Items 13 and 21 are
the two mangrove items and both key a threat.

PURIFICATION AND FILTRATION are printed as separate entries in STB-3.E.2 with
no distinction drawn between them, so no item asks a student to tell them
apart; items 4, 12 and 22 name both together.

NOT KEYED: no statute, permit, mitigation ratio, named wetland or area figure.
Every number belongs to the study in its own table.

DATA ITEMS: 4, 5, 6, 8, 12 and 13 carry tables and every keyed reading is
recomputed below from the table alone.

NEGATIVE CONTROL: `python3 verify_e8_4.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e8_4

NITRATE = "Nitrate in the water (milligrams per liter)"
SED = "Suspended sediment (milligrams per liter)"
WET = "Wetland remaining in the catchment (percent of original)"
PEAK = "Peak river height after a comparable storm (meters)"
LOST = "Area lost over 30 years (square kilometers)"
AREA = "Wetland area remaining (square kilometers)"
BIRDS = "Waterbird species recorded"
FISH = "Fish species recorded"
R_AREA = "Wetland area (square kilometers)"
R_NIT = "Nitrate leaving the site (milligrams per liter)"
CLEARED = "Mangrove cleared for development (percent)"
REMAIN = "Mangrove area remaining (hectares)"


def q4(table, item):
    points = cg.labels(table)
    nit = cg.col(table, NITRATE)
    sed = cg.col(table, SED)
    assert points[0].startswith("Entering") and points[-1].startswith("Leaving"), \
        f"the rows must run from inflow to outflow, got {points}"
    for series, name in ((nit, "nitrate"), (sed, "sediment")):
        assert all(series[i] > series[i + 1] for i in range(len(series) - 1)), \
            f"{name} does not fall along the flow path: {series}"
    assert nit[-1] < nit[0] and sed[-1] < sed[0], "the outflow must be lower in both"
    return (f"nitrate runs {nit} and sediment runs {sed} from inflow to outflow, both falling "
            "at every step")


def q5(table, item):
    wet = cg.col(table, WET)
    peak = cg.col(table, PEAK)
    pairs = sorted(zip(wet, peak))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the peak does not fall as wetland rises: {pairs}"
    assert peak[wet.index(min(wet))] == max(peak), \
        "'the least wetland recorded the lowest peak' must be false"
    assert len(set(peak)) == len(peak), "'the same in all four' must be false"
    return (f"sorted by remaining wetland the peaks run {[p for _, p in pairs]} meters, falling "
            "as the wetland share rises")


def q6(table, item):
    vals = dict(zip(cg.labels(table), cg.col(table, LOST)))
    top = max(vals, key=vals.get)
    assert top == "Commercial development", f"the largest recorded loss is {top}"
    named = {k: v for k, v in vals.items() if not k.startswith("Other")}
    assert vals["Pollutants from agriculture and industrial waste"] < vals[top], \
        "'pollutants account for more than any other cause' must be false"
    assert min(named, key=named.get) != "Dam construction and altered river flow", \
        "'dam construction is the smallest named cause' must be false"
    assert len(set(vals.values())) == len(vals), "'equal areas' must be false"
    return (f"commercial development accounts for {vals[top]:.0f} square kilometers, the largest "
            f"of {sorted(vals.values())}")


def q8(table, item):
    area = cg.col(table, AREA)
    birds = cg.col(table, BIRDS)
    fish = cg.col(table, FISH)
    for series, name in ((birds, "waterbird"), (fish, "fish")):
        pairs = sorted(zip(area, series))
        assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
            f"the {name} count does not fall with area: {pairs}"
    assert birds[area.index(min(area))] == min(birds) and fish[area.index(min(area))] == min(fish), \
        "'the smallest site records the most species' must be false"
    return (f"sorted by area the waterbird counts run {sorted(birds)} and the fish counts "
            f"{sorted(fish)}, both falling as the remaining area falls")


def q12(table, item):
    stages = cg.labels(table)
    area = dict(zip(stages, cg.col(table, R_AREA)))
    nit = dict(zip(stages, cg.col(table, R_NIT)))
    seq = list(stages)
    assert all(area[seq[i]] < area[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"the restored area does not grow: {area}"
    assert all(nit[seq[i]] > nit[seq[i + 1]] for i in range(len(seq) - 1)), \
        f"the nitrate leaving does not fall: {nit}"
    assert nit[seq[-1]] == min(nit.values()), "'the largest nitrate at the end' must be false"
    return (f"the area runs {[area[s] for s in seq]} square kilometers while the nitrate leaving "
            f"runs {[nit[s] for s in seq]} milligrams per liter")


def q13(table, item):
    cleared = cg.col(table, CLEARED)
    remain = cg.col(table, REMAIN)
    pairs = sorted(zip(cleared, remain))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the remaining area does not fall as clearing rises: {pairs}"
    assert remain[cleared.index(max(cleared))] == min(remain), \
        "'the most cleared section retains the largest area' must be false"
    assert len(set(remain)) == len(remain), "'the same area in all four' must be false"
    return (f"sorted by the share cleared the remaining areas run {[r for _, r in pairs]} hectares, "
            "falling as clearing rises")


CLAIMS = [
 ("water covers the soil, either part or all of the time",
  "STB-3.E.1 verbatim. Permanent inundation is only one of the two cases the definition allows, and open ocean, dry land and deep groundwater are none of them."),
 ("Water purification, flood protection, water filtration, and habitat",
  "STB-3.E.2 verbatim: wetlands provide a variety of ecological services, including water purification, flood protection, water filtration, and habitat. The rejected options are economic uses or effects from other topics rather than services the framework attributes to wetlands."),
 ("Commercial development, dam construction, overfishing, and pollutants",
  "STB-3.E.3 verbatim: threats to wetlands and mangroves include commercial development, dam construction, overfishing, and pollutants from agriculture and industrial waste. Ozone depletion, thermal inversion, noise and succession belong to other topics."),
 ("lower where the water leaves the wetland than where it enters",
  "Recomputed in q4 above: nitrate and suspended sediment both fall at every step from inflow to outflow. Water purification and water filtration are two of the services listed in STB-3.E.2."),
 ("retaining more wetland recorded lower peak river heights",
  "Recomputed in q5 above: ordering the catchments by remaining wetland puts the storm peaks in the opposite order. Flood protection is one of the services in STB-3.E.2."),
 ("Commercial development accounts for more of the recorded loss",
  "Recomputed in q6 above: commercial development holds the largest area in the table and the other named causes are smaller. Three of the four rows are threats named in STB-3.E.3."),
 ("populations of birds, fish and other animals that live and breed there",
  "Habitat is one of the four services in STB-3.E.2, and habitat is the place organisms live. Irrigation supply, navigation, fuel extraction and reflection are not services the framework attributes to wetlands."),
 ("number of waterbird species and the number of fish species fall",
  "Recomputed in q8 above: both species counts fall at every step as the remaining area falls. Habitat is one of the services in STB-3.E.2, so area loss bears on the species a wetland supports."),
 ("Commercial development",
  "STB-3.E.3 lists commercial development first among the threats to wetlands and mangroves, and draining a wetland to build on it is exactly that. The rejected options are the other threats in the same list and describe different activities."),
 ("Dam construction",
  "STB-3.E.3 names dam construction among the threats to wetlands and mangroves. Building on the wetland and removing too many fish are separate items in the same list, and noise and thermal pollution belong to STB-2.J and STB-3.G."),
 ("Restoring drained areas so that water again covers the soil",
  "Suggested skill 7.B. STB-3.E.2's services belong to wetlands, which STB-3.E.1 defines by water covering the soil, so restoring that condition is what could restore the services. Paving, deepening, filling and excluding water all remove it."),
 ("As the restored area grew, the nitrate leaving the site fell",
  "Recomputed in q12 above: the area grows at every stage while the nitrate leaving falls at every stage, ending at its smallest value. Water purification and filtration are services listed in STB-3.E.2."),
 ("more mangrove was cleared for development retain less mangrove area",
  "Recomputed in q13 above: ordering the sections by the share cleared puts the remaining area in the opposite order. Commercial development is one of the threats STB-3.E.3 names for wetlands and mangroves alike; no service is attributed to mangroves here."),
 ("either part or all of the time",
  "STB-3.E.1's own wording allows both cases, so an area flooded seasonally falls inside the definition. Depth, tree cover and coastal position form no part of it."),
 ("Reducing the fertilizer and pesticide carried in runoff",
  "Suggested skill 7.B against STB-3.E.3's threat of pollutants from agriculture: the response that addresses it is a reduction in what the runoff carries. The rejected options increase traffic, speed the delivery of runoff, or add a second threat from the same list."),
 ("Flood protection",
  "STB-3.E.2 lists flood protection among the ecological services wetlands provide, and slowing and storing storm water is that service. Purification, filtration and habitat are the other three, and timber production is not in the list."),
 ("holding water that now moves downstream instead",
  "STB-3.E.2 attributes flood protection to wetlands, so removing the wetland removes that service. The framework does not have wetlands generate rainfall, pump water underground, warm water or supply sediment."),
 ("limiting the catch taken from the wetland",
  "Suggested skill 7.B. Overfishing is one of STB-3.E.3's four threats and limiting the catch addresses it directly; every rejected pairing answers a threat with another item from the same list of threats."),
 ("a wetland can be lost or altered without being contaminated",
  "STB-3.E.3 lists commercial development, dam construction and overfishing alongside pollutants, so physical loss and alteration are threats in their own right. The framework does not restrict the list to contamination or to mangroves."),
 ("since water covers the soil for part of the time",
  "STB-3.E.1 covers areas where water covers the soil either part or all of the time, so seasonal flooding qualifies. The definition sets no minimum duration and mentions no depth."),
 ("Threats to wetlands and mangroves include commercial development",
  "STB-3.E.3 is the framework's only mention of mangroves, and converting mangrove shoreline to ponds and buildings is commercial development. The definition and service statements are written about wetlands, and the rejected options belong to STB-3.B.5 and STB-3.B.7."),
 ("entering the wetland and in the water leaving it",
  "STB-3.E.2's purification and filtration are changes to the water as it passes through, so paired inflow and outflow measurements are what demonstrate them. Visitor counts, area, bird counts and depth measure something else."),
 ("many more fish removed each year than in the past",
  "Overfishing in STB-3.E.3 is the removal of too many fish, so evidence for it concerns the catch and the fish population with the habitat unchanged. Each rejected option is evidence for one of the other three threats in the same list."),
 ("provide purification, flood protection, filtration and habitat",
  "Suggested skill 7.B. Reconnecting the site restores the condition in STB-3.E.1, and STB-3.E.2 attributes the services to wetlands so defined. The framework does not limit the threats to pollutants or make the services unrecoverable."),
 ("provide ecological services including water purification",
  "The argument is about value and STB-3.E.2 is the framework's statement of what wetlands provide. The definition and the threat list describe what a wetland is and what endangers it rather than what it does."),
 ("alongside the wetland area remaining in each",
  "Testing the effect requires the outcome and the wetland area measured together in both catchments over the same period, since STB-3.E.2 attributes the water quality service to the wetland. Population, building height, road counts and temperature measure neither."),
 ("losing that condition puts the services at risk",
  "STB-3.E.1 defines wetlands by water covering the soil part or all of the time and STB-3.E.2 attributes the services to wetlands so defined, which ties the services to that condition. It does not require year-round water."),
 ("review of dam projects, limits on fishing, and controls on agricultural and industrial pollutants",
  "Suggested skill 7.B. STB-3.E.3's threats are commercial development, dam construction, overfishing, and pollutants from agriculture and industrial waste, and only the keyed set addresses all four; the rejected options address one, none, or something outside the list."),
 ("depends on the wetland condition itself",
  "STB-3.E.2 attributes habitat, with the other services, to wetlands, and STB-3.E.1 defines a wetland by water covering the soil. Filling the area removes that condition, and the framework offers no substitute that supplies the service without it."),
 ("threatened by development, dams, overfishing and pollutants",
  "Each clause of the summary is one of STB-3.E.1, STB-3.E.2 and STB-3.E.3. Every rejected summary denies the definition, the list of services, or the list of threats."),
]

TABLE_CHECKS = {4: q4, 5: q5, 6: q6, 8: q8, 12: q12, 13: q13}

es.run(e8_4, CLAIMS, TABLE_CHECKS, sys.argv)
