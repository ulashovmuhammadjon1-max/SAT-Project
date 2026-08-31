"""Key audit for AP HUMAN GEOGRAPHY 7.2 Economic Sectors and Patterns.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective SPS-7.B and two statements:

    SPS-7.B.1 The different economic sectors -- including primary, secondary,
              tertiary, quaternary, and quinary -- are characterized by distinct
              development patterns.
    SPS-7.B.2 Labor, transportation (including shipping containers), the
              break-of-bulk point, least cost theory, markets, and resources
              influence the location of manufacturing such as core,
              semiperiphery, and periphery locations.

THE FIVE SECTORS are named by the CED and defined by none of it, so the module
header sets out the working definitions and items 2 to 6 take one each. The two
boundaries that actually cost marks are tertiary against quaternary (item 8) --
both are loosely called services, and what separates them is whether the work
delivers a service or produces information -- and quaternary against quinary
(item 9), which is a matter of decision authority rather than of subject.

"DISTINCT DEVELOPMENT PATTERNS" IS THE POINT OF SPS-7.B.1, not the list itself.
The sectors do not merely differ; each dominates at a different stage, which is
what makes sectoral composition a measure of development. Item 7 keys on that and
item 26's table is four economies at four positions on ONE path, with a secondary
share that rises and then falls -- the feature that distinguishes a sequence from
four unrelated cases, and the one its recompute asserts.

SPS-7.B.2 IS SIX LOCATION FACTORS and the module keeps them apart: labour (11),
transportation including shipping containers (12, 21, 28), the break-of-bulk
point (13), least cost theory (14 to 17, 27), markets (18) and resources (19).
Item 25 requires them to be told apart at once.

LEAST COST THEORY is stated in the module header because the CED names it without
stating it, and the consequence students are asked for is the bulk-reducing
against bulk-gaining pair -- items 15 and 16, which are the same reasoning run in
opposite directions. Item 27 makes it arithmetic, and the table is built so the
winning site is CHEAPEST ON NONE of the three components, because minimizing a
sum rather than an input is the whole content of the theory. Item 22 supplies the
limitation: the CED lists least cost theory as one of six influences, which is
the framework's own signal that cost does not exhaust the decision.

SYNONYM CARE. `geo_check` treats {"least cost theory", "weber's model", "weber
model"} as one construct, so every item names it in exactly one way.

NO REAL COUNTRY OR FIRM IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  the rows checked to sum to 100, and the SECONDARY share checked to rise and
      then fall -- a distractor asserts it rises steadily, and the peak is what
      makes the record a development sequence
  27  all three totals computed, and the verifier asserts the winning site leads
      on none of the individual components
  28  cost and time checked to fall together at every step and the cost factor
      derived, since one distractor claims cost merely halved

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g7_2

for _n, _item in enumerate(g7_2.QUESTIONS, 1):
    assert isinstance(_item.get("ans"), int), f"7.2 q{_n}: `ans` is {_item.get('ans')!r}"
    assert 0 <= _item["ans"] < len(_item["choices"]), f"7.2 q{_n}: ans out of range"


def q26_sector_sequence(table):
    """Shares sum to 100; the secondary share must PEAK, not rise steadily."""
    primary = [float(r[1]) for r in table["rows"]]
    secondary = [float(r[2]) for r in table["rows"]]
    higher = [float(r[3]) for r in table["rows"]]
    for p, s, h in zip(primary, secondary, higher):
        assert p + s + h == 100, (p, s, h)
    assert all(b < a for a, b in zip(primary, primary[1:])), primary
    assert all(b > a for a, b in zip(higher, higher[1:])), higher
    assert primary[0] == 58 and primary[-1] == 2, primary
    assert higher[0] == 25 and higher[-1] == 80, higher
    # The peak is what makes this a sequence rather than four separate cases,
    # and a distractor asserts the secondary share rises throughout.
    peak = secondary.index(max(secondary))
    assert 0 < peak < len(secondary) - 1, secondary
    assert secondary[-1] < secondary[peak], secondary
    return f"from {primary[0]:.0f} to {primary[-1]:.0f} percent"


def q27_least_cost_site(table):
    """Totals computed; the winner must lead on none of the components."""
    totals, components = {}, {}
    for name, materials, product, labour in table["rows"]:
        vals = [float(materials), float(product), float(labour)]
        components[name] = vals
        totals[name] = sum(vals)
    assert totals == {"Site A": 180, "Site B": 170, "Site C": 185}, totals
    winner = min(totals, key=totals.get)
    assert winner == "Site B", totals
    # Cheapest on NONE of the three, which is the point of minimizing a sum.
    for i in range(3):
        cheapest = min(components, key=lambda k: components[k][i])
        assert cheapest != winner, (i, components)
    return f"total of {totals[winner]:.0f} is below Site C's {totals['Site C']:.0f}"


def q28_container_costs(table):
    """Cost and time fall together; the cost factor is derived, not asserted."""
    cost = [float(r[1]) for r in table["rows"]]
    days = [float(r[2]) for r in table["rows"]]
    assert all(b < a for a, b in zip(cost, cost[1:])), cost
    assert all(b < a for a, b in zip(days, days[1:])), days
    assert cost[0] == 78 and cost[-1] == 6, cost
    assert days[0] == 45 and days[-1] == 14, days
    # A distractor says cost fell by about half; it fell by far more.
    assert cost[0] / cost[-1] > 10, cost
    return f"from {cost[0]:.0f} to {cost[-1]:.0f} and transit time from {days[0]:.0f} days to {days[-1]:.0f}"


CLAIMS = [
 ("Primary, secondary, tertiary, quaternary, and quinary",
  "EK SPS-7.B.1 names exactly these five and says they are characterized by distinct development patterns. Core, semiperiphery and periphery are positions in the world economy named in EK SPS-7.B.2 and classify places rather than kinds of work."),

 ("Taking materials directly from the earth",
  "EK SPS-7.B.1 names the primary sector first among the five. Everything else in an economy works on what this sector obtains, which is why it comes first in the sequence as well as first in the list."),

 ("Turning raw materials into finished or semi-finished goods",
  "EK SPS-7.B.1 names the secondary sector among the five, and EK SPS-7.B.2 is entirely about the location of MANUFACTURING, which is this sector. Adding value by transforming a material is what the category records."),

 ("Providing services directly to people and businesses",
  "EK SPS-7.B.1 names the tertiary sector among the five. What distinguishes it is that the output is a service performed rather than an object produced, which is why it grows as incomes rise and households buy work as well as goods."),

 ("Producing, processing and interpreting information",
  "EK SPS-7.B.1 names the quaternary sector among the five. It is separated from the tertiary sector by its material: the work produces knowledge rather than delivering a service to a customer in front of it."),

 ("carried out by a very small number of people",
  "EK SPS-7.B.1 names the quinary sector as the last of the five. What defines it is authority rather than subject -- deciding what an organization will do -- which is why it is tiny in employment and disproportionate in effect."),

 ("Each sector dominates employment at a different stage",
  "EK SPS-7.B.1 says the different economic sectors are characterized by distinct development patterns. That is a claim about sequence rather than about definition, and it is what makes a table of sector shares readable as a development measure."),

 ("while quaternary work produces and interprets information",
  "EK SPS-7.B.1 lists tertiary and quaternary as separate sectors. Both sit outside extraction and manufacturing, so the line between them must be drawn on what the work produces, and information is a different output from a service performed."),

 ("carries the authority to decide what an organization will do",
  "EK SPS-7.B.1 names quaternary and quinary as the last two of five sectors. The distinction is one of authority rather than of subject matter, which is why the quinary sector is described as the smallest and highest rather than as a different field."),

 ("the break-of-bulk point, least cost theory, markets, and resources",
  "EK SPS-7.B.2 names exactly this set as influencing the location of manufacturing. The rejected sets belong to the urban topics of Unit 6 and describe where cities are, how they are sized and what is inside them rather than where a factory goes."),

 ("Through what workers cost and through what skills they have",
  "EK SPS-7.B.2 names labor first among the influences on the location of manufacturing. Assembly needing little training follows low wages while production needing particular expertise follows the places that have it, so one word covers two opposite pulls."),

 ("distant low-wage locations became viable suppliers",
  "EK SPS-7.B.2 names transportation INCLUDING SHIPPING CONTAINERS among the influences on manufacturing location, an unusually specific mention. Standardizing the unit of cargo removed most of the handling cost from a sea journey, and what falls when transport falls is the penalty for distance."),

 ("goods are transferred from one mode of transport to another",
  "EK SPS-7.B.2 names the break-of-bulk point among the influences on the location of manufacturing. Handling costs money, so a place where cargo must be handled anyway is a place where processing it as well adds little to the total."),

 ("the combined cost of moving materials in, moving the product out, and labour is lowest",
  "EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing. It treats location as a minimization over costs that vary with place, which is why transport and labour are the terms it works with."),

 ("Near the ore, since moving the heavy raw material is far more expensive",
  "EK SPS-7.B.2 names least cost theory among the influences on manufacturing location, and weight lost in processing is what decides the pull. Carrying material that will be discarded is a cost avoided by discarding it before the journey."),

 ("Near the market, since the finished product is the expensive thing to move",
  "EK SPS-7.B.2 names least cost theory among the influences on manufacturing location, and the logic that pulls a weight-losing industry to its materials pulls a weight-gaining one to its customers. What is expensive to move is what a location is arranged around."),

 ("share suppliers, skilled labour and infrastructure",
  "EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing, and the pull toward clustering belongs to that account. A firm's costs depend on what is around it as well as on what it pays for transport and labour."),

 ("bulky, fragile or urgently needed",
  "EK SPS-7.B.2 names markets among the influences on the location of manufacturing. The market is one end of the journey the product must make, so its position enters the location decision on the same terms as the position of the materials."),

 ("drawn toward its source, since moving it is a large share of total cost",
  "EK SPS-7.B.2 names resources among the influences on manufacturing location and EK SPS-7.A.1 says resource availability facilitated industrialization. The mechanism is identical in both: what is expensive to move is what a location is organized around."),

 ("Positions in the world economy",
  "EK SPS-7.B.2 says these factors influence the location of manufacturing SUCH AS core, semiperiphery and periphery locations, categories from the world-systems framework named in EK SPS-7.E.1. The statement concerns a global division of production rather than sites within one country."),

 ("the wage difference between locations outweighs the cost of shipping",
  "EK SPS-7.B.2 names transportation including shipping containers alongside labor and markets as influences on manufacturing location. Location is a comparison between costs, so reducing one of them to near nothing lets a different one decide the outcome."),

 ("government incentives, trade rules, exchange rates or the pull of existing supplier networks",
  "EK SPS-7.B.2 lists least cost theory as ONE of six influences rather than as the explanation. A model minimizing over transport and labour accounts well for the terms it contains, and the other five entries on the CED's own list mark what it leaves out."),

 ("where production is distributed among core, semiperipheral and peripheral locations",
  "EK SPS-7.B.2 names break-of-bulk points and resources, which are particular places, alongside core, semiperiphery and periphery, which are positions in the world economy. One list of six factors answers a question about a site and a question about a continent."),

 ("Writing software for a research institute, matched to the quaternary sector",
  "EK SPS-7.B.1 names five sectors distinguished by what the work produces. Only one pairing here places an activity in the sector its output belongs to; each of the others moves an activity one or two steps along the CED's own sequence."),

 ("A processing plant built at a port where cargo transfers from ship to rail, matched to the break-of-bulk point",
  "EK SPS-7.B.2 names six distinct influences on the location of manufacturing. Only one pairing here matches a situation to the factor it actually illustrates, and each of the others attaches a case to a different factor on the same list."),

 ("from 58 to 2 percent",
  "Recomputed from the record: each row sums to 100, the primary share falls at every step from 58 to 2 percent and the tertiary and higher share rises at every step from 25 to 80, while the secondary share peaks in the middle at 28 and falls back to 18. EK SPS-7.B.1 says the sectors have distinct development patterns, and that peak is what makes the record a sequence.",
  ),

 ("total of 170 is below Site C's 185",
  "Recomputed from the record: the three components total 180, 170 and 185, and the verifier confirms that the winning site is cheapest on NONE of the three individually. EK SPS-7.B.2 names least cost theory among the influences on manufacturing location, and minimizing a sum rather than an input is exactly what distinguishes it.",
  ),

 ("from 78 to 6 and transit time from 45 days to 14",
  "Recomputed from the record: cost per tonne falls at every step from 78 to 6 currency units, a factor of thirteen, and transit time from 45 to 14 days. EK SPS-7.B.2 names transportation including shipping containers among the influences on manufacturing location, and a fall of that size is what lets a distant wage difference decide a location.",
  ),

 ("makes distant production possible without determining it",
  "EK SPS-7.B.2 names transportation as one of SIX influences on the location of manufacturing. Cheap shipping removes an obstacle rather than supplying a destination, so the record explains why a distant location became possible and not why a particular one was chosen."),

 ("five sectors whose relative size shifts as development proceeds",
  "EK SPS-7.B.1 supplies the five sectors and their distinct development patterns and EK SPS-7.B.2 supplies the six location influences and the three world-economy positions. Each rejected summary shortens one of the two lists or collapses the distinction between a kind of work and a kind of place."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"7.2 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"7.2 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_sector_sequence,
    27: q27_least_cost_site,
    28: q28_container_costs,
}

geo_check.check(g7_2, ANCHORS, TABLE_NOTES)
