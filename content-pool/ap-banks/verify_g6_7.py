"""Key audit for AP HUMAN GEOGRAPHY 6.7 Infrastructure.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective IMP-6.B, "Explain how a city's
infrastructure relates to local politics, society, and the environment",
suggested skill 3.C, and ONE essential knowledge statement:

    IMP-6.B.1 The location and quality of a city's infrastructure directly
              affects its spatial patterns of economic and social development.

THE STATEMENT HAS TWO INPUTS AND TWO OUTPUTS and every item sits somewhere on
that grid. LOCATION and QUALITY are different variables and the CED names both:
a district can be crossed by a trunk road it has no junction onto, and it can
have a water main that runs six hours a day. Items 3 and 4 separate them, item 5
combines them in one case, and item 18 keys on the measurement consequence -- pipe
length measures location and hours of service measures quality, and neither
substitutes for the other. Item 1's four distractors each delete one of the
statement's four terms, which is the cheapest way to check that all four are
being read.

THE WORD "SPATIAL" DOES REAL WORK and items 6 and 7 key on it. The claim is about
the distribution of development ACROSS a city's districts, not about a city-wide
total or growth rate, so both items offer the aggregate reading as a distractor.

THE LEARNING OBJECTIVE ADDS THREE RELATIONSHIPS the essential knowledge does not
name: politics, society and the environment. Items 8, 16, 23 and 24 take
politics, 9, 20 and 21 society, and 10, 11 and 19 the environment, with item 25
requiring all three to be told apart. The politics items key on the MECHANISM --
infrastructure is expensive, durable and publicly decided, and a route that could
run several ways distributes benefit and disruption whichever way it runs -- and
never on a motive attributed to a named party.

THE PROPERTY THAT MAKES INFRASTRUCTURE GEOGRAPHIC is that it is fixed in place
and outlasts the decision that put it there. Items 12, 13, 15 and 22 rest on
that, and item 15 supplies the reason gaps persist: investment follows the
districts that already generate demand and revenue, so the relationship runs both
ways over time. That is a loop rather than an intention, which is why the key
states it as one.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  all THREE infrastructure columns are checked to fall together while
      mortality rises -- the key's force comes from three independent measures
      agreeing, and one column disagreeing would undercut it
  27  floor area checked to fall at every step, since the key claims a gradient
      rather than merely a difference between the ends
  28  both columns checked to rise together and the runoff ratio derived, since
      the key claims a specific direction and the item's environmental point
      depends on it

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_7


def q26_provision_against_outcome(table):
    """Three infrastructure measures must fall together while mortality rises."""
    water = [float(r[1]) for r in table["rows"]]
    power = [float(r[2]) for r in table["rows"]]
    roads = [float(r[3]) for r in table["rows"]]
    mortality = [float(r[4]) for r in table["rows"]]
    for series in (water, power, roads):
        assert all(b < a for a, b in zip(series, series[1:])), series
    assert all(b > a for a, b in zip(mortality, mortality[1:])), mortality
    assert mortality[0] == 6 and mortality[-1] == 63, mortality
    # The three measures must agree on which district is best served, or the
    # key's claim that they move together would not hold.
    assert water.index(max(water)) == power.index(max(power)) == roads.index(max(roads))
    assert water.index(max(water)) == mortality.index(min(mortality)), (water, mortality)
    return f"child mortality rises from {mortality[0]:.0f} to {mortality[-1]:.0f}"


def q27_building_near_station(table):
    """New floor area must fall at every step, not merely between the ends."""
    area = [float(r[1].replace(",", "")) for r in table["rows"]]
    assert all(b < a for a, b in zip(area, area[1:])), area
    assert area[0] == 640 and area[-1] == 45, area
    assert area[0] > 10 * area[-1], area
    return f"from {area[0]:.0f} thousand square metres in the nearest band to {area[-1]:.0f}"


def q28_runoff_against_paving(table):
    """Impervious share and peak runoff rise together across all four."""
    impervious = [float(r[1]) for r in table["rows"]]
    runoff = [float(r[2]) for r in table["rows"]]
    assert all(b > a for a, b in zip(impervious, impervious[1:])), impervious
    assert all(b > a for a, b in zip(runoff, runoff[1:])), runoff
    assert impervious[0] == 12 and impervious[-1] == 74, impervious
    assert runoff[0] == 4.1 and runoff[-1] == 31.5, runoff
    assert runoff[-1] / runoff[0] > 7, runoff
    return (f"from {runoff[0]} to {runoff[-1]} cubic metres per second as "
            f"impervious surface rises from {impervious[0]:.0f} to {impervious[-1]:.0f} percent")


CLAIMS = [
 ("Its location and quality directly affect the city's spatial patterns",
  "EK IMP-6.B.1 states that the location AND quality of a city's infrastructure directly affects its spatial patterns of economic AND social development. All four terms sit in the sentence, and each rejected option removes exactly one of them."),

 ("utility networks such as water, sewerage, power and telecommunications",
  "EK IMP-6.B.1 refers to a city's infrastructure without enumerating it, and the category covers the built systems that make urban life possible. A student who hears only roads misses the utility and social networks that most directly determine who can live and work where."),

 ("so a station or an interchange pulls building toward it",
  "EK IMP-6.B.1 says the LOCATION of infrastructure directly affects spatial patterns of development. A network is reachable only at particular points, so its geography decides which sites are usable and which are passed over."),

 ("so a district can be nominally served and still unable to attract investment",
  "EK IMP-6.B.1 names QUALITY alongside location as a determinant of spatial patterns of development. A water main running six hours a day and a power supply failing nightly are both present on a map and absent in practice, which is exactly what the second term captures."),

 ("poorly served on both the location and the quality dimensions",
  "EK IMP-6.B.1 names location and quality together as determinants of spatial patterns of economic and social development. Proximity without access is a failure of location, since a network opens only at particular points, and unreliable power is a failure of quality."),

 ("uneven distribution of firms, jobs and investment across a city's districts",
  "EK IMP-6.B.1 says infrastructure affects a city's SPATIAL PATTERNS of economic and social development. The word spatial makes the claim about distribution within the city rather than about any city-wide total or growth rate."),

 ("uneven distribution across a city's districts of access to schooling",
  "EK IMP-6.B.1 names social development alongside economic development as something whose SPATIAL pattern infrastructure affects. Reading it as a city-wide measure loses the claim, which is precisely about differences between one district and another."),

 ("settled through a political process rather than by the network's own logic",
  "Learning objective IMP-6.B asks how a city's infrastructure relates to local politics, society and the environment. A route can usually serve several alignments about equally well on technical grounds, and choosing among them distributes benefit and disruption, which is what makes it political."),

 ("so the pattern of provision becomes a pattern of opportunity",
  "EK IMP-6.B.1 says infrastructure directly affects spatial patterns of SOCIAL development. Access is what a network delivers, so where it reaches and how well it works determines what a household can get to on an ordinary day."),

 ("so more of it runs off quickly and flooding downstream becomes more likely",
  "Learning objective IMP-6.B asks how a city's infrastructure relates to the environment. Replacing soil and vegetation with sealed surfaces changes the path water takes rather than the amount that arrives, and a faster path produces a higher peak flow."),

 ("so the same system protects the receiving rivers and the population's health",
  "Learning objective IMP-6.B asks how infrastructure relates to society and the environment, and EK IMP-6.B.1 makes its quality a determinant of social development. Untreated waste in a watercourse is at once an environmental discharge and a route by which disease returns to the population."),

 ("so journeys within it lengthen and the land beside the structure becomes less desirable",
  "EK IMP-6.B.1 says the location of infrastructure directly affects spatial patterns of economic and social development. A route built to move traffic THROUGH a place rather than to it is a barrier at ground level, and the benefit accrues to the through traveller while the disruption stays local."),

 ("determines what is possible long after the decision is forgotten",
  "EK IMP-6.B.1 makes the LOCATION of infrastructure a determinant of spatial patterns of development. Durability is what converts a decision into a geography: the network of a century ago is still the network today in most cities, and later building has been fitted to it."),

 ("built faster than networks can be extended",
  "EK IMP-6.B.1 says the location and quality of infrastructure directly affects spatial patterns of social development. Networks are planned, financed and laid over years while settlement can happen in months, and unrecognized tenure makes the investment harder to justify and to recover."),

 ("Investment tends to follow the districts that already generate demand and revenue",
  "EK IMP-6.B.1 says infrastructure directly affects spatial patterns of economic and social development, and over time the relationship runs both ways. A district with reliable service attracts firms and households whose activity then supplies the case for the next investment there."),

 ("maintenance prevents a failure that nobody sees",
  "Learning objective IMP-6.B asks how a city's infrastructure relates to local politics, and this is among the clearest instances. EK IMP-6.B.1 makes QUALITY a determinant of development, and deferred maintenance is exactly how quality falls while the map still shows a complete network."),

 ("the metropolitan area, where the network's overall shape determines which districts are connected",
  "EK IMP-6.B.1 says infrastructure affects SPATIAL PATTERNS of economic and social development, and a pattern exists only when districts are compared. The metropolitan network decides what is reachable while the local connection decides whether a particular household can use it."),

 ("hours per day the supply runs and whether the water meets safety standards",
  "EK IMP-6.B.1 names location and quality as two separate determinants, so a measure of one is not a measure of the other. Pipe length and coverage describe where a network goes; hours of service and water safety describe whether it does what it exists to do."),

 ("parks, street trees, wetlands, permeable paving",
  "Learning objective IMP-6.B asks how a city's infrastructure relates to the environment. Sealed surfaces speed runoff and store heat, and vegetated permeable features address both by restoring the processes those surfaces removed."),

 ("separated drinking water from human waste",
  "EK IMP-6.B.1 makes the quality of infrastructure a determinant of spatial patterns of social development. Density concentrates people and their waste in one place, so the network keeping the two apart is what makes dense settlement survivable at all."),

 ("determines what work, schooling and services a household or firm can obtain",
  "EK IMP-6.B.1 says the location and quality of a city's infrastructure directly affects spatial patterns of economic and social development. What makes something infrastructure is that access to it conditions what everything else can do, which is a functional test rather than a physical one."),

 ("improving the access improves the site without anything changing on the land itself",
  "EK IMP-6.B.1 says the location of infrastructure directly affects spatial patterns of economic development, and land value is where that effect registers first. What a site can be used for depends on what can reach it, so a new connection changes its possible uses and therefore its price."),

 ("requires agreement among authorities whose interests differ",
  "Learning objective IMP-6.B asks how a city's infrastructure relates to local politics. A network's logic is metropolitan while the authority to build it may be divided many ways, and EK IMP-6.B.1's location variable is exactly what such a division determines."),

 ("the people who pay and the people who benefit are often in different places",
  "Learning objective IMP-6.B asks how infrastructure relates to local politics, and EK IMP-6.B.1 makes its location a determinant of spatial patterns of development. A project in one district paid for city-wide, or paid for locally and used regionally, is a transfer between places however it is described."),

 ("Storm runoff rising as a catchment is paved over, matched to infrastructure and the environment",
  "Learning objective IMP-6.B names politics, society and the environment as three relationships. Only one pairing here matches an observation to the relationship it actually illustrates, and each of the others attaches an observation to one of the other two."),

 ("child mortality rises from 6 to 63",
  "Recomputed from the record: water coverage, electricity hours and paved road share all fall at every step across the four districts while deaths before age five rise from 6 to 63 per thousand. The verifier also checks that all three infrastructure measures agree on which district is best served, since the key's force comes from their agreement.",
  ),

 ("from 640 thousand square metres in the nearest band to 45",
  "Recomputed from the record: new floor area falls at every step from 640 to 310 to 120 to 45 thousand square metres as distance from the station rises, a fall of more than tenfold. EK IMP-6.B.1 says the LOCATION of infrastructure directly affects spatial patterns of economic development, and a network reachable only at points concentrates building at those points.",
  ),

 ("from 4.1 to 31.5 cubic metres per second as impervious surface rises",
  "Recomputed from the record: impervious surface rises at every step from 12 to 74 percent and peak runoff rises with it from 4.1 to 31.5 cubic metres per second, more than sevenfold. Learning objective IMP-6.B asks how a city's infrastructure relates to the environment, and sealed surfaces sending rain to the drain rather than into the ground is the mechanism.",
  ),

 ("without isolating the cause",
  "EK IMP-6.B.1 says infrastructure DIRECTLY AFFECTS spatial patterns of social development, but a table of districts cannot separate that effect from everything else varying between them. Poorly served districts are usually poorer in other respects too, so the record is consistent with the claim rather than a demonstration of it."),

 ("determine which districts get investment and jobs and which households can reach services",
  "EK IMP-6.B.1 names location AND quality as the inputs and spatial patterns of economic AND social development as the outputs. Each rejected summary drops one of those four terms, and the last denies the unevenness that makes the statement a claim about pattern at all."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.7 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.7 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_provision_against_outcome,
    27: q27_building_near_station,
    28: q28_runoff_against_paving,
}

geo_check.check(g6_7, ANCHORS, TABLE_NOTES)
