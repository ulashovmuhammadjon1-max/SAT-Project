"""Key audit for AP HUMAN GEOGRAPHY 5.2 Settlement Patterns and Survey Methods.

Units 4-7 verify against `geo_check`, which takes a flat ANCHORS list plus
TABLE_NOTES. The CLAIMS list below is the audit trail -- one (anchor, claim) pair
per item, in module order -- and ANCHORS is derived from it so the two cannot
drift apart.

WHAT MAY BE CITED. One learning objective, three essential knowledge statements:

    PSO-5.B   Identify different rural settlement patterns and methods of
              surveying rural settlements.
    PSO-5.B.1 Specific agricultural practices shape different rural land-use
              patterns.
    PSO-5.B.2 Rural settlement patterns are classified as clustered, dispersed,
              or linear.
    PSO-5.B.3 Rural survey methods include metes and bounds, township and range,
              and long lot.

TWO LISTS THAT ANSWER DIFFERENT QUESTIONS, and keeping them apart is most of
what this topic tests. A SETTLEMENT PATTERN says where the DWELLINGS are
relative to one another; a SURVEY METHOD says how the LAND was divided into
parcels. The two correlate strongly -- items 10 and 21 are about exactly why --
but neither determines the other, and every choice list in this module that
offers a term from one list as an answer to the other is doing so deliberately.
Items 1, 2, 16, 24 and 30 keep the distinction explicit.

WHAT THE CED DOES NOT DEFINE: any of the six terms. The definitions used in the
claims below are the standard ones -- clustered means dwellings grouped with
their fields around them; dispersed means each farmstead on the land it works;
linear means dwellings strung along a road, river or levee; metes and bounds
fixes boundaries by features, directions and distances; township and range lays
a rectangular grid from surveyed base lines and meridians; long lot cuts narrow
strips back from a waterway so each holding has frontage.

THE ONE ARITHMETIC FACT used anywhere in the module is the internal geometry of
a rectangular survey: a section is one square mile, which is 640 acres, so a
quarter is 160 and a quarter of a quarter is 40. That is a property of the survey
system rather than a claim about any state's land law, and item 28's recompute
derives all four figures from the table's own rows instead of asserting them.

PSO-5.B.1 IS THE CAUSAL STATEMENT and it is the one students skip. Practice
shapes pattern: work that needs many hands on one water source at the same moment
pulls dwellings together, while a household needing thousands of hectares pushes
them apart by the arithmetic of area alone. Items 12, 13, 14, 15, 21 and 25 run
that argument, and item 25 runs it with climate and crop held constant so that
practice is the only variable left.

NO REAL PLACE IS NAMED. These three statements name none, survey systems are
attached to particular national histories that are easy to get subtly wrong, and
describing a landscape tests the same reading without asserting anything
contestable.

The three table items (26, 27, 28) are the computational gate:

  26  the depth-to-frontage ratio of every parcel, plus the assertion that all
      four touch the river -- regularity alone would not separate a long lot
      from a rectangular survey, so both conditions are checked
  27  the share of dwellings in the largest settlement and the nearest-neighbour
      distance, with all four districts holding the same dwelling COUNT so that
      population size is excluded as an explanation
  28  every row's acreage checked against its stated share of a section, and the
      two successive quarterings resolved to one sixteenth

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting. One stem was reworded during the pass: item
16 asked what "the photograph" would show, which `geo_check` rejects outright --
this bank can carry a table and nothing else, and a stem pointing at an image it
cannot supply is the defect that rule exists to catch. It now asks about an
aerial view in the abstract, which is a question about what a survey method
looks like rather than a promise of a picture.
"""
import re

import geo_check
import g5_2


def q26_long_lot_ratio(table):
    """Depth over frontage for every parcel, and frontage on the river for all."""
    ratios = {}
    for name, frontage, depth in table["rows"]:
        f = float(frontage.replace(",", ""))
        d = float(depth.replace(",", ""))
        assert f > 0, (name, frontage)   # every parcel touches the river
        ratios[name] = d / f
    assert len(ratios) == 4, ratios
    assert min(ratios.values()) > 20, ratios
    # Not square, and not one mile across -- the two distractors' premises.
    assert all(r > 5 for r in ratios.values()), ratios
    return "more than twenty times as deep as it is wide"


def q27_clustered_districts(table):
    """Share in the largest settlement, and nearest-neighbour distance."""
    share, near, total = {}, {}, {}
    for name, dwellings, largest, distance in table["rows"]:
        n = float(dwellings.replace(",", ""))
        total[name] = n
        share[name] = float(largest) / n
        near[name] = float(distance)
    # Equal dwelling counts, so population size cannot explain the difference.
    assert len(set(total.values())) == 1, total
    clustered = sorted(k for k in share if share[k] > 0.8 and near[k] < 50)
    dispersed = sorted(k for k in share if share[k] < 0.05 and near[k] > 700)
    assert clustered == ["District A", "District C"], (share, near)
    assert dispersed == ["District B", "District D"], (share, near)
    assert len(clustered) + len(dispersed) == 4, (clustered, dispersed)
    return "Districts A and C"


def q28_quarter_of_a_quarter(table):
    """Every row's acreage against its share, then two successive quarterings."""
    shares = {"One whole": 1.0, "One half": 0.5, "One quarter": 0.25,
              "One sixteenth": 1 / 16}
    section = None
    for _, share, acres in table["rows"]:
        if share == "One whole":
            section = float(acres.replace(",", ""))
    assert section == 640, section
    for _, share, acres in table["rows"]:
        assert float(acres.replace(",", "")) == shares[share] * section, (share, acres)
    quarter_of_quarter = section * 0.25 * 0.25
    assert quarter_of_quarter == 40, quarter_of_quarter
    return f"{quarter_of_quarter:.0f} acres"


CLAIMS = [
 ("Clustered, dispersed, and linear",
  "EK PSO-5.B.2 names exactly clustered, dispersed and linear as the classification of rural settlement patterns. The three survey methods form a separate list in EK PSO-5.B.3 and answer a different question -- how the land was divided, not where the houses stand."),

 ("Metes and bounds, township and range, and long lot",
  "EK PSO-5.B.3 names exactly these three rural survey methods. A survey method divides land into parcels, which is a different classification from EK PSO-5.B.2's account of the arrangement of dwellings relative to one another."),

 ("since the dwellings are grouped and the fields surround the group",
  "EK PSO-5.B.2 classifies settlement patterns as clustered, dispersed or linear, and the clustered case is defined by dwellings grouped together with their land lying around the group. Long lot and township and range are survey methods and cannot answer a question about settlement pattern."),

 ("since each dwelling sits separately on its own holding",
  "EK PSO-5.B.2 names dispersed among its three settlement patterns, and its defining feature is that each dwelling stands apart on the land that dwelling works. The two survey terms offered describe how parcels were laid out rather than where houses were built."),

 ("since the dwellings follow the line of the river",
  "EK PSO-5.B.2 names linear among its three settlement patterns. These dwellings are close together, but they are strung along a line rather than gathered around a centre, which is exactly what separates the linear case from the clustered one."),

 ("fixes boundaries by natural features, directions, and distances",
  "EK PSO-5.B.3 names metes and bounds among the rural survey methods, and describing a boundary by the features it passes is the method itself. It is also why parcels laid out this way take irregular shapes that follow the ground."),

 ("a rectangular survey laid out from base lines and meridians",
  "EK PSO-5.B.3 names township and range among the rural survey methods. A grid surveyed from fixed reference lines yields square parcels and a road network on the same right angles, which is why the pattern remains visible from the air."),

 ("which gives each holding a share of the frontage",
  "EK PSO-5.B.3 names long lot among the rural survey methods. Narrow strips running back from a waterway exist so that every holding touches the water, which in a landscape without roads is the transport route, the water supply and often the best soil at once."),

 ("would touch the river or road that supplied transport",
  "EK PSO-5.B.3 names long lot among the survey methods, and the shape solves a distribution problem. Frontage is the scarce and valuable thing, so cutting it into many narrow shares gives every holding access to it rather than concentrating access in a few."),

 ("received a compact block of land and built on its own block",
  "EK PSO-5.B.1 says specific agricultural practices shape rural land-use patterns, and how land is handed out is part of that. When a household's land arrives as a single square block, the point closest to all of it is the middle of the block, which is where the dwelling goes."),

 ("streams, ridges, walls, trees",
  "EK PSO-5.B.3 names metes and bounds among the survey methods, and the irregularity follows from what it takes as references. A boundary defined by a creek has the shape of the creek, which is precisely what a rectangular survey is designed to avoid."),

 ("one water source at the same moment pulls dwellings together",
  "EK PSO-5.B.1 states that specific agricultural practices shape different rural land-use patterns. Where the work is simultaneous and the water is held in common, living apart imposes a daily cost on every household and living together removes it."),

 ("places its neighbours many kilometres away",
  "EK PSO-5.B.1 says agricultural practices shape rural land-use patterns, and holding size is the most direct route from practice to pattern. If one household requires several thousand hectares, the arithmetic of area alone puts the next household a long way off."),

 ("with land use organized outward from the village",
  "EK PSO-5.B.2 classifies the settlement itself as clustered while EK PSO-5.B.1 accounts for the land-use pattern the practice produces. Plots worked from one settlement and rested in rotation leave land at different stages arranged in rings around a single centre."),

 ("a narrow strip of usable building land",
  "EK PSO-5.B.2 names linear among the settlement patterns, and a levee is one of its standard causes. Where only a narrow ribbon of ground stays dry, the buildable land is itself a line and the settlement takes the shape of the resource."),

 ("The shapes of the field and property boundaries",
  "EK PSO-5.B.3 names three methods that differ in the geometry they impose -- irregular, rectangular, and narrow strip. Boundary shape is the visible trace of that geometry, whereas EK PSO-5.B.2's settlement categories are read from where the buildings stand."),

 ("travelling to fields that may lie some distance from the village",
  "EK PSO-5.B.2 names clustered among its three patterns, and every arrangement trades one cost for another. Living together makes shared labour, services and defence easy and puts a daily journey between the household and the far edge of its own land."),

 ("so services and shared labour are harder to organize",
  "EK PSO-5.B.2 names dispersed among its three patterns. Living on one's own land removes the journey to the fields and adds distance to everything else, which is why schools and clinics in dispersed districts must serve very large areas."),

 ("meet at right angles at regular intervals",
  "EK PSO-5.B.3 names township and range as a rural survey method, and the grid is laid out before the roads are built. Building along the parcel lines is cheapest because it uses land nobody is farming, so the survey geometry is still legible a century later."),

 ("be cut down, or disappear, leaving the boundary uncertain",
  "EK PSO-5.B.3 names metes and bounds among the survey methods, and its references are physical objects rather than coordinates. A boundary running to a named tree is exact only while the tree stands, which is why such descriptions generate disputes generations later."),

 ("which strings the dwellings along the water",
  "EK PSO-5.B.2 names linear as a settlement pattern and EK PSO-5.B.3 names long lot as a survey method, and what joins them is where the value of a parcel sits. If a holding's transport, water and best land are all at one narrow end, every household builds at that end."),

 ("how dwellings are arranged relative to one another within a district",
  "EK PSO-5.B.2 classifies patterns by the arrangement of dwellings, which is something visible from one aerial view or a walk across a district. National population distribution is a different measurement taken at a different scale and answering a different question."),

 ("from astronomical reference lines without needing landmarks",
  "EK PSO-5.B.3 names all three methods, and they differ in what they use as references. A rectangular survey needs only a base line and a meridian, which makes it usable exactly where a boundary-by-landmark description would have nothing to name."),

 ("Long lot with survey method",
  "EK PSO-5.B.2 supplies clustered, dispersed and linear as settlement patterns and EK PSO-5.B.3 supplies metes and bounds, township and range and long lot as survey methods. Only one pairing here places both of its terms in the list the framework places them in."),

 ("shape different rural land-use patterns",
  "EK PSO-5.B.1 states that specific agricultural practices shape different rural land-use patterns, and how land is held and worked is part of the practice. Field size, the number and placing of dwellings and road density all follow from whether ground is farmed in blocks of a thousand hectares or of five."),

 ("more than twenty times as deep as it is wide",
  "Recomputed from the figures: every parcel's depth exceeds its frontage by a factor above twenty, and every parcel has frontage on the river. EK PSO-5.B.3 attaches that geometry to the long lot, and the verifier checks both conditions because regularity by itself would not separate this from a rectangular survey.",
  ),

 ("almost all dwellings stand in one settlement",
  "Recomputed from the figures: two districts hold more than four fifths of their dwellings in a single settlement with the nearest neighbour under 50 metres away, while the other two hold under five percent in their largest settlement and average over 700 metres between dwellings. All four record the same dwelling count, so population size cannot account for the difference.",
  ),

 ("since a quarter of a quarter is one sixteenth of a section",
  "Recomputed from the record: a section is 640 acres, each row's acreage matches its stated share of one, and two successive quarterings give one sixteenth, which is 40 acres. The description names a quarter inside a quarter rather than two quarters added together, which is the arithmetic the distractors get wrong.",
  ),

 ("so later fields, roads and field boundaries were fitted to the lines already drawn",
  "EK PSO-5.B.3 names three survey methods, and each imposes a geometry on ownership rather than on any particular crop. Ownership boundaries outlast the people who drew them because moving one takes agreement and money, so later building follows the existing lines instead of replacing them."),

 ("settlements are classified as clustered, dispersed or linear",
  "EK PSO-5.B.1, EK PSO-5.B.2 and EK PSO-5.B.3 make exactly these three claims, and the two classifications are separate lists answering different questions. Survey method and settlement pattern are strongly associated in practice without either one determining the other."),
]

# --- checks geo_check does not perform, because it takes bare anchors ---------
assert len(CLAIMS) == 30, f"{len(CLAIMS)} claims, expected 30"
LETTER_REF = re.compile(
    r"(?<![A-Za-z])(?:[Cc]hoice|[Oo]ption|[Aa]nswer)\s+\(?([A-E])\)?(?![A-Za-z])")
for n, entry in enumerate(CLAIMS, 1):
    anchor, claim = entry[0], entry[1]
    assert len(claim.split()) >= 8, f"5.2 q{n}: claim too thin to audit: {claim!r}"
    m = LETTER_REF.search(claim)
    assert not m, (
        f"5.2 q{n}: claim names an option by letter ({m.group(0)!r}); "
        "export_units.py shuffles the choices -- name the option by its content")

ANCHORS = [entry[0] for entry in CLAIMS]

TABLE_NOTES = {
    26: q26_long_lot_ratio,
    27: q27_clustered_districts,
    28: q28_quarter_of_a_quarter,
}

geo_check.check(g5_2, ANCHORS, TABLE_NOTES)
