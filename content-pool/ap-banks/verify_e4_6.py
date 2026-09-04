"""Key audit for AP ENVIRONMENTAL SCIENCE 4.6 Watersheds.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-4.F.1  Characteristics of a given watershed include its area, length, slope,
           soil, vegetation types, and divides with adjoining watersheds.

That single sentence is the whole of the topic, and it is a list of six. Which
item keys which entry:

    area              -- items 1, 12, 17, 18, 20, 21, 30
    length            -- items 1, 13, 17, 30
    slope             -- items 1, 8, 17, 19, 20, 30
    soil              -- items 1, 10, 24, 30
    vegetation types  -- items 1, 9, 23, 24, 30
    divides           -- items 1, 5, 6, 11, 25, 26, 27, 28, 29, 30
    the count, the word INCLUDE, and what is absent -- items 2, 3, 4, 7, 14, 15, 16, 22

WHAT THE STATEMENT DOES NOT DO, and what no key here supplies. It does not define
a watershed, it attaches no consequence to any of the six characteristics, and it
gives no value for any of them. Item 15's key is exactly that absence. Nothing in
this module asserts that a steeper watershed sheds water faster or that a
forested one loses less soil -- claims of that shape belong to other topics, and
item 30's rejected summary is this statement with one of them appended.

BECAUSE THE FRAMEWORK GIVES NO VALUES, every comparison between watersheds is a
reading of a TABULATED record, and each of those claims says so: ERT-4.F.1
licenses the question by naming the characteristic, and the table settles the
answer.

TWO ITEMS TURN ON A SWAP and their anchors carry BOTH clauses: item 16, whose
rejected option exchanges this statement's subject with ERT-4.B.3's, and item 29,
whose rejected option asserts the agreement the record denies. An anchor naming
one half would match the swap as well as the key -- the defect already found once
in verify_e2_1.py.

DATA ITEMS: 17 to 29. Every keyed maximum, difference, count and percentage sum
is recomputed below from that table alone. The land cover shares are checked to
add to exactly one hundred percent in every watershed.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Several checks here read a
quantity that reversing every numeric column at once preserves -- a within-row
sum, a disagreement between two columns, a maximum that happens to sit in the
middle row -- so for those e_check flattens the table next and the check fails on
the row sum, the uniqueness or the ordering it also asserts. A sixth control,
added below and not available from e_check, corrupts the one STRING column whose
content is keyed: e_check mutates numbers only, and item 27 counts which river
each basin drains to. ``python3 verify_e4_6.py --selftest`` is the same run; the
controls are not behind the flag.
"""
import copy
import sys

import cg_check as cg
import e_check
import e4_6

AREA = "Area (square kilometers)"
LENGTH = "Length from the head to the outlet (kilometers)"
SLOPE = "Average slope (meters of fall per kilometer)"
FOREST = "Share of the surface under forest (percent)"
GRASS = "Share of the surface under grassland (percent)"
THINSOIL = "Share of the surface where the soil is thin or absent (percent)"
ADJOINING = "Number of watersheds adjoining it"
DIVIDE = "Length of the divide it shares with them (kilometers)"

NORTHERN = "The northern river"
MIN_DIVIDE = 10   # a divide has to be a real, measurable stretch


def _unique_max(values):
    i = max(range(len(values)), key=lambda k: values[k])
    assert values.count(values[i]) == 1, f"the maximum must be unique; got {values}"
    return i


def _ordering(table, header):
    """Row labels ordered by the named column, lowest first."""
    values = cg.col(table, header)
    labs = cg.labels(table)
    return [labs[i] for i in sorted(range(len(values)), key=lambda k: values[k])]


def _rivers(table):
    return [str(r[3]) for r in table["rows"]]


def q17(table, item):
    columns = {name: cg.col(table, name) for name in (AREA, LENGTH, SLOPE)}
    for name, values in columns.items():
        assert len(set(values)) == len(values), \
            f"{name} must differ from one watershed to the next; got {values}"
        assert min(values) > 0, f"{name} must be positive throughout; got {values}"
    return (f"beside each watershed the record carries an area {columns[AREA]}, a length "
            f"{columns[LENGTH]} and a slope {columns[SLOPE]}, each varying from watershed "
            "to watershed")


def q18(table, item):
    labs = cg.labels(table)
    area = cg.col(table, AREA)
    i = _unique_max(area)
    assert labs[i] == "Watershed B", \
        f"the largest area must belong to Watershed B; got {labs[i]}"
    assert _ordering(table, AREA) == ["Watershed C", "Watershed A", "Watershed B"], \
        f"the areas must rank C, then A, then B; got {_ordering(table, AREA)}"
    return (f"the areas are {dict(zip(labs, area))} square kilometers, ranking "
            f"{_ordering(table, AREA)} from smallest, so the largest is {labs[i]}")


def q19(table, item):
    labs = cg.labels(table)
    slope = cg.col(table, SLOPE)
    i = _unique_max(slope)
    assert labs[i] == "Watershed C", \
        f"the steepest must be Watershed C; got {labs[i]}"
    assert _ordering(table, SLOPE) == ["Watershed A", "Watershed B", "Watershed C"], \
        f"the slopes must rank A, then B, then C; got {_ordering(table, SLOPE)}"
    return (f"the slopes are {dict(zip(labs, slope))} meters of fall per kilometer, "
            f"ranking {_ordering(table, SLOPE)} from gentlest, so the steepest is {labs[i]}")


def q20(table, item):
    labs = cg.labels(table)
    area = cg.col(table, AREA)
    slope = cg.col(table, SLOPE)
    largest = _unique_max(area)
    steepest = _unique_max(slope)
    # Named booleans rather than a bare index comparison: the claim is a
    # DISAGREEMENT between two rankings, and stating it as its own boolean is
    # what stops a check from quietly asserting the opposite.
    largest_is_not_steepest = largest != steepest
    assert largest_is_not_steepest, (
        f"the largest and the steepest must be different watersheds; area {area} points at "
        f"row {largest} and slope {slope} at row {steepest}"
    )
    return (f"the unique largest area falls on row {largest}, {labs[largest]}, and the "
            f"unique steepest slope on row {steepest}, {labs[steepest]}, so the two "
            "characteristics rank the three differently")


def q21(table, item):
    labs = cg.labels(table)
    area = cg.col(table, AREA)
    gap = max(area) - min(area)
    assert gap == 235, f"the largest and smallest areas must differ by 235; got {gap}"
    assert gap not in area, \
        f"the difference must not coincide with any recorded area; got {gap} in {area}"
    others = {abs(a - b) for a in area for b in area if a != b}
    assert gap == max(others), \
        f"235 must be the largest gap among the three; got {sorted(others)}"
    return (f"the areas are {dict(zip(labs, area))} square kilometers, so the largest gap "
            f"is {gap:.0f}, larger than the other gaps {sorted(others - {gap})}")


def q22(table, item):
    labs = cg.labels(table)
    forest = cg.col(table, FOREST)
    grass = cg.col(table, GRASS)
    thin = cg.col(table, THINSOIL)
    sums = [f + g + t for f, g, t in zip(forest, grass, thin)]
    for lab, f, g, t, total in zip(labs, forest, grass, thin, sums):
        assert abs(total - 100) < 1e-9, \
            f"{lab}: {f} forest plus {g} grassland plus {t} thin soil must be 100, not {total}"
    assert all(t <= 100 for t in sums), "'they add to more than one hundred' must be false"
    return (f"the forested shares {forest}, the grassland shares {grass} and the thin soil "
            f"shares {thin} add to {sums} percent, exactly one hundred in every watershed")


def q23(table, item):
    labs = cg.labels(table)
    forest = cg.col(table, FOREST)
    i = _unique_max(forest)
    assert labs[i] == "Watershed A", \
        f"the largest forested share must belong to Watershed A; got {labs[i]}"
    assert len(set(forest)) == len(forest), \
        "'the three carry equal shares under forest' must be false"
    return (f"the forested shares are {dict(zip(labs, forest))} percent, all different, and "
            f"the largest belongs to {labs[i]}")


def q24(table, item):
    forest = cg.col(table, FOREST)
    grass = cg.col(table, GRASS)
    thin = cg.col(table, THINSOIL)
    for name, values in ((FOREST, forest), (GRASS, grass), (THINSOIL, thin)):
        assert len(set(values)) == len(values), \
            f"{name} must vary from watershed to watershed; got {values}"
    for f, g, t in zip(forest, grass, thin):
        assert abs(f + g + t - 100) < 1e-9, \
            f"{f}, {g} and {t} must be shares of one surface, adding to 100"
    assert AREA not in table["headers"] and LENGTH not in table["headers"], \
        "this record must not also carry the area or the length"
    return ("two of the three columns record plant cover, forest {} and grassland {}, and "
            "the third records where the soil is thin or absent {}, all varying and all "
            "shares of one surface".format(forest, grass, thin))


def q25(table, item):
    labs = cg.labels(table)
    adjoining = cg.col(table, ADJOINING)
    divide = cg.col(table, DIVIDE)
    for lab, n, d in zip(labs, adjoining, divide):
        assert n >= 1, f"{lab}: it must adjoin at least one other watershed; got {n}"
        assert d > MIN_DIVIDE, \
            f"{lab}: a divide of {d} kilometers is not a measurable stretch"
    assert len(set(adjoining)) == len(adjoining), \
        f"'they all adjoin the same number of others' must be false; got {adjoining}"
    return (f"the adjoining counts are {dict(zip(labs, adjoining))}, all at least one and "
            f"all different, and every divide runs {divide} kilometers, well over "
            f"{MIN_DIVIDE}")


def q26(table, item):
    labs = cg.labels(table)
    adjoining = cg.col(table, ADJOINING)
    i = _unique_max(adjoining)
    assert labs[i] == "Watershed C", \
        f"the most adjoining watersheds must belong to Watershed C; got {labs[i]}"
    return (f"the adjoining counts are {dict(zip(labs, adjoining))} and the largest is "
            f"unique and belongs to {labs[i]}")


def q27(table, item):
    rivers = _rivers(table)
    divide = cg.col(table, DIVIDE)
    northern = [r for r in rivers if r == NORTHERN]
    assert len(northern) == 2, \
        f"exactly two of the three must reach the northern river; got {rivers}"
    assert len(set(rivers)) == 2, \
        f"the three must not all drain the same way; got {rivers}"
    assert min(divide) > MIN_DIVIDE, \
        f"every basin must be separated by a measurable divide; got {divide}"
    return (f"the three basins drain to {rivers}, so exactly {len(northern)} reach the "
            f"northern river, and each is separated from its neighbours by a divide of "
            f"{divide} kilometers")


def q28(table, item):
    labs = cg.labels(table)
    divide = cg.col(table, DIVIDE)
    i = _unique_max(divide)
    assert labs[i] == "Watershed B", \
        f"the longest divide must belong to Watershed B; got {labs[i]}"
    assert _ordering(table, DIVIDE) == ["Watershed C", "Watershed A", "Watershed B"], \
        f"the divides must rank C, then A, then B; got {_ordering(table, DIVIDE)}"
    return (f"the divide lengths are {dict(zip(labs, divide))} kilometers, ranking "
            f"{_ordering(table, DIVIDE)} from shortest, so the longest is {labs[i]}")


def q29(table, item):
    labs = cg.labels(table)
    adjoining = cg.col(table, ADJOINING)
    divide = cg.col(table, DIVIDE)
    most_neighbours = _unique_max(adjoining)
    longest_divide = _unique_max(divide)
    rankings_disagree = most_neighbours != longest_divide
    assert rankings_disagree, (
        f"the watershed adjoining the most others must not be the one with the longest "
        f"divide; adjoining {adjoining} points at row {most_neighbours} and divide "
        f"{divide} at row {longest_divide}"
    )
    assert len(set(adjoining)) == len(adjoining), \
        "'all three adjoin the same number of others' must be false"
    return (f"the most neighbours falls on row {most_neighbours}, {labs[most_neighbours]}, "
            f"and the longest divide on row {longest_divide}, {labs[longest_divide]}, so "
            "the two columns rank the three differently")


CLAIMS = [
 ("vegetation types, and divides with adjoining watersheds",
  "ERT-4.F.1, near verbatim: characteristics of a given watershed include its area, length, slope, soil, vegetation types, and divides with adjoining watersheds. Two rejected lists drop half the entries, one adds a human population the statement never names, and one replaces the list altogether."),
 ("Six",
  "ERT-4.F.1 names area, length, slope, soil, vegetation types, and divides with adjoining watersheds, which is six entries in a single list."),
 ("number of people living in it",
  "ERT-4.F.1's six entries are area, length, slope, soil, vegetation types and divides with adjoining watersheds. A human population appears nowhere in the statement."),
 ("depth of the groundwater",
  "ERT-4.F.1's six entries are area, length, slope, soil, vegetation types and divides with adjoining watersheds. The depth of the groundwater is not among them, and the statement mentions no water beneath the surface at all."),
 ("Its divides with adjoining watersheds",
  "ERT-4.F.1 names divides with adjoining watersheds among the characteristics, and a divide is what lies between one watershed and the next. The other five entries describe the watershed itself rather than its edge."),
 ("neighbouring watersheds and a boundary it shares with them",
  "ERT-4.F.1 speaks of divides WITH ADJOINING watersheds, which places other watersheds beside this one and makes the divide the thing they share. The statement neither divides a watershed internally nor mentions ownership or politics."),
 ("without its claiming that nothing else about a watershed can be described",
  "ERT-4.F.1 opens with characteristics of a given watershed INCLUDE, which commits the framework to those six while making no claim about features it does not discuss. The same statement fixes the characteristics to a GIVEN watershed, so an option denying that is false as well."),
 ("Its slope",
  "ERT-4.F.1 names slope among the characteristics of a given watershed, and a measure of how steeply the land falls is what a slope is. Area, length, soil and vegetation types are the other entries and are recorded differently."),
 ("Its vegetation types",
  "ERT-4.F.1 names vegetation types among the characteristics of a given watershed, and a survey of the plants growing across the basin records exactly that and none of the other five."),
 ("Its soil",
  "ERT-4.F.1 names soil among the characteristics of a given watershed, and describing what the ground is made of at depth is a record of the soil rather than of anything growing on it."),
 ("boundaries between one watershed and the next",
  "ERT-4.F.1 names divides with adjoining watersheds among the characteristics, and a divide is what separates one watershed from its neighbour, so which side of it a hillside lies on is what decides which basin the rain falls in."),
 ("Their area",
  "ERT-4.F.1 names area among the characteristics of a given watershed, and the amount of land a basin drains is its area. The other entries record steepness, ground material, plant cover and the boundary with a neighbour."),
 ("Its length",
  "ERT-4.F.1 names length among the characteristics of a given watershed, and a distance measured from one end of the basin to the other is a length rather than an area or a steepness."),
 ("Characteristics of a given watershed include its area",
  "ERT-4.F.1 is a list of six characteristics belonging to one watershed, so the framework itself treats a watershed as described by several properties at once. The rejected statements are ERT-4.B.2, ERT-4.D.2, ERT-4.E.1 and ERT-4.A.1, none of which concerns a watershed."),
 ("affects the water leaving the watershed",
  "ERT-4.F.1 lists six characteristics and attaches no consequence to any of them. What a slope or a soil does to the water leaving a basin would have to come from another statement or from a measurement."),
 # Both clauses, in order: the rejected option exchanges this statement's
 # subject with ERT-4.B.3's, so an anchor naming one clause matches both.
 ("lists what can be described about a watershed, while that one says what protecting a soil does",
  "ERT-4.F.1 is a list of characteristics with no consequence attached to any of them. ERT-4.B.3, in topic 4.2, states that protecting soils can protect water quality as soils effectively filter and clean water that moves through them, which is a consequence rather than a description. Both statements mention soil, so an option denying that is false as well."),
 ("Its area, its length, and its slope",
  "Recomputed in q17 above: beside each watershed the record carries an area, a length and an average slope, each positive and each varying from one watershed to the next. ERT-4.F.1 names all three among the characteristics of a given watershed."),
 ("Watershed B",
  "Recomputed in q18 above: the three areas are 120, 310 and 75 square kilometers, ranking C, then A, then B from smallest, so the largest is unique. ERT-4.F.1 names area among the characteristics but supplies no value, so the comparison comes from the record."),
 ("Watershed C",
  "Recomputed in q19 above: the three slopes are 8, 15 and 31 meters of fall per kilometer, ranking A, then B, then C from gentlest, so the steepest is unique. ERT-4.F.1 names slope among the characteristics and supplies no value."),
 ("can rank the three differently",
  "Recomputed in q20 above: the unique largest area and the unique steepest slope belong to different watersheds. ERT-4.F.1 lists area and slope as separate characteristics of a given watershed and connects neither to the other."),
 ("235 square kilometers larger",
  "Recomputed in q21 above: 310 less 75 is 235, which coincides with no recorded area and is the largest of the three gaps in the record. The rejected values are the largest area itself and the smaller gaps."),
 ("add to one hundred percent in every watershed",
  "Recomputed in q22 above: the forested share, the grassland share and the share where the soil is thin or absent add to exactly one hundred percent in each of the three watersheds, so between them they account for the whole surface and never for more."),
 ("Watershed A",
  "Recomputed in q23 above: the three forested shares are 62, 18 and 40 percent, all different, and the largest is unique. ERT-4.F.1 names vegetation types among the characteristics of a given watershed and supplies no value."),
 ("Its vegetation types and its soil",
  "Recomputed in q24 above: two of the three columns record plant cover and the third records where the soil is thin or absent, all three varying and all three shares of one surface, and the record carries neither an area nor a length. ERT-4.F.1 names vegetation types and soil among the characteristics of a given watershed."),
 ("shares a divide of measurable length with them",
  "Recomputed in q25 above: every watershed adjoins at least one other, the counts differ from one another, and every divide runs tens of kilometers. ERT-4.F.1 names divides with adjoining watersheds among the characteristics of a given watershed."),
 ("Watershed C",
  "Recomputed in q26 above: the three counts of adjoining watersheds are 3, 2 and 4, all different, and the largest is unique. ERT-4.F.1 names the divides without supplying a number of neighbours, so the record settles it."),
 ("Two of the three",
  "Recomputed in q27 above: two of the three rows name the northern river and one names the southern, so the basins do not all drain the same way, and each is separated from its neighbours by a divide tens of kilometers long. ERT-4.F.1 names divides with adjoining watersheds among the characteristics."),
 ("Watershed B",
  "Recomputed in q28 above: the three divide lengths are 58, 71 and 46 kilometers, ranking C, then A, then B from shortest, so the longest is unique. ERT-4.F.1 names the divides without supplying a length."),
 # Both clauses: the rejected option asserts the agreement the record denies.
 ("the watershed adjoining the most others is not the one with the longest divide",
  "Recomputed in q29 above: the unique largest count of adjoining watersheds and the unique longest divide belong to different watersheds. A basin can touch many neighbours along short stretches or few along long ones, and ERT-4.F.1 names the divides without saying anything about their number or their length."),
 ("its vegetation types, and its divides with adjoining watersheds",
  "ERT-4.F.1 supplies six characteristics of a given watershed and nothing beyond them. Each rejected summary shortens the list, adds a population or a political boundary the statement never names, or attaches to the slope a consequence the statement does not."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


# --------------------------------------------------------------- string control
#
# e_check's table controls corrupt NUMBERS only. Item 27's keyed content is a
# COUNT OF A STRING -- how many of the three basins reach the northern river --
# and no numeric mutation can touch it, so e_check on its own would say nothing
# about whether q27 reads the river column at all. The control below rewrites
# that column so all three basins drain the same way, and q27 must fail on it.
# The mutation is asserted to change the table before it is used, because a
# control that cannot fail is worse than none.

def _string_control():
    same = copy.deepcopy(e4_6._T_DIVIDES)
    for row in same["rows"]:
        row[3] = NORTHERN
    assert same["rows"] != e4_6._T_DIVIDES["rows"], "the mutation changed nothing"
    assert len({str(r[3]) for r in same["rows"]}) == 1, \
        "the mutation must actually make every basin drain the same way"
    try:
        q27(same, None)
    except AssertionError as exc:
        print(f"    control OK  every basin sent to one river: {str(exc)[:80]}")
        return
    raise SystemExit("4.6 CONTROL FAILED: q27 passed with all three basins on one river")


if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

_string_control()
e_check.run(e4_6, CLAIMS, TABLE_CHECKS)
