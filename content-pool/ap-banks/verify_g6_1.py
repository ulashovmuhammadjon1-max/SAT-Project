"""Key audit for AP HUMAN GEOGRAPHY 6.1 The Origin and Influences of
Urbanization.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-6.A, "Explain the processes that
initiate and drive urbanization and suburbanization", and two statements:

    PSO-6.A.1 Site and situation influence the origin, function, and growth of
              cities.
    PSO-6.A.2 Changes in transportation and communication, population growth,
              migration, economic development, and government policies influence
              urbanization.

SITE AGAINST SITUATION IS THE WHOLE OF THE FIRST STATEMENT and the CED defines
neither term. The definitions used in every claim that depends on them:

    SITE      the absolute, physical characteristics of the place itself --
              terrain, water, soil, climate, defensibility, buildable ground.
    SITUATION the relative position of the place -- what routes, resources,
              settlements and markets it stands near or between.

The operative test, applied in items 4, 19, 25 and 28: a site attribute can be
stated without naming any other place and a situation attribute cannot. "A deep
sheltered harbour" needs no second place; "the nearest port to the wheat-growing
interior" cannot be said without one. Items 21 and 22 then establish that BOTH
can change, and that situation can change WITHOUT THE CITY MOVING -- a canal cut
a thousand kilometres away transforms a city's situation and leaves its site
untouched. That asymmetry is what makes situation the more powerful of the two
for explaining rise and decline, and items 7, 8 and 22 are built on it.

PSO-6.A.2 IS A CLOSED LIST OF FIVE and items 11 to 17 walk it. The CED pairs
transportation with communication in one entry, so items 11 and 12 take one
each and item 12's key states what distinguishes them -- transport moves bodies
and goods, communication moves information, and they relax different constraints.
Item 17 tests the boundary of the list, with the rank-size rule (EK PSO-6.C.1) as
the distractor. Nothing outside those five is keyed as a driver anywhere here.

THE DISTINCTION THE DATA ITEMS DEPEND ON, and item 24 asks for directly:
URBANIZATION IS A SHARE, not a count. The urban population and the urban share
can move at completely different rates while total population changes, which is
exactly what item 26's table demonstrates -- a share rising from 20 to 65 percent
alongside an urban population rising almost tenfold. A student who reads
urbanization as "cities got bigger" will misread every table in Unit 6, so the
recompute derives both numbers rather than either one.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE. Site and situation arguments about
real cities are contestable and often stale, and a described place tests the same
reasoning without asserting anything a verifier could not check.

The three table items (26, 27, 28) are the computational gate:

  26  the urban population is derived at all four dates from total times share,
      so both the count and the proportion are computed; the verifier asserts
      they grow at DIFFERENT rates, which is the item's whole point
  27  growth checked to fall at every step, and at least one town checked to
      have LOST population, since a distractor asserts all four grew
  28  the two columns checked to rank differently, so the record genuinely
      separates site from situation rather than totalling advantages

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_1


def q26_share_against_count(table):
    """Urban count and urban share both derived, and shown to grow differently."""
    totals, shares, urban = [], [], []
    for _, t, s in table["rows"]:
        total = float(t.replace(",", ""))
        share = float(s)
        totals.append(total)
        shares.append(share)
        urban.append(total * share / 100)
    assert urban[0] == 40 and urban[-1] == 390, urban
    assert shares[0] == 20 and shares[-1] == 65, shares
    count_growth = urban[-1] / urban[0]
    share_growth = shares[-1] / shares[0]
    assert 9 < count_growth < 10, count_growth
    # The point of the item: the two measures do NOT grow at the same rate.
    assert count_growth > 2 * share_growth, (count_growth, share_growth)
    return f"from {urban[0]:.0f} million to {urban[-1]:.0f} million"


def q27_growth_against_distance(table):
    """Growth falls at every step, and at least one town lost population."""
    dist = [float(r[1]) for r in table["rows"]]
    growth = [float(r[2]) for r in table["rows"]]
    assert all(b > a for a, b in zip(dist, dist[1:])), dist
    assert all(b < a for a, b in zip(growth, growth[1:])), growth
    # A distractor asserts all four grew; one must not have.
    assert min(growth) < 0, growth
    assert growth[0] == 410, growth
    return f"from {growth[0]:.0f} percent on the line"


def q28_site_against_situation(table):
    """The two columns must rank differently, or the record would not separate them."""
    site = {r[0]: float(r[1]) for r in table["rows"]}
    situation = {r[0]: float(r[2]) for r in table["rows"]}
    best_situation = max(situation, key=situation.get)
    best_site = max(site, key=site.get)
    assert best_situation == "Location 2", situation
    # If the same location led on both columns the item would not test the
    # distinction at all.
    assert best_site != best_situation, (site, situation)
    assert situation[best_situation] == 3, situation
    assert site[best_situation] == 1, site
    others = [v for k, v in situation.items() if k != best_situation]
    assert max(others) < situation[best_situation], situation
    words = {1: "one", 3: "three"}
    return (f"{words[int(situation[best_situation])]} situation advantages "
            f"recorded against {words[int(site[best_situation])]} site advantage")


CLAIMS = [
 ("Site and situation",
  "EK PSO-6.A.1 states that site and situation influence the origin, function and growth of cities. The rank-size rule and the urban structure models belong to Topics 6.4 and 6.5 and describe patterns among or within cities rather than why a city stands where it does."),

 ("terrain, water supply, soil and defensibility",
  "EK PSO-6.A.1 names site alongside situation as an influence on the origin, function and growth of cities. Site is the absolute description of a place, and everything in it can be stated without mentioning anywhere else."),

 ("what routes, resources and markets it stands near",
  "EK PSO-6.A.1 names situation alongside site. Situation is relative location, so every situational statement is a statement about a relationship, which is why a change elsewhere can alter a city's situation without anything at the city changing."),

 ("can be described without referring to any other place",
  "EK PSO-6.A.1 names both influences without defining either, so the working test has to come from what the words mean. A harbour's depth can be stated on its own; being the nearest harbour to a mining district cannot be stated without naming the district."),

 ("defensibility, fresh water and buildable ground",
  "EK PSO-6.A.1 names site among the influences on the origin of cities. Every attribute in the stem describes the ground the settlement stands on, and none of them requires another settlement or route to be mentioned."),

 ("position with respect to routes and the places they connect",
  "EK PSO-6.A.1 names situation among the influences on the origin, function and growth of cities. A crossing point has value only because of where the routes lead, so the advantage is a relationship to other places rather than a property of the ground."),

 ("while a city's situation continues to sustain it",
  "EK PSO-6.A.1 says site and situation influence the origin, FUNCTION and growth of cities, which allows the three to come apart over time. A city founded for one reason can persist for another, since accumulated population, capital and connections are themselves a situational advantage."),

 ("the pattern of routes around it changed while the town itself did not",
  "EK PSO-6.A.1 names situation among the influences on the growth of cities, and situation is relative. Nothing at the town altered, but the map of connections around it did, which is how situation can decline with no physical change on the ground."),

 ("trade, defence, administration, manufacturing",
  "EK PSO-6.A.1 names function alongside origin and growth. A defensible height suits a fortress, a sheltered harbour a port and a route crossing a market, so a location does not merely permit a city but shapes what the city is for."),

 ("increase in the share of a population living in urban areas",
  "EK PSO-6.A.2 names the influences on urbanization, and the term itself denotes a proportion rather than a count. Confusing the share with the number is the commonest error in reading urban data, because the two move differently whenever total population is changing."),

 ("extended the distance a person could live from work",
  "EK PSO-6.A.2 names changes in transportation among the influences on urbanization, and learning objective PSO-6.A covers suburbanization too. A city's radius is set by how far a person can travel in an acceptable commuting time, so raising the speed raises the radius."),

 ("loosens the requirement that people who work together be in the same place",
  "EK PSO-6.A.2 names changes in transportation AND communication together as influences on urbanization. Transport moves bodies and goods while communication moves information, and the second relaxes a different constraint on where activity must be located."),

 ("whether they arrive as migrants or are born there",
  "EK PSO-6.A.2 names population growth among the influences on urbanization. A city can grow by natural increase within it as well as by arrivals, which is why rapidly growing populations urbanize even where migration is limited."),

 ("raises the urban share directly",
  "EK PSO-6.A.2 names migration among the influences on urbanization. A move from a rural place to an urban one changes both the numerator and the denominator of the urban share at once, which is why it moves the measure faster than births alone can."),

 ("pay more than agriculture",
  "EK PSO-6.A.2 names economic development among the influences on urbanization. Manufacturing and services gain from being near labour, suppliers and customers in a way farming does not, so development concentrates work where people already are and draws in more."),

 ("where to site a capital and whether movement is restricted",
  "EK PSO-6.A.2 names government policies among the influences on urbanization. A government builds the infrastructure, sets the rules for building and in some states controls internal movement directly, so its decisions shape both the pull and the permission."),

 ("The rank-size rule",
  "EK PSO-6.A.2 names changes in transportation and communication, population growth, migration, economic development and government policies. The rank-size rule belongs to EK PSO-6.C.1 and describes the size distribution of a set of cities rather than what drives urbanization."),

 ("movements of population within the urban system",
  "Learning objective PSO-6.A asks for the processes that initiate and drive urbanization AND suburbanization, and EK PSO-6.A.2 names transportation among the influences. A faster journey both brings people to a city and lets them live further out within it."),

 ("harbour is site",
  "EK PSO-6.A.1 names both influences, and the two halves of this stem separate cleanly on the standard test. A harbour's depth can be stated without mentioning anywhere else; being the nearest port to somewhere cannot be stated without naming that somewhere."),

 ("may extend to a region, a continent or the world",
  "EK PSO-6.A.1 names both site and situation as influences on the origin, function and growth of cities. Site is bounded by the place itself, while situation is a claim about relationships whose reach depends on what the city is connected to."),

 ("have been altered by construction",
  "EK PSO-6.A.1 names site among the influences on cities, and nothing in the statement makes site permanent. Reclamation, drainage and levelling all change what is physically there, which is exactly what the term site describes."),

 ("while its site is exactly as it was",
  "EK PSO-6.A.1 names situation among the influences on the growth of cities, and situation is relative location. This is the cleanest demonstration that a city's situation can be transformed by construction it took no part in, thousands of kilometres away."),

 ("Economic development and migration",
  "EK PSO-6.A.2 names both economic development and migration among its five influences on urbanization. The factories are the development and the arrival of workers is the migration, and the CED lists them separately because either can occur without the other."),

 ("so the proportion living in cities stayed the same",
  "EK PSO-6.A.2 concerns influences on urbanization, which is the SHARE of a population living in cities. A share is a ratio, so it can hold steady while both of its terms grow, which is precisely why a count of city dwellers is not a measure of urbanization."),

 ("A confluence of two navigable rivers used by traders",
  "EK PSO-6.A.1 names site and situation as two distinct influences, and the test is whether an attribute can be stated without referring to another place. Only one pairing here puts an attribute in the category that test assigns it to; each of the others reverses it."),

 ("from 40 million to 390 million",
  "Recomputed from the record: multiplying each total by its urban share gives 40, 112, 240 and 390 million urban residents, so the count grows by a factor of about 9.75 while the share rises from 20 to 65 percent. The verifier asserts the two grow at different rates, which is the reason the item exists.",
  ),

 ("from 410 percent on the line",
  "Recomputed from the record: growth falls at every step as distance rises, from 410 percent for the town on the line to a loss of 12 percent for the town 95 kilometres away, so one town lost population. EK PSO-6.A.2 names changes in transportation among the influences on urbanization, and EK PSO-6.A.1's situation is what the railway altered for each of them.",
  ),

 ("three situation advantages recorded against one site advantage",
  "Recomputed from the record: one location records three situational advantages against no more than two for any other, and it is NOT the location leading on site advantages. The verifier asserts that the two columns rank differently, since a record in which one place led on both would not separate the two influences at all.",
  ),

 ("may partly share a cause rather than one producing the other",
  "EK PSO-6.A.2 names changes in transportation among the influences on urbanization and EK PSO-6.A.1 makes situation an influence on growth. A route is planned as well as built, so the towns it was routed through may have been chosen for prospects that a later record reports as its effect."),

 ("both the ground it stands on and its position relative to everywhere else",
  "EK PSO-6.A.1 supplies site and situation as influences on origin, function and growth, and EK PSO-6.A.2 supplies the five influences on urbanization. Each rejected summary either drops one of the two statements or reduces a list of five influences to a single one."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.1 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.1 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_share_against_count,
    27: q27_growth_against_distance,
    28: q28_site_against_situation,
}

geo_check.check(g6_1, ANCHORS, TABLE_NOTES)
