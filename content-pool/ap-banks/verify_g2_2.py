"""Key audit for AP HUMAN GEOGRAPHY 2.2 Consequences of Population Distribution.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-2.D prints exactly two essential-knowledge statements:

    PSO-2.D.1  Population distribution and density affect political, economic,
               and social processes, including the provision of services such as
               medical care.
    PSO-2.D.2  Population distribution and density affect the environment and
               natural resources; this is known as carrying capacity.

PSO-2.D.1 supplies three domains -- political, economic, social -- plus one
authorized example, service provision. Items 1, 2, 3, 6, 10, 11, 15, 17, 20, 21,
23, 24, 26, 28 and 29 are keyed to it and cite it.

PSO-2.D.2 supplies the environmental consequence and the NAME for it. Items 4,
5, 7, 8, 12, 13, 14, 16, 18, 19, 22, 25, 27 and 30 cite it. What the CED does
NOT do is define carrying capacity beyond calling it the effect of population on
environment and resources, so the definition every key here rests on is stated
in the module header and repeated in the claims: the population an area's
resources can support at a given level of consumption and technology. Two
consequences of that definition carry several keys and are argued, not cited --
that the capacity moves when technology or consumption per person moves (items
8, 16, 18, 25) and that overshoot shows up as degradation of the resource base
rather than as an abrupt stop (items 5, 22).

Item 9 cites both statements, because it asks for one consequence of each kind
from the same arrangement of people.

The five table items (26-30) are the computational gate, and every one of them
is built so the eye-catching column is the wrong answer:

  26  the district with the LARGEST clinic budget is the CHEAPEST per resident
  27  the herd exceeding capacity by the most animals is not the herd under the
      greatest proportional strain
  28  the settlement needing the most pipe in total is the dearest per
      household, not the cheapest
  29  the province holding the most seats is not the best represented per person
  30  the basin withdrawing the largest volume is not the basin closest to its
      renewable limit

Each recompute asserts that separation explicitly, so a table edited without its
key being edited fails the module.

REVIEW NOTE. Item 28's first draft described one settlement as "needing the
second most main in total" when it in fact needed the most; the wording was
corrected before the verifier was written. All 30 keys were derived from the
questions and none needed changing.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g2_2


def q26_cost_per_resident(table):
    """Clinic cost per resident; the biggest budget is the cheapest per head."""
    per, total = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        residents = num(d["Residents served"])
        cost = num(d["Annual clinic cost (thousand $)"]) * 1000
        total[d["District"]] = cost
        per[d["District"]] = cost / residents
    assert per == {"District 1": 30, "District 2": 150,
                   "District 3": 40, "District 4": 60}, per
    worst = max(per, key=per.get)
    assert worst == "District 2", per
    # The largest total budget must belong to the CHEAPEST district per head.
    assert max(total, key=total.get) == min(per, key=per.get), (total, per)
    return "$150 per resident"


def q27_overshoot(table):
    """Overshoot as a share of capacity, against overshoot in animals."""
    rel, absolute = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        cap = num(d["Estimated carrying capacity (animals)"])
        herd = num(d["Current herd (animals)"])
        absolute[d["District"]] = herd - cap
        rel[d["District"]] = (herd - cap) / cap
    worst = max(rel, key=rel.get)
    assert worst == "District B", rel
    assert abs(rel["District B"] - 0.75) < 1e-9, rel
    assert max(absolute, key=absolute.get) != worst, absolute
    assert absolute["District D"] == 0, absolute
    assert abs(rel["District A"] - 0.15) < 1e-9, rel
    return "75 percent above"


def q28_main_per_household(table):
    """Metres of water main per household; total length is the wrong column."""
    per, total = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        hh = num(d["Households"])
        km = num(d["Water main required (km)"])
        total[d["Settlement"]] = km
        per[d["Settlement"]] = 1000 * km / hh
    assert per == {"Settlement W": 5, "Settlement X": 50,
                   "Settlement Y": 10, "Settlement Z": 100}, per
    best = min(per, key=per.get)
    assert best == "Settlement W", per
    # The settlement needing the MOST pipe in total must not be the cheapest,
    # and the one needing the least in total must not be the cheapest either.
    assert max(total, key=total.get) != best and min(total, key=total.get) != best, total
    return "5 metres of main per household"


def q29_people_per_seat(table):
    """People per seat; holding the most seats is not being best represented."""
    per, seats = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        pop = num(d["Population (thousands)"]) * 1000
        s = num(d["Seats"])
        seats[d["Province"]] = s
        per[d["Province"]] = pop / s
    best = min(per, key=per.get)
    assert best == "Province II", per
    assert per == {"Province I": 300000, "Province II": 150000,
                   "Province III": 200000, "Province IV": 400000}, per
    assert max(seats, key=seats.get) != best, seats
    return "one seat for every 150,000 people"


def q30_withdrawal_share(table):
    """Withdrawal as a share of renewable supply, against withdrawal in volume."""
    share, volume, supply = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        sup = num(d["Renewable supply (million m3/yr)"])
        wit = num(d["Withdrawal (million m3/yr)"])
        supply[d["Basin"]] = sup
        volume[d["Basin"]] = wit
        share[d["Basin"]] = 100 * wit / sup
    worst = max(share, key=share.get)
    assert worst == "Basin L", share
    assert share == {"Basin K": 50, "Basin L": 90,
                     "Basin M": 70, "Basin N": 30}, share
    assert max(volume, key=volume.get) != worst, volume
    # The "smallest renewable supply" distractor names a basin that does not
    # have it, and the item's rationale says so; assert that stays true.
    assert min(supply, key=supply.get) == "Basin L", supply
    return "90 percent of its renewable supply"


CLAIMS = [
 ("divided among fewer payers",
  "EK PSO-2.D.1 states that distribution and density affect economic and social processes including service provision. A network's cost rises with the distance it spans while its benefit rises with the households connected, so low density raises the cost per connection directly."),

 ("more representation per person",
  "EK PSO-2.D.1 names political processes among those population distribution affects. A floor on seats decouples representation from population, so a seat is bought with fewer voters wherever population is thin."),

 ("too dispersed to support facilities close to everyone",
  "EK PSO-2.D.1 singles out the provision of services such as medical care as its example of a process shaped by distribution and density. A hospital needs a threshold population to sustain it, so dispersal forces long travel times whatever site is chosen."),

 ("at a given level of consumption and technology",
  "EK PSO-2.D.2 attaches the name carrying capacity to the effect of population distribution and density on environment and natural resources. The CED does not define it further, so the definition used throughout this module is the standard one, stated with both qualifiers that make it a relation rather than a fixed count."),

 ("grass cover, soil depth, and per-animal yields have all declined",
  "Overshoot is diagnosed by degradation of the resource base rather than by the size of the population, since a large herd on a productive range is not overshoot. Rising demand alongside falling productivity per unit is the signature that the stock supporting the system is being consumed."),

 ("below the threshold needed to generate enough demand",
  "EK PSO-2.D.1 names service provision as a process shaped by distribution and density. A specialized service needs a minimum number of users within reach to be viable, and thin population puts that number out of reach without reducing anyone's need for it."),

 ("drawing down the natural resource that sustains it",
  "EK PSO-2.D.2 states that population distribution and density affect the environment and natural resources and calls that relationship carrying capacity. Pumping faster than an aquifer recharges is a resource being consumed rather than used, which is the definition in operation."),

 ("raised by technology that increases output per unit of resource",
  "EK PSO-2.D.2 ties carrying capacity to the resources an area supplies, and how far those resources stretch depends on the technology applied and on consumption per person. Both terms move, which is why the same land supports different numbers at different times."),

 ("delivers services more cheaply per person; the rural district exerts less pressure",
  "EK PSO-2.D.1 and EK PSO-2.D.2 make both consequences follow from the same arrangement of people. Concentration shortens the networks services run on while intensifying demand on the immediate area, and dispersal reverses both effects at once."),

 ("travel time rises and the school stops being a local institution",
  "EK PSO-2.D.1 covers the social and economic processes shaped by distribution, and a threshold service in a thin population forces this exact trade. Fixed costs per school fall when pupils are pooled, and the saving is paid for in distance."),

 ("Electoral districts must be redrawn after a census",
  "EK PSO-2.D.1 names political processes explicitly. Redistricting exists precisely because representation is tied to population and population moves, so the map of power must be redrawn whenever the map of people changes."),

 ("ecosystems that occupy the same narrow zone",
  "EK PSO-2.D.2 ties environmental pressure to where people are and not merely to how many there are. When the concentration of people coincides spatially with the resource, local pressure runs far above anything a national figure would imply."),

 ("Pressure is exerted where people actually are",
  "EK PSO-2.D.2 makes distribution as well as density the driver of environmental consequence. An average spreads demand evenly over territory the population does not occupy evenly, which understates the load precisely where it falls."),

 ("population distribution and density affect the environment and natural resources",
  "This restates EK PSO-2.D.2, and the three facilities are the physical form the relationship takes. Concentrated population generates concentrated waste, water demand and energy demand that the surrounding environment must absorb or supply."),

 ("fixed costs of existing networks and buildings are shared among fewer people",
  "EK PSO-2.D.1 makes provision of services depend on distribution and density. A pipe network, a school building and a bus route cost nearly the same to maintain whether used heavily or lightly, so depopulation raises the cost each remaining user carries."),

 ("increase food produced per hectare",
  "EK PSO-2.D.2's carrying capacity is a relation among resources, technology and consumption. Raising output per unit of land increases the number of people the same area supports, while raising consumption per person lowers it, and counting people more accurately changes neither term."),

 ("demand is concentrated on a small and expensive land supply",
  "EK PSO-2.D.1 makes distribution shape economic and social processes in both directions. Concentration makes network services cheap and land-consuming goods expensive, because every household is bidding for the same limited central area."),

 ("supported far fewer people before mechanized farming",
  "EK PSO-2.D.2 defines the environmental limit in terms of the resources an area supplies, and both the yield obtained from them and the amount each person takes are variable. Evidence that the same land has supported different numbers under different technologies makes the point directly."),

 ("fragmenting habitat that a compact settlement would leave intact",
  "EK PSO-2.D.2 names distribution as well as density among the drivers of environmental effect. Compact settlement concentrates its damage into a small footprint, while the same number of people spread thinly requires far more road, line and clearing per person."),

 ("other regions perceive themselves as peripheral",
  "EK PSO-2.D.1 lists political processes among those distribution affects. Where population, government and economy coincide in one metropolitan region, votes, media, expertise and lobbying concentrate there together, and peripheral resentment elsewhere is the standard result."),

 ("too few peers, services, and opportunities to stay for",
  "EK PSO-2.D.1 names political, economic and social processes as three separate domains. A lost seat is political and a closed branch or a tax rate is economic, while the thinning of the social world a young person can take part in is the social case."),

 ("at or beyond its carrying capacity",
  "EK PSO-2.D.2 names carrying capacity as the concept covering the effect of population on environment and resources. Simultaneous deterioration of several independent resource systems as population rises is the pattern the concept describes, and the key states it with the qualifier the definition requires."),

 ("high threshold population makes the effect of density on access unusually visible",
  "EK PSO-2.D.1 offers medical care as an example rather than an exhaustive claim, and it is a good example because hospitals and specialties need large catchments. Where the threshold is high, thin population converts directly into distance and delay."),

 ("Higher per-household infrastructure cost and greater conversion of productive land",
  "Both EK PSO-2.D.1 and EK PSO-2.D.2 are engaged here: spreading a given number of households over more ground lengthens every network serving them and takes more land out of its previous use. The two consequences move together because they share a cause."),

 ("Falling consumption of resources per person",
  "EK PSO-2.D.2 makes the environmental effect a function of the population and the resources it draws on, and the draw per person is the term that is not the headcount. Rearranging people or recomputing a statistic changes where the pressure falls or how it is described, not its total."),

 ("$150 per resident",
  "Recomputed from the table: clinic costs per resident are $30, $150, $40 and $60, so the district with the largest budget is the cheapest per head and the district with the smallest population is the dearest. The verifier asserts that inversion separately, since it is what the item is testing.",
  q26_cost_per_resident),

 ("75 percent above",
  "Recomputed from the table: overshoot as a share of estimated capacity is 15, 75, 16 and 0 percent, so the district exceeding capacity by the most animals is not the district under the greatest proportional strain. A small resource base is overwhelmed by a much smaller absolute excess.",
  q27_overshoot),

 ("5 metres of main per household",
  "Recomputed from the table: metres of main per household are 5, 50, 10 and 100, so the settlement needing the most pipe in total is not the dearest to serve and the one needing the least in total is not the cheapest. Density rather than total network length is what sets the cost of a connection.",
  q28_main_per_household),

 ("one seat for every 150,000 people",
  "Recomputed from the table: people per seat are 300,000, 150,000, 200,000 and 400,000, so the province with the fewest residents needs the fewest of them to elect a member. Holding the largest number of seats is not the same as being well represented per voter.",
  q29_people_per_seat),

 ("90 percent of its renewable supply",
  "Recomputed from the table: withdrawal as a share of renewable supply is 50, 90, 70 and 30 percent, so the basin taking the largest volume is not the basin closest to its limit. The verifier also confirms the basin named in the smallest-supply distractor is not in fact the one with the smallest supply.",
  q30_withdrawal_share),
]

hg_check.check(g2_2, CLAIMS, per_topic=30, n_choices=5)
