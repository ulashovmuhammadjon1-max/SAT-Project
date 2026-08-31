"""Key audit for AP HUMAN GEOGRAPHY 5.11 Challenges of Contemporary Agriculture.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective IMP-5.B and four essential knowledge
statements -- the largest topic in Unit 5:

    IMP-5.B.1 innovations (biotechnology, genetically modified organisms,
              aquaculture) and the debates accompanying them (sustainability,
              soil and water usage, reductions in biodiversity, extensive
              fertilizer and pesticide use)
    IMP-5.B.2 movements relating to individual food choice (urban farming,
              community-supported agriculture, organic farming, value-added
              specialty crops, fair trade, local-food movements, dietary shifts)
    IMP-5.B.3 challenges of feeding a global population (lack of food access, as
              in food insecurity and food deserts; problems with distribution
              systems; adverse weather; land use lost to suburbanization)
    IMP-5.B.4 economic effects on food-production practices (location of
              food-processing facilities and markets, economies of scale,
              distribution systems, government policies)

THE OBJECTIVE'S WORD IS "DEBATES" AND IMP-5.B.1 SAYS "ACCOMPANIED BY". Neither
the CED nor this module takes a side on biotechnology, genetically modified
organisms or aquaculture. Every item on that statement is keyed to what an
innovation IS or to what the recorded debate is ABOUT, never to whether the
innovation is good, and items 3 and 6 offer both verdicts as distractors so that
the neutral reading is the one being tested. A key asserting that a contested
technology is safe or harmful would teach a position the framework does not hold,
which is exactly what SOCIAL_BRIEF.md's rule against guessing is for.

IMP-5.B.3'S FIRST CHALLENGE IS THE ONE STUDENTS MISREAD: it is LACK OF FOOD
ACCESS, not lack of food. Both of the CED's own examples -- food insecurity and
food deserts -- describe people who cannot reach or afford food that exists, and
the statement names problems with DISTRIBUTION SYSTEMS separately from any
shortfall in production. Items 17, 18, 19 and 29 rest on that, and it is why item
26's data item measures distance, vehicle access and poverty rather than the size
of any harvest.

THE TWO SIDES OF THE MARKET are IMP-5.B.2 and IMP-5.B.4, and item 25 requires
them to be told apart. The food-choice movements work by changing what people
buy, so they reach production through demand -- item 10 and item 15 key on that
mechanism explicitly. The economic forces work on the cost and organization of
producing. Both influence what is grown, by opposite routes.

SYNONYM CARE. `geo_check` treats {"genetically modified organisms", "gmos"} as
one construct and {"community-supported agriculture", "csa"} as another. The CED
pairs each abbreviation with its expansion, so where the statement is quoted both
forms sit inside a SINGLE choice; a pair of choices each carrying one form would
be flagged, and rightly, as two names for one thing.

The three table items (26, 27, 28) are the computational gate:

  26  all three columns are checked, and the keyed neighbourhood must be the
      extreme on distance AND on vehicle access -- distance alone is exactly the
      insufficient measure item 29 keys against, so the item must not reward
      reading one column
  27  both shares checked to sum to 100 in every year, and the farmed share
      confirmed to stay BELOW half, since one distractor asserts it passed half
  28  the four decadal figures summed and the four shares summed, with the
      largest single decade identified, because two distractors turn on which
      decade that was and on whether conversion continued

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_11


def q26_food_desert(table):
    """Distance AND the means to cover it must both point at the same place."""
    dist, vehicle, poverty = {}, {}, {}
    for name, d, v, p in table["rows"]:
        dist[name] = float(d)
        vehicle[name] = float(v)
        poverty[name] = float(p)
    worst = max(dist, key=dist.get)
    assert worst == "Neighbourhood 4", dist
    # Distance alone is not enough -- the same place must also be worst on
    # vehicle access, or the item would reward reading one column.
    assert min(vehicle, key=vehicle.get) == worst, vehicle
    assert max(poverty, key=poverty.get) == worst, poverty
    assert vehicle[worst] == 24, vehicle
    return f"{dist[worst]:.1f} kilometres from a full grocery store"


def q27_aquaculture_share(table):
    """Shares sum to 100 each year; the farmed share rises but stays below half."""
    farmed, wild = [], []
    for _, a, w in table["rows"]:
        assert float(a) + float(w) == 100, (a, w)
        farmed.append(float(a))
        wild.append(float(w))
    assert all(b > a for a, b in zip(farmed, farmed[1:])), farmed
    assert farmed[0] == 13 and farmed[-1] == 49, farmed
    # One distractor claims aquaculture passed half; it must not have.
    assert max(farmed) < 50, farmed
    return f"from {farmed[0]:.0f} to {farmed[-1]:.0f} percent"


def q28_farmland_converted(table):
    """Cumulative hectares and cumulative share, plus which decade was largest."""
    hectares, shares, decades = [], [], []
    for decade, ha, share in table["rows"]:
        decades.append(decade)
        hectares.append(float(ha.replace(",", "")))
        shares.append(float(share))
    total = sum(hectares)
    assert total == 1090000, total
    assert abs(sum(shares) - 11.5) < 0.001, sum(shares)
    # Two distractors turn on these: conversion did not stop, and the largest
    # decade was not the first.
    assert min(hectares) > 0, hectares
    assert decades[hectares.index(max(hectares))] == "1990s", (decades, hectares)
    return f"{total:,.0f} hectares"


CLAIMS = [
 ("Biotechnology, genetically modified organisms",
  "EK IMP-5.B.1 names exactly biotechnology, genetically modified organisms and aquaculture as the innovations accompanied by debate. Terraces and irrigation belong to EK IMP-5.A.2, urban farming and fair trade to EK IMP-5.B.2, and food deserts to EK IMP-5.B.3."),

 ("reductions in biodiversity, and extensive fertilizer",
  "EK IMP-5.B.1 names exactly sustainability, soil and water usage, reductions in biodiversity, and extensive fertilizer and pesticide use as the debates. Urban farming and dietary shifts are food-choice movements from EK IMP-5.B.2, which is the confusion the last option offers."),

 ("altered by direct intervention",
  "EK IMP-5.B.1 lists genetically modified organisms among innovations that have been ACCOMPANIED BY debates. The framework records the existence of a debate rather than resolving it, so a key asserting either verdict on safety would go beyond the statement it claims to rest on."),

 ("The farming of fish and other aquatic organisms",
  "EK IMP-5.B.1 names aquaculture among the innovations accompanied by debates over sustainability, soil and water usage and biodiversity. Farming aquatic species concentrates feed, waste and stock in one place, which is what connects the practice to each of the debates the statement lists."),

 ("displaces the many local varieties",
  "EK IMP-5.B.1 names reductions in biodiversity among the debates accompanying agricultural innovation. Uniformity is what a high-performing variety spreads, and uniformity across a landscape is the direct opposite of the diversity the debate concerns."),

 ("whether the gain can be sustained at that draw",
  "EK IMP-5.B.1 names soil and water usage among the debates accompanying innovations such as biotechnology and aquaculture. The word 'debates' is the framework's own, so this item is keyed to what is contested rather than to a verdict on it."),

 ("value-added specialty crops, fair trade, local-food movements",
  "EK IMP-5.B.2 names exactly these seven movements relating to individual food choice. Every rejected option is drawn from a different statement in this topic or from EK IMP-5.A.2, and telling the four lists apart is most of what this topic asks."),

 ("on rooftops, vacant lots and community plots",
  "EK IMP-5.B.2 names urban farming among the movements relating to individual food choice that influence patterns of food production and consumption. Producing inside the place of consumption is a direct reversal of the long chains described in EK PSO-5.E.1."),

 ("buy a share of a season's harvest in advance",
  "EK IMP-5.B.2 names community-supported agriculture among the movements relating to individual food choice. Paying before the harvest moves both the risk and the cash flow, which is what distinguishes the arrangement from simply buying local produce at a market."),

 ("rather than by regulation",
  "EK IMP-5.B.2 describes these as movements relating to INDIVIDUAL FOOD CHOICE that influence patterns of food production and consumption. The route from the movement to the field runs through the market, which is what makes them demand-side rather than policy changes."),

 ("commands a higher price than the ordinary commodity version",
  "EK IMP-5.B.2 names value-added specialty crops among the movements relating to individual food choice. The strategy is the exact opposite of competing on cost per tonne, which is why it is one route by which a small producer survives beside a large one."),

 ("The share of the final price that reaches the producer",
  "EK IMP-5.B.2 names fair trade among the movements relating to individual food choice, and EK PSO-5.E.1 places agricultural products in a global supply chain. The movement works on how value in that chain is divided, using buyers' willingness to pay more as its lever."),

 ("advantages in freshness, transport impact and support for the local economy",
  "EK IMP-5.B.2 names local-food movements among the movements relating to individual food choice. The claim is comparative rather than absolute, which is what makes the movement a counter-current to the long chains of EK PSO-5.E.1 rather than a rejection of trade."),

 ("changes what is worth growing",
  "EK IMP-5.B.2 names dietary shifts among the movements influencing patterns of food production AND consumption. Demand is what makes a crop worth planting, so a sustained change in what people eat reorganizes production wherever the market reaches."),

 ("reaches production through that demand",
  "EK IMP-5.B.2 describes all seven as movements relating to individual food choice that influence patterns of food production and consumption. That shared mechanism is what puts them on one list despite their differences in aim, scale and origin."),

 ("problems with distribution systems, adverse weather, and land use lost to suburbanization",
  "EK IMP-5.B.3 names exactly lack of food access, problems with distribution systems, adverse weather, and land use lost to suburbanization. The rejected options belong to EK IMP-5.B.1, EK IMP-5.B.2, EK IMP-5.B.4 and EK IMP-5.A.2 respectively."),

 ("reliable access to enough safe and nutritious food",
  "EK IMP-5.B.3 names lack of food access, as in cases of food insecurity and food deserts, among the challenges of feeding a global population. The framework's word is ACCESS, so the condition concerns reach and affordability rather than the size of a harvest."),

 ("little practical access to affordable fresh food",
  "EK IMP-5.B.3 gives food deserts as an example of lack of food access. The word 'desert' refers to the absence of food retail rather than to physical aridity, which is why food deserts occur in the middle of otherwise well-supplied cities."),

 ("still not reach the people who need it",
  "EK IMP-5.B.3 names problems with distribution systems alongside lack of food access among the challenges of feeding a global population. Listing them separately from any harvest shortfall is the framework distinguishing food that does not exist from food that does not arrive."),

 ("transmits that shortfall to prices everywhere",
  "EK IMP-5.B.3 names adverse weather among the challenges and EK PSO-5.E.1 places food in a global supply chain. A harvest is a biological outcome exposed to conditions nobody controls, and a chain linking producers to distant buyers passes the shortfall along to them."),

 ("which is often the best farmland",
  "EK IMP-5.B.3 names land use lost to suburbanization among the challenges of feeding a global population. Cities were founded where farming was good, so expansion takes the best land first, and building on soil is one of the few land-use changes that cannot readily be reversed."),

 ("economies of scale, distribution systems, and government policies",
  "EK IMP-5.B.4 names exactly the location of food-processing facilities and markets, economies of scale, distribution systems and government policies. Distinguishing this list from EK IMP-5.B.2's movements is the point: those work through what consumers buy, these through the cost of producing."),

 ("the plant's location concentrates that crop around it",
  "EK IMP-5.B.4 names the location of food-processing facilities and markets among the economic influences on food-production practices. Where a crop must reach a plant within hours, that plant's catchment is a hard boundary on where planting the crop makes sense at all."),

 ("changes what is profitable, and farmers respond to the altered returns",
  "EK IMP-5.B.4 names government policies among the economic forces bearing on food-production practices. Policy acting on prices leaves the decision with the farmer while changing which decision pays, which is why its effects appear as a shift in what gets grown."),

 ("matched to lack of food access",
  "EK IMP-5.B.1 to EK IMP-5.B.4 divide this topic into innovations and their debates, food-choice movements, challenges of feeding a global population, and economic forces on production. Only one pairing here places its case under the statement that actually covers it."),

 ("4.6 kilometres from a full grocery store",
  "Recomputed from the record: one neighbourhood is furthest from a full grocery store at 4.6 kilometres AND lowest on vehicle access at 24 percent, and it also records the highest poverty rate, so distance and the means of covering it point the same way. EK IMP-5.B.3 gives food deserts as an example of lack of food ACCESS, which is what those columns jointly measure.",
  ),

 ("rose from 13 to 49 percent",
  "Recomputed from the record: the two shares sum to 100 in every year, the farmed share rises at every step from 13 to 49 percent, and it does not pass half. EK IMP-5.B.1 names aquaculture among the innovations accompanied by debate, and a share approaching half of the supply is why those debates carry weight.",
  ),

 ("1,090,000 hectares were converted",
  "Recomputed from the record: the four decadal figures sum to 1,090,000 hectares and the four shares to 11.5 percent of prime farmland, with the largest single decade being the 1990s and conversion continuing in every decade shown. EK IMP-5.B.3 names land use lost to suburbanization among the challenges of feeding a global population.",
  ),

 ("Distance alone does not settle access",
  "EK IMP-5.B.3 names food deserts as a case of lack of food ACCESS rather than of distance. A short walk without money and a long drive with a car are different situations, so a distance figure is one input to the judgement rather than the judgement itself."),

 ("movements working through individual food choice",
  "EK IMP-5.B.1 covers innovations and their debates, EK IMP-5.B.2 the demand-side movements, EK IMP-5.B.3 the challenges of feeding a global population, and EK IMP-5.B.4 the economic forces on production. Keeping the four apart is exactly what the topic's structure asks a student to be able to do."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.11 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.11 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_food_desert,
    27: q27_aquaculture_share,
    28: q28_farmland_converted,
}

geo_check.check(g5_11, ANCHORS, TABLE_NOTES)
