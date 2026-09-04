# AP CHEMISTRY 9.10 Cell Potential Under Nonstandard Conditions
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.10.A: explain the relationship between deviations from standard cell
# conditions and changes in the cell potential. Suggested skill 6.D, provide reasoning to
# justify a claim using chemical principles or laws, or using mathematical justification.
#
# Essential knowledge relied on, in the framework's own words:
#   9.10.A.1  In a real system under nonstandard conditions, the cell potential will vary
#             depending on the concentrations of the active species. The cell potential is a
#             driving force toward equilibrium; the farther the reaction is from
#             equilibrium, the greater the magnitude of the cell potential.
#   9.10.A.2  Equilibrium arguments such as Le Chatelier's principle do not apply to
#             electrochemical systems, because the systems are not in equilibrium.
#   9.10.A.3  The standard cell potential corresponds to the standard conditions of a
#             reaction quotient of 1. As the system approaches equilibrium, the magnitude
#             (i.e., absolute value) of the cell potential decreases, reaching zero at
#             equilibrium (when the reaction quotient equals the equilibrium constant).
#             Deviations from standard conditions that take the cell further from
#             equilibrium than a reaction quotient of 1 will increase the magnitude of the
#             cell potential relative to the standard value. Deviations that take the cell
#             closer to equilibrium than a reaction quotient of 1 will decrease the
#             magnitude of the cell potential relative to the standard value. In
#             concentration cells, the direction of spontaneous electron flow can be
#             determined by considering the direction needed to reach equilibrium.
#   9.10.A.4  Algorithmic calculations using the Nernst equation are insufficient to
#             demonstrate an understanding of electrochemical cells under nonstandard
#             conditions. However, students should qualitatively understand the effects of
#             concentration on cell potential and use conceptual reasoning, including the
#             qualitative use of the Nernst equation, to solve problems.
#             EQN: \( E = E^\circ - \frac{RT}{nF} \ln Q \)
#
# EK 9.10.A.4 IS A FENCE, AND IT SHAPES EVERY ITEM HERE. The framework says an algorithmic
# Nernst calculation is INSUFFICIENT and asks instead for conceptual reasoning. So not one
# item below substitutes numbers into the Nernst equation to produce a voltage. What the
# items do compute is a reaction quotient from stated concentrations and its position
# relative to 1 and to the equilibrium constant -- which is exactly the comparison EK
# 9.10.A.3 is written in terms of. verify_h9_10.py recomputes every one of those and
# asserts that no key states a nonstandard potential as a number.
#
# THE THREE-WAY VERDICT THAT MUST NOT SHIP BACKWARDS. EK 9.10.A.3 makes the magnitude of
# the potential larger when a deviation takes the cell FURTHER from equilibrium than a
# quotient of 1 and smaller when it takes the cell CLOSER. Which of those a given set of
# concentrations produces is not a matter of taste: it is settled by comparing how far the
# quotient sits from the equilibrium constant against how far a quotient of 1 sits from it.
# verify_h9_10.py makes that comparison itself, from the numbers in the stem, and refuses a
# key that states the other verdict.
#
# LE CHATELIER IS BARRED, AND THE REASONING HERE OBEYS THAT. EK 9.10.A.2 says equilibrium
# arguments do not apply because the system is not at equilibrium. Every justification below
# is written in terms of distance from equilibrium or of the qualitative Nernst
# relationship, never as a shift in response to a stress, and the two items that mention Le
# Chatelier's principle at all do so in order to say that it does not apply.
#
# THE FIGURE PROBLEM. This bank carries no images. Every cell is described in words or
# carried as a table of concentrations, and no stem points at a picture.
#
# SCOPE. 9.9 owns the standard cell potential and its arithmetic, so no item here computes
# one from reduction potentials or uses the free energy equation. 9.11 owns Faraday's law,
# so no item computes a charge, a current or a mass.
#
# NOTATION. export_units.py does not typeset Chemistry; every span is hand-written and
# formulas in prose stay plain text.
TOPIC = ("9.10", "Cell Potential Under Nonstandard Conditions", 9)

_T_TRIALS = dict(
    headers=["Trial", "[X2+] (M)", "[Y2+] (M)"],
    rows=[["Trial 1", "0.50", "0.50"],
          ["Trial 2", "0.010", "1.0"],
          ["Trial 3", "1.0", "0.10"],
          ["Trial 4", "1.0", "0.010"]])

_T_CONC = dict(
    headers=["Cell", "Concentration in half-cell A (M)", "Concentration in half-cell B (M)"],
    rows=[["Cell 1", "0.10", "1.0"],
          ["Cell 2", "0.0010", "1.0"],
          ["Cell 3", "0.50", "0.50"]])

QUESTIONS = [

 dict(q="In a real system under nonstandard conditions, what does the framework say the cell "
        "potential varies with?",
      choices=[
        "The concentrations of the active species",
        "The mass of each of the two electrodes",
        "The total volume of solution in the two half-cells",
        "The salt chosen for the salt bridge",
        "Nothing, since the potential is a fixed property of the reaction"],
      ans=0,
      why="EK 9.10.A.1 states that in a real system under nonstandard conditions the cell "
          "potential will vary depending on the concentrations of the active species. The "
          "standard potential is the special case EK 9.10.A.3 attaches to a reaction "
          "quotient of 1."),

 dict(q="What does the framework say the cell potential IS, in relation to equilibrium?",
      choices=[
        "A driving force toward equilibrium",
        "A measure of how fast the cell reaction proceeds",
        "A measure of the total energy already delivered by the cell",
        "A property fixed by the temperature and nothing else",
        "A measure of how much charge has passed through the circuit"],
      ans=0,
      why="EK 9.10.A.1 calls the cell potential a driving force toward equilibrium, which is "
          "why the same statement makes its magnitude larger the farther the reaction sits "
          "from equilibrium. Speed is a kinetic question that Unit 5 rather than Unit 9 "
          "answers."),

 dict(q="How does the framework relate the magnitude of the cell potential to the distance "
        "from equilibrium?",
      choices=[
        "The farther the reaction is from equilibrium, the greater the magnitude",
        "The farther the reaction is from equilibrium, the smaller the magnitude",
        "The magnitude does not depend on the distance from equilibrium",
        "The magnitude is greatest exactly at equilibrium",
        "The magnitude depends only on the moles of electrons transferred"],
      ans=0,
      why="EK 9.10.A.1 states that the farther the reaction is from equilibrium, the greater "
          "the magnitude of the cell potential, and EK 9.10.A.3 completes the statement by "
          "putting the magnitude at zero once equilibrium is reached."),

 dict(q="What does the framework say about using equilibrium arguments such as Le "
        "Chatelier's principle on an electrochemical system?",
      choices=[
        "They do not apply, because such systems are not in equilibrium",
        "They apply, because the cell reaction is reversible",
        "They apply only while the cell is delivering current",
        "They apply only to concentration cells",
        "They apply once the cell potential has fallen to zero"],
      ans=0,
      why="EK 9.10.A.2 states that equilibrium arguments such as Le Chatelier's principle do "
          "not apply to electrochemical systems, because the systems are not in equilibrium. "
          "An operating cell is being driven toward equilibrium, which under EK 9.10.A.1 is "
          "precisely what gives it a potential."),

 dict(q="The standard cell potential corresponds to what value of the reaction quotient?",
      choices=["A reaction quotient of 1", "A reaction quotient of zero",
               "A reaction quotient equal to the equilibrium constant",
               "A reaction quotient larger than the equilibrium constant",
               "Any reaction quotient below 1"],
      ans=0,
      why="EK 9.10.A.3 opens by saying the standard cell potential corresponds to the "
          "standard conditions of a reaction quotient of 1. A quotient equal to the "
          "equilibrium constant is the other special case in the same statement, and it "
          "gives a potential of zero rather than the standard one."),

 dict(q="As an operating cell approaches equilibrium, what happens to the magnitude of its "
        "cell potential?",
      choices=[
        "It decreases, reaching zero at equilibrium",
        "It increases, reaching a maximum at equilibrium",
        "It stays at the standard value until equilibrium is reached",
        "It decreases to the standard value and stops there",
        "It changes in a way that cannot be predicted"],
      ans=0,
      why="EK 9.10.A.3 says that as the system approaches equilibrium the magnitude of the "
          "cell potential decreases, reaching zero at equilibrium. That is the same "
          "statement as EK 9.10.A.1's, read as the distance from equilibrium shrinks."),

 dict(q="A cell has run until its potential is zero. What is true of the reaction quotient?",
      choices=[
        "It equals the equilibrium constant, so the system is at equilibrium",
        "It equals 1, so the system is at standard conditions",
        "It equals zero, so no product remains",
        "It is larger than the equilibrium constant, so the reaction has overshot",
        "It cannot be known, since a potential of zero carries no information"],
      ans=0,
      why="EK 9.10.A.3 says the magnitude of the cell potential reaches zero at equilibrium, "
          "which is when the reaction quotient equals the equilibrium constant. A quotient "
          "of 1 is the standard condition, where the potential takes its standard value "
          "instead."),

 dict(q="A deviation from standard conditions takes a cell FARTHER from equilibrium than a "
        "reaction quotient of 1 would. What is the effect on the cell potential?",
      choices=[
        "Its magnitude increases relative to the standard value",
        "Its magnitude decreases relative to the standard value",
        "Its magnitude stays at the standard value",
        "Its magnitude falls to zero",
        "Its magnitude changes only if the temperature also changes"],
      ans=0,
      why="EK 9.10.A.3 states that deviations from standard conditions taking the cell "
          "further from equilibrium than a reaction quotient of 1 will increase the "
          "magnitude of the cell potential relative to the standard value, which is EK "
          "9.10.A.1's relationship between distance and magnitude applied to a comparison."),

 dict(q="A different deviation takes a cell CLOSER to equilibrium than a reaction quotient "
        "of 1 would. What is the effect on the cell potential?",
      choices=[
        "Its magnitude decreases relative to the standard value",
        "Its magnitude increases relative to the standard value",
        "Its magnitude stays at the standard value",
        "Its magnitude changes sign but keeps its size",
        "Its magnitude becomes independent of the concentrations"],
      ans=0,
      why="EK 9.10.A.3 states that deviations taking the cell closer to equilibrium than a "
          "reaction quotient of 1 will decrease the magnitude of the cell potential relative "
          "to the standard value. Nothing in the statement changes the sign; the sign turns "
          "only once the quotient passes the equilibrium constant."),

 dict(q="What does the framework say about algorithmic calculations using the Nernst "
        "equation?",
      choices=[
        "They are insufficient to demonstrate an understanding of cells under nonstandard "
        "conditions",
        "They are the only acceptable way to reason about nonstandard conditions",
        "They are required whenever the concentrations differ from the standard ones",
        "They are forbidden, so the equation itself is outside the course",
        "They are sufficient provided the temperature is stated"],
      ans=0,
      why="EK 9.10.A.4 says algorithmic calculations using the Nernst equation are "
          "insufficient to demonstrate an understanding, and asks instead that students "
          "qualitatively understand the effects of concentration and use conceptual "
          "reasoning, including the qualitative use of the equation."),

 dict(q="Which equation does the framework give for the cell potential under nonstandard "
        "conditions?",
      choices=[
        "\\( E = E^\\circ - \\frac{RT}{nF} \\ln Q \\)",
        "\\( E = E^\\circ + \\frac{RT}{nF} \\ln Q \\)",
        "\\( E = E^\\circ - \\frac{nF}{RT} \\ln Q \\)",
        "\\( E = E^\\circ - \\frac{RT}{nF} \\ln K \\)",
        "\\( E = -\\frac{RT}{nF} \\ln Q \\)"],
      ans=0,
      why="EK 9.10.A.4 gives the Nernst equation with the standard potential first and a "
          "term proportional to the logarithm of the reaction quotient SUBTRACTED from it. "
          "The subtraction is what makes the potential fall as the quotient rises, and the "
          "logarithm is of the quotient rather than of the equilibrium constant."),

 dict(q="A cell runs the reaction X(s) + Y2+(aq) gives X2+(aq) + Y(s), whose equilibrium "
        "constant is 100. The solutions are prepared with 0.50 M X2+ and 0.50 M Y2+. How "
        "does the cell potential compare with the standard cell potential?",
      choices=[
        "It equals the standard cell potential, because the reaction quotient is 1",
        "It is greater in magnitude than the standard cell potential",
        "It is smaller in magnitude than the standard cell potential",
        "It is zero, because the two concentrations are equal",
        "It cannot be compared without the temperature"],
      ans=0,
      why="EK 9.10.A.3 attaches the standard cell potential to the standard condition of a "
          "reaction quotient of 1, and the quotient for this reaction is the product ion "
          "concentration over the reactant ion concentration. Equal concentrations make that "
          "ratio 1 whatever their common value, so the cell sits at the standard point and "
          "not at equilibrium, which this constant places elsewhere."),

 dict(q="The same cell reaction, with the same equilibrium constant of 100, is instead "
        "prepared with 0.010 M X2+ and 1.0 M Y2+. How does the cell potential compare with "
        "the standard one?",
      choices=[
        "It is greater in magnitude, because the deviation takes the cell farther from "
        "equilibrium",
        "It is smaller in magnitude, because the deviation takes the cell farther from "
        "equilibrium",
        "It is greater in magnitude, because the deviation takes the cell closer to "
        "equilibrium",
        "It equals the standard cell potential, because only the ratio matters",
        "It is zero, because the reaction quotient is below 1"],
      ans=0,
      why="The reaction quotient here is far below 1 while the equilibrium constant is above "
          "1, so this preparation sits farther from equilibrium than the standard condition "
          "does. EK 9.10.A.3 says such a deviation increases the magnitude of the cell "
          "potential relative to the standard value, and EK 9.10.A.1 gives the reason: "
          "distance from equilibrium is what the potential measures."),

 dict(q="The same cell reaction, again with an equilibrium constant of 100, is prepared with "
        "1.0 M X2+ and 0.10 M Y2+. How does the cell potential compare with the standard one?",
      choices=[
        "It is smaller in magnitude, because the deviation takes the cell closer to "
        "equilibrium",
        "It is greater in magnitude, because the deviation takes the cell closer to "
        "equilibrium",
        "It is smaller in magnitude, because the deviation takes the cell farther from "
        "equilibrium",
        "It equals the standard cell potential, because the concentrations differ by a "
        "factor of ten",
        "It is zero, because the reaction quotient is above 1"],
      ans=0,
      why="The reaction quotient here lies between 1 and the equilibrium constant, so this "
          "preparation sits nearer to equilibrium than the standard condition does. EK "
          "9.10.A.3 says a deviation of that kind decreases the magnitude of the cell "
          "potential relative to the standard value, without taking it to zero, which "
          "happens only once the quotient reaches the constant."),

 dict(q="The same cell reaction, with an equilibrium constant of 100, is prepared with 1.0 M "
        "X2+ and 0.010 M Y2+. What is the cell potential?",
      choices=[
        "Zero, because the reaction quotient already equals the equilibrium constant",
        "Zero, because the reaction quotient already equals 1",
        "Equal to the standard cell potential, because the quotient equals the constant",
        "Greater in magnitude than the standard cell potential",
        "Smaller in magnitude than the standard cell potential, but not zero"],
      ans=0,
      why="EK 9.10.A.3 says the magnitude of the cell potential reaches zero at equilibrium, "
          "which is where the reaction quotient equals the equilibrium constant. Dividing "
          "the stated product ion concentration by the stated reactant ion concentration "
          "gives exactly the stated constant, so this cell has no driving force left under "
          "EK 9.10.A.1."),

 dict(q="The table gives four preparations of the cell reaction X(s) + Y2+(aq) gives "
        "X2+(aq) + Y(s), whose equilibrium constant is 100. In which trial does the cell "
        "potential equal the standard cell potential?",
      table=_T_TRIALS,
      choices=["Trial 1", "Trial 2", "Trial 3", "Trial 4", "In none of them"],
      ans=0,
      why="EK 9.10.A.3 attaches the standard cell potential to a reaction quotient of 1, and "
          "the quotient is the tabulated product ion concentration over the tabulated "
          "reactant ion concentration. Exactly one tabulated row gives a ratio of 1."),

 dict(q="Using the same four preparations, and the same equilibrium constant of 100, in "
        "which trial is the cell potential zero?",
      table=_T_TRIALS,
      choices=["Trial 4", "Trial 1", "Trial 2", "Trial 3", "In none of them"],
      ans=0,
      why="EK 9.10.A.3 puts the magnitude of the cell potential at zero when the reaction "
          "quotient equals the equilibrium constant. Exactly one tabulated row gives a ratio "
          "equal to the stated constant, and that cell has reached equilibrium."),

 dict(q="Among the same four preparations, still with an equilibrium constant of 100, which "
        "gives the cell potential of greatest magnitude?",
      table=_T_TRIALS,
      choices=["Trial 2", "Trial 1", "Trial 3", "Trial 4",
               "All four have the same magnitude"],
      ans=0,
      why="EK 9.10.A.1 makes the magnitude grow with the distance from equilibrium, and EK "
          "9.10.A.3 measures that distance by how far the reaction quotient sits from the "
          "equilibrium constant. One tabulated ratio is farther from the constant than any "
          "other, and farther than a ratio of 1 would be."),

 dict(q="Among the same four preparations, again with an equilibrium constant of 100, which "
        "gives a cell potential smaller in magnitude than the standard one without being "
        "zero?",
      table=_T_TRIALS,
      choices=["Trial 3", "Trial 1", "Trial 2", "Trial 4",
               "None of them, since only the standard condition matters"],
      ans=0,
      why="EK 9.10.A.3 says a deviation taking the cell closer to equilibrium than a "
          "reaction quotient of 1 decreases the magnitude of the potential relative to the "
          "standard value. Exactly one tabulated ratio lies between 1 and the stated "
          "equilibrium constant without reaching it."),

 dict(q="A concentration cell is built from two silver electrodes, each dipping into a "
        "silver nitrate solution, joined by a salt bridge. What is the STANDARD cell "
        "potential of such a cell?",
      choices=[
        "Zero, because the two half-reactions are the same and the standard condition makes "
        "the concentrations equal",
        "Zero, because silver has a standard reduction potential of zero",
        "Positive, because the cell delivers a potential when the concentrations differ",
        "Negative, because one half-cell must be driven",
        "It depends on which solution is placed in which half-cell"],
      ans=0,
      why="EK 9.10.A.3 ties the standard condition to a reaction quotient of 1, and for a "
          "cell whose two half-reactions are identical that means equal concentrations, at "
          "which the two half-cells offer nothing to each other. Any potential such a cell "
          "shows therefore comes entirely from the departure from that condition."),

 dict(q="In a concentration cell whose two half-cells hold the same metal ion at different "
        "concentrations, in which direction do electrons travel through the external wire?",
      choices=[
        "From the more dilute half-cell to the more concentrated one",
        "From the more concentrated half-cell to the more dilute one",
        "In whichever direction the salt bridge is oriented",
        "In neither direction, since the two half-reactions are the same",
        "In both directions equally, so no net current flows"],
      ans=0,
      why="EK 9.10.A.3 says that in concentration cells the direction of spontaneous "
          "electron flow can be determined by considering the direction needed to reach "
          "equilibrium, and equilibrium here is equal concentrations. Reaching it requires "
          "the dilute solution to gain ions, which happens where metal is oxidized, and the "
          "concentrated one to lose them, which happens where ions are reduced; EK 9.8.A.3 "
          "then sends the electrons from the first electrode to the second."),

 dict(q="As a concentration cell operates, what happens to the two concentrations?",
      choices=[
        "The dilute solution grows more concentrated and the concentrated one grows more "
        "dilute",
        "The dilute solution grows more dilute and the concentrated one grows more "
        "concentrated",
        "Both grow more concentrated as metal leaves the electrodes",
        "Both grow more dilute as metal plates onto the electrodes",
        "Neither changes, since the two half-reactions are the same"],
      ans=0,
      why="EK 9.10.A.3 says the direction of spontaneous electron flow in a concentration "
          "cell is the direction needed to reach equilibrium, and the equilibrium of two "
          "identical half-cells is equal concentrations. The cell therefore moves the two "
          "toward each other, which is the same approach to equilibrium EK 9.10.A.1 "
          "describes."),

 dict(q="When does a concentration cell stop delivering a potential?",
      choices=[
        "When the two concentrations have become equal",
        "When the more dilute solution has been used up entirely",
        "When both electrodes have the same mass",
        "When the reaction quotient reaches 1 rather than the equilibrium constant",
        "It never stops, since the two half-reactions are identical"],
      ans=0,
      why="For two identical half-cells the equilibrium state is equal concentrations, and "
          "EK 9.10.A.3 puts the magnitude of the cell potential at zero once equilibrium is "
          "reached. Here the reaction quotient of 1 and the equilibrium constant coincide, "
          "which is why the standard potential of such a cell is also zero."),

 dict(q="The table gives the concentrations in the two half-cells of three concentration "
        "cells built from the same metal. Which cell delivers the potential of greatest "
        "magnitude?",
      table=_T_CONC,
      choices=["Cell 2", "Cell 1", "Cell 3", "Cells 1 and 2 equally",
               "All three deliver the same potential"],
      ans=0,
      why="EK 9.10.A.1 makes the magnitude of the cell potential grow with the distance from "
          "equilibrium, and equilibrium for a concentration cell is equal concentrations. "
          "Comparing the tabulated ratios shows one cell whose two concentrations are "
          "farther apart than any other's."),

 dict(q="Using the same three concentration cells, which delivers no potential at all?",
      table=_T_CONC,
      choices=["Cell 3", "Cell 1", "Cell 2", "Cells 1 and 3 equally",
               "None of them, since every cell delivers something"],
      ans=0,
      why="A concentration cell is at equilibrium when its two concentrations are equal, and "
          "EK 9.10.A.3 puts the magnitude of the potential at zero there. Exactly one "
          "tabulated row has the same concentration in both half-cells."),

 dict(q="A student predicts the behaviour of an operating electrochemical cell by applying "
        "Le Chatelier's principle to it. What does the framework say about that method?",
      choices=[
        "It does not apply here, because an operating cell is not at equilibrium",
        "It applies here, because the cell reaction is reversible",
        "It applies here, but only to the half-cell where reduction occurs",
        "It applies here, provided the temperature is held constant",
        "It applies here, because the salt bridge keeps the system balanced"],
      ans=0,
      why="EK 9.10.A.2 states that equilibrium arguments such as Le Chatelier's principle do "
          "not apply to electrochemical systems, because the systems are not in equilibrium. "
          "EK 9.10.A.4 names the reasoning the framework does want in its place: qualitative "
          "use of the Nernst relationship and reasoning about distance from equilibrium."),

 dict(q="For a cell whose reaction is thermodynamically favored under standard conditions, "
        "some of the product species is added while the cell operates. Using the framework's "
        "equation qualitatively, what happens to the cell potential?",
      choices=[
        "It falls, because the reaction quotient rises and the equation subtracts a term "
        "proportional to its logarithm",
        "It rises, because the reaction quotient rises and the equation subtracts a term "
        "proportional to its logarithm",
        "It falls, because the reaction quotient falls and the equation adds a term "
        "proportional to its logarithm",
        "It is unchanged, because only the standard potential matters",
        "It falls to zero at once, because a product has been added"],
      ans=0,
      why="Adding product raises the reaction quotient, and EK 9.10.A.4's equation subtracts "
          "a term proportional to the logarithm of that quotient from the standard "
          "potential, so the potential falls. This is the qualitative use of the equation "
          "the framework asks for, rather than the equilibrium argument EK 9.10.A.2 rules "
          "out."),

 dict(q="Some of the reactant species is added instead to the same operating cell. Using the "
        "framework's equation qualitatively, what happens to the cell potential?",
      choices=[
        "It rises, because the reaction quotient falls and a smaller term is subtracted",
        "It falls, because the reaction quotient falls and a smaller term is subtracted",
        "It rises, because the reaction quotient rises and a larger term is subtracted",
        "It is unchanged, because adding a reactant cannot alter a potential",
        "It rises only until the reaction quotient reaches the equilibrium constant, then "
        "reverses"],
      ans=0,
      why="Adding reactant lowers the reaction quotient, and EK 9.10.A.4's equation "
          "subtracts a term proportional to its logarithm, so a smaller subtraction leaves a "
          "larger potential. The same conclusion follows from EK 9.10.A.1, since the cell "
          "has been moved farther from equilibrium."),

 dict(q="A cell reaction has an equilibrium constant of 0.010, so its standard cell potential "
        "is negative. The cell is prepared with a reaction quotient of 100. How does the "
        "magnitude of its potential compare with the standard one?",
      choices=[
        "It is greater, because a quotient of 100 is farther from the constant than a "
        "quotient of 1 is",
        "It is smaller, because a quotient of 100 is farther from the constant than a "
        "quotient of 1 is",
        "It is greater, because a quotient of 100 is nearer the constant than a quotient of "
        "1 is",
        "It is the same, because the standard potential is negative",
        "It is zero, because the quotient is above the equilibrium constant"],
      ans=0,
      why="EK 9.10.A.3's comparison is between the deviation and the standard condition, and "
          "it is made against the equilibrium constant rather than against 1. A quotient of "
          "100 sits four powers of ten from a constant of 0.010, where a quotient of 1 sits "
          "only two, so the deviation takes the cell farther from equilibrium and EK "
          "9.10.A.1 makes the magnitude larger."),

 dict(q="Which summary of the three special values of the reaction quotient matches the "
        "framework?",
      choices=[
        "At a quotient of 1 the potential is the standard one, at the equilibrium constant "
        "it is zero, and farther from the constant than 1 is the magnitude is larger",
        "At a quotient of 1 the potential is zero, at the equilibrium constant it is the "
        "standard one, and farther from the constant than 1 is the magnitude is larger",
        "At a quotient of 1 the potential is the standard one, at the equilibrium constant "
        "it is zero, and farther from the constant than 1 is the magnitude is smaller",
        "At a quotient of 1 the potential is zero, at the equilibrium constant it is also "
        "zero, and the magnitude never changes",
        "At a quotient of 1 the potential is the standard one, and the potential is "
        "unchanged at every other quotient"],
      ans=0,
      why="EK 9.10.A.3 states all three in one passage: the standard cell potential "
          "corresponds to a reaction quotient of 1, the magnitude reaches zero at "
          "equilibrium where the quotient equals the equilibrium constant, and a deviation "
          "farther from equilibrium than a quotient of 1 increases the magnitude relative to "
          "the standard value."),

]
