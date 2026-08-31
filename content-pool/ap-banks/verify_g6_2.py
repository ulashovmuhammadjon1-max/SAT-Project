"""Key audit for AP HUMAN GEOGRAPHY 6.2 Cities Across the World.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-6.A and the two statements assigned
here:

    PSO-6.A.3 Megacities and metacities are distinct spatial outcomes of
              urbanization increasingly located in countries of the periphery
              and semiperiphery.
    PSO-6.A.4 Processes of suburbanization, sprawl, and decentralization have
              created new land-use forms -- including edge cities, exurbs, and
              boomburbs -- and new challenges.

THE TWO STATEMENTS POINT IN OPPOSITE DIRECTIONS AND BOTH ARE TRUE. PSO-6.A.3 is
about concentration -- urbanization producing single agglomerations of tens of
millions -- and about where those are increasingly found. PSO-6.A.4 is about
dispersal, activity spreading outward from a centre, and the settlement forms
that spreading invented. Items 24 and 30 key on the fact that a metacity can be
growing enormously while its own residents are pushed further and further from
its middle.

THE THRESHOLDS. The CED names megacity and metacity and defines neither. The
figures used are the conventional ones for this course -- about ten million and
about twenty million -- and items 2 and 3 state them AS conventions, because no
authority fixes them and a key presenting a convention as a definition would be
overstating what can be known. Item 23 tests the reasoning instead: a threshold
is crossed by growth in the AGGLOMERATION, and an administrative boundary change
can move a municipality's recorded population without one extra person living in
the urban area.

"INCREASINGLY" IS A TREND CLAIM and item 25 keys on it directly, with "every
megacity is in the periphery" as the distractor. Reading the CED's word as the
stronger claim is what leaves a student vulnerable to a single counterexample,
and item 29 makes the same point about evidence: one column of populations
describes a moment and cannot demonstrate a change.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE, the data items included. Which
agglomerations are largest changes from year to year, so a ranking true when
written can be false when a student reads it, and no verifier could catch that.
The record in item 26 uses numbered agglomerations for that reason.

THE FIVE FORMS IN PSO-6.A.4, none of which the CED defines. The definitions used
here: suburbanization is residential growth at the edge; sprawl is low-density,
discontinuous, car-dependent expansion; decentralization moves jobs, retail and
services outward and not only residents; an edge city is a concentration of
offices and retail outside the downtown, characteristically at a highway
junction; an exurb is prosperous low-density settlement beyond the continuous
suburbs, still commuting in; a boomburb is a rapidly grown suburban municipality
with a city's population that is not its metropolitan area's largest. Items 8 to
15 walk them, and items 14 and 15 take the two distinctions students actually
confuse -- edge city against exurb, boomburb against ordinary suburb.

ONE ANCHOR IS ON THE DESCRIPTION RATHER THAN THE FORM. Item 22's matching item
uses "matched to an edge city" in two of its five choices, so an anchor on the
form name would have matched a distractor. The anchor is the office-tower cluster
instead -- the check working as intended.

SYNONYM CARE. `geo_check` treats {"world system theory", "world-systems theory",
"core-periphery model"} as one construct, so no choice list names that framework
in two ways.

The three table items (26, 27, 28) are the computational gate:

  26  the core and non-core counts are derived, and the smallest agglomeration
      is checked against the twenty-million threshold, since the key asserts
      both facts
  27  all four zones summed at both dates, with the central city confirmed to be
      the only one that fell -- a distractor claims the whole area lost
      population and another that only the fringe grew
  28  density checked to fall and car share to rise at EVERY step, so the
      relationship is monotone rather than driven by the two extremes

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_2


def q26_where_the_largest_are(table):
    """Count by world-economy position, and check the metacity threshold."""
    pops = [float(r[1].replace(",", "")) for r in table["rows"]]
    positions = [r[2] for r in table["rows"]]
    words = {6: "Six"}
    core = sum(1 for p in positions if p == "Core")
    non_core = sum(1 for p in positions
                   if p in ("Periphery", "Semiperiphery"))
    assert core + non_core == len(positions) == 8, positions
    assert non_core == 6 and core == 2, (core, non_core)
    # The key also asserts every one clears the metacity threshold.
    assert min(pops) >= 20, pops
    # And the largest must be a core case, so one distractor is plainly false.
    assert positions[pops.index(max(pops))] == "Core", (pops, positions)
    return f"{words[non_core]} of the eight"


def q27_zones_over_time(table):
    """Metropolitan totals at both dates, and which zones rose or fell."""
    before = {r[0]: float(r[1]) for r in table["rows"]}
    after = {r[0]: float(r[2]) for r in table["rows"]}
    total_b = round(sum(before.values()), 1)
    total_a = round(sum(after.values()), 1)
    assert total_b == 4.9 and total_a == 8.1, (total_b, total_a)
    fell = [k for k in before if after[k] < before[k]]
    assert fell == ["Central city"], fell
    grew = [k for k in before if after[k] > before[k]]
    assert len(grew) == 3, grew
    return f"from {total_b} to {total_a} million"


def q28_density_against_car_use(table):
    """Density falls and car share rises at every step, not just at the ends."""
    density = [float(r[1].replace(",", "")) for r in table["rows"]]
    car = [float(r[2]) for r in table["rows"]]
    assert all(b < a for a, b in zip(density, density[1:])), density
    assert all(b > a for a, b in zip(car, car[1:])), car
    assert car[0] == 31 and car[-1] == 95, car
    assert density[0] == 9200 and density[-1] == 210, density
    return f"from {car[0]:.0f} to {car[-1]:.0f} percent"


CLAIMS = [
 ("In countries of the periphery and semiperiphery",
  "EK PSO-6.A.3 states that megacities and metacities are distinct spatial outcomes of urbanization increasingly located in countries of the periphery and semiperiphery. The word 'increasingly' makes it a claim about a trend rather than about a fixed distribution."),

 ("at least about ten million people",
  "EK PSO-6.A.3 names megacities as a distinct spatial outcome of urbanization without fixing a number, and about ten million is the conventional threshold for this course. The unit measured is the agglomeration -- the continuous built-up area and its population -- rather than an administrative boundary."),

 ("at least about twenty million people",
  "EK PSO-6.A.3 names megacities and metacities together as distinct spatial outcomes of urbanization, and the metacity threshold is conventionally about twice the megacity one. The categories are nested, so the second is a subset of the first rather than a separate kind of place."),

 ("Concentrating tens of millions of people into one continuous built-up area",
  "EK PSO-6.A.3 calls megacities and metacities distinct spatial outcomes of urbanization. The same national rise in urban share can be delivered by dozens of medium cities or by a single enormous agglomeration, and those two produce entirely different geographies."),

 ("Positions in the world economy",
  "EK PSO-6.A.3 places megacities and metacities increasingly in countries of the periphery and semiperiphery, categories drawn from the world-systems framework named in EK SPS-7.E.1. They classify countries by economic position rather than by any physical characteristic."),

 ("fastest in the regions where the urban share was lowest",
  "EK PSO-6.A.3 says these agglomerations are increasingly located in the periphery and semiperiphery, and EK PSO-6.A.2 names population growth and migration among the influences on urbanization. Core countries urbanized earlier, so the great transfers from countryside to city are happening elsewhere now."),

 ("the pressure on that one place's housing, transport and services",
  "EK PSO-6.A.3 calls megacities and metacities distinct SPATIAL outcomes, which is a claim about arrangement rather than about totals. Where the arrangement concentrates, everything that follows population concentrates with it and so does everything that strains under it."),

 ("growth of residential settlement at the edge of a city",
  "EK PSO-6.A.4 names suburbanization among the processes that have created new land-use forms. It redistributes population within an urban area rather than changing how many people are urban, which is exactly what separates it from urbanization."),

 ("consumes a great deal of land per resident",
  "EK PSO-6.A.4 names sprawl among the processes creating new land-use forms and new challenges. The defining features are low density and discontinuity, and car dependence follows from them, since distances become too great to walk and densities too low for frequent transit."),

 ("movement of jobs, retail and services away from the central city",
  "EK PSO-6.A.4 names decentralization alongside suburbanization and sprawl. Suburbanization moves residents outward; decentralization is the broader movement that takes the workplaces and the shops with them, which is why the CED lists the two separately."),

 ("grown up at a major highway junction",
  "EK PSO-6.A.4 names edge cities among the new land-use forms created by suburbanization, sprawl and decentralization. What makes it a form rather than a large suburb is that work and commerce, and not only housing, have relocated there."),

 ("beyond the continuous built-up suburbs",
  "EK PSO-6.A.4 names exurbs among the new land-use forms. The commuting tie is what keeps an exurb part of the metropolitan area rather than a separate rural settlement, while the low density and the distance are what separate it from the suburbs."),

 ("not the largest city of its metropolitan area",
  "EK PSO-6.A.4 names boomburbs among the new land-use forms created by suburbanization and decentralization. The category exists because such places have the population of a city and the form and history of a suburb, a combination no earlier term captured."),

 ("while an exurb is dispersed low-density settlement whose residents commute elsewhere",
  "EK PSO-6.A.4 names both among the new land-use forms, and they differ in what has moved outward. In one case it is the jobs and the shops, in the other only the houses, so an exurb generates commuting while an edge city receives it."),

 ("grown to the population of a substantial city while remaining a suburb in form",
  "EK PSO-6.A.4 names boomburbs among the new land-use forms created by suburbanization, sprawl and decentralization. Scale is the whole of the distinction: the form is suburban and the population is urban, which is the combination that required a new word."),

 ("too few people per route to support frequent public transport",
  "EK PSO-6.A.4 names sprawl among the processes creating new land-use forms and new challenges. Transit needs riders per kilometre of route and walking needs destinations within a few hundred metres, and low density undermines both conditions at once."),

 ("roads, water, sewers and schools across a much larger area",
  "EK PSO-6.A.4 says these processes have created new land-use forms AND new challenges. Infrastructure is priced by length rather than by population, so spreading the same number of people over more ground raises the cost of serving each household."),

 ("can reverse the direction of the daily journey",
  "EK PSO-6.A.4 names decentralization among the processes creating new land-use forms. Once employment has moved outward, the assumption that commuting runs inward stops holding, which is one practical consequence of the edge city as a form."),

 ("where the largest agglomerations shift toward the periphery and semiperiphery",
  "EK PSO-6.A.3 makes a claim about the distribution of the largest cities among countries, which is a global comparison, while EK PSO-6.A.4 describes rearrangement within one urban area. The two sit in a single topic because both are outcomes of urbanization seen at different resolutions."),

 ("reachable from a large surrounding population",
  "EK PSO-6.A.4 names edge cities among the new land-use forms created by decentralization. Accessibility is what a central business district traditionally supplied, and in a car-based metropolitan area a motorway junction supplies a version of it at far lower land cost."),

 ("the existing vocabulary of city, suburb and countryside did not describe them",
  "EK PSO-6.A.4 describes these as NEW land-use forms created by suburbanization, sprawl and decentralization. A place with a downtown's employment and no downtown, or a suburb with a city's population, does not fit categories built for a single-centred city."),

 ("A cluster of office towers and a shopping mall",
  "EK PSO-6.A.4 names edge cities, exurbs and boomburbs as three distinct new land-use forms. Only one pairing here matches a description to the form whose definition it satisfies; each of the others attaches its description to one of the statement's other two categories."),

 ("which is a fact about the agglomeration rather than about any city boundary",
  "EK PSO-6.A.3 names megacities as distinct spatial outcomes of urbanization, and the unit being measured is the agglomeration. A boundary change can alter a municipality's recorded population without one additional person living in the urban area, which is why the agglomeration is the meaningful unit."),

 ("concentration and dispersal at different scales",
  "EK PSO-6.A.3 concerns the size of whole agglomerations while EK PSO-6.A.4 concerns how activity is arranged within an urban area. A metacity that keeps adding millions is also a metacity whose new residents are housed ever further from its centre."),

 ("has been rising, not that none are found in the core",
  "EK PSO-6.A.3 says megacities and metacities are INCREASINGLY located in countries of the periphery and semiperiphery. A statement about a changing share is weaker than one about every case, and reading it as the stronger claim is what leaves a student exposed to a single counterexample."),

 ("Six of the eight are in periphery or semiperiphery countries",
  "Recomputed from the record: two of the eight agglomerations are in core countries and six across the periphery and semiperiphery, and the smallest of the eight is twenty million, so all of them clear the metacity threshold. EK PSO-6.A.3 says megacities and metacities are increasingly located outside the core, and a count is what that claim looks like in a table.",
  ),

 ("from 4.9 to 8.1 million while the central city lost population",
  "Recomputed from the record: the four zones sum to 4.9 million in 1970 and 8.1 million in 2020, and the central city is the only zone to fall. EK PSO-6.A.4 names suburbanization, sprawl and decentralization as processes creating new land-use forms, and this is that redistribution recorded directly.",
  ),

 ("from 31 to 95 percent as density falls",
  "Recomputed from the record: density falls at every step from 9,200 to 210 persons per square kilometre while the car share rises at every step from 31 to 95 percent, so the two move in opposite directions throughout rather than only at the extremes. EK PSO-6.A.4 names sprawl among the processes creating new challenges, and car dependence is what links the density to the challenge.",
  ),

 ("cannot by itself show a trend",
  "EK PSO-6.A.3 says megacities and metacities are INCREASINGLY located in countries of the periphery and semiperiphery, which is a claim about change over time. One column of populations describes a moment, and demonstrating a trend needs the same measurement at two or more dates."),

 ("increasingly outside the core, while within metropolitan areas",
  "EK PSO-6.A.3 supplies the concentration and its shifting location and EK PSO-6.A.4 supplies the outward dispersal and the forms it has created. The two point in opposite directions and hold at the same time, which is why the CED places them in one topic."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.2 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.2 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_where_the_largest_are,
    27: q27_zones_over_time,
    28: q28_density_against_car_use,
}

geo_check.check(g6_2, ANCHORS, TABLE_NOTES)
