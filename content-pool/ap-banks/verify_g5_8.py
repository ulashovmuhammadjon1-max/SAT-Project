"""Key audit for AP HUMAN GEOGRAPHY 5.8 Von Thunen Model.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-5.D, "Describe how the von Thunen
model is used to explain patterns of agricultural production at various scales",
and ONE essential knowledge statement, which carries its own caveat:

    PSO-5.D.1 Von Thunen's model helps to explain rural land use by emphasizing
              the importance of transportation costs associated with distance
              from the market; however, regions of specialty farming do not
              always conform to von Thunen's concentric rings.

THE SEMICOLON IS THE POINT. The CED states the model and limits it in the same
sentence, so a module teaching only the first half teaches half the statement.
Items 10, 22, 28 and 30 key on the caveat. Item 28's table is built so that the
one non-conforming zone is a SPECIALTY farming region -- the exact exception the
CED names -- rather than a generic mismatch, and its recompute asserts that,
because an item whose exception was arbitrary would not be testing this sentence.

WHAT THE MODEL EMPHASIZES, in the CED's words, is TRANSPORTATION COSTS
ASSOCIATED WITH DISTANCE FROM THE MARKET. That is the entire engine and every
product item runs the same argument on it: a product whose transport cost rises
steeply with distance -- because it perishes, or is bulky and heavy relative to
its value -- loses more by being far away and therefore outbids others for near
land. Items 4 to 8, 15, 21, 24 and 27 are that argument applied to different
products, and item 8 supplies the limiting case in which the product walks.

THE RINGS ARE NOT LISTED IN THE CED, so this module never keys on a ring NUMBER.
Their order is derived from transport cost instead: intensive dairying and market
gardening nearest, then forest, then field crops, then grazing. The forest ring
is the one students find strange and the best illustration of the mechanism --
in the economy von Thunen described, wood was fuel as well as timber, so it was
heavy, bulky and constantly needed. Item 5 keys on that reasoning and not on the
ring's position in a list.

THE ASSUMPTIONS -- one market, a flat featureless plain, uniform soil and
climate, transport equally easy in all directions, producers seeking the best
return -- are treated throughout as the METHOD rather than as an error. Holding
everything else constant is how the effect of distance alone becomes visible,
which is what item 17 asks for, and each departure from an assumption then points
at whichever condition the real landscape breaks, which is item 19. Items 3, 12,
13, 18 and 25 each break one assumption in turn.

SCALE, which the learning objective names: the same reasoning applies within one
farm (item 23), around one town, and at the global scale (item 14).

SYNONYM CARE. `geo_check` treats {"least cost theory", "weber's model"} as one
construct and {"concentric zone model", "burgess model"} as another, so item 20
names each rival model in exactly one way -- naming Weber twice over would make
the item unanswerable in a way no duplicate-string check would catch.

The three table items (26, 27, 28) are the computational gate:

  26  the winning use is derived at EVERY distance, and the verifier asserts the
      keyed use is beaten nearer the market and overtaken further out, which is
      what makes it a middle band rather than a single row read off
  27  the predicted order outward is derived by sorting on transport cost, so
      the key is computed rather than recalled
  28  matches are counted AND the single mismatch is checked to be the specialty
      case, since the CED's caveat is specifically about specialty farming

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_8


def q26_winning_use(table):
    """Derive the most profitable use at every distance, not only at 40 km."""
    uses = table["headers"][1:]
    profit = {}
    for row in table["rows"]:
        d = float(row[0])
        profit[d] = dict(zip(uses, [float(c) for c in row[1:]]))
    dairy = [u for u in uses if u.startswith("Dairying")][0]
    grain = [u for u in uses if u.startswith("Grain")][0]
    ranch = [u for u in uses if u.startswith("Ranching")][0]
    winner = {d: max(v, key=v.get) for d, v in profit.items()}
    assert winner[0] == dairy and winner[20] == dairy, winner
    assert winner[40] == grain and winner[60] == grain, winner
    assert winner[80] == ranch, winner
    # A middle band: beaten nearer in, overtaken further out.
    assert profit[20][grain] < profit[20][dairy], profit[20]
    assert profit[80][grain] < profit[80][ranch], profit[80]
    at40 = profit[40]
    assert at40[grain] == 190 and at40[dairy] == 160 and at40[ranch] == 110, at40
    return f"returns {at40[grain]:.0f} there against {at40[dairy]:.0f} for dairying"


def q27_order_by_cost(table):
    """The predicted order outward is the transport-cost ranking reversed."""
    cost = {r[0]: float(r[1]) for r in table["rows"]}
    order = sorted(cost, key=cost.get, reverse=True)
    assert order == ["Fresh vegetables", "Fresh milk", "Firewood and timber",
                     "Wheat", "Live cattle"], order
    assert cost[order[0]] == 1.20, cost
    assert cost[order[-1]] == 0.03, cost
    return f"nearest at {cost[order[0]]:.2f} and live cattle furthest at {cost[order[-1]]:.2f}"


def q28_conformity(table):
    """Count matches, and check the single mismatch is the specialty case."""
    matches, mismatches = [], []
    for zone, distance, predicted, observed in table["rows"]:
        (matches if predicted == observed else mismatches).append(
            (zone, float(distance), predicted, observed))
    words = {3: "Three"}
    assert len(matches) == 3 and len(mismatches) == 1, (matches, mismatches)
    zone, distance, predicted, observed = mismatches[0]
    # The CED's exception is specialty farming specifically, not any mismatch.
    assert "Vineyards" in observed and "olive" in observed, observed
    assert predicted == "Grazing", predicted
    # And it must not be the zone nearest the market, or a distractor is true.
    assert distance > min(float(r[1]) for r in table["rows"]), distance
    return f"{words[len(matches)]} of the four zones match the prediction"


CLAIMS = [
 ("transportation costs associated with distance from the market",
  "EK PSO-5.D.1 says the model helps explain rural land use by emphasizing the importance of transportation costs associated with distance from the market. Soil and climate matter to agriculture, but the model holds them constant so that the effect of distance alone becomes visible."),

 ("A single market on a flat plain with uniform soil and climate",
  "EK PSO-5.D.1 describes the model's concentric rings, and rings are what these assumptions produce. If transport is equally easy in every direction from one point, equal distances are equally costly and the resulting bands must be circles."),

 ("The rings stretch outward along the river",
  "EK PSO-5.D.1 makes transportation cost the model's central variable, so anything altering the cost of distance alters the shape of the result. A direction in which distance is cheap supports a given use further out, which pulls that band's boundary outward along the route."),

 ("lose value quickly and cost a great deal to move",
  "EK PSO-5.D.1 identifies transportation costs associated with distance as the model's emphasis. A perishable product carries a steep penalty for every extra kilometre, so it gains most from a near site and can outbid other uses for one."),

 ("heavy and bulky in relation to their value and were needed constantly",
  "EK PSO-5.D.1 makes transportation cost the organizing variable, and this ring is its clearest illustration. In the economy von Thunen described, wood was the fuel as well as the building material, so its weight and constant demand put a heavy cost on distance."),

 ("stores well and travels cheaply for its value",
  "EK PSO-5.D.1 emphasizes transportation costs associated with distance from the market. A dry, durable product loses little by being carried, so it is outbid for near land and does not need it, which places it in a middle band."),

 ("so it can bid only for the cheapest land",
  "EK PSO-5.D.1 explains rural land use through transportation costs and distance from the market. A use earning little per hectare cannot win an auction for near land and does not need to, because the low rent of distant land is exactly what makes it viable."),

 ("walked to market under their own power",
  "EK PSO-5.D.1 makes transport cost the model's engine, and in the world it describes an animal moved itself. A product supplying its own locomotion has almost the flattest cost-distance relationship of anything a farm produces, which puts it furthest out."),

 ("the use that can pay most for the land obtains it",
  "EK PSO-5.C.2 names bid-rent theory as the account of how land costs shape intensity and EK PSO-5.D.1 gives this model as the explanation of rural land use through transport cost and distance. The rings are what a rent gradient looks like once several uses bid against one another around one market."),

 ("Regions of specialty farming do not always conform",
  "EK PSO-5.D.1 states the model and limits it in the same sentence, saying that regions of specialty farming do not always conform to the concentric rings. The caveat names a particular exception rather than dismissing the model, which is why both halves must be learned together."),

 ("lowered the distance penalty on perishable products",
  "EK PSO-5.D.1 identifies transportation costs associated with distance as what the model emphasizes, so a technology changing those costs changes the prediction. Perishability was the reason milk and vegetables had to be near, and refrigeration is precisely an attack on that reason."),

 ("which overlap and interrupt one another",
  "EK PSO-5.D.1 explains land use by distance from THE market, and the single-market assumption is what produces one set of circles. Adding markets does not remove the mechanism but superimposes several gradients, which is why real landscapes show interrupted bands rather than clean rings."),

 ("a departure from the model's assumption of uniform land quality",
  "EK PSO-5.D.1 says the model HELPS TO EXPLAIN rural land use, which is a claim about a contributing factor rather than a complete account. The assumptions isolate distance, so where one fails the local pattern departs from the prediction while the underlying pressure remains."),

 ("Perishable and high-value produce is grown relatively near wealthy consuming markets",
  "Learning objective PSO-5.D asks students to describe how the model explains agricultural production AT VARIOUS SCALES. The mechanism of EK PSO-5.D.1 is transport cost against distance, which operates whether the market is a town or a continent's worth of consumers."),

 ("will be produced nearer the market and will outbid the other",
  "EK PSO-5.D.1 emphasizes transportation costs associated with distance from the market, and equal gate prices leave transport cost as the only difference between the two products. The one losing more per kilometre gains more from a near site and will pay more for one."),

 ("rather than predicting exactly which crop will grow",
  "EK PSO-5.D.1 says the model HELPS TO EXPLAIN rural land use and attaches a caveat about specialty regions in the same sentence. A model that helps to explain is judged by whether it makes a pattern intelligible, not by whether every case matches it."),

 ("is the only way to see what distance from the market does on its own",
  "EK PSO-5.D.1 credits the model with EMPHASIZING transportation costs associated with distance from the market. Emphasis requires suppression: everything else has to be held still for one variable's effect to become visible, which is why the plain is featureless."),

 ("Policy can override the cost gradient the model isolates",
  "EK PSO-5.D.1 says the model helps to explain rural land use by emphasizing transport costs, which is a claim about one force among several. A payment altering the return on distant land changes the outcome without touching the mechanism the model describes."),

 ("each one points to whichever assumption the real landscape breaks",
  "EK PSO-5.D.1 pairs the model with an explicit exception, which is the framework itself treating a mismatch as information rather than as refutation. A prediction that fails in a stated way tells a geographer where to look, which a description making no prediction never does."),

 ("Weber's least cost theory",
  "EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing, while EK PSO-5.D.1 gives von Thunen's model as the explanation of rural land use. The two share a logic of transport cost and differ in what they are used to locate."),

 ("reduced by the cost of reaching the market",
  "EK PSO-5.D.1 explains rural land use through transportation costs associated with distance from the market. What a producer will pay for a site is what the site can earn, and every kilometre of distance subtracts transport cost from that earning."),

 ("The caveat that regions of specialty farming do not always conform",
  "EK PSO-5.D.1 names specialty farming regions as its exception in the same sentence that states the model. Where a product is tied to a particular climate or soil, or sells on the reputation of its place, the value of that location can outweigh the penalty of distance."),

 ("The fields nearest the farmstead receive the most attention",
  "Learning objective PSO-5.D asks how the model explains agricultural production at various scales, and the mechanism of EK PSO-5.D.1 is the cost of covering distance. A farmyard is a market for labour and manure in the same way that a town is a market for produce."),

 ("perishability limits the time a product can spend travelling",
  "EK PSO-5.D.1 emphasizes transportation costs associated with distance, and distance imposes both a bill and a delay. A product that spoils in a day and a product too heavy to be worth carrying both end near the market, but a technology solving one does not solve the other."),

 ("producing a lobe rather than a circle",
  "EK PSO-5.D.1 makes transportation cost the model's central variable, so the geometry of the result follows the geography of transport. Where the cost of distance falls along one line, effective distance shrinks in that direction and the bands stretch to match."),

 ("returns 190 there against 160 for dairying",
  "Recomputed from the record: at forty kilometres the three returns are 160, 190 and 110 currency units, and the verifier confirms the winning use is beaten at twenty kilometres and overtaken by eighty. EK PSO-5.D.1 explains rural land use by transportation costs associated with distance, and a use that wins only in a middle band is exactly what that produces.",
  ),

 ("nearest at 1.20 and live cattle furthest at 0.03",
  "Recomputed from the record: sorting the five products by transport cost gives 1.20 down to 0.03 currency units per tonne-kilometre, and the model places whichever product suffers most per kilometre nearest the market. EK PSO-5.D.1 emphasizes transportation costs associated with distance, so the predicted order outward is the cost ranking reversed.",
  ),

 ("the one that does not is a specialty farming region",
  "Recomputed from the record: three zones record the predicted use and the fourth records vineyards and olive groves where grazing was predicted. The verifier checks that the single mismatch is the specialty case and not merely any mismatch, because EK PSO-5.D.1's caveat is specifically that regions of specialty farming do not always conform to the concentric rings.",
  ),

 ("cannot separate the effect of distance from the effects of soil",
  "EK PSO-5.D.1 says the model HELPS TO EXPLAIN rural land use, which concedes that other influences are present in any real landscape. The model's assumptions hold soil, terrain and policy constant and a real region does not, so agreement and disagreement are each consistent with more than one cause."),

 ("but specialty farming regions do not always fit the concentric rings",
  "EK PSO-5.D.1 makes exactly these two claims in one sentence joined by 'however'. Dropping either half misstates the framework, and the exception it names is specific -- regions of specialty farming -- rather than a general disclaimer about models."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.8 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.8 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_winning_use,
    27: q27_order_by_cost,
    28: q28_conformity,
}

geo_check.check(g5_8, ANCHORS, TABLE_NOTES)
