"""Key audit for AP ENVIRONMENTAL SCIENCE 4.9 El Nino and La Nina.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
ENG-2.C.1  El Nino and La Nina are phenomena associated with changing ocean
           surface temperatures in the Pacific Ocean, and can cause global
           changes to rainfall, wind, and ocean circulation patterns
                          -- items 1, 2, 5, 6, 7, 9, 11, 13, 15, 16, 19, 21,
                             23, 24, 25, 27, 30
ENG-2.C.2  El Nino and La Nina are influenced by geological and geographic
           factors and can affect different locations in different ways
                          -- items 3, 4, 8, 10, 12, 14, 17, 18, 20, 22, 26,
                             28, 29

THE DIRECTION OF A PHASE IS NEVER REQUIRED FROM MEMORY. The framework does not
state which phase warms the eastern Pacific, so no key here depends on knowing
it. Where an item needs a direction the STEM states it, following the CED's own
sample question 15; where a table names a warm phase and a cool phase, the
label is the stem's own and the key is a reading of the numbers.

DATA ITEMS: 3, 4, 5, 6, 8, 9, 10, 13, 14, 18, 20, 24, 26 and 28 carry tables.
Every check below anchors at least one assertion to a NAMED ROW, because
reversing two columns together preserves the pairing between them and a
pairing-only check would survive the corruption without noticing.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e4_9

SST_DEP = ("Sea surface temperature during the event compared with the long term "
           "average (degrees Celsius)")
RAIN_PCT = "Rainfall during the event as a percentage of the long term average (%)"
SST_MEAN = ("Mean sea surface temperature of the eastern equatorial Pacific "
            "(degrees Celsius)")
STN_RAIN = "Rainfall at a station on the eastern Pacific coast (millimeters)"
ANOM = ("Sea surface temperature above the long term average in the eastern "
        "equatorial Pacific (degrees Celsius)")
CATCH = "Fish landed by the coastal fishery (thousands of tonnes)"
W_NEUTRAL = "Mean surface wind speed in neutral years (meters per second)"
W_EVENT = "Mean surface wind speed during the event (meters per second)"
GLOB = ("Rainfall during the event as a percentage of that location's long term "
        "average (%)")
DEPTH = "Depth below the sea surface (meters)"
T_NEUTRAL = "Water temperature in neutral years (degrees Celsius)"
T_EVENT = "Water temperature during the event (degrees Celsius)"
WARMPH = "Rainfall in warm phase years as a percentage of the average (%)"
COOLPH = "Rainfall in cool phase years as a percentage of the average (%)"

EAST = "Eastern equatorial Pacific coast"
WEST = "Western equatorial Pacific"
INTERIOR = "Interior of a southern continent"
US_SITE = "Site in the central United States"


def q3(table, item):
    rain = dict(zip(cg.labels(table), cg.col(table, RAIN_PCT)))
    assert max(rain, key=rain.get) == EAST, f"the wettest region is {max(rain, key=rain.get)}"
    assert any(v > 100 for v in rain.values()), "no region is wetter than average"
    assert any(v < 100 for v in rain.values()), "no region is drier than average"
    assert len(set(rain.values())) > 1, "'the same proportion everywhere' must be false"
    return (f"the rainfall column reads {list(rain.values())} percent of average, so two "
            "regions are above 100 and two below in the same event year")


def q4(table, item):
    dep = {lab: abs(v - 100) for lab, v in
           zip(cg.labels(table), cg.col(table, RAIN_PCT))}
    assert max(dep, key=dep.get) == EAST, f"the largest departure is at {max(dep, key=dep.get)}"
    assert dep[EAST] == 160, f"the eastern departure recomputes to {dep[EAST]}, not 160"
    assert len(set(dep.values())) > 1, "'all four the same' must be false"
    return (f"the departures from 100 percent are {list(dep.values())} percentage points, "
            "largest on the eastern equatorial Pacific coast")


def q5(table, item):
    assert cg.cell(table, "Warm phase years", SST_MEAN) == max(cg.col(table, SST_MEAN)), \
        "the warm phase row must hold the highest sea surface temperature"
    pairs = sorted(zip(cg.col(table, SST_MEAN), cg.col(table, STN_RAIN)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"rainfall must rise with sea surface temperature; got {pairs}"
    assert pairs[0][1] != max(r for _, r in pairs), \
        "'highest rainfall with the coolest water' must be false"
    return (f"ordered by sea surface temperature the rainfall figures are "
            f"{[r for _, r in pairs]} millimeters, rising without exception")


def q6(table, item):
    d = cg.cell(table, "Warm phase years", STN_RAIN) - cg.cell(table, "Cool phase years", STN_RAIN)
    assert d == 780, f"the difference recomputes to {d}, not 780"
    for wrong in (600, 180, 900, 1020):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"900 minus 120 is {d:.0f} millimeters, and no distractor equals it"


def q8(table, item):
    assert cg.cell(table, "Year 2", ANOM) == max(cg.col(table, ANOM)), \
        "Year 2 must carry the largest temperature departure"
    pairs = sorted(zip(cg.col(table, ANOM), cg.col(table, CATCH)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"catch must fall as the departure grows; got {pairs}"
    assert pairs[-1][1] != max(c for _, c in pairs), \
        "'the warmest year produced the largest catch' must be false"
    return (f"ordered by temperature departure the catches are {[c for _, c in pairs]} "
            "thousand tonnes, falling without exception")


def q9(table, item):
    assert cg.cell(table, "Western section", W_NEUTRAL) == max(cg.col(table, W_NEUTRAL)), \
        "the western section must hold the highest neutral-year wind speed"
    for lab in cg.labels(table):
        n, e = cg.cell(table, lab, W_NEUTRAL), cg.cell(table, lab, W_EVENT)
        assert e < n, f"{lab} did not weaken: {n} to {e}"
    return ("each of the three sections falls from its neutral value to its event value, "
            "6.5 to 3.1, 5.8 to 2.4 and 4.9 to 2.2 meters per second")


def q10(table, item):
    pct = dict(zip(cg.labels(table), cg.col(table, GLOB)))
    assert abs(pct[US_SITE] - 100) < 10, \
        f"the central United States site reads {pct[US_SITE]}, which is not the near-unchanged one"
    assert any(v > 120 for v in pct.values()), "no location is clearly wetter than average"
    assert any(v < 80 for v in pct.values()), "no location is clearly drier than average"
    assert len(set(pct.values())) > 1, "'identical percentage changes' must be false"
    return (f"the five locations read {list(pct.values())} percent of their own averages, "
            "two clearly above, two clearly below and one within a few points of 100")


def q13(table, item):
    diffs = [cg.cell(table, lab, T_EVENT) - cg.cell(table, lab, T_NEUTRAL)
             for lab in cg.labels(table)]
    assert all(d > 0 for d in diffs), f"'cooler at every depth' must be false; got {diffs}"
    assert all(diffs[i] > diffs[i + 1] for i in range(len(diffs) - 1)), \
        f"the warming must fall with depth; got {diffs}"
    assert diffs[0] == max(diffs) and diffs[-1] == min(diffs), \
        "the surface must warm most and the deepest level least"
    assert len(set(diffs)) > 1, "'the same at all four depths' must be false"
    return (f"the event minus neutral differences are {diffs} degrees Celsius at 0, 50, 100 "
            "and 200 meters, falling steadily with depth")


def q14(table, item):
    warm = dict(zip(cg.labels(table), cg.col(table, WARMPH)))
    cool = dict(zip(cg.labels(table), cg.col(table, COOLPH)))
    swings = {lab: warm[lab] - cool[lab] for lab in warm}
    assert abs(swings["Region 3"]) < 20, \
        f"Region 3 swings by {swings['Region 3']}, which is not 'barely moves'"
    assert swings["Region 1"] > 100, f"Region 1 swings by {swings['Region 1']}, not a large fall"
    assert swings["Region 2"] < -50, f"Region 2 swings by {swings['Region 2']}, not a large rise"
    return (f"the warm minus cool swings are {list(swings.values())} percentage points, "
            "opposite in the first two regions and near zero in the third")


def q18(table, item):
    d = cg.cell(table, EAST, SST_DEP) - cg.cell(table, WEST, SST_DEP)
    assert abs(d - 3.4) < 1e-9, f"the span recomputes to {d}, not 3.4"
    for wrong in (1.2, 2.3, 1.9, 1.1):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"2.3 degrees above average against 1.1 degrees below leaves the two departures "
            f"{d:.1f} degrees Celsius apart")


def q20(table, item):
    assert cg.cell(table, "Year 2", ANOM) == max(cg.col(table, ANOM)), \
        "Year 2 must carry the largest temperature departure"
    pairs = sorted(zip(cg.col(table, ANOM), cg.col(table, CATCH)))
    assert all(pairs[i][1] > pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"an association must be present for the key to describe one; got {pairs}"
    assert len(table["headers"]) == 3, \
        "the table must not report fishing effort, which the rejected option claims to read"
    return (f"the catches fall from {pairs[0][1]:.0f} to {pairs[-1][1]:.0f} thousand tonnes "
            "as the departure grows, over only four years and two reported variables")


def q24(table, item):
    d = cg.cell(table, "Western section", W_NEUTRAL) - cg.cell(table, "Western section", W_EVENT)
    assert abs(d - 3.4) < 1e-9, f"the fall recomputes to {d}, not 3.4"
    for wrong in (2.7, 3.1, 1.6, 9.6):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return f"6.5 minus 3.1 is {d:.1f} meters per second in the western section"


def q26(table, item):
    dep = cg.cell(table, INTERIOR, SST_DEP)
    rain = cg.cell(table, INTERIOR, RAIN_PCT)
    assert dep == 0.0, f"the interior row must show no local temperature departure; got {dep}"
    assert rain < 100, f"the interior rainfall {rain} is not below average"
    assert abs(dep) != max(abs(v) for v in cg.col(table, SST_DEP)), \
        "'the largest departure in the table' must be false for this row"
    return (f"the interior row pairs a departure of {dep} degrees Celsius with rainfall at "
            f"{rain:.0f} percent of average, so rainfall fell without a local warming")


def q28(table, item):
    pct = cg.col(table, GLOB)
    n = sum(1 for v in pct if abs(v - 100) > 20)
    assert n == 4, f"{n} locations exceed twenty percentage points, not four"
    assert n != len(pct), "'all five' must be false"
    return (f"the departures from 100 percent are {[abs(v - 100) for v in pct]}, of which "
            f"{n} exceed twenty percentage points")


CLAIMS = [
 ("Pacific Ocean",
  "ENG-2.C.1, near verbatim: El Nino and La Nina are phenomena associated with changing ocean surface temperatures in the Pacific Ocean. The framework attaches them to no other ocean and to no atmospheric layer."),
 ("wind and ocean circulation",
  "ENG-2.C.1 states that these phenomena can cause global changes to rainfall, wind, and ocean circulation patterns, and names exactly those three. Daylight hours and the angle of the rays belong to ENG-2.A, which concerns solar input rather than these events."),
 ("different locations in different ways",
  "Recomputed in q3 above: two regions above and two below their long term rainfall average in one event year. ENG-2.C.2 states that El Nino and La Nina can affect different locations in different ways."),
 ("160 percentage points above average",
  "Recomputed in q4 above: departures of 160, 45, 30 and 25 percentage points from each region's own average. ENG-2.C.2 is the statement that leads a student to expect an unequal response across locations."),
 ("years with more rainfall",
  "Recomputed in q5 above: ordered by sea surface temperature the station's rainfall rises from 120 to 300 to 900 millimeters. ENG-2.C.1 makes changing Pacific surface temperatures what these phenomena are associated with and names rainfall among the patterns they change."),
 ("780",
  "Recomputed in q6 above from the two tabulated groups of years: 900 minus 120. The rejected values pair the wrong groups or add rather than subtract."),
 ("opposite directions",
  "The stem supplies the movement of warm water from the western to the eastern equatorial Pacific, following the CED's own sample question. ENG-2.C.1 then makes these phenomena a matter of changing Pacific surface temperatures that can cause global changes to rainfall, wind, and ocean circulation patterns."),
 ("years of much smaller catches",
  "Recomputed in q8 above: ordered by temperature departure the catches fall from 820 to 180 thousand tonnes without exception. The direction of the association is read from the data; the framework supplies only that these events involve changing Pacific surface temperatures."),
 ("weaker in every section",
  "Recomputed in q9 above: every section falls from its neutral-year wind speed to its event wind speed. ENG-2.C.1 names wind among the patterns these phenomena can change."),
 ("at some locations drier conditions at others",
  "Recomputed in q10 above: five locations at 62, 245, 150, 74 and 104 percent of their own averages. ENG-2.C.2 states that these phenomena can affect different locations in different ways, and the two African sites show the changes are not confined to the Pacific rim."),
 ("can be global",
  "ENG-2.C.1 places the changing surface temperatures in the Pacific and then says the changes to rainfall, wind, and ocean circulation patterns can be GLOBAL. ENG-2.C.2 adds that different locations are affected differently, which rules out an identical worldwide response."),
 ("Geological and geographic factors",
  "ENG-2.C.2, near verbatim: El Nino and La Nina are influenced by geological and geographic factors and can affect different locations in different ways. The framework names no chemical, solar or human control on the events themselves."),
 ("largest at the surface",
  "Recomputed in q13 above: warming of 7, 6, 4 and 1 degrees Celsius at 0, 50, 100 and 200 meters. ENG-2.C.1 identifies these phenomena with changing ocean SURFACE temperatures, which is where the tabulated change is concentrated."),
 ("swing in opposite directions",
  "Recomputed in q14 above: Region 1 falls 170 percentage points between the phases while Region 2 rises 95 and Region 3 moves 7. ENG-2.C.2 states that these phenomena can affect different locations in different ways."),
 ("can cause global changes to rainfall",
  "ENG-2.C.1 states that these phenomena can cause global changes to rainfall, wind, and ocean circulation patterns, so a location far from the Pacific is not automatically outside their reach. ENG-2.C.2 makes the responses differ by location rather than be identical."),
 ("Pacific sea surface temperature",
  "ENG-2.C.1 defines these phenomena by changing ocean surface temperatures in the Pacific and by the global changes to rainfall, wind, and ocean circulation they can cause, so the diagnostic pair is a Pacific temperature departure together with those pattern changes."),
 ("preparations may need to differ",
  "ENG-2.C.2 states that El Nino and La Nina can affect different locations in different ways, so one plan cannot be assumed to fit both coasts. ENG-2.C.1 makes the changes global rather than confined to the water itself."),
 ("3.4 degrees",
  "Recomputed in q18 above: 2.3 degrees Celsius above average against 1.1 degrees below, a span of 3.4. The rejected values quote one departure alone or subtract without carrying the two signs."),
 ("in one direction and in other periods",
  "ENG-2.C.1 associates BOTH El Nino and La Nina with changing ocean surface temperatures in the Pacific, and the learning objective names the pair as the El Nino-Southern Oscillation, which is a back and forth rather than a one-way trend."),
 ("supports further investigation",
  "Recomputed in q20 above: an association across four years between two reported variables, which is not enough to establish a sole cause and says nothing about fishing effort, a quantity the table does not report."),
 ("global changes to rainfall",
  "Heavier rain and drought are rainfall changes and a shift in surface currents is a change in ocean circulation, and ENG-2.C.1 names rainfall, wind, and ocean circulation patterns together. The rejected statements belong to topics 4.7 and 4.8."),
 ("influenced by geological and geographic factors",
  "ENG-2.C.1 states what the phenomena are associated with and what they can change; ENG-2.C.2 adds that they are influenced by geological and geographic factors and can affect different locations in different ways. It adds a cause and a qualification rather than relocating or narrowing the phenomena."),
 ("close to their long term average",
  "The claim under test makes a Pacific temperature departure the reason for a drought, so the observation that undercuts it is the same drought occurring without any such departure. Distance from the Pacific weakens nothing, since ENG-2.C.1 makes the changes global."),
 ("3.4 meters",
  "Recomputed in q24 above: 6.5 minus 3.1 meters per second in the western section. The rejected values come from the other sections, from one figure alone, or from adding the pair."),
 ("many years of large Pacific temperature",
  "The claim links a Pacific temperature departure to a rainfall response elsewhere, so the design must group many years by the size of the departure and compare the rainfall that follows. A single pair of years cannot separate the association from ordinary year to year variation."),
 ("reached it without a local temperature change",
  "Recomputed in q26 above: a sea surface temperature departure of 0.0 degrees Celsius beside rainfall at 70 percent of average. ENG-2.C.1 makes the rainfall changes global rather than local to the water that warmed."),
 ("in the same ocean",
  "ENG-2.C.1 names the two together as phenomena associated with changing ocean surface temperatures in the Pacific Ocean that can cause global changes to the same three patterns. ENG-2.C.2 then makes their effects vary by location, which is the opposite of one identical effect."),
 ("Four of the five",
  "Recomputed in q28 above: departures of 38, 145, 50, 26 and 4 percentage points, of which four exceed twenty. ENG-2.C.2 states that these phenomena can affect different locations in different ways."),
 ("affect different locations in different ways",
  "ENG-2.C.2, near verbatim, and a record wet basin beside a record dry basin in one event is exactly that. ENG-2.C.1 already names rainfall among the patterns these events change, so the option denying it contradicts the framework."),
 ("differ from place to place",
  "ENG-2.C.1 supplies the Pacific surface temperature association and the three global patterns, and ENG-2.C.2 supplies the influence of geological and geographic factors together with the different effects in different locations. The rejected summaries drop a pattern, move the ocean, or reverse the framework's order of causation."),
]

TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 6: q6, 8: q8, 9: q9, 10: q10, 13: q13, 14: q14,
                18: q18, 20: q20, 24: q24, 26: q26, 28: q28}

e_check.run(e4_9, CLAIMS, TABLE_CHECKS)
