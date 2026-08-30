"""Key audit for AP HUMAN GEOGRAPHY 3.2 Cultural Landscapes.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic carries two learning objectives and two
essential-knowledge statements:

    PSO-3.B.1  Cultural landscapes are combinations of physical features,
               agricultural and industrial practices, religious and linguistic
               characteristics, evidence of sequent occupance, and other
               expressions of culture including traditional and postmodern
               architecture and land-use patterns.
    PSO-3.C.1  Attitudes toward ethnicity and gender, including the role of
               women in the workforce; ethnic neighborhoods; and indigenous
               communities and lands help shape the use of space in a given
               society.

PSO-3.B.1 is a list of the INGREDIENTS a landscape combines, and membership in
it is directly citable. Items 1, 2, 3, 4, 6, 8, 9, 15, 16, 18, 24 and 26 are
keyed to that membership. The word COMBINATION is itself examinable and item 2
asks about it: a landscape is many expressions laid over one another and over a
physical base, which is why item 18 can key to one feature belonging to two
categories at once.

SEQUENT OCCUPANCE is the only technical term the statement names, and the CED
does not define it. Every key using it rests on the definition in the module
header -- successive occupation by different groups, each leaving marks that
survive into later periods -- and item 12 asks for that definition directly.
The diagnostic items (10, 22, 27) all turn on the same point: age alone shows
duration, and what identifies succession is INCONGRUITY, two organizing logics
present at once.

PSO-3.C.1 is the half of the topic that gets under-taught. It names three things
that shape the USE OF SPACE -- attitudes toward ethnicity and gender including
women's role in the workforce, ethnic neighborhoods, and indigenous communities
and lands. Items 11, 13, 14, 20, 21, 23, 25, 28, 29 and 30 are keyed to it. Its
claim is spatial rather than attitudinal: a belief becomes a geographic object
when it decides where things are put and who may be where, which item 25 states
explicitly.

Item 23 also invokes EK PSO-3.A.3's ethnocentrism from the previous topic, and
its claim says so rather than pretending the point is local to 3.2.

A NOTE ON VISUAL SOURCES, since the suggested skill here is 4.B and this bank
carries no images. No stem says "the photograph shows". Where a landscape has to
be examined, it is supplied as a real inventory table -- counts of features,
dated structures, business types, land-use shares. CLAUDE.md's standing rule is
that a prose description may never substitute for a figure; an inventory is
data, not a description, and it is what a student would count off an image
anyway.

The five table items (26-30) are the computational gate:

  26  the largest culturally specific count decides, and the dated-building rows
      are evidence of a different category
  27  four periods survive AND most of each remains in use, which is what makes
      it succession rather than ruins
  28  both retail shares sum to 100 in each year, so the shift is compositional
  29  one district's community-serving share against the other's, with the
      larger total number of businesses belonging to the district that is NOT
      the answer
  30  both columns sum to 100, so only composition is comparable

REVIEW NOTE. All 30 keys were derived from the questions before this file was
written and none needed correcting.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g3_2


def q26_largest_cultural_count(table):
    """The largest culturally specific feature count in the inventory."""
    counts = {rowdict(table, r)["Feature type"]: num(rowdict(table, r)["Count"])
              for r in table["rows"]}
    # The dated-building rows are evidence of sequent occupance, not of one of
    # the named feature categories, so they are excluded from the comparison.
    dated = [k for k in counts if "dated" in k.lower()]
    assert len(dated) == 2, counts
    specific = {k: v for k, v in counts.items() if k not in dated}
    top = max(specific, key=specific.get)
    assert top == "Bilingual street signs", specific
    assert specific["Bilingual street signs"] == 42, specific
    # It must beat the others decisively, not by one or two.
    runner_up = sorted(specific.values(), reverse=True)[1]
    assert specific[top] > 5 * runner_up, specific
    return "42 bilingual signs"


def q27_four_eras_in_use(table):
    """All four periods survive, and most of each is still in use."""
    shares, surviving = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        surv = num(d["Structures surviving"])
        used = num(d["Still in use"])
        surviving[d["Period of construction"]] = surv
        shares[d["Period of construction"]] = 100 * used / surv
    assert len(shares) == 4, shares
    assert all(v > 0 for v in surviving.values()), surviving
    assert all(v > 60 for v in shares.values()), shares
    # The share in use must rise with recency, but even the oldest must be a
    # majority, which is what separates a living landscape from a ruin field.
    ordered = [shares[p] for p in ["Before 1500", "1500-1799", "1800-1939", "1940-2019"]]
    assert all(ordered[i] <= ordered[i + 1] for i in range(len(ordered) - 1)), ordered
    assert ordered[0] > 50, ordered
    return "structures from all four periods survive"


def q28_retail_shift(table):
    """Retail composition shifts as female participation rises."""
    rows = sorted((num(rowdict(table, r)["Year"]),
                   num(rowdict(table, r)["Female labour force participation (%)"]),
                   num(rowdict(table, r)["Retail floor space within 400 m of housing (%)"]),
                   num(rowdict(table, r)["Retail floor space at transport nodes and out of town (%)"]))
                  for r in table["rows"])
    for _, _, near, far in rows:
        assert near + far == 100, (near, far)
    (_, p0, near0, far0), (_, p1, near1, far1) = rows
    assert p1 > 2 * p0, (p0, p1)
    assert near1 < near0 and far1 > far0, (near0, near1, far0, far1)
    assert near0 > 70 and near1 < 40, (near0, near1)
    return "shifted from near housing to transport nodes"


def q29_ethnic_neighbourhood(table):
    """Community-serving share, against the larger raw business count."""
    d1, d2 = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        d1[d["Business type"]] = num(d["District 1"])
        d2[d["Business type"]] = num(d["District 2"])
    serving = "Serving one origin community in its own language"
    t1, t2 = sum(d1.values()), sum(d2.values())
    assert d2[serving] == 84 and t2 == 128, (d2, t2)
    assert d2[serving] / t2 > 0.6, (d2[serving], t2)
    assert d1[serving] / t1 < 0.1, (d1[serving], t1)
    # The district with MORE businesses in total must not be the answer.
    assert t1 > t2, (t1, t2)
    # Community institutions must be concentrated in the same district.
    for row_name in ("Places of worship of the community's tradition",
                     "Community associations and language schools"):
        assert d2[row_name] > d1[row_name], (row_name, d1[row_name], d2[row_name])
    return "84 of its 128 businesses"


def q30_land_authority(table):
    """Two composition columns; seasonal and protected uses dominate one."""
    ind = numcol(table, "Indigenous-titled area (% of land)")
    free = numcol(table, "Adjacent freehold area (% of land)")
    assert sum(ind) == 100 and sum(free) == 100, (sum(ind), sum(free))
    uses = column(table, "Land use")
    seasonal = uses.index("Managed burning and seasonal harvest")
    protected = uses.index("Protected ceremonial and habitat areas")
    cultivated = uses.index("Continuous cultivation")
    assert ind[seasonal] + ind[protected] == 89, (ind[seasonal], ind[protected])
    assert free[seasonal] + free[protected] == 4, (free[seasonal], free[protected])
    assert free[cultivated] > 10 * ind[cultivated], (ind[cultivated], free[cultivated])
    # The "unused" reading must be false: the indigenous column is fully
    # allocated to named uses, none of which is idleness.
    assert all(v >= 0 for v in ind) and min(ind) > 0, ind
    return "seasonal and protected uses"


CLAIMS = [
 ("combination of physical features, agricultural and industrial practices",
  "EK PSO-3.B.1 gives this list, and the operative word is combination: a cultural landscape is the accumulated result of many kinds of human activity on a physical base rather than any single feature of it."),

 ("many different expressions of culture at once",
  "EK PSO-3.B.1 lists at least five kinds of ingredient in one sentence. Reading a landscape means separating those layers, which is only possible if they are understood to be present together rather than as alternatives to one another."),

 ("linguistic characteristic and the ruined walls are evidence of sequent occupance",
  "EK PSO-3.B.1 names religious and linguistic characteristics and evidence of sequent occupance as separate ingredients. Bilingual signage records which languages are used and by whom, while surviving walls record who was there before."),

 ("ridge line along which a settlement is strung",
  "EK PSO-3.B.1 includes physical features among the ingredients a landscape combines, and a ridge is there whether or not anyone builds on it. Roofs, signs, boundaries and places of worship are all human works placed on that base."),

 ("successive groups have each left marks",
  "EK PSO-3.B.1 names evidence of sequent occupance among the ingredients of a cultural landscape. What makes four eras in simultaneous use the clearest case is that the earlier ones survive rather than having been erased by the later."),

 ("blast furnaces and rail sidings, matched to industrial practices",
  "EK PSO-3.B.1 names agricultural and industrial practices among the ingredients of a cultural landscape, and furnaces with rail sidings are the industrial case. Every other pairing attaches a feature to a category it does not belong to."),

 ("what the society that built it considered important enough",
  "EK PSO-3.B.1 names religious characteristics among the ingredients of a cultural landscape, and what a landscape records is the decision rather than the belief. Where a building is placed and how much of a settlement defers to it are observable facts."),

 ("Agricultural practices, one of the ingredients the framework lists",
  "EK PSO-3.B.1 names agricultural and industrial practices together as one of a landscape's ingredients. Silos, canals and machinery sheds are the physical apparatus of a particular way of farming, and they record which way that is."),

 ("Both inherited building forms and deliberately contemporary ones",
  "EK PSO-3.B.1 names traditional and postmodern architecture explicitly and puts them in a single clause. A landscape is not made cultural by being old, and a glass tower records the values of its moment exactly as a courtyard house records those of its own."),

 ("overlaid by roads following an entirely different one",
  "Sequent occupance shows as incongruity: two organizing systems present at once because a later group imposed its own without erasing the earlier one. A uniform pattern is evidence of a single occupation rather than of several."),

 ("ethnic neighbourhoods help shape the use of space",
  "EK PSO-3.C.1 names ethnic neighborhoods explicitly among the things that shape the use of space in a society. The concentration is not merely demographic: it reorganizes which businesses, institutions and signage occupy a district."),

 ("successive occupation of a place by different cultural groups",
  "EK PSO-3.B.1 names evidence of sequent occupance without defining it, and the standard definition turns on persistence. If each occupation erased the last there would be nothing to observe, so it is the survival of earlier layers that makes it visible."),

 ("attitudes toward gender, including the role of women in the workforce",
  "EK PSO-3.C.1 names attitudes toward gender and the role of women in the workforce among the things shaping the use of space. Where shops are put follows from when and how people can reach them, which follows from who is working where."),

 ("organized by the community's own priorities",
  "EK PSO-3.C.1 names indigenous communities and lands among the things shaping the use of space in a society. Who decides how land is used determines what appears on it, so a change in that authority becomes a change in the landscape over time."),

 ("languages appearing on shop fronts, street signs, and gravestones",
  "EK PSO-3.B.1 names linguistic characteristics among the ingredients of a cultural landscape. Public writing is where language becomes visible in space, and which language appears where records status as well as usage."),

 ("expressed as land-use patterns",
  "EK PSO-3.B.1 names land-use patterns among the expressions of culture a landscape combines. A street layout encodes what its designers assumed about cars, work and daily life, which is why layouts change when those assumptions do."),

 ("accumulates from countless separate decisions",
  "EK PSO-3.B.1 makes a landscape a combination of many ingredients, and nobody combines them deliberately. Each boundary, roof and sign was placed by someone pursuing their own end, and the assemblage records a society no one set out to describe."),

 ("also evidence of sequent occupance if a later use has been built around them",
  "EK PSO-3.B.1 names industrial practices and evidence of sequent occupance as separate ingredients, and disused works can be both at once. One feature belonging to two categories is exactly what the word combination in that statement permits."),

 ("who holds the resources and authority to reshape space",
  "EK PSO-3.B.1 makes the landscape an expression of culture, and expressions change when the people making them change or acquire new means. Two centuries of stability followed by a decade of rebuilding is a statement about power and capital rather than about geology."),

 ("which groups could buy property in which districts",
  "EK PSO-3.C.1 names attitudes toward ethnicity among the things shaping the use of space. A rule about who may live where converts an attitude directly into a map, and the resulting pattern outlasts the rule by decades."),

 ("embodies an assumption about gender roles that no longer holds",
  "EK PSO-3.C.1 names the role of women in the workforce among the things shaping the use of space. A built layout is durable while the assumptions behind it are not, so rising participation leaves a district organized around a household that has stopped existing."),

 ("different and incompatible principles, dated to different periods",
  "Age alone shows duration rather than succession, since a single culture can build over centuries. What identifies sequent occupance is incongruity -- two organizing logics present at once because different groups imposed them at different times."),

 ("mistaking a different use for no use",
  "EK PSO-3.C.1 names indigenous communities and lands among the things shaping the use of space, and EK PSO-3.A.3's ethnocentrism is the attitude on display. A category built for one system of land use fails to register another and reports it as absence."),

 ("record religion, language, ethnicity, and status together",
  "EK PSO-3.B.1 names religious and linguistic characteristics among a landscape's ingredients, and a cemetery carries both at once with dated evidence of who was present. Concentrating several categories in one readable place is what makes it efficient evidence."),

 ("through where things are placed and who may be where",
  "EK PSO-3.C.1's claim is spatial by construction: attitudes toward ethnicity and gender shape the USE of space. That is what makes a belief a geographic object, since it can then be found in a map of who lives where and what is built for whom."),

 ("42 bilingual signs",
  "Recomputed from the inventory: 42 bilingual signs is more than five times any other culturally specific count in the table. The verifier excludes the two dated-building rows from the comparison, since those are evidence of sequent occupance rather than of one of the named feature categories.",
  q26_largest_cultural_count),

 ("structures from all four periods survive",
  "Recomputed from the table: all four periods are represented and the share still in use runs 64, 82, 83 and 96 percent, rising with recency but never falling below a majority. A landscape holding four eras simultaneously in working use is what sequent occupance produces.",
  q27_four_eras_in_use),

 ("shifted from near housing to transport nodes",
  "Recomputed from the table: participation rises from 31 to 67 percent while retail near housing falls from 78 to 34 and retail at transport nodes rises from 22 to 66, with each year's two shares summing to 100. EK PSO-3.C.1 names women's role in the workforce among the things shaping the use of space.",
  q28_retail_shift),

 ("84 of its 128 businesses",
  "Recomputed from the table: one district records 84 of 128 businesses serving a single community in its own language, with more places of worship and more community institutions than its neighbour. The verifier confirms the district with the larger total number of businesses is the other one, so size is not what identifies an ethnic neighbourhood.",
  q29_ethnic_neighbourhood),

 ("seasonal and protected uses",
  "Recomputed from the table: both columns sum to 100, and seasonal management plus protected areas hold 89 percent of one area against 4 percent of the other while continuous cultivation runs 6 against 71. Every hectare of the indigenous-titled column is allocated to a named use, which is what disposes of the 'unused' reading.",
  q30_land_authority),
]

hg_check.check(g3_2, CLAIMS, per_topic=30, n_choices=5)
