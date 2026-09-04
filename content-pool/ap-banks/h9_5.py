# AP CHEMISTRY 9.5 Free Energy and Equilibrium
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.5.A: explain whether a process is thermodynamically favored using
# the relationships between the equilibrium constant, the standard free energy change,
# and the temperature.
# Suggested skill 6.D, provide reasoning to justify a claim using chemical principles or
# laws, or using mathematical justification.
#
# Essential knowledge relied on, in the framework's own words:
#   9.5.A.1  The phrase "thermodynamically favored" (standard free energy change below
#            zero) means that the products are favored at equilibrium (K greater than 1)
#            under standard conditions.
#   9.5.A.2  The equilibrium constant is related to free energy by the equations
#            EQN: K equals e raised to the negative standard free energy change over RT
#            and
#            EQN: the standard free energy change equals minus RT times the natural
#            logarithm of K.
#   9.5.A.3  Connections between K and the standard free energy change can be made
#            qualitatively through estimation. When the standard free energy change is
#            near zero, the equilibrium constant will be close to 1. When it is much
#            larger or much smaller than RT, the value of K deviates strongly from 1.
#   9.5.A.4  Processes with a standard free energy change below zero favor products
#            (K greater than 1) and those with one above zero favor reactants
#            (K less than 1).
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 9.3 AND 9.9, all three of which relate the free
# energy change to something else. 9.3 asks what the free energy change IS and where it
# comes from; 9.9 asks how it relates to a cell potential. Everything below asks about
# the POSITION OF EQUILIBRIUM: which side is favored, how far K sits from 1, and what RT
# has to do with judging "how far". No item here computes a free energy change from an
# enthalpy and an entropy, and verify_h9_5.py asserts that.
#
# THE SWAP GUARD. EK 9.5.A.4 pairs a free energy change below zero with K above 1. A key
# that paired them the other way round would read perfectly well, so verify_h9_5.py
# reads the sign and the K clause out of each such key as two separately named facts and
# requires them to agree.
#
# ARITHMETIC. RT is given in the stem wherever it is needed, so every calculation is one
# multiplication and is recomputed in the verifier from the stem alone.
#
# NO FIGURES.
TOPIC = ("9.5", "Free Energy and Equilibrium", 9)

_KCOL = "Equilibrium constant at 300 K"
_GCOL = "Standard free energy change, kJ/mol"

_T_K = dict(
    headers=["Reaction", _KCOL],
    rows=[["1", "1500"],
          ["2", "0.004"],
          ["3", "1.0"],
          ["4", "25"]])

_T_G = dict(
    headers=["Process", _GCOL],
    rows=[["P", "-30.0"],
          ["Q", "+15.0"],
          ["R", "-5.0"],
          ["S", "0.0"]])

QUESTIONS = [

 dict(q="What does the phrase thermodynamically favored mean about the position of "
        "equilibrium under standard conditions?",
      choices=[
        "The products are favored at equilibrium, so the equilibrium constant is greater "
        "than 1",
        "The reactants are favored at equilibrium, so the equilibrium constant is greater "
        "than 1",
        "The reaction goes entirely to products, leaving no reactants at all",
        "The equilibrium constant is exactly 1, so neither side is favored",
        "The reaction reaches equilibrium faster than an unfavored one would"],
      ans=0,
      why="EK 9.5.A.1 states that the phrase thermodynamically favored means the products "
          "are favored at equilibrium under standard conditions, with an equilibrium "
          "constant greater than 1. Favored is a statement about the position of "
          "equilibrium, not about going to completion."),

 dict(q="Which equation does the framework give for the standard free energy change in "
        "terms of the equilibrium constant?",
      choices=[
        "\\( \\Delta G^\\circ = -RT \\ln K \\)",
        "\\( \\Delta G^\\circ = RT \\ln K \\)",
        "\\( \\Delta G^\\circ = -RT \\ln Q \\)",
        "\\( \\Delta G^\\circ = -R \\ln K \\)",
        "\\( \\Delta G^\\circ = -\\frac{RT}{\\ln K} \\)"],
      ans=0,
      why="EK 9.5.A.2 gives this equation directly. Dropping the temperature or dividing "
          "by the logarithm instead of multiplying by it changes the units as well as the "
          "value, and the minus sign is what makes a large constant correspond to a "
          "negative free energy change."),

 dict(q="Which equation does the framework give for the equilibrium constant in terms of "
        "the standard free energy change?",
      choices=[
        "\\( K = e^{-\\Delta G^\\circ / RT} \\)",
        "\\( K = e^{\\Delta G^\\circ / RT} \\)",
        "\\( K = e^{-RT / \\Delta G^\\circ} \\)",
        "\\( K = -RT \\ln \\Delta G^\\circ \\)",
        "\\( K = -\\Delta G^\\circ / RT \\)"],
      ans=0,
      why="EK 9.5.A.2 gives the exponential form alongside the logarithmic one, and the "
          "two are the same relationship rearranged. Putting RT on top of the fraction, "
          "or dropping the exponential altogether, gives a quantity that does not even "
          "have the right behaviour as the free energy change passes through zero."),

 dict(q="A process has a standard free energy change below zero. What follows about the "
        "equilibrium constant under standard conditions?",
      choices=[
        "The equilibrium constant is greater than 1, and products are favored at "
        "equilibrium",
        "The equilibrium constant is less than 1, and reactants are favored at equilibrium",
        "The equilibrium constant is exactly 1, and neither side is favored",
        "The equilibrium constant is greater than 1, and reactants are favored at "
        "equilibrium",
        "The equilibrium constant cannot be inferred without the temperature"],
      ans=0,
      why="EK 9.5.A.4 states that processes with a standard free energy change below zero "
          "favor products, which is an equilibrium constant greater than 1. The pairing "
          "runs one way only, and the option that keeps the constant but swaps the side "
          "favored contradicts what a constant greater than 1 means."),

 dict(q="A process has a standard free energy change above zero. What follows about the "
        "equilibrium constant under standard conditions?",
      choices=[
        "The equilibrium constant is less than 1, and reactants are favored at equilibrium",
        "The equilibrium constant is greater than 1, and products are favored at "
        "equilibrium",
        "The equilibrium constant is exactly 1, and neither side is favored",
        "The equilibrium constant is negative, since the free energy change is positive",
        "The equilibrium constant is less than 1, and products are favored at equilibrium"],
      ans=0,
      why="EK 9.5.A.4 states that processes with a standard free energy change above zero "
          "favor reactants, which is an equilibrium constant less than 1. An equilibrium "
          "constant is never negative, whatever the sign of the free energy change."),

 dict(q="A process has a standard free energy change very near zero. What does the "
        "framework's qualitative estimation give for the equilibrium constant?",
      choices=[
        "It will be close to 1",
        "It will be very much greater than 1",
        "It will be very much less than 1",
        "It will be exactly zero",
        "It cannot be estimated without the exact value"],
      ans=0,
      why="EK 9.5.A.3 states that when the standard free energy change is near zero the "
          "equilibrium constant will be close to 1, and that this connection can be made "
          "qualitatively through estimation rather than by exact calculation."),

 dict(q="A process has a standard free energy change whose size is many times RT. What "
        "does the framework's estimation give for the equilibrium constant?",
      choices=[
        "It deviates strongly from 1",
        "It sits close to 1, since RT is small",
        "It is exactly 1, since the two quantities cancel",
        "It is negative, because the free energy change is large",
        "It cannot be estimated unless the sign of the free energy change is unknown"],
      ans=0,
      why="EK 9.5.A.3 states that when the standard free energy change is much larger or "
          "much smaller than RT, the value of K deviates strongly from 1. RT is the scale "
          "the comparison is made against, so a change many times its size is a large "
          "change in the sense that matters."),

 dict(q="At a temperature where \\( RT = 2.5 \\) kJ/mol, a reaction has \\( \\ln K = 4.0 "
        "\\). What is its standard free energy change?",
      choices=[
        "\\( -10.0 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +10.0 \\) kJ/mol, and the equilibrium constant is less than 1",
        "\\( -1.6 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +1.6 \\) kJ/mol, and the equilibrium constant is less than 1",
        "\\( -4.0 \\) kJ/mol, and the equilibrium constant is greater than 1"],
      ans=0,
      why="EK 9.5.A.2's logarithmic equation multiplies RT by the natural logarithm of the "
          "constant and reverses the sign, so a positive logarithm gives a negative free "
          "energy change. Dividing by RT instead of multiplying, or leaving RT out "
          "altogether, gives the other magnitudes offered."),

 dict(q="A reaction has \\( \\ln K = -8.0 \\) at a temperature where \\( RT = 2.5 \\) "
        "kJ/mol. What is its standard free energy change?",
      choices=[
        "\\( +20.0 \\) kJ/mol, and the equilibrium constant is less than 1",
        "\\( -20.0 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +3.2 \\) kJ/mol, and the equilibrium constant is less than 1",
        "\\( -3.2 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +8.0 \\) kJ/mol, and the equilibrium constant is less than 1"],
      ans=0,
      why="EK 9.5.A.2's equation turns a negative logarithm into a positive free energy "
          "change, and EK 9.5.A.4 makes such a process one that favors reactants, so the "
          "constant is below 1. A logarithm below zero belongs to a constant below 1."),

 dict(q="For a reaction with \\( \\ln K = 0 \\) at a temperature where \\( RT = 2.5 \\) "
        "kJ/mol, what is the standard free energy change?",
      choices=[
        "\\( 0.0 \\) kJ/mol, and the equilibrium constant is exactly 1",
        "\\( +2.5 \\) kJ/mol, and the equilibrium constant is less than 1",
        "\\( -2.5 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +1.0 \\) kJ/mol, and the equilibrium constant is less than 1",
        "The free energy change cannot be found from a logarithm of zero"],
      ans=0,
      why="EK 9.5.A.2's equation multiplies RT by a logarithm of zero, giving zero "
          "whatever RT is, and a logarithm of zero belongs to a constant of exactly 1. "
          "This is the boundary EK 9.5.A.4 draws between the two cases rather than a "
          "failure of the relationship."),

 dict(q="At a higher temperature, where \\( RT = 5.0 \\) kJ/mol, a reaction has \\( \\ln K "
        "= 4.0 \\). What is its standard free energy change?",
      choices=[
        "\\( -20.0 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +20.0 \\) kJ/mol, and the equilibrium constant is less than 1",
        "\\( -10.0 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( -0.8 \\) kJ/mol, and the equilibrium constant is greater than 1",
        "\\( +0.8 \\) kJ/mol, and the equilibrium constant is less than 1"],
      ans=0,
      why="EK 9.5.A.2's equation carries RT as a factor, so the same logarithm at twice "
          "the value of RT gives twice the free energy change. The value belonging to the "
          "smaller RT is offered as well, and it is the one a student gets by reusing the "
          "earlier temperature."),

 dict(q="A reaction has a standard free energy change of \\( -25.0 \\) kJ/mol at a "
        "temperature where \\( RT = 2.5 \\) kJ/mol. What is the natural logarithm of its "
        "equilibrium constant?",
      choices=["\\( \\ln K = +10.0 \\)", "\\( \\ln K = -10.0 \\)",
               "\\( \\ln K = +62.5 \\)", "\\( \\ln K = -62.5 \\)",
               "\\( \\ln K = +2.5 \\)"],
      ans=0,
      why="EK 9.5.A.2's equation rearranges to give the logarithm as the free energy "
          "change divided by RT with the sign reversed, so a negative free energy change "
          "gives a positive logarithm and a constant above 1. Multiplying instead of "
          "dividing gives the very large values offered."),

 dict(q="Another reaction has a standard free energy change of \\( +7.5 \\) kJ/mol where "
        "\\( RT = 2.5 \\) kJ/mol. What is the natural logarithm of its equilibrium "
        "constant?",
      choices=["\\( \\ln K = -3.0 \\)", "\\( \\ln K = +3.0 \\)",
               "\\( \\ln K = -18.75 \\)", "\\( \\ln K = +18.75 \\)",
               "\\( \\ln K = -7.5 \\)"],
      ans=0,
      why="EK 9.5.A.2's equation gives a negative logarithm for a positive free energy "
          "change, and EK 9.5.A.4 makes such a process one that favors reactants. A "
          "negative logarithm belongs to a constant below 1, which is what favoring "
          "reactants means."),

 dict(q="The table gives equilibrium constants for four reactions at 300 K. Which "
        "reaction favors its products most strongly?",
      table=_T_K,
      choices=["Reaction 1", "Reaction 2", "Reaction 3", "Reaction 4",
               "Reactions 1 and 4 equally"],
      ans=0,
      why="EK 9.5.A.4 makes an equilibrium constant greater than 1 the mark of a process "
          "favoring products, and the larger the constant the further the position of "
          "equilibrium lies toward them. The largest tabulated constant is much the "
          "largest."),

 dict(q="Using the same table of equilibrium constants, which reaction favors its "
        "reactants?",
      table=_T_K,
      choices=["Reaction 2", "Reaction 1", "Reaction 3", "Reaction 4",
               "None of the four reactions"],
      ans=0,
      why="EK 9.5.A.4 makes an equilibrium constant less than 1 the mark of a process "
          "favoring reactants, and exactly one tabulated constant is below 1."),

 dict(q="Using the tabulated constants once more, which reaction has a standard free "
        "energy change of exactly zero?",
      table=_T_K,
      choices=["Reaction 3", "Reaction 1", "Reaction 2", "Reaction 4",
               "None, since a free energy change is never exactly zero"],
      ans=0,
      why="EK 9.5.A.2's equation makes the free energy change the product of RT and the "
          "natural logarithm of the constant, with the sign reversed, and that logarithm "
          "is zero exactly when the constant is 1. One tabulated constant is 1."),

 dict(q="Using the tabulated constants again, which reactions are thermodynamically "
        "favored under standard conditions?",
      table=_T_K,
      choices=[
        "Reactions 1 and 4, whose constants are greater than 1",
        "Reactions 2 and 3, whose constants are greater than 1",
        "Reaction 1 alone, since its constant is much the largest",
        "Reactions 1, 3 and 4, since none of their constants is below 1",
        "All four, since every reaction reaches an equilibrium"],
      ans=0,
      why="EK 9.5.A.1 ties thermodynamic favorability to an equilibrium constant greater "
          "than 1 under standard conditions, and a constant of exactly 1 is not greater "
          "than 1, so the row at the boundary is excluded along with the one below it."),

 dict(q="The table gives standard free energy changes for four processes. Which has the "
        "largest equilibrium constant?",
      table=_T_G,
      choices=["Process P", "Process Q", "Process R", "Process S",
               "Processes P and R equally"],
      ans=0,
      why="EK 9.5.A.2's equation makes the logarithm of the constant the free energy "
          "change divided by RT with the sign reversed, so the most negative tabulated "
          "free energy change belongs to the largest constant."),

 dict(q="Using the same table of free energy changes, which process has an equilibrium "
        "constant of exactly 1?",
      table=_T_G,
      choices=["Process S", "Process P", "Process Q", "Process R",
               "None of the four processes"],
      ans=0,
      why="EK 9.5.A.2's equation gives a logarithm of zero when the free energy change is "
          "zero, and a logarithm of zero belongs to a constant of exactly 1. One "
          "tabulated value is zero."),

 dict(q="Using the tabulated free energy changes once more, which process favors its "
        "reactants at equilibrium?",
      table=_T_G,
      choices=["Process Q", "Process P", "Process R", "Process S",
               "Processes Q and S together"],
      ans=0,
      why="EK 9.5.A.4 states that processes with a standard free energy change above zero "
          "favor reactants, and exactly one tabulated value is above zero. A value of "
          "zero favors neither side."),

 dict(q="Among the tabulated processes that favor their products, which has the "
        "equilibrium constant closest to 1?",
      table=_T_G,
      choices=["Process R", "Process P", "Process Q", "Process S",
               "Processes P and R are equally close"],
      ans=0,
      why="EK 9.5.A.3 makes a free energy change near zero correspond to a constant close "
          "to 1, so among the tabulated processes that favor products the one with the "
          "smaller size of free energy change is the nearer to 1. The process at exactly "
          "zero does not favor products at all."),

 dict(q="What role does RT play in the framework's qualitative comparison between the free "
        "energy change and the equilibrium constant?",
      choices=[
        "It is the scale against which the size of the free energy change is judged",
        "It is the smallest free energy change that can be measured",
        "It is the value the free energy change takes at equilibrium",
        "It is the equilibrium constant expressed in units of energy",
        "It is the temperature at which the constant equals 1"],
      ans=0,
      why="EK 9.5.A.3 says the constant deviates strongly from 1 when the free energy "
          "change is much larger or much smaller than RT, so RT supplies the standard of "
          "comparison. Without it, calling a free energy change large or small would mean "
          "nothing."),

 dict(q="To what does the framework attach the qualification under standard conditions in "
        "its statement about favorability and the equilibrium constant?",
      choices=[
        "To the claim that a favored process has its products favored at equilibrium",
        "To the definition of the natural logarithm used in the equation",
        "To the requirement that the temperature be exactly 298 K",
        "To the claim that the equilibrium constant is always positive",
        "To the rule that RT is measured in kilojoules per mole"],
      ans=0,
      why="EK 9.5.A.1 attaches the phrase to the statement that thermodynamically favored "
          "means the products are favored at equilibrium, since the standard free energy "
          "change is defined for the standard state EK 9.3.A.1 sets out."),

 dict(q="At a temperature where \\( RT = 2.5 \\) kJ/mol, a process has a standard free "
        "energy change of \\( -0.5 \\) kJ/mol. What does estimation give for its "
        "equilibrium constant?",
      choices=[
        "A little above 1, since the free energy change is small compared with RT",
        "Very much above 1, since the free energy change is below zero",
        "A little below 1, since the free energy change is small compared with RT",
        "Exactly 1, since the free energy change is small",
        "Very much below 1, since the free energy change is small"],
      ans=0,
      why="EK 9.5.A.3 makes a free energy change near zero correspond to a constant close "
          "to 1, and EK 9.5.A.4 puts a change below zero on the side of the products, so "
          "the constant is a little above 1 rather than far from it in either direction."),

 dict(q="At the same temperature, where \\( RT = 2.5 \\) kJ/mol, a process has a standard "
        "free energy change of \\( -60.0 \\) kJ/mol. What does estimation give for its "
        "equilibrium constant?",
      choices=[
        "Very much greater than 1, since the free energy change is many times RT",
        "A little greater than 1, since the free energy change is below zero",
        "Very much less than 1, since the free energy change is large",
        "Close to 1, since RT is small compared with the free energy change",
        "Exactly 1, because a large free energy change cancels against RT"],
      ans=0,
      why="EK 9.5.A.3 says the constant deviates strongly from 1 when the free energy "
          "change is much larger or much smaller than RT, and EK 9.5.A.4 places a change "
          "below zero on the side of the products, so the deviation is upward."),

 dict(q="Two processes at the same temperature have standard free energy changes of \\( "
        "-5.0 \\) kJ/mol and \\( -50.0 \\) kJ/mol. Which has the larger equilibrium "
        "constant?",
      choices=[
        "The one whose free energy change is more negative",
        "The one whose free energy change is less negative",
        "They have equal constants, since both are below zero",
        "Neither, since both constants are below 1",
        "The comparison cannot be made without the value of RT"],
      ans=0,
      why="EK 9.5.A.2's equation makes the logarithm of the constant proportional to the "
          "free energy change with the sign reversed, so at one temperature the more "
          "negative change gives the larger logarithm and hence the larger constant. Both "
          "are above 1 under EK 9.5.A.4."),

 dict(q="A reaction is written in reverse, so its standard free energy change changes "
        "sign. What happens to its equilibrium constant, according to the framework's "
        "equation?",
      choices=[
        "The logarithm of the constant changes sign, so the constant becomes its reciprocal",
        "The constant changes sign as well, becoming negative",
        "The constant is unchanged, since it is a constant",
        "The constant is reduced by the value of RT",
        "The constant becomes exactly 1, since the two directions balance"],
      ans=0,
      why="EK 9.5.A.2 makes the logarithm of the constant the free energy change divided "
          "by RT with the sign reversed, so reversing the sign of the change reverses the "
          "sign of the logarithm, and a logarithm of the opposite sign belongs to the "
          "reciprocal constant. A constant is never negative."),

 dict(q="Suppose the standard free energy change of a process were the same at a higher "
        "temperature. What would happen to the natural logarithm of its equilibrium "
        "constant?",
      choices=[
        "Its size would fall, because RT is larger, so the constant moves toward 1",
        "Its size would rise, because RT is larger, so the constant moves away from 1",
        "It would be unchanged, because the free energy change is unchanged",
        "It would change sign, because the temperature appears with a minus sign",
        "It would fall to zero, because RT grows without limit"],
      ans=0,
      why="EK 9.5.A.2's equation divides the free energy change by RT to give the "
          "logarithm, so a larger RT with the same numerator gives a logarithm of smaller "
          "size, and EK 9.5.A.3 reads a small logarithm as a constant near 1. The "
          "supposition that the change itself stays fixed is what isolates the effect."),

 dict(q="By what means does the framework say connections between the equilibrium constant "
        "and the standard free energy change can be made?",
      choices=[
        "Qualitatively, through estimation",
        "Only by exact calculation with a calculator",
        "Only by measuring the constant experimentally first",
        "By assuming the constant is always close to 1",
        "By comparing the free energy change with the activation energy"],
      ans=0,
      why="EK 9.5.A.3 opens by saying that connections between K and the standard free "
          "energy change can be made qualitatively through estimation, which is why the "
          "topic asks for reasoning rather than for exact numerical answers."),

 dict(q="Which pairing of a standard free energy change with an equilibrium constant does "
        "the framework endorse?",
      choices=[
        "A change below zero with a constant above 1, and a change above zero with a "
        "constant below 1",
        "A change below zero with a constant below 1, and a change above zero with a "
        "constant above 1",
        "A change below zero with a constant below 1, and a change above zero with a "
        "constant below 1",
        "Either pairing, depending on the temperature chosen",
        "Neither pairing, since the two quantities are independent"],
      ans=0,
      why="EK 9.5.A.4 states that processes with a standard free energy change below zero "
          "favor products, meaning a constant greater than 1, and those above zero favor "
          "reactants, meaning a constant less than 1. The pairing is fixed by the minus "
          "sign in EK 9.5.A.2's equation and does not depend on the temperature."),

]
