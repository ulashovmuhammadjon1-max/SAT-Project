"""Key audit for AP HUMAN GEOGRAPHY 1.7 Regional Analysis.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. SPS-1.A prints four essential-knowledge statements, and this
is the rare Unit 1 topic where almost every key can be traced to one of them:

    SPS-1.A.1  Regions are defined on the basis of one or more unifying
               characteristics or on patterns of activity.
    SPS-1.A.2  Types of regions include formal, functional, and
               perceptual/vernacular.
    SPS-1.A.3  Regional boundaries are transitional and often contested and
               overlapping.
    SPS-1.A.4  Geographers apply regional analysis at local, national, and
               global scales.

The mapping the module is built on, stated once so every key is auditable:
SPS-1.A.1's TWO grounds -- a unifying characteristic, or a pattern of activity --
are the formal/functional split of SPS-1.A.2 given in advance. The third type,
perceptual/vernacular, rests on neither: it is constituted by belief, which is
why SPS-1.A.3's "contested" applies to it most sharply and why item 25 asks why
the CED prints the two words as one category.

Items citing SPS-1.A.1 or A.2 (type classification): 1, 2, 3, 5, 7, 8, 11, 14,
16, 18, 19, 21, 22, 23, 25, 26, 27.
Items citing SPS-1.A.3 (transitional, contested, overlapping): 4, 9, 10, 12, 17,
20, 24, 28, 29.
Items citing SPS-1.A.4 (scale): 6, 15, 18, 23.
Items citing nothing: 13, which turns on the fact that a functional boundary
moves when the node's reach changes -- true, standard, and not a framework
sentence, so it is argued rather than cited.

The five table items (26-30) are the computational gate:

  26  two criteria applied together admit FEWER counties than either alone,
      which is the point of a multi-criterion formal region
  27  a functional boundary is drawn on the commuting SHARE, and the town
      sending the most commuters in absolute terms does not have the highest
      share -- the recompute asserts that mismatch is really there
  28  agreement declines monotonically with distance, which is what a
      transitional perceptual boundary looks like when it is measured
  29  three inclusions on three different bases plus one exclusion
  30  three criteria admit 21, 15 and 26 countries with only 12 shared, so even
      the smallest list has members outside the common core

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written, and none needed correcting. The terminology constraint the module
observes -- never offering "perceptual region" and "vernacular region" as two
separate options -- is enforced independently by hg_check's SYNONYM_CLASSES,
which is why no question here does it.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g1_7


def q26_two_criteria(table):
    """Both criteria together, and the check that each alone would admit more."""
    wheat, rain = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        wheat[d["County"]] = num(d["Wheat share of cropped area (%)"])
        rain[d["County"]] = num(d["Annual rainfall (mm)"])
    both = [c for c in wheat if wheat[c] > 50 and rain[c] < 600]
    wheat_only = [c for c in wheat if wheat[c] > 50]
    rain_only = [c for c in rain if rain[c] < 600]
    assert both == ["County 1", "County 3"], f"counties meeting both: {both}"
    assert len(wheat_only) == 3 and len(rain_only) == 3, (wheat_only, rain_only)
    # The intersection must be strictly smaller than either single criterion.
    assert len(both) < len(wheat_only) and len(both) < len(rain_only)
    return "Counties 1 and 3"


def q27_commuting_share(table):
    """The functional boundary is a ratio, not a headcount."""
    share, count = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        workers = num(d["Workers"])
        commuters = num(d["Commuting to central city"])
        share[d["Town"]] = 100 * commuters / workers
        count[d["Town"]] = commuters
    inside = sorted(t for t in share if share[t] >= 25)
    assert inside == ["Town A", "Town C", "Town D"], f"inside the region: {share}"
    assert [round(share[t]) for t in inside] == [40, 30, 35], share
    # The largest absolute flow must come from a town that is NOT the highest share.
    assert max(count, key=count.get) != max(share, key=share.get), (count, share)
    assert max(count, key=count.get) == "Town C", count
    # Town E must genuinely fall below, or one distractor becomes true.
    assert share["Town E"] < 25, share
    return "40, 30, and 35 percent"


def q28_gradient(table):
    """Agreement falls monotonically with distance -- a measured transition zone."""
    pairs = []
    for row in table["rows"]:
        d = rowdict(table, row)
        pairs.append((num(d["Distance from core (km)"]),
                      num(d["Residents answering yes (%)"])))
    pairs.sort()
    yes = [y for _, y in pairs]
    assert all(yes[i] > yes[i + 1] for i in range(len(yes) - 1)), f"not monotonic: {yes}"
    assert yes[0] > 90 and yes[-1] < 10, yes
    # No jump large enough to read as a sharp edge anywhere in the sequence.
    drops = [yes[i] - yes[i + 1] for i in range(len(yes) - 1)]
    assert max(drops) < 30, f"a drop of {max(drops)} reads as a sharp boundary"
    # And the "exactly half agree" distractor must be false.
    assert sum(1 for y in yes if y >= 50) != len(yes) / 2, yes
    return "transition zone"


def q29_overlap(table):
    """Three inclusions on three different bases, and one exclusion."""
    inc = [rowdict(table, r) for r in table["rows"]
           if rowdict(table, r)["District included?"] == "Yes"]
    exc = [rowdict(table, r) for r in table["rows"]
           if rowdict(table, r)["District included?"] == "No"]
    assert len(inc) == 3 and len(exc) == 1, (len(inc), len(exc))
    bases = {d["Basis of definition"] for d in inc}
    assert len(bases) == 3, f"the three inclusions share a basis: {bases}"
    return "three overlapping regions"


def q30_criterion_disagreement(table):
    """Three criteria, three different country lists, one small shared core."""
    sizes, shared = [], set()
    for row in table["rows"]:
        d = rowdict(table, row)
        sizes.append(num(d["Countries included"]))
        shared.add(num(d["Countries also in all three lists"]))
    assert len(shared) == 1, f"the shared core is reported inconsistently: {shared}"
    core = shared.pop()
    assert core == 12, core
    assert len(set(sizes)) == 3, f"two criteria admit the same number: {sizes}"
    # Even the smallest list must extend beyond the shared core.
    assert min(sizes) > core, (sizes, core)
    return "Only 12 countries"


CLAIMS = [
 ("measurable characteristic its members share",
  "EK SPS-1.A.1 allows a region to rest on one or more unifying characteristics and EK SPS-1.A.2 names formal as the type built that way. A measured language threshold holding across an area is a shared trait rather than an activity organized from a center."),

 ("organized around a node by an activity",
  "EK SPS-1.A.1's second ground for a region is a pattern of activity, and EK SPS-1.A.2 attaches the functional label to it. A delivery area is held together by the operation of one center, not by any trait the households inside it share."),

 ("depends on what people believe",
  "EK SPS-1.A.2 prints perceptual and vernacular as a single type and EK SPS-1.A.3 says regional boundaries are often contested. A region whose extent varies with whom you ask is constituted by belief rather than by measurement."),

 ("gives way to that of another",
  "EK SPS-1.A.3 states that regional boundaries are transitional. Interaction with a node weakens with distance, so between two nodes there is a zone of divided allegiance rather than a line, which is what a commuting or trade-area edge actually is."),

 ("more than one unifying characteristic",
  "EK SPS-1.A.1 explicitly permits a region built on one OR MORE unifying characteristics. Combining elevation, rainfall and crop narrows the area without changing the type, since all three are traits the area possesses rather than activities radiating from a center."),

 ("the Corn Belt is national",
  "EK SPS-1.A.4 states that geographers apply regional analysis at local, national and global scales. The same three region types recur at every extent, and the scale is fixed by the extent of the area analyzed rather than by which type it is."),

 ("commuting is the activity that organizes it",
  "A numerical threshold makes a boundary crisp without changing what unifies the area, and what unifies this one is daily movement toward a single center. EK SPS-1.A.1's pattern of activity and EK SPS-1.A.2's functional type are the operative statements."),

 ("annual rainfall exceeds 1,000 millimetres",
  "EK SPS-1.A.2's formal type rests on a shared measurable characteristic, which a rainfall threshold is. The other four options are held together by activity organized from a center or by popular belief, making them functional or perceptual instead."),

 ("one place can belong to several",
  "EK SPS-1.A.3 says regional boundaries are often overlapping. Because each region is built on a different unifying criterion, membership in one implies nothing whatever about membership in another, and a single location can satisfy all of them."),

 ("place its edge differently",
  "EK SPS-1.A.3 states that regional boundaries are transitional and often contested, and a region built on belief is the extreme case of that. Mapping one honestly means showing a gradient of agreement rather than committing to a single line."),

 ("unified by movement toward one center or by a trait",
  "EK SPS-1.A.1 gives exactly two grounds for defining a region -- a unifying characteristic or a pattern of activity -- and EK SPS-1.A.2 attaches a type to each. Ownership, legal status, popular naming and size cut across the distinction and settle nothing."),

 ("transition zone in which the two functional regions overlap",
  "EK SPS-1.A.3's claim that regional boundaries are transitional and overlapping describes a split commuting field exactly. It is not a failure of the classification but what the edge of a functional region looks like when it is measured."),

 ("commute to the node from twice as far away",
  "A functional region is bounded by how far the node's activity effectively reaches, so anything extending that reach moves the boundary outward without touching the landscape. Yields, age structure, naming and survey accuracy leave the commuting field where it was."),

 ("combines formal criteria with a perceptual identity",
  "EK SPS-1.A.1 permits one or more unifying characteristics and EK SPS-1.A.2 lists three types without forbidding a region from carrying features of more than one. Measurable industrial decline and a shared sense of loss are both real here, and the honest classification records both."),

 ("At local, national, and global scales alike",
  "EK SPS-1.A.4 states in so many words that geographers apply regional analysis at local, national and global scales. Nothing in the definition of a region ties it to a particular extent -- only to a unifying criterion or a pattern of activity."),

 ("alike in some measured respect",
  "EK SPS-1.A.1's two grounds, a unifying characteristic and a pattern of activity, are precisely the two halves of this diagnostic question. Naming, size, authorship and publication cut across the formal-functional distinction and cannot resolve an ambiguous case."),

 ("gradient of agreement",
  "EK SPS-1.A.3 states that regional boundaries are transitional, and agreement declining smoothly outward from a core is the empirical form that transition takes. Choosing any single cut-off is then a decision by the analyst rather than a discovery about the region."),

 ("network of airports and routes",
  "EK SPS-1.A.4 admits regional analysis at the global scale and EK SPS-1.A.2's functional type is defined by activity organized through nodes. An airline alliance is exactly a set of nodes and the flows between them, spread across the world."),

 ("Uniformity is what defines a formal region only",
  "EK SPS-1.A.2 names three types and only one of them is built on a shared trait. EK SPS-1.A.1's alternative ground, a pattern of activity, is precisely a way of unifying an area that is internally varied rather than uniform."),

 ("regional boundaries are often contested",
  "EK SPS-1.A.3 says regional boundaries are transitional and often contested and overlapping. Two governments each publishing a map favouring its own claim is the political form of that contest, and it can happen to a formal region as easily as to a perceptual one."),

 ("trade area is the zone from which it actually draws customers",
  "A trade area is defined by where customers come from, which is a pattern of activity organized around a node exactly as EK SPS-1.A.1 and EK SPS-1.A.2 describe. Two stores compete where their trade areas overlap, which is what the functional concept makes visible."),

 ("Changing the criterion changes the region",
  "EK SPS-1.A.1 makes the unifying characteristic or the pattern of activity the basis of the region, so the region follows from the criterion chosen. Different traits and different thresholds yield different boundaries from the same underlying reality."),

 ("no two residents agree on exactly",
  "EK SPS-1.A.4 puts regional analysis at the local scale as well as the national and global, and EK SPS-1.A.2's perceptual type is built on shared belief. A named district whose limits shift from resident to resident is that type at neighborhood extent."),

 ("groups very different countries under one label",
  "EK SPS-1.A.1 makes a region a consequence of its defining criterion, and EK SPS-1.A.3 warns that boundaries are transitional and contested. A continental label conceals both the internal variety it contains and the arbitrariness of where the cut was made."),

 ("people name and believe in it",
  "EK SPS-1.A.2 prints the type as perceptual/vernacular, treating the pair as one category rather than two. What both words point at is a region constituted by common usage and belief, which is why it has no measurable criterion to appeal to."),

 ("the only counties meeting both criteria",
  "Recomputed from the table: 62 percent wheat with 540 millimetres and 71 percent with 580 are the only pairs satisfying both conditions, while either criterion applied alone would admit three counties. A multi-criterion formal region is the intersection and is therefore smaller than either part.",
  q26_two_criteria),

 ("40, 30, and 35 percent",
  "Recomputed from the table: commuting shares are 40, 20, 30, 35 and 19 percent, so three towns clear the twenty-five percent threshold. The verifier also confirms that the town sending the most commuters in absolute terms is not the town with the highest share, which is why a functional boundary is drawn on the ratio.",
  q27_commuting_share),

 ("declines steadily with distance from the core",
  "Recomputed from the table: agreement falls from 96 percent at the core to 9 percent at 260 kilometres with no step anywhere in the sequence, and the verifier confirms no single drop is large enough to read as an edge. A monotonic decline is the measured form of the transitional boundary the framework describes.",
  q28_gradient),

 ("three overlapping regions defined on three different bases",
  "Recomputed from the table: three rows record inclusion and one exclusion, and the three inclusions rest on three genuinely different bases -- a shared trait, a journey-to-work pattern and drainage. Overlapping membership on different criteria is exactly what the framework's statement about boundaries predicts.",
  q29_overlap),

 ("Only 12 countries appear on all three lists",
  "Recomputed from the table: the criteria admit 21, 15 and 26 countries while only 12 are common to all three, so even the smallest list contains members outside the shared core. A region is a consequence of its criterion, and different criteria genuinely disagree about who is in it.",
  q30_criterion_disagreement),
]

hg_check.check(g1_7, CLAIMS, per_topic=30, n_choices=5)
