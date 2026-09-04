"""Key audit for AP ENVIRONMENTAL SCIENCE 6.11 Hydrogen Fuel Cell.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.P.1  Hydrogen fuel cells are an alternate to non-renewable fuel
             sources. They use hydrogen as fuel, combining the hydrogen and
             oxygen in the air to form water and release energy (electricity)
             in the process. Water is the product (emission) of a fuel cell.
                          -- items 1, 2, 3, 4, 5, 6, 7, 13, 14, 19, 20, 21
  ENG-3.Q.1  Hydrogen fuel cells have low environmental impact and produce no
             carbon dioxide when the hydrogen is produced from water. However,
             the technology is expensive and energy is still needed to create
             the hydrogen gas used in the fuel cell.
                          -- items 8, 9, 10, 11, 12, 15, 16, 17, 18, 22, 23,
                             24, 25, 26, 27, 28, 29
  item 30 restates both.

THE CARBON DIOXIDE CLAIM IS CONDITIONAL and that condition is the whole of what
this topic is easiest to get wrong. ENG-3.Q.1 says NO CARBON DIOXIDE WHEN THE
HYDROGEN IS PRODUCED FROM WATER. Items 9, 10, 15, 18 and 22 key the condition
and each of those anchors carries it, because the distractor a prepared student
reaches for is the same sentence with the condition removed.

HYDROGEN IS NOT CLASSIFIED. ENG-3.P.1 calls a fuel cell AN ALTERNATE TO
NON-RENEWABLE FUEL SOURCES, which says what it stands beside and not what it is.
Item 2 keys that absence, and it agrees with the boundary already recorded in
e6_1.py, where hydrogen is deliberately excluded from the classification items.

WATER IS THE PRODUCT and the framework names it twice, in the reaction and as
the emission. Item 14 sets that against ENG-3.E.1, where the combustion of a
fossil fuel yields carbon dioxide AND water; one distractor there is the exact
swap of the two products, so the anchor carries both halves.

DATA ITEMS: 19 to 29, recomputed below from those tables alone. The hydrogen
chain table is the one that carries ENG-3.Q.1's second reservation: 100 energy
units invested in creating the hydrogen against 62 returned as electricity, so
the fuel has to be made before it can be used.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_11.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, and it establishes the clean pass
BEFORE any mutation so a standing defect cannot hide behind the controls.
"""
import e_check
import cg_check as cg
import e6_11

IN = "Amount entering the cell each hour (units)"
OUT = "Amount leaving the cell each hour (units)"
H2, O2, H2O, CO2 = "Hydrogen", "Oxygen taken from the air", "Water", "Carbon dioxide"

INVEST = "Energy invested to make one unit of hydrogen (energy units)"
MADECO2 = "Carbon dioxide released in making one unit of hydrogen (kilograms)"
FROMWATER = "Produced from water"
FROMFOSSIL = "Produced from a fossil fuel"

KIT = "Cost of the equipment for each vehicle (thousand currency units)"
PERDIST = "Carbon dioxide released for each unit of distance (kilograms)"
CELLFLEET = "Hydrogen fuel cell, hydrogen produced from water"
GASFLEET = "Gasoline engine"

STEPENERGY = "Energy involved at that step (energy units)"
MAKESTEP = "Energy invested to create the hydrogen gas"
DELIVERSTEP = "Electricity the fuel cell delivers from that hydrogen"


def q19(table, item):
    assert cg.cell(table, H2, IN) > 0 and cg.cell(table, O2, IN) > 0, \
        "hydrogen and oxygen must both enter the cell"
    assert cg.cell(table, H2O, OUT) > 0, "water must leave the cell"
    assert cg.cell(table, H2O, IN) == 0, "water must not enter, or it would be the fuel"
    assert cg.cell(table, CO2, IN) == 0 and cg.cell(table, CO2, OUT) == 0, \
        "carbon dioxide must be absent on both sides"
    assert cg.cell(table, H2, OUT) == 0, "'the hydrogen leaves unchanged' must be false"
    return (f"hydrogen enters at {cg.cell(table, H2, IN):.0f} units an hour and oxygen at "
            f"{cg.cell(table, O2, IN):.0f}, water leaves at {cg.cell(table, H2O, OUT):.0f}, and "
            "the carbon dioxide row is zero on both sides")


def q20(table, item):
    leaving = [lab for lab in cg.labels(table) if cg.cell(table, lab, OUT) > 0]
    assert leaving == [H2O], f"exactly water must leave the cell; got {leaving}"
    assert cg.cell(table, H2, IN) > 0, "hydrogen must be an input rather than an output"
    assert cg.cell(table, O2, IN) > 0, "oxygen must be an input rather than an output"
    return (f"the leaving column reads {cg.col(table, OUT)} units an hour, so {leaving[0]} is the "
            "only substance that comes out of the cell")


def q21(table, item):
    assert cg.cell(table, H2, IN) > 0, "hydrogen must enter the cell for a ratio to exist"
    assert cg.cell(table, O2, IN) > 0, "oxygen must enter the cell, or the reaction is not the one described"
    ratio = cg.cell(table, H2O, OUT) / cg.cell(table, H2, IN)
    assert ratio == 1, f"the ratio recomputes to {ratio}, not one to one"
    for wrong in (cg.cell(table, H2, IN) / cg.cell(table, O2, IN),
                  cg.cell(table, O2, IN) / cg.cell(table, H2, IN),
                  cg.cell(table, H2O, OUT),
                  0):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, H2, IN):.0f} units of hydrogen in and "
            f"{cg.cell(table, H2O, OUT):.0f} units of water out is {ratio:.0f} unit of water for "
            "each unit of hydrogen")


def q22(table, item):
    assert cg.cell(table, FROMWATER, MADECO2) == 0, \
        "the route from water must release no carbon dioxide"
    assert cg.cell(table, FROMFOSSIL, MADECO2) > 0, \
        "the other route must release some, or the condition would make no difference"
    return (f"producing the hydrogen from water releases "
            f"{cg.cell(table, FROMWATER, MADECO2):.0f} kilograms of carbon dioxide for each unit "
            f"against {cg.cell(table, FROMFOSSIL, MADECO2):.0f} from a fossil fuel, which is why "
            "the framework attaches a condition to its claim")


def q23(table, item):
    assert cg.cell(table, FROMWATER, MADECO2) == 0, \
        "the route from water must stay the one that releases nothing, so the rows are not swapped"
    for lab in cg.labels(table):
        assert cg.cell(table, lab, INVEST) > 0, \
            f"{lab} must carry an energy investment, or 'still needed' goes unshown"
    return (f"both routes carry an energy investment, {cg.col(table, INVEST)} energy units for "
            "each unit of hydrogen, so neither is free of the call on energy")


def q24(table, item):
    assert cg.cell(table, FROMWATER, MADECO2) == 0, \
        "the route from water must stay identified by its zero carbon dioxide"
    gap = cg.cell(table, FROMWATER, INVEST) - cg.cell(table, FROMFOSSIL, INVEST)
    assert gap == 15, f"the gap recomputes to {gap}, not 15 energy units"
    assert gap > 0, "'the route from water requires less energy' must be false"
    for wrong in (cg.cell(table, FROMFOSSIL, INVEST),
                  cg.cell(table, FROMWATER, INVEST) + cg.cell(table, FROMFOSSIL, INVEST),
                  cg.cell(table, FROMWATER, INVEST)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, FROMWATER, INVEST):.0f} minus "
            f"{cg.cell(table, FROMFOSSIL, INVEST):.0f} is {gap:.0f} energy units more for each "
            "unit of hydrogen by the route from water")


def q25(table, item):
    assert cg.cell(table, CELLFLEET, PERDIST) == 0, \
        "the fuel cell fleet must release no carbon dioxide for each unit of distance"
    assert cg.cell(table, GASFLEET, PERDIST) > 0, "the gasoline fleet must release some"
    assert cg.cell(table, CELLFLEET, KIT) > cg.cell(table, GASFLEET, KIT), \
        "the fuel cell equipment must be the dearer, or the trade-off does not appear"
    return (f"the fuel cell fleet reads {cg.cell(table, CELLFLEET, PERDIST):.0f} kilograms for "
            f"each unit of distance against {cg.cell(table, GASFLEET, PERDIST)}, while its "
            f"equipment costs {cg.cell(table, CELLFLEET, KIT):.0f} thousand currency units "
            f"against {cg.cell(table, GASFLEET, KIT):.0f}")


def q26(table, item):
    ratio = cg.cell(table, CELLFLEET, KIT) / cg.cell(table, GASFLEET, KIT)
    assert ratio == 3, f"the ratio recomputes to {ratio}, not 3"
    assert ratio > 1, "'the fuel cell equipment costs the less' must be false"
    for wrong in (2, 4, 30):
        assert ratio != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, CELLFLEET, KIT):.0f} divided by "
            f"{cg.cell(table, GASFLEET, KIT):.0f} is {ratio:.0f} times as much for the equipment "
            "on each vehicle")


def _chain(table):
    labs = cg.labels(table)
    assert labs == [MAKESTEP, DELIVERSTEP], \
        f"the record must run investment then delivery; got {labs}"
    return cg.cell(table, MAKESTEP, STEPENERGY), cg.cell(table, DELIVERSTEP, STEPENERGY)


def q27(table, item):
    invested, delivered = _chain(table)
    assert invested > 0, "the hydrogen must cost energy to create, or the reservation goes unshown"
    assert delivered > 0, "the cell must deliver something, or nothing is being compared"
    assert invested > delivered, \
        f"more energy must go in than comes back; got {invested} in and {delivered} out"
    return (f"{invested:.0f} energy units go into creating the hydrogen and {delivered:.0f} come "
            "back as electricity, so the fuel had to be made before it could be used")


def q28(table, item):
    invested, delivered = _chain(table)
    share = delivered / invested
    assert abs(share - 0.62) < 1e-9, f"the share recomputes to {share}, not 62 percent"
    for wrong in (1 - share, 1.0, share / 2, (invested + delivered) / invested):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{delivered:.0f} of the {invested:.0f} energy units invested comes back, which is "
            f"{share * 100:.0f} percent")


def q29(table, item):
    invested, delivered = _chain(table)
    lost = invested - delivered
    assert lost == 38, f"the shortfall recomputes to {lost}, not 38 energy units"
    assert lost > 0, "'all the energy comes back' must be false"
    for wrong in (delivered, lost / 2, invested):
        assert lost != wrong, f"the {wrong} distractor equals the key"
    return (f"{invested:.0f} minus {delivered:.0f} is {lost:.0f} energy units that do not come "
            "back as electricity")


CLAIMS = [
 ("An alternate to non-renewable fuel sources",
  "ENG-3.P.1 opens by stating that HYDROGEN FUEL CELLS ARE AN ALTERNATE TO NON-RENEWABLE FUEL SOURCES. The most widely used sources globally are fossil fuels in ENG-3.B.2, and nuclear power and passive solar systems are treated in topics 6.6 and 6.8."),
 ("says only what a fuel cell is an alternative to, and gives hydrogen no class",
  "ENG-3.P.1 calls a fuel cell an alternate to non-renewable fuel sources, which says what it stands beside rather than what it is. The framework labels nuclear power nonrenewable in ENG-3.G.4 and wind renewable in ENG-3.S.1, so it labels a source where it means to, and it plainly does treat hydrogen as a fuel."),
 ("Hydrogen",
  "ENG-3.P.1 states that fuel cells USE HYDROGEN AS FUEL. Water is the product of the cell rather than its fuel, and methane, ethanol and Uranium-235 belong to topics 6.3, 6.7 and 6.6."),
 ("Oxygen taken from the air",
  "ENG-3.P.1 states that the cell combines THE HYDROGEN AND OXYGEN IN THE AIR. Joining atoms into heavier ones is fusion, which the framework never describes, and no boiler appears anywhere in this topic."),
 ("forms water and releases energy in the form of electricity",
  "ENG-3.P.1 states that the cell combines the hydrogen and oxygen TO FORM WATER AND RELEASE ENERGY, and puts ELECTRICITY in brackets beside that energy. No turbine, generator or boiler appears in the framework's account of a fuel cell."),
 ("Water",
  "ENG-3.P.1 ends by stating that WATER IS THE PRODUCT, or emission, OF A FUEL CELL. The framework names it twice in the same statement, once in the reaction and once as the emission, so something does leave the cell."),
 ("combines with oxygen from the air, water forms, and electricity is released",
  "ENG-3.P.1 gives the whole account in one sentence: hydrogen as fuel, combined with oxygen in the air, forming water and releasing energy as electricity. Water is the product rather than the input, no steam or turbine appears, and joining atoms is fusion, which the framework never describes."),
 ("That it is low",
  "ENG-3.Q.1 opens by stating that HYDROGEN FUEL CELLS HAVE LOW ENVIRONMENTAL IMPACT. The same statement names two reservations, so low is not the same as none, and the claim is made rather than withheld."),
 ("When the hydrogen is produced from water",
  "ENG-3.Q.1 states that fuel cells PRODUCE NO CARBON DIOXIDE WHEN THE HYDROGEN IS PRODUCED FROM WATER. The condition is part of the claim, and the statement attaches no condition about cost, about where the oxygen comes from, or about the use the cell is put to."),
 ("holds when the hydrogen is produced from water, and it says nothing about hydrogen made another way",
  "ENG-3.Q.1 attaches the words WHEN THE HYDROGEN IS PRODUCED FROM WATER to the carbon dioxide claim. Dropping the condition states more than the framework does and reversing it states the opposite; the framework certainly does make the claim."),
 ("technology is expensive, and that energy is still needed to create the hydrogen gas",
  "ENG-3.Q.1 states that HOWEVER, THE TECHNOLOGY IS EXPENSIVE AND ENERGY IS STILL NEEDED TO CREATE THE HYDROGEN GAS USED IN THE FUEL CELL. One rejected option keeps the second reservation and inverts the first, so the anchor carries both."),
 ("hydrogen gas has to be made before it can be used, and making it takes energy",
  "ENG-3.Q.1 says ENERGY IS STILL NEEDED TO CREATE THE HYDROGEN GAS USED IN THE FUEL CELL, so the fuel is manufactured rather than found and the manufacture is itself a call on energy. Nothing in this topic has the cell making its own fuel."),
 ("Water is the product, or emission, of a fuel cell",
  "ENG-3.P.1 states this in so many words and names water twice, once in the reaction and once as the emission. Carbon monoxide belongs to burning biomass in topic 6.7 and the framework does name an emission rather than withholding one."),
 ("fossil fuel yields carbon dioxide and water; a fuel cell yields water alone",
  "ENG-3.E.1 states that the combustion of fossil fuels YIELDS CARBON DIOXIDE AND WATER, while ENG-3.P.1 names WATER as the product of a fuel cell. One rejected option is the exact swap of those two, so the anchor carries both halves."),
 ("Low environmental impact, and no carbon dioxide provided the hydrogen is produced from water",
  "ENG-3.Q.1 grants low environmental impact and no carbon dioxide WHEN THE HYDROGEN IS PRODUCED FROM WATER, and in the same breath calls the technology expensive. One rejected option is the same advantage with the condition removed, so the anchor carries the condition."),
 ("technology is expensive, and that making the hydrogen gas itself takes energy",
  "ENG-3.Q.1's two reservations are the expense of the technology and the energy still needed to create the hydrogen gas. Carbon monoxide belongs to burning biomass in topic 6.7 and hydrogen sulfide to geothermal energy in 6.10."),
 ("energy spent producing a quantity of hydrogen and setting it beside the electricity",
  "ENG-3.Q.1 says energy is still needed to create the hydrogen gas, which is a claim about energy spent before the cell is used, so it is tested by comparing that investment with what comes back. Water and oxygen measured at the cell bear on ENG-3.P.1 instead."),
 ("across the whole chain, recorded together with how the hydrogen was produced",
  "ENG-3.Q.1 conditions its claim on the hydrogen being PRODUCED FROM WATER, so the source of the hydrogen is part of what the claim is about and has to be recorded with the carbon dioxide. Water, cost and oxygen bear on other parts of this topic."),
 ("Hydrogen and oxygen enter, water leaves, and no carbon dioxide is involved",
  "Recomputed in q19 above: hydrogen in at 4 units an hour and oxygen at 2, water out at 4, and the carbon dioxide row zero on both sides. ENG-3.P.1 has the cell combining hydrogen and oxygen from the air to form water and release electricity."),
 ("Water, the only substance leaving the cell",
  "Recomputed in q20 above: water is the only row with a figure above zero in the leaving column. ENG-3.P.1 states that WATER IS THE PRODUCT, or emission, OF A FUEL CELL, and the hydrogen and oxygen are what enter."),
 ("One unit of water for each unit of hydrogen",
  "Recomputed in q21 above: four units of hydrogen in and four units of water out. The rejected values take the oxygen row for the hydrogen row, invert the ratio, quote a whole hour's output as a ratio, or deny an output the record shows."),
 ("where the hydrogen is produced from water, which is the condition the framework attaches",
  "Recomputed in q22 above: 0 kilograms of carbon dioxide for each unit of hydrogen by the route from water against 28 from a fossil fuel. ENG-3.Q.1 makes its claim WHEN THE HYDROGEN IS PRODUCED FROM WATER, and one rejected option keeps the reading and drops the condition, so the anchor carries both."),
 ("still needed to create the hydrogen gas, whichever way it is produced",
  "Recomputed in q23 above: 55 energy units for each unit of hydrogen from water and 40 from a fossil fuel, so neither route is free of the call on energy. ENG-3.Q.1 states that energy is still needed to create the hydrogen gas and exempts neither route."),
 ("15 energy units",
  "Recomputed in q24 above: 55 minus 40 energy units for each unit of hydrogen. The rejected values quote one route alone, add the two, or invert the comparison the record shows."),
 ("releases no carbon dioxide with hydrogen from water, but its equipment costs the more",
  "Recomputed in q25 above: 0 kilograms for each unit of distance against 0.9, with equipment at 72 thousand currency units for each vehicle against 24. ENG-3.Q.1 grants the absence of carbon dioxide when the hydrogen comes from water and calls the technology expensive in the same statement, so the anchor carries both halves."),
 ("Three times as much",
  "Recomputed in q26 above: 72 divided by 24 thousand currency units for each vehicle. The rejected values quote a wrong division, shift the answer by a power of ten, or invert the comparison the record shows."),
 ("energy is still needed to create the hydrogen gas used in the fuel cell",
  "Recomputed in q27 above: 100 energy units invested in creating the hydrogen against 62 returned as electricity. ENG-3.Q.1 states that energy is still needed to create the hydrogen gas, and a chain that spends more than it returns is what that reservation describes."),
 ("62 percent",
  "Recomputed in q28 above: 62 of the 100 energy units invested. The rejected values take the share lost rather than the share returned, assume nothing is lost, halve the answer, or claim a return the record does not show."),
 ("38 energy units",
  "Recomputed in q29 above: 100 minus 62 energy units. The rejected values quote the electricity delivered, halve the answer, quote the investment, or deny a shortfall the record plainly shows."),
 ("no carbon dioxide when the hydrogen is produced from water, but the technology is expensive",
  "The keyed summary carries ENG-3.P.1 and ENG-3.Q.1 in the framework's own terms, including the condition on the carbon dioxide claim and both reservations. Each rejected summary introduces steam or a turbine, drops the condition, claims a class the framework never assigns, or names the wrong gas from the air."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_11_mutant")
        mod.TOPIC = e6_11.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_11.QUESTIONS)
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

    print("selftest: the unmodified module must pass before any mutation is tried")
    run_on(copy.deepcopy(e6_11.QUESTIONS))

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
    must_fail("q19 carbon dioxide made to leave the cell", edit(19, CO2, OUT, "3"))
    must_fail("q20 a second substance made to leave the cell", edit(20, H2, OUT, "1"))
    must_fail("q21 water output moved off one for one", edit(21, H2O, OUT, "8"))
    must_fail("q22 the route from water given carbon dioxide",
              edit(22, FROMWATER, MADECO2, "12"))
    must_fail("q23 one route made to need no energy", edit(23, FROMFOSSIL, INVEST, "0"))
    must_fail("q24 gap moved off 15 energy units", edit(24, FROMWATER, INVEST, "60"))
    must_fail("q25 the fuel cell fleet given carbon dioxide",
              edit(25, CELLFLEET, PERDIST, "0.4"))
    must_fail("q26 ratio moved off three", edit(26, CELLFLEET, KIT, "96"))
    must_fail("q27 the chain made to return more than was invested",
              edit(27, DELIVERSTEP, STEPENERGY, "130"))
    must_fail("q28 returned share moved off 62 percent",
              edit(28, DELIVERSTEP, STEPENERGY, "70"))
    must_fail("q29 shortfall moved off 38 energy units", edit(29, MAKESTEP, STEPENERGY, "110"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_11.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_11, CLAIMS, TABLE_CHECKS)
