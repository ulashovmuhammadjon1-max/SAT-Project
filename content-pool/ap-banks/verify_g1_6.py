"""Key audit for AP HUMAN GEOGRAPHY 1.6 Scales of Analysis.

One (anchor, claim) per item, in module order; a third element recomputes the
item's arithmetic from its own table.

WHAT MAY BE CITED. This topic carries two learning objectives and two essential
knowledge statements:

    PSO-1.C.1  Scales of analysis include global, regional, national, and local.
    PSO-1.D.1  Patterns and processes at different scales reveal variations in,
               and different interpretations of, data.

PSO-1.C.1 is a closed list of four names, and items 1, 2, 3, 4, 6, 12, 14, 21
and 24 are keyed to membership in it and cite it. PSO-1.D.1 is the sentence with
real content -- the same data support different interpretations at different
scales -- and items 8, 9, 11, 13, 15, 17, 18, 19, 20, 23, 25 and every table
item are keyed to it and cite it.

Items 5, 7, 10, 16 and 22 cite nothing. Their keys rest on things the CED does
not state: that cartographic scale and scale of analysis are independent, that
an ecological fallacy carries an aggregate relationship illegitimately down to
individuals, and that the scale of evidence and the scale of a claim are
separate. These are standard course reasoning rather than framework sentences,
and attaching a code to them would be a fabricated citation.

The five table items (26-30) are the computational gate, and four of the five
exist to make an aggregation effect undeniable rather than merely asserted:

  26  a population-weighted national mean sits ABOVE three of four regions,
      because one small region is very rich
  27  a national pass rate RISES while the rate falls in both regions, purely
      from a shift in where the candidates are -- the item is a small,
      deliberately exact instance of the composition effect
  28  the population-weighted share (22.6%) and the unweighted mean of the
      district percentages (28.75%) differ, and the district with the highest
      RATE is not the district with the most affected households
  29  a national total is flat while one province loses 18,000 square
      kilometers, the losses netted off against gains elsewhere

Each function recomputes those figures from the printed cells and asserts the
effect is really present, so a table edited without its key being edited fails
the module rather than teaching a wrong number.

REVIEW NOTE. Item 26's first draft printed a national average of $9,880, which
was simply wrong: population-weighting the four regions gives $10,320. The error
was found by writing the recompute function, which is the argument for writing
one for every data item rather than only for the ones that look arithmetical.
No key was changed; all 30 were derived from the questions before this file was
written.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g1_6


def q26_weighted_mean(table):
    """A population-weighted national mean, not the average of four regions."""
    pops, gdps = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        pops[d["Region"]] = num(d["Population (millions)"])
        gdps[d["Region"]] = num(d["GDP per capita (US$)"])
    national = sum(pops[r] * gdps[r] for r in pops) / sum(pops.values())
    assert abs(national - 10320) < 1e-6, f"national mean is {national}"
    above = [r for r in gdps if gdps[r] < national]
    assert len(above) == 3, f"regions below the national mean: {above}"
    # The capital must be far above it, or the item has no point.
    assert gdps["Capital region"] > 3 * national, gdps
    return "$10,320"


def q27_composition(table):
    """The national rate rises while BOTH regional rates fall."""
    tot10 = tot20 = pass10 = pass20 = 0.0
    for row in table["rows"]:
        d = rowdict(table, row)
        n10, r10 = num(d["2010 candidates"]), num(d["2010 pass rate"]) / 100
        n20, r20 = num(d["2020 candidates"]), num(d["2020 pass rate"]) / 100
        assert r20 < r10, f"{d['Region']} did not fall: {r10} -> {r20}"
        tot10 += n10
        tot20 += n20
        pass10 += n10 * r10
        pass20 += n20 * r20
    nat10 = 100 * pass10 / tot10
    nat20 = 100 * pass20 / tot20
    assert abs(nat10 - 65) < 1e-9 and abs(nat20 - 80) < 1e-9, (nat10, nat20)
    assert nat20 > nat10, "the national rate did not rise"
    assert tot10 == tot20, "the candidate total changed, which muddies the effect"
    return "rose from 65 to 80 percent"


def q28_weighted_share(table):
    """Weighted share, unweighted mean, and which district holds the most."""
    hh, share, count = {}, {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        hh[d["District"]] = num(d["Households"])
        share[d["District"]] = num(d["Households without a car (%)"])
        count[d["District"]] = hh[d["District"]] * share[d["District"]] / 100
    weighted = 100 * sum(count.values()) / sum(hh.values())
    unweighted = sum(share.values()) / len(share)
    assert abs(weighted - 22.6) < 1e-9, weighted
    assert abs(unweighted - 28.75) < 1e-9, unweighted
    assert round(weighted) == 23 and round(unweighted) == 29, (weighted, unweighted)
    # The highest RATE and the highest COUNT must be different districts.
    assert max(share, key=share.get) != max(count, key=count.get), (share, count)
    assert sum(count.values()) == 11300, count
    return "About 23 percent"


def q29_netting(table):
    """The province rows sum to the national row in both years, and still hide a loss."""
    by_unit = {rowdict(table, r)["Unit"]: rowdict(table, r) for r in table["rows"]}
    provinces = [u for u in by_unit if u != "National total"]
    y0, y1 = "Forest area 2000 (km2)", "Forest area 2020 (km2)"
    for year in (y0, y1):
        s = sum(num(by_unit[p][year]) for p in provinces)
        assert s == num(by_unit["National total"][year]), (year, s)
    assert num(by_unit["National total"][y0]) == num(by_unit["National total"][y1]), \
        "the national total is not flat"
    changes = {p: num(by_unit[p][y1]) - num(by_unit[p][y0]) for p in provinces}
    worst = min(changes, key=changes.get)
    assert changes[worst] == -18000, changes
    assert sum(changes.values()) == 0, changes
    return "18,000 square kilometers"


def q30_multiscale(table):
    """National growth is positive while two sub-national units are negative."""
    rows = [rowdict(table, r) for r in table["rows"]]
    col = "Population change 2010-2020 (%)"
    national = [num(d[col]) for d in rows if d["Scale"] == "National"]
    sub = [num(d[col]) for d in rows if d["Scale"] != "National"]
    assert len(national) == 1 and national[0] > 0, national
    assert sum(1 for v in sub if v < 0) == 2, sub
    # The distractor offering the mean of the sub-national rows must be wrong.
    assert abs(sum(sub) / len(sub) - national[0]) > 1, (sub, national)
    biggest = max(rows[1:], key=lambda d: num(d[col]))
    assert biggest["Unit"] == "Capital city", biggest
    return "concentrated on the coast and in the capital"


CLAIMS = [
 ("the frame of comparison is the whole world",
  "EK PSO-1.C.1 names global among the four scales of analysis, and the scale is fixed by the extent over which comparison is drawn. A study covering every country on Earth compares globally even though each reported value belongs to one country."),

 ("across the units of a single country",
  "EK PSO-1.C.1 lists global, regional, national and local as the four scales. What fixes the scale is the extent within which variation is being examined, and here that extent is one country's own internal divisions."),

 ("a group of neighboring countries rather than the world or one state",
  "EK PSO-1.C.1 names regional as a scale distinct from both global and national. A study bounded by a multi-country world region is regional by construction, whatever scale the individual moves inside it occur at."),

 ("subdivisions of a single city",
  "EK PSO-1.C.1 lists local as one of the four scales, and it is the finest of them. The unit of comparison here is a neighborhood and the extent is one city, which is exactly what the local scale denotes."),

 ("the two are independent",
  "Cartographic scale is a ratio between map distance and ground distance, while scale of analysis is the extent being reasoned about, so one street map can appear inside a study comparing a hundred cities worldwide. Collapsing the two is the most common scale error in this course, and the CED does not state the distinction, so no code is cited for it."),

 ("across the states of one federation",
  "EK PSO-1.C.1's national scale means the frame of the comparison is one country and its internal divisions. A worldwide comparison is global, a set of neighboring countries is regional, and villages or city blocks are local."),

 ("one growth figure for the whole country",
  "The question asked is about internal variation, and a single national figure contains none by construction. Every coarsening of the unit averages away more of the pattern, and reporting one unit averages away all of it."),

 ("disappear or reverse at another",
  "EK PSO-1.D.1 states that patterns and processes at different scales reveal variations in, and different interpretations of, data. The claim is about the data behaving differently under aggregation, not about accuracy or about analysts disagreeing."),

 ("reveals an internal inequality that the national average conceals",
  "An average is a real summary of the values beneath it and carries no information about their spread, so a high mean is entirely consistent with wide internal inequality. EK PSO-1.D.1 names that divergence between scales as the expected result rather than a contradiction."),

 ("relationship among aggregates need not hold for the individuals",
  "Aggregate correlations can arise from composition and from confounders that vary between countries rather than within them, so carrying a between-unit finding down to individuals is unwarranted. The CED does not name this fallacy, so the claim is argued rather than cited."),

 ("weighted sum of many local changes",
  "EK PSO-1.D.1's interpretive variation appears here as arithmetic: an aggregate moves with the weighted total of its components, so a large rise in a small component is easily outweighed. Both the national fall and the district rise can be true at once."),

 ("birth rates highest -- global; where in this city",
  "EK PSO-1.C.1 lists the four scales, and the appropriate one is the extent the question ranges over. A worldwide ranking requires global coverage while a within-city ranking requires units finer than the city itself."),

 ("analysis at only one of them will miss part of it",
  "EK PSO-1.D.1 holds that different scales reveal different aspects of the same phenomenon. A study confined to the treaty misses the flooded street and one confined to the street misses the treaty, so the scales are complementary rather than mutually exclusive."),

 ("across the countries of the Sahel",
  "EK PSO-1.C.1's regional scale sits between national and global and denotes a group of neighboring countries or a coherent portion of a continent. A worldwide comparison is global and comparisons inside one country are national or local."),

 ("the rule of aggregation is part of the result",
  "Summing ballots nationally and summing them district by district are two different operations on the same votes, and they disagree because districts differ in size and margin. EK PSO-1.D.1's claim about differing interpretations is made concrete by that disagreement."),

 ("because the question asks about variation inside the city",
  "The unit must be finer than the thing being compared or there is nothing to compare, and coarser than the individual or the rates become unstable and personally identifying. Matching the unit to the question is the reasoning here, and no framework sentence states it."),

 ("a national total can be produced by a small number of places",
  "A national figure is a sum, and a sum carries no information about how evenly its contributions are distributed among the places producing it. Concentration inside a country is invisible from outside, which is why EK PSO-1.D.1 asks for more than one scale."),

 ("old-growth forest is cleared in one region and plantations expand",
  "A national total nets gains against losses and conceals both their location and their character, so a flat figure is compatible with very large offsetting changes. EK PSO-1.D.1's point about differing interpretations is precisely what a net figure hides."),

 ("a single shade per country is exactly an assertion of uniformity",
  "A choropleth assigns one value to the whole of each unit, so its visual claim is homogeneity even where the underlying distribution is extremely uneven. EK PSO-1.D.1 covers this: the interpretation follows from the unit chosen, not only from the data."),

 ("read against several different frames",
  "Comparing one value against national and continental benchmarks is an explicit multi-scale exercise, and the region's apparent performance shifts with the frame chosen. EK PSO-1.D.1 is the statement that makes that shift expected rather than surprising."),

 ("nested in extent",
  "EK PSO-1.C.1 lists four distinct scales and EK PSO-1.D.1 states that they reveal different interpretations; nesting is what makes the second sentence possible. Aggregation is a real operation that can change what the same data show."),

 ("the fieldwork is local while the analytical frame is global",
  "The scale at which evidence is gathered and the scale at which a claim is made are separate, and the second has to be argued rather than assumed. Saying so is what distinguishes a defensible generalization from an overreach, and the CED does not state it, so no code is cited."),

 ("where incomes are high and low",
  "Disaggregation adds no data; it stops discarding the spatial information the data already carried. The national figure is not made more accurate by being mapped, and medians do not sum, so the gain has to be stated as location rather than as precision."),

 ("crosses national borders and is shared by neighboring countries",
  "EK PSO-1.C.1 offers regional as a scale precisely for processes wider than a state and narrower than the world. The scale should match the extent of the process rather than the convenience of the data, since a national frame cuts a shared basin or drought into pieces."),

 ("more than fifty countries as one unit",
  "Reading a continental block off a global map and then speaking as though it were homogeneous is the scale error EK PSO-1.D.1 warns about. The correction is not that the map is wrong but that the conclusion was drawn at a coarser scale than the variation it describes."),

 ("above the level enjoyed in three of the four regions",
  "Recomputed from the table: weighting each regional figure by its population gives a national mean of $10,320, which exceeds three of the four regional figures and is less than a third of the capital's. One small very rich region is enough to pull a mean above most of the population it describes.",
  q26_weighted_mean),

 ("rose from 65 to 80 percent",
  "Recomputed from the table: 78 passes of 120 candidates in 2010 is 65 percent and 96 of 120 in 2020 is 80 percent, while both regional rates fell. The national rate rose because candidates shifted toward the higher-performing region, which is a change in composition rather than in performance.",
  q27_composition),

 ("About 23 percent",
  "Recomputed from the table: 2,400 plus 2,400 plus 3,000 plus 3,500 is 11,300 of 50,000 households, or 22.6 percent, while the unweighted mean of the four district percentages is 28.75. The verifier also confirms the district with the highest rate is not the district holding the most carless households.",
  q28_weighted_share),

 ("18,000 square kilometers",
  "Recomputed from the table: the three provinces sum to 80,000 square kilometers in both years, so the national row is internally consistent, yet one province fell by 18,000 while the other two gained 16,000 and 2,000. A net figure conceals the size and the location of offsetting change alike.",
  q29_netting),

 ("concentrated on the coast and in the capital",
  "Recomputed from the table: the national row is positive while two of the four sub-national rows are negative, and the largest gain belongs to the capital city. Averaging the four sub-national percentages would give plus 3.5, which is not how a population-weighted national figure is formed.",
  q30_multiscale),
]

hg_check.check(g1_6, CLAIMS, per_topic=30, n_choices=5)
