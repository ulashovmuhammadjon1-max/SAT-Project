# AP CHEMISTRY 7.7 Calculating Equilibrium Concentrations
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.7.A: identify the concentrations or partial pressures of chemical
# species at equilibrium based on the initial conditions and the equilibrium constant.
# Suggested skill 3.A, represent chemical phenomena using appropriate graphing
# techniques.
#
# Essential knowledge relied on, in the framework's own words:
#   7.7.A.1  The concentrations or partial pressures of species at equilibrium can be
#            predicted given the balanced reaction, initial concentrations, and the
#            appropriate K.
#   7.7.A.2  When Q < K, the reaction will proceed with a net consumption of reactants
#            and generation of products. When Q > K, the reaction will proceed with a net
#            consumption of products and generation of reactants. When Q = K, the system
#            is at dynamic equilibrium; both forward and reverse reactions proceed at the
#            same rate, and the proportion of reactants and products remains constant.
#
# SCOPE. 7.6 owns the algebra of manipulating K; 7.10 owns what a DISTURBANCE to a system
# already at equilibrium does to Q and K. Everything below starts from a stated initial
# condition and a stated K and asks for the equilibrium amounts, or compares a computed Q
# with K for a mixture that has not been disturbed. No item here mentions a stress
# applied to an equilibrium.
#
# ARITHMETIC. Every equilibrium amount below comes out exact in one or two
# calculator-free steps, and every one is recomputed in verify_h7_7.py from the balanced
# equation, the initial concentrations and K alone -- never asserted.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span is
# hand-written. Formulas and bracketed concentrations stay plain text; only scientific
# notation is set in a span.
TOPIC = ("7.7", "Calculating Equilibrium Concentrations", 7)

_T_MIXTURES = dict(
    headers=["Mixture", "[A] (M)", "[B] (M)"],
    rows=[["1", "0.40", "0.20"],
          ["2", "0.10", "0.50"],
          ["3", "0.25", "0.50"]])

_T_HI = dict(
    headers=["Vessel", "[H2] (M)", "[I2] (M)", "[HI] (M)"],
    rows=[["W", "0.10", "0.20", "0.40"],
          ["X", "0.20", "0.20", "0.80"],
          ["Y", "0.50", "0.50", "0.50"]])

_T_ICE = dict(
    headers=["Stage", "[A] (M)", "[B] (M)"],
    rows=[["Initial", "1.00", "0"],
          ["Change", "minus x", "plus x"],
          ["Equilibrium", "1.00 minus x", "x"]])

_T_PRESSURES = dict(
    headers=["Trial", "Partial pressure of A (atm)", "Partial pressure of B (atm)"],
    rows=[["1", "2.00", "4.00"],
          ["2", "0.50", "2.00"],
          ["3", "4.00", "2.00"]])

QUESTIONS = [

 dict(q="For the reaction A(g) to B(g) the equilibrium constant is 4.0. A vessel is "
        "charged with A(g) at 1.00 M and no B(g). What is the concentration of B(g) once "
        "equilibrium is reached?",
      choices=["[B] = 0.80 M", "[B] = 0.20 M", "[B] = 0.50 M", "[B] = 4.00 M",
               "[B] = 0.25 M"],
      ans=0,
      why="EK 7.7.A.1 makes the equilibrium amounts predictable from the balanced "
          "reaction, the initial concentration and K. Letting x be the amount of A "
          "converted, x divided by 1.00 minus x equals 4.0, so x is 0.80 M of B and "
          "0.20 M of A remains."),

 dict(q="A vessel initially holds only C(g) at 1.00 M for the reaction C(g) to D(g), "
        "whose equilibrium constant is 0.25. What is the concentration of C(g) at "
        "equilibrium?",
      choices=["[C] = 0.80 M", "[C] = 0.20 M", "[C] = 0.25 M", "[C] = 0.75 M",
               "[C] = 0.50 M"],
      ans=0,
      why="Under EK 7.7.A.1, x divided by 1.00 minus x equals 0.25, so x is 0.20 M of D "
          "and the remaining C is 0.80 M. A constant smaller than one leaves more "
          "reactant than product, which is the check on the answer."),

 dict(q="For the reaction H2(g) + I2(g) to 2 HI(g) the equilibrium constant is 36. Equal "
        "amounts of H2(g) and I2(g), each at 1.00 M, are placed in a vessel with no "
        "HI(g). What is the concentration of HI(g) at equilibrium?",
      choices=["[HI] = 1.50 M", "[HI] = 0.75 M", "[HI] = 0.25 M", "[HI] = 1.00 M",
               "[HI] = 2.00 M"],
      ans=0,
      why="Because the two reactants start equal, the equilibrium expression reduces to "
          "twice x divided by 1.00 minus x equals the square root of 36, which is six. "
          "That gives x equal to 0.75 M, so HI is twice that, 1.50 M, and each reactant "
          "is 0.25 M, as EK 7.7.A.1 allows to be predicted."),

 dict(q="A mixture is prepared for the reaction A(g) to B(g), whose equilibrium constant "
        "is 2.0. Using mixture 1 in the table, in which direction will there be net "
        "reaction?",
      table=_T_MIXTURES,
      choices=[
        "Net forward reaction, because Q is 0.50, which is less than K",
        "Net reverse reaction, because Q is 2.00, which is greater than K",
        "No net reaction, because Q equals K for this mixture",
        "Net reverse reaction, because Q is 0.50, which is less than K",
        "Net forward reaction, because Q is 2.00, which is greater than K"],
      ans=0,
      why="Q for mixture 1 is 0.20 divided by 0.40, which is 0.50. EK 7.7.A.2 states "
          "that when Q is less than K the reaction proceeds with a net consumption of "
          "reactants and generation of products, so net reaction runs forward."),

 dict(q="Using mixture 2 in the same table and the same equilibrium constant of 2.0 for "
        "A(g) to B(g), what will happen in that mixture?",
      table=_T_MIXTURES,
      choices=[
        "Net reverse reaction, because Q is 5.0 and exceeds K",
        "Net forward reaction, because Q is 5.0 and exceeds K",
        "Net forward reaction, because Q is 0.20 and is below K",
        "No net reaction, because Q equals K in this mixture",
        "Net reverse reaction, because Q is 0.20 and is below K"],
      ans=0,
      why="Q for mixture 2 is 0.50 divided by 0.10, which is 5.0, and that exceeds the "
          "value 2.0. EK 7.7.A.2 states that when Q is greater than K the reaction "
          "proceeds with a net consumption of products and generation of reactants."),

 dict(q="Mixture 3 in the table is examined at the same temperature, where the "
        "equilibrium constant for A(g) to B(g) is 2.0. Which statement about mixture 3 "
        "is correct?",
      table=_T_MIXTURES,
      choices=[
        "It is already at equilibrium, and the forward and reverse reactions proceed at "
        "the same rate",
        "It is already at equilibrium, and both the forward and the reverse reaction "
        "have stopped",
        "It will react forward, because the concentration of B is larger than the "
        "concentration of A",
        "It will react in reverse, because the concentration of B is larger than the "
        "concentration of A",
        "It cannot be assessed without knowing how the mixture was prepared"],
      ans=0,
      why="Q for mixture 3 is 0.50 divided by 0.25, which is 2.0 and equals K. EK "
          "7.7.A.2 states that when Q equals K the system is at dynamic equilibrium, "
          "with both forward and reverse reactions proceeding at the same rate; dynamic "
          "means the reactions continue, not that they stop."),

 dict(q="For the reaction A(g) to 2 B(g) the equilibrium constant is \\( 4.0 \\times "
        "10^{-6} \\). A container holds A(g) at 1.00 M initially and no B(g). What is "
        "the equilibrium concentration of B(g)?",
      choices=["[B] = \\( 2.0 \\times 10^{-3} \\) M",
               "[B] = \\( 1.0 \\times 10^{-3} \\) M",
               "[B] = \\( 4.0 \\times 10^{-6} \\) M",
               "[B] = \\( 2.0 \\times 10^{-6} \\) M",
               "[B] = \\( 4.0 \\times 10^{-3} \\) M"],
      ans=0,
      why="The constant is very small, so almost no A reacts and the concentration of A "
          "stays essentially 1.00 M. The expression becomes the square of twice x "
          "divided by 1.00, so twice x is the square root of four times ten to the "
          "negative sixth, which is two times ten to the negative third. EK 7.7.A.1 "
          "supports predicting the amount from the balanced equation, the initial "
          "concentration and K."),

 dict(q="A vessel is charged with only E(g) at 1.00 M for the reaction E(g) to F(g) + "
        "G(g), whose equilibrium constant is \\( 1.0 \\times 10^{-8} \\). What is the "
        "equilibrium concentration of F(g)?",
      choices=["[F] = \\( 1.0 \\times 10^{-4} \\) M",
               "[F] = \\( 1.0 \\times 10^{-8} \\) M",
               "[F] = \\( 2.0 \\times 10^{-4} \\) M",
               "[F] = \\( 1.0 \\times 10^{-16} \\) M",
               "[F] = \\( 5.0 \\times 10^{-9} \\) M"],
      ans=0,
      why="F and G are produced in equal amounts, so the expression is x squared divided "
          "by 1.00 minus x. The constant is tiny, so 1.00 minus x is essentially 1.00 "
          "and x is the square root of ten to the negative eighth, which is ten to the "
          "negative fourth."),

 dict(q="Which three pieces of information does the course framework say are sufficient "
        "to predict the concentrations of every species at equilibrium?",
      choices=[
        "The balanced reaction, the initial concentrations, and the appropriate value "
        "of K",
        "The balanced reaction, the rate constant of the forward step, and the total "
        "pressure",
        "The initial concentrations, the activation energy, and the total volume of the "
        "vessel",
        "The balanced reaction, the enthalpy change, and the time allowed for the "
        "reaction",
        "The initial concentrations, the identity of the catalyst, and the value of Q "
        "at the start"],
      ans=0,
      why="EK 7.7.A.1 states exactly this: the concentrations or partial pressures of "
          "species at equilibrium can be predicted given the balanced reaction, initial "
          "concentrations, and the appropriate K. Rate constants, activation energies "
          "and catalysts govern how fast equilibrium arrives, not where it lies."),

 dict(q="For A(g) to B(g) with an equilibrium constant of 9.0, a vessel starts with "
        "A(g) at 2.00 M and no B(g). What is the equilibrium concentration of A(g)?",
      choices=["[A] = 0.20 M", "[A] = 1.80 M", "[A] = 0.22 M", "[A] = 1.00 M",
               "[A] = 0.90 M"],
      ans=0,
      why="Letting x be the amount converted, x divided by 2.00 minus x equals 9.0, so x "
          "is 1.80 M and the A remaining is 0.20 M. EK 7.7.A.1 makes the pair "
          "predictable from the initial 2.00 M and the constant alone."),

 dict(q="The table shows an incomplete tabulation of initial, change and equilibrium "
        "amounts for A(g) to B(g). If the equilibrium constant is 3.0, what is the value "
        "of x?",
      table=_T_ICE,
      choices=["x = 0.75 M", "x = 0.25 M", "x = 3.00 M", "x = 0.33 M", "x = 0.50 M"],
      ans=0,
      why="The tabulated equilibrium row gives the ratio x over 1.00 minus x, which is "
          "set equal to 3.0. Solving gives x equal to 0.75 M, leaving 0.25 M of A. The "
          "value 0.25 M is the amount of A left, not the value of x."),

 dict(q="In vessel W of the table, the reaction H2(g) + I2(g) to 2 HI(g) has an "
        "equilibrium constant of 4.0. What will happen in vessel W?",
      table=_T_HI,
      choices=[
        "Net reverse reaction, because Q is 8.0 and lies above K",
        "Net forward reaction, because Q is 8.0 and lies above K",
        "Net forward reaction, because Q is 0.13 and lies below K",
        "No net reaction, because Q equals K in this vessel",
        "Net reverse reaction, because Q is 2.0 and lies below K"],
      ans=0,
      why="Q is the square of 0.40 divided by the product of 0.10 and 0.20, which is "
          "0.16 divided by 0.020, or 8.0. Since 8.0 exceeds 4.0, EK 7.7.A.2 predicts a "
          "net consumption of products and generation of reactants."),

 dict(q="Vessel X in the same table is examined, again with an equilibrium constant of "
        "4.0 for H2(g) + I2(g) to 2 HI(g). What is the reaction quotient in vessel X, "
        "and what follows?",
      table=_T_HI,
      choices=[
        "Q is 16 and the mixture reacts in reverse",
        "Q is 16 and the mixture reacts forward",
        "Q is 4.0 and the mixture is at equilibrium",
        "Q is 2.0 and the mixture reacts forward",
        "Q is 0.25 and the mixture reacts forward"],
      ans=0,
      why="Q is the square of 0.80 divided by the product of 0.20 and 0.20, which is "
          "0.64 divided by 0.040, or 16. That is larger than 4.0, so EK 7.7.A.2 gives a "
          "net consumption of products."),

 dict(q="Vessel Y in the same table holds all three gases at 0.50 M each, and the "
        "equilibrium constant for H2(g) + I2(g) to 2 HI(g) is 4.0. What is true of "
        "vessel Y?",
      table=_T_HI,
      choices=[
        "Q is 1.0, so the mixture reacts forward until Q rises to 4.0",
        "Q is 1.0, so the mixture reacts in reverse until Q falls to 4.0",
        "Q is 4.0, so the mixture is already at equilibrium",
        "Q is 0.50, so the mixture reacts forward until Q rises to 4.0",
        "Q is 2.0, so the mixture reacts in reverse until Q falls to 4.0"],
      ans=0,
      why="Q is the square of 0.50 divided by the product of 0.50 and 0.50, which is "
          "0.25 divided by 0.25, or 1.0. Since 1.0 is below 4.0, EK 7.7.A.2 predicts net "
          "forward reaction, and EK 7.7.A.2 also makes Q approach K as that happens."),

 dict(q="For the reaction H2(g) + I2(g) to 2 HI(g) with an equilibrium constant of 4.0, "
        "a vessel is charged with 1.00 M H2(g) and 1.00 M I2(g) and no HI(g). What is "
        "the equilibrium concentration of H2(g)?",
      choices=["[H2] = 0.50 M", "[H2] = 1.00 M", "[H2] = 0.25 M", "[H2] = 0.75 M",
               "[H2] = 0.20 M"],
      ans=0,
      why="Since the reactants start equal, twice x divided by 1.00 minus x equals the "
          "square root of 4.0, which is two. That gives x equal to 0.50 M, so H2 is "
          "1.00 minus 0.50, or 0.50 M, and HI is 1.00 M."),

 dict(q="A student is told only that a certain mixture has Q equal to K. Which "
        "conclusion is supported by the course framework?",
      choices=[
        "Both the forward and the reverse reaction continue at the same rate, so the "
        "proportion of reactants and products stays constant",
        "The forward reaction has run to completion and no reactant is left in the "
        "vessel",
        "Both the forward and the reverse reaction have stopped, so nothing further "
        "happens",
        "The concentrations of reactants and products in the vessel must now be equal "
        "to one another",
        "The reaction will proceed forward until the products outnumber the reactants"],
      ans=0,
      why="EK 7.7.A.2 states that when Q equals K the system is at dynamic equilibrium, "
          "both forward and reverse reactions proceed at the same rate, and the "
          "proportion of reactants and products remains constant. Equal RATES is not "
          "equal CONCENTRATIONS and is not a stopped reaction."),

 dict(q="The reaction 2 A(g) to B(g) has an equilibrium constant of 2.0. Trial 1 in the "
        "table lists partial pressures. What is Q for trial 1, and in which direction "
        "will there be net reaction?",
      table=_T_PRESSURES,
      choices=[
        "Q is 1.00, so there is net forward reaction",
        "Q is 1.00, so there is net reverse reaction",
        "Q is 2.00, so the trial is at equilibrium",
        "Q is 4.00, so there is net reverse reaction",
        "Q is 0.50, so there is net forward reaction"],
      ans=0,
      why="Q is the pressure of B divided by the square of the pressure of A, which is "
          "4.00 divided by 4.00, or 1.00. Since 1.00 is below 2.0, EK 7.7.A.2 gives a "
          "net consumption of reactants and generation of product."),

 dict(q="Trial 2 in the same table is examined for 2 A(g) to B(g) with an equilibrium "
        "constant of 2.0. What is the reaction quotient for trial 2?",
      table=_T_PRESSURES,
      choices=["Q is 8.00", "Q is 4.00", "Q is 2.00", "Q is 0.25", "Q is 16.0"],
      ans=0,
      why="Q is the pressure of B divided by the SQUARE of the pressure of A, which is "
          "2.00 divided by 0.25, or 8.00. Forgetting to square the pressure of A gives "
          "2.00 divided by 0.50, or 4.00, which is why the coefficient of two in the "
          "balanced equation has to be carried into the expression."),

 dict(q="Trial 3 in the same table is examined for 2 A(g) to B(g) with an equilibrium "
        "constant of 2.0. Which statement is correct about trial 3?",
      table=_T_PRESSURES,
      choices=[
        "Q is 0.125, which is below K, so B is generated",
        "Q is 0.125, which is below K, so A is generated",
        "Q is 0.50, which is below K, so B is generated",
        "Q is 8.00, which is above K, so A is generated",
        "Q is 2.00, so trial 3 is already at equilibrium"],
      ans=0,
      why="Q is 2.00 divided by the square of 4.00, which is 2.00 divided by 16, or "
          "0.125. Because that is below 2.0, EK 7.7.A.2 predicts a net consumption of "
          "reactants and generation of products, and B is the product."),

 dict(q="Why can the amount of reactant consumed be neglected in the denominator when "
        "the equilibrium constant is extremely small compared with the initial "
        "concentration?",
      choices=[
        "Because very little reactant is converted, so the equilibrium concentration of "
        "reactant is nearly the initial concentration",
        "Because a very small constant means the reaction does not begin at all until "
        "more reactant is supplied",
        "Because the equilibrium expression omits any species whose concentration falls "
        "during the reaction",
        "Because the amount consumed is exactly zero whenever the constant is smaller "
        "than one",
        "Because the numerator and the denominator of the expression must always be "
        "given equal values"],
      ans=0,
      why="A small K means the equilibrium proportion of product to reactant is small, "
          "so only a small fraction of the reactant is converted and the equilibrium "
          "concentration is close to the initial one. The approximation is about the "
          "SIZE of the change, not about the reaction failing to occur; a small "
          "conversion is not zero conversion."),

 dict(q="A vessel is charged with 0.50 M A(g) and no B(g) for A(g) to B(g) with an "
        "equilibrium constant of 4.0. What is the equilibrium concentration of B(g)?",
      choices=["[B] = 0.40 M", "[B] = 0.10 M", "[B] = 0.80 M", "[B] = 0.50 M",
               "[B] = 2.00 M"],
      ans=0,
      why="Letting x be the amount converted, x divided by 0.50 minus x equals 4.0, so x "
          "is 0.40 M and 0.10 M of A remains. Halving the initial concentration halves "
          "both equilibrium amounts here because the reaction converts one molecule into "
          "one molecule."),

 dict(q="For a reaction with a very large equilibrium constant, a vessel is charged with "
        "reactant alone. Which description of the equilibrium mixture is best supported?",
      choices=[
        "Almost all of the reactant has been converted, and only a small amount of it "
        "remains",
        "Almost none of the reactant has been converted, and very little product is "
        "present",
        "Exactly half of the reactant has been converted, whatever the size of the "
        "constant",
        "The reactant and the product end at equal concentrations, whatever the size of "
        "the constant",
        "No equilibrium is reached at all, because the reaction runs entirely to "
        "completion"],
      ans=0,
      why="A large K makes the product term far larger than the reactant term at "
          "equilibrium, so the conversion is nearly complete while a small amount of "
          "reactant is still present. EK 7.7.A.1 makes the amounts predictable from K "
          "and the initial conditions, and an equilibrium always retains some of every "
          "species that appears in the expression."),

 dict(q="A mixture of A(g) at 0.10 M and B(g) at 0.90 M is prepared for A(g) to B(g), "
        "whose equilibrium constant is 4.0. What is the reaction quotient, and what "
        "follows from it?",
      choices=[
        "Q is 9.0, so A is generated as the mixture approaches equilibrium",
        "Q is 9.0, so B is generated as the mixture approaches equilibrium",
        "Q is 0.11, so B is generated as the mixture approaches equilibrium",
        "Q is 4.0, so the mixture is already at equilibrium",
        "Q is 0.90, so A is generated as the mixture approaches equilibrium"],
      ans=0,
      why="Q is 0.90 divided by 0.10, which is 9.0, and that exceeds 4.0. EK 7.7.A.2 "
          "states that when Q is greater than K the reaction proceeds with a net "
          "consumption of products and generation of reactants, so A is generated."),

 dict(q="Two vessels hold the same reaction at the same temperature, and one is charged "
        "with twice the initial reactant concentration of the other. Which quantity is "
        "necessarily the SAME in the two vessels at equilibrium?",
      choices=[
        "The value of the equilibrium constant",
        "The equilibrium concentration of the product",
        "The equilibrium concentration of the reactant",
        "The number of moles of product formed in each vessel",
        "The reaction quotient at the instant of mixing"],
      ans=0,
      why="K depends on temperature and not on the initial amounts, so two vessels at the "
          "same temperature share it. EK 7.7.A.1 makes the equilibrium concentrations "
          "depend on the initial conditions as well as on K, so those differ between the "
          "vessels, and so does Q at the moment of mixing."),

 dict(q="A student solving for equilibrium amounts writes that the change in the "
        "reactant and the change in the product are equal in magnitude for the reaction "
        "A(g) to 2 B(g). What is wrong with that statement?",
      choices=[
        "The coefficients make the change in B twice the magnitude of the change in A",
        "The change in B is half the magnitude of the change in A because B appears "
        "twice",
        "Changes in a reactant and a product can never be compared in the same "
        "tabulation",
        "The change in A must be zero because A is consumed rather than produced",
        "The two changes are equal only when the equilibrium constant is exactly one"],
      ans=0,
      why="The changes are in the ratio of the stoichiometric coefficients, and the "
          "balanced equation makes two B for every one A consumed. EK 7.7.A.1 names the "
          "balanced reaction as one of the three inputs precisely because the "
          "coefficients set these ratios."),

 dict(q="For the reaction C(g) to D(g), a vessel starts with 1.00 M C(g) and reaches "
        "equilibrium with 0.25 M D(g). What is the equilibrium constant?",
      choices=["K = 0.33", "K = 0.25", "K = 4.0", "K = 3.0", "K = 0.75"],
      ans=0,
      why="At equilibrium D is 0.25 M and C is 1.00 minus 0.25, or 0.75 M, so the "
          "constant is 0.25 divided by 0.75, which is one third. Dividing by the initial "
          "1.00 M rather than the equilibrium 0.75 M would give 0.25 instead."),

 dict(q="A reaction mixture is found to have a reaction quotient smaller than the "
        "equilibrium constant. As the system moves toward equilibrium, what happens to "
        "the value of Q?",
      choices=[
        "It rises toward K, because products are generated and reactants are consumed",
        "It falls toward K, because reactants are generated and products are consumed",
        "It stays where it is, because Q changes only when the temperature changes",
        "It rises past K and then settles back down to a value below K",
        "It falls to zero, because Q is defined only for a system at equilibrium"],
      ans=0,
      why="EK 7.7.A.2 states that when Q is less than K the reaction proceeds with a net "
          "consumption of reactants and generation of products. Increasing the product "
          "terms in the numerator and decreasing the reactant terms in the denominator "
          "raises Q, which stops rising when it reaches K."),

 dict(q="A container is charged with A(g) at 4.00 M and no B(g) for A(g) to B(g), whose "
        "equilibrium constant is 1.00. What are the equilibrium concentrations?",
      choices=[
        "Both A and B are 2.00 M",
        "A is 4.00 M and B is 4.00 M",
        "A is 1.00 M and B is 3.00 M",
        "A is 3.00 M and B is 1.00 M",
        "A is 0 M and B is 4.00 M"],
      ans=0,
      why="A constant of exactly one requires the product and reactant concentrations to "
          "be equal at equilibrium, and the total is conserved at 4.00 M because one "
          "molecule of A becomes one of B. Half of 4.00 M is 2.00 M for each, as EK "
          "7.7.A.1 allows to be predicted from the equation, the initial amount and K."),

 dict(q="Why does a system charged only with product still reach the same equilibrium "
        "constant as one charged only with reactant, at the same temperature?",
      choices=[
        "Because the system reacts in whichever direction brings Q into agreement with "
        "the single value of K set by the temperature",
        "Because a system charged only with product cannot react at all until reactant "
        "is added to it",
        "Because K is redefined for each new starting mixture as the ratio actually "
        "observed",
        "Because the equilibrium concentrations are always identical whatever the "
        "starting mixture",
        "Because Q is fixed at one for any mixture that begins with a single substance"],
      ans=0,
      why="K belongs to the reaction at a temperature, and EK 7.7.A.2 makes the direction "
          "of net change depend on how Q compares with it: a vessel of pure product has "
          "a very large Q and reacts in reverse. The equilibrium CONCENTRATIONS depend "
          "on the starting amounts, but the ratio they settle to does not."),

 dict(q="For E(g) to F(g) with an equilibrium constant of 19, a vessel is charged with "
        "E(g) at 1.00 M and no F(g). What fraction of the initial E(g) remains at "
        "equilibrium?",
      choices=["5.0 percent", "19 percent", "50 percent", "95 percent", "20 percent"],
      ans=0,
      why="Letting x be the amount converted, x divided by 1.00 minus x equals 19, so x "
          "is 0.95 M and the E remaining is 0.05 M out of the original 1.00 M, which is "
          "5.0 percent. The 95 percent figure is the fraction converted rather than the "
          "fraction remaining."),

]
