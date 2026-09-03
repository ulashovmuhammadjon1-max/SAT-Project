# AP CHEMISTRY 5.3 Concentration Changes Over Time
# CED effective Fall 2024, Unit 5 Kinetics.
# Learning objective 5.3.A: identify the rate law expression of a chemical
# reaction using data that show how the concentrations of reaction species
# change over time. Suggested skill 5.B, identify an appropriate theory,
# definition, or mathematical relationship to solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   5.3.A.1  The order of a reaction can be inferred from a graph of
#            concentration of reactant versus time.
#   5.3.A.2  If a reaction is first order with respect to a reactant being
#            monitored, a plot of the natural log (ln) of the reactant
#            concentration as a function of time will be linear.
#   5.3.A.3  If a reaction is second order with respect to a reactant being
#            monitored, a plot of the reciprocal of the concentration of that
#            reactant versus time will be linear.
#   5.3.A.4  The slopes of the concentration versus time data for zeroth, first,
#            and second order reactions can be used to determine the rate
#            constant for the reaction.
#              Zeroth order:  [A]t - [A]0 = -kt
#              First order:   ln[A]t - ln[A]0 = -kt
#              Second order:  1/[A]t - 1/[A]0 = kt
#   5.3.A.5  Half-life is a critical parameter for first order reactions because
#            the half-life is constant and related to the rate constant for the
#            reaction by the equation t(1/2) = 0.693/k.
#   5.3.A.6  Radioactive decay processes provide an important illustration of
#            first order kinetics.
#
# NO GRAPHS, AND THAT IS THE POINT. 5.3.A.1 to 5.3.A.3 are all stated in terms
# of plots and the bank cannot carry a figure, so every "which plot is linear"
# item here is a TABLE carrying the concentration, its natural log and its
# reciprocal side by side at each time. The student reads which column has
# constant differences, which is exactly what linearity against evenly spaced
# times means, and the verifier recomputes those differences.
#
# THE HALF-LIFE CLAIM IS THE FRAMEWORK'S, NOT A GENERALISATION OF IT. 5.3.A.5
# says half-life is a critical parameter FOR FIRST ORDER REACTIONS BECAUSE it is
# constant. Items keying on a half-life being constant therefore say "first
# order" in the stem or establish it from data first.
#
# NOTATION. Chemistry is not typeset, so the three integrated equations and the
# half-life relation are hand-written \( ... \) spans.
TOPIC = ("5.3", "Concentration Changes Over Time", 5)

_T_FIRST = dict(
    headers=["Time (seconds)", "Concentration of A (moles per liter)",
             "Natural log of the concentration",
             "Reciprocal of the concentration (liters per mole)"],
    rows=[["0", "0.800", "-0.223", "1.25"],
          ["10", "0.400", "-0.916", "2.50"],
          ["20", "0.200", "-1.609", "5.00"],
          ["30", "0.100", "-2.303", "10.0"],
          ["40", "0.050", "-2.996", "20.0"]])

_T_SECOND = dict(
    headers=["Time (seconds)", "Concentration of B (moles per liter)",
             "Natural log of the concentration",
             "Reciprocal of the concentration (liters per mole)"],
    rows=[["0", "0.500", "-0.693", "2.00"],
          ["50", "0.333", "-1.100", "3.00"],
          ["100", "0.250", "-1.386", "4.00"],
          ["150", "0.200", "-1.609", "5.00"],
          ["200", "0.167", "-1.790", "6.00"]])

_T_ZEROTH = dict(
    headers=["Time (seconds)", "Concentration of D (moles per liter)",
             "Natural log of the concentration",
             "Reciprocal of the concentration (liters per mole)"],
    rows=[["0", "0.800", "-0.223", "1.25"],
          ["30", "0.650", "-0.431", "1.54"],
          ["60", "0.500", "-0.693", "2.00"],
          ["90", "0.350", "-1.050", "2.86"],
          ["120", "0.200", "-1.609", "5.00"]])

_T_WHICHPLOT = dict(
    headers=["Reaction", "The plot found to be a straight line against time"],
    rows=[["R1", "The natural log of the reactant concentration"],
          ["R2", "The reciprocal of the reactant concentration"],
          ["R3", "The reactant concentration itself"]])

_T_DECAY = dict(
    headers=["Number of half-lives elapsed", "Fraction of the sample remaining"],
    rows=[["1", "one half"],
          ["2", "one quarter"],
          ["3", "one eighth"],
          ["4", "one sixteenth"]])

QUESTIONS = [

 dict(q="What can be inferred from data showing how the concentration of a "
        "reactant changes over the course of a reaction?",
      choices=[
        "The order of the reaction with respect to that reactant",
        "The total energy released by the reaction",
        "The identity of every product the reaction forms",
        "The temperature at which the reaction was carried out",
        "The number of reactants that take part in the reaction"],
      ans=0,
      why="EK 5.3.A.1 states that the order of a reaction can be inferred from a "
          "graph of concentration of reactant versus time. Energy, product "
          "identity and temperature are not read off such data."),

 dict(q="For a reaction that is first order with respect to the reactant being "
        "monitored, which quantity plotted against time gives a straight line?",
      choices=[
        "The natural log of the reactant concentration",
        "The reactant concentration itself",
        "The reciprocal of the reactant concentration",
        "The square of the reactant concentration",
        "The square root of the reactant concentration"],
      ans=0,
      why="EK 5.3.A.2, near verbatim: if a reaction is first order with respect "
          "to a reactant being monitored, a plot of the natural log of the "
          "reactant concentration as a function of time will be linear."),

 dict(q="For a reaction that is second order with respect to the reactant being "
        "monitored, which quantity plotted against time gives a straight line?",
      choices=[
        "The reciprocal of the reactant concentration",
        "The natural log of the reactant concentration",
        "The reactant concentration itself",
        "The square of the reactant concentration",
        "The product of the concentration and the time"],
      ans=0,
      why="EK 5.3.A.3, near verbatim: if a reaction is second order with respect "
          "to a reactant being monitored, a plot of the reciprocal of the "
          "concentration of that reactant versus time will be linear."),

 dict(q="Which relationship does the course framework give for a zeroth order "
        "reaction?",
      choices=[
        r"\( [\mathrm{A}]_t - [\mathrm{A}]_0 = -kt \), the concentration itself "
        "falling linearly with time",
        r"\( \ln[\mathrm{A}]_t - \ln[\mathrm{A}]_0 = -kt \), the natural log "
        "falling linearly with time",
        r"\( \frac{1}{[\mathrm{A}]_t} - \frac{1}{[\mathrm{A}]_0} = kt \), the "
        "reciprocal rising linearly with time",
        r"\( t_{1/2} = \frac{0.693}{k} \), the half-life fixed by the rate "
        "constant",
        r"\( [\mathrm{A}]_t = [\mathrm{A}]_0 \), the concentration unchanged by "
        "the passage of time"],
      ans=0,
      why="EK 5.3.A.4 prints the zeroth order relationship as the difference of "
          "the concentrations equalling the negative of the rate constant times "
          "the time, which is a straight line in the concentration itself."),

 dict(q="The table gives the concentration of A, its natural log and its "
        "reciprocal at five evenly spaced times. What is the order of this "
        "reaction with respect to A?",
      table=_T_FIRST,
      choices=["First order", "Zero order", "Second order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.3.A.2 makes a linear plot of the natural log against time the "
          "mark of first order behavior. At evenly spaced times a column is "
          "linear when its successive differences are constant, and only the "
          "natural log column has that property here."),

 dict(q="Using the same table of A concentrations, what is the value of the rate "
        "constant?",
      table=_T_FIRST,
      choices=["0.0693 per second", "0.693 per second", "0.00693 per second",
               "0.0347 per second", "0.139 per second"],
      ans=0,
      why="EK 5.3.A.4 states that the slopes of the concentration versus time "
          "data can be used to determine the rate constant, and for first order "
          "the relationship is the difference of the natural logs equalling the "
          "negative of the constant times the elapsed time."),

 dict(q="From the same table of A concentrations, what is the half-life of this "
        "reaction?",
      table=_T_FIRST,
      choices=["10 seconds", "20 seconds", "5 seconds", "40 seconds",
               "0.693 seconds"],
      ans=0,
      why="EK 5.3.A.5 makes the half-life a critical parameter for first order "
          "reactions because it is constant. The tabulated concentrations show "
          "the same interval taking the concentration from each value to half of "
          "it, over and over."),

 dict(q="The table gives the concentration of B, its natural log and its "
        "reciprocal at five evenly spaced times. What is the order of this "
        "reaction with respect to B?",
      table=_T_SECOND,
      choices=["Second order", "First order", "Zero order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.3.A.3 makes a linear plot of the reciprocal against time the "
          "mark of second order behavior, and at evenly spaced times only the "
          "reciprocal column here has constant successive differences."),

 dict(q="Using the same table of B concentrations, what is the value of the rate "
        "constant?",
      table=_T_SECOND,
      choices=["0.0200 liters per mole per second",
               "0.200 liters per mole per second",
               "0.00200 liters per mole per second",
               "0.0500 liters per mole per second",
               "2.00 liters per mole per second"],
      ans=0,
      why="EK 5.3.A.4 gives the second order relationship as the difference of "
          "the reciprocals equalling the rate constant times the elapsed time, "
          "so the constant is the slope of the reciprocal column against time."),

 dict(q="The table gives the concentration of D, its natural log and its "
        "reciprocal at five evenly spaced times. What is the order of this "
        "reaction with respect to D?",
      table=_T_ZEROTH,
      choices=["Zero order", "First order", "Second order", "Third order",
               "Half order"],
      ans=0,
      why="EK 5.3.A.4 gives the zeroth order relationship as the concentration "
          "difference equalling the negative of the rate constant times the "
          "time, which makes the concentration column itself linear. Only that "
          "column has constant successive differences here."),

 dict(q="Using the same table of D concentrations, what is the value of the rate "
        "constant?",
      table=_T_ZEROTH,
      choices=["0.00500 moles per liter per second",
               "0.0500 moles per liter per second",
               "0.150 moles per liter per second",
               "0.000500 moles per liter per second",
               "0.0250 moles per liter per second"],
      ans=0,
      why="EK 5.3.A.4 states that the slopes of the concentration versus time "
          "data determine the rate constant, and for zeroth order the "
          "concentration falls by the constant times the elapsed time."),

 dict(q="A first order reaction has a rate constant of 0.0231 per second. What is "
        "its half-life?",
      choices=["30. seconds", "3.0 seconds", "300 seconds", "15 seconds",
               "0.016 seconds"],
      ans=0,
      why=r"EK 5.3.A.5 relates the half-life of a first order reaction to its "
          r"rate constant by \( t_{1/2} = \frac{0.693}{k} \), so dividing the "
          "constant 0.693 by the given rate constant gives the half-life "
          "directly."),

 dict(q="A first order reaction has a half-life of 20. seconds. What is its rate "
        "constant?",
      choices=["0.0347 per second", "0.347 per second", "0.00347 per second",
               "0.0693 per second", "13.9 per second"],
      ans=0,
      why=r"EK 5.3.A.5 gives \( t_{1/2} = \frac{0.693}{k} \) for a first order "
          "reaction, so rearranging makes the rate constant the ratio of 0.693 "
          "to the half-life."),

 dict(q="Why is half-life described as a critical parameter for first order "
        "reactions in particular?",
      choices=[
        "Because for a first order reaction the half-life is constant and fixed "
        "by the rate constant alone",
        "Because only a first order reaction is ever half finished at some point "
        "in time",
        "Because a first order reaction is the only kind whose rate constant can "
        "be measured",
        "Because the half-life of a first order reaction depends on how much "
        "reactant was present at the start",
        "Because a first order reaction always has a half-life of 0.693 seconds"],
      ans=0,
      why="EK 5.3.A.5, near verbatim: half-life is a critical parameter for "
          "first order reactions BECAUSE the half-life is constant and related "
          "to the rate constant by the equation given. Being constant is the "
          "property that makes it useful."),

 dict(q="A first order reaction is allowed to run for exactly three half-lives. "
        "What fraction of the original reactant remains?",
      choices=["One eighth", "One third", "One sixth", "One sixteenth",
               "Three quarters"],
      ans=0,
      why="EK 5.3.A.5 makes the half-life of a first order reaction constant, so "
          "each successive half-life leaves half of whatever was present at its "
          "start, and the fractions multiply."),

 dict(q="A first order reaction has a half-life of 25 seconds. How long does it "
        "take for the reactant concentration to fall to one sixteenth of its "
        "starting value?",
      choices=["100 seconds", "50 seconds", "75 seconds", "400 seconds",
               "25 seconds"],
      ans=0,
      why="EK 5.3.A.5 makes the half-life constant for a first order reaction, "
          "so reaching one sixteenth requires however many successive halvings "
          "multiply to that fraction, each taking the same time."),

 dict(q="Which physical process does the course framework offer as an important "
        "illustration of first order kinetics?",
      choices=[
        "Radioactive decay",
        "The dissolution of an ionic solid in water",
        "The boiling of a pure liquid at constant pressure",
        "The neutralization of a strong acid by a strong base",
        "The precipitation of an insoluble salt"],
      ans=0,
      why="EK 5.3.A.6, near verbatim: radioactive decay processes provide an "
          "important illustration of first order kinetics."),

 dict(q="A radioactive isotope has a half-life of 8 days. A sample initially "
        "contains 40. grams of the isotope. How much remains after 24 days?",
      choices=["5.0 grams", "10. grams", "13 grams", "20. grams", "2.5 grams"],
      ans=0,
      why="EK 5.3.A.6 makes radioactive decay an illustration of first order "
          "kinetics, and EK 5.3.A.5 makes the half-life of such a process "
          "constant, so each successive interval of one half-life leaves half of "
          "what was there."),

 dict(q="Which relationship does the course framework give for a second order "
        "reaction?",
      choices=[
        r"\( \frac{1}{[\mathrm{A}]_t} - \frac{1}{[\mathrm{A}]_0} = kt \), the "
        "reciprocal rising linearly with time",
        r"\( \ln[\mathrm{A}]_t - \ln[\mathrm{A}]_0 = -kt \), the natural log "
        "falling linearly with time",
        r"\( [\mathrm{A}]_t - [\mathrm{A}]_0 = -kt \), the concentration itself "
        "falling linearly with time",
        r"\( t_{1/2} = \frac{0.693}{k} \), the half-life fixed by the rate "
        "constant",
        r"\( [\mathrm{A}]_t = 2[\mathrm{A}]_0 \), the concentration doubling "
        "with time"],
      ans=0,
      why="EK 5.3.A.4 prints the second order relationship as the difference of "
          "the reciprocals of the concentrations equalling the rate constant "
          "times the time, which is a straight line in the reciprocal."),

 dict(q="A plot of the natural log of a reactant concentration against time is "
        "found to be a straight line with a negative slope. What does the "
        "magnitude of that slope equal?",
      choices=[
        "The rate constant for the reaction",
        "The half-life of the reaction",
        "The initial concentration of the reactant",
        "The overall order of the reaction",
        "The reciprocal of the initial concentration"],
      ans=0,
      why="EK 5.3.A.4 gives the first order relationship as the difference of "
          "the natural logs equalling the negative of the rate constant times "
          "the elapsed time, so the slope of that line is the negative of the "
          "rate constant."),

 dict(q="A plot of the reciprocal of a reactant concentration against time is a "
        "straight line with a positive slope. What does that slope equal?",
      choices=[
        "The rate constant for the reaction",
        "The negative of the rate constant",
        "The half-life of the reaction",
        "The initial concentration of the reactant",
        "The natural log of the rate constant"],
      ans=0,
      why="EK 5.3.A.4 gives the second order relationship as the difference of "
          "the reciprocals equalling the rate constant times the time, with no "
          "negative sign, so the slope is the constant itself."),

 dict(q="The table records, for three reactions, which plot against time turned "
        "out to be a straight line. What are the orders of the three reactions?",
      table=_T_WHICHPLOT,
      choices=[
        "R1 is first order, R2 is second order, and R3 is zero order",
        "R1 is zero order, R2 is first order, and R3 is second order",
        "R1 is second order, R2 is first order, and R3 is zero order",
        "R1 is first order, R2 is zero order, and R3 is second order",
        "All three are first order, because each gave a straight line"],
      ans=0,
      why="EK 5.3.A.2 assigns the linear natural log plot to first order and EK "
          "5.3.A.3 assigns the linear reciprocal plot to second order, while EK "
          "5.3.A.4's zeroth order equation makes the concentration itself linear."),

 dict(q="Two samples of the same first order reaction are prepared, one at twice "
        "the starting concentration of the other. How do their half-lives "
        "compare?",
      choices=[
        "They are equal, because the half-life of a first order reaction is "
        "fixed by the rate constant alone",
        "The more concentrated sample has the longer half-life, because it has "
        "more to consume",
        "The more concentrated sample has the shorter half-life, because its "
        "rate is larger",
        "They cannot be compared without knowing the temperature of each sample",
        "The more concentrated sample has twice the half-life of the other"],
      ans=0,
      why=r"EK 5.3.A.5 states that for a first order reaction the half-life is "
          r"constant and related to the rate constant by \( t_{1/2} = "
          r"\frac{0.693}{k} \) . The starting concentration does not appear in "
          "that relationship."),

 dict(q="A student measures a reactant concentration at several times and finds "
        "that neither the concentration nor its natural log gives a straight "
        "line, but the reciprocal does. What should the student conclude?",
      choices=[
        "The reaction is second order with respect to that reactant",
        "The reaction is first order with respect to that reactant",
        "The reaction is zero order with respect to that reactant",
        "The measurements must contain an error, because one of the other two "
        "plots should have been linear",
        "The order cannot be determined without also measuring the temperature"],
      ans=0,
      why="EK 5.3.A.3 states that a plot of the reciprocal of the concentration "
          "versus time is linear when the reaction is second order with respect "
          "to the reactant being monitored, which is precisely the observation "
          "described."),

 dict(q="A zeroth order reaction starts at 0.600 moles per liter and has a rate "
        "constant of 0.0100 moles per liter per second. What is the "
        "concentration after 40. seconds?",
      choices=["0.200 moles per liter", "0.400 moles per liter",
               "0.240 moles per liter", "0.560 moles per liter",
               "0.024 moles per liter"],
      ans=0,
      why=r"EK 5.3.A.4 gives the zeroth order relationship \( [\mathrm{A}]_t - "
          r"[\mathrm{A}]_0 = -kt \) , so the concentration falls from its "
          "starting value by the rate constant multiplied by the elapsed time."),

 dict(q="The table lists the fraction of a sample remaining after successive "
        "half-lives. Which reading tells a student how many half-lives have "
        "passed once one sixteenth of a sample remains?",
      table=_T_DECAY,
      choices=[
        "Four half-lives, the entry paired with one sixteenth in the table",
        "Sixteen half-lives, because the fraction names the number",
        "Two half-lives, because one sixteenth is the square of one quarter",
        "Eight half-lives, because one eighth appears earlier in the table",
        "One half-life, because every decay is complete after one"],
      ans=0,
      why="EK 5.3.A.5 makes the half-life of a first order process constant, so "
          "each successive half-life multiplies the remaining fraction by one "
          "half and the table simply records those products."),

 dict(q="What must be measured in order to use any of the three integrated "
        "relationships the framework gives?",
      choices=[
        "The concentration of the monitored reactant at known times",
        "The temperature of the mixture at the moment the reaction ends",
        "The mass of every product formed during the reaction",
        "The volume of the vessel in which the reaction is carried out",
        "The identity of the catalyst, if any, that is present"],
      ans=0,
      why="EK 5.3.A.1 has the order inferred from concentration versus time "
          "data, and each equation in EK 5.3.A.4 relates a concentration at time "
          "t to the concentration at time zero, so a set of concentrations with "
          "their times is what all of them need."),

 dict(q="For a first order reaction the natural log of the concentration falls "
        "from -1.20 to -2.58 over 60. seconds. What is the rate constant?",
      choices=["0.0230 per second", "0.0430 per second", "0.230 per second",
               "0.0138 per second", "0.0630 per second"],
      ans=0,
      why=r"EK 5.3.A.4 gives \( \ln[\mathrm{A}]_t - \ln[\mathrm{A}]_0 = -kt \) "
          "for a first order reaction, so the rate constant is the fall in the "
          "natural log divided by the elapsed time."),

 dict(q="Why does the framework single out concentration versus time data as the "
        "route to a reaction order?",
      choices=[
        "Because the way concentration changes with time differs between zeroth, "
        "first and second order reactions in a way that a plot reveals",
        "Because concentration is the only property of a reaction mixture that "
        "can be measured",
        "Because the order of a reaction changes as the reaction proceeds",
        "Because the time axis of a plot is the only place a rate constant can "
        "appear",
        "Because concentration versus time data also give the energy change of "
        "the reaction"],
      ans=0,
      why="EK 5.3.A.1 states that the order can be inferred from a graph of "
          "concentration of reactant versus time, and EK 5.3.A.2 to 5.3.A.4 give "
          "three different functions of the concentration, one of which is "
          "linear for each order."),

 dict(q="A first order reaction and a second order reaction are each monitored "
        "and each is found to have a well defined time for the first halving of "
        "its reactant. What distinguishes the two as the reactions continue?",
      choices=[
        "Only the first order reaction takes the same time for each successive "
        "halving",
        "Only the second order reaction takes the same time for each successive "
        "halving",
        "Both take the same time for each successive halving",
        "Neither takes a well defined time for any halving after the first",
        "The two take the same time as each other for every halving"],
      ans=0,
      why="EK 5.3.A.5 makes the half-life a critical parameter FOR FIRST ORDER "
          "REACTIONS because it is constant, which distinguishes them from the "
          "other orders; it is the constancy, not the existence of a first "
          "halving, that the framework attaches to first order."),
]
