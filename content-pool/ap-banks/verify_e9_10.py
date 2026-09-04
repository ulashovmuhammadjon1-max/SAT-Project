"""Key audit for AP ENVIRONMENTAL SCIENCE 9.10 Human Impacts on Biodiversity.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  EIN-4.C.1  HIPPCO -- habitat destruction, invasive species, population
             growth, pollution, climate change, and over exploitation --
             describes the main factors leading to a decrease in biodiversity
                 -- items 1, 2, 3, 15, 19, 20, 21, 30
  EIN-4.C.2  habitat fragmentation occurs when large habitats are broken into
             smaller, isolated areas; its causes include the construction of
             roads and pipelines, clearing for agriculture or development, and
             logging -- items 4, 5, 12, 15, 16, 21, 22, 25, 30
  EIN-4.C.3  the scale of fragmentation having an adverse effect will vary from
             species to species within that ecosystem -- items 6, 14, 23, 24, 30
  EIN-4.C.4  global climate change can cause habitat loss via changes in
             temperature, precipitation, and sea level rise
                 -- items 7, 15, 17, 26, 27, 30
  EIN-4.C.5  some organisms have been somewhat or completely domesticated and
             are managed for economic returns, such as honeybee colonies and
             domestic livestock, and this can have a negative impact on the
             biodiversity of that organism -- items 8, 9, 10, 13, 15, 28, 30
  EIN-4.C.6  mitigations include creating protected areas, use of habitat
             corridors, promoting sustainable land use practices, and restoring
             lost habitats -- items 3, 11, 12, 15, 18, 29, 30

THE OVERLAP WITH UNIT 2 AND WITH TOPICS 9.8 AND 9.9 IS KEPT OUT BY DESIGN. The
levels of biodiversity and the order in which habitat loss removes species are
ERT-2.A (topic 2.1); what an invasive species is is EIN-4.A (topic 9.8); how a
species becomes endangered, and the poaching and legislation strategies, are
EIN-4.B (topic 9.9). No key here defines biodiversity, defines an invasive
species, or names a strategy from EIN-4.B.5. What this topic owns is HIPPCO as a
list, fragmentation and its causes, the species-by-species scale of its effect,
climate change as a route to habitat loss, domestication, and EIN-4.C.6's four
mitigations.

THE FRAMEWORK RANKS NOTHING HERE, and no key does either. It gives no order
among HIPPCO's six factors and no order among the four mitigations, so items 20
and 29 state in terms that the sizes they report are properties of their own
record. EIN-4.C.3 likewise gives no fragment size at which harm begins, so item
14 refuses one rather than supplying it.

THE CROSS-SIDE SWAP IS THE TRAP THIS TOPIC SETS: habitat corridors and
protected areas are MITIGATIONS, while clearing and logging are CAUSES, and
each list is a plausible distractor for the other. Items 3, 12 and 15 each put a
member of one list among the other, and their anchors name the item together
with the side it is being wrongly placed on.

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run.

DATA ITEMS: 19 to 29 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e9_10

LOSSES = "Species losses in the region attributed to it"
PIECES = "Separate pieces the habitat has been broken into"
PIECE_AREA = "Mean area of one piece (hectares)"
SPECIES_LEFT = "Number of species still present"
THRESHOLD = "Smallest piece of habitat in which it still breeds (hectares)"
BIG_ENOUGH = "Percent of the region's pieces large enough for it"
EDGE = "Kilometres of new habitat edge it created"
MADE_PIECES = "Separate pieces of habitat it created"
TEMPRISE = "Rise in mean temperature (degrees Celsius)"
PRECIP = "Change in yearly precipitation (millimetres)"
SEALEVEL = "Rise in sea level (centimetres)"
HABITAT_LOST = "Habitat lost (hectares)"
GENERATIONS = "Generations under human management"
LINES = "Distinct genetic lines remaining in it"
MEASURE_AREA = "Area it covers (thousands of hectares)"
SPECIES_CHANGE = "Percent change in the species count after ten years"

# EIN-4.C.1's own six, in the framework's order.
HIPPCO = ["Habitat destruction", "Invasive species", "Population growth",
          "Pollution", "Climate change", "Over exploitation"]
# EIN-4.C.2's three named causes.
FRAG_CAUSES = ["Construction of roads and pipelines",
               "Clearing for agriculture or development", "Logging"]
# EIN-4.C.6's four named mitigations.
MITIGATIONS = ["Creating a protected area", "Use of habitat corridors",
               "Promoting sustainable land use practices", "Restoring lost habitat"]


def _rising(values):
    return all(values[i + 1] > values[i] for i in range(len(values) - 1))


def _falling(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def q19(table, item):
    labels = cg.labels(table)
    assert labels == HIPPCO, \
        f"the record must carry exactly the six factors the framework names; got {labels}"
    losses = cg.col(table, LOSSES)
    assert all(v > 0 for v in losses), \
        f"every factor must be credited with some loss, so 'one is credited with none' is false; got {losses}"
    assert len(set(losses)) == len(losses), \
        "the six counts must differ, so 'every factor is credited with the same' is false"
    return (f"the six rows are {labels}, the framework's own list, and each carries a "
            f"positive and distinct count, {losses}")


def q20(table, item):
    labels = cg.labels(table)
    losses = cg.col(table, LOSSES)
    top = max(range(len(losses)), key=lambda i: losses[i])
    assert labels[top] == "Habitat destruction", \
        f"the largest count must belong to habitat destruction; got {labels[top]}"
    assert len([v for v in losses if v == losses[top]]) == 1, \
        "that largest count must be unique"
    return (f"the counts read {losses}, whose single largest, {losses[top]:.0f}, belongs to "
            f"{labels[top]}")


def q21(table, item):
    pieces = cg.col(table, PIECES)
    area = cg.col(table, PIECE_AREA)
    species = cg.col(table, SPECIES_LEFT)
    assert _rising(pieces), f"the number of pieces must rise down the record; got {pieces}"
    assert _falling(area), f"the mean piece must shrink as the pieces multiply; got {area}"
    assert _falling(species), f"the species present must fall; got {species}"
    return (f"down the record the pieces read {pieces}, rising, the mean piece {area} "
            f"hectares, falling, and the species present {species}, falling")


def q22(table, item):
    labels = cg.labels(table)
    pieces = cg.col(table, PIECES)
    area = cg.col(table, PIECE_AREA)
    species = cg.col(table, SPECIES_LEFT)
    worst = max(range(len(pieces)), key=lambda i: pieces[i])
    assert worst == min(range(len(area)), key=lambda i: area[i]), \
        "the most fragmented landscape must also hold the smallest pieces"
    assert worst == min(range(len(species)), key=lambda i: species[i]), \
        "it must also hold the fewest species"
    assert labels[worst] == "Landscape 4", \
        f"that landscape must be Landscape 4; got {labels[worst]}"
    return (f"{labels[worst]} holds {pieces[worst]:.0f} pieces of {area[worst]:.0f} "
            f"hectares each, the most and the smallest, and {species[worst]:.0f} species, "
            "the fewest")


def q23(table, item):
    thresholds = cg.col(table, THRESHOLD)
    enough = cg.col(table, BIG_ENOUGH)
    assert len(set(thresholds)) == len(thresholds), \
        f"the four thresholds must differ, or the species-by-species claim is not shown; got {thresholds}"
    pairs = sorted(zip(thresholds, enough))
    assert _falling([e for _, e in pairs]), \
        f"the share of pieces large enough must fall as the threshold rises; got {pairs}"
    assert max(enough) < 100, "'every species finds every piece large enough' must be false"
    assert min(enough) > 0, "'no species finds any piece large enough' must be false"
    return (f"the breeding thresholds read {thresholds} hectares, all different, and the "
            f"share of pieces large enough {enough} percent, falling as the threshold rises")


def q24(table, item):
    labels = cg.labels(table)
    thresholds = cg.col(table, THRESHOLD)
    enough = cg.col(table, BIG_ENOUGH)
    first = max(range(len(thresholds)), key=lambda i: thresholds[i])
    assert first == min(range(len(enough)), key=lambda i: enough[i]), \
        "the largest threshold must go with the smallest share of usable pieces"
    assert labels[first] == "Species 4", \
        f"that species must be Species 4; got {labels[first]}"
    return (f"{labels[first]} needs {thresholds[first]:.0f} hectares, the largest "
            f"threshold, and finds only {enough[first]:.0f} percent of the pieces large "
            "enough, the smallest share")


def q25(table, item):
    labels = cg.labels(table)
    edge = dict(zip(labels, cg.col(table, EDGE)))
    made = dict(zip(labels, cg.col(table, MADE_PIECES)))
    for cause in FRAG_CAUSES:
        assert cause in labels, f"the record must carry the framework's cause {cause!r}"
        assert edge[cause] > 0 and made[cause] > 0, \
            f"{cause!r} must have created both edge and separate pieces; got {edge[cause]} and {made[cause]}"
    others = [lab for lab in labels if lab not in FRAG_CAUSES]
    assert len(others) == 1, f"exactly one row must lie outside the framework's causes; got {others}"
    assert edge[others[0]] == 0 and made[others[0]] == 0, \
        f"{others[0]!r} must have created neither edge nor pieces; got {edge[others[0]]} and {made[others[0]]}"
    return (f"the three rows {FRAG_CAUSES} are the framework's named causes and each "
            f"created edge and separate pieces, while {others[0]} created neither")


def q26(table, item):
    lost = cg.col(table, HABITAT_LOST)
    for driver in (TEMPRISE, SEALEVEL):
        pairs = sorted(zip(cg.col(table, driver), lost))
        assert _rising([h for _, h in pairs]), \
            f"sorted by {driver!r} the habitat lost must rise strictly; got {pairs}"
    by_rain = sorted(zip(cg.col(table, PRECIP), lost))
    assert _falling([h for _, h in by_rain]), \
        f"the habitat lost must fall as the precipitation change becomes less negative; got {by_rain}"
    assert all(p < 0 for p in cg.col(table, PRECIP)), \
        "'precipitation rose at every site' must be false"
    assert len(set(lost)) == len(lost), "'every site lost the same area' must be false"
    return (f"sorted by the temperature rise, by the fall in precipitation and by the sea "
            f"level rise in turn, the habitat lost reads {sorted(lost)} hectares each time")


def q27(table, item):
    lost = cg.col(table, HABITAT_LOST)
    gap = max(lost) - min(lost)
    assert abs(gap - 1620) < 1e-9, f"the difference must be 1,620 hectares; got {gap}"
    return (f"the habitat lost runs from {min(lost):.0f} to {max(lost):.0f} hectares, a "
            f"difference of {gap:.0f}")


def q28(table, item):
    generations = cg.col(table, GENERATIONS)
    lines = cg.col(table, LINES)
    assert generations[0] == 0, \
        f"the first row must be the unmanaged reference; got {generations[0]}"
    assert _rising(generations), \
        f"the generations under management must rise down the record; got {generations}"
    assert _falling(lines), \
        f"the distinct genetic lines must fall as management lengthens; got {lines}"
    return (f"down the record the generations under management read {generations}, rising "
            f"from none, and the distinct genetic lines {lines}, falling throughout")


def q29(table, item):
    labels = cg.labels(table)
    assert labels == MITIGATIONS, \
        f"the record must carry exactly the four mitigations the framework names; got {labels}"
    change = cg.col(table, SPECIES_CHANGE)
    area = cg.col(table, MEASURE_AREA)
    assert all(c > 0 for c in change), \
        f"every measure must be followed by a rise, so 'one is followed by a fall' is false; got {change}"
    assert len(set(change)) == len(change), \
        "the four changes must differ, so 'every measure is followed by the same change' is false"
    assert len(set(area)) == len(area), "the four areas must differ"
    largest_area = max(range(len(area)), key=lambda i: area[i])
    largest_rise = max(range(len(change)), key=lambda i: change[i])
    assert largest_area != largest_rise, \
        "'the measure covering the largest area brings the largest rise' must be false"
    return (f"the four rows are {labels}, the framework's own list, each followed by a "
            f"positive and distinct change, {change} percent, and the largest area is not "
            "the largest rise")


CLAIMS = [
 ("main factors leading to a decrease in biodiversity",
  "EIN-4.C.1, near verbatim: HIPPCO describes the main factors leading to a decrease in biodiversity, so it names causes of loss rather than remedies, stages or levels."),
 ("population growth, pollution, climate change and over exploitation",
  "EIN-4.C.1 spells HIPPCO out as habitat destruction, invasive species, population growth, pollution, climate change, and over exploitation, which is the set the keyed option names in full."),
 ("use of habitat corridors",
  "EIN-4.C.1 names six factors and habitat corridors is not among them; EIN-4.C.6 lists corridors as one of the ways of MITIGATING biodiversity loss, which is the opposite kind of thing. The anchor names the item that has been put on the wrong side."),
 ("large habitats are broken into smaller, isolated areas",
  "EIN-4.C.2, near verbatim: habitat fragmentation occurs when large habitats are broken into smaller, isolated areas. The anchor carries the direction because the rejected option reverses it."),
 ("construction of roads and pipelines, clearing for agriculture or development",
  "EIN-4.C.2 names the construction of roads and pipelines, clearing for agriculture or development, and logging as causes of habitat fragmentation."),
 ("varies from species to species within that ecosystem",
  "EIN-4.C.3, near verbatim: the scale of habitat fragmentation that has an adverse effect on the inhabitants of a given ecosystem will vary from species to species within that ecosystem."),
 ("temperature, in precipitation, and a rise in sea level",
  "EIN-4.C.4 states that global climate change can cause habitat loss via changes in temperature, precipitation, and sea level rise, naming all three routes together."),
 ("somewhat or completely domesticated and are now managed for economic returns",
  "EIN-4.C.5, near verbatim: some organisms have been somewhat or completely domesticated and are now managed for economic returns."),
 ("Honeybee colonies and domestic livestock",
  "EIN-4.C.5 gives honeybee colonies and domestic livestock as its examples of organisms somewhat or completely domesticated and managed for economic returns."),
 ("A negative impact on the biodiversity of that organism",
  "EIN-4.C.5 ends by stating that this domestication can have a negative impact on the biodiversity of that organism, so the effect falls on the domesticated organism itself and its direction is downward. The anchor carries both because the rejected options change one or the other."),
 ("Creating protected areas, using habitat corridors, promoting sustainable land use practices",
  "EIN-4.C.6 states that some ways humans can mitigate the impact of loss of biodiversity include creating protected areas, use of habitat corridors, promoting sustainable land use practices, and restoring lost habitats."),
 ("Clearing land for development",
  "EIN-4.C.6 names four mitigations, each of which the four rejected options restates. EIN-4.C.2 lists clearing for development among the CAUSES of habitat fragmentation instead, so it belongs on the other side of this topic."),
 ("allows partial domestication as well as complete domestication",
  "The phrase SOMEWHAT OR COMPLETELY in EIN-4.C.5 covers both a partial and a complete case, so neither is excluded, and the statement gives two examples rather than restricting itself to one."),
 ("adverse effect varies from species to species within an ecosystem",
  "EIN-4.C.3 states that the scale of habitat fragmentation having an adverse effect will vary from species to species within a given ecosystem, and it supplies no size at which the effect begins for all of them."),
 ("habitat corridors is among the main factors leading to a decrease in biodiversity",
  "EIN-4.C.6 names the use of habitat corridors as a way of mitigating biodiversity loss, not as a cause of it, and EIN-4.C.1's six factors do not include it. The four rejected options restate EIN-4.C.2, EIN-4.C.4, EIN-4.C.5 and EIN-4.C.6."),
 ("construction of pipelines a cause of habitat fragmentation",
  "EIN-4.C.2 defines habitat fragmentation as large habitats being broken into smaller, isolated areas and names the construction of roads and pipelines among its causes, which is exactly what the account describes."),
 ("global climate change a cause of habitat loss through sea level rise",
  "EIN-4.C.4 states that global climate change can cause habitat loss via changes in temperature, precipitation, and sea level rise, and the account reports habitat lost to the last of those three."),
 ("The use of habitat corridors",
  "EIN-4.C.6 names the use of habitat corridors among the ways humans can mitigate the impact of biodiversity loss, and a strip joining two isolated areas is such a corridor rather than a new reserve, a land use policy or a restoration."),
 ("six the framework names, and every one of them is credited with some of the loss",
  "Recomputed in q19 above: the six rows are exactly EIN-4.C.1's six factors, and each carries a positive count distinct from the others. The framework calls them the main factors leading to a decrease in biodiversity."),
 ("Habitat destruction",
  "Recomputed in q20 above: the largest and uniquely largest count belongs to that factor. EIN-4.C.1 lists the six without ranking them, so the order is a property of this record rather than of the framework."),
 ("broken into more and smaller pieces hold fewer species",
  "Recomputed in q21 above: down the record the number of pieces rises while the mean piece and the species present both fall. EIN-4.C.2 defines fragmentation as large habitats broken into smaller, isolated areas, and EIN-4.C.1 names habitat destruction among the main factors decreasing biodiversity."),
 ("Landscape 4, which holds the most pieces, the smallest pieces and the fewest species",
  "Recomputed in q22 above: the largest number of pieces, the smallest mean piece and the smallest species count all fall in the same row. EIN-4.C.2 describes fragmentation in exactly those terms."),
 ("differ in the size of piece they need, so a given degree of fragmentation does not affect them alike",
  "Recomputed in q23 above: the four breeding thresholds all differ and the share of pieces large enough falls as the threshold rises, with no species finding all pieces usable and none finding none. EIN-4.C.3 makes the harmful scale vary from species to species. The anchor carries both clauses because the rejected option reverses both."),
 ("Species 4, which needs the largest piece and finds the fewest large enough",
  "Recomputed in q24 above: the largest breeding threshold and the smallest share of usable pieces fall in the same row, so that species runs out of habitat before the others. EIN-4.C.3 makes the scale at which fragmentation harms vary from species to species."),
 ("Three of the four are the causes of fragmentation the framework names",
  "Recomputed in q25 above: three rows are exactly the causes EIN-4.C.2 names and each created habitat edge and separate pieces, while the remaining row created neither."),
 ("habitat lost grows as the temperature rise, the fall in precipitation and the sea level rise all grow",
  "Recomputed in q26 above: sorting the sites by the temperature rise, by the fall in precipitation and by the sea level rise in turn each leaves the habitat lost strictly rising, and every precipitation change is negative. EIN-4.C.4 names those three as the routes by which climate change causes habitat loss."),
 ("1,620 hectares more",
  "Recomputed in q27 above: the largest and smallest entries in the habitat lost column differ by 1,620 hectares. EIN-4.C.4 makes habitat loss the outcome those three changes bring about."),
 ("longer a population has been managed, the fewer distinct genetic lines it retains",
  "Recomputed in q28 above: the generations under management rise from none while the distinct genetic lines fall throughout. EIN-4.C.5 states that domestication can have a negative impact on the biodiversity of that organism. The anchor carries the direction because the rejected option reverses it."),
 ("four measures are ones the framework names, and each is followed by a rise",
  "Recomputed in q29 above: the four rows are exactly EIN-4.C.6's four mitigations, each followed by a positive and distinct change, and the largest area is not the largest rise. The framework ranks none of the four, so the sizes belong to this record."),
 ("fragmentation breaks large habitats into smaller isolated areas through roads, pipelines, clearing and logging",
  "EIN-4.C.1 supplies HIPPCO, EIN-4.C.2 the definition of fragmentation and its causes, EIN-4.C.3 the species-by-species scale, EIN-4.C.4 the three climate routes to habitat loss, EIN-4.C.5 the effect of domestication, and EIN-4.C.6 the four mitigations. Each rejected summary swaps causes for mitigations, reverses a direction, supplies a single harmful fragment size, or drops a statement."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25,
                26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e9_10, CLAIMS, TABLE_CHECKS)

e_check.run(e9_10, CLAIMS, TABLE_CHECKS)
