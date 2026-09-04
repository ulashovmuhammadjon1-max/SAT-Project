# AP CHEMISTRY 4.3 Representations of Reactions
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.3.A: represent a given chemical reaction or physical
# process with a consistent particulate model. Suggested skill 3.B, represent
# chemical substances or phenomena with appropriate diagrams or models.
#
# Essential knowledge relied on, in the framework's own words:
#   4.3.A.1  Balanced chemical equations in their various forms can be
#            translated into symbolic particulate representations.
#
# ONE ESSENTIAL KNOWLEDGE STATEMENT, AND IT IS A TRANSLATION CLAIM. The word
# doing the work in the learning objective is CONSISTENT: a particulate model
# is right when it agrees with the balanced equation it came from. What
# agreement means is fixed by EK 4.2.A.2 -- equal numbers of atoms of every
# element before and after, with mass and charge conserved -- and by EK 4.2.A.3,
# which supplies the "various forms" the framework says can all be translated.
# So every key here is either 4.3.A.1 itself or 4.3.A.1 applied through those
# two, and the module cites both when it does.
#
# THERE ARE NO PICTURES IN THIS BANK, AND THIS IS THE TOPIC MOST AT RISK FROM
# THAT. A particulate representation is normally drawn. Rather than write "the
# box shown above", every model in this module is given as a COUNT OF PARTICLES
# -- "4 H2 molecules and 2 O2 molecules" -- either in a table or in the stem,
# and the question is asked of those counts. Counts are what a drawn box
# conveys, and they are what the verifier can recompute, which a drawing is not.
#
# WHAT IS NOT HERE. Computing masses or moles from a balanced equation is 4.5's
# material, so no item here converts particles to grams. Classifying a reaction
# by type is 4.7 to 4.9. Writing the equation in the first place is 4.2, and
# this module hands the equation to the student in every item that needs one.
#
# NOTATION. Chemistry is not typeset. Formulas are plain text, the arrow is the
# word "gives", and ions are written Na+, Cl-, Ca2+ in the ordinary way.
TOPIC = ("4.3", "Representations of Reactions", 4)

_T_WATER = dict(
    headers=["Box", "Particles in the box"],
    rows=[["Before", "4 H2 molecules and 2 O2 molecules"],
          ["Proposal W", "4 H2O molecules"],
          ["Proposal X", "2 H2O molecules and 2 O2 molecules"],
          ["Proposal Y", "4 H2O molecules and 1 O2 molecule"],
          ["Proposal Z", "8 H2O molecules"]])

_T_AMMONIA = dict(
    headers=["Box", "Particles in the box"],
    rows=[["Before", "2 N2 molecules and 6 H2 molecules"],
          ["Proposal J", "4 NH3 molecules"],
          ["Proposal K", "2 NH3 molecules and 3 H2 molecules"],
          ["Proposal L", "6 NH3 molecules"],
          ["Proposal M", "2 NH3 molecules and 2 N2 molecules"]])

_T_FAULTY = dict(
    headers=["Box", "Particles in the box"],
    rows=[["Before", "3 CO molecules and 2 O2 molecules"],
          ["Proposal P", "3 CO2 molecules"],
          ["Proposal Q", "3 CO2 molecules and 1 O2 molecule"],
          ["Proposal R", "2 CO2 molecules and 1 O2 molecule"],
          ["Proposal S", "4 CO2 molecules"]])

_T_MIXTURE = dict(
    headers=["Box", "Particles in the box"],
    rows=[["Box 1", "6 CO molecules"],
          ["Box 2", "3 C2 molecules and 3 O2 molecules"],
          ["Box 3", "3 CO molecules and 3 CO2 molecules"]])

_T_DECOMP = dict(
    headers=["Box", "Particles in the box"],
    rows=[["Before", "4 CaCO3 formula units"],
          ["Proposal T", "4 CaO formula units and 4 CO2 molecules"],
          ["Proposal U", "4 CaO formula units and 2 CO2 molecules"],
          ["Proposal V", "2 CaO formula units and 4 CO2 molecules"],
          ["Proposal N", "4 CaO formula units and 4 CO molecules"]])

QUESTIONS = [

 dict(q="According to the framework, what can balanced chemical equations in "
        "their various forms be translated into?",
      choices=[
        "Symbolic particulate representations",
        "Measurements of the rate at which the reaction proceeds",
        "Predictions of the energy the reaction releases",
        "Tables of the solubility of each product",
        "Statements of the temperature at which the reaction occurs"],
      ans=0,
      why="EK 4.3.A.1, verbatim in substance: balanced chemical equations in "
          "their various forms can be translated into symbolic particulate "
          "representations. Rates belong to unit 5 and energy to unit 6."),

 dict(q="Which equation forms does that translation apply to?",
      choices=[
        "The balanced molecular, complete ionic and net ionic forms alike",
        "The balanced molecular form only",
        "The net ionic form only",
        "Only forms in which every substance is a solid",
        "Only forms whose coefficients are all equal to one"],
      ans=0,
      why="EK 4.3.A.1 says balanced chemical equations IN THEIR VARIOUS FORMS, "
          "and EK 4.2.A.3 names those forms as the balanced molecular, the "
          "complete ionic and the net ionic equation."),

 dict(q="What must a particulate model of a chemical change preserve if it is "
        "to be consistent with the balanced equation it came from?",
      choices=[
        "The number of atoms of each element, before and after",
        "The number of molecules, before and after",
        "The number of different substances, before and after",
        "The volume occupied by the particles, before and after",
        "The number of particles that are drawn as pairs"],
      ans=0,
      why="EK 4.3.A.1 makes the model a translation of the balanced equation, "
          "and EK 4.2.A.2 requires any representation of a chemical change to "
          "contain equal numbers of atoms of every element before and after. "
          "Molecule counts are free to change."),

 dict(q="A box of particles reacts according to 2 H2 + O2 gives 2 H2O. The "
        "table gives the particles in the box before the reaction and four "
        "proposals for the box afterwards. Which proposal is consistent?",
      table=_T_WATER,
      choices=[
        "Proposal W",
        "Proposal X",
        "Proposal Y",
        "Proposal Z",
        "None of the four proposals"],
      ans=0,
      why="EK 4.3.A.1 requires the particulate model to translate the balanced "
          "equation, and EK 4.2.A.2 requires the same number of atoms of each "
          "element afterwards. Counting the hydrogen and oxygen atoms in each "
          "proposal against the starting box is what settles it."),

 dict(q="A box holds 3 N2 molecules and 9 H2 molecules, and all of them react "
        "according to N2 + 3 H2 gives 2 NH3. What does the box hold afterwards?",
      choices=[
        "6 NH3 molecules",
        "3 NH3 molecules",
        "9 NH3 molecules",
        "12 NH3 molecules",
        "2 NH3 molecules and 1 N2 molecule"],
      ans=0,
      why="EK 4.3.A.1 translates the balanced equation into particles: each "
          "nitrogen molecule with three hydrogen molecules gives two ammonia "
          "molecules, so three sets give six. EK 4.2.A.2's atom counts agree, "
          "with six nitrogen and eighteen hydrogen atoms on each side."),

 dict(q="In a particulate model of oxygen gas at room temperature, how should "
        "each particle be drawn?",
      choices=[
        "As two oxygen atoms joined to one another",
        "As a single unattached oxygen atom",
        "As three oxygen atoms joined in a ring",
        "As one oxygen atom joined to one nitrogen atom",
        "As a cluster of many oxygen atoms packed together"],
      ans=0,
      why="EK 4.3.A.1 makes the particulate model a translation of the "
          "equation, and an equation writes the substance as O2, so each "
          "particle carries two oxygen atoms. Drawing separate atoms would "
          "represent a different substance."),

 dict(q="The table gives a starting box and four proposals for the box after "
        "the reaction N2 + 3 H2 gives 2 NH3 has consumed everything present. "
        "Which proposal is consistent with the equation?",
      table=_T_AMMONIA,
      choices=[
        "Proposal J",
        "Proposal K",
        "Proposal L",
        "Proposal M",
        "Every proposal is consistent"],
      ans=0,
      why="EK 4.3.A.1 requires the model to translate the balanced equation and "
          "EK 4.2.A.2 requires equal numbers of atoms of every element, so the "
          "nitrogen and hydrogen atoms in each proposal must match those in the "
          "starting box."),

 dict(q="Carbon monoxide burns according to 2 CO + O2 gives 2 CO2. Which box of "
        "reactant particles contains the two reactants in exactly the ratio the "
        "equation requires, with nothing left over?",
      choices=[
        "4 CO molecules and 2 O2 molecules",
        "4 CO molecules and 4 O2 molecules",
        "2 CO molecules and 2 O2 molecules",
        "3 CO molecules and 2 O2 molecules",
        "4 CO molecules and 1 O2 molecule"],
      ans=0,
      why="EK 4.3.A.1 translates the coefficients into particle counts: two "
          "carbon monoxide molecules for each oxygen molecule. Only a box in "
          "that two to one ratio consumes both reactants completely."),

 dict(q="The complete ionic equation for a precipitation is translated into a "
        "particulate model of the solution before reaction. How should the "
        "dissolved compounds be drawn?",
      choices=[
        "As separate positive and negative ions dispersed among the solvent "
        "particles",
        "As neutral formula units in which the ions remain joined",
        "As atoms of each element with no charge marked on any of them",
        "As one large particle containing every dissolved substance",
        "As the solid precipitate that will eventually form"],
      ans=0,
      why="EK 4.3.A.1 allows the equation in its various forms to be translated "
          "into a particulate representation, and EK 4.2.A.3's complete ionic "
          "form writes each dissolved substance as separate ions, so the picture "
          "that translates it shows them separated."),

 dict(q="A net ionic equation is translated into a particulate model. Which "
        "particles should appear in it?",
      choices=[
        "Only the ions that combine and the product they form",
        "Every ion present in the solution, whether it reacts or not",
        "Only the neutral compounds that were dissolved at the start",
        "Only the solvent particles",
        "The ions that do not react, and nothing else"],
      ans=0,
      why="EK 4.3.A.1 permits the translation of any of the forms, and EK "
          "4.2.A.3's net ionic form omits the species that stand unaltered on "
          "both sides, so the model translating it carries only what changes."),

 dict(q="A particulate model represents liquid water becoming water vapor. What "
        "must be true of the particles in the two boxes?",
      choices=[
        "The same water molecules appear in both, farther apart in the vapor",
        "The molecules in the vapor contain fewer atoms than those in the liquid",
        "The molecules in the liquid have separated into hydrogen and oxygen "
        "atoms",
        "There are twice as many molecules in the vapor as in the liquid",
        "The molecules in the vapor carry a positive charge"],
      ans=0,
      why="EK 4.3.A.1 and the learning objective extend the consistent "
          "particulate model to a physical process, and EK 4.1.A.1 makes a "
          "phase change one in which properties change but composition does "
          "not, so the same molecules must appear in both boxes."),

 dict(q="Solid sodium chloride dissolving in water is represented at the "
        "particulate level. Which model is consistent with the equation NaCl(s) "
        "gives Na+(aq) + Cl-(aq)?",
      choices=[
        "Equal numbers of separate Na+ and Cl- particles surrounded by water "
        "molecules",
        "Joined NaCl units drifting among the water molecules",
        "Twice as many Na+ particles as Cl- particles",
        "Separate Na and Cl atoms with no charges marked",
        "Na+ particles only, with the chlorine having left as a gas"],
      ans=0,
      why="EK 4.3.A.1 translates the equation into particles, and EK 4.2.A.2 "
          "requires charge as well as atoms to be conserved: one ion of each "
          "kind per formula unit gives a total charge of zero, matching the "
          "neutral solid."),

 dict(q="The table gives a starting box and four proposals for the box after "
        "the reaction 2 CO + O2 gives 2 CO2 has occurred. Which proposal "
        "conserves the atoms of every element?",
      table=_T_FAULTY,
      choices=[
        "Proposal Q",
        "Proposal P",
        "Proposal R",
        "Proposal S",
        "None of the four proposals"],
      ans=0,
      why="EK 4.2.A.2 requires equal numbers of atoms of every element before "
          "and after, which EK 4.3.A.1 carries into the particulate model. "
          "Counting carbon and oxygen atoms in each proposal against the "
          "starting box identifies the one that conserves them."),

 dict(q="A box is drawn holding 5 CH4 molecules. How many atoms of hydrogen "
        "does the box contain?",
      choices=["20", "5", "10", "16", "25"],
      ans=0,
      why="EK 4.3.A.1 makes the particulate model a translation of the formulas "
          "in the equation, and a formula's subscript is a count of atoms in "
          "one particle: four hydrogens in each of five molecules."),

 dict(q="A student's particulate model shows more atoms of one element after "
        "the reaction than before it. What is wrong with the model?",
      choices=[
        "It represents atoms as having been created, which no representation of "
        "a chemical change may do",
        "It uses too few colors to distinguish the elements",
        "It shows the reaction going in the wrong direction",
        "It fails only because the particles are drawn too close together",
        "Nothing is wrong, provided the extra atoms are drawn smaller"],
      ans=0,
      why="EK 4.2.A.2 requires any representation of a chemical change to "
          "contain equal numbers of atoms of every element before and after, "
          "and EK 4.3.A.1 makes the particulate model such a representation."),

 dict(q="What fixes the RATIO of particles a consistent particulate model shows "
        "reacting?",
      choices=[
        "The coefficients written in front of the formulas in the balanced "
        "equation",
        "The subscripts written inside the formulas",
        "The physical states written after the formulas",
        "The order in which the substances are written",
        "The total number of particles the student chooses to draw"],
      ans=0,
      why="EK 4.3.A.1 makes the model a translation of the balanced equation, "
          "in which the coefficients state how many particles of each substance "
          "take part; the subscripts instead state how atoms are grouped within "
          "one particle."),

 dict(q="What fixes how the atoms are grouped WITHIN each particle drawn?",
      choices=[
        "The subscripts written inside each formula",
        "The coefficients written in front of each formula",
        "The number of particles the student decides to draw",
        "Whether the substance is a reactant or a product",
        "The charge written after the formula"],
      ans=0,
      why="EK 4.3.A.1's translation runs from the equation to the picture, and a "
          "subscript states how many atoms of an element are joined in one "
          "particle, which is why altering one would represent a different "
          "substance under EK 4.1.A.1."),

 dict(q="Methane burns according to CH4 + 2 O2 gives CO2 + 2 H2O. A box holds 3 "
        "CH4 molecules and 6 O2 molecules and everything reacts. What does the "
        "box hold afterwards?",
      choices=[
        "3 CO2 molecules and 6 H2O molecules",
        "3 CO2 molecules and 3 H2O molecules",
        "1 CO2 molecule and 2 H2O molecules",
        "6 CO2 molecules and 3 H2O molecules",
        "3 CO2 molecules and 6 H2O molecules and 1 O2 molecule"],
      ans=0,
      why="EK 4.3.A.1 translates the coefficients into particle counts, so three "
          "sets of the equation give three carbon dioxide and six water "
          "molecules, and EK 4.2.A.2's atom counts agree at three carbon, "
          "twelve hydrogen and twelve oxygen atoms."),

 dict(q="A box holds 6 H2 molecules and 2 O2 molecules, which react by 2 H2 + O2 "
        "gives 2 H2O until one reactant is used up. What does the box hold "
        "afterwards?",
      choices=[
        "4 H2O molecules and 2 H2 molecules",
        "4 H2O molecules only",
        "6 H2O molecules only",
        "6 H2O molecules and 2 O2 molecules",
        "4 H2O molecules and 1 O2 molecule"],
      ans=0,
      why="EK 4.3.A.1 translates the coefficients into particles: two oxygen "
          "molecules can consume only four hydrogen molecules, leaving two "
          "undrawn from the six. EK 4.2.A.2's counts agree, with twelve "
          "hydrogen and four oxygen atoms in each box."),

 dict(q="The table gives three boxes of particles. Which box represents a "
        "mixture of two different compounds?",
      table=_T_MIXTURE,
      choices=[
        "Box 3",
        "Box 1",
        "Box 2",
        "All three boxes",
        "None of the three boxes"],
      ans=0,
      why="EK 4.3.A.1 makes a particulate model a symbolic representation of "
          "what substances are present, and a compound is a particle containing "
          "atoms of more than one element. The box with two kinds of such "
          "particle is the mixture of compounds."),

 dict(q="A particulate model of an aqueous solution shows 3 Ca2+ particles. How "
        "many Cl- particles must it show if the dissolved compound is CaCl2 and "
        "nothing else is present?",
      choices=["6", "3", "2", "9", "1"],
      ans=0,
      why="EK 4.3.A.1 translates the formula into the picture, and EK 4.2.A.2 "
          "requires charge to be conserved: two chloride ions of minus one for "
          "each calcium ion of plus two bring the total charge to zero."),

 dict(q="Calcium carbonate decomposes according to CaCO3 gives CaO + CO2. The "
        "table gives a starting box and four proposals for the box afterwards. "
        "Which proposal is consistent with the equation?",
      table=_T_DECOMP,
      choices=[
        "Proposal T",
        "Proposal U",
        "Proposal V",
        "Proposal N",
        "None of the four proposals"],
      ans=0,
      why="EK 4.3.A.1 requires the model to translate the equation and EK "
          "4.2.A.2 requires equal numbers of atoms of every element, so calcium, "
          "carbon and oxygen must each be counted in the proposals against the "
          "starting box."),

 dict(q="A student draws one H2 molecule and one O2 molecule reacting to give "
        "one H2O molecule. Why is the drawing unacceptable?",
      choices=[
        "An oxygen atom would have to disappear, and a representation of a "
        "chemical change may not lose atoms",
        "Water cannot be represented at the particulate level",
        "Hydrogen must always be drawn as separate atoms",
        "The drawing shows too few particles to represent any reaction",
        "Nothing is unacceptable about it"],
      ans=0,
      why="EK 4.2.A.2 requires equal numbers of atoms of every element before "
          "and after, and EK 4.3.A.1 makes the drawing a representation subject "
          "to that: two oxygen atoms go in and only one comes out."),

 dict(q="Magnesium burns according to 2 Mg + O2 gives 2 MgO. If a box holds 8 Mg "
        "atoms and enough oxygen, how many MgO formula units should the box hold "
        "afterwards?",
      choices=["8", "4", "16", "2", "6"],
      ans=0,
      why="EK 4.3.A.1 translates the coefficients into particle counts, and the "
          "equation pairs each magnesium atom with one formula unit of the "
          "oxide, so the magnesium count carries straight across."),

 dict(q="Which statement about the number of PARTICLES in a consistent "
        "particulate model is correct?",
      choices=[
        "It may differ before and after, even though the number of atoms of each "
        "element may not",
        "It must be the same before and after, like the number of atoms",
        "It must always increase as the reaction proceeds",
        "It must always decrease as the reaction proceeds",
        "It has no relationship to the balanced equation at all"],
      ans=0,
      why="EK 4.2.A.2 imposes equal numbers of ATOMS of every element, not equal "
          "numbers of particles, and EK 4.3.A.1 carries exactly that requirement "
          "into the model; three molecules becoming two is an ordinary result."),

 dict(q="Two students translate the same balanced equation into particulate "
        "models, one drawing twice as many particles as the other. Can both "
        "models be consistent with the equation?",
      choices=[
        "Yes, because what the equation fixes is the ratio of the particles "
        "rather than how many are drawn",
        "No, because only the smallest whole-number set of particles may be "
        "drawn",
        "No, because doubling the particles would double the atoms and break "
        "conservation",
        "Yes, but only if the second student also doubles the number of atoms "
        "in each particle",
        "It cannot be decided without knowing the temperature"],
      ans=0,
      why="EK 4.3.A.1 makes the model a translation of the equation, whose "
          "coefficients state proportions, and EK 4.2.A.2's conservation is "
          "satisfied in each box separately, so any set in the right ratio "
          "translates the same equation."),

 dict(q="Zinc displaces copper according to Zn(s) + Cu2+(aq) gives Zn2+(aq) + "
        "Cu(s). What must a consistent particulate model show about charge?",
      choices=[
        "The same total charge in the box before and after the change",
        "A total charge of zero in the box before the change",
        "A larger total charge afterwards, since a metal has dissolved",
        "No charges at all, since metals are neutral",
        "A total charge that doubles as the reaction proceeds"],
      ans=0,
      why="EK 4.2.A.2 states that equations demonstrate that mass and charge are "
          "conserved, and EK 4.3.A.1 makes the particulate model a translation "
          "of the equation, so the plus two carried by the copper ion is carried "
          "by the zinc ion afterwards."),

 dict(q="Which of the following does a particulate model of a chemical change "
        "NOT have to preserve?",
      choices=[
        "The number of separate particles drawn",
        "The number of atoms of each element",
        "The total charge in the box",
        "The identity of the elements present",
        "The grouping of atoms required by each formula"],
      ans=0,
      why="EK 4.2.A.2 requires equal numbers of atoms of every element and the "
          "conservation of mass and charge, and EK 4.3.A.1 carries those into "
          "the model, but nothing there constrains how many separate particles "
          "the box holds."),

 dict(q="A particulate model of the reaction Ag+(aq) + Cl-(aq) gives AgCl(s) is "
        "drawn with 5 Ag+ particles and 5 Cl- particles at the start. How many "
        "AgCl formula units should the solid contain when the reaction is "
        "complete?",
      choices=["5", "10", "1", "25", "2"],
      ans=0,
      why="EK 4.3.A.1 translates the net ionic equation into particles at a one "
          "to one ratio, and EK 4.2.A.2's conservation of atoms fixes the count: "
          "each pair of ions supplies exactly one formula unit."),

 dict(q="Why does the learning objective ask specifically for a CONSISTENT "
        "particulate model?",
      choices=[
        "Because a picture that contradicts the balanced equation misrepresents "
        "what the reaction does to the atoms",
        "Because two students should always draw the identical picture",
        "Because a model must be drawn to scale to be acceptable",
        "Because the picture is the only acceptable way to represent a reaction",
        "Because consistency means using the same colors as the textbook"],
      ans=0,
      why="EK 4.3.A.1 makes the model a TRANSLATION of the balanced equation, "
          "so its content is whatever the equation asserts; EK 4.2.A.2 fixes "
          "what must survive that translation, namely the atoms of every element "
          "and the total charge."),
]
