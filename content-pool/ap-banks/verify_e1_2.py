"""Key audit for AP ENVIRONMENTAL SCIENCE 1.2 Terrestrial Biomes.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
Items 1, 5, 6, 7, 12, 19, 20, 24, 27 and 29 rest on ERT-1.B.1: a biome contains
characteristic communities of plants and animals that result from, and are
adapted to, its climate. The direction of that sentence -- climate to community
-- is what items 12, 19 and 27 turn on.

Items 2 and 29 rest on ERT-1.B.2, the list of major terrestrial biomes: taiga,
temperate rainforests, temperate seasonal forests, tropical rainforests,
shrubland, temperate grassland, savanna, desert, and tundra.

Items 3, 13, 14, 15, 16, 17 and 28 rest on ERT-1.B.3: the global distribution of
nonmineral terrestrial natural resources, such as water and trees for lumber,
varies because of some combination of climate, geography, latitude and altitude,
nutrient availability, and soil. The phrase "some combination" is what makes
every single-factor option false.

Items 4, 10, 11, 21, 22, 23 and 30 rest on ERT-1.B.4: the worldwide distribution
of biomes is dynamic, has changed in the past, and may again shift as a result
of global climate changes.

BIOME NAMES. Items 18 and 25 use a biome name in the key. The content relied on
is only what the name itself carries: a temperate rainforest is by its name both
moderate in temperature and high in rainfall; a desert is by its name dry. No
item asks a student to produce a biome name from a climatogram, because the
framework tabulates no climate envelope for any of the nine names.

DATA ITEMS: 5, 6, 7, 8, 9, 10, 13, 15, 20, 21, 24 and 26 carry tables. Each
keyed conclusion is recomputed below from that table alone, and each check also
falsifies the distractors against the same numbers.

NEGATIVE CONTROL: ``python3 verify_e1_2.py --selftest`` corrupts a key, an
anchor, a table cell and the notation on purpose and confirms each check fires.
"""
import re
import sys

import cg_check as cg

_BANNED = [
    (re.compile(r"\\"), "a backslash: this subject is not typeset, so LaTeX prints raw"),
    (re.compile(r"(?<![A-Za-z])\d+\s?-\s?\d"), "a digit-hyphen-digit range: write 'to' instead"),
    (re.compile(r"\d\s?/\s?\d"), "a digit-slash-digit fraction: write it out in words"),
    (re.compile(r"\^"), "a bare caret, which prints raw outside a math span"),
    (re.compile(r"\$"), "a dollar sign, which the converter reads as inline math"),
]


def style(module):
    """No typeset notation anywhere in the module's student-facing text."""
    for i, item in enumerate(module.QUESTIONS, 1):
        texts = [item["q"], item["why"]] + list(item["choices"])
        t = item.get("table")
        if t:
            texts += [str(h) for h in t["headers"]] + [str(c) for r in t["rows"] for c in r]
        for text in texts:
            for pat, msg in _BANNED:
                hit = pat.search(text)
                assert not hit, f"{module.TOPIC[0]} q{i}: {msg} -- {hit.group(0)!r} in {text[:70]!r}"
    print(f"OK  {module.TOPIC[0]} notation: no typeset markup in "
          f"{len(module.QUESTIONS)} questions.")


TEMP = "Mean annual temperature (degrees Celsius)"
PRECIP = "Mean annual precipitation (millimeters)"
MTEMP = "Mean temperature (degrees Celsius)"
MPRECIP = "Mean precipitation (millimeters)"
SUMMER = "Mean summer temperature (degrees Celsius)"
EDGE = "Latitude of the northern edge of the forest (degrees north)"
SEASON = "Length of the frost-free growing season (days)"
VOLUME = "Standing timber volume (cubic meters per hectare)"
ELEVTEMP = "Mean annual temperature (degrees Celsius)"
TALL = "Mean height of the tallest plants (meters)"
ANNUAL = "Annual precipitation (millimeters)"
WARMSHARE = "Percent of annual precipitation falling in the four warmest months"
CONIFER = "Percent of pollen grains from cold-tolerant conifers"
BROAD = "Percent of pollen grains from warm-temperate broadleaf trees"
STORE = "Percent of plant species with deep water-storing tissue"
DROP = "Percent of plant species that lose their leaves before winter"
GROWTH = "Percent of yearly plant growth"


def _site_pairs(table):
    labs = cg.labels(table)
    t = dict(zip(labs, cg.col(table, TEMP)))
    p = dict(zip(labs, cg.col(table, PRECIP)))
    return labs, t, p


def q5(table, item):
    labs, t, p = _site_pairs(table)
    dt = abs(t["Site 1"] - t["Site 3"])
    dp = abs(p["Site 1"] - p["Site 3"])
    for a in range(len(labs)):
        for b in range(a + 1, len(labs)):
            pair = {labs[a], labs[b]}
            if pair == {"Site 1", "Site 3"}:
                continue
            close = (abs(t[labs[a]] - t[labs[b]]) <= dt
                     and abs(p[labs[a]] - p[labs[b]]) <= dp)
            assert not close, f"{pair} is at least as close on both columns as Site 1 and Site 3"
    assert abs(t["Site 1"] - t["Site 2"]) <= 1, "the temperature-matched distractor pair must be real"
    assert abs(p["Site 1"] - p["Site 2"]) > 2000, "that pair must nevertheless differ hugely in rainfall"
    assert abs(p["Site 2"] - p["Site 5"]) < 50, "the rainfall-matched distractor pair must be real"
    assert abs(t["Site 2"] - t["Site 5"]) > 30, "that pair must nevertheless differ hugely in temperature"
    return (f"Site 1 and Site 3 differ by {dt:.0f} degrees and {dp:.0f} millimeters, and no "
            "other pair is at least as close on both columns; the two single-column "
            "distractor pairs are each far apart on the other column")


def q6(table, item):
    labs, t, p = _site_pairs(table)
    assert min(t, key=t.get) == "Site 5", "Site 5 must hold the lowest temperature"
    assert sorted(p.values()).index(p["Site 5"]) <= 1, \
        "Site 5 must be among the two lowest precipitation totals"
    assert min(p, key=p.get) == "Site 2" and t["Site 2"] >= sorted(t.values())[-2], \
        "the driest site must be one of the warmest, so the dry-only distractor is not cold"
    assert p["Site 1"] == max(p.values()), "Site 1 must hold the highest precipitation total"
    return (f"Site 5 is coldest at {t['Site 5']:.0f} degrees and second driest at "
            f"{p['Site 5']:.0f} millimeters, while the driest site is one of the warmest")


def q7(table, item):
    labs, t, p = _site_pairs(table)
    assert abs(t["Site 1"] - t["Site 2"]) <= 1, "the stem's premise about temperature must hold"
    assert abs(p["Site 1"] - p["Site 2"]) > 2000, \
        "the two sites must differ greatly in precipitation for the key to hold"
    return (f"the two sites differ by {abs(t['Site 1'] - t['Site 2']):.0f} degree but by "
            f"{abs(p['Site 1'] - p['Site 2']):.0f} millimeters of annual rainfall")


def q8(table, item):
    temps = cg.col(table, MTEMP)
    rain = cg.col(table, MPRECIP)
    assert max(temps) - min(temps) <= 6, f"temperatures must be near-constant; got {temps}"
    assert min(temps) > 15, "the site must be warm in every month recorded"
    assert max(rain) > 10 * min(rain), f"rainfall must be far from even; got {rain}"
    return (f"the four temperatures span {max(temps) - min(temps):.0f} degrees while the "
            f"rainfall ranges from {min(rain):.0f} to {max(rain):.0f} millimeters")


def q9(table, item):
    temps = cg.col(table, MTEMP)
    rain = cg.col(table, MPRECIP)
    assert min(temps) > 20, f"the coldest month must be well above freezing; got {min(temps)}"
    hottest = temps.index(max(temps))
    assert rain.index(max(rain)) == hottest, \
        "the wettest and warmest months coincide, so that distractor is true and cannot be keyed"
    assert temps != sorted(temps), "'temperatures rise steadily' must be false"
    return (f"the lowest tabulated temperature is {min(temps):.0f} degrees, more than "
            "twenty above freezing, so no month approaches a growth-arresting value")


def q10(table, item):
    warm = cg.col(table, SUMMER)
    lat = cg.col(table, EDGE)
    assert all(warm[i + 1] > warm[i] for i in range(len(warm) - 1)), "summer temperature must rise"
    assert all(lat[i + 1] > lat[i] for i in range(len(lat) - 1)), "the forest edge must move north"
    return (f"summer temperature rises from {warm[0]} to {warm[-1]} degrees while the forest "
            f"edge moves from {lat[0]} to {lat[-1]} degrees north")


def q13(table, item):
    labs = cg.labels(table)
    rain = dict(zip(labs, cg.col(table, PRECIP)))
    days = dict(zip(labs, cg.col(table, SEASON)))
    vol = dict(zip(labs, cg.col(table, VOLUME)))
    assert max(rain, key=rain.get) == "Region A", "Region A must lead on precipitation"
    assert max(days, key=days.get) == "Region A", "Region A must lead on growing season"
    assert max(vol, key=vol.get) == "Region A", "Region A must lead on standing volume"
    assert days["Region C"] > days["Region B"] and rain["Region C"] == min(rain.values()), \
        "the driest region must really have the longer season of that pair, so the distractor is tempting"
    return (f"Region A leads all three columns, with {rain['Region A']:.0f} millimeters, "
            f"{days['Region A']:.0f} frost-free days and {vol['Region A']:.0f} cubic meters "
            "per hectare")


def q15(table, item):
    elev = [cg.num(r[0]) for r in table["rows"]]
    temps = cg.col(table, ELEVTEMP)
    tall = cg.col(table, TALL)
    assert all(elev[i + 1] > elev[i] for i in range(len(elev) - 1)), "elevations must ascend"
    assert all(temps[i + 1] < temps[i] for i in range(len(temps) - 1)), "temperature must fall"
    assert all(tall[i + 1] < tall[i] for i in range(len(tall) - 1)), "plant height must fall"
    assert tall[-1] != max(tall), "'tallest plants at the highest elevation' must be false"
    return (f"as elevation rises {elev}, temperature falls {temps} and plant height falls "
            f"{tall}, so both decrease together")


def q20(table, item):
    labs = cg.labels(table)
    tot = dict(zip(labs, cg.col(table, ANNUAL)))
    share = dict(zip(labs, cg.col(table, WARMSHARE)))
    assert len(set(tot.values())) == 1, f"the annual totals must be equal; got {tot}"
    assert abs(share["Site J"] - share["Site H"]) > 40, \
        "the seasonal distributions must differ sharply"
    return (f"both sites receive {list(tot.values())[0]:.0f} millimeters a year, but the "
            f"warm-season share differs by {abs(share['Site J'] - share['Site H']):.0f} "
            "percentage points")


def q21(table, item):
    depth = [cg.num(r[0]) for r in table["rows"]]
    con = cg.col(table, CONIFER)
    bro = cg.col(table, BROAD)
    assert all(depth[i + 1] > depth[i] for i in range(len(depth) - 1)), "rows must run shallow to deep"
    assert all(con[i + 1] > con[i] for i in range(len(con) - 1)), \
        "conifer pollen must increase with depth, that is, with age"
    assert all(bro[i + 1] < bro[i] for i in range(len(bro) - 1)), \
        "broadleaf pollen must decrease with depth"
    assert min(bro) > 0, "'only conifers are represented' must be false"
    assert bro[-1] != max(bro), "'the deepest sample holds the most broadleaf pollen' must be false"
    return (f"from the deepest sample to the shallowest, conifer pollen falls {con[::-1]} "
            f"and broadleaf pollen rises {bro[::-1]}, so the younger record is the "
            "warmer-adapted one")


def q24(table, item):
    labs = cg.labels(table)
    st = dict(zip(labs, cg.col(table, STORE)))
    dr = dict(zip(labs, cg.col(table, DROP)))
    storer = max(st, key=st.get)
    assert dr[storer] == min(dr.values()), \
        "the water-storing site must not also be the leaf-dropping site"
    assert st[storer] > 50 and dr[max(dr, key=dr.get)] > 50, \
        "each site must be dominated by one of the two traits"
    return (f"{storer} has {st[storer]:.0f} percent water-storing species and only "
            f"{dr[storer]:.0f} percent that drop their leaves, the reverse of the other site")


def q26(table, item):
    temps = cg.col(table, MTEMP)
    rain = cg.col(table, MPRECIP)
    grow = cg.col(table, GROWTH)
    assert max(rain) - min(rain) <= 10, f"precipitation must be near-constant; got {rain}"
    assert max(rain) < 2 * min(rain), "'precipitation varies by more than a factor of two' must be false"
    assert max(temps) - min(temps) > 25, f"temperature must vary widely; got {temps}"
    assert grow.index(max(grow)) == temps.index(max(temps)), \
        "peak growth must fall in the warmest month"
    assert grow.index(max(grow)) != rain.index(min(rain)), "peak growth is not tied to the rain minimum"
    assert len(set(grow)) > 1, "'growth is spread evenly' must be false"
    return (f"precipitation spans only {max(rain) - min(rain):.0f} millimeters while "
            f"temperature spans {max(temps) - min(temps):.0f} degrees, and the growth "
            "maximum falls in the warmest month")


CLAIMS = [
 ("result from, and are adapted to",
  "ERT-1.B.1, near verbatim: a biome contains characteristic communities of plants and animals that result from, and are adapted to, its climate. The sentence runs from climate to community, not the reverse, and it does not require the species to be found nowhere else."),
 ("Taiga",
  "ERT-1.B.2 lists taiga, temperate rainforests, temperate seasonal forests, tropical rainforests, shrubland, temperate grassland, savanna, desert and tundra as the major terrestrial biomes. Every rejected option is an aquatic biome listed under ERT-1.C."),
 ("some combination of climate",
  "ERT-1.B.3, near verbatim: the global distribution of nonmineral terrestrial natural resources varies because of some combination of climate, geography, latitude and altitude, nutrient availability, and soil. The phrase some combination rules out any single sufficient factor."),
 ("It is dynamic",
  "ERT-1.B.4, near verbatim: the worldwide distribution of biomes is dynamic; the distribution has changed in the past and may again shift as a result of global climate changes."),
 ("the closest pair on temperature",
  "Recomputed in q5 above. ERT-1.B.1 makes the community a result of the climate, and climate here is both tabulated columns, so the pair closest on both is the pair expected to hold the most similar communities. Each single-column match is checked far apart on the other column."),
 ("one of the two lowest",
  "Recomputed in q6 above. ERT-1.B.1 states that a biome's community is adapted to its climate, so the tolerances required at a site are read from both climate columns together. Only one site sits near the bottom of both."),
 ("climate includes precipitation",
  "Recomputed in q7 above: the two sites differ by one degree but by more than two thousand millimeters of rainfall. ERT-1.B.1 ties the community to the climate, and temperature alone is not the climate."),
 ("concentrated in part of the year",
  "Recomputed in q8 above: the four temperatures span a few degrees while the rainfall values differ by more than a factor of ten, which is the definition of uneven distribution across the year."),
 ("well above freezing",
  "Recomputed in q9 above: the lowest tabulated temperature is more than twenty degrees above freezing. A factor cannot be shown to be limiting by a record in which it never approaches a limiting value."),
 ("moved further north",
  "Recomputed in q10 above: mean summer temperature and the latitude of the forest edge both increase across the surveys. ERT-1.B.4 states that biome distribution may shift as a result of global climate changes."),
 ("may be replaced over time",
  "ERT-1.B.4 states that biome distribution is dynamic and may shift as a result of global climate changes, and ERT-1.B.1 ties the community present to the climate, so a large climate change is a reason to expect a change in the community."),
 ("similar climates",
  "ERT-1.B.1 states that the characteristic communities of a biome result from, and are adapted to, its climate, so a shared climate accounts for a shared community form without any shared history or shared species list."),
 ("the largest standing volume",
  "Recomputed in q13 above: one region leads on precipitation, on growing-season length and on standing timber volume. ERT-1.B.3 attributes the distribution of nonmineral resources such as trees for lumber to a combination of factors including climate."),
 ("fresh water and trees",
  "ERT-1.B.3 names water and trees for lumber as its examples of nonmineral terrestrial natural resources. Every rejected pair is a mineral or fossil deposit, which the word nonmineral excludes."),
 ("the vegetation becomes shorter",
  "Recomputed in q15 above: as elevation rises, both mean temperature and the height of the tallest plants fall. ERT-1.B.3 names latitude and altitude among the factors behind the distribution of terrestrial resources."),
 ("whose combination sets",
  "ERT-1.B.3 says the distribution varies because of some combination of climate, geography, latitude and altitude, nutrient availability, and soil, so latitude enters as one contributing factor rather than as a sufficient one."),
 ("nutrient availability",
  "ERT-1.B.3 lists nutrient availability and soil alongside climate, latitude and altitude. The stem holds every other listed factor constant, so those two are the only candidates the framework's own list leaves."),
 ("Moderate temperatures together with high",
  "The name carries both climate elements: temperate is the moderate temperature range and rainforest is heavy precipitation. ERT-1.B.1 ties the community present to those conditions. No climate envelope beyond the name itself is relied on."),
 ("runs the relationship the other way",
  "ERT-1.B.1 states that the characteristic communities of a biome result from, and are adapted to, its climate. The stated direction is climate to community, which is what the student has reversed."),
 ("the timing of precipitation",
  "Recomputed in q20 above: the two sites receive identical annual totals but differ by more than forty percentage points in the share falling in the warm season. ERT-1.B.1 makes the community a result of the climate, and when rain falls is part of a climate."),
 ("cold-tolerant to mostly warm-temperate",
  "Recomputed in q21 above: from the deepest sample to the shallowest the conifer share falls and the broadleaf share rises. ERT-1.B.4 states that the distribution of biomes has changed in the past."),
 ("once carried forest",
  "ERT-1.B.4 is a claim about change over time in where biomes occur, so evidence bearing on it must compare a place with its own past. A present-day map or species survey records no change."),
 ("dynamic and may shift",
  "The student's reasoning holds only if climate itself never moves. ERT-1.B.4 denies that, stating that the distribution of biomes has changed in the past and may shift again with global climate changes."),
 ("is the drier of the two",
  "Recomputed in q24 above: one site is dominated by water-storing species and the other by species that shed leaves before winter. ERT-1.B.1 makes the community adapted to its climate, so water-storing tissue points to a shortage of water."),
 ("receive very little precipitation",
  "The name desert carries aridity rather than heat, and ERT-1.B.1 ties a biome's community to its climate, so the shared feature justifying one classification across very different temperatures is the shared shortage of water."),
 ("temperature rather than precipitation limits growth",
  "Recomputed in q26 above: precipitation is near-constant across the record while temperature spans nearly thirty degrees and growth peaks in the warmest month. The variable that changes is the candidate for the limiting factor."),
 ("adapted to the climate",
  "ERT-1.B.1 states that the characteristic communities of a biome result from, and are adapted to, its climate, so a plant carried outside the climate it is adapted to has no reason to survive."),
 ("vary from place to place",
  "ERT-1.B.3 names trees for lumber as an example of a nonmineral terrestrial resource and attributes the uneven distribution of such resources to some combination of climate, geography, latitude and altitude, nutrient availability, and soil."),
 ("each with its own characteristic community",
  "ERT-1.B.2 lists temperate grassland and savanna as separate major terrestrial biomes, and ERT-1.B.1 makes each biome's community a result of its own climate, which is what keeps them distinct rather than interchangeable."),
 ("unmanaged sites",
  "ERT-1.B.4 attributes shifts in biome distribution to global climate changes, so the observation that separates that cause from local clearing is a consistent movement across many unmanaged sites accompanied by a measured change in climate."),
]

TABLE_CHECKS = {5: q5, 6: q6, 7: q7, 8: q8, 9: q9, 10: q10, 13: q13,
                15: q15, 20: q20, 21: q21, 24: q24, 26: q26}


def _selftest():
    """Negative control: every gate below must FAIL when its input is corrupted."""
    import copy
    import types

    def must_fail(label, mutate):
        mod = types.ModuleType("e1_2_mutant")
        mod.TOPIC = e1_2.TOPIC
        mod.QUESTIONS = copy.deepcopy(e1_2.QUESTIONS)
        claims = list(CLAIMS)
        try:
            mutate(mod, claims)
            cg.check(mod, claims, table_checks=TABLE_CHECKS)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:90]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def move_key(mod, claims):
        mod.QUESTIONS[1]["ans"] = 3

    def break_anchor(mod, claims):
        claims[2] = ("no such phrase anywhere in the module", claims[2][1])

    def corrupt_table(mod, claims):
        # make the forest edge retreat while the climate warms
        mod.QUESTIONS[9]["table"] = dict(
            headers=e1_2._T_TREELINE["headers"],
            rows=[[d, w, lat] for (d, w, _), lat in
                  zip(e1_2._T_TREELINE["rows"], ["68.6", "67.7", "66.9", "66.4"])])

    def duplicate_choice(mod, claims):
        mod.QUESTIONS[3]["choices"][2] = mod.QUESTIONS[3]["choices"][0]

    def thin_why(mod, claims):
        mod.QUESTIONS[13]["why"] = "It just is."

    def letter_reference(mod, claims):
        mod.QUESTIONS[16]["why"] = ("Choice D is wrong because the framework says so and "
                                    "the rest of the reasoning follows from that.")

    def latex_slips_in(mod, claims):
        mod.QUESTIONS[0]["choices"][2] = "They occur in \\frac{1}{3} of the biome only"
        style(mod)

    def range_slips_in(mod, claims):
        mod.QUESTIONS[3]["q"] = "Between 1950-2000 the worldwide distribution of biomes was mapped."
        style(mod)

    print("negative controls:")
    must_fail("a backslash macro in a choice", latex_slips_in)
    must_fail("a digit-hyphen-digit range in a stem", range_slips_in)
    must_fail("key moved off its anchor", move_key)
    must_fail("anchor no longer in the keyed choice", break_anchor)
    must_fail("table value corrupted so the keyed conclusion is false", corrupt_table)
    must_fail("a distractor made identical to the key", duplicate_choice)
    must_fail("a why reduced below the minimum", thin_why)
    must_fail("a why naming an option by letter", letter_reference)
    print("all negative controls raised as required.")


import e1_2  # noqa: E402

if __name__ == "__main__" and "--selftest" in sys.argv:
    _selftest()

style(e1_2)
cg.check(e1_2, CLAIMS, table_checks=TABLE_CHECKS)
