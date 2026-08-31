"""Key audit for AP HUMAN GEOGRAPHY 6.8 Urban Sustainability.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Two learning objectives and one statement each:

    IMP-6.C   Identify the different urban design initiatives and practices.
    IMP-6.C.1 Sustainable design initiatives and zoning practices include mixed
              land use, walkability, transportation-oriented development, and
              smart-growth policies, including New Urbanism, greenbelts, and
              slow-growth cities.
    IMP-6.D   Explain the effects of different urban design initiatives and
              practices.
    IMP-6.D.1 Praise for urban design initiatives includes the reduction of
              sprawl, improved walkability and transportation, improved and
              diverse housing options, improved livability and promotion of
              sustainable options. Criticisms include increased housing costs,
              possible de facto segregation, and the potential loss of historical
              or place character.

IMP-6.D.1 IS THE MOST EXPLICITLY TWO-SIDED STATEMENT IN THE COURSE. It gives a
list of praise and a list of criticisms in one statement, and it hedges the
second list twice: POSSIBLE de facto segregation, POTENTIAL loss of historical or
place character. Both failure modes are live here -- a module teaching only the
praise teaches half the statement, and one asserting the criticisms as
established outcomes overstates the other half. The module is built so neither
can happen: items 10 and 11 take the two lists against each other, items 12 to 15
take the four kinds of praise, items 16 to 18 take the three criticisms, item 19
keys on the framework supplying both, and item 30's distractors are exactly the
two one-sided readings.

ITEM 17 IS THE MOST CAREFULLY WRITTEN IN THE MODULE. The CED's phrase is
"possible de facto segregation" and both qualifiers are load-bearing: de facto
means in fact rather than in law, and "possible" marks it as a risk the framework
records rather than an established result. The key states the PRICE MECHANISM
that produces the outcome and attributes an intention to nobody, which is the
only way to key this item without asserting something the CED does not.

THE SEVEN INITIATIVES in IMP-6.C.1 are defined in the module header because the
CED defines none of them, and items 2 to 8 take one each. Item 24 requires them
to be told apart, and its distractors attach each initiative to the purpose of a
DIFFERENT one on the same list -- which is the real confusion, since a greenbelt
and mixed land use are both on the list and act at different scales on different
problems.

ZONING IS THE INSTRUMENT and item 9 keys on it: the statement says design
initiatives AND ZONING PRACTICES, so most of these work by changing what may
legally be built rather than by building anything.

SYNONYM CARE. `geo_check` treats {"transportation-oriented development",
"transit-oriented development"} as one construct. Every item here uses the CED's
own wording and no choice list contains both forms.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  both trip-share rows checked to sum to 100 in each period, so the record is
      a claim about mode split rather than about trip volume, and one distractor
      asserts they do not
  27  both indices checked to start at 100 and to RISE, since the key's claim is
      that prices rose in both cities and faster in one -- a fall in either
      would support a different reading
  28  the dwelling count is held constant by construction, so the verifier checks
      all three cost measures move together and derives the percentage saving

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_8


def q26_mode_shift(table):
    """Trip shares must sum to 100 in both periods; walking and transit rise."""
    rows = {r[0]: (float(r[1]), float(r[2])) for r in table["rows"]}
    dens_b, dens_a = rows["Dwellings per hectare"]
    dest_b, dest_a = rows["Shops and services within 400 metres"]
    non_car_b, non_car_a = rows["Share of local trips on foot or by transit (%)"]
    car_b, car_a = rows["Share of local trips by car (%)"]
    assert non_car_b + car_b == 100, (non_car_b, car_b)
    assert non_car_a + car_a == 100, (non_car_a, car_a)
    assert dens_a > dens_b and dest_a > dest_b, rows
    assert non_car_a > non_car_b and car_a < car_b, rows
    assert non_car_b == 14 and non_car_a == 46 and car_a == 54, rows
    return f"from {non_car_b:.0f} to {non_car_a:.0f} percent while the car share fell to {car_a:.0f}"


def q27_price_indices(table):
    """Both indices start at 100 and rise; the boundary city rises far more."""
    with_b = [float(r[1].replace(",", "")) for r in table["rows"]]
    without = [float(r[2].replace(",", "")) for r in table["rows"]]
    assert with_b[0] == without[0] == 100, (with_b, without)
    assert all(b > a for a, b in zip(with_b, with_b[1:])), with_b
    assert all(b > a for a, b in zip(without, without[1:])), without
    assert with_b[-1] == 231 and without[-1] == 149, (with_b, without)
    assert (with_b[-1] - with_b[0]) > 2 * (without[-1] - without[0]), (with_b, without)
    return f"an index of {with_b[-1]:.0f} against {without[-1]:.0f}"


def q28_compact_against_sprawl(table):
    """Same dwelling count by construction; all three costs must move together."""
    rows = {r[0]: [float(c.replace(",", "")) for c in r[1:]] for r in table["rows"]}
    low = rows["Low-density expansion"]
    compact = rows["Compact development"]
    land_l, road_l, cost_l = low
    land_c, road_c, cost_c = compact
    assert land_c < land_l and road_c < road_l and cost_c < cost_l, (low, compact)
    assert land_l == 2400 and land_c == 640, (land_l, land_c)
    assert road_l == 620 and road_c == 165, (road_l, road_c)
    saving = 100 * (cost_l - cost_c) / cost_l
    assert 45 < saving < 47, saving
    return f"on {land_c:.0f} hectares against {land_l:,.0f}"


CLAIMS = [
 ("Mixed land use, walkability, transportation-oriented development",
  "EK IMP-6.C.1 names exactly this set of sustainable design initiatives and zoning practices. Redlining and blockbusting are housing discrimination practices in EK SPS-6.A.1, the urban models belong to EK PSO-6.D.1 and the settlement forms to EK PSO-6.A.4."),

 ("rather than separating them into single-purpose zones",
  "EK IMP-6.C.1 names mixed land use among the sustainable design initiatives and zoning practices. Separating uses by zone is what puts every destination beyond walking distance, so mixing them again is the precondition for most of the other initiatives on the list."),

 ("reached on foot safely, directly and pleasantly",
  "EK IMP-6.C.1 names walkability among the sustainable design initiatives. It is a property of the environment rather than of the residents: whether a destination is close, whether the route is safe and whether the walk is worth making are all facts about the place."),

 ("so that the service has riders and the residents have a service",
  "EK IMP-6.C.1 names transportation-oriented development among the sustainable design initiatives and zoning practices. It works on both sides of the transit problem at once, since a service needs density within walking distance and density needs a service to be worth living at."),

 ("Direct new development into areas already served by infrastructure",
  "EK IMP-6.C.1 names smart-growth policies among the sustainable design initiatives and zoning practices. The word 'growth' is in the name: the aim is to direct where growth happens rather than to stop it, which is what separates smart growth from a slow-growth policy."),

 ("connected street grids, short blocks, mixed uses",
  "EK IMP-6.C.1 names New Urbanism among the smart-growth policies. It is a design movement rather than a regulatory one, and its content is a return to the street pattern and mixture of uses that pre-automobile towns had."),

 ("on which building is restricted, limiting the city's outward expansion",
  "EK IMP-6.C.1 names greenbelts among the smart-growth policies. The instrument is a restriction on where building may occur rather than a construction project, which is why it belongs among the ZONING practices the statement names."),

 ("deliberately limits the rate at which it adds housing",
  "EK IMP-6.C.1 names slow-growth cities among the smart-growth policies. The key word is deliberate: a slow-growth city is one whose growth rate is a policy choice, which distinguishes it from a city that simply is not growing."),

 ("the instrument is a rule rather than a building",
  "EK IMP-6.C.1 calls these sustainable design initiatives AND ZONING PRACTICES. Separated single-use zoning is what produced the pattern these initiatives address, so permitting a shop on a residential street is itself the reform in most cases."),

 ("improved and diverse housing options, and improved livability",
  "EK IMP-6.D.1 names exactly this set as praise for urban design initiatives. The rejected set is that same statement's list of CRITICISMS, and since the framework gives both in one sentence, telling the two apart is the whole of this topic's second half."),

 ("possible de facto segregation, and the potential loss of historical or place character",
  "EK IMP-6.D.1 names exactly these three criticisms and hedges two of them -- POSSIBLE de facto segregation and POTENTIAL loss of character. Those hedges are the framework's own and are part of what the statement actually asserts."),

 ("so the same growth occupies less new land",
  "EK IMP-6.D.1 names the reduction of sprawl first among the things praised. Sprawl is low-density outward expansion, so the counter-measure is to raise the density of new building and restrict where it may occur, which greenbelts and smart growth do together."),

 ("Putting destinations within walking distance makes walking useful",
  "EK IMP-6.D.1 names improved walkability and transportation among the things praised and EK IMP-6.C.1 names both initiatives. The two problems have a single solution, since the density that supports a bus route is also the density that puts a shop five minutes away."),

 ("can accommodate households at different stages and incomes",
  "EK IMP-6.D.1 names improved and diverse housing options among the things praised. A district built to a single housing type serves a single kind of household, which is the criticism of single-use, single-type zoning that this praise answers."),

 ("Streets that are pleasant to be in, destinations within reach",
  "EK IMP-6.D.1 names improved livability and promotion of sustainable options among the things praised. Livability concerns the daily experience of a place and sustainability its resource consumption, and the same design changes are credited with both."),

 ("so prices rise from both directions",
  "EK IMP-6.D.1 names increased housing costs among the criticisms. The mechanism is the awkward one: the same measures that make a district worth living in and limit outward expansion act on demand and on supply in the directions that both raise price."),

 ("Separation that results in practice rather than by rule",
  "EK IMP-6.D.1 names POSSIBLE de facto segregation among the criticisms, and both qualifiers matter. 'De facto' means in fact rather than in law, and 'possible' marks it as an outcome the framework treats as a risk rather than as an established result."),

 ("with a pattern that could be anywhere",
  "EK IMP-6.D.1 names the POTENTIAL loss of historical or place character among the criticisms. What distinguishes one district from another is often accumulated and irreplaceable, so a design applied uniformly can improve a place by its own criteria while removing what made it that place."),

 ("so an honest account of their effects has to include both",
  "EK IMP-6.D.1 puts both lists in one statement, and the entries on them are connected rather than independent. Making a district more desirable is simultaneously the achievement being praised and the first step in the price rise being criticized."),

 ("fixes the supply of developable land inside the ring",
  "EK IMP-6.C.1 names greenbelts among the smart-growth policies and EK IMP-6.D.1 names increased housing costs among the criticisms. A greenbelt is a restriction on quantity, and where demand keeps rising against a fixed quantity the adjustment must come through price."),

 ("homes, shops and workplaces stand on the same street",
  "EK IMP-6.C.1 names mixed land use among the sustainable design initiatives and zoning practices. Separation of uses is a rule about what may be built where, and its unavoidable consequence is distance between the things a household needs in one day."),

 ("Density without a service gives residents nothing to use",
  "EK IMP-6.C.1 names transportation-oriented development among the sustainable design initiatives. Each half of the arrangement is what makes the other worthwhile, which is why the initiative is defined by the pairing rather than by either element alone."),

 ("where a greenbelt or growth boundary directs where the whole region may expand",
  "EK IMP-6.C.1's list mixes two scales: mixed land use, walkability and New Urbanism are district-scale design, while greenbelts and slow-growth policies act on a whole region. An initiative at one scale cannot achieve what one at the other does."),

 ("the share of local trips actually made on foot",
  "EK IMP-6.D.1 names improved walkability among the things praised, and walkability is a property of the environment measured by what it makes possible. Destinations within range measure the opportunity and trips on foot measure the take-up, so the two together test the claim."),

 ("A greenbelt, matched to limiting a city's outward expansion",
  "EK IMP-6.C.1 names seven initiatives acting on different problems at different scales. Only one pairing here matches an initiative to what it actually does; each of the others attaches an initiative to the purpose of a different one on the same list."),

 ("from 14 to 46 percent while the car share fell to 54",
  "Recomputed from the record: dwellings per hectare rise from 18 to 47 and destinations within 400 metres from 3 to 21, while the two trip shares sum to 100 in both periods and the non-car share rises from 14 to 46 percent. EK IMP-6.D.1 names improved walkability and transportation among the things praised.",
  ),

 ("an index of 231 against 149",
  "Recomputed from the record: both indices start at 100 and both rise, but the city with a growth boundary reaches 231 against 149, a rise of 131 points against 49. EK IMP-6.D.1 names increased housing costs among the criticisms, and comparison against a city without the policy is what makes the difference attributable rather than merely observed.",
  ),

 ("on 640 hectares against 2,400",
  "Recomputed from the record: both scenarios house 40,000 dwellings, and the compact one uses 640 hectares against 2,400, 165 kilometres of road against 620, and 26,000 currency units per dwelling against 48,000, a saving of about 46 percent. Holding the dwelling count constant is what makes the comparison a fair one.",
  ),

 ("narrows the explanation without isolating it",
  "EK IMP-6.D.1 names increased housing costs among the CRITICISMS of urban design initiatives, which is a claim about an effect. A comparison city is never identical in every other respect, so a difference between the two is consistent with the criticism rather than a demonstration of it."),

 ("records both the benefits claimed for them and the criticisms",
  "EK IMP-6.C.1 supplies the list of initiatives and EK IMP-6.D.1 supplies both the praise and the criticisms in one statement. The two one-sided summaries each drop half of the second statement, and the remaining pair describe EK PSO-6.D.1 and EK PSO-6.C.1 instead."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.8 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.8 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_mode_shift,
    27: q27_price_indices,
    28: q28_compact_against_sprawl,
}

geo_check.check(g6_8, ANCHORS, TABLE_NOTES)
