"""Key audit for AP HUMAN GEOGRAPHY 6.4 The Size and Distribution of Cities.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-6.C, which names hierarchy,
interdependence, relative size and spacing as the concepts in play, and ONE
essential knowledge statement:

    PSO-6.C.1 Principles that are useful for explaining the distribution and size
              of cities include rank-size rule, the primate city, gravity, and
              Christaller's central place theory.

THE FOUR PRINCIPLES ANSWER FOUR DIFFERENT QUESTIONS and sorting them by question
is what this topic tests. Item 18 and item 25 ask for it directly:

    rank-size rule       how do a country's city SIZES relate to one another?
    the primate city     what does it mean when the largest is far bigger than
                         that relationship predicts?
    gravity              how much INTERACTION should two named places have?
    central place theory why are settlements of different sizes SPACED as they
                         are, and which services will each support?

The first two describe a size distribution, the third predicts a flow between a
specific pair, and the fourth explains a spatial arrangement. A student holding
them as four interchangeable "urban models" picks the wrong one every time, which
is why item 25's distractors each attach a real question to a principle with
nothing to say about it.

THE ARITHMETIC, stated because the CED names the principles and states none of
them. Rank-size: the nth city is the largest divided by n (items 3, 26). Gravity:
interaction is proportional to the product of the populations divided by the
SQUARE of the distance -- squaring is the step students drop, so items 8, 9 and
27 are built on it, and doubling a distance quarters the prediction while
doubling one population only doubles it. Central place theory: THRESHOLD is the
minimum market a service needs and RANGE is how far a customer will travel for
it, so viability is a comparison between the two and neither number is sufficient
alone (items 10, 11, 12, 28).

ALL FOUR ARE HEDGED IN THE CED'S OWN WORDS -- principles "useful for explaining"
-- which is the same hedge attached to von Thunen's model in Topic 5.8. None is a
law and each rests on assumptions no real country satisfies. Items 19, 20, 21 and
29 key on the limits of each in turn, and item 19's key states the productive
reading: a departure from a prediction is information about the country rather
than a refutation of the principle.

ONE ANCHOR IS THE WHOLE PAIRING. Item 25 repeats "answered by gravity" in a
distractor and repeats the trips question in another, so no short anchor is
unique; the anchor is the complete correct pairing. That is the anchor check
working, not a workaround.

SYNONYM CARE. `geo_check` treats {"central place theory", "christaller's model"}
as one construct, so every item names that theory in exactly one way.

NO REAL COUNTRY OR CITY IS NAMED ANYWHERE IN THIS MODULE.

The three table items (26, 27, 28) are the computational gate:

  26  the predicted population is recomputed from the largest city and the rank
      rather than trusted from the column, and every observation is checked
      against it
  27  all four interactions are computed, and the verifier asserts that the pair
      containing the single largest city ranks LAST -- that is the distractor
      the item is built to catch, and it only works if the arithmetic says so
  28  threshold and range are checked to rise together across all five services,
      since the key rests on the ordering rather than on one row

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_4


def q26_rank_size(table):
    """Recompute the prediction from the largest city and the rank."""
    rows = [(float(r[0]), float(r[1]), float(r[2])) for r in table["rows"]]
    largest = [p for rank, p, _ in rows if rank == 1][0]
    assert largest == 8.0, largest
    worst = 0.0
    for rank, observed, stated in rows:
        predicted = largest / rank
        # The column must itself be right, not merely consistent with the key.
        assert abs(predicted - stated) < 0.01, (rank, predicted, stated)
        worst = max(worst, abs(observed - predicted))
    assert worst <= 0.1 + 1e-9, worst
    return "within about 0.1 million"


def q27_gravity(table):
    """Compute all four interactions; the biggest city must NOT win."""
    inter = {}
    pops = {}
    for name, p1, p2, d in table["rows"]:
        a = float(p1.replace(",", ""))
        b = float(p2.replace(",", ""))
        dist = float(d.replace(",", ""))
        pops[name] = max(a, b)
        inter[name] = a * b / (dist ** 2)
    assert inter["Pair A"] == 200 and inter["Pair B"] == 100, inter
    assert inter["Pair C"] == 400 and inter["Pair D"] == 256, inter
    assert max(inter, key=inter.get) == "Pair C", inter
    # The pair holding the single largest city must rank LAST, or the item's
    # main distractor would not be wrong for the reason the key gives.
    biggest_city_pair = max(pops, key=pops.get)
    assert biggest_city_pair == "Pair B", pops
    assert min(inter, key=inter.get) == biggest_city_pair, (inter, pops)
    return (f"predicted interaction of {inter['Pair C']:.0f} exceeds "
            f"Pair D's {inter['Pair D']:.0f}")


def q28_threshold_and_range(table):
    """Threshold and range must rise together across all five services."""
    thresholds = [float(r[1].replace(",", "")) for r in table["rows"]]
    ranges = [float(r[2].replace(",", "")) for r in table["rows"]]
    assert all(b > a for a, b in zip(thresholds, thresholds[1:])), thresholds
    assert all(b > a for a, b in zip(ranges, ranges[1:])), ranges
    lowest = min(thresholds)
    assert lowest == 500, thresholds
    assert table["rows"][thresholds.index(lowest)][0] == "Convenience store"
    # The service with the greatest range must be the one with the greatest
    # threshold, which is why range alone cannot answer the question.
    assert ranges.index(max(ranges)) == thresholds.index(max(thresholds)), (
        thresholds, ranges)
    return f"threshold of {lowest:.0f} customers is the lowest"


CLAIMS = [
 ("The rank-size rule, the primate city, gravity",
  "EK PSO-6.C.1 names exactly the rank-size rule, the primate city, gravity and central place theory. The urban structure models belong to EK PSO-6.D.1 and describe what is inside a city, whereas these four describe how cities relate to one another in size, spacing and interaction."),

 ("about one nth of the largest city's population",
  "EK PSO-6.C.1 names the rank-size rule among the principles explaining the distribution and size of cities. It describes a regular relationship across a whole set of cities rather than a fact about any single one of them."),

 ("About 3 million",
  "The rule gives the nth city the largest city's population divided by n, so nine million divided by three is three million. EK PSO-6.C.1 names the rank-size rule among the principles explaining the size of cities, and dividing by the rank is the whole of the arithmetic."),

 ("disproportionately larger than the second largest",
  "EK PSO-6.C.1 names the primate city among the principles explaining the distribution and size of cities. The definition is comparative: what matters is the ratio to the next city down rather than the absolute population."),

 ("since the largest city is six times the second",
  "The rank-size rule would place the second city near six million and it is two, so the largest is far larger than the distribution predicts. EK PSO-6.C.1 names both the rank-size rule and the primate city, and the second is identified precisely by departure from the first."),

 ("so opportunity and investment are as well",
  "EK PSO-6.C.1 names the primate city among the principles explaining the distribution and size of cities. A city becomes disproportionate because functions accumulate in it, and each function it holds gives people another reason to go there rather than anywhere else."),

 ("falls with the square of the distance between them",
  "EK PSO-6.C.1 names gravity among the principles explaining the distribution and size of cities. It is the only one of the four that predicts a FLOW between two places rather than describing a pattern across many of them."),

 ("one quarter of its previous level",
  "EK PSO-6.C.1 names gravity among the principles explaining the interaction of cities, and the distance term is squared. Squaring is the step students drop, and it is the difference between a prediction that halves and one that falls to a quarter."),

 ("Interaction roughly doubles",
  "EK PSO-6.C.1 names gravity among the principles explaining the interaction of cities. The populations enter as a product and are not squared, so doubling one of them doubles the numerator and therefore doubles the prediction."),

 ("minimum number of customers needed for the service to survive",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities. Threshold is a claim about the market a service requires, which is why a service with a large threshold appears in very few places."),

 ("greatest distance a customer is willing to travel",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities. Range describes how far the service's market extends, so it is a claim about the customer's willingness to travel rather than about the business's requirements."),

 ("must contain at least enough people to meet its threshold",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and its two concepts have to be used together. Threshold states the customers required and range states how far they can be drawn from, so viability is a comparison between them."),

 ("only a settlement drawing on a large enough surrounding population",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and threshold is what sorts services into orders. A specialist service needs a large market and only a few places can assemble one."),

 ("tile a plain completely without overlaps or gaps",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution of cities. A market area is naturally a circle around a centre, but equal circles either overlap or leave gaps, and the hexagon is the shape closest to a circle that covers a plain exactly once."),

 ("fewer and further apart",
  "Learning objective PSO-6.C names spacing among the concepts useful for explaining the distribution of cities and EK PSO-6.C.1 names central place theory. A large threshold requires a large market area, a large market area occupies more ground, and fewer such centres therefore fit into a region."),

 ("smaller places using services in larger ones",
  "Learning objective PSO-6.C names interdependence among the concepts useful for explaining the distribution, size and interaction of cities. A settlement system works as a system precisely because no single place supplies everything its residents need."),

 ("which is what makes a distribution rank-size or primate",
  "Learning objective PSO-6.C names relative size among the concepts useful for explaining the distribution and size of cities. A population of four million means one thing beside a city of eight million and something entirely different beside a city of forty."),

 ("since it predicts interaction between a specific pair of places",
  "EK PSO-6.C.1 names four principles and they answer different questions. Only one of them takes two specific places and returns an expected flow between them, which is what a question about the number of trips requires."),

 ("since the rule is a regularity rather than a law",
  "EK PSO-6.C.1 calls these principles USEFUL FOR EXPLAINING the distribution and size of cities, which is weaker than calling them laws. A colonial history, a recently drawn border or a single dominant capital each produce recognizable departures, and the departure is what points to the cause."),

 ("a border, a language difference or a poor transport link",
  "EK PSO-6.C.1 names gravity among the principles USEFUL FOR EXPLAINING the interaction of cities. Two places of given sizes at a given distance can be separated by a closed border or joined by a fast rail link, and the model as stated sees neither of those."),

 ("flat plain of uniform fertility",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution of cities, and its hexagonal geometry follows from a uniform surface. Terrain, soils, rivers and unequal incomes all distort that pattern, while the behavioural assumptions offered alongside it are far more robust."),

 ("where a set of settlements of different sizes serves a surrounding area",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and its subject is a settlement system with its market areas. That is a regional object: it requires several settlements of different orders and the countryside they serve."),

 ("primacy describes dominance within a national system",
  "EK PSO-6.C.1 names the primate city among the principles explaining size within a system, while EK PSO-6.B.1 places world cities at the top of the WORLD'S urban hierarchy. The two answer different questions, so a city can satisfy either, both or neither."),

 ("a low-threshold service is available locally",
  "EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and this is its characteristic prediction. Bread has a small threshold and a short range while specialist treatment has a large threshold and a long range, so the two are obtained at different levels of the hierarchy."),

 ("How much travel should occur between two named cities, answered by gravity",
  "EK PSO-6.C.1 names four principles that answer four different questions. Only one pairing here matches a question to the principle designed for it, and each of the others attaches a question to a principle with nothing to say about it."),

 ("within about 0.1 million of what the rule predicts",
  "Recomputed from the record: dividing the largest city's 8.0 million by each rank reproduces the predicted column exactly, and every observed figure sits within 0.1 million of its prediction. EK PSO-6.C.1 names the rank-size rule among the principles explaining the size of cities, and this is what a country closely following it looks like.",
  ),

 ("predicted interaction of 400 exceeds Pair D's 256",
  "Recomputed from the record: multiplying the two populations and dividing by the square of the distance gives 200, 100, 400 and 256. The verifier also asserts that the pair containing the single largest city ranks LAST, since that is the distractor the item exists to catch and it is wrong only because the distance term is squared.",
  ),

 ("threshold of 500 customers is the lowest",
  "Recomputed from the record: threshold and range rise together across all five services, from 500 customers and 3 kilometres to 900,000 and 250, and the service with the greatest range is also the one with the greatest threshold. The number of settlements able to support a service falls as its threshold rises, which is central place theory's central prediction.",
  ),

 ("treats every kilometre as equally costly to cross",
  "EK PSO-6.C.1 names gravity among the principles USEFUL FOR EXPLAINING the interaction of cities, which concedes it is not complete. Distance in the formula is physical, while the friction that actually governs movement is political and infrastructural as well as spatial."),

 ("real systems depart from it in informative ways",
  "EK PSO-6.C.1 calls all four principles USEFUL FOR EXPLAINING the distribution and size of cities, the same hedge the CED attaches to von Thunen's model. The internal structure of a city belongs to EK PSO-6.D.1 and a city's site belongs to EK PSO-6.A.1, so neither is what these four are for."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.4 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.4 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_rank_size,
    27: q27_gravity,
    28: q28_threshold_and_range,
}

geo_check.check(g6_4, ANCHORS, TABLE_NOTES)
