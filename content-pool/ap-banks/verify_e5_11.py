"""Key audit for AP ENVIRONMENTAL SCIENCE 5.11 Ecological Footprints.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
EIN-2.N.1 is the topic's only statement: ecological footprints COMPARE RESOURCE
DEMANDS AND WASTE PRODUCTION required for AN INDIVIDUAL OR A SOCIETY. Three
things and no more -- two variables, joined by "and", and two scales, joined by
"or".

  the two variables       -- items 1, 3, 19, 20, 22, 24, 28
  the two scales          -- items 2, 4, 21, 25, 26
  data read at those      -- items 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
  what is NOT asserted    -- item 27
  the measure/goal split  -- items 23, 29 (chained to STB-1.A.1, named in the claim)
  the whole sentence      -- item 30

WHY SO MUCH DATA. One sentence cannot honestly carry thirty recall questions.
The topic's own suggested skill is 5.E, explain what the data implies, so
fourteen items carry a table and the answer is settled by the numbers, every
one of them recomputed below from that table alone and addressed by row label.

WHAT IS DELIBERATELY NOT KEYED anywhere in the module: that a footprint is an
AREA of land, global hectares, biocapacity, overshoot, or any real country. The
framework says none of it, and item 27 keys that absence rather than working
round it.

DATA ITEMS: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 and 18.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_11

RES4 = "Materials and energy used per person in a year (resource units)"
WASTE4 = "Waste produced per person in a year (waste units)"

FP = "Footprint per person in a year (units)"
POP = "Population (millions)"

RESH = "Water, fuel and materials used in a year (resource units)"
WASTEH = "Solid waste and wastewater produced in a year (waste units)"
H1 = "Household 1"
H2 = "Household 2"

RESC = "Resources used in the year (resource units)"
WASTEC = "Waste produced in the year (waste units)"
PRE = "Before the changes"
POST = "After the changes"

REST = "Resources used per person (resource units)"
WASTET = "Waste produced per person (waste units)"

P = "Person P"
Q = "Person Q"
FOOD = "Food and materials used (resource units)"
ENERGY = "Household energy used (resource units)"
LANDFILL = "Waste sent to landfill (waste units)"
SEWAGE = "Wastewater produced (waste units)"


def _totals(table):
    """Whole-population footprint per country, from the two tabulated columns."""
    return dict(zip(cg.labels(table),
                    [f * p for f, p in zip(cg.col(table, FP), cg.col(table, POP))]))


def q5(table, item):
    r, w = cg.col(table, RES4), cg.col(table, WASTE4)
    assert cg.cell(table, "Society A", RES4) == max(r), "Society A must lead the resource column"
    assert cg.cell(table, "Society A", WASTE4) == max(w), "Society A must lead the waste column"
    assert cg.cell(table, "Society D", RES4) == min(r), "Society D must trail the resource column"
    assert all(r[i] > r[i + 1] for i in range(len(r) - 1)), f"resource use must fall; got {r}"
    assert all(w[i] > w[i + 1] for i in range(len(w) - 1)), f"waste must fall with it; got {w}"
    return (f"resource use runs {r} units per person against waste of {w}, Society A leading "
            "both columns and Society D trailing both")


def q6(table, item):
    r, w = cg.col(table, RES4), cg.col(table, WASTE4)
    d = cg.cell(table, "Society A", RES4) - cg.cell(table, "Society D", RES4)
    assert d == 100, f"the difference recomputes to {d}, not 100"
    third = cg.cell(table, "Society C", RES4)
    for wrong in (max(r), max(r) + min(r), max(w) - min(w), max(r) - third):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"120 minus 20 is {d:.0f} resource units more per person in the highest society"


def q7(table, item):
    tot = _totals(table)
    per = dict(zip(cg.labels(table), cg.col(table, FP)))
    top_per = max(per, key=per.get)
    top_tot = max(tot, key=tot.get)
    assert top_per == "Country W", f"the largest per-person footprint is {top_per}, not Country W"
    assert top_tot == "Country X", f"the largest whole-population footprint is {top_tot}"
    assert top_per != top_tot, "the two scales must disagree for this item to have an answer"
    assert min(cg.col(table, POP)) == cg.cell(table, "Country W", POP), \
        "'the smallest population carries the largest total' must be checkable and false"
    assert tot["Country W"] != tot["Country X"], "'every total is the same size' must be false"
    return (f"per-person footprints are {per} while whole-population footprints are {tot} "
            f"million units, so {top_per} leads one scale and {top_tot} the other")


def q8(table, item):
    v = cg.cell(table, "Country X", FP) * cg.cell(table, "Country X", POP)
    tot = _totals(table)
    assert v == 480, f"Country X's whole-population footprint recomputes to {v}, not 480"
    for wrong in (cg.cell(table, "Country X", FP) + cg.cell(table, "Country X", POP),
                  tot["Country W"], tot["Country Y"], sum(tot.values())):
        assert v != wrong, f"the {wrong} distractor equals the key"
    return f"8 units per person times 60 million people is {v:.0f} million units in the year"


def q9(table, item):
    assert cg.cell(table, H1, RESH) > cg.cell(table, H2, RESH), \
        "the first household must place the larger demand on resources"
    assert cg.cell(table, H1, WASTEH) < cg.cell(table, H2, WASTEH), \
        "the second household must produce the larger amount of waste"
    return (f"the first household uses {cg.cell(table, H1, RESH):.0f} resource units against "
            f"{cg.cell(table, H2, RESH):.0f} but produces {cg.cell(table, H1, WASTEH):.0f} waste "
            f"units against {cg.cell(table, H2, WASTEH):.0f}, so the two halves disagree")


def q10(table, item):
    w = cg.col(table, WASTEH)
    d = cg.cell(table, H2, WASTEH) - cg.cell(table, H1, WASTEH)
    assert d == 45, f"the difference recomputes to {d}, not 45"
    for wrong in (max(w), max(w) + min(w),
                  cg.cell(table, H1, RESH) - cg.cell(table, H2, RESH), min(w)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"55 minus 10 is {d:.0f} waste units more from the second household in the year"


def q11(table, item):
    assert cg.cell(table, POST, RESC) < cg.cell(table, PRE, RESC), "resource use must fall"
    assert cg.cell(table, POST, WASTEC) < cg.cell(table, PRE, WASTEC), "waste must fall"
    return (f"resource use goes from {cg.cell(table, PRE, RESC):.0f} to "
            f"{cg.cell(table, POST, RESC):.0f} units and waste from "
            f"{cg.cell(table, PRE, WASTEC):.0f} to {cg.cell(table, POST, WASTEC):.0f}, both down")


def q12(table, item):
    before = cg.cell(table, PRE, RESC) + cg.cell(table, PRE, WASTEC)
    after = cg.cell(table, POST, RESC) + cg.cell(table, POST, WASTEC)
    assert before > 0, "the opening total must be non-zero for a share to exist"
    fall = 100 * (before - after) / before
    assert abs(fall - 30) < 1e-9, f"the fall recomputes to {fall} percent, not 30"
    for wrong in (70, 25, 50, 10):
        assert abs(fall - wrong) > 1e-9, f"the {wrong} percent distractor equals the key"
    return (f"the two columns total {before:.0f} units before and {after:.0f} after, a fall of "
            f"{fall:.0f} percent")


def q13(table, item):
    r, w = cg.col(table, REST), cg.col(table, WASTET)
    assert cg.cell(table, "First", REST) == min(r), "the first decade must carry the least use"
    assert all(r[i] < r[i + 1] for i in range(len(r) - 1)), f"resource use must rise; got {r}"
    assert all(w[i] < w[i + 1] for i in range(len(w) - 1)), f"waste must rise; got {w}"
    assert w[-1] / w[0] > r[-1] / r[0], \
        f"waste must rise faster: {w[-1] / w[0]} against {r[-1] / r[0]}"
    return (f"resource use runs {r} units per person and waste runs {w}, both rising and the "
            f"waste rising by a factor of {w[-1] / w[0]:.0f} against {r[-1] / r[0]:.1f}")


def q14(table, item):
    r, w = cg.col(table, REST), cg.col(table, WASTET)
    base = cg.cell(table, "First", WASTET)
    assert base > 0, "the first decade's waste must be non-zero for a ratio to exist"
    ratio = cg.cell(table, "Fourth", WASTET) / base
    assert ratio == 8, f"the ratio recomputes to {ratio}, not 8"
    for wrong in (r[-1] / r[0], 4, max(w) - min(w), 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"48 divided by 6 is {ratio:.0f} times as much waste per person in the fourth decade"


def q15(table, item):
    tot = _totals(table)
    per = dict(zip(cg.labels(table), cg.col(table, FP)))
    low_per = min(per, key=per.get)
    low_tot = min(tot, key=tot.get)
    assert low_per == "Country Z", f"the smallest per-person footprint is {low_per}"
    assert low_tot == "Country Z", f"the smallest whole-population footprint is {low_tot}"
    return (f"Country Z uses {per['Country Z']:.0f} units per person, the least of "
            f"{sorted(per.values())}, and carries {tot['Country Z']:.0f} million units in all, "
            f"the least of {sorted(tot.values())}")


def q16(table, item):
    tot = _totals(table)
    lo = min(tot.values())
    assert lo > 0, "the smallest total must be non-zero for a ratio to exist"
    ratio = max(tot.values()) / lo
    per = cg.col(table, FP)
    assert ratio == 12, f"the ratio recomputes to {ratio}, not 12"
    for wrong in (tot["Country X"] / tot["Country W"], max(per) / min(per), 2, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"480 million against 40 million units is {ratio:.0f} times as large between the "
            "largest and smallest whole-population footprints")


def q17(table, item):
    p_res = cg.cell(table, FOOD, P) + cg.cell(table, ENERGY, P)
    q_res = cg.cell(table, FOOD, Q) + cg.cell(table, ENERGY, Q)
    p_w = cg.cell(table, LANDFILL, P) + cg.cell(table, SEWAGE, P)
    q_w = cg.cell(table, LANDFILL, Q) + cg.cell(table, SEWAGE, Q)
    assert p_res > q_res, f"Person P must use more resources; got {p_res} against {q_res}"
    assert p_w < q_w, f"Person Q must produce more waste; got {p_w} against {q_w}"
    assert p_res + p_w < q_res + q_w, \
        f"Person Q's two halves together must be larger; got {p_res + p_w} against {q_res + q_w}"
    return (f"Person P uses {p_res:.0f} resource units against {q_res:.0f} but produces "
            f"{p_w:.0f} waste units against {q_w:.0f}, totalling {p_res + p_w:.0f} against "
            f"{q_res + q_w:.0f}")


def q18(table, item):
    p_w = cg.cell(table, LANDFILL, P) + cg.cell(table, SEWAGE, P)
    q_w = cg.cell(table, LANDFILL, Q) + cg.cell(table, SEWAGE, Q)
    assert p_w > 0, "Person P's waste must be non-zero for a ratio to exist"
    ratio = q_w / p_w
    assert ratio == 3, f"the ratio recomputes to {ratio}, not 3"
    for wrong in (2, 4, 0.5, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"36 waste units against 12 is {ratio:.0f} times as much from Person Q"


CLAIMS = [
 ("Resource demands and waste production",
  "EIN-2.N.1, near verbatim: ecological footprints compare RESOURCE DEMANDS AND WASTE PRODUCTION required for an individual or a society. Each rejected pair keeps at most one of the two variables the statement names."),
 ("For an individual or for a society",
  "EIN-2.N.1 says the comparison is of what is required FOR AN INDIVIDUAL OR A SOCIETY, so both scales sit inside the statement. Each rejected option excludes one of the two, or moves the measure to a species or an ecosystem the statement never mentions."),
 ("compares waste production as well as resource demands",
  "EIN-2.N.1 joins its two variables with AND, so omitting waste production drops half the measure. One distractor substitutes waste production FOR resource demands rather than adding it, which is the same mistake reversed, so the anchor carries the words as well as."),
 ("covers an individual as well as a society",
  "EIN-2.N.1 says the comparison is of what is required for AN INDIVIDUAL OR A SOCIETY, so the individual is inside the statement. One distractor substitutes one scale for the other, so the anchor carries the words as well as."),
 ("Society A places the largest demand on resources and produces the most waste",
  "Recomputed in q5 above: 120, 75, 40 and 20 resource units per person against 40, 25, 12 and 6 waste units. EIN-2.N.1 makes those two variables the content of the comparison, and here both rank the four societies the same way."),
 ("100 resource units greater",
  "Recomputed in q6 above: 120 minus 20 units per person. The rejected values quote the highest society alone, add the two, take the difference in the waste column, or pair the highest society with the third rather than the fourth."),
 ("largest footprint per person is not the country",
  "Recomputed in q7 above: Country W leads per person at 32 units but carries 160 million in all, against Country X's 8 units per person and 480 million in all. EIN-2.N.1 licenses the comparison for an individual OR a society, and the two scales need not agree."),
 ("480 million units",
  "Recomputed in q8 above: 8 units per person times 60 million people. The rejected values add the two columns instead of multiplying them, give another country's whole-population total, or total all four countries together."),
 ("larger demand on resources while the second produces the larger amount of waste",
  "Recomputed in q9 above: 90 resource units against 60, but 10 waste units against 55. Because EIN-2.N.1 makes the footprint a comparison of BOTH variables, one household can lead on one half and trail on the other, and the anchor carries both halves because a distractor differs only in whether they agree."),
 ("45 waste units more",
  "Recomputed in q10 above: 55 minus 10 waste units. The rejected values quote the larger figure alone, add the two, take the difference in the resource column, or quote the smaller alone."),
 ("Both halves of the footprint fell",
  "Recomputed in q11 above: resource use 80 to 60 units and waste 20 to 10. Both variables EIN-2.N.1 names moved downward, and each rejected option reverses one direction, both, or denies any change."),
 ("By 30 percent",
  "Recomputed in q12 above: 100 units before against 70 after. The rejected values give the share remaining, the fall in the resource column alone, the fall in the waste column alone, or the fall in waste units read as a percentage."),
 ("rose across the record, and the waste half rose the faster",
  "Recomputed in q13 above: resource use 30, 45, 60 and 75 units per person against waste 6, 12, 24 and 48, so the waste half multiplies by eight while the resource half multiplies by two and a half. One distractor swaps which half rose faster, so the anchor carries that clause."),
 ("Eight times as much",
  "Recomputed in q14 above: 48 divided by 6 waste units per person. The rejected values come from the resource column, from halving the interval, from the difference rather than the ratio, or from denying that the two differ."),
 ("Country Z, which is lowest both per person",
  "Recomputed in q15 above: 4 units per person, the lowest of the four, and 40 million units in all, also the lowest. EIN-2.N.1 licenses the comparison at both scales, and here they agree."),
 ("Twelve times as large",
  "Recomputed in q16 above: 480 million units against 40 million. The rejected values compare the wrong pair of countries or divide the per-person column alone."),
 ("Person Q's footprint is the larger when both halves are counted",
  "Recomputed in q17 above: 80 resource units against 64 but 12 waste units against 36, totalling 92 against 100. Counting only the resource half would reverse the answer, which is why EIN-2.N.1 names both variables, and why the anchor carries the whose-is-larger clause."),
 ("Three times as much",
  "Recomputed in q18 above: 36 waste units against 12. The rejected values misadd one of the two columns or reverse which person produces more."),
 ("mass of rubbish a household sends to landfill",
  "EIN-2.N.1 divides the measure into resource demands and waste production, and rubbish leaving the household is what it produces rather than what it draws in. Food, fuel and floor space are demands, and the number of residents is a denominator rather than either variable."),
 ("volume of fresh water a household draws",
  "EIN-2.N.1 puts resource demands on one side of the comparison and waste production on the other, and water drawn in is a demand. Wastewater, rubbish, exhaust gas and sewage sludge are all outputs, which is the other half of the measure."),
 ("multiplies the per-person figure by the number of people",
  "EIN-2.N.1 licenses the comparison for an individual OR a society, and population size is what relates the two scales. Each rejected option gets that relation wrong, swaps which scale carries which variable, or denies that the scales differ."),
 ("resource demands and waste production of one society against those of another",
  "EIN-2.N.1 says footprints COMPARE resource demands and waste production required for an individual or a society, so like against like at either scale is what the sentence directly supports. Each rejected option pairs one of the framework's variables with something the sentence does not name."),
 ("sustainability is a separate question about using resources without depleting them",
  "EIN-2.N.1 makes a footprint a comparison and stops there. Whether use can continue without depletion for future generations is STB-1.A.1, a separate statement in topic 5.12, so being lower than a neighbour settles nothing about it."),
 ("resources that person demands and the waste that person produces",
  "EIN-2.N.1 names exactly two variables and allows the measure at the scale of an individual, so both variables are the minimum. Society size, age, a neighbour's demands and land area are none of the things the statement names."),
 ("number of people in the society, so that the whole-population figure",
  "EIN-2.N.1 licenses the comparison at the scale of an individual or of a society, and moving between those scales is division by the number of people. Land area, species counts and income are not variables the statement names."),
 ("resource demands and waste production per person are also small",
  "EIN-2.N.1 licenses the comparison for an individual as well as for a society, so the per-person figure exists and can be small or large independently of the total. Each rejected option drops one variable, substitutes land area, or denies one of the two scales."),
 ("expressed as an area of land",
  "EIN-2.N.1 names two variables and two scales and says nothing about the units in which a footprint is reported. Treating an area of land as part of the definition adds to the statement, while each rejected option quotes something the statement does assert."),
 ("measure of the waste the company produced",
  "EIN-2.N.1 makes the footprint a comparison of resource demands AND waste production, so a consumption total is half of it. Profit, land occupied and headcount are not variables the statement names."),
 ("One supplies a way of measuring what is demanded and discarded; the other supplies the goal",
  "EIN-2.N.1 is a measure, comparing resource demands and waste production, while STB-1.A.1 states the goal of living on Earth and using resources without depletion for future generations. One distractor is the exact swap of measure and goal, so the anchor carries both halves."),
 ("compares the resource demands and the waste production required for an individual or for a society",
  "The keyed summary is EIN-2.N.1 with nothing removed and nothing added. Each rejected summary drops one of the two variables, drops one of the two scales, substitutes an area the statement never mentions, or replaces the measure with the separate sustainability goal of STB-1.A.1."),
]

TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12,
                13: q13, 14: q14, 15: q15, 16: q16, 17: q17, 18: q18}

e_check.run(e5_11, CLAIMS, TABLE_CHECKS)
