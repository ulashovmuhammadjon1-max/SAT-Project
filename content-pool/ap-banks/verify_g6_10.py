"""Key audit for AP HUMAN GEOGRAPHY 6.10 Challenges of Urban Changes.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-6.A and five essential knowledge
statements -- the largest set in Unit 6:

    SPS-6.A.1 challenges resulting as urban populations move within a city:
              housing and housing discrimination (redlining, blockbusting,
              affordability), access to services, rising crime, environmental
              injustice, and the growth of disamenity zones or zones of
              abandonment
    SPS-6.A.2 squatter settlements and conflicts over land tenure within large
              cities have increased
    SPS-6.A.3 responses can include inclusionary zoning and local food movements
    SPS-6.A.4 urban renewal and gentrification have both positive and negative
              consequences
    SPS-6.A.5 functional and geographic fragmentation of governments presents
              challenges in addressing urban issues

THE FIVE FORM A SEQUENCE and item 30 keys on it: challenges arise, one has grown,
responses exist, the two largest responses cut both ways, and the machinery for
responding is itself divided. The last statement is the reason the third is hard,
which a student holding five separate lists would never see.

HOW THE TWO NAMED DISCRIMINATION PRACTICES ARE HANDLED, and this is the most
carefully bounded part of the module. The CED names redlining and blockbusting,
so items 3 and 4 define them -- a student cannot recognize a practice they cannot
describe. Each definition states the MECHANISM and stops: no real place is named,
no claim is made about where or when either occurred or whether either continues,
and no party is named as having carried either out. What makes each a housing
challenge is structural and needs none of that. Item 26's table follows the same
rule: it records one hypothetical city's grades, refusal rates and value changes
and asserts nothing about any actual place or period.

SPS-6.A.4 IS EXPLICITLY TWO-SIDED, exactly like IMP-6.D.1 in Topic 6.8. Items 15,
16, 17 and 18 hold both halves; item 16 keys the positive consequences and item
17 the negative ones with each other's list as distractors, and item 18's key
states why they are inseparable -- the rising value that funds the improvement is
the same rise that displaces people. Neither a key celebrating gentrification nor
one condemning it would be reporting this statement.

THE ONE ITEM ABOUT RISING CRIME (item 8) is keyed to the geographic content of
the CED's phrase and nothing else: crime is distributed unevenly within a city and
concentrates where the other items on the same list concentrate. No cause is
attributed to any group, which is not squeamishness -- it is that the CED asserts
none, and SOCIAL_BRIEF.md's rule is that a key must trace to the framework.

WORKING DEFINITIONS the CED does not supply, each stated where a key rests on it:
affordability is cost against income rather than absolute price (items 5, 27);
environmental injustice is uneven exposure to hazards (item 7); disamenity zones
and zones of abandonment are what remains where investment and services withdrew
(item 9); land tenure is the recognized right to occupy, which is what a squatter
settlement's conflicts are about (item 11); inclusionary zoning attaches an
affordability condition to permission to build (item 12). Fragmentation is the
one term the CED does define, inside SPS-6.A.5 itself (item 20).

SYNONYM CARE. `geo_check` treats {"squatter settlement", "informal settlement"}
as one construct, so no choice list offers both names.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  refusal rate checked to rise and value growth to fall at EVERY step, since
      the key claims the two run against each other across the whole record
  27  rent as a share of income is computed for all four districts, and the
      verifier asserts that the burden rises while the RENT falls -- the whole
      point of the item, which a table where both moved together would destroy
  28  all three columns checked to rise together, so the record supports a claim
      about fragmentation rather than about any single measure of it

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. The module was drafted with 29 items; the
thirtieth is item 8, added because rising crime is named in SPS-6.A.1 and had no
item, and leaving a listed challenge uncovered would have been a quieter gap than
a short module.
"""
import re

import geo_check
import g6_10

for _n, _item in enumerate(g6_10.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"6.10 q{_n}: `ans` is {_item.get('ans')!r}"


def q26_credit_and_value(table):
    """Refusal rate rises and value growth falls at every step."""
    refused = [float(r[3]) for r in table["rows"]]
    growth = [float(r[4]) for r in table["rows"]]
    grades = [r[1] for r in table["rows"]]
    assert grades == ["A", "B", "C", "D"], grades
    assert all(b > a for a, b in zip(refused, refused[1:])), refused
    assert all(b < a for a, b in zip(growth, growth[1:])), growth
    assert refused[0] == 4 and refused[-1] == 62, refused
    assert growth[0] == 310 and growth[-1] == 9, growth
    return (f"from {refused[0]:.0f} to {refused[-1]:.0f} percent as the assigned "
            f"grade falls")


def q27_rent_burden(table):
    """Burden rises while the RENT itself falls -- that is the item."""
    income = [float(r[1].replace(",", "")) for r in table["rows"]]
    rent = [float(r[2].replace(",", "")) for r in table["rows"]]
    burden = [100 * 12 * r / i for i, r in zip(income, rent)]
    assert all(b < a for a, b in zip(rent, rent[1:])), rent
    assert all(b < a for a, b in zip(income, income[1:])), income
    assert all(b > a for a, b in zip(burden, burden[1:])), burden
    assert 22 < burden[0] < 24, burden
    assert 54 < burden[-1] < 56, burden
    # The cheapest district must be the least affordable, or the key fails.
    assert rent.index(min(rent)) == burden.index(max(burden)), (rent, burden)
    return f"about {burden[-1]:.0f} percent of median income"


def q28_fragmentation(table):
    """All three columns must rise together across the four metropolitan areas."""
    govts = [float(r[1].replace(",", "")) for r in table["rows"]]
    operators = [float(r[2]) for r in table["rows"]]
    years = [float(r[3]) for r in table["rows"]]
    for series in (govts, operators, years):
        assert all(b > a for a, b in zip(series, series[1:])), series
    assert govts[0] == 3 and govts[-1] == 140, govts
    assert years[0] == 6 and years[-1] == 26, years
    return (f"from {years[0]:.0f} years where there are {govts[0]:.0f} governments "
            f"to {years[-1]:.0f} where there are {govts[-1]:.0f}")


CLAIMS = [
 ("The movement of urban populations within a city",
  "EK SPS-6.A.1 begins by saying that AS URBAN POPULATIONS MOVE WITHIN A CITY, economic and social challenges result. The subject is redistribution inside an urban area rather than movement into a country or between countries."),

 ("environmental injustice, and the growth of disamenity zones",
  "EK SPS-6.A.1 names exactly this set of challenges. Suburbanization and sprawl are processes in EK PSO-6.A.4, the design initiatives belong to EK IMP-6.C.1 and the size principles to EK PSO-6.C.1, so each rejected option is drawn from a different statement."),

 ("refusing or restricting mortgage lending and insurance in areas marked out as high risk",
  "EK SPS-6.A.1 names redlining among the housing discrimination issues that result as urban populations move within a city. The mechanism is that the judgement is applied to an AREA rather than to an applicant, so every household is affected by where it lives."),

 ("Persuading owners to sell quickly and cheaply by suggesting",
  "EK SPS-6.A.1 names blockbusting among the housing discrimination issues. The practice works by manufacturing the expectation of a fall in value, since the fear of the fall is what produces the cheap sale it exists to obtain."),

 ("so a cheap dwelling can still be unaffordable to a low-income household",
  "EK SPS-6.A.1 names affordability among the housing issues resulting as urban populations move within a city. Affordability is a ratio rather than a price, which is why the least expensive districts of a city can be its least affordable ones."),

 ("which depends on where those are and how they are reached",
  "EK SPS-6.A.1 names access to services among the challenges resulting as urban populations move within a city. Access is a relationship between a household and a facility, so a city can be well provided overall and still contain districts that reach nothing."),

 ("concentrates where investment, services and stable occupancy have withdrawn",
  "EK SPS-6.A.1 lists rising crime alongside housing issues, access to services and the growth of zones of abandonment, all as consequences of movement within a city. What makes it a geographic item is that it appears in the same districts as the rest of the list."),

 ("uneven exposure of some communities to environmental hazards",
  "EK SPS-6.A.1 names environmental injustice among the challenges resulting as urban populations move within a city. What makes it a justice question rather than merely an environmental one is that the burden and the benefit fall on different communities."),

 ("sometimes beyond effective public control, and areas whose property has been given up",
  "EK SPS-6.A.1 names the growth of disamenity zones or zones of abandonment among the challenges. Both are what remains where investment, services and residents have withdrawn, which is why the statement pairs the two."),

 ("Both have increased",
  "EK SPS-6.A.2 states that squatter settlements and conflicts over land tenure within large cities have increased. The statement pairs them because the second follows from the first: settlement without recognized rights is what a tenure conflict is about."),

 ("without a recognized legal right to it",
  "EK SPS-6.A.2 names squatter settlements AND conflicts over land tenure together, which identifies what the conflict concerns. Without a recognized right a household cannot safely improve its dwelling and a utility has no straightforward basis on which to connect it."),

 ("a share of the dwellings in a new development be affordable",
  "EK SPS-6.A.3 names inclusionary zoning among the responses to economic and social challenges in urban areas. It works by attaching a condition to permission to build, which places affordable dwellings inside new development rather than in a separate district."),

 ("They address access to fresh food in districts that lack it",
  "EK SPS-6.A.3 names local food movements alongside inclusionary zoning as responses, and EK SPS-6.A.1 names access to services among the challenges. Food deserts are the specific access problem such movements address, which is why a food response belongs on this list."),

 ("examples of possible responses rather than a complete or guaranteed list",
  "EK SPS-6.A.3 says responses CAN INCLUDE inclusionary zoning and local food movements, which is illustrative rather than exhaustive. The hedge also stops short of claiming that either response resolves the challenge it addresses."),

 ("Both have positive and negative consequences",
  "EK SPS-6.A.4 states that urban renewal and gentrification have BOTH positive and negative consequences. The framework declines to settle the question, so a module keyed either way would be reporting something other than the statement."),

 ("Buildings repaired, vacant land brought back into use",
  "EK SPS-6.A.4 says urban renewal and gentrification have both positive and negative consequences, and these are the positive side. Investment returning to a district that had lost it repairs the physical stock and restores services, which is a real gain to whoever remains."),

 ("so an established community is dispersed and the businesses serving it close",
  "EK SPS-6.A.4 says urban renewal and gentrification have both positive and negative consequences, and these are the negative side. The same rise in value that funds the repairs is what prices out the households who lived through the decline."),

 ("since the framework asserts both",
  "EK SPS-6.A.4 says urban renewal and gentrification have BOTH positive and negative consequences. The two lists are connected rather than independent, since the rising value paying for the improvement is the same rise that displaces people."),

 ("dispersed between state, county, city and neighbourhood levels",
  "EK SPS-6.A.5 supplies this definition in its own words, glossing the term as the dispersal of agencies and institutions between state, county, city and neighborhood levels. It is one of the few terms the CED defines rather than merely naming."),

 ("must each agree, and none of them is accountable for the whole of it",
  "EK SPS-6.A.5 says fragmentation of governments presents challenges in addressing urban issues. Housing markets, watersheds and labour markets are metropolitan while authority is divided, so the unit that has the problem and the unit that can act on it are different units."),

 ("Responsibility is divided by subject as well as by territory",
  "EK SPS-6.A.5 names functional AND geographic fragmentation. Two authorities can cover the same territory and still be unable to act together because each holds a different subject, which is a second axis of division on top of the boundary one."),

 ("simultaneously the measure of its improvement and the reason existing residents can no longer afford to stay",
  "EK SPS-6.A.1 names affordability among the challenges and EK SPS-6.A.4 says gentrification has both positive and negative consequences. Price is the single variable through which both sets of consequences are transmitted, which is what makes them inseparable."),

 ("Departures reduce the demand and revenue that support services",
  "EK SPS-6.A.1 names the GROWTH of disamenity zones or zones of abandonment among the challenges. The word growth points at a process rather than a state, and a self-reinforcing withdrawal is what that process consists of."),

 ("the metropolitan area, whose divided governments and shared housing market produce it",
  "EK SPS-6.A.1 locates the challenges in movement WITHIN a city and EK SPS-6.A.5 locates the difficulty of responding in governments divided across a metropolitan area. A district-only account misses the cause and a metropolitan-only account misses who bears it."),

 ("Refusing mortgage lending across a whole marked-out neighbourhood, matched to redlining",
  "EK SPS-6.A.1, EK SPS-6.A.2 and EK SPS-6.A.3 name these terms for distinct things. Only one pairing here matches a description to the term the framework uses for it, and each of the others attaches a description to a different named concept."),

 ("from 4 to 62 percent as the assigned grade falls",
  "Recomputed from the record: refusal rates rise at every step from 4 to 62 percent as the assigned grade falls, while forty-year value growth falls at every step from 310 to 9 percent. EK SPS-6.A.1 names redlining among the housing discrimination issues, and a judgement applied to an area rather than an applicant produces exactly this pattern.",
  ),

 ("about 55 percent of median income",
  "Recomputed from the record: annual rent as a share of median income is about 23, 33, 44 and 55 percent across the four districts, so the burden rises as the rent itself falls. EK SPS-6.A.1 names affordability among the housing challenges, and the verifier asserts that the cheapest district is the least affordable one.",
  ),

 ("from 6 years where there are 3 governments to 26 where there are 140",
  "Recomputed from the record: general-purpose governments rise from 3 to 140, transit operators from 1 to 14 and completion time from 6 to 26 years, each at every step. EK SPS-6.A.5 says fragmentation presents challenges in addressing urban issues, and a project crossing more boundaries needs more agreements before it can start.",
  ),

 ("size and fragmentation are difficult to separate",
  "EK SPS-6.A.5 says fragmentation PRESENTS CHALLENGES in addressing urban issues, which is a claim about difficulty rather than a measured effect. Number of jurisdictions and metropolitan scale rise together, so a record showing both cannot attribute the delay to one alone."),

 ("divided government makes any response harder to deliver",
  "EK SPS-6.A.1 supplies the challenges, EK SPS-6.A.2 the growth of one of them, EK SPS-6.A.3 the responses, EK SPS-6.A.4 their two-sidedness and EK SPS-6.A.5 the difficulty of delivering them. The fifth statement is the reason the third is hard, which is the connection a list of five would miss."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.10 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.10 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_credit_and_value,
    27: q27_rent_burden,
    28: q28_fragmentation,
}

geo_check.check(g6_10, ANCHORS, TABLE_NOTES)
