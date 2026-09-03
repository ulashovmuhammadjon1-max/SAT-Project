# AP CHEMISTRY 7.6 Properties of the Equilibrium Constant
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.6.A: represent a multistep process with an overall equilibrium
# expression, using the constituent K expressions for each individual reaction.
# Suggested skill 5.A, identify quantities needed to solve a problem from given
# information.
#
# Essential knowledge relied on, in the framework's own words:
#   7.6.A.1  When a reaction is reversed, K is inverted.
#   7.6.A.2  When the stoichiometric coefficients of a reaction are multiplied by a
#            factor c, K is raised to the power c.
#   7.6.A.3  When reactions are added together, the K of the resulting overall reaction
#            is the product of the K's for the reactions that were summed.
#   7.6.A.4  Since the expressions for K and Q have identical mathematical forms, all
#            valid algebraic manipulations of K also apply to Q.
#
# SCOPE, so this topic does not reach into its neighbours. 7.3 owns the FORM of the
# reaction quotient and what is left out of it; 7.4 owns obtaining K from measured
# equilibrium concentrations; 7.5 owns what a large or small K says about the extent of
# reaction; 7.7 owns solving for equilibrium concentrations. Everything below is one of
# the four algebraic properties above and nothing else.
#
# ARITHMETIC. Every value is exact in one or two calculator-free steps and is recomputed
# in verify_h7_6.py from the stimulus alone.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span below is
# hand-written. A chemical formula in prose stays plain text (N2O4, SO3), and a reaction
# arrow is written as the word "to" so no glyph is left outside a span.
TOPIC = ("7.6", "Properties of the Equilibrium Constant", 7)

_T_STEPS = dict(
    headers=["Step", "Equation", "Equilibrium constant at 298 K"],
    rows=[["1", "A(g) + B(g) to C(g)", "4.0"],
          ["2", "C(g) + B(g) to D(g)", "5.0"],
          ["3", "D(g) to E(g) + B(g)", "2.0"]])

_T_NITROGEN = dict(
    headers=["Reaction", "Equation", "Equilibrium constant at 500 K"],
    rows=[["I", "N2(g) + O2(g) to 2 NO(g)", "0.0050"],
          ["II", "2 NO(g) + O2(g) to 2 NO2(g)", "400"]])

_T_HALIDES = dict(
    headers=["Reaction", "Equation", "Equilibrium constant"],
    rows=[["I", "H2(g) + Cl2(g) to 2 HCl(g)", "9.0"],
          ["II", "H2(g) + Br2(g) to 2 HBr(g)", "3.0"],
          ["III", "H2(g) + I2(g) to 2 HI(g)", "0.50"]])

_T_QUOTIENT = dict(
    headers=["Time", "Reaction quotient Q for the forward reaction"],
    rows=[["5 minutes", "0.50"],
          ["10 minutes", "0.25"],
          ["15 minutes", "0.20"]])

QUESTIONS = [

 dict(q="At a certain temperature the reaction N2O4(g) to 2 NO2(g) has an equilibrium "
        "constant of 4.0. What is the equilibrium constant, at that same temperature, "
        "for the reverse reaction 2 NO2(g) to N2O4(g)?",
      choices=["K = 0.25", "K = 4.0", "K = 2.0", "K = 8.0", "K = 16"],
      ans=0,
      why="EK 7.6.A.1 states that when a reaction is reversed, K is inverted. The "
          "reciprocal of 4.0 is 0.25. The other values come from leaving K unchanged, "
          "taking a square root, doubling, or squaring, none of which is a reversal."),

 dict(q="A student writes an equation backwards by mistake and reports an equilibrium "
        "constant of \\( 1.0 \\times 10^{3} \\) for it. If the equation had been written "
        "in the intended direction instead, what equilibrium constant would the same "
        "data give?",
      choices=["\\( 1.0 \\times 10^{-3} \\)",
               "\\( 1.0 \\times 10^{3} \\)",
               "\\( 1.0 \\times 10^{6} \\)",
               "\\( 2.0 \\times 10^{3} \\)",
               "\\( 1.0 \\times 10^{-6} \\)"],
      ans=0,
      why="EK 7.6.A.1: reversing the reaction inverts K, and the reciprocal of ten cubed "
          "is ten to the negative third. Squaring the reciprocal, which gives ten to the "
          "negative sixth, belongs to a change of coefficients under EK 7.6.A.2 and not "
          "to a reversal."),

 dict(q="For the reaction N2(g) + 3 H2(g) to 2 NH3(g) the equilibrium constant is 3.0. "
        "What is the equilibrium constant for 2 N2(g) + 6 H2(g) to 4 NH3(g) at the same "
        "temperature?",
      choices=["K = 9.0", "K = 6.0", "K = 3.0", "K = 1.5", "K = 0.33"],
      ans=0,
      why="Every coefficient has been multiplied by a factor of two, so EK 7.6.A.2 "
          "raises K to the power two: three squared is nine. Doubling K itself would "
          "give six, which is the error the framework's power rule exists to prevent."),

 dict(q="The equilibrium constant for the reaction 2 HI(g) to H2(g) + I2(g) is 16. What "
        "is the equilibrium constant for the equation obtained by halving every "
        "coefficient in it?",
      choices=["K = 4.0", "K = 8.0", "K = 16", "K = 32", "K = 256"],
      ans=0,
      why="The coefficients have been multiplied by one half, so EK 7.6.A.2 raises K to "
          "the power one half, which is the square root: the square root of sixteen is "
          "four. Halving K itself would give eight, and squaring it would give 256."),

 dict(q="An equation is rewritten with every stoichiometric coefficient multiplied by "
        "three. Its equilibrium constant was 2.0 before the rewrite. What is it "
        "afterwards?",
      choices=["K = 8.0", "K = 6.0", "K = 2.0", "K = 0.13", "K = 0.50"],
      ans=0,
      why="EK 7.6.A.2 states that multiplying the coefficients by a factor c raises K to "
          "the power c, so K becomes two cubed, which is eight. Multiplying K by three "
          "instead would give six, and inverting it would give one half."),

 dict(q="Two reactions are added to give an overall reaction. The first has an "
        "equilibrium constant of 2.0 and the second has an equilibrium constant of 5.0. "
        "What is the equilibrium constant of the overall reaction?",
      choices=["K = 10", "K = 7.0", "K = 2.5", "K = 0.40", "K = 3.0"],
      ans=0,
      why="EK 7.6.A.3 states that when reactions are added, the K of the overall "
          "reaction is the product of the individual K values, so two times five is ten. "
          "Adding the constants would give seven, which is the mistake the framework "
          "rules out by specifying a product."),

 dict(q="Three steps are summed to give one overall equation. Using the table, what is "
        "the equilibrium constant of that overall equation?",
      table=_T_STEPS,
      choices=["K = 40", "K = 11", "K = 2.5", "K = 0.025", "K = 20"],
      ans=0,
      why="EK 7.6.A.3 makes the overall K the product of the summed steps' constants, "
          "and four times five times two is forty. Summing the three constants would "
          "give eleven, and inverting the product would give 0.025."),

 dict(q="A reaction has an equilibrium constant of 2.0. It is first reversed, and then "
        "every coefficient in the reversed equation is doubled. What is the equilibrium "
        "constant of the final equation?",
      choices=["K = 0.25", "K = 0.50", "K = 4.0", "K = 1.0", "K = 16"],
      ans=0,
      why="EK 7.6.A.1 inverts K on reversal, giving one half, and EK 7.6.A.2 then raises "
          "that to the power two, giving one quarter. Stopping after the reversal gives "
          "one half; applying only the doubling gives four."),

 dict(q="Reaction Y is subtracted from reaction X, which is the same as reversing "
        "reaction Y and adding it to reaction X. Reaction X has an equilibrium constant "
        "of 12 and reaction Y has an equilibrium constant of 3.0. What is the "
        "equilibrium constant of the resulting equation?",
      choices=["K = 4.0", "K = 36", "K = 9.0", "K = 15", "K = 0.25"],
      ans=0,
      why="Reversing Y inverts its constant to one third under EK 7.6.A.1, and EK "
          "7.6.A.3 then multiplies: twelve times one third is four. Multiplying the two "
          "constants directly would give 36, and subtracting them would give nine."),

 dict(q="Which of the following correctly states what happens to the numerical value of "
        "an equilibrium constant when the equation it describes is written in reverse?",
      choices=[
        "It becomes the reciprocal of the original value, because the products and the "
        "reactants trade places in the expression.",
        "It becomes the negative of the original value, because the direction of the "
        "reaction has changed sign.",
        "It is unchanged, because the same chemical species are present on both sides "
        "of the equation either way.",
        "It is squared, because both the numerator and the denominator of the "
        "expression are affected by the change.",
        "It becomes zero, because a reaction written in reverse cannot reach "
        "equilibrium under the same conditions."],
      ans=0,
      why="EK 7.6.A.1 states that K is inverted when a reaction is reversed. The reason "
          "is structural: the concentrations that stood in the numerator now stand in "
          "the denominator, so the new value is the reciprocal of the old one."),

 dict(q="A student asks whether the algebraic rules for combining equilibrium constants "
        "also apply to reaction quotients. Which response is best supported by the "
        "course framework?",
      choices=[
        "They apply to Q as well, because the expressions for K and Q have identical "
        "mathematical forms.",
        "They apply only to K, because Q is measured away from equilibrium and so obeys "
        "different algebra.",
        "They apply only to Q, because K is fixed by temperature and cannot be "
        "manipulated at all.",
        "They apply to neither, because both quantities must be measured directly for "
        "every new equation.",
        "They apply to Q only at the instant when Q happens to be numerically equal to "
        "K for that equation."],
      ans=0,
      why="EK 7.6.A.4 states that since the expressions for K and Q have identical "
          "mathematical forms, all valid algebraic manipulations of K also apply to Q. "
          "The rules follow from the shape of the expression, not from whether the "
          "system happens to be at equilibrium."),

 dict(q="Using the table, what is the equilibrium constant for the overall reaction "
        "N2(g) + 2 O2(g) to 2 NO2(g), obtained by adding reactions I and II?",
      table=_T_NITROGEN,
      choices=["K = 2.0", "K = 400", "K = 80,000", "K = 0.50", "K = 0.0020"],
      ans=0,
      why="Adding the two equations cancels the 2 NO(g) that is a product of the first "
          "and a reactant of the second, giving the overall equation, so EK 7.6.A.3 "
          "makes the overall constant the product: 0.0050 times 400 is 2.0. Keeping only "
          "the larger constant gives 400 and dividing one by the other gives 80,000."),

 dict(q="An overall reaction is the sum of two steps and has an equilibrium constant of "
        "60. The first step has an equilibrium constant of 12. What is the equilibrium "
        "constant of the second step?",
      choices=["K = 5.0", "K = 48", "K = 0.20", "K = 72", "K = 12"],
      ans=0,
      why="EK 7.6.A.3 makes the overall constant the product of the two steps, so the "
          "unknown constant is sixty divided by twelve, which is five. Subtracting gives "
          "48, and treating the rule as an addition rather than a product is what "
          "produces that value."),

 dict(q="The formation of a certain complex ion has an equilibrium constant of \\( 5.0 "
        "\\times 10^{8} \\). Which statement about the reverse reaction, the "
        "dissociation of that complex ion, is correct?",
      choices=[
        "Its equilibrium constant is \\( 2.0 \\times 10^{-9} \\), the reciprocal of the "
        "formation constant.",
        "Its equilibrium constant is also \\( 5.0 \\times 10^{8} \\), since the same "
        "species appear in both equations.",
        "Its equilibrium constant is \\( 2.5 \\times 10^{17} \\), the square of the "
        "formation constant.",
        "Its equilibrium constant is \\( 5.0 \\times 10^{-8} \\), found by changing the "
        "sign of the exponent only.",
        "Its equilibrium constant cannot be found without new measurements made at the "
        "same temperature."],
      ans=0,
      why="EK 7.6.A.1 inverts K on reversal, and one divided by five times ten to the "
          "eighth is two times ten to the negative ninth. Changing only the sign of the "
          "exponent leaves the coefficient uninverted, and the framework makes the "
          "reverse constant available by algebra, so no new measurement is required."),

 dict(q="Doubling every coefficient in a balanced equation changes its equilibrium "
        "constant from 0.10 to which of the following?",
      choices=["K = 0.010", "K = 0.20", "K = 0.10", "K = 0.050", "K = 0.32"],
      ans=0,
      why="EK 7.6.A.2 raises K to the power two when the coefficients are doubled, and "
          "one tenth squared is one hundredth. Doubling K itself gives 0.20, halving it "
          "gives 0.050, and taking its square root gives about 0.32."),

 dict(q="Two reactions that share a common intermediate are added together. Which "
        "statement describes the equilibrium constant of the sum?",
      choices=[
        "It is the product of the two individual equilibrium constants.",
        "It is the sum of the two individual equilibrium constants.",
        "It is the larger of the two individual equilibrium constants.",
        "It is the average of the two individual equilibrium constants.",
        "It is the difference between the two individual equilibrium constants."],
      ans=0,
      why="EK 7.6.A.3 states that when reactions are added together, the K of the "
          "resulting overall reaction is the product of the K's for the reactions that "
          "were summed. Addition of equations corresponds to multiplication of their "
          "constants, not to addition of them."),

 dict(q="For 2 SO2(g) + O2(g) to 2 SO3(g) the constant Kp is 25 at a certain "
        "temperature. What is Kp for 4 SO2(g) + 2 O2(g) to 4 SO3(g) at that same "
        "temperature?",
      choices=["Kp = 625", "Kp = 50", "Kp = 25", "Kp = 5.0", "Kp = 100"],
      ans=0,
      why="Every coefficient has been multiplied by two, so EK 7.6.A.2 raises the "
          "constant to the power two, and 25 squared is 625. EK 7.6.A.4 confirms that "
          "the same algebra governs a pressure-based expression, and doubling the "
          "constant itself would give 50."),

 dict(q="A chemist multiplies every coefficient of an equation by three and finds the "
        "new equilibrium constant to be 27. What was the equilibrium constant before the "
        "change?",
      choices=["K = 3.0", "K = 9.0", "K = 27", "K = 81", "K = 0.33"],
      ans=0,
      why="EK 7.6.A.2 means the new constant is the old one cubed, so the old one is the "
          "cube root of 27, which is three. Dividing 27 by three gives nine, which would "
          "follow only if the rule multiplied K rather than raising it to a power."),

 dict(q="Reaction I in the table is reversed and then added to reaction II. What is the "
        "equilibrium constant of the resulting overall equation?",
      table=_T_HALIDES,
      choices=["K = 0.33", "K = 27", "K = 3.0", "K = 12", "K = 6.0"],
      ans=0,
      why="Reversing reaction I inverts its constant to one ninth under EK 7.6.A.1, and "
          "EK 7.6.A.3 then multiplies by the constant of reaction II, giving three "
          "ninths, or one third. Multiplying the two constants without reversing gives "
          "27."),

 dict(q="The equilibrium constant for the decomposition of an oxide is 0.040. What is "
        "the equilibrium constant for the same decomposition written with half of every "
        "coefficient?",
      choices=["K = 0.20", "K = 0.020", "K = 0.080", "K = 0.0016", "K = 5.0"],
      ans=0,
      why="Halving the coefficients raises K to the power one half under EK 7.6.A.2, and "
          "the square root of 0.040 is 0.20. Halving K itself gives 0.020 and squaring "
          "it gives 0.0016."),

 dict(q="Which change to how a balanced equation is written leaves the numerical value "
        "of its equilibrium constant unchanged?",
      choices=[
        "Listing the reactant formulas in a different left-to-right order while keeping "
        "every coefficient the same",
        "Reversing the direction in which the equation is written",
        "Multiplying every coefficient in the equation by two",
        "Multiplying every coefficient in the equation by one half",
        "Adding a second equilibrium equation to the equation"],
      ans=0,
      why="EK 7.6.A.1, 7.6.A.2 and 7.6.A.3 each name a change to the EQUATION that "
          "changes K: reversal inverts it, scaling the coefficients raises it to a "
          "power, and summing multiplies the constants. Reordering the reactants changes "
          "none of those, because the expression multiplies the same terms together in "
          "any order."),

 dict(q="A reaction quotient for a forward reaction is measured as 0.20 at one instant. "
        "At that same instant, what is the reaction quotient for the reverse reaction?",
      choices=["Q = 5.0", "Q = 0.20", "Q = 25", "Q = 0.040", "Q = 0.45"],
      ans=0,
      why="EK 7.6.A.4 extends every valid manipulation of K to Q, and EK 7.6.A.1 inverts "
          "on reversal, so the reverse quotient is the reciprocal of 0.20, which is "
          "five. Squaring gives 0.040 and taking a square root gives about 0.45; neither "
          "is a reversal."),

 dict(q="Consider three summed steps whose equilibrium constants are 2.0, 3.0 and 0.50. "
        "What is the equilibrium constant of the overall equation they produce?",
      choices=["K = 3.0", "K = 5.5", "K = 6.0", "K = 1.5", "K = 12"],
      ans=0,
      why="EK 7.6.A.3 makes the overall constant the product of the summed constants, "
          "and two times three times one half is three. Adding the three values gives "
          "5.5, and ignoring the fractional constant gives six."),

 dict(q="For the reaction represented by 2 A(g) to B(g), K is 0.50 at a given "
        "temperature. Which equation below has an equilibrium constant of 4.0 at that "
        "temperature?",
      choices=["2 B(g) to 4 A(g)", "B(g) to 2 A(g)", "4 A(g) to 2 B(g)",
               "6 A(g) to 3 B(g)", "3 B(g) to 6 A(g)"],
      ans=0,
      why="Reversing the given equation inverts K to 2.0 under EK 7.6.A.1, and doubling "
          "the coefficients of that reversed equation raises it to the power two under "
          "EK 7.6.A.2, giving 4.0. Reversal alone gives 2.0, and doubling the original "
          "without reversing gives 0.25."),

 dict(q="Why must a shared species cancel when two equations are added to give an "
        "overall equation whose constant is the product of theirs?",
      choices=[
        "Because the shared species stands on opposite sides of the two equations and so "
        "is removed when they are combined, leaving the overall equation",
        "Because an intermediate has an equilibrium constant of one and so contributes "
        "nothing to the product",
        "Because the product rule applies only to reactions that have no species in "
        "common at all",
        "Because intermediates are always solids or pure liquids and so never enter an "
        "equilibrium expression",
        "Because cancelling the intermediate is what converts the sum of the constants "
        "into their product"],
      ans=0,
      why="Adding equations is an operation on the equations themselves: a species that "
          "is a product of one step and a reactant of the next appears on both sides of "
          "the sum and cancels, which is what leaves the overall equation that EK "
          "7.6.A.3's product rule describes. An intermediate need not be a solid, and "
          "the rule requires a shared species rather than forbidding one."),

 dict(q="The table lists the reaction quotient of a forward reaction at three times "
        "during one run. At which listed time is the reaction quotient of the REVERSE "
        "reaction largest, and what is its value there?",
      table=_T_QUOTIENT,
      choices=["At 15 minutes, where it equals 5.0",
               "At 5 minutes, where it equals 2.0",
               "At 5 minutes, where it equals 0.50",
               "At 10 minutes, where it equals 4.0",
               "At 15 minutes, where it equals 0.20"],
      ans=0,
      why="EK 7.6.A.4 carries the inversion rule of EK 7.6.A.1 over to Q, so the reverse "
          "quotient at each time is the reciprocal of the tabulated value. Those "
          "reciprocals are 2.0, 4.0 and 5.0, so the largest is at 15 minutes, where the "
          "tabulated forward value is smallest."),

 dict(q="An equation with equilibrium constant 100 is rewritten in reverse, and then "
        "every coefficient of the reversed equation is multiplied by one half. What is "
        "the final equilibrium constant?",
      choices=["K = 0.10", "K = 0.010", "K = 0.20", "K = 0.0050", "K = 0.020"],
      ans=0,
      why="EK 7.6.A.1 inverts 100 to 0.010 on reversal, and EK 7.6.A.2 then takes the "
          "square root of that, giving 0.10. Stopping after the reversal gives 0.010, "
          "and halving the reversed value gives 0.0050."),

 dict(q="For the reaction 2 NOBr(g) to 2 NO(g) + Br2(g) the equilibrium constant is "
        "0.014 at a given temperature. Without any further data, which of the following "
        "can be determined?",
      choices=[
        "The equilibrium constant for 2 NO(g) + Br2(g) to 2 NOBr(g) at that same "
        "temperature",
        "The equilibrium concentration of Br2(g) inside one particular container at "
        "that temperature",
        "The equilibrium constant for this same reaction at a different temperature",
        "The rate at which the forward reaction reaches equilibrium in a given vessel",
        "The equilibrium constant for a reaction that shares no species with this one"],
      ans=0,
      why="EK 7.6.A.1 makes the reverse constant the reciprocal of the forward one at "
          "the same temperature, so it follows by algebra alone. A concentration also "
          "requires initial conditions, and none of the four algebraic properties in "
          "7.6.A relates constants at two different temperatures or to an unrelated "
          "reaction."),

 dict(q="A student claims that because two summed steps both have constants greater than "
        "one, the overall constant must be greater than either of them. Is the claim "
        "correct?",
      choices=[
        "Yes, because the product of two numbers each greater than one exceeds both of "
        "them",
        "No, because the overall constant is the sum of the two and could be smaller "
        "than either",
        "No, because the overall constant is the average of the two and so lies between "
        "them",
        "No, because the overall constant depends on which species cancel and not on "
        "the two values",
        "Yes, but only when the two steps happen to have equal equilibrium constants"],
      ans=0,
      why="EK 7.6.A.3 makes the overall constant the product of the two, and a product "
          "of two numbers each greater than one is larger than either factor. The "
          "reasoning holds for any such pair, equal or not, and the cancellation of a "
          "shared species does not change the arithmetic."),

 dict(q="The equilibrium constant for a hydration reaction is 2.0. Which value belongs "
        "to the equation obtained by reversing that reaction and then tripling every "
        "coefficient?",
      choices=["K = 0.125", "K = 0.167", "K = 1.5", "K = 8.0", "K = 6.0"],
      ans=0,
      why="Reversal inverts the constant to one half under EK 7.6.A.1, and tripling the "
          "coefficients raises that to the power three under EK 7.6.A.2, giving 0.125. "
          "Cubing without reversing gives 8.0, and multiplying the inverted constant by "
          "three gives about 0.167."),

]
