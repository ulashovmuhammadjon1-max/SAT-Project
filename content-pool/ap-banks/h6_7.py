# AP CHEMISTRY 6.7 Bond Enthalpies
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.7.A: calculate the enthalpy change of a reaction based on the
# average bond energies of bonds broken and formed in the reaction. Suggested skill 5.F,
# calculate, estimate, or predict an unknown quantity from known quantities by selecting
# and following a logical computational pathway and attending to precision.
#
# Essential knowledge relied on, in the framework's own words:
#   6.7.A.1  During a chemical reaction, bonds are broken and/or formed, and these events
#            change the potential energy of the system.
#   6.7.A.2  The average energy required to break all of the bonds in the reactant
#            molecules can be estimated by adding up the average bond energies of all the
#            bonds in the reactant molecules. Likewise, the average energy released in
#            forming the bonds in the product molecules can be estimated. If the energy
#            released is greater than the energy required, the reaction is exothermic. If
#            the energy required is greater than the energy released, the reaction is
#            endothermic.
#
# WHY EVERY BOND ENERGY IS TABULATED AND NONE IS ASSUMED. The framework gives no numbers,
# so a question that expected a student to know that an O-H bond is worth 463 kJ/mol would
# be testing recall the CED never asks for. Every value used below is in the table on the
# question, and verify_h6_7.py reads the values it recomputes with FROM THAT TABLE, not
# from a constant of its own -- so an edited table and a stale check cannot disagree
# silently.
#
# THE SUBTRACTION RUNS ONE WAY AND ONE WAY ONLY: energy required to break the reactant
# bonds MINUS energy released forming the product bonds. Bond energies are positive
# quantities, breaking costs and forming refunds, and it is the order of that subtraction
# -- not a stored sign -- that makes an exothermic reaction come out negative. Reversing it
# gives the same magnitude with the wrong sign, which is the single most likely defect in
# this topic, so every keyed choice states the direction as well as the number and every
# distractor list contains the reversed value.
#
# THE BOND COUNTS ARE NOT ASSERTED, THEY ARE DERIVED. Each reaction is written out in the
# stem, and verify_h6_7.py works out which bonds break and which form from the equation
# plus a table of the bonds in each species -- then checks that table against the molecular
# formulas it parses from the same equation, since each of these molecules is acyclic and
# so must carry one fewer bond than it has atoms. Every equation is atom- and
# charge-balanced by h_equation.py as well.
#
# THE FRAMEWORK SAYS "ESTIMATED" AND "AVERAGE" TWICE EACH, and item 9 and item 27 are there
# because that hedge is content. A bond energy tabulated for a bond type is an average over
# the molecules it occurs in, so the enthalpy change it yields is an estimate rather than a
# measurement, and no key here claims otherwise.
#
# SCOPE. 6.8 owns the standard enthalpies of formation and 6.9 owns Hess's law, so no item
# here reaches an enthalpy change by either route. 6.6 owns the sign convention itself and
# the molar enthalpy of reaction; this module uses that convention but does not re-teach
# it, and no item here multiplies an amount in moles by a molar enthalpy.
#
# NOTATION. export_units.py does not typeset Chemistry. Equations are plain text with the
# word "gives" for the arrow, as h5_7.py and h5_11.py write them; bonds are written H-H,
# O=O and, where a glyph would be needed, in words as "N-N triple bond".
TOPIC = ("6.7", "Bond Enthalpies", 6)

_T_BOND = dict(
    headers=["Bond", "Average bond energy (kJ/mol)"],
    rows=[["H-H", "436"],
          ["Cl-Cl", "243"],
          ["H-Cl", "431"],
          ["O=O", "498"],
          ["O-H", "463"],
          ["C-H", "413"],
          ["C=O", "799"],
          ["N-N triple bond", "946"],
          ["N-H", "391"]])

QUESTIONS = [

 dict(q="What does the framework say the breaking and forming of bonds during a chemical "
        "reaction does?",
      choices=[
        "It changes the potential energy of the system",
        "It changes the number of atoms in the system",
        "It changes the mass of the system",
        "It changes the temperature without changing any energy",
        "It leaves the energy of the system unchanged"],
      ans=0,
      why="EK 6.7.A.1 states that during a chemical reaction bonds are broken and/or "
          "formed, and these events change the potential energy of the system."),

 dict(q="How does the framework say the energy required to break all the bonds in the "
        "reactant molecules can be estimated?",
      choices=[
        "By adding up the average bond energies of all the bonds in the reactant molecules",
        "By adding up the average bond energies of all the bonds in the product molecules",
        "By subtracting the reactant bond energies from the product bond energies",
        "By multiplying the average bond energies of the reactant bonds together",
        "By taking the largest average bond energy among the reactant bonds"],
      ans=0,
      why="EK 6.7.A.2 opens by stating that the average energy required to break all of the "
          "bonds in the reactant molecules can be estimated by adding up the average bond "
          "energies of all the bonds in the reactant molecules."),

 dict(q="What does the framework say the same kind of sum over the product molecules "
        "estimates?",
      choices=[
        "The average energy released in forming the bonds in the product molecules",
        "The average energy required to break the bonds in the product molecules",
        "The temperature the products will reach",
        "The number of bonds the products contain",
        "The enthalpy change of the reaction on its own"],
      ans=0,
      why="EK 6.7.A.2 states that likewise the average energy released in forming the bonds "
          "in the product molecules can be estimated, so the product sum is a release where "
          "the reactant sum is a requirement."),

 dict(q="According to the framework, what is true of a reaction in which the energy "
        "released is greater than the energy required?",
      choices=[
        "It is exothermic",
        "It is endothermic",
        "It transfers no energy at all",
        "It cannot occur",
        "Its direction depends on whether a gas is produced"],
      ans=0,
      why="EK 6.7.A.2 states that if the energy released is greater than the energy "
          "required, the reaction is exothermic."),

 dict(q="According to the framework, what is true of a reaction in which the energy "
        "required is greater than the energy released?",
      choices=[
        "It is endothermic",
        "It is exothermic",
        "It transfers no energy at all",
        "It cannot occur",
        "Its direction depends on whether the products are solids"],
      ans=0,
      why="EK 6.7.A.2 states that if the energy required is greater than the energy "
          "released, the reaction is endothermic, which is the mirror of the exothermic "
          "case in the same statement."),

 dict(q="How is the enthalpy change of a reaction found from average bond energies?",
      choices=[
        "The energy required to break the reactant bonds minus the energy released forming "
        "the product bonds",
        "The energy released forming the product bonds minus the energy required to break "
        "the reactant bonds",
        "The energy required to break the reactant bonds plus the energy released forming "
        "the product bonds",
        "The largest reactant bond energy minus the largest product bond energy",
        "The average of the reactant and product bond energy totals"],
      ans=0,
      why="Learning objective 6.7.A asks for the enthalpy change based on the bonds broken "
          "and formed, and EK 6.7.A.2 makes the reaction exothermic when the release "
          "exceeds the requirement, which is what this subtraction reports as a negative "
          "value."),

 dict(q="Does breaking a chemical bond require energy or release it?",
      choices=[
        "It requires energy",
        "It releases energy",
        "It neither requires nor releases energy",
        "Energy is needed only when the bond is a double bond",
        "Energy is given out only when the bond is in a reactant"],
      ans=0,
      why="EK 6.7.A.2 speaks throughout of the energy REQUIRED to break all of the bonds in "
          "the reactant molecules, which is why the reactant sum enters the calculation as "
          "a cost."),

 dict(q="Does forming a chemical bond require energy or release it?",
      choices=[
        "It releases energy",
        "It requires energy",
        "It neither requires nor releases energy",
        "Energy is given out only when the product is a gas",
        "Energy is needed only when the bond is a single bond"],
      ans=0,
      why="EK 6.7.A.2 speaks of the energy RELEASED in forming the bonds in the product "
          "molecules, which is why the product sum enters the calculation as a refund."),

 dict(q="Why does the framework describe an enthalpy change found this way as an estimate?",
      choices=[
        "Because the bond energies used are averages over the molecules a bond occurs in",
        "Because the number of bonds broken can only be guessed",
        "Because the reaction may not go to completion",
        "Because the temperature of the surroundings is not known",
        "Because energy is not conserved in a chemical reaction"],
      ans=0,
      why="EK 6.7.A.2 twice says a sum can be ESTIMATED and twice calls the values AVERAGE "
          "bond energies, so a value tabulated for a bond type stands for many molecules "
          "rather than for the one in hand."),

 dict(q="Which of the tabulated bonds is the strongest?",
      table=_T_BOND,
      choices=[
        "N-N triple bond",
        "C=O",
        "O=O",
        "O-H",
        "H-H"],
      ans=0,
      why="EK 6.7.A.2 makes the average bond energy the energy required to break the bond, "
          "so the largest tabulated value marks the bond that takes the most energy to "
          "break."),

 dict(q="Which of the tabulated bonds is the weakest?",
      table=_T_BOND,
      choices=[
        "Cl-Cl",
        "N-H",
        "C-H",
        "H-Cl",
        "H-H"],
      ans=0,
      why="EK 6.7.A.2 makes the average bond energy the energy required to break the bond, "
          "so the smallest tabulated value marks the bond that takes the least energy to "
          "break."),

 dict(q="Consider the reaction H2 + Cl2 gives 2 HCl . Using the tabulated values, how much "
        "energy is required to break all the bonds in the reactant molecules?",
      table=_T_BOND,
      choices=[
        "679 kJ/mol",
        "862 kJ/mol",
        "1541 kJ/mol",
        "436 kJ/mol",
        "183 kJ/mol"],
      ans=0,
      why="EK 6.7.A.2 estimates the energy required by adding up the average bond energies "
          "of all the bonds in the reactant molecules, which here are one bond in each of "
          "the two diatomic reactants."),

 dict(q="For the reaction H2 + Cl2 gives 2 HCl , how much energy is released in forming "
        "the bonds in the product molecules, using the tabulated values?",
      table=_T_BOND,
      choices=[
        "862 kJ/mol",
        "679 kJ/mol",
        "431 kJ/mol",
        "1541 kJ/mol",
        "183 kJ/mol"],
      ans=0,
      why="EK 6.7.A.2 estimates the energy released by adding up the average bond energies "
          "of all the bonds in the product molecules, and two molecules of the product each "
          "carry one such bond."),

 dict(q="What is the enthalpy change of the reaction H2 + Cl2 gives 2 HCl , estimated from "
        "the tabulated bond energies?",
      table=_T_BOND,
      choices=[
        "-183 kJ/mol, so the reaction is exothermic",
        "+183 kJ/mol, so the reaction is endothermic",
        "-1541 kJ/mol, so the reaction is exothermic",
        "+1541 kJ/mol, so the reaction is endothermic",
        "-679 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="Learning objective 6.7.A subtracts the energy released forming the product bonds "
          "from the energy required to break the reactant bonds, and EK 6.7.A.2 makes the "
          "reaction exothermic because the release is the greater of the two."),

 dict(q="What is the enthalpy change of the reaction N2 + 3 H2 gives 2 NH3 , estimated "
        "from the tabulated bond energies?",
      table=_T_BOND,
      choices=[
        "-92 kJ/mol, so the reaction is exothermic",
        "+92 kJ/mol, so the reaction is endothermic",
        "-4600 kJ/mol, so the reaction is exothermic",
        "-2254 kJ/mol, so the reaction is exothermic",
        "-1400 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.7.A.2 adds the average bond energies of the bonds in the reactants and "
          "separately those in the products, and learning objective 6.7.A subtracts the "
          "second total from the first; the release is the larger, so the reaction is "
          "exothermic."),

 dict(q="What is the enthalpy change of the reaction 2 H2 + O2 gives 2 H2O , estimated "
        "from the tabulated bond energies?",
      table=_T_BOND,
      choices=[
        "-482 kJ/mol, so the reaction is exothermic",
        "+482 kJ/mol, so the reaction is endothermic",
        "-3222 kJ/mol, so the reaction is exothermic",
        "-1370 kJ/mol, so the reaction is exothermic",
        "-934 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.7.A.2 sums the average bond energies on each side and learning objective "
          "6.7.A subtracts the product total from the reactant total; four bonds are formed "
          "against three broken, and the release is the larger."),

 dict(q="What is the enthalpy change of the reaction 2 HCl gives H2 + Cl2 , estimated from "
        "the tabulated bond energies?",
      table=_T_BOND,
      choices=[
        "+183 kJ/mol, so the reaction is endothermic",
        "-183 kJ/mol, so the reaction is exothermic",
        "+1541 kJ/mol, so the reaction is endothermic",
        "+862 kJ/mol, so the reaction is endothermic",
        "+679 kJ/mol, so the reaction is endothermic"],
      ans=0,
      why="EK 6.7.A.2 makes the reaction endothermic when the energy required exceeds the "
          "energy released, which is the case here because the bonds broken are the "
          "stronger set; the subtraction therefore comes out positive."),

 dict(q="What is the enthalpy change of the reaction CH4 + 2 O2 gives CO2 + 2 H2O , "
        "estimated from the tabulated bond energies?",
      table=_T_BOND,
      choices=[
        "-802 kJ/mol, so the reaction is exothermic",
        "+802 kJ/mol, so the reaction is endothermic",
        "-6098 kJ/mol, so the reaction is exothermic",
        "-2648 kJ/mol, so the reaction is exothermic",
        "-1798 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.7.A.2 adds the average bond energies of every bond broken and every bond "
          "formed, and learning objective 6.7.A subtracts the second total from the first; "
          "the release is the larger, so the value is negative."),

 dict(q="How many bonds of the kind found in water are formed when 2 H2O molecules are "
        "produced?",
      table=_T_BOND,
      choices=[
        "Four",
        "Two",
        "Six",
        "One",
        "Eight"],
      ans=0,
      why="EK 6.7.A.2 requires ALL of the bonds in the product molecules to be counted, and "
          "each molecule of water carries two of them, so twice the number of molecules is "
          "the number of bonds formed."),

 dict(q="In the reaction N2 + 3 H2 gives 2 NH3 , which contributes more to the total energy "
        "required to break the reactant bonds?",
      table=_T_BOND,
      choices=[
        "The three hydrogen to hydrogen bonds together",
        "The single nitrogen to nitrogen triple bond",
        "The two contribute equally",
        "Neither, since breaking bonds requires no energy",
        "It cannot be decided without the enthalpy change of the reaction"],
      ans=0,
      why="EK 6.7.A.2 adds up the average bond energies of ALL the bonds in the reactant "
          "molecules, so three of the weaker bonds can outweigh one of the stronger, which "
          "the tabulated values decide."),

 dict(q="A student estimates an enthalpy change by adding the reactant bond energy total "
        "to the product bond energy total. What is wrong?",
      choices=[
        "The product total must be subtracted from the reactant total, not added to it",
        "The reactant total must be subtracted from the product total, not added to it",
        "The two totals must be multiplied rather than added",
        "The two totals must be averaged rather than added",
        "Nothing, since both sets of bonds require energy"],
      ans=0,
      why="Learning objective 6.7.A asks for the enthalpy change from the bonds broken AND "
          "formed, and EK 6.7.A.2 makes one a requirement and the other a release, so the "
          "two enter with opposite effect and their sum has no meaning."),

 dict(q="A student subtracts the product bond energy total from the reactant bond energy "
        "total and obtains a negative number. What does that mean?",
      choices=[
        "The reaction is exothermic, since more energy was released than required",
        "The reaction is endothermic, since more energy was released than required",
        "The reaction is exothermic, since more energy was required than released",
        "The student has made an arithmetic error, since the result cannot be negative",
        "Nothing, since the sign of the result carries no information"],
      ans=0,
      why="EK 6.7.A.2 states that if the energy released is greater than the energy "
          "required the reaction is exothermic, and that is exactly the case in which the "
          "requirement minus the release comes out below zero."),

 dict(q="A student subtracts the reactant bond energy total from the product bond energy "
        "total instead. What is the effect on the answer?",
      choices=[
        "The magnitude is right and the sign is reversed",
        "The magnitude is right and the sign is right",
        "The magnitude is doubled and the sign is right",
        "The magnitude is halved and the sign is reversed",
        "The result is unrelated to the enthalpy change"],
      ans=0,
      why="Learning objective 6.7.A takes the requirement minus the release, so exchanging "
          "the two terms negates the difference and leaves its size untouched, which under "
          "EK 6.7.A.2 reports the opposite direction."),

 dict(q="Why does the framework treat the breaking of bonds as a cost in this calculation?",
      choices=[
        "Because energy must be supplied to break the bonds in the reactant molecules",
        "Because the reactant molecules give up energy as their bonds break",
        "Because breaking bonds lowers the potential energy of the system",
        "Because the reactant bonds are always the weaker set",
        "Because breaking bonds changes the number of atoms present"],
      ans=0,
      why="EK 6.7.A.2 calls the reactant sum the average energy REQUIRED to break all of "
          "the bonds in the reactant molecules, so it is energy that has to be put in "
          "before anything is given back."),

 dict(q="One reaction has a reactant bond energy total of 2000 kJ/mol and a product total "
        "of 2400 kJ/mol. A second has a reactant total of 2400 kJ/mol and a product total "
        "of 2000 kJ/mol. Which is exothermic?",
      choices=[
        "The first, because the energy released exceeds the energy required",
        "The second, because the energy released exceeds the energy required",
        "The first, because the energy required exceeds the energy released",
        "Both, because every reaction releases energy overall",
        "Neither, because the two totals are the same numbers in each case"],
      ans=0,
      why="EK 6.7.A.2 states that if the energy released is greater than the energy "
          "required the reaction is exothermic, and the release is the product total while "
          "the requirement is the reactant total."),

 dict(q="A reaction is found to break exactly the same set of bonds as it forms. What "
        "enthalpy change does the bond energy estimate give?",
      choices=[
        "About zero, since the energy required and the energy released are the same",
        "A large negative value, since forming bonds always wins",
        "A large positive value, since breaking bonds always wins",
        "It cannot be estimated at all in this case",
        "Exactly the sum of all the bond energies involved"],
      ans=0,
      why="Learning objective 6.7.A subtracts the release from the requirement, so identical "
          "sets of bonds give identical totals and a difference of zero, which under EK "
          "6.7.A.2 is neither of the two named cases."),

 dict(q="What exactly does the framework call an average in this calculation, and what "
        "follows from it?",
      choices=[
        "The bond energies themselves are averages, so the enthalpy change obtained is an "
        "estimate",
        "The enthalpy change is an average, so the bond energies obtained are estimates",
        "The number of bonds is an average, so the totals are estimates",
        "The temperature is an average, so the bond energies are estimates",
        "Nothing in the calculation is an average, and the result is exact"],
      ans=0,
      why="EK 6.7.A.2 calls the tabulated quantities AVERAGE bond energies and says each "
          "total can be ESTIMATED from them, so the imprecision enters with the values and "
          "is carried through to the answer."),

 dict(q="Does the framework require that a chemical reaction both break bonds and form "
        "them?",
      choices=[
        "No; it says bonds are broken and/or formed",
        "Yes; every reaction must do both in equal numbers",
        "Yes; a reaction that only breaks bonds is impossible",
        "No; it says bonds are only ever broken",
        "No; it says bonds are only ever formed"],
      ans=0,
      why="EK 6.7.A.1 states that during a chemical reaction bonds are broken and/or "
          "formed, so the framework's own wording allows either or both rather than "
          "requiring the pair."),

 dict(q="A reaction breaks bonds totalling 1500 kJ/mol and forms bonds totalling 1750 "
        "kJ/mol. What is its estimated enthalpy change?",
      choices=[
        "-250 kJ/mol, so the reaction is exothermic",
        "+250 kJ/mol, so the reaction is endothermic",
        "-3250 kJ/mol, so the reaction is exothermic",
        "-1500 kJ/mol, so the reaction is exothermic",
        "-1750 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="Learning objective 6.7.A subtracts the energy released forming the product bonds "
          "from the energy required to break the reactant bonds, and EK 6.7.A.2 makes the "
          "reaction exothermic because the release is the larger."),

 dict(q="State the framework's rule for deciding from bond energies alone whether a "
        "reaction is exothermic.",
      choices=[
        "The reaction is exothermic when the energy released forming the product bonds "
        "exceeds the energy required to break the reactant bonds",
        "The reaction is exothermic when the energy required to break the reactant bonds "
        "exceeds the energy released forming the product bonds",
        "The reaction is exothermic when the reactant bonds are more numerous than the "
        "product bonds",
        "The reaction is exothermic when the strongest bond in the reaction is in a product",
        "The reaction is exothermic whenever any bonds are formed at all"],
      ans=0,
      why="EK 6.7.A.2's own sentence: if the energy released is greater than the energy "
          "required, the reaction is exothermic. The comparison is between the two totals "
          "and not between counts of bonds or individual bond strengths."),
]
