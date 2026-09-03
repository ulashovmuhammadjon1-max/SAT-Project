"""Key audit for AP ENVIRONMENTAL SCIENCE 4.8 Earth's Geography and Climate.

One (anchor, claim) per item, in module order. The anchor is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
ENG-2.B.1  weather and climate are affected not only by the sun's energy but by
           geologic and geographic factors, such as mountains and ocean
           temperature   -- items 1, 5, 6, 7, 10, 11, 13, 14, 15, 20, 21, 23,
                            25, 26, 28, 30
ENG-2.B.2  a rain shadow is a region of land that has become drier because a
           higher elevation area blocks precipitation from reaching the land
                         -- items 2, 3, 4, 8, 9, 12, 16, 17, 18, 19, 22, 24,
                            27, 29

The framework supplies no mechanism, so no key here rests on rising air
cooling, on a lapse rate, or on the words windward and leeward. Where a stem
needs a wind direction or a moisture source it states one.

DATA ITEMS: 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 18, 19, 22, 26 and 30 carry
tables. Each keyed conclusion is recomputed below from that table alone, and
each check also falsifies the distractors against the same numbers.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs.
"""
import e_check
import cg_check as cg
import e4_8

ELEV = "Elevation (meters)"
PRECIP = "Average annual precipitation (millimeters)"
DIST_SEA = "Distance from the ocean (kilometers)"
WARM = "Mean temperature of the warmest month (degrees Celsius)"
COLD = "Mean temperature of the coldest month (degrees Celsius)"
WATER_NEAR = "Mean temperature of the water just offshore (degrees Celsius)"
AIR = "Mean annual air temperature of the city (degrees Celsius)"
BARRIER = ("Height of the land the moist winds must cross before reaching the city "
           "(meters)")
STN_PRECIP = "Average annual precipitation (millimeters)"
WATER_OFF = "Mean temperature of the offshore water (degrees Celsius)"
STRIP = "Mean annual precipitation of the coastal strip (millimeters)"
DIST_LAKE = "Distance from the large lake (kilometers)"
LAT = "Latitude (degrees north)"

EAST_PLAIN = "Site 5, plain east of the range"
WEST_PLAIN = "Site 1, plain west of the range"
WEST_SLOPE = "Site 2, western slope"
CREST = "Site 3, crest of the range"


def _spread(table, lab):
    return cg.cell(table, lab, WARM) - cg.cell(table, lab, COLD)


def q3(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, PRECIP)))
    driest = min(p, key=p.get)
    assert driest == EAST_PLAIN, f"the driest site is {driest}"
    assert p[WEST_PLAIN] > p[EAST_PLAIN], "the western plain must not be the driest"
    assert all(v > 0 for v in p.values()), "'every site receives some precipitation' is true, so it cannot be the key alone"
    return (f"the tabulated precipitation runs {list(p.values())} and the eastern plain "
            f"holds the minimum at {p[EAST_PLAIN]:.0f} millimeters")


def q4(table, item):
    d = cg.cell(table, WEST_SLOPE, PRECIP) - cg.cell(table, EAST_PLAIN, PRECIP)
    assert d == 2190, f"the difference recomputes to {d}, not 2,190"
    for wrong in (1640, 1290, 310, 2610):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"2,400 minus 210 is {d:.0f} millimeters, and no distractor equals it"


def q5(table, item):
    assert cg.cell(table, "Harbour town", DIST_SEA) == min(cg.col(table, DIST_SEA)), \
        "the harbour town must be the nearest to the ocean"
    pairs = sorted((cg.cell(table, lab, DIST_SEA), _spread(table, lab))
                   for lab in cg.labels(table))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"the annual spread must widen with distance from the sea; got {pairs}"
    assert cg.cell(table, "Harbour town", WARM) < max(cg.col(table, WARM)), \
        "'the nearest town has the highest warmest month' must be false"
    assert cg.cell(table, "Plains town", COLD) < max(cg.col(table, COLD)), \
        "'the farthest town has the highest coldest month' must be false"
    return (f"ordered by distance the warm-to-cold spreads are {[s for _, s in pairs]} "
            "degrees Celsius, strictly widening, and both comparison distractors are false")


def q6(table, item):
    d = _spread(table, "Plains town")
    assert d == 36, f"the spread recomputes to {d}, not 36"
    for wrong in (24, 30, 11, -6):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"30 minus negative 6 is {d:.0f} degrees Celsius at the town 400 kilometers inland"


def q7(table, item):
    assert cg.cell(table, "City J", WATER_NEAR) == min(cg.col(table, WATER_NEAR)), \
        "City J must sit beside the coldest offshore water"
    pairs = sorted(zip(cg.col(table, WATER_NEAR), cg.col(table, AIR)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"air temperature must rise with offshore water temperature; got {pairs}"
    assert all(w != a for w, a in pairs), "'exactly equal' must be false for every city"
    assert pairs[0][1] != max(a for _, a in pairs), \
        "'coldest water paired with warmest air' must be false"
    return (f"sorted by water temperature the air temperatures are {[a for _, a in pairs]}, "
            "rising without exception, and no pair is equal")


def q8(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, PRECIP)))
    b = dict(zip(cg.labels(table), cg.col(table, BARRIER)))
    assert min(p, key=p.get) == "City S", f"the driest city is {min(p, key=p.get)}"
    assert max(b, key=b.get) == "City S", f"the highest barrier belongs to {max(b, key=b.get)}"
    assert max(p, key=p.get) == "City R", "the wettest city must be the one behind the lowest land"
    return (f"City S pairs the smallest precipitation {p['City S']:.0f} with the largest "
            f"upwind barrier {b['City S']:.0f} meters")


def q9(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, STN_PRECIP)))
    far = "Station on the far side of the crest"
    assert min(p, key=p.get) == far, f"the driest station is {min(p, key=p.get)}"
    assert p["Station on the crest of the range"] > p[far], \
        "the crest must not be drier than the far side"
    return (f"the three stations read {list(p.values())} millimeters and the far side of the "
            "crest holds the minimum")


def q10(table, item):
    assert cg.cell(table, "Coast W", WATER_OFF) == min(cg.col(table, WATER_OFF)), \
        "Coast W must sit beside the coldest offshore water"
    pairs = sorted(zip(cg.col(table, WATER_OFF), cg.col(table, STRIP)))
    assert all(pairs[i][1] < pairs[i + 1][1] for i in range(len(pairs) - 1)), \
        f"precipitation must rise with offshore water temperature; got {pairs}"
    assert pairs[0][1] != max(s for _, s in pairs), \
        "'coldest water gets the most precipitation' must be false"
    return (f"sorted by water temperature the coastal precipitation figures are "
            f"{[s for _, s in pairs]}, rising without exception")


def q11(table, item):
    gaps = {lab: cg.cell(table, lab, WARM) - cg.cell(table, lab, COLD)
            for lab in cg.labels(table)}
    assert min(gaps, key=gaps.get) == "Lakeside site", \
        f"the narrowest gap belongs to {min(gaps, key=gaps.get)}"
    assert cg.cell(table, "Far site", WARM) == max(cg.col(table, WARM)), \
        "'the farthest site has the coolest warmest month' must be false"
    assert len(set(gaps.values())) > 1, "'all three the same' must be false"
    return (f"the warm-to-cold gaps are {list(gaps.values())} degrees Celsius at 1, 40 and "
            "150 kilometers from the lake, narrowest at the lakeside")


def q13(table, item):
    lats = cg.col(table, LAT)
    assert len(set(lats)) == 1, f"the two towns must share a latitude; got {lats}"
    a = cg.cell(table, "Town of Ardale", PRECIP)
    b = cg.cell(table, "Town of Belmar", PRECIP)
    assert a > b, f"Ardale {a} must be the wetter of the two, not Belmar {b}"
    assert a - b > 1000, f"the precipitation gap {a - b} is too small to need an explanation"
    return (f"both towns sit at {lats[0]:.0f} degrees north yet record {a:.0f} and {b:.0f} "
            f"millimeters, a gap of {a - b:.0f} that latitude cannot supply")


def q18(table, item):
    p = dict(zip(cg.labels(table), cg.col(table, PRECIP)))
    assert max(p, key=p.get) == WEST_SLOPE, f"the wettest site is {max(p, key=p.get)}"
    assert p[CREST] < p[WEST_SLOPE], "the crest must not out-rank the western slope"
    return (f"the precipitation column reads {list(p.values())} and the western slope holds "
            f"the maximum at {p[WEST_SLOPE]:.0f} millimeters")


def q19(table, item):
    east = cg.cell(table, EAST_PLAIN, PRECIP)
    west = cg.cell(table, WEST_PLAIN, PRECIP)
    assert east == 210 and west == 1850, f"the two plains read {east} and {west}"
    assert west > east, "the western plain must be the wetter of the two"
    rise = cg.cell(table, EAST_PLAIN, ELEV) - cg.cell(table, WEST_PLAIN, ELEV)
    assert abs(rise) < 500, (
        f"the two plains differ by {rise} meters, which is large enough to confound the "
        "comparison the key makes"
    )
    return (f"the eastern plain records {east:.0f} millimeters against {west:.0f} on the "
            f"western plain, with only {rise:.0f} meters of elevation between them")


def q22(table, item):
    e = dict(zip(cg.labels(table), cg.col(table, ELEV)))
    p = dict(zip(cg.labels(table), cg.col(table, PRECIP)))
    assert max(e, key=e.get) == CREST, f"the highest site is {max(e, key=e.get)}"
    assert min(p, key=p.get) == EAST_PLAIN, f"the driest site is {min(p, key=p.get)}"
    assert e[EAST_PLAIN] < e[CREST], "the driest site must be lower than the crest"
    assert p[CREST] > p[EAST_PLAIN], "the crest must not be the driest site"
    return (f"the crest is the highest at {e[CREST]:.0f} meters yet records "
            f"{p[CREST]:.0f} millimeters against {p[EAST_PLAIN]:.0f} on the lower eastern plain")


def q26(table, item):
    w = dict(zip(cg.labels(table), cg.col(table, WATER_NEAR)))
    a = dict(zip(cg.labels(table), cg.col(table, AIR)))
    assert max(w, key=w.get) == "City M", f"the warmest water is at {max(w, key=w.get)}"
    assert min(w, key=w.get) == "City J", f"the coldest water is at {min(w, key=w.get)}"
    d = a["City M"] - a["City J"]
    assert d == 17, f"the air temperature difference recomputes to {d}, not 17"
    for wrong in (19, 12, 6, 35):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"26 minus 9 is {d:.0f} degrees Celsius between the two extreme cities"


def q30(table, item):
    assert cg.cell(table, "Coast W", WATER_OFF) == min(cg.col(table, WATER_OFF)), \
        "Coast W must hold the coldest offshore water"
    assert cg.cell(table, "Coast W", STRIP) == min(cg.col(table, STRIP)), \
        "Coast W must hold the least precipitation"
    return ("the first row carries both the smallest water temperature and the smallest "
            "precipitation figure in the table")


CLAIMS = [
 ("such as mountains and the temperature",
  "ENG-2.B.1, near verbatim: weather and climate are affected not only by the sun's energy but by geologic and geographic factors, such as mountains and ocean temperature. Those two examples are the framework's own, and it names no others here."),
 ("drier because a higher elevation area",
  "ENG-2.B.2, near verbatim: a rain shadow is a region of land that has become drier because a higher elevation area blocks precipitation from reaching the land. The rejected options reverse the direction of the effect or substitute an optical shadow for the blocking of precipitation."),
 ("Site 5",
  "Recomputed in q3 above: with the moisture arriving from the west, the eastern plain lies beyond the crest and records the smallest precipitation in the table. ENG-2.B.2 places the rain shadow on the land whose precipitation the higher elevation area blocks."),
 ("2,190",
  "Recomputed in q4 above from the two tabulated rows: 2,400 minus 210. The rejected values pair the wrong rows or add the two figures instead of differencing them."),
 ("widens as a town lies farther",
  "Recomputed in q5 above: the warm-to-cold spreads are 11, 24 and 36 degrees Celsius at 2, 120 and 400 kilometers from the coast. ENG-2.B.1 names ocean temperature among the geographic factors affecting weather and climate."),
 ("36 degrees",
  "Recomputed in q6 above: 30 degrees Celsius in the warmest month against negative 6 in the coldest. The rejected values are the other towns' spreads or one tabulated temperature standing alone."),
 ("warmer offshore water have warmer",
  "Recomputed in q7 above: sorted by offshore water temperature the air temperatures rise without exception, and no city's air equals its water. ENG-2.B.1 names ocean temperature as a geographic factor affecting weather and climate."),
 ("City S",
  "Recomputed in q8 above: the driest city is the one behind the highest upwind land. That pairing is exactly what ENG-2.B.2 describes when it makes a rain shadow the land left drier because a higher elevation area blocks precipitation from reaching it."),
 ("far side of the crest",
  "Recomputed in q9 above: 300 millimeters beyond the crest against 2,100 on the side the winds reach first and 1,400 at the crest. ENG-2.B.2 places the rain shadow beyond the blocking higher ground."),
 ("warmer offshore water receive more",
  "Recomputed in q10 above: sorted by offshore water temperature the coastal precipitation figures rise without exception. ENG-2.B.1 names ocean temperature among the geographic factors affecting weather and climate, so the relationship is one the framework invites a student to read."),
 ("narrowest gap",
  "Recomputed in q11 above: warm-to-cold gaps of 18, 27 and 34 degrees Celsius at 1, 40 and 150 kilometers from the lake. ENG-2.B.1 places the temperature of a large body of water among the geographic factors affecting weather and climate."),
 ("not because the high ground itself is dry",
  "ENG-2.B.2 attributes the dryness to a higher elevation area BLOCKING precipitation from reaching the land beyond, so the cause lies in what the high ground does to the moisture rather than in any dryness of the high ground. The framework offers no reflection or absorption mechanism."),
 ("not only by the sun's energy",
  "Recomputed in q13 above: two towns at 44 degrees north recording 1,980 and 240 millimeters. ENG-2.B.1 is the only one of the five statements offered that admits an influence beyond the sun's energy, and the stem holds latitude constant so the four solar statements cannot separate the towns."),
 ("act alongside it",
  "ENG-2.B.1 says weather and climate are affected NOT ONLY by the sun's energy BUT ALSO by geologic and geographic factors, which asserts that both sets of influences operate together. The rejected options drop one side of that sentence or split weather from climate."),
 ("presence of mountains",
  "ENG-2.B.1 gives mountains and ocean temperature as its two examples of geologic and geographic factors. Daylight hours and axial tilt belong to ENG-2.A.5, which concerns the sun's energy rather than geography."),
 ("no longer be kept dry by blocked precipitation",
  "ENG-2.B.2 makes the higher elevation area the cause of the dryness, so removing that cause removes the effect the framework attributes to it. The framework attaches the dryness to blocked precipitation rather than to the land, to slope, or to a season."),
 ("several times as much precipitation as the basin",
  "ENG-2.B.2 makes a rain shadow the land left drier because a higher elevation area blocks precipitation, so the diagnostic comparison is between the dry land and the land on the far side of the blocking ground. Lower elevation, fewer species and warm summers are each consistent with dryness produced some other way."),
 ("Site 2 on the western slope",
  "Recomputed in q18 above: the western slope holds the largest precipitation figure in the table. ENG-2.B.2 places the drier land beyond the higher elevation area rather than before it."),
 ("crest between them blocks precipitation",
  "Recomputed in q19 above: 210 millimeters east of the crest against 1,850 west of it, with only 250 meters of elevation between the two plains. That is the situation ENG-2.B.2 defines as a rain shadow."),
 ("ocean temperature is a geographic factor",
  "ENG-2.B.1 names ocean temperature among the geologic and geographic factors that affect weather and climate, so a difference in offshore water temperature is a difference the framework recognises. It states no fixed direction for the effect on precipitation."),
 ("both on flat ground",
  "ENG-2.B.1 names mountains and ocean temperature as the geographic factors, and the keyed pair holds both constant along with latitude. Each rejected pair varies one of those two, and ENG-2.B.2 makes the blocking case a large difference rather than a small one."),
 ("is not what makes land dry",
  "Recomputed in q22 above: the crest is the highest site in the table yet records more than seven times the precipitation of the lower plain beyond it. ENG-2.B.2 makes the cause of a rain shadow the blocking of precipitation by higher ground, not the elevation of the dry land itself."),
 ("inland town at the same latitude and elevation",
  "A test of one factor must vary that factor and hold the others fixed. ENG-2.B.1 names ocean temperature and mountains as the geographic factors and ENG-2.A.1 makes latitude a control on insolation, so only the keyed comparison changes proximity to the ocean alone."),
 ("leaving it drier than the forest side",
  "ENG-2.B.2 defines a rain shadow as land made drier because a higher elevation area blocks precipitation from reaching it, which is the described contrast across a single range at one latitude. Neither fire history nor soil type is a factor the framework names."),
 ("shape how that energy plays out",
  "The enduring understanding ENG-2 states that most of the Earth's atmospheric processes are driven by input of energy from the sun, and ENG-2.B.1 adds geologic and geographic factors as further influences on weather and climate. The rejected options swap those two roles."),
 ("17 degrees",
  "Recomputed in q26 above: the city beside the warmest water reads 26 degrees Celsius and the city beside the coldest reads 9, a difference of 17. The rejected values difference the water temperatures instead, or the wrong pair of cities."),
 ("must cross the range before reaching",
  "ENG-2.B.2 puts the rain shadow on the land whose precipitation a higher elevation area blocks, so the moisture must meet the range before it could reach the plateau. Winds passing around the range would block nothing."),
 ("very different precipitation",
  "ENG-2.B.1 states that weather and climate are affected not only by the sun's energy but by geologic and geographic factors, and ENG-2.B.2 supplies a mechanism by which one district can be far drier than its neighbour at the same latitude. The framework does not deny latitude a role, so calling precipitation unrelated to it overshoots."),
 ("describes one specific way",
  "ENG-2.B.1 names mountains among the geographic factors affecting weather and climate and ENG-2.B.2 then defines the rain shadow, a specific consequence of higher elevation land. The second develops the first rather than contradicting or merely restating it."),
 ("Coast W",
  "Recomputed in q30 above: the same stretch of coast carries both the smallest offshore water temperature and the smallest coastal precipitation. ENG-2.B.1 names ocean temperature among the geographic factors affecting weather and climate."),
]

TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 11: q11,
                13: q13, 18: q18, 19: q19, 22: q22, 26: q26, 30: q30}

e_check.run(e4_8, CLAIMS, TABLE_CHECKS)
