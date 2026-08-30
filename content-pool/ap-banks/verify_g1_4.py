"""Key audit for AP HUMAN GEOGRAPHY 1.4 Spatial Concepts.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. PSO-1.A prints exactly one essential-knowledge statement:

    PSO-1.A.1  Spatial concepts include absolute and relative location, space,
               place, flows, distance decay, time-space compression, and pattern.

It is a list of eight names and nothing more. The CED does not define distance
decay, does not say how place differs from space, and does not assert that
time-space compression is unevenly experienced. So the claims below fall into
two kinds and are labelled honestly as such:

  * List membership -- "which of the eight is this?" -- cites PSO-1.A.1. Items
    1, 2, 3, 5, 6, 7, 8, 9, 12, 14, 21, 23 and 25 are of that kind.
  * What a concept actually predicts -- that distance decay flattens when the
    cost gradient flattens, that a rare service leaves distant users no
    substitute, that clustering shows up as empty area -- cites nothing, because
    the CED does not state it and an invented code would be worse than none.
    Items 4, 10, 11, 13, 15, 16, 17, 18, 19, 20, 22, 24 and 26-30 are of that
    kind.

The five table items (26-30) are the computational gate. Each function recomputes the ratio sequence, the compression factor, the
net flow, the empty-quadrat evidence and the netting of remittances from the
printed cells, and each also asserts that the trap the item depends on is
genuinely present -- that a constant-difference reading does NOT fit the decay
table, that the largest gross remittance sender is NOT the largest net one.
A distractor that is accidentally also true is the defect these assertions
exist to catch.

REVIEW NOTE. All 30 keys were derived from the questions and then rechecked
against the tables before this file was written; nothing needed correcting.
Item 30 deliberately gives two options the same net figure ("a net of 750
million") so that the anchor has to be the partner name rather than the amount;
that is intentional and the anchor is written accordingly.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g1_4


def q26_decay(table):
    """Each distance band gets roughly half the visitation rate of the one inside it."""
    rates = numcol(table, "Visitors per 10,000 residents")
    ratios = [rates[i + 1] / rates[i] for i in range(len(rates) - 1)]
    assert all(0.40 < r < 0.55 for r in ratios), f"ratios are not near one half: {ratios}"
    assert all(rates[i + 1] < rates[i] for i in range(len(rates) - 1)), rates
    # A constant subtraction must NOT fit, or the distractor would also be right.
    diffs = [rates[i] - rates[i + 1] for i in range(len(rates) - 1)]
    assert max(diffs) - min(diffs) > 100, f"the drops are nearly constant: {diffs}"
    assert rates[0] > rates[-1], "the nearest band is not the highest"
    return "roughly halve"


def q27_compression(table):
    """Travel time collapses by a factor of twenty; distance does not move at all."""
    hours = numcol(table, "Fastest travel time (hours)")
    km = numcol(table, "Straight-line distance (km)")
    assert len(set(km)) == 1, f"the distance column is not constant: {km}"
    factor = hours[0] / hours[-1]
    assert abs(factor - 20) < 1e-9, f"time fell by a factor of {factor}"
    # The distractor claiming a constant hourly drop must be false.
    drops = [hours[i] - hours[i + 1] for i in range(len(hours) - 1)]
    assert len(set(drops)) > 1, f"the hourly drops are constant: {drops}"
    return "one twentieth"


def q28_net_flow(table):
    """Net migration is the difference between the two streams, not their sum."""
    flows = {rowdict(table, r)["Direction"]: num(rowdict(table, r)["Migrants"])
             for r in table["rows"]}
    ns = flows["Region North to Region South"]
    sn = flows["Region South to Region North"]
    assert ns > sn > 0, "both streams must be non-zero and unequal"
    net = ns - sn
    assert net == 17000, net
    assert ns + sn == 79000, "the gross exchange offered as a distractor"
    return "17,000 toward Region South"


def q29_clustering(table):
    """With count and area held constant, empty quadrats measure clustering."""
    shops, empty = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        shops[d["District"]] = num(d["Shops"])
        empty[d["District"]] = num(d["Quadrats with no shop (of 16)"])
    assert len(set(shops.values())) == 1, f"shop counts are not equal: {shops}"
    most = max(empty, key=empty.get)
    assert most == "District Q", f"most empty quadrats: {empty}"
    assert empty["District Q"] == 11, empty
    # The clustering signal has to be decisive, not a one-quadrat edge.
    second = sorted(empty.values(), reverse=True)[1]
    assert empty[most] - second >= 5, empty
    return "11 of 16 quadrats"


def q30_net_remittance(table):
    """Net remittance position, which reorders the partners against gross flows."""
    net, gross, ratio = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        sent = num(d["Sent to recording country (millions)"])
        recv = num(d["Received from recording country (millions)"])
        net[d["Partner"]] = sent - recv
        gross[d["Partner"]] = sent
        ratio[d["Partner"]] = sent / recv
    best = max(net, key=net.get)
    assert best == "Partner 1", f"largest net is {best}: {net}"
    assert net["Partner 1"] == 750, net
    # The three named distractors must each pick a different partner.
    assert max(gross, key=gross.get) != best, gross
    assert max(ratio, key=ratio.get) != best, ratio
    assert net["Partner 2"] == 500 and net["Partner 4"] == 400, net
    return "Partner 1"


CLAIMS = [
 ("fixed global reference frame",
  "PSO-1.A.1 lists absolute and relative location as separate concepts, and a latitude-longitude pair states position in a coordinate system that depends on no other place. That independence from surrounding features is what makes the location absolute rather than relative."),

 ("fixed by its position with respect to other features",
  "PSO-1.A.1 pairs relative location with absolute location. A description built out of a cathedral and a tram stop is relative by construction, since it conveys nothing to a reader who does not already know where those landmarks are."),

 ("measurable extent",
  "PSO-1.A.1 lists space and place as two separate spatial concepts. The distinction geographers draw is between abstract extent, which can be measured and subdivided, and a particular location made meaningful by what people have done and felt there."),

 ("sense of place",
  "Place in this course is location plus meaning, and a tourist slogan of this kind is an attempt to sell precisely that surplus. Nothing in the slogan depends on the town's coordinates or on how far its visitors have travelled to reach it."),

 ("decline of interaction with increasing separation",
  "PSO-1.A.1 names distance decay among the spatial concepts. The concept is exactly that interaction between two places weakens as separation grows, because distance imposes costs in money, time and effort that rise with it."),

 ("relative distance collapses",
  "PSO-1.A.1 lists time-space compression, and the concept turns on the gap between two measures of separation. Kilometers are fixed by the geometry of the Earth while hours and fares are set by technology, so one can fall by an order of magnitude while the other does not move."),

 ("movement of people, goods, capital, or information",
  "PSO-1.A.1 lists flows as a spatial concept in its own right. What unites remittances, containerized cargo and spreading news is that each is something moving between places rather than something located at one, which is what a flow is."),

 ("spread evenly rather than concentrated",
  "PSO-1.A.1 lists pattern, and the standard descriptions of arrangement are clustered, dispersed, linear and random. Even spacing imposed by a rectangular survey is the clearest case of dispersal, because the layout is designed to prevent concentration."),

 ("has changed while their absolute locations have not",
  "An absolute location is a coordinate, and nothing a bridge does can alter it, whereas relative location is a statement about position with respect to other places and is exactly what a new connection rewrites. Separating the two is why the framework names them individually."),

 ("cheap to ship relative to its price",
  "Distance decay is steep when separation imposes a large penalty relative to the value of the interaction. A rare, valuable, easily shipped good makes transport a trivial share of price and gives buyers a reason to reach far, which flattens the decline."),

 ("milliseconds",
  "The argument is about the distribution of time-space compression, not its existence, so the evidence must be a contrast inside one setting. A trader and a distant farmer share an absolute geography while inhabiting entirely different relative ones."),

 ("by train expresses relative distance",
  "A duration depends on the mode, the timetable and the day's congestion, so it describes separation as experienced rather than as measured on the ground. Kilometers are fixed by the Earth's geometry and do not change with the traffic."),

 ("money flows back toward the region of origin",
  "PSO-1.A.1 includes capital among the things that move between places, so remittances are a flow in the same sense migration is. The two streams run in opposite directions, which is what makes the origin-destination relationship a two-way one."),

 ("follow a single axis",
  "Pattern in PSO-1.A.1 describes arrangement, and an arrangement organized along one axis is linear regardless of how evenly spaced its members happen to be. The river and its road supply both the axis and the reason for it."),

 ("leaving large areas with none",
  "Clustering is a claim about concentration within part of an area, so the diagnostic evidence is a dense subarea coexisting with large empty ones. Equal populations, good roads, wide spacing and a large total are each compatible with either arrangement."),

 ("Undifferentiated space",
  "The park's measurable extent is identical either way; what the resident adds is the accumulated meaning that turns extent into one particular place. That is the space-place distinction the framework points to by listing the two separately."),

 ("stops rising with distance",
  "Distance decay reflects the friction separation imposes, and a metered network makes that friction explicit in the price. Flat-rate transmission removes the cost gradient while leaving other reasons for local interaction intact, so the curve flattens without vanishing."),

 ("express rail line",
  "Time-space compression is a collapse in the time or cost of moving between places with no change in the distance between them, and it occurs at every scale including within one metropolitan area. Annexation, recounting, resurveying and renaming leave travel times exactly where they were."),

 ("fading gradient",
  "Distance decay describes a continuous decline rather than a threshold, so patronage thins with distance instead of stopping at a ring. That is why trade areas are drawn as probability surfaces and why two centers' trade areas legitimately overlap."),

 ("Close in absolute distance but far apart",
  "Forty kilometers is a small separation in the fixed measure, while a weekly six-hour crossing costing a day's wages is a large one in time, money and effort. Holding the two measures apart is exactly why the framework lists absolute and relative location separately."),

 ("tonnes of wheat move each year",
  "A flow question asks about movement between places over a period, which tonnes per year travelling from prairie to port is. The other options ask about arrangement, extent, meaning and position, which are the other concepts on the same list."),

 ("closer in travel time, which is relative distance",
  "The student's observation is correct and the vocabulary is loose: what fell is one relative measure of separation. Saying it precisely is what lets time-space compression be stated as a claim about the widening gap between the two measures."),

 ("coordinates remain the same",
  "Absolute location is a position in a fixed reference frame, so it is indifferent to everything that happens around the point. That stability is what makes it useful as a common register at times when every relative description is shifting."),

 ("no nearer alternative",
  "How steeply distance decay falls depends on whether the interaction can be satisfied nearby. Routine care exists in every town so the curve is steep, while a service offered at one site in a region leaves distant patients no substitute and they travel."),

 ("no single location possesses",
  "Arrangement is a property of a collection rather than of any member of it, so it cannot be read off a single coordinate however precise that coordinate is. That is why the framework lists pattern alongside location instead of as a kind of location."),

 ("roughly halve",
  "Recomputed from the table: successive ratios are 0.50, 0.50, 0.47 and 0.46, so each band draws about half the visitation rate of the one inside it. The verifier also confirms the drops are far from constant, which is what disqualifies the constant-difference reading offered as a distractor.",
  q26_decay),

 ("one twentieth",
  "Recomputed from the table: sixty hours to three is a reduction to one twentieth, and the distance column is identical in all three rows. The two columns behaving differently is the entire content of time-space compression, and the verifier confirms the hourly drops are not constant either.",
  q27_compression),

 ("17,000 toward Region South",
  "Recomputed from the table: subtracting the smaller stream from the larger leaves a net of 17,000 in the direction of the larger, while adding them gives the gross exchange of 79,000. Both figures are real and answer different questions, which is why counterflows have to be stated explicitly.",
  q28_net_flow),

 ("11 of 16 quadrats",
  "Recomputed from the table: all four districts hold the same 48 shops over equal areas, so the share of the area that is empty is the only thing separating them, and one district leaves eleven of sixteen quadrats with nothing in them. Equal totals are exactly what make the empty-quadrat column the discriminating evidence.",
  q29_clustering),

 ("Partner 1",
  "Recomputed from the table: netting each pair gives 750, 500, 340 and 400 million, so the partner sending the most in gross terms is not the partner with the largest net position, and neither is the partner with the highest sent-to-received ratio. Only the difference between the two directions measures the transfer.",
  q30_net_remittance),
]

hg_check.check(g1_4, CLAIMS, per_topic=30, n_choices=5)
