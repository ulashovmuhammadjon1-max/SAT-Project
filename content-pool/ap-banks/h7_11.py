# AP CHEMISTRY 7.11 Introduction to Solubility Equilibria
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.11.A: calculate the solubility of a salt based on the value of Ksp
# for the salt. Suggested skill 5.B, identify an appropriate theory, definition, or
# mathematical relationship to solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   7.11.A.1  The dissolution of a salt is a reversible process whose extent can be
#             described by Ksp, the solubility-product constant.
#   7.11.A.2  The solubility of a substance can be calculated from the Ksp for the
#             dissolution process. This relationship can also be used to predict the
#             relative solubility of different substances.
#   7.11.A.3  The solubility rules (see 4.7.A.5) can be quantitatively related to Ksp, in
#             which Ksp values greater than 1 correspond to soluble salts.
#   7.11.A.4  The molar solubility of one or more species in a saturated solution can be
#             used to calculate the Ksp of a substance.
#
# SCOPE. 7.12 owns the common-ion effect -- what happens when a salt dissolves into a
# solution ALREADY containing one of its ions -- and 8.11 owns the pH sensitivity of a
# salt whose ion is a weak acid or base. Every dissolution below is into pure water at a
# fixed temperature, and no item mentions a shared ion or a change of pH.
#
# THE TRAP THIS TOPIC MUST NOT TEACH. EK 7.11.A.2 licenses predicting RELATIVE solubility
# from Ksp, and the naive form of that -- larger Ksp means more soluble -- is only valid
# between salts that dissociate into the same number of ions. Items 19 and 25 are built on
# a pair for which it fails, with the two solubilities recomputed in the verifier, so the
# bank states the limitation rather than quietly relying on it.
#
# ARITHMETIC. Every molar solubility and every Ksp below is exact and is recomputed in
# verify_h7_11.py from the stated value alone.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span is
# hand-written. A formula in prose stays plain text (AgCl, PbI2).
TOPIC = ("7.11", "Introduction to Solubility Equilibria", 7)

_T_ONE_TO_ONE = dict(
    headers=["Salt", "Ions produced per formula unit", "Ksp at 298 K"],
    rows=[["AgCl", "one silver ion and one chloride ion", "\\( 1.8 \\times 10^{-10} \\)"],
          ["AgBr", "one silver ion and one bromide ion", "\\( 5.0 \\times 10^{-13} \\)"],
          ["AgI", "one silver ion and one iodide ion", "\\( 8.5 \\times 10^{-17} \\)"]])

_T_SOLUBILITY = dict(
    headers=["Salt", "Formula type", "Molar solubility in pure water (M)"],
    rows=[["Salt J", "one cation and one anion", "0.0010"],
          ["Salt L", "one cation and two anions", "0.0010"],
          ["Salt M", "one cation and one anion", "0.0050"]])

_T_KSPS = dict(
    headers=["Salt", "Formula type", "Ksp at 298 K"],
    rows=[["Salt P", "one cation and one anion", "\\( 1.0 \\times 10^{-8} \\)"],
          ["Salt R", "one cation and two anions", "\\( 4.0 \\times 10^{-9} \\)"],
          ["Salt T", "one cation and one anion", "\\( 2.5 \\)"]])

QUESTIONS = [

 dict(q="What does the course framework say the dissolution of a salt is, and what "
        "describes its extent?",
      choices=[
        "A reversible process whose extent is described by the solubility-product "
        "constant",
        "An irreversible process whose extent is described by the rate of dissolving",
        "A reversible process whose extent is described by the enthalpy of solution",
        "An irreversible process whose extent is described by the molar mass of the salt",
        "A reversible process whose extent cannot be described by any constant"],
      ans=0,
      why="EK 7.11.A.1 states it directly: the dissolution of a salt is a reversible "
          "process whose extent can be described by Ksp, the solubility-product constant. "
          "A rate describes speed rather than extent."),

 dict(q="Which expression is the solubility-product expression for the dissolution of "
        "PbI2(s) into Pb2+(aq) and I-(aq)?",
      choices=["\\( K_{sp} = [\\mathrm{Pb^{2+}}][\\mathrm{I^-}]^{2} \\)",
               "\\( K_{sp} = [\\mathrm{Pb^{2+}}][\\mathrm{I^-}] \\)",
               "\\( K_{sp} = [\\mathrm{Pb^{2+}}]^{2}[\\mathrm{I^-}] \\)",
               "\\( K_{sp} = \\frac{[\\mathrm{Pb^{2+}}][\\mathrm{I^-}]^{2}}{[\\mathrm{PbI_2}]} \\)",
               "\\( K_{sp} = [\\mathrm{Pb^{2+}}] + 2[\\mathrm{I^-}] \\)"],
      ans=0,
      why="Each ion concentration is raised to its coefficient in the dissolution "
          "equation, and two iodide ions are released per formula unit. The solid is a "
          "pure solid and so is left out of the expression, which is why no denominator "
          "appears."),

 dict(q="A salt of the type one cation to one anion has a solubility-product constant of "
        "\\( 4.0 \\times 10^{-10} \\). What is its molar solubility in pure water?",
      choices=["\\( 2.0 \\times 10^{-5} \\) M", "\\( 4.0 \\times 10^{-10} \\) M",
               "\\( 1.6 \\times 10^{-19} \\) M", "\\( 2.0 \\times 10^{-10} \\) M",
               "\\( 4.0 \\times 10^{-5} \\) M"],
      ans=0,
      why="EK 7.11.A.2 makes the solubility calculable from Ksp. For a one-to-one salt "
          "both ion concentrations equal the molar solubility, so Ksp is the square of "
          "the solubility and the solubility is its square root."),

 dict(q="A one-to-one salt has a solubility-product constant of \\( 9.0 \\times 10^{-12} "
        "\\). What is its molar solubility in pure water?",
      choices=["\\( 3.0 \\times 10^{-6} \\) M", "\\( 9.0 \\times 10^{-6} \\) M",
               "\\( 4.5 \\times 10^{-12} \\) M", "\\( 3.0 \\times 10^{-12} \\) M",
               "\\( 8.1 \\times 10^{-23} \\) M"],
      ans=0,
      why="EK 7.11.A.2 gives the solubility as the square root of Ksp for a salt "
          "releasing one of each ion, and the square root of nine times ten to the "
          "negative twelfth is three times ten to the negative sixth."),

 dict(q="A one-to-one salt is found to have a molar solubility of \\( 1.0 \\times "
        "10^{-4} \\) M in pure water. What is its solubility-product constant?",
      choices=["\\( 1.0 \\times 10^{-8} \\)", "\\( 1.0 \\times 10^{-4} \\)",
               "\\( 2.0 \\times 10^{-4} \\)", "\\( 1.0 \\times 10^{-2} \\)",
               "\\( 1.0 \\times 10^{-12} \\)"],
      ans=0,
      why="EK 7.11.A.4 states that the molar solubility of a species in a saturated "
          "solution can be used to calculate Ksp. Both ions are present at the molar "
          "solubility, so the product is the square of that value."),

 dict(q="Which expression is the solubility-product expression for the dissolution of "
        "Ca3(PO4)2(s) into Ca2+(aq) and PO4 3-(aq)?",
      choices=[
        "\\( K_{sp} = [\\mathrm{Ca^{2+}}]^{3}[\\mathrm{PO_4^{3-}}]^{2} \\)",
        "\\( K_{sp} = [\\mathrm{Ca^{2+}}]^{2}[\\mathrm{PO_4^{3-}}]^{3} \\)",
        "\\( K_{sp} = [\\mathrm{Ca^{2+}}][\\mathrm{PO_4^{3-}}] \\)",
        "\\( K_{sp} = 3[\\mathrm{Ca^{2+}}] + 2[\\mathrm{PO_4^{3-}}] \\)",
        "\\( K_{sp} = [\\mathrm{Ca^{2+}}]^{3} + [\\mathrm{PO_4^{3-}}]^{2} \\)"],
      ans=0,
      why="Three calcium ions and two phosphate ions are released per formula unit, so "
          "each concentration is raised to its own coefficient and the two are multiplied. "
          "The charges on the ions set the formula but do not appear as exponents."),

 dict(q="For a salt releasing one cation and two anions per formula unit, how is Ksp "
        "related to the molar solubility s?",
      choices=["\\( K_{sp} = 4s^{3} \\)", "\\( K_{sp} = s^{2} \\)",
               "\\( K_{sp} = 2s^{2} \\)", "\\( K_{sp} = s^{3} \\)",
               "\\( K_{sp} = 3s^{3} \\)"],
      ans=0,
      why="Dissolving s moles per litre gives s of the cation and twice s of the anion, "
          "so the product is s times the square of two s, which is four s cubed. Losing "
          "the factor of two before squaring is what produces the s cubed answer."),

 dict(q="A salt of the type one cation to two anions has a solubility-product constant of "
        "\\( 3.2 \\times 10^{-11} \\). What is its molar solubility in pure water?",
      choices=["\\( 2.0 \\times 10^{-4} \\) M", "\\( 3.2 \\times 10^{-11} \\) M",
               "\\( 5.7 \\times 10^{-6} \\) M", "\\( 4.0 \\times 10^{-4} \\) M",
               "\\( 8.0 \\times 10^{-12} \\) M"],
      ans=0,
      why="Ksp is four s cubed for this formula type, so s cubed is eight times ten to "
          "the negative twelfth and s is two times ten to the negative fourth. Taking a "
          "square root instead would give about 5.7 times ten to the negative sixth."),

 dict(q="A salt releasing one cation and two anions has a molar solubility of \\( 2.0 "
        "\\times 10^{-3} \\) M. What is its solubility-product constant?",
      choices=["\\( 3.2 \\times 10^{-8} \\)", "\\( 8.0 \\times 10^{-9} \\)",
               "\\( 4.0 \\times 10^{-6} \\)", "\\( 1.6 \\times 10^{-8} \\)",
               "\\( 2.0 \\times 10^{-3} \\)"],
      ans=0,
      why="EK 7.11.A.4 lets Ksp be calculated from the molar solubility. The anion is "
          "present at twice the solubility, so Ksp is four times the cube of the "
          "solubility. Omitting the factor of four gives eight times ten to the negative "
          "ninth."),

 dict(q="Which value of a solubility-product constant would the course framework "
        "associate with a salt classed as SOLUBLE by the solubility rules?",
      choices=["A value greater than one", "A value close to zero",
               "A value between zero and one thousandth",
               "A negative value", "A value that cannot be defined"],
      ans=0,
      why="EK 7.11.A.3 states that the solubility rules can be quantitatively related to "
          "Ksp, in which Ksp values greater than one correspond to soluble salts. An "
          "equilibrium constant is a ratio of concentrations and so is never negative."),

 dict(q="Using the table of silver halides, which salt is the LEAST soluble in pure "
        "water?",
      table=_T_ONE_TO_ONE,
      choices=["AgI", "AgCl", "AgBr", "All three are equally soluble",
               "The comparison cannot be made from these data"],
      ans=0,
      why="All three salts release one cation and one anion, so EK 7.11.A.2 lets their "
          "solubilities be ranked directly by Ksp, and the smallest tabulated constant "
          "belongs to the least soluble salt."),

 dict(q="Using that same table, why is a direct comparison of the three constants a valid "
        "way to rank the three salts?",
      table=_T_ONE_TO_ONE,
      choices=[
        "Because all three release the same number of ions per formula unit, so "
        "solubility is the square root of Ksp in every case",
        "Because all three contain the same cation, which makes their constants "
        "comparable",
        "Because all three constants are smaller than one, which is the only requirement",
        "Because Ksp is always proportional to solubility for any salt whatever",
        "Because the three salts are listed in order of increasing molar mass"],
      ans=0,
      why="EK 7.11.A.2 licenses predicting relative solubility from Ksp, but the "
          "relationship between the two depends on the formula type. Where the type is "
          "shared, as it is here, the same function of Ksp gives the solubility for each "
          "salt and the ranking carries over."),

 dict(q="The table lists molar solubilities. What is the solubility-product constant of "
        "salt J?",
      table=_T_SOLUBILITY,
      choices=["\\( 1.0 \\times 10^{-6} \\)", "\\( 1.0 \\times 10^{-3} \\)",
               "\\( 4.0 \\times 10^{-9} \\)", "\\( 2.0 \\times 10^{-3} \\)",
               "\\( 1.0 \\times 10^{-9} \\)"],
      ans=0,
      why="EK 7.11.A.4 lets Ksp be computed from the molar solubility. Salt J releases "
          "one of each ion, so its constant is the square of its tabulated solubility."),

 dict(q="Using the same table, what is the solubility-product constant of salt L?",
      table=_T_SOLUBILITY,
      choices=["\\( 4.0 \\times 10^{-9} \\)", "\\( 1.0 \\times 10^{-6} \\)",
               "\\( 1.0 \\times 10^{-9} \\)", "\\( 2.0 \\times 10^{-6} \\)",
               "\\( 8.0 \\times 10^{-9} \\)"],
      ans=0,
      why="Salt L releases one cation and two anions, so its constant is four times the "
          "cube of the tabulated solubility. Salts J and L have the same solubility but "
          "different constants, which is exactly why a constant cannot be compared across "
          "formula types."),

 dict(q="Salts J and L in the table have the same molar solubility but different "
        "solubility-product constants. What does that establish?",
      table=_T_SOLUBILITY,
      choices=[
        "That the relationship between Ksp and solubility depends on how many ions the "
        "formula unit releases",
        "That one of the two tabulated solubilities must have been measured incorrectly",
        "That Ksp is not related to solubility for any salt at all",
        "That the two salts must be at different temperatures",
        "That the salt with the larger constant is always the more soluble"],
      ans=0,
      why="EK 7.11.A.2 makes solubility calculable from Ksp, but the calculation runs "
          "through the stoichiometry of the dissolution. Two salts of different formula "
          "types with equal solubilities therefore have unequal constants, which is the "
          "limit on comparing constants directly."),

 dict(q="Using the same table, which salt has the largest solubility-product constant?",
      table=_T_SOLUBILITY,
      choices=["Salt M", "Salt J", "Salt L",
               "Salts J and L, which are tied", "All three are equal"],
      ans=0,
      why="Salt M is a one-to-one salt with the largest tabulated solubility, so its "
          "constant is the square of that value and comes out larger than the square "
          "computed for salt J or the four-times-cube computed for salt L."),

 dict(q="A saturated solution of a one-to-one salt is analysed and found to contain "
        "\\( 5.0 \\times 10^{-5} \\) M of its cation. What is the solubility-product "
        "constant of that salt?",
      choices=["\\( 2.5 \\times 10^{-9} \\)", "\\( 5.0 \\times 10^{-5} \\)",
               "\\( 1.0 \\times 10^{-4} \\)", "\\( 2.5 \\times 10^{-10} \\)",
               "\\( 5.0 \\times 10^{-10} \\)"],
      ans=0,
      why="EK 7.11.A.4 states that the molar solubility of one or more species in a "
          "saturated solution can be used to calculate Ksp. For a one-to-one salt the "
          "anion is at the same concentration as the cation, so the product is the square "
          "of the measured value."),

 dict(q="Why is the concentration of the undissolved solid left out of a "
        "solubility-product expression?",
      choices=[
        "Because a pure solid has a concentration that does not depend on how much of it "
        "is present",
        "Because a solid cannot take part in a reversible process",
        "Because the solid is completely consumed once the solution is saturated",
        "Because the solid appears on the same side of the equation as the ions",
        "Because including it would make the constant negative"],
      ans=0,
      why="EK 7.11.A.1 makes dissolution a reversible process described by Ksp, and an "
          "equilibrium expression omits any species whose concentration does not depend "
          "on the amount present. In a saturated solution undissolved solid is still "
          "there, so it is not consumed."),

 dict(q="Salt V releases one cation and one anion and has a solubility-product constant "
        "of \\( 1.0 \\times 10^{-10} \\). Salt W releases one cation and two anions and "
        "has a solubility-product constant of \\( 4.0 \\times 10^{-12} \\). Which salt is "
        "more soluble in pure water?",
      choices=[
        "Salt W, even though its constant is the smaller of the two",
        "Salt V, because its constant is the larger of the two",
        "Salt V, because a one-to-one salt is always the more soluble type",
        "They are equally soluble, because both constants are very small",
        "The comparison cannot be made without knowing the two molar masses"],
      ans=0,
      why="EK 7.11.A.2 makes solubility calculable from Ksp, and the calculation depends "
          "on the formula type. The square root of the first constant is ten to the "
          "negative fifth, while the cube root of a quarter of the second is ten to the "
          "negative fourth, so the salt with the smaller constant dissolves ten times as "
          "far."),

 dict(q="A saturated solution of a salt releasing one cation and two anions is found to "
        "contain \\( 4.0 \\times 10^{-3} \\) M of its ANION. What is the molar solubility "
        "of the salt?",
      choices=["\\( 2.0 \\times 10^{-3} \\) M", "\\( 4.0 \\times 10^{-3} \\) M",
               "\\( 8.0 \\times 10^{-3} \\) M", "\\( 1.0 \\times 10^{-3} \\) M",
               "\\( 2.0 \\times 10^{-6} \\) M"],
      ans=0,
      why="Two anions are released per formula unit, so the anion concentration is twice "
          "the molar solubility and the solubility is half the measured value. EK "
          "7.11.A.4 allows the constant to be built from the concentration of any one "
          "species once the stoichiometry is applied."),

 dict(q="Using the table of constants, what is the molar solubility of salt P in pure "
        "water?",
      table=_T_KSPS,
      choices=["0.00010 M", "0.000010 M", "0.0010 M", "0.010 M", "0.00000010 M"],
      ans=0,
      why="Salt P releases one of each ion, so EK 7.11.A.2 makes its solubility the "
          "square root of the tabulated constant, and the square root of ten to the "
          "negative eighth is ten to the negative fourth."),

 dict(q="Using the same table of constants, what is the molar solubility of salt R in "
        "pure water?",
      table=_T_KSPS,
      choices=["0.0010 M", "0.00010 M", "0.000063 M", "0.0020 M", "0.010 M"],
      ans=0,
      why="Salt R releases one cation and two anions, so its constant is four times the "
          "cube of the solubility. A quarter of the tabulated constant is ten to the "
          "negative ninth, whose cube root is ten to the negative third."),

 dict(q="Using the same table, which salt would the solubility rules class as soluble?",
      table=_T_KSPS,
      choices=["Salt T", "Salt P", "Salt R", "Salts P and R", "None of the three"],
      ans=0,
      why="EK 7.11.A.3 relates the solubility rules to Ksp by making a constant greater "
          "than one the mark of a soluble salt. Only one of the three tabulated constants "
          "exceeds one."),

 dict(q="Two salts of the SAME formula type are compared, and the first has a "
        "solubility-product constant one hundred times that of the second. How do their "
        "molar solubilities in pure water compare, if each releases one cation and one "
        "anion?",
      choices=[
        "The first is ten times as soluble as the second",
        "The first is one hundred times as soluble as the second",
        "The first is twice as soluble as the second",
        "The two are equally soluble, since the formula type is the same",
        "The second is ten times as soluble as the first"],
      ans=0,
      why="For a one-to-one salt EK 7.11.A.2 makes the solubility the square root of the "
          "constant, and the square root of one hundred is ten. A ratio of constants is "
          "therefore not the ratio of solubilities."),

 dict(q="A student ranks four salts by solubility using their solubility-product "
        "constants alone, without checking their formulas. What is the risk in that "
        "procedure?",
      choices=[
        "A salt releasing more ions can be more soluble than one with a larger constant",
        "The constants may all have been measured at different temperatures",
        "The constants of insoluble salts cannot be measured at all",
        "The ranking will be exactly reversed from the true order",
        "There is no risk, because a larger constant always means a more soluble salt"],
      ans=0,
      why="EK 7.11.A.2 makes solubility calculable from Ksp, but the function relating "
          "them depends on how many ions the formula unit releases. A one-to-two salt "
          "with a smaller constant can be the more soluble, so the ranking must be made "
          "on the computed solubilities."),

 dict(q="Which change describes what happens to a saturated solution in contact with "
        "excess solid when a little more of the same solid is added at constant "
        "temperature?",
      choices=[
        "Nothing measurable changes, because the solution was already saturated and Ksp "
        "is unchanged",
        "The ion concentrations rise until the added solid has dissolved",
        "The value of Ksp rises in proportion to the amount of solid added",
        "The solution becomes unsaturated and can dissolve still more solid",
        "The ion concentrations fall as the added solid draws ions out of solution"],
      ans=0,
      why="EK 7.11.A.1 makes dissolution a reversible process whose extent is set by Ksp "
          "at a given temperature. A saturated solution already satisfies that constant, "
          "and adding more of a pure solid changes nothing in the expression."),

 dict(q="A one-to-one salt has a solubility-product constant of \\( 2.5 \\times 10^{-1} "
        "\\). What does that value indicate under the course framework?",
      choices=[
        "The salt is only sparingly soluble, since the constant is below one",
        "The salt is soluble by the solubility rules, since the constant is above zero",
        "The salt is soluble by the solubility rules, since the constant is above one",
        "The salt cannot dissolve at all, since the constant is a fraction",
        "The constant says nothing about solubility for a one-to-one salt"],
      ans=0,
      why="EK 7.11.A.3 makes a Ksp greater than one the mark of a salt classed as "
          "soluble, and this constant is a quarter, which is less than one. Being "
          "positive is not the criterion the framework gives."),

 dict(q="Why can the molar solubility of a salt be obtained from the concentration of "
        "just ONE of its ions in a saturated solution?",
      choices=[
        "Because the stoichiometry of the dissolution fixes the ratio of that ion to the "
        "formula units that dissolved",
        "Because every salt releases exactly one of each ion per formula unit",
        "Because the two ion concentrations in a saturated solution are always equal",
        "Because the concentration of one ion is always half the value of Ksp",
        "Because the other ion does not appear in the solubility-product expression"],
      ans=0,
      why="EK 7.11.A.4 says the molar solubility of one OR MORE species in a saturated "
          "solution can be used to calculate Ksp, and the link is the balanced "
          "dissolution equation: a known ratio of ions to formula units converts one "
          "measurement into the solubility."),

 dict(q="A salt releasing two cations and one anion per formula unit has molar solubility "
        "s. Which expression gives its solubility-product constant?",
      choices=["\\( K_{sp} = 4s^{3} \\)", "\\( K_{sp} = 2s^{3} \\)",
               "\\( K_{sp} = s^{3} \\)", "\\( K_{sp} = 2s^{2} \\)",
               "\\( K_{sp} = 8s^{3} \\)"],
      ans=0,
      why="The cation is present at twice the solubility and the anion at the solubility "
          "itself, so the product is the square of two s multiplied by s, which is four s "
          "cubed. The squared cation term is what supplies the factor of four rather than "
          "a factor of two."),

 dict(q="At a higher temperature a salt is found to have a larger solubility-product "
        "constant. What follows about its molar solubility in pure water?",
      choices=[
        "It is larger at the higher temperature, since solubility rises with the constant "
        "for a fixed formula type",
        "It is unchanged, since the formula type has not changed",
        "It is smaller at the higher temperature, since a larger constant leaves fewer "
        "ions in solution",
        "It cannot be inferred, because Ksp and solubility are unrelated quantities",
        "It is larger only if the salt releases exactly two ions per formula unit"],
      ans=0,
      why="EK 7.11.A.2 makes the solubility calculable from Ksp, and for one salt the "
          "formula type is fixed, so the solubility is an increasing function of the "
          "constant. The comparison here is of one salt with itself, which is the case "
          "where reading Ksp directly is safe."),

]
