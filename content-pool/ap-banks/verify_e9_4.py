"""Key audit for AP ENVIRONMENTAL SCIENCE 9.4 Increases in the Greenhouse Gases.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student.

WHAT THE KEYS REST ON
---------------------
STB-4.E.1 is the whole of this topic's required content, and it is one sentence
plus a second:

    Global climate change, caused by excess greenhouse gases in the atmosphere,
    can lead to a variety of environmental problems including rising sea levels
    resulting from melting ice sheets and ocean water expansion, and disease
    vectors spreading from the tropics toward the poles. These problems can lead
    to changes in population dynamics and population movements in response.

Every key here rests on one of its five separable claims:

  (a) the cause is EXCESS greenhouse gases in the atmosphere
                    -- items 1, 16, 25, 26, 27, 30
  (b) the problems are a VARIETY, of which the sentence names some
                    -- items 2, 8, 24, 28, 30
  (c) sea level rises from TWO stated contributions, melting ice sheets AND the
      expansion of ocean water
                    -- items 4, 9, 10, 11, 17, 20, 22, 29, 30
  (d) disease vectors spread FROM THE TROPICS TOWARD THE POLES, that direction
      and no other
                    -- items 5, 12, 14, 15, 18, 30
  (e) the problems can lead to changes in POPULATION DYNAMICS and POPULATION
      MOVEMENTS in response
                    -- items 6, 13, 19, 21, 30

Two items borrow an identification from elsewhere in unit 9 and say so in their
own ``why``: items 3, 7 and 27 use STB-4.C.1 (the principal greenhouse gases are
carbon dioxide, methane, water vapor, nitrous oxide and CFCs) to say what the
tabulated gases are, and item 16 uses STB-4.C.3 (the greenhouse effect results in
the surface temperature necessary for life on Earth to exist) to distinguish the
presence of the gases from an EXCESS of them. Items 1, 8, 17 and 28 reject a
distractor on STB-4.A.3 (a decrease in stratospheric ozone increases the UV rays
reaching the surface; exposure can lead to skin cancer and cataracts) and item 1
also on EIN-3.C.2 (dysentery from untreated sewage) and EIN-3.C.4 (respiratory
problems from tropospheric ozone). All five statements were read in the CED, not
recalled.

TWO GLOSSES, STATED PLAINLY. Item 9's key and item 29's key each explain what one
of the two named contributions IS -- expansion changes the volume the same water
occupies, and an ice sheet is land ice whose meltwater is added to the ocean.
Neither goes beyond the meaning of the framework's own two nouns, and the
operative clause of each key ("one of the two contributions the statement gives")
is STB-4.E.1 verbatim. Nothing else in the module explains a mechanism.

TWO ITEMS TURN ON A SWAP and their anchors carry BOTH clauses. Item 17 pairs a
problem with its mechanism and its distractors re-pair the same nouns; item 26
names the cause and the consequence and its distractor exchanges them. An anchor
naming one half would match the swap as well as the key -- the defect already
found once in verify_e2_1.py.

ON SCOPE. Topic 9.3 keys which gases are greenhouse gases and how their potencies
compare, 9.5 the effects of climate change on ecosystems, 9.6 ocean warming and
9.7 ocean acidification. No key here states any of those. NOT KEYED ANYWHERE: a
projected sea level, a temperature target, a named country or island, a date, or
a named disease.

DATA ITEMS: 3, 7, 11, 15, 19 and 23 carry tables, because the suggested skill is
2.C and the bank cannot show a picture. Every keyed reading, sum, difference and
percentage is recomputed below from that table alone.

NEGATIVE CONTROL: e_check.run corrupts a key, an anchor, a choice, a why, the
notation, a figure reference, and EVERY data table in turn, and requires each
corruption to raise BEFORE the real gate runs. The ranking check on item 19 reads
an agreement between two columns that a reversal of both preserves, so for that
one e_check flattens the table next and the check fails, because a flat column
has no ranking. ``python3 verify_e9_4.py --selftest`` is the same run; the
controls are not behind the flag.
"""
import sys

import cg_check as cg
import e_check
import e9_4

CO2 = "Carbon dioxide (parts per million)"
CH4 = "Methane (parts per billion)"
N2O = "Nitrous oxide (parts per billion)"
EARLIER = "Concentration in the earlier record (parts per billion)"
LATER = "Concentration in the later record (parts per billion)"
ICE = "Contribution from melting ice sheets (millimeters per year)"
EXPANSION = "Contribution from the expansion of ocean water (millimeters per year)"
TOTAL = "Total rise in sea level (millimeters per year)"
LATITUDE = "Northernmost latitude at which the disease vector was found (degrees)"
LANDLOST = "Share of the district's land lost to the sea (percent)"
PEOPLE = "People who left the district over the same period"
RELEASED = ("Greenhouse gases released each year (billions of tons of carbon dioxide "
            "equivalent)")
MEASURED = "Carbon dioxide measured in the atmosphere (parts per million)"


def _rises(v):
    return all(v[i + 1] > v[i] for i in range(len(v) - 1))


def q3(table, item):
    columns = {name: cg.col(table, name) for name in (CO2, CH4, N2O)}
    for name, values in columns.items():
        assert _rises(values), f"{name} must rise at every step; got {values}"
    assert len(columns) == 3, "three gases must be tabulated"
    return (f"all three columns rise at every step: carbon dioxide {columns[CO2]}, "
            f"methane {columns[CH4]}, nitrous oxide {columns[N2O]}")


def q7(table, item):
    labs = cg.labels(table)
    earlier = dict(zip(labs, cg.col(table, EARLIER)))
    later = dict(zip(labs, cg.col(table, LATER)))
    pct = {lab: (later[lab] - earlier[lab]) / earlier[lab] * 100 for lab in labs}
    largest_rise = max(pct, key=pct.get)
    assert largest_rise == "Methane", \
        f"the largest percentage rise must belong to methane; got {largest_rise} ({pct})"
    assert pct["Methane"] > 100, f"methane must more than double; got {pct['Methane']}"
    for lab in ("Carbon dioxide", "Nitrous oxide"):
        assert pct[lab] < 100, f"{lab} must rise by less than one hundred percent; got {pct[lab]}"
    # The distractor that reasons from size rather than from change: the gas
    # with the largest concentration must NOT be the one with the largest rise.
    largest_concentration = max(later, key=later.get)
    assert largest_concentration == "Carbon dioxide", \
        f"carbon dioxide must hold the largest concentration; got {largest_concentration}"
    assert largest_concentration != largest_rise, \
        "the largest concentration must not also be the largest percentage rise"
    return (f"the percentage rises are {({k: round(v) for k, v in pct.items()})}, so the "
            f"largest belongs to {largest_rise} while the largest concentration belongs "
            f"to {largest_concentration}")


def q11(table, item):
    ice = cg.col(table, ICE)
    expansion = cg.col(table, EXPANSION)
    total = cg.col(table, TOTAL)
    ice_grew = _rises(ice)
    expansion_grew = _rises(expansion)
    assert ice_grew, f"the ice sheet contribution must grow across the periods; got {ice}"
    assert expansion_grew, f"the expansion contribution must grow across the periods; got {expansion}"
    for i, (a, b, t) in enumerate(zip(ice, expansion, total), 1):
        assert abs(a + b - t) < 0.051, \
            f"period {i}: {a} plus {b} must account for the whole rise of {t}"
    return (f"the ice sheet contribution runs {ice} and the expansion {expansion}, both "
            f"growing, and in every period the two add to the recorded total {total}")


def q15(table, item):
    lat = cg.col(table, LATITUDE)
    assert _rises(lat), f"the range limit must move poleward at every step; got {lat}"
    assert lat[-1] != lat[0], "'the same latitude in the first and last decades' must be false"
    return (f"the northernmost latitude recorded runs {lat} degrees, rising at every step, "
            "which is movement away from the equator")


def q19(table, item):
    labs = cg.labels(table)
    land = dict(zip(labs, cg.col(table, LANDLOST)))
    people = dict(zip(labs, cg.col(table, PEOPLE)))
    by_land = sorted(labs, key=lambda lab: land[lab])
    by_people = sorted(labs, key=lambda lab: people[lab])
    assert by_land == by_people, \
        f"the two rankings must agree; land gives {by_land} and people {by_people}"
    assert len(set(land.values())) == len(labs), f"the land losses must differ; got {land}"
    assert len(set(people.values())) == len(labs), f"the departures must differ; got {people}"
    assert min(people.values()) > 0, f"every district must have lost people; got {people}"
    return (f"ranking the districts by land lost gives {by_land} and ranking them by people "
            f"who left gives {by_people}, the same order, with land {land} and people {people}")


def q23(table, item):
    released = cg.col(table, RELEASED)
    measured = cg.col(table, MEASURED)
    release_rose = _rises(released)
    concentration_rose = _rises(measured)
    assert release_rose, f"the yearly release must rise across the periods; got {released}"
    assert concentration_rose, \
        f"the measured concentration must rise across the periods; got {measured}"
    return (f"the yearly release runs {released} billions of tons and the measured "
            f"concentration {measured} parts per million, both rising at every step")


CLAIMS = [
 ("Excess greenhouse gases in the atmosphere",
  "STB-4.E.1 states that global climate change is caused by excess greenhouse gases in the atmosphere. The rejected causes belong to STB-4.A.2 (stratospheric ozone depletion), EIN-3.C.4 (tropospheric ozone) and EIN-3.C.2 (untreated sewage in streams and rivers)."),
 ("Rising sea levels, and disease vectors spreading from the tropics toward the poles",
  "STB-4.E.1 names rising sea levels and disease vectors spreading from the tropics toward the poles among the variety of environmental problems global climate change can lead to. The rejected sets reverse a direction or import ozone depletion, eutrophication and landfill gas from other statements."),
 ("rose at every step",
  "Recomputed in q3 above: each of the three tabulated columns is larger in every later row than in the row above it. STB-4.C.1 names carbon dioxide, methane and nitrous oxide among the principal greenhouse gases and STB-4.E.1 attributes global climate change to an excess of such gases in the atmosphere."),
 ("Melting ice sheets and the expansion of ocean water",
  "STB-4.E.1 states that rising sea levels result from melting ice sheets and ocean water expansion. Those two and no others are the contributions the statement gives, so each rejected pair keeps at most one of them."),
 ("From the tropics toward the poles",
  "STB-4.E.1 states that disease vectors are spreading from the tropics toward the poles. Each rejected option reverses that direction or substitutes a different axis of movement."),
 ("Changes in population dynamics and population movements in response",
  "STB-4.E.1's second sentence states that these problems can lead to changes in population dynamics and population movements in response. The rejected options attribute outcomes the statement does not."),
 ("Methane, which rose by more than one hundred percent",
  "Recomputed in q7 above: methane is the only one of the three whose increase exceeds its earlier value, and the gas holding the largest concentration is not the gas with the largest percentage rise. STB-4.C.1 names all three among the principal greenhouse gases."),
 ("ultraviolet radiation reaching",
  "STB-4.E.1 names rising sea levels from melting ice sheets and ocean water expansion, and disease vectors spreading poleward. An increase in ultraviolet radiation at the surface belongs to STB-4.A.3, which follows a decrease in stratospheric ozone rather than an excess of greenhouse gases."),
 ("one adding water and the other changing the volume",
  "STB-4.E.1 names melting ice sheets and ocean water expansion as two sources of one rise, so the framework treats them as separate contributions rather than as one process or as offsetting effects. The keyed gloss goes no further than the meaning of the statement's own word expansion."),
 ("resulting from melting ice sheets and the expansion of ocean water",
  "STB-4.E.1 names rising sea levels, resulting from melting ice sheets and ocean water expansion, among the environmental problems global climate change can lead to, which is the problem a plan for coastal flooding responds to. The rejected options belong to other statements in the course."),
 ("the two together account for the whole rise",
  "Recomputed in q11 above: both contribution columns grow across the periods and in every period they add to the recorded total. STB-4.E.1 names melting ice sheets and ocean water expansion as the sources of the rise in sea level."),
 ("Disease vectors spreading from the tropics toward the poles",
  "STB-4.E.1 names disease vectors spreading from the tropics toward the poles among the problems, and the learning objective STB-4.E is to identify the threats to HUMAN HEALTH and the environment. The other items in the statement concern the level of the sea and the movement of populations."),
 ("changes within populations while the other concerns populations relocating",
  "STB-4.E.1 states that these problems can lead to changes in population dynamics AND population movements in response, naming two outcomes rather than one, and it restricts neither to a particular kind of population."),
 ("moving away from the tropics over successive decades",
  "STB-4.E.1 asserts a movement from the tropics toward the poles, so repeated surveys of the range limit over time are what would test it. A single survey shows no movement, and a population count, a price and a sea level measure other quantities."),
 ("moved steadily farther from the equator",
  "Recomputed in q15 above: the recorded northernmost latitude rises at every step across the four decades. STB-4.E.1 states that disease vectors are spreading from the tropics toward the poles."),
 ("the amount beyond that which the framework connects",
  "STB-4.E.1 attributes global climate change to EXCESS greenhouse gases in the atmosphere, while STB-4.C.3 states that the greenhouse effect results in the surface temperature necessary for life on Earth to exist. The two together distinguish the presence of the gases from an excess of them."),
 # Both clauses: the distractors re-pair the same nouns, so an anchor naming the
 # problem alone or the mechanism alone would match a swap as well as the key.
 ("Rising sea levels, paired with melting ice sheets",
  "STB-4.E.1 attributes the rise in sea level to melting ice sheets and ocean water expansion, and names the poleward spread of disease vectors as a separate problem with no mechanism attached to it. Ultraviolet radiation belongs to STB-4.A.3."),
 ("spreading from the tropics toward the poles as a consequence",
  "STB-4.E.1 names disease vectors spreading from the tropics toward the poles among the problems that global climate change can lead to, which is what the arrival of a formerly tropical disease in a temperate region would be an instance of."),
 ("lost the most land also lost the most people",
  "Recomputed in q19 above: ranking the districts by the share of land lost to the sea gives the same order as ranking them by the number of people who left, with no ties in either column. STB-4.E.1 states that these problems can lead to changes in population dynamics and population movements in response."),
 ("measured separately",
  "STB-4.E.1 names two contributions to the rise in sea level, so measuring each of them on its own is what shows how much each adds. A total alone cannot be divided between them, and the remaining options measure other quantities."),
 ("follow from the environmental problems it lists rather than causing them",
  "STB-4.E.1 states that these problems can lead to changes in population dynamics and population movements IN RESPONSE, which places the movements after the problems in the chain and alongside the changes in dynamics rather than before them."),
 ("in step with measured ice sheet loss and ocean warming",
  "STB-4.E.1 attributes rising sea levels to melting ice sheets and the expansion of ocean water, so a record tying a local rise to those two processes is what supports the claim. Settlement history, coastal orientation, population and a change of name bear on none of it."),
 ("Both the yearly release of greenhouse gases and the concentration measured in the atmosphere rose",
  "Recomputed in q23 above: both columns rise at every step across the four periods. STB-4.E.1 attributes global climate change to excess greenhouse gases in the atmosphere, and the two columns are the yearly release and the amount then present."),
 ("examples rather than a complete list",
  "STB-4.E.1 says global climate change can lead to a VARIETY of environmental problems INCLUDING the ones it then names, and the word including marks those as examples rather than as the whole set."),
 # Both ends of the chain: a distractor keeps the tail and swaps the head, so
 # the anchor has to name the head as well.
 ("Excess greenhouse gases lead to global climate change, which raises sea levels",
  "STB-4.E.1 runs from excess greenhouse gases, to global climate change, to rising sea levels among a variety of problems, and then to changes in population dynamics and population movements in response. Each rejected chain reverses a link or removes the problem standing between the gases and the movement."),
 # Both clauses: the distractor exchanges the cause and the consequence.
 ("Excess greenhouse gases are the cause and rising sea levels are a consequence",
  "STB-4.E.1 states that global climate change is CAUSED BY excess greenhouse gases in the atmosphere and CAN LEAD TO problems including rising sea levels, so the gases stand at the causal end of the statement and the sea level rise at the consequence end."),
 ("are the excess the framework connects",
  "STB-4.C.1 identifies the principal greenhouse gases and STB-4.E.1 attributes global climate change, and the problems that follow from it, to excess greenhouse gases in the atmosphere. That is the connection between a table of rising concentrations and a broader environmental issue."),
 ("skin cancer and cataracts",
  "STB-4.A.3 states that exposure to the UV rays that follow a decrease in stratospheric ozone can lead to skin cancer and cataracts in humans. STB-4.E.1 attributes the four rejected outcomes to global climate change and does not attribute those two to it."),
 ("Water held on land as ice adds to the ocean",
  "STB-4.E.1 names melting ice sheets as one of TWO contributions to rising sea levels, the other being ocean water expansion, so the melting is neither the only contribution, nor a reducer of the ocean, nor a consequence of the rise. The keyed gloss goes no further than the meaning of the statement's own words."),
 ("including sea levels rising from melting ice sheets and the expansion of ocean water",
  "Every clause of the keyed summary is part of STB-4.E.1: the excess gases, the variety of problems, the two contributions to the sea level rise, the poleward spread of disease vectors, and the changes in population dynamics and population movements. Each rejected summary substitutes ozone depletion for climate change, reverses a direction, denies the population consequences, or replaces the two named contributions with one the framework never gives."),
]

TABLE_CHECKS = {3: q3, 7: q7, 11: q11, 15: q15, 19: q19, 23: q23}

if "--selftest" in sys.argv:
    print("note: e_check.run negative-controls every gate on every run; "
          "--selftest is the same run, not a separate one.")

e_check.run(e9_4, CLAIMS, TABLE_CHECKS)
