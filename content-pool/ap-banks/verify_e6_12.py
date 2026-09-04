"""Key audit for AP ENVIRONMENTAL SCIENCE 6.12 Wind Energy.

e6_12.py was written by an agent that was stopped before it wrote this file, so
the module stood in the tree with NO GATE AT ALL. Everything below was written
against the module afterwards: every key was re-derived from the CED, every
anchor is pinned to a distinctive substring of its own keyed choice, and every
table is recomputed from the table alone.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.R.1  Wind turbines use the kinetic energy of moving air to spin a
             turbine, which spins a generator, producing electricity.
                          -- items 1, 2, 3, 4, 5, 14, 17, 18, 19, 20
  ENG-3.S.1  Wind energy is a renewable, clean source of energy. However, birds
             and bats may be killed if they fly into the spinning turbine
             blades.
                          -- items 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 21, 22,
                             23, 24, 25, 26, 27, 28, 29
  item 30 restates both.

THE HARM IS NARROW AND HEDGED, and three items key those three restrictions
separately: MAY (a possible outcome, not a certain one, item 8), BIRDS AND BATS
(two named groups and no others, item 9), and THE SPINNING TURBINE BLADES (that
part of the machine and not the tower, item 10). No key overstates any of them,
and item 26 keys that the framework sets no order between the two groups even
where a record shows one outnumbering the other.

WIND IS THE ONE SOURCE IN THIS UNIT WITH NO COST CLAIM. ENG-3.K.1 calls solar
expensive, ENG-3.M.1 calls hydroelectric construction expensive, ENG-3.O.1 calls
the cost of accessing geothermal energy prohibitively expensive and ENG-3.Q.1
calls fuel cell technology expensive; nothing anywhere calls wind energy
anything of the kind. Item 16 keys that absence and every distractor there
quotes a real cost claim attached to a DIFFERENT source, so a student who
transfers one is caught. Item 29 supplies a cost from a trial record and its
claim says in so many words that the figure comes from the record rather than
from the framework.

CROSS-REFERENCES CHECKED AGAINST THE CED, not against memory: ENG-3.E.2 (the
fossil fuel sequence burns fuel to raise steam before its turbine, item 14),
ENG-3.A.2 (renewable means replenished naturally at or near the rate of
consumption, which is why it is the claim about SUPPLY, items 15 and 22),
ENG-3.F.1 (volatile organic compounds belong to fracking), ENG-3.M.1 (the loss
of or change in habitats follows the construction of DAMS).

DATA ITEMS: 17 to 29, recomputed below from those tables alone and
calculator-free.

TWO DEFECTS THIS GATE CAUGHT ON ITS FIRST RUN, both of them the kind only a
structural check finds: "Renewable and clean" sat inside the distractor
"Nonrenewable and clean" as a substring, and "40 energy units, the same at every
site where the air is moving" sat inside "240 energy units, the same at every
site ...". A student who accepts the shorter option has no ground to reject the
longer. Both distractors were rewritten. Neither key moved.

NEGATIVE CONTROL: ``e_check.run`` corrupts a key, an anchor, a choice, a
``why``, the notation, a figure reference and every table in turn, BEFORE the
real gate runs, and it is not behind a flag. ``python3 verify_e6_12.py
--selftest`` adds the stronger property: for each of the thirteen data items, a
SINGLE CELL is edited so that the keyed conclusion becomes false, and each edit
must be caught.

WHY THE PER-CELL EDITS EXIST RATHER THAN A REVERSAL. Reversing every numeric
column of the four-site wind speed record reverses the speed column and the
output column together, so every site keeps the pair of numbers it had and the
record still says exactly what it said. A reversal control on that table CANNOT
fail and would prove nothing -- the same shape of empty control that had to be
replaced in verify_e2_1.py. The selftest below therefore moves one cell at a
time, and each mutation is chosen to make the keyed sentence false.
"""
import e_check
import cg_check as cg
import e6_12

SPEED = "Average wind speed at the hub (speed units)"
OUT = "Electricity the turbine delivers each day (energy units)"

POLL = "Air pollutants released for each unit of electricity (grams)"
CO2E = "Carbon dioxide released for each unit of electricity (kilograms)"
WIND, COAL = "Wind farm", "Coal plant"

NTURB = "Turbines standing in the array"
BIRDS = "Birds found killed at the array in a year"
BATS = "Bats found killed at the array in a year"

DEATHS = "Birds and bats found killed in a year"
DELIV = "Electricity delivered in a year (thousand energy units)"
BEFORE = "Before the measure"
YEAR1 = "First year with the measure"
YEAR2 = "Second year with the measure"


# ---------------------------------------------------------------- the wind record

def _sites(table):
    """(speed, output) for every site, ordered by speed."""
    return sorted(zip(cg.col(table, SPEED), cg.col(table, OUT)))


def _rate(table):
    """Energy units delivered for each unit of wind speed, where the air moves."""
    moving = [(s, o) for s, o in _sites(table) if s > 0]
    assert moving, "no site records moving air, so no rate exists"
    rates = {o / s for s, o in moving}
    assert len(rates) == 1, f"the output for each unit of speed is not constant; got {rates}"
    return rates.pop()


def q17(table, item):
    pairs = _sites(table)
    still = [o for s, o in pairs if s == 0]
    assert still, "one site must record still air, or the keyed clause has nothing to rest on"
    assert still[0] == 0, f"the still site must deliver nothing; got {still[0]}"
    assert all(pairs[i + 1][1] > pairs[i][1] for i in range(len(pairs) - 1)), \
        f"output must rise with wind speed; got {pairs}"
    assert pairs[-1][1] == max(o for _, o in pairs), \
        "'the turbine delivers less where the air moves faster' must be false"
    assert still[0] != max(o for _, o in pairs), \
        "'most of all where the air is still' must be false"
    assert len({o for _, o in pairs}) == len(pairs), \
        "'the same amount at every site' must be false"
    return (f"sorted by wind speed the outputs read {[o for _, o in pairs]} energy units, "
            "strictly increasing from nothing at the still site")


def q18(table, item):
    rate = _rate(table)
    assert rate == 60, f"the rate recomputes to {rate}, not 60 energy units for each speed unit"
    for wrong in (40, 240, 0):
        assert rate != wrong, f"the {wrong} distractor equals the key"
    return (f"dividing output by wind speed at each moving site gives {rate:.0f} energy units for "
            "each speed unit, the same at all three of them")


def q19(table, item):
    rate = _rate(table)
    expected = rate * 7
    assert expected == 420, f"seven speed units recomputes to {expected}, not 420 energy units"
    for wrong in [o for _, o in _sites(table)] + [700]:
        assert expected != wrong, f"the {wrong} distractor equals the key"
    return (f"{rate:.0f} energy units for each speed unit times seven speed units is "
            f"{expected:.0f} energy units a day")


def q20(table, item):
    moving = [o for s, o in _sites(table) if s > 0]
    gap = max(moving) - min(moving)
    assert gap == 300, f"the gap recomputes to {gap}, not 300 energy units"
    for wrong in (max(moving), max(moving) + min(moving), 180, 120):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{max(moving):.0f} minus {min(moving):.0f} is {gap:.0f} energy units more a day at "
            "the windiest site than at the slowest site where the air still moves")


# ------------------------------------------------------------- what is released

def _emission_headers(table):
    """Both measured columns must be about what is RELEASED, and nothing else."""
    measured = [cg.normalize(h) for h in table["headers"][1:]]
    assert measured, "the record must measure something"
    for h in measured:
        assert "released" in h, f"column {h!r} is not a record of what is released"
    for banned in ("replenish", "consumption", "supply", "bird", "bat", "turbine", "cost"):
        for h in measured:
            assert banned not in h, f"column {h!r} measures more than what is released"
    return measured


def q21(table, item):
    _emission_headers(table)
    assert cg.cell(table, WIND, POLL) == 0, "the wind farm must release no air pollutants"
    assert cg.cell(table, WIND, CO2E) == 0, "the wind farm must release no carbon dioxide"
    assert cg.cell(table, COAL, POLL) > cg.cell(table, WIND, POLL), \
        "'the wind farm releases more air pollutants than the coal plant' must be false"
    assert cg.cell(table, COAL, CO2E) > cg.cell(table, WIND, CO2E), \
        "'the two release the same amounts' must be false"
    return (f"the wind farm reads {cg.cell(table, WIND, POLL):.0f} grams of air pollutants and "
            f"{cg.cell(table, WIND, CO2E):.0f} kilograms of carbon dioxide for each unit of "
            f"electricity against the coal plant's {cg.cell(table, COAL, POLL):.0f} and "
            f"{cg.cell(table, COAL, CO2E)}")


def q22(table, item):
    measured = _emission_headers(table)
    # The claim about what is released IS tested by this record, which is what
    # makes the untested claim the other one.
    assert cg.cell(table, WIND, POLL) == 0 and cg.cell(table, COAL, POLL) > 0, \
        "the record must separate the two on what they release, or nothing here is tested"
    assert len(measured) == 2, f"the record must measure exactly the two emissions; got {measured}"
    return (f"the record carries {len(measured)} columns and both of them count what is released, "
            f"with the wind farm at {cg.cell(table, WIND, POLL):.0f} grams against the coal "
            f"plant's {cg.cell(table, COAL, POLL):.0f}, so nothing here bears on replenishment")


# ------------------------------------------------------------------ the wildlife

def _arrays(table):
    """(turbines, birds, bats) for every array, ordered by size."""
    return sorted(zip(cg.col(table, NTURB), cg.col(table, BIRDS), cg.col(table, BATS)))


def q23(table, item):
    rows = _arrays(table)
    for n, birds, bats in rows:
        assert birds > 0, f"the array of {n:.0f} turbines records no birds killed"
        assert bats > 0, f"the array of {n:.0f} turbines records no bats killed"
    assert all(rows[i + 1][1] > rows[i][1] for i in range(len(rows) - 1)), \
        f"bird counts must rise with the size of the array; got {rows}"
    assert all(rows[i + 1][2] > rows[i][2] for i in range(len(rows) - 1)), \
        f"bat counts must rise with the size of the array; got {rows}"
    for h in [cg.normalize(x) for x in table["headers"]]:
        assert "pollutant" not in h, "no column may record air pollutants; the framework calls wind clean"
    return (f"every array records deaths in both groups, birds {[b for _, b, _ in rows]} and bats "
            f"{[b for _, _, b in rows]}, rising together with the {[n for n, _, _ in rows]} "
            "turbines standing")


def q24(table, item):
    rows = _arrays(table)
    bird_rates = {round(birds / n, 6) for n, birds, _ in rows}
    bat_rates = {round(bats / n, 6) for n, _, bats in rows}
    assert bird_rates == {1.4}, f"the bird rate recomputes to {bird_rates}, not 1.4 for each turbine"
    assert bat_rates == {2.2}, f"the bat rate recomputes to {bat_rates}, not 2.2 for each turbine"
    assert bird_rates != bat_rates, "the 2.2 distractor is the bat rate and must not equal the key"
    assert 14 not in bird_rates, "the 14 distractor is a whole array's count, not a rate"
    return (f"dividing birds by turbines at each array gives {sorted(bird_rates)}, the same "
            f"everywhere, against a bat rate of {sorted(bat_rates)}")


def q25(table, item):
    n, birds, bats = _arrays(table)[-1]
    total = birds + bats
    assert total == 360, f"the total recomputes to {total}, not 360"
    for wrong in (birds, bats, bats - birds, bats / 2):
        assert total != wrong, f"the {wrong} distractor equals the key"
    return (f"at the largest array, the one with {n:.0f} turbines, {birds:.0f} birds plus "
            f"{bats:.0f} bats is {total:.0f} animals in a year")


def q26(table, item):
    rows = _arrays(table)
    for n, birds, bats in rows:
        assert bats > birds, \
            f"bats must outnumber birds at the array of {n:.0f} turbines; got {bats} against {birds}"
    assert any(bats != birds for _, birds, bats in rows), \
        "'the record shows equal numbers of the two' must be false"
    return (f"bats outnumber birds at every array, {[b for _, _, b in rows]} against "
            f"{[b for _, b, _ in rows]}, which is the reading the keyed answer sets aside")


# ------------------------------------------------------------------- the trial

def _stages(table):
    labs = cg.labels(table)
    assert labs == [BEFORE, YEAR1, YEAR2], f"the trial must run in stage order; got {labs}"
    return cg.col(table, DEATHS), cg.col(table, DELIV)


def q27(table, item):
    deaths, _ = _stages(table)
    assert all(deaths[i + 1] < deaths[i] for i in range(len(deaths) - 1)), \
        f"the count of deaths must fall across the trial; got {deaths}"
    for h in [cg.normalize(x) for x in table["headers"]]:
        for banned in ("pollutant", "carbon", "waste"):
            assert banned not in h, f"column {h!r} would give the measure something else to address"
    return (f"the yearly count of birds and bats killed runs {[int(d) for d in deaths]} across the "
            "trial, and no column of the record counts anything else the measure could address")


def q28(table, item):
    deaths, _ = _stages(table)
    fall = deaths[0] - deaths[-1]
    assert fall == 240, f"the fall recomputes to {fall}, not 240"
    for wrong in (deaths[0], deaths[0] + deaths[-1], deaths[0] - deaths[1], deaths[1] - deaths[-1]):
        assert fall != wrong, f"the {wrong} distractor equals the key"
    return (f"{deaths[0]:.0f} minus {deaths[-1]:.0f} is a fall of {fall:.0f} birds and bats a year "
            "from before the measure to the second year with it")


def q29(table, item):
    _, deliv = _stages(table)
    cost = deliv[0] - deliv[-1]
    assert cost == 35, f"the cost recomputes to {cost}, not 35 thousand energy units"
    assert cost > 0, "'the output was unchanged' must be false"
    for wrong in (deliv[0] - deliv[1], deliv[0], deliv[-1]):
        assert cost != wrong, f"the {wrong} distractor equals the key"
    return (f"{deliv[0]:.0f} minus {deliv[-1]:.0f} is {cost:.0f} thousand energy units of "
            "electricity given up over the year the measure ran")


CLAIMS = [
 ("kinetic energy of moving air",
  "ENG-3.R.1 opens by stating that WIND TURBINES USE THE KINETIC ENERGY OF MOVING AIR. The energy is the energy of motion rather than heat or chemical bonds; moving water is hydroelectric power in ENG-3.L.1 and light from the sun is solar energy in topic 6.8."),
 ("spins a turbine",
  "ENG-3.R.1 has the kinetic energy of moving air spin A TURBINE, and the generator comes after the turbine in the framework's own order. Turning a source directly into electrical energy without either part appears nowhere in this topic."),
 ("spins a generator, which produces the electricity",
  "ENG-3.R.1 states that the turbine SPINS A GENERATOR, PRODUCING ELECTRICITY, so the two parts are separate and the electricity comes from the second. Steam belongs to ENG-3.E.2 and no storage appears anywhere in this topic."),
 ("spins a turbine, the turbine spins a generator",
  "ENG-3.R.1 gives the whole sequence in one sentence: moving air, turbine, generator, electricity. One rejected sequence exchanges the turbine and the generator, so the anchor carries both of those clauses rather than either alone."),
 ("turbine spins a generator, and the generator is what produces",
  "ENG-3.R.1 assigns the production of electricity to the GENERATOR that the turbine spins, so a claim that the blades make it is corrected by naming the generator. One rejected option reverses which part spins which, so the anchor carries both halves."),
 ("Renewable and clean",
  "ENG-3.S.1 states that WIND ENERGY IS A RENEWABLE, CLEAN SOURCE OF ENERGY, and those are the two words it uses. The framework says nothing anywhere about what wind energy costs, and the same statement goes on to name a risk to birds and bats."),
 ("killed if they fly into the spinning turbine blades",
  "ENG-3.S.1 states that BIRDS AND BATS MAY BE KILLED IF THEY FLY INTO THE SPINNING TURBINE BLADES. The same statement calls wind energy clean, so no air pollutant is involved, and the loss of or change in habitats after a dam is built is ENG-3.M.1 in topic 6.9."),
 ("possible rather than certain",
  "ENG-3.S.1 says birds and bats MAY BE KILLED IF THEY FLY INTO THE SPINNING TURBINE BLADES. MAY asserts a possible outcome under a condition, not a certain one, and the statement restricts the risk to neither one of the two animal groups nor to any location."),
 ("Birds and bats",
  "ENG-3.S.1 names BIRDS AND BATS and no other animals. Adding insects or fish goes beyond the statement and dropping either named group leaves it incomplete; the framework names no harm to fish anywhere in this unit."),
 ("spinning blades",
  "ENG-3.S.1 puts the collision at THE SPINNING TURBINE BLADES. The tower, the generator housing and the cables appear nowhere in the clause, and the part involved is named rather than left open."),
 ("names only the risk to birds and bats",
  "ENG-3.S.1 calls wind energy a RENEWABLE, CLEAN SOURCE OF ENERGY and then names one effect, the risk to birds and bats. Volatile organic compounds belong to fracking in ENG-3.F.1, and the statement does make a claim about wind rather than withholding one."),
 ("Collisions of birds and bats",
  "ENG-3.S.1 names exactly one effect of wind energy, and it is birds and bats flying into the spinning blades, so that is what a response to the framework's concern must address. The same statement calls wind energy clean, and no statement gives a turbine waste, water use or carbon dioxide in operation."),
 ("Counting the birds and bats found killed",
  "ENG-3.S.1's effect is that birds and bats may be killed at the spinning blades, so a count of those deaths is the observation that bears on it. Emissions, output, cost and wind speed each belong to a different claim or to no claim in this topic."),
 ("spinning a generator; only the fossil fuel sequence burns a fuel to raise steam first",
  "ENG-3.R.1 runs moving air, turbine, generator, electricity, while ENG-3.E.2 runs burning, heat, steam, turbine, generator, electricity. The turbine and the generator are common to both; the combustion and the steam belong only to the fossil fuel account, and one rejected option is the exact swap, so the anchor carries both clauses."),
 ("Renewable is the claim about supply; clean is the claim about what is released",
  "ENG-3.A.2 makes a renewable source one REPLENISHED NATURALLY, AT OR NEAR THE RATE OF CONSUMPTION, which is a claim about supply, while calling a source clean is a claim about what its use puts out. ENG-3.S.1 applies both words to wind energy in one sentence, and one rejected option exchanges them, so the anchor carries both halves."),
 ("makes no claim about what wind energy costs",
  "ENG-3.R.1 describes the machinery and ENG-3.S.1 gives two adjectives and one risk; neither mentions cost. Each rejected option quotes a cost claim the framework really does make about a DIFFERENT source, ENG-3.K.1 for solar, ENG-3.M.1 for hydroelectric construction, ENG-3.O.1 for geothermal access and ENG-3.Q.1 for fuel cell technology."),
 ("moves faster, and nothing at all where the air is still",
  "Recomputed in q17 above: sorted by wind speed the outputs read 0, 240, 360 and 540 energy units. ENG-3.R.1 makes the KINETIC ENERGY OF MOVING AIR what drives the turbine, so still air drives nothing; one rejected option keeps the first clause and inverts the second, so the anchor carries both."),
 ("60 energy units",
  "Recomputed in q18 above: 240 over 4, 360 over 6 and 540 over 9 all give 60 energy units for each unit of wind speed. The rejected values pair one site's output with another site's speed, or quote a whole day's output as though it were a rate."),
 ("420 energy units",
  "Recomputed in q19 above: 60 energy units for each speed unit, times seven speed units. The rejected values quote a neighbouring site's whole output, multiply the speed by a round hundred, or quote the slowest moving site."),
 ("300 energy units",
  "Recomputed in q20 above: 540 minus 240 energy units a day. The rejected values quote the windiest site alone, add the two, or take one of the steps between adjacent sites."),
 ("Clean, since the wind farm releases neither air pollutants",
  "Recomputed in q21 above: the wind farm reads 0 grams of air pollutants and 0 kilograms of carbon dioxide for each unit of electricity against the coal plant's 310 and 0.95. ENG-3.S.1 calls wind energy a RENEWABLE, CLEAN SOURCE, and a record of what is released speaks to the second of those two words rather than the first."),
 ("renewable, because a record of what is released says nothing about whether the source is replenished",
  "Recomputed in q22 above: both measured columns of the record count what is released, and they do separate the two ways of generating. ENG-3.A.2 defines a renewable source by comparing a rate of replenishment with a rate of consumption, which is not a quantity this record holds."),
 ("birds and bats may be killed if they fly into the spinning turbine blades",
  "Recomputed in q23 above: every array records deaths in both groups, 14 birds and 22 bats at the smallest and 140 and 220 at the largest. ENG-3.S.1 names BIRDS AND BATS together, and the same statement calls wind energy clean, so no air pollutant is involved."),
 ("1.4 birds for each turbine",
  "Recomputed in q24 above: 14 over 10, 56 over 40 and 140 over 100 all give 1.4 birds for each turbine. The rejected values quote the bat rate of 2.2, quote a whole array's count as a rate, or deny an arithmetic the record plainly allows."),
 ("360",
  "Recomputed in q25 above: at the array of 100 turbines, 140 birds plus 220 bats. The rejected values quote one column alone, take the difference between the two, or halve the larger of them."),
 ("names birds and bats together without ranking them",
  "Recomputed in q26 above: bats outnumber birds at every array, 22 against 14, 88 against 56 and 220 against 140. ENG-3.S.1 names BIRDS AND BATS together and sets no order between them, so which group is the larger does not alter what the framework asserts."),
 ("killing of birds and bats",
  "Recomputed in q27 above: the yearly count of deaths runs 360, 150 and 120 across the trial, and the record holds no column of pollutants, carbon dioxide or waste. ENG-3.S.1 names the deaths of birds and bats at the spinning blades as the one effect of wind energy."),
 ("By 240",
  "Recomputed in q28 above: 360 minus 120 in a year. The rejected values quote the opening count, add the two ends, or take one of the two steps within the trial rather than the whole fall."),
 ("35 thousand energy units",
  "Recomputed in q29 above: 900 minus 865 thousand energy units delivered in a year. The framework names no cost for wind energy, so this figure comes from the trial record rather than from ENG-3.S.1, and the rejected values take the first year's step alone, quote one reading, or deny a fall the record shows."),
 ("birds and bats may be killed if they fly into the spinning blades",
  "The keyed summary carries ENG-3.R.1 and ENG-3.S.1 in the framework's own terms: the sequence from moving air to generator, both adjectives, and the hedged risk to birds and bats. Each rejected summary introduces steam, reverses the classification, drops the wildlife clause, moves the electricity into the blades, or adds a cost claim the framework never makes about wind."),
]

TABLE_CHECKS = {17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
                24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """One cell at a time, each edit chosen to make the keyed sentence false."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_12_mutant")
        mod.TOPIC = e6_12.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_12.QUESTIONS)
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

    def rename_header(qi, header, new_header):
        def mutate(qs):
            t = copy.deepcopy(qs[qi - 1]["table"])
            j = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(header))
            t["headers"][j] = new_header
            qs[qi - 1]["table"] = t
        return mutate

    print("selftest: the unmodified module must pass before any mutation is tried")
    run_on(copy.deepcopy(e6_12.QUESTIONS))

    print("selftest: one cell at a time, against the keyed number")
    must_fail("q17 the still site made the biggest producer", edit(17, "Site 1", OUT, "700"))
    must_fail("q18 rate moved off 60 energy units a speed unit", edit(18, "Site 3", OUT, "300"))
    must_fail("q19 the rate broken, so 420 no longer follows", edit(19, "Site 4", SPEED, "10"))
    must_fail("q20 gap moved off 300 energy units", edit(20, "Site 2", OUT, "300"))
    must_fail("q21 the wind farm given air pollutants", edit(21, WIND, POLL, "50"))
    # q22's key is that this record CANNOT bear on replenishment, and what
    # settles that is what the columns COUNT. The first control written here
    # gave the wind farm a carbon dioxide figure; it did not fire, and it should
    # not have -- a record of emissions still says nothing about replenishment
    # whatever the emissions are, so the mutation left the keyed sentence true.
    # The check was right and the control was empty. Renaming a column so the
    # record does carry replenishment is the mutation that actually contradicts
    # the key.
    must_fail("q22 a column changed to count replenishment rather than emissions",
              rename_header(22, CO2E, "Share of the source replenished each year (percent)"))
    must_fail("q23 one array made to kill no bats", edit(23, "Array 2", BATS, "0"))
    must_fail("q24 bird rate moved off 1.4 for each turbine", edit(24, "Array 2", BIRDS, "60"))
    must_fail("q25 total at the largest array moved off 360", edit(25, "Array 3", BATS, "200"))
    must_fail("q26 birds made to outnumber bats at one array", edit(26, "Array 1", BATS, "10"))
    must_fail("q27 the deaths made to rise under the measure", edit(27, YEAR2, DEATHS, "400"))
    must_fail("q28 fall moved off 240 deaths", edit(28, BEFORE, DEATHS, "400"))
    must_fail("q29 cost moved off 35 thousand energy units", edit(29, YEAR2, DELIV, "800"))

    # A column swap, which is a different corruption from moving one number: it
    # keeps every value in the record and only exchanges what they count.
    def swap_bird_bat(qs, qi):
        t = copy.deepcopy(qs[qi - 1]["table"])
        jb = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(BIRDS))
        jt = [cg.normalize(h) for h in t["headers"]].index(cg.normalize(BATS))
        for r in t["rows"]:
            r[jb], r[jt] = r[jt], r[jb]
        qs[qi - 1]["table"] = t

    print("selftest: a column swap, which moves no value but changes what each counts")
    must_fail("q24 the bird and bat columns exchanged", lambda qs: swap_bird_bat(qs, 24))
    must_fail("q26 the bird and bat columns exchanged", lambda qs: swap_bird_bat(qs, 26))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_12.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_12, CLAIMS, TABLE_CHECKS)
