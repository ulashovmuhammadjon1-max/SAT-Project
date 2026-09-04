"""Key audit for AP ENVIRONMENTAL SCIENCE 5.17 Sustainable Forestry.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  STB-1.G.1  Some of the methods for mitigating deforestation include
             reforestation, using and buying wood harvested by ecologically
             sustainable forestry techniques, and reusing wood.
                    -- items 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 23, 24, 27
  STB-1.G.2  Methods to protect forests from pathogens and insects include
             integrated pest management (IPM) and the removal of affected trees.
                    -- items 5, 6, 9, 16, 17, 26
  STB-1.G.3  Prescribed burn is a method by which forests are set on fire under
             controlled conditions in order to reduce the occurrence of natural
             fires.        -- items 7, 8, 18, 19, 20, 21, 22, 25, 28
Items 29 and 30 read the three statements against each other.

NO MECHANISM IS EVER KEYED. The framework says nothing about HOW reforestation
restores a forest, how removing affected trees checks a pathogen, or how a
controlled fire reduces natural ones. Every method item is keyed by which
statement names it or by what a table shows, and item 28 keys the absence of any
mechanism directly.

THE DOUBLE HEDGE. STB-1.G.1 reads SOME OF THE METHODS ... INCLUDE, partial twice
over. Item 23 keys that, and no item anywhere says the three are the only ways.

THE TWO-VERB CLAUSE. STB-1.G.1 says USING AND BUYING sustainably harvested wood.
Item 3 anchors on both verbs, because two distractors keep one and deny
the other.

BOUNDARY WITH 5.14, gated by item 9: STB-1.G.2 NAMES integrated pest management
while STB-1.C.1 DEFINES it. The definition is never keyed here, and item 9's
anchor spans both halves because a distractor swaps the two roles.

BOUNDARY WITH 5.12: that topic's worked forest setting is annual growth against
annual cut. No table here reuses it.

DATA ITEMS: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 and 21, recomputed below
from those tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_17

AREA = "Forest area (thousand hectares)"
PLANTED = "Trees planted during the period (millions)"
PRE = "Before the programme began"
TEN = "Ten years after it began"
TWENTY = "Twenty years after it began"

REPLANTED = "Share of the logged area replanted within two years (percent)"
STREAMS = "Streams on the estate meeting the water quality standard (percent)"
UNCERT = "Estate selling uncertified timber"
CERT = "Estate selling certified timber"

RECLAIMED = "Reclaimed timber used each year (thousand cubic meters)"
FELLED = "Newly felled timber bought each year (thousand cubic meters)"
NOREUSE = "No old timber reused"
SOMEREUSE = "Some old timber reused"
MOSTREUSE = "Most old timber reused"

REMOVED = "Affected trees removed in the first season (percent)"
INFESTED = "Trees infested three seasons later (percent)"
NOREMOVE = "No affected trees removed"
HALFREMOVE = "Half the affected trees removed"
MOSTREMOVE = "Nearly all affected trees removed"

LITTER = "Dead wood and litter on the ground (tonnes per hectare)"
BURNED_AREA = "Area burned by natural fires over ten years (percent of the block)"
NOBURN = "No prescribed burning"
BURN = "Prescribed burning carried out"

FIRES = "Natural fires recorded in twenty years"
NEVER = "No prescribed burns at all"
TENYR = "A burn every ten years"
FOURYR = "A burn every four years"


def q10(table, item):
    a, p = cg.col(table, AREA), cg.col(table, PLANTED)
    assert cg.cell(table, PRE, AREA) == min(a), \
        "'the largest area was recorded before the programme' must be false"
    assert all(a[i] < a[i + 1] for i in range(len(a) - 1)), f"forest area must grow; got {a}"
    assert cg.cell(table, PRE, PLANTED) == 0, "no trees may have been planted before the programme"
    assert cg.cell(table, TEN, PLANTED) > 0 and cg.cell(table, TWENTY, PLANTED) > 0, \
        "'no trees were planted at any point' must be false"
    return (f"forest area runs {a} thousand hectares while trees planted run {p} million, the "
            "area growing as the planting continues")


def q11(table, item):
    a = cg.col(table, AREA)
    d = cg.cell(table, TWENTY, AREA) - cg.cell(table, PRE, AREA)
    assert d == 63, f"the growth recomputes to {d}, not 63"
    for wrong in (max(a), max(a) + min(a),
                  cg.cell(table, TEN, AREA) - cg.cell(table, PRE, AREA),
                  cg.cell(table, TWENTY, AREA) - cg.cell(table, TEN, AREA)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"183 minus 120 is {d:.0f} thousand hectares more forest after twenty years"


def q12(table, item):
    assert cg.cell(table, CERT, REPLANTED) > cg.cell(table, UNCERT, REPLANTED), \
        "the certified estate must replant the larger share"
    assert cg.cell(table, CERT, STREAMS) > cg.cell(table, UNCERT, STREAMS), \
        "the certified estate must keep more streams within the standard"
    assert cg.cell(table, CERT, REPLANTED) > 3 * cg.cell(table, UNCERT, REPLANTED), \
        "the replanting difference must be large, not marginal"
    return (f"the certified estate replants {cg.cell(table, CERT, REPLANTED):.0f} percent against "
            f"{cg.cell(table, UNCERT, REPLANTED):.0f} and keeps "
            f"{cg.cell(table, CERT, STREAMS):.0f} percent of its streams within the standard "
            f"against {cg.cell(table, UNCERT, STREAMS):.0f}")


def q13(table, item):
    d = cg.cell(table, CERT, REPLANTED) - cg.cell(table, UNCERT, REPLANTED)
    assert d == 76, f"the difference recomputes to {d}, not 76"
    for wrong in (cg.cell(table, CERT, REPLANTED),
                  cg.cell(table, CERT, REPLANTED) + cg.cell(table, UNCERT, REPLANTED),
                  cg.cell(table, CERT, STREAMS) - cg.cell(table, UNCERT, STREAMS),
                  cg.cell(table, UNCERT, REPLANTED)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"94 minus 18 is {d:.0f} percentage points more of the logged area replanted"


def q14(table, item):
    r, f = cg.col(table, RECLAIMED), cg.col(table, FELLED)
    assert cg.cell(table, NOREUSE, RECLAIMED) == min(r), \
        "the practice using no reclaimed timber must sit at the bottom of that column"
    assert cg.cell(table, NOREUSE, FELLED) == max(f), \
        "'the practice using no reclaimed timber bought the least new timber' must be false"
    assert all(r[i] < r[i + 1] for i in range(len(r) - 1)), f"reclaimed use must rise; got {r}"
    assert all(f[i] > f[i + 1] for i in range(len(f) - 1)), f"new purchases must fall; got {f}"
    return (f"reclaimed timber runs {r} thousand cubic meters against new purchases of {f}, the "
            "two moving in opposite directions")


def q15(table, item):
    f = cg.col(table, FELLED)
    d = cg.cell(table, NOREUSE, FELLED) - cg.cell(table, MOSTREUSE, FELLED)
    assert d == 150, f"the difference recomputes to {d}, not 150"
    for wrong in (max(f), max(f) + min(f),
                  cg.cell(table, NOREUSE, FELLED) - cg.cell(table, SOMEREUSE, FELLED), min(f)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"240 minus 90 is {d:.0f} thousand cubic meters less new timber bought each year"


def q16(table, item):
    r, i = cg.col(table, REMOVED), cg.col(table, INFESTED)
    assert cg.cell(table, NOREMOVE, REMOVED) == 0, "the untreated stand must remove nothing"
    assert cg.cell(table, NOREMOVE, INFESTED) == max(i), \
        "'the stand from which none were removed had the fewest infested' must be false"
    assert all(r[i2] < r[i2 + 1] for i2 in range(len(r) - 1)), f"removal must rise; got {r}"
    assert all(i[i2] > i[i2 + 1] for i2 in range(len(i) - 1)), f"infestation must fall; got {i}"
    assert len(set(i)) > 1, "'the same share in all three stands' must be false"
    return (f"removal runs {r} percent against infestation three seasons later of {i} percent, "
            "the two moving in opposite directions")


def q17(table, item):
    i = cg.col(table, INFESTED)
    d = cg.cell(table, NOREMOVE, INFESTED) - cg.cell(table, MOSTREMOVE, INFESTED)
    assert d == 58, f"the difference recomputes to {d}, not 58"
    for wrong in (max(i), max(i) + min(i),
                  cg.cell(table, NOREMOVE, INFESTED) - cg.cell(table, HALFREMOVE, INFESTED),
                  cg.cell(table, MOSTREMOVE, REMOVED)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"64 minus 6 is {d:.0f} percentage points fewer trees infested three seasons later"


def q18(table, item):
    assert cg.cell(table, BURN, LITTER) < cg.cell(table, NOBURN, LITTER), \
        "the burned block must carry less dead wood and litter"
    assert cg.cell(table, BURN, BURNED_AREA) < cg.cell(table, NOBURN, BURNED_AREA), \
        "the burned block must lose less area to natural fires"
    assert cg.cell(table, NOBURN, LITTER) > 2 * cg.cell(table, BURN, LITTER), \
        "the litter difference must be large, not marginal"
    return (f"the burned block carries {cg.cell(table, BURN, LITTER):.0f} tonnes per hectare "
            f"against {cg.cell(table, NOBURN, LITTER):.0f} and loses "
            f"{cg.cell(table, BURN, BURNED_AREA):.0f} percent of its area to natural fires "
            f"against {cg.cell(table, NOBURN, BURNED_AREA):.0f}")


def q19(table, item):
    d = cg.cell(table, NOBURN, BURNED_AREA) - cg.cell(table, BURN, BURNED_AREA)
    assert d == 31, f"the difference recomputes to {d}, not 31"
    for wrong in (cg.cell(table, NOBURN, BURNED_AREA),
                  cg.cell(table, NOBURN, BURNED_AREA) + cg.cell(table, BURN, BURNED_AREA),
                  cg.cell(table, NOBURN, LITTER) - cg.cell(table, BURN, LITTER),
                  cg.cell(table, BURN, BURNED_AREA)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"38 minus 7 is {d:.0f} percentage points less of the block lost to natural fires"


def q20(table, item):
    l, f = cg.col(table, LITTER), cg.col(table, FIRES)
    assert cg.cell(table, NEVER, LITTER) == max(l), \
        "the block never burned must carry the most litter"
    assert cg.cell(table, NEVER, FIRES) == max(f), \
        "'the block never given a prescribed burn recorded the fewest natural fires' must be false"
    assert all(l[i] > l[i + 1] for i in range(len(l) - 1)), f"litter must fall; got {l}"
    assert all(f[i] > f[i + 1] for i in range(len(f) - 1)), f"natural fires must fall; got {f}"
    assert len(set(f)) > 1, "'the same number of natural fires' must be false"
    return (f"litter runs {l} tonnes per hectare against natural fires of {f}, both falling as "
            "the interval between prescribed burns shortens")


def q21(table, item):
    base = cg.cell(table, FOURYR, FIRES)
    assert base > 0, "the frequently burned block must record some fires for a ratio to exist"
    ratio = cg.cell(table, NEVER, FIRES) / base
    assert ratio == 5, f"the ratio recomputes to {ratio}, not 5"
    for wrong in (cg.cell(table, TENYR, FIRES) / base,
                  cg.cell(table, NEVER, FIRES) - base, 12, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"15 divided by 3 is {ratio:.0f} times as many natural fires in the unburned block"


CLAIMS = [
 ("Reforestation, using and buying wood harvested by ecologically sustainable",
  "STB-1.G.1 names reforestation, using and buying wood harvested by ecologically sustainable forestry techniques, and reusing wood. Clearcutting is the impact EIN-2.C describes rather than a mitigation, and the remaining lists are STB-1.E.1's soil conservation methods and STB-1.C.1's pest management methods."),
 ("Clearing a further area of forest",
  "STB-1.G.1's methods are reforestation, using and buying sustainably harvested wood, and reusing wood. Clearing more forest is the deforestation the statement sets out to mitigate, and every rejected option is quoted from the statement itself."),
 ("Using it and buying it",
  "STB-1.G.1 names USING AND BUYING wood harvested by ecologically sustainable forestry techniques, so the method covers both what a person does with the wood and what a person pays for. Two distractors keep one verb and deny the other, so the anchor carries both."),
 ("Reusing wood",
  "STB-1.G.1 names REUSING WOOD as its third method. Burning it for fuel, replacing it with concrete, storing it unused and exporting it are none of them, and the framework names no substitute material anywhere in this topic."),
 ("Integrated pest management and the removal of affected trees",
  "STB-1.G.2 states that methods to protect forests from pathogens and insects include INTEGRATED PEST MANAGEMENT (IPM) AND THE REMOVAL OF AFFECTED TREES. Prescribed burning belongs to STB-1.G.3, whose stated purpose is reducing natural fires rather than controlling pathogens."),
 ("Prescribed burning",
  "STB-1.G.2 names integrated pest management and the removal of affected trees. Prescribed burning is STB-1.G.3, and the framework gives its purpose as reducing the occurrence of natural fires, not as protecting a forest from pathogens or insects."),
 ("forests are set on fire under controlled conditions",
  "STB-1.G.3 states that a prescribed burn is a method by which FORESTS ARE SET ON FIRE UNDER CONTROLLED CONDITIONS. The fire is deliberately set and controlled, which is what separates it from a natural fire left to run."),
 ("To reduce the occurrence of natural fires",
  "STB-1.G.3 states that the fire is set IN ORDER TO REDUCE THE OCCURRENCE OF NATURAL FIRES. Protecting a forest from pathogens and insects is the purpose STB-1.G.2 attaches to its own two methods, and the framework names no agricultural or yield purpose here."),
 ("one of two methods for protecting forests from pathogens and insects; there it is defined",
  "STB-1.G.2 NAMES integrated pest management as one of two methods for protecting forests from pathogens and insects, while STB-1.C.1 in topic 5.14 DEFINES it as a combination of biological, physical and limited chemical methods. One distractor is the exact swap of the naming and the definition, so the anchor carries both halves."),
 ("forest area grew across the record as trees continued to be planted",
  "Recomputed in q10 above: 120, 148 and 183 thousand hectares against 0, 31 and 36 million trees planted. STB-1.G.1 names reforestation among the methods for mitigating deforestation. One distractor reverses the direction, so the anchor carries it."),
 ("By 63 thousand hectares",
  "Recomputed in q11 above: 183 minus 120 thousand hectares. The rejected values quote the final area alone, add the two, or take the growth over one of the two ten-year intervals."),
 ("replants far more of what it logs and keeps far more of its streams",
  "Recomputed in q12 above: 94 percent of the logged area replanted against 18, and 88 percent of streams within the standard against 35. STB-1.G.1 names using and buying wood harvested by ecologically sustainable forestry techniques among the methods for mitigating deforestation. One distractor keeps the first half and reverses the second, so the anchor carries both."),
 ("76 percentage points greater",
  "Recomputed in q13 above: 94 minus 18 percent of the logged area. The rejected values quote the certified estate alone, add the two, take the difference in the stream column, or quote the uncertified estate alone."),
 ("more reclaimed timber the trade used, the less newly felled timber it bought",
  "Recomputed in q14 above: reclaimed timber 0, 60 and 150 thousand cubic meters against new purchases of 240, 180 and 90. STB-1.G.1 names reusing wood among the methods for mitigating deforestation. One distractor reverses the direction, so the anchor carries it."),
 ("150 thousand cubic meters less",
  "Recomputed in q15 above: 240 minus 90 thousand cubic meters bought each year. The rejected values quote the unreused case alone, add the two, take an intermediate step, or quote the reused case alone."),
 ("affected trees were removed at the outset, the fewer trees were infested",
  "Recomputed in q16 above: removal of 0, 50 and 95 percent against infestation three seasons later of 64, 29 and 6 percent. STB-1.G.2 names the removal of affected trees among the methods to protect forests from pathogens and insects. One distractor reverses the direction, so the anchor carries it."),
 ("58 percentage points smaller",
  "Recomputed in q17 above: 64 minus 6 percent of the trees. The rejected values quote the untreated stand alone, add the two, compare the wrong pair of stands, or take a reading from the removal column."),
 ("carried less dead wood and litter and lost less area to natural fires",
  "Recomputed in q18 above: 12 tonnes of litter per hectare against 46, and 7 percent of the area lost to natural fires against 38. STB-1.G.3 gives reducing the occurrence of natural fires as the purpose of a prescribed burn. One distractor keeps the litter half and reverses the fire half, so the anchor carries both."),
 ("31 percentage points less",
  "Recomputed in q19 above: 38 minus 7 percent of the block. The rejected values quote the unburned block alone, add the two, take the difference in the litter column, or quote the burned block alone."),
 ("less litter lay on the ground and the fewer natural fires were recorded",
  "Recomputed in q20 above: litter of 52, 27 and 11 tonnes per hectare against 15, 6 and 3 natural fires as the interval shortens. STB-1.G.3 gives reducing the occurrence of natural fires as the purpose of a prescribed burn. Distractors reverse one or both directions, so the anchor carries both."),
 ("Five times as many",
  "Recomputed in q21 above: 15 divided by 3 natural fires in twenty years. The rejected values come from the block burned every ten years, from the difference rather than the ratio, or from denying that the blocks differ."),
 ("fire that people set deliberately under controlled conditions",
  "STB-1.G.3 states that forests ARE SET ON FIRE UNDER CONTROLLED CONDITIONS, so the fire is deliberate and managed rather than natural and unmanaged. Protecting forests from pathogens and insects is STB-1.G.2's purpose for its own two methods, not this one's."),
 ("gives SOME of the methods and says they INCLUDE these three",
  "STB-1.G.1 opens with SOME OF THE METHODS and then says they INCLUDE the three it names, which marks the list as partial twice over. Nothing in the wording claims completeness, and the pathogen methods are a separate statement, STB-1.G.2."),
 ("area under forest in the district grew over the years trees were planted",
  "STB-1.G.1 names reforestation among the methods for mitigating DEFORESTATION, so the area under forest is the quantity that reports success. Natural fires belong to STB-1.G.3 and pathogens to STB-1.G.2, and sawmills and prices measure neither."),
 ("Fewer natural fires occurred in the block afterwards",
  "STB-1.G.3 gives the purpose as reducing THE OCCURRENCE OF NATURAL FIRES, so the count of natural fires is the quantity that reports success. Timber cut, pathogen loads and forest area answer to other statements."),
 ("affected trees taken out at the outset, and the share of trees infested",
  "STB-1.G.2 names the removal of affected trees as a method to protect forests from pathogens and insects, so a test needs a measure of the removal AND a measure of the infestation afterwards. Each rejected pair supplies at most one of the two or tests a different statement, which is why the anchor spans the pairing."),
 ("Buying wood harvested by ecologically sustainable forestry techniques, and reusing old wood",
  "STB-1.G.1's three methods are reforestation, using and buying sustainably harvested wood, and reusing wood, so the second and third remain open to someone who plants nothing. Prescribed burning is STB-1.G.3 and serves a different purpose, and the framework nowhere calls for abandoning wood."),
 ("account of how a controlled fire reduces the occurrence of natural fires",
  "STB-1.G.3 defines the practice, states the condition and gives the purpose, and stops there. It supplies no mechanism, so an account of how a controlled fire reduces natural ones would be added rather than read. Each rejected option quotes something the statement does supply."),
 ("lists methods against deforestation, one lists methods against pathogens and insects",
  "STB-1.G.1 addresses deforestation, STB-1.G.2 addresses pathogens and insects, and STB-1.G.3 defines a prescribed burn and gives reducing natural fires as its purpose. They are three different threats, and one forest can face all three at once."),
 ("Some methods against deforestation include reforestation, using and buying sustainably harvested wood",
  "The keyed summary carries STB-1.G.1's three methods with its hedged wording, STB-1.G.2's two protection methods, and STB-1.G.3's definition and purpose. Each rejected summary shortens a list, moves a method to the wrong statement, reverses the purpose, or denies that a purpose is given."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19, 20: q20, 21: q21}

e_check.run(e5_17, CLAIMS, TABLE_CHECKS)
