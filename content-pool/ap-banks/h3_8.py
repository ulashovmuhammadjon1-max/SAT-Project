r"""AP CHEMISTRY 3.8 Representations of Solutions.

CED effective Fall 2024, Unit 3 Properties of Substances and Mixtures.
Learning objective 3.8.A: using particulate models for mixtures,
  i. represent interactions between components;
  ii. represent concentrations of components.
Suggested skill 3.C, represent visually the relationship between the structures
and interactions across multiple levels or scales.

Essential knowledge relied on, in the framework's own words:

  3.8.A.1  Particulate representations of solutions communicate the structure
           and properties of solutions, by illustration of the relative
           concentrations of the components in the solution and/or drawings that
           show interactions among the components.

           Exclusion Statement: Colligative properties will not be assessed on
           the AP Exam.
           Exclusion Statement: Calculations of molality, percent by mass, and
           percent by volume for solutions will not be assessed on the AP Exam.

THE PROBLEM THIS TOPIC POSES, AND HOW IT IS SOLVED HERE. The whole topic is
about pictures and this bank cannot show one. So no item asks a student to read
a drawing. Instead every drawing is DESCRIBED -- as a count of particles in a
table, or as explicit numbers in the stem -- and the question is asked of the
description. verify_h3_8.py enforces that mechanically: any stem that says a
representation SHOWS something must either carry a table or state the counts in
figures, and no stem may point at anything with a deictic word like "above",
"below" or "as shown".

THE STOICHIOMETRY IS SUPPLIED BY THE STEM, NOT ASSUMED. Where an item asks
whether a drawing represents a dissolved ionic compound correctly, the stem
states how many cations and anions each formula unit provides. Deciding that
for a named formula is unit 2 and unit 4 material; what EK 3.8.A.1 owns is
whether the drawing shows the components in the right relative amounts, and that
is all these items test.

THE EXCLUSIONS ARE CONTENT HERE. Two items key them, since knowing what is out
of scope is worth knowing. Everywhere else the excluded measures appear only as
distractors, and verify_h3_8.py refuses any key stating one unless the stem
frames it as excluded or as something representations do not communicate.

ARITHMETIC. Every ratio and every ranking a key asserts is recomputed in
verify_h3_8.py from the table or the stated counts alone.

NOTATION. Plain prose; no math spans are needed in this module.
"""
TOPIC = ("3.8", "Representations of Solutions", 3)

# Four described drawings of the same solute in the same solvent, each said to
# depict the same volume. Ratios recompute to 0.20, 0.40, 0.10 and 0.10.
_T_REP = dict(
    headers=["Representation", "Solute particles drawn", "Solvent particles drawn"],
    rows=[["Representation 1", "4", "20"],
          ["Representation 2", "8", "20"],
          ["Representation 3", "2", "20"],
          ["Representation 4", "4", "40"]])

# Four described drawings of a dissolved ionic compound. The stem of each item
# states how many cations and anions one formula unit provides.
_T_IONS = dict(
    headers=["Drawing", "Cations drawn", "Anions drawn"],
    rows=[["Drawing W", "6", "3"],
          ["Drawing X", "3", "6"],
          ["Drawing Y", "4", "4"],
          ["Drawing Z", "2", "6"]])

# Described drawings that differ in the volume they depict as well as in the
# number of solute particles.
_T_CONC = dict(
    headers=["Beaker", "Volume represented (mL)", "Solute particles drawn"],
    rows=[["Beaker A", "100", "10"],
          ["Beaker B", "200", "10"],
          ["Beaker C", "100", "20"],
          ["Beaker D", "200", "60"]])

QUESTIONS = [

 dict(q="What does the framework say particulate representations of solutions communicate?",
      choices=[
        "The structure and properties of solutions",
        "The cost of preparing the solution",
        "The exact molar mass of the solute",
        "The temperature at which the solution was prepared",
        "The order in which the components were mixed"],
      ans=0,
      why="EK 3.8.A.1 opens by saying that particulate representations of solutions "
          "communicate the structure and properties of solutions. It is a claim about what a "
          "picture at the particle scale can convey about the substance, not about the "
          "history of the sample."),

 dict(q="By what two means does the framework say particulate representations communicate "
        "what they communicate?",
      choices=[
        "By illustrating the relative concentrations of the components, and by drawings that "
        "show interactions among the components",
        "By listing the masses of the components, and by naming the solvent",
        "By reporting the percent by mass, and by giving the boiling point",
        "By showing the container's shape, and by labelling the temperature",
        "By giving the molar mass of each component, and by giving its melting point"],
      ans=0,
      why="EK 3.8.A.1 names exactly those two means: illustration of the relative "
          "concentrations of the components in the solution, and drawings that show "
          "interactions among the components. Both are things a particle-scale picture can "
          "carry."),

 dict(q="Which class of property does an exclusion statement attached to this topic place "
        "outside the exam?",
      choices=[
        "Colligative properties",
        "Intermolecular forces",
        "Relative concentrations of components",
        "Interactions among components",
        "The structure of solutions"],
      ans=0,
      why="One of the two exclusion statements attached to EK 3.8.A.1 says colligative "
          "properties will not be assessed on the AP Exam. The four rejected options are "
          "each named in the essential knowledge statement itself as things this topic is "
          "about."),

 dict(q="Which calculations does an exclusion statement attached to this topic place outside "
        "the exam?",
      choices=[
        "Calculations of molality, percent by mass, and percent by volume for solutions",
        "Calculations of molarity for solutions",
        "Calculations of the number of moles of solute",
        "Calculations of the volume of a solution",
        "All calculations involving solutions"],
      ans=0,
      why="The second exclusion statement attached to EK 3.8.A.1 names those three "
          "calculations specifically. Molarity is not among them, and learning objective "
          "3.7.A explicitly asks for the number of solute particles, the volume and the "
          "molarity to be calculated."),

 dict(q="The learning objective for this topic asks students to use particulate models for "
        "mixtures to do two things. What is the first of them?",
      choices=[
        "Represent interactions between components",
        "Represent the mass of each component",
        "Represent the boiling point of the mixture",
        "Represent the order in which components dissolve",
        "Represent the cost of each component"],
      ans=0,
      why="Learning objective 3.8.A lists representing interactions between components as "
          "its first part, and EK 3.8.A.1 backs it by naming drawings that show interactions "
          "among the components as one of the two means of communication."),

 dict(q="Besides representing interactions, what second thing does this topic's learning "
        "objective ask a particulate model for mixtures to represent?",
      choices=[
        "Represent concentrations of components",
        "Represent the density of the solvent",
        "Represent the vapour pressure of the mixture",
        "Represent the electrical conductivity of the mixture",
        "Represent the age of the sample"],
      ans=0,
      why="Learning objective 3.8.A lists representing concentrations of components as its "
          "second part, and EK 3.8.A.1 backs it by naming illustration of the relative "
          "concentrations of the components as one of the two means of communication."),

 dict(q="Two particulate representations depict equal volumes of the same solution system. "
        "What must be true of the one representing the more concentrated solution?",
      choices=[
        "It draws more solute particles in the same depicted volume",
        "It draws fewer solute particles in the same depicted volume",
        "It draws the solute particles larger",
        "It draws the container larger",
        "It draws the solvent particles further apart"],
      ans=0,
      why="EK 3.8.A.1 makes the illustration of relative concentrations one of the two things "
          "a particulate representation does, and concentration at a fixed depicted volume is "
          "carried by how many solute particles appear. Drawing the same number of particles "
          "larger changes its appearance without changing the amounts it depicts."),

 dict(q="Representation P shows 5 solute particles among 25 solvent particles. Representation "
        "Q shows 5 solute particles among 50 solvent particles. Which represents the more "
        "concentrated solution?",
      choices=[
        "Representation P",
        "Representation Q",
        "They represent the same concentration",
        "Neither, because concentration cannot be represented by particle counts",
        "It cannot be decided without the molar mass of the solute"],
      ans=0,
      why="EK 3.8.A.1 has such a drawing illustrate the RELATIVE concentrations of the "
          "components, so the comparison is between the counts of solute and solvent within "
          "each picture. The two drawings show the same number of solute particles, so the "
          "one carrying fewer solvent particles is the more concentrated."),

 dict(q="Two drawings each show 8 solute particles. The first is said to depict 100 mL of "
        "solution and the second 200 mL. Which represents the more concentrated solution?",
      choices=[
        "The first drawing",
        "The second drawing",
        "They represent the same concentration",
        "Neither, because a drawing cannot depict a volume",
        "It cannot be decided without the number of solvent particles"],
      ans=0,
      why="EK 3.8.A.1 makes relative concentration the thing being illustrated, and "
          "concentration is an amount per volume. The same number of solute particles spread "
          "through a larger depicted volume is the more dilute of the two."),

 dict(q="A particulate drawing of a solution places several polar solvent molecules around a "
        "dissolved ion, each oriented in a particular direction. Which part of the "
        "framework's account does that drawing serve?",
      choices=[
        "Drawings that show interactions among the components",
        "Illustration of the relative concentrations of the components",
        "Calculation of the percent by mass of the solute",
        "Measurement of a colligative property",
        "Determination of the molar mass of the solvent"],
      ans=0,
      why="EK 3.8.A.1 names drawings that show interactions among the components as one of "
          "its two means, and EK 3.1.A.3 makes the orientation of a solvent dipole toward an "
          "ion the qualitative content of such an interaction. Orientation carries "
          "information about interaction rather than about how much of each component is "
          "present."),

 dict(q="Which of the following is NOT something the framework says a particulate "
        "representation of a solution communicates?",
      choices=[
        "The percent by mass of the solute",
        "The structure of the solution",
        "The properties of the solution",
        "The relative concentrations of the components",
        "The interactions among the components"],
      ans=0,
      why="EK 3.8.A.1 names structure, properties, relative concentrations and interactions, "
          "and one of the exclusion statements attached to it puts calculations of percent by "
          "mass outside the exam altogether. The four rejected options are each drawn from "
          "the sentence itself."),

 dict(q="The framework says representations illustrate the RELATIVE concentrations of the "
        "components. What does that word contribute?",
      choices=[
        "That the drawing shows how the components' amounts compare with one another",
        "That the drawing gives an absolute measured concentration in moles per litre",
        "That the drawing applies only to dilute solutions",
        "That the drawing applies only to concentrated solutions",
        "That the drawing shows the concentration relative to a standard solution kept in "
        "the laboratory"],
      ans=0,
      why="EK 3.8.A.1's phrase is the relative concentrations of the components in the "
          "solution, which is a comparison among the things drawn. A count of particles in a "
          "picture carries that comparison without carrying any measured value in moles per "
          "litre."),

 dict(q="The framework joins its two means of communication with the words AND/OR. What does "
        "that allow?",
      choices=[
        "A representation may illustrate relative concentrations, show interactions, or do "
        "both",
        "A representation must do both at once or it communicates nothing",
        "A representation may show interactions but never concentrations",
        "A representation may show concentrations but never interactions",
        "A representation may do neither and still communicate structure"],
      ans=0,
      why="EK 3.8.A.1 writes illustration of the relative concentrations and/or drawings that "
          "show interactions, which permits either means alone as well as the two together. "
          "Requiring both would be a stronger claim than the sentence makes."),

 dict(q="An ionic compound dissolves so that every formula unit provides 2 cations and 1 "
        "anion. A drawing of the solution shows 6 cations and 3 anions. Does it represent "
        "the relative amounts correctly?",
      choices=[
        "Yes, because the drawn cations outnumber the drawn anions two to one",
        "No, because a drawing must show equal numbers of cations and anions",
        "No, because the drawn anions should outnumber the drawn cations two to one",
        "Yes, but only because the total number of ions drawn is odd",
        "It cannot be decided without the volume the drawing depicts"],
      ans=0,
      why="EK 3.8.A.1 makes the relative concentrations of the components the thing such a "
          "drawing carries, and the stem states what those relative amounts must be. Six to "
          "three is the stated two-to-one ratio, so the drawing matches the composition the "
          "stem supplies."),

 dict(q="A drawing of a solution shows 5 cations and 3 anions, and the compound dissolved "
        "in it provides 2 cations and 1 anion per formula unit. Does the drawing represent "
        "the relative amounts correctly?",
      choices=[
        "No, because five to three is not the stated two-to-one ratio",
        "Yes, because more cations than anions are drawn",
        "Yes, because the numbers drawn are both small",
        "No, because a drawing must show equal numbers of cations and anions",
        "It cannot be decided without the identity of the compound"],
      ans=0,
      why="EK 3.8.A.1 makes the drawing's job the relative amounts of the components, and the "
          "stem states the ratio those amounts must take. Drawing more cations than anions is "
          "necessary but not sufficient, since the ratio itself has to come out right."),

 dict(q="The tabulated representations each depict the same volume of the same solution "
        "system. Which represents the most concentrated solution?",
      table=_T_REP,
      choices=[
        "Representation 2",
        "Representation 1",
        "Representation 3",
        "Representation 4",
        "All four represent the same concentration"],
      ans=0,
      why="EK 3.8.A.1 has each drawing illustrate the relative concentrations of its "
          "components, so the count of solute particles is compared with the count of solvent "
          "particles within each row rather than across rows."),

 dict(q="Which two of the tabulated representations depict the same relative concentration "
        "as each other?",
      table=_T_REP,
      choices=[
        "Representations 3 and 4",
        "Representations 1 and 2",
        "Representations 1 and 3",
        "Representations 2 and 4",
        "No two of them depict the same relative concentration"],
      ans=0,
      why="EK 3.8.A.1's relative concentration is a ratio, so two drawings can agree in it "
          "while differing in both the number of solute particles and the number of solvent "
          "particles drawn, which is what one pair in the table does."),

 dict(q="Which tabulated representation depicts twice the relative concentration of "
        "Representation 1?",
      table=_T_REP,
      choices=[
        "Representation 2",
        "Representation 3",
        "Representation 4",
        "None of them depicts twice that concentration",
        "All of the others depict twice that concentration"],
      ans=0,
      why="EK 3.8.A.1's relative concentration is the ratio of the components within one "
          "drawing, so the row wanted is the one whose ratio of solute to solvent particles "
          "is double the reference row's."),

 dict(q="In how many of the tabulated representations do the solute particles drawn exceed "
        "one for every ten solvent particles drawn?",
      table=_T_REP,
      choices=[
        "Exactly two",
        "Exactly one",
        "Exactly three",
        "All four",
        "None of them"],
      ans=0,
      why="EK 3.8.A.1's relative concentration is formed within each drawing, so each "
          "tabulated row's ratio of solute to solvent particles is compared with the stated "
          "threshold in turn."),

 dict(q="An ionic compound provides 2 cations and 1 anion per formula unit. Which tabulated "
        "drawing represents its solution correctly?",
      table=_T_IONS,
      choices=[
        "Drawing W",
        "Drawing X",
        "Drawing Y",
        "Drawing Z",
        "None of the tabulated drawings does"],
      ans=0,
      why="EK 3.8.A.1 makes the relative amounts of the components the content of the "
          "drawing, and the stem supplies the ratio those amounts must take. Only one "
          "tabulated row draws twice as many cations as anions."),

 dict(q="A different ionic compound provides 1 cation and 3 anions per formula unit. Which "
        "tabulated drawing represents its solution correctly?",
      table=_T_IONS,
      choices=[
        "Drawing Z",
        "Drawing W",
        "Drawing X",
        "Drawing Y",
        "None of the tabulated drawings does"],
      ans=0,
      why="The stem supplies the ratio and EK 3.8.A.1 makes matching it the drawing's job. "
          "Only one tabulated row draws three times as many anions as cations."),

 dict(q="A third ionic compound provides 1 cation and 1 anion per formula unit. Which "
        "tabulated drawing represents its solution correctly?",
      table=_T_IONS,
      choices=[
        "Drawing Y",
        "Drawing W",
        "Drawing X",
        "Drawing Z",
        "None of the tabulated drawings does"],
      ans=0,
      why="The stem supplies the ratio and EK 3.8.A.1 makes the relative amounts the content "
          "of the drawing. Only one tabulated row draws the two kinds of ion in equal "
          "numbers."),

 dict(q="Each tabulated beaker is drawn with the volume of solution it represents. Which "
        "depicts the most concentrated solution?",
      table=_T_CONC,
      choices=[
        "Beaker D",
        "Beaker A",
        "Beaker B",
        "Beaker C",
        "All four depict the same concentration"],
      ans=0,
      why="EK 3.8.A.1 has the drawing carry concentration, and concentration is an amount per "
          "volume, so the number of solute particles drawn has to be set against the volume "
          "that row depicts rather than compared on its own."),

 dict(q="Of the tabulated beakers, which depicts the most dilute solution?",
      table=_T_CONC,
      choices=[
        "Beaker B",
        "Beaker A",
        "Beaker C",
        "Beaker D",
        "All four depict the same concentration"],
      ans=0,
      why="EK 3.8.A.1's concentration is an amount per volume, so the row wanted is the one "
          "with the fewest solute particles drawn for the volume it depicts, which is not "
          "simply the row with the fewest particles."),

 dict(q="Which tabulated beaker depicts twice the concentration of Beaker A?",
      table=_T_CONC,
      choices=[
        "Beaker C",
        "Beaker B",
        "Beaker D",
        "None of them depicts twice that concentration",
        "All three of the others depict twice that concentration"],
      ans=0,
      why="Concentration is the number of solute particles drawn divided by the volume "
          "depicted, so the row wanted is the one whose quotient is double the reference "
          "row's. Doubling the particles alone would not do it if the volume doubled too."),

 dict(q="How many of the tabulated beakers depict a solution more concentrated than Beaker "
        "A?",
      table=_T_CONC,
      choices=[
        "Exactly two",
        "Exactly one",
        "Exactly three",
        "None of them",
        "All of the others"],
      ans=0,
      why="Each row's number of solute particles is divided by the volume that row depicts "
          "and the quotients are compared with the reference row's, since EK 3.8.A.1 makes "
          "concentration what the drawing carries."),

 dict(q="A student wants a drawing to communicate an ion-dipole interaction in a solution. "
        "Which feature of the drawing would do that?",
      choices=[
        "Polar solvent molecules drawn with their partially negative ends turned toward a "
        "cation",
        "Polar solvent molecules drawn with their partially positive ends turned toward a "
        "cation",
        "Solvent molecules drawn in a regular repeating lattice",
        "A larger number of solute particles drawn in the same volume",
        "Solute particles drawn in a brighter colour than the solvent"],
      ans=0,
      why="EK 3.8.A.1 names drawings that show interactions among the components as one of "
          "its two means, and EK 3.1.A.3 says the orientation dependence of ion-dipole forces "
          "is understood by considering the sign of the partial charges and how they interact "
          "with an ion. A cation carries positive charge, so the solvent's partially negative "
          "end is the one drawn facing it. Changing how many particles are drawn communicates "
          "concentration instead, which is the framework's other means."),

 dict(q="Two drawings depict the same solute in the same solvent and the same volume, one "
        "dilute and one concentrated. How does the dilute drawing differ?",
      choices=[
        "It draws fewer solute particles for the same number of solvent particles",
        "It draws more solute particles for the same number of solvent particles",
        "It draws the solute particles closer together",
        "It draws no solvent particles at all",
        "It draws the solute particles in a regular repeating lattice"],
      ans=0,
      why="EK 3.8.A.1 has the drawing carry the relative concentrations of the components, "
          "and the dilute member of a pair is the one with less solute for the same amount of "
          "solvent. A regular lattice would be a representation of a crystalline solid rather "
          "than of a solution."),

 dict(q="Which pairing of a drawing's feature with what the framework says it communicates is "
        "correct?",
      choices=[
        "The relative numbers of particles drawn communicate concentration, and the "
        "arrangement of solvent around solute particles communicates interactions",
        "The relative numbers of particles drawn communicate interactions, and the "
        "arrangement of solvent around solute particles communicates concentration",
        "The relative numbers of particles drawn communicate concentration, and the "
        "arrangement of solvent around solute particles communicates nothing the framework "
        "names",
        "The arrangement of solvent around solute particles communicates interactions, and "
        "the relative numbers of particles drawn communicate the identity of the solute",
        "Neither feature communicates anything the framework names"],
      ans=0,
      why="EK 3.8.A.1 pairs illustration of the relative concentrations with how much of each "
          "component is present, and drawings that show interactions with how the components "
          "act on one another. Exchanging the two keeps every word of the sentence and makes "
          "it false, which is why the pairing is stated in full."),

 dict(q="Which statement puts together everything EK 3.8.A.1 asserts?",
      choices=[
        "Particulate representations communicate the structure and properties of solutions, "
        "by illustrating relative concentrations of the components and by showing "
        "interactions among them",
        "Particulate representations communicate only the identity of the solvent, and "
        "nothing about amounts or interactions",
        "Particulate representations communicate the measured molarity of a solution "
        "directly",
        "Particulate representations communicate the colligative properties of a solution",
        "Particulate representations communicate the percent by volume of each component"],
      ans=0,
      why="EK 3.8.A.1 has three parts and this option carries all three: what is "
          "communicated, and the two means by which it is communicated. The rejected options "
          "either drop the means or replace them with quantities the exclusion statements put "
          "outside the exam."),
]
