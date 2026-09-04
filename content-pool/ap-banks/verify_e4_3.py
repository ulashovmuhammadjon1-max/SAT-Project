"""Key audit for AP ENVIRONMENTAL SCIENCE 4.3 Soil Composition and Properties.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-4.C.1  Water holding capacity, the total amount of water soil can hold,
           varies with different soil types. Water retention contributes to land
           productivity and fertility of soils.
                   -- items 1, 2, 3, 14, 15, 17, 18, 19, 20, 30
ERT-4.C.2  The particle size and composition of each soil horizon can affect the
           porosity, permeability, and fertility of the soil.
                   -- items 4, 5, 15, 16, 25, 26, 27, 28, 30
ERT-4.C.3  There are a variety of methods to test the chemical, physical, and
           biological properties of soil that can aid in a variety of decisions,
           such as irrigation and fertilizer requirements.
                   -- items 6, 7, 8, 13, 14, 29, 30
ERT-4.C.4  A soil texture triangle allows for the identification and comparison
           of soil types based on their percentages of clay, silt, and sand.
           Loam consists of a blend of clay, silt, and sand that can support a
           variety of crops.
                   -- items 9, 10, 11, 12, 15, 21, 22, 23, 30

WHAT THE FRAMEWORK WITHHOLDS, AND WHAT THIS MODULE THEREFORE WITHHOLDS TOO.
ERT-4.C.1 says the capacity VARIES with soil type; it never says which type holds
most. ERT-4.C.2 says particle size and composition CAN AFFECT porosity,
permeability and fertility; it never says in which direction. So items 18, 25, 26,
27 and 28 are readings of a tabulated record, and their claims below say so: the
framework licenses the question, and the table settles the answer. No key in this
module states a direction or a ranking as an assertion of the framework.

LOAM. ERT-4.C.4 calls loam a BLEND of clay, silt, and sand. Item 22 turns on an
arithmetic criterion the table settles -- exactly one sample has no component
above half -- and not on any numerical boundary between named soil types, since
the framework fixes none.

TWO HEDGES ARE KEYED AS HEDGES: ERT-4.C.3's decisions SUCH AS irrigation and
fertilizer requirements (item 8) and ERT-4.C.2's CAN AFFECT (item 16). No key
elsewhere hardens either.

DATA ITEMS: 17 to 29. Every keyed ranking, difference, direction and percentage
sum is recomputed below from that table alone. The texture percentages are
checked to add to exactly one hundred in every sample, which is the arithmetic
the missing soil texture triangle would otherwise carry.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. Reversing every numeric column at
once preserves a co-varying gradient, a within-row sum and an agreement between
two columns, so for those items e_check flattens the table next and the check
fails on the strictness, the uniqueness or the row sum it also asserts.
``python3 verify_e4_3.py --selftest`` is the same run; the controls are not
behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e4_3

WHC = "Water the soil can hold (centimeters of water per meter of soil)"
YIELD = "Grain yield recorded on it (tonnes per hectare)"
CLAY = "Clay (percent)"
SILT = "Silt (percent)"
SAND = "Sand (percent)"
DIAMETER = "Typical particle diameter (millimeters)"
POROSITY = "Porosity (percent of the volume that is pore space)"
PERMEABILITY = "Permeability (centimeters of water passing through per hour)"
NITROGEN = "Nitrogen found in the soil (kilograms per hectare)"
HELDWATER = "Water held by the soil at the time of the test (percent by volume)"
FERTILIZER = "Fertilizer the grower then applied (kilograms per hectare)"
IRRIGATION = "Irrigation the grower then applied (millimeters)"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def _falls(v):
    return all(v[i + 1] < v[i] for i in range(len(v) - 1))


def _by(table, key_header, *headers):
    keys = cg.col(table, key_header)
    order = sorted(range(len(table["rows"])), key=lambda i: keys[i])
    return [[cg.col(table, h)[i] for i in order] for h in headers]


def _unique_max(values):
    i = max(range(len(values)), key=lambda k: values[k])
    assert values.count(values[i]) == 1, f"the maximum must be unique; got {values}"
    return i


def _unique_min(values):
    i = min(range(len(values)), key=lambda k: values[k])
    assert values.count(values[i]) == 1, f"the minimum must be unique; got {values}"
    return i


def q17(table, item):
    held = cg.col(table, WHC)
    assert len(set(held)) == len(held), \
        f"the four soil types must differ in what they can hold; got {held}"
    assert min(held) > 0, f"every soil type must hold some water; got {held}"
    return (f"the four capacities read {held} centimeters of water per meter of soil, all "
            "different and all above zero")


def q18(table, item):
    labs = cg.labels(table)
    held = cg.col(table, WHC)
    i = _unique_max(held)
    assert labs[i] == "Clay loam", \
        f"the largest capacity must belong to the clay loam; got {labs[i]}"
    return (f"the capacities are {dict(zip(labs, held))} and the largest is unique and "
            f"belongs to {labs[i]}")


def q19(table, item):
    loam = cg.cell(table, "Loam", WHC)
    sand = cg.cell(table, "Coarse sand", WHC)
    gap = loam - sand
    assert gap == 110, f"the difference must be 110 centimeters per meter; got {gap}"
    assert gap != loam and gap != sand, \
        "the difference must not coincide with either capacity"
    other = cg.cell(table, "Clay loam", WHC) - cg.cell(table, "Sandy loam", WHC)
    assert gap != other, f"a different pair must give a different difference; got {other}"
    return (f"the loam holds {loam:.0f} and the coarse sand {sand:.0f} centimeters per "
            f"meter, a difference of {gap:.0f}, against {other:.0f} for the other pair")


def q20(table, item):
    (yields,) = _by(table, WHC, YIELD)
    assert _rises(yields), \
        f"the yield must rise with the water the soil can hold; got {yields}"
    assert len(set(yields)) == len(yields), "'the same yield on all four' must be false"
    return (f"ordered by the water each soil can hold the yields read {yields} tonnes per "
            "hectare, strictly increasing")


def q21(table, item):
    clay = cg.col(table, CLAY)
    silt = cg.col(table, SILT)
    sand = cg.col(table, SAND)
    sums = [c + s + a for c, s, a in zip(clay, silt, sand)]
    for i, total in enumerate(sums, 1):
        assert abs(total - 100) < 1e-9, (
            f"sample {i}: {clay[i - 1]} clay plus {silt[i - 1]} silt plus {sand[i - 1]} "
            f"sand must be 100 percent, not {total}"
        )
    assert all(t <= 100 for t in sums), "'they add to more than one hundred' must be false"
    return (f"the clay {clay}, silt {silt} and sand {sand} percentages add to {sums} "
            "in the four samples, exactly one hundred in every one")


def q22(table, item):
    labs = cg.labels(table)
    clay = cg.col(table, CLAY)
    silt = cg.col(table, SILT)
    sand = cg.col(table, SAND)
    largest = [max(c, s, a) for c, s, a in zip(clay, silt, sand)]
    blends = [lab for lab, m in zip(labs, largest) if m <= 50]
    assert blends == ["Sample 2"], \
        f"exactly the second sample must have no component above half; got {blends} " \
        f"from largest shares {dict(zip(labs, largest))}"
    dominated = [lab for lab, m in zip(labs, largest) if m > 50]
    assert len(dominated) == len(labs) - 1, \
        "'all four equally' must be false: the other three must each be dominated"
    return (f"the largest single component of each sample reads "
            f"{dict(zip(labs, largest))} percent, so exactly one sample has none above "
            f"half and the other {len(dominated)} are each dominated by one component")


def q23(table, item):
    labs = cg.labels(table)
    clay = cg.col(table, CLAY)
    i = _unique_max(clay)
    assert labs[i] == "Sample 3", \
        f"the largest clay share must belong to the third sample; got {labs[i]}"
    return f"the clay shares are {dict(zip(labs, clay))} percent and the largest is {labs[i]}"


def q24(table, item):
    silt = cg.col(table, SILT)
    span = max(silt) - min(silt)
    assert span == 58, f"the silt shares must span 58 percentage points; got {span}"
    assert span != max(silt) and span != min(silt), \
        "the span must not coincide with either endpoint"
    return (f"the silt shares run {max(silt):.0f} down to {min(silt):.0f} percent, a span "
            f"of {span:.0f} points")


def q25(table, item):
    (perm,) = _by(table, DIAMETER, PERMEABILITY)
    assert _rises(perm), \
        f"ordered by rising particle size the permeability must rise, so finer particles " \
        f"pass water more slowly; got {perm}"
    assert len(set(perm)) == len(perm), "'the same speed in all three' must be false"
    assert min(perm) > 0, f"water must pass through every horizon; got {perm}"
    return (f"ordered by particle diameter the permeabilities read {perm} centimeters an "
            "hour, strictly increasing with the size of the particles and never zero")


def q26(table, item):
    (por,) = _by(table, DIAMETER, POROSITY)
    assert _falls(por), \
        f"ordered by rising particle size the porosity must fall, so finer particles hold " \
        f"more pore space; got {por}"
    assert min(por) > 0, f"the pore space must not reach zero in any horizon; got {por}"
    return (f"ordered by particle diameter the porosities read {por} percent, strictly "
            "decreasing, so the finest horizon carries the largest pore space and none is "
            "zero")


def q27(table, item):
    por = cg.col(table, POROSITY)
    perm = cg.col(table, PERMEABILITY)
    most_pore = _unique_max(por)
    slowest = _unique_min(perm)
    fastest = _unique_max(perm)
    # Named booleans, not a comparison between parallel tuples: one claim is that
    # the two columns rank the horizons oppositely, the other that they do not
    # rank them alike, and stating both separately is what keeps them straight.
    most_pore_is_slowest = most_pore == slowest
    most_pore_is_not_fastest = most_pore != fastest
    assert most_pore_is_slowest, (
        f"the horizon with the most pore space must be the slowest; porosity {por} points "
        f"at row {most_pore} and permeability {perm} at row {slowest}"
    )
    assert most_pore_is_not_fastest, \
        "'the horizon with the most pore space is also the fastest' must be false"
    return (f"the porosities {por} and the permeabilities {perm} rank the horizons in "
            f"opposite orders: the unique largest pore space and the unique smallest "
            f"permeability both fall on row {most_pore}")


def q28(table, item):
    labs = cg.labels(table)
    perm = cg.col(table, PERMEABILITY)
    diameter = cg.col(table, DIAMETER)
    por = cg.col(table, POROSITY)
    fastest = _unique_max(perm)
    coarsest = _unique_max(diameter)
    least_pore = _unique_min(por)
    assert fastest == coarsest, (
        f"the fastest horizon must be the coarsest; permeability {perm} points at row "
        f"{fastest} and diameter {diameter} at row {coarsest}"
    )
    assert fastest == least_pore, (
        f"the fastest horizon must also hold the least pore space; porosity {por} points "
        f"at row {least_pore}"
    )
    return (f"the largest permeability, the largest particle diameter and the smallest "
            f"porosity all fall on row {fastest}, {labs[fastest]}")


def q29(table, item):
    fertilizer_by_nitrogen, = _by(table, NITROGEN, FERTILIZER)
    irrigation_by_water, = _by(table, HELDWATER, IRRIGATION)
    more_nitrogen_less_fertilizer = _falls(fertilizer_by_nitrogen)
    more_water_less_irrigation = _falls(irrigation_by_water)
    assert more_nitrogen_less_fertilizer, (
        f"ordered by rising measured nitrogen the fertilizer applied must fall; got "
        f"{fertilizer_by_nitrogen}"
    )
    assert more_water_less_irrigation, (
        f"ordered by rising measured water the irrigation applied must fall; got "
        f"{irrigation_by_water}"
    )
    return (f"ordered by rising measured nitrogen the fertilizer applied reads "
            f"{fertilizer_by_nitrogen} kilograms per hectare and ordered by rising measured "
            f"water the irrigation reads {irrigation_by_water} millimeters, both strictly "
            "falling")


CLAIMS = [
 ("total amount of water a soil can hold",
  "ERT-4.C.1 defines water holding capacity as the total amount of water soil can hold. The rate at which water passes downward through a soil is permeability, which ERT-4.C.2 treats as a separate property."),
 ("The type of soil",
  "ERT-4.C.1 states that water holding capacity varies with different soil types, and names nothing else that it varies with. The rejected options substitute a quantity the statement never mentions or deny the variation outright."),
 ("Land productivity and the fertility of soils",
  "ERT-4.C.1 states that water retention contributes to land productivity and fertility of soils, naming both. The rejected options are quantities belonging to other topics or a denial of the statement."),
 ("Porosity, permeability, and fertility",
  "ERT-4.C.2 states that the particle size and composition of each soil horizon can affect the porosity, permeability, and fertility of the soil, naming all three. Two of the rejected options drop one or two of them."),
 ("particle size and its composition",
  "ERT-4.C.2 names the particle size and composition of each soil horizon as what can affect those properties. Slope and area belong to the watershed statement ERT-4.F.1 and the remaining pairs appear nowhere in this topic."),
 ("Chemical, physical, and biological properties",
  "ERT-4.C.3 states that there are a variety of methods to test the chemical, physical, and biological properties of soil, naming all three kinds. Each rejected option drops at least one of them."),
 ("such as irrigation and fertilizer requirements",
  "ERT-4.C.3 states that the methods can aid in a variety of decisions, such as irrigation and fertilizer requirements. Those are the two examples the statement gives, and none of the rejected decisions appears in it."),
 ("examples of the decisions rather than the whole list",
  "ERT-4.C.3 writes a variety of decisions, SUCH AS irrigation and fertilizer requirements, which makes the two named instances of a wider set. Treating them as the whole set is stronger than the statement and excluding either is weaker."),
 ("identification and comparison of soil types",
  "ERT-4.C.4 states that a soil texture triangle allows for the identification and comparison of soil types based on their percentages of clay, silt, and sand. It offers an identification and a comparison, and not a depth, a forecast, an age or a count."),
 ("Clay, silt, and sand",
  "ERT-4.C.4 names the percentages of clay, silt, and sand as the basis of the identification. Organic material belongs to ERT-4.B.2 and the horizon categories, and gravel, water and air appear nowhere in this statement."),
 ("A blend of clay, silt, and sand",
  "ERT-4.C.4 states that loam consists of a blend of clay, silt, and sand. Each rejected option removes at least two of the three components or substitutes one the statement never names."),
 ("Support a variety of crops",
  "ERT-4.C.4 states that loam consists of a blend of clay, silt, and sand that can support a variety of crops, and attributes no other capability to it. ERT-4.B.1 requires parent material for any soil to form at all."),
 ("aid decisions such as fertilizer requirements",
  "ERT-4.C.3 states that the methods for testing soil properties can aid in a variety of decisions, such as irrigation and fertilizer requirements, which is exactly the decision the grower is making. The rejected statements define a property, say what affects other properties, or describe a soil type."),
 ("total amount of water the soil can hold",
  "ERT-4.C.1 defines water holding capacity as the total amount of water soil can hold and ERT-4.C.3 names irrigation requirements among the decisions a soil test can aid, so the capacity is the quantity bearing on the decision. None of the rejected measurements is connected to irrigation anywhere in the framework."),
 ("every soil type holds the same amount of water",
  "ERT-4.C.1, ERT-4.C.2 and ERT-4.C.4 supply the four rejected statements in their own words. ERT-4.C.1 says the capacity VARIES with different soil types, which rules out its being the same in every type."),
 ("able to change those properties",
  "ERT-4.C.2 is written CAN AFFECT, which commits the framework to the connection while stopping short of asserting that every difference in particle size works through all three properties at once. Hardening it is stronger than the statement and denying it is weaker."),
 ("differs from one soil type to another",
  "Recomputed in q17 above: the four capacities are 60, 110, 170 and 190 centimeters of water per meter of soil, all different and all above zero. ERT-4.C.1 states that water holding capacity varies with different soil types."),
 ("The clay loam",
  "Recomputed in q18 above: the largest capacity in the record is unique and belongs to one soil type. ERT-4.C.1 states that water holding capacity VARIES with different soil types without saying which type holds most, so the ranking is settled by the tabulated measurements and not by the framework."),
 ("110 centimeters per meter more",
  "Recomputed in q19 above: 170 less 60 is 110, which coincides with neither capacity and differs from the gap between the other pair of soils. The rejected values are those other quantities."),
 ("hold more water recorded the higher yields",
  "Recomputed in q20 above: ordered by the water each soil can hold the yields run 1.8, 3.4, 5.1 and 5.6 tonnes per hectare, strictly increasing. ERT-4.C.1 states that water retention contributes to land productivity and fertility of soils."),
 ("add to one hundred in every one",
  "Recomputed in q21 above: the clay, silt and sand percentages add to exactly one hundred in each of the four samples, so between them they account for the whole of every sample and never for more. ERT-4.C.4 makes those three percentages the basis on which soil types are identified and compared."),
 ("no one of the three makes up more than half",
  "Recomputed in q22 above: in three of the four samples a single component exceeds fifty percent and in exactly one none does. ERT-4.C.4 states that loam consists of a BLEND of clay, silt, and sand, which is what a sample with no dominant component is and the others are not. The criterion is arithmetic and the framework fixes no numerical boundary between named soil types."),
 ("Sample 3",
  "Recomputed in q23 above: the clay shares are 12, 20, 55 and 8 percent and the largest is unique. ERT-4.C.4 makes the percentages of clay, silt, and sand the basis on which soil types are identified and compared."),
 ("By 58 points",
  "Recomputed in q24 above: the silt shares run from 78 down to 20 percent, a span of 58 points, which coincides with neither endpoint. The rejected values are those endpoints and a difference between a different pair of samples."),
 ("more slowly where the particles are finer",
  "Recomputed in q25 above: ordered by particle diameter the permeabilities are strictly increasing, so the finest horizon passes water most slowly. ERT-4.C.2 states that the particle size and composition of each horizon CAN AFFECT its permeability; the direction is read from the record, since the framework gives none."),
 ("pore space rises",
  "Recomputed in q26 above: ordered by particle diameter the porosities are strictly decreasing and none reaches zero, so the finest horizon carries the largest share of pore space. ERT-4.C.2 states that particle size can affect the porosity of the soil, and the direction is read from the record."),
 ("the horizon with the most pore space is the one water passes through most slowly",
  "Recomputed in q27 above: the unique largest porosity and the unique smallest permeability fall on the same horizon, so the two columns rank the horizons in opposite orders and cannot be one property measured twice. ERT-4.C.2 lists porosity and permeability separately among the properties particle size and composition can affect."),
 ("coarsest particles",
  "Recomputed in q28 above: the largest permeability, the largest particle diameter and the smallest porosity all fall on the same horizon, each unique in its column. ERT-4.C.2 states that particle size can affect the permeability of the soil."),
 # Both clauses: a distractor reverses both directions at once.
 ("found more nitrogen the grower applied less fertilizer, and where it found more water the grower applied less irrigation",
  "Recomputed in q29 above: ordered by rising measured nitrogen the fertilizer applied falls, and ordered by rising measured water the irrigation applied falls. ERT-4.C.3 states that methods for testing soil properties can aid in a variety of decisions, such as irrigation and fertilizer requirements."),
 ("loam being a blend of the three that supports a variety of crops",
  "ERT-4.C.1 supplies the definition, the variation with soil type and the contribution of water retention to land productivity and fertility; ERT-4.C.2 the three properties particle size and composition can affect; ERT-4.C.3 the three kinds of test and the two example decisions; and ERT-4.C.4 the basis of identification and the description of loam. Each rejected summary redefines the capacity, drops a kind of test, reverses what water retention does, or narrows what loam can support."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e4_3, CLAIMS, TABLE_CHECKS)
