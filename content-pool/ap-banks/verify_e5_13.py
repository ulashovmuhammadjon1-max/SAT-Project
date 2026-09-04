"""Key audit for AP ENVIRONMENTAL SCIENCE 5.13 Methods to Reduce Urban Runoff.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
STB-1.B.1 is the topic's only statement: METHODS TO INCREASE WATER INFILTRATION
INCLUDE replacing traditional pavement with permeable pavement, planting trees,
increased use of public transportation, and building up, not out.

  the list itself           -- items 1, 3, 4, 5, 22, 26, 28, 30
  the stated purpose        -- items 2, 17, 21, 24, 30
  data read against a method-- items 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
  which method is available -- items 19, 20
  the word INCLUDE          -- item 27
  research design (skill 4.B) -- items 16, 18, 25

ONE CHAIN, named in its claim and never keyed on its own:
  EIN-2.M.3  impervious surfaces are human-made structures that do not allow
             water to reach the soil, leading to flooding   -- items 12, 23, 29

WHAT IS DELIBERATELY NOT ASSERTED. The framework supplies no mechanism for any
of the four methods, no cost, and no ranking. No key here says one method
infiltrates more than another or explains WHY public transport or building
upward should help; item 26 keys the absence of a ranking directly, and item 27
keys that the list is introduced by INCLUDE and so is not offered as complete.

DATA ITEMS: 6, 7, 8, 9, 10, 11, 12, 13, 14 and 15, recomputed below from those
tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_13

THROUGH = "Rain soaking through in one hour (millimeters)"
OFF = "Rain running off in one hour (millimeters)"
ASPH = "Traditional asphalt"
CONC = "Traditional concrete"
BLOCKS = "Permeable paving blocks"
POROUS = "Permeable porous asphalt"

RAIN = "Rain falling on the car park in the storm (millimeters)"
RUNOFF = "Runoff leaving the car park in the storm (millimeters)"
PRE = "Before repaving, traditional surface"
POST = "After repaving with a permeable surface"

CANOPY = "Tree canopy cover (percent of the ground)"
DRAINS = "Rainfall reaching the drains as runoff (percent)"

TRIPS = "Trips made by public transport (percent)"
LAND = "City land given to roads and parking (percent)"
LOWPT = "City with little public transport"
HIGHPT = "City with heavy public transport"

STOREYS = "Storeys in each building"
COVERED = "Ground covered by buildings, roads and parking (hectares)"
UNPAVED = "Ground left unpaved (hectares)"
OUTWARD = "Plan that builds outward"
UPWARD = "Plan that builds upward"


def q6(table, item):
    trad = [cg.cell(table, ASPH, THROUGH), cg.cell(table, CONC, THROUGH)]
    perm = [cg.cell(table, BLOCKS, THROUGH), cg.cell(table, POROUS, THROUGH)]
    assert min(perm) > 5 * max(trad), \
        f"the permeable surfaces {perm} must take far more through than the traditional {trad}"
    assert cg.cell(table, POROUS, OFF) < cg.cell(table, ASPH, OFF), \
        "'the permeable surfaces shed more runoff' must be false"
    assert len(set(cg.col(table, THROUGH))) > 1, "'about the same depth' must be false"
    return (f"the traditional surfaces take {trad} millimeters through and the permeable ones "
            f"{perm}, with runoff of {cg.col(table, OFF)} running the other way")


def q7(table, item):
    t = cg.col(table, THROUGH)
    d = cg.cell(table, POROUS, THROUGH) - cg.cell(table, ASPH, THROUGH)
    assert d == 22, f"the difference recomputes to {d}, not 22"
    for wrong in (max(t), max(t) + min(t),
                  cg.cell(table, BLOCKS, THROUGH) - cg.cell(table, CONC, THROUGH),
                  cg.cell(table, CONC, THROUGH)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"24 minus 2 is {d:.0f} millimeters more soaking through in the hour"


def q8(table, item):
    assert cg.cell(table, PRE, RAIN) == cg.cell(table, POST, RAIN), \
        "the two storms must be the same size, or the surface is not isolated"
    assert cg.cell(table, POST, RUNOFF) < cg.cell(table, PRE, RUNOFF), \
        "runoff must fall after the repaving"
    assert cg.cell(table, PRE, RUNOFF) != cg.cell(table, PRE, RAIN), \
        "'the rain and the runoff were equal before repaving' must be false"
    return (f"rainfall reads {cg.cell(table, PRE, RAIN):.0f} millimeters in both storms while "
            f"runoff falls from {cg.cell(table, PRE, RUNOFF):.0f} to "
            f"{cg.cell(table, POST, RUNOFF):.0f}")


def q9(table, item):
    r = cg.col(table, RUNOFF)
    d = cg.cell(table, PRE, RUNOFF) - cg.cell(table, POST, RUNOFF)
    assert d == 23, f"the fall recomputes to {d}, not 23"
    for wrong in (max(r), max(r) + min(r),
                  cg.cell(table, PRE, RAIN) - cg.cell(table, POST, RUNOFF), min(r)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"34 minus 11 is {d:.0f} millimeters less runoff from a storm of the same size"


def q10(table, item):
    c, d = cg.col(table, CANOPY), cg.col(table, DRAINS)
    assert cg.cell(table, "Neighbourhood 1", CANOPY) == min(c), \
        "the first neighbourhood must carry the least canopy"
    assert all(c[i] < c[i + 1] for i in range(len(c) - 1)), f"canopy must rise; got {c}"
    assert all(d[i] > d[i + 1] for i in range(len(d) - 1)), f"runoff share must fall; got {d}"
    assert cg.cell(table, "Neighbourhood 1", DRAINS) == max(d), \
        "'the least wooded neighbourhood sent the smallest share' must be false"
    return (f"canopy runs {c} percent against runoff shares of {d} percent, the two moving in "
            "opposite directions throughout")


def q11(table, item):
    c, d = cg.col(table, CANOPY), cg.col(table, DRAINS)
    diff = cg.cell(table, "Neighbourhood 1", DRAINS) - cg.cell(table, "Neighbourhood 4", DRAINS)
    assert diff == 32, f"the difference recomputes to {diff}, not 32"
    for wrong in (max(d), max(d) + min(d), max(c) - min(c), min(d)):
        assert diff != wrong, f"the {wrong} distractor equals the key"
    return f"62 minus 30 is {diff:.0f} percentage points less of the rainfall reaching the drains"


def q12(table, item):
    assert cg.cell(table, HIGHPT, TRIPS) > cg.cell(table, LOWPT, TRIPS), \
        "the second city must carry more trips by public transport"
    assert cg.cell(table, HIGHPT, LAND) < cg.cell(table, LOWPT, LAND), \
        "the second city must give less land to roads and parking"
    assert cg.cell(table, HIGHPT, LAND) != cg.cell(table, LOWPT, LAND), \
        "'the same share of their land' must be false"
    return (f"public transport carries {cg.cell(table, LOWPT, TRIPS):.0f} and "
            f"{cg.cell(table, HIGHPT, TRIPS):.0f} percent of trips against "
            f"{cg.cell(table, LOWPT, LAND):.0f} and {cg.cell(table, HIGHPT, LAND):.0f} percent "
            "of the land given to roads and parking")


def q13(table, item):
    d = cg.cell(table, LOWPT, LAND) - cg.cell(table, HIGHPT, LAND)
    assert d == 19, f"the difference recomputes to {d}, not 19"
    for wrong in (cg.cell(table, LOWPT, LAND),
                  cg.cell(table, LOWPT, LAND) + cg.cell(table, HIGHPT, LAND),
                  cg.cell(table, HIGHPT, TRIPS),
                  cg.cell(table, HIGHPT, TRIPS) - cg.cell(table, HIGHPT, LAND)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"38 minus 19 is {d:.0f} percentage points less of the city given to roads and parking"


def q14(table, item):
    assert cg.cell(table, UPWARD, STOREYS) > cg.cell(table, OUTWARD, STOREYS), \
        "the upward plan must be the taller of the two"
    cov_ratio = cg.cell(table, OUTWARD, COVERED) / cg.cell(table, UPWARD, COVERED)
    unp_ratio = cg.cell(table, UPWARD, UNPAVED) / cg.cell(table, OUTWARD, UNPAVED)
    assert cov_ratio == 3, f"the covered-ground ratio recomputes to {cov_ratio}, not 3"
    assert unp_ratio == 7, f"the unpaved ratio recomputes to {unp_ratio}, not 7"
    assert cg.cell(table, UPWARD, UNPAVED) > cg.cell(table, OUTWARD, UNPAVED), \
        "'the outward plan leaves more unpaved' must be false"
    return (f"the outward plan covers {cg.cell(table, OUTWARD, COVERED):.0f} hectares against "
            f"{cg.cell(table, UPWARD, COVERED):.0f}, a factor of {cov_ratio:.0f}, and leaves "
            f"{cg.cell(table, OUTWARD, UNPAVED):.0f} unpaved against "
            f"{cg.cell(table, UPWARD, UNPAVED):.0f}, a factor of {unp_ratio:.0f}")


def q15(table, item):
    d = cg.cell(table, UPWARD, UNPAVED) - cg.cell(table, OUTWARD, UNPAVED)
    assert d == 24, f"the difference recomputes to {d}, not 24"
    for wrong in (cg.cell(table, UPWARD, UNPAVED),
                  cg.cell(table, UPWARD, UNPAVED) + cg.cell(table, OUTWARD, UNPAVED),
                  cg.cell(table, UPWARD, COVERED), cg.cell(table, OUTWARD, COVERED)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"28 minus 4 is {d:.0f} hectares more of the site left unpaved by the taller plan"


CLAIMS = [
 ("Replacing traditional pavement with permeable pavement, planting trees, increased use of public transportation",
  "STB-1.B.1, near verbatim: methods to increase water infiltration include replacing traditional pavement with permeable pavement, planting trees, increased use of public transportation, and building up, not out. One distractor is that list with every item reversed, so the anchor spans several of them rather than any single phrase."),
 ("Increasing water infiltration",
  "STB-1.B.1 introduces its four methods as METHODS TO INCREASE WATER INFILTRATION, so the aim concerns where rain goes once it has fallen. The rejected aims -- faster drainage, less rainfall, saltier groundwater, more carbon dioxide -- belong to other statements or to none."),
 ("Channelling runoff into concrete storm drains",
  "STB-1.B.1 names permeable pavement, planting trees, public transportation and building up rather than out, and nothing else. Storm drains move water away from a surface rather than into the soil and appear nowhere in the statement, while every rejected option is quoted from it."),
 ("Traditional pavement",
  "STB-1.B.1 names REPLACING TRADITIONAL PAVEMENT WITH PERMEABLE PAVEMENT, so the thing replaced is the older paved surface. The method calls for removing no tree, no transport route, no building and no soil."),
 ("smaller area of ground by building upward rather than spreading outward",
  "STB-1.B.1's phrase is BUILDING UP, NOT OUT, whose plain reading is upward on less ground rather than outward across more. The framework offers no further gloss, so stilts, storey limits and elevated ground may not be read in. One distractor is the exact reversal, so the anchor carries both halves."),
 ("permeable surfaces let far more rain through",
  "Recomputed in q6 above: 2 and 3 millimeters through the traditional surfaces against 21 and 24 through the permeable ones, with runoff running the other way. STB-1.B.1 offers replacing traditional pavement with permeable pavement as a method to increase water infiltration. One distractor swaps which pair is which, so the anchor names the pair."),
 ("22 millimeters more",
  "Recomputed in q7 above: 24 minus 2 millimeters in the hour. The rejected values quote the permeable surface alone, add the two, compare the wrong pair of surfaces, or quote a traditional surface's own infiltration."),
 ("same rain fell in both storms, so the fall in runoff is attributable to the new surface",
  "Recomputed in q8 above: 40 millimeters of rain in both storms against runoff of 34 and 11. The one variable that changed is the surface, which is what STB-1.B.1's method alters. One distractor blames the weather instead, so the anchor carries the attribution."),
 ("By 23 millimeters",
  "Recomputed in q9 above: 34 minus 11 millimeters of runoff. The rejected values quote the earlier storm alone, add the two, use the rainfall in place of one runoff figure, or quote the later storm alone."),
 ("more tree canopy sent a smaller share of the rainfall to the drains",
  "Recomputed in q10 above: canopy 6, 15, 28 and 44 percent against runoff shares of 62, 54, 41 and 30 percent. STB-1.B.1 lists planting trees among its methods to increase water infiltration. One distractor reverses only the direction, so the anchor carries it."),
 ("32 percentage points smaller",
  "Recomputed in q11 above: 62 minus 30 percent of the rainfall. The rejected values quote the least wooded neighbourhood alone, add the two, take the difference in canopy cover, or quote the most wooded alone."),
 ("more trips are made by public transport gives a smaller share of its land",
  "Recomputed in q12 above: 8 and 46 percent of trips against 38 and 19 percent of land given to roads and parking. STB-1.B.1 lists increased use of public transportation, and EIN-2.M.3 makes roads and parking lots impervious surfaces. One distractor reverses the direction, so the anchor carries it."),
 ("19 percentage points smaller",
  "Recomputed in q13 above: 38 minus 19 percent of the city's land. The rejected values quote the first city alone, add the two, take a reading from the transport column, or difference the second city's two entries across the columns."),
 ("covers a third of the ground the outward plan covers and leaves seven times as much",
  "Recomputed in q14 above: 36 hectares covered against 12, and 4 hectares unpaved against 28, for the same 900 dwellings. STB-1.B.1's phrase is building up, not out. One distractor inverts both ratios, so the anchor carries both."),
 ("24 hectares more",
  "Recomputed in q15 above: 28 minus 4 hectares left unpaved. The rejected values quote the taller plan alone, add the two, or take one of the two figures for ground covered instead."),
 ("adjacent plots of the same soil and slope, apply the same rainfall",
  "A comparison isolates the surface only when everything else is matched, so the plots must share soil, slope and rainfall. Each rejected design supplies no comparison plot, lets the weather or the soil vary alongside the surface, or collects opinion in place of measurement."),
 ("depth of water that passes through the surface into the soil",
  "STB-1.B.1's stated aim is to INCREASE WATER INFILTRATION, and water passing through the surface into the soil is that quantity itself. Standing water, traffic counts, building height and street area are at best indirect."),
 ("rainfall applied to each plot and the soil lying beneath each plot",
  "A difference can be assigned to the surface only when the surface is the one thing that differs, so the water applied and the ground receiving it must match. Holding the pavement type the same would remove the comparison being made."),
 ("Replacing the traditional pavement with permeable pavement",
  "STB-1.B.1 lists four methods, and the only one that consists of changing a paved surface is replacing traditional pavement with permeable pavement. The others require changes to travel or to buildings, which this council may not make."),
 ("Planting trees",
  "STB-1.B.1 lists planting trees as a method in its own right, requiring neither repaving nor new building. Widening storm drains is not on the framework's list at all, and the other named methods are closed to this council."),
 ("given as ways to increase infiltration, not as ways to change how much rain falls",
  "STB-1.B.1 introduces the four as METHODS TO INCREASE WATER INFILTRATION, which concerns where rain goes after it falls. One distractor asserts the student's own claim, so the anchor carries both halves of the correction."),
 ("substitutes one paved surface for another rather than removing paving",
  "STB-1.B.1 names REPLACING traditional pavement WITH permeable pavement, so a surface remains after the change. The statement says nothing about stripping paving away or about paving ground that is currently bare."),
 ("keep rainfall from soaking into the ground cause water to collect and flood",
  "EIN-2.M.3 states that impervious surfaces are human-made structures that do not allow water to reach the soil, leading to flooding, and every method in STB-1.B.1 works on infiltration. One distractor reverses the mechanism, so the anchor carries the direction."),
 ("larger share of the rain falling on the treated area soaked into the ground",
  "STB-1.B.1's stated purpose is to increase water infiltration, so the outcome to look for is more of the rain entering the ground. Rainfall totals, traffic, surface colour and building height are not the quantity the statement is about."),
 ("may differ in soil, slope, paving or rainfall, so the comparison does not isolate",
  "A before-and-after comparison taken across two different sites confounds the treatment with every other difference between them. The remedy is the same street before and after, or two matched streets at the same time."),
 ("ranking of the four methods",
  "STB-1.B.1 gives its four methods in an unordered list and attaches no quantity to any of them, so a ranking would be added rather than read. Each rejected option quotes something the statement does supply."),
 ("introduced by the word include, so it is not offered as complete",
  "STB-1.B.1 says methods to increase water infiltration INCLUDE the four it names, and a list introduced that way is not presented as exhaustive. Reading it as complete, or as a blanket endorsement of any proposal, both go past the wording."),
 ("Increased use of public transportation, and building up, not out",
  "STB-1.B.1's four methods divide into two that change a surface, permeable pavement and tree planting, and two that change travel and building form. Each rejected pair takes one from each group, so the anchor names both members of the right one."),
 ("other statement names the problem, surfaces that keep water from the soil; this one names methods",
  "EIN-2.M.3 defines impervious surfaces and attaches flooding to them, while STB-1.B.1 lists methods to increase water infiltration. One is the impact and the other the mitigation, and one distractor is the exact swap, so the anchor carries both halves."),
 ("include replacing traditional pavement with permeable pavement, planting trees, increasing the use of public transportation",
  "The keyed summary is STB-1.B.1's purpose together with all four of its methods and nothing else. Each rejected summary shortens the list and adds a ranking, changes the purpose to drainage or to rainfall, or denies that a purpose is stated."),
]

TABLE_CHECKS = {6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13,
                14: q14, 15: q15}

e_check.run(e5_13, CLAIMS, TABLE_CHECKS)
