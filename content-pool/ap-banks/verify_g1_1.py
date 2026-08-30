"""Key audit for AP HUMAN GEOGRAPHY 1.1 Introduction to Maps.

One (anchor, claim) per item, in module order; a third element is a function
that recomputes the item's arithmetic from its own table.

WHAT IS AND IS NOT CITED HERE, because it decides what a key may rest on.
IMP-1.A prints exactly three essential-knowledge statements: the reference /
thematic split (A.1), the list of spatial patterns -- absolute and relative
distance and direction, clustering, dispersal, elevation (A.2) -- and the
selectivity-and-distortion claim (A.3). It does NOT name a single thematic map
type or a single projection. Items 3-9 and 19-24 therefore cite no EK: they are
keyed to what a choropleth, a dot map or a Mercator projection actually DOES,
which is a property a student can reason about and a reader can check. Writing
"EK IMP-1.A.1" beside a Mercator item would be a fabricated citation, and this
project has already paid for the habit of dressing an assertion in a code.

The five table items (10, 27, 28, 29, 30) are the ones with a computational
gate. Their functions below recompute the classification breaks, the densities,
the representative fractions, the time-versus-distance reversal and the dot
conversion from the printed cells, so a table edited without the key being
edited fails the module rather than shipping.
"""
import hg_check
from hg_check import num, numcol, column
import g1_1


def q10_classes(table):
    """Equal-width and equal-count breaks really do move Cranmere."""
    names = column(table, "County")
    rates = numcol(table, "Unemployment rate (%)")
    lo, hi = min(rates), max(rates)
    w = (hi - lo) / 3
    equal_width = [min(2, int((r - lo) / w)) if r < hi else 2 for r in rates]
    order = sorted(range(len(rates)), key=lambda k: rates[k])
    equal_count = [0] * len(rates)
    for rank, k in enumerate(order):
        equal_count[k] = rank // 2
    i = names.index("Cranmere")
    assert equal_width[i] == 0, equal_width
    assert equal_count[i] == 1, equal_count
    j = names.index("Fairholt")
    assert equal_width[j] == 2 and equal_count[j] == 2
    # ...and the two classifications are genuinely not the same map.
    assert equal_width != equal_count
    return "Cranmere"


def q27_density(table):
    """Birch is densest; Alder is largest by population and is not densest."""
    names = column(table, "County")
    pop = numcol(table, "Population")
    area = numcol(table, "Land area (square miles)")
    dens = [p / a for p, a in zip(pop, area)]
    assert names[pop.index(max(pop))] == "Alder"
    assert names[dens.index(max(dens))] == "Birch"
    assert abs(dens[names.index("Birch")] - 1000) < 1e-9
    assert abs(dens[names.index("Alder")] - 400) < 1e-9
    return "Birch"


def q28_scale(table):
    """The largest scale is the smallest denominator."""
    opts = column(table, "Option")
    # num() would read the leading 1 of "1:12,000"; the denominator is what
    # ranks a representative fraction, so split the ratio first.
    denom = [num(rf.split(":")[1]) for rf in column(table, "Representative fraction")]
    assert opts[denom.index(min(denom))] == "Y"
    assert min(denom) == 12000
    return "Y"


def q29_reversal(table):
    """Stonebridge is twice Redford's distance and reached sooner."""
    towns = column(table, "Town")
    km = dict(zip(towns, numcol(table, "Straight-line distance (km)")))
    mins = dict(zip(towns, numcol(table, "Scheduled travel time (min)")))
    assert km["Stonebridge"] == 2 * km["Redford"]
    assert mins["Stonebridge"] < mins["Redford"]
    # The distractor pairs really do run the same way in both measures.
    assert km["Pinehill"] < km["Redford"] and mins["Pinehill"] < mins["Redford"]
    assert km["Quarry Bay"] < km["Stonebridge"] and mins["Quarry Bay"] < mins["Stonebridge"]
    return "Stonebridge"


def q30_dots(table):
    """44 dots at 5,000 each is 220,000, and it is also the densest district."""
    names = column(table, "District")
    dots = numcol(table, "Dots on map")
    area = numcol(table, "Land area (sq km)")
    people = [d * 5000 for d in dots]
    dens = [p / a for p, a in zip(people, area)]
    assert names[people.index(max(people))] == "Eastmoor"
    assert names[dens.index(max(dens))] == "Eastmoor"
    assert people[names.index("Eastmoor")] == 220000
    assert people[names.index("Westbrook")] == 35000
    assert people[names.index("Southgate")] != people[names.index("Eastmoor")]
    return "220,000"


CLAIMS = [
 ("reference map",
  "EK IMP-1.A.1 names reference and thematic as the two types of map. The office asks for boundaries and streets and names no variable, which is the reference map's job -- to show where things are."),
 ("show the spatial pattern of one variable",
  "EK IMP-1.A.1. The reference/thematic distinction is one of purpose. Scale, projection, subject matter and extent all vary freely within both types, which is why each of those is offered as a distractor."),
 ("Choropleth",
  "A choropleth fills an enumeration unit with one shade, so the value must already be standardised for the size of the unit. A median household income is such a value; a count, a movement and a point observation are not."),
 ("makes large counties look important simply because they are large",
  "The area of the polygon does the visual work in a choropleth, so an unnormalised count conflates 'many people' with 'much land'. This is the standard reason choropleths take rates, densities and percentages only."),
 ("Where within each state the animals actually are",
  "A dot distribution map places dots at the phenomenon's locations, so internal clustering and empty ground remain visible. A choropleth assigns one shade to the whole unit and destroys exactly that information."),
 ("Isoline",
  "An isoline map is the type built for a continuous surface -- a variable with a value at every point, not only inside a drawn boundary. Rainfall, elevation, temperature and pressure are the standard cases."),
 ("True area and shape",
  "A cartogram is a value-by-area map: it abandons true geometry deliberately so that the size a reader perceives is the quantity itself. Adjacency between units is usually kept, which is what leaves the map readable."),
 ("flow-line map",
  "Flow-line mapping is the technique for interaction between places rather than attributes of places: the line carries direction and its width carries volume. No static-location map type encodes both at once."),
 ("circle twice as wide represents four times the value",
  "Graduated symbols encode magnitude in a two-dimensional area, and area grows as the square of the radius. The standard caution about the type is that readers underestimate the large symbols."),
 ("Cranmere sits in the lowest class under equal-width breaks and the middle class under equal-count breaks",
  "EK IMP-1.A.3 -- all maps are selective. Classification is one of those selections, and the recompute function confirms that these six rates really do put Cranmere in different classes under the two standard methods, with no change to the data at all.",
  q10_classes),
 ("Deciding which borders and which cities to draw is itself a selection",
  "EK IMP-1.A.3 applies to reference maps as much as to thematic ones. Omission is a choice, and a map must resolve a contested border one way or the other, which is a position rather than a neutral record."),
 ("Absolute distance",
  "EK IMP-1.A.2 lists absolute and relative distance among the spatial patterns maps represent. Absolute distance is separation stated in a standard unit; the distractors are how far apart places feel, how interaction weakens with separation, and connectivity change."),
 ("Relative distance, then absolute distance",
  "EK IMP-1.A.2. Time, cost and effort measure relative distance and change with traffic, mode and infrastructure; kilometers are the standard unit and therefore absolute. The order in the stem is minutes first, kilometers second."),
 ("Relative direction",
  "EK IMP-1.A.2 pairs absolute and relative direction. A bearing measured from the pole is absolute and does not depend on the speaker; 'up north' is stated from where the speaker stands and would be false for a speaker in Ontario."),
 ("Clustering",
  "EK IMP-1.A.2 names clustering and dispersal. Concentration of the phenomenon into a limited part of the area mapped is clustering; the emptiness elsewhere is the same observation from the other side, not a second pattern."),
 ("Dispersal",
  "EK IMP-1.A.2's dispersal is the opposite of clustering -- features spread across the whole area rather than concentrated in part of it. Regular one-per-quarter-section spacing is its strongest form."),
 ("much steeper",
  "Contours are isolines of elevation at a fixed vertical interval, so horizontal spacing reads directly as slope: the same rise crossed in less ground is a steeper gradient. EK IMP-1.A.2 lists elevation among the patterns maps portray."),
 ("curved surface cannot be flattened without stretching or tearing",
  "EK IMP-1.A.3 asserts that projections inevitably distort shape, area, distance and direction. The reason is geometric, not technical: a sphere is not a developable surface, so accuracy in one property is bought with error in another."),
 ("Mercator",
  "Mercator is conformal and was built so that a rhumb line -- a course of constant compass bearing -- plots straight, which is why it persists on nautical charts. The same spacing of parallels inflates area with latitude."),
 ("stretches area increasingly with latitude",
  "The areal exaggeration on Mercator is a function of latitude, because the parallels are spaced ever wider toward the poles to keep angles true. Africa straddles the equator and Greenland sits above 60 degrees north, which is the whole of the illusion."),
 ("Gall-Peters",
  "Comparing a distribution between regions requires equal ground areas to occupy equal page areas, which is the definition of an equal-area projection. Robinson is a compromise and is exactly equal-area nowhere, which is why it is offered as the trap."),
 ("keep their true relative size with less shape distortion",
  "Interruption moves the unavoidable error into the oceans, where a land-distribution map has nothing to say, so the continents come out equal-area and better shaped than an uninterrupted equal-area map allows. The same cuts make it useless for sea routes."),
 ("distorts shape, area, distance and direction moderately",
  "A compromise projection holds no property exactly and keeps every error small, which suits a general reference map and disqualifies it from any measurement that needs a property held true."),
 ("polar azimuthal projection",
  "Azimuthal projections hold true direction outward from the point of tangency, which is the property a polar hub-and-spoke route map needs. Distortion grows with distance from that center, which is acceptable when everything of interest radiates from it."),
 ("Larger in scale, and therefore able to show far more detail over far less ground",
  "A representative fraction is a ratio: the smaller the denominator, the larger the fraction and the larger the scale. 1/24,000 far exceeds 1/50,000,000, and the magnification is paid for in extent."),
 ("world's major language families",
  "Small scale means a large denominator, great extent and little detail. Only a worldwide distribution needs that extent; a block, a subdivision, a floor plan and a single avenue all demand magnification of a very small area."),
 ("Birch, which has far from the largest population but by far the highest density",
  "Recomputed from the table: Alder leads on population with 480,000, Birch leads on density with 1,000 per square mile against Alder's 400. A dot map is driven by the count and a density choropleth by the ratio, so the two maps crown different counties.",
  q27_density),
 ("smallest denominator",
  "Recomputed from the table: 12,000 is the smallest of the four denominators, so 1:12,000 is the largest scale. Building footprints are tens of meters across and survive only at that magnification.",
  q28_scale),
 ("Stonebridge is twice as far in kilometers yet is reached sooner",
  "Recomputed from the table: 120 km is exactly twice 60 km, and 70 minutes is less than 90. The two distractor pairs offered as 'as expected' really do run the same way in both measures, which is checked too, so only one option shows the reversal.",
  q29_reversal),
 ("220,000 residents",
  "Recomputed from the table: 44 dots at a stated 5,000 residents each is 220,000, the largest count; over 2,200 square kilometers that is 100 per square kilometer, also the highest. A stated dot value is what makes a dot map quantitative rather than merely suggestive.",
  q30_dots),
]

hg_check.check(g1_1, CLAIMS, per_topic=30, n_choices=5)
