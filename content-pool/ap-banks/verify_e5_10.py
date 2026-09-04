"""Key audit for AP ENVIRONMENTAL SCIENCE 5.10 Impacts of Urbanization.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  EIN-2.M.1  Urbanization can lead to depletion of resources and saltwater
             intrusion in the hydrologic cycle.     -- items 1, 2, 14, 15, 22
  EIN-2.M.2  Urbanization, through the burning of fossil fuels and landfills,
             affects the carbon cycle by increasing the amount of carbon dioxide
             in the atmosphere.                     -- items 3, 4, 16, 17
  EIN-2.M.3  Impervious surfaces are human-made structures -- such as roads,
             buildings, sidewalks, and parking lots -- that do not allow water to
             reach the soil, leading to flooding.
                                     -- items 5, 6, 7, 10, 11, 12, 13, 23, 24, 25, 26, 27
  EIN-2.M.4  Urban sprawl is the change in population distribution from high
             population density areas to low density suburbs that spread into
             rural lands, leading to potential environmental problems.
                                                    -- items 8, 9, 18, 19, 28

Items 20, 21, 29 and 30 read across the four statements.

TWO ANCHORS CARRY BOTH CLAUSES ON PURPOSE. EIN-2.M.4's movement runs FROM high
density areas TO low density suburbs, and the reversal is the distractor a
prepared student reaches for; items 8, 18 and 20 therefore anchor on both ends
of the movement rather than on either half, because either half alone also
matches the swapped option.

DATA ITEMS: 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 25 and 26 carry tables,
recomputed below from those tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_10

IMPERV = "Impervious cover (percent of the catchment)"
RUNOFF_PC = "Rainfall that runs off the surface (percent)"
PEAK = ("Peak stream flow after a storm of the same size "
        "(cubic meters per second)")
BEFORE = "Before development"
AFTER = "After development"

PUMPED = "Water pumped from the coastal aquifer (million cubic meters)"
CHLORIDE = "Chloride in the town's well water (milligrams per litre)"

CO2 = "Carbon dioxide released in one year (thousand tonnes)"
FOSSIL = "Burning of fossil fuels for transport, heating and power"
LANDFILL = "Landfills serving the city"
OTHER = "All other sources combined"

POP1 = "Population in the first year (thousands)"
POP2 = "Population thirty years later (thousands)"
DENSITY = "People per square kilometer thirty years later"
CENTRE = "Central city"
SUBURB = "Outer suburbs on former farmland"

SOAK = "Rain soaking into the soil in one hour (millimeters)"
RUN = "Rain running off the surface in one hour (millimeters)"
GRASS = "Grass over deep soil"
ASPHALT = "Asphalt paving"


def q10(table, item):
    imp, run = cg.col(table, IMPERV), cg.col(table, RUNOFF_PC)
    assert cg.cell(table, "Catchment 1", IMPERV) == min(imp), \
        "Catchment 1 must carry the least impervious cover"
    assert all(imp[i] < imp[i + 1] for i in range(len(imp) - 1)), \
        f"impervious cover must rise down the table; got {imp}"
    assert all(run[i] < run[i + 1] for i in range(len(run) - 1)), \
        f"runoff must rise with it; got {run}"
    assert len(set(run)) > 1, "'the same in all four catchments' must be false"
    assert cg.cell(table, "Catchment 1", RUNOFF_PC) == min(run), \
        "'the least paved catchment sheds the most runoff' must be false"
    return (f"impervious cover runs {imp} percent against runoff of {run} percent, the two "
            "rising together without exception")


def q11(table, item):
    run = cg.col(table, RUNOFF_PC)
    imp = cg.col(table, IMPERV)
    d = max(run) - min(run)
    assert d == 55, f"the difference recomputes to {d}, not 55"
    for wrong in (max(run), max(run) + min(run), max(imp) - min(imp), min(run)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"65 minus 10 is {d:.0f} percentage points more of the rainfall running off"


def q12(table, item):
    assert cg.cell(table, AFTER, PEAK) > cg.cell(table, BEFORE, PEAK), \
        "the peak flow must rise after development"
    assert cg.cell(table, AFTER, PEAK) > 2 * cg.cell(table, BEFORE, PEAK), \
        "the rise must be several times over, not merely a rise"
    assert cg.cell(table, AFTER, IMPERV) > cg.cell(table, BEFORE, IMPERV), \
        "'impervious cover fell as the development proceeded' must be false"
    return (f"impervious cover goes from {cg.cell(table, BEFORE, IMPERV):.0f} to "
            f"{cg.cell(table, AFTER, IMPERV):.0f} percent and the peak flow from "
            f"{cg.cell(table, BEFORE, PEAK):.0f} to {cg.cell(table, AFTER, PEAK):.0f} cubic "
            "meters per second for a storm of the same size")


def q13(table, item):
    base = cg.cell(table, BEFORE, PEAK)
    assert base > 0, "the pre-development peak must be non-zero for a ratio to exist"
    ratio = cg.cell(table, AFTER, PEAK) / base
    assert ratio == 4, f"the ratio recomputes to {ratio}, not 4"
    for wrong in (2, 3, 9, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return f"48 divided by 12 is {ratio:.0f} times the peak flow after the same storm"


def q14(table, item):
    p, c = cg.col(table, PUMPED), cg.col(table, CHLORIDE)
    assert cg.cell(table, "Year 1", PUMPED) == min(p), "Year 1 must carry the least pumping"
    assert all(p[i] < p[i + 1] for i in range(len(p) - 1)), f"pumping must rise; got {p}"
    assert all(c[i] < c[i + 1] for i in range(len(c) - 1)), f"chloride must rise; got {c}"
    assert len(set(c)) > 1, "'the chloride did not change' must be false"
    return (f"pumping runs {p} million cubic meters against chloride of {c} milligrams per "
            "litre, the two rising together")


def q15(table, item):
    c = cg.col(table, CHLORIDE)
    d = cg.cell(table, "Year 30", CHLORIDE) - cg.cell(table, "Year 1", CHLORIDE)
    assert d == 860, f"the rise recomputes to {d}, not 860"
    for wrong in (max(c), max(c) + min(c), 460, 540):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"900 minus 40 is {d:.0f} milligrams per litre more chloride in the well water"


def q16(table, item):
    named = cg.cell(table, FOSSIL, CO2) + cg.cell(table, LANDFILL, CO2)
    other = cg.cell(table, OTHER, CO2)
    assert named > 10 * other, \
        f"the two named routes ({named}) must supply nearly all against {other}"
    assert cg.cell(table, FOSSIL, CO2) > cg.cell(table, LANDFILL, CO2), \
        "'the landfills alone account for nearly all' must be false"
    assert cg.cell(table, FOSSIL, CO2) > 0, "'fossil fuels account for none' must be false"
    vals = cg.col(table, CO2)
    assert max(vals) > 2 * min(vals), "'about equal amounts' must be false"
    return (f"the three sources release {vals} thousand tonnes, so the two routes the framework "
            f"names supply {named:.0f} against {other:.0f} from everything else")


def q17(table, item):
    named = cg.cell(table, FOSSIL, CO2) + cg.cell(table, LANDFILL, CO2)
    total = sum(cg.col(table, CO2))
    assert total > 0, "the total must be non-zero for a share to exist"
    share = 100 * named / total
    assert abs(share - 98) < 1e-9, f"the share recomputes to {share}, not 98 percent"
    for wrong in (82, 16, 84, 50):
        assert abs(share - wrong) > 1e-9, f"the {wrong} percent distractor equals the key"
    return f"820 plus 160 over a total of {total:.0f} is {share:.0f} percent"


def q18(table, item):
    assert cg.cell(table, CENTRE, POP2) < cg.cell(table, CENTRE, POP1), \
        "the central city must lose population"
    assert cg.cell(table, SUBURB, POP2) > cg.cell(table, SUBURB, POP1), \
        "the outer suburbs must gain population"
    assert cg.cell(table, CENTRE, DENSITY) > cg.cell(table, SUBURB, DENSITY), \
        "the centre must remain the denser of the two, or the movement is not outward"
    return (f"the centre falls from {cg.cell(table, CENTRE, POP1):.0f} to "
            f"{cg.cell(table, CENTRE, POP2):.0f} thousand while the suburbs rise from "
            f"{cg.cell(table, SUBURB, POP1):.0f} to {cg.cell(table, SUBURB, POP2):.0f}, at "
            f"{cg.cell(table, SUBURB, DENSITY):.0f} people per square kilometer against "
            f"{cg.cell(table, CENTRE, DENSITY):.0f}")


def q19(table, item):
    gain = cg.cell(table, SUBURB, POP2) - cg.cell(table, SUBURB, POP1)
    loss = cg.cell(table, CENTRE, POP1) - cg.cell(table, CENTRE, POP2)
    net = (cg.cell(table, CENTRE, POP2) + cg.cell(table, SUBURB, POP2)
           - cg.cell(table, CENTRE, POP1) - cg.cell(table, SUBURB, POP1))
    assert gain == 390, f"the suburban gain recomputes to {gain}, not 390"
    for wrong in (loss, cg.cell(table, SUBURB, POP2), net, 120):
        assert gain != wrong, f"the {wrong} distractor equals the key"
    return (f"540 minus 150 is {gain:.0f} thousand more people in the suburbs, against a loss "
            f"of {loss:.0f} thousand from the centre")


def q25(table, item):
    a_in, a_out = cg.cell(table, ASPHALT, SOAK), cg.cell(table, ASPHALT, RUN)
    g_in, g_out = cg.cell(table, GRASS, SOAK), cg.cell(table, GRASS, RUN)
    assert a_out > 10 * a_in, f"asphalt must shed almost all the rain; got {a_in} in, {a_out} off"
    assert g_in > 5 * g_out, f"grass must absorb almost all the rain; got {g_in} in, {g_out} off"
    assert a_in == min(cg.col(table, SOAK)), "asphalt must let the least rain reach the soil"
    assert len(set(cg.col(table, SOAK))) > 1, "'the same depth on all three' must be false"
    assert g_out < a_out, "'the grass plot sheds more runoff than the asphalt' must be false"
    return (f"asphalt takes {a_in:.0f} millimeter in and sheds {a_out:.0f}, against "
            f"{g_in:.0f} in and {g_out:.0f} off the grass")


def q26(table, item):
    d = cg.cell(table, ASPHALT, RUN) - cg.cell(table, GRASS, RUN)
    assert d == 21, f"the difference recomputes to {d}, not 21"
    for wrong in (cg.cell(table, ASPHALT, RUN),
                  cg.cell(table, ASPHALT, RUN) + cg.cell(table, GRASS, RUN),
                  cg.cell(table, "Gravel", RUN),
                  cg.cell(table, GRASS, RUN)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"24 minus 3 is {d:.0f} millimeters more runoff from the asphalt in the hour"


CLAIMS = [
 ("Depletion of resources and saltwater intrusion",
  "EIN-2.M.1, near verbatim: urbanization can lead to DEPLETION OF RESOURCES AND SALTWATER INTRUSION in the hydrologic cycle. Each rejected option reverses one of the two effects, drops one, or denies both, so the anchor carries both."),
 ("The hydrologic cycle",
  "EIN-2.M.1 places both the depletion of resources and the saltwater intrusion in the HYDROLOGIC cycle by name. The framework's separate carbon claim is EIN-2.M.2 and concerns the atmosphere, not water."),
 ("burning of fossil fuels and landfills",
  "EIN-2.M.2 states that urbanization acts on the carbon cycle THROUGH THE BURNING OF FOSSIL FUELS AND LANDFILLS. The rejected options substitute the impervious surfaces of EIN-2.M.3 or the sprawl of EIN-2.M.4 for one or both of the two named routes."),
 ("increase in the amount of carbon dioxide",
  "EIN-2.M.2 states that urbanization affects the carbon cycle BY INCREASING THE AMOUNT OF CARBON DIOXIDE IN THE ATMOSPHERE. The framework names carbon dioxide rather than methane or nitrous oxide, and gives the direction as an increase."),
 ("structures that do not allow water to reach the soil",
  "EIN-2.M.3 defines impervious surfaces as HUMAN-MADE structures that DO NOT ALLOW WATER TO REACH THE SOIL. One distractor keeps the human-made half and reverses what the structure does to water, so the anchor is the clause that separates them."),
 ("sidewalks, and parking lots",
  "EIN-2.M.3 gives roads, buildings, sidewalks and parking lots as its examples. Each rejected list contains at least one natural surface, which cannot meet the framework's requirement that the structure be human-made."),
 ("Flooding, because the water cannot reach the soil",
  "EIN-2.M.3 ends by stating that impervious surfaces do not allow water to reach the soil, LEADING TO FLOODING. Saltwater intrusion belongs to EIN-2.M.1 and waterlogging to EIN-2.F.1 in the irrigation topic."),
 ("from high population density areas to low density suburbs",
  "EIN-2.M.4 defines urban sprawl as the change in population distribution FROM high population density areas TO low density suburbs that spread into rural lands. One distractor runs that movement backwards, so the anchor carries both ends of it."),
 ("Urban sprawl",
  "EIN-2.M.4 defines urban sprawl as exactly this change in population distribution, from high density areas to low density suburbs spreading into rural lands. Saltwater intrusion is EIN-2.M.1, sustainable yield STB-1.A.2, rotational grazing STB-1.E.3 and clearcutting EIN-2.C."),
 ("impervious surfaces rises, the share of rainfall that runs off the surface rises",
  "Recomputed in q10 above: impervious cover 5, 20, 45 and 80 percent against runoff 10, 22, 40 and 65 percent. EIN-2.M.3 states that impervious surfaces do not allow water to reach the soil. One distractor differs only in the final direction word, so the anchor carries it."),
 ("55 percentage points greater",
  "Recomputed in q11 above: 65 minus 10 percent of the rainfall. The rejected values quote the heaviest catchment alone, add the two, take the difference in impervious cover, or quote the lightest alone."),
 ("raised the peak flow after an identical storm several times over",
  "Recomputed in q12 above: impervious cover 6 to 54 percent and peak flow 12 to 48 cubic meters per second for a storm of the same size, so storm size cannot explain the rise. EIN-2.M.3 attaches flooding to surfaces that keep water from the soil."),
 ("Four times as large",
  "Recomputed in q13 above: 48 divided by 12 cubic meters per second. The rejected values come from halving rather than dividing, from the impervious cover column, or from denying that the two differ."),
 ("chloride in the well water rose, which is the pattern saltwater intrusion",
  "Recomputed in q14 above: pumping 10, 25, 40 and 55 million cubic meters against chloride 40, 180, 460 and 900 milligrams per litre. EIN-2.M.1 names saltwater intrusion as an effect of urbanization in the hydrologic cycle, and chloride is the salt in seawater. One distractor reverses only the direction, so the anchor carries it."),
 ("860 milligrams per litre higher",
  "Recomputed in q15 above: 900 minus 40 milligrams per litre. The rejected values quote the final reading alone, add the two, or take a reading from the middle of the record."),
 ("landfills together account for nearly all of the release",
  "Recomputed in q16 above: 820 and 160 against 20 thousand tonnes from everything else. EIN-2.M.2 names the burning of fossil fuels AND landfills as the two routes by which urbanization raises atmospheric carbon dioxide."),
 ("98 percent",
  "Recomputed in q17 above: 980 of 1,000 thousand tonnes. The rejected values quote the fossil fuel share alone, the landfill share alone, the fossil fuel share paired with the unnamed sources instead of the landfills, or an even split."),
 ("population moved from the dense centre out to low density suburbs",
  "Recomputed in q18 above: the centre falls from 600 to 420 thousand while the suburbs rise from 150 to 540, at 700 people per square kilometer against 5,200. EIN-2.M.4 defines that movement as urban sprawl. One distractor names the same term with the movement reversed, so the anchor carries both ends."),
 ("390 thousand people",
  "Recomputed in q19 above: 540 minus 150 thousand in the suburbs. The rejected values give the loss from the centre, the final suburban total alone, the net change across both parts, or neither."),
 ("built structures that keep water from the soil; urban sprawl is a movement of population",
  "EIN-2.M.3 defines impervious surfaces as human-made structures that do not allow water to reach the soil, while EIN-2.M.4 defines urban sprawl as a change in population distribution. One distractor is the exact swap of the two, so the anchor carries both halves of the distinction."),
 ("also places depletion of resources and saltwater intrusion in the hydrologic cycle",
  "EIN-2.M.1 gives urbanization two effects in the hydrologic cycle and EIN-2.M.2 gives it one in the carbon cycle, so the framework names both. Each rejected option denies a statement the framework makes or reverses its direction."),
 ("growing steadily saltier as withdrawals from the aquifer increase",
  "EIN-2.M.1 names saltwater intrusion as its second effect, so the evidence is salt appearing in fresh groundwater as it is drawn down. Rainfall says nothing about salt, and parking lots and landfills test EIN-2.M.3 and EIN-2.M.2 instead."),
 ("pavement and buildings, and the peak stream flow after a storm",
  "EIN-2.M.3 claims that impervious surfaces keep water from the soil and thereby lead to flooding, so a test of it needs a measure of the surface AND a measure of the flood response. Each rejected pair supplies at most one of the two, which is why the anchor spans the pairing."),
 ("do not allow water to reach the soil, leading to flooding",
  "Paving ground that now absorbs rainfall creates the human-made surface EIN-2.M.3 describes, and that statement's own consequence is flooding. The rejected options are all framework statements, but none of them is about a surface."),
 ("Almost none of the rain reaches the soil under the asphalt",
  "Recomputed in q25 above: 1 millimeter soaks in and 24 run off under asphalt, against 22 and 3 under grass. EIN-2.M.3 defines an impervious surface as one that does not allow water to reach the soil. One distractor reverses both halves, so the anchor carries the direction."),
 ("21 millimeters more",
  "Recomputed in q26 above: 24 minus 3 millimeters of runoff in the hour. The rejected values quote the asphalt alone, add the two, take the gravel reading, or quote the grass alone."),
 ("meadow of deep soil under grass",
  "EIN-2.M.3 requires a HUMAN-MADE structure that does not allow water to reach the soil and names roads, buildings, sidewalks and parking lots. A meadow is neither human-made nor a barrier to infiltration, while each rejected option is on the framework's list or is a building."),
 ("without asserting that any particular problem must follow",
  "EIN-2.M.4 says sprawl leads to POTENTIAL environmental problems, so the framework asserts a risk rather than a list of certain outcomes. Reading it as a guarantee and reading it as a denial both go past what the statement says."),
 ("One names two effects in the water cycle, one an effect on the carbon cycle",
  "EIN-2.M.1 is the hydrologic pair, EIN-2.M.2 the carbon dioxide increase, EIN-2.M.3 impervious surfaces and their flooding, and EIN-2.M.4 the population shift. They are four different kinds of effect and one place can show all four together."),
 ("depletes resources and brings saltwater intrusion in the water cycle",
  "The keyed summary carries EIN-2.M.1's two hydrologic effects, EIN-2.M.2's route and direction, EIN-2.M.3's definition and consequence, and EIN-2.M.4's movement of population. Each rejected summary reverses a direction or drops a whole statement."),
]

TABLE_CHECKS = {10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
                17: q17, 18: q18, 19: q19, 25: q25, 26: q26}

e_check.run(e5_10, CLAIMS, TABLE_CHECKS)
