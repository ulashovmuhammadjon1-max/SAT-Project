"""Key audit for AP HUMAN GEOGRAPHY 6.3 Cities and Globalization.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. Learning objective PSO-6.B, "Explain how cities embody
processes of globalization", suggested skill 5.B, and two statements:

    PSO-6.B.1 World cities function at the top of the world's urban hierarchy
              and drive globalization.
    PSO-6.B.2 Cities are connected globally by networks and linkages and mediate
              global processes.

THE IDEA THAT MAKES THIS TOPIC HARD is that world-city status is NOT population.
The CED places world cities at the top of the world's urban HIERARCHY, and a
hierarchy of function is not a ranking by size: what lifts a city is the reach of
the decisions taken there and the services supplied from there. A city of twenty
million serving mainly its own country ranks below a city of five million where
global finance is transacted. Items 2, 4, 17 and 27 are built on this, and item
27's table is constructed so that population and world-city standing rank the
four cities in almost exactly OPPOSITE orders. Its recompute asserts that
reversal, because a table where the two agreed would teach the error the item
exists to correct.

"MEDIATE GLOBAL PROCESSES" IS PSO-6.B.2'S HARDEST PHRASE and item 9 asks for it
directly. To mediate is to be the place through which something passes and is
acted on: a global movement of capital, a cultural trend or a supply-chain
decision does not float free but is decided in an office, priced on an exchange,
filmed in a studio. Items 10, 21 and 22 walk that through finance, crisis and
culture in turn.

THE COUNTER-INTUITIVE CONSEQUENCE, items 12 and 28: a world city can be more
tightly connected to world cities on other continents than to medium cities in
its own country. A network is organized by function, not by proximity. Item 28's
record is built so that the MOST DISTANT destination has the most flights, and
its recompute asserts that, since a table in which frequency simply fell with
distance would support the opposite reading.

NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE, the three data items included.
World-city rankings are compiled by particular research groups on particular
criteria and they change; naming a city as top-tier would present one group's
current judgement as a fact, and item 29 keys on exactly that limitation -- an
index is built from chosen indicators weighted in a chosen way.

TWO ANCHORS ARE ON THE FEATURE RATHER THAN THE CATEGORY. Items 25 and 26 have
choices that repeat a category phrase across options, so anchoring on the
category name would have matched a distractor; the anchors are the distinguishing
content instead. That is the anchor check doing its job rather than a workaround.

The three table items (26, 27, 28) are the computational gate:

  26  the leading city is derived on all four measures independently, and the
      verifier asserts the four columns AGREE -- the item's key claims a clean
      lead, which a split verdict would not support
  27  the population ranking and the index ranking are both computed and checked
      to be reversed at the extremes
  28  the two totals are summed and the distance-frequency relationship is
      checked to run the wrong way, which is the item's point

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import re

import geo_check
import g6_3


def q26_leader_on_every_measure(table):
    """The keyed city must lead on all four columns, not on a majority."""
    cities = [r[0] for r in table["rows"]]
    cols = list(zip(*[[float(c.replace(",", "")) for c in r[1:]]
                      for r in table["rows"]]))
    leaders = [cities[list(col).index(max(col))] for col in cols]
    assert len(set(leaders)) == 1, leaders
    assert leaders[0] == "City 1", leaders
    hq = dict(zip(cities, cols[0]))
    index = dict(zip(cities, cols[3]))
    assert hq["City 1"] == 61 and index["City 1"] == 94, (hq, index)
    # And the lead must be clear, not a tie with the runner-up.
    runner = sorted(hq.values())[-2]
    assert hq["City 1"] > runner, hq
    return f"{hq['City 1']:.0f} headquarters"


def q27_size_against_status(table):
    """Population ranking and world-city ranking must be reversed at the ends."""
    pop = {r[0]: float(r[1]) for r in table["rows"]}
    index = {r[0]: float(r[2]) for r in table["rows"]}
    biggest = max(pop, key=pop.get)
    smallest = min(pop, key=pop.get)
    assert index[biggest] == min(index.values()), (pop, index)
    ranked = sorted(index, key=index.get, reverse=True)
    assert ranked[1] == smallest, (pop, index)
    # The two orders must not coincide, or the item teaches the wrong lesson.
    assert sorted(pop, key=pop.get) != sorted(index, key=index.get), (pop, index)
    return "has the lowest world-city index"


def q28_network_beats_proximity(table):
    """Intercontinental links outweigh domestic ones, and distance runs backwards."""
    world, domestic = 0.0, 0.0
    flights = {}
    for dest, kind, n in table["rows"]:
        flights[dest] = float(n.replace(",", ""))
        if kind.startswith("World city"):
            world += float(n)
        else:
            domestic += float(n)
    assert world == 680 and domestic == 225, (world, domestic)
    assert world > domestic, (world, domestic)
    # The most distant destination must have the MOST flights, or the item's
    # point about networks over proximity does not follow from the record.
    assert max(flights, key=flights.get) == "City D", flights
    assert flights["Regional city 2"] == min(flights.values()), flights
    return f"{world:.0f} weekly flights to two world cities"


CLAIMS = [
 ("top of the world's urban hierarchy and drive globalization",
  "EK PSO-6.B.1 states that world cities function at the top of the world's urban hierarchy and drive globalization. Both halves matter: a position in a hierarchy, and an active role in the process rather than a passive exposure to it."),

 ("command point for the world economy",
  "EK PSO-6.B.1 places world cities at the top of the WORLD'S urban hierarchy, which is a functional position rather than a demographic one. What lifts a city into that role is the reach of the decisions taken and the services supplied there."),

 ("ranked by the reach and importance of the functions they perform",
  "EK PSO-6.B.1 uses the phrase 'the world's urban hierarchy'. A hierarchy orders places by the level of function they support, and the level a world city supports is one whose customers, decisions and effects are worldwide."),

 ("a very large city may perform mainly national functions",
  "EK PSO-6.B.1 places world cities at the top of the world's urban HIERARCHY, and a functional hierarchy is not a size ranking. A city of twenty million serving its own country ranks below a city of five million where global finance is transacted."),

 ("depend on face-to-face contact with those clients",
  "EK PSO-6.B.1 says world cities function at the top of the world's urban hierarchy and drive globalization. Specialized services for globally operating firms are the concrete form that function takes, and they cluster because expertise, clients and deal-making all gain from proximity."),

 ("so the process is generated there rather than arriving from outside",
  "EK PSO-6.B.1 says world cities DRIVE globalization, and the verb attributes agency. A decision to open a plant, move capital or acquire a firm is taken in an office in a particular city, and the effects of it then appear in many others."),

 ("Networks and linkages",
  "EK PSO-6.B.2 states that cities are connected globally by networks and linkages and mediate global processes. The term is structural: what matters is the pattern of connections between places rather than the characteristics of any single one."),

 ("Flows of capital, information, people and goods",
  "EK PSO-6.B.2 names networks and linkages without listing them, and these four flows are what actually move between cities. Each leaves a measurable trace -- office networks, data routes, air links, port traffic -- which is what makes global connectivity mappable."),

 ("actually happens in particular offices, exchanges and studios",
  "EK PSO-6.B.2 says cities are connected globally by networks and linkages AND mediate global processes. To mediate is to be the place through which something passes and is acted upon, which is what turns an abstraction like 'global capital' into transactions with addresses."),

 ("since the decision organizing production elsewhere was made there",
  "EK PSO-6.B.1 says world cities function at the top of the world's urban hierarchy and drive globalization. The command function is exactly this: control over activity taking place somewhere else, exercised from a particular office in a particular city."),

 ("record a demand for face-to-face contact between them",
  "EK PSO-6.B.2 says cities are connected globally by networks and linkages. Advanced producer services depend on people meeting, so an airline network is one of the few global flows leaving a public, countable record of where those meetings happen."),

 ("can be stronger than its links within its own national urban system",
  "EK PSO-6.B.2 says cities are connected GLOBALLY by networks and linkages. A network is organized by function rather than by proximity, so two places doing the same specialized work can be more tightly linked than two places that merely lie near each other."),

 ("a local place where people live and a node in a global network",
  "Learning objective PSO-6.B asks how cities EMBODY processes of globalization and EK PSO-6.B.2 describes them as globally connected while remaining particular places. The same trading floor is a workplace in one neighbourhood and a point in a worldwide system, and the topic is about holding both readings together."),

 ("as one market closes and another opens",
  "EK PSO-6.B.2 says cities mediate global processes, and continuous trading is among the clearest examples of mediation. The market has no location of its own; it exists as a relay between particular exchanges in particular cities as the earth turns."),

 ("while production needs labour, land and inputs",
  "EK PSO-6.B.1 says world cities function at the top of the world's urban hierarchy and drive globalization. The separation of command from production is the mechanism by which they do so, since directing an activity and performing it have different location requirements."),

 ("those can be gained or lost as firms, markets and infrastructure move",
  "EK PSO-6.B.1 describes world cities by what they DO rather than by identity. A position defined by function is held only while the function is held, which is why such rankings are recompiled periodically rather than fixed once."),

 ("rather than by the position of the country containing them",
  "EK PSO-6.B.1 places world cities at the top of the WORLD'S urban hierarchy, which ranks cities rather than states. A city concentrating global finance and corporate command performs that function whatever the classification of the country around it."),

 ("and so does the low-paid service work that supports it",
  "EK PSO-6.B.1 says world cities function at the top of the world's urban hierarchy, and that function is carried out by a labour market with two very different halves. The same demand that pays a financial analyst well raises the rent paid by the person who cleans the building."),

 ("headquarters of globally operating firms and of international business-service offices",
  "EK PSO-6.B.1 defines world cities by their position at the top of the world's urban hierarchy, which is a claim about function. Counting the offices from which global decisions are made and global services supplied measures that function directly, whereas population measures something else."),

 ("disproportionately large within its own country's urban system",
  "EK PSO-6.B.1 places world cities at the top of the world's urban hierarchy while EK PSO-6.C.1 names the primate city among the principles explaining the size of cities within a system. One is a claim about global function and the other about national size distribution, and a city can be either, both or neither."),

 ("so a shock travels along the connections that ordinarily carry business",
  "EK PSO-6.B.2 says cities are connected globally by networks and linkages and mediate global processes. The same links that carry capital and information in ordinary times carry a shock, which is why connectivity is a source of vulnerability as well as of advantage."),

 ("much of what circulates worldwide is produced and selected in them",
  "EK PSO-6.B.2 says cities mediate global processes, and cultural circulation is one of them. A film, a campaign or a magazine is commissioned and made somewhere, so the geography of those industries is part of the explanation of what becomes globally familiar."),

 ("a property of the whole structure rather than of the city alone",
  "EK PSO-6.B.2 describes cities as connected globally by networks and linkages. A network is nodes plus the links between them, so two cities with identical populations and industries can occupy completely different positions depending on what each is joined to."),

 ("so its position in that hierarchy falls even if its population does not",
  "EK PSO-6.B.1 defines world cities by the functions they perform at the top of the world's urban hierarchy. A position in a functional hierarchy is held only while the functions are, which is why such a loss registers as a fall in rank with no change in resident population."),

 ("A cluster of headquarters of globally operating firms",
  "EK PSO-6.B.1 places world cities at the top of the world's urban hierarchy by function and EK PSO-6.B.2 describes the networks connecting them. Only one pairing here matches a feature to what it actually evidences; the others substitute size for function or attach a global indicator to a local claim."),

 ("leads on all four measures with 61 headquarters",
  "Recomputed from the record: one city leads on every one of the four measures, with 61 headquarters against 34 for the runner-up and a connectivity index of 94 against 78. The verifier asserts the four columns agree on the leader, since a split verdict would not support the clean lead the key claims.",
  ),

 ("The largest city by population has the lowest world-city index",
  "Recomputed from the record: ranking the four by population gives 21, 14, 8 and 5 million and ranking them by world-city index gives 88, 71, 31 and 22, so the largest city holds the lowest index and the smallest the second highest. EK PSO-6.B.1 places world cities at the top of a FUNCTIONAL hierarchy, which is why a size ranking and a hierarchy ranking need not agree.",
  ),

 ("680 weekly flights to two world cities",
  "Recomputed from the record: the two intercontinental world-city links total 680 weekly flights against 225 for the two domestic destinations, and the most distant destination carries the most flights of all. EK PSO-6.B.2 says cities are connected globally by networks and linkages, and a network organized by function rather than by proximity is exactly what a frequency running against distance shows.",
  ),

 ("weighted in a chosen way",
  "EK PSO-6.B.1 says world cities function at the top of the world's urban hierarchy without specifying how that hierarchy is to be measured. Any index decides what to count and how heavily to weight it, so the ranking it produces is one defensible reading rather than a fact about the cities."),

 ("joined by networks along which global processes travel",
  "EK PSO-6.B.1 supplies the hierarchy and the driving role and EK PSO-6.B.2 supplies the networks and the mediation of global processes. Each rejected summary either strips cities of agency, substitutes size for function, or denies the global reach of the connections."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"6.3 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"6.3 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_leader_on_every_measure,
    27: q27_size_against_status,
    28: q28_network_beats_proximity,
}

geo_check.check(g6_3, ANCHORS, TABLE_NOTES)
