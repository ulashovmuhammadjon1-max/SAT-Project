"""Key audit for AP ENVIRONMENTAL SCIENCE 6.3 Fuel Types and Uses.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.C.1  Wood is commonly used as fuel in the forms of firewood and
             charcoal. It is often used in developing countries because it is
             easily accessible.            -- items 1, 2, 15, 29
  ENG-3.C.2  Peat is partially decomposed organic material that can be burned
             for fuel.                     -- items 3, 13
  ENG-3.C.3  Three types of coal used for fuel are lignite, bituminous, and
             anthracite. Heat, pressure, and depth of burial contribute to the
             development of various coal types and their qualities.
                                           -- items 4, 5, 13, 14, 19, 20, 21
  ENG-3.C.4  Natural gas, the cleanest of the fossil fuels, is mostly methane.
                                           -- items 6, 7, 18, 22, 23, 24
  ENG-3.C.5  Crude oil can be recovered from tar sands, which are a combination
             of clay, sand, water, and bitumen.   -- items 8, 9, 28
  ENG-3.C.6  Fossil fuels can be made into specific fuel types for specialized
             uses.                         -- items 10, 16
  ENG-3.C.7  Cogeneration occurs when a fuel source is used to generate both
             useful heat and electricity.  -- items 11, 12, 17, 25, 26, 27
  item 30 reads across all seven.

THE RANKING THAT IS NOT IN THE FRAMEWORK. ENG-3.C.3 names three coals and names
three things that contribute to their development and qualities. It does NOT
order lignite, bituminous and anthracite by carbon content, energy released or
age. No key here asserts such an order from memory: item 14 keys the absence,
and where the arithmetic needs numbers, item 19's table supplies them and
ENG-3.C.3 supplies only the licence to relate depth of burial to quality.

DATA ITEMS: 19 to 29, recomputed below from those tables alone.

THE COAL TABLE SURVIVES A COLUMN REVERSAL with its (depth, energy) pairs
intact, so the three checks that read it also pin the shallowest and deepest
seams BY ROW LABEL. Without that, reversing the table would leave the
association and both differences unchanged and the checks would say nothing.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_3.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback.
"""
import e_check
import cg_check as cg
import e6_3

DEPTH = "Depth at which the seam was buried (meters)"
KGENERGY = "Energy released by one kilogram (energy units)"
S1, S2, S3 = "Sample 1", "Sample 2", "Sample 3"

SO2 = "Sulfur dioxide released for each unit of energy (grams)"
PART = "Particulates released for each unit of energy (grams)"
COAL, OILP, GAS = "Coal", "Crude oil products", "Natural gas"

FUELIN = "Fuel energy put in (energy units)"
ELEC = "Electricity produced (energy units)"
HEAT = "Useful heat delivered to buildings (energy units)"
P1, P2 = "Plant 1", "Plant 2"

MASSSHARE = "Share of the deposit by mass (percent)"
CLAY, SAND, WATER, BITUMEN = "Clay", "Sand", "Water", "Bitumen"

WOODSHARE = "Households whose main fuel is firewood or charcoal (percent)"
GRIDSHARE = "Households connected to an electricity supply (percent)"
DEVED, DEVING = "Developed countries", "Developing countries"


def _pin_coal(table):
    """The record must be read shallowest first, by ROW LABEL.

    Reversing both numeric columns of this table leaves the (depth, energy)
    pairs exactly as they were, so an association-only check cannot fire and
    neither can a difference taken between the extreme values. Naming the rows
    is what a reversal breaks.
    """
    depths = cg.col(table, DEPTH)
    assert cg.cell(table, S1, DEPTH) == min(depths), "the first sample must be the shallowest"
    assert cg.cell(table, S3, DEPTH) == max(depths), "the third sample must be the deepest"


def q19(table, item):
    depths = [cg.cell(table, s, DEPTH) for s in (S1, S2, S3)]
    energy = [cg.cell(table, s, KGENERGY) for s in (S1, S2, S3)]
    _pin_coal(table)
    assert all(depths[i] < depths[i + 1] for i in range(2)), f"depth must rise; got {depths}"
    assert all(energy[i] < energy[i + 1] for i in range(2)), f"energy must rise; got {energy}"
    assert len(set(energy)) == 3, "'all three released the same energy' must be false"
    return (f"the seams lie at {depths} meters and one kilogram releases {energy} energy units, "
            "the two columns rising together from the shallowest sample to the deepest")


def q20(table, item):
    _pin_coal(table)
    gap = cg.cell(table, S3, KGENERGY) - cg.cell(table, S1, KGENERGY)
    assert gap == 16, f"the gap recomputes to {gap}, not 16 energy units"
    for wrong in (cg.cell(table, S3, KGENERGY),
                  cg.cell(table, S3, KGENERGY) + cg.cell(table, S1, KGENERGY),
                  cg.cell(table, S2, KGENERGY),
                  sum(cg.col(table, KGENERGY))):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, S3, KGENERGY):.0f} minus {cg.cell(table, S1, KGENERGY):.0f} is "
            f"{gap:.0f} energy units for each kilogram")


def q21(table, item):
    _pin_coal(table)
    ratio = cg.cell(table, S3, DEPTH) / cg.cell(table, S1, DEPTH)
    assert ratio == 9, f"the ratio recomputes to {ratio}, not 9"
    for wrong in (3, 2, 27, 1):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, S3, DEPTH):.0f} divided by {cg.cell(table, S1, DEPTH):.0f} is "
            f"{ratio:.0f} times as deep")


def q22(table, item):
    assert cg.cell(table, GAS, SO2) == min(cg.col(table, SO2)), \
        "natural gas must release the least sulfur dioxide"
    assert cg.cell(table, GAS, PART) == min(cg.col(table, PART)), \
        "natural gas must release the fewest particulates"
    assert cg.cell(table, COAL, SO2) == max(cg.col(table, SO2)), \
        "'coal is the cleanest' must be false on the sulfur dioxide column"
    assert cg.cell(table, OILP, PART) > cg.cell(table, GAS, PART), \
        "'crude oil products are the cleanest' must be false on the particulate column"
    assert len(set(cg.col(table, SO2))) == 3, "'the three release the same amounts' must be false"
    return (f"sulfur dioxide runs {cg.col(table, SO2)} grams and particulates "
            f"{cg.col(table, PART)} grams for each unit of energy, natural gas lowest on both")


def q23(table, item):
    base = cg.cell(table, GAS, SO2)
    assert base > 0, "the natural gas figure must be non-zero for a ratio to exist"
    ratio = cg.cell(table, COAL, SO2) / base
    assert ratio == 600, f"the ratio recomputes to {ratio}, not 600"
    for wrong in (60, cg.cell(table, COAL, SO2), 300, 6):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, COAL, SO2):.0f} divided by {base:.0f} is {ratio:.0f} times as much "
            "sulfur dioxide for each unit of energy")


def q24(table, item):
    gap = cg.cell(table, COAL, PART) - cg.cell(table, OILP, PART)
    assert gap == 42, f"the gap recomputes to {gap}, not 42 grams"
    assert gap > 0, "'coal releases less than crude oil products' must be false"
    for wrong in (cg.cell(table, COAL, PART),
                  cg.cell(table, COAL, PART) + cg.cell(table, OILP, PART),
                  cg.cell(table, OILP, PART)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, COAL, PART):.0f} minus {cg.cell(table, OILP, PART):.0f} is "
            f"{gap:.0f} grams more particulate matter for each unit of energy")


def q25(table, item):
    assert cg.cell(table, P1, FUELIN) == cg.cell(table, P2, FUELIN), \
        "the two plants must burn the same fuel energy for the comparison to be fair"
    assert cg.cell(table, P2, ELEC) > 0 and cg.cell(table, P2, HEAT) > 0, \
        "the second plant must deliver BOTH electricity and useful heat"
    assert cg.cell(table, P1, HEAT) == 0, \
        "the first plant must deliver no useful heat, or both plants would qualify"
    assert cg.cell(table, P1, ELEC) > cg.cell(table, P2, ELEC), \
        "'the cogeneration plant qualifies because it makes less electricity' must be rejectable"
    return (f"the second plant turns {cg.cell(table, P2, FUELIN):.0f} energy units of fuel into "
            f"{cg.cell(table, P2, ELEC):.0f} of electricity and {cg.cell(table, P2, HEAT):.0f} of "
            f"useful heat, while the first delivers {cg.cell(table, P1, HEAT):.0f} useful heat")


def _useful_share(table, plant):
    return ((cg.cell(table, plant, ELEC) + cg.cell(table, plant, HEAT))
            / cg.cell(table, plant, FUELIN))


def q26(table, item):
    share = _useful_share(table, P2)
    assert abs(share - 0.75) < 1e-9, f"the share recomputes to {share}, not 75 percent"
    for wrong in (cg.cell(table, P2, ELEC) / cg.cell(table, P2, FUELIN),
                  cg.cell(table, P2, HEAT) / cg.cell(table, P2, FUELIN),
                  cg.cell(table, P1, ELEC) / cg.cell(table, P1, FUELIN),
                  1.0):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, P2, ELEC):.0f} plus {cg.cell(table, P2, HEAT):.0f} is "
            f"{share * 100:.0f} percent of the {cg.cell(table, P2, FUELIN):.0f} energy units "
            "put in")


def q27(table, item):
    gap = 100 * (_useful_share(table, P2) - _useful_share(table, P1))
    assert abs(gap - 40) < 1e-9, f"the gap recomputes to {gap}, not 40 percentage points"
    for wrong in (100 * _useful_share(table, P2),
                  100 * (_useful_share(table, P2) + _useful_share(table, P1)),
                  cg.cell(table, P2, ELEC),
                  cg.cell(table, P2, HEAT)):
        assert abs(gap - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{100 * _useful_share(table, P2):.0f} percent against "
            f"{100 * _useful_share(table, P1):.0f} percent is a gap of {gap:.0f} percentage "
            "points of useful output")


def q28(table, item):
    shares = cg.col(table, MASSSHARE)
    assert abs(sum(shares) - 100) < 1e-9, f"the four shares must total 100; got {sum(shares)}"
    assert cg.cell(table, SAND, MASSSHARE) == max(shares), "sand must be the largest component"
    assert cg.cell(table, WATER, MASSSHARE) == min(shares), "water must be the smallest component"
    bit = cg.cell(table, BITUMEN, MASSSHARE)
    tonnes = 100 / bit
    assert tonnes == 5, f"the mass of deposit for one tonne of bitumen recomputes to {tonnes}, not 5"
    for wrong in (20, 2, 1, 80):
        assert tonnes != wrong, f"the {wrong} distractor equals the key"
    assert cg.cell(table, CLAY, MASSSHARE) + cg.cell(table, SAND, MASSSHARE) > bit, \
        "the mineral fraction must outweigh the bitumen, or handling five tonnes would not matter"
    return (f"bitumen is {bit:.0f} percent of the deposit by mass, so {tonnes:.0f} tonnes of "
            "deposit hold one tonne of bitumen")


def q29(table, item):
    wood = {lab: cg.cell(table, lab, WOODSHARE) for lab in cg.labels(table)}
    grid = {lab: cg.cell(table, lab, GRIDSHARE) for lab in cg.labels(table)}
    assert wood[DEVING] > wood[DEVED], \
        f"the developing group must lean on wood more; got {wood[DEVING]} against {wood[DEVED]}"
    assert wood[DEVING] > 10 * wood[DEVED], "the gap must be large enough to read as a pattern"
    assert grid[DEVING] < grid[DEVED], \
        "the developing group must be the less well supplied with electricity"
    return (f"firewood or charcoal is the main fuel for {wood[DEVING]:.0f} percent of households "
            f"in the developing group against {wood[DEVED]:.0f} percent in the developed group")


CLAIMS = [
 ("Firewood and charcoal",
  "ENG-3.C.1, near verbatim: WOOD IS COMMONLY USED AS FUEL IN THE FORMS OF FIREWOOD AND CHARCOAL. Peat and the three coals carry their own statements, bitumen belongs to the tar sand description, and methane is what natural gas is mostly made of."),
 ("easily accessible",
  "ENG-3.C.1 supplies the reason itself: wood IS OFTEN USED IN DEVELOPING COUNTRIES BECAUSE IT IS EASILY ACCESSIBLE. The framework makes no energy-content comparison for wood and applies the word cleanest to natural gas rather than to wood."),
 ("Partially decomposed organic material",
  "ENG-3.C.2, near verbatim: PEAT IS PARTIALLY DECOMPOSED ORGANIC MATERIAL THAT CAN BE BURNED FOR FUEL. The three coals of ENG-3.C.3 do not include peat, and the four-material combination described elsewhere is a tar sand."),
 ("Lignite, bituminous, and anthracite",
  "ENG-3.C.3, near verbatim: THREE TYPES OF COAL USED FOR FUEL ARE LIGNITE, BITUMINOUS, AND ANTHRACITE. Peat, charcoal, bitumen and methane each belong to a different statement in this topic and coke appears in none of them."),
 ("Heat, pressure, and depth of burial",
  "ENG-3.C.3, near verbatim: HEAT, PRESSURE, AND DEPTH OF BURIAL CONTRIBUTE TO THE DEVELOPMENT of various coal types and their qualities. Rainfall, salinity, wind, soil type and sulfur content appear nowhere in the statement."),
 ("Natural gas",
  "ENG-3.C.4 opens by calling NATURAL GAS THE CLEANEST OF THE FOSSIL FUELS, and the framework applies that word to no other fuel in this topic. Peat is treated in its own statement rather than as one of the fossil fuels here."),
 ("Methane",
  "ENG-3.C.4 states that natural gas IS MOSTLY METHANE. Bitumen belongs to the tar sand description and none of the other rejected substances is named as a constituent of natural gas anywhere in this topic."),
 ("Tar sands",
  "ENG-3.C.5 states that CRUDE OIL CAN BE RECOVERED FROM TAR SANDS. Peat, anthracite and charcoal appear in this topic as fuels in their own right rather than as sources of crude oil, and methane hydrate is named nowhere in it."),
 ("Clay, sand, water, and bitumen",
  "ENG-3.C.5 states that tar sands ARE A COMBINATION OF CLAY, SAND, WATER, AND BITUMEN. Each rejected list swaps one of those four materials for something the statement does not name."),
 ("Specific fuel types for specialized uses",
  "ENG-3.C.6 states that FOSSIL FUELS CAN BE MADE INTO SPECIFIC FUEL TYPES FOR SPECIALIZED USES and gives motor vehicles as its own example. Processing does not make a fossil fuel renewable, and the statement claims nothing about what combustion releases."),
 ("both useful heat and electricity",
  "ENG-3.C.7, near verbatim: COGENERATION OCCURS WHEN A FUEL SOURCE IS USED TO GENERATE BOTH USEFUL HEAT AND ELECTRICITY. The number of fuels burned and the number of plants involved are not what the statement turns on, and heat drawn from the Earth's interior is geothermal energy in topic 6.10."),
 ("only one of the two useful outputs",
  "ENG-3.C.7 requires BOTH useful heat AND electricity from the one fuel source, and heat vented to the air is not delivered as useful heat. Nothing in the statement turns on which fuel is burned."),
 ("Peat is partially decomposed organic material, and the three coals named",
  "ENG-3.C.2 gives peat its own statement as partially decomposed organic material while ENG-3.C.3 names lignite, bituminous and anthracite as the three coals used for fuel. Charcoal belongs to ENG-3.C.1, which is about wood."),
 ("ranks them by the energy each releases",
  "ENG-3.C.3 names the three coals and names heat, pressure and depth of burial as contributors to their development and qualities, and stops there. It sets no order among them by energy content, so a ranking would have to be imported from outside the framework."),
 ("commonly used as firewood and charcoal, and often in developing countries",
  "ENG-3.C.1 covers both halves of the case, the two forms wood is burned in and the reason it is often the fuel in developing countries. Each rejected option quotes a different statement of this topic that the case does not touch."),
 ("fossil fuels can be made into specific fuel types for specialized uses",
  "ENG-3.C.6 states this and offers motor vehicles as the example, which is exactly what the refinery is doing. Recovery from tar sands, in ENG-3.C.5, is where crude oil comes from rather than what it is made into."),
 ("Cogeneration",
  "ENG-3.C.7 defines cogeneration as one fuel source used to generate both useful heat and electricity, which is what the factory does when the same steam drives the generator and then heats the buildings. Each rejected term names a different process in this topic."),
 ("pollutants released for each unit of energy by natural gas",
  "ENG-3.C.4 calls natural gas the cleanest of the fossil fuels, which is a comparison about what burning releases and can only be reported by measuring that. Price, depth of occurrence and the number of holding countries sit outside the statement."),
 ("more deeply buried seams released more energy for each kilogram",
  "Recomputed in q19 above: seams at 300, 900 and 2,700 meters against 16, 24 and 32 energy units for each kilogram, the two columns rising together. ENG-3.C.3 names DEPTH OF BURIAL among the things that contribute to coal types and their qualities."),
 ("16 energy units",
  "Recomputed in q20 above: 32 minus 16 energy units, with the deepest and shallowest seams identified by row rather than by position. The rejected values quote the deepest sample alone, add the deepest and shallowest, quote the middle sample, or add all three."),
 ("Nine times as deep",
  "Recomputed in q21 above: 2,700 divided by 300 meters. The rejected values come from the step between adjacent samples, from the ratio in the energy column, or from denying that the depths differ at all."),
 ("Natural gas, and it agrees with the framework, which calls natural gas the cleanest",
  "Recomputed in q22 above: 2 grams of sulfur dioxide and 0.2 grams of particulates for each unit of energy from natural gas, the least on both counts, against 1,200 and 60 from coal. ENG-3.C.4 calls natural gas the cleanest of the fossil fuels. One rejected option keeps the framework's attribution and misreads the data and another keeps the data and misattributes the framework, so the anchor carries both clauses."),
 ("600 times as much",
  "Recomputed in q23 above: 1,200 divided by 2 grams for each unit of energy. The rejected values read the particulate column instead, quote the coal figure alone, halve the answer, or drop two powers of ten."),
 ("42 grams",
  "Recomputed in q24 above: 60 minus 18 grams for each unit of energy. The rejected values quote one row alone, add the two rows, or invert the direction the table actually shows."),
 ("The second plant, because one fuel source there yields both useful heat",
  "Recomputed in q25 above: the second plant turns 100 energy units of fuel into 30 of electricity and 45 of useful heat, while the first delivers 35 of electricity and no useful heat. ENG-3.C.7 requires both outputs from one fuel source, and it sets no condition on how much electricity is produced. One rejected option attaches the correct ground to the wrong plant, so the anchor carries both."),
 ("75 percent",
  "Recomputed in q26 above: 30 plus 45 of the 100 energy units put in. The rejected values quote one output alone, quote the other plant's electricity, or assume nothing is lost at all."),
 ("40 percentage points",
  "Recomputed in q27 above: 75 percent of the fuel energy delivered usefully against 35 percent. The rejected values quote the cogeneration plant alone, add the two shares, or quote just one of that plant's two useful outputs."),
 ("Five tonnes",
  "Recomputed in q28 above: bitumen is 20 percent of the deposit by mass, one part in five. ENG-3.C.5 lists bitumen as one of the four materials a tar sand combines, the others being clay, sand and water."),
 ("often used as a fuel in developing countries because it is easily accessible",
  "Recomputed in q29 above: firewood or charcoal is the main fuel for 61 percent of households in the developing group against 3 percent in the developed group. ENG-3.C.1 states that wood is often used in developing countries because it is easily accessible. One rejected option is the same sentence with the two groups exchanged, so the anchor carries the group as well as the reason."),
 ("crude oil can come from tar sands; fossil fuels can be made into specialized fuels",
  "The keyed summary carries ENG-3.C.1 through C.7 in the framework's own terms and adds nothing. Each rejected summary misplaces peat among the coals, inverts the claim about natural gas, moves wood to the wrong group of countries, invents a coal ranking the framework does not give, or imports the renewable definition from topic 6.1."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback.

    ``e_check.run`` corrupts each table by reversing its numeric columns and,
    only if that is not caught, by flattening them. The flatten fallback is the
    loophole a weak check slips through, and the coal table is exactly the case
    that needs watching: reversing both of its columns leaves the (depth,
    energy) pairs untouched, so the association and both differences survive.
    The three coal checks pin the shallowest and deepest seams by row label for
    that reason, and this control is what proves the pin does the work.
    """
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_3_mutant")
        mod.TOPIC = e6_3.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_3.QUESTIONS)
        mutate(qs)
        try:
            run_on(qs)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:88]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def reverse_columns(table):
        t = copy.deepcopy(table)
        for j in range(1, len(t["headers"])):
            vals = [r[j] for r in t["rows"]]
            for r, v in zip(t["rows"], reversed(vals)):
                r[j] = v
        return t

    print("selftest: reversal alone must be caught for every table")
    for i in sorted(TABLE_CHECKS):
        must_fail(f"q{i} table columns reversed (no flatten fallback)",
                  lambda qs, i=i: qs[i - 1].__setitem__(
                      "table", reverse_columns(qs[i - 1]["table"])))

    def edit(qi, row_label, header, value):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(header))
            for r in t["rows"]:
                if cg.normalize(r[0]) == cg.normalize(row_label):
                    r[j] = value
            qs[qi - 1]["table"] = t
        return mutate

    print("selftest: one cell at a time, against the keyed number")
    must_fail("q20 gap moved off 16 energy units", edit(20, S3, KGENERGY, "40"))
    must_fail("q21 ratio moved off nine times as deep", edit(21, S3, DEPTH, "3,000"))
    must_fail("q23 ratio moved off 600 times as much", edit(23, GAS, SO2, "3"))
    must_fail("q24 gap moved off 42 grams", edit(24, OILP, PART, "20"))
    must_fail("q26 useful share moved off 75 percent", edit(26, P2, HEAT, "40"))
    must_fail("q27 gap moved off 40 percentage points", edit(27, P1, ELEC, "30"))
    must_fail("q28 bitumen share moved off one part in five",
              edit(28, BITUMEN, MASSSHARE, "25"))
    must_fail("q29 wood shares brought level", edit(29, DEVING, WOODSHARE, "4"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_3.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_3, CLAIMS, TABLE_CHECKS)
