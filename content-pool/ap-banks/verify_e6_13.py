"""Key audit for AP ENVIRONMENTAL SCIENCE 6.13 Energy Conservation.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.T.1  Some of the methods for conserving energy around a home include
             adjusting the thermostat to reduce the use of heat and air
             conditioning, conserving water, use of energy-efficient
             appliances, and conservation landscaping.
                          -- items 1, 2, 3, 4, 5, 6, 17, 18, 19, 20, 21
  ENG-3.T.2  Methods for conserving energy on a large scale include improving
             fuel economy for vehicles, using BEVs (battery electric vehicles)
             and hybrid vehicles, using public transportation, and implementing
             green building design features.
                          -- items 7, 8, 9, 10, 11, 13, 22, 23, 24, 25, 26, 27,
                             28, 29
  items 12, 14, 15, 16 and 30 rest on both.

ONE ITEM WAS CUT AND REPLACED. A draft item keyed the hedge in SOME OF THE
METHODS ... INCLUDE; e6_4 q5 and e9_9 q17 already ask that of SUCH AS in their
own statements, and its keyed choice was almost word for word theirs. It scored
only 0.41 against them on a token signature, which is well under any reject
line and is exactly why the threshold decides what to READ rather than what to
accept. It is replaced by item 12, which keys something true of this topic
alone: of the eight named methods only the thermostat carries a stated purpose.

THE FRAMEWORK GIVES NO NUMBER AND NO RANKING. Two statements, eight named
methods, not one figure and no claim that any method saves more than another.
That is the single easiest thing to get wrong in this topic, and it is why item
21 exists: the four home methods are ranked in the record printed with the
question and the keyed choice says in so many words that the ranking is the
record's rather than the framework's. Items 17 and 18 are the pair that makes
the point -- the method saving the largest QUANTITY and the method saving the
largest SHARE are different methods, and neither ordering comes from the CED.

SCALE IS THE AXIS THE ITEMS TURN ON. Two of the eight methods sit where a
student does not expect: CONSERVING WATER is a home method and GREEN BUILDING
DESIGN FEATURES is a large-scale one. Items 3, 5, 7, 10, 11, 13 and 14 key which
list a method is on, and wherever a distractor is the exact swap of the key --
items 11, 14, 15 and 30 -- the anchor carries BOTH clauses, because either
clause alone matches the swap as well as the key.

CONSERVING IS NOT GENERATING, and item 16 holds that boundary against ENG-3.R.1,
where a wind turbine spins a generator PRODUCING ELECTRICITY. Neither ENG-3.T.1
nor ENG-3.T.2 names a single energy source, which is what item 15 keys.

BOUNDARY WITH 5.13, checked against the CED rather than assumed: STB-1.B.1 names
increased use of public transportation too, but as a method to INCREASE WATER
INFILTRATION alongside permeable pavement and tree planting. Item 10's keyed
choice therefore says public transportation is named on one energy list, not on
none and not on two, and items 3 and 5 use permeable pavement and infiltration
tree planting as distractors precisely because they belong to that other list.

DATA ITEMS: 17 to 29, recomputed below from those tables alone and
calculator-free, in keeping with the topic's suggested skill 6.C, calculate an
accurate numeric answer with appropriate units.

NEGATIVE CONTROL: ``e_check.run`` corrupts a key, an anchor, a choice, a
``why``, the notation, a figure reference and every table in turn BEFORE the
real gate runs, and it is not behind a flag. ``python3 verify_e6_13.py
--selftest`` adds the stronger property: for each of the thirteen data items a
SINGLE CELL is edited so that the keyed conclusion becomes false, and each edit
must be caught. Two further controls swap a pair of COLUMNS, which moves no
value at all and only exchanges what each column counts -- the corruption a
check that reads the right cells for the wrong reason survives.

EVERY MUTATION BELOW WAS CONFIRMED TO CONTRADICT THE KEY IT TARGETS. A control
that cannot fail is worse than none: in verify_e2_1.py one lowered a count that
had already fallen as far as it could, and while gating 6.12 one gave a wind
farm a carbon dioxide figure in a check about replenishment. Both passed
silently and proved nothing.
"""
import e_check
import cg_check as cg
import e6_13

BEFORE_H = "Energy that part used in the year before the method (energy units)"
WITH_H = "Energy that part used in the year with the method (energy units)"
THERMO = "Heating and air conditioning, thermostat adjusted"
APPLI = "Appliances, replaced with energy-efficient ones"
WATER = "Heating and pumping water, water use reduced"
LAND = "Grounds around the house, conservation landscaping"

DIST = "Distance travelled in the year (distance units)"
FUEL = "Fuel used in that year (fuel units)"

TOTALE = "Energy the journey uses in total (energy units)"
PAX = "Passengers carried"
CAR = "One person driving a car alone"
BUS = "A bus"
TRAIN = "A train"

USE = "Energy the building used in the year (thousand energy units)"
PRE = "Before the design features"
YR1 = "First year after the design features"
YR2 = "Second year after the design features"


# ------------------------------------------------------------------- one home

def _savings(table):
    """Energy saved on each part of the home's use, by row label."""
    return {lab: cg.cell(table, lab, BEFORE_H) - cg.cell(table, lab, WITH_H)
            for lab in cg.labels(table)}


def _shares(table):
    """Share of its own former use each method saved, by row label."""
    return {lab: (cg.cell(table, lab, BEFORE_H) - cg.cell(table, lab, WITH_H))
            / cg.cell(table, lab, BEFORE_H)
            for lab in cg.labels(table)}


def q17(table, item):
    saved = _savings(table)
    best = max(saved, key=saved.get)
    assert best == THERMO, f"the thermostat must be the largest saving; got {best}"
    assert saved[THERMO] == 600, f"the thermostat saving recomputes to {saved[THERMO]}, not 600"
    assert saved[APPLI] == 400, f"the appliance saving recomputes to {saved[APPLI]}, not 400"
    assert saved[WATER] == 120, f"the water saving recomputes to {saved[WATER]}, not 120"
    assert saved[LAND] == 80, f"the landscaping saving recomputes to {saved[LAND]}, not 80"
    assert len(set(saved.values())) == len(saved), "'all four saved the same amount' must be false"
    return (f"the four savings recompute to {[int(v) for v in saved.values()]} energy units, so "
            "the thermostat saved the most of the four")


def q18(table, item):
    shares = _shares(table)
    saved = _savings(table)
    best_share = max(shares, key=shares.get)
    assert best_share == APPLI, f"the appliances must save the largest share; got {best_share}"
    for lab, want in ((THERMO, 0.15), (APPLI, 0.20), (WATER, 0.10), (LAND, 0.10)):
        assert abs(shares[lab] - want) < 1e-9, \
            f"the share for {lab!r} recomputes to {shares[lab]}, not {want}"
    assert best_share != max(saved, key=saved.get), \
        "the largest share and the largest quantity must be different methods, or the item is empty"
    return (f"the shares recompute to {[round(v * 100) for v in shares.values()]} percent, so the "
            "largest share belongs to the appliances and the largest quantity does not")


def q19(table, item):
    before = sum(cg.col(table, BEFORE_H))
    after = sum(cg.col(table, WITH_H))
    total = before - after
    assert total == 1200, f"the total saved recomputes to {total}, not 1,200 energy units"
    saved = _savings(table)
    for wrong in (max(saved.values()), after, before, total - min(saved.values())):
        assert total != wrong, f"the {wrong} distractor equals the key"
    return (f"{before:.0f} energy units before the methods and {after:.0f} with them is "
            f"{total:.0f} energy units saved across the four parts")


def q20(table, item):
    before = sum(cg.col(table, BEFORE_H))
    share = (before - sum(cg.col(table, WITH_H))) / before
    assert abs(share - 0.15) < 1e-9, f"the share recomputes to {share}, not 15 percent"
    for wrong in (1 - share, max(_shares(table).values()), min(_shares(table).values())):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"the saving is {share * 100:.0f} percent of the {before:.0f} energy units the home "
            "used before the methods")


def q21(table, item):
    labs = [cg.normalize(lab) for lab in cg.labels(table)]
    # normalize() KEEPS the hyphen, so the framework's "energy-efficient" must be
    # matched with the hyphen. Searching for "energy efficient" found nothing and
    # the checker, not the module, was what had to change.
    for method in ("thermostat", "energy-efficient", "water", "conservation landscaping"):
        hits = [lab for lab in labs if method in lab]
        assert len(hits) == 1, \
            f"exactly one part must be the framework's {method!r} method; got {hits}"
    saved = _savings(table)
    assert len(set(saved.values())) > 1, \
        "the savings must differ, or the record adds no ranking for the framework to lack"
    return (f"the four parts carry the four methods ENG-3.T.1 names around a home, and their "
            f"savings of {[int(v) for v in saved.values()]} energy units differ, so the record "
            "ranks what the framework leaves unranked")


# ------------------------------------------------------------------- the fleet

def _economy(table):
    """Distance travelled for each unit of fuel, by vehicle."""
    return {lab: cg.cell(table, lab, DIST) / cg.cell(table, lab, FUEL)
            for lab in cg.labels(table)}


def q22(table, item):
    dists = cg.col(table, DIST)
    assert len(set(dists)) == 1, \
        f"every vehicle must travel the same distance for the stem to hold; got {dists}"
    econ = _economy(table)
    best = max(econ, key=econ.get)
    assert best == "Vehicle 4", f"Vehicle 4 must have the best economy; got {best}"
    assert econ[best] == 50, f"the best economy recomputes to {econ[best]}, not 50"
    assert econ["Vehicle 1"] == 20, \
        f"Vehicle 1's economy recomputes to {econ['Vehicle 1']}, not 20"
    assert len(set(econ.values())) == len(econ), \
        "'all four are equal' must be false, or equal distances would make the item empty"
    return (f"dividing distance by fuel gives {[int(v) for v in econ.values()]} distance units for "
            f"each fuel unit over an identical {dists[0]:.0f} distance units travelled")


def q23(table, item):
    saved = cg.cell(table, "Vehicle 1", FUEL) - cg.cell(table, "Vehicle 4", FUEL)
    assert saved == 360, f"the saving recomputes to {saved}, not 360 fuel units"
    for wrong in (cg.cell(table, "Vehicle 1", FUEL),
                  cg.cell(table, "Vehicle 1", FUEL) + cg.cell(table, "Vehicle 4", FUEL),
                  cg.cell(table, "Vehicle 4", FUEL),
                  0):
        assert saved != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, 'Vehicle 1', FUEL):.0f} minus "
            f"{cg.cell(table, 'Vehicle 4', FUEL):.0f} is {saved:.0f} fuel units over the same "
            "distance")


def q24(table, item):
    best = max(_economy(table).values())
    total_distance = sum(cg.col(table, DIST))
    need = total_distance / best
    actual = sum(cg.col(table, FUEL))
    assert need == 960, f"the fleet would need {need} fuel units, not 960"
    for wrong in (actual, actual - need, min(cg.col(table, FUEL)), total_distance / 20):
        assert need != wrong, f"the {wrong} distractor equals the key"
    return (f"{total_distance:.0f} distance units at the best economy of {best:.0f} distance units "
            f"for each fuel unit is {need:.0f} fuel units, against {actual:.0f} actually used")


def q25(table, item):
    heads = [cg.normalize(h) for h in table["headers"]]
    assert any("distance travelled" in h for h in heads), "no column records distance travelled"
    assert any("fuel used" in h for h in heads), "no column records fuel used"
    for banned in ("passenger", "building", "water", "thermostat", "appliance"):
        for h in heads:
            assert banned not in h, f"column {h!r} would point the record at another method"
    econ = _economy(table)
    assert len(set(econ.values())) > 1, \
        "the economies must differ, or the record shows nothing to improve"
    return ("the record carries a distance column and a fuel column and nothing else, which is "
            f"exactly what a fuel economy is computed from; the economies read "
            f"{[int(v) for v in econ.values()]}")


# ----------------------------------------------------------------- one journey

def _per_passenger(table):
    return {lab: cg.cell(table, lab, TOTALE) / cg.cell(table, lab, PAX)
            for lab in cg.labels(table)}


def q26(table, item):
    per = _per_passenger(table)
    least = min(per, key=per.get)
    assert least == TRAIN, f"the train must use the least for each passenger; got {least}"
    assert per[TRAIN] == 8, f"the train recomputes to {per[TRAIN]}, not 8 for each passenger"
    assert per[BUS] == 12, f"the bus recomputes to {per[BUS]}, not 12 for each passenger"
    assert per[CAR] == 60, f"the car recomputes to {per[CAR]}, not 60 for each passenger"
    assert cg.cell(table, TRAIN, TOTALE) == max(cg.col(table, TOTALE)), \
        "the train must use the most in total, or the item's trap does not exist"
    return (f"dividing each journey's energy by its passengers gives {per[CAR]:.0f} for the car, "
            f"{per[BUS]:.0f} for the bus and {per[TRAIN]:.0f} for the train, while the train's "
            "total is the largest of the three")


def q27(table, item):
    per = _per_passenger(table)
    gap = per[CAR] - per[BUS]
    assert gap == 48, f"the difference recomputes to {gap}, not 48 energy units"
    for wrong in (per[BUS], per[CAR], per[CAR] - per[TRAIN],
                  cg.cell(table, BUS, TOTALE) - cg.cell(table, CAR, TOTALE)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{per[CAR]:.0f} energy units for the person driving alone minus {per[BUS]:.0f} for "
            f"each bus passenger is {gap:.0f} energy units")


# ---------------------------------------------------------------- one building

def _stages(table):
    labs = cg.labels(table)
    assert labs == [PRE, YR1, YR2], f"the record must run in stage order; got {labs}"
    return cg.col(table, USE)


def q28(table, item):
    use = _stages(table)
    assert all(use[i + 1] < use[i] for i in range(len(use) - 1)), \
        f"the building's yearly use must fall across the record; got {use}"
    for h in [cg.normalize(x) for x in table["headers"]]:
        for banned in ("vehicle", "fuel", "landscap"):
            assert banned not in h, f"column {h!r} would point the record at another method"
    return (f"the building's yearly use runs {[int(u) for u in use]} thousand energy units, "
            "falling at each stage after the design features")


def q29(table, item):
    use = _stages(table)
    share = (use[0] - use[-1]) / use[0]
    assert abs(share - 0.20) < 1e-9, f"the fall recomputes to {share}, not 20 percent"
    for wrong in (1 - share,
                  (use[0] - use[1]) / use[0],
                  (use[0] - use[-1]) / use[-1],
                  share / 2):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{use[0]:.0f} falling to {use[-1]:.0f} thousand energy units is a fall of "
            f"{use[0] - use[-1]:.0f}, which is {share * 100:.0f} percent of the starting figure")


CLAIMS = [
 ("reduce the use of heat and air conditioning",
  "ENG-3.T.1 names ADJUSTING THE THERMOSTAT TO REDUCE THE USE OF HEAT AND AIR CONDITIONING first among the methods for conserving energy around a home. Adjusting it the other way increases exactly what the statement asks to reduce, and no larger unit, open window or relocated thermostat appears anywhere in the framework."),
 ("use of heat and air conditioning",
  "ENG-3.T.1 supplies a purpose for this method and for no other in either list: the thermostat is adjusted TO REDUCE THE USE OF HEAT AND AIR CONDITIONING. Lighting, hot water and solid waste appear nowhere in the statement, and vehicle fuel belongs to ENG-3.T.2's large-scale list."),
 ("Conserving water",
  "ENG-3.T.1 lists CONSERVING WATER among the methods for conserving energy around a home and explains no further. Replacing traditional pavement with permeable pavement is STB-1.B.1 in topic 5.13, a method to increase water infiltration rather than to conserve energy."),
 ("appliances is among the methods for conserving energy around a home",
  "ENG-3.T.1 names USE OF ENERGY-EFFICIENT APPLIANCES among its home methods, while ENG-3.T.2's large-scale list names vehicles, public transportation and green building design. The framework sets no replacement interval and never claims an efficient appliance uses more energy."),
 ("around a home, with no description of what it involves",
  "ENG-3.T.1 ends its home list with CONSERVATION LANDSCAPING and describes it no further, so any definition offered for it comes from outside the framework. Planting trees so that rainwater soaks in is STB-1.B.1 in topic 5.13, and the framework ranks no method against another."),
 ("using energy-efficient appliances, and conservation landscaping",
  "ENG-3.T.1's four home methods are adjusting the thermostat, conserving water, use of energy-efficient appliances, and conservation landscaping. Public transportation and the whole of one rejected set belong to ENG-3.T.2, a wind turbine appears in neither list, and the fourth method is named rather than absent."),
 ("conserving energy on a large scale",
  "ENG-3.T.2 opens with IMPROVING FUEL ECONOMY FOR VEHICLES among the methods for conserving energy on a large scale, and ENG-3.T.1's home list names the thermostat, water, appliances and landscaping instead. Increasing water infiltration is STB-1.B.1 in topic 5.13, and improving fuel economy generates no electricity."),
 ("one of the named methods, and nothing about how they work",
  "ENG-3.T.2 names USING BEVs (BATTERY ELECTRIC VEHICLES) AND HYBRID VEHICLES and says nothing further about either kind, so it neither describes them nor prefers one to the other. Hydrogen combined with oxygen from the air is ENG-3.P.1's fuel cell in topic 6.11, hybrids are named separately in the same clause, and the framework ranks nothing."),
 ("two kinds rather than one",
  "ENG-3.T.2 joins BEVs and hybrid vehicles with AND in a single clause, which names two kinds rather than defining one by the other. Dropping either leaves the clause incomplete, and public transportation is a further item in the same list rather than the only one."),
 ("names public transportation for each of those two purposes",
  "ENG-3.T.2 names USING PUBLIC TRANSPORTATION among the methods for conserving energy on a large scale, and STB-1.B.1 in topic 5.13 names increased use of public transportation among the methods to increase water infiltration. Two statements, two purposes; neither attaches a condition about the size of the place, and both were read in the CED rather than recalled."),
 ("on its large-scale list, not among the home methods",
  "ENG-3.T.2 ends with IMPLEMENTING GREEN BUILDING DESIGN FEATURES while ENG-3.T.1's home list stops at conservation landscaping. One rejected option is the exact reversal of those two lists, so the anchor carries both clauses, and the framework plainly gives two lists rather than one."),
 ("thermostat, which is adjusted to reduce",
  "ENG-3.T.1 writes ADJUSTING THE THERMOSTAT TO REDUCE THE USE OF HEAT AND AIR CONDITIONING, and that clause is the only purpose either statement supplies for any of the eight named methods. Each rejected option supplies a purpose that is reasonable and that the framework does not give, which is the whole trap: conserving water, energy-efficient appliances, public transportation and green building design features are named and left unexplained."),
 ("using public transportation, and implementing green building design features",
  "ENG-3.T.2's four large-scale methods are improving fuel economy for vehicles, using battery electric and hybrid vehicles, using public transportation, and implementing green building design features. Conserving water belongs to ENG-3.T.1, and nuclear power, wind turbines and fuel cells are the subject of topics 6.6, 6.12 and 6.11."),
 ("Conserving water around a home; improving fuel economy on a large scale",
  "ENG-3.T.1 names conserving water among the home methods and ENG-3.T.2 names improving fuel economy for vehicles among the large-scale ones. One rejected pairing is the exact exchange of the two, so the anchor carries both halves rather than either alone."),
 ("methods for conserving energy, and neither names a source of energy",
  "ENG-3.T.1 and ENG-3.T.2 between them name a thermostat setting, water use, appliances, landscaping, fuel economy, two kinds of vehicle, public transportation and building design, and not one of the eight is a source of energy. The sources are the subject of topics 6.3 to 6.12, and one rejected option is the exact reversal of the key."),
 ("a turbine produces electricity rather than conserving energy",
  "ENG-3.T.1 names four home methods and a turbine is not among them, and ENG-3.T.2 does not name one either. ENG-3.R.1 in topic 6.12 has a wind turbine spin a generator PRODUCING ELECTRICITY, which is generation; both statements here are about using less of the energy already drawn, and one rejected option shares the first clause and moves the turbine to the other list."),
 ("saved 600 energy units",
  "Recomputed in q17 above: the four parts saved 600, 400, 120 and 80 energy units in the year. ENG-3.T.1 names all four methods and ranks none of them, so the ordering here belongs to the record and not to the framework."),
 ("Replacing the appliances, at 20 percent",
  "Recomputed in q18 above: the shares of each part's former use are 15, 20, 10 and 10 percent, so the largest share and the largest quantity belong to different methods. Every rejected option states its own method's share correctly and is simply not the largest of the four."),
 ("1,200 energy units",
  "Recomputed in q19 above: 8,000 energy units before the methods against 6,800 with them. The rejected values quote the largest single saving, one of the two column totals, or a sum that leaves out the smallest of the four methods."),
 ("15 percent",
  "Recomputed in q20 above: 1,200 energy units saved out of the 8,000 used before the methods. The rejected values quote the share saved on one part of the home's use rather than on the whole of it, quote the share still used, or deny an arithmetic the record plainly allows."),
 ("around a home, and the record adds a ranking the framework itself does not give",
  "Recomputed in q21 above: the four parts carry the thermostat, energy-efficient appliances, conserving water and conservation landscaping, which are exactly ENG-3.T.1's four home methods, and their savings differ. The framework gives no figure and no ranking anywhere in this topic, so the ordering is the record's."),
 ("Vehicle 4, at 50 distance units",
  "Recomputed in q22 above: over an identical distance the four vehicles return 20, 30, 40 and 50 distance units for each fuel unit. Equal distances make the fuel column the whole of the comparison rather than making the four vehicles equal, and each rejected option crosses a vehicle with the wrong economy."),
 ("360 fuel units",
  "Recomputed in q23 above: 600 minus 240 fuel units over the same distance. The rejected values quote one vehicle alone, add the two, or treat equal distances as equal fuel, which is what ENG-3.T.2's improving fuel economy for vehicles denies."),
 ("960 fuel units",
  "Recomputed in q24 above: 48,000 distance units at the best economy of 50 distance units for each fuel unit. The rejected values quote what the fleet actually used, the difference between the two, one vehicle's own figure, or what the fleet would need at the worst economy rather than the best."),
 ("Improving fuel economy for vehicles",
  "Recomputed in q25 above: the record carries a distance column and a fuel column and nothing else, which is exactly what a fuel economy is computed from. ENG-3.T.2 names improving fuel economy for vehicles, and no column here counts passengers, buildings or water."),
 ("8 energy units for each passenger, which supports using public transportation",
  "Recomputed in q26 above: 60 energy units for each passenger by car, 12 by bus and 8 by train, while the train's total for the journey is the largest of the three. ENG-3.T.2 names USING PUBLIC TRANSPORTATION among the large-scale methods, and conserving water is on the other list."),
 ("48 energy units",
  "Recomputed in q27 above: 60 energy units for the person driving alone against 12 for each bus passenger. The rejected values quote one of the two amounts, take the train's figure instead of the bus's, or subtract the journey totals without dividing by the passengers carried."),
 ("Green building design features, and the building's yearly use fell",
  "Recomputed in q28 above: the building used 500, then 410, then 400 thousand energy units. ENG-3.T.2 names implementing green building design features among the large-scale methods, landscaping is a home method, and fuel economy concerns vehicles; one rejected option keeps the method and inverts the direction, so the anchor carries both clauses."),
 ("20 percent",
  "Recomputed in q29 above: 500 falling to 400 thousand energy units is a fall of 100, a fifth of the starting figure. The rejected values stop at the first year, divide by the final figure rather than the starting one, halve the fall, or quote the share still used."),
 ("conservation landscaping; on a large scale they are improving fuel economy",
  "The keyed summary carries ENG-3.T.1 and ENG-3.T.2 in the framework's own terms, both lists complete and each on its own scale. Each rejected summary exchanges the two lists, invents a ranking the framework never gives, denies the large-scale list, or moves ways of generating electricity onto it."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """One cell at a time, each edit chosen to make the keyed sentence false."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_13_mutant")
        mod.TOPIC = e6_13.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_13.QUESTIONS)
        mutate(qs)
        try:
            run_on(qs)
        except AssertionError as exc:
            print(f"  control OK  {label}: {str(exc)[:88]}")
            return
        raise SystemExit(f"CONTROL FAILED: {label} did not raise")

    def edit(qi, row_label, header, value):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(header))
            hit = 0
            for r in t["rows"]:
                if cg.normalize(r[0]) == cg.normalize(row_label):
                    r[j] = value
                    hit += 1
            assert hit == 1, f"the mutation for q{qi} matched {hit} rows, so it changes nothing"
            qs[qi - 1]["table"] = t
        return mutate

    def rename_row(qi, row_label, new_label):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            hit = 0
            for r in t["rows"]:
                if cg.normalize(r[0]) == cg.normalize(row_label):
                    r[0] = new_label
                    hit += 1
            assert hit == 1, f"the mutation for q{qi} matched {hit} rows, so it changes nothing"
            qs[qi - 1]["table"] = t
        return mutate

    def rename_header(qi, header, new_header):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(header))
            t["headers"][j] = new_header
            qs[qi - 1]["table"] = t
        return mutate

    def swap_columns(qi, left, right):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            heads = [cg.normalize(h) for h in t["headers"]]
            a, b = heads.index(cg.normalize(left)), heads.index(cg.normalize(right))
            for r in t["rows"]:
                r[a], r[b] = r[b], r[a]
            qs[qi - 1]["table"] = t
        return mutate

    print("selftest: the unmodified module must pass before any mutation is tried")
    run_on(copy.deepcopy(e6_13.QUESTIONS))

    print("selftest: one cell at a time, against the keyed number")
    must_fail("q17 the appliances made the largest saving", edit(17, APPLI, WITH_H, "1,000"))
    must_fail("q18 the appliance share dropped below the thermostat's",
              edit(18, APPLI, WITH_H, "1,800"))
    must_fail("q19 total saved moved off 1,200 energy units", edit(19, WATER, WITH_H, "1,000"))
    must_fail("q20 share moved off 15 percent of the home's use",
              edit(20, THERMO, BEFORE_H, "6,000"))
    must_fail("q21 a home method replaced by one from the other list",
              rename_row(21, LAND, "Vehicles, replaced with hybrid ones"))
    must_fail("q22 the best economy moved to another vehicle", edit(22, "Vehicle 4", FUEL, "800"))
    must_fail("q23 saving moved off 360 fuel units", edit(23, "Vehicle 1", FUEL, "500"))
    must_fail("q24 fleet requirement moved off 960 fuel units",
              edit(24, "Vehicle 4", FUEL, "200"))
    must_fail("q25 the fuel column changed to count passengers",
              rename_header(25, FUEL, "Passengers carried in that year"))
    must_fail("q26 the bus made the smallest for each passenger", edit(26, TRAIN, PAX, "100"))
    must_fail("q27 difference moved off 48 energy units", edit(27, BUS, TOTALE, "600"))
    must_fail("q28 the building's use made to rise under the features",
              edit(28, YR2, USE, "600"))
    must_fail("q29 fall moved off 20 percent", edit(29, YR2, USE, "450"))

    # A column swap moves no value at all: it only exchanges what each column
    # counts. A check that reads the right cells for the wrong reason survives a
    # single edited number and does not survive this.
    print("selftest: a column swap, which moves no value but changes what each counts")
    must_fail("q17 the before and with columns exchanged",
              swap_columns(17, BEFORE_H, WITH_H))
    must_fail("q22 the distance and fuel columns exchanged", swap_columns(22, DIST, FUEL))
    must_fail("q26 the energy and passenger columns exchanged", swap_columns(26, TOTALE, PAX))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_13.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_13, CLAIMS, TABLE_CHECKS)
