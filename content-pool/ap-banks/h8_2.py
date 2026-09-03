# AP CHEMISTRY 8.2 pH and pOH of Strong Acids and Bases
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.2.A: calculate pH and pOH based on concentrations of all species in
# a solution of a strong acid or a strong base. Suggested skill 5.B, identify an
# appropriate theory, definition, or mathematical relationship to solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   8.2.A.1  Molecules of a strong acid (e.g., HCl, HBr, HI, HClO4, H2SO4, and HNO3) will
#            completely ionize in aqueous solution to produce hydronium ions and the
#            conjugate base of the acid. As such, the concentration of H3O+ in a strong
#            acid solution is equal to the initial concentration of the strong acid, and
#            thus the pH of the strong acid solution is easily calculated.
#   8.2.A.2  When dissolved in solution, strong bases (e.g., group I and II hydroxides)
#            completely dissociate to produce hydroxide ions. As such, the concentration
#            of OH- in a strong base solution is equal to the initial concentration of a
#            group I hydroxide and DOUBLE the initial concentration of a group II
#            hydroxide, and thus the pOH (and pH) of the strong base solution is easily
#            calculated.
#
# SCOPE. 8.1 owns the definitions of pH and pOH and the autoionization constant; 8.3 owns
# weak acids and bases, where only a small percentage ionizes. Every solute below is one
# the framework names as strong, and the whole point of each item is that complete
# ionization makes the ion concentration READABLE OFF the stated concentration.
#
# THE FACTOR OF TWO. EK 8.2.A.2 states in its own words that the hydroxide concentration is
# DOUBLE the initial concentration for a group II hydroxide, and that asymmetry with group
# I is the single most testable thing in this topic. Items 6, 7, 12, 17, 20, 23, 26 and 29
# turn on it, and verify_h8_2.py recomputes each from the stated formula rather than from a
# remembered rule.
#
# ONE DELIBERATE OMISSION. H2SO4 appears in the framework's list of strong acids, but only
# its FIRST ionization is complete; the second is not, and the framework says nothing about
# how to treat it. So H2SO4 appears here only where a strong acid must be IDENTIFIED, never
# in a calculation. Guessing a factor of two for it is exactly the kind of unstated
# assumption SCIENCE_BRIEF.md says to cut rather than ship.
#
# ARITHMETIC. Every concentration is chosen so the logarithm is exact, including after the
# doubling: 0.0050 M of a group II hydroxide gives 0.010 M hydroxide and a pOH of 2.00.
#
# NOTATION. export_units.py does not typeset Chemistry; every span below is hand-written.
TOPIC = ("8.2", "pH and pOH of Strong Acids and Bases", 8)

_T_ACIDS = dict(
    headers=["Solution", "Solute", "Initial concentration (M)"],
    rows=[["1", "HCl", "0.010"],
          ["2", "HNO3", "0.0010"],
          ["3", "HBr", "0.10"]])

_T_BASES = dict(
    headers=["Solution", "Solute", "Group of the metal",
             "Initial concentration (M)"],
    rows=[["4", "NaOH", "group I", "0.010"],
          ["5", "Ca(OH)2", "group II", "0.0050"],
          ["6", "KOH", "group I", "0.0010"]])

_T_MIXED = dict(
    headers=["Sample", "Solute", "Initial concentration (M)"],
    rows=[["P", "HI", "0.0010"],
          ["Q", "Ba(OH)2", "0.00050"],
          ["R", "LiOH", "0.10"]])

QUESTIONS = [

 dict(q="What does the course framework say happens to molecules of a strong acid in "
        "aqueous solution?",
      choices=[
        "They completely ionize, producing hydronium ions and the conjugate base of the "
        "acid",
        "They partly ionize, so most of the acid remains in molecular form",
        "They completely ionize, producing hydroxide ions and the conjugate acid",
        "They dissolve without ionizing, so the solution stays neutral",
        "They ionize only after the solution has been heated"],
      ans=0,
      why="EK 8.2.A.1 states that molecules of a strong acid will completely ionize in "
          "aqueous solution to produce hydronium ions and the conjugate base of the acid. "
          "Partial ionization is what EK 8.3.A.1 reserves for a WEAK acid."),

 dict(q="A solution is 0.010 M in HCl. What is its pH?",
      choices=["pH = 2.00", "pH = 12.00", "pH = 1.00", "pH = 0.010", "pH = 7.00"],
      ans=0,
      why="EK 8.2.A.1 makes the hydronium concentration equal to the initial concentration "
          "of the strong acid, so it is 0.010 M and the pH is two. The value 12.00 is the "
          "pOH of the same solution at 25 degrees Celsius."),

 dict(q="A solution is 0.0010 M in HNO3. What is its pH?",
      choices=["pH = 3.00", "pH = 11.00", "pH = 2.00", "pH = 0.0010", "pH = 4.00"],
      ans=0,
      why="Complete ionization under EK 8.2.A.1 makes the hydronium concentration 0.0010 "
          "M, so the pH is three. Nitric acid is on the framework's own list of strong "
          "acids, so no equilibrium calculation is needed."),

 dict(q="Why is the pH of a strong acid solution described by the framework as easily "
        "calculated?",
      choices=[
        "Because complete ionization makes the hydronium concentration equal to the "
        "stated concentration of the acid",
        "Because a strong acid always produces a pH of exactly 1.00",
        "Because the ionization constant of a strong acid is exactly one",
        "Because the hydronium concentration of any acid is fixed by Kw alone",
        "Because a strong acid does not affect the hydronium concentration at all"],
      ans=0,
      why="EK 8.2.A.1 says that because ionization is complete, the concentration of "
          "hydronium in a strong acid solution is EQUAL TO the initial concentration of "
          "the strong acid, which is why no equilibrium has to be solved."),

 dict(q="A solution is 0.010 M in NaOH. What is its pOH?",
      choices=["pOH = 2.00", "pOH = 12.00", "pOH = 1.70", "pOH = 7.00", "pOH = 0.010"],
      ans=0,
      why="Sodium is a group I metal, so EK 8.2.A.2 makes the hydroxide concentration "
          "equal to the initial concentration of the hydroxide, which is 0.010 M, giving "
          "a pOH of two. Doubling would be the group II rule and is not applied here."),

 dict(q="A solution is 0.0050 M in Ca(OH)2. What is its hydroxide ion concentration?",
      choices=["0.010 M", "0.0050 M", "0.0025 M", "0.10 M", "0.0010 M"],
      ans=0,
      why="Calcium is a group II metal, and EK 8.2.A.2 states that the hydroxide "
          "concentration is DOUBLE the initial concentration of a group II hydroxide. "
          "Twice 0.0050 M is 0.010 M; taking it as equal to the stated concentration is "
          "the group I rule."),

 dict(q="For that same 0.0050 M solution of Ca(OH)2, what is the pOH?",
      choices=["pOH = 2.00", "pOH = 2.30", "pOH = 12.00", "pOH = 5.00", "pOH = 1.70"],
      ans=0,
      why="EK 8.2.A.2 doubles the stated concentration for a group II hydroxide, giving "
          "0.010 M hydroxide and a pOH of two. Using the undoubled 0.0050 M would give "
          "about 2.30 instead, which is the error the doubling rule exists to prevent."),

 dict(q="Which of the following does the course framework name as an example of a strong "
        "acid?",
      choices=["HClO4", "CH3COOH", "HF", "H2CO3", "NH4+"],
      ans=0,
      why="EK 8.2.A.1 gives the examples HCl, HBr, HI, HClO4, H2SO4 and HNO3. Acetic acid "
          "is named in EK 8.6.A.1 as a carboxylic acid, one common class of WEAK acid, and "
          "the others are weak as well."),

 dict(q="Using the table of acid solutions, which one has the lowest pH?",
      table=_T_ACIDS,
      choices=["Solution 3", "Solution 1", "Solution 2",
               "All three have the same pH", "The pH cannot be found from these data"],
      ans=0,
      why="All three solutes are on the framework's list of strong acids, so EK 8.2.A.1 "
          "makes each hydronium concentration equal to the tabulated concentration. The "
          "largest concentration gives the smallest negative logarithm, which is the "
          "lowest pH."),

 dict(q="Using the same table of acid solutions, what is the pH of solution 2?",
      table=_T_ACIDS,
      choices=["pH = 3.00", "pH = 2.00", "pH = 1.00", "pH = 11.00", "pH = 4.00"],
      ans=0,
      why="EK 8.2.A.1 makes the hydronium concentration equal to the tabulated "
          "concentration of this strong acid, and the negative logarithm of that value is "
          "three."),

 dict(q="Using the same table of acid solutions, what is the hydroxide ion concentration "
        "in solution 1 at 25 degrees Celsius?",
      table=_T_ACIDS,
      choices=["\\( 1.0 \\times 10^{-12} \\) M", "\\( 1.0 \\times 10^{-2} \\) M",
               "\\( 1.0 \\times 10^{-7} \\) M", "\\( 1.0 \\times 10^{-14} \\) M",
               "\\( 1.0 \\times 10^{-11} \\) M"],
      ans=0,
      why="EK 8.2.A.1 gives the hydronium concentration as the tabulated 0.010 M, and the "
          "autoionization constant of EK 8.1.A.2 then fixes the hydroxide concentration as "
          "Kw divided by that value."),

 dict(q="Using the table of base solutions, what is the pOH of solution 5?",
      table=_T_BASES,
      choices=["pOH = 2.00", "pOH = 2.30", "pOH = 3.00", "pOH = 12.00", "pOH = 1.00"],
      ans=0,
      why="The tabulated group tells the rule to use: EK 8.2.A.2 doubles the "
          "concentration for a group II hydroxide, giving 0.010 M hydroxide and a pOH of "
          "two. The tabulated group I entries at the same concentration would not be "
          "doubled."),

 dict(q="Using the same table of base solutions, what is the pH of solution 6 at 25 "
        "degrees Celsius?",
      table=_T_BASES,
      choices=["pH = 11.00", "pH = 3.00", "pH = 10.00", "pH = 12.00", "pH = 14.00"],
      ans=0,
      why="Potassium is a group I metal, so EK 8.2.A.2 makes the hydroxide concentration "
          "the tabulated 0.0010 M and the pOH three. EK 8.1.A.3 then gives the pH as the "
          "remainder of fourteen."),

 dict(q="Using the same table of base solutions, which two solutions have the SAME "
        "hydroxide ion concentration?",
      table=_T_BASES,
      choices=["Solutions 4 and 5", "Solutions 4 and 6", "Solutions 5 and 6",
               "No two of them match", "All three of them match"],
      ans=0,
      why="EK 8.2.A.2 leaves a group I hydroxide's concentration alone and doubles a group "
          "II hydroxide's, so the tabulated 0.010 M group I solution and the tabulated "
          "0.0050 M group II solution both give 0.010 M hydroxide."),

 dict(q="A student calculates the pH of a 0.10 M solution of HBr by solving an "
        "equilibrium expression with an ionization constant. What is wrong with the "
        "approach?",
      choices=[
        "HBr is a strong acid, so ionization is complete and no equilibrium needs to be "
        "solved",
        "HBr is a weak acid, so the ionization constant must be looked up rather than "
        "assumed",
        "HBr produces hydroxide rather than hydronium, so the wrong equation was used",
        "The pH of any acid solution is fixed by Kw and cannot be calculated from "
        "concentration",
        "Nothing is wrong, since every acid requires an equilibrium calculation"],
      ans=0,
      why="EK 8.2.A.1 lists HBr among the strong acids and states that such molecules "
          "COMPLETELY ionize, which is why the hydronium concentration equals the initial "
          "concentration and the pH follows directly."),

 dict(q="What does the course framework say strong bases do when dissolved in solution?",
      choices=[
        "They completely dissociate to produce hydroxide ions",
        "They partly dissociate, so most of the base remains undissociated",
        "They completely dissociate to produce hydronium ions",
        "They react with water to produce a conjugate acid and hydroxide in equilibrium",
        "They dissolve without producing any ions at all"],
      ans=0,
      why="EK 8.2.A.2 states that when dissolved in solution, strong bases such as group I "
          "and II hydroxides completely dissociate to produce hydroxide ions. Partial "
          "reaction with water is what EK 8.3.A.3 reserves for a weak base."),

 dict(q="Two solutions are prepared at the same concentration, one of a group I hydroxide "
        "and one of a group II hydroxide. How do their hydroxide ion concentrations "
        "compare?",
      choices=[
        "The group II solution has twice the hydroxide concentration of the group I "
        "solution",
        "The two have equal hydroxide concentrations, since both dissociate completely",
        "The group I solution has twice the hydroxide concentration of the group II "
        "solution",
        "The group II solution has half the hydroxide concentration of the group I "
        "solution",
        "The comparison depends on which particular metals are involved"],
      ans=0,
      why="EK 8.2.A.2 makes the hydroxide concentration equal to the initial concentration "
          "for a group I hydroxide and DOUBLE the initial concentration for a group II "
          "hydroxide, so at equal stated concentrations the group II solution supplies "
          "twice as much hydroxide."),

 dict(q="A solution is 0.10 M in HI. What is its pH?",
      choices=["pH = 1.00", "pH = 13.00", "pH = 0.10", "pH = 2.00", "pH = 10.00"],
      ans=0,
      why="Hydroiodic acid is on the framework's list of strong acids, so EK 8.2.A.1 makes "
          "the hydronium concentration 0.10 M and the pH one. The value 13.00 is the pOH "
          "of the same solution."),

 dict(q="A 0.10 M solution of a strong acid is diluted with water to ten times its "
        "original volume. What is the pH of the diluted solution?",
      choices=["pH = 2.00", "pH = 1.00", "pH = 0.10", "pH = 10.00", "pH = 12.00"],
      ans=0,
      why="Diluting tenfold lowers the concentration to 0.010 M, and EK 8.2.A.1 keeps the "
          "hydronium concentration equal to that, so the pH rises by exactly one unit to "
          "two. Complete ionization is what makes the new pH readable off the new "
          "concentration."),

 dict(q="A solution is 0.050 M in Sr(OH)2, a group II hydroxide. What is its pOH?",
      choices=["pOH = 1.00", "pOH = 1.30", "pOH = 13.00", "pOH = 2.00", "pOH = 0.70"],
      ans=0,
      why="EK 8.2.A.2 doubles the stated concentration for a group II hydroxide, giving "
          "0.10 M hydroxide and a pOH of one. Using the undoubled value would give about "
          "1.30."),

 dict(q="Which species is present in the largest concentration in a 0.10 M solution of "
        "HCl at 25 degrees Celsius, apart from water itself?",
      choices=[
        "Chloride ion, at the same concentration as the hydronium ion",
        "Undissociated HCl molecules, since most of the acid stays molecular",
        "Hydroxide ion, since water autoionizes in every solution",
        "Chloride ion, at twice the concentration of the hydronium ion",
        "Hydronium ion, at twice the concentration of the chloride ion"],
      ans=0,
      why="EK 8.2.A.1 makes ionization complete and produces hydronium ion together with "
          "the conjugate base, one of each per molecule, so the two are present in equal "
          "amounts and essentially no molecular acid remains. Hydroxide is present only at "
          "the tiny level Kw allows."),

 dict(q="Using the table of mixed samples, what is the pH of sample P at 25 degrees "
        "Celsius?",
      table=_T_MIXED,
      choices=["pH = 3.00", "pH = 11.00", "pH = 4.00", "pH = 2.00", "pH = 10.00"],
      ans=0,
      why="The tabulated solute is on the framework's list of strong acids, so EK 8.2.A.1 "
          "makes the hydronium concentration equal to the tabulated value and the pH its "
          "negative logarithm."),

 dict(q="Using the same table of mixed samples, what is the pOH of sample Q?",
      table=_T_MIXED,
      choices=["pOH = 3.00", "pOH = 3.30", "pOH = 11.00", "pOH = 4.00", "pOH = 2.00"],
      ans=0,
      why="Barium is a group II metal, so EK 8.2.A.2 doubles the tabulated concentration "
          "to give 0.0010 M hydroxide and a pOH of three. Using the tabulated value "
          "undoubled would give about 3.30."),

 dict(q="Using the same table of mixed samples, which sample has the highest pH at 25 "
        "degrees Celsius?",
      table=_T_MIXED,
      choices=["Sample R", "Sample P", "Sample Q",
               "Samples Q and R are tied", "All three have the same pH"],
      ans=0,
      why="One tabulated sample is a strong acid and the other two are strong bases, and "
          "of the two bases EK 8.2.A.2 gives the larger hydroxide concentration to the "
          "group I hydroxide at 0.10 M rather than to the group II hydroxide at 0.00050 "
          "M, so that sample has the lowest pOH and the highest pH."),

 dict(q="Why does the framework treat the hydroxide contributed by the autoionization of "
        "water as negligible in a 0.010 M solution of NaOH?",
      choices=[
        "Because the hydroxide from the base is far larger than the amount water supplies "
        "on its own",
        "Because water does not autoionize once a base has been added to it",
        "Because the autoionization constant becomes zero in basic solution",
        "Because sodium ion consumes the hydroxide that water produces",
        "Because the pOH is defined without reference to water at all"],
      ans=0,
      why="EK 8.2.A.2 makes the hydroxide concentration equal to the initial concentration "
          "of the group I hydroxide, which is 0.010 M here, while EK 8.1.A.2 leaves water "
          "supplying hydroxide near the ten to the negative seventh level. The larger term "
          "dominates the sum."),

 dict(q="A 0.00050 M solution of a group II hydroxide and a solution of a group I "
        "hydroxide have the same pOH. What is the concentration of the group I hydroxide "
        "solution?",
      choices=["0.0010 M", "0.00050 M", "0.00025 M", "0.010 M", "0.0020 M"],
      ans=0,
      why="EK 8.2.A.2 doubles the group II concentration, giving 0.0010 M hydroxide, and "
          "leaves the group I concentration alone, so the group I solution must itself be "
          "0.0010 M to match. Equal pOH means equal hydroxide concentration, not equal "
          "solute concentration."),

 dict(q="Which of the following is NOT on the framework's list of examples of strong "
        "acids?",
      choices=["HF", "HCl", "HBr", "HI", "HNO3"],
      ans=0,
      why="EK 8.2.A.1 lists HCl, HBr, HI, HClO4, H2SO4 and HNO3 as examples of strong "
          "acids. Hydrofluoric acid is not among them, and EK 8.6.A.1 places the strength "
          "of an acid in the stability of its conjugate base rather than in the family it "
          "belongs to."),

 dict(q="A solution of a strong acid has a pH of 2.00 at 25 degrees Celsius. What was the "
        "concentration of the acid?",
      choices=["0.010 M", "0.10 M", "0.0010 M", "2.0 M", "0.020 M"],
      ans=0,
      why="EK 8.2.A.1 makes the hydronium concentration equal to the initial concentration "
          "of the strong acid, so raising ten to the negative of the pH recovers that "
          "concentration directly. No equilibrium constant is involved."),

 dict(q="A solution of a group II hydroxide has a pOH of 2.00 at 25 degrees Celsius. What "
        "was the concentration of the hydroxide?",
      choices=["0.0050 M", "0.010 M", "0.020 M", "0.0025 M", "0.10 M"],
      ans=0,
      why="A pOH of two means a hydroxide concentration of 0.010 M, and EK 8.2.A.2 makes "
          "that DOUBLE the initial concentration of a group II hydroxide, so the solute "
          "concentration is half of it. Reporting 0.010 M would apply the group I rule."),

 dict(q="Two solutions at 25 degrees Celsius are prepared, one 0.0010 M in a strong acid "
        "and one 0.0010 M in a group I hydroxide. What is the sum of their pH values?",
      choices=["14.00", "7.00", "3.00", "11.00", "22.00"],
      ans=0,
      why="EK 8.2.A.1 gives the acid a pH of three, and EK 8.2.A.2 gives the base a pOH of "
          "three, which EK 8.1.A.3 turns into a pH of eleven at this temperature. Three "
          "and eleven sum to fourteen."),

]
