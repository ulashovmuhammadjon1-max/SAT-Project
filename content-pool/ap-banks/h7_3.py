# AP CHEMISTRY 7.3 Reaction Quotient and Equilibrium Constant
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.3.A: represent the reaction quotient Qc or Qp, for a reversible
# reaction, and the corresponding equilibrium expressions Kc = Qc or Kp = Qp. Suggested
# skill 3.A, represent chemical phenomena using appropriate graphing techniques, including
# correct scale and units.
#
# Essential knowledge relied on, in the framework's own words:
#   7.3.A.1  The reaction quotient Qc describes the relative concentrations of reaction
#            species at any time. For gas phase reactions, the reaction quotient may
#            instead be written in terms of partial pressures as Qp. The reaction quotient
#            tends toward the equilibrium constant such that at equilibrium Kc = Qc and
#            Kp = Qp. As examples, for the reaction aA + bB to cC + dD the law of mass
#            action indicates that the equilibrium expression for (Kc, Qc) is
#            Kc = [C]^c[D]^d / ([A]^a[B]^b) and that for (Kp, Qp) is
#            Kp = (PC)^c(PD)^d / ((PA)^a(PB)^b).
#            Exclusion Statement: Conversion between Kc and Kp will not be assessed on the
#            AP Exam. Students should be aware of the conceptual differences and pay
#            attention to whether Kc or Kp is used in an exam question.
#            Exclusion Statement: Equilibrium calculations on systems where a dissolved
#            species is in equilibrium with that species in the gas phase will not be
#            assessed on the AP Exam.
#   7.3.A.2  The reaction quotient does not include substances whose concentrations (or
#            partial pressures) are independent of the amount, such as for solids and
#            pure liquids.
#
# SCOPE, agreed with the neighbouring modules before this one was written. h7_6.py's own
# header records that "7.3 owns the FORM of the reaction quotient and what is left out of
# it", and that is exactly what this module does. 7.4 owns obtaining a value of K from
# measurements taken AT EQUILIBRIUM; 7.5 owns what the size of K means; 7.7 and 7.10 own
# comparing a computed Q with K to predict which way a reaction proceeds. So every number
# below is a quotient evaluated at a stated, arbitrary moment, never a K read off an
# equilibrium mixture, and NO item asks which direction a reaction will go.
# verify_h7_3.py asserts that last point over every stem and choice.
#
# THE TWO EXCLUSION STATEMENTS ARE ENFORCED, NOT MERELY QUOTED. Items 11 and 12 state
# them, and verify_h7_3.py additionally asserts that no item asks for a numerical
# conversion between Kc and Kp, and that no reaction anywhere in the module places a
# species in solution in equilibrium with the same species as a gas.
#
# ARITHMETIC. Every quotient evaluated below is exact in one or two calculator-free steps
# and is recomputed in verify_h7_3.py from the tabulated concentrations and the balanced
# equation alone -- including the heterogeneous cases, where the recomputation is what
# proves the solid really was left out.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span below is
# hand-written. A formula in prose stays plain text (SO3, CaCO3, N2O4) and a reaction
# arrow is written as the word "to" so no glyph is left outside a span.
TOPIC = ("7.3", "Reaction Quotient and Equilibrium Constant", 7)

_T_NO2 = dict(
    headers=["Species", "Concentration at the moment of sampling (M)"],
    rows=[["N2O4(g)", "0.20"],
          ["NO2(g)", "0.40"]])

_T_SO3 = dict(
    headers=["Species", "Concentration at the moment of sampling (M)"],
    rows=[["SO2(g)", "0.20"],
          ["O2(g)", "0.50"],
          ["SO3(g)", "0.10"]])

_T_HETERO = dict(
    headers=["Species", "Amount present at the moment of sampling"],
    rows=[["C(s)", "12 grams of solid"],
          ["H2O(g)", "0.50 M"],
          ["CO(g)", "0.20 M"],
          ["H2(g)", "0.50 M"]])

_T_MIXTURES = dict(
    headers=["Mixture", "[N2O4] (M)", "[NO2] (M)"],
    rows=[["1", "0.40", "0.40"],
          ["2", "0.20", "0.40"],
          ["3", "0.10", "0.20"]])

QUESTIONS = [

 dict(q="What does the reaction quotient Qc describe, according to the framework?",
      choices=[
        "The relative concentrations of the reaction species at any time",
        "The relative concentrations of the reaction species only once equilibrium is "
        "reached",
        "The rate at which the reaction converts reactants to products",
        "The fraction of the reactant that has been consumed so far",
        "The energy released as the reaction proceeds"],
      ans=0,
      why="EK 7.3.A.1 opens by saying the reaction quotient Qc describes the relative "
          "concentrations of reaction species at any time. The restriction to equilibrium "
          "belongs to the equilibrium CONSTANT, which the same statement reaches only at "
          "the end."),

 dict(q="What does the framework say the reaction quotient tends toward?",
      choices=[
        "The equilibrium constant, so that at equilibrium the two are equal",
        "Zero, since reactants are eventually used up",
        "One, since the numerator and denominator become equal",
        "The rate constant of the forward reaction",
        "A value fixed by the initial concentrations alone"],
      ans=0,
      why="EK 7.3.A.1 states that the reaction quotient tends toward the equilibrium "
          "constant such that at equilibrium Kc equals Qc and Kp equals Qp. Neither zero "
          "nor one is named there, and a rate constant belongs to kinetics rather than to "
          "the law of mass action."),

 dict(q="For a reaction among gases, in what other terms does the framework say the "
        "reaction quotient may be written?",
      choices=[
        "Partial pressures, written as Qp",
        "Total pressure of the vessel, written as Qp",
        "Numbers of molecules, written as Qn",
        "Volumes of each gas, written as Qv",
        "Masses of each gas, written as Qm"],
      ans=0,
      why="EK 7.3.A.1 says that for gas phase reactions the reaction quotient may instead "
          "be written in terms of PARTIAL pressures as Qp. The total pressure of the "
          "vessel is a sum over all the gases and cannot distinguish the species the "
          "expression requires."),

 dict(q="Which expression is the equilibrium constant Kc for 2 SO2(g) + O2(g) to "
        "2 SO3(g)?",
      choices=[
        "\\( K_c = \\frac{[\\mathrm{SO_3}]^{2}}{[\\mathrm{SO_2}]^{2}[\\mathrm{O_2}]} \\)",
        "\\( K_c = \\frac{[\\mathrm{SO_2}]^{2}[\\mathrm{O_2}]}{[\\mathrm{SO_3}]^{2}} \\)",
        "\\( K_c = \\frac{[\\mathrm{SO_3}]}{[\\mathrm{SO_2}][\\mathrm{O_2}]} \\)",
        "\\( K_c = \\frac{2[\\mathrm{SO_3}]}{2[\\mathrm{SO_2}][\\mathrm{O_2}]} \\)",
        "\\( K_c = [\\mathrm{SO_3}]^{2}[\\mathrm{SO_2}]^{2}[\\mathrm{O_2}] \\)"],
      ans=0,
      why="EK 7.3.A.1's law of mass action puts the product concentrations in the "
          "numerator and the reactant concentrations in the denominator, each raised to "
          "the power of its coefficient in the balanced equation. A coefficient becomes an "
          "exponent, not a multiplier, and inverting the expression would describe the "
          "reverse reaction."),

 dict(q="Which expression is the equilibrium constant Kp for the same reaction, "
        "2 SO2(g) + O2(g) to 2 SO3(g)?",
      choices=[
        "\\( K_p = \\frac{(P_{\\mathrm{SO_3}})^{2}}{(P_{\\mathrm{SO_2}})^{2}(P_{\\mathrm{O_2}})} \\)",
        "\\( K_p = \\frac{(P_{\\mathrm{SO_2}})^{2}(P_{\\mathrm{O_2}})}{(P_{\\mathrm{SO_3}})^{2}} \\)",
        "\\( K_p = \\frac{(P_{\\mathrm{SO_3}})^{2}}{(P_{\\mathrm{total}})^{3}} \\)",
        "\\( K_p = \\frac{2P_{\\mathrm{SO_3}}}{2P_{\\mathrm{SO_2}} + P_{\\mathrm{O_2}}} \\)",
        "\\( K_p = (P_{\\mathrm{SO_3}})^{2}(P_{\\mathrm{SO_2}})^{2}(P_{\\mathrm{O_2}}) \\)"],
      ans=0,
      why="EK 7.3.A.1 gives the pressure form of the law of mass action with each partial "
          "pressure raised to the power of its coefficient, products over reactants. The "
          "total pressure does not identify a species, and coefficients never become "
          "multipliers or terms in a sum."),

 dict(q="For the general reaction aA + bB to cC + dD, which arrangement does the law of "
        "mass action give for the equilibrium expression?",
      choices=[
        "The product concentrations in the numerator and the reactant concentrations in "
        "the denominator, each raised to its coefficient",
        "The reactant concentrations in the numerator and the product concentrations in "
        "the denominator, each raised to its coefficient",
        "All four concentrations multiplied together, each raised to its coefficient",
        "The product concentrations in the numerator and the reactant concentrations in "
        "the denominator, each multiplied by its coefficient",
        "The sum of the product concentrations divided by the sum of the reactant "
        "concentrations"],
      ans=0,
      why="EK 7.3.A.1 writes the expression for (Kc, Qc) with the concentrations of C and "
          "D over those of A and B, each carrying its own coefficient as an EXPONENT. "
          "Multiplying by a coefficient, or adding concentrations, is a different "
          "operation and gives a different number."),

 dict(q="Which kinds of substance does the framework say are left out of the reaction "
        "quotient?",
      choices=[
        "Solids and pure liquids",
        "Gases and solids",
        "Solutes and pure liquids",
        "Catalysts and gases",
        "Only substances that appear on the reactant side"],
      ans=0,
      why="EK 7.3.A.2 states that the reaction quotient does not include substances whose "
          "concentrations or partial pressures are independent of the amount, such as for "
          "solids and pure liquids. Gases and dissolved species do have amounts that "
          "change with how much is present, so they appear."),

 dict(q="Which expression is Kc for the decomposition CaCO3(s) to CaO(s) + CO2(g)?",
      choices=[
        "\\( K_c = [\\mathrm{CO_2}] \\)",
        "\\( K_c = \\frac{[\\mathrm{CaO}][\\mathrm{CO_2}]}{[\\mathrm{CaCO_3}]} \\)",
        "\\( K_c = [\\mathrm{CaO}][\\mathrm{CO_2}] \\)",
        "\\( K_c = \\frac{[\\mathrm{CO_2}]}{[\\mathrm{CaCO_3}]} \\)",
        "\\( K_c = \\frac{1}{[\\mathrm{CO_2}]} \\)"],
      ans=0,
      why="EK 7.3.A.2 leaves out substances whose concentration is independent of the "
          "amount present, and both solids here are such substances, so only the gas "
          "remains. Keeping either solid in the expression would make the constant depend "
          "on how much solid the flask happened to contain."),

 dict(q="Which expression is Kc for C(s) + H2O(g) to CO(g) + H2(g)?",
      choices=[
        "\\( K_c = \\frac{[\\mathrm{CO}][\\mathrm{H_2}]}{[\\mathrm{H_2O}]} \\)",
        "\\( K_c = \\frac{[\\mathrm{CO}][\\mathrm{H_2}]}{[\\mathrm{C}][\\mathrm{H_2O}]} \\)",
        "\\( K_c = \\frac{[\\mathrm{H_2O}]}{[\\mathrm{CO}][\\mathrm{H_2}]} \\)",
        "\\( K_c = [\\mathrm{CO}][\\mathrm{H_2}][\\mathrm{H_2O}] \\)",
        "\\( K_c = \\frac{[\\mathrm{CO}] + [\\mathrm{H_2}]}{[\\mathrm{H_2O}]} \\)"],
      ans=0,
      why="EK 7.3.A.1 puts products over reactants and EK 7.3.A.2 removes the solid "
          "carbon, leaving the two gaseous products over the one gaseous reactant. "
          "Concentrations in an equilibrium expression are multiplied, never added."),

 dict(q="Why does the framework leave solids and pure liquids out of the reaction "
        "quotient?",
      choices=[
        "Their concentrations are independent of the amount present",
        "They do not take part in the reaction at all",
        "Their concentrations are always exactly one molar",
        "They react too slowly to affect the quotient",
        "They are consumed completely before equilibrium is reached"],
      ans=0,
      why="EK 7.3.A.2 gives exactly this reason: the quotient does not include substances "
          "whose concentrations or partial pressures are independent of the amount. A "
          "solid does take part in the reaction, which is why it appears in the balanced "
          "equation but not in the expression."),

 dict(q="The framework excludes conversion between Kc and Kp from the exam. What does it "
        "say students should do instead?",
      choices=[
        "Be aware of the conceptual differences and attend to which one a question uses",
        "Assume that Kc and Kp are numerically equal for every reaction",
        "Convert every constant to Kc before answering",
        "Use Kp for reactions in solution and Kc for reactions among gases",
        "Treat Kp as the reciprocal of Kc"],
      ans=0,
      why="The exclusion statement attached to EK 7.3.A.1 says conversion between Kc and "
          "Kp will not be assessed, and that students should be aware of the conceptual "
          "differences and pay attention to whether Kc or Kp is used in a question. It "
          "does not say the two are equal or reciprocal."),

 dict(q="Which type of equilibrium calculation does the framework's second exclusion "
        "statement place outside the scope of the exam?",
      choices=[
        "One on a system where a dissolved species is in equilibrium with the same species "
        "in the gas phase",
        "One on a system containing a solid in equilibrium with a gas",
        "One on a system containing two gases only",
        "One on a system where a weak acid is in equilibrium with its conjugate base",
        "One on any system whose expression contains an exponent"],
      ans=0,
      why="The second exclusion statement attached to EK 7.3.A.1 names exactly that case. "
          "A solid with a gas is the ordinary heterogeneous equilibrium EK 7.3.A.2 tells "
          "students how to handle, so it is squarely inside the course."),

 dict(q="A mixture of reactants and products has just been prepared and is nowhere near "
        "equilibrium. Can a reaction quotient be written for it?",
      choices=[
        "Yes, because the quotient is defined at any time",
        "No, because a quotient can only be evaluated at equilibrium",
        "Yes, but only if the mixture contains no products",
        "No, because the concentrations are still changing",
        "Yes, but its value is zero until equilibrium is reached"],
      ans=0,
      why="EK 7.3.A.1 says the reaction quotient describes the relative concentrations of "
          "reaction species AT ANY TIME. What is reserved for equilibrium is the equality "
          "of the quotient with the constant, not the existence of the quotient."),

 dict(q="The table gives concentrations sampled from a vessel holding N2O4(g) and NO2(g), "
        "which interconvert by N2O4(g) to 2 NO2(g). What is the value of Qc at that "
        "moment?",
      table=_T_NO2,
      choices=["0.80", "2.0", "0.50", "0.16", "1.6"],
      ans=0,
      why="EK 7.3.A.1's law of mass action puts the product concentration in the numerator "
          "raised to its coefficient of two, over the reactant concentration. Squaring the "
          "tabulated product concentration and dividing by the tabulated reactant "
          "concentration gives the value; forgetting to square gives a different one."),

 dict(q="The table gives concentrations sampled from a vessel in which 2 SO2(g) + O2(g) "
        "to 2 SO3(g) is occurring. What is the value of Qc at that moment?",
      table=_T_SO3,
      choices=["0.50", "1.0", "0.10", "2.0", "0.020"],
      ans=0,
      why="EK 7.3.A.1 raises each tabulated concentration to the power of its coefficient "
          "and divides products by reactants, so the square of the product concentration "
          "is divided by the square of one reactant concentration times the other. "
          "Dropping either exponent changes the result."),

 dict(q="The table gives the amounts present in a vessel in which C(s) + H2O(g) to CO(g) + "
        "H2(g) is occurring. What is the value of Qc at that moment?",
      table=_T_HETERO,
      choices=["0.20", "0.0167", "2.4", "0.10", "0.50"],
      ans=0,
      why="EK 7.3.A.2 removes the solid carbon from the expression however much of it is "
          "present, so the tabulated mass plays no part; the two gaseous product "
          "concentrations are multiplied and divided by the gaseous reactant "
          "concentration. Dividing by the mass as well would make the answer depend on how "
          "much solid was weighed out."),

 dict(q="In an equilibrium expression, what does a coefficient from the balanced equation "
        "become?",
      choices=[
        "An exponent on that species' concentration",
        "A multiplier in front of that species' concentration",
        "A divisor applied to that species' concentration",
        "A term added to that species' concentration",
        "Nothing, since coefficients do not appear in the expression"],
      ans=0,
      why="EK 7.3.A.1 writes the expression with each concentration raised to the power of "
          "its coefficient. Treating a coefficient as a multiplier gives a different "
          "number for every mixture, which is why the distinction is worth stating."),

 dict(q="More solid CaCO3 is added to a sealed vessel in which CaCO3(s) to CaO(s) + "
        "CO2(g) is occurring. What happens to the value of the reaction quotient at that "
        "instant?",
      choices=[
        "It is unchanged, because the solid does not appear in the expression",
        "It increases, because more reactant is present",
        "It decreases, because more reactant is present",
        "It becomes undefined until the added solid has reacted",
        "It doubles if the amount of solid is doubled"],
      ans=0,
      why="EK 7.3.A.2 leaves solids out of the reaction quotient because their "
          "concentrations are independent of the amount present, so nothing in the "
          "expression changes when solid is added. The expression for this reaction "
          "contains the gas alone."),

 dict(q="Which expression is Kc for N2(g) + 3 H2(g) to 2 NH3(g)?",
      choices=[
        "\\( K_c = \\frac{[\\mathrm{NH_3}]^{2}}{[\\mathrm{N_2}][\\mathrm{H_2}]^{3}} \\)",
        "\\( K_c = \\frac{[\\mathrm{NH_3}]^{2}}{[\\mathrm{N_2}]^{2}[\\mathrm{H_2}]^{3}} \\)",
        "\\( K_c = \\frac{[\\mathrm{N_2}][\\mathrm{H_2}]^{3}}{[\\mathrm{NH_3}]^{2}} \\)",
        "\\( K_c = \\frac{[\\mathrm{NH_3}]}{[\\mathrm{N_2}][\\mathrm{H_2}]} \\)",
        "\\( K_c = \\frac{2[\\mathrm{NH_3}]}{[\\mathrm{N_2}] + 3[\\mathrm{H_2}]} \\)"],
      ans=0,
      why="EK 7.3.A.1's law of mass action gives the ammonia concentration squared over "
          "the nitrogen concentration times the hydrogen concentration cubed, each "
          "exponent taken from the balanced equation. Nitrogen's coefficient is one, so it "
          "carries no written exponent."),

 dict(q="Which expression is Kp for N2(g) + 3 H2(g) to 2 NH3(g)?",
      choices=[
        "\\( K_p = \\frac{(P_{\\mathrm{NH_3}})^{2}}{(P_{\\mathrm{N_2}})(P_{\\mathrm{H_2}})^{3}} \\)",
        "\\( K_p = \\frac{(P_{\\mathrm{N_2}})(P_{\\mathrm{H_2}})^{3}}{(P_{\\mathrm{NH_3}})^{2}} \\)",
        "\\( K_p = \\frac{(P_{\\mathrm{NH_3}})^{2}}{(P_{\\mathrm{N_2}})^{3}(P_{\\mathrm{H_2}})} \\)",
        "\\( K_p = \\frac{P_{\\mathrm{NH_3}}}{P_{\\mathrm{N_2}} + P_{\\mathrm{H_2}}} \\)",
        "\\( K_p = \\frac{(P_{\\mathrm{NH_3}})^{2}}{P_{\\mathrm{total}}} \\)"],
      ans=0,
      why="EK 7.3.A.1's pressure form mirrors the concentration form exactly: each partial "
          "pressure is raised to the power of its own coefficient, with products over "
          "reactants. Swapping the two exponents assigns each coefficient to the wrong "
          "species."),

 dict(q="A reaction is carried out in water and one of the reactants written in the "
        "balanced equation is H2O(l), the solvent itself. How does it enter the reaction "
        "quotient?",
      choices=[
        "It does not enter at all, because a pure liquid is left out",
        "It enters in the denominator, since it is a reactant",
        "It enters in the numerator, since its amount is very large",
        "It enters raised to the power of its coefficient like any other species",
        "It enters as the reciprocal of its concentration"],
      ans=0,
      why="EK 7.3.A.2 says the reaction quotient does not include substances whose "
          "concentrations are independent of the amount, such as solids and PURE LIQUIDS. "
          "The solvent's concentration is set by the liquid itself rather than by how much "
          "of it is in the flask."),

 dict(q="What distinguishes the reaction quotient from the equilibrium constant, in the "
        "framework's account?",
      choices=[
        "The quotient can be evaluated at any moment, while the constant is the value it "
        "reaches at equilibrium",
        "The quotient uses concentrations while the constant uses partial pressures",
        "The quotient includes solids while the constant does not",
        "The quotient applies to the reverse reaction and the constant to the forward one",
        "There is no difference; the two words name the same quantity"],
      ans=0,
      why="EK 7.3.A.1 defines the quotient at any time and then says it tends toward the "
          "equilibrium constant, so that at equilibrium the two are equal. Both come in a "
          "concentration form and a pressure form, and EK 7.3.A.2's omission rule applies "
          "to both."),

 dict(q="The table gives concentrations for three separate mixtures of N2O4(g) and "
        "NO2(g), which interconvert by N2O4(g) to 2 NO2(g). Which mixture has the largest "
        "value of Qc?",
      table=_T_MIXTURES,
      choices=["Mixture 2", "Mixture 1", "Mixture 3", "Mixtures 1 and 3 are tied for the "
               "largest", "All three have the same value"],
      ans=0,
      why="EK 7.3.A.1's expression squares the tabulated NO2 concentration and divides by "
          "the tabulated N2O4 concentration, and evaluating it for all three mixtures "
          "gives one largest value. Comparing the NO2 concentrations alone would not "
          "settle it, because two mixtures share that value."),

 dict(q="A student writes the equilibrium expression for a gas phase reaction using the "
        "total pressure of the vessel in place of each partial pressure. What is wrong "
        "with this?",
      choices=[
        "The expression requires the partial pressure of each species separately",
        "Nothing is wrong, since the total pressure is the sum of the partial pressures",
        "The expression requires concentrations and can never use pressures",
        "The total pressure should be used only in the denominator",
        "The total pressure should be raised to the sum of all the coefficients"],
      ans=0,
      why="EK 7.3.A.1 writes Kp with (PC), (PD), (PA) and (PB) -- one partial pressure per "
          "species, each raised to its own coefficient. A single total pressure cannot "
          "distinguish the species and would give the same value for mixtures of quite "
          "different composition."),

 dict(q="Two vessels hold the same reaction at the same temperature but were charged "
        "differently, and each has now reached equilibrium. What is true of the value of "
        "the quotient in the two vessels?",
      choices=[
        "It is the same in both, because at equilibrium the quotient equals the constant",
        "It is larger in the vessel that started with more reactant",
        "It is larger in the vessel that started with more product",
        "It cannot be compared unless the two vessels have the same volume",
        "It is zero in both, since neither is changing"],
      ans=0,
      why="EK 7.3.A.1 says the reaction quotient tends toward the equilibrium constant "
          "such that at equilibrium Kc equals Qc. The constant belongs to the reaction and "
          "the temperature, so two equilibrium mixtures of the same reaction at the same "
          "temperature give the same value however they were charged."),

 dict(q="Which of the following would appear in the reaction quotient for a reaction "
        "involving a dissolved solute, a gas, a solid and a pure liquid?",
      choices=[
        "The dissolved solute and the gas only",
        "The dissolved solute, the gas and the pure liquid",
        "The gas and the solid only",
        "All four species",
        "The solid and the pure liquid only"],
      ans=0,
      why="EK 7.3.A.2 removes substances whose concentrations or partial pressures are "
          "independent of the amount, naming solids and pure liquids. A dissolved solute "
          "and a gas both have amounts that change with how much is present, so both "
          "remain in the expression."),

 dict(q="Using the table of concentrations for the N2O4 and NO2 mixture, what value would "
        "a student obtain who forgot to square the NO2 concentration?",
      table=_T_NO2,
      choices=["2.0", "0.80", "0.16", "0.50", "0.040"],
      ans=0,
      why="Dividing the tabulated NO2 concentration by the tabulated N2O4 concentration "
          "without applying the coefficient of two gives this value, while EK 7.3.A.1's "
          "law of mass action requires the exponent and gives a different one. The "
          "difference between the two numbers is the whole content of the exponent rule."),

 dict(q="A reaction is written with the products on the left and the reactants on the "
        "right by mistake, and the expression is built from that. How does the value "
        "obtained relate to the correct one?",
      choices=[
        "It is the reciprocal of the correct value",
        "It is the negative of the correct value",
        "It is the same as the correct value",
        "It differs by the ratio of the coefficients",
        "It is the square of the correct value"],
      ans=0,
      why="EK 7.3.A.1 fixes which species go in the numerator and which in the "
          "denominator, so exchanging them exchanges numerator and denominator and gives "
          "the reciprocal. A concentration quotient is a positive quantity, so a sign "
          "change is not available."),

 dict(q="In which form should a question about a mixture of gases in a sealed flask be "
        "answered when the data supplied are partial pressures?",
      choices=[
        "Using Qp, built from the supplied partial pressures",
        "Using Qc, after first converting each pressure to a concentration",
        "Using Qc, treating each pressure as though it were a concentration",
        "Using whichever form gives the larger number",
        "Using Qp, but only if the flask also contains a solid"],
      ans=0,
      why="EK 7.3.A.1 offers the pressure form for gas phase reactions, and its exclusion "
          "statement asks students to pay attention to whether Kc or Kp is used rather "
          "than to convert between them. Treating a pressure as a concentration would "
          "silently mix the two forms."),

 dict(q="Using the table of concentrations for the vessel holding SO2, O2 and SO3, what "
        "value would a student obtain who wrote the expression upside down, with the "
        "reactants in the numerator?",
      table=_T_SO3,
      choices=["2.0", "0.50", "0.10", "1.0", "0.020"],
      ans=0,
      why="Building the quotient with the two tabulated reactant concentrations over the "
          "tabulated product concentration, each raised to its coefficient, gives the "
          "reciprocal of the correct value. EK 7.3.A.1 fixes the arrangement as products "
          "over reactants, which is what makes the two numbers different."),

]
