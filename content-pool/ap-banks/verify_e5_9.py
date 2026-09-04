"""Key audit for AP ENVIRONMENTAL SCIENCE 5.9 Impacts of Mining.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHY THIS FILE EXISTS AT ALL. e5_9.py shipped with thirty questions and no
verifier -- an agent stopped mid-topic -- which means it carried no gate of any
kind. Every question below was re-read against the CED before this file was
written, and one clarity edit was made to the module (item 25's choices said
"the high grade figure" where they meant a NUMBER; e_check.no_figure_reference
deliberately over-matches the word "figure", and the house fix is always to
write "value" rather than to loosen the pattern).

WHAT THE KEYS REST ON -- the topic's four essential knowledge statements, in the
framework's own words:

  EIN-2.K.1  As the more accessible ores are mined to depletion, mining
             operations are forced to access lower grade ores. Accessing these
             ores requires increased use of resources that can cause increased
             waste and pollution.                    -- items 1, 2, 3, 4, 5, 22, 25
  EIN-2.K.2  Surface mining is the removal of large portions of soil and rock,
             called overburden, in order to access the ore underneath. An
             example is strip mining, which removes the vegetation from an area,
             making the area more susceptible to erosion.
                                                     -- items 6, 8, 9, 10, 23, 28
  EIN-2.L.1  Mining wastes include the soil and rocks that are moved to gain
             access to the ore and the waste, called slag and tailings that
             remain when the minerals have been removed from the ore. Mining
             helps to provide low cost energy and material necessary to make
             products. The mining of coal can destroy habitats, contaminate
             ground water, and release dust particles and methane.
                                  -- items 7, 11, 12, 13, 14, 15, 16, 17, 21, 24, 26
  EIN-2.L.2  As coal reserves get smaller, due to a lack of easily accessible
             reserves, it becomes necessary to access coal through subsurface
             mining, which is very expensive.        -- items 18, 19, 20, 27

Items 29 and 30 read across all four. Every code cited in a `why` outside this
topic was checked to exist and to say what the `why` says it says: EIN-2.F.1
waterlogging, EIN-2.F.6 salinization, EIN-2.I.5 desertification, STB-3.F.1
eutrophication, ENG-3.C.2 peat and ENG-3.C.3 lignite.

NO KEY NAMES a mine, a metal, a company or a country, because the framework
names none, and none gives a figure, so every quantitative item prints its data
in a table recomputed below from that table alone.

DATA ITEMS: 3, 4, 5, 9, 10, 11, 12, 15, 16, 17, 19, 20, 25 and 28.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_9

METAL = "Metal in the ore (kilograms per tonne of rock)"
ROCK = "Rock that must be moved for one tonne of metal (tonnes)"
ENERGY = "Energy used per tonne of metal (gigajoules)"
HIGH = "High grade ore, mined first"
MED = "Medium grade ore"
LOW = "Low grade ore, mined last"

COVER = "Vegetation cover (percent of the ground)"
SOIL = "Soil lost in one year (tonnes per hectare)"
BEFORE = "Undisturbed before mining"
STRIPPED = "Stripped of vegetation and overburden"
REPLANTED = "Replanted ten years after mining"

MASS = "Mass (thousand tonnes)"
OVERB = "Overburden moved to reach the ore"
TAIL = "Tailings left after the minerals were removed"
SLAG = "Slag left after smelting"
SOLD = "Metal sold"

DIST = "Distance from the coal mine (kilometers)"
SULF = "Sulfate in the well water (milligrams per litre)"

COST = "Cost per tonne of coal produced (currency units)"
DEPTH = "Depth of the coal worked (meters)"
SHALLOW = "Surface mining of a shallow seam"
DEEP = "Subsurface mining of a deep seam"

DUST = "Dust particles in the air (micrograms per cubic meter)"
METHANE = "Methane in the air above the workings (parts per million)"
WORKINGS = "At the workings"


def q3(table, item):
    m, r, e = cg.col(table, METAL), cg.col(table, ROCK), cg.col(table, ENERGY)
    assert cg.cell(table, HIGH, METAL) == max(m), "the first row must hold the richest ore"
    assert all(m[i] > m[i + 1] for i in range(len(m) - 1)), f"metal content must fall; got {m}"
    assert all(r[i] < r[i + 1] for i in range(len(r) - 1)), f"rock moved must rise; got {r}"
    assert all(e[i] < e[i + 1] for i in range(len(e) - 1)), f"energy used must rise; got {e}"
    return (f"metal content runs {m} kilograms per tonne while rock moved runs {r} tonnes and "
            f"energy runs {e} gigajoules, both rising as the grade falls")


def q4(table, item):
    base = cg.cell(table, HIGH, ROCK)
    assert base > 0, "the high grade rock figure must be non-zero for a ratio to exist"
    ratio = cg.cell(table, LOW, ROCK) / base
    assert ratio == 10, f"the ratio recomputes to {ratio}, not 10"
    for wrong in (4, 7, 2.5, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"500 divided by 50 is {ratio:.0f} times as much rock moved per tonne of metal"


def q5(table, item):
    d = cg.cell(table, LOW, ENERGY) - cg.cell(table, HIGH, ENERGY)
    assert d == 180, f"the difference recomputes to {d}, not 180"
    for wrong in (210, 120, 60, 240):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"210 minus 30 is {d:.0f} gigajoules more per tonne of metal"


def q9(table, item):
    c, s = cg.col(table, COVER), cg.col(table, SOIL)
    assert cg.cell(table, BEFORE, COVER) == max(c), "the undisturbed row must hold the most cover"
    assert cg.cell(table, STRIPPED, COVER) == min(c), "the stripped row must hold the least cover"
    assert cg.cell(table, STRIPPED, SOIL) == max(s), "the stripped row must lose the most soil"
    assert cg.cell(table, BEFORE, SOIL) == min(s), "the undisturbed row must lose the least soil"
    assert cg.cell(table, STRIPPED, SOIL) > 4 * cg.cell(table, BEFORE, SOIL), \
        "the stripped loss must be a multiple of the undisturbed loss, not merely larger"
    assert cg.cell(table, BEFORE, COVER) > cg.cell(table, REPLANTED, COVER) > \
        cg.cell(table, STRIPPED, COVER), "replanting must recover part but not all of the cover"
    assert cg.cell(table, STRIPPED, SOIL) > cg.cell(table, REPLANTED, SOIL) > \
        cg.cell(table, BEFORE, SOIL), "replanting must recover part but not all of the soil loss"
    return (f"cover runs {c} percent and soil lost runs {s} tonnes per hectare across the three "
            "conditions, stripping cutting the cover and multiplying the loss and replanting "
            "returning part of each")


def q10(table, item):
    base = cg.cell(table, BEFORE, SOIL)
    assert base > 0, "the undisturbed loss must be non-zero for a ratio to exist"
    ratio = cg.cell(table, STRIPPED, SOIL) / base
    assert ratio == 29, f"the ratio recomputes to {ratio}, not 29"
    for wrong in (4, 6, 23, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"58 divided by 2 is {ratio:.0f} times as much soil lost in the year after stripping"


def q11(table, item):
    v = cg.col(table, MASS)
    assert cg.cell(table, OVERB, MASS) == max(v), "the overburden row must hold the largest mass"
    assert cg.cell(table, SOLD, MASS) == min(v), "the metal sold must be the smallest mass"
    assert cg.cell(table, OVERB, MASS) > 100 * cg.cell(table, SOLD, MASS), \
        "the overburden must be FAR larger than the metal sold, not merely larger"
    assert len(set(v)) == len(v), "'about equal masses' must be false"
    assert cg.cell(table, TAIL, MASS) > 0 and cg.cell(table, SLAG, MASS) > 0, \
        "'no waste leaves the operation' must be false"
    return (f"the four masses are {v} thousand tonnes, the overburden much the largest and the "
            "metal sold much the smallest")


def q12(table, item):
    total = (cg.cell(table, OVERB, MASS) + cg.cell(table, TAIL, MASS)
             + cg.cell(table, SLAG, MASS))
    assert total == 996, f"the waste total recomputes to {total}, not 996"
    assert total + cg.cell(table, SOLD, MASS) == 1000, \
        "the 1,000 distractor must be the total INCLUDING the metal sold"
    for wrong in (1000, 970, 216, 780):
        assert total != wrong, f"the {wrong} distractor equals the key"
    return f"780 plus 190 plus 26 is {total:.0f} thousand tonnes of waste in the year"


def q15(table, item):
    d, s = cg.col(table, DIST), cg.col(table, SULF)
    assert cg.cell(table, "Well 1", DIST) == min(d), "Well 1 must be the nearest to the mine"
    assert all(d[i] < d[i + 1] for i in range(len(d) - 1)), f"distance must rise; got {d}"
    assert all(s[i] > s[i + 1] for i in range(len(s) - 1)), f"sulfate must fall; got {s}"
    assert cg.cell(table, "Well 1", SULF) == max(s), \
        "'the nearest well has the lowest concentration' must be false"
    return (f"distances run {d} kilometers against sulfate of {s} milligrams per litre, the "
            "concentration falling steadily away from the mine")


def q16(table, item):
    d = cg.cell(table, "Well 1", SULF) - cg.cell(table, "Well 4", SULF)
    assert d == 575, f"the difference recomputes to {d}, not 575"
    for wrong in (610, 490, 305, 645):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"610 minus 35 is {d:.0f} milligrams per litre higher at the nearest well"


def q17(table, item):
    du, me = cg.col(table, DUST), cg.col(table, METHANE)
    assert cg.cell(table, WORKINGS, DUST) == max(du), "the workings must carry the most dust"
    assert cg.cell(table, WORKINGS, METHANE) == max(me), "the workings must carry the most methane"
    assert all(du[i] > du[i + 1] for i in range(len(du) - 1)), f"dust must fall; got {du}"
    assert all(me[i] > me[i + 1] for i in range(len(me) - 1)), f"methane must fall; got {me}"
    return (f"dust runs {du} micrograms per cubic meter and methane runs {me} parts per million "
            "with distance, both falling together")


def q19(table, item):
    assert cg.cell(table, DEEP, COST) > cg.cell(table, SHALLOW, COST), \
        "the deep seam must cost more per tonne than the shallow one"
    assert cg.cell(table, DEEP, COST) > 3 * cg.cell(table, SHALLOW, COST), \
        "the deep seam must cost FAR more, not merely more"
    assert cg.cell(table, DEEP, DEPTH) > cg.cell(table, SHALLOW, DEPTH), \
        "'the shallow seam lies deeper' must be false"
    return (f"the deep seam costs {cg.cell(table, DEEP, COST):.0f} currency units per tonne "
            f"against {cg.cell(table, SHALLOW, COST):.0f}, at "
            f"{cg.cell(table, DEEP, DEPTH):.0f} meters against "
            f"{cg.cell(table, SHALLOW, DEPTH):.0f}")


def q20(table, item):
    base = cg.cell(table, SHALLOW, COST)
    assert base > 0, "the shallow cost must be non-zero for a ratio to exist"
    ratio = cg.cell(table, DEEP, COST) / base
    assert round(ratio) == 4, f"the ratio recomputes to {ratio}, which does not round to four"
    for wrong in (2, 13, 7, 1):
        assert round(ratio) != wrong, f"the {wrong} distractor equals the key"
    return f"74 divided by 18 is {ratio:.2f}, which rounds to about four times as much"


def q25(table, item):
    med, high = cg.cell(table, MED, METAL), cg.cell(table, HIGH, METAL)
    assert med == 5, f"the medium grade metal content recomputes to {med}, not 5"
    assert high > 0, "the high grade content must be non-zero for a ratio to exist"
    assert abs(med / high - 0.25) < 1e-9, \
        f"the medium grade is {med / high} of the high grade, not one quarter"
    assert med != cg.cell(table, LOW, METAL), "the medium and low grades must differ"
    return f"5 against 20 kilograms per tonne is {med / high:.2f}, one quarter of the high grade"


CLAIMS = [
 ("forced to access lower grade ores",
  "EIN-2.K.1, near verbatim: as the more accessible ores are mined to depletion, mining operations are FORCED TO ACCESS LOWER GRADE ORES. The same statement has resource use rising rather than falling, so the energy and waste options point the wrong way."),
 ("which can cause increased waste and pollution",
  "EIN-2.K.1 states that accessing lower grade ores requires INCREASED use of resources THAT CAN CAUSE INCREASED WASTE AND POLLUTION. One rejected option keeps the increased resource use but severs it from the waste, so the anchor spans both clauses."),
 ("more rock must be moved and more energy used",
  "Recomputed in q3 above: metal content 20, 5 and 2 kilograms per tonne against rock moved 50, 200 and 500 tonnes and energy 30, 90 and 210 gigajoules. EIN-2.K.1 states that accessing lower grade ores requires increased use of resources."),
 ("Ten times as much",
  "Recomputed in q4 above: 500 divided by 50 tonnes of rock per tonne of metal. The rejected values come from the medium grade row, from the energy column, or from denying that the grades differ."),
 ("180 gigajoules more",
  "Recomputed in q5 above: 210 minus 30 gigajoules per tonne of metal. The rejected values quote the low grade energy alone, pair the wrong grades, or add the two."),
 ("Overburden",
  "EIN-2.K.2 states that surface mining is the removal of large portions of soil and rock, CALLED OVERBURDEN, in order to access the ore underneath. EIN-2.L.1 reserves slag and tailings for what remains after the minerals have been removed from the ore."),
 ("Slag and tailings",
  "EIN-2.L.1 names the waste that remains when the minerals have been removed from the ore as SLAG AND TAILINGS. Overburden is what is moved to reach the ore under EIN-2.K.2, and peat and lignite are fuels under ENG-3.C.2 and ENG-3.C.3."),
 ("surface mining that removes the vegetation from an area",
  "EIN-2.K.2 gives strip mining as an example of SURFACE mining and states that it removes the vegetation from an area, making the area more susceptible to erosion. The rejected options move it to subsurface mining, to restoration, to processing, or reverse what it does to the vegetation."),
 ("cut the cover sharply and multiplied the soil lost",
  "Recomputed in q9 above: cover 92, 4 and 61 percent against soil lost 2, 58 and 9 tonnes per hectare. EIN-2.K.2 states that strip mining removes the vegetation from an area, making the area more susceptible to erosion."),
 ("Twenty-nine times as much",
  "Recomputed in q10 above: 58 divided by 2 tonnes per hectare. The rejected values come from the replanted row, from a difference rather than a ratio, or from denying that the two differ."),
 ("overburden moved to reach the ore is the largest single mass",
  "Recomputed in q11 above: 780, 190, 26 and 4 thousand tonnes. EIN-2.L.1 states that mining wastes include the soil and rocks that are moved to gain access to the ore as well as the slag and tailings left afterwards."),
 ("996 thousand tonnes",
  "Recomputed in q12 above: 780 plus 190 plus 26 thousand tonnes. The rejected values add the metal sold, drop the slag, count only the two smaller wastes, or quote the overburden alone."),
 ("low cost energy and material necessary to make products",
  "EIN-2.L.1 states, in the same statement as the list of wastes, that MINING HELPS TO PROVIDE LOW COST ENERGY AND MATERIAL NECESSARY TO MAKE PRODUCTS. The framework does record a benefit, so the option denying one is wrong on its face."),
 ("contaminated ground water, and the release of dust particles and methane",
  "EIN-2.L.1 states that the mining of coal can destroy habitats, contaminate ground water, and release dust particles and methane. Salinization is EIN-2.F.6, waterlogging EIN-2.F.1, eutrophication STB-3.F.1 and desertification EIN-2.I.5, all in other topics."),
 ("concentration falls with distance from the mine",
  "Recomputed in q15 above: 1, 3, 8 and 20 kilometers against 610, 340, 120 and 35 milligrams per litre. EIN-2.L.1 states that the mining of coal can contaminate ground water, and a gradient falling away from the source is what that looks like in well data."),
 ("575 milligrams per litre higher",
  "Recomputed in q16 above: 610 minus 35 milligrams per litre. The rejected values quote the nearest well alone, pair the wrong wells, or add the two readings."),
 ("most concentrated at the workings and fall away with distance",
  "Recomputed in q17 above: dust 180, 90 and 22 micrograms per cubic meter and methane 24, 8 and 2 parts per million. EIN-2.L.1 states that the mining of coal can release dust particles and methane. The anchor spans both the position and the direction, because one distractor reverses only the direction."),
 ("subsurface mining, which is very expensive",
  "EIN-2.L.2, near verbatim: as coal reserves get smaller, due to a lack of easily accessible reserves, it becomes necessary to access coal through SUBSURFACE mining, WHICH IS VERY EXPENSIVE. One distractor swaps subsurface for surface and expensive for cheap, so the anchor carries both."),
 ("costs far more per tonne than working the shallow one",
  "Recomputed in q19 above: 74 currency units per tonne at 400 meters against 18 at 30 meters. EIN-2.L.2 states that reaching coal through subsurface mining is very expensive."),
 ("About four times as much",
  "Recomputed in q20 above: 74 divided by 18 is about 4.1. The rejected values come from the depth column, from halving rather than dividing, or from denying that the two differ."),
 ("The same statement that lists mining wastes also says",
  "EIN-2.L.1 opens with the wastes and then states that mining helps to provide low cost energy and material necessary to make products, so the benefit and the harm sit in one statement. The framework does list wastes and does name both the energy and the material."),
 ("tonne of rock, and the waste rock produced",
  "EIN-2.K.1 links falling ore grade to increased use of resources and increased waste, so a test of it needs a measure of grade AND a measure of waste per unit of product. Each rejected pair supplies at most one of the two, which is why the anchor spans the pairing rather than either half."),
 ("Restoring vegetation cover on the stripped ground",
  "EIN-2.K.2 names the removal of vegetation as what makes a strip mined area more susceptible to erosion, so returning the vegetation addresses the stated mechanism. Each rejected action strips more ground, moves more rock, or makes more waste."),
 ("Overburden is moved to reach the ore; tailings are what remains",
  "EIN-2.K.2 defines overburden as the soil and rock removed in order to access the ore underneath and EIN-2.L.1 defines slag and tailings as what remains when the minerals have been removed from the ore. One distractor is the exact swap, so the anchor carries both halves of the distinction."),
 ("5 kilograms per tonne, which is one quarter",
  "Recomputed in q25 above: 5 against 20 kilograms of metal per tonne of rock. The rejected options invert the comparison, quote another row, or read the rock-moved column as a metal content."),
 ("much higher concentrations of a mine-related substance",
  "EIN-2.L.1 states that the mining of coal can contaminate ground water, and a concentration that is high beside the mine and low away from it is what a local source looks like. Employment, seasonal output and price say nothing about the water."),
 ("very expensive to produce, because subsurface mining",
  "EIN-2.L.2 states that as easily accessible reserves run short it becomes necessary to access coal through subsurface mining, WHICH IS VERY EXPENSIVE. The framework has the deep coal reached at high cost, not left unreachable."),
 ("most but not all of its original level",
  "Recomputed in q28 above: cover 61 percent against 92 before mining and 4 when stripped, soil lost 9 tonnes per hectare against 2 before mining and 58 when stripped. Both sit partway back, which is what EIN-2.K.2's susceptibility to erosion leads a student to check."),
 ("first describes how ore is reached and what that requires; the second describes what the operation leaves behind",
  "EIN-2.K covers extraction, with falling ore grade in EIN-2.K.1 and overburden and stripped vegetation in EIN-2.K.2, while EIN-2.L covers ecological AND economic impacts, with slag and tailings, the low cost energy and material, and the coal mining harms. One distractor is the exact swap, so the anchor carries both halves."),
 ("Falling ore grades force more rock and energy per tonne of metal",
  "The keyed summary carries EIN-2.K.1's falling grades and rising resource use, EIN-2.K.2's overburden and stripped vegetation, EIN-2.L.1's wastes and its low cost energy and material, and EIN-2.L.2's expensive subsurface mining. Each rejected summary reverses a direction or drops a whole statement."),
]


def q28(table, item):
    c_before = cg.cell(table, BEFORE, COVER)
    c_after = cg.cell(table, REPLANTED, COVER)
    c_strip = cg.cell(table, STRIPPED, COVER)
    s_before = cg.cell(table, BEFORE, SOIL)
    s_after = cg.cell(table, REPLANTED, SOIL)
    s_strip = cg.cell(table, STRIPPED, SOIL)
    assert c_strip < c_after < c_before, \
        f"replanted cover {c_after} must sit between {c_strip} and {c_before}"
    assert s_before < s_after < s_strip, \
        f"replanted soil loss {s_after} must sit between {s_before} and {s_strip}"
    assert c_after != c_before and s_after != s_before, "'returned exactly' must be false"
    assert c_after > 0.5 * c_before, "'most of its original level' requires more than half back"
    return (f"the replanted row reads {c_after:.0f} percent cover against {c_before:.0f} before "
            f"and {c_strip:.0f} when stripped, and {s_after:.0f} tonnes per hectare lost against "
            f"{s_before:.0f} before and {s_strip:.0f} when stripped")


TABLE_CHECKS = {3: q3, 4: q4, 5: q5, 9: q9, 10: q10, 11: q11, 12: q12, 15: q15,
                16: q16, 17: q17, 19: q19, 20: q20, 25: q25, 28: q28}

e_check.run(e5_9, CLAIMS, TABLE_CHECKS)
