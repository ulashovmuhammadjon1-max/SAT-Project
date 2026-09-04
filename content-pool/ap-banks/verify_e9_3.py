"""Key audit for AP ENVIRONMENTAL SCIENCE 9.3 The Greenhouse Effect.

One (anchor, claim) per item, in module order; the anchor must appear in the
keyed choice and in no distractor. `cg_check.check` is the structural gate and
`es_check` carries the notation gate and the negative control.

WHAT THE KEYS REST ON
---------------------
  STB-4.C.1  the principal greenhouse gases are carbon dioxide, methane, water
             vapor, nitrous oxide and chlorofluorocarbons -- items 1, 9, 14,
             29;
  STB-4.C.2  water vapor is a greenhouse gas but does not contribute
             significantly because its residence time is short -- items 2, 7,
             10, 14, 21, 27;
  STB-4.C.3  the greenhouse effect results in the surface temperature necessary
             for life on Earth to exist -- items 4, 11, 12, 25;
  STB-4.D.1  carbon dioxide has a GWP of 1 and is the reference; CFCs have the
             highest GWP, followed by nitrous oxide, then methane -- items 3,
             5, 6, 8, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 26, 28.
Item 30 joins all four.

SCOPE. The threats posed by an INCREASE in greenhouse gases are keyed in 9.4
under STB-4.E.1 and the effects of climate change in 9.5 under STB-4.F. No key
here states a consequence of excess greenhouse gases.

THE TWO ERRORS THIS TOPIC INVITES are both put in front of the student and both
refused by a key: item 12 refuses the reading that the greenhouse effect is
itself the problem, and items 14, 21 and 27 refuse both halves of the water
vapor mistake -- denying that it is a greenhouse gas, and making it the leading
contributor.

NOT KEYED: no atmospheric concentration, no numeric GWP or residence time
presented as the framework's own, and no source attributed to a gas beyond what
STB-4.D.1 supports. The numbers in the tables are the items' own stimulus and
every one of them is recomputed below.

DATA ITEMS: 3, 7, 11, 15, 19 and 23 carry tables. Items 15, 19 and 23 turn on a
product that the verifier recomputes rather than asserts, and item 11 on a
difference. Temperatures are in kelvins so that no cell needs a minus sign.

NEGATIVE CONTROL: `python3 verify_e9_3.py --selftest`.
"""
import sys

import cg_check as cg
import es_check as es
import e9_3

GWP = "Warming potential compared with the same mass of carbon dioxide"
RESID = "Average time a molecule stays in the atmosphere (years)"
SHARE = "Share of the long term warming attributed to it (percent)"
TEMP = "Average surface temperature (kelvins)"
MASS = "Mass released (tons)"


def q3(table, item):
    gases = [g.strip().lower() for g in cg.labels(table)]
    gwp = cg.col(table, GWP)
    order = [g for _, g in sorted(zip(gwp, gases), reverse=True)]
    assert order[:3] == ["chlorofluorocarbon", "nitrous oxide", "methane"], \
        f"the top three do not run chlorofluorocarbon, nitrous oxide, methane: {order}"
    co2 = gases.index("carbon dioxide")
    assert gwp[co2] == 1.0, f"carbon dioxide is not set at one: {gwp[co2]}"
    assert gwp[co2] == min(gwp), "carbon dioxide is not the smallest value in the table"
    assert len(set(gwp)) == len(gwp), "'all four the same' must be false"
    return (f"sorted by warming potential the gases run {order}, with carbon dioxide fixed "
            f"at {gwp[co2]:.0f} as the reference")


def q7(table, item):
    gases = [g.strip().lower() for g in cg.labels(table)]
    resid = cg.col(table, RESID)
    share = cg.col(table, SHARE)
    w = gases.index("water vapor")
    assert resid[w] == min(resid), f"water vapor is not the shortest lived: {resid}"
    assert min(r for i, r in enumerate(resid) if i != w) > 100 * resid[w], \
        f"water vapor's residence time is not shorter by orders of magnitude: {resid}"
    assert share[w] == min(share), f"water vapor does not carry the smallest share: {share}"
    longest = resid.index(max(resid))
    assert share[longest] != min(share), \
        "'the longest lived gas carries the smallest share' must be false"
    return (f"water vapor stays {resid[w]} years against {[r for i, r in enumerate(resid) if i != w]} "
            f"for the others and carries {share[w]:.0f} percent of the warming, the smallest share")


def q11(table, item):
    conditions = cg.labels(table)
    temp = cg.col(table, TEMP)
    withg = [i for i, c in enumerate(conditions) if "no greenhouse" not in c.lower()]
    without = [i for i, c in enumerate(conditions) if "no greenhouse" in c.lower()]
    assert len(withg) == 1 and len(without) == 1, \
        f"the two conditions are not one with and one without greenhouse gases: {conditions}"
    a, b = withg[0], without[0]
    diff = temp[a] - temp[b]
    assert diff > 10, f"the difference is {diff}, not tens of kelvins"
    assert diff < 100, f"the difference is {diff}, larger than this item claims"
    return (f"the modeled surface runs {temp[a]:.0f} kelvins with greenhouse gases against "
            f"{temp[b]:.0f} without, a difference of {diff:.0f} kelvins")


def _equivalents(table):
    mass = cg.col(table, MASS)
    gwp = cg.col(table, GWP)
    return [m * g for m, g in zip(mass, gwp)], mass, gwp


def q15(table, item):
    names = [n.strip().lower() for n in cg.labels(table)]
    eq, mass, gwp = _equivalents(table)
    top = eq.index(max(eq))
    assert names[top] == "release 2", \
        f"the largest equivalent belongs to {names[top]}, not the second row"
    assert abs(eq[top] - 280) < 1e-6, \
        f"the largest equivalent is {eq[top]:.0f} tons, not two hundred eighty"
    assert len(set(eq)) == len(eq), "two releases give the same equivalent"
    assert eq[names.index("release 1")] != max(eq), \
        "'the first release is the largest' must be false"
    return (f"the carbon dioxide equivalents are {[round(e) for e in eq]} tons, the largest "
            f"being {names[top]} at {eq[top]:.0f}")


def q19(table, item):
    gases = [g.strip().lower() for g in cg.labels(table)]
    eq, mass, gwp = _equivalents(table)
    co2 = gases.index("carbon dioxide")
    assert eq[co2] == max(eq), \
        f"carbon dioxide is not the largest equivalent: {[round(e) for e in eq]}"
    assert gwp[co2] == min(gwp), "carbon dioxide is not the smallest warming potential here"
    assert eq[co2] > 0, "'carbon dioxide contributes nothing' must be false"
    others = [i for i in range(len(gases)) if i != co2]
    assert all(eq[co2] > eq[i] for i in others), "some other gas matches or exceeds it"
    return (f"the equivalents are {[round(e) for e in eq]} tons, largest for carbon dioxide "
            f"despite its potential of {gwp[co2]:.0f}, the smallest in the table")


def q23(table, item):
    gases = [g.strip().lower() for g in cg.labels(table)]
    eq, mass, gwp = _equivalents(table)
    cfc = [i for i, g in enumerate(gases) if "chlorofluorocarbon" in g][0]
    co2 = gases.index("carbon dioxide")
    assert mass[cfc] < mass[co2], "the chlorofluorocarbon is not the smaller release by mass"
    assert eq[cfc] > eq[co2], \
        f"the chlorofluorocarbon does not outweigh the carbon dioxide: {eq[cfc]} against {eq[co2]}"
    assert eq[cfc] > 0, "'it contributes nothing' must be false"
    return (f"one ton of the chlorofluorocarbon is {eq[cfc]:.0f} tons of carbon dioxide "
            f"equivalent against {eq[co2]:.0f} for {mass[co2]:.0f} tons of carbon dioxide")


CLAIMS = [
 ("Carbon dioxide, methane, water vapor, nitrous oxide and chlorofluorocarbons",
  "STB-4.C.1 verbatim: the principal greenhouse gases are carbon dioxide, methane, water vapor, nitrous oxide and chlorofluorocarbons. The rejected options list the constituents of dry air, the unit 7 air pollutants, or part of the list."),
 ("does not contribute significantly because it has a short residence time",
  "STB-4.C.2 verbatim in substance: while water vapor is a greenhouse gas, it does not contribute significantly to global climate change because it has a short residence time in the atmosphere. The framework neither excludes it nor makes it the largest contributor."),
 ("largest potential, followed by nitrous oxide, then methane, with carbon dioxide at one",
  "Recomputed in q3 above: sorting the table by warming potential gives chlorofluorocarbon, nitrous oxide, methane, with carbon dioxide at exactly one and smallest. That is the order and the reference point STB-4.D.1 states."),
 ("surface temperature necessary for life on Earth to exist",
  "STB-4.C.3 verbatim: the greenhouse effect results in the surface temperature necessary for life on Earth to exist. Ozone depletion, ozone formation and ocean circulation belong to other statements."),
 ("global warming potential of one and is used as the reference point",
  "STB-4.D.1 states that carbon dioxide, which has a global warming potential of 1, is used as a reference point for the comparison of different greenhouse gases and their impacts on global climate change."),
 ("Chlorofluorocarbons highest, followed by nitrous oxide, then methane",
  "STB-4.D.1 states that chlorofluorocarbons have the highest GWP, followed by nitrous oxide, then methane. Each rejected option rearranges or denies that order."),
 ("shortest residence time and the smallest share of the long term warming",
  "Recomputed in q7 above: water vapor's residence time is shorter than every other row by more than a hundredfold and its share of the warming is the smallest, while the longest lived gas is not the smallest contributor. That is STB-4.C.2's reason."),
 ("Expressing each gas relative to one common gas",
  "STB-4.D.1 states that carbon dioxide is used as a reference point for the comparison of different greenhouse gases and their impacts, and it assigns the highest potential to chlorofluorocarbons rather than to the reference."),
 ("Sulfur dioxide",
  "STB-4.C.1 names carbon dioxide, methane, water vapor, nitrous oxide and chlorofluorocarbons, so sulfur dioxide, an air pollutant treated in unit 7, is the one option not on the list."),
 ("stays in the atmosphere only briefly before it leaves",
  "STB-4.C.2 attributes water vapor's limited contribution to its short residence time in the atmosphere, which concerns how long the gas remains rather than where it is found or what produces it."),
 ("tens of kelvins warmer than the same atmosphere without greenhouse gases",
  "Recomputed in q11 above: subtracting the two rows gives a difference of tens of kelvins in favor of the atmosphere containing greenhouse gases. STB-4.C.3 states that the greenhouse effect produces the surface temperature necessary for life."),
 ("so the effect itself is not the problem",
  "STB-4.C.3 states that the greenhouse effect results in the surface temperature necessary for life on Earth to exist, so the framework treats the effect as a condition of life rather than as a problem in itself."),
 ("small mass can be equivalent to a much larger mass of carbon dioxide",
  "STB-4.D.1 makes global warming potential a comparison against carbon dioxide, with chlorofluorocarbons highest followed by nitrous oxide then methane, so a small mass of a high potential gas can outweigh a larger mass of a low potential one."),
 ("calls water vapor a greenhouse gas and sets it aside only because its residence time",
  "STB-4.C.1 lists water vapor among the principal greenhouse gases and STB-4.C.2 says it does not contribute significantly because its residence time is short, so both halves of the sentence have to be kept."),
 ("The second release, at 280 tons of carbon dioxide equivalent",
  "Recomputed in q15 above: each mass times its warming potential gives the equivalent, and the largest belongs to the second row at exactly the keyed figure, ahead of a close third row. STB-4.D.1 makes carbon dioxide the reference."),
 ("Chlorofluorocarbons, paired with the highest global warming potential",
  "STB-4.D.1 places chlorofluorocarbons highest, followed by nitrous oxide, then methane, with carbon dioxide fixed at one as the reference. Each rejected pairing contradicts that order."),
 ("mass of each gas released together with the warming potential of each gas",
  "STB-4.D.1 makes global warming potential a comparison of gases against carbon dioxide, so the potential converts a mass into a comparable quantity and neither figure suffices alone."),
 ("reference against which the others are measured, so its potential is defined as one",
  "STB-4.D.1 states that carbon dioxide, which has a global warming potential of 1, is used as a reference point, so the value marks the reference rather than an absence of effect or a residence time."),
 ("even though it has the smallest warming potential of the three",
  "Recomputed in q19 above: multiplying each mass by its potential leaves the carbon dioxide row largest despite carrying the smallest potential in the table. STB-4.D.1 makes the potential a per unit comparison, so the mass matters as well."),
 ("comparison against one common reference lets the impacts of different gases be placed on a single scale",
  "STB-4.D.1 states that carbon dioxide is used as a reference point for the comparison of different greenhouse gases and their impacts, and assigns the highest potential to chlorofluorocarbons rather than to carbon dioxide."),
 ("water vapor is the largest contributor to global climate change",
  "STB-4.C.2 states that water vapor does not contribute significantly because of its short residence time, so this is the claim the framework denies. The four rejected options restate STB-4.C.1, STB-4.C.2, STB-4.C.3 and STB-4.D.1."),
 ("nitrous oxide release has the greater warming impact",
  "STB-4.D.1 ranks chlorofluorocarbons highest, followed by nitrous oxide, then methane, so for equal masses the nitrous oxide carries the greater impact and both rank above the reference."),
 ("single ton of the chlorofluorocarbon outweighs a thousand tons of carbon dioxide",
  "Recomputed in q23 above: the chlorofluorocarbon row is the smaller release by mass yet the larger product of mass and potential. STB-4.D.1 gives chlorofluorocarbons the highest potential and fixes carbon dioxide at one."),
 ("smallest of those three, though still above that of carbon dioxide",
  "STB-4.D.1 lists chlorofluorocarbons highest, followed by nitrous oxide, then methane, with carbon dioxide fixed at one, so methane is last of the three ranked above the reference. STB-4.C.1 includes methane among the principal gases."),
 ("lack the temperature the framework says is necessary for life",
  "STB-4.C.3 states that the greenhouse effect results in the surface temperature necessary for life on Earth to exist, so its absence would remove that condition. Ozone in either layer belongs to other statements."),
 ("how much of each gas is released and how potent each gas is relative to carbon dioxide",
  "STB-4.D.1 makes the potential a per unit comparison against carbon dioxide, so the equivalent contribution of a release depends on the mass and the potential together."),
 ("greenhouse gas whose short residence time keeps it from contributing significantly",
  "STB-4.C.2 states that while water vapor is a greenhouse gas, it does not contribute significantly to global climate change because it has a short residence time. Each rejected option drops or reverses one half of that sentence."),
 ("warming impact of two hundred sixty five times that mass of the first",
  "STB-4.D.1 defines global warming potential as a comparison with carbon dioxide, set at one, so the ratio of two potentials is a ratio of impacts per unit mass rather than of residence times or abundances."),
 ("differ from one another in potency and in how long they remain",
  "STB-4.C.1 lists five gases, STB-4.C.2 distinguishes water vapor by its short residence time, and STB-4.D.1 ranks the potencies, so the framework treats them as distinct gases with distinct properties."),
 ("water vapor is set aside for its short residence time",
  "Each clause of the keyed summary is one of STB-4.C.1, STB-4.C.2, STB-4.C.3 and STB-4.D.1. Every rejected summary treats the effect itself as the problem, excludes water vapor from the gases, misplaces carbon dioxide in the ranking, or denies that potencies differ."),
]

TABLE_CHECKS = {3: q3, 7: q7, 11: q11, 15: q15, 19: q19, 23: q23}

es.run(e9_3, CLAIMS, TABLE_CHECKS, sys.argv)
