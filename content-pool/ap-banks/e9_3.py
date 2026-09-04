# AP ENVIRONMENTAL SCIENCE 9.3 The Greenhouse Effect
# CED effective Fall 2026, Unit 9 Global Change. Enduring understanding STB-4, local and
# regional human activities can have impacts at the global level. Learning objectives
# STB-4.C (identify the greenhouse gases) and STB-4.D (identify the sources and potency
# of the greenhouse gases). Suggested skill 1.B, explain environmental concepts and
# processes.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-4.C.1  The principal greenhouse gases are carbon dioxide, methane, water vapor,
#              nitrous oxide, and chlorofluorocarbons (CFCs).
#   STB-4.C.2  While water vapor is a greenhouse gas, it doesn't contribute significantly
#              to global climate change because it has a short residence time in the
#              atmosphere.
#   STB-4.C.3  The greenhouse effect results in the surface temperature necessary for
#              life on Earth to exist.
#   STB-4.D.1  Carbon dioxide, which has a global warming potential (GWP) of 1, is used as
#              a reference point for the comparison of different greenhouse gases and
#              their impacts on global climate change. Chlorofluorocarbons (CFCs) have the
#              highest GWP, followed by nitrous oxide, then methane.
#
# ON SCOPE. Topic 9.4 keys the threats posed by an INCREASE in greenhouse gases
# (STB-4.E.1) and topic 9.5 keys the effects of climate change (STB-4.F). This topic keys
# what the gases are, why water vapor is set aside, what the effect itself does, and how
# the gases are ranked against one another. No key here states a consequence of excess
# greenhouse gases; that is 9.4's content.
#
# TWO ERRORS THIS TOPIC INVITES, and both are deliberately put in front of the student.
# The first is treating the greenhouse effect itself as the problem, when STB-4.C.3 says
# it produces the surface temperature necessary for life. The second is treating water
# vapor as a major driver, when STB-4.C.2 sets it aside for its short residence time
# WITHOUT denying that it is a greenhouse gas.
#
# ON THE FIGURES. The bank carries no images, so every representation is a table. Six
# items carry real numbers and verify_e9_3.py recomputes every product, difference and
# ranking from the table alone. Temperatures are given in kelvins so that no cell needs a
# minus sign, which would print as a bare hyphen in a subject that is not typeset.
#
# NOT KEYED: no concentration for any gas, no numeric GWP presented as the framework's
# own, no residence time presented as the framework's own, and no source attributed to a
# gas beyond what STB-4.D.1 supports.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("9.3", "The Greenhouse Effect", 9)

_T_RANK = dict(
    headers=["Greenhouse gas",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Carbon dioxide", "1.0"],
          ["Methane", "28"],
          ["Nitrous oxide", "265"],
          ["Chlorofluorocarbon", "10900"]])

_T_RESIDENCE = dict(
    headers=["Greenhouse gas", "Average time a molecule stays in the atmosphere (years)",
             "Share of the long term warming attributed to it (percent)"],
    rows=[["Water vapor", "0.030", "2.0"],
          ["Methane", "12", "16"],
          ["Nitrous oxide", "120", "18"],
          ["Carbon dioxide", "100", "64"]])

_T_TEMP = dict(
    headers=["Condition modeled for the Earth",
             "Average surface temperature (kelvins)"],
    rows=[["The atmosphere as it actually is", "288"],
          ["The same atmosphere with no greenhouse gases in it", "255"]])

_T_EQUIV = dict(
    headers=["Release considered", "Mass released (tons)",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Release 1", "100", "1.0"],
          ["Release 2", "10", "28"],
          ["Release 3", "1.0", "265"]])

_T_SOURCE = dict(
    headers=["Gas released by one facility in a year", "Mass released (tons)",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Carbon dioxide", "5000", "1.0"],
          ["Methane", "100", "28"],
          ["Nitrous oxide", "10", "265"]])

_T_TRAP = dict(
    headers=["Gas released by a second facility in a year", "Mass released (tons)",
             "Warming potential compared with the same mass of carbon dioxide"],
    rows=[["Carbon dioxide", "1000", "1.0"],
          ["Chlorofluorocarbon", "1.0", "10900"]])

QUESTIONS = [

 dict(q="Which gases does the framework name as the principal greenhouse gases?",
      choices=[
        "Carbon dioxide, methane, water vapor, nitrous oxide and chlorofluorocarbons",
        "Oxygen, nitrogen, argon, helium and neon",
        "Sulfur dioxide, nitrogen dioxide, carbon monoxide and ground level ozone",
        "Carbon dioxide and methane only",
        "Water vapor and oxygen only"],
      ans=0,
      why="STB-4.C.1 states that the principal greenhouse gases are carbon dioxide, "
          "methane, water vapor, nitrous oxide and chlorofluorocarbons. The rejected "
          "options list the main constituents of dry air, the criteria air pollutants of "
          "unit 7, or an incomplete part of the framework's list."),

 dict(q="What does the framework say about water vapor's contribution to global climate "
        "change?",
      choices=[
        "It is a greenhouse gas, but it does not contribute significantly because it has a "
        "short residence time in the atmosphere",
        "It is not a greenhouse gas at all",
        "It is the largest single contributor to global climate change",
        "It contributes significantly because it remains in the atmosphere for centuries",
        "It contributes only when it is frozen into ice crystals"],
      ans=0,
      why="STB-4.C.2 states that while water vapor is a greenhouse gas, it does not "
          "contribute significantly to global climate change because it has a short "
          "residence time in the atmosphere. The framework neither excludes it from the "
          "gases nor makes it the largest contributor."),

 dict(q="Warming potentials for four gases are listed.",
      table=_T_RANK,
      choices=[
        "The chlorofluorocarbon carries the largest potential, followed by nitrous oxide, "
        "then methane, with carbon dioxide at one",
        "Methane carries the largest potential, followed by nitrous oxide, then the "
        "chlorofluorocarbon",
        "Carbon dioxide carries the largest potential of the four",
        "All four gases carry the same potential",
        "Nitrous oxide carries the largest potential, followed by the chlorofluorocarbon"],
      ans=0,
      why="Sorting the table by warming potential puts the chlorofluorocarbon first, then "
          "nitrous oxide, then methane, with carbon dioxide at one. That is the order "
          "STB-4.D.1 gives, and STB-4.D.1 also fixes carbon dioxide's value at one as the "
          "reference point."),

 dict(q="What does the framework say the greenhouse effect results in?",
      choices=[
        "The surface temperature necessary for life on Earth to exist",
        "The complete loss of life from the surface of the Earth",
        "The depletion of ozone in the stratosphere",
        "The formation of ozone near the ground",
        "The circulation of ocean currents around the globe"],
      ans=0,
      why="STB-4.C.3 states that the greenhouse effect results in the surface temperature "
          "necessary for life on Earth to exist. Ozone depletion, ozone formation and ocean "
          "circulation are described in other statements."),

 dict(q="What role does the framework give carbon dioxide in comparing greenhouse gases?",
      choices=[
        "It has a global warming potential of one and is used as the reference point for "
        "comparing the other gases",
        "It has the highest global warming potential of any greenhouse gas",
        "It has no global warming potential and is excluded from the comparison",
        "It is compared against methane, which serves as the reference point",
        "It is the only greenhouse gas whose potential can be measured"],
      ans=0,
      why="STB-4.D.1 states that carbon dioxide, which has a global warming potential of 1, "
          "is used as a reference point for the comparison of different greenhouse gases "
          "and their impacts on global climate change."),

 dict(q="In what order does the framework rank the global warming potentials of the gases "
        "it names?",
      choices=[
        "Chlorofluorocarbons highest, followed by nitrous oxide, then methane",
        "Methane highest, followed by nitrous oxide, then chlorofluorocarbons",
        "Nitrous oxide highest, followed by methane, then chlorofluorocarbons",
        "Carbon dioxide highest, followed by chlorofluorocarbons, then methane",
        "All of the gases share the same potential, so no order exists"],
      ans=0,
      why="STB-4.D.1 states that chlorofluorocarbons have the highest global warming "
          "potential, followed by nitrous oxide, then methane. Each rejected option "
          "rearranges that order or denies it."),

 dict(q="Residence times and shares of long term warming are listed for four gases.",
      table=_T_RESIDENCE,
      choices=[
        "Water vapor has by far the shortest residence time and the smallest share of the "
        "long term warming of the four gases listed",
        "Water vapor has the longest residence time and the largest share of the warming",
        "All four gases have the same residence time",
        "Water vapor has the shortest residence time but the largest share of the warming",
        "The gas with the longest residence time carries the smallest share of the warming"],
      ans=0,
      why="The water vapor row carries the smallest residence time by orders of magnitude "
          "and the smallest share of the warming. STB-4.C.2 states that water vapor does "
          "not contribute significantly to global climate change because it has a short "
          "residence time in the atmosphere."),

 dict(q="Why is a single gas used as the reference point when the potencies of greenhouse "
        "gases are compared?",
      choices=[
        "Expressing each gas relative to one common gas makes the impacts of different "
        "gases directly comparable",
        "Only one gas can be measured in the atmosphere at a time",
        "The reference gas is the only one that causes any warming",
        "The other gases have no measurable effect on the climate",
        "The reference gas is chosen because it has the highest potency"],
      ans=0,
      why="STB-4.D.1 states that carbon dioxide is used as a reference point for the "
          "comparison of different greenhouse gases and their impacts on global climate "
          "change, and it assigns carbon dioxide the value one rather than the highest "
          "value, which STB-4.D.1 gives to chlorofluorocarbons."),

 dict(q="Which of the following is NOT one of the principal greenhouse gases the framework "
        "names?",
      choices=[
        "Sulfur dioxide",
        "Methane",
        "Nitrous oxide",
        "Water vapor",
        "Chlorofluorocarbons"],
      ans=0,
      why="STB-4.C.1 names carbon dioxide, methane, water vapor, nitrous oxide and "
          "chlorofluorocarbons. Sulfur dioxide is an air pollutant treated in unit 7 and "
          "does not appear on this list."),

 dict(q="What does a short residence time in the atmosphere mean for a gas?",
      choices=[
        "An average molecule of the gas stays in the atmosphere only briefly before it "
        "leaves",
        "An average molecule of the gas stays in the atmosphere for centuries",
        "The gas cannot absorb any energy while it is in the atmosphere",
        "The gas is present only at high altitudes",
        "The gas is produced only by human activity"],
      ans=0,
      why="STB-4.C.2 attributes water vapor's limited contribution to its short residence "
          "time in the atmosphere, which is a statement about how long the gas remains "
          "rather than about where it is found or what produces it."),

 dict(q="Two modeled conditions for the Earth are compared.",
      table=_T_TEMP,
      choices=[
        "The atmosphere as it actually is gives a surface temperature tens of kelvins "
        "warmer than the same atmosphere without greenhouse gases",
        "The atmosphere as it actually is gives a colder surface than the same atmosphere "
        "without greenhouse gases",
        "The two conditions give the same surface temperature",
        "The difference between the two conditions is less than one kelvin",
        "The condition without greenhouse gases gives the warmer surface"],
      ans=0,
      why="Subtracting one row from the other gives a difference of tens of kelvins in "
          "favor of the atmosphere that contains greenhouse gases. STB-4.C.3 states that "
          "the greenhouse effect results in the surface temperature necessary for life on "
          "Earth to exist."),

 dict(q="A student writes that the greenhouse effect is itself an environmental problem "
        "that should be eliminated. What is the clearest correction from the framework?",
      choices=[
        "The greenhouse effect results in the surface temperature necessary for life on "
        "Earth to exist, so the effect itself is not the problem",
        "The greenhouse effect has no influence on the surface temperature of the Earth",
        "The greenhouse effect cools the surface of the Earth",
        "The greenhouse effect is caused only by water vapor",
        "The greenhouse effect occurs only in the stratosphere"],
      ans=0,
      why="STB-4.C.3 states that the greenhouse effect results in the surface temperature "
          "necessary for life on Earth to exist, so the framework treats the effect as a "
          "condition of life rather than as a problem in itself."),

 dict(q="Why can a gas released in a small quantity still matter for global climate "
        "change?",
      choices=[
        "Its warming potential can be many times that of carbon dioxide, so a small mass "
        "can be equivalent to a much larger mass of carbon dioxide",
        "Its warming potential is always one, the same as carbon dioxide",
        "Small releases are always more damaging than large ones",
        "Its residence time in the atmosphere must be short",
        "Only the mass released matters, and never the gas involved"],
      ans=0,
      why="STB-4.D.1 makes global warming potential a comparison against carbon dioxide, "
          "with chlorofluorocarbons highest followed by nitrous oxide then methane, so a "
          "small mass of a high potential gas can outweigh a larger mass of a low potential "
          "one."),

 dict(q="A student says water vapor is not a greenhouse gas because the framework says it "
        "does not contribute significantly. What is the precise correction?",
      choices=[
        "The framework calls water vapor a greenhouse gas and sets it aside only because "
        "its residence time in the atmosphere is short",
        "The framework does exclude water vapor from the greenhouse gases",
        "The framework says water vapor contributes more than any other gas",
        "The framework says water vapor has the longest residence time of any greenhouse "
        "gas",
        "The framework says water vapor is a pollutant rather than a greenhouse gas"],
      ans=0,
      why="STB-4.C.1 lists water vapor among the principal greenhouse gases and STB-4.C.2 "
          "states that while water vapor is a greenhouse gas, it does not contribute "
          "significantly to global climate change because it has a short residence time. "
          "Both halves have to be kept."),

 dict(q="Three releases of different gases are compared. Which contributes the most in "
        "carbon dioxide equivalent terms?",
      table=_T_EQUIV,
      choices=[
        "The second release, at 280 tons of carbon dioxide equivalent",
        "The first release, at 280 tons of carbon dioxide equivalent",
        "The third release, at 280 tons of carbon dioxide equivalent",
        "The first release, at 100 tons of carbon dioxide equivalent, which is the largest",
        "All three releases are equivalent to the same amount of carbon dioxide"],
      ans=0,
      why="Multiplying each mass by its warming potential gives the carbon dioxide "
          "equivalent of each release, and the largest product belongs to the second row. "
          "STB-4.D.1 makes carbon dioxide the reference against which the other gases are "
          "compared."),

 dict(q="Which pairing of a gas with its place in the framework's ranking is correct?",
      choices=[
        "Chlorofluorocarbons, paired with the highest global warming potential",
        "Methane, paired with the highest global warming potential",
        "Carbon dioxide, paired with the highest global warming potential",
        "Nitrous oxide, paired with a potential below that of methane",
        "Carbon dioxide, paired with a potential above that of nitrous oxide"],
      ans=0,
      why="STB-4.D.1 places chlorofluorocarbons highest, followed by nitrous oxide, then "
          "methane, with carbon dioxide fixed at one as the reference. Each rejected "
          "pairing contradicts that order."),

 dict(q="What is needed in order to compare the climate impact of releasing two different "
        "greenhouse gases?",
      choices=[
        "The mass of each gas released together with the warming potential of each gas",
        "The mass of each gas released alone",
        "The warming potential of each gas alone",
        "The residence time of each gas alone",
        "The number of facilities releasing each gas"],
      ans=0,
      why="STB-4.D.1 makes global warming potential a comparison of gases against carbon "
          "dioxide, so the potential converts a mass into a comparable quantity and neither "
          "the mass nor the potential is sufficient by itself."),

 dict(q="Which statement best explains what a global warming potential of one means?",
      choices=[
        "That gas is the reference against which the others are measured, so its potential "
        "is defined as one",
        "That gas has no effect on the climate at all",
        "That gas is the most potent of the greenhouse gases",
        "That gas remains in the atmosphere for exactly one year",
        "That gas makes up one percent of the atmosphere"],
      ans=0,
      why="STB-4.D.1 states that carbon dioxide, which has a global warming potential of 1, "
          "is used as a reference point for the comparison of different greenhouse gases, "
          "so the value one marks the reference rather than an absence of effect or a "
          "residence time."),

 dict(q="One facility's yearly releases are listed.",
      table=_T_SOURCE,
      choices=[
        "Carbon dioxide contributes the most in carbon dioxide equivalent terms even though "
        "it has the smallest warming potential of the three",
        "Nitrous oxide contributes the most in carbon dioxide equivalent terms because its "
        "potential is largest",
        "Methane contributes the most in carbon dioxide equivalent terms",
        "The three gases contribute equally in carbon dioxide equivalent terms",
        "Carbon dioxide contributes nothing because its potential is only one"],
      ans=0,
      why="Multiplying each mass by its potential shows the carbon dioxide row with the "
          "largest product despite carrying the smallest potential. STB-4.D.1 makes the "
          "potential a comparison per unit mass, so the mass released matters as well."),

 dict(q="Why does the framework express the potency of a greenhouse gas as a comparison "
        "with carbon dioxide rather than as an absolute quantity?",
      choices=[
        "A comparison against one common reference lets the impacts of different gases be "
        "placed on a single scale",
        "Carbon dioxide is the only gas whose effect can be measured",
        "The other gases have no effect until carbon dioxide is present",
        "The comparison is arbitrary and carries no meaning",
        "Carbon dioxide has the highest potency, so it sets the upper limit"],
      ans=0,
      why="STB-4.D.1 states that carbon dioxide is used as a reference point for the "
          "comparison of different greenhouse gases and their impacts on global climate "
          "change, and it assigns the highest potential to chlorofluorocarbons rather than "
          "to carbon dioxide."),

 dict(q="Which of the following does the framework NOT state in this topic?",
      choices=[
        "That water vapor is the largest contributor to global climate change",
        "That water vapor is a greenhouse gas",
        "That the greenhouse effect gives the Earth a surface temperature that allows life",
        "That chlorofluorocarbons have the highest global warming potential",
        "That carbon dioxide serves as the reference for comparing greenhouse gases"],
      ans=0,
      why="STB-4.C.2 states that water vapor does not contribute significantly to global "
          "climate change because of its short residence time, so calling it the largest "
          "contributor contradicts the framework. The four rejected options restate "
          "STB-4.C.1, STB-4.C.2, STB-4.C.3 and STB-4.D.1."),

 dict(q="Two facilities each release one ton of a gas, one releasing nitrous oxide and the "
        "other methane. What does the framework's ranking imply?",
      choices=[
        "The nitrous oxide release has the greater warming impact, because nitrous oxide "
        "ranks above methane",
        "The methane release has the greater warming impact, because methane ranks above "
        "nitrous oxide",
        "The two releases have identical warming impacts",
        "Neither release has any warming impact",
        "The comparison cannot be made because both gases are ranked below carbon dioxide"],
      ans=0,
      why="STB-4.D.1 ranks chlorofluorocarbons highest, followed by nitrous oxide, then "
          "methane, so for equal masses the nitrous oxide carries the greater impact. Both "
          "gases rank above carbon dioxide, which is set at one."),

 dict(q="A second facility's yearly releases are listed.",
      table=_T_TRAP,
      choices=[
        "The single ton of the chlorofluorocarbon outweighs a thousand tons of carbon "
        "dioxide in equivalent terms",
        "The thousand tons of carbon dioxide outweighs the chlorofluorocarbon in equivalent "
        "terms",
        "The two releases are equivalent to the same amount of carbon dioxide",
        "The chlorofluorocarbon contributes nothing because so little of it is released",
        "Neither release can be expressed in carbon dioxide equivalent terms"],
      ans=0,
      why="Multiplying each mass by its warming potential makes the single ton of the "
          "chlorofluorocarbon the larger product. STB-4.D.1 gives chlorofluorocarbons the "
          "highest global warming potential and makes carbon dioxide the reference at one."),

 dict(q="Why does the framework's ranking put methane last among the three gases it "
        "compares with carbon dioxide?",
      choices=[
        "Its global warming potential is the smallest of those three, though still above "
        "that of carbon dioxide",
        "Its global warming potential is smaller than that of carbon dioxide",
        "It is not a greenhouse gas at all",
        "It has the shortest residence time of any greenhouse gas",
        "It is the reference point against which the others are measured"],
      ans=0,
      why="STB-4.D.1 lists chlorofluorocarbons highest, followed by nitrous oxide, then "
          "methane, with carbon dioxide fixed at one as the reference, so methane is last "
          "of the three ranked above the reference. STB-4.C.1 includes methane among the "
          "principal greenhouse gases."),

 dict(q="What would the framework's account predict if the greenhouse effect did not occur "
        "at all?",
      choices=[
        "The surface would lack the temperature the framework says is necessary for life "
        "on Earth to exist",
        "The surface would be warmer than it is now",
        "The surface temperature would be unchanged",
        "The stratospheric ozone layer would be depleted",
        "Ozone would build up near the ground"],
      ans=0,
      why="STB-4.C.3 states that the greenhouse effect results in the surface temperature "
          "necessary for life on Earth to exist, so its absence would remove that "
          "condition. Ozone in either layer belongs to other statements."),

 dict(q="A regulator can reduce the release of only one gas from a facility and wants the "
        "largest reduction in carbon dioxide equivalent terms. What must be considered?",
      choices=[
        "Both how much of each gas is released and how potent each gas is relative to "
        "carbon dioxide",
        "Only how much of each gas is released",
        "Only how potent each gas is relative to carbon dioxide",
        "Only which gas has the shortest residence time",
        "Only which gas was discovered first"],
      ans=0,
      why="STB-4.D.1 makes the potential a per unit comparison against carbon dioxide, so "
          "the equivalent contribution of a release depends on the mass and the potential "
          "together."),

 dict(q="Which statement about water vapor is exactly what the framework says?",
      choices=[
        "It is a greenhouse gas whose short residence time keeps it from contributing "
        "significantly to global climate change",
        "It is not a greenhouse gas and therefore contributes nothing",
        "It is a greenhouse gas whose long residence time makes it the leading contributor",
        "It is a greenhouse gas that contributes significantly despite a short residence "
        "time",
        "It is a greenhouse gas only when the air is cold enough for it to condense"],
      ans=0,
      why="STB-4.C.2 states that while water vapor is a greenhouse gas, it does not "
          "contribute significantly to global climate change because it has a short "
          "residence time in the atmosphere. Each rejected option drops or reverses one "
          "half of that sentence."),

 dict(q="Two gases have global warming potentials of 1 and 265. What does that pair of "
        "numbers say?",
      choices=[
        "A given mass of the second gas has the warming impact of two hundred sixty five "
        "times that mass of the first",
        "A given mass of the first gas has the warming impact of two hundred sixty five "
        "times that mass of the second",
        "The two gases have the same warming impact per unit mass",
        "The second gas remains in the atmosphere two hundred sixty five times as long",
        "The second gas makes up two hundred sixty five times as much of the atmosphere"],
      ans=0,
      why="STB-4.D.1 defines global warming potential as a comparison with carbon dioxide, "
          "which is set at one, so the ratio of the two numbers is a ratio of impacts per "
          "unit mass rather than of residence times or abundances."),

 dict(q="Why does the framework name five principal greenhouse gases rather than one?",
      choices=[
        "Several different gases contribute to the effect, and they differ from one another "
        "in potency and in how long they remain",
        "The five gases are five names for the same molecule",
        "Only one of the five actually absorbs energy and the rest are listed by mistake",
        "The five gases all have identical warming potentials",
        "The five gases all have identical residence times in the atmosphere"],
      ans=0,
      why="STB-4.C.1 lists five gases, STB-4.C.2 distinguishes water vapor by its short "
          "residence time, and STB-4.D.1 ranks the potencies of several of them, so the "
          "framework treats them as distinct gases with distinct properties."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "The principal greenhouse gases are carbon dioxide, methane, water vapor, nitrous "
        "oxide and chlorofluorocarbons, water vapor is set aside for its short residence "
        "time, the effect itself gives the Earth the surface temperature life requires, and "
        "potencies are compared against carbon dioxide, with chlorofluorocarbons highest, "
        "then nitrous oxide, then methane",
        "The greenhouse effect makes the Earth uninhabitable and should be eliminated "
        "entirely",
        "Water vapor is excluded from the greenhouse gases because it is not one",
        "Carbon dioxide has the highest global warming potential of any greenhouse gas",
        "All greenhouse gases have the same potency, so only the mass released matters"],
      ans=0,
      why="Each clause of the keyed summary is one of STB-4.C.1, STB-4.C.2, STB-4.C.3 and "
          "STB-4.D.1. Every rejected summary treats the effect itself as the problem, "
          "excludes water vapor from the gases, misplaces carbon dioxide in the ranking, or "
          "denies that potencies differ."),
]
