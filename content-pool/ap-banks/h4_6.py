# AP CHEMISTRY 4.6 Introduction to Titration
# CED effective Fall 2024, Unit 4 Chemical Reactions.
# Learning objective 4.6.A: identify the equivalence point in a titration based
# on the amounts of the titrant and analyte, assuming the titration reaction
# goes to completion. Suggested skill 3.A, represent chemical phenomena using
# appropriate graphing techniques.
#
# Essential knowledge relied on, in the framework's own words:
#   4.6.A.1  Titrations may be used to determine the amount of an analyte in
#            solution. The titrant has a known concentration of a species that
#            reacts specifically and quantitatively with the analyte. The
#            equivalence point of the titration occurs when the analyte is
#            totally consumed by the reacting species in the titrant. The
#            equivalence point is often indicated by a change in a property
#            (such as color) that occurs when the equivalence point is reached.
#            This observable event is called the endpoint of the titration.
#
# ONE ESSENTIAL KNOWLEDGE STATEMENT, THIRTY QUESTIONS. 4.6.A.1 is a single
# statement, so the variety here comes from the LEARNING OBJECTIVE rather than
# from extra content: the objective asks a student to identify the equivalence
# point FROM THE AMOUNTS of titrant and analyte, which is a calculation, and
# most items are that calculation on different stoichiometries. The remaining
# items key on the four things the statement itself defines -- what a titrant
# is, what an analyte is, when the equivalence point occurs, and what the
# endpoint is.
#
# NO pH THEORY. Acid strength, indicators' own equilibria and the pH at
# equivalence belong to Unit 8. Where a pH column appears it is only a measured
# property whose sharp change locates the equivalence point, which is what
# 4.6.A.1 itself says an observable property change does.
#
# NO GRAPHS. Skill 3.A is about graphing and the bank cannot carry a figure, so
# every titration curve here is a TABLE of volume against a measured property.
#
# NOTATION. Chemistry is not typeset; formulas stay plain text.
TOPIC = ("4.6", "Introduction to Titration", 4)

_T_CURVE = dict(
    headers=["Volume of 0.100 M NaOH added (milliliters)", "Measured pH"],
    rows=[["10.0", "2.7"],
          ["20.0", "3.4"],
          ["24.0", "4.1"],
          ["25.0", "8.2"],
          ["26.0", "11.5"],
          ["30.0", "12.0"]])

_T_CONDUCT = dict(
    headers=["Volume of 0.050 M Ba(OH)2 added (milliliters)",
             "Conductivity of the mixture (arbitrary units)"],
    rows=[["0.0", "980"],
          ["5.0", "610"],
          ["10.0", "240"],
          ["15.0", "30"],
          ["20.0", "300"],
          ["25.0", "590"]])

_T_TRIALS = dict(
    headers=["Trial", "Volume of analyte used (milliliters)",
             "Volume of 0.150 M titrant at the endpoint (milliliters)"],
    rows=[["1", "25.0", "18.2"],
          ["2", "25.0", "18.0"],
          ["3", "25.0", "31.6"],
          ["4", "25.0", "18.1"]])

_T_COLOR = dict(
    headers=["Volume of titrant added (milliliters)", "Color of the flask contents"],
    rows=[["0.00", "Colorless"],
          ["12.00", "Colorless"],
          ["17.40", "Colorless"],
          ["17.60", "Faint permanent pink"],
          ["20.00", "Deep pink"]])

_T_TWOACIDS = dict(
    headers=["Flask", "Acid in the flask", "Volume of acid (milliliters)",
             "Concentration of acid (moles per liter)"],
    rows=[["1", "HCl", "20.0", "0.100"],
          ["2", "H2SO4", "20.0", "0.100"]])

QUESTIONS = [

 dict(q="In a titration, which condition defines the equivalence point?",
      choices=[
        "The analyte has been totally consumed by the reacting species in the "
        "titrant",
        "Equal volumes of titrant and analyte solution have been combined",
        "The mixture has become neutral to the touch and stops changing "
        "temperature",
        "The buret has been emptied of all the titrant it was filled with",
        "The concentrations of titrant and analyte in the flask have become "
        "equal to one another"],
      ans=0,
      why="EK 4.6.A.1, near verbatim: the equivalence point of the titration "
          "occurs when the analyte is totally consumed by the reacting species "
          "in the titrant. Nothing in that definition refers to equal volumes "
          "or equal concentrations."),

 dict(q="A titration is carried out with an indicator that turns pink as the "
        "last of the analyte is used up. What is the name for that observable "
        "color change?",
      choices=[
        "The endpoint of the titration",
        "The equivalence point of the titration",
        "The standardization of the titrant",
        "The stoichiometric ratio of the reaction",
        "The limiting condition of the analyte"],
      ans=0,
      why="EK 4.6.A.1 states that the equivalence point is often indicated by a "
          "change in a property, such as color, and that this observable event "
          "is called the endpoint of the titration. The endpoint is the "
          "observation; the equivalence point is the condition it signals."),

 dict(q="Which description of a titrant matches the course framework?",
      choices=[
        "A solution of known concentration containing a species that reacts "
        "specifically and quantitatively with the analyte",
        "A solution of unknown concentration whose amount is to be determined by "
        "the experiment",
        "A dye added in a single drop to make the color change visible at the "
        "end",
        "Any solvent used to dilute the sample so that its volume can be read "
        "accurately",
        "A solution that reacts with every species present in the flask in the "
        "same proportion"],
      ans=0,
      why="EK 4.6.A.1, near verbatim: the titrant has a known concentration of a "
          "species that reacts specifically and quantitatively with the analyte. "
          "Being of known concentration is what allows the analyte amount to be "
          "computed from the volume delivered."),

 dict(q="Why must the species in the titrant react SPECIFICALLY with the analyte "
        "rather than with several substances in the flask?",
      choices=[
        "Because the volume delivered would otherwise measure the analyte "
        "together with whatever else consumed the titrant",
        "Because a titrant that reacted with more than one species would fail to "
        "dissolve in the solvent",
        "Because a specific reaction is the only kind that can be made to go to "
        "completion at room temperature",
        "Because otherwise the concentration of the titrant would change while "
        "it sat in the buret",
        "Because reacting with several species would prevent the flask from ever "
        "changing color"],
      ans=0,
      why="EK 4.6.A.1 requires the titrant to react specifically and "
          "quantitatively with the analyte, and the whole calculation converts "
          "the delivered amount of titrant into an amount of analyte. A side "
          "reaction would put some of that delivered amount somewhere else."),

 dict(q="A 25.0 mL sample of hydrochloric acid is titrated with 0.100 M sodium "
        "hydroxide, which reacts with it in a one to one ratio. The equivalence "
        "point is reached after 20.0 mL of the base has been delivered. What is "
        "the concentration of the acid?",
      choices=["0.0800 M", "0.125 M", "0.100 M", "0.0500 M", "0.200 M"],
      ans=0,
      why="EK 4.6.A.1 makes the equivalence point the moment the analyte is "
          "totally consumed. The base delivers 2.00 millimoles, the one to one "
          "ratio makes that the acid amount, and dividing by the 25.0 mL sample "
          "volume gives the concentration."),

 dict(q="Sulfuric acid reacts with sodium hydroxide according to H2SO4 + 2 NaOH → "
        "Na2SO4 + 2 H2O. What volume of 0.200 M NaOH is required to reach the "
        "equivalence point with 10.0 mL of 0.100 M H2SO4?",
      choices=["10.0 mL", "5.00 mL", "20.0 mL", "2.50 mL", "40.0 mL"],
      ans=0,
      why="EK 4.6.A.1 places the equivalence point where the analyte is totally "
          "consumed, and the balanced equation requires two moles of base per "
          "mole of acid. The flask holds 1.00 millimole of acid, so 2.00 "
          "millimoles of base are needed."),

 dict(q="The table records the pH of a flask of hydrochloric acid as 0.100 M "
        "sodium hydroxide is added. At approximately what volume of added base "
        "was the equivalence point reached?",
      table=_T_CURVE,
      choices=[
        "25.0 mL, because the measured property changes most sharply between the "
        "readings on either side of it",
        "10.0 mL, because that is the first volume at which a reading was taken",
        "30.0 mL, because that is where the pH stops rising",
        "20.0 mL, because the pH there is closest to the middle of the range "
        "covered",
        "Between 5.0 mL and 10.0 mL, because the earliest readings change by the "
        "largest number of pH units per milliliter"],
      ans=0,
      why="EK 4.6.A.1 states that the equivalence point is often indicated by a "
          "change in a measurable property. The tabulated pH rises by less than "
          "one unit over each early interval and by more than four units across "
          "the interval bracketing the stated volume."),

 dict(q="A student reports that a titration reached its endpoint at 22.35 mL and "
        "assumes this equals the equivalence point. Which statement about that "
        "assumption is correct?",
      choices=[
        "The endpoint is the observable signal and may be reached slightly "
        "before or after the analyte is totally consumed",
        "The endpoint and the equivalence point are the same event under every "
        "circumstance, so there is nothing to check",
        "The endpoint always comes first, because an indicator changes color "
        "before any analyte has reacted",
        "The endpoint is a calculated quantity while the equivalence point is "
        "measured with the buret",
        "The endpoint depends only on the concentration of the analyte, so it "
        "cannot be affected by the indicator chosen"],
      ans=0,
      why="EK 4.6.A.1 defines the equivalence point as the condition in which "
          "the analyte is totally consumed and the endpoint as the observable "
          "event indicating it. They are separate things, so an indicator "
          "changing a little early or late shifts the reading from the true "
          "value."),

 dict(q="What quantity does a titration determine directly?",
      choices=[
        "The amount of the analyte present in the solution being titrated",
        "The rate at which the analyte and the titrant react with one another",
        "The temperature at which the reaction between titrant and analyte "
        "becomes complete",
        "The relative strengths of the bonds broken in the titration reaction",
        "The identity of every substance dissolved in the flask"],
      ans=0,
      why="EK 4.6.A.1 opens by stating that titrations may be used to determine "
          "the amount of an analyte in solution. Rate belongs to Unit 5 and is "
          "not what the delivered volume of titrant measures."),

 dict(q="A 20.0 mL sample of a sodium hydroxide solution requires 16.0 mL of "
        "0.250 M hydrochloric acid, which reacts with it one to one, to reach "
        "the equivalence point. What amount of sodium hydroxide was present in "
        "the sample?",
      choices=["4.00 millimoles", "5.00 millimoles", "3.20 millimoles",
               "0.800 millimoles", "8.00 millimoles"],
      ans=0,
      why="EK 4.6.A.1 makes the equivalence point the moment the analyte is "
          "totally consumed by the titrant. Multiplying the acid concentration "
          "by the volume delivered gives the acid amount, and the one to one "
          "ratio makes the base amount equal to it."),

 dict(q="Before a titration, a student adds 50 mL of distilled water to the flask "
        "containing the analyte solution. Assuming everything else is unchanged, "
        "what happens to the volume of titrant needed to reach the equivalence "
        "point?",
      choices=[
        "It is unchanged, because adding water changes the concentration of the "
        "analyte but not the amount of it in the flask",
        "It doubles, because the analyte solution now occupies a larger volume",
        "It is halved, because the analyte has been diluted to half its former "
        "concentration",
        "It becomes impossible to determine, because the analyte concentration "
        "is no longer known",
        "It increases slightly, because the added water reacts with a small part "
        "of the titrant"],
      ans=0,
      why="EK 4.6.A.1 puts the equivalence point where the analyte is totally "
          "consumed, and that depends on how much analyte is present, not on "
          "how much solvent surrounds it. Diluting adds no analyte and removes "
          "none."),

 dict(q="The table gives the conductivity of a solution of sulfuric acid as "
        "0.050 M barium hydroxide is added, forming insoluble barium sulfate and "
        "water. Which volume is closest to the equivalence point, and why?",
      table=_T_CONDUCT,
      choices=[
        "15.0 mL, because the conductivity reaches its lowest value there and "
        "then rises again",
        "0.0 mL, because the conductivity is at its largest value there",
        "25.0 mL, because the conductivity is rising steadily at that point",
        "10.0 mL, because the conductivity is about a quarter of its starting "
        "value there",
        "20.0 mL, because it is the midpoint of the volumes for which readings "
        "were taken"],
      ans=0,
      why="EK 4.6.A.1 states that the equivalence point is often indicated by a "
          "change in a property. Ions are removed from solution until the "
          "analyte is totally consumed, so conductivity falls to a minimum "
          "there and rises once excess titrant begins to accumulate."),

 dict(q="Potassium permanganate solution is used to titrate iron(II), reacting "
        "according to MnO4- + 5 Fe2+ + 8 H+ → Mn2+ + 5 Fe3+ + 4 H2O. If 0.0020 "
        "mol of permanganate is delivered at the equivalence point, what amount "
        "of iron(II) was present?",
      choices=["0.010 mol", "0.0020 mol", "0.00040 mol", "0.040 mol",
               "0.0050 mol"],
      ans=0,
      why="EK 4.6.A.1 makes the equivalence point the point at which the analyte "
          "is totally consumed by the reacting species in the titrant, and the "
          "balanced equation puts five iron(II) ions with every permanganate "
          "ion."),

 dict(q="A titration of 25.0 mL of vinegar requires 20.0 mL of 0.500 M sodium "
        "hydroxide, which reacts one to one with the acetic acid present. Taking "
        "the molar mass of acetic acid as 60.0 grams per mole, what mass of "
        "acetic acid was in the sample?",
      choices=["0.600 g", "0.300 g", "1.20 g", "0.150 g", "6.00 g"],
      ans=0,
      why="EK 4.6.A.1 lets the delivered titrant fix the analyte amount: 0.0100 "
          "mol of base, matched one to one, is 0.0100 mol of acid. Multiplying "
          "by the stated molar mass converts that amount to a mass."),

 dict(q="The table shows four trials of the same titration, all using 25.0 mL of "
        "the same analyte solution. Which trial should be excluded before "
        "averaging, and why?",
      table=_T_TRIALS,
      choices=[
        "Trial 3, because its endpoint volume differs from the other three by "
        "more than thirteen milliliters",
        "Trial 1, because its endpoint volume is the largest of the first three "
        "trials",
        "Trial 2, because its endpoint volume is the smallest recorded",
        "Trial 4, because it was the last trial performed and is therefore the "
        "least careful",
        "None of them, because every trial used the same volume of analyte"],
      ans=0,
      why="EK 4.6.A.1 makes the delivered titrant volume the measurement of the "
          "analyte amount, and the same analyte volume and concentration must "
          "give the same delivered volume. Three trials agree within 0.2 mL and "
          "one does not, so that one records something other than the same "
          "equivalence point."),

 dict(q="What does the assumption that the titration reaction goes to completion "
        "allow a student to conclude?",
      choices=[
        "That at the equivalence point the amount of titrant delivered is "
        "related to the analyte amount by the coefficients alone",
        "That the reaction between titrant and analyte occurs instantly no "
        "matter how quickly the titrant is added",
        "That the endpoint and the equivalence point must occur at exactly the "
        "same volume",
        "That the analyte and titrant must be present in equal concentrations at "
        "the equivalence point",
        "That no indicator is needed, because the completion of the reaction is "
        "always visible"],
      ans=0,
      why="EK 4.6.A.1 defines the equivalence point as the analyte being totally "
          "consumed by the reacting species in the titrant. If none of either "
          "remains unreacted, the balanced coefficients alone connect the two "
          "amounts."),

 dict(q="A student titrates 10.0 mL of 0.200 M calcium hydroxide with "
        "hydrochloric acid, which reacts according to Ca(OH)2 + 2 HCl → CaCl2 + "
        "2 H2O. What amount of hydrochloric acid is required to reach the "
        "equivalence point?",
      choices=["4.00 millimoles", "2.00 millimoles", "1.00 millimole",
               "8.00 millimoles", "0.500 millimoles"],
      ans=0,
      why="EK 4.6.A.1 places the equivalence point where the analyte is totally "
          "consumed. The flask holds 2.00 millimoles of calcium hydroxide and "
          "the equation requires two moles of acid per mole of it."),

 dict(q="Two flasks are prepared as shown in the table, and each is titrated to "
        "the equivalence point with the same 0.100 M sodium hydroxide solution. "
        "How do the volumes of base required compare?",
      table=_T_TWOACIDS,
      choices=[
        "Flask 2 requires twice the volume of flask 1, because each mole of "
        "H2SO4 supplies two protons to be neutralized",
        "The two flasks require the same volume, because they hold equal volumes "
        "at equal concentrations",
        "Flask 1 requires twice the volume of flask 2, because HCl is the "
        "stronger of the two acids",
        "Flask 2 requires half the volume of flask 1, because H2SO4 has the "
        "larger molar mass",
        "The comparison cannot be made without knowing the temperature of the "
        "two flasks"],
      ans=0,
      why="EK 4.6.A.1 makes the equivalence point the total consumption of the "
          "analyte by the titrant. The tabulated volumes and concentrations give "
          "equal amounts of the two acids, but neutralizing H2SO4 completely "
          "consumes two hydroxide ions per acid molecule against one for HCl."),

 dict(q="Which of the following would cause a titration to report an analyte "
        "amount LARGER than the true one?",
      choices=[
        "Continuing to add titrant past the volume at which the indicator first "
        "changed color permanently",
        "Rinsing the flask with distilled water before adding the analyte "
        "solution to it",
        "Reading the buret from slightly above the level of the meniscus",
        "Stirring the flask continuously throughout the addition of titrant",
        "Using a titrant whose concentration is larger than the analyte "
        "concentration"],
      ans=0,
      why="EK 4.6.A.1 makes the delivered titrant volume the measure of the "
          "analyte amount. Titrant added after the analyte is totally consumed "
          "is counted as though it had reacted, so the computed amount comes out "
          "too large."),

 dict(q="The table records the color of a flask during the titration of an "
        "iron(II) solution with potassium permanganate, which is itself deeply "
        "colored. Which volume best represents the endpoint?",
      table=_T_COLOR,
      choices=[
        "17.60 mL, because it is the smallest volume at which a permanent color "
        "persists in the flask",
        "20.00 mL, because the color there is the most intense recorded",
        "17.40 mL, because it is the largest volume at which the flask is still "
        "colorless",
        "12.00 mL, because it is halfway through the addition",
        "0.00 mL, because the flask starts out colorless and any change from "
        "that is the endpoint"],
      ans=0,
      why="EK 4.6.A.1 calls the observable property change the endpoint. The "
          "purple titrant is decolorized while any analyte remains, so the first "
          "reading at which color persists is the observable signal that the "
          "analyte has been consumed."),

 dict(q="A titrant is described as standardized. What does that mean, and why "
        "does it matter?",
      choices=[
        "Its concentration has been determined accurately, which is required "
        "because the analyte amount is computed from it",
        "It has been diluted until its concentration equals that of the analyte, "
        "so equal volumes are needed",
        "It has been filtered so that no solid particles interfere with reading "
        "the buret",
        "It has been warmed to a standard temperature so that its volume is "
        "reproducible",
        "It has been mixed with an indicator so that the color change occurs at "
        "the equivalence point"],
      ans=0,
      why="EK 4.6.A.1 requires the titrant to have a KNOWN concentration. The "
          "analyte amount follows from concentration times delivered volume, so "
          "an error in that concentration passes straight into the reported "
          "result."),

 dict(q="A 15.0 mL sample of an unknown acid requires 30.0 mL of 0.0500 M base "
        "for complete neutralization in a one to one reaction. What is the "
        "concentration of the acid?",
      choices=["0.100 M", "0.0250 M", "0.0500 M", "0.150 M", "0.0333 M"],
      ans=0,
      why="EK 4.6.A.1 puts the equivalence point at the total consumption of the "
          "analyte. The base delivers 1.50 millimoles, which is the acid amount, "
          "and dividing it by the 15.0 mL of sample gives the concentration."),

 dict(q="At the equivalence point of a titration in which the analyte and titrant "
        "react in a one to two ratio, which statement is true?",
      choices=[
        "The amount of titrant delivered is twice the amount of analyte "
        "originally present",
        "The volume of titrant delivered is twice the volume of the analyte "
        "solution",
        "The concentration of the titrant is twice the concentration of the "
        "analyte",
        "The mass of titrant delivered is twice the mass of the analyte",
        "The amount of analyte remaining is twice what it was at the start"],
      ans=0,
      why="EK 4.6.A.1 makes the equivalence point the complete consumption of "
          "the analyte by the reacting species in the titrant, and a one to two "
          "ratio is a statement about AMOUNTS. Volumes, concentrations and "
          "masses stand in that ratio only by coincidence."),

 dict(q="Which piece of information is NOT required in order to compute an "
        "analyte concentration from a titration?",
      choices=[
        "The identity of the indicator used to signal the endpoint",
        "The concentration of the titrant",
        "The volume of titrant delivered at the endpoint",
        "The volume of the analyte solution taken",
        "The mole ratio in which the titrant and analyte react"],
      ans=0,
      why="EK 4.6.A.1 makes the computation depend on the known titrant "
          "concentration, the delivered volume, the reaction stoichiometry and "
          "the analyte sample volume. The indicator only makes the endpoint "
          "visible and does not enter the arithmetic."),

 dict(q="A 0.500 g sample of an impure solid acid is dissolved and titrated, "
        "requiring 0.00400 mol of base in a one to one reaction. If the pure "
        "acid has a molar mass of 100. grams per mole, what mass of the acid was "
        "in the sample?",
      choices=["0.400 g", "0.500 g", "0.0400 g", "0.100 g", "0.800 g"],
      ans=0,
      why="EK 4.6.A.1 makes the delivered titrant fix the analyte amount, which "
          "the one to one ratio puts at 0.00400 mol. Multiplying that amount by "
          "the stated molar mass gives the mass of acid actually present."),

 dict(q="During a titration the flask is swirled continuously. What is the reason "
        "for this?",
      choices=[
        "To mix the added titrant thoroughly so that it reacts with analyte "
        "throughout the flask rather than only where it lands",
        "To raise the temperature of the mixture so that the reaction can reach "
        "completion",
        "To break up the indicator so that its color is distributed evenly",
        "To drive dissolved gases out of the solution before the endpoint is "
        "reached",
        "To slow the delivery of titrant so that the buret reading can be taken "
        "accurately"],
      ans=0,
      why="EK 4.6.A.1 requires the titrant to react quantitatively with the "
          "analyte for the delivered volume to measure the analyte amount. "
          "Unmixed titrant sitting in a local excess is titrant that has been "
          "delivered but has not yet found analyte to react with."),

 dict(q="A student must titrate 25.0 mL of 0.0800 M oxalic acid, H2C2O4, with "
        "0.100 M sodium hydroxide, which removes both of its protons. What "
        "volume of base is required to reach the equivalence point?",
      choices=["40.0 mL", "20.0 mL", "80.0 mL", "10.0 mL", "25.0 mL"],
      ans=0,
      why="EK 4.6.A.1 places the equivalence point at total consumption of the "
          "analyte. The flask holds 2.00 millimoles of the acid and each "
          "molecule requires two hydroxide ions, so 4.00 millimoles of base are "
          "needed."),

 dict(q="Two students titrate identical 20.0 mL samples of the same analyte. One "
        "uses a 0.100 M titrant and the other a 0.200 M titrant, and both reach "
        "the equivalence point correctly. How do their results compare?",
      choices=[
        "They report the same analyte amount, and the student with the more "
        "concentrated titrant delivered half the volume",
        "They report different analyte amounts, because a more concentrated "
        "titrant consumes more analyte",
        "They report the same analyte amount only if they also used the same "
        "volume of titrant",
        "The student with the more concentrated titrant reports twice the "
        "analyte amount",
        "Neither result is valid, because a titrant concentration must match the "
        "analyte concentration"],
      ans=0,
      why="EK 4.6.A.1 makes the equivalence point the total consumption of the "
          "analyte, which is a property of the sample and not of the titrant. "
          "The same analyte amount is reached with half the volume when the "
          "titrant is twice as concentrated."),

 dict(q="Why does the equivalence point of a titration depend on the balanced "
        "equation for the titration reaction?",
      choices=[
        "Because the coefficients set how much titrant is needed to consume the "
        "analyte totally",
        "Because the coefficients determine how quickly the color change appears "
        "at the endpoint",
        "Because the coefficients fix the concentration the titrant must be "
        "prepared at",
        "Because the coefficients determine the volume of the flask that must be "
        "used",
        "Because the coefficients set the temperature at which the reaction is "
        "complete"],
      ans=0,
      why="EK 4.6.A.1 defines the equivalence point as the analyte being totally "
          "consumed by the reacting species in the titrant, and EK 4.5.A.2 makes "
          "the coefficients the proportionality between the amounts. A one to "
          "two reaction reaches that condition at a different delivered amount "
          "than a one to one reaction does."),

 dict(q="An indicator is chosen whose color changes noticeably later than the "
        "moment the analyte is totally consumed. What effect does this have on "
        "the reported analyte amount?",
      choices=[
        "It is reported as larger than it truly is, because extra titrant is "
        "counted as having reacted with analyte",
        "It is reported as smaller than it truly is, because some analyte is "
        "left unmeasured in the flask",
        "It is unaffected, because the indicator does not take part in the "
        "reaction being measured",
        "It is unaffected, because the equivalence point is calculated rather "
        "than observed",
        "It is reported as larger only if the titrant is more concentrated than "
        "the analyte"],
      ans=0,
      why="EK 4.6.A.1 separates the equivalence point from the endpoint that "
          "signals it. All the titrant delivered up to the endpoint is treated "
          "as having reacted with analyte, so an endpoint reached late inflates "
          "the computed amount."),
]
