"""Key audit for AP HUMAN GEOGRAPHY 1.2 Geographic Data.

One (anchor, claim) per item, in module order; a third element is a function
that recomputes the item's arithmetic from its own table.

WHAT MAY AND MAY NOT BE CITED HERE. Learning objective IMP-1.B prints exactly
three essential-knowledge statements:

    IMP-1.B.1  Data may be gathered in the field by organizations or by
               individuals.
    IMP-1.B.2  Geospatial technologies include geographic information systems
               (GIS), satellite navigation systems, remote sensing, and online
               mapping and visualization.
    IMP-1.B.3  Spatial information can come from written accounts in the form of
               field observations, media reports, travel narratives, policy
               documents, personal interviews, landscape analysis, and
               photographic interpretation.

That is the whole topic. The three statements are LISTS -- of collectors, of
technologies, of written sources. They do not rank sources by reliability, do
not define "quantitative" or "qualitative", and do not name a single GIS
operation. So the claims below split into two kinds, and the split is deliberate
rather than cosmetic:

  * Items 1, 2, 3, 6, 9, 10, 11, 12, 13, 16, 20 and 25 turn on membership in one
    of the CED's own lists, and their claims cite the EK.
  * Items 4, 5, 7, 8, 14, 15, 17, 18, 19, 21, 22, 23, 24 and 26-30 turn on what
    a method can and cannot record -- undercount landing in a denominator, a
    volunteered trace describing its contributors, an aggregate that cannot be
    taken apart. Those claims cite no EK, because writing "EK IMP-1.B.2" beside
    a buffering item would be a fabricated citation, and this project has
    already paid for the habit of dressing an assertion in a code.

The five table items (26-30) are the computational gate. Each function below
recomputes the loss rate, the undercount rates, the response rates, the overlay
intersection and the coverage-versus-resolution comparison from the printed
cells, so a table edited without its key being edited fails the module rather
than shipping a wrong figure to a student.

REVIEW NOTE. All 30 keys were re-derived from the questions before these anchors
were written, and none was changed. Item 27's fourth option ("Group Z ... 3
percent short") states a true figure that is nevertheless not the answer, which
is intended: the question asks for the LARGEST percentage shortfall, and an
arithmetically true distractor is what makes that reading necessary.
"""
import hg_check
from hg_check import num, numcol, column, rowdict
import g1_2


def q26_land_cover(table):
    """Forest really does fall 40 percent while built-up land nearly quintuples."""
    rows = {r[0]: r for r in table["rows"]}
    f90, f20 = num(rows["Forest"][1]), num(rows["Forest"][3])
    b90, b20 = num(rows["Built-up"][1]), num(rows["Built-up"][3])
    c90, c20 = num(rows["Cropland"][1]), num(rows["Cropland"][3])
    w90, w20 = num(rows["Water"][1]), num(rows["Water"][3])
    loss = 100 * (f90 - f20) / f90
    assert abs(loss - 40) < 1e-9, f"forest loss is {loss}%, not 40%"
    growth = b20 / b90
    assert 4.5 <= growth < 5.0, f"built-up growth is {growth}x, not nearly fivefold"
    # The three distractors that make arithmetic claims are all false.
    assert abs(100 * (c90 - c20) / c90 - loss) > 1, "cropland did not fall like forest"
    assert abs(100 * (b20 - b90) / b90 - 40) > 1, "built-up growth is not 40 percent"
    assert w20 == w90, "water area is stated as unchanged"
    return "40 percent"


def q27_undercount(table):
    """The worst undercount RATE, which is not the worst absolute shortfall."""
    rates, gaps = {}, {}
    for row in table["rows"]:
        d = rowdict(table, row)
        pub, true = num(d["Published count"]), num(d["Estimated true count"])
        rates[d["Group"]] = 100 * (true - pub) / true
        gaps[d["Group"]] = true - pub
    worst_rate = max(rates, key=rates.get)
    worst_gap = max(gaps, key=gaps.get)
    assert worst_rate == "Group X", f"worst rate is {worst_rate}"
    assert abs(rates["Group X"] - 5) < 1e-9, rates
    # The trap only works if the largest absolute shortfall belongs elsewhere.
    assert worst_gap != worst_rate, "absolute and proportional worst coincide"
    assert len(set(round(r, 6) for r in rates.values())) > 1, "rates are not all equal"
    return "Group X"


def q28_response_rate(table):
    """Lowest response rate, and it is far below the other three."""
    rates = {}
    for row in table["rows"]:
        d = rowdict(table, row)
        rates[d["District"]] = 100 * num(d["Surveys returned"]) / num(d["Surveys mailed"])
    worst = min(rates, key=rates.get)
    assert worst == "Brambly", f"lowest response rate is {worst}: {rates}"
    assert abs(rates["Brambly"] - 20) < 1e-9, rates
    others = sorted(r for k, r in rates.items() if k != worst)
    assert others[0] - rates[worst] > 30, "the gap is not decisive"
    # Ashcroft's rate is 62 percent but is NOT the lowest, which is the distractor.
    assert abs(rates["Ashcroft"] - 62) < 1e-9, rates
    return "Brambly"


def q29_overlay(table):
    """Exactly one site satisfies every requirement -- an overlay intersection."""
    passing = []
    for row in table["rows"]:
        d = rowdict(table, row)
        conds = [v for h, v in d.items() if h != "Site"]
        if all(v == "Yes" for v in conds):
            passing.append(d["Site"])
        else:
            assert sum(1 for v in conds if v == "Yes") == 2, (
                f"{d['Site']} fails more than one requirement; the distractors assume one")
    assert passing == ["Site 3"], f"sites satisfying all three: {passing}"
    return "Site 3"


def q30_source_fit(table):
    """Only one source both reaches back before 1985 and resolves below the tract."""
    early = []
    for row in table["rows"]:
        d = rowdict(table, row)
        first = d["Earliest year available"]
        if first != "n/a" and num(first) < 1985:
            early.append(d["Source"])
    assert early == ["Satellite imagery archive"], f"sources reaching 1985: {early}"
    # The census and the permits are excluded on coverage, not on resolution.
    by_source = {rowdict(table, r)["Source"]: rowdict(table, r) for r in table["rows"]}
    assert num(by_source["National census"]["Earliest year available"]) > 1985
    assert num(by_source["Municipal building permits"]["Earliest year available"]) > 1985
    assert by_source["Satellite imagery archive"]["Reporting unit"] != \
        by_source["National census"]["Reporting unit"]
    return "satellite imagery archive"


CLAIMS = [
 ("generated on site",
  "EK IMP-1.B.1 admits field collection by organizations or individuals, and IMP-1.B.3 lists field observations among the written accounts. Walking the blocks and recording each storefront on a form is first-hand generation of the record on the ground, which no other listed method is."),

 ("Satellite navigation fixes a position on Earth; a geographic information system stores, layers and analyzes spatial data",
  "EK IMP-1.B.2 lists satellite navigation systems and geographic information systems as separate geospatial technologies. A receiver reports where it is; combining, querying and mapping many layers is the analytical work a GIS does with data that already exists."),

 ("inaccessible ground",
  "Remote sensing acquires data without contact, so absence of roads is no obstacle, and an archive of past imagery lets a present-day analyst measure a 1990 condition nobody surveyed at the time. Interviews, coordinates and policy documents can supply none of that."),

 ("Overlay analysis",
  "Stacking independent layers so that one question can be asked of all of them at once is the operation a geographic information system exists to perform; EK IMP-1.B.2 names GIS as a geospatial technology. No other method in the list can relate four separate datasets to one another."),

 ("Buffering",
  "A zone of specified distance drawn around a point, line or polygon is a buffer, and its purpose is to turn a proximity question into an area other layers can be intersected with. Georeferencing, interpolation and classification each operate on the same data to a different end."),

 ("online mapping and visualization",
  "EK IMP-1.B.2's list contains both halves of the workflow described: the fresh satellite imagery is remote sensing, and the shared publicly editable web map that many contributors build and agencies consult is online mapping and visualization."),

 ("count everyone",
  "A complete enumeration is what allows results to be published for very small areas; a sample large enough to do the same everywhere would cost nearly as much as a census. That fine-grained coverage, not currency or freedom from error, is the property that makes a census irreplaceable."),

 ("less populous than they are",
  "Census undercount is spatially concentrated rather than random, so the error attaches to particular tracts instead of cancelling out. Because the count sits in the denominator of most mapped rates, an undercount inflates every per-capita figure computed for the same area."),

 ("Travel narratives",
  "EK IMP-1.B.3 lists travel narratives among the sources of spatial information. A published journal is evidence about a place and equally about the traveller's frame of reference, which is exactly why it suits a study of how outsiders understood a region."),

 ("state the reasoning",
  "EK IMP-1.B.3 lists policy documents among the written sources. Intent is a stated thing, so only a document in which a government gives its reasons records it; imagery and coordinates capture outcomes, from which intent can only be inferred."),

 ("reasons people give for moving",
  "EK IMP-1.B.3 lists personal interviews. A count of migrants establishes that movement happened and how much of it; only testimony supplies motive, which is what a study of why families left a district actually requires."),

 ("Landscape analysis",
  "EK IMP-1.B.3 lists landscape analysis among the sources geographers draw on. The method treats the visible fabric of a place -- building ages, signage, places of worship, land uses -- as an accumulated record of who occupied it and when."),

 ("sequence of images",
  "EK IMP-1.B.3 lists photographic interpretation. A single image records a state; a dated series turns those states into a chronology, which is the only way to establish when each change occurred where nobody documented it at the time."),

 ("no longer theirs",
  "Counts of housing units, car ownership shares, median rent comparisons and distances to transit are all measurements. How residents understand their own neighborhood is not a measurement, and EK IMP-1.B.3's interviews and written accounts exist to supply what a table cannot."),

 ("cannot be disaggregated",
  "Aggregation destroys internal variation: one provincial unemployment figure is equally consistent with an even spread and with extreme neighborhood concentration, and nothing in the published number distinguishes them. The remedy is data collected at the finer unit, not arithmetic on the coarser one."),

 ("Absolute location, produced by a satellite navigation system",
  "EK IMP-1.B.2 lists satellite navigation systems among the geospatial technologies, and a latitude-longitude pair states position in a fixed global reference frame rather than against another place, which is what makes it absolute rather than relative."),

 ("no longer describe the population",
  "A census is a snapshot whose usefulness decays as a place changes, and in a rapidly redeveloping district the households counted in 2010 may largely have been replaced by 2026. The source is not wrong; it is out of date for this particular purpose."),

 ("exact counts for fixed small areas",
  "The instrument follows the purpose. Legal apportionment needs defensible counts for each district, which only complete enumeration provides, while a labour-market indicator needs timeliness far more than small-area precision, which is what a repeated sample delivers cheaply."),

 ("do not yet ride is invisible",
  "Volunteered geographic data describes its contributors rather than the population. Traces are dense where cycling is already comfortable, so the evidence systematically argues for building where investment is least needed -- a self-selection problem no improvement in positioning accuracy can fix."),

 ("organizations or by individuals",
  "This restates EK IMP-1.B.1, which explicitly admits both collectors into the definition of field data and therefore covers the international office and the village cooperative alike. The other four options are genuine framework sentences from elsewhere in Unit 1 and are simply off point."),

 ("conditions under which it fails",
  "The failure described is specific and physical -- an optical sensor needs an unobstructed line of sight -- rather than evidence that remote sensing is generally inferior. Knowing each method's failure conditions is precisely what leads geographers to combine sources."),

 ("harder to dismiss",
  "Minutes record official reasoning, press coverage records contemporaneous public framing, interviews record the experience of those displaced and imagery records the physical outcome. Their independence is the point: a conclusion all four support is not an artefact of any one of them."),

 ("how residents feel",
  "Sensors record reflected electromagnetic energy, so imagery can establish that a building exists and can never record an attitude toward it. The other four pairings each match a question to a source physically or evidentially capable of answering it."),

 ("inherits every error",
  "Processing does not improve source data; it only makes the output look authoritative. A misclassified land-cover layer or a stale address file yields a clean, confident and wrong map, and nothing on the finished page signals the defect."),

 ("high-water marks",
  "EK IMP-1.B.1 distinguishes collection by organizations from collection by individuals. A weather service, a census bureau, a satellite operator and a transport ministry are institutional programmes with staff and instruments; only the residents of the street are individuals generating the record themselves."),

 ("nearly fivefold",
  "Recomputed from the table: forest falls from 42,000 to 25,200 hectares, exactly 40 percent, while built-up land rises from 4,000 to 19,800, a factor of 4.95. Cropland barely moves and water does not move at all, so the two large opposite changes are what the imagery shows.",
  q26_land_cover),

 ("Group X",
  "Recomputed from the table: shortfalls of 40,000, 30,000, 6,000 and 45,000 become rates of 2, 5, 2 and 3 percent once divided by the estimated true counts, so the largest absolute gap and the largest proportional gap belong to different groups. An undercount has to be judged as a rate.",
  q27_undercount),

 ("Brambly",
  "Recomputed from the table: response rates are 62, 20, 65 and 70 percent, so one district sits more than forty points below the others. A low rate matters because the households that answer are not a random subset of those that do not, and several hundred returns cannot repair that bias by being numerous.",
  q28_response_rate),

 ("Site 3",
  "Recomputed from the table: exactly one row is Yes on all three requirements, and each of the other three fails exactly one. An overlay retains only the area where every layer's condition holds, which makes the surviving site unique rather than merely the best on points.",
  q29_overlay),

 ("begins before 1985",
  "Recomputed from the table: only the imagery archive's record starts before 1985, since the census begins in 1991 and the permits in 2004, and of the sources listed only the imagery resolves change at 30 metres rather than at the census tract. Coverage in time and resolution in space both have to be satisfied.",
  q30_source_fit),
]

hg_check.check(g1_2, CLAIMS, per_topic=30, n_choices=5)
