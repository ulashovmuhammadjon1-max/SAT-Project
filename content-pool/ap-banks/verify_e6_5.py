"""Key audit for AP ENVIRONMENTAL SCIENCE 6.5 Fossil Fuels.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.E.1  The combustion of fossil fuels is a chemical reaction between the
             fuel and oxygen that yields carbon dioxide and water and releases
             energy.                    -- items 1, 2, 3, 18, 24, 25, 26
  ENG-3.E.2  Energy from fossil fuels is produced by burning those fuels to
             generate heat, which then turns water into steam. That steam turns
             a turbine, which spins a generator, producing electricity.
                            -- items 4, 5, 6, 7, 8, 9, 19, 20, 21, 22, 23
  ENG-3.E.3  Humans use a variety of methods to extract fossil fuels from the
             earth for energy generation.        -- items 10, 11, 12
  ENG-3.F.1  Hydraulic fracturing (fracking) can cause groundwater contamination
             and the release of volatile organic compounds.
                                        -- items 13, 14, 15, 16, 17, 27, 28, 29
  item 30 reads across all four.

THE SEQUENCE IS THE FRAMEWORK'S OWN and five items turn on it. The natural
distractor is the chain with two links exchanged -- the steam spinning the
generator and the generator turning the turbine -- so those anchors carry the
sequence rather than a single link. An anchor naming one link alone would match
the exchanged chain too, which is the defect this project has already shipped in
another module.

ENG-3.E.3 NAMES NO METHOD. It says A VARIETY OF METHODS and stops, so no key
asserts that the framework names drilling, surface mining or any other
technique; item 12 keys the absence. The only extraction method named anywhere
in the topic is hydraulic fracturing, and it appears only in ENG-3.F.1.

ENG-3.F.1 ATTACHES EXACTLY TWO EFFECTS, groundwater contamination and the
release of volatile organic compounds, and it hedges them with CAN. Induced
earthquakes, methane leakage and subsidence are not in the statement, so item 14
keys the correction and item 15 keys the hedge.

WHAT COMBUSTION YIELDS, exactly. ENG-3.E.1 names carbon dioxide and water.
Sulfur dioxide, nitrogen oxides and particulates belong to other statements, so
every item about products asks what the FRAMEWORK NAMES rather than what a
furnace emits, and the distractors are drawn from those other statements.

DATA ITEMS: 20 to 29, recomputed below from those tables alone.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_5.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, without e_check's flatten fallback --
which matters most for the fracking table, whose control column of distant
wells reads 3, 4 and 3 and is therefore unchanged by a reversal.
"""
import e_check
import cg_check as cg
import e6_5

AVAIL = "Energy still available at that stage (energy units)"
FUEL = "Chemical energy in the fuel burned"
STEAM = "Heat carried by the steam"
TURBINE = "Mechanical energy turning the turbine"
GENERATOR = "Electricity leaving the generator"
CHAIN = [FUEL, STEAM, TURBINE, GENERATOR]

CO2COL = "Carbon dioxide released for each unit of energy (kilograms)"
H2OCOL = "Water released for each unit of energy (kilograms)"
COAL, OILP, GAS = "Coal", "Crude oil products", "Natural gas"

NEAR = "Wells within two kilometers of the site above the contaminant limit (percent)"
FAR = "Wells more than ten kilometers away above the limit (percent)"
VOC = "Volatile organic compounds in the air at the site (parts per billion)"
BEFORE = "Before fracking began"
YEAR1 = "One year after fracking began"
YEAR3 = "Three years after fracking began"


def _stage_values(table):
    labs = cg.labels(table)
    assert labs == CHAIN, f"the record must run fuel, steam, turbine, generator; got {labs}"
    return [cg.cell(table, lab, AVAIL) for lab in CHAIN]


def q20(table, item):
    vals = _stage_values(table)
    assert all(vals[i] > vals[i + 1] for i in range(3)), \
        f"the energy still available must fall at every step; got {vals}"
    return (f"the record runs {CHAIN} with {vals} energy units still available, the sequence "
            "ENG-3.E.2 gives and falling at every step")


def _losses(table):
    vals = _stage_values(table)
    return [vals[i] - vals[i + 1] for i in range(3)]


def q21(table, item):
    losses = _losses(table)
    biggest = max(range(3), key=lambda i: losses[i])
    assert biggest == 1, \
        f"the largest loss must fall between the steam and the turbine; got step {biggest}"
    assert losses[1] == 480, f"that loss recomputes to {losses[1]}, not 480 energy units"
    assert losses[0] == 120, f"the first loss recomputes to {losses[0]}, not 120 energy units"
    assert losses[2] == 20, f"the last loss recomputes to {losses[2]}, not 20 energy units"
    assert len(set(losses)) == 3, "'the same amount is lost at every step' must be false"
    return (f"the three losses recompute to {losses} energy units, so the fall from the steam to "
            "the turbine is the largest and no other step matches it")


def q22(table, item):
    vals = _stage_values(table)
    share = vals[3] / vals[0]
    assert abs(share - 0.38) < 1e-9, f"the share recomputes to {share}, not 38 percent"
    for wrong in (vals[1] / vals[0], vals[2] / vals[0], 1 - share, 1.0):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{vals[3]:.0f} of the {vals[0]:.0f} energy units in the fuel leaves as electricity, "
            f"which is {share * 100:.0f} percent")


def q23(table, item):
    vals = _stage_values(table)
    loss = vals[0] - vals[1]
    assert loss == 120, f"the loss recomputes to {loss}, not 120 energy units"
    for wrong in (vals[0] - vals[3], vals[1] - vals[2], vals[0] - vals[2], vals[1]):
        assert loss != wrong, f"the {wrong} distractor equals the key"
    return (f"{vals[0]:.0f} minus {vals[1]:.0f} is {loss:.0f} energy units lost turning the "
            "chemical energy of the fuel into the heat carried by the steam")


def q24(table, item):
    co2, water = cg.col(table, CO2COL), cg.col(table, H2OCOL)
    assert all(v > 0 for v in co2), f"every fuel must release carbon dioxide; got {co2}"
    assert all(v > 0 for v in water), f"every fuel must release water; got {water}"
    assert cg.cell(table, COAL, CO2COL) == max(co2), \
        "coal must lead the carbon dioxide column, so the record is read on the right rows"
    assert len(set(co2)) == len(co2), "'the three release the same carbon dioxide' must be false"
    return (f"carbon dioxide runs {co2} and water runs {water} kilograms for each unit of energy, "
            "both positive in every row, which is what ENG-3.E.1 names as the products")


def q25(table, item):
    gap = cg.cell(table, COAL, CO2COL) - cg.cell(table, GAS, CO2COL)
    assert gap == 42, f"the gap recomputes to {gap}, not 42 kilograms"
    for wrong in (cg.cell(table, COAL, CO2COL) - cg.cell(table, OILP, CO2COL),
                  cg.cell(table, COAL, CO2COL) + cg.cell(table, GAS, CO2COL),
                  cg.cell(table, COAL, CO2COL),
                  cg.cell(table, GAS, CO2COL)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, COAL, CO2COL):.0f} minus {cg.cell(table, GAS, CO2COL):.0f} is "
            f"{gap:.0f} kilograms more carbon dioxide for each unit of energy")


def q26(table, item):
    co2, water = cg.col(table, CO2COL), cg.col(table, H2OCOL)
    assert cg.cell(table, GAS, CO2COL) == min(co2), "natural gas must release the least carbon dioxide"
    assert cg.cell(table, GAS, H2OCOL) == max(water), "natural gas must release the most water"
    assert cg.cell(table, COAL, CO2COL) == max(co2), \
        "'coal releases the least carbon dioxide' must be false"
    assert cg.cell(table, OILP, CO2COL) != min(co2), \
        "'crude oil products release the least of both' must be false"
    return (f"natural gas sits at {cg.cell(table, GAS, CO2COL):.0f} kilograms of carbon dioxide, "
            f"the lowest of {co2}, and {cg.cell(table, GAS, H2OCOL):.0f} kilograms of water, the "
            f"highest of {water}")


def _frack(table):
    near = [cg.cell(table, r, NEAR) for r in (BEFORE, YEAR1, YEAR3)]
    far = [cg.cell(table, r, FAR) for r in (BEFORE, YEAR1, YEAR3)]
    voc = [cg.cell(table, r, VOC) for r in (BEFORE, YEAR1, YEAR3)]
    return near, far, voc


def q27(table, item):
    near, far, voc = _frack(table)
    assert all(near[i] < near[i + 1] for i in range(2)), \
        f"the share of nearby wells above the limit must rise; got {near}"
    assert all(voc[i] < voc[i + 1] for i in range(2)), \
        f"volatile organic compounds in the air must rise; got {voc}"
    assert near[2] > 5 * near[0], "the groundwater change must be large enough to read"
    assert voc[2] > 5 * voc[0], "the air change must be large enough to read"
    return (f"nearby wells above the limit run {near} percent while volatile organic compounds "
            f"run {voc} parts per billion, both rising after fracking began")


def q28(table, item):
    near, _, _ = _frack(table)
    rise = near[2] - near[0]
    assert rise == 34, f"the rise recomputes to {rise}, not 34 percentage points"
    for wrong in (near[2], near[2] + near[0], near[1] - near[0], near[2] - near[1]):
        assert rise != wrong, f"the {wrong} distractor equals the key"
    return (f"{near[2]:.0f} minus {near[0]:.0f} is {rise:.0f} percentage points more nearby wells "
            "above the contaminant limit")


def q29(table, item):
    """The distant wells are the control, and the near column is what moves.

    Reversing this table leaves the control column reading 3, 4, 3 exactly as
    before, so a check that read only that column could not fire. The rising
    near column is part of the keyed conclusion and is asserted here for that
    reason as well as on its merits.
    """
    near, far, voc = _frack(table)
    assert max(far) - min(far) <= 2, f"the distant wells must barely move; got {far}"
    assert all(near[i] < near[i + 1] for i in range(2)), \
        f"the nearby wells must be the column that rises; got {near}"
    assert near[2] > 5 * max(far), \
        "the nearby share must end far above the distant share, or the rise is not local"
    assert far[2] >= far[0] - 1, "'the distant wells fell sharply' must be false"
    assert max(voc) > min(voc), \
        "the volatile organic compound column must be the one that carries the air reading"
    return (f"the distant wells run {far} percent throughout while the nearby wells run {near} "
            "percent, so the change is confined to the ground close to the site")


CLAIMS = [
 ("chemical reaction between the fuel and oxygen",
  "ENG-3.E.1, near verbatim: the combustion of fossil fuels IS A CHEMICAL REACTION BETWEEN THE FUEL AND OXYGEN. Nuclear reactions belong to topic 6.6, nothing in the statement makes combustion a physical change, and the gas named is oxygen rather than nitrogen."),
 ("Carbon dioxide and water",
  "ENG-3.E.1 states that the reaction YIELDS CARBON DIOXIDE AND WATER. Carbon monoxide, nitrogen oxides and particulates appear in ENG-3.I.1 for biomass and in the atmospheric pollution unit, not in this statement."),
 ("It releases energy",
  "ENG-3.E.1 ends by saying the reaction RELEASES ENERGY, which is why the fuel is burned at all. Oxygen is a reactant rather than a product in the statement, and carbon dioxide is produced rather than removed."),
 ("It turns water into steam",
  "ENG-3.E.2 states that burning the fuel generates heat, WHICH THEN TURNS WATER INTO STEAM. The turbine and the generator come later in the framework's sequence, and splitting atoms is nuclear fission in topic 6.6."),
 ("It turns a turbine",
  "ENG-3.E.2 states that THAT STEAM TURNS A TURBINE. The generator comes after the turbine in the framework's sequence, and steam is the working fluid rather than a fuel in its own right."),
 ("It spins a generator, which produces the electricity",
  "ENG-3.E.2 states that the steam turns a turbine, WHICH SPINS A GENERATOR, PRODUCING ELECTRICITY. The turbine and the generator are separate parts of the sequence and the electricity comes from the second of them."),
 ("the steam turns a turbine, the turbine spins a generator",
  "ENG-3.E.2 gives the whole sequence in one sentence, and each rejected sequence exchanges two of its links. An anchor naming one link alone would match the exchanged chain as well, so it carries two consecutive links instead."),
 ("heat turns water into steam, and it is the steam that turns the turbine",
  "ENG-3.E.2 puts steam between the heat and the turbine. The framework plainly does give a sequence, and the generator comes after the turbine rather than before it, so the corrections that reorder those two parts are wrong in a second way."),
 ("turbine spins a generator, and the generator is what produces the electricity",
  "ENG-3.E.2 states that the steam turns a turbine WHICH SPINS A GENERATOR, PRODUCING ELECTRICITY, so the two parts have different jobs. Nothing in the statement gives the generator a storage role or gives the turbine the electrical one."),
 ("a variety of methods, without the framework naming which ones",
  "ENG-3.E.3 states that HUMANS USE A VARIETY OF METHODS TO EXTRACT FOSSIL FUELS FROM THE EARTH FOR ENERGY GENERATION, and it lists none of them. Fossil fuels are certainly extracted and the framework does address extraction, so the options denying either are wrong on their face."),
 ("Energy generation",
  "ENG-3.E.3 states that the extraction is FOR ENERGY GENERATION. Materials manufacture, export earnings and construction are not named in the statement, and the statement does supply a purpose rather than withholding one."),
 ("names drilling and surface mining as the two methods",
  "ENG-3.E.3 says a variety of methods and names none, so any list of specific techniques is imported from outside the framework. Each rejected option is a direct reading of the statement, and the only extraction method the framework names anywhere in this topic is hydraulic fracturing in ENG-3.F.1."),
 ("Groundwater contamination and the release of volatile organic compounds",
  "ENG-3.F.1, near verbatim: hydraulic fracturing CAN CAUSE GROUNDWATER CONTAMINATION AND THE RELEASE OF VOLATILE ORGANIC COMPOUNDS. Radioactive waste belongs to nuclear power in topic 6.6 and the remaining effects are treated in other units."),
 ("volatile organic compounds to fracking, and nothing else",
  "ENG-3.F.1 names exactly two possible effects and earthquakes is not among them. The statement does attach effects, so denying that it does is wrong in the other direction, and dropping the groundwater half leaves the statement incomplete."),
 ("possible consequences rather than certain ones",
  "ENG-3.F.1 says fracking CAN CAUSE those two effects, which asserts possibility rather than certainty. Reading the hedge away in either direction changes what the framework claims, and the statement is not restricted to any set of countries."),
 ("Contamination of groundwater and the release of volatile organic compounds",
  "The method described is hydraulic fracturing, and ENG-3.F.1 attaches those two effects to it. The rejected options quote the effects the framework attaches to nuclear power, wind energy, geothermal energy and hydroelectric power in other topics of this unit."),
 ("Testing wells near a fracking site for contaminants",
  "ENG-3.F.1 names groundwater contamination and the release of volatile organic compounds, so testing the groundwater and the air is what bears on it. Well counts, the later combustion of the gas, its price and its energy content each belong to a different statement."),
 ("combustion yields carbon dioxide and water and releases energy",
  "ENG-3.E.1 is about the products of the reaction, so it describes what the burning puts out. ENG-3.E.2 describes the machinery, ENG-3.E.3 the getting of the fuel, and ENG-3.F.1 the effects of one extraction method rather than of the burning."),
 ("heat is transferred to water, and the steam that forms is what turns the turbine",
  "ENG-3.E.2 makes steam the link between the heat and the turbine. Water is a product of combustion in ENG-3.E.1 rather than a reactant, it is not a fuel, and nothing in the framework gives it a cooling or conducting role in this account."),
 ("own: fuel, then steam, then turbine, then generator",
  "Recomputed in q20 above: the record runs from the chemical energy in the fuel to the heat in the steam, then the mechanical energy at the turbine, then the electricity leaving the generator, and the energy still available falls at every step. ENG-3.E.2 gives exactly that sequence."),
 ("Between the steam and the turbine, where 480 energy units are lost",
  "Recomputed in q21 above: the record falls 1,000, 880, 400 and 380 energy units, so the three losses are 120, 480 and 20. One rejected option pairs the right size with the wrong step, so the anchor carries both the step and the amount."),
 ("38 percent",
  "Recomputed in q22 above: 380 of the 1,000 energy units in the fuel. The rejected values quote an intermediate stage, take the share lost rather than the share delivered, or assume nothing is lost at all."),
 ("120 energy units",
  "Recomputed in q23 above: 1,000 minus 880 energy units. The rejected values take the whole loss across the plant, take a later step, run the loss all the way to the turbine, or quote the energy remaining rather than the amount lost."),
 ("All three fuels release both carbon dioxide and water",
  "Recomputed in q24 above: carbon dioxide of 95, 73 and 53 kilograms and water of 30, 40 and 60 kilograms for each unit of energy, every value positive. ENG-3.E.1 names both as what the reaction yields, so water is a product rather than a reactant."),
 ("42 kilograms",
  "Recomputed in q25 above: 95 minus 53 kilograms for each unit of energy. The rejected values take the gap to crude oil products instead, add the two rows, or quote one row alone."),
 ("Natural gas, which also releases the most water for each unit of energy",
  "Recomputed in q26 above: natural gas is lowest in the carbon dioxide column at 53 kilograms and highest in the water column at 60. ENG-3.E.1 names both as products of the one reaction, so a fuel can be lowest on one and highest on the other. One rejected option keeps the fuel and inverts the second clause, so the anchor carries both."),
 ("can cause groundwater contamination and the release of volatile organic compounds",
  "Recomputed in q27 above: nearby wells above the contaminant limit rise from 4 to 26 to 38 percent while volatile organic compounds rise from 5 to 41 to 55 parts per billion. ENG-3.F.1 names both effects together, and the two rejected options that keep one and drop the other are what the anchor's conjunction excludes."),
 ("By 34 percentage points",
  "Recomputed in q28 above: 38 minus 4 percent of nearby wells. The rejected values quote the final round alone, add the two, or take one of the two steps within the record."),
 ("stays near where it began, so the rise is confined to the wells close to the site",
  "Recomputed in q29 above: the distant wells run 3, 4 and 3 percent throughout while the nearby wells run 4, 26 and 38 percent. A control that does not move is what ties the change to the site, which is the evidence ENG-3.F.1's claim about groundwater contamination requires."),
 ("the steam turns a turbine, the turbine spins a generator that makes electricity",
  "The keyed summary carries ENG-3.E.1, E.2, E.3 and F.1 in the framework's own terms and adds nothing. Each rejected summary misnames the reaction, exchanges two links of the sequence, invents an extraction method or an effect the framework does not name, or imports the renewable definition from topic 6.1."),
]

TABLE_CHECKS = {20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25,
                26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_5_mutant")
        mod.TOPIC = e6_5.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_5.QUESTIONS)
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
            try:
                [cg.num(v) for v in vals]
            except AssertionError:
                continue
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
    must_fail("q20 the chain made to gain energy at a step", edit(20, TURBINE, AVAIL, "900"))
    must_fail("q21 the largest loss moved to the first step", edit(21, STEAM, AVAIL, "450"))
    must_fail("q22 delivered share moved off 38 percent", edit(22, GENERATOR, AVAIL, "300"))
    must_fail("q23 first loss moved off 120 energy units", edit(23, STEAM, AVAIL, "800"))
    must_fail("q24 one fuel made to release no water", edit(24, OILP, H2OCOL, "0"))
    must_fail("q25 gap moved off 42 kilograms", edit(25, GAS, CO2COL, "50"))
    must_fail("q26 natural gas made the driest rather than the wettest",
              edit(26, GAS, H2OCOL, "10"))
    must_fail("q27 the air reading left flat", edit(27, YEAR3, VOC, "5"))
    must_fail("q28 rise moved off 34 percentage points", edit(28, YEAR3, NEAR, "30"))
    must_fail("q29 the distant control made to rise with the near wells",
              edit(29, YEAR3, FAR, "36"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_5.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_5, CLAIMS, TABLE_CHECKS)
