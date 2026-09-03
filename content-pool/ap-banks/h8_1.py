# AP CHEMISTRY 8.1 Introduction to Acids and Bases
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.1.A: calculate the values of pH and pOH, based on Kw and the
# concentration of all species present in a neutral solution of water. Suggested skill
# 5.B, identify an appropriate theory, definition, or mathematical relationship to solve a
# problem.
#
# Essential knowledge relied on, in the framework's own words:
#   8.1.A.1  The concentrations of hydronium ion and hydroxide ion are often reported as
#            pH and pOH, respectively.  EQN: pH = -log[H3O+]   EQN: pOH = -log[OH-]
#            The terms "hydrogen ion" and "hydronium ion" and the symbols H+(aq) and
#            H3O+(aq) are often used interchangeably; H3O+(aq) is preferred, but H+(aq) is
#            also accepted on the AP Exam.
#   8.1.A.2  Water autoionizes with an equilibrium constant Kw.
#            EQN: Kw = [H3O+][OH-] = 1.0 x 10^-14 at 25 degrees Celsius.
#   8.1.A.3  In pure water, pH = pOH is called a neutral solution. At 25 degrees Celsius,
#            pKw = 14.0 and thus pH = pOH = 7.0.  EQN: pKw = 14 = pH + pOH at 25 degrees.
#   8.1.A.4  The value of Kw is temperature dependent, so the pH of pure, neutral water
#            will deviate from 7.0 at temperatures other than 25 degrees Celsius.
#
# SCOPE. 8.2 owns pH from the concentration of a STRONG acid or base; 8.3 owns weak acid
# and base equilibria. Every item below is the water autoionization constant, the
# definitions of pH and pOH, or the neutral condition -- nothing here dissolves a solute
# other than to state its ion concentration directly.
#
# THE STATEMENT MOST OFTEN GOT WRONG, and item 12 and items 20 to 24 are built on it:
# EK 8.1.A.3 defines neutral as pH EQUAL TO pOH, not as pH equal to 7.0. The value 7.0 is
# stated only for 25 degrees Celsius, and EK 8.1.A.4 says the neutral pH deviates from it
# at other temperatures. A bank that treated 7.0 as the definition would teach the error
# the framework spends a whole statement excluding.
#
# ARITHMETIC. Every logarithm below is exact: the concentrations are powers of ten, and
# the two temperature-dependent items use values of Kw whose square root is also an exact
# power of ten. Each is recomputed in verify_h8_1.py from the stated value alone.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span is
# hand-written and every function name inside one is escaped.
TOPIC = ("8.1", "Introduction to Acids and Bases", 8)

_T_SOLUTIONS = dict(
    headers=["Solution", "Hydronium ion concentration (M)"],
    rows=[["1", "\\( 1.0 \\times 10^{-3} \\)"],
          ["2", "\\( 1.0 \\times 10^{-7} \\)"],
          ["3", "\\( 1.0 \\times 10^{-11} \\)"]])

_T_KW = dict(
    headers=["Temperature in degrees Celsius", "Value of Kw"],
    rows=[["10", "\\( 2.9 \\times 10^{-15} \\)"],
          ["25", "\\( 1.0 \\times 10^{-14} \\)"],
          ["60", "\\( 9.6 \\times 10^{-14} \\)"]])

_T_PAIRS = dict(
    headers=["Sample", "pH", "pOH"],
    rows=[["W", "3.00", "11.00"],
          ["X", "7.00", "7.00"],
          ["Y", "9.00", "5.00"]])

QUESTIONS = [

 dict(q="Which equation defines pH, according to the course framework?",
      choices=["\\( \\mathrm{pH} = -\\log[\\mathrm{H_3O^+}] \\)",
               "\\( \\mathrm{pH} = \\log[\\mathrm{H_3O^+}] \\)",
               "\\( \\mathrm{pH} = -\\log[\\mathrm{OH^-}] \\)",
               "\\( \\mathrm{pH} = \\frac{1}{[\\mathrm{H_3O^+}]} \\)",
               "\\( \\mathrm{pH} = -\\ln[\\mathrm{H_3O^+}] \\)"],
      ans=0,
      why="EK 8.1.A.1 gives the equation as the negative base-ten logarithm of the "
          "hydronium ion concentration. The negative logarithm of the HYDROXIDE "
          "concentration is pOH, and a natural logarithm is not what the framework's "
          "equation uses."),

 dict(q="A solution has a hydronium ion concentration of \\( 1.0 \\times 10^{-4} \\) M. "
        "What is its pH?",
      choices=["pH = 4.00", "pH = 10.00", "pH = 0.40", "pH = 14.00", "pH = 4.40"],
      ans=0,
      why="EK 8.1.A.1 defines pH as the negative base-ten logarithm of the hydronium ion "
          "concentration, and the logarithm of ten to the negative fourth is exactly "
          "negative four. The value 10.00 is the pOH of the same solution at 25 degrees "
          "Celsius."),

 dict(q="A solution at 25 degrees Celsius has a hydroxide ion concentration of \\( 1.0 "
        "\\times 10^{-2} \\) M. What is its pOH?",
      choices=["pOH = 2.00", "pOH = 12.00", "pOH = 0.20", "pOH = 7.00", "pOH = 14.00"],
      ans=0,
      why="EK 8.1.A.1 defines pOH as the negative base-ten logarithm of the hydroxide ion "
          "concentration, so a concentration of ten to the negative second gives a pOH of "
          "two. The value 12.00 is the pH of that same solution."),

 dict(q="What is the equilibrium constant for the autoionization of water at 25 degrees "
        "Celsius, and what does it equal?",
      choices=[
        "Kw, equal to the product of the hydronium and hydroxide concentrations, which is "
        "\\( 1.0 \\times 10^{-14} \\)",
        "Kw, equal to the sum of the hydronium and hydroxide concentrations, which is "
        "\\( 1.0 \\times 10^{-14} \\)",
        "Ka, equal to the ratio of the hydronium to the hydroxide concentration, which "
        "is 1.0",
        "Kw, equal to the product of pH and pOH, which is 49",
        "Kb, equal to the hydroxide concentration alone, which is \\( 1.0 \\times "
        "10^{-7} \\)"],
      ans=0,
      why="EK 8.1.A.2 states that water autoionizes with an equilibrium constant Kw, given "
          "as the PRODUCT of the hydronium and hydroxide concentrations and equal to one "
          "times ten to the negative fourteenth at 25 degrees Celsius."),

 dict(q="At 25 degrees Celsius, what is the relationship between pH and pOH for any "
        "aqueous solution?",
      choices=["Their sum is 14", "Their difference is 14", "Their product is 14",
               "Their ratio is 14", "Their sum is 7"],
      ans=0,
      why="EK 8.1.A.3 gives the equation pKw equal to 14 equal to pH plus pOH at 25 "
          "degrees Celsius. The value 7.0 is what each of them equals in pure water at "
          "that temperature, not what they sum to."),

 dict(q="A solution at 25 degrees Celsius has a pH of 5.00. What is its pOH?",
      choices=["pOH = 9.00", "pOH = 5.00", "pOH = 14.00", "pOH = 2.00", "pOH = 7.00"],
      ans=0,
      why="EK 8.1.A.3 makes the sum of pH and pOH equal to 14 at 25 degrees Celsius, so "
          "subtracting five from fourteen gives nine. Equal values would describe a "
          "neutral solution, which this is not."),

 dict(q="Using the table, what is the pH of solution 3?",
      table=_T_SOLUTIONS,
      choices=["pH = 11.00", "pH = 3.00", "pH = 7.00", "pH = 1.10", "pH = 14.00"],
      ans=0,
      why="EK 8.1.A.1 defines pH as the negative base-ten logarithm of the tabulated "
          "hydronium ion concentration, and the exponent on that concentration is "
          "negative eleven."),

 dict(q="Using the same table, which solution is neutral at 25 degrees Celsius?",
      table=_T_SOLUTIONS,
      choices=["Solution 2", "Solution 1", "Solution 3",
               "Both solutions 1 and 3", "None of the three"],
      ans=0,
      why="EK 8.1.A.3 makes pure water at 25 degrees Celsius have pH and pOH both equal "
          "to 7.0, which corresponds to a hydronium concentration of ten to the negative "
          "seventh. Exactly one tabulated concentration matches that."),

 dict(q="Using the same table, what is the hydroxide ion concentration of solution 1 at "
        "25 degrees Celsius?",
      table=_T_SOLUTIONS,
      choices=["\\( 1.0 \\times 10^{-11} \\) M", "\\( 1.0 \\times 10^{-3} \\) M",
               "\\( 1.0 \\times 10^{-7} \\) M", "\\( 1.0 \\times 10^{-14} \\) M",
               "\\( 1.0 \\times 10^{-17} \\) M"],
      ans=0,
      why="EK 8.1.A.2 makes the product of the two concentrations equal to one times ten "
          "to the negative fourteenth at 25 degrees Celsius, so dividing that constant by "
          "the tabulated hydronium concentration gives the hydroxide concentration."),

 dict(q="According to the course framework, which symbols and names may be used "
        "interchangeably for the aqueous ion of hydrogen?",
      choices=[
        "Hydrogen ion and hydronium ion, written as H+(aq) or H3O+(aq)",
        "Hydrogen ion and hydride ion, written as H+(aq) or H-(aq)",
        "Hydronium ion and hydroxide ion, written as H3O+(aq) or OH-(aq)",
        "Hydrogen atom and hydronium ion, written as H(g) or H3O+(aq)",
        "Only H3O+(aq) may be used, since no other symbol is accepted"],
      ans=0,
      why="EK 8.1.A.1 states that the terms hydrogen ion and hydronium ion, and the "
          "symbols H+(aq) and H3O+(aq), are often used interchangeably, with the "
          "hydronium form preferred but the other also accepted on the AP Exam. Hydroxide "
          "and hydride are different species."),

 dict(q="Which change does the course framework attribute to a change in temperature for "
        "pure water?",
      choices=[
        "The value of Kw changes, so the pH of pure neutral water deviates from 7.0",
        "The value of Kw is fixed, so the pH of pure water is 7.0 at every temperature",
        "The definition of pH changes, so the logarithm is taken to a different base",
        "The pH of pure water changes but its pOH does not, so the two are no longer "
        "equal",
        "Water stops autoionizing altogether above 25 degrees Celsius"],
      ans=0,
      why="EK 8.1.A.4 states that the value of Kw is temperature dependent, so the pH of "
          "pure, neutral water will deviate from 7.0 at temperatures other than 25 "
          "degrees Celsius. The definition of pH is unchanged, and pure water remains "
          "neutral, with pH equal to pOH."),

 dict(q="What does the course framework use as the DEFINITION of a neutral solution?",
      choices=[
        "A solution in which pH equals pOH",
        "A solution whose pH is exactly 7.0 at any temperature",
        "A solution in which no hydronium ion is present",
        "A solution in which Kw is exactly \\( 1.0 \\times 10^{-14} \\)",
        "A solution whose pH and pOH sum to 14 at any temperature"],
      ans=0,
      why="EK 8.1.A.3 says that in pure water, pH equal to pOH is called a neutral "
          "solution, and only then adds that at 25 degrees Celsius this makes both equal "
          "to 7.0. EK 8.1.A.4 makes the numerical value temperature dependent, so the "
          "equality rather than the number is the definition."),

 dict(q="Water autoionizes. Which equation represents that process?",
      choices=[
        "2 H2O(l) to H3O+(aq) + OH-(aq)",
        "H2O(l) to H2(g) + O2(g)",
        "H2O(l) + H3O+(aq) to 2 H2O(l) + H+(aq)",
        "H2O(l) to H+(aq) + OH-(aq) + e-",
        "2 H2O(l) to H2O2(aq) + H2(g)"],
      ans=0,
      why="EK 8.1.A.2 defines Kw as the product of the hydronium and hydroxide "
          "concentrations, which are the two species the autoionization produces: one "
          "water molecule transfers a proton to another. Decomposition into the elements "
          "and formation of peroxide are different processes entirely."),

 dict(q="A solution at 25 degrees Celsius has a pOH of 3.00. What is its hydroxide ion "
        "concentration?",
      choices=["\\( 1.0 \\times 10^{-3} \\) M", "\\( 1.0 \\times 10^{-11} \\) M",
               "\\( 3.0 \\times 10^{-1} \\) M", "\\( 1.0 \\times 10^{-7} \\) M",
               "\\( 1.0 \\times 10^{-14} \\) M"],
      ans=0,
      why="EK 8.1.A.1 makes pOH the negative base-ten logarithm of the hydroxide "
          "concentration, so a pOH of three corresponds to a concentration of ten to the "
          "negative third. The value ten to the negative eleventh is the hydronium "
          "concentration of that same solution."),

 dict(q="Using the table of samples, which one is neutral at 25 degrees Celsius?",
      table=_T_PAIRS,
      choices=["Sample X", "Sample W", "Sample Y", "Samples W and Y",
               "None of the three"],
      ans=0,
      why="EK 8.1.A.3 defines a neutral solution as one in which pH equals pOH, and "
          "exactly one tabulated sample has the two equal. The other two samples still "
          "have pH and pOH summing to 14, which every aqueous solution does at this "
          "temperature."),

 dict(q="Using the same table of samples, what do all three have in common?",
      table=_T_PAIRS,
      choices=[
        "The sum of pH and pOH is 14 for each of them",
        "The difference between pH and pOH is 14 for each of them",
        "Each has a pH greater than its pOH",
        "Each has a hydronium concentration of \\( 1.0 \\times 10^{-7} \\) M",
        "Each is neutral, since all three are aqueous"],
      ans=0,
      why="EK 8.1.A.3 gives pKw equal to 14 equal to pH plus pOH at 25 degrees Celsius, "
          "and the tabulated pairs each sum to that value. Only one of the three has pH "
          "equal to pOH, so they are not all neutral."),

 dict(q="Which statement about the two ion concentrations in any aqueous solution at 25 "
        "degrees Celsius is correct?",
      choices=[
        "Their product is fixed, so raising one lowers the other",
        "Their sum is fixed, so raising one lowers the other",
        "They are always equal, whatever solute is present",
        "They are unrelated, since they come from different sources",
        "Their product is fixed only in pure water"],
      ans=0,
      why="EK 8.1.A.2 gives Kw as the PRODUCT of the two concentrations and states its "
          "value at 25 degrees Celsius. An equilibrium constant applies to every aqueous "
          "solution at that temperature, not only to pure water, so the two "
          "concentrations move in opposite directions."),

 dict(q="A solution has a hydronium ion concentration of \\( 1.0 \\times 10^{-9} \\) M at "
        "25 degrees Celsius. Which description is correct?",
      choices=[
        "Its pH is 9.00, and its pOH is 5.00, so it is basic",
        "Its pH is 9.00, and its pOH is 9.00, so it is neutral",
        "Its pH is 5.00, and its pOH is 9.00, so it is acidic",
        "Its pH is 9.00, and its pOH is 14.00, so it is basic",
        "Its pH is 0.90, and its pOH is 13.10, so it is acidic"],
      ans=0,
      why="EK 8.1.A.1 gives the pH as nine from the exponent, and EK 8.1.A.3 makes the "
          "pOH the remainder of fourteen, which is five. A pH above the neutral value of "
          "7.0 at this temperature is basic."),

 dict(q="The table lists Kw at three temperatures. What does the trend show?",
      table=_T_KW,
      choices=[
        "Kw increases as the temperature rises",
        "Kw decreases as the temperature rises",
        "Kw is the same at every tabulated temperature",
        "Kw increases and then decreases as the temperature rises",
        "Kw is defined only at 25 degrees Celsius"],
      ans=0,
      why="EK 8.1.A.4 states that the value of Kw is temperature dependent, and the "
          "tabulated values rise with each rise in temperature. The framework fixes the "
          "value of one times ten to the negative fourteenth at 25 degrees Celsius only."),

 dict(q="Using the same table, what happens to the pH of PURE water as the temperature "
        "rises from 10 degrees Celsius to 60 degrees Celsius?",
      table=_T_KW,
      choices=[
        "It falls, because Kw rises and so both ion concentrations rise",
        "It rises, because Kw rises and so the solution becomes more basic",
        "It stays at 7.0, because pure water is neutral at every temperature",
        "It falls, because pure water becomes acidic as it is heated",
        "It cannot be determined without the hydroxide concentration"],
      ans=0,
      why="In pure water the two ion concentrations are equal, so each is the square root "
          "of Kw. The tabulated Kw rises with temperature, so the hydronium concentration "
          "rises and the pH, its negative logarithm, falls. EK 8.1.A.4 is exactly this "
          "deviation from 7.0; the water stays neutral because pH still equals pOH."),

 dict(q="At a certain temperature Kw is \\( 1.0 \\times 10^{-12} \\). What is the pH of "
        "pure water at that temperature?",
      choices=["pH = 6.00", "pH = 7.00", "pH = 12.00", "pH = 5.00", "pH = 6.50"],
      ans=0,
      why="In pure water the two ion concentrations are equal, so each is the square root "
          "of Kw, which is ten to the negative sixth. EK 8.1.A.4 makes exactly this "
          "deviation from 7.0 expected at a temperature other than 25 degrees Celsius."),

 dict(q="At the temperature where Kw is \\( 1.0 \\times 10^{-12} \\), is pure water "
        "acidic, basic or neutral?",
      choices=[
        "Neutral, because pH still equals pOH",
        "Acidic, because its pH is below 7.0",
        "Basic, because its pOH is below 7.0",
        "Acidic, because Kw is larger than it is at 25 degrees Celsius",
        "It cannot be classified at a temperature other than 25 degrees Celsius"],
      ans=0,
      why="EK 8.1.A.3 defines a neutral solution as one in which pH equals pOH, and pure "
          "water satisfies that at every temperature because the autoionization produces "
          "the two ions in equal amounts. The value 7.0 is a consequence of Kw at 25 "
          "degrees Celsius, not the definition."),

 dict(q="At a certain temperature Kw is \\( 1.0 \\times 10^{-13} \\). What is the pH of "
        "pure water at that temperature?",
      choices=["pH = 6.50", "pH = 7.00", "pH = 6.00", "pH = 13.00", "pH = 7.50"],
      ans=0,
      why="Each ion concentration in pure water is the square root of Kw, which is ten to "
          "the negative six and a half. Its negative logarithm is 6.50, the deviation "
          "from 7.0 that EK 8.1.A.4 describes."),

 dict(q="At the temperature where Kw is \\( 1.0 \\times 10^{-13} \\), what is the sum of "
        "pH and pOH for any aqueous solution?",
      choices=["13", "14", "12", "6.50", "7.0"],
      ans=0,
      why="The sum of pH and pOH is pKw, the negative logarithm of Kw, and EK 8.1.A.3 "
          "gives the value 14 specifically for 25 degrees Celsius. Where Kw is ten to the "
          "negative thirteenth, that sum is thirteen instead."),

 dict(q="The hydroxide ion concentration in a solution held at 25 degrees Celsius is "
        "measured as \\( 1.0 \\times 10^{-6} \\) M. What is the pH of that solution?",
      choices=["pH = 8.00", "pH = 6.00", "pH = 7.00", "pH = 14.00", "pH = 2.00"],
      ans=0,
      why="EK 8.1.A.1 makes the pOH six, and EK 8.1.A.3 makes the pH the remainder of "
          "fourteen, which is eight. Taking the negative logarithm of the hydroxide "
          "concentration and calling it the pH gives six, which is the pOH."),

 dict(q="Which quantity does a LOWER value of pH correspond to?",
      choices=[
        "A higher hydronium ion concentration",
        "A lower hydronium ion concentration",
        "A higher hydroxide ion concentration",
        "A lower value of Kw",
        "A higher value of pOH plus pH"],
      ans=0,
      why="EK 8.1.A.1 makes pH the NEGATIVE logarithm of the hydronium concentration, so "
          "the two run in opposite directions. At a fixed temperature EK 8.1.A.2 makes "
          "the hydroxide concentration fall as the hydronium concentration rises."),

 dict(q="Two solutions at 25 degrees Celsius have pH values of 3.00 and 6.00. How do "
        "their hydronium ion concentrations compare?",
      choices=[
        "The first is 1,000 times the second",
        "The first is twice the second",
        "The first is half the second",
        "The first is 3 times the second",
        "The first is 100 times the second"],
      ans=0,
      why="EK 8.1.A.1 makes pH a base-ten logarithm, so a difference of three pH units is "
          "a factor of ten cubed in concentration, and the lower pH is the more "
          "concentrated. A difference in pH is not a difference in concentration."),

 dict(q="Why is the concentration of liquid water itself absent from the expression for "
        "Kw?",
      choices=[
        "Because a pure liquid has a concentration that does not depend on how much is "
        "present",
        "Because water is a product of the autoionization rather than a reactant",
        "Because the concentration of water is exactly 1 M in every aqueous solution",
        "Because water molecules do not participate in the autoionization",
        "Because including it would make Kw larger than one"],
      ans=0,
      why="EK 8.1.A.2 writes Kw as the product of the two ion concentrations alone. An "
          "equilibrium expression omits a pure liquid because its concentration does not "
          "depend on the amount present, and water is a reactant in the autoionization "
          "rather than a product."),

 dict(q="A student reports that a solution has pH 4.00 and pOH 4.00 at 25 degrees "
        "Celsius. What is wrong with the report?",
      choices=[
        "The two values must sum to 14 at that temperature, and these sum to 8",
        "The two values must be equal only in an acidic solution, and these are equal",
        "A pH of 4.00 is impossible in any aqueous solution",
        "A pOH of 4.00 would require a negative hydroxide concentration",
        "Nothing is wrong, since a solution may have any pair of values"],
      ans=0,
      why="EK 8.1.A.3 gives pKw equal to 14 equal to pH plus pOH at 25 degrees Celsius, "
          "which the reported pair violates. Equal values would also mean the solution "
          "was neutral, which a pH of 4.00 at that temperature is not."),

 dict(q="Which pair of quantities does the framework's equation pKw = 14 = pH + pOH hold "
        "for?",
      choices=[
        "Any aqueous solution at 25 degrees Celsius",
        "Pure water only, and at any temperature",
        "Pure water only, and only at 25 degrees Celsius",
        "Any aqueous solution, at any temperature",
        "Acidic solutions only, at 25 degrees Celsius"],
      ans=0,
      why="EK 8.1.A.2 makes Kw the product of the two ion concentrations in aqueous "
          "solution, so its logarithmic form applies wherever water is the solvent. EK "
          "8.1.A.4 restricts the numerical value 14 to 25 degrees Celsius, since Kw is "
          "temperature dependent."),

]
