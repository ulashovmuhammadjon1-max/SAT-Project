r"""AP CHEMISTRY 1.4 Composition of Mixtures.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.4.A: explain the quantitative relationship between the
elemental composition by mass and the composition of substances in a mixture.
Suggested skill 5.A, identify quantities needed to solve a problem from given
information (text, mathematical expressions, graphs, or tables).

Essential knowledge relied on, in the framework's own words:

  1.4.A.1  Pure substances contain atoms, molecules, or formula units of a
           single type. Mixtures contain atoms, molecules, or formula units of
           two or more types, whose relative proportions can vary.
  1.4.A.2  Elemental analysis can be used to determine the relative numbers of
           atoms in a substance and to determine its purity.

HOW THIS TOPIC IS KEPT DISTINCT FROM 1.3. Topic 1.3 is the law of definite
proportions and the empirical formula of a PURE substance; this one is what
happens when the sample is not pure. The two share a technique -- decompose,
weigh the elements -- and SOCIAL_DEDUPE.md warns that neighbouring topics
sharing statements is exactly where repeats come from. So no item here asks for
an empirical formula, and no item in 1.3 asks about purity or about varying
proportions. Where this module needs definite proportions it is as the
BASELINE a real analysis is compared against (items 5, 17, 19, 24), which is a
different question from establishing the baseline.

ON WHAT ELEMENTAL ANALYSIS CAN SHOW. EK 1.4.A.2 says it can determine the
relative numbers of atoms in a substance and determine its purity. The bank
asserts nothing beyond that -- in particular no item claims that elemental
analysis can identify an unknown impurity or prove a substance pure beyond
doubt, neither of which the framework states.

ON MOLAR MASSES AND BASELINES. Every percentage a purity calculation is
compared against is printed in the item's own table. Nothing here asks a
student to recall the composition of a named compound.

NOTATION. Plain prose; formulas in prose stay plain text per SCIENCE_BRIEF.md.
"""
TOPIC = ("1.4", "Composition of Mixtures", 1)

_T_MIX1 = dict(
    headers=["Component", "Mass in the mixture (grams)"],
    rows=[["Sodium chloride", "12.0"], ["Sand", "8.0"]])

_T_MIX3 = dict(
    headers=["Component", "Mass in the mixture (grams)"],
    rows=[["Substance A", "5.0"], ["Substance B", "10.0"], ["Substance C", "5.0"]])

_T_PURITY = dict(
    headers=["Measurement", "Value"],
    rows=[["Mass of the sample taken", "5.00 grams"],
          ["Mass of calcium recovered from the sample", "1.80 grams"],
          ["Percent calcium by mass in pure calcium carbonate", "40.0 percent"]])

_T_CUO = dict(
    headers=["Measurement", "Value"],
    rows=[["Mass of the copper and copper(II) oxide mixture", "10.0 grams"],
          ["Mass of oxygen recovered from the mixture", "1.6 grams"],
          ["Percent oxygen by mass in pure copper(II) oxide", "20.0 percent"]])

_T_VARY = dict(
    headers=["Preparation", "Mass of potassium chloride added (grams)",
             "Mass of sucrose added (grams)"],
    rows=[["Preparation 1", "5.0", "5.0"],
          ["Preparation 2", "2.0", "8.0"],
          ["Preparation 3", "8.0", "2.0"]])

_T_PORTIONS = dict(
    headers=["Portion analyzed", "Percent carbon by mass"],
    rows=[["Portion 1", "27.3"], ["Portion 2", "31.5"],
          ["Portion 3", "24.8"], ["Portion 4", "29.0"]])

_T_FOUR_SOLIDS = dict(
    headers=["Solid", "Percent nitrogen by mass, first analysis",
             "Percent nitrogen by mass, second analysis"],
    rows=[["Solid E", "35.0", "35.0"],
          ["Solid F", "35.0", "28.4"],
          ["Solid G", "12.9", "19.7"],
          ["Solid H", "46.6", "41.2"]])

_T_ORE = dict(
    headers=["Measurement", "Value"],
    rows=[["Mass of ore sample", "50.0 grams"],
          ["Mass of iron recovered from the ore sample", "14.0 grams"],
          ["Percent iron by mass in the pure mineral being sought", "70.0 percent"]])

QUESTIONS = [

 dict(q="Which statement correctly describes the difference in composition between a "
        "pure substance and a mixture?",
      choices=[
        "A pure substance contains particles of a single type, while a mixture contains "
        "particles of two or more types whose relative proportions can vary.",
        "A pure substance contains only one element, while a mixture contains two or "
        "more elements.",
        "A pure substance is always a solid, while a mixture may be a solid, a liquid "
        "or a gas.",
        "A pure substance can be separated into simpler substances, while a mixture "
        "cannot.",
        "A pure substance contains particles of two or more types in a fixed ratio, "
        "while a mixture contains particles of a single type."],
      ans=0,
      why="EK 1.4.A.1, near verbatim: pure substances contain atoms, molecules, or "
          "formula units of a single type, while mixtures contain them of two or more "
          "types whose relative proportions can vary. A compound of several elements is "
          "still a single type of particle, which is where the element-counting option "
          "goes wrong."),

 dict(q="What is the percent by mass of sodium chloride in the mixture described in the "
        "table?",
      table=_T_MIX1,
      choices=["60.0 percent", "40.0 percent", "12.0 percent", "66.7 percent",
               "150 percent"],
      ans=0,
      why="A component's percent by mass is its own mass divided by the total mass of "
          "the mixture, here 12.0 out of 20.0. Dividing by the mass of the other "
          "component instead gives the rejected value of 150."),

 dict(q="Elemental analysis of a substance is carried out. According to the framework, "
        "which two things can that analysis be used to determine?",
      choices=[
        "The relative numbers of atoms in the substance and the purity of the substance.",
        "The geometry of the molecules in the substance and the angles between their "
        "bonds.",
        "The temperature at which the substance melts and the temperature at which it "
        "boils.",
        "The identity of any impurity present and the process by which the impurity "
        "arrived.",
        "The number of moles of substance present and the volume the sample occupies."],
      ans=0,
      why="EK 1.4.A.2 states that elemental analysis can be used to determine the "
          "relative numbers of atoms in a substance and to determine its purity. "
          "Naming an unknown impurity is a stronger claim than the framework makes."),

 dict(q="Which component makes up half the mass of the mixture described in the table?",
      table=_T_MIX3,
      choices=["Substance B", "Substance A", "Substance C",
               "Substances A and C together make up half, and no single component does",
               "No component makes up half, because three components cannot divide "
               "evenly"],
      ans=0,
      why="A component's share is its own mass over the total mass of the mixture, and "
          "the tabulated total is 20.0 grams. The two five gram components do together "
          "make ten grams, but the item asks which single component does."),

 dict(q="A sample said to be pure calcium carbonate was analyzed with the results in "
        "the table. What is the percent purity of the sample with respect to calcium "
        "carbonate?",
      table=_T_PURITY,
      choices=["90.0 percent", "36.0 percent", "45.0 percent", "80.0 percent",
               "111 percent"],
      ans=0,
      why="EK 1.4.A.2 makes elemental analysis a test of purity by comparison with the "
          "composition a pure sample would have: 5.00 grams of pure material would "
          "yield 2.00 grams of calcium, and only 1.80 was recovered. Dividing the "
          "recovered calcium by the whole sample mass gives the rejected 36.0."),

 dict(q="Four portions were taken from different parts of one container of material and "
        "each was analyzed, with the results shown. What do the data indicate about the "
        "contents of the container?",
      table=_T_PORTIONS,
      choices=[
        "The contents are not a single pure substance, because the composition differs "
        "from portion to portion.",
        "The contents are a single pure substance, because every portion contains "
        "carbon.",
        "The contents are a single pure substance, because all four percentages lie "
        "between 24 and 32 percent.",
        "The analysis must be in error, because a mixture cannot contain carbon in "
        "every portion.",
        "Nothing can be concluded, because purity can never be judged from elemental "
        "composition."],
      ans=0,
      why="EK 1.4.A.1 allows the relative proportions in a mixture to vary while a pure "
          "substance is of a single type throughout, and EK 1.4.A.2 makes elemental "
          "analysis a legitimate purity test. Portions of one pure substance would "
          "return the same percentage."),

 dict(q="A 40.0 gram sample of a mixture is known to be 15.0 percent sulfur by mass. "
        "What mass of sulfur does the sample contain?",
      choices=["6.00 grams", "15.0 grams", "2.67 grams", "266 grams",
               "The mass cannot be found without knowing the other components"],
      ans=0,
      why="A percent by mass is a share of the whole sample, so the mass of the "
          "component is 0.150 multiplied by 40.0 grams. What the rest of the mixture "
          "consists of does not enter that calculation."),

 dict(q="A student wants the percent by mass of one component of a two-component solid "
        "mixture. Which pair of quantities is sufficient?",
      choices=[
        "The mass of that component and the total mass of the mixture.",
        "The mass of that component and the volume of the mixture.",
        "The molar mass of that component and the molar mass of the other component.",
        "The total mass of the mixture and the temperature at which it was weighed.",
        "The number of components present and the mass of the container."],
      ans=0,
      why="Suggested skill 5.A asks which quantities a problem actually needs. A "
          "percent by mass is one mass divided by another, so the two masses are "
          "exactly sufficient and nothing about volume, molar mass or temperature "
          "enters the ratio."),

 dict(q="Three preparations were made by combining the same two substances in the "
        "amounts shown. Which conclusion about the resulting materials is best "
        "supported?",
      table=_T_VARY,
      choices=[
        "All three are mixtures, because the same two substances were combined in "
        "proportions that vary from one preparation to the next.",
        "All three are the same pure compound, because each was made from the same two "
        "substances.",
        "Only the first is a mixture, because only there were the two masses equal.",
        "None is a mixture, because each preparation has a total mass of 10.0 grams.",
        "The first is a pure substance and the other two are mixtures, because only "
        "equal masses give a fixed composition."],
      ans=0,
      why="EK 1.4.A.1 makes the ability of relative proportions to vary the defining "
          "feature of a mixture, and the three preparations differ in proportion while "
          "using the same components. Equal masses of two substances make a mixture no "
          "less a mixture."),

 dict(q="A 10.0 gram sample of a mixture of copper metal and copper(II) oxide was fully "
        "analyzed with the results in the table. What mass of copper(II) oxide was in "
        "the mixture?",
      table=_T_CUO,
      choices=["8.0 grams", "1.6 grams", "2.0 grams", "5.0 grams", "10.0 grams"],
      ans=0,
      why="Only one component of the mixture contains oxygen, so the whole 1.6 grams "
          "recovered came from that component, and a component that is 20.0 percent "
          "oxygen must weigh five times as much as its oxygen. Reporting the oxygen "
          "itself as the mass of the oxide is the rejected 1.6."),

 dict(q="Using the same analysis, what mass of copper metal was present in the mixture?",
      table=_T_CUO,
      choices=["2.0 grams", "8.0 grams", "1.6 grams", "6.4 grams", "10.0 grams"],
      ans=0,
      why="The copper(II) oxide accounts for 8.0 grams of the 10.0 gram mixture, so "
          "what is left is the copper metal. Reporting the mass of the oxide rather "
          "than the remainder is the rejected 8.0."),

 dict(q="A chemist adds 10.0 grams of pure substance X to a 30.0 gram mixture that "
        "already contains 6.0 grams of X. What is the percent by mass of X in the "
        "resulting 40.0 gram mixture?",
      choices=["40.0 percent", "20.0 percent", "25.0 percent", "16.0 percent",
               "60.0 percent"],
      ans=0,
      why="Both the mass of X and the total mass change, so the new share is 16.0 "
          "divided by 40.0. Adding the ten grams to the numerator while leaving the "
          "denominator at thirty gives one of the rejected values, and this variability "
          "is exactly what EK 1.4.A.1 permits a mixture to do."),

 dict(q="Which statement about the components of a mixture is correct?",
      choices=[
        "Each component keeps its own chemical formula, and only the proportions in "
        "which they are combined change.",
        "The components combine into a new compound with a formula of its own.",
        "The components lose their identities and can no longer be recovered.",
        "Each component must be present in the same mass as every other component.",
        "The components must all be elements rather than compounds."],
      ans=0,
      why="EK 1.4.A.1 describes a mixture as containing atoms, molecules, or formula "
          "units of two or more types, which is a statement about which particles are "
          "present rather than about a new substance being formed. The proportions are "
          "the part the framework allows to vary."),

 dict(q="Four solids were each analyzed twice, on samples taken from different parts of "
        "the same bottle, with the results shown. Which solid is the best candidate for "
        "a pure substance?",
      table=_T_FOUR_SOLIDS,
      choices=["Solid E", "Solid F", "Solid G", "Solid H",
               "None of them, because two analyses are never enough to judge purity"],
      ans=0,
      why="EK 1.4.A.1 lets the relative proportions of a mixture vary from place to "
          "place while a pure substance is of one type throughout, so agreement between "
          "analyses of different portions is the evidence sought. Only one solid gives "
          "the same percentage twice."),

 dict(q="A 50.0 gram ore sample was analyzed for iron with the results in the table. "
        "What percent of the ore sample is made up of the pure mineral being sought?",
      table=_T_ORE,
      choices=["40.0 percent", "28.0 percent", "70.0 percent", "20.0 percent",
               "35.0 percent"],
      ans=0,
      why="The recovered iron all came from the mineral, and a mineral that is 70.0 "
          "percent iron must weigh 20.0 grams to supply 14.0 grams of iron, which is "
          "20.0 out of 50.0 of the ore. Reporting the iron as a share of the ore gives "
          "the rejected 28.0."),

 dict(q="Two samples of a pure compound and two samples of a mixture are each analyzed "
        "for their percent composition by mass. What pattern should be expected?",
      choices=[
        "The two samples of the compound must agree with each other, while the two "
        "samples of the mixture need not.",
        "Both pairs must agree, because percent composition is fixed for any material.",
        "Neither pair need agree, because percent composition depends on the size of "
        "the sample.",
        "The two samples of the mixture must agree, while the two samples of the "
        "compound need not.",
        "Both pairs must disagree, because no two samples are ever identical."],
      ans=0,
      why="EK 1.3.A.2 fixes the ratio of constituent masses for any pure sample of a "
          "compound, while EK 1.4.A.1 states that the relative proportions in a mixture "
          "can vary. The size of the sample affects neither, since a percentage is a "
          "proportion."),

 dict(q="An analyst reports that a sample believed to be a pure compound of carbon and "
        "hydrogen also contains a measurable amount of chlorine. What is the most "
        "reasonable conclusion?",
      choices=[
        "The sample is not pure, since a pure sample would contain only the particle "
        "type the compound is made of.",
        "The compound must be redefined to include chlorine as one of its elements.",
        "The chlorine has no bearing on purity, since purity concerns only the total "
        "mass of the sample.",
        "The sample is pure, because elemental analysis cannot detect impurities.",
        "The sample must be a pure element rather than a pure compound."],
      ans=0,
      why="EK 1.4.A.1 makes a pure substance one containing particles of a single type, "
          "and EK 1.4.A.2 makes elemental analysis a legitimate test of purity. Finding "
          "an element that the claimed compound does not contain is evidence of a "
          "second type of particle."),

 dict(q="A student is asked to decide whether a white powder is a pure substance or a "
        "mixture and is given the mass of the sample, the mass of each element it "
        "yields on complete decomposition, and the sample's color. Which of these is "
        "not needed for the decision?",
      choices=[
        "The color of the sample.",
        "The mass of the sample.",
        "The mass of each element the sample yields.",
        "Every mass measurement in the list, since a ratio needs both a part and a "
        "whole.",
        "All three are needed, because purity cannot be judged from mass data alone."],
      ans=0,
      why="Suggested skill 5.A asks which quantities the problem requires. EK 1.4.A.2 "
          "grounds a purity judgement in elemental analysis, which needs the elemental "
          "masses and the sample mass they are compared against; nothing in the "
          "framework connects color to composition."),

 dict(q="A sample of a substance is 95.0 percent pure by mass. What is the mass of "
        "impurity in a 200 gram sample?",
      choices=["10.0 grams", "5.00 grams", "95.0 grams", "190 grams", "21.1 grams"],
      ans=0,
      why="If 95.0 percent of the mass is the substance itself, the remaining 5.00 "
          "percent is impurity, and 0.0500 multiplied by 200 grams is 10.0 grams. "
          "Reading the percentage itself as a mass gives the rejected 5.00."),

 dict(q="Which of the following materials is a mixture rather than a pure substance?",
      choices=[
        "Seawater, which contains water together with dissolved salts in proportions "
        "that differ from ocean to ocean.",
        "Distilled water, every portion of which contains only water molecules.",
        "Solid carbon dioxide, every portion of which contains only CO2 molecules.",
        "Table salt that has been recrystallized until every portion is sodium chloride.",
        "Nitrogen gas that has been purified until only N2 molecules remain."],
      ans=0,
      why="EK 1.4.A.1 defines a mixture as containing particles of two or more types "
          "whose relative proportions can vary, and each rejected option is explicitly "
          "described as containing one type of particle throughout."),

 dict(q="A 25.0 gram mixture is 40.0 percent substance A by mass and contains nothing "
        "but substances A and B. What mass of substance B does it contain?",
      choices=["15.0 grams", "10.0 grams", "40.0 grams", "60.0 grams",
               "12.5 grams"],
      ans=0,
      why="Substance A accounts for 0.400 multiplied by 25.0 grams, which is 10.0 "
          "grams, so the remaining mass of the two-component mixture is substance B. "
          "Reporting the mass of A instead of the remainder gives the rejected 10.0."),

 dict(q="How does adding an inert impurity that contains no carbon affect the measured "
        "percent by mass of carbon in a sample of a carbon-containing compound?",
      choices=[
        "It lowers the measured percentage, because the mass of carbon stays the same "
        "while the total mass rises.",
        "It raises the measured percentage, because the total mass rises.",
        "It leaves the measured percentage unchanged, because the impurity contains no "
        "carbon.",
        "It leaves the measured percentage unchanged, because percent composition is a "
        "fixed property of a compound.",
        "It lowers the measured percentage, because the impurity destroys some of the "
        "carbon."],
      ans=0,
      why="A percent by mass is the mass of the element over the total mass, so a "
          "component that adds to the denominator and not the numerator must reduce the "
          "ratio. EK 1.4.A.1 makes such a shift possible for a mixture, and EK 1.4.A.2 "
          "is why the shift is detectable."),

 dict(q="Two portions of the same mixture, taken from the same well-stirred container, "
        "are analyzed and give the same percent composition. What does this result "
        "establish?",
      choices=[
        "It is consistent with the container holding a mixture of uniform composition "
        "and does not by itself prove the material is a pure substance.",
        "It proves the material is a pure substance, because only a pure substance can "
        "give repeatable results.",
        "It proves the material is a mixture, because a pure substance gives different "
        "results for different portions.",
        "It proves an error was made, because two portions of a mixture can never agree.",
        "It establishes nothing at all, because percent composition is not a "
        "measurable quantity."],
      ans=0,
      why="EK 1.4.A.1 lets the proportions of a mixture vary but does not require them "
          "to vary within one well-stirred container. Agreement between portions is "
          "therefore evidence against the material being non-uniform, not proof that "
          "only one type of particle is present."),

 dict(q="An analysis of a sample gives a ratio of 1.00 mole of element M to 1.37 moles "
        "of element N, and no simple whole number ratio close to that is found. If the "
        "measurements are reliable, what does the result most likely indicate?",
      choices=[
        "The sample is not a single pure compound, since a pure compound would give a "
        "simple whole number ratio of atoms.",
        "Element M and element N cannot combine chemically with each other.",
        "The sample is a pure compound whose atoms combine in fractional numbers.",
        "The molar masses used in the calculation must both have been too large.",
        "The sample is a pure element rather than a compound."],
      ans=0,
      why="EK 1.3.A.3 makes the atom ratio in a pure compound a whole number ratio, and "
          "EK 1.4.A.2 makes elemental analysis a test of purity, so a persistent "
          "non-whole ratio points to more than one type of particle being present. "
          "Scaling both molar masses would not change their ratio."),

 dict(q="Which quantity must be measured, in addition to the mass of an element "
        "recovered, in order to report the percent by mass of that element in a sample?",
      choices=[
        "The mass of the whole sample before the element was recovered.",
        "The molar mass of the element recovered.",
        "The number of components the sample contains.",
        "The volume of the container the sample was held in.",
        "The mass of the apparatus used in the recovery."],
      ans=0,
      why="Suggested skill 5.A asks which quantity the calculation needs. A percentage "
          "is one mass divided by a total mass, so the total is the missing quantity; "
          "the molar mass would be needed for a mole count, which is a different "
          "question."),

 dict(q="Sample 1 of a mixture of salt and sand is 30.0 percent salt by mass, and "
        "sample 2 of a mixture of the same two substances is 70.0 percent salt by mass. "
        "Which conclusion follows?",
      choices=[
        "Both are mixtures of the same two substances, since a mixture's relative "
        "proportions are free to vary.",
        "One of the two analyses must be wrong, since the same two substances must "
        "always combine in the same proportion.",
        "The two samples must contain different substances, since their compositions "
        "differ.",
        "Sample 2 is a pure substance, since it contains more salt than sand.",
        "Neither sample is a mixture, since a true mixture must be exactly half of "
        "each component."],
      ans=0,
      why="EK 1.4.A.1 states that the relative proportions of the components of a "
          "mixture can vary, so two mixtures of the same components may differ in "
          "composition without either analysis being in error. The fixed-proportion "
          "requirement of EK 1.3.A.2 applies to a pure compound, not to a mixture."),

 dict(q="Why can elemental analysis be used as a purity test at all?",
      choices=[
        "Because a pure substance has one composition by mass that can be predicted "
        "from its formula, so a measured departure from it indicates something else is "
        "present.",
        "Because impurities always contain elements that pure substances never contain.",
        "Because an impure sample always weighs more than a pure sample of the same "
        "substance.",
        "Because elemental analysis measures the number of impurity particles directly.",
        "Because a pure substance yields no elements at all when it is decomposed."],
      ans=0,
      why="EK 1.4.A.2 states that elemental analysis can be used to determine purity, "
          "and EK 1.3.A.2 supplies the reason by fixing the ratio of constituent masses "
          "for any pure sample. The test is a comparison against that predicted "
          "composition."),

 dict(q="A 20.0 gram mixture contains 5.0 grams of substance J, 5.0 grams of substance "
        "K and 10.0 grams of substance L. If 10.0 grams more of substance J is added, "
        "what happens to the percent by mass of substance L?",
      choices=[
        "It falls from 50.0 percent to about 33.3 percent, because the total mass rises "
        "while the mass of L does not.",
        "It rises from 50.0 percent to about 66.7 percent, because the mixture is now "
        "larger.",
        "It stays at 50.0 percent, because no substance L was added or removed.",
        "It falls from 50.0 percent to 25.0 percent, because the mass of J has doubled.",
        "It cannot be determined, because the percent composition of a mixture is not "
        "defined."],
      ans=0,
      why="The share of a component is its own mass over the new total, so ten grams of "
          "L in a thirty gram mixture is one third. EK 1.4.A.1 makes exactly this kind "
          "of change in relative proportion available to a mixture."),

 dict(q="A student claims that because a mixture of two compounds has a definite total "
        "mass, it must also have a definite chemical formula. Which evaluation is "
        "correct?",
      choices=[
        "The claim is wrong, because the proportions of the components of a mixture can "
        "vary, so no single set of subscripts describes it.",
        "The claim is right, because any material with a measurable mass has a formula.",
        "The claim is wrong, because a mixture has no mass of its own.",
        "The claim is right, but only when the two compounds are present in equal "
        "masses.",
        "The claim cannot be evaluated without knowing which two compounds are present."],
      ans=0,
      why="EK 1.4.A.1 makes variable relative proportions the defining feature of a "
          "mixture, and a chemical formula records a fixed ratio. Having a definite "
          "mass is a property of any sample and says nothing about fixed proportions."),

 dict(q="An elemental analysis is performed on a sample and returns the relative "
        "numbers of atoms of each element present. What further information is required "
        "before that result can be used to judge whether the sample is pure?",
      choices=[
        "The composition that the substance would have if it were pure, so the measured "
        "result has something to be compared against.",
        "The total number of atoms in the sample, so that the relative numbers can be "
        "made absolute.",
        "The temperature at which the analysis was performed, since composition depends "
        "on temperature.",
        "The mass of the empty apparatus, since purity is measured relative to it.",
        "Nothing further, since any elemental analysis reports purity directly."],
      ans=0,
      why="EK 1.4.A.2 lists determining relative numbers of atoms and determining purity "
          "as two separate uses of the technique, and the second needs a baseline: EK "
          "1.3.A.2's fixed mass ratio for a pure sample is what the measurement is "
          "checked against."),
]
