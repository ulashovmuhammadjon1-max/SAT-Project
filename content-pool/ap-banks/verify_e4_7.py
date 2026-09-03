"""Key audit for AP ENVIRONMENTAL SCIENCE 4.7 Solar Radiation and Earth's Seasons.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` names the essential-knowledge statement the key rests on,
for a human to audit.

WHAT THE KEYS REST ON
---------------------
ENG-2.A.1  insolation is the Earth's main source of energy and depends on
           season and latitude                       -- items 1, 2, 17, 29
ENG-2.A.2  the angle of the sun's rays determines intensity; because of the
           shape of the Earth the latitude directly horizontal to the
           radiation receives the most intensity     -- items 3, 4, 7, 15, 18,
                                                        20, 23, 27, 28
ENG-2.A.3  highest radiation per unit area at the equator, decreasing toward
           the poles                                 -- items 5, 6, 19, 26, 30
ENG-2.A.4  radiation at a location varies seasonally, most on the longest
           summer day and least on the shortest winter day
                                                     -- items 9, 10, 13, 14, 22
ENG-2.A.5  axial tilt causes the seasons and the number of daylight hours
                                                     -- items 8, 11, 12, 16,
                                                        21, 24, 25

DATA ITEMS: 5, 6, 7, 8, 13, 14, 18, 21, 22 and 25 carry tables. Each keyed
conclusion is recomputed below from that table alone, and each check also
falsifies the distractors against the same numbers. No item asks a student to
recall a measured value, and no stem points at a figure the bank cannot show.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It runs every time, not behind
a flag.
"""
import e_check
import cg_check as cg
import e4_7

RAD_YEAR = ("Average solar radiation received per unit area over a year "
            "(watts per square meter)")
ANGLE = "Angle of the sun above the horizon at noon (degrees)"
ENERGY = "Solar energy reaching one square meter of level ground (watts)"
JUN_HRS = "Hours of daylight on June 21"
DEC_HRS = "Hours of daylight on December 21"
HRS = "Hours of daylight"
RAD_MONTH = "Solar radiation received per unit area (watts per square meter)"
JUN_RAD = "Solar radiation per unit area in June (watts per square meter)"
DEC_RAD = "Solar radiation per unit area in December (watts per square meter)"
NOON = "Angle of the sun above the horizon at noon on the March equinox (degrees)"
JUN_H = "Hours of daylight in June"
DEC_H = "Hours of daylight in December"


def q5(table, item):
    vals = cg.col(table, RAD_YEAR)
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)), \
        f"radiation must fall with latitude; got {vals}"
    assert vals[0] == max(vals), "the equator row must hold the maximum"
    assert vals[2] != max(vals), "the 40 degree row must not hold the maximum"
    return (f"the tabulated values {vals} fall from the equator to 80 degrees without a "
            "reversal, so the equator holds the maximum")


def q6(table, item):
    d = cg.cell(table, "0 degrees", RAD_YEAR) - cg.cell(table, "60 degrees", RAD_YEAR)
    assert d == 144, f"the difference recomputes to {d}, not 144"
    for wrong in (131, 189, 59, 406):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"275 minus 131 is {d:.0f} watts per square meter, and no distractor equals it"


def q7(table, item):
    pairs = sorted(zip(cg.col(table, ANGLE), cg.col(table, ENERGY)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"energy must rise with angle; got {pairs}"
    hi, lo = dict(pairs)[60.0], dict(pairs)[30.0]
    assert abs(lo - hi / 2) > 1, "halving the angle halves the energy, so 'proportional' would be true"
    assert max(pairs, key=lambda p: p[1])[0] != 45.0, "the 45 degree row must not be the maximum"
    return (f"sorted by angle the energies are {[e for _, e in pairs]}, strictly rising, and "
            f"30 degrees gives {lo} rather than half of {hi}")


def q8(table, item):
    swing = {lab: abs(cg.cell(table, lab, JUN_HRS) - cg.cell(table, lab, DEC_HRS))
             for lab in cg.labels(table)}
    biggest = max(swing, key=swing.get)
    assert biggest == "Site at 66 degrees north", f"the largest swing is at {biggest}"
    assert len(set(swing.values())) > 1, "'all four the same' must be false"
    return (f"the June to December differences are {sorted(swing.values())}, so the "
            "highest-latitude site changes most and the four are not equal")


def q13(table, item):
    rng = {lab: cg.cell(table, lab, JUN_RAD) - cg.cell(table, lab, DEC_RAD)
           for lab in cg.labels(table)}
    a, b = rng["Site A, 5 degrees north"], rng["Site B, 48 degrees north"]
    assert b > a, f"the higher-latitude range {b} does not exceed the equatorial range {a}"
    assert abs(b - a) > 1, "'about the same' must be false"
    assert a != 0 and b != 0, "'neither varies' must be false"
    assert cg.cell(table, "Site B, 48 degrees north", JUN_RAD) < \
        cg.cell(table, "Site A, 5 degrees north", JUN_RAD), \
        "'the higher-latitude site receives more in both months' must be false"
    return (f"Site A swings {a:.0f} watts and Site B swings {b:.0f}, and Site B is the lower "
            "of the two in June as well")


def q14(table, item):
    hrs = dict(zip(cg.labels(table), cg.col(table, HRS)))
    rad = dict(zip(cg.labels(table), cg.col(table, RAD_MONTH)))
    assert max(hrs, key=hrs.get) == "June", "June must hold the most daylight hours"
    assert max(rad, key=rad.get) == "June", "June must hold the most radiation"
    assert min(hrs, key=hrs.get) == "December", "December must hold the fewest daylight hours"
    return (f"June carries both the largest daylight figure {hrs['June']} and the largest "
            f"radiation figure {rad['June']}, and December carries the smallest day length")


def q18(table, item):
    vals = cg.col(table, NOON)
    assert vals[0] == 90, "the equator row must read 90 degrees on the equinox"
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)), \
        f"the noon angle must fall as latitude rises; got {vals}"
    assert len(set(vals)) > 1, "'the same at every latitude' must be false"
    assert any(v > 0 for v in vals), "'the sun does not rise anywhere' must be false"
    return (f"the tabulated angles {vals} start at 90 degrees over the equator and fall "
            "without a reversal toward the pole")


def q21(table, item):
    swing = {lab: abs(cg.cell(table, lab, JUN_HRS) - cg.cell(table, lab, DEC_HRS))
             for lab in cg.labels(table)}
    eq = swing["Site at the equator"]
    assert eq == min(swing.values()), f"the equatorial swing {eq} is not the smallest"
    assert eq < 0.5, f"the equatorial day length changes by {eq} hours, which is not 'unchanged'"
    assert cg.cell(table, "Site at the equator", DEC_HRS) > 0, \
        "'no daylight on December 21' must be false for the equator"
    assert cg.cell(table, "Site at the equator", JUN_HRS) < \
        max(cg.col(table, JUN_HRS)), "'longest June day' must be false for the equator"
    return (f"the equatorial row changes by {eq} hours against {sorted(swing.values())[1:]} "
            "at the other three sites, and its December value is above zero")


def q22(table, item):
    d = cg.cell(table, "June", RAD_MONTH) - cg.cell(table, "December", RAD_MONTH)
    assert d == 220, f"the difference recomputes to {d}, not 220"
    for wrong in (291, 109, 115, 362):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"291 minus 71 is {d:.0f} watts per square meter, and no distractor equals it"


def q25(table, item):
    p, q = "Site P, 40 degrees north", "Site Q, 40 degrees south"
    pj, pd = cg.cell(table, p, JUN_H), cg.cell(table, p, DEC_H)
    qj, qd = cg.cell(table, q, JUN_H), cg.cell(table, q, DEC_H)
    assert pj > pd, f"the northern site must have the longer June day; got {pj} against {pd}"
    assert qd > qj, f"the southern site must have the longer December day; got {qd} against {qj}"
    assert not (pj > qj and pd > qd), "'more daylight in both months' must be false"
    return (f"the northern site reads {pj} hours in June against {pd} in December while the "
            f"southern site reads {qj} against {qd}, so the long months are opposite")


CLAIMS = [
 ("supplies more of the energy",
  "ENG-2.A.1 states that incoming solar radiation, insolation, is the Earth's MAIN source of energy. Main means largest, so the key reads it as a comparison and not as an exclusive claim; the framework nowhere ranks the interior or combustion above sunlight."),
 ("season and the latitude",
  "ENG-2.A.1, near verbatim: insolation is dependent on season and latitude. The framework names no other control on the quantity arriving, so longitude, elevation, population and wind are all outside it."),
 ("determines the intensity of the radiation",
  "ENG-2.A.2, near verbatim: the angle of the sun's rays determines the intensity of the solar radiation. Nothing in the framework varies the sun's output through the day or makes the Earth-sun distance change across one afternoon."),
 ("most intense solar radiation of any latitude",
  "ENG-2.A.2 states that, due to the shape of the Earth, the latitude that is directly horizontal to the solar radiation receives the most intensity. The key restates that latitude's status; the rejected options invert it or attach a day-length rule the framework does not."),
 ("greatest at the equator and falls steadily",
  "Recomputed in q5 above. ENG-2.A.3 states that the highest solar radiation per unit area is received at the equator and decreases toward the poles, and the tabulated values fall monotonically from 275 to 86."),
 ("144",
  "Recomputed in q6 above from the two tabulated rows: 275 minus 131. The rejected values are one of the rows itself, a difference taken against the wrong row, and the sum instead of the difference."),
 ("increases as the sun stands higher",
  "Recomputed in q7 above: sorted by angle the energies rise without exception, which is the relationship ENG-2.A.2 asserts when it makes the angle of the rays the determinant of intensity. The strict-proportion reading is falsified on the same two rows."),
 ("66 degrees north",
  "Recomputed in q8 above: the June minus December day-length differences are 0.0, 3.7, 8.3 and 24.0 hours. ENG-2.A.5 attributes the number of hours of daylight at a location to the tilt of the Earth's axis of rotation."),
 ("longest summer day",
  "ENG-2.A.4, near verbatim: the most radiation is received during the location's longest summer day. The framework assigns the seasonal pattern to axial tilt in ENG-2.A.5 rather than to orbital distance or to weather."),
 ("shortest winter day",
  "ENG-2.A.4 pairs the annual minimum with the location's shortest winter day. A location's latitude is fixed through the year, so the option that moves it is not a statement the framework can support."),
 ("tilt of the Earth's axis of rotation",
  "ENG-2.A.5, near verbatim: the tilt of Earth's axis of rotation causes the Earth's seasons and the number of hours of daylight in a particular location. Rotation produces the daily alternation rather than the annual cycle."),
 ("tilt of the Earth's axis",
  "ENG-2.A.5 makes axial tilt the cause of the seasons, and ENG-2.A.2 ties intensity to the angle of the rays, so the correction replaces orbital distance with tilt and angle. The framework offers no seasonal role for solar output or atmospheric thickness."),
 ("higher-latitude site varies far more",
  "Recomputed in q13 above: 22 watts per square meter of seasonal swing at 5 degrees north against 183 at 48 degrees north. ENG-2.A.4 states that radiation at a location varies seasonally and ENG-2.A.1 makes that variation depend on latitude as well as season."),
 ("most daylight hours and the most radiation",
  "Recomputed in q14 above: June holds both the largest day length and the largest radiation figure in the table, which is the pairing ENG-2.A.4 describes for the longest summer day."),
 ("strike the curved surface at a lower angle",
  "ENG-2.A.2 traces the difference between latitudes to the shape of the Earth and to the angle of the rays, and ENG-2.A.3 records the resulting fall in radiation per unit area from the equator toward the poles. The framework never makes the pole-to-sun distance a cause."),
 ("no longer see its daylight hours change",
  "ENG-2.A.5 makes axial tilt the cause of both the seasons and the number of daylight hours, so removing the tilt removes both together. The equator-to-pole gradient of ENG-2.A.3 comes from the shape of the Earth and would remain."),
 ("season which the framework names",
  "ENG-2.A.1 names season and latitude together, so a prediction from latitude alone drops the seasonal half of the statement. Longitude, altitude and surface colour are not named as controls on insolation."),
 ("directly overhead at the equator",
  "Recomputed in q18 above: the tabulated noon angles fall from 90 degrees at the equator to 0 degrees at the pole. ENG-2.A.2 identifies the latitude lying directly horizontal to the radiation as the one receiving the greatest intensity."),
 ("lower latitudes receive more radiation per unit area",
  "ENG-2.A.3 states that the highest solar radiation per unit area is received at the equator and decreases toward the poles, and that is a statement about the amount received rather than about day length alone."),
 ("energy arriving on each square meter",
  "ENG-2.A.3 speaks of solar radiation per unit area and ENG-2.A.2 makes that quantity depend on the angle of the rays, so intensity is energy per area. A hemisphere-wide total, a count of hours and an air temperature each depend on more than the concentration of the beam."),
 ("day length is essentially unchanged",
  "Recomputed in q21 above: the equatorial row changes by 0.0 hours between the two dates while the other three change by 3.7, 8.3 and 24.0. ENG-2.A.5 ties the changing number of daylight hours to axial tilt."),
 ("220",
  "Recomputed in q22 above from the two tabulated months: 291 minus 71. The rejected values are the June figure alone, two adjacent-month gaps, and the sum of the two months."),
 ("sun stands lower above the horizon there",
  "ENG-2.A.2 makes the angle of the rays the determinant of intensity and ENG-2.A.3 puts the greatest radiation per unit area at the equator, so a long polar day does not by itself raise the energy on each square meter. Day length and intensity are separate quantities in the framework."),
 ("seasons and the number of daylight hours at a location",
  "ENG-2.A.5 names exactly two consequences of axial tilt, the Earth's seasons and the number of hours of daylight in a particular location. The rejected pairs attach the tilt to quantities the framework never links to it."),
 ("opposite months of the year",
  "Recomputed in q25 above: each site's long month is the other's short month on the tabulated hours. ENG-2.A.5 attributes the number of daylight hours at a location to the tilt of the Earth's axis of rotation."),
 ("Build nearer the equator",
  "ENG-2.A.3 puts the greatest radiation per unit area at the equator, and the day-length pattern of ENG-2.A.5 keeps the equatorial day near twelve hours while the high-latitude winter day shortens. Longitude sets clock time rather than the angle of the rays."),
 ("as the sun climbs higher through the morning",
  "The claim under test links a rising sun angle to a rising intensity, so the observation that tests it must vary the angle and watch the energy per unit area respond. ENG-2.A.2 is the statement being tested."),
 ("first student is correct",
  "ENG-2.A.2 attributes the latitude pattern to the shape of the Earth and to the angle at which the rays arrive, and ENG-2.A.3 records the resulting decrease from the equator toward the poles. The framework gives no causal role to a pole-to-sun distance."),
 ("how directly the rays can ever arrive",
  "ENG-2.A.1 makes insolation depend on both season and latitude, ENG-2.A.2 ties intensity to the arriving angle, and ENG-2.A.5 ties the seasonal change in angle and daylight to axial tilt. The rejected summaries drop one of the two named controls."),
 ("much closer to the equator",
  "ENG-2.A.3 states that radiation per unit area is greatest at the equator and decreases toward the poles, so moving equatorward raises the annual figure. Moving along a latitude changes longitude only, which the framework does not name as a control."),
]

TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 13: q13, 14: q14, 18: q18,
                21: q21, 22: q22, 25: q25}

e_check.run(e4_7, CLAIMS, TABLE_CHECKS)
