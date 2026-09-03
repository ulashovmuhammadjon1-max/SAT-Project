# AP CHEMISTRY 5.2 Introduction to Rate Law
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.2.A: represent experimental data with a consistent rate
# law expression. Suggested skill 5.C, explain the relationship between
# variables within an equation when one variable changes.
#
# Essential knowledge relied on, in the framework's own words:
#   5.2.A.1  Experimental methods can be used to monitor the amounts of
#            reactants and/or products of a reaction over time and to determine
#            the rate of the reaction.
#   5.2.A.2  The rate law expresses the rate of a reaction as proportional to
#            the concentration of each reactant raised to a power.
#   5.2.A.3  The power of each reactant in the rate law is the order of the
#            reaction with respect to that reactant. The sum of the powers of
#            the reactant concentrations in the rate law is the overall order of
#            the reaction.
#   5.2.A.4  The proportionality constant in the rate law is called the rate
#            constant. The value of this constant is temperature dependent and
#            the units reflect the overall reaction order.
#   5.2.A.5  Comparing initial rates of a reaction is a method to determine the
#            order with respect to each reactant.
#
# WHERE THIS TOPIC STOPS. Integrated rate laws, linear plots and half-life are
# 5.3; inferring a rate law from the molecularity of an elementary step is 5.4;
# deriving one from a mechanism is 5.8 and 5.9. Nothing here keys on any of
# those. Every order in this module is obtained the way 5.2.A.5 says -- by
# comparing initial rates in which one concentration changes at a time.
#
# NOTATION. Chemistry is not typeset by export_units.py, so every rate law and
# every unit of a rate constant is a hand-written \( ... \) span. Concentrations
# in prose are plain text, and a bracketed concentration inside a span is
# written \([\mathrm{A}]\) with the species upright.
TOPIC = ("5.2", "Introduction to Rate Law", 5)

_T_AB = dict(
    headers=["Experiment", "Initial concentration of A (moles per liter)",
             "Initial concentration of B (moles per liter)",
             "Initial rate (moles per liter per second)"],
    rows=[["1", "0.10", "0.10", "0.0020"],
          ["2", "0.20", "0.10", "0.0040"],
          ["3", "0.10", "0.20", "0.0080"]])

_T_XY = dict(
    headers=["Experiment", "Initial concentration of X (moles per liter)",
             "Initial concentration of Y (moles per liter)",
             "Initial rate (moles per liter per second)"],
    rows=[["1", "0.20", "0.20", "0.016"],
          ["2", "0.40", "0.20", "0.064"],
          ["3", "0.20", "0.40", "0.016"]])

_T_KT = dict(
    headers=["Temperature (kelvins)",
             "Rate constant measured for the same reaction"],
    rows=[["300", "0.0012"],
          ["310", "0.0025"],
          ["320", "0.0051"]])

_T_THREE = dict(
    headers=["Experiment", "Initial [A] (moles per liter)",
             "Initial [B] (moles per liter)", "Initial [C] (moles per liter)",
             "Initial rate (moles per liter per second)"],
    rows=[["1", "0.10", "0.10", "0.10", "0.00010"],
          ["2", "0.20", "0.10", "0.10", "0.00020"],
          ["3", "0.10", "0.30", "0.10", "0.00010"],
          ["4", "0.10", "0.10", "0.20", "0.00040"]])

_T_UNITS = dict(
    headers=["Overall order of the reaction", "Units of the rate constant"],
    rows=[["Zero", "moles per liter per second"],
          ["One", "per second"],
          ["Two", "liters per mole per second"],
          ["Three", "liters squared per mole squared per second"]])

QUESTIONS = [

 dict(q="What does a rate law express?",
      choices=[
        "The rate of a reaction as proportional to the concentration of each "
        "reactant raised to a power",
        "The total amount of product a reaction will eventually produce from "
        "given amounts of reactant",
        "The energy that must be supplied before the reactants can be converted "
        "to products",
        "The ratio of product concentrations to reactant concentrations once "
        "the mixture stops changing",
        "The order in which the reactants are added to the vessel"],
      ans=0,
      why="EK 5.2.A.2, near verbatim: the rate law expresses the rate of a "
          "reaction as proportional to the concentration of each reactant raised "
          "to a power. Yield, energy and the final composition are separate "
          "questions."),

 dict(q=r"A reaction has the rate law \( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}] \). "
        "What is the order of the reaction with respect to A?",
      choices=["Second order", "First order", "Third order", "Zero order",
               "Half order"],
      ans=0,
      why="EK 5.2.A.3 states that the power of each reactant in the rate law is "
          "the order of the reaction with respect to that reactant. The exponent "
          "written on that concentration is the answer directly."),

 dict(q=r"For the rate law \( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}] \), what is "
        "the overall order of the reaction?",
      choices=["Third order", "Second order", "First order", "Fourth order",
               "Zero order"],
      ans=0,
      why="EK 5.2.A.3 states that the sum of the powers of the reactant "
          "concentrations in the rate law is the overall order of the reaction, "
          "so the two exponents are added."),

 dict(q="What is the proportionality constant in a rate law called, and what is "
        "it sensitive to?",
      choices=[
        "The rate constant, whose value is temperature dependent",
        "The rate constant, whose value depends on the concentrations of the "
        "reactants",
        "The equilibrium constant, whose value is fixed for a given reaction",
        "The order of the reaction, whose value is set by the coefficients of "
        "the balanced equation",
        "The activation constant, whose value depends on the container used"],
      ans=0,
      why="EK 5.2.A.4, near verbatim: the proportionality constant in the rate "
          "law is called the rate constant, and the value of this constant is "
          "temperature dependent. Concentration appears in the rate law "
          "separately, not inside the constant."),

 dict(q="Why do the units of a rate constant differ from one reaction to another?",
      choices=[
        "Because the units reflect the overall reaction order, which differs "
        "from reaction to reaction",
        "Because the units reflect the temperature at which the constant was "
        "measured",
        "Because the units reflect how many reactants appear in the balanced "
        "equation",
        "Because the units reflect whether the reaction is exothermic or "
        "endothermic",
        "Because the units are chosen by the experimenter and carry no chemical "
        "information"],
      ans=0,
      why="EK 5.2.A.4 states that the units of the rate constant reflect the "
          "overall reaction order. The rate itself always has units of "
          "concentration per time, so whatever concentration factors appear in "
          "the rate law fix what the constant's units must be."),

 dict(q="Which experimental approach is identified in the course framework as a "
        "method for determining the order with respect to each reactant?",
      choices=[
        "Comparing the initial rates of runs that differ in one reactant "
        "concentration at a time",
        "Adding the coefficients of the reactants in the balanced chemical "
        "equation",
        "Measuring how much product forms once the reaction has finished",
        "Measuring the temperature change of the mixture as the reaction "
        "proceeds",
        "Comparing the masses of the reactants weighed out at the start"],
      ans=0,
      why="EK 5.2.A.5, near verbatim: comparing initial rates of a reaction is a "
          "method to determine the order with respect to each reactant. Adding "
          "coefficients is not a method the framework offers for an overall "
          "reaction."),

 dict(q="The table gives initial-rate data for a reaction of A with B. What is "
        "the order of the reaction with respect to A?",
      table=_T_AB,
      choices=["First order", "Second order", "Zero order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.2.A.5 makes the comparison of initial rates the method. Two "
          "experiments in the table hold B fixed while A changes, so the factor "
          "by which the rate changes against the factor by which A changes gives "
          "the power."),

 dict(q="Using the same initial-rate table for A and B, what is the order of the "
        "reaction with respect to B?",
      table=_T_AB,
      choices=["Second order", "First order", "Zero order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.2.A.5 makes the comparison of initial rates the method for each "
          "reactant separately. Two experiments hold A fixed while B changes, "
          "and the rate changes by the square of the factor B does."),

 dict(q="From the same initial-rate table for A and B, what is the overall order "
        "of the reaction?",
      table=_T_AB,
      choices=["Third order", "Second order", "First order", "Fourth order",
               "Zero order"],
      ans=0,
      why="EK 5.2.A.3 makes the overall order the sum of the powers of the "
          "reactant concentrations, and each power is obtained from the paired "
          "comparisons EK 5.2.A.5 describes."),

 dict(q="Which rate law is consistent with the initial-rate data for A and B in "
        "the table?",
      table=_T_AB,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}]^{2} \), third order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}] \), third order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}] \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}]^{2} \), fourth order overall",
        r"\( \mathrm{rate} = k[\mathrm{B}]^{2} \), second order overall"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to each reactant concentration "
          "raised to a power, and EK 5.2.A.5 supplies the powers from the paired "
          "comparisons in the table, one reactant at a time."),

 dict(q="Using the initial-rate data for A and B, what is the numerical value of "
        "the rate constant?",
      table=_T_AB,
      choices=["2.0", "0.20", "0.020", "4.5", "0.80"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to the concentration factors, "
          "so once the powers are known the constant is the measured rate "
          "divided by those factors evaluated for that experiment."),

 dict(q="A reaction is found to be third order overall. Which units must its rate "
        "constant carry?",
      choices=[
        "Liters squared per mole squared per second",
        "Liters per mole per second",
        "Reciprocal seconds",
        "Moles per liter per second",
        "Moles squared per liter squared per second"],
      ans=0,
      why="EK 5.2.A.4 states that the units of the rate constant reflect the "
          "overall reaction order. The rate carries concentration per time, so "
          "the constant must carry whatever cancels three factors of "
          "concentration."),

 dict(q="The table gives initial-rate data for a reaction of X with Y. What is "
        "the order of the reaction with respect to Y?",
      table=_T_XY,
      choices=["Zero order", "First order", "Second order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.2.A.5 makes the comparison of initial rates the method. Two "
          "experiments hold X fixed while Y doubles, and the measured rate does "
          "not change at all, which is what a power of zero means."),

 dict(q="Using the same initial-rate table for X and Y, what is the order with "
        "respect to X?",
      table=_T_XY,
      choices=["Second order", "First order", "Zero order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.2.A.5 makes the comparison of initial rates the method. Two "
          "experiments hold Y fixed while X doubles, and the rate rises by a "
          "factor of four, which is two raised to the power in question."),

 dict(q="Which rate law is consistent with the initial-rate data for X and Y?",
      table=_T_XY,
      choices=[
        r"\( \mathrm{rate} = k[\mathrm{X}]^{2} \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{X}]^{2}[\mathrm{Y}] \), third order overall",
        r"\( \mathrm{rate} = k[\mathrm{X}][\mathrm{Y}] \), second order overall",
        r"\( \mathrm{rate} = k[\mathrm{X}][\mathrm{Y}]^{2} \), third order overall",
        r"\( \mathrm{rate} = k[\mathrm{Y}]^{2} \), second order overall"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to each reactant concentration "
          "raised to a power, and a power of zero removes that reactant from the "
          "expression because any concentration raised to zero is one."),

 dict(q="For the X and Y reaction, what is the numerical value of the rate "
        "constant implied by the table?",
      table=_T_XY,
      choices=["0.40", "4.0", "0.080", "0.0040", "1.6"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to the concentration factors "
          "in the rate law, so the constant is a measured rate divided by those "
          "factors evaluated for the same experiment."),

 dict(q="A reaction is second order with respect to a reactant. If the "
        "concentration of that reactant is doubled and nothing else changes, "
        "what happens to the rate?",
      choices=[
        "It becomes four times as large",
        "It becomes twice as large",
        "It is unchanged",
        "It becomes eight times as large",
        "It becomes half as large"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to the concentration raised to "
          "a power, and EK 5.2.A.3 makes that power the order. Doubling a "
          "concentration that enters squared multiplies the rate by two raised "
          "to the second power."),

 dict(q="A reaction is zero order with respect to one of its reactants. What does "
        "that imply?",
      choices=[
        "Changing the concentration of that reactant leaves the rate unchanged",
        "That reactant is not consumed during the reaction",
        "The overall order of the reaction must also be zero",
        "The rate constant for the reaction must be zero",
        "The reaction cannot proceed until that reactant is entirely used up"],
      ans=0,
      why="EK 5.2.A.3 makes the power in the rate law the order with respect to "
          "that reactant, and EK 5.2.A.2 makes the rate proportional to the "
          "concentration raised to that power. Any concentration raised to the "
          "power zero is one, so the factor drops out."),

 dict(q="A reaction is first order overall. Which units must its rate constant "
        "carry?",
      choices=[
        "Reciprocal seconds, that is one over a second",
        "Moles per liter per second",
        "Liters per mole per second",
        "Liters squared per mole squared per second",
        "Moles per second"],
      ans=0,
      why="EK 5.2.A.4 states that the units of the rate constant reflect the "
          "overall reaction order. A rate carries concentration per time and one "
          "concentration factor appears in the rate law, so those two "
          "concentrations cancel."),

 dict(q="The table gives the rate constant measured for one reaction at three "
        "temperatures. Which statement is supported?",
      table=_T_KT,
      choices=[
        "The value of the rate constant rises as the temperature rises, which is "
        "the temperature dependence the framework attributes to it",
        "The rate constant is unchanged by temperature, and the small "
        "differences are experimental scatter",
        "The rate constant falls as the temperature rises, because warm mixtures "
        "are more dilute",
        "The rate constant depends on the concentrations used, which must have "
        "differed among the three measurements",
        "No statement can be made, because a rate constant has no numerical "
        "value until an order is known"],
      ans=0,
      why="EK 5.2.A.4 states that the value of the rate constant is temperature "
          "dependent. The table holds the reaction fixed and varies only the "
          "temperature, and the tabulated values move together with it."),

 dict(q="The table gives initial-rate data for a reaction of A, B and C. What is "
        "the order with respect to C?",
      table=_T_THREE,
      choices=["Second order", "First order", "Zero order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.2.A.5 makes the comparison of initial rates the method. One pair "
          "of experiments holds A and B fixed while C doubles, and the rate rises "
          "by a factor of four."),

 dict(q="Using the same three-reactant table, what is the overall order of the "
        "reaction?",
      table=_T_THREE,
      choices=["Third order", "Second order", "First order", "Fourth order",
               "Zero order"],
      ans=0,
      why="EK 5.2.A.3 makes the overall order the sum of the powers of the "
          "reactant concentrations, and EK 5.2.A.5 supplies each power from the "
          "pair of experiments in which only that reactant changes."),

 dict(q="From the same three-reactant table, which pair of experiments should be "
        "compared to find the order with respect to B?",
      table=_T_THREE,
      choices=[
        "The first and third experiments, in which only the concentration of B "
        "differs",
        "The first and second experiments, in which only the concentration of A "
        "differs",
        "The second and fourth experiments, in which two concentrations differ "
        "at once",
        "The third and fourth experiments, in which two concentrations differ at "
        "once",
        "All four experiments together, since every order requires the whole "
        "data set"],
      ans=0,
      why="EK 5.2.A.5 determines the order with respect to each reactant by "
          "comparing initial rates, and the comparison is informative only when "
          "one concentration changes and the others are held fixed."),

 dict(q="What must an experimenter be able to do in order to determine a rate law "
        "at all?",
      choices=[
        "Monitor the amounts of reactants or products over time so that a rate "
        "can be measured",
        "Predict the products of the reaction from the identities of the "
        "reactants",
        "Measure the total energy released when the reaction finishes",
        "Prepare all reactants at exactly the same concentration",
        "Run the reaction until every reactant has been consumed"],
      ans=0,
      why="EK 5.2.A.1 states that experimental methods can be used to monitor "
          "the amounts of reactants and/or products over time and to determine "
          "the rate of the reaction, which is the measurement every later step "
          "rests on."),

 dict(q="A student writes that the rate law for the overall reaction 2 A + B → C "
        r"must be \( \mathrm{rate} = k[\mathrm{A}]^{2}[\mathrm{B}] \) because those are "
        "the coefficients. Which response is best?",
      choices=[
        "The powers must be found from experimental data, since the framework "
        "obtains them by comparing initial rates",
        "The student is correct, because the coefficients of an equation are "
        "always the powers in its rate law",
        "The student is correct only if the reaction is exothermic",
        "The powers cannot be found at all for a reaction with two reactants",
        "The powers are the coefficients divided by the number of reactants"],
      ans=0,
      why="EK 5.2.A.1 has the rate determined by experiment and EK 5.2.A.5 makes "
          "comparing initial rates the method for finding each order. Nothing in "
          "either statement licenses reading the powers off the balanced "
          "equation."),

 dict(q=r"For a reaction with the rate law \( \mathrm{rate} = k[\mathrm{A}][\mathrm{B}]^{2} \), "
        "the concentration of B is tripled while that of A is held constant. By "
        "what factor does the rate change?",
      choices=["9", "3", "6", "27", "1"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to each concentration raised "
          "to its power, so multiplying a concentration by a factor multiplies "
          "the rate by that factor raised to the corresponding power."),

 dict(q="The table lists four overall reaction orders with the units a rate "
        "constant carries for each. Which pairing is correct for a reaction whose "
        "rate does not change when any concentration is altered?",
      table=_T_UNITS,
      choices=[
        "Zero order, with the rate constant carrying moles per liter per second",
        "First order, with the rate constant carrying per second",
        "Second order, with the rate constant carrying liters per mole per "
        "second",
        "Third order, with the rate constant carrying liters squared per mole "
        "squared per second",
        "None of them, because a rate constant always carries the same units"],
      ans=0,
      why="EK 5.2.A.3 makes the order the power on a concentration, so a rate "
          "unaffected by every concentration has every power at zero and an "
          "overall order of zero. EK 5.2.A.4 then makes the constant's units "
          "those of the rate itself."),

 dict(q="Two runs of the same reaction are carried out at the same temperature "
        "with different starting concentrations. What is true of the rate "
        "constant in the two runs?",
      choices=[
        "It has the same value in both, because the constant depends on "
        "temperature rather than on concentration",
        "It is larger in the run with the larger concentrations, because the "
        "rate is larger there",
        "It is smaller in the run with the larger concentrations, because the "
        "reactants are consumed faster",
        "It cannot be compared, because a rate constant applies to only one set "
        "of concentrations",
        "It has different units in the two runs, because the rates differ"],
      ans=0,
      why="EK 5.2.A.4 states that the value of the rate constant is temperature "
          "dependent. Concentration enters the rate law through the "
          "concentration factors of EK 5.2.A.2, not through the constant."),

 dict(q="A rate law is found to be first order in one reactant and first order in "
        "a second reactant. If both concentrations are doubled at once, what "
        "happens to the rate?",
      choices=[
        "It becomes four times as large, because each doubling contributes a "
        "factor of two",
        "It becomes twice as large, because the two effects are averaged",
        "It is unchanged, because the two doublings cancel",
        "It becomes eight times as large, because the overall order is three",
        "It cannot be predicted without knowing the rate constant"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to the product of the "
          "concentration factors, so multiplying two of them each by two "
          "multiplies the whole product by their product."),

 dict(q="Why does the framework describe a rate law as expressing the rate as "
        "PROPORTIONAL to concentrations rather than as equal to them?",
      choices=[
        "Because a constant of proportionality is needed to relate the "
        "concentration factors to a rate with its own units",
        "Because the rate is only approximately related to the concentrations",
        "Because the concentrations are measured less accurately than the rate",
        "Because proportionality allows the powers to change during the reaction",
        "Because the rate and the concentrations are always numerically equal in "
        "any case"],
      ans=0,
      why="EK 5.2.A.2 makes the rate proportional to the concentrations raised "
          "to powers, and EK 5.2.A.4 names the proportionality constant the rate "
          "constant and states that its units reflect the overall order, which "
          "is exactly the role a proportionality constant plays."),
]
