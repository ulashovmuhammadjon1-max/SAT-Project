# AP CHEMISTRY 7.4 Calculating the Equilibrium Constant
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.4.A: calculate Kc or Kp based on experimental observations of
# concentrations or pressures at equilibrium. Suggested skill 5.C, explain the
# relationship between variables within an equation when one variable changes.
#
# Essential knowledge relied on, in the framework's own words -- this topic has one
# statement, and the learning objective carries as much of the content as the statement:
#   7.4.A.1  Equilibrium constants can be determined from experimental measurements of the
#            concentrations or partial pressures of the reactants and products at
#            equilibrium.
#
# SCOPE, and the split that keeps this module out of its neighbours. h7_6.py records the
# agreement: 7.3 owns the FORM of the expression and what is left out of it, 7.5 owns what
# the SIZE of K says, 7.6 owns the algebra of manipulating a K once you have one, and 7.7
# owns going the other way -- from a known K and initial conditions to the equilibrium
# amounts. This module goes from MEASUREMENTS TAKEN AT EQUILIBRIUM to a number. Nothing
# below reverses a reaction, multiplies its coefficients, adds two reactions, or solves for
# an unknown equilibrium concentration from a given K; verify_h7_4.py asserts the first
# three by checking no item names those operations.
#
# WHAT DOES BELONG HERE, and why the ICE-style items are 7.4 and not 7.7: EK 7.4.A.1 asks
# for K from measurements at equilibrium, and an experiment normally measures an INITIAL
# amount and ONE equilibrium amount, leaving the rest to stoichiometry. That derivation
# ends at a value of K, which is this topic's learning objective; 7.7 starts from a K and
# ends at a concentration, the opposite direction.
#
# ARITHMETIC. Every constant below is exact in one or two calculator-free steps, and every
# one is recomputed in verify_h7_4.py from the tabulated or stated measurements and the
# balanced equation alone. The heterogeneous items are recomputed with the condensed phase
# omitted AND with it included, so the check proves the omission mattered.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span below is
# hand-written. A formula in prose stays plain text (N2O4, CaCO3) and a reaction arrow is
# written as the word "to" so no glyph is left outside a span.
TOPIC = ("7.4", "Calculating the Equilibrium Constant", 7)

_T_HI = dict(
    headers=["Species", "Equilibrium concentration (M)"],
    rows=[["H2(g)", "0.20"],
          ["I2(g)", "0.20"],
          ["HI(g)", "0.80"]])

_T_SO3 = dict(
    headers=["Species", "Equilibrium concentration (M)"],
    rows=[["SO2(g)", "0.20"],
          ["O2(g)", "0.10"],
          ["SO3(g)", "0.40"]])

_T_NH3 = dict(
    headers=["Species", "Equilibrium concentration (M)"],
    rows=[["N2(g)", "0.20"],
          ["H2(g)", "0.10"],
          ["NH3(g)", "0.20"]])

_T_PRESS = dict(
    headers=["Species", "Equilibrium partial pressure (atm)"],
    rows=[["N2O4(g)", "0.50"],
          ["NO2(g)", "1.00"]])

_T_ICE = dict(
    headers=["Stage", "[A] (M)"],
    rows=[["Before any reaction", "1.00"],
          ["At equilibrium", "0.80"]])

_T_ICE2 = dict(
    headers=["Stage", "[B] (M)"],
    rows=[["Before any reaction", "0"],
          ["At equilibrium", "0.20"]])

_T_MOLES = dict(
    headers=["Species", "Moles present at equilibrium"],
    rows=[["A(g)", "2.0"],
          ["B(g)", "4.0"],
          ["C(g)", "1.0"]])

_T_TRIALS = dict(
    headers=["Trial", "[A] at equilibrium (M)", "[B] at equilibrium (M)"],
    rows=[["1", "0.80", "0.20"],
          ["2", "0.40", "0.10"],
          ["3", "0.20", "0.05"]])

_T_TEMPS = dict(
    headers=["Temperature (K)", "[A] at equilibrium (M)", "[B] at equilibrium (M)"],
    rows=[["300", "0.80", "0.20"],
          ["500", "0.50", "0.50"]])

QUESTIONS = [

 dict(q="What does the framework say equilibrium constants can be determined from?",
      choices=[
        "Experimental measurements of the concentrations or partial pressures of the "
        "reactants and products at equilibrium",
        "Experimental measurements taken at the moment the reactants are first mixed",
        "The coefficients of the balanced equation alone",
        "The rate constants of the forward and reverse reactions",
        "The masses of reactant weighed out before the reaction begins"],
      ans=0,
      why="EK 7.4.A.1 states that equilibrium constants can be determined from "
          "experimental measurements of the concentrations or partial pressures of the "
          "reactants and products at equilibrium. Measurements taken at mixing describe a "
          "system that has not yet arrived, and coefficients on their own fix the form of "
          "the expression rather than its value."),

 dict(q="The table gives the concentrations measured at equilibrium in a vessel in which "
        "H2(g) + I2(g) to 2 HI(g) has been allowed to settle. What is the value of Kc?",
      table=_T_HI,
      choices=["16", "4.0", "20", "0.0625", "8.0"],
      ans=0,
      why="EK 7.4.A.1 licenses building the constant directly from measurements at "
          "equilibrium, and the law of mass action of EK 7.3.A.1 squares the tabulated "
          "product concentration and divides by the product of the two tabulated reactant "
          "concentrations. Omitting the exponent gives a much smaller number."),

 dict(q="A vessel in which 2 SO2(g) + O2(g) to 2 SO3(g) has reached equilibrium gives the "
        "concentrations in the table. What is the value of Kc?",
      table=_T_SO3,
      choices=["40", "20", "8.0", "0.025", "2.0"],
      ans=0,
      why="EK 7.4.A.1 takes the value from measurements at equilibrium, and EK 7.3.A.1's "
          "expression squares both the tabulated SO3 and SO2 concentrations while leaving "
          "the O2 concentration to the first power. Dropping the exponent on the reactant "
          "halves the denominator and doubles the answer."),

 dict(q="For the synthesis N2(g) + 3 H2(g) to 2 NH3(g), a vessel at equilibrium gives the "
        "tabulated concentrations. What is the value of Kc?",
      table=_T_NH3,
      choices=["200", "20", "2.0", "0.0050", "2000"],
      ans=0,
      why="EK 7.4.A.1 builds the constant from the tabulated equilibrium concentrations, "
          "and EK 7.3.A.1 cubes the hydrogen concentration and squares the ammonia "
          "concentration. The cube is what makes the denominator small and the constant "
          "large; using the first power of hydrogen gives a tenth of the value."),

 dict(q="A rigid flask holding N2O4(g) to 2 NO2(g) has reached equilibrium and the "
        "partial pressures are given in the table. What is the value of Kp?",
      table=_T_PRESS,
      choices=["2.0", "0.50", "4.0", "0.25", "1.0"],
      ans=0,
      why="EK 7.4.A.1 allows partial pressures as well as concentrations, and EK 7.3.A.1's "
          "pressure form squares the tabulated NO2 pressure and divides by the tabulated "
          "N2O4 pressure. Forgetting the exponent gives the ratio of the two pressures "
          "instead."),

 dict(q="Solid CaCO3 is heated in a sealed evacuated flask until CaCO3(s) to CaO(s) + "
        "CO2(g) reaches equilibrium, at which point the carbon dioxide pressure is 0.25 "
        "atm and 8.0 grams of solid remain. What is the value of Kp?",
      choices=["0.25", "2.0", "0.031", "8.0", "0.125"],
      ans=0,
      why="EK 7.4.A.1 takes the constant from the measurement at equilibrium, and EK "
          "7.3.A.2 leaves both solids out of the expression because their concentrations "
          "are independent of the amount present. The mass of solid therefore plays no "
          "part, and the constant is the carbon dioxide pressure itself."),

 dict(q="A vessel is charged with A(g) alone, which converts by A(g) to B(g), and the "
        "table reports the concentration of A before the reaction and at equilibrium. What "
        "is the value of Kc?",
      table=_T_ICE,
      choices=["0.25", "0.80", "4.0", "0.20", "1.25"],
      ans=0,
      why="EK 7.4.A.1 asks for the constant from measurements at equilibrium, and the "
          "amount of B present follows from the amount of A that disappeared, since none "
          "was there to begin with. Dividing the equilibrium concentration of B by that of "
          "A gives the constant; using the INITIAL concentration of A in the denominator "
          "gives a different number."),

 dict(q="Another vessel is charged with 0.50 M A(g) alone, which converts by A(g) to "
        "2 B(g). The table reports the concentration of B before the reaction and at "
        "equilibrium. What is the value of Kc?",
      table=_T_ICE2,
      choices=["0.10", "0.080", "0.40", "0.020", "2.5"],
      ans=0,
      why="Two molecules of B appear for each molecule of A consumed, so the tabulated "
          "equilibrium concentration of B fixes how much A was used and therefore how much "
          "remains. EK 7.4.A.1 then takes the constant from those equilibrium values, with "
          "the B concentration squared as EK 7.3.A.1 requires."),

 dict(q="A 2.0 L vessel holding A(g) + B(g) to C(g) has reached equilibrium, and the "
        "table reports the moles of each species present. What is the value of Kc?",
      table=_T_MOLES,
      choices=["0.25", "0.13", "2.0", "0.50", "8.0"],
      ans=0,
      why="EK 7.4.A.1 speaks of the CONCENTRATIONS at equilibrium, so each tabulated mole "
          "figure has to be divided by the volume of the vessel before it enters the "
          "expression. Using the moles directly gives a different number, because the "
          "expression is not balanced in the number of species on each side."),

 dict(q="Three trials of the reaction A(g) to B(g) were run at the same temperature from "
        "different starting amounts, and the table reports the equilibrium concentrations "
        "in each. What is the value of Kc?",
      table=_T_TRIALS,
      choices=["0.25, the same in all three trials",
               "0.25 in the first trial only, with different values in the others",
               "4.0, the same in all three trials",
               "It differs from trial to trial because the starting amounts differed",
               "It cannot be found without the starting amounts"],
      ans=0,
      why="EK 7.4.A.1 takes the constant from the equilibrium measurements alone, and "
          "dividing the tabulated B concentration by the tabulated A concentration in each "
          "trial gives the same number three times. That is what makes the quantity a "
          "CONSTANT rather than a property of one particular mixture."),

 dict(q="What do the three tabulated trials of A(g) to B(g) demonstrate about the "
        "equilibrium constant?",
      table=_T_TRIALS,
      choices=[
        "Its value does not depend on the amounts the vessel was charged with",
        "Its value depends on the amounts the vessel was charged with",
        "Its value depends on how long the reaction was allowed to run",
        "Its value can only be obtained when the two concentrations are equal",
        "Its value is the average of the three ratios, which happen to differ"],
      ans=0,
      why="The three tabulated equilibrium mixtures have quite different concentrations "
          "and give the same ratio, which is what EK 7.4.A.1's claim that the constant can "
          "be DETERMINED from any equilibrium measurement requires. If the value depended "
          "on the charging, no single number could be reported for the reaction."),

 dict(q="The reaction A(g) to B(g) was allowed to reach equilibrium at two temperatures "
        "and the table reports the concentrations. What is the value of Kc at 300 K?",
      table=_T_TEMPS,
      choices=["0.25", "0.50", "4.0", "1.0", "0.80"],
      ans=0,
      why="EK 7.4.A.1 builds the constant from measurements at equilibrium, so dividing "
          "the tabulated B concentration by the tabulated A concentration in the lower "
          "temperature row gives the value. The other row belongs to a different "
          "temperature and therefore to a different constant."),

 dict(q="Using the same two-temperature table, how do the two values of Kc compare?",
      table=_T_TEMPS,
      choices=[
        "The value at the higher temperature is the larger of the two",
        "The value at the lower temperature is the larger of the two",
        "The two values are equal, since the reaction is the same",
        "The two values cannot be compared without the starting concentrations",
        "The value at the higher temperature is exactly twice the other"],
      ans=0,
      why="EK 7.4.A.1 gives a constant from each row separately, and the two ratios "
          "differ. EK 7.10.A.2 states that a change in temperature causes a change in K, "
          "which is why one reaction has two values here and the ratio of them is not "
          "fixed by anything in the data."),

 dict(q="Why does the framework insist the measurements used be taken AT equilibrium?",
      choices=[
        "Because the quotient equals the constant only once equilibrium has been reached",
        "Because concentrations cannot be measured while a reaction is occurring",
        "Because the coefficients of the equation change during a reaction",
        "Because the constant is defined as the value at the moment of mixing",
        "Because measurements taken later would include the products of side reactions"],
      ans=0,
      why="EK 7.3.A.1 says the reaction quotient tends toward the equilibrium constant "
          "such that at equilibrium the two are equal, so a set of concentrations taken "
          "before then evaluates the quotient at some other value. EK 7.4.A.1 accordingly "
          "specifies measurements at equilibrium."),

 dict(q="A student mixes reactants, waits thirty seconds, measures every concentration and "
        "builds the mass-action expression from those numbers. What has the student "
        "actually calculated?",
      choices=[
        "A reaction quotient at that moment, which is not yet the constant",
        "The equilibrium constant, since the expression was built correctly",
        "The rate of the forward reaction at that moment",
        "Nothing meaningful, since the expression cannot be evaluated before equilibrium",
        "Half the equilibrium constant, since the reaction was half finished"],
      ans=0,
      why="EK 7.3.A.1 defines the quotient at any time and makes it equal to the constant "
          "only at equilibrium, and EK 7.4.A.1 asks for measurements at equilibrium for "
          "exactly that reason. The expression can certainly be evaluated earlier; what it "
          "returns is simply not the constant."),

 dict(q="An experimenter records the number of moles of each species present at "
        "equilibrium. What else is needed before Kc can be calculated?",
      choices=[
        "The volume of the vessel",
        "The temperature of the vessel",
        "The time the reaction was allowed to run",
        "The initial number of moles of each species",
        "Nothing else, since moles may be used in place of concentrations"],
      ans=0,
      why="EK 7.4.A.1 speaks of the CONCENTRATIONS at equilibrium, and a number of moles "
          "becomes a concentration only when divided by the volume. Temperature fixes "
          "WHICH constant is being measured but does not enter the arithmetic, and the "
          "initial amounts are not needed once every equilibrium amount is known."),

 dict(q="For N2O4(g) to 2 NO2(g) at equilibrium, the concentration of N2O4 is 0.10 M and "
        "that of NO2 is 0.20 M. What is the value of Kc?",
      choices=["0.40", "2.0", "0.20", "4.0", "0.040"],
      ans=0,
      why="EK 7.4.A.1 takes the constant from the two stated equilibrium concentrations, "
          "and EK 7.3.A.1 squares the NO2 concentration because its coefficient is two. "
          "Dividing without squaring gives the ratio of the two concentrations instead."),

 dict(q="At equilibrium in a vessel holding C(s) + CO2(g) to 2 CO(g), the concentration of "
        "CO2 is 0.20 M and that of CO is 0.40 M, with 5.0 grams of carbon still present. "
        "What is the value of Kc?",
      choices=["0.80", "0.16", "2.0", "4.0", "0.16 divided by the mass of carbon"],
      ans=0,
      why="EK 7.3.A.2 leaves the solid carbon out of the expression because its "
          "concentration is independent of the amount present, so the stated mass does not "
          "enter. Squaring the CO concentration and dividing by the CO2 concentration is "
          "what EK 7.4.A.1 and the law of mass action leave."),

 dict(q="A reaction 2 A(g) to B(g) reaches equilibrium with the concentration of A at 0.20 "
        "M and that of B at 0.40 M. What is the value of Kc?",
      choices=["10", "2.0", "0.10", "20", "0.50"],
      ans=0,
      why="EK 7.3.A.1 puts the product concentration over the SQUARE of the reactant "
          "concentration, because the coefficient of A is two, and EK 7.4.A.1 evaluates it "
          "at the stated equilibrium values. Leaving the exponent off gives the plain ratio "
          "of the two concentrations."),

 dict(q="A flask in which 2 SO2(g) + O2(g) to 2 SO3(g) has settled has partial pressures "
        "of 0.10 atm of SO2, 0.20 atm of O2 and 0.20 atm of SO3. What is the value of Kp?",
      choices=["20", "10", "2.0", "0.050", "200"],
      ans=0,
      why="EK 7.4.A.1 permits partial pressures, and EK 7.3.A.1's pressure form squares "
          "the SO3 pressure and divides by the square of the SO2 pressure times the O2 "
          "pressure. Both exponents matter: dropping the one on SO2 changes the "
          "denominator by a factor of ten."),

 dict(q="Which set of experimental data is sufficient on its own to calculate Kc for a "
        "gas phase reaction?",
      choices=[
        "The concentration of every species measured after the system has stopped changing",
        "The concentration of every species measured immediately after mixing",
        "The initial concentration of every species and the temperature",
        "The concentration of one species at equilibrium and nothing else",
        "The masses of the reactants weighed out and the volume of the vessel"],
      ans=0,
      why="EK 7.4.A.1 asks for the concentrations of the reactants AND products at "
          "equilibrium, and a system that has stopped changing is at equilibrium under EK "
          "7.1.A.2. One species alone leaves the rest of the expression unknown, and "
          "initial values describe a state the constant is not defined at."),

 dict(q="Can Kc be found when only the initial concentration of the single reactant and "
        "the equilibrium concentration of the single product are known?",
      choices=[
        "Yes, because the amount of reactant consumed follows from the amount of product "
        "formed",
        "No, because the equilibrium concentration of the reactant was never measured",
        "Yes, but only if the reaction has a one-to-one stoichiometry",
        "No, because initial concentrations may never be used in any part of the working",
        "Yes, but the value obtained is a reaction quotient rather than a constant"],
      ans=0,
      why="The balanced equation converts the product formed into the reactant consumed, "
          "and subtracting that from the initial concentration gives the equilibrium "
          "concentration EK 7.4.A.1 requires. The stoichiometry may be any ratio, since the "
          "coefficients supply it."),

 dict(q="Using the tabulated equilibrium concentrations for 2 SO2(g) + O2(g) to 2 SO3(g), "
        "what value would a student obtain who used the first power of every "
        "concentration?",
      table=_T_SO3,
      choices=["20", "40", "4.0", "0.050", "10"],
      ans=0,
      why="Dividing the tabulated SO3 concentration by the product of the two tabulated "
          "reactant concentrations, with no exponents at all, gives this value against the "
          "correct one that EK 7.3.A.1's coefficients produce. The gap between the two "
          "numbers is exactly what the exponent rule is for."),

 dict(q="A vessel is charged with 1.00 M of A(g) alone and half of it has been converted "
        "by A(g) to B(g) when equilibrium is reached. What is the value of Kc?",
      choices=["1.0", "0.50", "2.0", "0.25", "0.020"],
      ans=0,
      why="Half of the initial concentration remains as A and half has become B, so the "
          "two equilibrium concentrations are equal and EK 7.4.A.1's ratio comes out at "
          "one. The value one arises here from the particular extent of reaction, not from "
          "any general rule."),

 dict(q="A reaction carried out in aqueous solution has H2O(l) among its reactants. How is "
        "the water treated when the constant is calculated?",
      choices=[
        "It is left out of the expression entirely",
        "Its concentration is measured like any other reactant",
        "Its concentration is taken as one molar",
        "It is placed in the numerator because it is the solvent",
        "It is included only if its coefficient is greater than one"],
      ans=0,
      why="EK 7.3.A.2 states that the expression does not include substances whose "
          "concentrations are independent of the amount, naming solids and pure liquids, "
          "and EK 7.4.A.1's calculation uses whatever the expression contains. A "
          "coefficient cannot bring back a species the expression omits."),

 dict(q="Two laboratories measure the same reaction at equilibrium and report different "
        "values for the constant. Which difference between the experiments would account "
        "for that?",
      choices=[
        "The two laboratories worked at different temperatures",
        "The two laboratories used vessels of different volume",
        "The two laboratories charged their vessels with different amounts",
        "The two laboratories waited different lengths of time",
        "One laboratory measured concentrations and the other measured the same "
        "concentrations twice"],
      ans=0,
      why="EK 7.10.A.2 states that a change in temperature causes a change in K, while EK "
          "7.4.A.1 makes the value follow from the equilibrium measurements alone, so "
          "different charges, volumes or waiting times all end at the same constant, as "
          "the three tabulated trials in this topic show."),

 dict(q="A student computing Kc for a heterogeneous reaction divides by the mass of the "
        "solid present. What is the consequence?",
      choices=[
        "The value obtained changes whenever a different amount of solid is used, so it is "
        "not a constant",
        "The value obtained is correct, since the solid is a reactant",
        "The value obtained is the reciprocal of the correct one",
        "The value obtained is correct only when exactly one gram of solid is present",
        "The value obtained is unchanged, since dividing by a mass has no effect"],
      ans=0,
      why="EK 7.3.A.2 leaves solids out precisely because their concentrations are "
          "independent of the amount present, so a value that depends on the mass weighed "
          "out could not be reported as a property of the reaction. That failure is the "
          "reason the omission rule exists."),

 dict(q="For which of the following would the equilibrium expression contain exactly one "
        "concentration?",
      choices=[
        "A solid decomposing to another solid and a single gas",
        "A gas decomposing to two different gases",
        "Two gases combining to form one gas",
        "A solid decomposing to two different gases",
        "A gas dissolving into a pure liquid solvent"],
      ans=0,
      why="EK 7.3.A.2 removes both solids and leaves the single gas, so one concentration "
          "remains. Each of the other cases leaves either two or three species that EK "
          "7.3.A.2 does not remove, and the last is the case the exclusion statement "
          "attached to EK 7.3.A.1 puts outside the exam."),

 dict(q="Using the tabulated equilibrium concentrations for the hydrogen iodide vessel, "
        "could Kc be calculated from the HI concentration alone?",
      table=_T_HI,
      choices=[
        "No, because the expression also requires the two reactant concentrations",
        "Yes, because the HI concentration is the only product concentration",
        "Yes, because the reactant concentrations are equal to each other",
        "No, because the initial concentrations would also be needed",
        "Yes, provided the HI concentration is squared"],
      ans=0,
      why="EK 7.4.A.1 asks for measurements of the reactants AND products at equilibrium, "
          "and EK 7.3.A.1's expression divides by both tabulated reactant concentrations. "
          "That the two happen to be equal in this vessel makes the arithmetic easier but "
          "does not remove them from the expression."),

 dict(q="Summarise what a measured value of Kc for a reaction is a property of.",
      choices=[
        "The reaction and the temperature",
        "The reaction and the volume of the vessel",
        "The reaction and the amounts originally charged",
        "The reaction alone, at every temperature",
        "The particular sample measured, and nothing more general"],
      ans=0,
      why="EK 7.4.A.1 has the same value follow from any equilibrium mixture of that "
          "reaction, as the three tabulated trials here show, while EK 7.10.A.2 makes a "
          "change in temperature change K. Volume and charging do not survive into the "
          "value, and temperature does."),

]
