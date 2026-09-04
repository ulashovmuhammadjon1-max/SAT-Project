# AP CHEMISTRY 8.9 Henderson- Hasselbalch Equation
# CED effective Fall 2024, Unit 8 Acids and Bases. The title in TOPIC below is copied
# verbatim out of CHEMISTRY_topics.json, including the space after the hyphen, because
# export_units.py compares titles exactly.
# Learning objective 8.9.A: identify the pH of a buffer solution based on the identity and
# concentrations of the conjugate acid-base pair used to create the buffer. Suggested skill
# 5.F, calculate, estimate, or predict an unknown quantity from known quantities by
# selecting and following a logical computational pathway and attending to precision.
#
# Essential knowledge relied on, in the framework's own words:
#   8.9.A.1  The pH of the buffer is related to the pKa of the acid and the concentration
#            ratio of the conjugate acid-base pair. This relation is a consequence of the
#            equilibrium expression associated with the dissociation of a weak acid, and is
#            described by the Henderson-Hasselbalch equation. Adding small amounts of acid
#            or base to a buffered solution does not significantly change the ratio of
#            [A-]/[HA] and thus does not significantly change the solution pH. The change
#            in pH on addition of acid or base to a buffered solution is therefore much
#            less than it would have been in the absence of the buffer.
#            EQN: pH = pKa + log([A-]/[HA])
#            Exclusion Statement: Computation of the change in pH resulting from the
#            addition of an acid or a base to a buffer will not be assessed on the AP Exam.
#            Exclusion Statement: Derivation of the Henderson-Hasselbalch equation will not
#            be assessed on the AP Exam.
#
# THE FOUR BUFFER TOPICS. h8_4.py's header records the split agreed before any of them was
# written, and this module is the ARITHMETIC entry: pH from pKa and the ratio, and the
# ratio from pH. 8.4 owns deciding which case a mixture is, 8.8 owns the mechanism and its
# net ionic equations, and 8.10 owns capacity -- including scaling both concentrations at a
# fixed ratio. So no item below writes a net ionic equation or compares two buffers'
# capacity, and verify_h8_9.py asserts that.
#
# THE TWO EXCLUSION STATEMENTS ARE ENFORCED, NOT MERELY QUOTED. Items 7 and 8 state them,
# and verify_h8_9.py additionally asserts that no item computes a NUMERICAL change in pH on
# adding acid or base to a buffer, and that no item asks the student to derive the
# equation. The qualitative statements EK 8.9.A.1 makes about small additions are in scope
# and are used in items 4, 5, 6 and 29; what is excluded is putting a number on them.
#
# ARITHMETIC. Every ratio in this module is a power of ten, so every logarithm is exact and
# every item is answerable without a calculator, which is what the real exam expects.
# verify_h8_9.py recomputes each pH and each ratio from the tabulated or stated values
# alone, through one implementation of the equation written once.
#
# NOTATION. export_units.py does not typeset Chemistry, so every \( ... \) span below is
# hand-written and the function name inside one is escaped as \log.
TOPIC = ("8.9", "Henderson- Hasselbalch Equation", 8)

_T_BUFFERS = dict(
    headers=["Buffer", "pKa of the acid", "[A-] (M)", "[HA] (M)"],
    rows=[["1", "4.00", "0.10", "0.10"],
          ["2", "4.00", "1.00", "0.10"],
          ["3", "4.00", "0.10", "1.00"],
          ["4", "9.00", "0.50", "0.050"]])

_T_RATIOS = dict(
    headers=["Solution", "Measured pH", "pKa of the acid it was made from"],
    rows=[["A", "5.00", "5.00"],
          ["B", "6.00", "5.00"],
          ["C", "3.00", "5.00"]])

QUESTIONS = [

 dict(q="According to the framework, what is the pH of a buffer related to?",
      choices=[
        "The pKa of the acid and the concentration ratio of the conjugate acid-base pair",
        "The pKa of the acid and the total volume of the solution",
        "The concentration of the acid alone",
        "The concentration of the conjugate base alone",
        "The temperature and the identity of the spectator ion"],
      ans=0,
      why="EK 8.9.A.1 opens by stating that the pH of the buffer is related to the pKa of "
          "the acid and the concentration ratio of the conjugate acid-base pair. A ratio is "
          "unchanged by the volume the pair is dissolved in, which is why volume does not "
          "appear."),

 dict(q="Which equation does the framework give for the pH of a buffer?",
      choices=[
        "\\( \\mathrm{pH} = \\mathrm{p}K_a + \\log\\frac{[\\mathrm{A^-}]}{[\\mathrm{HA}]} \\)",
        "\\( \\mathrm{pH} = \\mathrm{p}K_a - \\log\\frac{[\\mathrm{A^-}]}{[\\mathrm{HA}]} \\)",
        "\\( \\mathrm{pH} = \\mathrm{p}K_a + \\log\\frac{[\\mathrm{HA}]}{[\\mathrm{A^-}]} \\)",
        "\\( \\mathrm{pH} = \\mathrm{p}K_a + \\frac{[\\mathrm{A^-}]}{[\\mathrm{HA}]} \\)",
        "\\( \\mathrm{p}K_a = \\mathrm{pH} + \\log\\frac{[\\mathrm{A^-}]}{[\\mathrm{HA}]} \\)"],
      ans=0,
      why="EK 8.9.A.1 gives the Henderson-Hasselbalch equation with the pKa plus the "
          "logarithm of the base-to-acid concentration ratio. Inverting the ratio or "
          "changing the sign of the logarithm would make the pH fall where the framework's "
          "equation has it rise."),

 dict(q="What does the framework say the relation between buffer pH and the pair's ratio "
        "is a consequence of?",
      choices=[
        "The equilibrium expression associated with the dissociation of a weak acid",
        "The autoionization of water",
        "The complete ionization of a strong acid",
        "The conservation of mass in a closed system",
        "The definition of the equivalence point of a titration"],
      ans=0,
      why="EK 8.9.A.1 states that the relation is a consequence of the equilibrium "
          "expression associated with the dissociation of a weak acid, and is described by "
          "the Henderson-Hasselbalch equation. The other principles listed are real but are "
          "not the ones this relation follows from."),

 dict(q="What does the framework say adding a small amount of acid or base does to the "
        "ratio of conjugate base to conjugate acid in a buffer?",
      choices=[
        "It does not change it significantly",
        "It reverses it",
        "It doubles it",
        "It drives it to zero",
        "It makes it equal to one"],
      ans=0,
      why="EK 8.9.A.1 states that adding small amounts of acid or base to a buffered "
          "solution does not significantly change the ratio of the conjugate base to the "
          "conjugate acid. Both members are present in large concentration under EK "
          "8.8.A.1, so a small addition moves the ratio very little."),

 dict(q="And what does the framework say follows for the pH of the buffer?",
      choices=[
        "The pH does not change significantly either",
        "The pH changes in proportion to the amount added",
        "The pH becomes equal to the pKa",
        "The pH becomes neutral",
        "The pH cannot be predicted at all after an addition"],
      ans=0,
      why="EK 8.9.A.1 says the ratio does not significantly change and THUS the solution pH "
          "does not significantly change. The equation makes the pH depend on the ratio, so "
          "a ratio that barely moves gives a pH that barely moves."),

 dict(q="How does the framework compare the pH change on adding acid to a buffered "
        "solution with the change in an unbuffered one?",
      choices=[
        "The change in the buffered solution is much less",
        "The change in the buffered solution is much greater",
        "The two changes are equal in size but opposite in direction",
        "The buffered solution shows no change of any size",
        "The comparison depends on which acid was added"],
      ans=0,
      why="EK 8.9.A.1 states that the change in pH on addition of acid or base to a "
          "buffered solution is much less than it would have been in the absence of the "
          "buffer. Much less is not none, which is why the framework says stabilize rather "
          "than fix."),

 dict(q="Which computation does the framework's first exclusion statement place outside the "
        "AP Exam?",
      choices=[
        "The change in pH resulting from adding an acid or a base to a buffer",
        "The pH of a buffer from the pKa and the ratio of the pair",
        "The ratio of the pair from the pH and the pKa",
        "The pKa of an acid from its ionization constant",
        "The pH of a solution of a strong acid"],
      ans=0,
      why="The first exclusion statement attached to EK 8.9.A.1 names computation of the "
          "change in pH resulting from the addition of an acid or a base to a buffer. The "
          "equation itself, used in either direction on a stated composition, is squarely "
          "in scope."),

 dict(q="Which task does the framework's second exclusion statement place outside the AP "
        "Exam?",
      choices=[
        "Deriving the Henderson-Hasselbalch equation",
        "Using the Henderson-Hasselbalch equation",
        "Recognising the Henderson-Hasselbalch equation",
        "Identifying the pKa that appears in the equation",
        "Identifying which concentration goes in the numerator"],
      ans=0,
      why="The second exclusion statement attached to EK 8.9.A.1 says derivation of the "
          "Henderson-Hasselbalch equation will not be assessed. Using it is the learning "
          "objective of the topic, so it is plainly not excluded."),

 dict(q="The table gives four buffers. What is the pH of buffer 1?",
      table=_T_BUFFERS,
      choices=["4.00", "5.00", "3.00", "7.00", "1.00"],
      ans=0,
      why="EK 8.9.A.1's equation adds the logarithm of the tabulated base-to-acid ratio to "
          "the tabulated pKa. The two tabulated concentrations are equal here, so the "
          "logarithm is zero and the pH is the pKa itself."),

 dict(q="Using the same table of four buffers, what is the pH of buffer 2?",
      table=_T_BUFFERS,
      choices=["5.00", "4.00", "3.00", "1.00", "0.40"],
      ans=0,
      why="The tabulated base concentration is ten times the tabulated acid concentration, "
          "so the logarithm in EK 8.9.A.1's equation is one and the pH sits one unit above "
          "the tabulated pKa. More conjugate base raises the pH, which is the direction the "
          "equation's plus sign gives."),

 dict(q="Using the same table of four buffers, what is the pH of buffer 3?",
      table=_T_BUFFERS,
      choices=["3.00", "4.00", "5.00", "0.10", "6.00"],
      ans=0,
      why="The tabulated acid concentration is ten times the tabulated base concentration, "
          "so the ratio is a tenth, the logarithm is negative one, and the pH sits one unit "
          "BELOW the tabulated pKa. Reading the ratio upside down would move it the wrong "
          "way."),

 dict(q="Using the same table of four buffers, what is the pH of buffer 4?",
      table=_T_BUFFERS,
      choices=["10.00", "9.00", "8.00", "0.55", "11.00"],
      ans=0,
      why="Dividing the tabulated base concentration by the tabulated acid concentration "
          "gives ten, whose logarithm is one, and EK 8.9.A.1's equation adds that to the "
          "tabulated pKa. The concentrations themselves are different from those in the "
          "other buffers, but only their ratio enters."),

 dict(q="Using the same table of four buffers, in which buffer does the pH equal the pKa of "
        "its acid?",
      table=_T_BUFFERS,
      choices=["Buffer 1", "Buffer 2", "Buffer 3", "Buffer 4",
               "In none of them, since a buffer pH never equals a pKa"],
      ans=0,
      why="EK 8.9.A.1's equation makes the pH equal the pKa exactly when the logarithm term "
          "vanishes, which happens when the two tabulated concentrations are equal. Exactly "
          "one tabulated row has that property."),

 dict(q="A buffer is made with equal concentrations of a weak acid and its conjugate base. "
        "The acid has a pKa of 6.00. What is the pH of the buffer?",
      choices=["6.00", "7.00", "5.00", "8.00", "1.00"],
      ans=0,
      why="EK 8.9.A.1's equation adds the logarithm of the ratio to the pKa, and the "
          "logarithm of one is zero, so the pH is the pKa. Nothing here makes the pH "
          "neutral; a buffer's pH is set by the acid it is built from."),

 dict(q="A buffer contains ten times as much conjugate base as conjugate acid, and the acid "
        "has a pKa of 4.50. What is the pH?",
      choices=["5.50", "3.50", "4.50", "0.45", "45.0"],
      ans=0,
      why="The logarithm of ten is one, and EK 8.9.A.1's equation ADDS it to the pKa, so "
          "the pH sits one unit above. Subtracting would describe the case in which the "
          "acid form is in excess instead."),

 dict(q="A buffer contains ten times as much conjugate acid as conjugate base, and the acid "
        "has a pKa of 4.50. What is the pH?",
      choices=["3.50", "5.50", "4.50", "0.45", "44.5"],
      ans=0,
      why="The ratio of base to acid is a tenth, whose logarithm is negative one, so EK "
          "8.9.A.1's equation puts the pH one unit below the pKa. The excess of the acid "
          "form is what makes the solution more acidic than a one-to-one mixture."),

 dict(q="A buffer contains one hundred times as much conjugate base as conjugate acid, and "
        "the acid has a pKa of 3.00. What is the pH?",
      choices=["5.00", "1.00", "3.00", "4.00", "300"],
      ans=0,
      why="The logarithm of one hundred is two, which EK 8.9.A.1's equation adds to the "
          "pKa. Each further factor of ten in the ratio moves the pH by one more unit, "
          "which is what makes the logarithm the right function for the job."),

 dict(q="The table gives the measured pH of three buffer solutions and the pKa of the acid "
        "each was made from. What is the ratio of conjugate base to conjugate acid in "
        "solution B?",
      table=_T_RATIOS,
      choices=["The base is ten times the acid", "The acid is ten times the base",
               "The two are present in equal concentrations",
               "The base is one hundred times the acid",
               "The acid is one hundred times the base"],
      ans=0,
      why="Rearranging EK 8.9.A.1's equation makes the logarithm of the ratio equal to the "
          "tabulated pH minus the tabulated pKa, which is one for this solution, so the "
          "ratio is ten. A pH above the pKa means more of the base form, which is the "
          "direction the equation's plus sign gives."),

 dict(q="Using the same table of three solutions, in which solution are the two members of "
        "the pair present in equal concentrations?",
      table=_T_RATIOS,
      choices=["Solution A", "Solution B", "Solution C",
               "In all three, since all three are buffers",
               "In none of them, since equal concentrations are impossible"],
      ans=0,
      why="EK 8.9.A.1's equation makes the ratio one exactly when the tabulated pH equals "
          "the tabulated pKa, since the logarithm of one is zero. One tabulated row has the "
          "two numbers identical."),

 dict(q="Using the same table of three solutions, what is the ratio of conjugate base to "
        "conjugate acid in solution C?",
      table=_T_RATIOS,
      choices=["The acid is one hundred times the base",
               "The base is one hundred times the acid",
               "The acid is ten times the base", "The base is ten times the acid",
               "The two are present in equal concentrations"],
      ans=0,
      why="The tabulated pH is two units below the tabulated pKa, so the logarithm of the "
          "ratio is negative two and the ratio is one hundredth. A pH below the pKa means "
          "the acid form is in excess, and by a factor the logarithm fixes exactly."),

 dict(q="A buffer has a measured pH of 5.00 and was made from an acid of pKa 5.00. What is "
        "the ratio of conjugate base to conjugate acid?",
      choices=["The two are present in equal concentrations",
               "The base is ten times the acid", "The acid is ten times the base",
               "The base is five times the acid",
               "It cannot be determined from the pH and the pKa alone"],
      ans=0,
      why="EK 8.9.A.1's equation makes the logarithm of the ratio equal to the pH minus the "
          "pKa, which is zero here, and the only ratio whose logarithm is zero is one. The "
          "ratio is fixed by the difference alone, so it certainly can be determined."),

 dict(q="A buffer has a pH exactly one unit above the pKa of the acid it was made from. "
        "What is the ratio of conjugate base to conjugate acid?",
      choices=["The base is ten times the acid", "The acid is ten times the base",
               "The two are present in equal concentrations",
               "The base is twice the acid", "The acid is twice the base"],
      ans=0,
      why="Rearranging EK 8.9.A.1's equation gives the logarithm of the ratio as the pH "
          "minus the pKa, which is one, so the ratio is ten. A difference of one pH unit is "
          "a factor of ten in the ratio, not a factor of two."),

 dict(q="Two buffers are made with the same base-to-acid ratio but from acids of different "
        "pKa. How do their pH values compare?",
      choices=[
        "They differ by the difference between the two pKa values",
        "They are equal, because the ratio is the same",
        "They differ by the logarithm of the ratio",
        "The buffer made from the larger pKa has the lower pH",
        "The comparison requires the concentrations rather than the ratio"],
      ans=0,
      why="EK 8.9.A.1's equation adds the same logarithm term to each pKa when the ratios "
          "agree, so the two pH values are displaced from their own pKa values by the same "
          "amount and differ by whatever the pKa values differ by."),

 dict(q="Two buffers are made from the same acid, one with a base-to-acid ratio of ten and "
        "one with a ratio of one tenth. Which has the higher pH, and by how many units do "
        "they differ?",
      choices=[
        "The one with the larger ratio, by two units",
        "The one with the larger ratio, by one unit",
        "The one with the smaller ratio, by two units",
        "The one with the smaller ratio, by one unit",
        "They have the same pH, since the acid is the same"],
      ans=0,
      why="EK 8.9.A.1's equation puts one buffer one unit above the shared pKa and the "
          "other one unit below it, so the gap is the sum of the two displacements. More of "
          "the base form always means the higher pH, by the plus sign in the equation."),

 dict(q="A buffer's pH is found to be below the pKa of its acid. What does the equation say "
        "about the ratio of the pair?",
      choices=[
        "The ratio of base to acid is less than one",
        "The ratio of base to acid is greater than one",
        "The ratio of base to acid is exactly one",
        "The ratio cannot be related to the pH",
        "The ratio of base to acid is negative"],
      ans=0,
      why="EK 8.9.A.1's equation makes the logarithm of the ratio equal to the pH minus the "
          "pKa, and a negative logarithm belongs to a ratio below one. A ratio of "
          "concentrations is a positive quantity, so it can be small but never negative."),

 dict(q="What has to be true of a buffer for its pH to equal the pKa of its acid exactly?",
      choices=[
        "The two members of the pair are present in equal concentrations",
        "The two members of the pair are present in a ten-to-one ratio",
        "The buffer must be at a pH of 7.00",
        "The acid must be a strong acid",
        "The buffer must be very dilute"],
      ans=0,
      why="EK 8.9.A.1's equation leaves the pH equal to the pKa only when the logarithm "
          "term vanishes, and the logarithm of a ratio is zero only when that ratio is one. "
          "The pKa may be any value, so no particular pH is required."),

 dict(q="A chemist needs a buffer at pH 5.00 and has an acid of pKa 4.00 with its conjugate "
        "base. In what ratio should they be combined?",
      choices=[
        "Ten parts conjugate base to one part acid",
        "One part conjugate base to ten parts acid",
        "Equal parts of the two",
        "One hundred parts conjugate base to one part acid",
        "Five parts conjugate base to four parts acid"],
      ans=0,
      why="EK 8.9.A.1's equation requires the logarithm of the ratio to make up the "
          "difference between the target pH and the pKa, which is one unit, so the ratio "
          "must be ten. Matching the numbers 5 and 4 as a ratio is not what the logarithm "
          "does."),

 dict(q="A chemist needs a buffer at pH 9.00 and intends to use equal concentrations of the "
        "two members. Which acid should be chosen?",
      choices=[
        "One with a pKa of 9.00",
        "One with a pKa of 5.00",
        "One with a pKa of 7.00",
        "One with a pKa of 10.00",
        "Any acid, provided the concentrations are equal"],
      ans=0,
      why="EK 8.9.A.1's equation reduces to pH equals pKa when the two concentrations are "
          "equal, so the target pH fixes the pKa required. The identity of the acid is "
          "exactly what the equation makes it matter."),

 dict(q="Why does adding a small amount of strong acid leave the ratio of the pair almost "
        "unchanged?",
      choices=[
        "Both members are present in large concentration, so a small addition converts only "
        "a small fraction",
        "The added acid does not react with either member",
        "The added acid reacts with both members equally",
        "The added acid is neutralized by the water before it can reach the pair",
        "The ratio is fixed by the pKa and cannot change at all"],
      ans=0,
      why="EK 8.8.A.1 puts a large concentration of both members in a buffer and EK 8.9.A.1 "
          "concludes that small additions do not significantly change the ratio. The added "
          "acid does react, with the conjugate base, which is why the ratio changes at all "
          "rather than not at all."),

 dict(q="Summarise what the Henderson-Hasselbalch equation lets a student calculate.",
      choices=[
        "The pH of a buffer from the pKa and the ratio, or the ratio from the pH and the "
        "pKa",
        "The change in pH when acid is added to a buffer",
        "The capacity of a buffer to absorb added acid",
        "The value of the ionization constant from the concentration of the acid alone",
        "The volume of titrant needed to reach the equivalence point"],
      ans=0,
      why="Learning objective 8.9.A is to identify the pH of a buffer from the identity and "
          "concentrations of the pair, and rearranging EK 8.9.A.1's equation runs the same "
          "relation the other way. The change in pH on addition is named in the topic's own "
          "exclusion statement."),

]
