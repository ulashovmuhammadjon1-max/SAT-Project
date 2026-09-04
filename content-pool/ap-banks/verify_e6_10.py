"""Key audit for AP ENVIRONMENTAL SCIENCE 6.10 Geothermal Energy.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor, so an off-by-one key or a reordered choice
list fails here rather than reaching a student.

WHAT THE KEYS REST ON
---------------------
  ENG-3.N.1  Geothermal energy is obtained by using the heat stored in the
             Earth's interior to heat up water, which is brought back to the
             surface as steam. The steam is used to drive an electric generator.
                     -- items 1, 2, 3, 4, 5, 6, 7, 15, 16, 19, 20, 21
  ENG-3.O.1  The cost of accessing geothermal energy can be prohibitively
             expensive, as is not easily accessible in many parts of the world.
             In addition, it can cause the release of hydrogen sulfide.
                     -- items 8, 9, 10, 11, 12, 13, 17, 18, 22, 23, 24, 25, 26,
                        27, 28, 29
  item 14 keys what the framework does NOT supply, and item 30 restates both.

THE FRAMEWORK NAMES NO ADVANTAGE FOR GEOTHERMAL ENERGY, and item 14 keys that
rather than inventing one. Wind gets two adjectives in ENG-3.S.1, solar two in
ENG-3.K.1, hydroelectricity a denial of air pollution and waste in ENG-3.M.1;
geothermal energy gets a process and three drawbacks. The distractors on that
item are the advantages the framework grants to the other four sources, so a
student who transfers one is caught by the item rather than by nothing.

NO FUEL IS BURNED. The heat is STORED IN THE EARTH'S INTERIOR. The steam in this
statement looks exactly like the steam in ENG-3.E.2 and ENG-3.G.1 and the source
of the heat is the whole difference, so items 6, 15 and 16 key it and item 16's
anchor carries both sources because one distractor is their exact swap.

BOTH HEDGES ARE KEYED. The cost CAN BE prohibitively expensive and the plant CAN
CAUSE the release of hydrogen sulfide; the accessibility clause carries no
hedge. Item 12 keys what PROHIBITIVELY adds beyond merely high, and item 13 keys
the two hedges without extending either to the unhedged clause.

DATA ITEMS: 19 to 29, recomputed below from those tables alone.

TWO TABLES SURVIVE A COLUMN REVERSAL with their pairs intact -- the region
survey's (depth, cost) and the sampling record's (distance, concentration) --
so every check that reads them also pins its rows BY ROW LABEL. Without that,
the cost for each thousand meters, the extreme difference and the falling
gradient would all be unchanged by a reversal.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
``python3 verify_e6_10.py --selftest`` adds the stronger property that a
REVERSAL ALONE is caught for every table, and it establishes the clean pass
BEFORE any mutation, so a standing defect cannot hide behind the controls.
"""
import e_check
import cg_check as cg
import e6_10

AVAIL = "Energy still available at that stage (energy units)"
ROCK = "Heat drawn from the hot rock below"
STEAM = "Heat carried by the steam at the surface"
GEN = "Electricity leaving the generator"
CHAIN = [ROCK, STEAM, GEN]

DEPTH = "Depth to rock hot enough to raise steam (meters)"
DRILL = "Cost of drilling to that depth (million currency units)"
G1, G2, G3 = "Region 1", "Region 2", "Region 3"

KM = "Distance from the geothermal plant (kilometers)"
H2S = "Hydrogen sulfide in the air (parts per billion)"
PT1, PT2, PT3, PT4 = "Point 1", "Point 2", "Point 3", "Point 4"

SDEPTH = "Depth to the hot rock (meters)"
PROJECT = "Cost of the whole project (million currency units)"
FUNDS = "Funds the community can raise (million currency units)"
SITEA, SITEB = "Site A", "Site B"


def _stages(table):
    labs = cg.labels(table)
    assert labs == CHAIN, f"the record must run rock, steam, generator; got {labs}"
    return [cg.cell(table, lab, AVAIL) for lab in CHAIN]


def q19(table, item):
    vals = _stages(table)
    assert all(vals[i] > vals[i + 1] for i in range(2)), \
        f"the energy still available must fall at every step; got {vals}"
    return (f"the record runs {CHAIN} with {vals} energy units still available, the sequence "
            "ENG-3.N.1 gives and falling at every step")


def q20(table, item):
    vals = _stages(table)
    share = vals[2] / vals[0]
    assert abs(share - 0.15) < 1e-9, f"the share recomputes to {share}, not 15 percent"
    for wrong in (vals[1] / vals[0], 1 - vals[1] / vals[0], 1 - share, 1.0):
        assert abs(share - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"{vals[2]:.0f} of the {vals[0]:.0f} energy units drawn from the rock leaves as "
            f"electricity, which is {share * 100:.0f} percent")


def q21(table, item):
    vals = _stages(table)
    loss = vals[0] - vals[1]
    assert loss == 280, f"the loss recomputes to {loss}, not 280 energy units"
    for wrong in (vals[0] - vals[2], vals[1] - vals[2], vals[1], vals[2]):
        assert loss != wrong, f"the {wrong} distractor equals the key"
    return (f"{vals[0]:.0f} minus {vals[1]:.0f} is {loss:.0f} energy units lost between the hot "
            "rock and the steam reaching the surface")


def _pin_regions(table):
    """The shallowest region must be the first, by ROW LABEL.

    Reversing this table's two numeric columns leaves the (depth, cost) pairs
    exactly as they were, so the cost for each thousand meters and the
    difference between the extremes both survive a reversal. Naming the rows is
    what a reversal breaks.
    """
    depths = cg.col(table, DEPTH)
    assert cg.cell(table, G1, DEPTH) == min(depths), "the first region must be the shallowest"
    assert cg.cell(table, G3, DEPTH) == max(depths), "the third region must be the deepest"


def q22(table, item):
    _pin_regions(table)
    depths = [cg.cell(table, g, DEPTH) for g in (G1, G2, G3)]
    costs = [cg.cell(table, g, DRILL) for g in (G1, G2, G3)]
    assert all(depths[i] < depths[i + 1] for i in range(2)), f"depth must rise; got {depths}"
    assert all(costs[i] < costs[i + 1] for i in range(2)), \
        f"cost must rise with depth, not fall; got {costs}"
    assert max(depths) > 5 * min(depths), \
        "the regions must differ widely enough for 'not easily accessible in many parts' to read"
    return (f"the depth to usable rock runs {depths} meters and the drilling cost {costs} million "
            "currency units, so what is shallow and cheap in one region is deep and dear in "
            "another")


def _cost_rate(table):
    _pin_regions(table)
    rates = [cg.cell(table, g, DRILL) / (cg.cell(table, g, DEPTH) / 1000) for g in (G1, G2, G3)]
    assert len(set(round(r, 9) for r in rates)) == 1, \
        f"the cost for each thousand meters must be the same in all three regions; got {rates}"
    return rates[0]


def q23(table, item):
    rate = _cost_rate(table)
    assert rate == 5, f"the rate recomputes to {rate}, not 5 million currency units"
    for wrong in (cg.cell(table, G1, DRILL), cg.cell(table, G2, DRILL)):
        assert rate != wrong, f"the {wrong} distractor equals the key"
    return (f"cost divided by depth gives {rate:.0f} million currency units for each thousand "
            "meters in every one of the three regions")


def q24(table, item):
    _pin_regions(table)
    gap = cg.cell(table, G3, DRILL) - cg.cell(table, G1, DRILL)
    assert gap == 26, f"the gap recomputes to {gap}, not 26 million currency units"
    for wrong in (cg.cell(table, G3, DRILL),
                  cg.cell(table, G3, DRILL) + cg.cell(table, G1, DRILL),
                  cg.cell(table, G3, DRILL) - cg.cell(table, G2, DRILL),
                  cg.cell(table, G2, DRILL)):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{cg.cell(table, G3, DRILL):.0f} minus {cg.cell(table, G1, DRILL):.0f} is "
            f"{gap:.0f} million currency units more to drill in the deepest region")


def _pin_points(table):
    """The nearest sampling point must be the first, by ROW LABEL.

    Reversing this table leaves the (distance, concentration) pairs untouched,
    so the falling gradient and the extreme difference both survive one.
    """
    km = cg.col(table, KM)
    assert cg.cell(table, PT1, KM) == min(km), "the first point must be the nearest to the plant"
    assert cg.cell(table, PT4, KM) == max(km), "the fourth point must be the farthest away"


def q25(table, item):
    _pin_points(table)
    conc = [cg.cell(table, p, H2S) for p in (PT1, PT2, PT3, PT4)]
    assert all(conc[i] > conc[i + 1] for i in range(3)), \
        f"the concentration must fall with distance; got {conc}"
    assert max(conc) > 0, "'the gas was not detected anywhere' must be false"
    return (f"hydrogen sulfide reads {conc} parts per billion at "
            f"{[cg.cell(table, p, KM) for p in (PT1, PT2, PT3, PT4)]} kilometers, falling with "
            "distance from the plant")


def q26(table, item):
    _pin_points(table)
    conc = [cg.cell(table, p, H2S) for p in (PT1, PT2, PT3, PT4)]
    assert conc[0] == max(conc), "the reading must be highest at the nearest point"
    assert conc[-1] == min(conc), "the reading must be lowest at the farthest point"
    assert len(set(conc)) == 4, "'the reading is the same at all four points' must be false"
    assert min(conc) > 0, "'the reading is zero everywhere' must be false"
    return (f"the readings run {conc} parts per billion with distance rising, so the gas is "
            "concentrated where the plant is and thins steadily away from it")


def q27(table, item):
    _pin_points(table)
    conc = {p: cg.cell(table, p, H2S) for p in (PT1, PT2, PT3, PT4)}
    gap = conc[PT1] - conc[PT4]
    assert gap == 178, f"the gap recomputes to {gap}, not 178 parts per billion"
    for wrong in (conc[PT1], conc[PT1] + conc[PT4], conc[PT1] - conc[PT2], conc[PT3] - conc[PT4]):
        assert gap != wrong, f"the {wrong} distractor equals the key"
    return (f"{conc[PT1]:.0f} minus {conc[PT4]:.0f} is {gap:.0f} parts per billion more hydrogen "
            "sulfide at the nearest point than at the farthest")


def q28(table, item):
    cost = {s: cg.cell(table, s, PROJECT) for s in (SITEA, SITEB)}
    money = {s: cg.cell(table, s, FUNDS) for s in (SITEA, SITEB)}
    assert money[SITEA] == money[SITEB], "the community's funds must be the same at both sites"
    assert cost[SITEB] > money[SITEB], "the second site must cost more than the community can raise"
    assert cost[SITEA] < money[SITEA], \
        "the first site must be within reach, so 'both sites' and 'the first site' are false"
    assert cg.cell(table, SITEB, SDEPTH) > cg.cell(table, SITEA, SDEPTH), \
        "'the second site is the shallower' must be false"
    return (f"the second site costs {cost[SITEB]:.0f} million currency units against the "
            f"{money[SITEB]:.0f} million the community can raise, while the first costs "
            f"{cost[SITEA]:.0f} million")


def q29(table, item):
    cost = {s: cg.cell(table, s, PROJECT) for s in (SITEA, SITEB)}
    money = cg.cell(table, SITEB, FUNDS)
    over = cost[SITEB] - money
    assert over == 8, f"the excess recomputes to {over}, not 8 million currency units"
    assert cost[SITEB] > cost[SITEA], "the dearer project must be the second site"
    for wrong in (cost[SITEB], cost[SITEB] + money, money - cost[SITEA], money - 5):
        assert over != wrong, f"the {wrong} distractor equals the key"
    return (f"{cost[SITEB]:.0f} minus {money:.0f} is {over:.0f} million currency units by which "
            "the dearer project exceeds the funds available")


CLAIMS = [
 ("In the Earth's interior",
  "ENG-3.N.1 states that geothermal energy is obtained by using THE HEAT STORED IN THE EARTH'S INTERIOR. Fuel rods belong to nuclear power in topic 6.6, chemical energy in a fuel to fossil fuels in 6.5, and a heated tank to an active solar system in 6.8."),
 ("Heat up water",
  "ENG-3.N.1 states that the stored heat is used TO HEAT UP WATER. Splitting atoms is fission in topic 6.6, and warming a building directly with no equipment is a passive solar system in topic 6.8."),
 ("As steam",
  "ENG-3.N.1 states that the water IS BROUGHT BACK TO THE SURFACE AS STEAM. The statement plainly has the water returning, and nothing in it is burned or frozen."),
 ("Drive an electric generator",
  "ENG-3.N.1 ends by stating that THE STEAM IS USED TO DRIVE AN ELECTRIC GENERATOR. Heating a liquid for storage is an active solar system in topic 6.8, and steam is a working fluid rather than a fuel."),
 ("heats water, the water returns to the surface as steam, and the steam drives an electric generator",
  "ENG-3.N.1 gives the whole sequence in one sentence. Each rejected sequence reverses two steps, sends the water the wrong way, or introduces a fuel the statement does not have, so the anchor carries the steps rather than one link."),
 ("heat comes from the Earth's interior, and nothing is burned",
  "ENG-3.N.1 makes the source THE HEAT STORED IN THE EARTH'S INTERIOR, which is neither a combustion nor a fission. Sunlight absorbed at the surface is solar energy in topic 6.8, and the framework certainly does name the source."),
 ("heat first heats water, which returns as steam and drives an electric generator",
  "ENG-3.N.1 puts water and steam between the stored heat and the generator. Transforming energy directly into electricity is what photovoltaic cells do in topic 6.8, and storing energy in a tank is an active solar system there."),
 ("That it can be prohibitively expensive",
  "ENG-3.O.1 states that THE COST OF ACCESSING GEOTHERMAL ENERGY CAN BE PROHIBITIVELY EXPENSIVE. The word can makes it a possibility rather than a universal, and the framework does make the claim rather than withholding it."),
 ("not easily accessible in many parts of the world",
  "ENG-3.O.1 states this in so many words. The availability of sunlight limits photovoltaic cells in topic 6.8 rather than geothermal energy, and no region of the world is singled out by the statement."),
 ("Hydrogen sulfide",
  "ENG-3.O.1 ends by stating that geothermal energy CAN CAUSE THE RELEASE OF HYDROGEN SULFIDE. Volatile organic compounds belong to fracking in topic 6.5, hazardous solid waste to nuclear power in 6.6, and nitrogen oxides to burning biomass in 6.7."),
 ("production of hazardous solid waste",
  "ENG-3.O.1 names a prohibitively expensive cost, poor accessibility in many parts of the world, and the possible release of hydrogen sulfide. Hazardous solid waste is what ENG-3.G.4 attaches to nuclear power, and every rejected option restates one of the three drawbacks the framework does give."),
 ("high enough to prevent access altogether, not merely high",
  "A prohibitive cost is one that stops the thing being done, so ENG-3.O.1's phrase makes the expense a barrier to access rather than a large number. Nothing in the statement concerns law, timing, or a comparison with other sources."),
 ("prohibitive cost and the release of hydrogen sulfide are possible rather than certain",
  "ENG-3.O.1 hedges both of those clauses with CAN BE and CAN CAUSE. The accessibility clause carries no hedge and is not restricted to shallow rock, so the hedges are not extended to it here."),
 ("None; it describes the process and then names three drawbacks",
  "ENG-3.N.1 explains how geothermal energy is obtained and ENG-3.O.1 gives cost, accessibility and hydrogen sulfide. The rejected options quote the advantages the framework grants to wind in ENG-3.S.1, hydroelectricity in ENG-3.M.1, solar energy in ENG-3.K.1 and biomass in ENG-3.I.1, so a student who transfers one is caught here."),
 ("all three, heat turns water into steam and the steam drives the generation of electricity",
  "ENG-3.N.1, ENG-3.E.2 and ENG-3.G.1 all run through steam on the way to electricity. Only the fossil fuel account burns a fuel, only the nuclear account splits atoms, and transforming light directly is photovoltaic solar energy in topic 6.8."),
 ("geothermal heat is already stored in the Earth's interior; the fossil fuel heat is released by a chemical reaction",
  "ENG-3.N.1 uses THE HEAT STORED IN THE EARTH'S INTERIOR while ENG-3.E.1 makes combustion A CHEMICAL REACTION BETWEEN THE FUEL AND OXYGEN that releases energy. One rejected option is the exact swap of the two sources, so the anchor carries both halves."),
 ("Measuring hydrogen sulfide in the air around a working geothermal plant",
  "ENG-3.O.1 names the release of hydrogen sulfide, so measuring that gas around a plant is what bears on it. Depth and drilling cost bear on the accessibility and cost clauses, and steam temperature and plant counts on neither."),
 ("across many regions, how deep one must drill to reach rock hot enough",
  "ENG-3.O.1 says geothermal energy is NOT EASILY ACCESSIBLE IN MANY PARTS OF THE WORLD, which is a claim about how the resource varies from place to place, so the observation must cover many regions. Hydrogen sulfide bears on the third clause and the rest on neither."),
 ("own: heat from the rock, then steam at the surface, then electricity from the generator",
  "Recomputed in q19 above: 1,000, 720 and 150 energy units still available at the three stages, falling throughout. ENG-3.N.1 gives exactly that sequence."),
 ("15 percent",
  "Recomputed in q20 above: 150 of the 1,000 energy units drawn from the rock. The rejected values quote the intermediate stage, take the share lost rather than the share delivered, or assume nothing is lost."),
 ("280 energy units",
  "Recomputed in q21 above: 1,000 minus 720 energy units. The rejected values take the whole loss across the plant, take the later step, or quote the energy remaining rather than the amount lost."),
 ("not easily accessible in many parts of the world, and that the cost of access can be prohibitively",
  "Recomputed in q22 above: depths of 800, 2,400 and 6,000 meters against drilling costs of 4, 12 and 30 million currency units. ENG-3.O.1 names both the accessibility and the cost, and the anchor carries both because one rejected option keeps the data reading and drops the second clause."),
 ("5 million currency units, the same in all three regions",
  "Recomputed in q23 above: 4 over 800, 12 over 2,400 and 30 over 6,000 meters all give the same rate. The rejected values quote a whole project cost or deny an arithmetic the record plainly allows."),
 ("26 million currency units",
  "Recomputed in q24 above: 30 minus 4 million currency units, with the deepest and shallowest regions identified by row. The rejected values quote the deepest region alone, add the two, take the step between the two deeper regions, or quote the middle region's cost."),
 ("can cause the release of hydrogen sulfide",
  "Recomputed in q25 above: 180 parts per billion half a kilometer from the plant falling to 2 at twenty-five kilometers. ENG-3.O.1 states that geothermal energy CAN CAUSE THE RELEASE OF HYDROGEN SULFIDE, and the gas measured is that one."),
 ("highest closest to the plant and falls steadily with distance from it",
  "Recomputed in q26 above: readings of 180, 60, 8 and 2 parts per billion at rising distances, with the nearest point identified by row. A gradient pointing at one place is what ties a release to a source."),
 ("178 parts per billion higher",
  "Recomputed in q27 above: 180 minus 2 parts per billion. The rejected values quote the nearest point alone, add the two, or take one of the steps between adjacent points."),
 ("second site, because the project would cost more than the community can raise",
  "Recomputed in q28 above: 28 million currency units against 20 million available, while the first site costs 5 million. ENG-3.O.1 calls the cost of access PROHIBITIVELY expensive, which is a cost that stops the project rather than merely a large one. One rejected option gives the correct ground for the wrong site, so the anchor carries both."),
 ("By 8 million currency units",
  "Recomputed in q29 above: 28 minus 20 million currency units. The rejected values quote the project cost alone, add the two, or subtract the cheaper project instead."),
 ("cost of access can be prohibitively expensive, geothermal energy is not easily accessible",
  "The keyed summary carries ENG-3.N.1 and ENG-3.O.1 in the framework's own terms, including all three drawbacks and both hedges. Each rejected summary introduces a fuel, removes the water and steam, substitutes a drawback from another topic, denies the drawbacks, or grants an advantage the framework gives to wind rather than to geothermal energy."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24,
                25: q25, 26: q26, 27: q27, 28: q28, 29: q29}


def _selftest():
    """Reversal alone must be caught for every table, with no flatten fallback."""
    import copy
    import types

    def run_on(questions):
        mod = types.ModuleType("e6_10_mutant")
        mod.TOPIC = e6_10.TOPIC
        mod.QUESTIONS = questions
        e_check.style(mod)
        e_check.no_figure_reference(mod)
        cg.check(mod, CLAIMS, table_checks=TABLE_CHECKS)

    def must_fail(label, mutate):
        qs = copy.deepcopy(e6_10.QUESTIONS)
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

    # The clean pass is established BEFORE any mutation, so a standing defect
    # cannot make every later control raise for the wrong reason and print
    # "control OK" while proving nothing. That happened once in this unit.
    print("selftest: the unmodified module must pass before any mutation is tried")
    run_on(copy.deepcopy(e6_10.QUESTIONS))

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
    must_fail("q19 the chain made to gain energy at a step", edit(19, STEAM, AVAIL, "1,200"))
    must_fail("q20 delivered share moved off 15 percent", edit(20, GEN, AVAIL, "200"))
    must_fail("q21 first loss moved off 280 energy units", edit(21, STEAM, AVAIL, "800"))
    must_fail("q22 the cost made to fall as depth rises", edit(22, G3, DRILL, "2"))
    must_fail("q23 the rate made to differ between regions", edit(23, G2, DRILL, "14"))
    must_fail("q24 gap moved off 26 million", edit(24, G3, DRILL, "34"))
    must_fail("q25 the gradient broken at one point", edit(25, PT3, H2S, "90"))
    must_fail("q26 the farthest point given the highest reading", edit(26, PT4, H2S, "400"))
    must_fail("q27 gap moved off 178 parts per billion", edit(27, PT4, H2S, "10"))
    must_fail("q28 the dearer project brought within the funds",
              edit(28, SITEB, PROJECT, "18"))
    must_fail("q29 excess moved off 8 million", edit(29, SITEB, PROJECT, "32"))

    print("selftest: the unmodified module must still pass (positive control)")
    run_on(copy.deepcopy(e6_10.QUESTIONS))
    print("all selftest controls raised as required, and the clean module passes.")


if __name__ == "__main__":
    import sys
    if "--selftest" in sys.argv:
        _selftest()

e_check.run(e6_10, CLAIMS, TABLE_CHECKS)
