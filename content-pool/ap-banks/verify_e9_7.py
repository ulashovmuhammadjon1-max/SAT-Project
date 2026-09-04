"""Key audit for AP ENVIRONMENTAL SCIENCE 9.7 Ocean Acidification.

One (anchor, claim) per item, in module order. ``anchor`` is a distinctive
substring that must appear in the KEYED choice and in no distractor, so an
off-by-one key or a reordered choice list fails here rather than reaching a
student. ``claim`` states what the key rests on, for a human to audit.

WHAT THE KEYS REST ON
---------------------
  STB-4.H.1  ocean acidification is the decrease in pH of the oceans, primarily
             due to increased CO2 concentrations in the atmosphere, and can be
             expressed as chemical equations
                 -- items 1, 2, 3, 9, 12, 15, 18, 19, 20, 30
  STB-4.H.2  as more CO2 is released, the oceans, which absorb a large part of
             it, become more acidic -- items 4, 5, 15, 17, 21, 22, 30
  STB-4.H.3  the anthropogenic activities contributing to acidification are
             those leading to increased atmospheric CO2: burning of fossil
             fuels, vehicle emissions, and deforestation
                 -- items 6, 7, 8, 15, 16, 23, 24, 30
  STB-4.H.4  acidification damages coral because it makes shell formation
             difficult, due to the loss of calcium carbonate
                 -- items 10, 11, 13, 14, 15, 25, 26, 27, 28, 29, 30

ACIDIFICATION AND WARMING ARE DIFFERENT MECHANISMS, AND KEEPING THEM APART IS
THE POINT OF THIS MODULE'S DESIGN. STB-4.H.4 makes acidification damage coral
through the LOSS OF CALCIUM CARBONATE, leaving shell formation difficult;
STB-4.G.3, which belongs to topic 9.6, makes warming cause BLEACHING through
the LOSS OF ALGAE within the coral. Items 13, 14 and 29 each carry a distractor
that swaps the two, so every anchor on those items names BOTH the process AND
its mechanism. An anchor naming only "bleaching", or only "the loss of calcium
carbonate", would match the swapped distractor as readily as the key -- exactly
the defect already found once in this subject's banks.

NO CHEMICAL EQUATION APPEARS ANYWHERE. STB-4.H.1 says acidification CAN BE
EXPRESSED as chemical equations and gives none, and this subject is exported as
prose with no typesetting, so a hand-written equation would reach a student as
raw characters. Item 3 keys what the framework says about the equations without
writing one, and the notation gate refuses a backslash or a caret anywhere in
the module.

WHAT IS DELIBERATELY NOT KEYED. STB-4.H.1's hedge PRIMARILY is kept in item 9
rather than hardened into a sole cause. STB-4.H.3 explains no mechanism beyond
"activities that lead to increased CO2 concentrations", so no item explains how
deforestation raises atmospheric carbon dioxide. STB-4.H.2 says A LARGE PART and
gives no figure, so no key states a share; item 22 reads its share from its own
record instead.

NO FIGURE IS REFERENCED; ``e_check.no_figure_reference`` enforces that on every
run.

DATA ITEMS: 19 to 29 carry tables, each recomputed below from that table alone.

NEGATIVE CONTROLS run on every invocation through ``e_check.run``; ``--selftest``
adds ``es_check.selftest``, which rotates all thirty keys one at a time and
corrupts every cell of every table individually.
"""
import sys

import cg_check as cg
import e_check
import es_check as es

import e9_7

CO2 = "Atmospheric carbon dioxide (parts per million)"
PH = "Mean pH of the ocean surface"
RELEASED = "Carbon dioxide released to the atmosphere (billions of tonnes)"
TAKEN = "Carbon dioxide taken up by the ocean (billions of tonnes)"
EMITTED = "Carbon dioxide added to the atmosphere (millions of tonnes each year)"
TANKPH = "pH of the seawater"
CARBONATE = "Calcium carbonate available to the corals (relative index)"
SKELETON = "New skeleton laid down in ninety days (grams)"
REEFPH = "Mean pH of the surrounding water"
GROWTH = "New coral skeleton laid down (millimetres each year)"
TEMP = "Water temperature (degrees Celsius)"
WATERPH = "pH of the water"
WHITE = "Percent of colonies turned white"

WIND = "Generating electricity from wind and sunlight"
COAL = "Burning fossil fuels in power stations"


def _rising(values):
    return all(values[i + 1] > values[i] for i in range(len(values) - 1))


def _falling(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def q19(table, item):
    co2 = cg.col(table, CO2)
    ph = cg.col(table, PH)
    assert _rising(co2), f"the carbon dioxide must rise at every decade; got {co2}"
    assert _falling(ph), f"the pH must fall at every decade; got {ph}"
    return (f"in decade order the carbon dioxide reads {co2} parts per million, rising, "
            f"while the surface pH reads {ph}, falling")


def q20(table, item):
    ph = cg.col(table, PH)
    fall = ph[0] - ph[-1]
    assert abs(fall - 0.08) < 1e-6, f"the pH must fall by 0.08; got {fall}"
    assert fall > 0, "the movement must be a fall rather than a rise"
    return (f"the surface pH runs from {ph[0]} to {ph[-1]}, a fall of {fall:.2f}")


def q21(table, item):
    pairs = sorted(zip(cg.col(table, RELEASED), cg.col(table, TAKEN)))
    taken = [t for _, t in pairs]
    assert _rising(taken), f"the uptake must rise with the release; got {pairs}"
    for released, up in pairs:
        assert 0 < up < released, \
            f"the ocean must take up part but not all of the release; got {up} of {released}"
    assert len(set(taken)) == len(taken), "'the same amount whatever is released' must be false"
    return (f"sorted by the amount released the uptake reads {taken} billion tonnes, "
            "strictly rising, and each uptake is a part of that year's release")


def q22(table, item):
    shares = [t / r for r, t in zip(cg.col(table, RELEASED), cg.col(table, TAKEN))]
    assert all(abs(s - 0.30) < 1e-9 for s in shares), \
        f"every year's share must be 30 percent; got {shares}"
    assert len(set(round(s, 6) for s in shares)) == 1, "the share must not move across the years"
    return (f"dividing each year's uptake by that year's release gives "
            f"{[round(s * 100) for s in shares]} percent, the same figure every year")


def q23(table, item):
    labels = cg.labels(table)
    emitted = cg.col(table, EMITTED)
    top = max(range(len(emitted)), key=lambda i: emitted[i])
    assert labels[top] == COAL, f"the largest emitter must be {COAL!r}; got {labels[top]}"
    assert len([e for e in emitted if e == emitted[top]]) == 1, \
        "that largest figure must be unique, so 'all four add the same' is false"
    return (f"the emissions read {emitted} million tonnes a year, whose single largest "
            f"belongs to {labels[top]}")


def q24(table, item):
    labels = cg.labels(table)
    emitted = cg.col(table, EMITTED)
    zero = [labels[i] for i, e in enumerate(emitted) if e == 0]
    assert zero == [WIND], f"exactly the wind and sunlight row must add none; got {zero}"
    named = [COAL, "Vehicle emissions", "Deforestation"]
    for lab in named:
        assert lab in labels, f"the record must carry the framework's activity {lab!r}"
        assert cg.cell(table, lab, EMITTED) > 0, f"{lab!r} must add a positive amount"
    return (f"three rows of the record are the activities the framework names, each adding "
            f"a positive amount, and the fourth, {zero[0]}, adds none")


def q25(table, item):
    trio = sorted(zip(cg.col(table, TANKPH), cg.col(table, CARBONATE),
                      cg.col(table, SKELETON)))
    carbonate = [c for _, c, _ in trio]
    skeleton = [s for _, _, s in trio]
    assert _rising(carbonate), f"the calcium carbonate must rise with the pH; got {trio}"
    assert _rising(skeleton), f"the skeleton laid down must rise with the pH; got {trio}"
    assert len(set(skeleton)) == len(skeleton), \
        "'every tank laid down the same amount' must be false"
    return (f"sorted by pH the calcium carbonate index reads {carbonate} and the skeleton "
            f"laid down {skeleton} grams, both rising, so both fall together as the pH does")


def q26(table, item):
    labels = cg.labels(table)
    ph = cg.col(table, TANKPH)
    carbonate = cg.col(table, CARBONATE)
    skeleton = cg.col(table, SKELETON)
    worst = min(range(len(skeleton)), key=lambda i: skeleton[i])
    assert worst == min(range(len(ph)), key=lambda i: ph[i]), \
        "the tank laying down least skeleton must be the one at the lowest pH"
    assert worst == min(range(len(carbonate)), key=lambda i: carbonate[i]), \
        "it must also hold the least available calcium carbonate"
    assert labels[worst] == "Tank 4", f"that tank must be Tank 4; got {labels[worst]}"
    return (f"{labels[worst]} holds the lowest pH, {ph[worst]}, the least calcium "
            f"carbonate, {carbonate[worst]:.0f}, and lays down the least skeleton, "
            f"{skeleton[worst]} grams")


def q27(table, item):
    pairs = sorted(zip(cg.col(table, REEFPH), cg.col(table, GROWTH)))
    growth = [g for _, g in pairs]
    assert _rising(growth), f"the skeleton laid down must rise with the pH; got {pairs}"
    assert len(set(growth)) == len(growth), "'every reef lays down the same' must be false"
    assert len(set(cg.col(table, REEFPH))) == len(cg.col(table, REEFPH)), \
        "'every reef sits in water of the same pH' must be false"
    return (f"sorted by the pH of their water the reefs lay down {growth} millimetres a "
            "year, strictly rising")


def q28(table, item):
    pairs = sorted(zip(cg.col(table, REEFPH), cg.col(table, GROWTH)))
    gap = pairs[-1][1] - pairs[0][1]
    assert abs(gap - 9.4) < 1e-6, f"the difference must be 9.4 millimetres; got {gap}"
    assert gap > 0, "the reef in the highest pH water must lay down the more"
    return (f"the reef in the highest pH water lays down {pairs[-1][1]} millimetres a year "
            f"against {pairs[0][1]} in the lowest, a difference of {gap:.1f}")


def q29(table, item):
    temp = dict(zip(cg.labels(table), cg.col(table, TEMP)))
    ph = dict(zip(cg.labels(table), cg.col(table, WATERPH)))
    white = dict(zip(cg.labels(table), cg.col(table, WHITE)))
    skel = dict(zip(cg.labels(table), cg.col(table, SKELETON)))
    for tank in ("Tank W", "Tank A", "Tank C"):
        assert tank in temp, f"the record must carry {tank}"

    # The design: W differs from the control in temperature alone, A in pH alone.
    warmed_is_hottest = temp["Tank W"] > temp["Tank A"] and temp["Tank W"] > temp["Tank C"]
    acid_is_lowest_ph = ph["Tank A"] < ph["Tank W"] and ph["Tank A"] < ph["Tank C"]
    assert warmed_is_hottest, f"Tank W must be the warmed one; got {temp}"
    assert acid_is_lowest_ph, f"Tank A must be the acidified one; got {ph}"
    assert abs(temp["Tank A"] - temp["Tank C"]) < 1e-9, \
        "the acidified tank must sit at the control's temperature"
    assert abs(ph["Tank W"] - ph["Tank C"]) < 1e-9, \
        "the warmed tank must sit at the control's pH"

    # Named booleans rather than parallel tuples: the one inverted check this
    # project has already paid for was two lists that read as parallel and were not.
    warmed_turned_white = white["Tank W"] > 10 * white["Tank C"]
    acid_stayed_coloured = white["Tank A"] < 2 * white["Tank C"]
    warmed_kept_skeleton = skel["Tank W"] > 0.8 * skel["Tank C"]
    acid_lost_skeleton = skel["Tank A"] < 0.5 * skel["Tank C"]
    assert warmed_turned_white, f"the warmed tank must have turned white; got {white}"
    assert acid_stayed_coloured, f"the acidified tank must not have turned white; got {white}"
    assert warmed_kept_skeleton, f"the warmed tank must still lay down skeleton; got {skel}"
    assert acid_lost_skeleton, f"the acidified tank must lay down far less; got {skel}"
    return (f"against the control's {white['Tank C']:.0f} percent white and "
            f"{skel['Tank C']} grams of skeleton, the warmed tank turned "
            f"{white['Tank W']:.0f} percent white while laying down {skel['Tank W']} "
            f"grams, and the acidified tank stayed at {white['Tank A']:.0f} percent white "
            f"while laying down only {skel['Tank A']} grams")


CLAIMS = [
 ("decrease in pH of the oceans",
  "STB-4.H.1, near verbatim: ocean acidification is the decrease in pH of the oceans. The anchor carries the direction because the rejected option is the same phrase with increase in place of decrease."),
 ("Increased carbon dioxide concentrations in the atmosphere",
  "STB-4.H.1 states that the decrease in pH is primarily due to increased CO2 concentrations in the atmosphere. The loss of calcium carbonate is a consequence the framework attaches to acidification rather than its cause."),
 ("expressed as chemical equations",
  "STB-4.H.1 ends by stating that ocean acidification can be expressed as chemical equations. The statement supplies none of them, so nothing beyond the fact that it can be so expressed is available to key -- and no equation is written anywhere in this module, since the subject is exported untypeset."),
 ("They become more acidic",
  "STB-4.H.2 states that as more CO2 is released into the atmosphere, the oceans, which absorb a large part of that CO2, become more acidic."),
 ("absorb a large part of it",
  "STB-4.H.2 describes the oceans as absorbing a large part of the carbon dioxide released into the atmosphere, which is why a change in the air reaches the water at all. It gives no figure for that part."),
 ("Burning of fossil fuels, vehicle emissions, and deforestation",
  "STB-4.H.3, near verbatim: the anthropogenic activities that contribute to ocean acidification are burning of fossil fuels, vehicle emissions, and deforestation."),
 ("dumping of plastic waste at sea",
  "STB-4.H.3 names burning of fossil fuels, vehicle emissions and deforestation, which the four rejected options restate in one wording or another. Plastic waste appears nowhere in this topic's statements."),
 ("lead to increased carbon dioxide concentrations in the atmosphere",
  "STB-4.H.3 describes the contributing activities as those that lead to increased CO2 concentrations in the atmosphere, and then names three of them. It offers no further mechanism, so nothing more can be keyed to it."),
 ("chief cause, without ruling out that anything else contributes",
  "The hedge PRIMARILY in STB-4.H.1 marks increased atmospheric carbon dioxide as the chief cause of the decrease in pH without asserting that it is the only one, and without casting doubt on it."),
 ("making it difficult for them to form shells",
  "STB-4.H.4 states that ocean acidification damages coral because acidification makes it difficult for them to form shells. The loss of algae within corals is what STB-4.G.3 calls bleaching, under ocean warming, and is a different process."),
 ("loss of calcium carbonate",
  "STB-4.H.4 attributes the difficulty in forming shells to the loss of calcium carbonate. The loss of algae belongs to the framework's account of bleaching under ocean warming."),
 ("defines ocean acidification as a decrease in the pH",
  "STB-4.H.1 states that ocean acidification is the decrease in pH of the oceans, so the direction in the student's account is the reverse of the framework's."),
 ("bleaching, which the framework attributes to warming through the loss of algae; acidification instead makes shell formation difficult through the loss of calcium carbonate",
  "STB-4.G.3 makes bleaching, the loss of algae within corals, the damage caused by ocean warming, while STB-4.H.4 makes the difficulty in forming shells, through the loss of calcium carbonate, the damage caused by acidification. The anchor carries both processes with their own mechanisms, because one rejected option is that sentence with the two exchanged."),
 ("whitened reef to ocean warming through the loss of algae, and the skeleton-poor reef to acidification through the loss of calcium carbonate",
  "STB-4.G.3 attributes corals turning white through the loss of algae to ocean warming, and STB-4.H.4 attributes the difficulty in forming shells through the loss of calcium carbonate to acidification. The anchor pairs each observation with its own process, because the rejected option swaps the pairing."),
 ("caused primarily by a rise in the temperature of the ocean",
  "STB-4.H.1 attributes the decrease in pH primarily to increased carbon dioxide concentrations in the atmosphere, not to a rise in temperature. The four rejected options restate STB-4.H.1, STB-4.H.2, STB-4.H.3 and STB-4.H.4."),
 ("naming burning of fossil fuels among the activities",
  "STB-4.H.3 names burning of fossil fuels among the anthropogenic activities contributing to ocean acidification by leading to increased CO2 concentrations in the atmosphere, and coal fired generation is such burning."),
 ("released into the atmosphere and of the pH of the ocean over the same years",
  "STB-4.H.2 asserts that the oceans grow more acidic as more carbon dioxide is released, so the evidence bearing on it follows both quantities over the same period rather than either one alone."),
 ("pH of the water at that site, measured over a period of years",
  "STB-4.H.1 defines ocean acidification as the decrease in pH of the oceans, so a record of pH over time speaks to the definition directly, while temperature, depth, catch and cloud do not appear in it."),
 ("the pH falls at every decade",
  "Recomputed in q19 above: in decade order the carbon dioxide rises at every step while the surface pH falls at every step. STB-4.H.1 defines acidification as a decrease in pH primarily due to increased atmospheric carbon dioxide."),
 ("It fell by 0.08",
  "Recomputed in q20 above: the first and last entries of the pH column differ by 0.08, downward. STB-4.H.1 makes a decrease in pH the definition of ocean acidification, so the direction is part of the key."),
 ("the more the ocean takes up",
  "Recomputed in q21 above: sorting the years by the amount released leaves the uptake strictly rising, and each year's uptake is a part of that year's release rather than all or none of it. STB-4.H.2 describes the oceans as absorbing a large part of the carbon dioxide released."),
 ("30 percent, the same share in every year",
  "Recomputed in q22 above: dividing each year's uptake by that year's release gives the same figure in all four years. STB-4.H.2 says the oceans absorb a large part without giving a number, so the share is read from the record."),
 ("Burning fossil fuels in power stations",
  "Recomputed in q23 above: the largest and uniquely largest entry in the emissions column belongs to that activity. STB-4.H.3 names burning of fossil fuels among the activities contributing to ocean acidification by raising atmospheric carbon dioxide."),
 ("Generating electricity from wind and sunlight",
  "Recomputed in q24 above: three rows of the record are the three activities STB-4.H.3 names and each adds a positive amount, while the fourth adds none and is not among them."),
 ("less calcium carbonate is available and less skeleton is laid down",
  "Recomputed in q25 above: sorting the tanks by pH leaves both the calcium carbonate available and the skeleton laid down strictly rising, so both fall as the pH does. STB-4.H.4 states that acidification makes shell formation difficult due to the loss of calcium carbonate."),
 ("Tank 4, which held the lowest pH and the least available calcium carbonate",
  "Recomputed in q26 above: the least skeleton, the lowest pH and the least available calcium carbonate all fall in the same row, which is the pairing STB-4.H.4's account predicts."),
 ("lowest pH water lay down the least skeleton",
  "Recomputed in q27 above: sorting the reefs by the pH of their water leaves the skeleton laid down strictly rising, with no ties in either column. STB-4.H.4 ties the difficulty in forming shells to acidification."),
 ("9.4 millimetres more each year",
  "Recomputed in q28 above: the reefs in the highest and lowest pH water differ by 9.4 millimetres a year, the higher pH laying down the more. STB-4.H.4 makes that the relevant comparison."),
 ("warmed tank turned white while laying down normal skeleton, and the lowered pH tank laid down little skeleton",
  "Recomputed in q29 above: against a control at the usual temperature and pH, the warmed tank differs in colour alone and the acidified tank in skeleton alone. STB-4.G.3 attributes the turning white to warming through the loss of algae and STB-4.H.4 the failure to build skeleton to acidification through the loss of calcium carbonate. The anchor carries both halves because the rejected option swaps them."),
 ("damages coral by making shell formation difficult through the loss of calcium carbonate",
  "STB-4.H.1 supplies the definition and the primary cause, STB-4.H.2 the absorption of a large part of the released carbon dioxide, STB-4.H.3 the three named activities and what they have in common, and STB-4.H.4 the damage to coral and its mechanism. Bleaching belongs to the framework's separate statement on ocean warming, which is what one rejected summary imports."),
]

TABLE_CHECKS = {19: q19, 20: q20, 21: q21, 22: q22, 23: q23, 24: q24, 25: q25,
                26: q26, 27: q27, 28: q28, 29: q29}

if "--selftest" in sys.argv:
    es.selftest(e9_7, CLAIMS, TABLE_CHECKS)

e_check.run(e9_7, CLAIMS, TABLE_CHECKS)
