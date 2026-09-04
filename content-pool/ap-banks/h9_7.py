# AP CHEMISTRY 9.7 Coupled Reactions
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.7.A: explain the relationship between external sources of energy
# or coupled reactions and their ability to drive thermodynamically unfavorable
# processes.
# Suggested skill 4.D, explain the degree to which a model or representation describes
# the connection between particulate-level properties and macroscopic properties.
#
# Essential knowledge relied on, in the framework's own words:
#   9.7.A.1  An external source of energy can be used to make a thermodynamically
#            unfavorable process occur. Examples include:
#              i.  Electrical energy to drive an electrolytic cell or charge a battery.
#              ii. Light to drive the overall conversion of carbon dioxide to glucose in
#                  photosynthesis.
#   9.7.A.2  A desired product can be formed by coupling a thermodynamically unfavorable
#            reaction that produces that product to a favorable reaction (for example the
#            conversion of ATP to ADP in biological systems). In the coupled system, the
#            individual reactions share one or more common intermediates. The sum of the
#            individual reactions produces an overall reaction that achieves the desired
#            outcome and has a standard free energy change below zero.
#
# THE TEST OF A COUPLING IS ARITHMETIC, and it is a STRICT inequality: EK 9.7.A.2 requires
# the SUM to be below zero, so a pair that sums to exactly zero does not achieve the
# outcome. Every sum below is recomputed in verify_h9_7.py from the stem or the table
# alone, and one item sits deliberately at zero so the boundary is tested rather than
# assumed.
#
# SCOPE. 9.7.A.1 names the electrolytic cell as an example, so the phrase belongs here --
# but the cells themselves are 9.8 to 9.11's material and nothing below computes a cell
# potential, names an electrode, or uses Faraday's law. verify_h9_7.py asserts that.
#
# NO FIGURES. Every stimulus is a table or is stated in the stem.
TOPIC = ("9.7", "Coupled Reactions", 9)

_T_COUPLE = dict(
    headers=["Pair", "Free energy change of the unfavorable step, kJ/mol",
             "Free energy change of the favorable step, kJ/mol"],
    rows=[["Pair 1", "+45.0", "-70.0"],
          ["Pair 2", "+90.0", "-30.0"],
          ["Pair 3", "+15.0", "-15.0"],
          ["Pair 4", "+20.0", "-55.0"]])

QUESTIONS = [

 dict(q="What does the framework say an external source of energy can be used to do?",
      choices=[
        "Make a thermodynamically unfavorable process occur",
        "Make a thermodynamically favored process occur more quickly",
        "Change the sign of the entropy change of a process",
        "Remove the need for a chemical reaction altogether",
        "Lower the temperature at which a favored process occurs"],
      ans=0,
      why="EK 9.7.A.1 opens by saying that an external source of energy can be used to make "
          "a thermodynamically unfavorable process occur, and gives two examples of doing "
          "so. It says nothing about speeding a favored process up."),

 dict(q="Which examples of external sources of energy does the framework give?",
      choices=[
        "Electrical energy driving an electrolytic cell or charging a battery, and light "
        "driving the conversion of carbon dioxide to glucose",
        "Heat from a flame and stirring of the reaction mixture",
        "Sound waves and mechanical grinding of the reactants",
        "A rise in pressure and a fall in temperature",
        "Adding more reactant and removing the product as it forms"],
      ans=0,
      why="EK 9.7.A.1 lists exactly two examples: electrical energy to drive an "
          "electrolytic cell or charge a battery, and light to drive the overall "
          "conversion of carbon dioxide to glucose in photosynthesis."),

 dict(q="Which example of coupling in biological systems does the framework give?",
      choices=[
        "The conversion of ATP to ADP",
        "The conversion of glucose to carbon dioxide",
        "The transport of oxygen by haemoglobin",
        "The formation of a peptide bond between two amino acids",
        "The breakdown of hydrogen peroxide by an enzyme"],
      ans=0,
      why="EK 9.7.A.2 names the conversion of ATP to ADP in biological systems as its "
          "example of a favorable reaction coupled to an unfavorable one that produces a "
          "desired product."),

 dict(q="What must be true of the sum of the individual reactions in a coupled system?",
      choices=[
        "Its standard free energy change is below zero",
        "Its standard free energy change is above zero",
        "Its standard free energy change is exactly zero",
        "Its enthalpy change is below zero",
        "Its entropy change is above zero"],
      ans=0,
      why="EK 9.7.A.2 says the sum of the individual reactions produces an overall reaction "
          "that achieves the desired outcome and has a standard free energy change below "
          "zero. The condition is on the free energy change of the sum, not on its "
          "enthalpy or entropy separately."),

 dict(q="What do the individual reactions in a coupled system share, according to the "
        "framework?",
      choices=[
        "One or more common intermediates",
        "The same standard free energy change",
        "The same reactants and the same products",
        "The same temperature dependence",
        "A common catalyst that speeds both of them"],
      ans=0,
      why="EK 9.7.A.2 states that in the coupled system the individual reactions share one "
          "or more common intermediates, which is what allows their sum to be a single "
          "overall reaction."),

 dict(q="An unfavorable step has \\( \\Delta G^\\circ = +30.0 \\) kJ/mol and is coupled to "
        "a favorable step with \\( \\Delta G^\\circ = -50.0 \\) kJ/mol. What is the "
        "standard free energy change of the overall reaction?",
      choices=[
        "\\( -20.0 \\) kJ/mol, so the coupling achieves the desired outcome",
        "\\( +20.0 \\) kJ/mol, so the coupling fails to achieve the desired outcome",
        "\\( +80.0 \\) kJ/mol, so the coupling fails to achieve the desired outcome",
        "\\( -80.0 \\) kJ/mol, so the coupling achieves the desired outcome",
        "\\( -50.0 \\) kJ/mol, so the coupling achieves the desired outcome"],
      ans=0,
      why="EK 9.7.A.2 makes the overall reaction the sum of the individual reactions, so "
          "the two free energy changes are added with their signs. The result is below "
          "zero, which is the condition the same statement sets for achieving the desired "
          "outcome."),

 dict(q="A step with \\( \\Delta G^\\circ = +60.0 \\) kJ/mol is coupled to one with \\( "
        "\\Delta G^\\circ = -25.0 \\) kJ/mol. What is the standard free energy change of "
        "the overall reaction?",
      choices=[
        "\\( +35.0 \\) kJ/mol, so the coupling fails to achieve the desired outcome",
        "\\( -35.0 \\) kJ/mol, so the coupling achieves the desired outcome",
        "\\( +85.0 \\) kJ/mol, so the coupling fails to achieve the desired outcome",
        "\\( -85.0 \\) kJ/mol, so the coupling achieves the desired outcome",
        "\\( -25.0 \\) kJ/mol, so the coupling achieves the desired outcome"],
      ans=0,
      why="EK 9.7.A.2 requires the SUM of the individual reactions to have a standard free "
          "energy change below zero, and here the favorable step is not large enough to "
          "outweigh the unfavorable one. Coupling to a favorable reaction is not by itself "
          "enough."),

 dict(q="A step with \\( \\Delta G^\\circ = +40.0 \\) kJ/mol is coupled to one with \\( "
        "\\Delta G^\\circ = -40.0 \\) kJ/mol. Does the coupling achieve the desired "
        "outcome?",
      choices=[
        "No, the sum is \\( 0.0 \\) kJ/mol, which is not below zero",
        "Yes, the sum is \\( 0.0 \\) kJ/mol, which is enough",
        "Yes, the sum is \\( -80.0 \\) kJ/mol",
        "No, the sum is \\( +80.0 \\) kJ/mol",
        "Yes, because the favorable step is as large as the unfavorable one"],
      ans=0,
      why="EK 9.7.A.2 requires the overall reaction to have a standard free energy change "
          "BELOW zero, and a sum of exactly zero does not meet that condition. Matching "
          "the unfavorable step exactly leaves the overall process on the boundary rather "
          "than past it."),

 dict(q="The table gives the two steps of four proposed couplings. Which couplings achieve "
        "an overall reaction that is thermodynamically favored?",
      table=_T_COUPLE,
      choices=["Pairs 1 and 4", "Pairs 2 and 3", "Pairs 1, 3 and 4", "Pair 4 alone",
               "All four pairs"],
      ans=0,
      why="EK 9.7.A.2 makes the overall free energy change the sum of the two steps and "
          "requires it to be below zero. Two of the tabulated sums are below zero, one is "
          "above it, and one is exactly zero, which does not qualify."),

 dict(q="Using the same table, which proposed coupling fails even though its second step "
        "is thermodynamically favored?",
      table=_T_COUPLE,
      choices=["Pair 2", "Pair 1", "Pair 3", "Pair 4", "None of the four pairs"],
      ans=0,
      why="EK 9.7.A.2 requires the SUM to be below zero, so a favorable step that is too "
          "small to outweigh the unfavorable one leaves the overall reaction above zero. "
          "Exactly one tabulated sum is above zero."),

 dict(q="Using the tabulated pairs once more, which coupling gives an overall reaction "
        "with a standard free energy change of exactly zero?",
      table=_T_COUPLE,
      choices=["Pair 3", "Pair 1", "Pair 2", "Pair 4", "None of the four pairs"],
      ans=0,
      why="Summing the two tabulated steps gives exactly zero for one pair, and EK 9.7.A.2 "
          "requires a value below zero, so that pair sits on the boundary and does not "
          "achieve the outcome."),

 dict(q="Using the tabulated pairs again, which coupling gives the most negative overall "
        "standard free energy change?",
      table=_T_COUPLE,
      choices=["Pair 4", "Pair 1", "Pair 2", "Pair 3", "Pairs 1 and 4 equally"],
      ans=0,
      why="EK 9.7.A.2 makes the overall change the sum of the two tabulated steps, and "
          "comparing the four sums identifies a single most negative value. A larger "
          "favorable step does not by itself decide it, since the unfavorable steps differ "
          "as well."),

 dict(q="In a coupled system, the step P(s) + Q(aq) gives R(aq) is unfavorable and the "
        "step R(aq) gives S(aq) + T(g) is favorable. Which species is the common "
        "intermediate?",
      choices=["R(aq)", "P(s)", "Q(aq)", "S(aq)", "T(g)"],
      ans=0,
      why="EK 9.7.A.2 says the individual reactions of a coupled system share one or more "
          "common intermediates, and exactly one species here is produced by the first "
          "step and consumed by the second, so it cancels when the two are added."),

 dict(q="For the same two steps, P(s) + Q(aq) gives R(aq) and R(aq) gives S(aq) + T(g), "
        "what is the overall reaction of the coupled system?",
      choices=[
        "P(s) + Q(aq) gives S(aq) + T(g)",
        "P(s) + Q(aq) gives R(aq) + S(aq)",
        "R(aq) gives S(aq) + T(g)",
        "S(aq) + T(g) gives P(s) + Q(aq)",
        "P(s) gives S(aq) + T(g)"],
      ans=0,
      why="EK 9.7.A.2 says the sum of the individual reactions produces the overall "
          "reaction, and the common intermediate appears once on each side of that sum, so "
          "it cancels and does not appear in the overall equation."),

 dict(q="Why must the reactions of a coupled system share a common intermediate?",
      choices=[
        "So that adding them gives a single overall reaction producing the desired product",
        "So that the two reactions occur at the same rate as one another",
        "So that the two reactions have the same standard free energy change",
        "So that the unfavorable reaction becomes favorable on its own",
        "So that no catalyst is needed for either reaction"],
      ans=0,
      why="EK 9.7.A.2 says the individual reactions share one or more common intermediates "
          "and that their SUM produces an overall reaction achieving the desired outcome, "
          "so the shared species is what makes the two into one."),

 dict(q="Does coupling change the standard free energy change of the unfavorable reaction "
        "itself?",
      choices=[
        "No, the unfavorable step keeps its own positive value and it is the sum that lies "
        "below zero",
        "Yes, the unfavorable step becomes favorable once it is coupled",
        "Yes, its value becomes the average of the two steps",
        "No, and for that reason coupling cannot produce the desired product",
        "Yes, its value falls to zero once the two share an intermediate"],
      ans=0,
      why="EK 9.7.A.2 places the condition on the SUM of the individual reactions, which "
          "produces an overall reaction with a standard free energy change below zero. The "
          "individual reaction is unchanged, and the desired product is still formed "
          "because the overall reaction is the one that occurs."),

 dict(q="Light drives the overall conversion of carbon dioxide to glucose in "
        "photosynthesis. What does the framework offer this as an example of?",
      choices=[
        "An external source of energy making a thermodynamically unfavorable process occur",
        "A coupled system in which two reactions share a common intermediate",
        "A thermodynamically favored process occurring at a measurable rate",
        "A process whose entropy change is made positive by the light",
        "A reaction whose equilibrium position is unaffected by the energy supplied"],
      ans=0,
      why="EK 9.7.A.1 lists light driving the conversion of carbon dioxide to glucose as "
          "its second example of an external source of energy used to make a "
          "thermodynamically unfavorable process occur. The coupling of shared "
          "intermediates is the separate mechanism of EK 9.7.A.2."),

 dict(q="Electrical energy is used to drive an electrolytic cell or to charge a battery. "
        "What does the framework offer this as an example of?",
      choices=[
        "An external source of energy making a thermodynamically unfavorable process occur",
        "Two reactions coupled through a shared common intermediate",
        "A thermodynamically favored process being slowed down",
        "A process whose free energy change is zero by construction",
        "A way of raising the temperature at which a process becomes favored"],
      ans=0,
      why="EK 9.7.A.1 lists electrical energy driving an electrolytic cell or charging a "
          "battery as its first example of an external source of energy used to make a "
          "thermodynamically unfavorable process occur."),

 dict(q="Which of these is NOT a way the framework describes for making a thermodynamically "
        "unfavorable process occur?",
      choices=[
        "Waiting long enough for the process to occur of its own accord",
        "Supplying electrical energy from outside the system",
        "Supplying light energy from outside the system",
        "Coupling the process to a thermodynamically favorable reaction",
        "Adding the process to a favorable one with which it shares an intermediate"],
      ans=0,
      why="EK 9.7.A.1 names external sources of energy and EK 9.7.A.2 names coupling "
          "through a common intermediate, and those are the two routes the topic gives. "
          "Neither statement suggests that time alone makes an unfavorable process occur."),

 dict(q="A desired product is formed by a reaction that is thermodynamically unfavorable. "
        "What does the framework say can be done about it?",
      choices=[
        "Couple that reaction to a favorable one with which it shares an intermediate",
        "Reverse the reaction so that it becomes favorable",
        "Wait until the reaction reaches equilibrium on its own",
        "Raise the concentration of the desired product",
        "Choose a different product that a favorable reaction already makes"],
      ans=0,
      why="EK 9.7.A.2 says a desired product can be formed by coupling a thermodynamically "
          "unfavorable reaction that produces that product to a favorable reaction, with "
          "the two sharing one or more common intermediates. Reversing the reaction would "
          "stop it producing the product at all."),

 dict(q="What must be true of the reaction that an unfavorable step is coupled to?",
      choices=[
        "It must be favorable, and favorable enough that the two sum to a value below zero",
        "It must be favorable, and any favorable reaction will do",
        "It must be unfavorable by a smaller amount than the first",
        "It must have exactly the opposite free energy change",
        "It must produce the same desired product as the first"],
      ans=0,
      why="EK 9.7.A.2 requires the SUM of the individual reactions to have a standard free "
          "energy change below zero, so the size of the favorable reaction matters as well "
          "as its sign. An exactly opposite value would leave the sum at zero."),

 dict(q="An unfavorable step has \\( \\Delta G^\\circ = +55.0 \\) kJ/mol. Which favorable "
        "step would NOT be enough to make the coupled sum thermodynamically favored?",
      choices=["\\( -50.0 \\) kJ/mol", "\\( -60.0 \\) kJ/mol", "\\( -75.0 \\) kJ/mol",
               "\\( -90.0 \\) kJ/mol", "\\( -120.0 \\) kJ/mol"],
      ans=0,
      why="EK 9.7.A.2 requires the sum of the two steps to lie below zero, so the favorable "
          "step has to exceed the unfavorable one in size. Exactly one of the values "
          "offered is smaller in size than the unfavorable step and so leaves the sum "
          "above zero."),

 dict(q="A student says that coupling makes the unfavorable reaction favorable in its own "
        "right. What is wrong with that?",
      choices=[
        "It is the overall sum that is below zero, not the unfavorable reaction itself",
        "Nothing is wrong: coupling changes the free energy change of each step",
        "Coupling makes the favorable reaction unfavorable instead",
        "Coupling has no effect on any free energy change at all, so nothing is achieved",
        "The unfavorable reaction stops occurring once it is coupled"],
      ans=0,
      why="EK 9.7.A.2 puts the condition on the sum of the individual reactions, which "
          "produces an overall reaction with a standard free energy change below zero. Each "
          "individual reaction keeps its own value, and coupling still achieves the desired "
          "outcome because the overall reaction is what occurs."),

 dict(q="A student says that any thermodynamically favorable reaction can be used to drive "
        "any unfavorable one. What is wrong with that?",
      choices=[
        "The two must share a common intermediate and must sum to a value below zero",
        "Only reactions with the same enthalpy change can be coupled",
        "Only reactions occurring at the same temperature can be coupled",
        "Nothing is wrong, provided both reactions occur in the same container",
        "Only reactions in biological systems can be coupled"],
      ans=0,
      why="EK 9.7.A.2 sets two conditions: the individual reactions share one or more "
          "common intermediates, and their sum has a standard free energy change below "
          "zero. Sharing a container is not one of them."),

 dict(q="What role does the conversion of ATP to ADP play in the framework's example?",
      choices=[
        "It is the favorable reaction to which an unfavorable one is coupled",
        "It is the unfavorable reaction that produces the desired product",
        "It is the common intermediate shared by the two reactions",
        "It is the external source of energy supplied from outside the system",
        "It is the overall reaction produced by the coupling"],
      ans=0,
      why="EK 9.7.A.2 offers the conversion of ATP to ADP as its example while describing "
          "the coupling of a thermodynamically unfavorable reaction that produces a desired "
          "product TO a favorable reaction, so it plays the favorable part."),

 dict(q="How does an external source of energy differ from a coupled reaction as a way of "
        "driving an unfavorable process?",
      choices=[
        "The energy comes from outside the chemical system rather than from another "
        "reaction within it",
        "The energy source changes the sign of the free energy change of the process",
        "The energy source works only for physical processes and not for chemical ones",
        "A coupled reaction requires no shared species, while an energy source does",
        "There is no difference, since the framework treats them as the same thing"],
      ans=0,
      why="EK 9.7.A.1 speaks of an EXTERNAL source of energy, naming electricity and light, "
          "while EK 9.7.A.2 describes a second reaction inside the same chemical system "
          "sharing a common intermediate. Neither alters the free energy change of the "
          "unfavorable process itself."),

 dict(q="Two steps sum to an overall reaction whose standard free energy change is below "
        "zero. What does the framework say has been achieved?",
      choices=[
        "An overall reaction that achieves the desired outcome",
        "A favorable reaction that no longer needs the unfavorable step",
        "A reaction that will proceed at a measurable rate",
        "A reaction whose equilibrium lies entirely toward the products",
        "A process that requires no reactants at all"],
      ans=0,
      why="EK 9.7.A.2 says the sum of the individual reactions produces an overall reaction "
          "that achieves the desired outcome and has a standard free energy change below "
          "zero. Whether it proceeds at a measurable rate is the separate question of EK "
          "9.4.A.2."),

 dict(q="Charging a battery is the reverse of the process that occurs when the battery is "
        "used. What does that make the charging?",
      choices=[
        "A thermodynamically unfavorable process driven by an external source of energy",
        "A thermodynamically favored process that needs no help",
        "A coupled system sharing a common intermediate",
        "A process whose free energy change is zero",
        "A process that becomes favorable at a high enough temperature"],
      ans=0,
      why="EK 9.7.A.1 names charging a battery among its examples of using electrical "
          "energy from outside to make a thermodynamically unfavorable process occur, "
          "which is what the reverse of a favorable process must be."),

 dict(q="Which two routes does this topic give for bringing about a thermodynamically "
        "unfavorable process?",
      choices=[
        "Supplying energy from outside the system, or coupling to a favorable reaction "
        "within it",
        "Raising the temperature, or lowering the pressure",
        "Adding a catalyst, or waiting for equilibrium",
        "Increasing the concentration of reactants, or removing the products",
        "Reversing the process, or slowing it down"],
      ans=0,
      why="EK 9.7.A.1 gives the first route and EK 9.7.A.2 the second, and those two "
          "statements are the whole content of the topic. Neither route changes the free "
          "energy change of the unfavorable process itself."),

 dict(q="In a coupled system the unfavorable step has \\( \\Delta G^\\circ = +75.0 \\) "
        "kJ/mol and the overall reaction has \\( \\Delta G^\\circ = -15.0 \\) kJ/mol. What "
        "is the standard free energy change of the favorable step?",
      choices=["\\( -90.0 \\) kJ/mol", "\\( +90.0 \\) kJ/mol", "\\( -60.0 \\) kJ/mol",
               "\\( +60.0 \\) kJ/mol", "\\( -15.0 \\) kJ/mol"],
      ans=0,
      why="EK 9.7.A.2 makes the overall reaction the SUM of the individual reactions, so "
          "the favorable step is the overall change less the unfavorable one. Subtracting "
          "in the other order gives a value of the wrong sign, and taking the difference "
          "of the sizes gives the wrong magnitude as well."),

]
