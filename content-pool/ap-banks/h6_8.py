# AP CHEMISTRY 6.8 Enthalpy of Formation
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.8.A: calculate the enthalpy change for a chemical or physical process
# based on the standard enthalpies of formation. Suggested skill 5.F, calculate, estimate, or
# predict an unknown quantity from known quantities by selecting and following a logical
# computational pathway and attending to precision.
#
# Essential knowledge relied on, in the framework's own words:
#   6.8.A.1  Tables of standard enthalpies of formation can be used to calculate the standard
#            enthalpies of reactions.
#            EQN: delta H(reaction) = SUM delta Hf(products) - SUM delta Hf(reactants)
#
# That single statement and that single equation are the WHOLE of what the framework says
# about this topic, and everything below is keyed to them. Two other statements are borrowed,
# both cited where they are used:
#   6.6.A.1  The enthalpy change of a reaction gives the amount of heat energy released (for
#            negative values) or absorbed (for positive values) by a chemical reaction at
#            constant pressure.
#   6.6.A.2  Thermal energy is transferred TO the surroundings in an exothermic reaction and
#            FROM the surroundings in an endothermic one.
# 6.6 owns that sign convention; this module uses it to name a direction but does not re-teach
# it, and no item here multiplies an amount in moles by a molar enthalpy, which is 6.6's own
# calculation.
#
# WHY EVERY STANDARD ENTHALPY OF FORMATION IS TABULATED, INCLUDING THE ZEROS. The framework
# does not state anywhere that an element in its standard state has a standard enthalpy of
# formation of zero. It is true, and every chemist knows it, and it is exactly the kind of
# thing this project has a rule against keying from memory. So the zeros for O2, H2, N2, C and
# Fe are printed in the table like every other value, and verify_h6_8.py reads the numbers it
# recomputes with FROM THAT TABLE rather than from constants of its own. A student is never
# asked to supply a value the stimulus does not give, and an edited table and a stale check
# cannot pass together.
#
# THE SUBTRACTION RUNS ONE WAY AND ONE WAY ONLY: the sum over the PRODUCTS minus the sum over
# the REACTANTS. Reversing it gives the same magnitude with the wrong sign, which is the single
# most likely defect in this topic and, unlike a wrong magnitude, it is the sign a student
# would go on to act on. So every keyed enthalpy of reaction states its direction as well as
# its number, every anchor carries the sign AND the direction word, and the reversed value sits
# in exactly one distractor of every such item.
#
# THE SIGNS IN THE TABLE ARE NOT DECORATION EITHER. Three of the tabulated substances carry a
# POSITIVE standard enthalpy of formation, which is what makes items 9, 16, 18 and 22 come out
# the way they do -- two of the eleven reactions below are endothermic, and they are endothermic
# because of the table, not because a distractor list needed variety.
#
# SCOPE. 6.7 owns the average bond energies and 6.9 owns Hess's law, so no item here reaches an
# enthalpy by either route, and verify_h6_8.py asserts it. The CED attaches an EXCLUSION
# STATEMENT to 6.9 -- the concept of state functions will not be assessed -- and nothing in
# this module mentions state functions at all.
#
# NOTATION. export_units.py does not typeset Chemistry. Equations are plain text with the word
# "gives" for the arrow and phase labels in parentheses, as h5_7.py and h6_7.py write them;
# enthalpies are plain signed numbers with the unit spelled kJ/mol, which needs no math span.
TOPIC = ("6.8", "Enthalpy of Formation", 6)

# Standard enthalpies of formation, in kJ/mol. Every value a question needs is here,
# including the zeros, so that nothing has to be supplied from memory.
_T_FORM = dict(
    headers=["Substance", "Standard enthalpy of formation (kJ/mol)"],
    rows=[["CH4(g)", "-75"],
          ["CO(g)", "-111"],
          ["CO2(g)", "-394"],
          ["H2O(l)", "-286"],
          ["NH3(g)", "-46"],
          ["NO(g)", "+90"],
          ["NO2(g)", "+33"],
          ["SO2(g)", "-297"],
          ["SO3(g)", "-396"],
          ["CaO(s)", "-635"],
          ["CaCO3(s)", "-1207"],
          ["Fe2O3(s)", "-824"],
          ["O2(g)", "0"],
          ["H2(g)", "0"],
          ["N2(g)", "0"],
          ["C(s)", "0"],
          ["Fe(s)", "0"]])

QUESTIONS = [

 dict(q="What does the framework say tables of standard enthalpies of formation can be used "
        "to calculate?",
      choices=[
        "The standard enthalpies of reactions",
        "The standard enthalpies of formation of the elements",
        "The average bond energies of the bonds broken in a reaction",
        "The heat capacity of the reaction mixture",
        "The temperature at which a reaction begins"],
      ans=0,
      why="EK 6.8.A.1 states that tables of standard enthalpies of formation can be used to "
          "calculate the standard enthalpies of reactions, and supplies the equation that "
          "does it."),

 dict(q="Which expression does the framework give for the standard enthalpy of a reaction?",
      choices=[
        "The sum over the products minus the sum over the reactants",
        "The sum over the reactants minus the sum over the products",
        "The sum over the products plus the sum over the reactants",
        "The sum over the products multiplied by the sum over the reactants",
        "The larger of the two sums minus the smaller"],
      ans=0,
      why="EK 6.8.A.1's equation sets the standard enthalpy of reaction equal to the sum of "
          "the standard enthalpies of formation of the products minus the sum over the "
          "reactants. Taking the larger minus the smaller would force the answer positive "
          "every time and destroy the information the sign carries."),

 dict(q="A student adds the sum over the products to the sum over the reactants. What is "
        "wrong with that?",
      choices=[
        "The two sums must be subtracted, one from the other, rather than added",
        "The two sums must be multiplied rather than added",
        "The two sums must be averaged rather than added",
        "The two sums must be added and then halved",
        "Nothing, since both sums are made of standard enthalpies of formation"],
      ans=0,
      why="EK 6.8.A.1's equation is a difference of the two sums, not a total. Adding them "
          "produces a number that grows with both sides at once and cannot report which way "
          "the enthalpy went."),

 dict(q="A student subtracts the sum over the products from the sum over the reactants "
        "instead. What is the effect on the answer?",
      choices=[
        "The magnitude is right and the sign is reversed",
        "The magnitude is right and the sign is right",
        "The magnitude is doubled and the sign is right",
        "The magnitude is halved and the sign is reversed",
        "The result is unrelated to the standard enthalpy of reaction"],
      ans=0,
      why="EK 6.8.A.1 takes the product sum minus the reactant sum, so exchanging the two "
          "terms negates the difference and leaves its size untouched. Under EK 6.6.A.1 that "
          "reports the opposite direction of heat flow, which is the whole content of the "
          "answer."),

 dict(q="In the reaction 2 H2(g) + O2(g) gives 2 H2O(l) , how many times does the standard "
        "enthalpy of formation of H2O(l) enter the sum over the products?",
      choices=[
        "Twice, once for each mole of it produced",
        "Once, no matter how many moles are produced",
        "Three times, once for each substance in the equation",
        "Not at all, since only the reactants carry coefficients",
        "Twice, but with the sign reversed the second time"],
      ans=0,
      why="EK 6.8.A.1's sum runs over the products of the reaction as written, so a substance "
          "produced in two moles contributes its tabulated value twice. Learning objective "
          "6.8.A asks for the enthalpy change of the process as written, which is what makes "
          "the coefficients part of the arithmetic."),

 dict(q="A standard enthalpy of reaction calculated from the table comes out negative. What "
        "does that mean?",
      choices=[
        "Heat energy is released by the reaction at constant pressure",
        "Heat energy is absorbed by the reaction at constant pressure",
        "No heat energy is exchanged with the surroundings",
        "The reaction cannot take place",
        "Every product has a positive standard enthalpy of formation"],
      ans=0,
      why="EK 6.6.A.1 says the enthalpy change of a reaction gives the amount of heat energy "
          "released for negative values, and EK 6.6.A.2 calls a reaction that transfers "
          "thermal energy to its surroundings exothermic."),

 dict(q="A standard enthalpy of reaction calculated from the table comes out positive. What "
        "does that mean?",
      choices=[
        "Heat energy is absorbed by the reaction at constant pressure",
        "Heat energy is released by the reaction at constant pressure",
        "No heat energy is exchanged with the surroundings",
        "The reaction takes place without any change in energy",
        "Every reactant has a negative standard enthalpy of formation"],
      ans=0,
      why="EK 6.6.A.1 says the enthalpy change gives the amount of heat energy absorbed for "
          "positive values, and EK 6.6.A.2 calls a reaction that draws thermal energy from "
          "its surroundings endothermic."),

 dict(q="Which of the tabulated substances has the most negative standard enthalpy of "
        "formation?",
      table=_T_FORM,
      choices=[
        "CaCO3(s)",
        "Fe2O3(s)",
        "SO3(g)",
        "CO2(g)",
        "H2O(l)"],
      ans=0,
      why="EK 6.8.A.1's equation uses the tabulated values as they stand, signs included, so "
          "the comparison is a reading of the table: the most negative entry is the one "
          "furthest below zero, not the one largest in magnitude regardless of sign."),

 dict(q="Which of these tabulated substances has a positive standard enthalpy of formation?",
      table=_T_FORM,
      choices=[
        "NO(g)",
        "CO(g)",
        "NH3(g)",
        "CH4(g)",
        "SO2(g)"],
      ans=0,
      why="EK 6.8.A.1's equation carries the tabulated signs into the sums, so which "
          "substances are tabulated above zero decides which reactions come out endothermic. "
          "Only one of these five is."),

 dict(q="According to the table, what is the standard enthalpy of formation of CO2(g), and "
        "what does the sign of that value report?",
      table=_T_FORM,
      choices=[
        "-394 kJ/mol, and the negative sign reports heat energy released",
        "+394 kJ/mol, and the positive sign reports heat energy absorbed",
        "-286 kJ/mol, and the negative sign reports heat energy released",
        "-111 kJ/mol, and the negative sign reports heat energy released",
        "0 kJ/mol, and no heat energy is reported either way"],
      ans=0,
      why="EK 6.8.A.1's calculation begins by reading each substance's tabulated value with "
          "its sign attached, and EK 6.6.A.1 makes a negative enthalpy heat energy released. "
          "Dropping the sign, or reading the row for water or for carbon monoxide, gives "
          "three of the other values offered."),

 dict(q="For the reaction CH4(g) + 2 O2(g) gives CO2(g) + 2 H2O(l) , what is the sum of the "
        "standard enthalpies of formation of the products?",
      table=_T_FORM,
      choices=[
        "-966 kJ/mol",
        "-75 kJ/mol",
        "-680 kJ/mol",
        "-891 kJ/mol",
        "-1041 kJ/mol"],
      ans=0,
      why="EK 6.8.A.1's first term sums the tabulated values of the products of the reaction "
          "as written, so the value for water is counted twice. Counting it once, summing the "
          "reactants instead, or completing the whole subtraction gives the other values "
          "offered."),

 dict(q="For the same reaction, CH4(g) + 2 O2(g) gives CO2(g) + 2 H2O(l) , what is the sum of "
        "the standard enthalpies of formation of the reactants?",
      table=_T_FORM,
      choices=[
        "-75 kJ/mol",
        "-966 kJ/mol",
        "0 kJ/mol",
        "-891 kJ/mol",
        "-1041 kJ/mol"],
      ans=0,
      why="EK 6.8.A.1's second term sums the tabulated values of the reactants, and the table "
          "gives zero for the oxygen, so only the methane contributes. Taking the oxygen "
          "alone, summing the products instead, or completing the subtraction gives the other "
          "values offered."),

 dict(q="What is the standard enthalpy of the reaction CH4(g) + 2 O2(g) gives CO2(g) + "
        "2 H2O(l) , from the tabulated values?",
      table=_T_FORM,
      choices=[
        "-891 kJ/mol, so the reaction is exothermic",
        "+891 kJ/mol, so the reaction is endothermic",
        "-1041 kJ/mol, so the reaction is exothermic",
        "-966 kJ/mol, so the reaction is exothermic",
        "-75 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.8.A.1's equation subtracts the reactant sum from the product sum, and "
          "EK 6.6.A.1 makes a negative result heat energy released. Reversing the "
          "subtraction, adding the two sums, or reporting one sum on its own gives the other "
          "values offered."),

 dict(q="What is the standard enthalpy of the reaction 2 H2(g) + O2(g) gives 2 H2O(l) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "-572 kJ/mol, so the reaction is exothermic",
        "+572 kJ/mol, so the reaction is endothermic",
        "-286 kJ/mol, so the reaction is exothermic",
        "-1144 kJ/mol, so the reaction is exothermic",
        "+286 kJ/mol, so the reaction is endothermic"],
      ans=0,
      why="EK 6.8.A.1's equation sums the tabulated value of the water twice and subtracts a "
          "reactant sum the table makes zero. Dropping the coefficient, applying it a second "
          "time, or reversing the subtraction gives the other values offered."),

 dict(q="What is the standard enthalpy of the reaction N2(g) + 3 H2(g) gives 2 NH3(g) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "-92 kJ/mol, so the reaction is exothermic",
        "+92 kJ/mol, so the reaction is endothermic",
        "-46 kJ/mol, so the reaction is exothermic",
        "-184 kJ/mol, so the reaction is exothermic",
        "+46 kJ/mol, so the reaction is endothermic"],
      ans=0,
      why="EK 6.8.A.1's equation counts the tabulated ammonia value twice and subtracts a "
          "reactant sum the table makes zero, so the product sum is the whole answer. "
          "EK 6.6.A.1 makes the negative result heat energy released."),

 dict(q="What is the standard enthalpy of the reaction CaCO3(s) gives CaO(s) + CO2(g) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "+178 kJ/mol, so the reaction is endothermic",
        "-178 kJ/mol, so the reaction is exothermic",
        "-2236 kJ/mol, so the reaction is exothermic",
        "-1029 kJ/mol, so the reaction is exothermic",
        "-1207 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.8.A.1's subtraction leaves a positive result here because the single reactant "
          "is tabulated further below zero than the two products together, and EK 6.6.A.1 "
          "makes a positive result heat energy absorbed."),

 dict(q="What is the standard enthalpy of the reaction 2 SO2(g) + O2(g) gives 2 SO3(g) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "-198 kJ/mol, so the reaction is exothermic",
        "+198 kJ/mol, so the reaction is endothermic",
        "-1386 kJ/mol, so the reaction is exothermic",
        "-792 kJ/mol, so the reaction is exothermic",
        "-594 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.8.A.1's equation doubles both tabulated sulfur oxide values and takes the "
          "difference, with the tabulated zero for oxygen adding nothing. Reversing the "
          "subtraction, adding the sums, or reporting one sum alone gives the other values "
          "offered."),

 dict(q="What is the standard enthalpy of the reaction N2(g) + O2(g) gives 2 NO(g) , from the "
        "tabulated values?",
      table=_T_FORM,
      choices=[
        "+180 kJ/mol, so the reaction is endothermic",
        "-180 kJ/mol, so the reaction is exothermic",
        "+90 kJ/mol, so the reaction is endothermic",
        "+360 kJ/mol, so the reaction is endothermic",
        "-90 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.8.A.1's equation counts the tabulated nitrogen monoxide value twice against a "
          "reactant sum the table makes zero, and that value is one of the positive ones, so "
          "EK 6.6.A.1 makes the reaction one that absorbs heat energy."),

 dict(q="What is the standard enthalpy of the reaction 2 CO(g) + O2(g) gives 2 CO2(g) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "-566 kJ/mol, so the reaction is exothermic",
        "+566 kJ/mol, so the reaction is endothermic",
        "-1010 kJ/mol, so the reaction is exothermic",
        "-788 kJ/mol, so the reaction is exothermic",
        "-222 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.8.A.1's equation doubles both tabulated oxide values and takes the difference. "
          "Both sums are negative here, so the answer is the amount by which the products lie "
          "below the reactants rather than either sum on its own."),

 dict(q="What is the standard enthalpy of the reaction 2 NH3(g) gives N2(g) + 3 H2(g) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "+92 kJ/mol, so the reaction is endothermic",
        "-92 kJ/mol, so the reaction is exothermic",
        "+46 kJ/mol, so the reaction is endothermic",
        "+184 kJ/mol, so the reaction is endothermic",
        "-46 kJ/mol, so the reaction is exothermic"],
      ans=0,
      why="EK 6.8.A.1's equation now finds the tabulated zeros on the product side and the "
          "ammonia on the reactant side, so the subtraction comes out positive and "
          "EK 6.6.A.1 makes it heat energy absorbed."),

 dict(q="What is the standard enthalpy of the reaction C(s) + O2(g) gives CO2(g) , from the "
        "tabulated values?",
      table=_T_FORM,
      choices=[
        "-394 kJ/mol, so the reaction is exothermic",
        "+394 kJ/mol, so the reaction is endothermic",
        "-788 kJ/mol, so the reaction is exothermic",
        "-111 kJ/mol, so the reaction is exothermic",
        "0 kJ/mol, since both reactants are tabulated at zero"],
      ans=0,
      why="EK 6.8.A.1's equation gives the single product's tabulated value minus a reactant "
          "sum the table makes zero, so the standard enthalpy of this reaction is exactly the "
          "tabulated entry for the product."),

 dict(q="What is the standard enthalpy of the reaction 2 NO(g) + O2(g) gives 2 NO2(g) , from "
        "the tabulated values?",
      table=_T_FORM,
      choices=[
        "-114 kJ/mol, so the reaction is exothermic",
        "+114 kJ/mol, so the reaction is endothermic",
        "+246 kJ/mol, so the reaction is endothermic",
        "+66 kJ/mol, so the reaction is endothermic",
        "+180 kJ/mol, so the reaction is endothermic"],
      ans=0,
      why="EK 6.8.A.1's equation gives a negative answer even though both tabulated nitrogen "
          "oxide values are positive, because the product sum lies below the reactant sum. "
          "The sign of a tabulated entry and the sign of the reaction's enthalpy are separate "
          "questions."),

 dict(q="What is the standard enthalpy of the reaction 4 Fe(s) + 3 O2(g) gives 2 Fe2O3(s) , "
        "from the tabulated values?",
      table=_T_FORM,
      choices=[
        "-1648 kJ/mol, so the reaction is exothermic",
        "+1648 kJ/mol, so the reaction is endothermic",
        "-824 kJ/mol, so the reaction is exothermic",
        "-3296 kJ/mol, so the reaction is exothermic",
        "0 kJ/mol, since the reactants are tabulated at zero"],
      ans=0,
      why="EK 6.8.A.1's equation counts the tabulated iron oxide value twice against a "
          "reactant sum the table makes zero. Dropping the coefficient, applying it twice, or "
          "reversing the subtraction gives the other values offered."),

 dict(q="In the reaction N2(g) + 3 H2(g) gives 2 NH3(g) , why does the sum over the reactants "
        "contribute nothing to the standard enthalpy of reaction?",
      table=_T_FORM,
      choices=[
        "Because the table gives a standard enthalpy of formation of zero for both reactants",
        "Because the reactants are consumed rather than produced",
        "Because there are more moles of reactant than of product",
        "Because both reactants are gases at the standard state",
        "Because the sum over the reactants is never part of the calculation"],
      ans=0,
      why="EK 6.8.A.1's equation always subtracts the reactant sum; here that sum happens to "
          "be zero because of what the table lists for these two substances, and not because "
          "of anything about their role in the equation."),

 dict(q="The reaction 2 NH3(g) gives N2(g) + 3 H2(g) is the reverse of the reaction N2(g) + "
        "3 H2(g) gives 2 NH3(g) . From the tabulated values, how do their standard enthalpies "
        "of reaction compare?",
      table=_T_FORM,
      choices=[
        "They are equal in magnitude and opposite in sign",
        "They are equal in magnitude and have the same sign",
        "The reverse reaction has twice the magnitude of the forward one",
        "The reverse reaction has half the magnitude of the forward one",
        "No comparison can be made from the tabulated values alone"],
      ans=0,
      why="Reversing the equation exchanges which substances are products and which are "
          "reactants, so EK 6.8.A.1's two sums swap places and the difference is negated. "
          "Nothing else in the calculation changes, so the magnitude is untouched."),

 dict(q="Of the tabulated CO(g), CO2(g) and CH4(g), which has the most negative standard "
        "enthalpy of formation?",
      table=_T_FORM,
      choices=[
        "CO2(g)",
        "CO(g)",
        "CH4(g)",
        "All three are tabulated at the same value",
        "It cannot be decided without a chemical equation"],
      ans=0,
      why="EK 6.8.A.1's calculation reads the tabulated values with their signs, so ranking "
          "them is a reading of the table. Carbon dioxide is tabulated furthest below zero of "
          "the three."),

 dict(q="One reaction has a sum over the products of -500 kJ/mol and a sum over the reactants "
        "of -200 kJ/mol. A second reaction has a sum over the products of -200 kJ/mol and a "
        "sum over the reactants of -500 kJ/mol. Which is exothermic?",
      choices=[
        "The first, since its standard enthalpy of reaction comes out negative",
        "The second, since its standard enthalpy of reaction comes out negative",
        "The first, since its standard enthalpy of reaction comes out positive",
        "Both, since every reaction releases heat energy overall",
        "Neither, since the same two numbers appear in each"],
      ans=0,
      why="EK 6.8.A.1 subtracts the reactant sum from the product sum, which is negative for "
          "the first pair and positive for the second, and EK 6.6.A.1 makes a negative "
          "standard enthalpy heat energy released."),

 dict(q="A reaction's sum over the products and its sum over the reactants come out equal. "
        "What is its standard enthalpy of reaction?",
      choices=[
        "Zero, since the two sums cancel in the framework's subtraction",
        "Equal to the sum over the products",
        "Equal to twice the sum over the products",
        "Negative, since every reaction releases heat energy overall",
        "It cannot be found without the individual tabulated values"],
      ans=0,
      why="EK 6.8.A.1's equation is the difference of the two sums, so equal sums leave "
          "nothing behind. EK 6.6.A.1 attaches a direction of heat flow to a negative or a "
          "positive value, and this result is neither."),

 dict(q="The table gives a standard enthalpy of formation of 0 kJ/mol for O2(g). What does "
        "3 mol of O2(g) appearing as a reactant contribute to the sum over the reactants?",
      table=_T_FORM,
      choices=[
        "Nothing at all, since zero multiplied by the coefficient is still zero",
        "Three times the standard enthalpy of formation of the product",
        "A positive contribution, because three moles of a gas are consumed",
        "A negative contribution, because oxygen appears on the reactant side",
        "It cannot be decided without the standard enthalpy of the reaction"],
      ans=0,
      why="EK 6.8.A.1's sum multiplies each substance's tabulated value by the number of "
          "moles of it in the equation as written, and the table's entry for this substance "
          "is zero, so no coefficient can make it contribute."),

 dict(q="Which statement correctly combines what a table of standard enthalpies of formation "
        "gives and what the sign of the result means?",
      choices=[
        "The sum over the products minus the sum over the reactants, with a negative result "
        "meaning heat energy is released",
        "The sum over the products minus the sum over the reactants, with a negative result "
        "meaning heat energy is absorbed",
        "The sum over the reactants minus the sum over the products, with a negative result "
        "meaning heat energy is released",
        "The two sums added together, with a negative result meaning heat energy is released",
        "The sum over the products minus the sum over the reactants, with the sign of the "
        "result carrying no meaning"],
      ans=0,
      why="EK 6.8.A.1 supplies the subtraction and its direction, and EK 6.6.A.1 supplies "
          "what the sign of the answer reports: heat energy released for negative values and "
          "absorbed for positive ones. Each rejected option breaks one of those two links."),
]
