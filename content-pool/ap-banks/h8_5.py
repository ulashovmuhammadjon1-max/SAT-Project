# AP CHEMISTRY 8.5 Acid-Base Titrations
# CED effective Fall 2024, Unit 8 Acids and Bases.
# Learning objective 8.5.A: explain results from the titration of a mono- or polyprotic
# acid or base solution, in relation to the properties of the solution and its components.
# Suggested skill 5.D, identify information presented graphically to solve a problem.
#
# Essential knowledge relied on, in the framework's own words:
#   8.5.A.1  An acid-base reaction can be carried out under controlled conditions in a
#            titration. A titration curve, plotting pH against the volume of titrant added,
#            is useful for summarizing results from a titration.
#   8.5.A.2  At the equivalence point for titrations of monoprotic acids or bases, the
#            number of moles of titrant added is equal to the number of moles of analyte
#            originally present. This relationship can be used to obtain the concentration
#            of the analyte. This is the case for titrations of strong acids/bases and weak
#            acids/bases.
#   8.5.A.3  For titrations of weak acids/bases it is useful to consider the point halfway
#            to the equivalence point, the half-equivalence point. At this point there are
#            equal concentrations of each species in the conjugate acid-base pair, for
#            example [HA] = [A-]. Because pH = pKa when the conjugate acid and base have
#            equal concentrations, the pKa can be determined from the pH at the
#            half-equivalence point in a titration.
#   8.5.A.4  At the equivalence point, pH is determined by the major species in solution.
#            Strong acid and strong base titrations result in neutral pH at the equivalence
#            point. However, in titrations of weak acids (weak bases), the conjugate base
#            of the weak acid (conjugate acid of the weak base) is present at the
#            equivalence point and can undergo proton-transfer reactions with the
#            surrounding water, producing basic (acidic) solutions.
#   8.5.A.5  For polyprotic acids, titration curves can be used to determine the number of
#            acidic protons. In doing so, the major species present at any point along the
#            curve can be identified, along with the pKa associated with each proton in a
#            weak polyprotic acid.
#            Exclusion Statement: computation of the concentration of each species present
#            in the titration curve for polyprotic acids will not be assessed. Qualitative
#            reasoning about which species are present in large versus small concentrations
#            at any point in a polyprotic titration IS within scope.
#
# THE FIGURE PROBLEM, and how it is solved. EK 8.5.A.1 makes the titration CURVE the
# characteristic representation of this topic, and this bank cannot show one. Every curve
# below is therefore given as a TABLE of volume of titrant against pH, which is exactly
# what the curve plots and leaves nothing to be read off a picture. No stem says "shown",
# "the curve above" or "the graph". verify_h8_5.py asserts that.
#
# SCOPE. 8.4 owns the mole bookkeeping of a mixture away from any titration; 8.7 owns
# indicators, including EK 8.7.A.3's rule about choosing one whose pKa is close to the
# equivalence pH, and NO item here selects an indicator. The polyprotic items stay
# qualitative, as EK 8.5.A.5's exclusion statement requires.
#
# ARITHMETIC. Every equivalence-point calculation is exact and is recomputed in
# verify_h8_5.py from the stated or tabulated volumes and concentrations alone.
#
# NOTATION. export_units.py does not typeset Chemistry; every span is hand-written.
TOPIC = ("8.5", "Acid-Base Titrations", 8)

_T_WEAK_CURVE = dict(
    headers=["Volume of 0.100 M NaOH added (mL)", "pH of the flask"],
    rows=[["0.00", "2.90"],
          ["5.00", "4.00"],
          ["10.00", "4.75"],
          ["15.00", "5.50"],
          ["20.00", "8.80"],
          ["25.00", "12.00"]])

_T_STRONG_CURVE = dict(
    headers=["Volume of 0.100 M NaOH added (mL)", "pH of the flask"],
    rows=[["0.00", "1.00"],
          ["10.00", "1.37"],
          ["20.00", "3.00"],
          ["25.00", "7.00"],
          ["30.00", "11.00"]])

_T_DIPROTIC = dict(
    headers=["Volume of 0.100 M NaOH added (mL)", "pH of the flask"],
    rows=[["0.00", "1.90"],
          ["10.00", "2.90"],
          ["20.00", "5.00"],
          ["30.00", "7.20"],
          ["40.00", "10.00"],
          ["50.00", "12.00"]])

_T_TRIALS = dict(
    headers=["Trial", "Volume of analyte (mL)", "Concentration of titrant (M)",
             "Volume of titrant at the equivalence point (mL)"],
    rows=[["1", "25.00", "0.100", "20.00"],
          ["2", "50.00", "0.200", "25.00"],
          ["3", "10.00", "0.500", "10.00"]])

QUESTIONS = [

 dict(q="What does a titration curve plot, according to the course framework?",
      choices=[
        "The pH of the flask against the volume of titrant added",
        "The volume of titrant added against the mass of analyte present",
        "The concentration of the analyte against time",
        "The temperature of the flask against the volume of titrant added",
        "The pH of the flask against the ionization constant of the analyte"],
      ans=0,
      why="EK 8.5.A.1 states that a titration curve plots pH against the volume of titrant "
          "added and is useful for summarizing results from a titration."),

 dict(q="What is true at the equivalence point of a titration of a monoprotic acid or "
        "base?",
      choices=[
        "The moles of titrant added equal the moles of analyte originally present",
        "The volume of titrant added equals the volume of analyte originally present",
        "The concentration of titrant equals the concentration of analyte",
        "The pH of the flask equals the pKa of the analyte",
        "Half of the analyte has been consumed by the titrant"],
      ans=0,
      why="EK 8.5.A.2 states that at the equivalence point the number of moles of titrant "
          "added is equal to the number of moles of analyte originally present. Equal "
          "volumes or equal concentrations would follow only in the special case where "
          "both happen to hold, and the pH equalling the pKa is the HALF-equivalence point "
          "of EK 8.5.A.3."),

 dict(q="A 25.00 mL sample of a monoprotic acid requires 20.00 mL of 0.100 M NaOH to "
        "reach the equivalence point. What is the concentration of the acid?",
      choices=["0.0800 M", "0.100 M", "0.125 M", "0.0500 M", "0.200 M"],
      ans=0,
      why="EK 8.5.A.2 makes the moles of titrant at the equivalence point equal to the "
          "moles of analyte, so 2.00 millimoles of hydroxide means 2.00 millimoles of "
          "acid, and dividing by the 25.00 mL sample volume gives the concentration. The "
          "value 0.125 M comes from dividing by the titrant volume instead."),

 dict(q="Does the equivalence-point relationship between moles of titrant and moles of "
        "analyte hold for a weak acid as well as a strong one?",
      choices=[
        "Yes, the framework states it holds for titrations of both strong and weak acids "
        "and bases",
        "No, it holds only for strong acids and bases, since weak ones ionize partly",
        "No, it holds only for weak acids and bases, since strong ones react too quickly",
        "Yes, but only when the titrant is also weak",
        "Only when the equivalence point falls at a pH of exactly 7"],
      ans=0,
      why="EK 8.5.A.2 ends by saying this is the case for titrations of strong "
          "acids and bases AND weak acids and bases. Partial ionization changes the pH "
          "reached, not the stoichiometry of the neutralization."),

 dict(q="What is true at the half-equivalence point of a weak acid titration?",
      choices=[
        "The concentrations of the weak acid and its conjugate base are equal, so the pH "
        "equals the pKa",
        "The concentration of the conjugate base is twice that of the weak acid",
        "All of the weak acid has been converted to its conjugate base",
        "The pH equals 7.00 at 25 degrees Celsius",
        "The moles of titrant added equal the moles of acid originally present"],
      ans=0,
      why="EK 8.5.A.3 says that at the half-equivalence point there are equal "
          "concentrations of each species in the conjugate pair, and because pH equals pKa "
          "when the conjugate acid and base have equal concentrations, the pKa can be read "
          "from the pH there. Complete conversion happens at the FULL equivalence point."),

 dict(q="The table gives pH readings during the titration of a weak monoprotic acid with "
        "0.100 M NaOH, and the equivalence point falls at 20.00 mL. What is the pKa of the "
        "acid?",
      table=_T_WEAK_CURVE,
      choices=["pKa = 4.75", "pKa = 8.80", "pKa = 2.90", "pKa = 4.00", "pKa = 5.50"],
      ans=0,
      why="EK 8.5.A.3 puts the half-equivalence point halfway to the equivalence point, "
          "which is 10.00 mL here, and makes the pH there equal to the pKa. The value 8.80 "
          "is the pH at the equivalence point, which EK 8.5.A.4 explains separately."),

 dict(q="Using the same table, what is the concentration of the weak acid if the analyte "
        "sample was 25.00 mL and the equivalence point falls at 20.00 mL?",
      table=_T_WEAK_CURVE,
      choices=["0.0800 M", "0.100 M", "0.125 M", "0.0400 M", "0.200 M"],
      ans=0,
      why="EK 8.5.A.2 equates the moles of titrant at the equivalence point with the moles "
          "of analyte, and the tabulated titrant concentration multiplied by the "
          "equivalence volume gives 2.00 millimoles. Dividing by the 25.00 mL sample gives "
          "the concentration, and the relationship holds for a weak acid as it does for a "
          "strong one."),

 dict(q="Using the same table, why is the pH at the equivalence point above 7.00?",
      table=_T_WEAK_CURVE,
      choices=[
        "The conjugate base of the weak acid is present there and undergoes proton "
        "transfer with water",
        "Excess sodium hydroxide remains at the equivalence point of any titration",
        "The weak acid is still present in large amounts at the equivalence point",
        "The pH at the equivalence point of every titration is above 7.00",
        "Sodium ion reacts with water to produce hydroxide ion"],
      ans=0,
      why="EK 8.5.A.4 says that in titrations of weak acids the conjugate base is present "
          "at the equivalence point and can undergo proton-transfer reactions with the "
          "surrounding water, producing a basic solution. No titrant is in excess at the "
          "equivalence point, and sodium ion is a spectator."),

 dict(q="The table gives pH readings during the titration of a strong monoprotic acid "
        "with 0.100 M NaOH. What is the pH at the equivalence point, and why?",
      table=_T_STRONG_CURVE,
      choices=[
        "7.00, because a strong acid and strong base titration results in a neutral pH at "
        "the equivalence point",
        "7.00, because every titration reaches a neutral pH at its equivalence point",
        "3.00, because the acid is still partly present at the equivalence point",
        "11.00, because the conjugate base of the strong acid reacts with water",
        "1.00, because the pH cannot rise above its starting value"],
      ans=0,
      why="EK 8.5.A.4 states that strong acid and strong base titrations result in neutral "
          "pH at the equivalence point, and the tabulated readings show the pH passing "
          "through 7.00 at 25.00 mL. Weak-component titrations do NOT end at 7.00, which "
          "is why the framework distinguishes the cases."),

 dict(q="Using the same table for the strong acid titration, what was the concentration of "
        "the acid if the analyte sample was 25.00 mL?",
      table=_T_STRONG_CURVE,
      choices=["0.100 M", "0.0800 M", "0.125 M", "0.200 M", "0.0500 M"],
      ans=0,
      why="EK 8.5.A.2 makes the moles of titrant at the equivalence point equal the moles "
          "of analyte. The tabulated pH reaches 7.00 at 25.00 mL of 0.100 M titrant, which "
          "is 2.50 millimoles, and dividing by the 25.00 mL sample gives the "
          "concentration."),

 dict(q="Why does a strong acid titration have no half-equivalence point of the kind the "
        "framework describes?",
      choices=[
        "Because a strong acid has no conjugate acid-base pair present in comparable "
        "amounts during the titration",
        "Because a strong acid reaches its equivalence point too quickly to measure",
        "Because the volume halfway to the equivalence point cannot be located on a curve",
        "Because a strong acid has a pKa of exactly zero",
        "Because the pH of a strong acid never changes during a titration"],
      ans=0,
      why="EK 8.5.A.3 introduces the half-equivalence point specifically for titrations of "
          "WEAK acids and bases, where an un-ionized acid and its conjugate base coexist. "
          "A strong acid is essentially fully ionized under EK 8.2.A.1, so there is no "
          "such pair to reach equal concentrations."),

 dict(q="Using the table of titration trials, what is the concentration of the analyte in "
        "trial 2?",
      table=_T_TRIALS,
      choices=["0.100 M", "0.200 M", "0.400 M", "0.0500 M", "0.250 M"],
      ans=0,
      why="EK 8.5.A.2 equates moles of titrant with moles of analyte, so multiplying the "
          "tabulated titrant concentration by the tabulated equivalence volume and "
          "dividing by the tabulated analyte volume gives the answer."),

 dict(q="Using the same table of trials, which trial has the most concentrated analyte?",
      table=_T_TRIALS,
      choices=["Trial 3", "Trial 1", "Trial 2",
               "Trials 1 and 2 are tied", "All three are equal"],
      ans=0,
      why="EK 8.5.A.2 makes each analyte concentration the tabulated titrant concentration "
          "times the tabulated equivalence volume divided by the tabulated analyte volume, "
          "and comparing the three results identifies a single largest value."),

 dict(q="Using the same table of trials, what is the concentration of the analyte in trial "
        "3?",
      table=_T_TRIALS,
      choices=["0.500 M", "0.250 M", "1.00 M", "0.0500 M", "0.100 M"],
      ans=0,
      why="The tabulated equivalence volume equals the tabulated analyte volume in this "
          "trial, so EK 8.5.A.2 makes the analyte concentration equal to the titrant "
          "concentration. Equal volumes are what make the two concentrations agree, and "
          "that is a coincidence of this trial rather than a general rule."),

 dict(q="The table gives pH readings during the titration of a weak DIPROTIC acid with "
        "0.100 M NaOH, and two separate pH jumps occur. How many acidic protons does the "
        "acid have, and how is that read from the data?",
      table=_T_DIPROTIC,
      choices=[
        "Two, because the readings pass through two separate regions of rapid pH rise",
        "One, because there is only one analyte in the flask",
        "Three, because there are three readings above pH 7",
        "Two, because the titrant concentration is 0.100 M",
        "The number of protons cannot be found from a titration"],
      ans=0,
      why="EK 8.5.A.5 states that for polyprotic acids, titration curves can be used to "
          "determine the number of acidic protons. Each proton removed produces its own "
          "region of rapid pH change, and the tabulated readings rise steeply twice."),

 dict(q="What does the framework say can be identified along a polyprotic titration curve, "
        "besides the number of acidic protons?",
      choices=[
        "The major species present at any point, and the pKa associated with each proton",
        "The exact concentration of every species present at every point",
        "The rate at which each proton is removed",
        "The enthalpy change for each proton transfer",
        "The identity of the titrant used"],
      ans=0,
      why="EK 8.5.A.5 says the major species present at any point along the curve can be "
          "identified, along with the pKa associated with each proton. Its exclusion "
          "statement rules out computing the concentration of each species present."),

 dict(q="Which calculation does the framework's exclusion statement place OUTSIDE the "
        "scope of the exam for a polyprotic titration?",
      choices=[
        "Computing the concentration of each species present along the curve",
        "Identifying which species are present in large versus small amounts",
        "Determining the number of acidic protons from the curve",
        "Identifying the pKa associated with each proton",
        "Recognising the shape of the curve as a polyprotic one"],
      ans=0,
      why="The exclusion statement attached to EK 8.5.A.5 says computation of the "
          "concentration of each species present in the titration curve for polyprotic "
          "acids will not be assessed, while qualitative reasoning about which species are "
          "present in large versus small concentrations remains within scope."),

 dict(q="A weak base is titrated with a strong acid. What does the framework say about the "
        "pH at the equivalence point?",
      choices=[
        "It is acidic, because the conjugate acid of the weak base is present and "
        "transfers a proton to water",
        "It is basic, because the analyte was a base",
        "It is exactly 7.00, as for every equivalence point",
        "It is acidic, because excess strong acid remains at the equivalence point",
        "It cannot be predicted without the value of Kb"],
      ans=0,
      why="EK 8.5.A.4 says that in titrations of weak bases the conjugate acid of the weak "
          "base is present at the equivalence point and can undergo proton transfer with "
          "the surrounding water, producing an acidic solution. No titrant is in excess "
          "there, by the definition of the equivalence point."),

 dict(q="Using the table of readings for the weak acid titration, what is the pH at the "
        "half-equivalence point, given an equivalence volume of 20.00 mL?",
      table=_T_WEAK_CURVE,
      choices=["pH = 4.75", "pH = 4.00", "pH = 5.50", "pH = 8.80", "pH = 2.90"],
      ans=0,
      why="The half-equivalence point sits at half the equivalence volume, which is 10.00 "
          "mL, and the table reports the pH there directly. EK 8.5.A.3 is what makes this "
          "particular reading worth locating."),

 dict(q="Why does the framework describe the half-equivalence point as useful?",
      choices=[
        "Because the pKa of the weak acid can be determined from the pH measured there",
        "Because the analyte concentration can be determined from the volume used there",
        "Because the solution is exactly neutral there",
        "Because all of the analyte has reacted by that point",
        "Because the titrant concentration can be determined from the pH there"],
      ans=0,
      why="EK 8.5.A.3 says the pKa can be determined from the pH at the half-equivalence "
          "point, because the conjugate acid and base are present in equal concentrations "
          "there. The analyte CONCENTRATION comes from the equivalence point under EK "
          "8.5.A.2, a different reading."),

 dict(q="A 50.00 mL sample of a monoprotic weak acid is titrated with 0.200 M NaOH and the "
        "equivalence point is reached after 25.00 mL. What is the concentration of the "
        "acid?",
      choices=["0.100 M", "0.200 M", "0.400 M", "0.0500 M", "0.250 M"],
      ans=0,
      why="EK 8.5.A.2 equates the moles of titrant with the moles of analyte: 5.00 "
          "millimoles of hydroxide means 5.00 millimoles of acid, and dividing by 50.00 mL "
          "gives the concentration. The relationship holds for a weak acid exactly as for "
          "a strong one."),

 dict(q="A monoprotic weak acid is titrated and the pH at the half-equivalence point is "
        "measured as 5.00. What is the acid ionization constant of the acid?",
      choices=["\\( 1.0 \\times 10^{-5} \\)", "\\( 1.0 \\times 10^{-9} \\)",
               "\\( 5.0 \\times 10^{-1} \\)", "\\( 1.0 \\times 10^{-14} \\)",
               "\\( 1.0 \\times 10^{-10} \\)"],
      ans=0,
      why="EK 8.5.A.3 makes the pH at the half-equivalence point equal to the pKa, and EK "
          "8.3.A.2 defines pKa as the negative logarithm of Ka, so the constant is ten "
          "raised to the negative of that pH. The value ten to the negative ninth would be "
          "the conjugate base constant."),

 dict(q="Two weak monoprotic acids of the same concentration are titrated with the same "
        "titrant. Acid J has a half-equivalence pH of 3.00 and acid L has a "
        "half-equivalence pH of 6.00. Which is the stronger acid?",
      choices=[
        "Acid J, because its lower half-equivalence pH means a lower pKa",
        "Acid L, because its higher half-equivalence pH means a lower pKa",
        "They are equally strong, since both are weak",
        "Acid L, because a higher pH always means a stronger acid",
        "The comparison requires the two equivalence volumes"],
      ans=0,
      why="EK 8.5.A.3 makes the half-equivalence pH equal to the pKa, and EK 8.3.A.2 makes "
          "pKa the negative logarithm of Ka, so the smaller pKa belongs to the larger "
          "ionization constant and therefore to the stronger acid."),

 dict(q="Two weak acids of the same concentration and volume are titrated with the same "
        "titrant. What must be true of their equivalence volumes?",
      choices=[
        "They are equal, because the equivalence volume depends on moles rather than on "
        "acid strength",
        "The stronger acid reaches its equivalence point at a smaller volume",
        "The weaker acid reaches its equivalence point at a smaller volume",
        "The equivalence volumes differ by the difference in the two pKa values",
        "The equivalence volumes cannot be compared without the two ionization constants"],
      ans=0,
      why="EK 8.5.A.2 fixes the equivalence point by the equality of MOLES of titrant and "
          "analyte, which depends on concentration and volume alone. Acid strength moves "
          "the pH reached at that point, which EK 8.5.A.4 describes, but not the volume "
          "required to get there."),

 dict(q="Using the table of readings for the diprotic acid titration, which pH reading is "
        "closest to the FIRST equivalence point, if the second falls at 40.00 mL?",
      table=_T_DIPROTIC,
      choices=["The reading at 20.00 mL", "The reading at 10.00 mL",
               "The reading at 30.00 mL", "The reading at 40.00 mL",
               "The reading at 50.00 mL"],
      ans=0,
      why="EK 8.5.A.5 has the curve reveal the number of acidic protons, and for a diprotic "
          "acid the two protons are removed in equal amounts of titrant, so the first "
          "equivalence point falls at half the volume of the second. The tabulated "
          "readings include exactly that volume."),

 dict(q="Which species is present in the largest amount just after the first equivalence "
        "point in the titration of a weak diprotic acid H2A?",
      choices=[
        "The singly deprotonated ion HA-",
        "The fully protonated acid H2A",
        "The fully deprotonated ion A2-",
        "Hydroxide ion from the titrant",
        "Undissociated water only"],
      ans=0,
      why="At the first equivalence point one proton has been removed from essentially "
          "every molecule and the second has not yet begun to be removed, so the "
          "singly deprotonated species dominates. EK 8.5.A.5 permits exactly this "
          "qualitative identification of the major species while excluding computation of "
          "each concentration."),

 dict(q="Why does the framework call a titration a reaction carried out under CONTROLLED "
        "conditions?",
      choices=[
        "Because the titrant is added in measured amounts so the composition at each stage "
        "is known",
        "Because the temperature is held at exactly 25 degrees Celsius throughout",
        "Because the analyte concentration is known before the titration begins",
        "Because only strong acids and strong bases may be used",
        "Because the reaction is stopped before the equivalence point is reached"],
      ans=0,
      why="EK 8.5.A.1 pairs the phrase with the titration curve, which plots pH against "
          "the VOLUME OF TITRANT ADDED, so the measured addition is what makes each point "
          "on the curve interpretable. The analyte concentration is normally the unknown "
          "being determined under EK 8.5.A.2."),

 dict(q="A 10.00 mL sample of a monoprotic base is titrated with 0.500 M HCl, and the "
        "equivalence point is reached after 10.00 mL. What is the concentration of the "
        "base?",
      choices=["0.500 M", "0.250 M", "1.00 M", "0.100 M", "0.0500 M"],
      ans=0,
      why="EK 8.5.A.2 equates the moles of titrant with the moles of analyte, and 5.00 "
          "millimoles of acid means 5.00 millimoles of base in 10.00 mL. The two volumes "
          "being equal is what makes the two concentrations equal here."),

 dict(q="At which point in a weak acid titration is the flask a buffer, according to the "
        "species present?",
      choices=[
        "Between the start and the equivalence point, where both the weak acid and its "
        "conjugate base are present",
        "Exactly at the equivalence point, where the conjugate base is present",
        "After the equivalence point, where excess titrant is present",
        "Only at the very start, before any titrant has been added",
        "At no point, since a titration destroys any buffer"],
      ans=0,
      why="EK 8.5.A.3 places equal concentrations of the conjugate pair at the "
          "half-equivalence point, and both members are present throughout the region "
          "before the equivalence point. EK 8.5.A.4 puts only the conjugate base at the "
          "equivalence point itself, so the pair is gone by then."),

 dict(q="A monoprotic weak base is titrated with a strong acid and the pH at the "
        "half-equivalence point is 9.00. What is the pKa of the conjugate acid of that "
        "base at 25 degrees Celsius?",
      choices=["pKa = 9.00", "pKa = 5.00", "pKa = 14.00", "pKa = 4.50", "pKa = 23.00"],
      ans=0,
      why="EK 8.5.A.3's statement is about equal concentrations of the two members of the "
          "conjugate pair, which is where pH equals the pKa of the conjugate ACID of the "
          "base. Subtracting from fourteen would give the pKb of the base instead."),

]
