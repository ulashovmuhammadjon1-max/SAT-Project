# AP CHEMISTRY 7.12 Common-Ion Effect
# CED effective Fall 2024, Unit 7 Equilibrium.
# Learning objective 7.12.A: identify the solubility of a salt, and/or the value of Ksp
# for the salt, based on the concentration of a common ion already present in solution.
# Suggested skill 2.F, explain how modifications to an experimental procedure will alter
# results.
#
# Essential knowledge relied on, in the framework's own words:
#   7.12.A.1  The solubility of a salt is reduced when it is dissolved into a solution
#             that already contains one of the ions present in the salt. The impact of
#             this "common-ion effect" on solubility can be understood qualitatively using
#             Le Chatelier's principle or calculated from the Ksp for the dissolution
#             process.
#
# SCOPE. 7.11 owns dissolution into PURE WATER; every item there is a pure-water
# calculation and none mentions a shared ion. Every item below has the salt dissolving into
# a solution that ALREADY contains one of its own ions, which is the one thing this topic
# is. 8.11 owns the separate case where the shared species is a proton, so nothing here
# changes the pH.
#
# THE TWO ROUTES EK 7.12.A.1 NAMES ARE BOTH USED, and the module keeps them apart: items
# 1-6, 9, 12, 16, 20, 22, 25, 27, 29 and 30 take the qualitative Le Chatelier route, and
# items 7, 8, 10, 11, 13, 14, 15, 17, 18, 19, 21, 23, 24, 26 and 28 calculate from Ksp.
#
# ARITHMETIC. When a common ion is present at a concentration far above the solubility,
# the amount the dissolving salt contributes to it is negligible, and every number below
# is chosen so that approximation is exact to the digits shown. verify_h7_12.py recomputes
# each one AND checks that the neglected contribution really is negligible, which is the
# assumption a wrong answer here would hide.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span is
# hand-written; formulas in prose stay plain text (AgCl, NaCl, PbI2).
TOPIC = ("7.12", "Common-Ion Effect", 7)

_T_SOLUTIONS = dict(
    headers=["Solution", "Solute dissolved in it", "Ions present in solution"],
    rows=[["1", "NaCl", "sodium ion and chloride ion"],
          ["2", "NaNO3", "sodium ion and nitrate ion"],
          ["3", "AgNO3", "silver ion and nitrate ion"],
          ["4", "CaCl2", "calcium ion and chloride ion"]])

_T_CHLORIDE = dict(
    headers=["Beaker", "Chloride ion concentration already present (M)"],
    rows=[["A", "0.010"],
          ["B", "0.10"],
          ["C", "1.0"]])

_T_TRIALS = dict(
    headers=["Trial", "Solution the salt was added to",
             "Molar solubility measured (M)"],
    rows=[["1", "pure water", "0.0010"],
          ["2", "0.010 M solution of a salt sharing the anion", "0.00010"],
          ["3", "0.10 M solution of a salt sharing the anion", "0.000010"]])

QUESTIONS = [

 dict(q="What does the course framework say happens to the solubility of a salt when it "
        "is dissolved into a solution that already contains one of the ions present in "
        "that salt?",
      choices=[
        "The solubility is reduced",
        "The solubility is increased",
        "The solubility is unchanged",
        "The solubility becomes exactly zero",
        "The solubility is reduced only if the shared ion is the cation"],
      ans=0,
      why="EK 7.12.A.1 states it directly: the solubility of a salt is reduced when it is "
          "dissolved into a solution that already contains one of the ions present in the "
          "salt. The statement makes no distinction between a shared cation and a shared "
          "anion, and a reduced solubility is not a zero solubility."),

 dict(q="Solid AgCl is added to a 0.10 M solution of NaCl rather than to pure water. "
        "Using Le Chatelier's principle, why does less of it dissolve?",
      choices=[
        "The chloride ion already present pushes the dissolution equilibrium back toward "
        "the undissolved solid",
        "The sodium ion already present reacts with the silver ion to form a new "
        "compound",
        "The dissolution equilibrium is destroyed once any other salt is present",
        "The solubility-product constant of AgCl falls when NaCl is added",
        "The added chloride ion raises the temperature of the solution"],
      ans=0,
      why="EK 7.12.A.1 offers Le Chatelier's principle as the qualitative route. The "
          "chloride ion is a product of the dissolution equilibrium, so a supply of it "
          "already in solution is relieved by the reverse direction, which keeps more of "
          "the salt undissolved. The constant itself is fixed by temperature."),

 dict(q="Using the table, in which solution would solid AgCl be MOST soluble?",
      table=_T_SOLUTIONS,
      choices=["Solution 2", "Solution 1", "Solution 3", "Solution 4",
               "AgCl is equally soluble in all four"],
      ans=0,
      why="EK 7.12.A.1 reduces the solubility only where the solution already contains an "
          "ion present in the salt. AgCl supplies silver ion and chloride ion, and "
          "exactly one tabulated solution contains neither of those, so it is the only "
          "one in which the solubility is not reduced."),

 dict(q="Using the same table, which solution reduces the solubility of AgCl by "
        "supplying the same CATION that AgCl releases?",
      table=_T_SOLUTIONS,
      choices=["Solution 3", "Solution 1", "Solution 2", "Solution 4",
               "No tabulated solution supplies that cation"],
      ans=0,
      why="AgCl releases silver ion and chloride ion. Two tabulated solutions supply "
          "chloride ion and exactly one supplies silver ion, which is the cation of the "
          "salt, so EK 7.12.A.1's reduction operates through the cation in that one case "
          "and through the anion in the others."),

 dict(q="Using the same table, which solutions would each reduce the solubility of "
        "AgCl?",
      table=_T_SOLUTIONS,
      choices=["Solutions 1, 3 and 4", "Solutions 1, 2 and 3", "Solutions 2, 3 and 4",
               "Solutions 1, 2 and 4", "All four solutions"],
      ans=0,
      why="EK 7.12.A.1 requires an ion already present that also appears in the salt. Two "
          "tabulated solutions supply chloride ion and one supplies silver ion, and all "
          "three of those ions appear in AgCl, while nitrate, sodium and calcium do not."),

 dict(q="A student claims the common-ion effect works because the added ion physically "
        "blocks the surface of the solid. What is the better account, according to the "
        "framework?",
      choices=[
        "The added ion is one of the products of the dissolution equilibrium, so its "
        "presence shifts that equilibrium back toward the solid",
        "The added ion lowers the value of the solubility-product constant of the salt",
        "The added ion changes the identity of the salt into a less soluble compound",
        "The added ion raises the concentration of water, which dilutes the solution",
        "The added ion increases the rate at which the solid dissolves but not the "
        "extent"],
      ans=0,
      why="EK 7.12.A.1 says the effect can be understood qualitatively using Le "
          "Chatelier's principle, which treats the dissolved ions as products of a "
          "reversible process. Supplying a product shifts the process back toward the "
          "reactant, which is the undissolved salt. The constant is a function of "
          "temperature and does not change."),

 dict(q="A one-to-one salt has a solubility-product constant of \\( 1.0 \\times 10^{-10} "
        "\\). What is its molar solubility in a 0.10 M solution of a soluble salt sharing "
        "its anion?",
      choices=["\\( 1.0 \\times 10^{-9} \\) M", "\\( 1.0 \\times 10^{-5} \\) M",
               "\\( 1.0 \\times 10^{-11} \\) M", "\\( 1.0 \\times 10^{-4} \\) M",
               "\\( 1.0 \\times 10^{-10} \\) M"],
      ans=0,
      why="EK 7.12.A.1 allows the effect to be calculated from Ksp. The anion "
          "concentration is held at 0.10 M by the salt already in solution, so the "
          "solubility is the constant divided by that value. In pure water the same salt "
          "would dissolve to ten to the negative fifth molar, so the reduction is by four "
          "powers of ten."),

 dict(q="That same one-to-one salt with a constant of \\( 1.0 \\times 10^{-10} \\) is "
        "instead added to a 0.010 M solution sharing its anion. What is its molar "
        "solubility there?",
      choices=["\\( 1.0 \\times 10^{-8} \\) M", "\\( 1.0 \\times 10^{-9} \\) M",
               "\\( 1.0 \\times 10^{-12} \\) M", "\\( 1.0 \\times 10^{-5} \\) M",
               "\\( 1.0 \\times 10^{-6} \\) M"],
      ans=0,
      why="The constant divided by the fixed anion concentration of 0.010 M gives ten to "
          "the negative eighth. A less concentrated common ion reduces the solubility "
          "less, which is the pattern EK 7.12.A.1 describes."),

 dict(q="Using the table of beakers, in which beaker would a one-to-one silver salt be "
        "most soluble?",
      table=_T_CHLORIDE,
      choices=["Beaker A", "Beaker B", "Beaker C",
               "All three give the same solubility",
               "The comparison requires the value of Ksp"],
      ans=0,
      why="EK 7.12.A.1 makes the reduction larger the more of the shared ion is already "
          "present, so the smallest tabulated concentration leaves the salt most soluble. "
          "The ranking follows from the concentrations alone and does not need the value "
          "of the constant."),

 dict(q="A one-to-one silver salt has a constant of \\( 1.0 \\times 10^{-10} \\). Using "
        "the table of beakers, what is its molar solubility in beaker C?",
      table=_T_CHLORIDE,
      choices=["\\( 1.0 \\times 10^{-10} \\) M", "\\( 1.0 \\times 10^{-9} \\) M",
               "\\( 1.0 \\times 10^{-5} \\) M", "\\( 1.0 \\times 10^{-8} \\) M",
               "\\( 1.0 \\times 10^{-11} \\) M"],
      ans=0,
      why="The chloride concentration in that beaker is held at 1.0 M, so dividing the "
          "constant by it leaves the solubility numerically equal to the constant. That "
          "is the largest reduction of the three beakers, as EK 7.12.A.1 predicts for the "
          "largest common-ion concentration."),

 dict(q="How many times smaller is the solubility of a one-to-one salt of constant \\( "
        "1.0 \\times 10^{-10} \\) in a 0.10 M solution sharing its anion than in pure "
        "water?",
      choices=["10,000 times smaller", "10 times smaller", "100 times smaller",
               "1,000 times smaller", "100,000 times smaller"],
      ans=0,
      why="In pure water the solubility is the square root of the constant, ten to the "
          "negative fifth. With the anion held at 0.10 M it is the constant divided by "
          "that, ten to the negative ninth. The ratio of the two is ten thousand, which "
          "is the size of the reduction EK 7.12.A.1 names."),

 dict(q="Solid PbI2 is added to a solution of KI. Which species already in the solution "
        "is responsible for reducing the solubility of PbI2?",
      choices=["The iodide ion", "The potassium ion", "The lead ion",
               "The water molecules", "No species in the solution is responsible"],
      ans=0,
      why="EK 7.12.A.1 requires an ion already present that also appears in the salt "
          "being dissolved. PbI2 releases lead ion and iodide ion, and the solution of KI "
          "supplies potassium ion and iodide ion, so iodide is the shared species. Lead "
          "ion is not present until the salt dissolves."),

 dict(q="A salt releasing one cation and two anions has a solubility-product constant of "
        "\\( 4.0 \\times 10^{-12} \\). What is its molar solubility in a 0.10 M solution "
        "of a soluble salt sharing its ANION?",
      choices=["\\( 4.0 \\times 10^{-10} \\) M", "\\( 4.0 \\times 10^{-11} \\) M",
               "\\( 2.0 \\times 10^{-6} \\) M", "\\( 1.0 \\times 10^{-4} \\) M",
               "\\( 4.0 \\times 10^{-13} \\) M"],
      ans=0,
      why="The anion concentration is held at 0.10 M by the salt already present, and it "
          "enters the expression squared, so the solubility is the constant divided by "
          "the square of 0.10, which is the constant divided by 0.010. Forgetting to "
          "square the common-ion concentration gives ten times too small a value."),

 dict(q="A salt releasing one cation and two anions has a solubility-product constant of "
        "\\( 4.0 \\times 10^{-11} \\). What is the ANION concentration contributed by "
        "that salt when it is added to a 0.10 M solution sharing its CATION?",
      choices=["\\( 2.0 \\times 10^{-5} \\) M", "\\( 4.0 \\times 10^{-10} \\) M",
               "\\( 1.0 \\times 10^{-5} \\) M", "\\( 4.0 \\times 10^{-6} \\) M",
               "\\( 2.0 \\times 10^{-6} \\) M"],
      ans=0,
      why="The cation is held at 0.10 M, so the square of the anion concentration is the "
          "constant divided by 0.10, which is four times ten to the negative tenth, and "
          "the anion concentration is its square root. The molar solubility of the salt "
          "is half that value, since two anions come from each formula unit."),

 dict(q="For the salt in the previous calculation, with a constant of \\( 4.0 \\times "
        "10^{-11} \\) in a 0.10 M solution sharing its cation, what is the MOLAR "
        "SOLUBILITY of the salt itself?",
      choices=["\\( 1.0 \\times 10^{-5} \\) M", "\\( 2.0 \\times 10^{-5} \\) M",
               "\\( 4.0 \\times 10^{-5} \\) M", "\\( 5.0 \\times 10^{-6} \\) M",
               "\\( 4.0 \\times 10^{-10} \\) M"],
      ans=0,
      why="Each formula unit that dissolves releases two anions, so the molar solubility "
          "is half the anion concentration of two times ten to the negative fifth. "
          "Reporting the anion concentration itself is the error the stoichiometry is "
          "there to catch."),

 dict(q="Why does adding a soluble salt with NO ion in common leave the solubility of a "
        "sparingly soluble salt essentially unchanged?",
      choices=[
        "Because neither ion of the added salt appears in the dissolution equilibrium of "
        "the sparingly soluble salt",
        "Because the added salt is soluble and so cannot affect any other salt",
        "Because the added salt raises and lowers the solubility by equal amounts",
        "Because the solubility-product constant is defined only for pure water",
        "Because the added salt precipitates before it can have any effect"],
      ans=0,
      why="EK 7.12.A.1 makes the reduction depend on the solution ALREADY CONTAINING one "
          "of the ions present in the salt. A salt supplying two unrelated ions puts "
          "nothing into the equilibrium expression, so there is no product term to shift "
          "the equilibrium back."),

 dict(q="A saturated solution of a one-to-one salt is prepared in 0.20 M of a solution "
        "sharing its anion, and the salt's molar solubility there is measured as \\( 5.0 "
        "\\times 10^{-10} \\) M. What is the solubility-product constant of the salt?",
      choices=["\\( 1.0 \\times 10^{-10} \\)", "\\( 2.5 \\times 10^{-19} \\)",
               "\\( 5.0 \\times 10^{-10} \\)", "\\( 2.5 \\times 10^{-10} \\)",
               "\\( 1.0 \\times 10^{-9} \\)"],
      ans=0,
      why="EK 7.12.A.1 allows the value of Ksp to be obtained from a measurement made in "
          "the presence of a common ion. The cation concentration is the measured "
          "solubility and the anion concentration is fixed at 0.20 M, so the product is "
          "the two multiplied together. Squaring the solubility, as one would in pure "
          "water, gives a far smaller and wrong value."),

 dict(q="The table lists three measurements of the same salt. What do the three trials "
        "establish about the common-ion effect?",
      table=_T_TRIALS,
      choices=[
        "Each tenfold increase in the shared ion lowers the measured solubility by a "
        "factor of ten",
        "Each tenfold increase in the shared ion lowers the measured solubility by a "
        "factor of one hundred",
        "The measured solubility is unaffected by the concentration of the shared ion",
        "The measured solubility rises with the concentration of the shared ion",
        "The measured solubility falls to zero once any shared ion is present"],
      ans=0,
      why="Between the second and third trials the shared-ion concentration rises "
          "tenfold and the measured solubility falls tenfold, which is what a one-to-one "
          "salt "
          "requires when the constant is the product of the solubility and a fixed "
          "shared-ion concentration. It is a reduction, not an abolition, as EK 7.12.A.1 "
          "says."),

 dict(q="Using the same three trials, what is the solubility-product constant of the salt "
        "as computed from trial 3?",
      table=_T_TRIALS,
      choices=["\\( 1.0 \\times 10^{-6} \\)", "\\( 1.0 \\times 10^{-10} \\)",
               "\\( 1.0 \\times 10^{-5} \\)", "\\( 1.0 \\times 10^{-11} \\)",
               "\\( 1.0 \\times 10^{-7} \\)"],
      ans=0,
      why="In trial 3 the shared ion is held at 0.10 M and the measured solubility "
          "supplies the other ion, so the constant is the product of those two values. "
          "The same product is obtained from trial 1 by squaring the pure-water "
          "solubility, which is the consistency check on the set."),

 dict(q="A chemist wants to recover as much of a dissolved silver salt as possible from a "
        "solution. Which procedure does the common-ion effect recommend?",
      choices=[
        "Add an excess of a soluble salt that supplies the same anion as the silver salt",
        "Add an excess of a soluble salt that supplies two ions unrelated to the silver "
        "salt",
        "Dilute the solution with a large volume of pure water",
        "Warm the solution so that the salt reaches its equilibrium faster",
        "Add more of the solid silver salt to the same solution"],
      ans=0,
      why="EK 7.12.A.1 makes solubility fall when an ion of the salt is already present, "
          "so flooding the solution with the shared ion drives the salt out of solution. "
          "Dilution works in the opposite direction, and an unrelated salt supplies no "
          "shared ion."),

 dict(q="Which quantity is NOT changed when a sparingly soluble salt is dissolved into a "
        "solution containing one of its ions, at constant temperature?",
      choices=[
        "The value of the solubility-product constant",
        "The molar solubility of the salt",
        "The mass of salt that dissolves in a litre of the solution",
        "The concentration of the ion not shared with the solution",
        "The number of moles of solid that remain undissolved"],
      ans=0,
      why="EK 7.12.A.1 has the common ion reduce the SOLUBILITY and be calculated FROM "
          "Ksp, which means the constant is the fixed quantity in the calculation. It is "
          "a function of temperature, so it is what stays put while every amount in the "
          "beaker changes."),

 dict(q="A one-to-one salt of constant \\( 9.0 \\times 10^{-12} \\) is added to a 0.030 M "
        "solution sharing its cation. What is its molar solubility?",
      choices=["\\( 3.0 \\times 10^{-10} \\) M", "\\( 3.0 \\times 10^{-6} \\) M",
               "\\( 9.0 \\times 10^{-10} \\) M", "\\( 2.7 \\times 10^{-13} \\) M",
               "\\( 1.0 \\times 10^{-10} \\) M"],
      ans=0,
      why="The cation is held at 0.030 M by the salt already present, so the anion "
          "concentration, which equals the molar solubility, is the constant divided by "
          "0.030. In pure water the solubility would be three times ten to the negative "
          "sixth, so the common ion has reduced it by four powers of ten."),

 dict(q="Two beakers hold the same sparingly soluble salt in contact with solution. One "
        "contains pure water and the other a solution of a salt sharing its anion. Which "
        "comparison of the CATION concentrations is correct?",
      choices=[
        "The cation concentration is lower in the beaker containing the shared anion",
        "The cation concentration is higher in the beaker containing the shared anion",
        "The two cation concentrations are equal, since the constant is the same",
        "The cation concentration is zero in the beaker containing the shared anion",
        "The comparison depends on which salt supplied the shared anion"],
      ans=0,
      why="The cation enters solution only from the sparingly soluble salt, so its "
          "concentration IS the molar solubility, and EK 7.12.A.1 reduces that where a "
          "shared ion is already present. The constant being equal in the two beakers is "
          "what forces the cation term down when the anion term is raised."),

 dict(q="A one-to-one salt has a constant of \\( 2.0 \\times 10^{-9} \\). In which "
        "solution is its molar solubility exactly \\( 1.0 \\times 10^{-8} \\) M?",
      choices=["A 0.20 M solution of a salt sharing its anion",
               "A 0.020 M solution of a salt sharing its anion",
               "A 2.0 M solution of a salt sharing its anion",
               "A 0.10 M solution of a salt sharing its anion",
               "Pure water at the same temperature"],
      ans=0,
      why="The solubility is the constant divided by the concentration of the shared ion, "
          "so the required concentration is the constant divided by the stated solubility, "
          "which is 0.20 M. In pure water the same salt would dissolve to about four "
          "times ten to the negative fifth molar."),

 dict(q="Which statement about the common-ion effect and Le Chatelier's principle is "
        "supported by the course framework?",
      choices=[
        "The effect can be understood qualitatively using the principle, or calculated "
        "from the solubility-product constant",
        "The effect can only be understood qualitatively, since no calculation applies "
        "to it",
        "The effect can only be calculated, since the principle does not apply to "
        "dissolution",
        "The principle and the constant give opposite predictions about the effect",
        "The principle applies only when the shared ion is the cation of the salt"],
      ans=0,
      why="EK 7.12.A.1 offers both routes in one sentence: the impact of the common-ion "
          "effect on solubility can be understood qualitatively using Le Chatelier's "
          "principle or calculated from the Ksp for the dissolution process. The two "
          "agree, which is why either may be used."),

 dict(q="A student measures the molar solubility of a one-to-one salt in a solution "
        "containing a shared ion and then computes the constant by SQUARING that "
        "solubility. What is wrong with the calculation?",
      choices=[
        "The two ion concentrations are not equal here, so the constant is the product of "
        "the solubility and the much larger shared-ion concentration",
        "The constant cannot be computed at all when a shared ion is present",
        "The solubility must be doubled rather than squared when a shared ion is present",
        "The constant must be divided by the shared-ion concentration rather than "
        "multiplied",
        "Nothing is wrong, since squaring the solubility always gives the constant"],
      ans=0,
      why="Squaring works in pure water only because both ions arrive from the dissolving "
          "salt in equal amounts. Where one ion is already present at a much higher "
          "concentration, EK 7.12.A.1's calculation from Ksp uses the actual "
          "concentration of each ion, which are far from equal."),

 dict(q="A saturated solution of a sparingly soluble salt is in contact with excess "
        "solid. A concentrated solution supplying the salt's anion is added dropwise. "
        "What is observed?",
      choices=[
        "More solid appears, because the reduced solubility can no longer support the "
        "dissolved cation already present",
        "The solid dissolves further, because the total ion concentration has risen",
        "Nothing changes, because the solution was already saturated",
        "The solid dissolves further, because the added solution increases the volume",
        "The solid changes into a different compound with a larger constant"],
      ans=0,
      why="EK 7.12.A.1 reduces the solubility when a shared ion is supplied, so the "
          "cation already dissolved is now more than the solution can hold, and the "
          "excess leaves as solid. That precipitation is the qualitative form of the "
          "effect under Le Chatelier's principle."),

 dict(q="A salt releasing one cation and two anions is added to a solution already "
        "containing its anion. In the solubility-product expression, how does that "
        "shared-ion concentration enter?",
      choices=[
        "As a squared term, because two of that ion appear in the formula unit",
        "As a term to the first power, because only one solution supplied it",
        "As a term to the first power, because the solid supplies the rest",
        "Not at all, because it did not come from the dissolving salt",
        "As a cubed term, because three ions in total are released"],
      ans=0,
      why="The exponent in the expression comes from the coefficient in the dissolution "
          "equation, not from where the ion originated. EK 7.12.A.1's calculation from "
          "Ksp therefore squares the total anion concentration, which the added solution "
          "has fixed."),

 dict(q="Under what circumstance is it safe to treat the shared-ion concentration as "
        "unchanged by the small amount of salt that dissolves?",
      choices=[
        "When the shared ion is already present at a concentration far larger than the "
        "molar solubility of the salt",
        "When the salt is a one-to-one salt rather than a one-to-two salt",
        "When the solubility-product constant is greater than one",
        "When the shared ion is the cation rather than the anion",
        "Under every circumstance, since a sparingly soluble salt never affects a "
        "solution"],
      ans=0,
      why="The approximation is a statement about relative sizes: the dissolving salt "
          "adds its molar solubility to a pool already far larger, so the total is "
          "unchanged to the digits reported. It has nothing to do with the formula type "
          "or with which ion is shared, and a constant above one would describe a salt "
          "that is not sparingly soluble at all."),

 dict(q="Two students disagree about a beaker in which a sparingly soluble salt sits in a "
        "solution sharing its anion. One says the constant is smaller than in pure water; "
        "the other says the constant is the same and only the solubility is smaller. Who "
        "is right, and why?",
      choices=[
        "The second, because the constant depends on temperature while the solubility "
        "depends on what else is in the solution",
        "The first, because the constant is defined by the measured solubility in each "
        "solution",
        "The first, because a smaller solubility must mean a smaller constant",
        "Neither, because both the constant and the solubility are unchanged",
        "Neither, because the constant rises while the solubility falls"],
      ans=0,
      why="EK 7.12.A.1 has the effect CALCULATED FROM the constant, which treats the "
          "constant as the fixed input and the solubility as the output. The constant "
          "belongs to the salt at a temperature; the solubility belongs to the salt in a "
          "particular solution."),

]
