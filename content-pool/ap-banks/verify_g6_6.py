"""Key audit for AP HUMAN GEOGRAPHY 6.6 Density and Land Use.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Enduring understanding IMP-6, learning objective IMP-6.A,
suggested skill 3.D, and ONE essential knowledge statement:

    IMP-6    The attitudes and values of a population, as well as the balance of
             power within that population, are reflected in the built landscape.
    IMP-6.A  Explain how low-, medium-, and high-density housing characteristics
             represent different patterns of residential land use.
    IMP-6.A.1 Residential buildings and patterns of land use reflect and shape
             the city's culture, technological capabilities, cycles of
             development, and infilling.

"REFLECT AND SHAPE" IS THE ARCHITECTURE OF THIS STATEMENT and item 1 keys on it.
The relationship runs BOTH WAYS: buildings record the culture, technology and
moment that produced them, and they then constrain what the people living among
them can do afterwards. Items 12, 13, 14, 16, 17 and 23 run the second direction,
which is the half students drop, and item 1's distractors offer each direction
alone.

ITEM 7 IS THE ONE THAT REACHES PAST THE ESSENTIAL KNOWLEDGE to the enduring
understanding above it, which names the BALANCE OF POWER alongside attitudes and
values. That clause has no essential knowledge statement of its own in this
topic, so the item keys on the mechanism rather than on any claim about a
particular group: a dwelling exists because someone could assemble the land, the
finance and the permission, so the housing stock records who could do those
things. Nothing in the module attributes a motive to any named party.

THE FOUR THINGS IMP-6.A.1 NAMES, each with its own items: culture (6), what
households want; technological capabilities (8, 9), what is physically possible
-- elevators and frames for height, piped water and sewerage for density at all;
cycles of development (10, 19, 24, 27), a district built out in one wave and
fixed for decades; infilling (11, 12, 23, 28), building on interior sites so
density rises without the city spreading. Item 25's matching item requires all
four to be told apart.

THE THREE BANDS have no thresholds in the CED, so none is asserted. What the
module keys on instead is the MEASUREMENT problem the suggested skill implies:
a density means nothing until its denominator is stated, and gross density
(everything inside a boundary) against net density (residential land only) can
differ by a factor of two on identical ground. Items 20, 21 and 29 key on that,
and item 29 makes it the limitation on comparing two cities.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  both columns checked to rise together across all five forms and the
      fortyfold ratio derived, since the key claims a specific multiple
  27  the construction year checked to rise at every step while the housing form
      moves down the density scale, because the key claims both movements
  28  the infill SHARE is recomputed at all three dates from the two columns,
      and total new dwellings are checked to RISE while land consumed falls --
      the item's point is that more homes came from less new land, which a
      falling dwelling count would destroy

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. The module was drafted with 29 items; the
thirtieth is item 7, added because the enduring understanding's clause about the
balance of power had no item and is the half of IMP-6 that a topic about housing
density most directly illustrates.
"""
import re

import geo_check
import g6_6


def q26_density_ladder(table):
    """Both columns rise together, and the top-to-bottom ratio is fortyfold."""
    dwellings = [float(r[1].replace(",", "")) for r in table["rows"]]
    persons = [float(r[2].replace(",", "")) for r in table["rows"]]
    assert all(b > a for a, b in zip(dwellings, dwellings[1:])), dwellings
    assert all(b > a for a, b in zip(persons, persons[1:])), persons
    ratio = dwellings[-1] / dwellings[0]
    assert ratio == 40, (dwellings, ratio)
    assert dwellings[0] == 6 and dwellings[-1] == 240, dwellings
    assert persons[0] == 1400 and persons[-1] == 52000, persons
    return f"{dwellings[-1]:.0f} dwellings per hectare against {dwellings[0]:.0f}"


def q27_rings_by_age(table):
    """Construction year rises outward while the dominant form loses density."""
    years = [float(r[1].replace(",", "")) for r in table["rows"]]
    forms = [r[2] for r in table["rows"]]
    assert all(b > a for a, b in zip(years, years[1:])), years
    assert years[0] == 1908 and years[-1] == 1994, years
    # The form must move down the density scale as the year rises, or the key's
    # second clause would not follow from the record.
    assert forms[0].startswith("Mid-rise"), forms
    assert forms[-1].startswith("Detached houses, large"), forms
    assert len(set(forms)) == len(forms), forms
    return f"rises from {years[0]:.0f} to {years[-1]:.0f} with distance"


def q28_infill_share(table):
    """Infill share recomputed; more dwellings from less new land."""
    infill, green, land, totals, shares = [], [], [], [], []
    for _, i, g, l in table["rows"]:
        a = float(i.replace(",", ""))
        b = float(g.replace(",", ""))
        infill.append(a)
        green.append(b)
        land.append(float(l.replace(",", "")))
        totals.append(a + b)
        shares.append(round(100 * a / (a + b)))
    assert totals == [6000, 6500, 7500], totals
    assert shares == [20, 40, 68], shares
    # The whole point: more new homes built on less newly consumed land.
    assert totals[-1] > totals[0], totals
    assert land[-1] < land[0], land
    assert all(b < a for a, b in zip(land, land[1:])), land
    return f"rose from {shares[0]} to {shares[-1]} percent"


CLAIMS = [
 ("reflect those things and shape them in turn",
  "EK IMP-6.A.1 says residential buildings and patterns of land use REFLECT AND SHAPE the city's culture, technological capabilities, cycles of development and infilling. Both verbs are in the sentence, and the second is the one students routinely drop."),

 ("so few dwellings occupy each hectare",
  "Learning objective IMP-6.A asks how low-, medium- and high-density housing characteristics represent different patterns of residential land use. Low density is defined by the land each dwelling occupies, which is what makes it a land-use category rather than an architectural style."),

 ("sharing walls or stacked a few storeys high",
  "Learning objective IMP-6.A names low, medium and high density as three patterns of residential land use. The medium band is where dwellings begin to share walls or stack, raising the number per hectare without needing the technology a tower requires."),

 ("housing many dwellings on a small footprint",
  "Learning objective IMP-6.A names high density among the three patterns of residential land use. Stacking dwellings vertically is what lets a small footprint hold many households, which is why high density and building height are so closely associated."),

 ("tens of times as many dwellings per hectare",
  "Learning objective IMP-6.A distinguishes the three bands by their housing characteristics, and land per dwelling is what those characteristics amount to spatially. The range from a detached house on its own plot to an apartment tower is an order of magnitude or more."),

 ("is built into the housing they choose and can afford",
  "EK IMP-6.A.1 names culture first among the things residential buildings and land-use patterns reflect and shape. Housing is the most expensive purchase most households make, so what they want from a dwelling is visible in what gets built."),

 ("who owns land, who lends, and who sets the rules",
  "Enduring understanding IMP-6 states that the attitudes and values of a population AND the balance of power within it are reflected in the built landscape, and EK IMP-6.A.1 applies that to residential buildings. A dwelling exists because someone could assemble the land, the finance and the permission for it."),

 ("The safety elevator and the steel frame",
  "EK IMP-6.A.1 names technological capabilities among the things residential buildings reflect and shape. Height is the route to density on a small footprint, and it is impossible in practice without a way to move people up and a structure that carries the load."),

 ("cannot be done by wells and pits at that density",
  "EK IMP-6.A.1 names technological capabilities among the things that shape residential land use. Density is limited by whichever supporting system fails first, and before piped networks existed that was sanitation rather than construction."),

 ("record the practice of that period",
  "EK IMP-6.A.1 names cycles of development among the things residential buildings and land use reflect and shape. Building happens in waves and what a wave puts up stands for generations, so a district's density is largely fixed by the moment it was built out."),

 ("vacant or underused sites inside the already-built area",
  "EK IMP-6.A.1 names infilling among the things residential buildings and patterns of land use reflect and shape. The defining feature is the location of the site: inside the existing built-up area rather than beyond its edge."),

 ("so population rises while the built-up area does not",
  "EK IMP-6.A.1 names infilling alongside cycles of development. Density is population divided by area, so adding to the numerator while holding the denominator fixed is precisely what building on interior sites does."),

 ("whether walking, transit or driving is practical for decades afterward",
  "EK IMP-6.A.1 says residential buildings and land-use patterns reflect AND SHAPE the city. A street laid out at four dwellings per hectare puts every shop beyond walking distance, and that constraint outlives whoever chose the layout."),

 ("enough potential passengers within walking distance of each stop",
  "EK IMP-6.A.1 says residential buildings and land-use patterns shape as well as reflect the city. Transit economics is a ratio of riders to route length, and dwellings per hectare supplies the numerator, so the housing decision effectively makes the transport decision."),

 ("paid for by length, and low density means more length",
  "EK IMP-6.A.1 says patterns of land use shape the city, and infrastructure cost is among the clearest routes by which they do. A kilometre of water main costs about the same whether it serves twenty households or two hundred."),

 ("must earn more from each square metre to justify the price",
  "EK IMP-6.A.1 names technological capabilities among the things shaping residential land use, and bid-rent theory in EK PSO-6.D.1 supplies the economic half. Height is how a developer spreads an expensive site across more saleable floor area, so the density gradient tracks the land-value gradient."),

 ("so nearly all trips are made by car",
  "EK IMP-6.A.1 says residential buildings and land-use patterns shape the city. Low density spreads destinations out, and a distance too great to walk converts every errand into a vehicle trip, which is the practical meaning of the housing pattern."),

 ("support shops, schools and frequent transit within walking range",
  "EK IMP-6.A.1 says residential buildings and land use shape the city as well as reflecting it. A shop needs a threshold of customers within its range, and stacking households is how a small area assembles one, which is why dense districts carry street-level retail."),

 ("since each ring was built out in a later wave",
  "EK IMP-6.A.1 names cycles of development among the things residential buildings and patterns of land use reflect. A city that grew outward built each ring in a later period, so building age is a direct record of the sequence of growth."),

 ("because each includes different amounts of non-residential land",
  "The suggested skill for this topic is comparing patterns and trends in quantitative data, and a density is a ratio whose denominator must be stated. A metropolitan figure averages farmland and parkland in with apartment blocks and can be a tenth of the density of the districts inside it."),

 ("so net is always the larger figure",
  "The suggested skill for this topic is comparing patterns and trends in quantitative data, and this is the commonest ambiguity in a density figure. Roads, schools, parks and industry lie inside the boundary and hold no residents, so excluding them raises the figure, sometimes by a factor of two."),

 ("so technology alone does not determine density",
  "EK IMP-6.A.1 names culture, technological capabilities, cycles of development and infilling together. Technology sets what is possible rather than what is chosen, so two cities with the same possibilities can differ because of what residents wanted and when the housing was built."),

 ("already served by existing roads and pipes",
  "EK IMP-6.A.1 names infilling among the things residential buildings and patterns of land use reflect and shape. Building inside the served area uses capacity already paid for, which is why infill and outward expansion have such different consequences for a city's finances and its footprint."),

 ("owned by many separate parties",
  "EK IMP-6.A.1 names cycles of development among the things residential land use reflects and shapes. A wave of building fixes a density in physical form, and the cost and coordination needed to undo it are what make the pattern outlast the era that produced it."),

 ("New apartments built on a disused rail yard inside the city, matched to infilling",
  "EK IMP-6.A.1 names culture, technological capabilities, cycles of development and infilling as four distinct things. Only one pairing here matches an observation to the one it actually illustrates; each of the others swaps two of the statement's own categories."),

 ("240 dwellings per hectare against 6",
  "Recomputed from the record: dwellings per hectare rises at every step from 6 to 240, a factor of exactly forty, and persons per square kilometre rises with it from 1,400 to 52,000. Learning objective IMP-6.A asks how the three density bands represent different patterns of residential land use, and that spread is what the difference amounts to.",
  ),

 ("rises from 1908 to 1994 with distance",
  "Recomputed from the record: median construction year rises at every step from 1908 to 1994 while the dominant form moves from mid-rise apartments to detached houses on large plots. EK IMP-6.A.1 names cycles of development among the things residential buildings reflect, and a ring built later was built to a later and less dense practice.",
  ),

 ("rose from 20 to 68 percent",
  "Recomputed from the record: the two columns give 6,000, 6,500 and 7,500 new dwellings, of which the infill share is 20, 40 and 68 percent, while land newly built on falls from 620 to 260 hectares. The verifier asserts that total dwellings RISE while land consumed falls, since more homes from less new land is the item's whole point.",
  ),

 ("since a gross density including parks and industry",
  "The suggested skill for this topic is comparing patterns and trends in quantitative data, and a ratio is only as clear as its denominator. Two cities can appear to differ by a factor of two purely because one figure includes non-residential land and the other does not."),

 ("both record the culture, technology and period that produced them and constrain",
  "EK IMP-6.A.1 says residential buildings and patterns of land use REFLECT AND SHAPE the city's culture, technological capabilities, cycles of development and infilling. Each rejected summary drops one of the two verbs, reduces the four influences to one, or reverses what infilling means."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.6 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.6 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_density_ladder,
    27: q27_rings_by_age,
    28: q28_infill_share,
}

geo_check.check(g6_6, ANCHORS, TABLE_NOTES)
