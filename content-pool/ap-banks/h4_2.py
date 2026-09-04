# AP CHEMISTRY 4.2 Net Ionic Equations
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.2.A: represent changes in matter with a balanced chemical
# or net ionic equation, (i) for physical changes, (ii) for given information
# about the identity of the reactants and/or products, (iii) for ions in a given
# chemical reaction. Suggested skill 5.E, determine a balanced chemical equation
# for a given chemical phenomenon.
#
# Essential knowledge relied on, in the framework's own words:
#   4.2.A.1  All physical and chemical processes can be represented symbolically
#            by balanced equations.
#   4.2.A.2  Chemical equations represent chemical changes. These changes are
#            the result of a rearrangement of atoms into new combinations; thus,
#            any representation of a chemical change must contain equal numbers
#            of atoms of every element before and after the change occurred.
#            Equations thus demonstrate that mass and charge are conserved in
#            chemical reactions.
#   4.2.A.3  Balanced molecular, complete ionic, and net ionic equations are
#            differing symbolic forms used to represent a chemical reaction. The
#            form used to represent the reaction depends on the context in which
#            it is to be used.
#
# 4.2.A.2 IS A COUNTABLE CLAIM, so this module leans on it. Every equation that
# appears in a choice is parsed by h_equation.py and its atoms and its charge
# are added up on both sides, so a keyed equation that did not balance would
# fail the verifier rather than teach a student a false balance. That parser
# carries its own positive and negative controls.
#
# WHAT IS NOT HERE. Which substances are soluble, and therefore which
# combination gives a precipitate, is 4.7 and 4.8's material; every item here
# either states the products or asks about the FORM of the equation rather than
# about predicting one. Particulate drawings of the same reaction are 4.3.
# Classifying a change as physical or chemical is 4.1 and 4.4.
#
# NOTATION. Chemistry is not typeset, so the arrow is the word "gives" and ions
# are written the ordinary plain-text way: Ag+, Cl-, Ca2+, SO42-. There is no
# mathematics in this topic and therefore no hand-written span.
TOPIC = ("4.2", "Net Ionic Equations", 4)

_T_EQUATIONS = dict(
    headers=["Label", "Equation as the student wrote it"],
    rows=[["E1", "2 H2(g) + O2(g) gives 2 H2O(l)"],
          ["E2", "N2(g) + H2(g) gives NH3(g)"],
          ["E3", "CaCO3(s) gives CaO(s) + CO2(g)"],
          ["E4", "Al(s) + O2(g) gives Al2O3(s)"]])

_T_FORMS = dict(
    headers=["Row", "Equation"],
    rows=[["R1", "CaCl2(aq) + Na2CO3(aq) gives CaCO3(s) + 2 NaCl(aq)"],
          ["R2", "Ca2+(aq) + 2 Cl-(aq) + 2 Na+(aq) + CO32-(aq) gives "
                 "CaCO3(s) + 2 Na+(aq) + 2 Cl-(aq)"],
          ["R3", "Ca2+(aq) + CO32-(aq) gives CaCO3(s)"]])

_T_CHARGE = dict(
    headers=["Label", "Proposed net ionic equation"],
    rows=[["N1", "Ag+(aq) + Cl-(aq) gives AgCl(s)"],
          ["N2", "Ba2+(aq) + SO42-(aq) gives BaSO4(s)"],
          ["N3", "Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu2+(aq)"],
          ["N4", "H3O+(aq) + OH-(aq) gives 2 H2O(l)"]])

QUESTIONS = [

 dict(q="According to the framework, what must any representation of a chemical "
        "change contain?",
      choices=[
        "Equal numbers of atoms of every element before and after the change",
        "Equal numbers of molecules before and after the change",
        "Equal numbers of substances before and after the change",
        "The same physical states before and after the change",
        "A whole number of atoms of at least one element on each side"],
      ans=0,
      why="EK 4.2.A.2, near verbatim: any representation of a chemical change "
          "must contain equal numbers of atoms of every element before and "
          "after the change occurred. The count is by element, not by molecule "
          "or by substance."),

 dict(q="Why does the framework require those numbers to be equal?",
      choices=[
        "Because a chemical change is a rearrangement of atoms into new "
        "combinations rather than a creation or destruction of atoms",
        "Because chemists have agreed to write equations that way for "
        "convenience",
        "Because the coefficients in an equation are chosen to make the "
        "arithmetic simple",
        "Because every chemical change happens in a sealed container",
        "Because the products of a reaction always weigh the same as one "
        "another"],
      ans=0,
      why="EK 4.2.A.2 states that these changes are the result of a "
          "rearrangement of atoms into new combinations, and draws the equal "
          "atom counts from that. The requirement is about what a chemical "
          "change is, not about notation."),

 dict(q="What does the framework say balanced equations demonstrate about "
        "chemical reactions?",
      choices=[
        "That mass and charge are conserved",
        "That energy and volume are conserved",
        "That the number of molecules is conserved",
        "That the temperature of the system is conserved",
        "That the number of substances is conserved"],
      ans=0,
      why="EK 4.2.A.2 ends by stating that equations thus demonstrate that mass "
          "and charge are conserved in chemical reactions. Molecule counts "
          "routinely change, as four molecules going to two shows."),

 dict(q="Which processes does the framework say can be represented "
        "symbolically by balanced equations?",
      choices=[
        "All physical and chemical processes",
        "Only chemical processes, since physical changes make no new substances",
        "Only processes in which a precipitate or a gas forms",
        "Only processes carried out in aqueous solution",
        "Only processes whose products have been identified by experiment"],
      ans=0,
      why="EK 4.2.A.1, verbatim in substance: all physical and chemical "
          "processes can be represented symbolically by balanced equations. A "
          "phase change is therefore writable as an equation."),

 dict(q="Which three symbolic forms does the framework name for representing a "
        "chemical reaction?",
      choices=[
        "Balanced molecular, complete ionic, and net ionic equations",
        "Balanced molecular, particulate, and energy equations",
        "Empirical, molecular, and structural equations",
        "Complete ionic, net ionic, and half reaction equations",
        "Balanced molecular, thermochemical, and rate equations"],
      ans=0,
      why="EK 4.2.A.3, near verbatim: balanced molecular, complete ionic, and "
          "net ionic equations are differing symbolic forms used to represent a "
          "chemical reaction."),

 dict(q="What determines which of those forms a chemist writes for a given "
        "reaction?",
      choices=[
        "The context in which the equation is to be used",
        "The number of atoms the reaction rearranges",
        "Whether the reaction gives off energy",
        "The phase of the product with the greatest mass",
        "Whether the reaction can be carried out in a laboratory"],
      ans=0,
      why="EK 4.2.A.3 states that the form used to represent the reaction "
          "depends on the context in which it is to be used, so none of the "
          "three is the single correct representation of a reaction."),

 dict(q="Propane, C3H8, burns completely in oxygen to give carbon dioxide and "
        "water. Which equation is balanced?",
      choices=[
        "C3H8 + 5 O2 gives 3 CO2 + 4 H2O",
        "C3H8 + 3 O2 gives 3 CO2 + 4 H2O",
        "C3H8 + 5 O2 gives 3 CO2 + 3 H2O",
        "C3H8 + 4 O2 gives 3 CO2 + 4 H2O",
        "C3H8 + 5 O2 gives CO2 + 4 H2O"],
      ans=0,
      why="EK 4.2.A.2 requires equal numbers of atoms of every element on the "
          "two sides. Three carbons, eight hydrogens and ten oxygens appear on "
          "each side of the keyed equation and on neither side of any other."),

 dict(q="Iron reacts with oxygen to form Fe2O3. In the equation 4 Fe + n O2 "
        "gives 2 Fe2O3, what value of n balances it?",
      choices=["3", "2", "4", "5", "6"],
      ans=0,
      why="EK 4.2.A.2 requires equal atom counts by element. Two units of Fe2O3 "
          "carry six oxygen atoms, and three O2 molecules supply exactly six, "
          "while the four iron atoms already match."),

 dict(q="Silver nitrate solution is mixed with sodium chloride solution and "
        "solid silver chloride forms. Which equation is the net ionic equation "
        "for the reaction?",
      choices=[
        "Ag+(aq) + Cl-(aq) gives AgCl(s)",
        "AgNO3(aq) + NaCl(aq) gives AgCl(s) + NaNO3(aq)",
        "Ag+(aq) + NO3-(aq) + Na+(aq) + Cl-(aq) gives AgCl(s) + Na+(aq) + "
        "NO3-(aq)",
        "Na+(aq) + NO3-(aq) gives NaNO3(aq)",
        "Ag+(aq) + 2 Cl-(aq) gives AgCl2(s)"],
      ans=0,
      why="EK 4.2.A.3 names the net ionic equation as one of three symbolic "
          "forms; it carries only the ions whose combination is the change. "
          "One silver ion and one chloride ion give one formula unit of the "
          "solid, and the total charge is zero on both sides."),

 dict(q="In the mixing of silver nitrate solution with sodium chloride "
        "solution, which ions appear unaltered on both sides of the complete "
        "ionic equation?",
      choices=[
        "Sodium ion and nitrate ion",
        "Silver ion and chloride ion",
        "Silver ion and nitrate ion",
        "Sodium ion and chloride ion",
        "Every ion present appears unaltered on both sides"],
      ans=0,
      why="EK 4.2.A.3 distinguishes the complete ionic from the net ionic form. "
          "Writing every dissolved species out shows sodium and nitrate in "
          "solution before and after, while silver and chloride leave solution "
          "as the solid."),

 dict(q="A student writes Ag+(aq) + NO3-(aq) + Na+(aq) + Cl-(aq) gives AgCl(s) "
        "+ Na+(aq) + NO3-(aq). Which form of equation has been written?",
      choices=[
        "The complete ionic equation",
        "The net ionic equation",
        "The balanced molecular equation",
        "A physical change equation",
        "An equation that is not balanced at all"],
      ans=0,
      why="EK 4.2.A.3 names three forms. Every dissolved substance has been "
          "written as separate ions and the unchanged ones are still present, "
          "which is what distinguishes the complete ionic form from the net "
          "ionic one."),

 dict(q="Which of the following is the balanced molecular equation for the "
        "reaction of barium chloride solution with sodium sulfate solution to "
        "give solid barium sulfate?",
      choices=[
        "BaCl2(aq) + Na2SO4(aq) gives BaSO4(s) + 2 NaCl(aq)",
        "Ba2+(aq) + SO42-(aq) gives BaSO4(s)",
        "BaCl2(aq) + Na2SO4(aq) gives BaSO4(s) + NaCl(aq)",
        "Ba2+(aq) + 2 Cl-(aq) + 2 Na+(aq) + SO42-(aq) gives BaSO4(s) + 2 Na+(aq) "
        "+ 2 Cl-(aq)",
        "BaCl2(aq) + NaSO4(aq) gives BaSO4(s) + NaCl2(aq)"],
      ans=0,
      why="EK 4.2.A.3 makes the molecular form the one in which each substance "
          "is written as a compound rather than as ions, and EK 4.2.A.2 "
          "requires the atom counts to match, which needs two formula units of "
          "sodium chloride."),

 dict(q="Which equation conserves both the number of atoms of every element and "
        "the total charge?",
      choices=[
        "Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu(s)",
        "Zn(s) + Cu2+(aq) gives Zn2+(aq) + Cu2+(aq)",
        "2 Ag+(aq) + Cu(s) gives Ag(s) + Cu2+(aq)",
        "Fe(s) + 2 H3O+(aq) gives Fe3+(aq) + H2(g) + 2 H2O(l)",
        "Mg(s) + H3O+(aq) gives Mg2+(aq) + H2(g) + H2O(l)"],
      ans=0,
      why="EK 4.2.A.2 says equations demonstrate that mass AND charge are "
          "conserved, so both sums must agree. Only the keyed equation has one "
          "zinc and one copper on each side together with a total charge of "
          "plus two on each side."),

 dict(q="Which equation represents the vaporization of liquid water?",
      choices=[
        "H2O(l) gives H2O(g)",
        "H2O(g) gives H2O(l)",
        "H2O(l) gives H2(g) + O2(g)",
        "2 H2O(l) gives 2 H2(g) + O2(g)",
        "H2O(l) gives H2O(s)"],
      ans=0,
      why="EK 4.2.A.1 allows all physical processes to be represented "
          "symbolically by balanced equations, and vaporization takes the "
          "liquid to the gas with the composition unaltered, as EK 4.1.A.1 "
          "requires of a phase change."),

 dict(q="Solid sodium chloride dissolving is written NaCl(s) gives Na+(aq) + "
        "Cl-(aq). What does this equation demonstrate about charge?",
      choices=[
        "The total charge is zero on each side, so charge is conserved",
        "The total charge rises from zero to plus one, so charge is created",
        "The total charge falls from zero to minus one, so charge is destroyed",
        "Charge cannot be assessed because the solid carries no ions",
        "Charge is conserved only if the two ions are written on separate lines"],
      ans=0,
      why="EK 4.2.A.2 has equations demonstrate that mass and charge are "
          "conserved. The neutral solid gives one ion of plus one and one of "
          "minus one, whose sum is zero, matching the left side."),

 dict(q="The table gives four equations written by a student. In which of them "
        "do equal numbers of atoms of every element appear on both sides?",
      table=_T_EQUATIONS,
      choices=[
        "E1 and E3",
        "E2 and E4",
        "All four of them",
        "Only E1",
        "Only E3"],
      ans=0,
      why="EK 4.2.A.2 requires equal numbers of atoms of every element before "
          "and after the change. Counting each element in each tabulated "
          "equation is what separates those that meet the requirement from "
          "those that do not."),

 dict(q="Hydrochloric acid is neutralized by sodium hydroxide solution. Which "
        "equation is the net ionic equation for the neutralization?",
      choices=[
        "H3O+(aq) + OH-(aq) gives 2 H2O(l)",
        "HCl(aq) + NaOH(aq) gives NaCl(aq) + H2O(l)",
        "Na+(aq) + Cl-(aq) gives NaCl(aq)",
        "H3O+(aq) + OH-(aq) gives H2O(l)",
        "H3O+(aq) + Cl-(aq) + Na+(aq) + OH-(aq) gives Na+(aq) + Cl-(aq) + "
        "2 H2O(l)"],
      ans=0,
      why="EK 4.2.A.3 makes the net ionic equation the form carrying only the "
          "species that change. Four hydrogens and two oxygens on the left "
          "require two water molecules on the right, which EK 4.2.A.2's equal "
          "atom counts settle."),

 dict(q="What is the advantage of the net ionic form when a chemist wants to "
        "show what the reaction actually accomplishes?",
      choices=[
        "It is the form that suits that context, because it carries only the "
        "species whose combination differs before and after",
        "It is the only one of the three forms that is balanced",
        "It is the only form in which charge is conserved",
        "It is the only form that may be used on a written examination",
        "It is the form that shows the largest number of substances"],
      ans=0,
      why="EK 4.2.A.3 states that the form used depends on the context in which "
          "it is to be used, so the net ionic form is a choice suited to a "
          "purpose rather than a more correct equation; EK 4.2.A.2's "
          "conservation holds for all three forms."),

 dict(q="Magnesium metal is dropped into hydrochloric acid and hydrogen gas is "
        "released. Which equation is the net ionic equation?",
      choices=[
        "Mg(s) + 2 H3O+(aq) gives Mg2+(aq) + H2(g) + 2 H2O(l)",
        "Mg(s) + 2 HCl(aq) gives MgCl2(aq) + H2(g)",
        "Mg(s) + H3O+(aq) gives Mg2+(aq) + H2(g) + H2O(l)",
        "Mg(s) + 2 Cl-(aq) gives MgCl2(aq)",
        "Mg2+(aq) + 2 Cl-(aq) gives MgCl2(aq)"],
      ans=0,
      why="EK 4.2.A.3 makes the net ionic form the one without the unchanged "
          "chloride, and EK 4.2.A.2 requires the atoms and the charge to "
          "balance: six hydrogens and two oxygens on each side, with a total of "
          "plus two on each side."),

 dict(q="A strip of zinc is placed in copper sulfate solution, the strip "
        "darkens, and the blue color fades. The net ionic equation is Zn(s) + "
        "Cu2+(aq) gives Zn2+(aq) + Cu(s). Which statement about it is correct?",
      choices=[
        "Charge is conserved, because the total is plus two on each side",
        "Charge is not conserved, because a neutral atom appears on each side",
        "Charge is not conserved, because the two ions carry opposite signs",
        "Charge cannot be assessed until the sulfate ion is written in",
        "Charge is conserved only because zinc and copper have equal masses"],
      ans=0,
      why="EK 4.2.A.2 has equations demonstrate the conservation of charge. "
          "Adding the charges gives plus two on the left from the copper ion "
          "and plus two on the right from the zinc ion, with the metals "
          "contributing nothing."),

 dict(q="Which of the following proposed equations fails to conserve charge?",
      choices=[
        "Zn(s) + Ag+(aq) gives Zn2+(aq) + Ag(s)",
        "Ag+(aq) + Cl-(aq) gives AgCl(s)",
        "Ba2+(aq) + SO42-(aq) gives BaSO4(s)",
        "H3O+(aq) + OH-(aq) gives 2 H2O(l)",
        "Ca2+(aq) + CO32-(aq) gives CaCO3(s)"],
      ans=0,
      why="EK 4.2.A.2 requires an equation to demonstrate that charge is "
          "conserved. Adding the charges in the keyed equation gives plus one "
          "on the left and plus two on the right, since one silver ion cannot "
          "supply the charge the zinc ion carries away."),

 dict(q="A student proposes Al(s) + O2(g) gives Al2O3(s) for the formation of "
        "aluminum oxide. What is wrong with it?",
      choices=[
        "The numbers of aluminum and of oxygen atoms differ across the equation",
        "The charge is not conserved across the equation",
        "The physical states are written incorrectly",
        "Nothing is wrong with it as written",
        "Aluminum oxide should have been written as a solution"],
      ans=0,
      why="EK 4.2.A.2 requires equal numbers of atoms of every element on the "
          "two sides. One aluminum faces two, and two oxygens face three, so "
          "the representation is not admissible; no species in it carries a "
          "charge."),

 dict(q="Ethanol, C2H5OH, burns completely in oxygen. Which equation is "
        "balanced?",
      choices=[
        "C2H5OH + 3 O2 gives 2 CO2 + 3 H2O",
        "C2H5OH + 2 O2 gives 2 CO2 + 3 H2O",
        "C2H5OH + 3 O2 gives 2 CO2 + 2 H2O",
        "C2H5OH + O2 gives 2 CO2 + 3 H2O",
        "C2H5OH + 3 O2 gives CO2 + 3 H2O"],
      ans=0,
      why="EK 4.2.A.2 requires equal atom counts by element. Two carbons, six "
          "hydrogens and seven oxygens appear on each side of the keyed "
          "equation, counting the oxygen already in the ethanol."),

 dict(q="Iodine sublimes when a solid sample is warmed. Can this be represented "
        "by a balanced equation, and if so how?",
      choices=[
        "Yes, as I2(s) gives I2(g), since the framework allows all physical "
        "processes to be represented symbolically",
        "No, because an equation may only be written for a chemical change",
        "No, because the composition of the sample does not change",
        "Yes, but only as 2 I(s) gives I2(g)",
        "Yes, but only if the temperature is written above the arrow"],
      ans=0,
      why="EK 4.2.A.1 states that all physical and chemical processes can be "
          "represented symbolically by balanced equations, and two iodine atoms "
          "appear on each side of the keyed representation."),

 dict(q="When balancing, why must a chemist adjust the numbers written in front "
        "of the formulas rather than the small numbers inside them?",
      choices=[
        "Because altering a number inside a formula changes the composition, "
        "and so the identity of the substance being represented",
        "Because the numbers inside a formula are always fixed at one",
        "Because the numbers in front of the formulas have no effect on the "
        "atom counts",
        "Because only the numbers in front of the formulas may be whole numbers",
        "Because the numbers inside a formula are decided by the physical state"],
      ans=0,
      why="EK 4.2.A.2 requires the equation to represent the change that "
          "occurred, and EK 4.1.A.1 makes composition the identity of a "
          "substance, so a rewritten formula would represent a different "
          "substance rather than a balanced version of the same one."),

 dict(q="Calcium chloride solution is mixed with sodium carbonate solution and "
        "solid calcium carbonate forms. Which equation is the net ionic "
        "equation?",
      choices=[
        "Ca2+(aq) + CO32-(aq) gives CaCO3(s)",
        "CaCl2(aq) + Na2CO3(aq) gives CaCO3(s) + 2 NaCl(aq)",
        "Ca2+(aq) + 2 Cl-(aq) + 2 Na+(aq) + CO32-(aq) gives CaCO3(s) + 2 Na+(aq) "
        "+ 2 Cl-(aq)",
        "2 Na+(aq) + 2 Cl-(aq) gives 2 NaCl(aq)",
        "Ca2+(aq) + 2 CO32-(aq) gives Ca(CO3)2(s)"],
      ans=0,
      why="EK 4.2.A.3 makes the net ionic form the one from which the unchanged "
          "sodium and chloride ions have been left out, and EK 4.2.A.2's charge "
          "conservation is satisfied because plus two and minus two sum to the "
          "zero charge of the solid."),

 dict(q="The table gives three equations for the same reaction. Which row is "
        "the net ionic equation?",
      table=_T_FORMS,
      choices=[
        "R3",
        "R1",
        "R2",
        "Both R1 and R2",
        "None of the three rows"],
      ans=0,
      why="EK 4.2.A.3 names balanced molecular, complete ionic and net ionic "
          "equations as differing forms of the same reaction. The net ionic "
          "form is the one written with ions in which no species stands "
          "unaltered on both sides."),

 dict(q="Aluminum reacts with chlorine gas to form solid aluminum chloride, "
        "AlCl3. Which equation represents the reaction?",
      choices=[
        "2 Al(s) + 3 Cl2(g) gives 2 AlCl3(s)",
        "Al(s) + Cl2(g) gives AlCl3(s)",
        "Al(s) + 3 Cl2(g) gives AlCl3(s)",
        "2 Al(s) + 3 Cl2(g) gives AlCl3(s)",
        "3 Al(s) + 2 Cl2(g) gives 2 AlCl3(s)"],
      ans=0,
      why="EK 4.2.A.2 requires equal atom counts by element given the stated "
          "identity of the product. Two aluminums and six chlorines appear on "
          "each side of the keyed equation and on neither side of any other."),

 dict(q="The table lists four proposed net ionic equations. Which one does NOT "
        "conserve charge?",
      table=_T_CHARGE,
      choices=[
        "N3",
        "N1",
        "N2",
        "N4",
        "All four conserve charge"],
      ans=0,
      why="EK 4.2.A.2 states that equations demonstrate that mass and charge "
          "are conserved. Summing the charges on each side of every tabulated "
          "equation is what identifies the one that fails."),

 dict(q="Two students disagree: one says a balanced equation shows only that "
        "mass is conserved, the other that it also shows charge is conserved. "
        "Which position does the framework take?",
      choices=[
        "The second, because the framework says equations demonstrate that mass "
        "and charge are conserved in chemical reactions",
        "The first, because charge appears only in a net ionic equation",
        "The first, because charge is a property of ions rather than of a "
        "reaction",
        "Neither, because the framework treats conservation as an assumption "
        "rather than something an equation shows",
        "The second, but only for reactions carried out in solution"],
      ans=0,
      why="EK 4.2.A.2 ends with exactly that statement, and it is made about "
          "chemical reactions generally rather than about one of the three "
          "symbolic forms EK 4.2.A.3 names."),
]
