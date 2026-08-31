"""Key audit for AP HUMAN GEOGRAPHY 5.7 Spatial Organization of Agriculture.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-5.C, "Explain how economic forces
influence agricultural practices", and the three statements assigned here:

    PSO-5.C.3 Large-scale commercial agricultural operations are replacing small
              family farms.
    PSO-5.C.4 Complex commodity chains link production and consumption of
              agricultural products.
    PSO-5.C.5 Technology has increased economies of scale in the agricultural
              sector and the carrying capacity of the land.

THE THREE STATEMENTS ARE ONE ARGUMENT and reading them as three facts is how the
topic is missed. PSO-5.C.5 supplies the cause: technology raised economies of
scale, so a larger operation now costs less per tonne. PSO-5.C.3 is the
consequence: a commodity producer takes the price rather than setting it, so the
unit-cost gap decides who survives, and large operations displace small family
farms. PSO-5.C.4 describes what the resulting system looks like from the eater's
end -- a long chain of intermediaries between a field and a plate. Items 3, 14,
18 and 30 run that argument, and item 30's distractors each reverse one of its
three directions.

THE TWO TERMS THE CED NAMES WITHOUT DEFINING, supplied here because every key
that uses them depends on the definition:

    economies of scale  the fall in cost PER UNIT as output rises, because large
                        fixed costs are spread over more units. Item 4 keys on
                        "per unit" and item 18 on the fixed-cost mechanism.
    carrying capacity   the population an area can support GIVEN THE TECHNOLOGY
                        IN USE. Item 5 keys on that qualifier, because a student
                        who treats carrying capacity as a fixed natural constant
                        misreads both this statement and Malthus in Unit 2 --
                        which is what item 21 tests.

A COMMODITY CHAIN, since PSO-5.C.4 names one without listing its links: inputs,
production, processing, transport, wholesaling, retailing, consumption. The
geographic content is that these steps occur in DIFFERENT PLACES, so the term
measures the distance between the person who grows food and the person who eats
it. Items 6, 7, 12, 13 and 27 rest on that, and item 8 on where along the chain
the money stops.

WHAT NO ITEM HERE ASSERTS, because the CED does not: that small family farms have
disappeared, that consolidation runs at the same rate in every sector, or that
technology can raise carrying capacity without limit. Items 19, 16 and 21 key
against those three overstatements in turn, and item 16's key says in so many
words that the framework makes a claim about what HAS happened rather than about
what must continue.

The three table items (26, 27, 28) are the computational gate:

  26  the percentage fall in farms, the rise in average size, and the change in
      TOTAL farmland -- the third is what makes the record evidence of
      consolidation rather than of land abandonment, and the verifier also
      checks the table is internally consistent, since farms times average size
      must reproduce the stated total area
  27  the five shares checked to sum to 100, with the growing stage confirmed
      as the minimum and the selling stage as the maximum
  28  costs falling at every step AND the successive savings shrinking, since
      the key asserts diminishing returns to scale and not merely a fall

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g5_7


def q26_consolidation(table):
    """Fewer farms, larger farms, roughly constant total area -- and consistent."""
    years, farms, size, land = [], [], [], []
    for y, f, s, l in table["rows"]:
        years.append(y)
        farms.append(float(f.replace(",", "")))       # thousands
        size.append(float(s.replace(",", "")))        # hectares
        land.append(float(l.replace(",", "")))        # million hectares
    # Internal consistency: thousands of farms x hectares = million hectares.
    for f, s, l in zip(farms, size, land):
        assert abs(f * s / 1000 - l) < 1, (f, s, l)
    assert all(b <= a for a, b in zip(farms, farms[1:])), farms
    assert all(b >= a for a, b in zip(size, size[1:])), size
    decline = 100 * (farms[0] - farms[-1]) / farms[0]
    assert 62 < decline < 64, decline
    land_change = 100 * abs(land[-1] - land[0]) / land[0]
    assert land_change < 15, land_change
    assert size[0] == 86 and size[-1] == 200, size
    return f"about {decline:.0f} percent"


def q27_chain_shares(table):
    """Shares sum to 100; the growing stage is the minimum, selling the maximum."""
    share = {r[0]: float(r[1]) for r in table["rows"]}
    assert sum(share.values()) == 100, share
    assert min(share, key=share.get) == "Farm production", share
    assert max(share, key=share.get) == "Retailing", share
    return (f"retains {share['Farm production']:.0f} percent while retailing "
            f"retains {share['Retailing']:.0f} percent")


def q28_diminishing_scale(table):
    """Unit cost falls at every step, and each further saving is smaller."""
    sizes = [float(r[0].replace(",", "")) for r in table["rows"]]
    costs = [float(r[1].replace(",", "")) for r in table["rows"]]
    assert all(b > a for a, b in zip(sizes, sizes[1:])), sizes
    assert all(b < a for a, b in zip(costs, costs[1:])), costs
    savings = [a - b for a, b in zip(costs, costs[1:])]
    # Diminishing returns: each successive saving is smaller than the last.
    assert all(b < a for a, b in zip(savings, savings[1:])), savings
    assert costs[0] == 265 and costs[-1] == 131, costs
    return f"from {costs[0]:.0f} to {costs[-1]:.0f}"


CLAIMS = [
 ("replaced by large-scale commercial agricultural operations",
  "EK PSO-5.C.3 states that large-scale commercial agricultural operations are replacing small family farms. The direction is one-way in the framework's wording, and the mechanism behind it is the increased economies of scale named in EK PSO-5.C.5."),

 ("link the production and the consumption of agricultural products",
  "EK PSO-5.C.4 states that complex commodity chains link production and consumption of agricultural products. The word 'complex' is doing work: the link runs through many steps in many places rather than directly from a field to a table."),

 ("at a lower cost per tonne",
  "EK PSO-5.C.5 names increased economies of scale and EK PSO-5.C.3 names the replacement that follows from them. A commodity producer takes the market price rather than setting it, so whichever operation has the lower unit cost keeps a margin at a price that leaves the other with none."),

 ("as the scale of production rises",
  "EK PSO-5.C.5 says technology has increased economies of scale in the agricultural sector. The measure is cost PER UNIT rather than total cost, which is why a larger operation can spend far more in total and still produce more cheaply per tonne than a small one."),

 ("depends on the technology in use",
  "EK PSO-5.C.5 pairs economies of scale with carrying capacity as two things technology has raised. Treating carrying capacity as a property of the land alone is precisely what that statement rules out, since one hectare supports very different numbers under different methods."),

 ("inputs, production, processing, transport, wholesaling, retailing",
  "EK PSO-5.C.4 says complex commodity chains link production and consumption of agricultural products. What makes the concept geographic is that its steps happen in different places, so a chain is a description of distance as much as of process."),

 ("complex commodity chains link the production and consumption",
  "EK PSO-5.C.4 names complex commodity chains as the link between production and consumption. Four countries and five stages between the tree and the shopper is exactly the complexity the framework's adjective is carrying."),

 ("processing, distribution and retailing -- rather than with the farmer",
  "EK PSO-5.C.4 describes a complex chain linking production and consumption, and every link takes a margin. The growing stage has many competing suppliers of an interchangeable raw product while the later stages are fewer and hold the brand, so bargaining power sits downstream."),

 ("Vertical integration",
  "EK PSO-5.C.4 describes complex commodity chains linking production and consumption, and owning consecutive links is one response to that complexity. Integration removes the negotiation between stages, which is worth most where timing is tight and quality has to be guaranteed."),

 ("schools, shops and services lose the population that supported them",
  "EK PSO-5.C.3 states that large-scale commercial operations are replacing small family farms, and every farm that disappears was also a household. Rural services depend on the number of people rather than on the number of hectares, so consolidation thins a district even while the land stays in production."),

 ("the grower's decisions are set by the next link",
  "EK PSO-5.C.4 describes complex commodity chains linking production and consumption of agricultural products. Where a downstream firm supplies the inputs and buys the whole output, what to plant and when to harvest are decided at that link, so the chain reaches back into the field."),

 ("under conditions the consumer cannot see or verify",
  "EK PSO-5.C.4 says complex commodity chains link production and consumption, and the link separates as well as connects. Each additional stage puts distance and another firm between the field and the shelf, so what is visible at the point of sale is a package rather than a place."),

 ("a single package may contain output from hundreds of farms",
  "EK PSO-5.C.4 describes the chains as complex, and blending at a processing stage is one form that complexity takes. Once output from many suppliers is pooled, the finished product no longer corresponds to any single field, which is what makes tracing back through it hard."),

 ("output per farm rises faster than the number of farms falls",
  "EK PSO-5.C.3 describes large operations replacing small family farms and EK PSO-5.C.5 attributes rising economies of scale and carrying capacity to technology. Fewer, larger and higher-yielding units is exactly the combination that produces more food from the same ground."),

 ("so it must be stated together with the methods in use",
  "EK PSO-5.C.5 says technology has increased the carrying capacity of the land, which makes the figure a function of method as well as of place. A limit that moves is still a limit, so this is not a claim that population can grow without constraint."),

 ("it says nothing about that process continuing indefinitely",
  "EK PSO-5.C.5 makes a claim about what HAS happened rather than about what must continue. Reading a past increase as an unlimited future one goes beyond the sentence, and it is exactly the move the environmental costs of EK IMP-5.A.1 make questionable."),

 ("the district whose settlement thins",
  "EK PSO-5.C.3 describes a change in the units of production, EK PSO-5.C.4 a chain crossing continents, and EK PSO-5.C.5 the technology behind both. The three statements sit at different scales, so an account confined to one of them misses most of the topic."),

 ("so its cost per hectare falls as the area worked rises",
  "EK PSO-5.C.5 attributes increased economies of scale to technology, and a fixed cost is the mechanism that produces them. The purchase price of a machine is incurred once, so the arithmetic of spreading it favours whoever has the most hectares to spread it over."),

 ("delicate or specialty products keep a place for smaller producers",
  "EK PSO-5.C.3 says large operations are replacing small family farms and EK PSO-5.C.5 gives economies of scale as the reason. Where the scale advantage is small -- hand-picked fruit, a product sold on its particular character -- the pressure the statement describes is correspondingly weaker."),

 ("Competing on something other than cost per tonne",
  "EK PSO-5.C.5 attributes the pressure to economies of scale, which is an advantage in the cost per unit of an identical product. A small producer cannot win that comparison but can decline to make it, which is why survival runs through differentiation rather than through price."),

 ("while this statement records technology raising the number a given area can support",
  "EK PSO-5.C.5 says technology has increased the carrying capacity of the land, which is the historical answer to the mechanism Malthus proposed. It does not settle the argument, since a capacity that has risen is not thereby shown to be capable of rising forever."),

 ("of which the farm itself is one part",
  "EK PSO-5.C.4 describes complex commodity chains linking production and consumption, and the term names the commercial system those chains constitute. Reading agriculture as the farm alone leaves out most of the value in the chain and most of the decisions."),

 ("so they have little bargaining power over price",
  "EK PSO-5.C.4 names complex commodity chains linking production and consumption, and bargaining power depends on how many actors occupy each link. Many identical sellers facing few buyers is the structural position that leaves the growing stage with the thinnest margin."),

 ("whose costs were incurred before the harvest",
  "EK PSO-5.C.4 describes complex commodity chains linking production and consumption. Downstream links can substitute another supplier or another region, while a grower has one crop in one field, which is why weather risk stops where substitution stops."),

 ("with total farmland roughly unchanged",
  "EK PSO-5.C.3 states that large-scale operations are replacing small family farms, which is a claim about the same land being held in fewer and larger units. Fewer farms with a stable total area is exactly that, whereas a rising farm count would contradict the statement outright."),

 ("about 63 percent",
  "Recomputed from the record: farms fall from 5,400 to 2,000 thousand, a decline of about 63 percent, while average size rises from 86 to 200 hectares and total farmland moves by under 15 percent. The verifier also checks the table's internal consistency, since farms multiplied by average size must reproduce the stated total area in every row.",
  ),

 ("retains 8 percent while retailing retains 49 percent",
  "Recomputed from the record: the five shares sum to 100, the smallest belongs to the stage that grows the crop and the largest to the stage that sells it. EK PSO-5.C.4 describes complex chains linking production and consumption, and every additional link is a place where part of the retail price stops.",
  ),

 ("each further increase in size saves less than the one before",
  "Recomputed from the record: cost per tonne falls at every step from 265 to 131, but the successive savings are 75, 42 and 17, so the advantage of further size is shrinking. EK PSO-5.C.5 says technology has increased economies of scale, and a falling unit cost with diminishing gains is what that looks like in figures.",
  ),

 ("but not whether it is decisive",
  "EK PSO-5.C.3 states that large operations are replacing small family farms and EK PSO-5.C.5 supplies economies of scale as a mechanism, but neither says it is the only one. A unit-cost gradient makes that mechanism plausible without ruling out credit, land prices and succession, which operate alongside it."),

 ("which let large operations displace small family farms",
  "EK PSO-5.C.5 supplies the technological cause, EK PSO-5.C.3 the change in the units of production, and EK PSO-5.C.4 the chain linking those units to consumers. Each rejected version reverses one of the three directions the statements set."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.7 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.7 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_consolidation,
    27: q27_chain_shares,
    28: q28_diminishing_scale,
}

geo_check.check(g5_7, ANCHORS, TABLE_NOTES)
