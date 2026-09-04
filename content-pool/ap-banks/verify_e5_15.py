"""Key audit for AP ENVIRONMENTAL SCIENCE 5.15 Sustainable Agriculture.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  STB-1.E.1  The goal of soil conservation is to prevent soil erosion. Different
             methods of soil conservation include contour plowing, windbreaks,
             perennial crops, terracing, no-till agriculture, and strip cropping.
                    -- items 1, 2, 3, 10, 11, 12, 13, 14, 15, 22, 24, 26, 28
  STB-1.E.2  Strategies to improve soil fertility include crop rotation and the
             addition of green manure and limestone.
                    -- items 4, 5, 16, 17, 18, 19, 23, 27
  STB-1.E.3  Rotational grazing is the regular rotation of livestock between
             different pastures in order to avoid overgrazing in a particular
             area.                                  -- items 6, 7, 20, 21, 25
Items 8, 9, 29 and 30 read the three statements against each other.

NO MECHANISM IS EVER KEYED. STB-1.E.1 names six practices and explains none of
them; it does not say that contour plowing works across the slope, that
windbreaks slow the wind, or that limestone acts on acidity. Every practice item
here is keyed by WHICH LIST it belongs to or by what a table of measurements
shows, never by how it works, and item 28 keys the absence of any explanation
and any ranking directly.

THE PRACTICE IN TWO STATEMENTS. Crop rotation is a fertility strategy under
STB-1.E.2 and an integrated pest management method under STB-1.C.1 in topic
5.14. Item 9 keys both roles, because a student who has met it in one place
treats the other as an error.

BOUNDARY WITH 5.4 AND 5.7, which hold the DAMAGE rather than the practice:
EIN-2.H for tilling, slash-and-burn and fertilizer, EIN-2.I for overgrazing. No
table here repeats a setting used in either.

DATA ITEMS: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 and 21, recomputed below
from those tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_15

LOST = "Soil lost in one year (tonnes per hectare)"
NONE = "Ploughed up and down the slope, no conservation method"
CONTOUR = "Contour plowing"
TERRACE = "Terracing"
NOTILL = "No-till agriculture"

WIND = "Wind speed measured over the field (meters per second)"
BLOWN = "Soil blown off in one year (tonnes per hectare)"
OPEN = "Open field with no windbreak"
SINGLE = "Field with a single row of trees"
DOUBLE = "Field with a double row of trees"

ROOTS = "Months of the year the soil holds living roots"
PLOST = "Soil lost in one year (tonnes per hectare)"
ANNUAL = "Annual crop, replanted each spring"
PERENNIAL = "Perennial crop, left in the ground"

ORGANIC = "Soil organic matter after five years (percent)"
YIELD5 = "Yield in the fifth year (tonnes per hectare)"
UNTREATED = "No treatment"
MANURE = "Green manure ploughed in"
BOTH = "Green manure and limestone added"

NITROGEN = "Nitrogen in the soil after six years (kilograms per hectare)"
GRAIN = "Grain yield in the sixth year (tonnes per hectare)"
MONO = "The same grain every year"
ROTATED = "Grain rotated with a legume"

ONPAST = "Days the livestock spend on a pasture before being moved"
REST = "Days a pasture rests before the livestock return"
HEIGHT = "Grass height when the livestock return (centimeters)"
ALLSEASON = "Livestock left on one pasture all season"
MOVED = "Livestock moved between four pastures"


def q10(table, item):
    v = cg.col(table, LOST)
    base = cg.cell(table, NONE, LOST)
    assert base == max(v), "the untreated field must lose the most soil"
    for row in (CONTOUR, TERRACE, NOTILL):
        assert cg.cell(table, row, LOST) < base, f"{row!r} must lose less than the untreated field"
    assert len(set(v)) > 1, "'the four fields lost the same amount' must be false"
    return (f"the untreated field loses {base:.0f} tonnes per hectare against "
            f"{[cg.cell(table, r, LOST) for r in (CONTOUR, TERRACE, NOTILL)]} under the three "
            "conservation methods")


def q11(table, item):
    v = cg.col(table, LOST)
    d = cg.cell(table, NONE, LOST) - cg.cell(table, NOTILL, LOST)
    assert d == 28, f"the difference recomputes to {d}, not 28"
    for wrong in (max(v), max(v) + min(v),
                  cg.cell(table, NONE, LOST) - cg.cell(table, CONTOUR, LOST),
                  cg.cell(table, CONTOUR, LOST) - cg.cell(table, NOTILL, LOST)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"32 minus 4 is {d:.0f} tonnes per hectare less soil lost in the year"


def q12(table, item):
    w, b = cg.col(table, WIND), cg.col(table, BLOWN)
    assert cg.cell(table, OPEN, WIND) == max(w), "the open field must be the windiest"
    assert cg.cell(table, OPEN, BLOWN) == max(b), "the open field must lose the most soil"
    assert all(w[i] > w[i + 1] for i in range(len(w) - 1)), f"wind speed must fall; got {w}"
    assert all(b[i] > b[i + 1] for i in range(len(b) - 1)), f"soil blown off must fall; got {b}"
    return (f"wind speed runs {w} meters per second against soil blown off of {b} tonnes per "
            "hectare, both falling as the boundary thickens")


def q13(table, item):
    b = cg.col(table, BLOWN)
    d = cg.cell(table, OPEN, BLOWN) - cg.cell(table, DOUBLE, BLOWN)
    assert d == 16, f"the difference recomputes to {d}, not 16"
    for wrong in (max(b), max(b) + min(b),
                  cg.cell(table, OPEN, BLOWN) - cg.cell(table, SINGLE, BLOWN), min(b)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"21 minus 5 is {d:.0f} tonnes per hectare less soil blown off in the year"


def q14(table, item):
    assert cg.cell(table, PERENNIAL, ROOTS) > cg.cell(table, ANNUAL, ROOTS), \
        "the perennial plot must hold living roots for more of the year"
    assert cg.cell(table, PERENNIAL, ROOTS) == 12, \
        "'the whole year' requires twelve months of living roots"
    assert cg.cell(table, PERENNIAL, PLOST) < cg.cell(table, ANNUAL, PLOST), \
        "the perennial plot must lose less soil"
    assert cg.cell(table, ANNUAL, PLOST) > 3 * cg.cell(table, PERENNIAL, PLOST), \
        "the difference must be large, not marginal"
    return (f"the perennial plot holds roots for {cg.cell(table, PERENNIAL, ROOTS):.0f} months "
            f"and loses {cg.cell(table, PERENNIAL, PLOST):.0f} tonnes per hectare, against "
            f"{cg.cell(table, ANNUAL, ROOTS):.0f} months and "
            f"{cg.cell(table, ANNUAL, PLOST):.0f} tonnes")


def q15(table, item):
    base = cg.cell(table, PERENNIAL, PLOST)
    assert base > 0, "the perennial loss must be non-zero for a ratio to exist"
    ratio = cg.cell(table, ANNUAL, PLOST) / base
    assert ratio == 6, f"the ratio recomputes to {ratio}, not 6"
    for wrong in (base, cg.cell(table, ANNUAL, PLOST) - base, 2, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"18 divided by 3 is {ratio:.0f} times as much soil lost from the replanted plot"


def q16(table, item):
    o, y = cg.col(table, ORGANIC), cg.col(table, YIELD5)
    assert cg.cell(table, UNTREATED, ORGANIC) == min(o), \
        "'the untreated plot held the most organic matter' must be false"
    assert all(o[i] < o[i + 1] for i in range(len(o) - 1)), f"organic matter must rise; got {o}"
    assert all(y[i] < y[i + 1] for i in range(len(y) - 1)), f"yield must rise with it; got {y}"
    return (f"organic matter runs {o} percent against yields of {y} tonnes per hectare across "
            "no treatment, green manure, and green manure with limestone")


def q17(table, item):
    y = cg.col(table, YIELD5)
    d = cg.cell(table, BOTH, YIELD5) - cg.cell(table, UNTREATED, YIELD5)
    assert abs(d - 1.9) < 1e-9, f"the difference recomputes to {d}, not 1.9"
    for wrong in (max(y), max(y) + min(y),
                  cg.cell(table, MANURE, YIELD5) - cg.cell(table, UNTREATED, YIELD5),
                  cg.cell(table, BOTH, YIELD5) - cg.cell(table, MANURE, YIELD5)):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"4.0 minus 2.1 is {d:.1f} tonnes per hectare more in the fifth year"


def q18(table, item):
    assert cg.cell(table, ROTATED, NITROGEN) > cg.cell(table, MONO, NITROGEN), \
        "the rotated plot must hold more nitrogen"
    assert cg.cell(table, ROTATED, GRAIN) > cg.cell(table, MONO, GRAIN), \
        "the rotated plot must yield more grain"
    assert cg.cell(table, ROTATED, NITROGEN) != cg.cell(table, MONO, NITROGEN), \
        "'the same amount of nitrogen' must be false"
    return (f"the rotated plot holds {cg.cell(table, ROTATED, NITROGEN):.0f} kilograms of "
            f"nitrogen per hectare against {cg.cell(table, MONO, NITROGEN):.0f} and yields "
            f"{cg.cell(table, ROTATED, GRAIN):.1f} tonnes per hectare against "
            f"{cg.cell(table, MONO, GRAIN):.1f}")


def q19(table, item):
    d = cg.cell(table, ROTATED, NITROGEN) - cg.cell(table, MONO, NITROGEN)
    yd = cg.cell(table, ROTATED, GRAIN) - cg.cell(table, MONO, GRAIN)
    assert d == 58, f"the difference recomputes to {d}, not 58"
    assert abs(yd - 1.7) < 1e-9, f"the yield difference recomputes to {yd}, not 1.7"
    for wrong in (cg.cell(table, ROTATED, NITROGEN),
                  cg.cell(table, ROTATED, NITROGEN) + cg.cell(table, MONO, NITROGEN),
                  cg.cell(table, MONO, NITROGEN), yd):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return (f"96 minus 38 is {d:.0f} kilograms of nitrogen per hectare more, against a yield "
            f"difference of {yd:.1f} tonnes")


def q20(table, item):
    assert cg.cell(table, MOVED, REST) > cg.cell(table, ALLSEASON, REST), \
        "rotation must give the pasture the longer rest"
    assert cg.cell(table, ALLSEASON, REST) == 0, \
        "the pasture grazed all season must get no rest at all"
    assert cg.cell(table, MOVED, HEIGHT) > cg.cell(table, ALLSEASON, HEIGHT), \
        "the grass must be taller where the livestock were moved"
    assert cg.cell(table, MOVED, ONPAST) < cg.cell(table, ALLSEASON, ONPAST), \
        "rotation must keep the livestock on a pasture for fewer days at a time"
    return (f"rotation keeps the livestock {cg.cell(table, MOVED, ONPAST):.0f} days on a pasture "
            f"and rests it {cg.cell(table, MOVED, REST):.0f}, with grass at "
            f"{cg.cell(table, MOVED, HEIGHT):.0f} centimeters against "
            f"{cg.cell(table, ALLSEASON, HEIGHT):.0f} where the livestock stayed all season")


def q21(table, item):
    base = cg.cell(table, ALLSEASON, HEIGHT)
    assert base > 0, "the continuously grazed height must be non-zero for a ratio to exist"
    ratio = cg.cell(table, MOVED, HEIGHT) / base
    assert ratio == 4, f"the ratio recomputes to {ratio}, not 4"
    for wrong in (2, 3, cg.cell(table, MOVED, HEIGHT) - base, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"16 divided by 4 is {ratio:.0f} times as tall on the rotated pasture"


CLAIMS = [
 ("To prevent soil erosion",
  "STB-1.E.1 opens by stating that THE GOAL OF SOIL CONSERVATION IS TO PREVENT SOIL EROSION. Improving fertility is the goal of the separate statement STB-1.E.2, and the other options name outcomes the framework never sets as a goal."),
 ("Contour plowing, windbreaks, perennial crops, terracing, no-till agriculture",
  "STB-1.E.1 lists contour plowing, windbreaks, perennial crops, terracing, no-till agriculture, and strip cropping. The rejected lists are STB-1.E.2's fertility strategies, EIN-2.E.2's irrigation types, STB-1.C.1's pest management methods, and STB-1.G's forestry methods."),
 ("Flood irrigation",
  "STB-1.E.1's list is contour plowing, windbreaks, perennial crops, terracing, no-till agriculture, and strip cropping. Flood irrigation is EIN-2.E.2 and EIN-2.F.3 in the irrigation topic, where the framework attaches water loss and waterlogging to it rather than erosion control."),
 ("Crop rotation and the addition of green manure and limestone",
  "STB-1.E.2, near verbatim: strategies to improve soil fertility include CROP ROTATION AND THE ADDITION OF GREEN MANURE AND LIMESTONE. Every rejected list is drawn from STB-1.E.1's erosion methods or from other topics."),
 ("Terracing",
  "STB-1.E.2 names crop rotation, green manure and limestone. Terracing sits in STB-1.E.1, whose stated goal is preventing erosion rather than improving fertility, and the framework does not move a practice between its two lists. Every rejected option restates one of the three fertility strategies."),
 ("regular rotation of livestock between different pastures",
  "STB-1.E.3 defines rotational grazing as THE REGULAR ROTATION OF LIVESTOCK BETWEEN DIFFERENT PASTURES. It rotates animals rather than crops, and it moves them rather than removing or concentrating them."),
 ("To avoid overgrazing in a particular area",
  "STB-1.E.3 states that livestock are rotated IN ORDER TO AVOID OVERGRAZING IN A PARTICULAR AREA. Improving fertility is the purpose of STB-1.E.2's separate list, and the rejected options reverse the practice or forbid grazing altogether."),
 ("Soil conservation aims at preventing erosion; the second list of strategies aims at improving fertility",
  "STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion, while STB-1.E.2 introduces its practices as strategies to IMPROVE SOIL FERTILITY. One distractor is the exact swap of the two goals, so the anchor carries both halves."),
 ("Here it is a strategy to improve soil fertility; there it is one of the methods",
  "STB-1.E.2 lists crop rotation among the strategies to improve soil fertility, and STB-1.C.1 in topic 5.14 lists it among the methods of integrated pest management. One distractor is the exact swap of the two roles, so the anchor carries both."),
 ("conservation methods lost less soil than the field worked without one",
  "Recomputed in q10 above: 32 tonnes per hectare untreated against 14 under contour plowing, 6 under terracing and 4 under no-till agriculture. STB-1.E.1 names all three as soil conservation methods and gives preventing erosion as their goal. One distractor reverses the direction, so the anchor carries it."),
 ("28 tonnes per hectare less",
  "Recomputed in q11 above: 32 minus 4 tonnes per hectare. The rejected values quote the untreated field alone, add the two, compare the wrong pair of treatments, or take a difference within the treated fields."),
 ("wind speed over the field and the soil blown off it were lower",
  "Recomputed in q12 above: wind 9, 6 and 4 meters per second against soil blown off 21, 11 and 5 tonnes per hectare, from an open boundary to a double row of trees. STB-1.E.1 names windbreaks among its soil conservation methods. One distractor reverses both directions, so the anchor carries the direction word."),
 ("16 tonnes per hectare less",
  "Recomputed in q13 above: 21 minus 5 tonnes per hectare. The rejected values quote the open field alone, add the two, compare the wrong pair of fields, or quote the sheltered field alone."),
 ("holding living roots through the whole year lost far less soil",
  "Recomputed in q14 above: 12 months of roots and 3 tonnes per hectare lost on the perennial plot against 5 months and 18 tonnes on the annual. STB-1.E.1 names perennial crops among its soil conservation methods. One distractor reverses the direction, so the anchor carries it."),
 ("Six times as much",
  "Recomputed in q15 above: 18 divided by 3 tonnes per hectare. The rejected values quote the perennial plot's own loss, take the difference rather than the ratio, halve the answer, or deny that the plots differ."),
 ("organic matter in the soil and the yield rose with each",
  "Recomputed in q16 above: organic matter 1.4, 2.9 and 3.3 percent against yields of 2.1, 3.4 and 4.0 tonnes per hectare. STB-1.E.2 names green manure and limestone among the strategies to improve soil fertility. Distractors reverse one or both directions, so the anchor carries the direction."),
 ("1.9 tonnes per hectare greater",
  "Recomputed in q17 above: 4.0 minus 2.1 tonnes per hectare. The rejected values quote the treated plot alone, add the two, take the green manure step alone, or take the limestone step alone."),
 ("rotated with a legume held more nitrogen and yielded more grain",
  "Recomputed in q18 above: 96 kilograms of nitrogen per hectare against 38, and 3.6 tonnes of grain against 1.9. STB-1.E.2 names crop rotation among the strategies to improve soil fertility. Distractors reverse one or both directions, so the anchor carries both."),
 ("58 kilograms per hectare more",
  "Recomputed in q19 above: 96 minus 38 kilograms of nitrogen per hectare. The rejected values quote one plot alone, add the two, or take the difference of 1.7 from the yield column instead."),
 ("gave each pasture a rest, and the grass was taller",
  "Recomputed in q20 above: 10 days on a pasture and 30 days of rest with grass at 16 centimeters, against 150 days with no rest and 4 centimeters. STB-1.E.3 defines rotational grazing as the regular rotation of livestock between different pastures to avoid overgrazing in a particular area. One distractor reverses both halves, so the anchor carries both."),
 ("Four times as tall",
  "Recomputed in q21 above: 16 divided by 4 centimeters. The rejected values halve the answer, take the difference rather than the ratio, or deny that the two pastures differ."),
 ("soil conservation list, because the framework gives preventing soil erosion as its goal",
  "STB-1.E.1 states that the goal of soil conservation is to prevent soil erosion, so soil washing off a hillside is exactly what that list addresses. Each rejected option pairs the wrong list with the goal or denies that goals are stated, so the anchor carries the list and the ground together."),
 ("fertility list, whose strategies are crop rotation and the addition of green manure",
  "STB-1.E.2 introduces crop rotation, green manure and limestone as STRATEGIES TO IMPROVE SOIL FERTILITY, which is this district's reported problem. STB-1.E.1's stated goal is preventing erosion, which the district says it does not have."),
 ("on the soil conservation list, whose goal is preventing erosion",
  "STB-1.E.1 names no-till agriculture among the soil conservation methods and gives preventing soil erosion as their goal. STB-1.E.2's fertility strategies are crop rotation, green manure and limestone, and no-till is not among them."),
 ("moving livestock between pastures on a regular cycle, not removing them",
  "STB-1.E.3 defines rotational grazing as the REGULAR ROTATION OF LIVESTOCK BETWEEN DIFFERENT PASTURES in order to avoid overgrazing in a particular area, so the animals keep grazing and only the place changes. Nothing in the statement removes or concentrates them, so the anchor carries both halves."),
 ("Less soil left the treated field over the year",
  "STB-1.E.1 sets the goal of soil conservation as preventing soil erosion, so soil leaving the field is the quantity that reports success. Fertilizer applied, livestock carried, ploughing frequency and crop variety measure other things."),
 ("soil grew more productive over the years",
  "STB-1.E.2 introduces its practices as strategies to IMPROVE SOIL FERTILITY, so a more productive soil is the outcome that reports success. Each rejected observation reports an erosion measure or names a practice from the other list."),
 ("explanation of how each method prevents erosion",
  "STB-1.E.1 states a goal and lists six methods and stops there, offering no mechanism for any of them and no ranking among them. Each rejected option quotes something the statement does supply."),
 ("gives a goal and the methods that serve it, one gives a second goal",
  "STB-1.E.1 pairs preventing erosion with six methods, STB-1.E.2 pairs improving fertility with three strategies, and STB-1.E.3 defines rotational grazing and names avoiding overgrazing as its purpose. One farm can apply all three at once."),
 ("prevent erosion, by contour plowing, windbreaks, perennial crops, terracing",
  "The keyed summary carries STB-1.E.1's goal and six methods, STB-1.E.2's three fertility strategies, and STB-1.E.3's definition and purpose. Each rejected summary swaps the two goals, substitutes practices the framework never names, or denies that goals and lists are given."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19, 20: q20, 21: q21}

e_check.run(e5_15, CLAIMS, TABLE_CHECKS)
