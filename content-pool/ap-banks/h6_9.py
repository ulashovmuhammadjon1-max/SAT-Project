# AP CHEMISTRY 6.9 Hess's Law
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.9.A: represent a chemical or physical process as a sequence of steps.
# Learning objective 6.9.B: explain the relationship between the enthalpy of a chemical or
# physical process and the sum of the enthalpies of the individual steps. Suggested skill 5.A,
# identify quantities needed to solve a problem from given information.
#
# Essential knowledge relied on, in the framework's own words:
#   6.9.A.1  Many processes can be broken down into a series of steps. Each step in the series
#            has its own energy change.
#   6.9.B.1  Because total energy is conserved (first law of thermodynamics), and each
#            individual reaction in a sequence transfers thermal energy to or from the
#            surroundings, the net thermal energy transferred in the sequence will be equal to
#            the sum of the thermal energy transfers in each of the steps. These thermal energy
#            transfers are the result of potential energy changes among the species in the
#            reaction sequence; thus, at constant pressure, the enthalpy change of the overall
#            process is equal to the sum of the enthalpy changes of the individual steps.
#   6.9.B.2  The following are essential principles of Hess's law:
#              i.   When a reaction is reversed, the enthalpy change stays constant in
#                   magnitude but becomes reversed in mathematical sign.
#              ii.  When a reaction is multiplied by a factor c, the enthalpy change is
#                   multiplied by the same factor c.
#              iii. When two (or more) reactions are added to obtain an overall reaction, the
#                   individual enthalpy changes of each reaction are added to obtain the net
#                   enthalpy change of the overall reaction.
#
# THE EXCLUSION STATEMENT IS PART OF THE TOPIC. The CED attaches one to 6.9: "The concept of
# state functions will not be assessed on the AP Exam." So no item here asks whether the
# enthalpy change depends on the path taken, or names a state function, or hints at one -- and
# verify_h6_9.py bans the phrase from every stem, every choice and every rationale. That is a
# real constraint: path independence is the most natural question anyone would write about
# Hess's law, and the framework has asked for it not to be asked.
#
# THE SIGN IS THE ANSWER IN THIS TOPIC, MORE THAN IN ANY OTHER. Principle i is a rule about a
# sign and nothing else, and a step reversed without its sign reversed produces a plausible
# number that is wrong by twice that step's enthalpy change -- which is item 26, computed. So
# every keyed enthalpy below states its direction as well as its number, every anchor carries
# the sign AND the direction word, and the sign-flipped value sits in exactly one distractor of
# every such item. verify_h6_9.py recomputes each of them through h6_thermo, whose hess_step
# refuses a negative factor precisely so that a reversal cannot be smuggled in as a scaling.
#
# THE ALGEBRA IS CHECKED AS WELL AS THE ARITHMETIC. Getting the enthalpy right is only half of
# a Hess's law item: the combined steps also have to ADD UP to the overall reaction being asked
# about. verify_h6_9.py reverses and scales the tabulated equations exactly as each item's
# combination says, then cancels the species and asserts the remainder is the target equation
# printed in the stem. So an item cannot be arithmetically right about a combination that does
# not actually produce the reaction it claims to.
#
# NO IMAGES, so the steps are carried in a table with their equations and their enthalpy
# changes, which is how the real exam presents them anyway.
#
# NOTATION. export_units.py does not typeset Chemistry. Equations are plain text with the word
# "gives" for the arrow and phase labels in parentheses, as h5_7.py, h6_7.py and h6_8.py write
# them; enthalpies are plain signed numbers with the unit spelled kJ/mol.
TOPIC = ("6.9", "Hess’s Law", 6)

# Nine steps with their own enthalpy changes, as EK 6.9.A.1 describes a series. Every equation
# a question combines is read from this table, so the equation a check uses is the equation the
# student reads.
_T_STEPS = dict(
    headers=["Step", "Reaction", "Enthalpy change (kJ/mol)"],
    rows=[["Step 1", "C(s) + O2(g) gives CO2(g)", "-394"],
          ["Step 2", "2 CO(g) + O2(g) gives 2 CO2(g)", "-566"],
          ["Step 3", "N2(g) + O2(g) gives 2 NO(g)", "+180"],
          ["Step 4", "2 NO(g) + O2(g) gives 2 NO2(g)", "-114"],
          ["Step 5", "S(s) + O2(g) gives SO2(g)", "-297"],
          ["Step 6", "2 SO2(g) + O2(g) gives 2 SO3(g)", "-198"],
          ["Step 7", "CaCO3(s) gives CaO(s) + CO2(g)", "+178"],
          ["Step 8", "2 H2(g) + O2(g) gives 2 H2O(l)", "-572"],
          ["Step 9", "CH4(g) + 2 O2(g) gives CO2(g) + 2 H2O(l)", "-891"]])

QUESTIONS = [

 dict(q="What does the framework say about many chemical and physical processes?",
      choices=[
        "They can be broken down into a series of steps, each with its own energy change",
        "They occur in a single step whose energy change cannot be divided",
        "They can be broken into steps, but only the first step carries an energy change",
        "They can be broken into steps of equal energy change",
        "They can be broken into steps only when no gas is involved"],
      ans=0,
      why="EK 6.9.A.1 states that many processes can be broken down into a series of steps and "
          "that each step in the series has its own energy change, which is what makes a "
          "sequence something to add up."),

 dict(q="At constant pressure, what does the framework say the enthalpy change of an overall "
        "process is equal to?",
      choices=[
        "The sum of the enthalpy changes of the individual steps",
        "The largest of the enthalpy changes of the individual steps",
        "The product of the enthalpy changes of the individual steps",
        "The average of the enthalpy changes of the individual steps",
        "The enthalpy change of the first step in the sequence"],
      ans=0,
      why="EK 6.9.B.1 concludes that, at constant pressure, the enthalpy change of the overall "
          "process is equal to the sum of the enthalpy changes of the individual steps."),

 dict(q="What reason does the framework give for the net thermal energy transferred in a "
        "sequence being equal to the sum of the transfers in each step?",
      choices=[
        "Because total energy is conserved, which is the first law of thermodynamics",
        "Because every step in a sequence transfers the same amount of thermal energy",
        "Because the surroundings return whatever energy the system takes",
        "Because the steps are carried out one after another rather than at once",
        "Because thermal energy is not transferred at all during a sequence of steps"],
      ans=0,
      why="EK 6.9.B.1 opens by naming the reason: because total energy is conserved, which it "
          "labels the first law of thermodynamics, and because each individual reaction in the "
          "sequence transfers thermal energy to or from the surroundings."),

 dict(q="According to the framework's principles, what happens to the enthalpy change when a "
        "reaction is reversed?",
      choices=[
        "It stays constant in magnitude but its mathematical sign is reversed",
        "It stays constant in magnitude and keeps its mathematical sign",
        "Its magnitude is doubled and its sign is reversed",
        "Its magnitude is halved and its sign is kept",
        "It becomes zero, since the reaction undoes itself"],
      ans=0,
      why="EK 6.9.B.2 i states that when a reaction is reversed the enthalpy change stays "
          "constant in magnitude but becomes reversed in mathematical sign. Both halves are "
          "part of the rule."),

 dict(q="Under the framework's principles, a reaction is multiplied by a factor c. What "
        "happens to its enthalpy change?",
      choices=[
        "It is multiplied by the same factor c",
        "It is divided by the factor c",
        "It is left unchanged, since the substances are the same",
        "It is multiplied by the square of the factor c",
        "Its sign is reversed and its magnitude is left unchanged"],
      ans=0,
      why="EK 6.9.B.2 ii states that when a reaction is multiplied by a factor c the enthalpy "
          "change is multiplied by the same factor c. Nothing in the rule touches the sign."),

 dict(q="Two or more reactions are added to obtain an overall reaction. Under the "
        "framework's principles, what happens to their enthalpy changes?",
      choices=[
        "They are added to obtain the net enthalpy change of the overall reaction",
        "They are multiplied to obtain the net enthalpy change",
        "They are averaged to obtain the net enthalpy change",
        "Only the largest of them is kept",
        "They are subtracted in the order the reactions are written"],
      ans=0,
      why="EK 6.9.B.2 iii states that when two or more reactions are added to obtain an "
          "overall reaction, the individual enthalpy changes of each reaction are added to "
          "obtain the net enthalpy change."),

 dict(q="The framework says the thermal energy transfers in a reaction sequence are the result "
        "of what?",
      choices=[
        "Potential energy changes among the species in the reaction sequence",
        "The number of steps the sequence is written in",
        "The order in which the steps are carried out",
        "The temperature of the surroundings before the sequence begins",
        "The pressure at which the last step is carried out"],
      ans=0,
      why="EK 6.9.B.1 says these thermal energy transfers are the result of potential energy "
          "changes among the species in the reaction sequence, which is what connects the heat "
          "measured to the chemistry that produced it."),

 dict(q="Under what condition does the framework say the enthalpy change of the overall "
        "process equals the sum of the enthalpy changes of the individual steps?",
      choices=[
        "At constant pressure",
        "At constant temperature",
        "At constant volume",
        "Only when every step is exothermic",
        "Only when the sequence has exactly two steps"],
      ans=0,
      why="EK 6.9.B.1 attaches that condition to its conclusion in so many words: thus, at "
          "constant pressure, the enthalpy change of the overall process is equal to the sum "
          "of the enthalpy changes of the individual steps."),

 dict(q="A reaction has an enthalpy change of -250 kJ/mol. What is the enthalpy change of the "
        "reverse reaction?",
      choices=[
        "+250 kJ/mol, so the reverse reaction is endothermic",
        "-250 kJ/mol, so the reverse reaction is exothermic",
        "+500 kJ/mol, so the reverse reaction is endothermic",
        "-500 kJ/mol, so the reverse reaction is exothermic",
        "0 kJ/mol, since reversing a reaction cancels its enthalpy change"],
      ans=0,
      why="EK 6.9.B.2 i keeps the magnitude and reverses the mathematical sign, so the "
          "released energy of the forward reaction becomes energy absorbed on the way back, "
          "which EK 6.6.A.1 reads from the positive value."),

 dict(q="A reaction has an enthalpy change of +120 kJ/mol. What is the enthalpy change when "
        "the whole equation is multiplied by 3?",
      choices=[
        "+360 kJ/mol, so it is endothermic",
        "+120 kJ/mol, so it is endothermic",
        "-360 kJ/mol, so it is exothermic",
        "+40 kJ/mol, so it is endothermic",
        "-120 kJ/mol, so it is exothermic"],
      ans=0,
      why="EK 6.9.B.2 ii multiplies the enthalpy change by the same factor the reaction was "
          "multiplied by, and leaves the sign alone, so a positive value stays positive and "
          "EK 6.6.A.1 still reads it as heat energy absorbed."),

 dict(q="Two steps in a sequence have enthalpy changes of -180 kJ/mol and +40 kJ/mol. What is "
        "the enthalpy change of the overall process?",
      choices=[
        "-140 kJ/mol, so the overall process is exothermic",
        "+140 kJ/mol, so the overall process is endothermic",
        "-220 kJ/mol, so the overall process is exothermic",
        "+220 kJ/mol, so the overall process is endothermic",
        "-180 kJ/mol, so the overall process is exothermic"],
      ans=0,
      why="EK 6.9.B.2 iii adds the individual enthalpy changes with their signs, so a positive "
          "step subtracts from a negative one rather than adding to its magnitude."),

 dict(q="A step whose enthalpy change is -300 kJ/mol has to be reversed and also multiplied "
        "by 2 before being added. What does it contribute to the overall enthalpy change?",
      choices=[
        "+600 kJ/mol, so its contribution is endothermic",
        "-600 kJ/mol, so its contribution is exothermic",
        "+300 kJ/mol, so its contribution is endothermic",
        "-300 kJ/mol, so its contribution is exothermic",
        "+1200 kJ/mol, so its contribution is endothermic"],
      ans=0,
      why="EK 6.9.B.2 i reverses the sign and EK 6.9.B.2 ii multiplies the magnitude by the "
          "factor, so both rules act and the contribution is positive and twice the size of "
          "the tabulated change."),

 dict(q="A student writes a step backwards in a sequence but carries its enthalpy change "
        "across unchanged. What is wrong with that?",
      choices=[
        "Reversing a reaction reverses the mathematical sign of its enthalpy change",
        "Reversing a reaction doubles the magnitude of its enthalpy change",
        "Reversing a reaction halves the magnitude of its enthalpy change",
        "Reversing a reaction sets its enthalpy change to zero",
        "Nothing, since an enthalpy change belongs to the substances and not to the direction"],
      ans=0,
      why="EK 6.9.B.2 i is a rule about the sign and only the sign: the magnitude stays "
          "constant but the mathematical sign becomes reversed, so carrying the value across "
          "unchanged reports heat flowing the wrong way."),

 dict(q="For the overall reaction CaO(s) + CO2(g) gives CaCO3(s) , what is the enthalpy change "
        "from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "-178 kJ/mol, so the overall reaction is exothermic",
        "+178 kJ/mol, so the overall reaction is endothermic",
        "-356 kJ/mol, so the overall reaction is exothermic",
        "+356 kJ/mol, so the overall reaction is endothermic",
        "-89 kJ/mol, so the overall reaction is exothermic"],
      ans=0,
      why="The overall reaction is one tabulated step written backwards, so EK 6.9.B.2 i "
          "applies on its own: the magnitude is the tabulated one and the mathematical sign is "
          "reversed. Carrying the sign across unchanged, or doubling or halving the magnitude, "
          "gives the other values offered."),

 dict(q="For the overall reaction 4 H2(g) + 2 O2(g) gives 4 H2O(l) , what is the enthalpy "
        "change from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "-1144 kJ/mol, so the overall reaction is exothermic",
        "-572 kJ/mol, so the overall reaction is exothermic",
        "+1144 kJ/mol, so the overall reaction is endothermic",
        "-2288 kJ/mol, so the overall reaction is exothermic",
        "+572 kJ/mol, so the overall reaction is endothermic"],
      ans=0,
      why="The overall reaction is one tabulated step with every coefficient doubled, so "
          "EK 6.9.B.2 ii applies on its own and multiplies the enthalpy change by the same "
          "factor. Leaving the factor off, applying it twice, or reversing the sign gives the "
          "other values offered."),

 dict(q="For the overall reaction N2(g) + 2 O2(g) gives 2 NO2(g) , what is the enthalpy change "
        "from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "+66 kJ/mol, so the overall reaction is endothermic",
        "-66 kJ/mol, so the overall reaction is exothermic",
        "+294 kJ/mol, so the overall reaction is endothermic",
        "-294 kJ/mol, so the overall reaction is exothermic",
        "+180 kJ/mol, so the overall reaction is endothermic"],
      ans=0,
      why="Two tabulated steps add directly to this overall reaction, so EK 6.9.B.2 iii adds "
          "their enthalpy changes with their signs. Adding the magnitudes instead, or "
          "reporting one step alone, gives the other values offered."),

 dict(q="For the overall reaction 2 C(s) + O2(g) gives 2 CO(g) , what is the enthalpy change "
        "from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "-222 kJ/mol, so the overall reaction is exothermic",
        "+222 kJ/mol, so the overall reaction is endothermic",
        "-1354 kJ/mol, so the overall reaction is exothermic",
        "-960 kJ/mol, so the overall reaction is exothermic",
        "-566 kJ/mol, so the overall reaction is exothermic"],
      ans=0,
      why="Reaching this overall reaction needs one tabulated step doubled and another "
          "reversed, so all three of the framework's principles act at once. Failing to "
          "reverse the second step, or leaving the factor off the first, gives the other "
          "values offered."),

 dict(q="For the overall reaction 2 S(s) + 3 O2(g) gives 2 SO3(g) , what is the enthalpy "
        "change from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "-792 kJ/mol, so the overall reaction is exothermic",
        "+792 kJ/mol, so the overall reaction is endothermic",
        "-495 kJ/mol, so the overall reaction is exothermic",
        "-990 kJ/mol, so the overall reaction is exothermic",
        "-594 kJ/mol, so the overall reaction is exothermic"],
      ans=0,
      why="One tabulated step has to be doubled before the two are added, so EK 6.9.B.2 ii "
          "multiplies that step's enthalpy change by two and EK 6.9.B.2 iii then adds them. "
          "Leaving the factor off, applying it to both steps, or reporting the doubled step "
          "alone gives the other values offered."),

 dict(q="For the overall reaction C(s) + 2 H2(g) gives CH4(g) , what is the enthalpy change "
        "from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "-75 kJ/mol, so the overall reaction is exothermic",
        "+75 kJ/mol, so the overall reaction is endothermic",
        "-1857 kJ/mol, so the overall reaction is exothermic",
        "-966 kJ/mol, so the overall reaction is exothermic",
        "+1857 kJ/mol, so the overall reaction is endothermic"],
      ans=0,
      why="Three tabulated steps are needed and one of them has to be reversed, so "
          "EK 6.9.B.2 i changes that step's sign before EK 6.9.B.2 iii adds all three. "
          "Carrying that step's sign across unchanged, or leaving it out altogether, gives the "
          "other values offered."),

 dict(q="Which tabulated step has to be written backwards in order to reach the overall "
        "reaction C(s) + 2 H2(g) gives CH4(g) ?",
      table=_T_STEPS,
      choices=[
        "Step 9",
        "Step 1",
        "Step 8",
        "Step 2",
        "None of them, since all three are used as written"],
      ans=0,
      why="EK 6.9.B.2 iii adds reactions to obtain an overall reaction, and the substance that "
          "has to end up as a product appears as a reactant in only one of the tabulated "
          "steps, so that step is the one EK 6.9.B.2 i must be applied to."),

 dict(q="Which tabulated step has to be multiplied by two in order to reach the overall "
        "reaction 2 S(s) + 3 O2(g) gives 2 SO3(g) ?",
      table=_T_STEPS,
      choices=[
        "Step 5",
        "Step 6",
        "Step 1",
        "Step 3",
        "Neither of the two steps used, since both are used as written"],
      ans=0,
      why="EK 6.9.B.2 ii multiplies a reaction by a factor so that the species which must "
          "cancel appear in equal amounts on the two sides. Only one of the two steps needed "
          "here is written with too little of that species."),

 dict(q="When the tabulated steps are combined to give the overall reaction 2 C(s) + O2(g) "
        "gives 2 CO(g) , which species disappears entirely?",
      table=_T_STEPS,
      choices=[
        "Carbon dioxide, CO2(g)",
        "Carbon monoxide, CO(g)",
        "Carbon, C(s)",
        "Oxygen, O2(g)",
        "No species disappears; every one of them appears in the overall reaction"],
      ans=0,
      why="EK 6.9.B.2 iii adds the reactions, so a species produced in equal amount by one "
          "step and consumed by another leaves nothing behind in the overall reaction. Oxygen "
          "appears on both sides too but not in equal amounts, so some of it survives."),

 dict(q="What is the enthalpy change of the reverse of tabulated Step 4?",
      table=_T_STEPS,
      choices=[
        "+114 kJ/mol, so the reverse step is endothermic",
        "-114 kJ/mol, so the reverse step is exothermic",
        "+228 kJ/mol, so the reverse step is endothermic",
        "-228 kJ/mol, so the reverse step is exothermic",
        "+57 kJ/mol, so the reverse step is endothermic"],
      ans=0,
      why="EK 6.9.B.2 i keeps the tabulated magnitude and reverses the mathematical sign, so "
          "a step tabulated below zero contributes above zero when it is written backwards."),

 dict(q="For the overall reaction 2 NO2(g) gives N2(g) + 2 O2(g) , what is the enthalpy change "
        "from the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "-66 kJ/mol, so the overall reaction is exothermic",
        "+66 kJ/mol, so the overall reaction is endothermic",
        "-294 kJ/mol, so the overall reaction is exothermic",
        "+294 kJ/mol, so the overall reaction is endothermic",
        "-180 kJ/mol, so the overall reaction is exothermic"],
      ans=0,
      why="Both tabulated steps have to be written backwards here, so EK 6.9.B.2 i reverses "
          "each sign before EK 6.9.B.2 iii adds them. Adding the magnitudes, or reporting one "
          "reversed step alone, gives the other values offered."),

 dict(q="For the overall reaction CO2(g) gives C(s) + O2(g) , what is the enthalpy change from "
        "the tabulated steps?",
      table=_T_STEPS,
      choices=[
        "+394 kJ/mol, so the overall reaction is endothermic",
        "-394 kJ/mol, so the overall reaction is exothermic",
        "+788 kJ/mol, so the overall reaction is endothermic",
        "-788 kJ/mol, so the overall reaction is exothermic",
        "+197 kJ/mol, so the overall reaction is endothermic"],
      ans=0,
      why="The overall reaction is one tabulated step written backwards, so EK 6.9.B.2 i "
          "reverses the sign and leaves the magnitude alone. EK 6.6.A.1 then reads the "
          "positive value as heat energy absorbed."),

 dict(q="A student combines the tabulated steps correctly to reach C(s) + 2 H2(g) gives "
        "CH4(g) , but carries the reversed step's tabulated enthalpy change across unchanged "
        "instead of reversing its sign. By how much does the answer differ from the correct "
        "one?",
      table=_T_STEPS,
      choices=[
        "By 1782 kJ/mol, which is twice that step's enthalpy change",
        "By 891 kJ/mol, which is that step's enthalpy change",
        "By 966 kJ/mol, which is the sum of the other two steps' enthalpy changes",
        "By 75 kJ/mol, which is the size of the correct answer",
        "Not at all, since reversing a reaction leaves its enthalpy change alone"],
      ans=0,
      why="EK 6.9.B.2 i says the sign is reversed, so using the tabulated value instead of its "
          "negative shifts the total by the difference between them, which is twice that "
          "step's enthalpy change rather than once."),

 dict(q="A step has to be both reversed and multiplied by a factor before it is added into a "
        "sequence. Does the order in which those two principles are applied change what the "
        "step contributes?",
      choices=[
        "No, the contribution comes out the same either way",
        "Yes, reversing first gives a contribution of the opposite sign",
        "Yes, multiplying first gives a contribution twice as large",
        "No, because reversing a reaction does not change its enthalpy change at all",
        "It cannot be decided without knowing the factor"],
      ans=0,
      why="EK 6.9.B.2 i changes only the sign and EK 6.9.B.2 ii scales only the magnitude, so "
          "the two act on different parts of the number and neither undoes the other. The "
          "rejected reasons each deny one of the two rules."),

 dict(q="A sequence of three steps has enthalpy changes of -100 kJ/mol, +250 kJ/mol and "
        "-50 kJ/mol. What is the enthalpy change of the overall process?",
      choices=[
        "+100 kJ/mol, so the overall process is endothermic",
        "-100 kJ/mol, so the overall process is exothermic",
        "+400 kJ/mol, so the overall process is endothermic",
        "-400 kJ/mol, so the overall process is exothermic",
        "+250 kJ/mol, so the overall process is endothermic"],
      ans=0,
      why="EK 6.9.B.2 iii adds the individual enthalpy changes with their signs, so the two "
          "negative steps subtract from the positive one. Adding the magnitudes, or keeping "
          "the largest step alone, gives the other values offered."),

 dict(q="How many of the tabulated steps used to reach C(s) + 2 H2(g) gives CH4(g) have to be "
        "written backwards?",
      table=_T_STEPS,
      choices=[
        "Exactly one",
        "None of them",
        "Exactly two",
        "All three",
        "It depends on the order in which they are added"],
      ans=0,
      why="EK 6.9.B.2 iii adds the steps as they stand unless a species has to move from one "
          "side to the other, and only one of the three steps needed here has its substances "
          "on the wrong sides for the overall reaction."),

 dict(q="Two reactions are added to obtain an overall reaction, with one of them reversed "
        "first and the other multiplied by 3. Which of the framework's principles are needed, "
        "and what do they do to the enthalpy changes?",
      choices=[
        "All three: the reversed step's enthalpy change changes sign, the multiplied step's is "
        "tripled, and the two are then added",
        "All three, except that the reversed step's enthalpy change keeps its sign",
        "All three, except that the multiplied step's enthalpy change is left unchanged",
        "Only the addition principle, since reversing and multiplying do not affect an "
        "enthalpy change",
        "Only the reversal principle, since the other two follow from it"],
      ans=0,
      why="EK 6.9.B.2 lists the three principles separately and this combination uses each "
          "once: i on the reversed reaction, ii on the multiplied one, and iii to put the two "
          "together into the net enthalpy change."),
]
