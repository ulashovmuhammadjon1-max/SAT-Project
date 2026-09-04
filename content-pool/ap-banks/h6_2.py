# AP CHEMISTRY 6.2 Energy Diagrams
# CED effective Fall 2024, Unit 6 Thermochemistry.
# Learning objective 6.2.A: represent a chemical or physical transformation with an energy
# diagram. Suggested skill 3.A, represent chemical phenomena using appropriate graphing
# techniques, including correct scale and units.
#
# Essential knowledge relied on, in the framework's own words:
#   6.2.A.1  A physical or chemical process can be described with an energy diagram that
#            shows the endothermic or exothermic nature of that process.
#
# ONE ESSENTIAL KNOWLEDGE STATEMENT, AND THIS BANK CANNOT DRAW. That is the whole problem
# with this topic, and it is worth stating plainly rather than working around quietly. The
# topic is named after a picture; no question here can show one; and a stem that says "the
# diagram above" with nothing behind it is a defect this project has already shipped once.
#
# WHAT IS ASKED INSTEAD, and why it is the same skill. EK 6.2.A.1 says the diagram SHOWS
# the endothermic or exothermic nature of a process, and what carries that information in
# a drawn diagram is the relative height of the initial and final states. So every item
# below either supplies those two energies in a table and asks what the diagram of that
# process would look like, or states in the stem itself the feature of a diagram being
# discussed -- the axis, its units, its scale, which state is drawn higher. Nothing is
# asked that would require a student to read a value off a picture, and verify_h6_2.py
# asserts both halves of that: no item points at a diagram, and no item mentioning a
# diagram is left without either a table or its own description of what is drawn.
#
# THE DIRECTION IS THE CONTENT. EK 6.2.A.1 gives the diagram exactly one job, and getting
# it backwards -- products drawn above the reactants for an exothermic process -- is the
# only way this topic can lie to a student. So every keyed choice that names a direction
# names the relative height as well, every table item has its energies subtracted in the
# verifier with the SIGN checked, and no item whose key names a direction may be answerable
# from that word alone: a distractor must always offer the same word with a wrong reason.
#
# SCOPE. This is not 5.6. A reaction energy profile carrying a transition state and an
# activation energy belongs to Unit 5 Kinetics, and h5_6.py and h5_10.py own it; EK
# 6.2.A.1 says nothing about a barrier between the two states, and no item here mentions
# one. Within unit 6, 6.1 owns the observation-to-energy link, 6.3 the particle-level
# account, 6.4 the calorimetry arithmetic, and 6.5 to 6.9 everything with the word
# enthalpy in it. verify_h6_2.py asserts all of that against stems, keyed choices and why
# text.
#
# NOTATION. export_units.py does not typeset Chemistry. Nothing here needs a math span:
# energies are plain numbers with kJ/mol written out.
TOPIC = ("6.2", "Energy Diagrams", 6)

_T_STATES = dict(
    headers=["Process", "Energy of the initial state (kJ/mol)",
             "Energy of the final state (kJ/mol)"],
    rows=[["Process 1", "0", "-198"],
          ["Process 2", "0", "57"],
          ["Process 3", "0", "-92"],
          ["Process 4", "0", "180"],
          ["Process 5", "0", "0"]])

_T_PHYSICAL = dict(
    headers=["Physical process for substance J", "Energy before (kJ/mol)",
             "Energy after (kJ/mol)"],
    rows=[["Melting", "0", "9.5"],
          ["Freezing", "0", "-9.5"],
          ["Vaporizing", "0", "31.0"],
          ["Condensing", "0", "-31.0"],
          ["Warming the liquid", "0", "5.2"]])

_T_TWO = dict(
    headers=["Reaction", "Energy of the reactants (kJ/mol)",
             "Energy of the products (kJ/mol)"],
    rows=[["Reaction A", "120", "28"],
          ["Reaction B", "75", "166"],
          ["Reaction C", "40", "40"],
          ["Reaction D", "210", "95"],
          ["Reaction E", "60", "12"]])

QUESTIONS = [

 dict(q="According to the framework, what does an energy diagram of a process show?",
      choices=[
        "The endothermic or exothermic nature of that process",
        "How fast the process reaches completion",
        "How much of each substance is present at the end",
        "The temperature at which the process is carried out",
        "The number of separate steps the process is made of"],
      ans=0,
      why="EK 6.2.A.1 states that a physical or chemical process can be described with an "
          "energy diagram that shows the endothermic or exothermic nature of that "
          "process. That is the job the framework gives the representation."),

 dict(q="Which kinds of process does the framework say can be described with an energy "
        "diagram?",
      choices=[
        "Both physical processes and chemical processes",
        "Chemical processes only",
        "Physical processes only",
        "Only processes that release energy",
        "Only processes carried out at constant temperature"],
      ans=0,
      why="EK 6.2.A.1 opens with the phrase a physical or chemical process, so both are "
          "named and neither is singled out. Nothing in the statement restricts the "
          "representation to one direction of energy change."),

 dict(q="A student draws an energy diagram for an exothermic chemical transformation. "
        "Where should the products be drawn relative to the reactants, and why?",
      choices=[
        "Lower than the reactants, because the energy of the system decreases in an "
        "exothermic process",
        "Higher than the reactants, because an exothermic process stores the released "
        "energy in the products",
        "Higher than the reactants, because the energy of the system decreases in an "
        "exothermic process",
        "At the same height as the reactants, because energy is conserved overall",
        "Lower than the reactants, but only if the process is also a phase change"],
      ans=0,
      why="EK 6.2.A.1 makes the diagram the representation of the endothermic or "
          "exothermic nature of a process, and EK 6.1.A.3 makes an exothermic reaction "
          "one in which the energy of the system decreases, so the final state is drawn "
          "below the initial state."),

 dict(q="A student draws an energy diagram for an endothermic chemical transformation. "
        "Where should the products be drawn relative to the reactants, and why?",
      choices=[
        "Higher than the reactants, because the energy of the system increases in an "
        "endothermic process",
        "Lower than the reactants, because an endothermic process uses up the energy of "
        "the reactants",
        "Lower than the reactants, because the energy of the system increases in an "
        "endothermic process",
        "At the same height as the reactants, because the surroundings supply the energy",
        "Higher than the reactants, but only if the products are gases"],
      ans=0,
      why="EK 6.2.A.1 gives the diagram the job of showing the endothermic or exothermic "
          "nature of the process, and EK 6.1.A.3 makes an endothermic reaction one in "
          "which the energy of the system increases, so the final state is drawn above "
          "the initial state."),

 dict(q="An energy diagram is drawn with the final state at exactly the same height as "
        "the initial state. What does it represent?",
      choices=[
        "A process in which the energy of the system does not change",
        "A process that cannot occur at all",
        "A process that must be a physical change rather than a chemical one",
        "A process whose energy change is too small to draw",
        "A process that occurs in two steps of equal size"],
      ans=0,
      why="EK 6.1.A.3 lists remaining the same alongside decreasing and increasing as an "
          "outcome for the energy of a reacting system, and EK 6.2.A.1 makes the relative "
          "heights of the two states the diagram's report of which outcome occurred."),

 dict(q="A student is setting up the axes for an energy diagram. What must the vertical "
        "axis carry, and in what kind of unit?",
      choices=[
        "Energy, in an energy unit such as kJ/mol",
        "Time, in seconds",
        "Temperature, in degrees Celsius",
        "Concentration, in moles per liter",
        "Mass, in grams"],
      ans=0,
      why="EK 6.2.A.1 calls the representation an ENERGY diagram whose job is to show the "
          "endothermic or exothermic nature of the process, and suggested skill 3.A asks "
          "for appropriate graphing with correct scale and units, so the axis must carry "
          "an energy."),

 dict(q="A student draws two energy diagrams side by side. In the first, a drop of 5 "
        "kJ/mol is drawn the same height as a drop of 200 kJ/mol in the second. What is "
        "wrong with the pair?",
      choices=[
        "The two are not drawn to the same scale, so their energy changes cannot be "
        "compared by eye",
        "Nothing, because only the direction of each change matters",
        "The first diagram should have been drawn upside down",
        "The second diagram should have used a different unit",
        "The two processes cannot both be represented by diagrams"],
      ans=0,
      why="Suggested skill 3.A asks for representations with correct scale, and EK "
          "6.2.A.1 puts the size of the energy change in the height of the step, so two "
          "diagrams drawn on unequal scales report a comparison that is not there."),

 dict(q="A student draws an energy diagram carefully but leaves the vertical axis with no "
        "units marked on it at all. What has been lost?",
      choices=[
        "The size of the energy change, which can no longer be read from the drawing",
        "The direction of the energy change, which can no longer be read from the drawing",
        "Nothing, because an energy diagram never carries numbers",
        "The identity of the substances taking part in the process",
        "The order in which the initial and final states occur"],
      ans=0,
      why="Suggested skill 3.A asks for correct units, and without them the height of the "
          "step has no value attached; the relative position of the two states still "
          "reports the direction EK 6.2.A.1 names, so it is the size and not the "
          "direction that is lost."),

 dict(q="What can still be read from an energy diagram whose vertical axis carries no "
        "numbers?",
      choices=[
        "Whether the process is endothermic or exothermic",
        "By how many kJ/mol the energy of the system changed",
        "How long the process takes to finish",
        "How much of the substance was used",
        "Nothing at all, since an unlabeled diagram carries no information"],
      ans=0,
      why="EK 6.2.A.1 gives the diagram the job of showing the endothermic or exothermic "
          "nature of the process, and that is carried by which of the two states is drawn "
          "higher, which survives the loss of the numbers."),

 dict(q="Five processes have had the energy of their initial and final states measured. "
        "Which one would be drawn with the largest downward step?",
      table=_T_STATES,
      choices=[
        "Process 1",
        "Process 4",
        "Process 3",
        "Process 2",
        "Process 5"],
      ans=0,
      why="EK 6.2.A.1 puts the endothermic or exothermic nature of a process into the "
          "relative heights of its two states, so the process whose final state lies "
          "furthest below its initial state is drawn with the largest downward step."),

 dict(q="Using the same five processes, which two would be drawn with the final state "
        "above the initial state?",
      table=_T_STATES,
      choices=[
        "Process 2 and Process 4",
        "Process 1 and Process 3",
        "Process 1 and Process 5",
        "Process 3 and Process 4",
        "Process 2 and Process 5"],
      ans=0,
      why="EK 6.1.A.3 makes a rise in the energy of the system the endothermic case, and "
          "EK 6.2.A.1 has the diagram report it by placing the final state higher, so the "
          "processes whose measured energy rose are the pair."),

 dict(q="Among the same five, which process would be drawn with the largest upward step?",
      table=_T_STATES,
      choices=[
        "Process 4",
        "Process 2",
        "Process 1",
        "Process 3",
        "Process 5"],
      ans=0,
      why="EK 6.2.A.1 carries the size of the energy change in the height of the step, so "
          "the process whose final state lies furthest above its initial state is drawn "
          "with the largest rise."),

 dict(q="Among the same five, which process would be drawn with its two states at the "
        "same height?",
      table=_T_STATES,
      choices=[
        "Process 5",
        "Process 1",
        "Process 2",
        "Process 3",
        "Process 4"],
      ans=0,
      why="EK 6.1.A.3 allows the energy of a system to remain the same, and EK 6.2.A.1 "
          "has the diagram report that by drawing the final state level with the initial "
          "state, which is what one of the measured processes shows."),

 dict(q="Five processes undergone by one substance have had their energies measured "
        "before and after. Which would be drawn with the largest upward step?",
      table=_T_PHYSICAL,
      choices=[
        "Vaporizing",
        "Melting",
        "Warming the liquid",
        "Condensing",
        "Freezing"],
      ans=0,
      why="EK 6.2.A.1 puts the size and direction of the energy change into the step "
          "between the two states, so the process whose measured energy rose by the most "
          "is drawn with the tallest upward step."),

 dict(q="Among those same five processes for that substance, which would be drawn with "
        "the largest downward step?",
      table=_T_PHYSICAL,
      choices=[
        "Condensing",
        "Freezing",
        "Vaporizing",
        "Melting",
        "Warming the liquid"],
      ans=0,
      why="EK 6.1.A.3 makes a fall in the energy of the system the exothermic case, and "
          "EK 6.2.A.1 draws it as a downward step, so the process whose measured energy "
          "fell by the most gives the deepest one."),

 dict(q="Which of those processes would be drawn as the exact mirror of the diagram for "
        "melting, the same size of step in the opposite direction?",
      table=_T_PHYSICAL,
      choices=[
        "Freezing",
        "Condensing",
        "Vaporizing",
        "Warming the liquid",
        "Melting itself, drawn twice"],
      ans=0,
      why="EK 6.2.A.1 makes the step between the two states the whole content of the "
          "diagram, so the process whose measured energy change is equal in size and "
          "opposite in sign to melting's is the one drawn as its mirror."),

 dict(q="Which of those processes would be drawn with an upward step even though it is "
        "not a change of state at all?",
      table=_T_PHYSICAL,
      choices=[
        "Warming the liquid",
        "Melting",
        "Vaporizing",
        "Freezing",
        "Condensing"],
      ans=0,
      why="EK 6.1.A.2 names the heating of a substance alongside phase changes among the "
          "processes described as endothermic or exothermic, and EK 6.2.A.1 lets any such "
          "process be drawn, so the one measured rise that is not a change of state is "
          "the answer."),

 dict(q="Five reactions have had the energies of their reactants and products measured. "
        "Which would be drawn with the greatest downward step?",
      table=_T_TWO,
      choices=[
        "Reaction D",
        "Reaction A",
        "Reaction E",
        "Reaction B",
        "Reaction C"],
      ans=0,
      why="EK 6.2.A.1 represents the energy change as the step from reactants to "
          "products, so subtracting the two measured energies for each reaction and "
          "taking the largest fall identifies the deepest step."),

 dict(q="Among those same five reactions, which would be drawn with an upward step?",
      table=_T_TWO,
      choices=[
        "Reaction B",
        "Reaction A",
        "Reaction C",
        "Reaction D",
        "Reaction E"],
      ans=0,
      why="EK 6.1.A.3 makes an increase in the energy of the system the endothermic case, "
          "and EK 6.2.A.1 draws it as a rise from reactants to products, so the one "
          "reaction whose products were measured above its reactants is drawn that way."),

 dict(q="Among those same five reactions, in which one would the products be drawn level "
        "with the reactants?",
      table=_T_TWO,
      choices=[
        "Reaction C",
        "Reaction A",
        "Reaction B",
        "Reaction D",
        "Reaction E"],
      ans=0,
      why="EK 6.1.A.3 allows the energy of the system to remain the same, and EK 6.2.A.1 "
          "reports that as two states at the same height, which is what one pair of "
          "measured energies shows."),

 dict(q="Among those same five reactions, which would be drawn with the shallowest "
        "downward step?",
      table=_T_TWO,
      choices=[
        "Reaction E",
        "Reaction A",
        "Reaction D",
        "Reaction B",
        "Reaction C"],
      ans=0,
      why="EK 6.2.A.1 puts the size of the energy change into the height of the step, so "
          "among the reactions whose products were measured below their reactants, the "
          "smallest measured fall is drawn as the shallowest step."),

 dict(q="Two students draw energy diagrams for the same exothermic reaction. One places "
        "the products 60 kJ/mol below the reactants and the other places them 60 kJ/mol "
        "above. Which drawing is correct?",
      choices=[
        "The one with the products below, because the energy of the system decreases in "
        "an exothermic reaction",
        "The one with the products above, because an exothermic reaction gives its energy "
        "to the products",
        "The one with the products above, because the energy of the system decreases in "
        "an exothermic reaction",
        "Either, because a diagram may be drawn either way up",
        "Neither, because 60 kJ/mol is too small a change to draw"],
      ans=0,
      why="EK 6.1.A.3 makes an exothermic reaction one in which the energy of the system "
          "decreases, and EK 6.2.A.1 makes the diagram the representation of exactly that "
          "nature, so the final state belongs below the initial state."),

 dict(q="An energy diagram for the dissolving of a salt places the solution above the "
        "separate solid and water. What does the drawing represent?",
      choices=[
        "An endothermic dissolution, in which the energy of the system increases",
        "An exothermic dissolution, in which the energy of the system increases",
        "An endothermic dissolution, in which the energy of the system decreases",
        "A dissolution that cannot occur, since a solution always lies lower",
        "A dissolution in which no energy is exchanged with the surroundings"],
      ans=0,
      why="EK 6.1.A.4 allows the formation of a solution to be endothermic or exothermic, "
          "and EK 6.2.A.1 has the diagram report which by the relative heights, so a "
          "solution drawn higher is the endothermic case."),

 dict(q="A student labels the horizontal axis of an energy diagram Energy and the "
        "vertical axis Progress of the process. What is wrong?",
      choices=[
        "The two axes have been exchanged; the energy belongs on the vertical axis",
        "Nothing, because either axis may carry the energy",
        "The horizontal axis should carry the temperature instead",
        "The vertical axis should have been left unlabeled",
        "The diagram should have had only one axis"],
      ans=0,
      why="EK 6.2.A.1 makes the endothermic or exothermic nature visible as the relative "
          "HEIGHT of the two states, which requires the energy to run up the page, and "
          "suggested skill 3.A asks for correct axes, scale and units."),

 dict(q="A physical process is represented by an energy diagram whose final state lies "
        "below its initial state. What follows?",
      choices=[
        "The process is exothermic, so energy passes from the system to the surroundings",
        "The process is exothermic, so energy passes from the surroundings to the system",
        "The process is endothermic, so energy passes from the system to the surroundings",
        "The process must be a chemical change rather than a physical one",
        "The process cannot be represented this way, since only reactions can be"],
      ans=0,
      why="EK 6.2.A.1 covers physical as well as chemical processes, EK 6.1.A.3 makes a "
          "fall in the energy of the system exothermic, and the same statement sends the "
          "energy the system loses to the surroundings."),

 dict(q="Which feature of a drawn energy diagram carries the information the framework "
        "says the diagram exists to show?",
      choices=[
        "The relative heights of the initial and final states",
        "The height of the initial state above the bottom of the axis",
        "The horizontal distance between the initial and final states",
        "The number of tick marks placed on the vertical axis",
        "The thickness of the line used to draw each state"],
      ans=0,
      why="EK 6.2.A.1 says the diagram shows the endothermic or exothermic nature of the "
          "process, which is a matter of whether the energy of the system rose or fell, "
          "so it is the two states' positions relative to each other that carry it."),

 dict(q="A student draws an energy diagram for a chemical transformation and marks the "
        "initial state at 0 kJ/mol rather than at a measured value. Is that acceptable?",
      choices=[
        "Yes, because the endothermic or exothermic nature depends on the difference "
        "between the two states",
        "No, because the initial state must always be drawn at a positive energy",
        "No, because a diagram with a zero on it cannot be drawn to scale",
        "Yes, but only for a physical process rather than a chemical one",
        "Yes, but only if the final state is also marked at zero"],
      ans=0,
      why="EK 6.2.A.1 gives the diagram the job of showing whether the process is "
          "endothermic or exothermic, and EK 6.1.A.3 settles that by whether the energy "
          "of the system rose or fell, which is a difference and not an absolute height."),

 dict(q="A student labels the vertical axis of an energy diagram in degrees Celsius. Why "
        "can the diagram no longer do what the framework asks of it?",
      choices=[
        "Because the axis must carry an energy, and a temperature is a different quantity",
        "Because degrees Celsius may not be used anywhere in chemistry",
        "Because the axis must carry a mass instead",
        "Because temperature always falls during a chemical process",
        "Because a temperature axis would make every process look exothermic"],
      ans=0,
      why="EK 6.2.A.1 calls for an energy diagram, and EK 6.1.A.1 makes a temperature "
          "change an INDICATOR of an energy change rather than the energy itself, so an "
          "axis in degrees is not the axis the representation calls for."),

 dict(q="Two energy diagrams for two different reactions are drawn on the same scale and "
        "in the same units. Which comparison between them is legitimate?",
      choices=[
        "Which reaction changes the energy of the system by the greater amount",
        "Which reaction reaches completion sooner",
        "Which reaction uses the greater mass of reactant",
        "Which reaction takes place at the higher temperature",
        "Which reaction produces the greater number of products"],
      ans=0,
      why="EK 6.2.A.1 puts the endothermic or exothermic nature and, with a scale, the "
          "size of the energy change into the step between the two states, and suggested "
          "skill 3.A makes a shared correct scale what allows two such steps to be "
          "compared."),

 dict(q="A chemical process and a physical process are each represented by an energy "
        "diagram whose final state is drawn above its initial state. What do the two "
        "drawings have in common?",
      choices=[
        "Both represent endothermic processes, in which the energy of the system "
        "increases",
        "Both represent exothermic processes, in which the energy of the system increases",
        "Both represent endothermic processes, in which the energy of the system "
        "decreases",
        "Both must represent the same process drawn twice",
        "Nothing, since a physical and a chemical process cannot be compared"],
      ans=0,
      why="EK 6.2.A.1 covers a physical OR chemical process with the same representation, "
          "and EK 6.1.A.3 makes a rise in the energy of the system the endothermic case, "
          "so the two drawings report the same direction for different kinds of change."),
]
