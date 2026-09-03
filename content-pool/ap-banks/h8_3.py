# AP CHEMISTRY 8.3 Weak Acid and Base Equilibria
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.3.A: explain the relationship among pH, pOH, and concentrations of
# all species in a solution of a monoprotic weak acid or weak base. Suggested skill 5.C,
# explain the relationship between variables within an equation when one variable changes.
#
# Essential knowledge relied on, in the framework's own words:
#   8.3.A.1  Weak acids react with water to produce hydronium ions. However, only a small
#            percentage of molecules of a weak acid will ionize in this way. Thus the
#            concentration of H3O+ is much less than the initial concentration of the
#            molecular acid, and the vast majority of the acid molecules remain un-ionized.
#   8.3.A.2  A solution of a weak acid involves equilibrium between an un-ionized acid and
#            its conjugate base. The equilibrium constant is Ka, often reported as pKa. The
#            pH can be determined from the initial acid concentration and the pKa.
#            EQN: Ka = [H3O+][A-]/[HA]      EQN: pKa = -log Ka
#   8.3.A.3  Weak bases react with water to produce hydroxide ions, but ordinarily only a
#            small percentage of the molecules ionize, so [OH-] does not equal the initial
#            concentration of the base.
#   8.3.A.4  A solution of a weak base involves equilibrium between an un-ionized base and
#            its conjugate acid, with constant Kb, often reported as pKb.
#            EQN: Kb = [OH-][HB+]/[B]       EQN: pKb = -log Kb
#   8.3.A.5  The percent ionization of a weak acid (or base) can be calculated from its pKa
#            (pKb) and the initial concentration, or from the initial concentration and the
#            equilibrium concentration of any species in the expression.
#   8.3.A.6  For any conjugate acid-base pair, Kw = Ka x Kb and pKw = pKa + pKb.
#
# SCOPE. 8.2 owns the strong acids and bases, where ionization is complete. 8.7 owns which
# FORM predominates at a given pH, and 8.9 owns the Henderson-Hasselbalch arithmetic for a
# solution containing BOTH members of a pair. Every solution below is a weak acid alone or
# a weak base alone in water, and no item here adds the conjugate deliberately.
#
# ARITHMETIC AND ITS ASSUMPTION. Each pH here comes from the standard one-step result that
# the hydronium concentration is the square root of Ka times the initial concentration,
# which rests on EK 8.3.A.1's own statement that only a small percentage ionizes. Every
# number is chosen so the logarithm is exact AND so the ionized fraction stays at or below
# a few percent; verify_h8_3.py recomputes each value and asserts that fraction, so an item
# whose numbers quietly broke the assumption could not pass.
#
# NOTATION. export_units.py does not typeset Chemistry; every span is hand-written and
# every function name inside one is escaped.
TOPIC = ("8.3", "Weak Acid and Base Equilibria", 8)

_T_ACIDS = dict(
    headers=["Acid", "Ka at 298 K", "pKa"],
    rows=[["HA", "\\( 1.0 \\times 10^{-3} \\)", "3.00"],
          ["HB", "\\( 1.0 \\times 10^{-5} \\)", "5.00"],
          ["HD", "\\( 1.0 \\times 10^{-7} \\)", "7.00"]])

_T_IONIZATION = dict(
    headers=["Solution", "Initial acid concentration (M)",
             "Hydronium ion concentration at equilibrium (M)"],
    rows=[["1", "0.10", "0.0010"],
          ["2", "0.20", "0.0020"],
          ["3", "0.010", "0.0010"]])

_T_BASES = dict(
    headers=["Base", "Kb at 298 K", "pKb"],
    rows=[["B1", "\\( 1.0 \\times 10^{-5} \\)", "5.00"],
          ["B2", "\\( 1.0 \\times 10^{-9} \\)", "9.00"],
          ["B3", "\\( 1.0 \\times 10^{-11} \\)", "11.00"]])

QUESTIONS = [

 dict(q="What does the course framework say about the fraction of a weak acid's molecules "
        "that ionize in aqueous solution?",
      choices=[
        "Only a small percentage ionize, so the vast majority of the molecules remain "
        "un-ionized",
        "All of them ionize, so the hydronium concentration equals the initial "
        "concentration",
        "Exactly half of them ionize, whatever the initial concentration",
        "None of them ionize unless a strong base is also present",
        "The percentage that ionizes is the same for every weak acid"],
      ans=0,
      why="EK 8.3.A.1 states that only a small percentage of molecules of a weak acid will "
          "ionize, so the concentration of hydronium is much less than the initial "
          "concentration of the molecular acid and the vast majority remain un-ionized. "
          "Complete ionization is what EK 8.2.A.1 reserves for a strong acid."),

 dict(q="Which expression is the acid ionization constant for the weak acid HA?",
      choices=[
        "\\( K_a = \\frac{[\\mathrm{H_3O^+}][\\mathrm{A^-}]}{[\\mathrm{HA}]} \\)",
        "\\( K_a = \\frac{[\\mathrm{HA}]}{[\\mathrm{H_3O^+}][\\mathrm{A^-}]} \\)",
        "\\( K_a = [\\mathrm{H_3O^+}][\\mathrm{A^-}][\\mathrm{HA}] \\)",
        "\\( K_a = \\frac{[\\mathrm{A^-}]}{[\\mathrm{H_3O^+}][\\mathrm{HA}]} \\)",
        "\\( K_a = \\frac{[\\mathrm{OH^-}][\\mathrm{A^-}]}{[\\mathrm{HA}]} \\)"],
      ans=0,
      why="EK 8.3.A.2 gives the equation with the two product concentrations in the "
          "numerator and the un-ionized acid in the denominator. Hydroxide belongs to the "
          "base ionization constant of EK 8.3.A.4, not to Ka."),

 dict(q="A weak acid has an ionization constant of \\( 1.0 \\times 10^{-5} \\). What is "
        "its pKa?",
      choices=["pKa = 5.00", "pKa = 9.00", "pKa = 0.50", "pKa = 14.00", "pKa = 5.50"],
      ans=0,
      why="EK 8.3.A.2 defines pKa as the negative base-ten logarithm of Ka, and the "
          "logarithm of ten to the negative fifth is negative five. The value 9.00 is the "
          "pKb of the conjugate base under EK 8.3.A.6."),

 dict(q="A 1.0 M solution of a weak acid has an ionization constant of \\( 1.0 \\times "
        "10^{-6} \\). What is the pH of the solution?",
      choices=["pH = 3.00", "pH = 6.00", "pH = 1.00", "pH = 11.00", "pH = 3.50"],
      ans=0,
      why="EK 8.3.A.2 says the pH of a weak acid solution can be determined from the "
          "initial acid concentration and the constant. Because only a small percentage "
          "ionizes under EK 8.3.A.1, the hydronium concentration is the square root of the "
          "constant times the initial concentration, which is ten to the negative third."),

 dict(q="A 0.10 M solution of a weak acid has an ionization constant of \\( 1.0 \\times "
        "10^{-5} \\). What is the pH of the solution?",
      choices=["pH = 3.00", "pH = 5.00", "pH = 1.00", "pH = 2.00", "pH = 4.00"],
      ans=0,
      why="The hydronium concentration is the square root of the constant times the "
          "initial concentration, which is the square root of ten to the negative sixth, "
          "or ten to the negative third. EK 8.3.A.1's small percentage is what allows the "
          "initial concentration to be used in place of the equilibrium concentration."),

 dict(q="For the 0.10 M weak acid solution with an ionization constant of \\( 1.0 \\times "
        "10^{-5} \\), what percentage of the acid has ionized?",
      choices=["1.0 percent", "3.2 percent", "0.32 percent", "50 percent",
               "100 percent"],
      ans=0,
      why="EK 8.3.A.5 says the percent ionization can be calculated from the constant and "
          "the initial concentration. The hydronium concentration is 0.0010 M out of an "
          "initial 0.10 M, which is one part in a hundred. That small figure is the "
          "premise EK 8.3.A.1 states."),

 dict(q="A 0.10 M solution of a weak acid has an ionization constant of \\( 1.0 \\times "
        "10^{-6} \\). What is the pH of the solution?",
      choices=["pH = 3.50", "pH = 3.00", "pH = 6.00", "pH = 4.00", "pH = 7.00"],
      ans=0,
      why="The hydronium concentration is the square root of the product of the constant "
          "and the initial concentration, which is the square root of ten to the negative "
          "seventh, or ten to the negative three and a half. Halving an exponent is what "
          "produces the half-unit pH."),

 dict(q="Two weak acids are prepared at the same concentration, and one has a larger "
        "ionization constant than the other. Which solution has the lower pH?",
      choices=[
        "The one with the larger constant, because a larger constant means more hydronium "
        "at equilibrium",
        "The one with the smaller constant, because a smaller constant means more "
        "hydronium at equilibrium",
        "They have the same pH, because both acids are weak",
        "The one with the smaller constant, because a smaller constant means a larger pKa",
        "The comparison cannot be made without the two pKb values"],
      ans=0,
      why="EK 8.3.A.2 puts the hydronium concentration in the numerator of Ka, so a larger "
          "constant at the same initial concentration means a larger hydronium "
          "concentration and therefore a lower pH."),

 dict(q="Using the table of acids, which one is the strongest?",
      table=_T_ACIDS,
      choices=["HA", "HB", "HD", "All three are equally strong",
               "The strongest cannot be identified from these data"],
      ans=0,
      why="EK 8.3.A.2 makes Ka the equilibrium constant for the ionization, so the largest "
          "tabulated constant belongs to the acid that ionizes furthest. The tabulated "
          "pKa values order the same three acids in the opposite direction, since pKa is "
          "the negative logarithm of Ka."),

 dict(q="Using the same table of acids, what is the relationship between the two "
        "tabulated columns?",
      table=_T_ACIDS,
      choices=[
        "Each pKa is the negative base-ten logarithm of the Ka on the same row",
        "Each pKa is the reciprocal of the Ka on the same row",
        "Each pKa is fourteen minus the Ka on the same row",
        "Each pKa is the natural logarithm of the Ka on the same row",
        "The two columns are unrelated and must be measured separately"],
      ans=0,
      why="EK 8.3.A.2 gives the equation pKa equal to the negative logarithm of Ka, and "
          "each tabulated pair satisfies it: a constant of ten to the negative third goes "
          "with a pKa of three."),

 dict(q="Using the same table of acids, which acid gives the highest pH when prepared at "
        "1.0 M?",
      table=_T_ACIDS,
      choices=["HD", "HA", "HB", "All three give the same pH",
               "The answer depends on the volume prepared"],
      ans=0,
      why="At a fixed initial concentration the hydronium concentration rises with the "
          "constant, so the smallest tabulated constant gives the least hydronium and the "
          "highest pH. EK 8.3.A.2 makes the pH determinable from the initial concentration "
          "and the constant alone."),

 dict(q="What does the course framework say happens when a weak base is dissolved in "
        "water?",
      choices=[
        "It reacts with water to produce hydroxide ions, but only a small percentage of "
        "its molecules ionize",
        "It reacts with water to produce hydronium ions, and all of its molecules ionize",
        "It dissociates completely to produce hydroxide ions",
        "It produces hydroxide ions equal in concentration to the initial concentration "
        "of the base",
        "It does not react with water at all unless an acid is present"],
      ans=0,
      why="EK 8.3.A.3 states that weak bases react with water to produce hydroxide ions "
          "but that ordinarily just a small percentage of the molecules ionize, so the "
          "hydroxide concentration does not equal the initial concentration of the base."),

 dict(q="Which expression is the base ionization constant for the weak base B?",
      choices=[
        "\\( K_b = \\frac{[\\mathrm{OH^-}][\\mathrm{HB^+}]}{[\\mathrm{B}]} \\)",
        "\\( K_b = \\frac{[\\mathrm{B}]}{[\\mathrm{OH^-}][\\mathrm{HB^+}]} \\)",
        "\\( K_b = \\frac{[\\mathrm{H_3O^+}][\\mathrm{HB^+}]}{[\\mathrm{B}]} \\)",
        "\\( K_b = [\\mathrm{OH^-}][\\mathrm{HB^+}][\\mathrm{B}] \\)",
        "\\( K_b = \\frac{[\\mathrm{HB^+}]}{[\\mathrm{OH^-}][\\mathrm{B}]} \\)"],
      ans=0,
      why="EK 8.3.A.4 gives the equation with the hydroxide ion and the conjugate acid in "
          "the numerator and the un-ionized base in the denominator. Hydronium belongs to "
          "the acid ionization constant of EK 8.3.A.2."),

 dict(q="A 0.10 M solution of a weak base has a base ionization constant of \\( 1.0 "
        "\\times 10^{-5} \\). What is the pH of the solution at 25 degrees Celsius?",
      choices=["pH = 11.00", "pH = 3.00", "pH = 5.00", "pH = 9.00", "pH = 10.50"],
      ans=0,
      why="The hydroxide concentration is the square root of the constant times the "
          "initial concentration, which is 0.0010 M, giving a pOH of three. EK 8.1.A.3 "
          "then makes the pH the remainder of fourteen. The value 3.00 is the pOH, not "
          "the pH."),

 dict(q="A weak base prepared at an initial concentration of 0.10 M has a base "
        "ionization constant of \\( 1.0 \\times 10^{-6} \\). What is its pOH?",
      choices=["pOH = 3.50", "pOH = 3.00", "pOH = 6.00", "pOH = 10.50", "pOH = 7.00"],
      ans=0,
      why="The hydroxide concentration is the square root of the product of the constant "
          "and the initial concentration, which is ten to the negative three and a half. "
          "EK 8.3.A.3's small percentage is what allows the initial concentration to be "
          "used unchanged in that product."),

 dict(q="For a conjugate acid-base pair, what relationship does the framework give between "
        "Ka and Kb?",
      choices=[
        "Their product is Kw",
        "Their sum is Kw",
        "Their ratio is Kw",
        "Their product is one",
        "They are equal to one another"],
      ans=0,
      why="EK 8.3.A.6 gives the equation Kw equal to Ka times Kb for any conjugate "
          "acid-base pair, together with its logarithmic form, pKw equal to pKa plus pKb."),

 dict(q="A weak acid has a pKa of 5.00. What is the pKb of its conjugate base at 25 "
        "degrees Celsius?",
      choices=["pKb = 9.00", "pKb = 5.00", "pKb = 14.00", "pKb = 19.00", "pKb = 7.00"],
      ans=0,
      why="EK 8.3.A.6 gives pKw equal to pKa plus pKb, and EK 8.1.A.3 makes pKw fourteen "
          "at 25 degrees Celsius, so the pKb is fourteen minus five."),

 dict(q="A weak acid has an ionization constant of \\( 1.0 \\times 10^{-4} \\). What is "
        "the base ionization constant of its conjugate base at 25 degrees Celsius?",
      choices=["\\( 1.0 \\times 10^{-10} \\)", "\\( 1.0 \\times 10^{-4} \\)",
               "\\( 1.0 \\times 10^{-14} \\)", "\\( 1.0 \\times 10^{-18} \\)",
               "\\( 1.0 \\times 10^{-7} \\)"],
      ans=0,
      why="EK 8.3.A.6 makes the product of the two constants equal to Kw, so dividing Kw "
          "by the acid constant gives the base constant. Subtracting the exponents rather "
          "than dividing is the error the equation prevents."),

 dict(q="Using the table of bases, which one produces the highest pH when prepared at "
        "0.10 M?",
      table=_T_BASES,
      choices=["B1", "B2", "B3", "All three give the same pH",
               "The comparison requires the three pKa values"],
      ans=0,
      why="EK 8.3.A.4 makes Kb the equilibrium constant for the reaction with water, so "
          "the largest tabulated constant produces the most hydroxide at a fixed initial "
          "concentration, which is the lowest pOH and the highest pH."),

 dict(q="Using the same table of bases, what is the pKa of the conjugate acid of B2 at 25 "
        "degrees Celsius?",
      table=_T_BASES,
      choices=["pKa = 5.00", "pKa = 9.00", "pKa = 14.00", "pKa = 4.00", "pKa = 23.00"],
      ans=0,
      why="EK 8.3.A.6 gives pKw equal to pKa plus pKb, so subtracting the tabulated pKb "
          "from fourteen gives the pKa of the conjugate acid at 25 degrees Celsius."),

 dict(q="The table lists three weak acid solutions with their initial concentrations and "
        "the hydronium concentrations reached at equilibrium. Which solution has the "
        "largest percent ionization?",
      table=_T_IONIZATION,
      choices=["Solution 3", "Solution 1", "Solution 2",
               "Solutions 1 and 2 are tied", "All three are equal"],
      ans=0,
      why="EK 8.3.A.5 allows percent ionization to be calculated from the initial "
          "concentration and the equilibrium concentration of a species. Dividing each "
          "tabulated hydronium concentration by its own initial concentration gives the "
          "fraction ionized, and one solution's ratio is ten times the others'."),

 dict(q="Using the same table of solutions, what is the percent ionization of solution 2?",
      table=_T_IONIZATION,
      choices=["1.0 percent", "2.0 percent", "0.50 percent", "5.0 percent",
               "20 percent"],
      ans=0,
      why="EK 8.3.A.5 makes the percent ionization the equilibrium hydronium concentration "
          "divided by the initial acid concentration, expressed as a percentage. The two "
          "tabulated values for that solution are in the ratio of one to a hundred."),

 dict(q="Using the same table of solutions, what is the pH of solution 1?",
      table=_T_IONIZATION,
      choices=["pH = 3.00", "pH = 1.00", "pH = 2.00", "pH = 11.00", "pH = 4.00"],
      ans=0,
      why="The tabulated equilibrium hydronium concentration is what pH is defined from "
          "under EK 8.1.A.1, so no constant is needed here: the negative logarithm of the "
          "tabulated value is the answer."),

 dict(q="A weak acid solution is diluted. What does the framework's relationship predict "
        "about the percent ionization?",
      choices=[
        "It rises, because the percent ionized depends on the initial concentration as "
        "well as on the constant",
        "It falls, because there is less acid present to ionize",
        "It is unchanged, because the ionization constant is unchanged",
        "It rises to one hundred percent, because dilution completes the ionization",
        "It cannot be predicted, since percent ionization is measured rather than "
        "calculated"],
      ans=0,
      why="EK 8.3.A.5 makes the percent ionization a function of the constant AND the "
          "initial concentration, not of the constant alone. The hydronium concentration "
          "falls only as the square root of the dilution while the initial concentration "
          "falls in full, so the ratio between them rises."),

 dict(q="Why is the hydronium concentration in a weak acid solution not equal to the "
        "initial concentration of the acid, as it would be for a strong acid?",
      choices=[
        "Because only a small percentage of the weak acid molecules ionize, so most stay "
        "un-ionized",
        "Because a weak acid produces hydroxide ion rather than hydronium ion",
        "Because a weak acid ionizes completely but the hydronium is then consumed by "
        "water",
        "Because the ionization constant of a weak acid is larger than one",
        "Because the initial concentration of a weak acid cannot be measured"],
      ans=0,
      why="EK 8.3.A.1 draws exactly this contrast: the concentration of hydronium is much "
          "less than the initial concentration of the molecular acid because only a small "
          "percentage ionizes. EK 8.2.A.1 makes the two equal for a strong acid, where "
          "ionization is complete."),

 dict(q="A 0.20 M solution of a weak acid is found to have a hydronium ion concentration "
        "of 0.0020 M at equilibrium. What is the concentration of the un-ionized acid at "
        "equilibrium?",
      choices=["0.198 M", "0.20 M", "0.0020 M", "0.202 M", "0.10 M"],
      ans=0,
      why="Each molecule that ionizes removes one from the un-ionized pool and adds one "
          "hydronium ion, so the un-ionized concentration is the initial value less the "
          "hydronium concentration. EK 8.3.A.1's small percentage is why the answer is so "
          "close to the initial value."),

 dict(q="Which pair of quantities does EK 8.3.A.2 say determines the pH of a weak acid "
        "solution?",
      choices=[
        "The initial acid concentration and the pKa",
        "The initial acid concentration and the pKb of the acid",
        "The equilibrium hydroxide concentration and Kw alone",
        "The volume of the solution and the mass of acid dissolved",
        "The pKa alone, whatever the concentration"],
      ans=0,
      why="EK 8.3.A.2 states that the pH of a weak acid solution can be determined from "
          "the initial acid concentration and the pKa. Neither quantity alone is enough, "
          "which is why two acids of the same pKa at different concentrations have "
          "different pH values."),

 dict(q="A weak base solution has a pOH of 3.00 at 25 degrees Celsius. What is the "
        "hydroxide ion concentration, and how does it compare with the initial "
        "concentration of the base?",
      choices=[
        "0.0010 M, which is much smaller than the initial concentration of the base",
        "0.0010 M, which equals the initial concentration of the base",
        "0.0010 M, which is much larger than the initial concentration of the base",
        "3.0 M, which equals the initial concentration of the base",
        "0.0010 M, which is exactly half the initial concentration of the base"],
      ans=0,
      why="EK 8.1.A.1 turns the pOH into the hydroxide concentration, and EK 8.3.A.3 "
          "states that the hydroxide concentration in a weak base solution does NOT equal "
          "the initial concentration of the base, because only a small percentage of "
          "molecules ionize."),

 dict(q="A weak acid and its conjugate base are described at 25 degrees Celsius. If the "
        "acid becomes weaker, what happens to the base ionization constant of its "
        "conjugate?",
      choices=[
        "It becomes larger, because the product of the two constants is fixed at Kw",
        "It becomes smaller, because a weaker acid has a weaker conjugate base",
        "It is unchanged, because the two constants are independent of one another",
        "It becomes larger, because the sum of the two constants is fixed at Kw",
        "It becomes smaller, because both constants fall together as the temperature "
        "changes"],
      ans=0,
      why="EK 8.3.A.6 fixes the PRODUCT of Ka and Kb at Kw for a conjugate pair, so a "
          "smaller Ka forces a larger Kb at a given temperature. The relationship is a "
          "product, not a sum."),

 dict(q="A 1.0 M solution of a weak acid has an ionization constant of \\( 1.0 \\times "
        "10^{-8} \\). What is the pH?",
      choices=["pH = 4.00", "pH = 8.00", "pH = 3.00", "pH = 10.00", "pH = 4.50"],
      ans=0,
      why="The hydronium concentration is the square root of the constant times the "
          "initial concentration, which is the square root of ten to the negative eighth, "
          "or ten to the negative fourth. EK 8.3.A.2 makes this determinable from the "
          "initial concentration and the constant alone."),

]
