"""Key audit for AP ENVIRONMENTAL SCIENCE 5.12 Introduction to Sustainability.

One (anchor, claim) per item, in module order. The anchor must appear in the
KEYED choice and in no distractor.

WHAT THE KEYS REST ON
---------------------
  STB-1.A.1  Sustainability refers to humans living on Earth and their use of
             resources without depletion of the resources for future
             generations. Environmental indicators that can guide humans to
             sustainability include biological diversity, food production,
             average global surface temperatures and CO2 concentrations, human
             population, and resource depletion.
                          -- items 1, 2, 3, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                             23, 24, 26
  STB-1.A.2  Sustainable yield is the amount of a renewable resource that can be
             taken without reducing the available supply.
                          -- items 5, 6, 7, 8, 9, 10, 20, 21, 22, 25, 28
Items 27, 29 and 30 read the two statements against each other.

TWO CHAINS, both named in their claims and neither used as a key on its own:
  ENG-3.A.1 / ENG-3.A.2   nonrenewable sources exist in a fixed amount;
                          renewable sources are replenished naturally at or near
                          the rate of consumption            -- items 5, 21
  EIN-2.N.1               a footprint is a MEASURE; sustainability is a GOAL
                          (topic 5.11)                       -- boundary only

WHAT IS DELIBERATELY NOT KEYED. The framework introduces its indicator list with
the word INCLUDE, states no order of importance among them, sets no numerical
threshold, and names no country or year. Item 26 keys that absence directly
rather than working round it, and no item counts the list.

DATA ITEMS: 7, 8, 9, 10, 11, 12, 13, 14, 15 and 16, recomputed below from those
tables alone and addressed by row label.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and every table in turn, and requires each
corruption to raise, BEFORE the real gate runs. It is not behind a flag.
"""
import e_check
import cg_check as cg
import e5_12

GROWN = "New timber grown each year (thousand cubic meters)"
CUT = "Timber cut each year (thousand cubic meters)"

RECHARGE = "Water recharged to the aquifer each year (million cubic meters)"
PUMPED = "Water pumped out each year (million cubic meters)"
D1, D2, D3 = "District 1", "District 2", "District 3"

FIRST = "First survey"
LATER = "Survey thirty years later"
BIRDS = "Bird species breeding in the region (number)"
GRAIN = "Grain produced (million tonnes a year)"
CO2R = "Carbon dioxide in the atmosphere (parts per million)"
PEOPLE = "Human population (millions)"

TEMP = "Average global surface temperature (degrees Celsius)"
CO2C = "Carbon dioxide in the atmosphere (parts per million)"

FOOD = "Food produced (million tonnes a year)"
FED = "People to be fed (millions)"


def q7(table, item):
    g, c = cg.col(table, GROWN), cg.col(table, CUT)
    assert len(set(g)) == 1, f"every estate must grow the same amount for this item; got {g}"
    within = [lab for lab, cut in zip(cg.labels(table), c) if cut <= g[0]]
    assert within == ["Estate 1", "Estate 2"], \
        f"the estates within the annual growth are {within}, not the first two"
    assert cg.cell(table, "Estate 4", CUT) > g[0], "the fourth estate must be over the growth"
    assert len(set(c)) > 1, "'all four take exactly what the forest grows' must be false"
    return (f"growth is {g[0]:.0f} thousand cubic meters on every estate against cuts of {c}, so "
            f"{within} take no more than the forest grows and the others take more")


def q8(table, item):
    g, c = cg.col(table, GROWN), cg.col(table, CUT)
    d = max(c) - cg.cell(table, "Estate 4", GROWN)
    assert d == 30, f"the excess recomputes to {d}, not 30"
    for wrong in (max(c), max(c) + g[0], g[0] - min(c), max(c) - min(c)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"70 minus 40 is {d:.0f} thousand cubic meters more than the forest grows in a year"


def q9(table, item):
    over = [lab for lab in cg.labels(table)
            if cg.cell(table, lab, PUMPED) > cg.cell(table, lab, RECHARGE)]
    assert over == [D2], f"the districts pumping above their recharge are {over}, not {[D2]}"
    assert cg.cell(table, D1, PUMPED) < cg.cell(table, D1, RECHARGE), \
        "the first district must pump below its recharge"
    assert cg.cell(table, D3, PUMPED) == cg.cell(table, D3, RECHARGE), \
        "the third district must pump exactly its recharge"
    return (f"recharge runs {cg.col(table, RECHARGE)} against pumping of {cg.col(table, PUMPED)} "
            f"million cubic meters, so only {over[0]} takes more than is replaced")


def q10(table, item):
    d = cg.cell(table, D2, PUMPED) - cg.cell(table, D2, RECHARGE)
    margin = cg.cell(table, D1, RECHARGE) - cg.cell(table, D1, PUMPED)
    assert d == 5, f"the excess recomputes to {d}, not 5"
    assert margin == 6, f"the first district's unused margin recomputes to {margin}, not 6"
    for wrong in (cg.cell(table, D2, PUMPED),
                  cg.cell(table, D2, PUMPED) + cg.cell(table, D2, RECHARGE),
                  margin, cg.cell(table, D2, RECHARGE)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return (f"14 minus 9 is {d:.0f} million cubic meters over the recharge, against the first "
            f"district's unused margin of {margin:.0f}")


def q11(table, item):
    assert cg.cell(table, BIRDS, LATER) < cg.cell(table, BIRDS, FIRST), \
        "the bird count must fall"
    for row in (GRAIN, CO2R, PEOPLE):
        assert cg.cell(table, row, LATER) > cg.cell(table, row, FIRST), \
            f"the reading for {row!r} must rise"
    return (f"birds {cg.cell(table, BIRDS, FIRST):.0f} to {cg.cell(table, BIRDS, LATER):.0f}, "
            f"grain {cg.cell(table, GRAIN, FIRST):.0f} to {cg.cell(table, GRAIN, LATER):.0f}, "
            f"carbon dioxide {cg.cell(table, CO2R, FIRST):.0f} to "
            f"{cg.cell(table, CO2R, LATER):.0f} and population "
            f"{cg.cell(table, PEOPLE, FIRST):.0f} to {cg.cell(table, PEOPLE, LATER):.0f}")


def q12(table, item):
    d = cg.cell(table, BIRDS, FIRST) - cg.cell(table, BIRDS, LATER)
    pop = cg.cell(table, PEOPLE, LATER) - cg.cell(table, PEOPLE, FIRST)
    assert d == 54, f"the loss recomputes to {d}, not 54"
    for wrong in (cg.cell(table, BIRDS, FIRST),
                  cg.cell(table, BIRDS, FIRST) + cg.cell(table, BIRDS, LATER),
                  pop, cg.cell(table, BIRDS, LATER)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"180 minus 126 is {d:.0f} breeding bird species lost across the thirty years"


def q13(table, item):
    t, c = cg.col(table, TEMP), cg.col(table, CO2C)
    assert cg.cell(table, "First", TEMP) == min(t), "the first decade must be the coolest"
    assert all(t[i] < t[i + 1] for i in range(len(t) - 1)), f"temperature must rise; got {t}"
    assert all(c[i] < c[i + 1] for i in range(len(c) - 1)), f"carbon dioxide must rise; got {c}"
    return (f"temperature runs {t} degrees Celsius against carbon dioxide of {c} parts per "
            "million, both rising throughout")


def q14(table, item):
    c = cg.col(table, CO2C)
    d = cg.cell(table, "Fourth", CO2C) - cg.cell(table, "First", CO2C)
    step = cg.cell(table, "Fourth", CO2C) - cg.cell(table, "Third", CO2C)
    assert d == 80, f"the rise recomputes to {d}, not 80"
    for wrong in (max(c), max(c) + min(c), step, min(c)):
        assert d != wrong, f"the {wrong} distractor equals the key"
    return f"410 minus 330 is {d:.0f} parts per million more carbon dioxide across the record"


def q15(table, item):
    f, p = cg.col(table, FOOD), cg.col(table, FED)
    assert all(f[i] < f[i + 1] for i in range(len(f) - 1)), f"food produced must rise; got {f}"
    per = [a / b for a, b in zip(f, p)]
    assert all(per[i] > per[i + 1] for i in range(len(per) - 1)), \
        f"food for each person must fall; got {per}"
    assert cg.cell(table, "First", FOOD) == min(f), "the first decade must produce the least"
    return (f"production runs {f} million tonnes against {p} million people, so the amount for "
            f"each person runs {[round(x, 2) for x in per]} tonnes and falls throughout")


def q16(table, item):
    first = cg.cell(table, "First", FOOD) / cg.cell(table, "First", FED)
    fourth = cg.cell(table, "Fourth", FOOD) / cg.cell(table, "Fourth", FED)
    third = cg.cell(table, "Third", FOOD) / cg.cell(table, "Third", FED)
    d = first - fourth
    assert abs(first - 1.5) < 1e-9, f"the first decade recomputes to {first}, not 1.5"
    assert abs(fourth - 1.0) < 1e-9, f"the fourth decade recomputes to {fourth}, not 1.0"
    assert abs(d - 0.5) < 1e-9, f"the fall recomputes to {d}, not 0.5"
    for wrong in (first, fourth, third - fourth, 0.1):
        assert abs(d - wrong) > 1e-9, f"the {wrong} distractor equals the key"
    return (f"30 over 20 is {first:.2f} tonnes per person and 54 over 54 is {fourth:.2f}, a fall "
            f"of {d:.2f}")


CLAIMS = [
 ("using resources without depleting those resources for future generations",
  "STB-1.A.1, near verbatim: sustainability refers to humans LIVING ON EARTH AND THEIR USE OF RESOURCES WITHOUT DEPLETION OF THE RESOURCES FOR FUTURE GENERATIONS. Each rejected option forbids use altogether or drops the future-generations clause."),
 ("whether the resources will still be there for people who come later",
  "STB-1.A.1 makes the standard use WITHOUT DEPLETION OF THE RESOURCES FOR FUTURE GENERATIONS, so what remains for later people is the test. The framework fixes no number of generations and imposes no rule on how much future generations may use."),
 ("Biological diversity, food production, average global surface temperatures and carbon dioxide",
  "STB-1.A.1 lists biological diversity, food production, average global surface temperatures and CO2 concentrations, human population, and resource depletion. Each rejected list substitutes economic figures or ordinary weather readings the statement never names."),
 ("Average household income",
  "STB-1.A.1's list is biological diversity, food production, average global surface temperatures and CO2 concentrations, human population, and resource depletion. Household income appears nowhere in it, while every rejected option is quoted from the list directly."),
 ("A renewable resource",
  "STB-1.A.2 states that sustainable yield is the amount of A RENEWABLE RESOURCE that can be taken without reducing the available supply. ENG-3.A.1 puts nonrenewable sources in a fixed amount, so no rate of taking one leaves its supply unreduced."),
 ("leave the available supply undiminished",
  "STB-1.A.2 defines sustainable yield as the amount that can be taken WITHOUT REDUCING THE AVAILABLE SUPPLY, so the condition falls on what is left behind. A harvest that reduces the supply by any share, however small, fails it."),
 ("first two estates take no more timber than the forest grows",
  "Recomputed in q7 above: growth of 40 thousand cubic meters on every estate against cuts of 25, 40, 55 and 70. STB-1.A.2 allows the amount that can be taken without reducing the available supply, and only the first two estates meet it. One distractor swaps which pair is which, so the anchor carries the direction."),
 ("By 30 thousand cubic meters",
  "Recomputed in q8 above: 70 minus 40 thousand cubic meters. The rejected values quote the heaviest cut alone, add the two, take the lightest estate's shortfall, or pair the wrong estate."),
 ("second district, which pumps out more than is recharged",
  "Recomputed in q9 above: 18 against 12, 9 against 14, and 25 against 25 million cubic meters. STB-1.A.2 allows the amount that can be taken without reducing the available supply, so only the second district is over it."),
 ("By 5 million cubic meters",
  "Recomputed in q10 above: 14 minus 9 million cubic meters. The rejected values quote the pumping alone, add the two, give the first district's unused margin of 6, or quote the recharge alone."),
 ("Biological diversity fell while food production, carbon dioxide and human population all rose",
  "Recomputed in q11 above: 180 to 126 breeding bird species, 9 to 14 million tonnes of grain, 340 to 420 parts per million and 20 to 34 million people. All four are indicators STB-1.A.1 names and they do not all move the same way, so the anchor carries both directions."),
 ("54 species",
  "Recomputed in q12 above: 180 minus 126 breeding bird species. The rejected values quote the first survey alone, add the two, take the rise in the population row, or quote the later survey alone."),
 ("carbon dioxide concentration both rose across the record",
  "Recomputed in q13 above: 14.0 to 14.9 degrees Celsius against 330 to 410 parts per million. STB-1.A.1 names average global surface temperatures and CO2 concentrations together in its list of indicators. Distractors reverse one or both directions, so the anchor carries the direction word."),
 ("By 80 parts per million",
  "Recomputed in q14 above: 410 minus 330 parts per million. The rejected values quote the final reading alone, add the two, take a single decade's step, or quote the opening reading alone."),
 ("rose across the record, but the food available for each person fell",
  "Recomputed in q15 above: 30 to 54 million tonnes against 20 to 54 million people, so the amount for each person falls from 1.5 to 1.0 tonnes. Food production and human population are both indicators STB-1.A.1 names, and reading either alone would mislead. The anchor carries both directions."),
 ("By 0.5 tonnes per person",
  "Recomputed in q16 above: 30 over 20 against 54 over 54. The rejected values quote one of the two ratios alone or take the change across a single decade."),
 ("number of species recorded in repeated surveys",
  "STB-1.A.1 lists biological diversity among the indicators that can guide humans to sustainability, and a count of species present in repeated surveys measures it directly. Each rejected option names a different indicator from the same list."),
 ("Average global surface temperatures and carbon dioxide concentrations",
  "STB-1.A.1's list reads biological diversity, food production, average global surface temperatures AND CO2 CONCENTRATIONS, human population, and resource depletion, so those two readings are joined in a single item. Each rejected pair joins two items the statement lists separately."),
 ("about USE without depletion, not about abstaining from use",
  "STB-1.A.1 speaks of humans living on Earth AND THEIR USE OF RESOURCES without depletion for future generations, so use is assumed and the condition falls on depletion. One rejected option drops the future-generations clause instead, which is the opposite error."),
 ("largest possible harvest may still reduce the available supply",
  "STB-1.A.2 sets the test as taking WITHOUT REDUCING THE AVAILABLE SUPPLY, a condition on the stock left behind rather than on what a stand could yield if pushed. The framework supplies no fraction of the maximum and no exemption for nonrenewables."),
 ("replenished naturally at or near the rate of consumption",
  "STB-1.A.2 states the yield for a renewable resource, and ENG-3.A.2 defines renewable sources as those replenished naturally at or near the rate of consumption, which is what makes a non-depleting rate of taking possible. ENG-3.A.1 puts nonrenewable sources in a fixed amount."),
 ("grows back each year, and how much is cut each year",
  "STB-1.A.2 compares what is taken against what leaves the available supply unreduced, so the regrowth and the take are the minimum pair. Price, area, rainfall and livestock numbers say nothing about whether the supply is being reduced, which is why the anchor spans the pairing."),
 ("They can guide humans to sustainability",
  "STB-1.A.1 says environmental indicators CAN GUIDE HUMANS TO SUSTAINABILITY, a hedged and forward-looking role. Nothing in the statement makes an indicator a proof, a limit, or a substitute for resource depletion, which the same list names in its own right."),
 ("quantity of a resource still available falling year after year",
  "STB-1.A.1 lists resource depletion among its indicators, and depletion is a fall in what remains available. Price, employment, trade and the number of applications may accompany depletion, but none of them measures the remaining stock."),
 ("amount recharged to the aquifer over the same period",
  "STB-1.A.2 makes the sustainable amount the one that can be taken without reducing the available supply, so the take must be set beside what replaces it. A neighbour's pumping, total rainfall and the number of households all leave that comparison unmade."),
 ("ranks its environmental indicators in order of importance",
  "STB-1.A.1 gives its indicators as a list introduced by the word include, with no order and no weighting stated, so a ranking would be added rather than read. Each rejected option quotes something the two statements do assert."),
 ("Sustainability is the goal of using resources without depleting them for future generations; a sustainable yield is the amount",
  "STB-1.A.1 states a goal about use without depletion for future generations while STB-1.A.2 states an amount that may be taken from a renewable resource. One distractor is the exact swap of the goal and the amount, so the anchor carries both halves."),
 ("faster-growing bed is within the sustainable yield and the take from the slower-growing bed is not",
  "STB-1.A.2 sets the test by whether the available supply is reduced, so an identical take of 50 tonnes passes against 80 tonnes of regrowth and fails against 30. Equal takes do not imply equal outcomes, and taking some of a renewable resource is not by itself a breach. One distractor swaps the two beds, so the anchor carries both."),
 ("puts the definition's requirement into a quantity",
  "STB-1.A.1 supplies the requirement, that resources not be depleted for future generations, and STB-1.A.2 supplies the amount that satisfies it for a renewable resource. One is the standard and the other is that standard expressed as a quantity."),
 ("indicators including biological diversity, food production, temperature and carbon dioxide",
  "The keyed summary carries STB-1.A.1's definition and its list of indicators together with STB-1.A.2's amount for a renewable resource. Each rejected summary forbids use, drops the future-generations clause, swaps the indicators for economic ones, or denies that the framework defines the terms."),
]

TABLE_CHECKS = {7: q7, 8: q8, 9: q9, 10: q10, 11: q11, 12: q12, 13: q13, 14: q14,
                15: q15, 16: q16}

e_check.run(e5_12, CLAIMS, TABLE_CHECKS)
