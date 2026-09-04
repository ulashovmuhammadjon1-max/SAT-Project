"""Key audit for AP ENVIRONMENTAL SCIENCE 5.16 Aquaculture.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  STB-1.F.1  Aquaculture has expanded because it is highly efficient, requires
             only small areas of water, and requires little fuel.
                                        -- items 1, 2, 8, 9, 10, 11, 26, 28
  STB-1.F.2  Aquaculture can contaminate wastewater, and fish that escape may
             compete or breed with wild fish. The density of fish in aquaculture
             can lead to increases in disease incidences, which can be
             transmitted to wild fish.
             -- items 3, 4, 5, 6, 7, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 27
Items 20, 29 and 30 read the two statements against each other.

THREE THINGS THIS FILE GATES DELIBERATELY.
 1. THE HEDGES. STB-1.F.2 says CAN contaminate, MAY compete or breed, CAN lead
    to increases. No key anywhere says aquaculture always does any of the three,
    and item 27 keys the hedging directly.
 2. THE TWO-VERB CLAUSE. Escapees may COMPETE OR BREED -- an ecological
    consequence and a genetic one. Items 4 and 21 anchor on both verbs, because
    a distractor keeps one and denies the other.
 3. THE CAUSE OF DISEASE. The framework attributes it to THE DENSITY OF FISH,
    not to water quality, temperature, species or fuel. Items 5 and 22 key that,
    and each distractor puts the cause somewhere else.

BOUNDARY WITH 5.8: overfishing and the extreme scarcity of some fish species are
EIN-2.J.1 and are never keyed here; they appear only as rejected options, in
items 28 and 30.

DATA ITEMS: 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 and 19, recomputed below
from those tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_16

AREA = "Water area used per tonne of fish produced (hectares)"
FUEL = "Fuel used per tonne of fish produced (litres)"
AQUA = "Aquaculture in ponds and cages"
COASTAL = "Coastal fishing fleet"
DISTANT = "Distant-water fishing fleet"

FEED = "Feed eaten per kilogram of body mass gained (kilograms)"
CONVERTED = "Share of the feed converted to edible flesh (percent)"
FISH = "Farmed fish"
POULTRY = "Farmed poultry"
CATTLE = "Farmed cattle"

NITROGEN = "Nitrogen (milligrams per litre)"
SOLIDS = "Suspended solids (milligrams per litre)"
IN = "Water entering the ponds"
OUT = "Water leaving the ponds"

ESCAPED = "Farmed fish that escaped that year (thousands)"
FARMED_SHARE = "Share of the river's spawning fish of farmed origin (percent)"

DENSITY = "Stocking density (fish per cubic meter)"
DISEASED = "Fish showing the disease at harvest (percent)"

DIST = "Distance from the fish cages (kilometers)"
PARASITE = "Wild fish carrying the parasite (percent)"


def q8(table, item):
    assert cg.cell(table, AQUA, AREA) == min(cg.col(table, AREA)), \
        "aquaculture must use the least water area per tonne"
    assert cg.cell(table, AQUA, FUEL) == min(cg.col(table, FUEL)), \
        "aquaculture must use the least fuel per tonne"
    assert cg.cell(table, COASTAL, AREA) > 10 * cg.cell(table, AQUA, AREA), \
        "the water-area difference must be large, not marginal"
    assert cg.cell(table, DISTANT, FUEL) > cg.cell(table, COASTAL, FUEL), \
        "'the distant-water fleet uses the least fuel' must be false"
    assert len(set(cg.col(table, AREA))) > 1, "'the same water area' must be false"
    return (f"aquaculture uses {cg.cell(table, AQUA, AREA)} hectares and "
            f"{cg.cell(table, AQUA, FUEL):.0f} litres per tonne against "
            f"{cg.cell(table, COASTAL, AREA):.0f} and {cg.cell(table, COASTAL, FUEL):.0f} for the "
            f"coastal fleet and {cg.cell(table, DISTANT, AREA):.0f} and "
            f"{cg.cell(table, DISTANT, FUEL):.0f} for the distant-water fleet")


def q9(table, item):
    base = cg.cell(table, AQUA, FUEL)
    assert base > 0, "the aquaculture figure must be non-zero for a ratio to exist"
    ratio = cg.cell(table, DISTANT, FUEL) / base
    assert ratio == 10, f"the ratio recomputes to {ratio}, not 10"
    for wrong in (cg.cell(table, COASTAL, FUEL) / base,
                  cg.cell(table, DISTANT, FUEL) / cg.cell(table, COASTAL, FUEL), 13, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"950 divided by 95 is {ratio:.0f} times as much fuel per tonne of fish"


def q10(table, item):
    f, c = cg.col(table, FEED), cg.col(table, CONVERTED)
    assert cg.cell(table, FISH, FEED) == min(f), "farmed fish must need the least feed"
    assert cg.cell(table, FISH, CONVERTED) == max(c), "farmed fish must convert the largest share"
    assert cg.cell(table, CATTLE, CONVERTED) == min(c), \
        "'cattle turn the largest share into edible flesh' must be false"
    assert all(f[i] < f[i + 1] for i in range(len(f) - 1)), f"feed needed must rise; got {f}"
    assert all(c[i] > c[i + 1] for i in range(len(c) - 1)), f"the share converted must fall; got {c}"
    return (f"feed needed runs {f} kilograms per kilogram gained against shares converted of {c} "
            "percent, the fish leading on both")


def q11(table, item):
    base = cg.cell(table, FISH, FEED)
    assert base > 0, "the fish figure must be non-zero for a ratio to exist"
    ratio = cg.cell(table, CATTLE, FEED) / base
    assert abs(ratio - 5) < 1e-9, f"the ratio recomputes to {ratio}, not 5"
    for wrong in (cg.cell(table, POULTRY, FEED) / base, 3, cg.cell(table, CATTLE, FEED), 1):
        assert abs(ratio - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"6.0 divided by 1.2 is {ratio:.0f} times as much feed per kilogram gained"


def q12(table, item):
    assert cg.cell(table, OUT, NITROGEN) > cg.cell(table, IN, NITROGEN), \
        "the water leaving must carry more nitrogen"
    assert cg.cell(table, OUT, SOLIDS) > cg.cell(table, IN, SOLIDS), \
        "the water leaving must carry more suspended solids"
    assert cg.cell(table, OUT, NITROGEN) > 3 * cg.cell(table, IN, NITROGEN), \
        "the nitrogen difference must be large, not marginal"
    return (f"nitrogen rises from {cg.cell(table, IN, NITROGEN)} to "
            f"{cg.cell(table, OUT, NITROGEN)} milligrams per litre and suspended solids from "
            f"{cg.cell(table, IN, SOLIDS):.0f} to {cg.cell(table, OUT, SOLIDS):.0f}")


def q13(table, item):
    base = cg.cell(table, IN, NITROGEN)
    assert base > 0, "the entering concentration must be non-zero for a ratio to exist"
    ratio = cg.cell(table, OUT, NITROGEN) / base
    solids = cg.cell(table, OUT, SOLIDS) / cg.cell(table, IN, SOLIDS)
    assert abs(ratio - 8) < 1e-9, f"the ratio recomputes to {ratio}, not 8"
    assert abs(solids - 9) < 1e-9, f"the solids ratio recomputes to {solids}, not 9"
    for wrong in (solids, 6, 2, 1):
        assert abs(ratio - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"7.2 divided by 0.9 is {ratio:.0f} times as much nitrogen, against a solids ratio "
            f"of {solids:.0f}")


def q14(table, item):
    e, s = cg.col(table, ESCAPED), cg.col(table, FARMED_SHARE)
    assert cg.cell(table, "Year 1", ESCAPED) == min(e), "the first year must carry the fewest escapes"
    assert all(e[i] < e[i + 1] for i in range(len(e) - 1)), f"escapes must rise; got {e}"
    assert all(s[i] < s[i + 1] for i in range(len(s) - 1)), f"the farmed share must rise; got {s}"
    assert len(set(s)) > 1, "'the share stayed level' must be false"
    return (f"escapes run {e} thousand against a farmed share of spawners of {s} percent, the "
            "two rising together")


def q15(table, item):
    e, s = cg.col(table, ESCAPED), cg.col(table, FARMED_SHARE)
    d = cg.cell(table, "Year 10", FARMED_SHARE) - cg.cell(table, "Year 1", FARMED_SHARE)
    assert d == 26, f"the rise recomputes to {d}, not 26"
    for wrong in (max(s), max(s) + min(s), max(e) - min(e), cg.cell(table, "Year 5", FARMED_SHARE)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"28 minus 2 is {d:.0f} percentage points more of the spawners of farmed origin"


def q16(table, item):
    dn, ds = cg.col(table, DENSITY), cg.col(table, DISEASED)
    assert cg.cell(table, "Cage 1", DENSITY) == min(dn), "Cage 1 must be the most thinly stocked"
    assert cg.cell(table, "Cage 1", DISEASED) == min(ds), \
        "'the most thinly stocked cage held the largest diseased share' must be false"
    assert all(dn[i] < dn[i + 1] for i in range(len(dn) - 1)), f"density must rise; got {dn}"
    assert all(ds[i] < ds[i + 1] for i in range(len(ds) - 1)), f"disease must rise with it; got {ds}"
    return (f"density runs {dn} fish per cubic meter against diseased shares of {ds} percent, "
            "rising together without exception")


def q17(table, item):
    ds = cg.col(table, DISEASED)
    d = max(ds) - min(ds)
    assert d == 49, f"the difference recomputes to {d}, not 49"
    for wrong in (max(ds), max(ds) + min(ds), cg.cell(table, "Cage 3", DISEASED), min(ds)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"52 minus 3 is {d:.0f} percentage points more of the fish diseased at the top density"


def q18(table, item):
    dist, p = cg.col(table, DIST), cg.col(table, PARASITE)
    assert cg.cell(table, "Site 1", DIST) == min(dist), "Site 1 must be nearest the cages"
    assert cg.cell(table, "Site 1", PARASITE) == max(p), \
        "the nearest site must carry the commonest parasite"
    assert all(dist[i] < dist[i + 1] for i in range(len(dist) - 1)), f"distance must rise; got {dist}"
    assert all(p[i] > p[i + 1] for i in range(len(p) - 1)), f"the parasite must fall; got {p}"
    assert min(p) > 0, "'found only more than forty kilometers away' must be false"
    return (f"distances run {dist} kilometers against parasite shares of {p} percent, falling "
            "steadily away from the cages")


def q19(table, item):
    p = cg.col(table, PARASITE)
    d = cg.cell(table, "Site 1", PARASITE) - cg.cell(table, "Site 4", PARASITE)
    assert d == 35, f"the difference recomputes to {d}, not 35"
    for wrong in (max(p), max(p) + min(p),
                  cg.cell(table, "Site 1", PARASITE) - cg.cell(table, "Site 3", PARASITE),
                  cg.cell(table, "Site 3", PARASITE)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"38 minus 3 is {d:.0f} percentage points commoner in the wild fish nearest the cages"


CLAIMS = [
 ("highly efficient, requires only small areas of water, and requires little fuel",
  "STB-1.F.1, near verbatim: aquaculture has expanded BECAUSE IT IS HIGHLY EFFICIENT, REQUIRES ONLY SMALL AREAS OF WATER, AND REQUIRES LITTLE FUEL. Each rejected option reverses one of the three or replaces them with claims the framework never makes, so the anchor carries all three."),
 ("eliminates disease among the fish being raised",
  "STB-1.F.1 gives efficiency, small areas of water and little fuel. Far from claiming that disease is eliminated, STB-1.F.2 states that the density of fish in aquaculture can lead to INCREASES in disease incidences. Every rejected option quotes one of the three real reasons."),
 ("It can contaminate it",
  "STB-1.F.2 opens by stating that AQUACULTURE CAN CONTAMINATE WASTEWATER. The rejected options reverse the effect, overstate it, or deny that the statement exists."),
 ("Compete or breed with wild fish",
  "STB-1.F.2 states that fish that escape MAY COMPETE OR BREED WITH WILD FISH -- an ecological consequence and a genetic one. Two distractors keep one verb and deny the other, so the anchor carries both."),
 ("The density of fish in aquaculture",
  "STB-1.F.2 states that THE DENSITY OF FISH IN AQUACULTURE can lead to increases in disease incidences. Temperature, species and fuel appear nowhere in the statement, and the small area of water is one of STB-1.F.1's reasons for the expansion rather than a cause of disease."),
 ("They can be transmitted to wild fish",
  "STB-1.F.2 states that the increases in disease incidences CAN BE TRANSMITTED TO WILD FISH. The framework does not confine them to the farm, and it separately states that escapees may breed with wild fish."),
 ("escaped farmed fish may breed with wild fish",
  "Interbreeding mixes farmed with wild stock, which changes what the wild population IS rather than how many there are, and STB-1.F.2 names it alongside competition. Contaminated wastewater and density-driven disease are the statement's other drawbacks, and small water area is one of STB-1.F.1's benefits."),
 ("far less water area and far less fuel for each tonne",
  "Recomputed in q8 above: 0.4 hectares and 95 litres per tonne against 60 and 475 for the coastal fleet and 310 and 950 for the distant-water fleet. STB-1.F.1 gives only small areas of water and little fuel among its reasons. One distractor keeps the water half and reverses the fuel half, so the anchor carries both."),
 ("Ten times as much",
  "Recomputed in q9 above: 950 divided by 95 litres per tonne. The rejected values compare the coastal fleet with aquaculture, compare the two fleets with each other, or deny that the methods differ."),
 ("least feed for each kilogram gained and turn the largest share",
  "Recomputed in q10 above: 1.2 kilograms of feed per kilogram gained against 2.4 and 6.0, and 46 percent converted against 33 and 13. STB-1.F.1's first reason for the expansion is that aquaculture is HIGHLY EFFICIENT. One distractor keeps the feed half and reverses the conversion half, so the anchor carries both."),
 ("Five times as much",
  "Recomputed in q11 above: 6.0 divided by 1.2 kilograms of feed per kilogram gained. The rejected values compare poultry with fish, quote the cattle figure alone, or deny that the animals differ."),
 ("leaving the ponds carried far more nitrogen and far more suspended solids",
  "Recomputed in q12 above: nitrogen 0.9 to 7.2 milligrams per litre and suspended solids 6 to 54 across the ponds. STB-1.F.2 states that aquaculture can contaminate wastewater, and water leaving dirtier than it arrived is that contamination measured. One distractor reverses both, so the anchor carries the direction."),
 ("Eight times as much",
  "Recomputed in q13 above: 7.2 divided by 0.9 milligrams per litre. The rejected values come from the suspended solids column, whose ratio is nine, from the entering concentration, or from denying that the samples differ."),
 ("more farmed fish escaped, a larger share of the river's spawning fish",
  "Recomputed in q14 above: escapes of 4, 19 and 46 thousand against farmed shares of spawners of 2, 11 and 28 percent. STB-1.F.2 states that fish that escape may compete or BREED with wild fish, and farmed fish among the spawners is the breeding half. One distractor reverses the direction, so the anchor carries it."),
 ("By 26 percentage points",
  "Recomputed in q15 above: 28 minus 2 percent of the spawners. The rejected values quote the final share alone, add the two, take the rise in the escapes column, or quote the middle year."),
 ("more densely a cage was stocked, the larger the share of fish showing the disease",
  "Recomputed in q16 above: densities of 5, 15, 30 and 60 fish per cubic meter against diseased shares of 3, 11, 26 and 52 percent. STB-1.F.2 states that THE DENSITY OF FISH IN AQUACULTURE can lead to increases in disease incidences. One distractor reverses the direction, so the anchor carries it."),
 ("49 percentage points larger",
  "Recomputed in q17 above: 52 minus 3 percent of the fish. The rejected values quote the densest cage alone, add the two, quote a middle cage, or quote the thinnest cage alone."),
 ("commonest in the wild fish nearest the cages and rarer with distance",
  "Recomputed in q18 above: 1, 5, 15 and 40 kilometers against parasite shares of 38, 21, 9 and 3 percent. STB-1.F.2 states that increases in disease incidences can be TRANSMITTED TO WILD FISH. One distractor reverses the direction, so the anchor carries it."),
 ("35 percentage points commoner",
  "Recomputed in q19 above: 38 minus 3 percent of the wild fish. The rejected values quote the nearest site alone, add the two, compare the wrong pair of sites, or quote a middle site."),
 ("three reasons for its expansion: efficiency, small areas of water, and little fuel",
  "STB-1.F.1 supplies three reasons for the expansion before STB-1.F.2 supplies the drawbacks, so the framework carries both sides. Reducing the reasons to one, or denying the drawbacks, both misreport it."),
 ("escapees may compete OR BREED with wild fish",
  "STB-1.F.2 states that fish that escape MAY COMPETE OR BREED WITH WILD FISH, so both consequences sit inside the statement. One distractor keeps the breeding half and denies the competing half, so the anchor carries both verbs."),
 ("attributes the rise to the density of fish in aquaculture",
  "STB-1.F.2 names THE DENSITY OF FISH IN AQUACULTURE as what can lead to increases in disease incidences. Fuel and small water area are STB-1.F.1's reasons for the expansion, and interbreeding is a separate drawback within the same statement."),
 ("farmed origin found spawning in a river alongside its wild fish",
  "STB-1.F.2 states that fish that escape may compete or breed with wild fish, and farmed fish spawning in a wild river is that meeting observed. The rejected observations report the wastewater drawback, the density drawback, or one of STB-1.F.1's benefits."),
 ("carrying more nitrogen and solids than the water entering it",
  "STB-1.F.2 states that aquaculture CAN CONTAMINATE WASTEWATER, so water leaving dirtier than it arrived is the direct evidence. One distractor reverses the direction, so the anchor carries it; the others report a different drawback or a benefit."),
 ("number of fish held in each cubic meter of a cage, and the share of its fish showing disease",
  "STB-1.F.2 ties increases in disease incidences to the DENSITY of fish, so the test needs a measure of density AND a measure of disease. Each rejected pair supplies at most one of the two or tests a different drawback, which is why the anchor spans the pairing."),
 ("replaced wild capture fishing across the world",
  "STB-1.F.1 says aquaculture has EXPANDED and gives three reasons for it; nothing in either statement says it has replaced capture fishing anywhere. Each rejected option quotes one of the two statements directly."),
 ("things that can happen rather than as certainties",
  "STB-1.F.2 says aquaculture CAN contaminate wastewater, that escapees MAY compete or breed, and that density CAN lead to increases in disease. Each is a possibility, so reading any of them as a guarantee or as an impossibility departs from the wording."),
 ("giving efficiency, small areas of water and little fuel as reasons",
  "STB-1.F.1 gives high efficiency, only small areas of water and little fuel as the reasons aquaculture has expanded, which are claims about resources. The drawbacks are a separate statement, and the scarcity of fish species is EIN-2.J.1 in topic 5.8."),
 ("One gives the reasons the practice has expanded; the other gives the drawbacks",
  "STB-1.F.1 supplies efficiency, small water area and little fuel as reasons for the expansion, and STB-1.F.2 supplies contaminated wastewater, escapees that may compete or breed, and density-driven disease. One distractor swaps their order, so the anchor carries both halves."),
 ("highly efficient and needs only small areas of water and little fuel; but it can contaminate",
  "The keyed summary carries STB-1.F.1's three reasons and all three of STB-1.F.2's drawbacks. Each rejected summary reverses a reason, denies the drawbacks, drops two of the three, or adds a claim about replacing capture fishing that the framework never makes."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15,
                16: q16, 17: q17, 18: q18, 19: q19}

e_check.run(e5_16, CLAIMS, TABLE_CHECKS)
