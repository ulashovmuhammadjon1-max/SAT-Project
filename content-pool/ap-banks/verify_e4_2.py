"""Key audit for AP ENVIRONMENTAL SCIENCE 4.2 Soil Formation and Erosion.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-4.B.1  Soils are formed when parent material is weathered, transported, and
           deposited.
                   -- items 1, 2, 3, 11, 16, 19, 30
ERT-4.B.2  Soils are generally categorized by horizons based on their composition
           and organic material.
                   -- items 4, 5, 6, 14, 17, 21, 22, 23, 24, 30
ERT-4.B.3  Soils can be eroded by winds or water. Protecting soils can protect
           water quality as soils effectively filter and clean water that moves
           through them.
                   -- items 7, 8, 9, 10, 12, 13, 15, 18, 20, 25, 26, 27, 28, 29, 30

THE ORDER IN ERT-4.B.1 IS THE FRAMEWORK'S OWN -- weathered, then transported,
then deposited -- and item 2 turns on it, so its anchor names all three steps in
sequence. An anchor naming one step would match the reversed distractor too.

THE TWO HEDGED WORDS ARE KEYED AS HEDGES. ERT-4.B.2 says soils are GENERALLY
categorized by horizons (item 6) and ERT-4.B.3 says soils can be eroded by winds
OR water (items 7 and 15), which names both agents and requires neither. No key
anywhere hardens either into a rule.

WHAT ERT-4.B.3 SAYS THE SOIL DOES TO THE WATER IS A REMOVAL, not an addition:
it FILTERS and CLEANS the water moving through it. Item 18's key is exactly that
distinction and item 30's rejected summary is the same sentence with the removal
replaced by an addition.

NOT KEYED, because the framework does not state it: the letters by which horizons
are conventionally named, any particular kind of weathering, how long a soil takes
to form, how deep a soil is, or the mechanism by which a soil filters water. No
item asks a student to name a horizon by letter, and item 16's key marks the
missing timescale rather than filling it. Items 19 and 20 tabulate soil depths
against time as a STIMULUS and ask a reading of the table; no key states a rate of
soil formation as a claim of the framework.

BOUNDARY WITH 4.3. Water holding capacity, porosity, permeability, fertility and
the soil texture triangle are ERT-4.C.1 to ERT-4.C.4. Item 17 marks that line and
its anchor carries BOTH clauses, since the rejected option is this topic's claim
and 4.3's exchanged with one another -- the swap defect already found once in
verify_e2_1.py.

DATA ITEMS: 19 to 29. Every keyed direction, maximum, difference, ratio and
percentage sum is recomputed below from that table alone. The percentage columns
in the layer record are checked to sum to one hundred in every row.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Several checks here read a
co-varying gradient or a within-row identity that reversing every numeric column
at once preserves, so for those e_check flattens the table next and the check
fails on the strictness, the uniqueness or the row sum it also asserts -- a flat
column has no gradient, no unique maximum, and its rows do not add to one
hundred. ``python3 verify_e4_2.py --selftest`` is the same run; the controls are
not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e4_2

EXPOSED = "Years since the parent material was first exposed"
SOILDEPTH = "Depth of soil formed (centimeters)"
LAYERDEPTH = "Depth below the surface (centimeters)"
ORGANIC = "Organic material (percent by mass)"
MINERAL = "Sand, silt and clay together (percent by mass)"
WIND = "Soil lost to wind (tonnes per hectare per year)"
WATER = "Soil lost to running water (tonnes per hectare per year)"
TOTAL = "Total soil lost (tonnes per hectare per year)"
SEDIMENT = "Sediment carried (milligrams per liter)"
NITRATE = "Nitrate carried (milligrams per liter)"

RAIN = "Rain as it falls on the surface"
INTACT = "Water that has moved down through intact soil"
STRIPPED = "Water running off ground whose soil has been stripped away"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def q19(table, item):
    (depth,) = _by(table, EXPOSED, SOILDEPTH)
    assert _rises(depth), \
        f"the soil must be deeper where the parent material was exposed longer; got {depth}"
    assert len(set(depth)) == len(depth), "'the same depth at all four sites' must be false"
    assert min(depth) > 0, f"every site must have formed some soil; got {depth}"
    return (f"ordered by the time since exposure the soil depths read {depth} centimeters, "
            "strictly increasing and all above zero")


def q20(table, item):
    years = cg.col(table, EXPOSED)
    depth = cg.col(table, SOILDEPTH)
    oldest = max(range(len(years)), key=lambda i: years[i])
    assert years.count(years[oldest]) == 1, f"the oldest site must be unique; got {years}"
    rate = depth[oldest] / (years[oldest] / 1000)
    assert rate == 10, \
        f"the oldest site must give 10 centimeters per thousand years; got {rate}"
    assert all(rate != d for d in depth), \
        f"the rate must not coincide with any recorded depth; got {rate} against {depth}"
    return (f"the oldest site records {depth[oldest]:.0f} centimeters over "
            f"{years[oldest]:.0f} years, which is {rate:.0f} centimeters per thousand years")


def q21(table, item):
    depth = cg.col(table, LAYERDEPTH)
    organic = cg.col(table, ORGANIC)
    richest = max(range(len(organic)), key=lambda i: organic[i])
    shallowest = min(range(len(depth)), key=lambda i: depth[i])
    assert organic.count(organic[richest]) == 1, \
        f"the largest organic share must be unique; got {organic}"
    assert depth.count(depth[shallowest]) == 1, \
        f"the shallowest layer must be unique; got {depth}"
    assert richest == shallowest, (
        f"the layer richest in organic material must be the shallowest one; organic "
        f"{organic} points at row {richest} and the depths {depth} at row {shallowest}"
    )
    return (f"the organic shares read {organic} percent and the depths {depth} centimeters, "
            f"and the unique maximum of the first falls on the same row, {richest}, as the "
            "unique minimum of the second")


def q22(table, item):
    (organic,) = _by(table, LAYERDEPTH, ORGANIC)
    assert _falls(organic), \
        f"the organic share must fall at every step down the record; got {organic}"
    assert organic[-1] == min(organic), \
        "'it falls and then rises again in the deepest layer' must be false"
    return (f"ordered by depth the organic shares read {organic} percent, strictly "
            "decreasing to a minimum in the deepest layer")


def q23(table, item):
    organic = cg.col(table, ORGANIC)
    mineral = cg.col(table, MINERAL)
    sums = [o + m for o, m in zip(organic, mineral)]
    for i, s in enumerate(sums, 1):
        assert abs(s - 100) < 1e-9, f"layer {i}: {organic[i - 1]} plus {mineral[i - 1]} " \
                                    f"must be 100 percent, not {s}"
    assert all(s <= 100 for s in sums), "'they add to more than one hundred' must be false"
    return (f"the organic shares {organic} and the mineral shares {mineral} add to {sums} "
            "percent, exactly one hundred in every layer")


def q24(table, item):
    organic = cg.col(table, ORGANIC)
    mineral = cg.col(table, MINERAL)
    depth = cg.col(table, LAYERDEPTH)
    assert len(set(organic)) == len(organic), \
        f"the organic share must differ from layer to layer; got {organic}"
    assert len(set(mineral)) == len(mineral), \
        f"the mineral share must differ from layer to layer; got {mineral}"
    assert len(set(depth)) == len(depth), f"each layer must lie at its own depth; got {depth}"
    for o, m in zip(organic, mineral):
        assert abs(o + m - 100) < 1e-9, \
            f"{o} and {m} must be shares of the same whole, adding to 100"
    return (f"beside the depths {depth} the record carries an organic share {organic} and a "
            f"mineral share {mineral}, both varying layer by layer and adding to one "
            "hundred, which are organic material and composition")


def q25(table, item):
    labs = cg.labels(table)
    wind = cg.col(table, WIND)
    water = cg.col(table, WATER)
    total = cg.col(table, TOTAL)
    for lab, a, b, t in zip(labs, wind, water, total):
        assert a > 0, f"{lab}: the wind must have removed some soil; got {a}"
        assert b > 0, f"{lab}: running water must have removed some soil; got {b}"
        assert abs(a + b - t) < 1e-9, f"{lab}: {a} plus {b} must account for the total {t}"
    assert len(set(total)) == len(total), f"the four totals must differ; got {total}"
    return (f"on every plot the wind removed {wind} and running water {water} tonnes per "
            f"hectare, both above zero, and the two add to the recorded totals {total}")


def q26(table, item):
    labs = cg.labels(table)
    total = cg.col(table, TOTAL)
    worst = max(range(len(total)), key=lambda i: total[i])
    assert total.count(total[worst]) == 1, f"the largest total must be unique; got {total}"
    assert labs[worst] == "Bare and sloping", \
        f"the largest total must belong to the bare sloping plot; got {labs[worst]}"
    return (f"the totals are {dict(zip(labs, total))} tonnes per hectare and the largest is "
            f"unique and belongs to {labs[worst]}")


def q27(table, item):
    bare = cg.cell(table, "Bare and sloping", TOTAL)
    covered = cg.cell(table, "Covered and sloping", TOTAL)
    gap = bare - covered
    assert abs(gap - 21.0) < 1e-9, f"the difference must be 21.0 tonnes per hectare; got {gap}"
    assert gap != bare and gap != covered, \
        "the difference must not coincide with either total"
    other = cg.cell(table, "Bare and level", TOTAL) - cg.cell(table, "Covered and level", TOTAL)
    assert abs(gap - other) > 1e-9, \
        f"the level plots must give a different difference; got {other}"
    return (f"the bare sloping plot loses {bare} and the covered sloping plot {covered} "
            f"tonnes per hectare, a difference of {gap:.1f}, against {other:.1f} for the "
            "level pair")


def q28(table, item):
    rain_sed = cg.cell(table, RAIN, SEDIMENT)
    rain_nit = cg.cell(table, RAIN, NITRATE)
    intact_sed = cg.cell(table, INTACT, SEDIMENT)
    intact_nit = cg.cell(table, INTACT, NITRATE)
    strip_sed = cg.cell(table, STRIPPED, SEDIMENT)
    strip_nit = cg.cell(table, STRIPPED, NITRATE)
    # Named booleans rather than a comparison between parallel tuples: the two
    # directions are opposite and a swapped comparison would read as parallel.
    intact_carries_less = intact_sed < rain_sed and intact_nit < rain_nit
    stripped_carries_more = strip_sed > rain_sed and strip_nit > rain_nit
    assert intact_carries_less, (
        f"water through intact soil must carry less than the rain; sediment {intact_sed} "
        f"against {rain_sed}, nitrate {intact_nit} against {rain_nit}"
    )
    assert stripped_carries_more, (
        f"runoff from stripped ground must carry more than the rain; sediment {strip_sed} "
        f"against {rain_sed}, nitrate {strip_nit} against {rain_nit}"
    )
    return (f"against the rain's {rain_sed:.0f} sediment and {rain_nit} nitrate, the water "
            f"through intact soil carries {intact_sed:.0f} and {intact_nit} while the "
            f"runoff from stripped ground carries {strip_sed:.0f} and {strip_nit}")


def q29(table, item):
    strip_sed = cg.cell(table, STRIPPED, SEDIMENT)
    intact_sed = cg.cell(table, INTACT, SEDIMENT)
    rain_sed = cg.cell(table, RAIN, SEDIMENT)
    ratio = strip_sed / intact_sed
    assert abs(ratio - 70) < 0.5, f"the ratio must be about 70; got {ratio}"
    for wrong in (12, 7, 2):
        assert abs(ratio - wrong) > 1, f"a ratio of about {wrong} must be false"
    assert ratio > 1, "'less, rather than more' must be false"
    assert rain_sed != strip_sed, "the rain and the runoff must not carry the same sediment"
    return (f"the runoff carries {strip_sed:.0f} milligrams of sediment per liter against "
            f"{intact_sed:.0f} for the water through intact soil, a ratio of {ratio:.0f}")


CLAIMS = [
 ("weathered, transported, and deposited",
  "ERT-4.B.1, near verbatim: soils are formed when parent material is weathered, transported, and deposited. Each rejected option removes the parent material, removes one of the three processes, or places the deposition before the weathering."),
 # All three steps in sequence: a distractor reverses the order.
 ("Weathered first, then transported, then deposited",
  "ERT-4.B.1 lists the processes as weathered, transported, and deposited, in that sequence, so the order is the statement's own and not an inference. Each rejected option reorders them or denies that any order is given."),
 ("Parent material",
  "ERT-4.B.1 names parent material as the thing weathered, transported and deposited to form a soil. Loam appears in ERT-4.C.4 as a blend of clay, silt and sand rather than as the source a soil forms from."),
 ("By horizons, on the basis of their composition",
  "ERT-4.B.2, near verbatim: soils are generally categorized by horizons based on their composition and organic material. Each rejected option substitutes a quantity the statement never mentions."),
 ("Composition and organic material",
  "ERT-4.B.2 names composition and organic material as the two things the horizon categories rest on. Slope and area belong to the watershed statement ERT-4.F.1 and the remaining pairs appear nowhere in this topic."),
 ("the usual basis of the categories",
  "ERT-4.B.2 is written soils are GENERALLY categorized by horizons, which commits the framework to horizons as the ordinary basis while stopping short of asserting it is the only one. Hardening it into every soil having identical horizons is stronger than the statement."),
 ("Winds or water",
  "ERT-4.B.3 states that soils can be eroded by winds or water, naming both agents and requiring neither. Earthquakes and volcanic eruptions belong to the plate boundary statements ERT-4.A.1 and ERT-4.A.2 and are not named here."),
 ("Water quality",
  "ERT-4.B.3 states that protecting soils can protect water quality, and names no other thing that protecting a soil protects."),
 ("effectively filter and clean water",
  "ERT-4.B.3 gives its reason with the word AS: protecting soils can protect water quality AS soils effectively filter and clean water that moves through them. The statement neither stops the water reaching a river nor holds it permanently."),
 ("because soils filter and clean the water moving through them",
  "ERT-4.B.3 states that protecting soils can protect water quality as soils effectively filter and clean water that moves through them, which is what keeping the soil on a stream bank does. The statement attaches no other consequence to protecting a soil."),
 ("Filtration of water",
  "ERT-4.B.1 names weathering, transport and deposition acting on parent material. Filtering and cleaning water is what ERT-4.B.3 says a soil already formed does; it is not one of the processes that form one."),
 ("mass of soil carried off each plot",
  "ERT-4.B.3 states that soils can be eroded by winds or water, so the quantity at issue is how much soil leaves, and the cover crop is the one thing that should differ between the plots compared. Each rejected measure records something that does not change with the treatment."),
 ("where the soil is intact with the quality of water leaving plots",
  "ERT-4.B.3 connects the presence of the soil to the quality of the water moving through it, so a test has to vary the soil and measure the water. A single measurement on one plot varies nothing, and the remaining options measure neither the soil nor the water leaving it."),
 ("organic content of each layer",
  "ERT-4.B.2 states that soils are generally categorized by horizons based on their composition and organic material, so those two quantities, taken layer by layer, are exactly what the categories rest on. None of the rejected measurements appears in the statement."),
 ("names winds and water as agents",
  "ERT-4.B.3 states that soils can be eroded by winds OR water, so each agent counts on its own and neither is required for the other to. The statement makes no reference to plate boundaries."),
 ("How long the weathering, transport and deposition take",
  "ERT-4.B.1 supplies the starting material and three processes and attaches no timescale to any of them. The four rejected options are the statement's own content."),
 # Both clauses, in order: the rejected option is this topic's claim and 4.3's
 # exchanged with one another, so an anchor naming one clause matches both.
 ("horizons are the basis on which soils are categorized, while that one says what the particle size",
  "ERT-4.B.2 states that soils are generally categorized by horizons based on their composition and organic material. ERT-4.C.2, in the next topic, states that the particle size and composition of each horizon can affect the porosity, permeability and fertility of the soil. One statement sets up the unit and the other says what the properties of that unit go on to affect."),
 ("adds nutrients to the water",
  "ERT-4.B.3 supplies the four rejected statements in its own words. It describes the soil as FILTERING and CLEANING the water moving through it, which is a removal from the water, and it nowhere describes a soil as adding anything to it."),
 ("exposed longer",
  "Recomputed in q19 above: ordered by the time since exposure the soil depths run 3, 14, 62 and 120 centimeters, strictly increasing and all above zero. ERT-4.B.1 states that soils are FORMED when parent material is weathered, transported and deposited, so a soil accumulates on parent material rather than being present from the start."),
 ("About 10 centimeters per thousand years",
  "Recomputed in q20 above: 120 centimeters over 12,000 years is 10 centimeters per thousand years, and that figure matches none of the recorded depths. The rejected values are depths from the record read as though they were rates."),
 ("nearest the surface",
  "Recomputed in q21 above: the largest organic share and the smallest depth are each unique in their column and fall on the same layer. ERT-4.B.2 makes organic material one of the two things the horizon categories are based on."),
 ("falls at every step down the record",
  "Recomputed in q22 above: ordered by depth the organic shares run 62, 9, 3 and 1 percent, strictly decreasing to a minimum in the deepest layer. ERT-4.B.2 states that soils are generally categorized by horizons based on their composition and organic material, and a change of that size from layer to layer is what separates one horizon from the next."),
 ("add to one hundred in every layer",
  "Recomputed in q23 above: the organic share and the mineral share add to exactly one hundred percent in each of the four layers, so between them they account for the whole of every layer and never for more than it. ERT-4.B.2 names composition and organic material as the two things the categories rest on."),
 ("the basis of horizons",
  "Recomputed in q24 above: beside the depth of each layer the record carries an organic share and a mineral share, both varying layer by layer and adding to one hundred. Those two are organic material and composition, which ERT-4.B.2 names as the basis of the horizon categories."),
 ("Both wind and running water removed soil",
  "Recomputed in q25 above: every plot records a loss above zero in both the wind column and the running water column, and the two add to the recorded total in every row. ERT-4.B.3 states that soils can be eroded by winds or water, naming both agents."),
 ("The bare sloping plot",
  "Recomputed in q26 above: the four totals are 10.0, 24.0, 0.9 and 3.0 tonnes per hectare and the largest is unique and belongs to the plot that is both bare and sloping. ERT-4.B.3 names winds and water as agents that can erode soils."),
 ("21.0 tonnes per hectare less",
  "Recomputed in q27 above: 24.0 less 3.0 is 21.0, which coincides with neither total and differs from the gap between the two level plots. The rejected values are the two totals themselves and that other gap."),
 # Both clauses: a distractor exchanges the two directions with one another.
 ("carried less than the rain that fell, while runoff from stripped ground carried far more",
  "Recomputed in q28 above: against the rain's 12 milligrams of sediment and 4.0 of nitrate per liter, the water that has passed through intact soil carries 2 and 1.2 while the runoff from stripped ground carries 140 and 6.5. ERT-4.B.3 states that protecting soils can protect water quality as soils effectively filter and clean water that moves through them."),
 ("About 70 times as much",
  "Recomputed in q29 above: 140 divided by 2 is 70, and no smaller multiple among the rejected values is within reach of it. The comparison is a direct reading of one column."),
 ("because soils filter and clean the water moving through them",
  "ERT-4.B.1 supplies the parent material and the three processes in order, ERT-4.B.2 the horizons, the two things they rest on and its hedge, and ERT-4.B.3 the two agents of erosion, the protection of water quality and the filtering and cleaning that is its reason. Each rejected summary reverses the order of the processes, drops an agent of erosion, changes what the categories rest on, or replaces the filtering with an addition to the water."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25,
                26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e4_2, CLAIMS, TABLE_CHECKS)
