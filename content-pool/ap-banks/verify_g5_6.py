"""Key audit for AP HUMAN GEOGRAPHY 5.6 Agricultural Production Regions.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-5.C, "Explain how economic forces
influence agricultural practices", and the two statements assigned to this topic:

    PSO-5.C.1 Agricultural production regions are defined by the extent to which
              they reflect subsistence or commercial practices (monocropping or
              monoculture).
    PSO-5.C.2 Intensive and extensive farming practices are determined in part by
              land costs (bid-rent theory).

TWO HEDGES DECIDE THIS MODULE, and both are in the CED's own words.

"THE EXTENT TO WHICH". PSO-5.C.1 does not sort regions into a subsistence box and
a commercial box; it says they are defined by the DEGREE to which they reflect
one or the other. The classification is therefore a spectrum with real cases in
the middle, and a household that eats most of what it grows and sells a modest
surplus is the commonest case in the world. Items 6, 17, 24 and 30 key on this,
and item 17 offers both pure readings as distractors because both are what a
two-box classification would force.

"DETERMINED IN PART BY". PSO-5.C.2 attributes intensity to land costs only
partly, and the concession is real: climate, soil, perishability, labour supply
and policy all bear on it too. Items 11 and 21 key against the stronger reading,
and item 11 asks for the concession directly.

BID-RENT THEORY, since the CED names it without explaining it. Land near a market
is scarce and every user wants it, so its rent is bid up; a user earning a great
deal from each hectare can pay that rent and one earning little cannot. The land
nearest the market therefore goes to the most intensive use, and intensity falls
as rent falls with distance. The mechanism is COMPETITIVE BIDDING and not a rule
about where a crop can grow -- nothing stops wheat growing beside a city, it is
simply outbid there. Item 10 asks for exactly that and item 26 makes it
arithmetic.

THE BOUNDARY WITH TOPIC 5.8. Von Thunen's model is this rent gradient applied to
agricultural land use and it has its own statement, EK PSO-5.D.1. Item 22 marks
the relationship rather than pretending there is none, and no other item in this
module keys on the model's rings.

SYNONYM CARE. `geo_check` treats {"monocropping", "monoculture"} as one
construct, so two choices in one item may not each carry one of them. The CED's
own parenthesis pairs the words, so where the statement is being quoted they
appear together inside a SINGLE choice, which the checker allows and which is
also what the framework actually says.

The three table items (26, 27, 28) are the computational gate:

  26  the winning bidder is derived at EVERY distance, not just at the one the
      question asks about, and the verifier asserts that the keyed use is
      outbid both nearer the market and further from it -- that is what makes
      the item a test of bidding rather than of reading one row
  27  both share columns checked to sum to 100, so the record is a claim about
      destination of output and not about volume
  28  the two columns checked to move in OPPOSITE directions at every step,
      since a single reversal would break the association the key states

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_6


def q26_bid_rent_winner(table):
    """Derive the winning bidder at every distance, not only at 20 km."""
    uses = table["headers"][1:]
    winners = {}
    bids = {}
    for row in table["rows"]:
        d = float(row[0])
        offers = [float(c.replace(",", "")) for c in row[1:]]
        bids[d] = dict(zip(uses, offers))
        winners[d] = uses[offers.index(max(offers))]
    market = [u for u in uses if u.startswith("Market gardening")][0]
    dairy = [u for u in uses if u.startswith("Dairying")][0]
    grain = [u for u in uses if u.startswith("Grain")][0]
    # Intensity falls outward: gardening nearest, dairying next, grain furthest.
    assert winners[0] == market and winners[10] == market, winners
    assert winners[20] == dairy, winners
    assert winners[30] == grain and winners[40] == grain, winners
    # The keyed use must be OUTBID both nearer and further, or the item would
    # not be testing bidding at all.
    assert bids[10][dairy] < bids[10][market], bids[10]
    assert bids[30][dairy] < bids[30][grain], bids[30]
    at20 = bids[20]
    assert at20[dairy] == 380 and at20[grain] == 300 and at20[market] == 200, at20
    return f"bids {at20[dairy]:.0f} there against {at20[grain]:.0f} for grain"


def q27_most_commercial(table):
    """Shares must sum to 100, and the most commercial region is the max sold."""
    sold = {}
    for name, eaten, sell in table["rows"]:
        assert float(eaten) + float(sell) == 100, (name, eaten, sell)
        sold[name] = float(sell)
    top = max(sold, key=sold.get)
    assert top == "Region 4", sold
    assert sold[top] == 97, sold
    assert min(sold.values()) == 12, sold
    return f"sells {sold[top]:.0f} percent of its output"


def q28_diversity_against_sales(table):
    """The two columns must move in opposite directions at every step."""
    crops = [float(r[1]) for r in table["rows"]]
    sold = [float(r[2]) for r in table["rows"]]
    assert all(b < a for a, b in zip(crops, crops[1:])), crops
    assert all(b > a for a, b in zip(sold, sold[1:])), sold
    assert crops[0] == 9 and crops[-1] == 1, crops
    assert sold[0] == 15 and sold[-1] == 97, sold
    return "fall from nine to one"


CLAIMS = [
 ("The extent to which they reflect subsistence or commercial practices",
  "EK PSO-5.C.1 states that agricultural production regions are defined by the extent to which they reflect subsistence or commercial practices. Climate and land division influence what is farmed, but the framework's defining criterion in this topic is economic -- who the output is for."),

 ("primarily to feed the household and community that grows the food",
  "EK PSO-5.C.1 contrasts subsistence with commercial practices as the two poles defining production regions. The distinction concerns the destination of the output rather than the technology used, the size of the holding or the climate it lies in."),

 ("so the household's income rather than its diet depends on the harvest",
  "EK PSO-5.C.1 names commercial practices as one of the two poles. Once output is sold rather than eaten, price, transport cost and market access begin to govern what is planted, which is why learning objective PSO-5.C is about economic forces."),

 ("a single crop, or a very narrow range of crops, across a large area",
  "EK PSO-5.C.1 attaches its parenthesis to commercial practices, and both words in it name the same thing. Specialization of that kind makes sense only when the crop is sold, since a household eating only what it grew could not live on one crop."),

 ("can specialize in whichever one pays best",
  "EK PSO-5.C.1 places monocropping and monoculture beside commercial practices. Selling the harvest converts it into money that will buy anything, which removes the requirement that the farm supply a complete diet and permits specialization in whatever land and market favour."),

 ("The classification is a spectrum",
  "EK PSO-5.C.1's phrase 'the extent to which' is deliberately about degree rather than category. Households that eat most of what they grow and sell a modest surplus are extremely common, and a two-box classification would have nowhere to put them."),

 ("and rent falls with distance from the market",
  "EK PSO-5.C.2 names bid-rent theory as its account of how land costs bear on farming practice. The theory is about competition: a site everyone wants goes to whoever pays most for it, and proximity to a market is the quality being competed for."),

 ("only a high return per hectare can cover a high rent per hectare",
  "EK PSO-5.C.2 says intensive and extensive practices are determined in part by land costs. A hectare that costs a great deal must earn a great deal, and only a use working each hectare hard can do so, which puts the highest intensity where the rent is highest."),

 ("low rents make it affordable to spread modest returns over a large area",
  "EK PSO-5.C.2 attributes the intensive-extensive division in part to land costs. Where a hectare is cheap, a use earning little from each hectare remains viable, and land can substitute for the labour and capital an intensive system would need."),

 ("the site goes to the highest bidder",
  "EK PSO-5.C.2 names bid-rent theory, and bidding is the process the name refers to. Nothing prevents wheat from growing beside a city; a use earning more per hectare simply outbids it there, so the observed pattern is the outcome of an auction rather than of a physical rule."),

 ("labour supply and policy",
  "EK PSO-5.C.2's phrase 'in part' is a genuine hedge rather than a stylistic softening. A rent gradient explains much of where intensity is found, but a frost-free winter, a deep soil or a subsidy can each move a practice away from what rent alone would predict."),

 ("earns enough per hectare near the city to cover the higher rent",
  "EK PSO-5.C.2 attributes the intensive-extensive pattern in part to land costs, and perishability is what makes proximity worth paying for. A product that spoils or loses value in transit has a transport cost rising steeply with distance, which pushes its bid for near land up."),

 ("stores and travels well, so it can afford distance",
  "EK PSO-5.C.2 says land costs partly determine whether a practice is intensive or extensive. A durable crop earning little per hectare loses the bidding for near land and gains nothing from winning it, so it settles where rent is low enough for an extensive system to pay."),

 ("harvesting several times a week for city shops",
  "EK PSO-5.C.2 connects intensity to land costs through bid-rent theory. The use earning most from each hectare each year can offer most for a site, and continuous harvesting of a high-value perishable crop is the highest-earning of the five uses offered."),

 ("most of the output eaten by the household",
  "EK PSO-5.C.1 defines production regions by the extent to which they reflect subsistence or commercial practices. A household eating what it grows must grow a range of things and has little cash for inputs, so crop diversity and low purchased inputs travel together."),

 ("output sold rather than eaten, and reliance on purchased inputs",
  "EK PSO-5.C.1 attaches monocropping and monoculture to commercial practices. Once the harvest is sold the farm's own diet no longer constrains what it plants, and specialization supported by purchased inputs is the arrangement that follows."),

 ("As lying between the two poles",
  "EK PSO-5.C.1's phrase 'the extent to which' makes the classification a matter of degree. A district selling a third of its output is doing both things, and forcing it to either pole would discard exactly the information the framework's wording preserves."),

 ("because everything depends on one crop",
  "EK PSO-5.C.1 names monocropping and monoculture as features of commercial regions, and concentration is what specialization means. Diversity spreads exposure across several markets and several biologies, so removing it raises the return in a good year and the loss in a bad one."),

 ("which lowers cost per unit sold",
  "EK PSO-5.C.1 associates monocropping with commercial practice, and the reason is economic rather than agronomic. Equipment, storage and a buyer relationship built around one crop are all cheaper per tonne than five of each, which is the pressure a farm selling its output faces."),

 ("at the farm scale, where an individual holding sells more or less of what it grows",
  "EK PSO-5.C.1 speaks of production REGIONS, which are areas, while the practice being measured is what an individual farm does with its harvest. A region is more commercial because more of its farms sell more of their output, so the two scales are joined by aggregation."),

 ("so the pattern of uses stretches outward",
  "EK PSO-5.C.2 attributes intensity in part to land costs, and land costs near a market reflect what distant land cannot do. Cheaper transport reduces the penalty of distance, which raises what distant land is worth to a use that previously had to be close."),

 ("producing the concentric arrangement of uses",
  "EK PSO-5.C.2 names bid-rent theory as the account of how land costs shape intensity, and EK PSO-5.D.1 gives von Thunen's model as the explanation of rural land use by transportation costs and distance from market. The second is the first worked out for a farming landscape."),

 ("which is an economic criterion rather than a climatic one",
  "EK PSO-5.C.1 supplies the defining criterion in its own words, and it concerns who the output is for. Climate governs what CAN be grown, which EK PSO-5.A.1 covers in a different topic, but it is not what the framework uses to define a production region."),

 ("largely subsistence with a small commercial element",
  "EK PSO-5.C.1 classifies by the extent to which practices are subsistence or commercial, which permits a mixed reading of exactly this kind. A small cash income is what converts a self-provisioning farm into a household able to obtain goods no farm produces."),

 ("prices set elsewhere and on transport and buyers it does not control",
  "EK PSO-5.C.1 defines the commercial pole by the practice of selling output, and a sale requires a buyer somewhere else. A subsistence household's harvest has the same value to it whatever a distant market does, which is the exposure specialization trades away for higher income."),

 ("which bids 380 there against 300 for grain",
  "Recomputed from the record: at twenty kilometres the three bids are 200, 380 and 300 currency units, and the verifier also confirms that the winning use is outbid at ten kilometres and again at thirty. A use that wins only in a middle band is what bid-rent theory predicts, and EK PSO-5.C.2 names that theory as its account of land costs.",
  ),

 ("which sells 97 percent of its output",
  "Recomputed from the record: the two shares sum to 100 in every row, and the sold share runs from 12 to 39 to 88 to 97 percent, so one region is more commercial than any other on the framework's own criterion. EK PSO-5.C.1 defines production regions by the extent to which they reflect subsistence or commercial practices.",
  ),

 ("crops per farm fall from nine to one",
  "Recomputed from the record: crops per farm fall at every step from nine to one while the share of output sold rises at every step from 15 to 97 percent, so the two measures move in opposite directions throughout. EK PSO-5.C.1 attaches monocropping and monoculture to commercial practices, which is that association expressed as numbers.",
  ),

 ("since the framework defines the distinction by whether output is eaten or sold",
  "EK PSO-5.C.1 defines production regions by the extent to which practices are subsistence or commercial, and puts monocropping in a parenthesis rather than in the definition. Diversity is strongly associated with subsistence without being what the term means, so a crop count supports the reading rather than establishing it."),

 ("and how intensively land is farmed depends partly on what that land costs",
  "EK PSO-5.C.1 supplies the spectrum and its association with monocropping, and EK PSO-5.C.2 supplies the partial role of land costs through bid-rent theory. Every rejected summary drops one of the framework's two hedges -- 'the extent to which' and 'in part'."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.6 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.6 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_bid_rent_winner,
    27: q27_most_commercial,
    28: q28_diversity_against_sales,
}

geo_check.check(g5_6, ANCHORS, TABLE_NOTES)
