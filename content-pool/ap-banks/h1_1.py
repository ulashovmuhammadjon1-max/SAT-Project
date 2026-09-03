r"""AP CHEMISTRY 1.1 Moles and Molar Mass.

CED effective Fall 2024, Unit 1 Atomic Structure and Properties.
Learning objective 1.1.A: calculate quantities of a substance or its relative
number of particles using dimensional analysis and the mole concept.
Suggested skill 5.B, identify an appropriate theory, definition, or
mathematical relationship to solve a problem.

Essential knowledge relied on, in the framework's own words:

  1.1.A.1  One cannot count particles directly while performing laboratory
           work. Thus, there must be a connection between the masses of
           substances reacting and the actual number of particles undergoing
           chemical changes.
  1.1.A.2  Avogadro's number (NA = 6.022 x 10^23 mol^-1) provides the
           connection between the number of moles in a pure sample of a
           substance and the number of constituent particles (or formula
           units) of that substance.
  1.1.A.3  Expressing the mass of an individual atom or molecule in atomic
           mass units (amu) is useful because the average mass in amu of one
           particle (atom or molecule) or formula unit of a substance will
           always be numerically equal to the molar mass of that substance in
           grams. Thus, there is a quantitative connection between the mass of
           a substance and the number of particles that the substance
           contains.
           EQN: n = m/M

ON MOLAR MASSES. Nothing here asks a student to recall one. Every molar mass an
item needs is either printed in the stem or carried in the item's own table,
and every arithmetic claim is recomputed from that number in verify_h1_1.py.
The AP exam supplies a periodic table; this bank does not assume one.

ON THE FORMULA-UNIT WORDING. EK 1.1.A.2 writes "constituent particles (or
formula units)" and EK 1.1.A.3 writes "one particle (atom or molecule) or
formula unit". Items 7 and 18 turn on that distinction and nothing more; the
bank never asserts a crystal structure, which the CED excludes at 2.3.A.1.

NOTATION. Hand-written spans per SCIENCE_BRIEF.md -- the converter does not run
on Chemistry. Chemical formulas stay plain text in prose (H2SO4, CO2); only the
scientific notation and the algebra are typeset. Gated by chem_notation.py and
rendered at throwOnError: true by chem_katex_gate.py.
"""
TOPIC = ("1.1", "Moles and Molar Mass", 1)

_T_MOLAR = dict(
    headers=["Substance", "Molar mass (grams per mole)"],
    rows=[["Water, H2O", "18.0"],
          ["Methane, CH4", "16.0"],
          ["Carbon dioxide, CO2", "44.0"],
          ["Sodium chloride, NaCl", "58.5"],
          ["Glucose, C6H12O6", "180.0"]])

_T_SAMPLES = dict(
    headers=["Sample", "Substance", "Mass of sample (grams)",
             "Molar mass (grams per mole)"],
    rows=[["Sample 1", "Water, H2O", "36.0", "18.0"],
          ["Sample 2", "Carbon dioxide, CO2", "44.0", "44.0"],
          ["Sample 3", "Methane, CH4", "8.0", "16.0"],
          ["Sample 4", "Glucose, C6H12O6", "90.0", "180.0"]])

_T_EQUAL_MASS = dict(
    headers=["Sample", "Substance", "Mass of sample (grams)",
             "Molar mass (grams per mole)"],
    rows=[["Sample W", "Helium, He", "12.0", "4.0"],
          ["Sample X", "Methane, CH4", "12.0", "16.0"],
          ["Sample Y", "Carbon dioxide, CO2", "12.0", "44.0"],
          ["Sample Z", "Glucose, C6H12O6", "12.0", "180.0"]])

_T_RANK = dict(
    headers=["Container", "Mass of substance (grams)",
             "Molar mass (grams per mole)"],
    rows=[["Container 1", "50.0", "25.0"],
          ["Container 2", "60.0", "20.0"],
          ["Container 3", "40.0", "40.0"],
          ["Container 4", "80.0", "16.0"]])

_T_UNKNOWNS = dict(
    headers=["Unknown", "Mass of sample (grams)", "Moles in the sample"],
    rows=[["Unknown J", "12.0", "0.500"],
          ["Unknown K", "12.0", "0.250"],
          ["Unknown L", "12.0", "1.50"],
          ["Unknown M", "12.0", "0.100"]])

QUESTIONS = [

 dict(q="A student weighs out a sample of solid potassium iodide on an analytical "
        "balance in order to work out how many particles of the compound the sample "
        "holds. Which of the following best explains why a quantity such as the mole "
        "is needed at all in this situation?",
      choices=[
        "Particles cannot be counted directly during laboratory work, so a measured "
        "mass must be connected to the number of particles taking part in the change.",
        "Mass is not conserved during a chemical change, so a count of particles is "
        "the only quantity that stays fixed.",
        "A balance reports the number of particles directly, and the mass of the "
        "sample then has to be worked out from that count.",
        "The number of particles in a sample rises as the sample is warmed, so a "
        "separate unit is needed for each temperature.",
        "A chemical formula gives only masses and never numbers of atoms, so the two "
        "quantities cannot be related to each other."],
      ans=0,
      why="EK 1.1.A.1 states that one cannot count particles directly while performing "
          "laboratory work, and that there must therefore be a connection between the "
          "masses of substances reacting and the actual number of particles undergoing "
          "chemical changes. The mole is that connection."),

 dict(q="Avogadro's number is \\(6.022 \\times 10^{23}\\) per mole. Which of the "
        "following does that constant supply?",
      choices=[
        "The number of constituent particles, or formula units, in one mole of a pure "
        "substance.",
        "The mass in grams of one atom of any element in the periodic table.",
        "The number of grams contained in one mole of any substance.",
        "The number of protons carried by one mole of atoms of any element.",
        "The volume in liters that one mole of any gas occupies."],
      ans=0,
      why="EK 1.1.A.2 states that Avogadro's number provides the connection between the "
          "number of moles in a pure sample of a substance and the number of "
          "constituent particles (or formula units) of that substance. It is a count "
          "per mole, not a mass, a volume or a nuclear property."),

 dict(q="Using the molar masses in the table, how many moles of carbon dioxide are "
        "present in a sample of CO2 that has a mass of 88.0 grams?",
      table=_T_MOLAR,
      choices=["2.00 moles", "0.500 moles", "0.0500 moles", "22.0 moles",
               "3.87 moles"],
      ans=0,
      why="The relationship is n = m/M from EK 1.1.A.3. Dividing 88.0 grams by the "
          "tabulated molar mass of 44.0 grams per mole gives 2.00 moles, and the "
          "reciprocal division would give the value near 0.500 instead."),

 dict(q="A chemist notes that the average mass of one molecule of a certain compound "
        "is 44.0 atomic mass units and that the molar mass of the same compound is "
        "44.0 grams per mole. Which statement best accounts for the two numbers "
        "agreeing?",
      choices=[
        "The average mass in atomic mass units of one particle of a substance is "
        "always numerically equal to the molar mass of that substance in grams.",
        "One atomic mass unit and one gram are two names for the same quantity of "
        "mass.",
        "The molar mass of a substance is defined as the mass in grams of a single one "
        "of its molecules.",
        "Atomic mass units are used for elements while grams per mole are used for "
        "compounds, so the numbers cannot disagree.",
        "The mass in atomic mass units of one particle equals Avogadro's number "
        "multiplied by the molar mass."],
      ans=0,
      why="EK 1.1.A.3 states this numerical equality outright and calls it the reason "
          "the atomic mass unit is useful: it is what makes a measured mass in grams "
          "translate into a number of particles."),

 dict(q="A sealed flask holds 0.250 moles of neon gas. How many neon atoms does the "
        "flask hold?",
      choices=[
        "\\(1.51 \\times 10^{23}\\) atoms",
        "\\(6.02 \\times 10^{23}\\) atoms",
        "\\(2.41 \\times 10^{24}\\) atoms",
        "\\(1.51 \\times 10^{22}\\) atoms",
        "\\(4.00 \\times 10^{23}\\) atoms"],
      ans=0,
      why="EK 1.1.A.2 makes Avogadro's number the conversion from moles to particles, "
          "so the count is 0.250 multiplied by \\(6.022 \\times 10^{23}\\), which is "
          "about \\(1.51 \\times 10^{23}\\). Dividing instead of multiplying produces "
          "the value near \\(2.41 \\times 10^{24}\\)."),

 dict(q="A sample of argon is found to contain \\(3.01 \\times 10^{23}\\) atoms. How "
        "many moles of argon are present?",
      choices=["0.500 moles", "2.00 moles", "1.00 moles", "0.250 moles",
               "\\(1.81 \\times 10^{47}\\) moles"],
      ans=0,
      why="Dividing the particle count by Avogadro's number, as EK 1.1.A.2 requires, "
          "gives \\(3.01 \\times 10^{23}\\) divided by \\(6.022 \\times 10^{23}\\), "
          "which is 0.500. Multiplying the two instead produces the impossibly large "
          "value."),

 dict(q="Sodium chloride is an ionic compound that does not exist as discrete NaCl "
        "molecules. Which of the following best describes what one mole of sodium "
        "chloride contains?",
      choices=[
        "\\(6.022 \\times 10^{23}\\) formula units, each of which supplies one sodium "
        "ion and one chloride ion.",
        "\\(6.022 \\times 10^{23}\\) individual NaCl molecules held together by "
        "covalent bonds.",
        "\\(6.022 \\times 10^{23}\\) sodium ions and no chloride ions, since only one "
        "kind of particle can be counted at a time.",
        "\\(3.011 \\times 10^{23}\\) ion pairs, because two ions must share a single "
        "count.",
        "\\(1.204 \\times 10^{24}\\) formula units, because the compound contains two "
        "elements."],
      ans=0,
      why="EK 1.1.A.2 writes the countable entity as the number of constituent "
          "particles or formula units, which is the wording that covers a substance "
          "with no discrete molecules. One mole is Avogadro's number of those units "
          "whatever the unit happens to be."),

 dict(q="Four samples were prepared as shown in the table. Which sample contains the "
        "greatest number of particles of the substance named?",
      table=_T_SAMPLES,
      choices=["Sample 1, which holds 2.00 moles",
               "Sample 2, which holds 1.00 mole",
               "Sample 3, which holds 0.50 mole",
               "Sample 4, which holds 0.50 mole",
               "All four samples hold the same number of particles because each is a "
               "pure substance"],
      ans=0,
      why="The number of particles goes as the number of moles, by EK 1.1.A.2, and "
          "n = m/M gives 2.00 moles for the water sample against 1.00 and 0.50 for the "
          "others. The largest mass in the table is not the largest count, which is "
          "the point of the comparison."),

 dict(q="What mass of glucose is needed to supply 2.50 moles of the compound, given "
        "the molar masses in the table?",
      table=_T_MOLAR,
      choices=["450 grams", "72.0 grams", "180 grams", "0.0139 grams",
               "1,130 grams"],
      ans=0,
      why="Rearranging n = m/M from EK 1.1.A.3 gives m equal to n multiplied by M, so "
          "2.50 moles multiplied by the tabulated 180.0 grams per mole is 450 grams. "
          "Dividing rather than multiplying gives the very small value."),

 dict(q="Sulfuric acid has the formula H2SO4. How many moles of oxygen atoms are "
        "present in 1.00 mole of sulfuric acid?",
      choices=["4.00 moles of oxygen atoms", "1.00 mole of oxygen atoms",
               "2.00 moles of oxygen atoms", "7.00 moles of oxygen atoms",
               "\\(2.41 \\times 10^{24}\\) moles of oxygen atoms"],
      ans=0,
      why="The subscript in the formula fixes the ratio of atoms to formula units, so "
          "each mole of the compound supplies four moles of oxygen atoms. The value "
          "of seven counts every atom in the formula rather than the oxygen atoms "
          "alone."),

 dict(q="Equal masses of 10.0 grams of methane, CH4, and of carbon dioxide, CO2, are "
        "placed in separate flasks. Using the molar masses in the table, which flask "
        "holds more molecules, and why?",
      table=_T_MOLAR,
      choices=[
        "The methane flask, because the smaller molar mass means the same mass "
        "corresponds to more moles.",
        "The carbon dioxide flask, because the larger molar mass means the same mass "
        "corresponds to more moles.",
        "The carbon dioxide flask, because its molecules each contain more atoms than "
        "a methane molecule does.",
        "Neither flask, because equal masses of any two substances always contain "
        "equal numbers of molecules.",
        "The methane flask, because gases of low molar mass are compressed into a "
        "smaller volume."],
      ans=0,
      why="With n = m/M and the mass held fixed, the number of moles varies inversely "
          "with the molar mass, so the tabulated 16.0 grams per mole gives more moles "
          "than 44.0 does. EK 1.1.A.2 then makes the larger mole count the larger "
          "particle count."),

 dict(q="Two flasks each contain 0.400 moles of a pure gas. One holds helium, of molar "
        "mass 4.0 grams per mole, and the other holds argon, of molar mass 40.0 grams "
        "per mole. Which statement about the two flasks is correct?",
      choices=[
        "The two flasks hold the same number of atoms, and the argon sample has the "
        "greater mass.",
        "The two flasks hold the same number of atoms, and the helium sample has the "
        "greater mass.",
        "The helium flask holds ten times as many atoms as the argon flask does.",
        "The argon flask holds ten times as many atoms as the helium flask does.",
        "The two flasks hold both the same number of atoms and the same mass."],
      ans=0,
      why="Equal numbers of moles mean equal numbers of particles by EK 1.1.A.2, while "
          "m equals n multiplied by M from EK 1.1.A.3 makes the mass ten times larger "
          "for the gas whose molar mass is ten times larger."),

 dict(q="The table lists the contents of four containers. In which container is the "
        "number of moles of substance the greatest?",
      table=_T_RANK,
      choices=["Container 4", "Container 1", "Container 2", "Container 3",
               "Containers 1 and 2 tie for the greatest number of moles"],
      ans=0,
      why="Applying n = m/M to each row gives 2.00, 3.00, 1.00 and 5.00 moles in turn, "
          "so the container with both the largest mass and the smallest molar mass "
          "wins. Choosing on mass alone or on molar mass alone gives a different and "
          "wrong answer."),

 dict(q="A student has a mass in grams of a pure molecular compound and wants the "
        "number of molecules present. Which sequence of operations produces it?",
      choices=[
        "Divide the mass by the molar mass, then multiply by Avogadro's number.",
        "Multiply the mass by the molar mass, then multiply by Avogadro's number.",
        "Divide the mass by Avogadro's number, then multiply by the molar mass.",
        "Multiply the mass by Avogadro's number, then multiply by the molar mass.",
        "Divide the mass by the molar mass, then divide by Avogadro's number."],
      ans=0,
      why="EK 1.1.A.3 gives n = m/M for the first step and EK 1.1.A.2 makes Avogadro's "
          "number the moles-to-particles factor for the second. Each rejected sequence "
          "leaves units that are not a count of molecules."),

 dict(q="The average mass of one molecule of a certain gas is 30.0 atomic mass units. "
        "A sample of that gas has a mass of 60.0 grams. How many moles are in the "
        "sample?",
      choices=["2.00 moles", "0.500 moles", "30.0 moles", "1,800 moles",
               "0.0333 moles"],
      ans=0,
      why="EK 1.1.A.3 makes the molar mass numerically equal to the average particle "
          "mass in atomic mass units, so the molar mass is 30.0 grams per mole and "
          "n = m/M gives 60.0 divided by 30.0. The trap is to treat the two units as "
          "unrelated and leave the problem unsolvable."),

 dict(q="A procedure calls for 0.100 moles of a solid compound whose molar mass is "
        "84.0 grams per mole. Which single laboratory measurement lets the student "
        "deliver that quantity?",
      choices=[
        "Weighing out 8.40 grams of the solid on a balance.",
        "Weighing out 84.0 grams of the solid on a balance.",
        "Counting out \\(6.022 \\times 10^{23}\\) particles of the solid.",
        "Measuring 0.100 liters of the solid in a graduated cylinder.",
        "Weighing out 840 grams of the solid on a balance."],
      ans=0,
      why="EK 1.1.A.1 says the count cannot be made directly, so the mole quantity has "
          "to be delivered as a mass: 0.100 multiplied by 84.0 grams per mole is 8.40 "
          "grams. The rejected options either deliver a full mole or attempt the "
          "direct count the framework rules out."),

 dict(q="A 20.0 gram sample of a pure compound is found to contain 0.250 moles of that "
        "compound. What is the molar mass of the compound?",
      choices=["80.0 grams per mole", "5.00 grams per mole",
               "0.0125 grams per mole", "20.0 grams per mole",
               "8.00 grams per mole"],
      ans=0,
      why="Rearranging n = m/M gives M equal to m divided by n, so 20.0 grams divided "
          "by 0.250 moles is 80.0 grams per mole. Multiplying the two numbers instead "
          "produces the value of 5.00."),

 dict(q="Magnesium chloride, MgCl2, is an ionic compound. How many moles of ions are "
        "released when 1.00 mole of magnesium chloride dissolves completely in water?",
      choices=["3.00 moles of ions", "1.00 mole of ions", "2.00 moles of ions",
               "6.00 moles of ions", "0.500 moles of ions"],
      ans=0,
      why="The formula unit named in EK 1.1.A.2 supplies one magnesium ion and two "
          "chloride ions, so a mole of formula units supplies three moles of ions. "
          "Counting only the chloride ions gives the value of two."),

 dict(q="Four unknown solids were each weighed and the number of moles in each sample "
        "determined, as shown. Which unknown has the largest molar mass?",
      table=_T_UNKNOWNS,
      choices=["Unknown M", "Unknown J", "Unknown K", "Unknown L",
               "All four have the same molar mass because all four masses are equal"],
      ans=0,
      why="With M equal to m divided by n and every mass equal, the largest molar mass "
          "belongs to the sample holding the fewest moles. The tabulated values give "
          "24.0, 48.0, 8.00 and 120 grams per mole in row order."),

 dict(q="A chemist doubles the mass of a pure sample of a compound while keeping the "
        "compound the same. Which statement describes what happens to the number of "
        "moles and to the molar mass?",
      choices=[
        "The number of moles doubles and the molar mass is unchanged.",
        "The number of moles is unchanged and the molar mass doubles.",
        "Both the number of moles and the molar mass double.",
        "The number of moles doubles and the molar mass is halved.",
        "Neither quantity changes, because both depend only on the identity of the "
        "compound."],
      ans=0,
      why="In n = m/M the molar mass is a property of the substance and not of the "
          "size of the sample, so doubling m with M fixed doubles n. Treating the "
          "molar mass as something a larger sample changes is the misconception the "
          "rejected options share."),

 dict(q="A student writes that Avogadro's number is the mass in grams of one mole of a "
        "substance. Which correction is appropriate?",
      choices=[
        "Avogadro's number is a count of particles per mole; the mass in grams of one "
        "mole is the molar mass.",
        "Avogadro's number is a count of particles per gram; the mass in grams of one "
        "mole is the atomic mass unit.",
        "Avogadro's number is a mass, but it applies only to elements and not to "
        "compounds.",
        "Avogadro's number is a volume per mole, and the student has confused it with "
        "the molar mass.",
        "The student is correct, because the molar mass and Avogadro's number are two "
        "names for the same quantity."],
      ans=0,
      why="EK 1.1.A.2 defines Avogadro's number as the link between moles and the "
          "number of constituent particles, so its units are particles per mole. The "
          "mass of a mole is the separate quantity that EK 1.1.A.3 relates to the "
          "average particle mass in atomic mass units."),

 dict(q="A copper sample contains \\(6.022 \\times 10^{22}\\) copper atoms. How many "
        "moles of copper does the sample contain?",
      choices=["0.100 moles", "1.00 mole", "10.0 moles", "0.0100 moles",
               "6.02 moles"],
      ans=0,
      why="Dividing \\(6.022 \\times 10^{22}\\) by \\(6.022 \\times 10^{23}\\) gives "
          "0.100, applying the moles-to-particles connection of EK 1.1.A.2 in "
          "reverse. Misreading the exponent by one place gives the value of 1.00."),

 dict(q="A sample of sulfur contains \\(3.011 \\times 10^{23}\\) sulfur atoms. If the "
        "molar mass of sulfur is 32.0 grams per mole, what is the mass of the sample?",
      choices=["16.0 grams", "32.0 grams", "64.0 grams", "9.63 grams",
               "0.500 grams"],
      ans=0,
      why="The atom count is half of Avogadro's number, which is 0.500 moles by EK "
          "1.1.A.2, and multiplying by 32.0 grams per mole gives 16.0 grams. Treating "
          "the count as a full mole gives the value of 32.0."),

 dict(q="A 100 gram sample of a pure compound is divided into two equal portions. "
        "Which quantity has the same value for one portion as it had for the whole "
        "original sample?",
      choices=["The molar mass of the compound",
               "The mass of the sample",
               "The number of moles in the sample",
               "The number of molecules in the sample",
               "The number of oxygen atoms in the sample"],
      ans=0,
      why="The molar mass in n = m/M is a property of the substance and not of how "
          "much of it is present, while mass, moles and particle counts all scale with "
          "the size of the portion."),

 dict(q="Each sample in the table has a mass of 12.0 grams. Which sample contains the "
        "smallest number of particles?",
      table=_T_EQUAL_MASS,
      choices=["Sample Z, which holds about 0.0667 moles",
               "Sample W, which holds 3.00 moles",
               "Sample X, which holds 0.750 moles",
               "Sample Y, which holds about 0.273 moles",
               "All four samples hold the same number of particles because the masses "
               "are equal"],
      ans=0,
      why="With the mass fixed, n = m/M makes the number of moles smallest for the "
          "largest molar mass, and EK 1.1.A.2 makes the smallest mole count the "
          "smallest particle count. Equal masses of different substances are exactly "
          "what EK 1.1.A.1 warns cannot be read as equal counts."),

 dict(q="How many moles of atoms in total are present in 0.500 moles of methane, CH4?",
      choices=["2.50 moles of atoms", "0.500 moles of atoms",
               "2.00 moles of atoms", "5.00 moles of atoms",
               "1.50 moles of atoms"],
      ans=0,
      why="One molecule of the compound carries five atoms, one carbon and four "
          "hydrogen, so 0.500 moles of molecules carries 2.50 moles of atoms. "
          "Counting the hydrogen atoms alone gives the value of 2.00."),

 dict(q="Sample P and sample Q contain the same number of molecules. Sample P is a "
        "compound of molar mass 20.0 grams per mole and sample Q is a compound of "
        "molar mass 60.0 grams per mole. Which statement about the masses of the two "
        "samples is correct?",
      choices=[
        "The mass of sample Q is three times the mass of sample P.",
        "The mass of sample P is three times the mass of sample Q.",
        "The two samples have equal masses, because they hold equal numbers of "
        "molecules.",
        "The mass of sample Q is nine times the mass of sample P.",
        "The two masses cannot be compared without knowing the number of molecules."],
      ans=0,
      why="Equal particle counts mean equal mole counts by EK 1.1.A.2, and m equals n "
          "multiplied by M, so the mass ratio is exactly the molar mass ratio of three "
          "to one. The number of molecules cancels and therefore need not be known."),

 dict(q="What mass of water is required to supply \\(1.204 \\times 10^{24}\\) water "
        "molecules, given the molar masses in the table?",
      table=_T_MOLAR,
      choices=["36.0 grams", "18.0 grams", "9.00 grams", "72.0 grams",
               "\\(2.17 \\times 10^{25}\\) grams"],
      ans=0,
      why="The count is twice Avogadro's number, so the sample is 2.00 moles by EK "
          "1.1.A.2, and multiplying by the tabulated 18.0 grams per mole gives 36.0 "
          "grams. Skipping the conversion to moles altogether produces the absurd "
          "value."),

 dict(q="Why is it useful to express the mass of an individual atom or molecule in "
        "atomic mass units rather than in grams?",
      choices=[
        "Because that average mass in atomic mass units is numerically the same as the "
        "molar mass in grams, which turns a weighed mass into a number of particles.",
        "Because the atomic mass unit is a larger unit than the gram and so needs "
        "fewer digits.",
        "Because masses in grams cannot be measured for solids, only for liquids and "
        "gases.",
        "Because the atomic mass unit already includes Avogadro's number, so no "
        "further conversion is ever required.",
        "Because atomic mass units apply to single particles while grams apply only to "
        "whole moles, and the two can never be compared."],
      ans=0,
      why="EK 1.1.A.3 gives precisely this reason: the numerical equality is what "
          "supplies the quantitative connection between the mass of a substance and "
          "the number of particles it contains. The atomic mass unit is far smaller "
          "than a gram, not larger."),

 dict(q="Two students argue about a 5.00 gram sample of an unknown pure solid. The "
        "first says the number of particles in the sample can be found once the "
        "identity of the solid is known; the second says no number of particles can "
        "ever be assigned to a sample that has only been weighed. Which evaluation is "
        "correct?",
      choices=[
        "The first student is correct, because the identity fixes the molar mass and "
        "the molar mass converts the weighed mass into moles and then into particles.",
        "The second student is correct, because a mass measurement carries no "
        "information about how many particles are present.",
        "The second student is correct, because only a sample of a gas can be "
        "converted from mass to a number of particles.",
        "The first student is correct, because a balance reports the number of "
        "particles alongside the mass.",
        "Neither student is correct, because the number of particles depends on the "
        "temperature at which the sample is weighed."],
      ans=0,
      why="EK 1.1.A.1 asserts that the connection between mass and particle number "
          "exists precisely because direct counting is impossible, and EK 1.1.A.3 "
          "supplies it through the molar mass. What the identity of the substance adds "
          "is the value of M in n = m/M."),
]
