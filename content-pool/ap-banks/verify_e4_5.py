"""Key audit for AP ENVIRONMENTAL SCIENCE 4.5 Global Wind Patterns.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ERT-4.E.1  Global wind patterns primarily result from the most intense solar
           radiation arriving at the equator, resulting in density differences
           and the Coriolis effect.

That single sentence is the whole of the topic. Its five separable claims and the
items resting on each:

    the patterns are GLOBAL                       -- items 16, 30
    they PRIMARILY result from the stated cause   -- items 4, 8, 30
    the radiation is most intense AT THE EQUATOR  -- items 1, 2, 9, 17, 18, 19, 30
    it results in DENSITY DIFFERENCES             -- items 3, 5, 6, 10, 20, 21, 22, 30
    and in the CORIOLIS EFFECT                    -- items 3, 5, 6, 11, 25, 29, 30
    the order of cause and result                 -- items 14, 15
    what the sentence does NOT say                -- items 12, 13

WHAT THE SENTENCE WITHHOLDS, AND WHAT NO KEY HERE SUPPLIES. It never states the
DIRECTION in which the Coriolis effect deflects a moving parcel of air, and it
names no prevailing wind and no band of latitude. Items 12 and 13 key those two
absences outright. Items 23, 24, 26, 27 and 29 do use hemispheric directions, but
only as readings of a TABULATED RECORD of measured deflections and measured
prevailing quarters: the framework licenses the question by naming the Coriolis
effect among the results, and the table settles the answer. That division is
stated in each of those claims below, so nobody can mistake a tabulated
observation for a framework assertion.

THE NORTH-SOUTH SWAP IS THIS TOPIC'S CHARACTERISTIC TRAP. Items 23, 26 and 27
each have a distractor that exchanges the two hemispheres, so each anchor names
BOTH clauses. An anchor reading only "curved to the right" would match the
swapped distractor exactly as well as the key -- the defect already found once in
verify_e2_1.py. Item 15's anchor likewise carries the cause and the result
together, since its distractors reverse the chain.

DATA ITEMS: 17 to 29. Every keyed direction, maximum, difference and count is
recomputed below from that table alone.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. The two records whose keyed
content is a set of DIRECTION STRINGS carry a numeric column as well -- the
degrees each path turned, and the days each wind blew from its quarter -- and
every check on them asserts a floor on that column (a turn of at least five
degrees, a wind on more than half the days). Reversing the column leaves the
floor satisfied, so e_check flattens it next and the floor fails. The same
flatten pass catches the co-varying gradients in the solar and density records.
``python3 verify_e4_5.py --selftest`` is the same run; the controls are not
behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e4_5

LATITUDE = "Middle of the band (degrees of latitude)"
RADIATION = "Solar radiation received (watts per square meter, annual average)"
TEMPERATURE = "Temperature (degrees Celsius)"
DENSITY = "Density (kilograms per cubic meter)"
TURNED = "Degrees by which its path had turned after one thousand kilometers"
DAYS = "Days in the year it blew from that quarter"

NORTH_TRADE = "Band from 5 to 25 degrees north"
SOUTH_TRADE = "Band from 5 to 25 degrees south"
NORTH_MID = "Band from 35 to 55 degrees north"
SOUTH_MID = "Band from 35 to 55 degrees south"

MIN_TURN = 5          # every trial must record a real deflection
HALF_A_YEAR = 182     # a prevailing wind must beat this
DAYS_IN_YEAR = 365


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


def _text_col(table, j):
    return [str(r[j]) for r in table["rows"]]


def _quarter(table, label):
    labs = cg.labels(table)
    assert labs.count(label) == 1, f"row {label!r} appears {labs.count(label)} times"
    return _text_col(table, 1)[labs.index(label)]


def _prevails(table, label):
    """A wind blows from its recorded quarter on more than half the year, not all of it."""
    days = cg.cell(table, label, DAYS)
    assert days > HALF_A_YEAR, \
        f"{label}: {days} days is not more than half the year, so nothing prevails"
    assert days < DAYS_IN_YEAR, f"{label}: {days} days would make the wind constant"
    return days


def q17(table, item):
    (radiation,) = _by(table, LATITUDE, RADIATION)
    assert _falls(radiation), \
        f"the radiation must fall as the latitude rises; got {radiation}"
    assert len(set(radiation)) == len(radiation), \
        "'the same in every band' must be false"
    return (f"ordered by latitude the readings run {radiation} watts per square meter, "
            "strictly decreasing")


def q18(table, item):
    labs = cg.labels(table)
    latitude = cg.col(table, LATITUDE)
    radiation = cg.col(table, RADIATION)
    brightest = _unique_max(radiation)
    lowest = _unique_min(latitude)
    assert brightest == lowest, (
        f"the band receiving most must be the band of lowest latitude; radiation "
        f"{radiation} points at row {brightest} and latitude {latitude} at row {lowest}"
    )
    return (f"the unique largest reading and the unique lowest latitude both fall on row "
            f"{brightest}, {labs[brightest]}")


def q19(table, item):
    low = cg.cell(table, "Band at 5 degrees", RADIATION)
    high = cg.cell(table, "Band at 85 degrees", RADIATION)
    gap = low - high
    assert gap == 210, f"the difference must be 210 watts per square meter; got {gap}"
    assert gap != low and gap != high, \
        "the difference must not coincide with either reading"
    other = cg.cell(table, "Band at 25 degrees", RADIATION) - \
        cg.cell(table, "Band at 65 degrees", RADIATION)
    assert gap != other, f"a different pair must give a different difference; got {other}"
    return (f"the lowest band reads {low:.0f} and the highest {high:.0f} watts per square "
            f"meter, a difference of {gap:.0f}, against {other:.0f} for the inner pair")


def q20(table, item):
    (density,) = _by(table, TEMPERATURE, DENSITY)
    assert _falls(density), \
        f"ordered by rising temperature the density must fall; got {density}"
    assert len(set(density)) == len(density), \
        "'all four have the same density' must be false"
    return (f"ordered by rising temperature the densities read {density} kilograms per "
            "cubic meter, strictly decreasing")


def q21(table, item):
    temperature = cg.col(table, TEMPERATURE)
    density = cg.col(table, DENSITY)
    densest = _unique_max(density)
    coldest = _unique_min(temperature)
    assert densest == coldest, (
        f"the densest air mass must be the coldest; density {density} points at row "
        f"{densest} and temperature {temperature} at row {coldest}"
    )
    return (f"the unique largest density and the unique lowest temperature both fall on "
            f"row {densest}")


def q22(table, item):
    warm = cg.cell(table, "Air mass 1", DENSITY)
    cold = cg.cell(table, "Air mass 4", DENSITY)
    warm_t = cg.cell(table, "Air mass 1", TEMPERATURE)
    cold_t = cg.cell(table, "Air mass 4", TEMPERATURE)
    assert warm_t > cold_t, \
        f"the first air mass must be the warmer; got {warm_t} against {cold_t}"
    gap = cold - warm
    assert abs(gap - 0.13) < 1e-9, \
        f"the densities must differ by 0.13 kilograms per cubic meter; got {gap}"
    assert abs(gap - warm) > 1e-9 and abs(gap - cold) > 1e-9, \
        "the difference must not coincide with either density"
    return (f"the warmest air mass reads {warm} and the coldest {cold} kilograms per cubic "
            f"meter, a difference of {gap:.2f}")


def _deflection(table):
    hemispheres = _text_col(table, 1)
    headings = _text_col(table, 2)
    sides = _text_col(table, 3)
    turns = cg.col(table, TURNED)
    for h, t in zip(hemispheres, turns):
        assert t >= MIN_TURN, \
            f"the {h.lower()} trial turned only {t} degrees, which is no deflection at all"
    return hemispheres, headings, sides, turns


def q23(table, item):
    hemispheres, _, sides, turns = _deflection(table)
    north = {s for h, s in zip(hemispheres, sides) if h == "Northern"}
    south = {s for h, s in zip(hemispheres, sides) if h == "Southern"}
    # Named booleans, not a comparison between parallel tuples: the two claims
    # are about different hemispheres and stating each separately is what keeps
    # a swapped comparison from reading as a correct one.
    northern_curved_right = north == {"The right"}
    southern_curved_left = south == {"The left"}
    assert northern_curved_right, f"the northern trials must curve right; got {north}"
    assert southern_curved_left, f"the southern trials must curve left; got {south}"
    assert north != south, "the two hemispheres must not curve the same way"
    return (f"the northern trials curved {sorted(north)} and the southern {sorted(south)}, "
            f"every path turning at least {MIN_TURN} degrees: {turns}")


def q24(table, item):
    hemispheres, headings, sides, turns = _deflection(table)
    for hemisphere in ("Northern", "Southern"):
        rows = [i for i, h in enumerate(hemispheres) if h == hemisphere]
        assert len(rows) == 2, f"{hemisphere}: two trials must be recorded; got {len(rows)}"
        assert len({headings[i] for i in rows}) == 2, \
            f"{hemisphere}: the two trials must have run in opposite directions"
        assert len({sides[i] for i in rows}) == 1, (
            f"{hemisphere}: both trials must curve to the same side; got "
            f"{[sides[i] for i in rows]}"
        )
    assert len(set(sides)) == 2, "the record must show both sides across the four trials"
    return (f"in each hemisphere the two trials ran in opposite directions and curved to "
            f"the same side; across the four trials the sides are {sorted(set(sides))} and "
            f"the turns {turns}")


def q25(table, item):
    hemispheres, _, sides, turns = _deflection(table)
    assert set(hemispheres) == {"Northern", "Southern"}, \
        f"both hemispheres must be represented; got {set(hemispheres)}"
    assert len(set(sides)) == 2, \
        f"the record must show a curving to two different sides; got {set(sides)}"
    assert min(turns) >= MIN_TURN, f"every path must have turned measurably; got {turns}"
    return (f"every one of the {len(turns)} trials records a path curving to one side or "
            f"the other by at least {MIN_TURN} degrees, in both hemispheres")


def q26(table, item):
    north = _quarter(table, NORTH_TRADE)
    south = _quarter(table, SOUTH_TRADE)
    north_days = _prevails(table, NORTH_TRADE)
    south_days = _prevails(table, SOUTH_TRADE)
    northern_from_northeast = north == "The northeast"
    southern_from_southeast = south == "The southeast"
    assert northern_from_northeast, f"the northern band must blow from the northeast; got {north!r}"
    assert southern_from_southeast, f"the southern band must blow from the southeast; got {south!r}"
    assert north != south, "the two bands must not record the same quarter"
    return (f"the northern band records {north!r} on {north_days:.0f} days and the southern "
            f"{south!r} on {south_days:.0f}, both more than half the year and different "
            "from one another")


def q27(table, item):
    north = _quarter(table, NORTH_MID)
    south = _quarter(table, SOUTH_MID)
    north_days = _prevails(table, NORTH_MID)
    south_days = _prevails(table, SOUTH_MID)
    northern_from_southwest = north == "The southwest"
    southern_from_northwest = south == "The northwest"
    assert northern_from_southwest, f"the northern band must blow from the southwest; got {north!r}"
    assert southern_from_northwest, f"the southern band must blow from the northwest; got {south!r}"
    assert north != south, "the two bands must not record the same quarter"
    return (f"the northern band records {north!r} on {north_days:.0f} days and the southern "
            f"{south!r} on {south_days:.0f}, both more than half the year and different "
            "from one another")


def q28(table, item):
    labs = cg.labels(table)
    days = [_prevails(table, lab) for lab in labs]
    assert len(set(days)) == len(days), f"the four counts must differ; got {days}"
    assert min(days) > HALF_A_YEAR, "every band must beat half the year"
    assert max(days) < DAYS_IN_YEAR, "'on every day of the year' must be false"
    return (f"the four bands record their quarter on {days} days, every count above "
            f"{HALF_A_YEAR} and below {DAYS_IN_YEAR}")


def q29(table, item):
    pairs = ((NORTH_TRADE, SOUTH_TRADE), (NORTH_MID, SOUTH_MID))
    for north_label, south_label in pairs:
        north = _quarter(table, north_label)
        south = _quarter(table, south_label)
        assert north != south, (
            f"{north_label} and {south_label} must record different quarters; both read "
            f"{north!r}"
        )
        _prevails(table, north_label)
        _prevails(table, south_label)
    return (f"in each of the {len(pairs)} pairs of bands the northern and southern quarters "
            "differ from one another while both blow on more than half the days, so the "
            "difference lies between the hemispheres rather than between the latitudes")


CLAIMS = [
 ("arriving at the equator",
  "ERT-4.E.1, near verbatim: global wind patterns primarily result from the most intense solar radiation arriving at the equator. The rejected options move that radiation to the poles, remove it altogether, or substitute a quantity belonging to another statement."),
 ("At the equator",
  "ERT-4.E.1 places the most intense solar radiation at the equator, and everything else in the sentence follows from that placement."),
 ("Density differences and the Coriolis effect",
  "ERT-4.E.1 states that the radiation results in density differences AND the Coriolis effect, naming both in one clause. Two rejected options keep one and drop the other, and temperature gradients belong to ERT-4.D.2 and the layers of the atmosphere."),
 ("the main one, without the framework excluding every other influence",
  "ERT-4.E.1 is written PRIMARILY result from, which commits the framework to the stated cause being the principal one while ruling nothing else out. Demoting it to one among equals is weaker than the statement and denying it contradicts the statement."),
 ("length of the day",
  "ERT-4.E.1 names density differences and the Coriolis effect as what the intense equatorial radiation results in, and makes the global wind patterns what primarily results from all of it. The length of the day appears nowhere in the statement."),
 ("Both follow from the same cause",
  "ERT-4.E.1 puts density differences and the Coriolis effect in a single clause following a single cause, so the statement gives both together rather than choosing between them."),
 ("global wind patterns primarily result from the most intense solar radiation",
  "ERT-4.E.1 is the only statement in this unit that supplies a cause for the winds. The rejected options are ERT-4.D.1, ERT-4.D.2, ERT-4.B.2 and ERT-4.F.1, none of which mentions wind at all."),
 ("with the Coriolis effect among the results rather than the whole cause",
  "ERT-4.E.1 makes the intense equatorial radiation the primary cause and lists the Coriolis effect among what that radiation results in. The student has promoted a result into the cause and dropped the cause the statement gives."),
 ("per square meter at a range of latitudes",
  "ERT-4.E.1 asserts that the radiation is most intense at one place rather than another, so a comparison across latitudes is what tests it. A single site, a rainfall count, a layer boundary and a gas share each measure something else."),
 ("differ in how much they have been heated",
  "ERT-4.E.1 states that the intense equatorial radiation results in density differences, so a record of density against heating is what bears on that claim. The rejected measurements belong to other statements or to none in this topic."),
 ("recorded in both hemispheres",
  "ERT-4.E.1 names the Coriolis effect among the results of the intense equatorial radiation, and a curving of a moving parcel is what that effect is observed as. None of the rejected quantities records a curving at all."),
 ("direction in which the Coriolis effect deflects",
  "ERT-4.E.1 supplies the four rejected options in its own words. It names the Coriolis effect without saying which way it turns a moving parcel, so that direction has to come from a measurement rather than from the framework."),
 ("names of the prevailing winds",
  "ERT-4.E.1 gives the cause, the two results and the global scale of the patterns, and names no wind and no band of latitude. A named prevailing wind can only come from a record of observations."),
 ("resulting in density differences and the Coriolis effect",
  "Uneven heating between the equator and higher latitudes is the density difference and the turning of moving air is the Coriolis effect, and ERT-4.E.1 names both as results of the intense equatorial radiation from which the wind patterns primarily follow."),
 # Cause and result together: every distractor reverses one link of the chain.
 ("The intense equatorial radiation comes first, the density differences and the Coriolis effect follow from it",
  "ERT-4.E.1 reads that global wind patterns primarily result from the most intense solar radiation arriving at the equator, RESULTING IN density differences and the Coriolis effect, so the radiation stands at the causal end and the wind patterns at the other. Each rejected option reverses a link in that chain."),
 ("the patterns are global",
  "ERT-4.E.1 opens with GLOBAL wind patterns, so the scale is part of the statement rather than an addition to it. Nothing in the framework narrows the patterns to one continent, one basin or one day."),
 ("falls steadily as the latitude rises",
  "Recomputed in q17 above: ordered by latitude the readings run 300, 270, 200, 130 and 90 watts per square meter, strictly decreasing. ERT-4.E.1 states that the most intense solar radiation arrives at the equator, and a record falling away from low latitudes is what that looks like in numbers."),
 ("band of lowest latitude",
  "Recomputed in q18 above: the unique largest reading and the unique lowest latitude fall on the same band. ERT-4.E.1 states that the most intense solar radiation arrives at the equator."),
 ("210 watts per square meter more",
  "Recomputed in q19 above: 300 less 90 is 210, which coincides with neither reading and differs from the gap between the inner pair of bands. The rejected values are those other quantities."),
 # Both halves of the direction: a distractor reverses it.
 ("the warmer an air mass is, the lower its density",
  "Recomputed in q20 above: ordered by rising temperature the densities run 1.29, 1.25, 1.20 and 1.16 kilograms per cubic meter, strictly decreasing. ERT-4.E.1 states that the intense equatorial radiation results in density differences; it gives no direction, so the direction is read from the record."),
 ("The coldest of the four",
  "Recomputed in q21 above: the unique largest density and the unique lowest temperature fall on the same air mass. ERT-4.E.1 names density differences among the results of uneven solar heating without saying which way they run, so the record settles it."),
 ("By 0.13 kilograms per cubic meter",
  "Recomputed in q22 above: 1.29 less 1.16 is 0.13, which coincides with neither density. The rejected values are the two densities themselves and a difference between a different pair of air masses."),
 # BOTH clauses: the distractor exchanges the two hemispheres, and an anchor
 # naming one of them would match it exactly as well as the key.
 ("curved to the right, and those released in the southern hemisphere curved to the left",
  "Recomputed in q23 above: both northern trials curved to one side, both southern trials to the other, and every path turned by at least five degrees. ERT-4.E.1 names the Coriolis effect among the results of the intense equatorial radiation and states no direction for it, so the direction here is the record's and not the framework's."),
 ("the parcel moving north and the parcel moving south curved to the same side",
  "Recomputed in q24 above: within each hemisphere the two trials ran in opposite directions and curved to the same side, while the two hemispheres curved oppositely. What differs between the trials that curved differently is the hemisphere and not the heading."),
 ("The Coriolis effect",
  "Recomputed in q25 above: every trial records a path curving measurably to one side or the other, in both hemispheres. ERT-4.E.1 names the Coriolis effect as one of the two things the intense equatorial radiation results in; density differences are the other, and the remaining terms belong to ERT-4.D.2, ERT-4.D.1 and ERT-4.F.1."),
 # BOTH clauses again: the distractor exchanges the two bands.
 ("the wind blew from the northeast, and in the southern band it blew from the southeast",
  "Recomputed in q26 above: the two bands nearer the equator record different quarters from one another and each recorded its quarter on more than half the days of the year. ERT-4.E.1 names no wind and no band, so the quarters come from the record."),
 ("the wind blew from the southwest, and in the southern band it blew from the northwest",
  "Recomputed in q27 above: the two middle latitude bands record different quarters from one another and each recorded its quarter on more than half the days of the year. The framework names no prevailing wind, so the quarters come from the record."),
 ("more than half the days of the year in every band",
  "Recomputed in q28 above: all four counts lie above 182 days and below 365, so every band has a prevailing wind without the wind being constant. That is what makes a recorded quarter a pattern rather than a single observation."),
 ("which the framework names among the results",
  "Recomputed in q29 above: in each pair of bands the northern and southern quarters differ from one another while both prevail, so the difference lies between the hemispheres rather than between the latitudes. ERT-4.E.1 names the Coriolis effect among the results of the intense equatorial radiation, and the rejected options belong to ERT-4.D.1, ERT-4.B.2 and ERT-4.F.1."),
 ("Global wind patterns primarily result from the most intense solar radiation arriving at the equator, which results in density differences",
  "ERT-4.E.1 supplies the global scale, the hedge PRIMARILY, the equatorial placement of the most intense radiation, and both named results. Each rejected summary hardens the hedge, moves the radiation to the poles, drops one of the two results, narrows the scale, or reverses the direction of the causation."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


# --------------------------------------------------------------- string controls
#
# e_check's table controls corrupt NUMBERS: it reverses each numeric column and,
# failing that, flattens it. In this module the keyed content of two records is a
# set of DIRECTION STRINGS -- which side a parcel curved to, which quarter a wind
# blew from -- and no numeric mutation touches them. So e_check's controls, on
# their own, would say nothing about whether q23, q24, q26, q27 or q29 reads the
# directions at all.
#
# These controls swap the strings instead: they exchange the northern and southern
# rows so that the record asserts the mirror image of what it does now, which is
# exactly the swap the distractors in items 23, 26 and 27 offer. Each check below
# must fail on the swapped record. A control that cannot fail is worse than none,
# so each mutation is asserted to change the table before it is used.

def _swap_rows(table, i, j, columns):
    """A copy of ``table`` with the named column indexes exchanged between two rows."""
    import copy
    t = copy.deepcopy(table)
    for c in columns:
        t["rows"][i][c], t["rows"][j][c] = t["rows"][j][c], t["rows"][i][c]
    assert t["rows"] != table["rows"], "the mutation changed nothing"
    return t


def _string_controls():
    fired = []

    def must_fail(label, check, table):
        try:
            check(table, None)
        except AssertionError:
            fired.append(label)
            return
        raise SystemExit(f"4.5 CONTROL FAILED: {label} did not raise")

    # Exchange the curving side between a northern and a southern trial, so the
    # record now says northern parcels curve left and southern ones curve right.
    flipped = _swap_rows(e4_5._T_DEFLECT, 0, 2, [3])
    flipped = _swap_rows(flipped, 1, 3, [3])
    assert {r[3] for r in flipped["rows"] if r[1] == "Northern"} == {"The left"}, \
        "the deflection mutation must actually invert the northern trials"
    must_fail("the hemispheres' deflection exchanged", q23, flipped)

    # Give one hemisphere two different sides, so no side belongs to a hemisphere.
    muddled = _swap_rows(e4_5._T_DEFLECT, 1, 2, [3])
    must_fail("one hemisphere given two different sides", q24, muddled)

    # Exchange the prevailing quarters between the paired northern and southern
    # bands, which is precisely the swapped distractor in items 26 and 27.
    swapped_trades = _swap_rows(e4_5._T_WINDS, 0, 1, [1])
    must_fail("the two bands near the equator exchanged", q26, swapped_trades)
    swapped_mid = _swap_rows(e4_5._T_WINDS, 2, 3, [1])
    must_fail("the two middle latitude bands exchanged", q27, swapped_mid)

    # Give a northern and a southern band the SAME quarter, which would leave the
    # mirroring that item 29 keys with nothing to rest on.
    same = _swap_rows(e4_5._T_WINDS, 0, 1, [1])
    same["rows"][1][1] = same["rows"][0][1]
    assert same["rows"][0][1] == same["rows"][1][1], "the mutation must equalise the pair"
    must_fail("a northern and a southern band given the same quarter", q29, same)

    print(f"    {len(fired)} string controls all raised as required "
          "(the numeric controls in e_check cannot reach a direction).")


if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

_string_controls()
e_check.run(e4_5, CLAIMS, TABLE_CHECKS)
