r"""AP CHEMISTRY 1.3 Elemental Composition of Pure Substances.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.3.A: explain the quantitative relationship between the
elemental composition by mass and the empirical formula of a pure substance.
Suggested skill 2.A, identify a testable scientific question based on an
observation, data, or a model.

Essential knowledge relied on, in the framework's own words:

  1.3.A.1  Some pure substances are composed of individual molecules, while
           others consist of atoms or ions held together in fixed proportions
           as described by a formula unit.
  1.3.A.2  According to the law of definite proportions, the ratio of the
           masses of the constituent elements in any pure sample of that
           compound is always the same.
  1.3.A.3  The chemical formula that lists the lowest whole number ratio of
           atoms of the elements in a compound is the empirical formula.

ON MOLECULAR FORMULAS. The framework defines the empirical formula here and
distinguishes molecules from formula units at 1.3.A.1, but it does not print a
rule for recovering a molecular formula. Items 17 and 24 are the only two that
go there, and both are chained explicitly: EK 1.3.A.3 makes the empirical
formula the LOWEST whole number ratio, so a molecule's own formula must be a
whole number multiple of it, and EK 1.1.A.3's molar mass fixes which multiple.
The chain is written out in the claim rather than assumed.

ON MOLAR MASSES. Every molar mass an item needs is printed in the item's own
table. Nothing here asks a student to recall one, and every ratio a key states
is recomputed in verify_h1_3.py from that table.

ON SKILL 2.A. Items 13 and 27 are the testable-question items the suggested
skill points at: which question a stated measurement could actually answer.

NOTATION. Formulas stay plain text in prose per SCIENCE_BRIEF.md (H2O, Al2O3);
nothing in this topic needs a typeset span, so the module has none. That is a
deliberate outcome and not an oversight -- writing \(\mathrm{H_2O}\) where
plain H2O reads correctly is what made the converter's output ugly on the
economics banks.
"""
TOPIC = ("1.3", "Elemental Composition of Pure Substances", 1)

_T_MM = dict(
    headers=["Element", "Molar mass (grams per mole)"],
    rows=[["Hydrogen", "1.0"], ["Carbon", "12.0"], ["Nitrogen", "14.0"],
          ["Oxygen", "16.0"], ["Magnesium", "24.0"], ["Aluminum", "27.0"],
          ["Sulfur", "32.0"], ["Iron", "56.0"]])

_T_CH = dict(
    headers=["Element", "Mass in the sample (grams)", "Molar mass (grams per mole)"],
    rows=[["Carbon", "24.0", "12.0"], ["Hydrogen", "4.0", "1.0"]])

_T_ALO = dict(
    headers=["Element", "Mass in the sample (grams)", "Molar mass (grams per mole)"],
    rows=[["Aluminum", "5.4", "27.0"], ["Oxygen", "4.8", "16.0"]])

_T_NO = dict(
    headers=["Element", "Mass in the sample (grams)", "Molar mass (grams per mole)"],
    rows=[["Nitrogen", "7.0", "14.0"], ["Oxygen", "16.0", "16.0"]])

_T_DEFINITE = dict(
    headers=["Sample", "Mass of element A recovered (grams)",
             "Mass of element B recovered (grams)"],
    rows=[["Sample 1", "3.00", "8.00"],
          ["Sample 2", "6.00", "16.00"],
          ["Sample 3", "4.50", "12.00"]])

_T_TWO_COMPOUNDS = dict(
    headers=["Sample", "Mass of carbon recovered (grams)",
             "Mass of oxygen recovered (grams)"],
    rows=[["Sample P", "12.0", "32.0"],
          ["Sample Q", "12.0", "16.0"]])

_T_OXIDE = dict(
    headers=["Measurement", "Value (grams)"],
    rows=[["Mass of iron used", "11.2"],
          ["Mass of iron oxide produced", "16.0"]])

_T_PERCENT = dict(
    headers=["Compound", "Percent carbon by mass", "Percent hydrogen by mass",
             "Percent oxygen by mass"],
    rows=[["Compound R", "40.0", "6.7", "53.3"],
          ["Compound S", "75.0", "25.0", "0.0"],
          ["Compound T", "27.3", "0.0", "72.7"]])

_T_MASS_RATIO = dict(
    headers=["Compound", "Formula",
             "Mass of the first element listed, per mole of compound (grams)",
             "Molar mass of the compound (grams per mole)"],
    rows=[["Compound U", "MgO", "24.0", "40.0"],
          ["Compound V", "H2O", "2.0", "18.0"],
          ["Compound W", "CO2", "12.0", "44.0"],
          ["Compound Y", "NH3", "14.0", "17.0"]])

QUESTIONS = [

 dict(q="Which of the following describes what a chemical formula must list in order "
        "to be called the empirical formula of a compound?",
      choices=[
        "The lowest whole number ratio of atoms of the elements in the compound.",
        "The actual number of atoms of each element in one molecule of the compound.",
        "The ratio of the masses of the elements in the compound.",
        "The number of moles of each element in a one gram sample of the compound.",
        "The order in which the atoms of the compound are bonded to one another."],
      ans=0,
      why="EK 1.3.A.3, near verbatim: the chemical formula that lists the lowest whole "
          "number ratio of atoms of the elements in a compound is the empirical "
          "formula. It is a ratio of atoms, not of masses, and it says nothing about "
          "connectivity."),

 dict(q="Two chemists purify samples of the same compound from completely different "
        "sources and then decompose each sample into its elements. What does the law "
        "of definite proportions predict about the two results?",
      choices=[
        "The ratio of the masses of the constituent elements will be the same in both "
        "samples.",
        "The total mass recovered will be the same in both samples, whatever their "
        "starting sizes.",
        "The ratio of the masses of the constituent elements will depend on which "
        "source the sample came from.",
        "Each element will be recovered in equal mass to every other element in the "
        "same sample.",
        "The number of moles of each element recovered will be the same in both "
        "samples."],
      ans=0,
      why="EK 1.3.A.2 states the law of definite proportions as the claim that the "
          "ratio of the masses of the constituent elements in any pure sample of a "
          "compound is always the same. It fixes a ratio, so it says nothing about the "
          "absolute masses, which depend on how large a sample was taken."),

 dict(q="A pure compound is decomposed and the masses of its two elements are "
        "recovered as shown. What is the empirical formula of the compound?",
      table=_T_CH,
      choices=["CH2", "C2H4", "CH4", "C6H12", "C3H6"],
      ans=0,
      why="Dividing each mass by its own molar mass gives 2.00 moles of carbon and 4.00 "
          "moles of hydrogen, a ratio of one to two. EK 1.3.A.3 requires the LOWEST "
          "whole number ratio, so the doubled and sixfold forms are rejected even "
          "though they carry the same proportion."),

 dict(q="Some pure substances are made of individual molecules, while others consist "
        "of atoms or ions held together in fixed proportions. Which statement about "
        "solid sodium chloride follows from that distinction?",
      choices=[
        "Its composition is described by a formula unit rather than by an individual "
        "molecule.",
        "Its composition cannot be described by a chemical formula at all.",
        "Its composition varies from one sample to another because it has no molecules.",
        "It contains individual NaCl molecules that are joined together into a larger "
        "structure.",
        "It is a mixture rather than a pure substance, because two elements are "
        "present."],
      ans=0,
      why="EK 1.3.A.1 states that some pure substances are composed of individual "
          "molecules while others consist of atoms or ions held together in fixed "
          "proportions as described by a formula unit. A fixed proportion is precisely "
          "what a variable composition would lack."),

 dict(q="Using the molar masses in the table, what percent by mass of water is oxygen?",
      table=_T_MM,
      choices=["About 88.9 percent", "About 50.0 percent", "About 11.1 percent",
               "About 66.7 percent", "About 33.3 percent"],
      ans=0,
      why="One formula unit of H2O carries 16.0 grams per mole of oxygen out of a total "
          "of 18.0, so the oxygen share is 16.0 divided by 18.0. Counting atoms rather "
          "than masses gives the rejected value near 33 percent."),

 dict(q="Glucose has the molecular formula C6H12O6. What is its empirical formula?",
      choices=["CH2O", "C6H12O6", "C3H6O3", "C2H4O2", "CHO"],
      ans=0,
      why="EK 1.3.A.3 requires the lowest whole number ratio of atoms, and dividing the "
          "subscripts six, twelve and six by their greatest common factor of six leaves "
          "one, two and one. The halved and third forms preserve the proportion but are "
          "not the lowest."),

 dict(q="A pure compound is decomposed into aluminum and oxygen with the results shown. "
        "What is the empirical formula of the compound?",
      table=_T_ALO,
      choices=["Al2O3", "Al3O2", "AlO", "Al2O5", "Al4O6"],
      ans=0,
      why="Each mass divided by its own molar mass gives 0.200 moles of aluminum and "
          "0.300 moles of oxygen, a ratio of two to three once cleared to whole "
          "numbers. Reversing the two ratios gives the rejected Al3O2."),

 dict(q="Three samples of what is claimed to be the same pure compound were each fully "
        "decomposed, with the results in the table. Do the data support the claim?",
      table=_T_DEFINITE,
      choices=[
        "Yes, because the ratio of the mass of A to the mass of B is the same in all "
        "three samples.",
        "Yes, because the total mass recovered is the same in all three samples.",
        "No, because the three samples yielded different masses of element A.",
        "No, because a pure compound must yield equal masses of its two elements.",
        "The data cannot decide the question, because the sizes of the samples differ."],
      ans=0,
      why="EK 1.3.A.2 makes the constant ratio of the masses of the constituent "
          "elements the test for samples of one pure compound, and a ratio is exactly "
          "what survives a change in sample size. Differing total masses are therefore "
          "expected rather than disqualifying."),

 dict(q="Two samples were each fully decomposed into carbon and oxygen, with the "
        "results shown. What do the data indicate?",
      table=_T_TWO_COMPOUNDS,
      choices=[
        "The two samples are not the same compound, because the mass of oxygen per "
        "gram of carbon differs between them.",
        "The two samples are the same compound, because both contain the same two "
        "elements.",
        "The two samples are the same compound, because both yielded the same mass of "
        "carbon.",
        "The two samples are the same compound, because neither contains any other "
        "element.",
        "Neither sample can be a pure compound, because the masses recovered are not "
        "equal."],
      ans=0,
      why="EK 1.3.A.2 requires any pure sample of a given compound to show the same "
          "ratio of constituent masses, so a different ratio rules out the samples "
          "being the same compound. Containing the same elements is not the same "
          "condition as containing them in the same proportion."),

 dict(q="Using the molar masses in the table, what percent by mass of magnesium oxide, "
        "MgO, is magnesium?",
      table=_T_MM,
      choices=["60.0 percent", "50.0 percent", "40.0 percent", "24.0 percent",
               "66.7 percent"],
      ans=0,
      why="A formula unit of MgO carries 24.0 grams per mole of magnesium out of a "
          "total of 40.0, so the magnesium share is 24.0 divided by 40.0. A one to one "
          "atom ratio does not make a one to one mass ratio, which is what the rejected "
          "50.0 percent assumes."),

 dict(q="A pure compound is decomposed into nitrogen and oxygen with the results in the "
        "table. What is its empirical formula?",
      table=_T_NO,
      choices=["NO2", "N2O", "NO3", "N4O2", "N3O4"],
      ans=0,
      why="Dividing each mass by its own molar mass gives 0.500 moles of nitrogen and "
          "1.00 mole of oxygen, a ratio of one to two. The doubled form carries the "
          "same proportion but is not the lowest whole number ratio EK 1.3.A.3 "
          "requires."),

 dict(q="A 50.0 gram sample of a pure compound is known to be 40.0 percent carbon by "
        "mass. What mass of carbon does the sample contain?",
      choices=["20.0 grams", "40.0 grams", "10.0 grams", "125 grams",
               "The mass cannot be found without the formula of the compound"],
      ans=0,
      why="A percent composition by mass is a fixed proportion under EK 1.3.A.2, so it "
          "applies to any size of pure sample: 0.400 multiplied by 50.0 grams is 20.0 "
          "grams. The formula is not needed once the percentage is given."),

 dict(q="A student has a sample of a pure white solid and access to equipment that can "
        "decompose it and weigh the mass of each element released. Which question can "
        "that measurement alone answer?",
      choices=[
        "What is the ratio of the masses of the elements in this compound?",
        "What geometry do the molecules of this compound adopt?",
        "How strong are the forces holding one particle of this compound to the next?",
        "At what temperature does this compound begin to melt?",
        "How is each atom in this compound bonded to its neighbors?"],
      ans=0,
      why="Skill 2.A asks which question the available observation can actually test, "
          "and the masses of the elements released are exactly the quantities EK "
          "1.3.A.2 speaks of. Geometry, bonding and thermal behavior are not "
          "determined by an elemental mass measurement."),

 dict(q="What distinguishes a pure compound from a mixture of the same elements, when "
        "the composition of samples is examined?",
      choices=[
        "Every pure sample of the compound shows the same ratio of elemental masses, "
        "while a mixture's proportions can vary from sample to sample.",
        "A pure compound contains only one element, while a mixture contains more than "
        "one.",
        "A pure compound has a mass that is a whole number, while a mixture does not.",
        "A pure compound can be separated into its elements, while a mixture cannot be "
        "separated at all.",
        "A pure compound has no empirical formula, because its composition is fixed."],
      ans=0,
      why="EK 1.3.A.2 fixes the ratio of constituent masses for any pure sample of a "
          "compound, and EK 1.4.A.1 states that the relative proportions of the "
          "components of a mixture can vary. Constancy of proportion is therefore the "
          "distinguishing observation."),

 dict(q="Compound R has the percent composition by mass shown in the table. What is its "
        "empirical formula?",
      table=_T_PERCENT,
      choices=["CH2O", "CHO", "C2H3O2", "CH4O", "C3H6O3"],
      ans=0,
      why="Taking a 100 gram sample turns each percentage into a mass, and dividing by "
          "the molar masses 12.0, 1.0 and 16.0 gives about 3.33, 6.7 and 3.33 moles, a "
          "ratio of one to two to one. The threefold form has the same proportion but "
          "is not the lowest ratio."),

 dict(q="Compound S in the table contains only carbon and hydrogen. What is its "
        "empirical formula?",
      table=_T_PERCENT,
      choices=["CH4", "C3H", "CH3", "C2H6", "C4H12"],
      ans=0,
      why="From a 100 gram sample, 75.0 grams of carbon is 6.25 moles and 25.0 grams of "
          "hydrogen is 25.0 moles, a ratio of one to four. Comparing the percentages "
          "themselves rather than the mole amounts is what makes the three to one form "
          "look plausible."),

 dict(q="A compound has the empirical formula CH2 and a molar mass of 42.0 grams per "
        "mole. Given that the molar mass of the CH2 unit is 14.0 grams per mole, what "
        "is the molecular formula of the compound?",
      choices=["C3H6", "CH2", "C2H4", "C4H8", "C42H84"],
      ans=0,
      why="EK 1.3.A.3 makes the empirical formula the lowest whole number ratio, so a "
          "molecule's own formula must be some whole number multiple of it, and the "
          "molar mass fixes which multiple: 42.0 divided by 14.0 is three. Applying the "
          "wrong multiple is the only way to reach any of the rejected formulas."),

 dict(q="Why does the percent composition by mass of a pure compound stay the same when "
        "a chemist takes a sample ten times larger?",
      choices=[
        "Because a percent composition is a ratio of masses, and the law of definite "
        "proportions fixes that ratio for any pure sample.",
        "Because the mass of each element in the sample stays the same as the sample "
        "grows.",
        "Because a larger sample contains a larger number of different compounds, which "
        "cancel out.",
        "Because percent composition depends on the volume of the sample rather than "
        "on its mass.",
        "Because the atoms in a larger sample are more tightly packed, which "
        "compensates for the extra mass."],
      ans=0,
      why="EK 1.3.A.2 states that the ratio of the masses of the constituent elements "
          "is always the same in any pure sample of a compound, and a percentage is "
          "that ratio expressed per hundred grams. The individual masses do grow with "
          "the sample; their proportions do not."),

 dict(q="In a compound of carbon and oxygen the ratio of carbon atoms to oxygen atoms "
        "is one to one, yet the ratio of the mass of carbon to the mass of oxygen is "
        "not one to one. Which explanation is correct?",
      choices=[
        "A carbon atom and an oxygen atom have different masses, so equal numbers of "
        "them do not carry equal masses.",
        "The oxygen atoms are more numerous than the formula suggests, because oxygen "
        "is a gas.",
        "The masses of the two elements must in fact be equal, and the measurement is "
        "in error.",
        "Mass ratios and atom ratios are always numerically equal, so the compound "
        "cannot be pure.",
        "The empirical formula gives mass ratios directly, so the atom ratio has been "
        "misread."],
      ans=0,
      why="EK 1.3.A.3 makes the formula a ratio of ATOMS, while EK 1.3.A.2 speaks of a "
          "ratio of MASSES; the two agree only if the atoms have equal mass, and EK "
          "1.1.A.3 attaches a distinct molar mass to each element. Confusing the two "
          "ratios is exactly the error the rejected options make."),

 dict(q="Which of these formulas is already written as an empirical formula?",
      choices=["NH3", "H2O2", "C4H8", "C2H6", "N2O4"],
      ans=0,
      why="EK 1.3.A.3 requires the subscripts to be in the lowest whole number ratio. "
          "The rejected formulas all have subscripts sharing a common factor greater "
          "than one, so each reduces further, while one and three share no such factor."),

 dict(q="A pure compound of two elements is analyzed twice, and the second analysis "
        "uses a sample three times as large as the first. Which quantity should be "
        "three times as large in the second analysis?",
      choices=[
        "The mass of each element recovered.",
        "The ratio of the masses of the two elements recovered.",
        "The percent by mass of each element in the sample.",
        "The subscripts in the empirical formula of the compound.",
        "None of these quantities, because all four are fixed by the identity of the "
        "compound."],
      ans=0,
      why="EK 1.3.A.2 fixes the RATIO of constituent masses, not the masses themselves, "
          "so an amount scales with the sample while a proportion does not. The "
          "empirical formula of EK 1.3.A.3 is a property of the compound and is "
          "unaffected by how much of it was taken."),

 dict(q="A sample of iron is heated in oxygen until it is completely converted into an "
        "iron oxide, with the masses recorded in the table. If the molar mass of iron "
        "is 56.0 grams per mole and that of oxygen is 16.0 grams per mole, what is the "
        "empirical formula of the oxide?",
      table=_T_OXIDE,
      choices=["Fe2O3", "FeO5", "Fe3O4", "FeO3", "Fe3O2"],
      ans=0,
      why="The oxygen taken up is the difference between the two recorded masses, 4.8 "
          "grams, which is 0.300 moles against 0.200 moles of iron, a ratio of two to "
          "three. Forgetting to subtract and treating the whole product mass as oxygen "
          "is the error that leads away from this answer."),

 dict(q="Compound T in the table contains only carbon and oxygen. What is its empirical "
        "formula?",
      table=_T_PERCENT,
      choices=["CO2", "C2O", "CO3", "C3O2", "C2O5"],
      ans=0,
      why="From a 100 gram sample, 27.3 grams of carbon is about 2.28 moles and 72.7 "
          "grams of oxygen is about 4.54 moles, a ratio very close to one to two. "
          "Comparing the two percentages directly rather than the mole amounts is what "
          "makes the one to one form look plausible."),

 dict(q="A compound has the empirical formula CH2O, whose unit has a molar mass of 30.0 "
        "grams per mole. A second compound has the same empirical formula but a molar "
        "mass of 180.0 grams per mole. Which statement about the two compounds is "
        "correct?",
      choices=[
        "They share the same ratio of atoms but differ in the actual number of atoms "
        "per molecule, by a factor of six.",
        "They must be the same compound, because two substances with the same empirical "
        "formula are identical.",
        "They cannot both exist, because a compound's molar mass is fixed by its "
        "empirical formula.",
        "They differ in the ratio of atoms, because their molar masses differ.",
        "They share the same molar mass, because the empirical formula fixes it."],
      ans=0,
      why="EK 1.3.A.3 makes the empirical formula the LOWEST whole number ratio, so it "
          "fixes the proportions and leaves the multiple open; EK 1.1.A.3's molar mass "
          "is what selects the multiple, here 180.0 divided by 30.0. Two substances can "
          "therefore share an empirical formula without being the same substance."),

 dict(q="A chemist reports that a certain pure compound contains 5.00 grams of sulfur "
        "for every 5.00 grams of oxygen. Using the molar masses in the table, what is "
        "the ratio of sulfur atoms to oxygen atoms in the compound?",
      table=_T_MM,
      choices=["Fewer sulfur atoms than oxygen atoms, in a ratio of about one to two",
               "Equal numbers of sulfur and oxygen atoms, because the masses are equal",
               "More sulfur atoms than oxygen atoms, in a ratio of about two to one",
               "More sulfur atoms than oxygen atoms, in a ratio of about four to one",
               "The ratio cannot be found from mass data alone"],
      ans=0,
      why="Equal masses of two elements do not give equal numbers of atoms, because "
          "each mass must be divided by its own molar mass first: 5.00 over 32.0 "
          "against 5.00 over 16.0. EK 1.3.A.3's atom ratio is therefore the reverse of "
          "the naive reading of the equal masses."),

 dict(q="Which experimental result would be sufficient, on its own, to establish the "
        "empirical formula of a pure compound containing only carbon and hydrogen?",
      choices=[
        "The mass of carbon and the mass of hydrogen obtained by completely "
        "decomposing a weighed sample.",
        "The mass of the sample before it is decomposed, measured to high precision.",
        "The temperature at which the compound melts and the temperature at which it "
        "boils.",
        "The volume of the sample and its density at room temperature.",
        "The color of the flame produced when the sample is burned."],
      ans=0,
      why="Skill 2.A asks which measurement can answer the question posed. EK 1.3.A.3's "
          "atom ratio is reached by dividing each elemental mass by its own molar mass, "
          "so the elemental masses are exactly what is required and the total sample "
          "mass alone carries no information about proportion."),

 dict(q="For the compounds listed in the table, in which one does a single formula unit "
        "or molecule carry the largest percentage of its mass as the element written "
        "first in the formula?",
      table=_T_MASS_RATIO,
      choices=["Compound Y, at about 82 percent nitrogen",
               "Compound U, at 60 percent magnesium",
               "Compound V, at about 11 percent hydrogen",
               "Compound W, at about 27 percent carbon",
               "All four are equal, because each formula lists its first element once"],
      ans=0,
      why="Each percentage is the molar mass contributed by that element divided by the "
          "tabulated molar mass of the whole compound. Because the elements differ in "
          "molar mass, writing an element first in a formula says nothing about how "
          "much of the mass it carries."),

 dict(q="A student claims that the empirical formula of a compound tells you exactly "
        "how many atoms of each element are present in one molecule of that compound. "
        "Which evaluation of the claim is correct?",
      choices=[
        "It is wrong, because the empirical formula gives only the lowest whole number "
        "ratio, which a molecule may contain several times over.",
        "It is wrong, because the empirical formula gives a ratio of masses rather than "
        "a ratio of atoms.",
        "It is correct, because a compound cannot contain more atoms than its formula "
        "lists.",
        "It is correct, but only for compounds that consist of formula units rather "
        "than molecules.",
        "It cannot be evaluated without knowing the percent composition of the "
        "compound."],
      ans=0,
      why="EK 1.3.A.3 defines the empirical formula as the lowest whole number ratio of "
          "atoms, and a lowest ratio is compatible with any whole number multiple of "
          "itself in an actual molecule. The formula is a ratio of atoms, which is "
          "where the second rejected option goes wrong."),

 dict(q="Using the molar masses in the table, compare the percent by mass of oxygen in "
        "carbon dioxide, CO2, with the percent by mass of oxygen in water, H2O.",
      table=_T_MM,
      choices=[
        "The percentage is larger in water, even though a molecule of carbon dioxide "
        "contains more oxygen atoms.",
        "The percentage is larger in carbon dioxide, because it contains twice as many "
        "oxygen atoms per molecule.",
        "The two percentages are equal, because oxygen has the same molar mass in both "
        "compounds.",
        "The percentage is larger in carbon dioxide, because carbon is heavier than "
        "hydrogen.",
        "The comparison cannot be made without knowing the masses of the two samples."],
      ans=0,
      why="The share of the mass is the oxygen contribution divided by the total molar "
          "mass, which is 32.0 over 44.0 against 16.0 over 18.0. Counting oxygen atoms "
          "rather than computing mass shares is what makes the rejected reasoning look "
          "right, and by EK 1.3.A.2 the sizes of the samples are irrelevant."),

 dict(q="Two different pure compounds are each formed from only nitrogen and oxygen. "
        "Which statement about the two compounds is supported by the law of definite "
        "proportions?",
      choices=[
        "Each compound has its own fixed mass ratio of nitrogen to oxygen, and the two "
        "ratios need not be equal to each other.",
        "Both compounds must have the same mass ratio of nitrogen to oxygen, since both "
        "contain the same two elements.",
        "Neither compound can have a fixed mass ratio, since two compounds of the same "
        "elements exist.",
        "The mass ratio of each compound varies with the temperature at which the "
        "sample was prepared.",
        "Only the compound with the larger molar mass has a fixed mass ratio of its "
        "elements."],
      ans=0,
      why="EK 1.3.A.2 constrains samples of one compound to a single mass ratio; it "
          "makes no claim relating one compound to a different compound. Two "
          "substances built from the same pair of elements are therefore each fixed "
          "internally without being fixed to each other."),
]
