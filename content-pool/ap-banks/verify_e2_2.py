"""Key audit for AP ENVIRONMENTAL SCIENCE 2.2 Ecosystem Services.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
ERT-2.B.1  There are four categories of ecosystem services: provisioning,
           regulating, cultural, and supporting.
                              -- items 1, 2, 3, 4, 21, 22, 23, 30
ERT-2.C.1  Anthropogenic activities can disrupt ecosystem services, potentially
           resulting in economic and ecological consequences.
                              -- items 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17,
                                 18, 20, 24, 25, 26, 27, 28, 29, 30

WHAT IS DELIBERATELY NOT ASKED. ERT-2.B.1 names four categories and defines
none of them, so no item sorts a named service into a category on the strength
of a definition the framework never gives, and nothing turns on the
regulating-versus-supporting boundary. Items 21 and 22 ask which of the
framework's own four NAMES fits a described case by the ordinary meaning of the
word; the claims below say so outright, and both were chosen because ordinary
English settles them.

ERT-2.C.1's modal words are load-bearing: CAN disrupt, POTENTIALLY resulting.
Items 7 and 27 turn on exactly that, and no key anywhere hardens the claim into
a certainty or drops one of the two kinds of consequence.

DATA ITEMS: 8 to 20 carry tables. Every keyed conclusion is recomputed below
from that table alone, by column header, and each check also falsifies the
distractor it is most likely to be confused with.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. ``python3 verify_e2_2.py
--selftest`` is the same run; the controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e2_2

AREA = "Wetland area remaining (hectares)"
FLOODCOST = "Cost of flood damage each year (thousands of dollars)"
DIST = "Distance to the nearest natural woodland (kilometres)"
FRUIT = "Percent of flowers that set fruit"
REMOVED = "Percent of the mangrove removed before the storm"
DAMAGE = "Cost of property damage from the storm (thousands of dollars)"
FOREST = "Forest cover remaining (percent)"
TREAT = "Cost of treating the town water supply each year (thousands of dollars)"
FISH = "Fish species recorded in the stream"
TILLAGE = "Years of continuous tillage"
TOPSOIL = "Topsoil depth (centimetres)"
GRAIN = "Grain harvested (tonnes per hectare)"
CORAL = "Living coral cover (percent)"
DIVERS = "Visitors booking guided dives each year"
MARGIN = "Area of flowering field margins left uncut (hectares)"
BEES = "Wild bee species recorded"
YIELD = "Yield of an insect pollinated crop (tonnes)"
MARSH = "Marsh area retained (hectares)"
NITROGEN = "Nitrogen reaching the lake each year (tonnes)"
TREES = "Mature trees left standing (thousands)"
TIMBER = "Timber harvested from the block each year (cubic metres)"
DUNE = "Sand dune volume remaining (percent of the original)"
HOUSES = "Houses damaged in the same storm"


def _falls(vals):
    return all(vals[i + 1] < vals[i] for i in range(len(vals) - 1))


def _rises(vals):
    return all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))


def _by(table, key_header, *headers):
    """Rows sorted ascending on ``key_header``; returns one list per header."""
    order = sorted(range(len(table["rows"])), key=lambda i: cg.col(table, key_header)[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q8(table, item):
    area = cg.col(table, AREA)
    cost = cg.col(table, FLOODCOST)
    assert _falls(area), f"the wetland area must fall at every stage; got {area}"
    assert _rises(cost), f"the flood damage cost must rise at every stage; got {cost}"
    assert cost[-1] != cost[0], "'the cost stayed the same' must be false"
    return (f"the wetland area runs {area} hectares while the flood cost runs {cost} "
            "thousands of dollars, one strictly falling and the other strictly rising")


def q9(table, item):
    cost = cg.col(table, FLOODCOST)
    ratio = cost[-1] / cost[0]
    assert abs(ratio - 13) < 0.05, f"the cost must rise about thirteenfold; got {ratio}"
    assert abs(ratio - 4) > 1, "'about fourfold' must be false"
    assert ratio > 1, "'it fell' must be false"
    return (f"the yearly flood cost goes {cost[0]:.0f} to {cost[-1]:.0f} thousands of "
            f"dollars, a factor of {ratio:.1f}")


def q10(table, item):
    (fruit,) = _by(table, DIST, FRUIT)
    assert _falls(fruit), f"fruit set must fall as distance rises; got {fruit}"
    assert len(set(fruit)) == len(fruit), "'all four orchards set the same percent' must be false"
    assert fruit[-1] != max(fruit), "'the furthest orchard set the most fruit' must be false"
    return (f"sorted by distance from woodland the fruit set reads {fruit} percent, "
            "strictly decreasing across the four orchards")


def q11(table, item):
    (dam,) = _by(table, REMOVED, DAMAGE)
    assert _rises(dam), f"damage must rise as more mangrove is removed; got {dam}"
    assert dam[0] == min(dam), \
        "'the stretch with no mangrove removed suffered most' must be false"
    assert len(set(dam)) == len(dam), "'damage was the same on all four' must be false"
    return (f"sorted by the percent of mangrove removed the storm damage reads {dam} "
            "thousands of dollars, strictly increasing")


def q12(table, item):
    treat, fish = _by(table, FOREST, TREAT, FISH)
    treat, fish = treat[::-1], fish[::-1]  # most forested first
    assert _rises(treat), f"treatment cost must rise as forest falls; got {treat}"
    assert _falls(fish), f"fish species must fall as forest falls; got {fish}"
    return (f"from the most forested catchment to the least, treatment cost reads {treat} "
            f"thousands of dollars and fish species reads {fish}, one rising and one falling")


def q13(table, item):
    labs = cg.labels(table)
    treat = dict(zip(labs, cg.col(table, TREAT)))
    fish = dict(zip(labs, cg.col(table, FISH)))
    dearest = max(treat, key=treat.get)
    poorest = min(fish, key=fish.get)
    assert dearest == poorest == "Catchment 4", \
        f"the dearest and the poorest row must both be Catchment 4; got {dearest} and {poorest}"
    assert len(set(treat.values())) == len(treat), "the treatment costs must all differ"
    assert len(set(fish.values())) == len(fish), "the fish counts must all differ"
    return (f"the highest treatment cost {treat[dearest]:.0f} and the lowest fish count "
            f"{fish[poorest]:.0f} fall in the same row, {dearest}")


def q14(table, item):
    soil, grain = _by(table, TILLAGE, TOPSOIL, GRAIN)
    assert _falls(soil), f"topsoil must fall with years of tillage; got {soil}"
    assert _falls(grain), f"the harvest must fall with years of tillage; got {grain}"
    assert grain[-1] != max(grain), "'the longest tilled field yields most' must be false"
    return (f"sorted by years of tillage the topsoil reads {soil} centimetres and the "
            f"harvest reads {grain} tonnes per hectare, both strictly falling")


def q15(table, item):
    (vis,) = _by(table, CORAL, DIVERS)
    assert _rises(vis), f"visitors must rise with living coral; got {vis}"
    assert vis[0] == min(vis), "'the site with least coral attracts most visitors' must be false"
    assert len(set(vis)) == len(vis), "'the same number at every site' must be false"
    return (f"sorted by living coral cover the visitor counts read {vis}, strictly "
            "increasing with the coral")


def q16(table, item):
    bees, yld = _by(table, MARGIN, BEES, YIELD)
    assert _rises(bees), f"bee species must rise with margin area; got {bees}"
    assert _rises(yld), f"crop yield must rise with margin area; got {yld}"
    assert bees[0] != max(bees), "'the smallest margin records the most bees' must be false"
    return (f"sorted by margin area the bee species read {bees} and the yield reads {yld} "
            "tonnes, both strictly increasing, so both fall as the margins go")


def q17(table, item):
    bees, yld = _by(table, MARGIN, BEES, YIELD)
    assert _rises(bees), f"the species column must move with margin area; got {bees}"
    assert _rises(yld), f"the yield column must move with margin area; got {yld}"
    assert bees != yld, "the two columns must be distinguishable rather than identical"
    assert max(yld) > max(bees), \
        "the tonnage column must be the larger one, so the two are not interchangeable"
    return (f"the species column reads {bees} and the tonnage column reads {yld}; both "
            "track the margin area and they are different measurements of it")


def q18(table, item):
    marsh = cg.col(table, MARSH)
    nit = cg.col(table, NITROGEN)
    assert _falls(marsh), f"the retained marsh must fall across the steps; got {marsh}"
    assert _rises(nit), f"the nitrogen load must rise across the steps; got {nit}"
    assert nit[0] == min(nit), "'the load was highest while the marsh was intact' must be false"
    return (f"the retained marsh runs {marsh} hectares while the nitrogen load runs {nit} "
            "tonnes a year, one strictly falling and the other strictly rising")


def q19(table, item):
    (tim,) = _by(table, TREES, TIMBER)
    assert _rises(tim), f"timber taken must rise with trees standing; got {tim}"
    assert tim[0] == min(tim), "'the block with fewest trees yields most' must be false"
    assert len(set(tim)) == len(tim), "'the same volume from every block' must be false"
    return (f"sorted by mature trees standing the annual harvest reads {tim} cubic metres, "
            "strictly increasing with the trees")


def q20(table, item):
    (hs,) = _by(table, DUNE, HOUSES)
    assert _falls(hs), f"houses damaged must fall as dune volume rises; got {hs}"
    assert hs[-1] == min(hs), "'the intact section suffered most' must be false"
    assert len(set(hs)) == len(hs), "'the same number on every section' must be false"
    return (f"sorted by dune volume remaining the houses damaged read {hs}, strictly "
            "decreasing as the dunes are retained")


CLAIMS = [
 ("cultural and supporting",
  "ERT-2.B.1, near verbatim: there are four categories of ecosystem services: provisioning, regulating, cultural, and supporting. Each rejected list replaces at least one of those four names."),
 ("Four",
  "ERT-2.B.1 states that there are four categories of ecosystem services and then names exactly four, so the count is the framework's own."),
 ("Regenerating",
  "ERT-2.B.1 names provisioning, regulating, cultural and supporting. Regenerating is not among the four, so it is the heading that does not belong."),
 ("fourth category, supporting",
  "ERT-2.B.1 gives four categories and the student's three are the first three of them, so the omission is supporting and nothing else."),
 ("Anthropogenic activities",
  "ERT-2.C.1 states that anthropogenic activities can disrupt ecosystem services. Anthropogenic means human caused, which is the class of activity the statement is about."),
 ("Economic and ecological",
  "ERT-2.C.1, near verbatim: anthropogenic activities can disrupt ecosystem services, potentially resulting in economic and ecological consequences. Both kinds are named together."),
 ("possible outcomes rather than guaranteed",
  "ERT-2.C.1 is written with can and potentially, which assert possibility rather than necessity, so neither disruption nor its consequences is claimed to be inevitable."),
 ("rose at every stage while the wetland area fell",
  "Recomputed in q8 above: the wetland area strictly falls while the yearly flood cost strictly rises. ERT-2.C.1 names economic consequences as one of the two kinds anthropogenic disruption can bring."),
 ("thirteenfold",
  "Recomputed in q9 above: 2,600 divided by 200 is 13. The size of the change is read from the record rather than assumed, and ERT-2.C.1 supplies the category of consequence it belongs to."),
 ("the smaller the percent of its flowers",
  "Recomputed in q10 above: sorted by distance from woodland the fruit set is strictly decreasing. ERT-2.B.1 establishes that ecosystems supply services, and this record measures one across a gradient of separation."),
 ("larger where more of the mangrove",
  "Recomputed in q11 above: sorted by the share of mangrove removed the storm damage is strictly increasing, and one storm crossed all four stretches. ERT-2.C.1 attaches economic consequences to anthropogenic disruption."),
 ("an economic and an ecological consequence together",
  "Recomputed in q12 above: as forest cover falls the treatment cost rises and the fish species count falls. ERT-2.C.1 names economic and ecological consequences together, and one column measures each."),
 ("Catchment 4",
  "Recomputed in q13 above: the highest treatment cost and the lowest fish count fall in the same row. ERT-2.C.1 allows the two kinds of consequence to appear in the same case."),
 ("Both topsoil depth and grain harvested fall",
  "Recomputed in q14 above: sorted by years of tillage both the topsoil depth and the harvest are strictly decreasing. ERT-2.C.1 links anthropogenic activity to consequences of both kinds."),
 ("Fewer visitors book dives",
  "Recomputed in q15 above: visitor bookings are strictly increasing in living coral cover. ERT-2.B.1 names cultural services among the four categories, and ERT-2.C.1 attaches economic consequences to disruption."),
 ("Both the count of wild bee species and the crop yield fall",
  "Recomputed in q16 above: sorted by margin area both the bee species count and the crop yield are strictly increasing, so both fall as the margins are cut. ERT-2.C.1 pairs ecological with economic consequences."),
 ("wild bee species is the ecological consequence",
  "Recomputed in q17 above: the two columns are distinct measurements that both track margin area. A count of species present measures the living system and a harvest measured in tonnes measures production, which is ERT-2.C.1's pairing of ecological with economic."),
 ("rose as the retained marsh area fell",
  "Recomputed in q18 above: the retained marsh strictly falls while the nitrogen load strictly rises. ERT-2.C.1 states that anthropogenic activities can disrupt ecosystem services, and clearing the marsh is such an activity."),
 ("Less timber is taken each year",
  "Recomputed in q19 above: the annual harvest is strictly increasing in the number of mature trees standing. ERT-2.B.1 names provisioning among the four categories, and harvested timber is a good the system supplies."),
 ("retaining less of their dune volume",
  "Recomputed in q20 above: houses damaged are strictly decreasing in the dune volume retained, for one storm across all four sections. ERT-2.C.1 attaches economic consequences to anthropogenic disruption."),
 ("Provisioning",
  "ERT-2.B.1 supplies the four names and defines none of them, so the match rests on the ordinary meaning of the framework's own word: to provision is to supply. One option is not a framework category at all."),
 ("Cultural",
  "ERT-2.B.1 supplies the four names and defines none of them, so the match rests on the ordinary meaning of the framework's own word: ceremony, story and recreation are matters of culture. One option is not a framework category at all."),
 ("without ranking them",
  "ERT-2.B.1 states that there are four categories and lists them, attaching no order of importance, so every ranking offered here is an addition to the framework rather than a reading of it."),
 ("comparable marsh left intact",
  "ERT-2.C.1 links anthropogenic disruption to economic consequences, so the evidence must be a cost that moved with the clearing, and an uncleared marsh is what separates the clearing from whatever else changed over the same years."),
 ("number of fish species living in a stream",
  "ERT-2.C.1 names economic and ecological consequences as two kinds. A count of species present is a property of the living system, while every rejected option is a sum of money or a count of jobs."),
 ("pays more each year to treat the water",
  "ERT-2.C.1 names economic and ecological consequences as two kinds. A recurring payment is money changing hands, while every rejected option describes a change in the living system itself."),
 ("a case with no measured cost does not contradict it",
  "ERT-2.C.1 asserts possibility, not necessity, through the words can and potentially, so a single case without a measured consequence is consistent with the statement."),
 ("Draining a marsh to build houses",
  "ERT-2.C.1 is a statement about anthropogenic activities, meaning human caused ones. Every rejected option is a natural event, which the framework treats separately under natural disruptions to ecosystems."),
 ("may carry consequences both for the economy and for the living system",
  "ERT-2.C.1 states that anthropogenic activities CAN disrupt ecosystem services, POTENTIALLY resulting in economic AND ecological consequences. Each rejected account hardens can into always, drops a consequence, denies the human role, or adds a ranking."),
 ("potentially with economic and ecological consequences",
  "ERT-2.B.1 supplies the count and the four names and ERT-2.C.1 supplies the anthropogenic cause and the pair of possible consequences, so the two statements together are exactly what the keyed summary says and no more."),
]

TABLE_CHECKS = {8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16, 17: q17, 18: q18, 19: q19, 20: q20}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e2_2, CLAIMS, TABLE_CHECKS)
