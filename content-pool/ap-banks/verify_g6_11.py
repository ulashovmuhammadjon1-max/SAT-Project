"""Key audit for AP HUMAN GEOGRAPHY 6.11 Challenges of Urban Sustainability.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-6.B and two statements:

    SPS-6.B.1 Challenges to urban sustainability include suburban sprawl,
              sanitation, climate change, air and water quality, the large
              ecological footprint of cities, and energy use.
    SPS-6.B.2 Responses to urban sustainability challenges can include regional
              planning efforts, remediation and redevelopment of brownfields,
              establishment of urban growth boundaries, and farmland protection
              policies.

THE OBJECTIVE'S WORD IS EFFECTIVENESS and that is what separates this topic from
a pair of vocabulary lists. SPS-6.B asks students to DESCRIBE THE EFFECTIVENESS
of different attempts, so items 15 to 18 and 22 to 25 evaluate each response
rather than naming it, and item 19 asks why the objective is phrased that way at
all. Every one of those keys states an achievement AND a cost or a displacement
in the same sentence, which is what an honest description of effectiveness looks
like: a growth boundary contains sprawl and restricts land supply, brownfield
redevelopment uses served land and costs more per hectare, regional planning acts
at the right scale and needs agreement from the divided governments of EK
SPS-6.A.5, farmland protection keeps land in production and can push growth past
it. None of that is scepticism about the policies; it is the question the CED
asked.

THE ECOLOGICAL FOOTPRINT IS THE MOST MISREAD ITEM ON THE LIST and three items
handle it. A footprint is the land and water needed to supply what a population
consumes and absorb what it emits, so it is many times a city's own area and lies
mostly outside it -- item 20 and item 28's 138-to-1 ratio. But item 21 keys on
the distinction that follows: SPS-6.B.1 says the footprint OF CITIES is large,
which is a claim about a TOTAL, and per PERSON dense living is lighter on every
measure in item 26's table. A student who reads the statement as "cities are the
problem" has drawn a per-city conclusion from a per-person question, and item
26's recompute asserts both per-person measures fall as density rises so the key
cannot be reached any other way.

A BROWNFIELD is defined in item 12 because the CED names one without defining it:
previously built land, often industrial, whose reuse requires contamination to be
dealt with first. Remediation is the cleaning and redevelopment is what follows,
which is why item 27 prices the two separately.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  density checked to rise while BOTH per-person measures fall, at every
      step -- the key's whole claim is that the two readings of footprint point
      opposite ways
  27  the three cost rows summed for each site type, and the verifier asserts
      the remediation charge alone EXCEEDS the total difference, since that is
      why the key attributes the gap to remediation rather than to land price
  28  the three off-site components summed and the ratio to built-up area
      derived, with the carbon component checked to be the largest, because one
      distractor names food instead

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. One item was written with a malformed token
in place of `ans=0` -- the second time this session, after Topic 6.9 -- and was
caught the same way, by importing the module and asserting every `ans` was
present and in range before any claim was written. That check now runs at the top
of this file too. The lesson is worth stating plainly: a Python module that
imports without error is not thereby a well-formed question bank, and the cheap
assertion catches in one second what reading thirty items might not catch at all.
"""
import re

import geo_check
import g6_11

for _n, _item in enumerate(g6_11.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"6.11 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"6.11 q{_n}: ans out of range"


def q26_density_and_footprint(table):
    """Density rises while BOTH per-person measures fall, at every step."""
    density = [float(r[1].replace(",", "")) for r in table["rows"]]
    footprint = [float(r[2]) for r in table["rows"]]
    energy = [float(r[3]) for r in table["rows"]]
    assert all(b > a for a, b in zip(density, density[1:])), density
    assert all(b < a for a, b in zip(footprint, footprint[1:])), footprint
    assert all(b < a for a, b in zip(energy, energy[1:])), energy
    assert footprint[0] == 6.8 and footprint[-1] == 3.2, footprint
    assert energy[0] == 82 and energy[-1] == 11, energy
    assert density[0] == 900 and density[-1] == 14000, density
    return (f"footprint per person falls from {footprint[0]} to {footprint[-1]} "
            f"and transport energy per person falls from {energy[0]:.0f} to {energy[-1]:.0f}")


def q27_brownfield_costs(table):
    """Totals per site type, and remediation alone exceeds the difference."""
    rows = {r[0]: (float(r[1]), float(r[2])) for r in table["rows"]}
    cost_rows = ["Land acquisition", "Contamination remediation",
                 "New roads, water and sewerage"]
    brown = sum(rows[k][0] for k in cost_rows)
    green = sum(rows[k][1] for k in cost_rows)
    assert abs(brown - 4.5) < 1e-9 and abs(green - 3.0) < 1e-9, (brown, green)
    remediation = rows["Contamination remediation"]
    assert remediation[1] == 0.0, remediation
    # The key attributes the gap to remediation, so remediation must be larger
    # than the whole difference for that attribution to hold.
    assert remediation[0] > (brown - green), (remediation, brown, green)
    farmland = rows["Farmland consumed (hectares)"]
    assert farmland[0] == 0.0 and farmland[1] == 1.0, farmland
    infra = rows["New roads, water and sewerage"]
    assert infra[0] < infra[1], infra
    return f"costs {brown} million against the greenfield site's {green} million"


def q28_footprint_ratio(table):
    """Off-site components summed, ratio derived, carbon confirmed largest."""
    comp = {r[0]: float(r[1].replace(",", "")) for r in table["rows"]}
    built = comp["The city's own built-up area"]
    off_site = {k: v for k, v in comp.items() if k != "The city's own built-up area"}
    total = sum(off_site.values())
    assert total == 46900, total
    ratio = total / built
    assert 137 < ratio < 139, ratio
    largest = max(off_site, key=off_site.get)
    # One distractor names food; the carbon component must in fact be largest.
    assert largest.startswith("Land and sea to absorb"), off_site
    return f"total {total:,.0f} square kilometres, about {ratio:.0f} times"


CLAIMS = [
 ("the large ecological footprint of cities, and energy use",
  "EK SPS-6.B.1 names exactly this set of challenges to urban sustainability. The rejected first alternative is EK SPS-6.B.2's list of RESPONSES to those challenges, which is the distinction this topic's two statements draw and the one an item most easily blurs."),

 ("Regional planning efforts, remediation and redevelopment of brownfields",
  "EK SPS-6.B.2 names exactly these four responses. Inclusionary zoning and local food movements are EK SPS-6.A.3's responses to economic and social challenges, and the design initiatives belong to EK IMP-6.C.1, so each rejected option answers a different statement."),

 ("so it raises the resources each resident needs",
  "EK SPS-6.B.1 names suburban sprawl first among the challenges to urban sustainability. Sustainability is a question about resources per person over time, and low-density outward growth raises the land, energy and infrastructure each household requires."),

 ("Concentrating people concentrates their waste",
  "EK SPS-6.B.1 names sanitation among the challenges to urban sustainability. Density is what makes the problem urban: arrangements that serve a thinly spread population adequately fail entirely once the same number of people are concentrated."),

 ("are also exposed to its effects, including heat, flooding and storms",
  "EK SPS-6.B.1 names climate change among the challenges to urban sustainability. Cities concentrate the energy use and the emissions and they also concentrate the people and property exposed to heat, flood and storm, so they sit on both sides of the problem."),

 ("so pollutants accumulate where the most people are breathing them",
  "EK SPS-6.B.1 names air and water quality among the challenges to urban sustainability. Concentration is the mechanism throughout this list: the same emissions spread over a wide area are a smaller problem than the same emissions released where millions live."),

 ("all reach the same watercourses that supply the city",
  "EK SPS-6.B.1 names air and water quality together among the challenges. A city collects rain from a sealed surface and returns it quickly and dirty, so both the volume and the content of what leaves are altered by the city's presence."),

 ("required to supply what its population consumes and absorb what it emits",
  "EK SPS-6.B.1 names the large ecological footprint of cities among the challenges to urban sustainability. The measure is deliberately not the built area but the productive area a population's consumption requires, which is why a footprint is many times a city's own extent."),

 ("Energy use is the underlying activity",
  "EK SPS-6.B.1 lists energy use alongside climate change and air and water quality. Listing the driver as well as its consequences is what makes reduction a possible response, since a policy can act on how much energy is used rather than only on what its use produces."),

 ("so that land use, transport and growth are settled at the scale the problems actually occupy",
  "EK SPS-6.B.2 names regional planning efforts among the responses to urban sustainability challenges. Sprawl, air quality, watersheds and transport are all metropolitan in scale, so a response confined to one municipality is smaller than the problem it addresses."),

 ("whose reuse first requires contamination in the soil or groundwater to be removed",
  "EK SPS-6.B.2 names remediation and redevelopment of brownfields among the responses. The two words describe two steps: contamination must be dealt with before the site can carry a new use, which is the whole reason such land sits idle."),

 ("A line beyond which urban development is not permitted",
  "EK SPS-6.B.2 names the establishment of urban growth boundaries among the responses to urban sustainability challenges. It is a limit on where building may occur rather than a description of where building currently is, which distinguishes it from a city's own boundary."),

 ("since building on soil is effectively permanent",
  "EK SPS-6.B.2 names farmland protection policies among the responses, and EK IMP-5.B.3 names land use lost to suburbanization among the challenges of feeding a global population. The two statements meet at the metropolitan edge, where the best farmland and the cheapest building land are the same land."),

 ("puts upward pressure on housing prices inside the line",
  "EK SPS-6.B.2 names growth boundaries among the responses and learning objective SPS-6.B asks for their EFFECTIVENESS. The instrument works on the thing it targets, and EK IMP-6.D.1 records increased housing costs among the criticisms, so describing effectiveness means stating both."),

 ("cleaning contaminated ground makes each hectare more expensive",
  "EK SPS-6.B.2 names remediation and redevelopment of brownfields among the responses, and learning objective SPS-6.B asks how effective such attempts are. The land is in the right place and the ground has to be paid for twice, which is why such sites stay idle without a policy to bridge the gap."),

 ("divided among state, county, city and neighbourhood levels",
  "EK SPS-6.B.2 names regional planning efforts among the responses and EK SPS-6.A.5 names functional and geographic fragmentation of governments as a challenge in addressing urban issues. The response operates at the metropolitan scale and the authority to deliver it does not."),

 ("so growth can move past the protected area rather than stopping",
  "EK SPS-6.B.2 names farmland protection policies among the responses and learning objective SPS-6.B asks how effective attempts are. A restriction on one parcel redirects demand rather than extinguishing it, which is why such policies work best alongside a boundary or a regional plan."),

 ("each response achieves some things, costs something and displaces something else",
  "Learning objective SPS-6.B asks students to DESCRIBE THE EFFECTIVENESS of different attempts to address urban sustainability challenges. A list of responses is the input to that question rather than an answer to it, which is what makes this topic an evaluation rather than a vocabulary exercise."),

 ("more than a hundred times its own size",
  "EK SPS-6.B.1 names the large ecological footprint of cities among the challenges. The footprint measures the productive area a population's consumption requires, and the gap between that and a city's own extent is what makes a city a place that lives on other places."),

 ("while the footprint PER PERSON is generally smaller in dense cities",
  "EK SPS-6.B.1 names the large ecological footprint OF CITIES, which is a statement about a total. Shorter journeys, shared walls and shared infrastructure make dense living lighter per person, so the per-capita and per-city readings of one measure point in opposite directions."),

 ("which limits where outward development may occur",
  "EK SPS-6.B.1 names suburban sprawl among the challenges and EK SPS-6.B.2 names growth boundaries among the responses. Sprawl is defined by outward extent, so the instrument acting on outward extent is the one aimed at it."),

 ("makes the expensive remediation of brownfield sites more viable and housing less affordable",
  "Learning objective SPS-6.B asks for the effectiveness of different attempts, which has to be judged across a package rather than one instrument at a time. A higher land price inside a boundary is at once the criticism recorded in EK IMP-6.D.1 and the thing that makes a contaminated site worth cleaning."),

 ("Resource use and emissions per resident over time",
  "Learning objective SPS-6.B asks students to describe the EFFECTIVENESS of attempts to address urban sustainability challenges. A total rises with population whatever a policy achieves, so a per-resident measure is what separates a policy effect from simple growth."),

 ("which change slowly, so most of the effect appears long after the policy is adopted",
  "EK SPS-6.B.2's responses act on where building may occur and on what is built there, and EK IMP-6.A.1 makes those decisions long-lived. A boundary changes the next fifty years of building rather than the existing stock, so an early evaluation measures mostly the period before it took hold."),

 ("Loss of agricultural land at the metropolitan edge, matched to farmland protection policies",
  "EK SPS-6.B.1 names the challenges and EK SPS-6.B.2 the responses, and each response is aimed at a particular problem. Only one pairing here matches a challenge to the instrument designed for it; each of the others attaches a challenge to a different response on the same list."),

 ("footprint per person falls from 6.8 to 3.2",
  "Recomputed from the record: density rises at every step from 900 to 14,000 while footprint per person falls from 6.8 to 3.2 global hectares and transport energy per person from 82 to 11 gigajoules. EK SPS-6.B.1 names the large ecological footprint of cities, and this record is why the per-city and per-person readings of that measure differ.",
  ),

 ("costs 4.5 million against the greenfield site's 3.0 million",
  "Recomputed from the record: the three cost rows total 4.5 million for the brownfield site and 3.0 million for the greenfield one, and the 2.4 million remediation charge is larger than the whole 1.5 million difference, which is what justifies attributing the gap to remediation. EK SPS-6.B.2 names remediation and redevelopment of brownfields among the responses.",
  ),

 ("total 46,900 square kilometres, about 138 times",
  "Recomputed from the record: the three off-site components sum to 46,900 square kilometres against a built-up area of 340, a ratio of about 138 to 1, and the carbon component at 22,400 exceeds the food component at 18,900. EK SPS-6.B.1 names the large ecological footprint of cities, and the ratio is what the word large refers to.",
  ),

 ("so density is not the only thing varying between them",
  "EK SPS-6.B.1 names the large ecological footprint of cities among the challenges without attributing it to a single variable. A footprint responds to what a population consumes as well as to how it is arranged, so a density gradient narrows the explanation without isolating it."),

 ("what it achieves, what it costs and what it displaces rather than on being adopted",
  "EK SPS-6.B.1 supplies the challenges, EK SPS-6.B.2 the responses with the hedge CAN INCLUDE, and learning objective SPS-6.B asks for their effectiveness. Adopting a policy and achieving an outcome are different things, which is exactly what the objective's verb insists on."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.11 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.11 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_density_and_footprint,
    27: q27_brownfield_costs,
    28: q28_footprint_ratio,
}

geo_check.check(g6_11, ANCHORS, TABLE_NOTES)
