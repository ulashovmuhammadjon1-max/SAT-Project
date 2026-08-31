"""Key audit for AP HUMAN GEOGRAPHY 5.9 The Global System of Agriculture.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-5.E, "Explain the interdependence
among regions of agricultural production and consumption", and three statements:

    PSO-5.E.1 Food and other agricultural products are part of a global supply
              chain.
    PSO-5.E.2 Some countries have become highly dependent on one or more export
              commodities.
    PSO-5.E.3 The main elements of global food distribution networks are affected
              by political relationships, infrastructure, and patterns of world
              trade.

THE OBJECTIVE'S WORD IS INTERDEPENDENCE and it runs both ways: producing regions
depend on consuming regions for income, consuming regions on producing regions
for food they cannot grow. Item 2 keys on both directions. But the dependence is
NOT SYMMETRICAL, and item 18 keys on that separately: a buyer with several
possible suppliers can substitute, while a country whose earnings rest on one
commodity cannot. Interdependence describes the relationship and bargaining power
describes who can leave it, and conflating the two is the commonest error here.

PSO-5.E.2's "SOME COUNTRIES" IS A HEDGE and item 3 keys on it directly, with
"every country" offered as the distractor. NO REAL COUNTRY IS NAMED ANYWHERE IN
THIS MODULE as commodity-dependent. That is deliberate and not squeamishness:
the composition of a country's exports changes, so a claim true when written can
be false when a student reads it, and there is no way for a verifier to catch
that. Both data items use lettered countries for the same reason.

PSO-5.E.3 IS A LIST OF THREE FORCES and the module keeps them apart:

    political relationships  a route closed by a decision (items 9, 22)
    infrastructure           a route closed by the absence of a road, a port or
                             refrigeration (items 10, 20, 21, 24, 28)
    patterns of world trade  tariffs, subsidies, established trading
                             relationships (items 7, 11)

Item 25 requires all three to be told apart at once, which is the skill the
statement's structure asks for. Its ANCHOR is the situation rather than the force
name, because three of the five choices end in the same phrase -- an anchor on
the force would have matched a distractor, which is the check working as
intended.

THE DISTINCTION MOST WORTH TEACHING, and item 23's key: food SECURITY against
food SELF-SUFFICIENCY. A country can be secure without being self-sufficient if
it can reliably buy what it does not grow, and self-sufficient yet insecure if
its own harvest fails. PSO-5.E.1's global chain is what makes the first possible
and PSO-5.E.3's three forces are what make it fragile.

The three table items (26, 27, 28) are the computational gate:

  26  BOTH columns are checked -- the largest commodity's share and the number
      of commodities reaching 80 percent of exports -- since either alone could
      be read as ordinary specialization
  27  the ratio of highest to lowest price, plus an explicit check that the
      series does NOT trend, because two distractors assert a steady rise and a
      steady fall
  28  both infrastructure measures checked to rise while losses fall at every
      step, so the relationship is monotone rather than driven by one pair

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_9


def q26_export_concentration(table):
    """Both columns: the top commodity's share, and how few reach 80 percent."""
    share, count = {}, {}
    for name, top, n in table["rows"]:
        share[name] = float(top)
        count[name] = float(n)
    top_country = max(share, key=share.get)
    assert top_country == "Country W", share
    assert share[top_country] == 71, share
    # The same country must also be the most concentrated on the second measure.
    assert min(count, key=count.get) == top_country, count
    assert count[top_country] == 1, count
    assert max(count.values()) == 24, count
    return f"{share[top_country]:.0f} percent of exports"


def q27_price_volatility(table):
    """Ratio of highest to lowest price, and a check that it does not trend."""
    prices = [float(r[1].replace(",", "")) for r in table["rows"]]
    ratio = max(prices) / min(prices)
    assert ratio > 2.5, (prices, ratio)
    assert max(prices) == 3050 and min(prices) == 1150, prices
    # Two distractors claim a steady rise and a steady fall; neither may be true.
    rising = all(b > a for a, b in zip(prices, prices[1:]))
    falling = all(b < a for a, b in zip(prices, prices[1:]))
    assert not rising and not falling, prices
    return "more than two and a half times the lowest"


def q28_infrastructure_and_losses(table):
    """Both infrastructure measures rise while losses fall at every step."""
    roads = [float(r[1].replace(",", "")) for r in table["rows"]]
    cold = [float(r[2]) for r in table["rows"]]
    loss = [float(r[3]) for r in table["rows"]]
    assert all(b > a for a, b in zip(roads, roads[1:])), roads
    assert all(b > a for a, b in zip(cold, cold[1:])), cold
    assert all(b < a for a, b in zip(loss, loss[1:])), loss
    assert loss[0] == 41 and loss[-1] == 4, loss
    return f"from {loss[0]:.0f} to {loss[-1]:.0f} percent"


CLAIMS = [
 ("part of a global supply chain",
  "EK PSO-5.E.1 states that food and other agricultural products are part of a global supply chain. That is the premise the rest of the topic rests on, since a chain crossing borders is what makes the interdependence named in PSO-5.E worth explaining at all."),

 ("rely on consuming regions for income",
  "Learning objective PSO-5.E asks students to explain the interdependence among regions of agricultural production and consumption. The word carries a claim in both directions at once, so an account of only one side does not answer what the objective asks."),

 ("Some countries have become highly dependent",
  "EK PSO-5.E.2 says SOME countries have become highly dependent on one or more export commodities. Both hedges are real: the claim covers some countries rather than all, and 'have become' describes a condition that arose historically and can change again."),

 ("cuts the country's export earnings with nothing else to offset it",
  "EK PSO-5.E.2 records that some countries have become highly dependent on one or more export commodities. Concentration means national earnings follow one price, and primary commodity prices are among the most volatile in world trade."),

 ("can remove most of the country's export earnings at once",
  "EK PSO-5.E.2 names dependence on one or more export commodities as a condition some countries have reached. A single crop is a single biological system, so one pathogen or one bad season reaches the whole export base rather than a part of it."),

 ("since processing and branding happen in other countries",
  "EK PSO-5.E.1 places agricultural products in a global supply chain and EK PSO-5.E.2 records dependence on export commodities. Exporting an unprocessed commodity means the value added by later stages accrues wherever those stages are, so dependence is a matter of position as well as of price."),

 ("colonial-era specialization",
  "EK PSO-5.E.2 says some countries HAVE BECOME highly dependent, which points at a history rather than a decision taken once. EK PSO-5.E.3 names patterns of world trade among the shaping forces, and an established trading relationship is exactly the kind of pattern that persists."),

 ("infrastructure, and patterns of world trade",
  "EK PSO-5.E.3 names exactly political relationships, infrastructure and patterns of world trade. Climate and soil govern what can be grown, which is EK PSO-5.A.1's subject, whereas this statement concerns what happens to a product once it exists."),

 ("closed by a decision rather than by any physical obstacle",
  "EK PSO-5.E.3 names political relationships first among the forces affecting global food distribution networks. Nothing physical changed in this case, and that is what identifies the force: the route existed throughout and was closed by a choice."),

 ("the physical means of moving and holding the product are missing",
  "EK PSO-5.E.3 names infrastructure among the forces affecting global food distribution networks. A product that exists and cannot move is the clearest case of it, since the failure lies in the network rather than in the growing or in any political decision."),

 ("since the terms on which goods cross borders changed",
  "EK PSO-5.E.3 names patterns of world trade among its three forces. A tariff is a term of trade rather than a road or a diplomatic rupture, and changing it changes which flows are worth making without altering the physical network or the political relationship."),

 ("bear directly on what it can eat",
  "EK PSO-5.E.1 places food in a global supply chain and EK PSO-5.E.3 names the three forces affecting the network that carries it. An importing country's supply travels along that network, so a closure or a bottleneck anywhere on it reaches its shops."),

 ("opposite growing seasons to supply one another",
  "EK PSO-5.E.1 states that food and other agricultural products are part of a global supply chain, and PSO-5.E asks for the interdependence that follows. Opposite hemispheres have opposite seasons, so a chain able to cross the equator turns two seasonal supplies into one continuous one."),

 ("whether the network can move it there and back economically",
  "EK PSO-5.E.1 places agricultural products in a global supply chain and EK PSO-5.E.3 names infrastructure and patterns of world trade among the forces affecting it. Production cost and transport cost together decide whether a distant source can undercut a near one."),

 ("the household that finds a product on a shelf or does not",
  "EK PSO-5.E.1 describes a global chain, EK PSO-5.E.3 names forces acting largely at the national scale, and the consequence appears wherever someone buys food. An account confined to one of those scales leaves out either the cause or the effect."),

 ("raises the price everyone else pays",
  "EK PSO-5.E.1 states that agricultural products are part of a global supply chain and EK PSO-5.E.3 names political relationships among the forces affecting distribution. A world market clears at one price, so a large change in supply is felt by every buyer in that market."),

 ("a disruption anywhere on the chain reaches consumers who have no local alternative",
  "EK PSO-5.E.1 places food in a global supply chain and EK PSO-5.E.3 names three forces able to disrupt it. Specialization is what lowers the cost and it is also what removes the local fallback, so efficiency and vulnerability follow from the same arrangement."),

 ("while the exporter has few alternative sources of earnings",
  "Learning objective PSO-5.E concerns interdependence and EK PSO-5.E.2 records that some countries have become highly dependent on one or more export commodities. Mutual dependence does not imply equal dependence, and the side holding substitutes is the side that can walk away."),

 ("so that earnings rest on more than one price",
  "EK PSO-5.E.2 says some countries HAVE BECOME highly dependent, describing a condition rather than a permanent state. Diversifying export earnings and capturing more stages of the chain both attack the concentration that makes one commodity's price decisive."),

 ("extends the time a perishable product can spend in transit",
  "EK PSO-5.E.3 names infrastructure among the forces affecting global food distribution networks. A perishable product's range is set by how long it stays saleable, so a technology lengthening that window widens the map of who can supply whom."),

 ("use another country's ports",
  "EK PSO-5.E.3 names both infrastructure and political relationships among the forces affecting distribution networks, and a landlocked exporter is exposed to both at once. The extra transit is a cost and depending on a neighbour's willingness is a vulnerability."),

 ("the network carrying it has been reshaped by a political relationship",
  "EK PSO-5.E.3 names political relationships among the forces affecting the main elements of global food distribution networks. This is the pure case: production and demand are untouched and only the route between them has been altered."),

 ("reliable access to enough food by any means",
  "EK PSO-5.E.1's global supply chain is what makes secure access possible without domestic production, and EK PSO-5.E.3's three forces are what make that access fragile. A self-sufficient country whose harvest fails is insecure, and an importing country with reliable suppliers is secure."),

 ("a network's capacity can bind exports",
  "EK PSO-5.E.3 names infrastructure among the forces affecting global food distribution networks. A binding capacity constraint is precisely the case in which crop and buyers both exist and the network between them is what limits the flow."),

 ("A sanctions regime blocking grain shipments",
  "EK PSO-5.E.3 names political relationships, infrastructure and patterns of world trade as three distinct forces. Only one pairing here matches a case to the force whose description it satisfies; each of the others swaps two of the statement's own categories."),

 ("71 percent of exports",
  "Recomputed from the record: one country holds 71 percent of its exports in a single commodity and reaches 80 percent of exports with that one commodity alone, while the others need three, nine and twenty-four to reach the same threshold. EK PSO-5.E.2 says some countries have become highly dependent on one or more export commodities, and both columns measure that concentration.",
  ),

 ("more than two and a half times the lowest",
  "Recomputed from the figures: the price ranges from 1,150 to 3,050 currency units, so the highest is about 2.65 times the lowest, and the verifier also confirms the series neither rises nor falls steadily. EK PSO-5.E.2 records dependence on one or more export commodities, and a swing of that size passes straight through to a dependent country's earnings.",
  ),

 ("Losses fall from 41 to 4 percent",
  "Recomputed from the record: road density and cold storage coverage both rise at every step while harvest losses fall at every step from 41 to 4 percent. EK PSO-5.E.3 names infrastructure among the forces affecting global food distribution networks, and produce that cannot be moved or held is produce that never reaches a market.",
  ),

 ("narrows the explanation without isolating it",
  "EK PSO-5.E.3 names infrastructure alongside political relationships and patterns of world trade, so the framework itself treats distribution as multi-causal. A record in which one named force varies while others also differ supports the reading rather than establishing it."),

 ("some countries' earnings rest on one or two of those products",
  "EK PSO-5.E.1 supplies the chain, EK PSO-5.E.2 the commodity dependence of some countries, and EK PSO-5.E.3 the three forces shaping the network. Each rejected summary either denies one of the three statements or converts PSO-5.E.2's 'some countries' into all of them."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.9 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.9 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_export_concentration,
    27: q27_price_volatility,
    28: q28_infrastructure_and_losses,
}

geo_check.check(g5_9, ANCHORS, TABLE_NOTES)
