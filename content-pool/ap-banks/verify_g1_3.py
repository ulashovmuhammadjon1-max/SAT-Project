"""Key audit for AP HUMAN GEOGRAPHY 1.3 The Power of Geographic Data.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. IMP-1.C prints exactly one essential-knowledge statement:

    IMP-1.C.1  Geospatial and geographical data, including census data and
               satellite imagery, are used at all scales for personal, business
               and organizational, and governmental decision-making purposes.

That sentence supports two kinds of key and no more: which class of decision
maker a scenario belongs to, and the assertion that the same data serve every
scale. Items 1-4, 10, 17, 20 and 25 are keyed to it and cite it. The learning
objective -- explain the geographical EFFECTS of decisions made using
geographical information -- is what the rest of the module rests on, and those
claims are arguments about consequence rather than quotations. No EK code is
attached to them, because a fabricated citation is worse than an honest
uncited claim.

The five table items (26-30) are the computational gate. Each function below
recomputes the served population, the elevation threshold, the forgone grant,
the unserved-household counts and the yield cutoff from the printed cells, and
each also asserts that the trap the item is built around is really present --
that the largest household count is NOT the largest served population, that the
largest missed count is NOT the largest forgone grant, that the worst
connection rate is NOT the largest unserved count. A distractor that is
accidentally also correct is the failure these assertions exist to catch.

REVIEW NOTE, written while building the tables. Three items were wrong on the
first pass and were corrected before this verifier was written: item 26 had two
sites tied at 24,000 served, so "the largest" named two options at once; item 28
originally gave the largest forgone grant to the city offered as a distractor;
and item 30's threshold rule excluded a zone the key included, because 15
percent below an average of 7.0 is 5.95 and the zone sat at exactly 6.0. All
three are now recomputed here rather than trusted.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g1_3


def q26_site(table):
    """Served population is households times mean household size, not households."""
    served, hh, comp = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        hh[d["Site"]] = num(d["Households within 3 km"])
        served[d["Site"]] = hh[d["Site"]] * num(d["Average household size"])
        comp[d["Site"]] = num(d["Nearest competitor (km)"])
    best = max(served, key=served.get)
    assert best == "Site 2", f"largest served population is {best}: {served}"
    assert abs(served["Site 2"] - 24000) < 1e-6, served
    # The trap: the most households is a different site, and there is no tie.
    assert max(hh, key=hh.get) != best, "households alone gives the same answer"
    top = sorted(served.values(), reverse=True)
    assert top[0] > top[1], f"two sites tie on served population: {served}"
    # The key also asserts the furthest competitor, so that has to hold.
    assert max(comp, key=comp.get) == best, comp
    return "24,000 people"


def q27_flood_zone(table):
    """Parcels below 4 m, and the households they hold."""
    inside = [rowdict(table, r) for r in table["rows"]
              if num(rowdict(table, r)["Elevation (m)"]) < 4.0]
    hh_in = sum(num(d["Households"]) for d in inside)
    hh_all = sum(num(rowdict(table, r)["Households"]) for r in table["rows"])
    assert len(inside) == 3, f"{len(inside)} parcels below 4 m"
    assert hh_in == 47 and hh_all == 63, (hh_in, hh_all)
    # The key claims MOST of the listed households are inside, so check it.
    assert hh_in > hh_all / 2, "the affected households are not a majority"
    return "47 of the 63 households"


def q28_forgone_grant(table):
    """Forgone grant is the missed count times that city's own per-resident rate."""
    loss, missed, rate, size = {}, {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        c, t = num(d["Counted population"]), num(d["Estimated true population"])
        per = num(d["Grant per resident"])
        missed[d["City"]] = t - c
        rate[d["City"]] = (t - c) / t
        size[d["City"]] = t
        loss[d["City"]] = (t - c) * per
    worst = max(loss, key=loss.get)
    assert worst == "Brightmoor", f"largest forgone grant is {worst}: {loss}"
    assert loss["Brightmoor"] == 480000, loss
    # Each distractor names a different city on a different measure; none may
    # coincide with the answer or the item has two defensible keys.
    assert max(missed, key=missed.get) != worst, missed
    assert max(rate, key=rate.get) != worst, rate
    assert max(size, key=size.get) != worst, size
    assert loss["Ashvale"] == 300000, loss
    return "$480,000"


def q29_unserved(table):
    """Unserved households, which rank differently from connection rates."""
    unserved, share = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        total = num(d["Households"])
        s = num(d["Share with broadband access"]) / 100.0
        share[d["District"]] = s
        unserved[d["District"]] = total * (1 - s)
    worst = max(unserved, key=unserved.get)
    assert worst == "District L", f"most unserved is {worst}: {unserved}"
    assert abs(unserved["District L"] - 10000) < 1e-6, unserved
    # The trap: the lowest connection share belongs to a different district.
    assert min(share, key=share.get) != worst, share
    assert abs(unserved["District K"] - 5400) < 1e-6, unserved
    assert abs(unserved["District M"] - 5600) < 1e-6, unserved
    return "10,000 unserved households"


def q30_fertilizer(table):
    """Zones more than 15 percent below the area-weighted field average."""
    zones, areas, yields = [], [], []
    for row in table["rows"]:
        d = rowdict(table, row)
        zones.append(d["Zone"])
        areas.append(num(d["Area (hectares)"]))
        yields.append(num(d["Yield (tonnes per hectare)"]))
    avg = sum(a * y for a, y in zip(areas, yields)) / sum(areas)
    cutoff = 0.85 * avg
    below = [z for z, y in zip(zones, yields) if y < cutoff]
    assert abs(avg - 7.0) < 1e-9, f"field average is {avg}"
    assert abs(cutoff - 5.95) < 1e-9, cutoff
    assert below == ["Zone 2", "Zone 4"], f"zones under the cutoff: {below}"
    # No zone may sit exactly on the cutoff, which is what broke the first draft.
    assert all(abs(y - cutoff) > 0.01 for y in yields), yields
    return "5.95 tonne cutoff"


CLAIMS = [
 ("an individual is using the data",
  "EK IMP-1.C.1 names personal decision making as one of its three classes of use, and the class is fixed by whose decision the data informs rather than by who owns the data or the road. Here a single driver is choosing her own route, which is the personal case exactly."),

 ("business decision made with census data",
  "EK IMP-1.C.1 lists census data among the geographic data used for business decision making. The collector of a dataset and the user of it are different parties, and choosing between two commercial sites is a firm's judgement about where its customers live."),

 ("Organizational decision making using satellite imagery",
  "EK IMP-1.C.1 pairs satellite imagery with organizational decision making and asserts these data are used at all scales. A relief agency is neither an individual nor a state, and no census can exist for a camp that formed within weeks."),

 ("converted directly into political representation",
  "Apportionment is a rule that mechanically transforms population counts into legislative seats, so the data determine the outcome rather than merely advising it. That direct conversion is why census accuracy becomes a political contest rather than only a technical one."),

 ("helped produce the decline it claimed to predict",
  "A lending rule applied through a map redistributes credit across space, and withheld investment degrades housing stock over decades. The apparent confirmation of the map is circular, since the decline it produced was then offered as evidence that its grades were accurate."),

 ("less funding than its actual population warrants",
  "Where a formula takes counted population as its input, an undercount passes straight into the allocation and persists until a new count replaces it. The effect is geographic because undercount concentrates in particular kinds of places rather than spreading evenly."),

 ("where police have looked",
  "Arrest counts record enforcement activity rather than offending, so deploying patrols on them creates a loop in which attention manufactures the evidence for further attention. The resulting map is self-confirming whatever the underlying distribution of crime is."),

 ("the boundary itself becomes economically visible",
  "A line that changes the cost of holding property on one side and not the other produces a discontinuity in prices and in building decisions across it. The map does not merely describe the landscape; it becomes one of the forces shaping what is built there."),

 ("including places no one can currently reach",
  "Immediately after a disaster the roads and communications that ground reporting depends on are the very systems that have failed, so coverage is thinnest exactly where damage is worst. Imagery covers the whole scene uniformly and requires no access to it."),

 ("the same field is treated as several different places",
  "EK IMP-1.C.1 asserts that geospatial data are used at all scales, and the finest of those is within a single holding. Treating one field as an internally varied surface rather than a uniform unit is precisely what a yield map makes possible."),

 ("the spatial clustering points to a shared source",
  "A cluster drawn tight around one piece of shared infrastructure is evidence about that infrastructure, and testing it is both the cheapest and the most direct response available. The blaming reading and the citywide shutdown both go well past what the pattern supports."),

 ("cheap land is not a neutral variable",
  "An analysis returns whatever its criteria ask for, and land price is correlated with the wealth and political weight of the people living nearby. The apparent objectivity of the output conceals the choice of inputs, which is where the distributional consequence was actually decided."),

 ("more precise rather than less possible",
  "Resolution is a capability rather than a value, so the same fineness of data that lets a fair boundary be verified lets an unfair one be optimized. Coarse data limits how tightly a district can be tuned, which is why precision and manipulability rise together."),

 ("place of worship",
  "A location trace is a record of participation in particular places, so the sensitive inferences follow from the places themselves rather than from the identifier. Breach risk, unread terms and offshore storage attach to any dataset whether or not it carries coordinates."),

 ("under-reporting neighborhoods will appear reliable",
  "The utility's dataset measures reported outages rather than experienced ones, so a systematic difference in reporting becomes a systematic difference in capital investment. It is the same reporting bias that makes complaint and crime data hazardous as an allocation rule."),

 ("too coarse for the decision",
  "Choosing the right province and choosing the right site inside it are different questions, and a provincial average carries no information about the internal distribution of poverty. The mismatch between the scale of the data and the scale of the decision is where the error enters."),

 ("comparing school catchment maps and commute times",
  "EK IMP-1.C.1 separates personal use from business, organizational and governmental use. Four of the options describe institutions deciding on behalf of a population; only the household is deciding for itself, which is what makes it the personal case."),

 ("mistaken for an absence of need",
  "A planning process that reads its world from a dataset can act only on what the dataset contains, so an unmapped population is invisible to every step that follows. Being left off the base map is therefore a material harm rather than a cartographic detail."),

 ("arrangement of the stops in space",
  "What makes the routing problem geographic is that its objective is built out of distances, adjacencies and travel times that vary from place to place. That vans are physical, that drivers live somewhere and that regulation differs by country are all true and none of them makes the decision spatial."),

 ("treating the zone boundary as a real line",
  "Once an authoritative line is published, actors with money at stake write it into decisions that outlast any single storm season. Its influence on land, credit and insurance markets is a larger long-run effect than its use during the few days of an emergency."),

 ("the imagery misread or missed",
  "A titling programme converts a data product into a durable legal right, so both the accuracy and the omissions of the imagery become permanent. Formalization is rarely uniformly good or bad; it redistributes security toward the households the data captured correctly."),

 ("draw customers away from the company's own stores",
  "Catchments that overlap by more than half mean the same households are already being served by the firm, so most of the new store's revenue is transferred rather than added. Detecting that cannibalization is the whole purpose of the drive-time analysis."),

 ("an individual choosing a route, a firm choosing a site, and a state allocating seats",
  "EK IMP-1.C.1 states the range explicitly by naming personal, business and organizational, and governmental users in one sentence about all scales. What distinguishes the uses is the decision being made, not a scale at which the data suddenly become valid."),

 ("Victims may be identifiable",
  "Releasing at the finest spatial unit erodes the anonymity that aggregation supplies and lets a handful of incidents stigmatize one named block. Both harms follow from the resolution of the release rather than from the decision to publish at all."),

 ("each user pursues a different end with it",
  "EK IMP-1.C.1 lists governmental, business and personal users side by side, and nothing in a dataset restricts it to one of them. The ministry may move teachers, the firm may site a branch and the parent may choose a house, all from the same published map."),

 ("24,000 people",
  "Recomputed from the table: households times average household size gives served populations of 18,900, 24,000, 22,000 and 15,000, so the site with the most households is not the site serving the most people. The verifier also confirms there is no tie for the largest and that the same site has the most distant competitor.",
  q26_site),

 ("47 of the 63 households",
  "Recomputed from the table: elevations of 2.5, 3.2 and 1.8 metres fall under the four-metre rule and their parcels hold 12, 20 and 15 households, which is 47 of the 63 listed and therefore a majority. A threshold stated in metres has its real effect in the households it reaches.",
  q27_flood_zone),

 ("$480,000",
  "Recomputed from the table: missed counts times each city's own per-resident rate give $300,000, $480,000, $240,000 and $405,000. The largest missed count, the highest undercount rate and the largest population each belong to a different city from the answer, which the verifier asserts separately.",
  q28_forgone_grant),

 ("10,000 unserved households",
  "Recomputed from the table: unserved households are 4,000, 5,400, 10,000 and 5,600, so the district with the worst connection rate is not the district with the most unserved households. Which measure the funding rule names is what decides where the money goes.",
  q29_unserved),

 ("5.95 tonne cutoff",
  "Recomputed from the table: four equal-area zones average exactly 7.0 tonnes per hectare, putting the fifteen-percent cutoff at 5.95, and yields of 5.6 and 5.0 fall under it while 8.4 and 9.0 sit above the mean. The verifier also asserts that no zone sits on the cutoff, which is the defect the first draft of this item had.",
  q30_fertilizer),
]

hg_check.check(g1_3, CLAIMS, per_topic=30, n_choices=5)
