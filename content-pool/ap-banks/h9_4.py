# AP CHEMISTRY 9.4 Thermodynamic and Kinetic Control
# CED effective Fall 2024, Unit 9 Thermodynamics and Electrochemistry.
# Learning objective 9.4.A: explain, in terms of kinetics, why a thermodynamically
# favored reaction might not occur at a measurable rate.
# Suggested skill 6.E, provide reasoning to justify a claim using connections between
# particulate and macroscopic scales or levels.
#
# Essential knowledge relied on, in the framework's own words:
#   9.4.A.1  Many processes that are thermodynamically favored do not occur to any
#            measurable extent, or they occur at extremely slow rates.
#   9.4.A.2  Processes that are thermodynamically favored, but do not proceed at a
#            measurable rate, are under "kinetic control". High activation energy is a
#            common reason for a process to be under kinetic control. The fact that a
#            process does not proceed at a noticeable rate does not mean that the
#            chemical system is at equilibrium. If a process is known to be
#            thermodynamically favored, and yet does not occur at a measurable rate, it
#            is reasonable to conclude that the process is under kinetic control.
#
# THE WHOLE TOPIC IS TWO SENTENCES, so the variety below comes from asking them of
# different situations rather than from adding content the framework does not carry.
# Nothing here asserts a rate law, an order, a collision model or a catalyst: Unit 5
# owns all of those, and verify_h9_4.py asserts that none of them appears.
#
# THE PRECONDITION IS THE DEFECT TO GUARD AGAINST. "Under kinetic control" is defined by
# EK 9.4.A.2 only for a process that IS thermodynamically favored, so a process showing
# no change because it is UNFAVORED is not under kinetic control. An item that keyed a
# positive free energy change as kinetic control would read plausibly and be wrong, and
# verify_h9_4.py recomputes that precondition from every tabulated row.
#
# NO FIGURES. Every stimulus is a table or is stated in the stem.
#
# NOTATION. This topic needs no math spans except where a free energy value is quoted.
TOPIC = ("9.4", "Thermodynamic and Kinetic Control", 9)

_GCOL = "Standard free energy change, kJ/mol"

_T_OBS = dict(
    headers=["Process", _GCOL, "Change observed after one hour at 298 K"],
    rows=[["1", "-210.0", "none detectable"],
          ["2", "-95.0", "substantial"],
          ["3", "+130.0", "none detectable"],
          ["4", "-58.0", "none detectable"]])

_T_EA = dict(
    headers=["Reaction", _GCOL, "Activation energy, kJ/mol"],
    rows=[["W", "-150.0", "250.0"],
          ["X", "-150.0", "35.0"],
          ["Y", "+80.0", "40.0"],
          ["Z", "-20.0", "30.0"]])

QUESTIONS = [

 dict(q="What name does the framework give to a process that is thermodynamically favored "
        "but does not proceed at a measurable rate?",
      choices=[
        "It is said to be under kinetic control",
        "It is said to be at equilibrium",
        "It is said to be thermodynamically unfavored after all",
        "It is said to be under thermodynamic control",
        "It is said to have no activation energy"],
      ans=0,
      why="EK 9.4.A.2 says in so many words that processes which are thermodynamically "
          "favored but do not proceed at a measurable rate are under kinetic control. The "
          "same statement denies that a process failing to proceed is at equilibrium."),

 dict(q="What does the framework name as a common reason for a process to be under "
        "kinetic control?",
      choices=[
        "A high activation energy",
        "A standard free energy change close to zero",
        "A low concentration of every reactant",
        "The absence of any product at the start",
        "A positive standard free energy change"],
      ans=0,
      why="EK 9.4.A.2 states that high activation energy is a common reason for a process "
          "to be under kinetic control. A positive free energy change would make the "
          "process unfavored instead, which is a different situation altogether."),

 dict(q="A mixture of reactants shows no detectable change over several days. Does that "
        "establish that the chemical system is at equilibrium?",
      choices=[
        "No, the framework states that failing to proceed at a noticeable rate does not "
        "mean the system is at equilibrium",
        "Yes, an unchanging composition is what equilibrium means",
        "Yes, provided the temperature has been held constant throughout",
        "No, because equilibrium can never be reached in a closed container",
        "Only if the standard free energy change is known to be positive"],
      ans=0,
      why="EK 9.4.A.2 says directly that the fact that a process does not proceed at a "
          "noticeable rate does not mean that the chemical system is at equilibrium. An "
          "unchanging composition can equally mean the process is under kinetic control."),

 dict(q="A process is known to be thermodynamically favored and yet does not occur at a "
        "measurable rate. What does the framework say it is reasonable to conclude?",
      choices=[
        "That the process is under kinetic control",
        "That the free energy change was calculated incorrectly",
        "That the system has already reached equilibrium",
        "That the process is thermodynamically unfavored at that temperature",
        "That no reaction between those substances is possible"],
      ans=0,
      why="EK 9.4.A.2 closes with exactly that inference: if a process is known to be "
          "thermodynamically favored, and yet does not occur at a measurable rate, it is "
          "reasonable to conclude that the process is under kinetic control."),

 dict(q="What does the framework say about the number of thermodynamically favored "
        "processes that fail to be observed?",
      choices=[
        "Many do not occur to any measurable extent, or occur at extremely slow rates",
        "A few rare cases exist, and all of them involve gases",
        "None, since a favored process always occurs once the reactants are mixed",
        "Only those whose free energy change is very close to zero",
        "Only those carried out below room temperature"],
      ans=0,
      why="EK 9.4.A.1 opens the topic by saying that MANY processes that are "
          "thermodynamically favored do not occur to any measurable extent, or they occur "
          "at extremely slow rates, which is why the topic exists at all."),

 dict(q="Does a negative standard free energy change tell you how quickly a process will "
        "occur?",
      choices=[
        "No, a favored process may still occur at an extremely slow rate",
        "Yes, the more negative the value the faster the process",
        "Yes, any negative value guarantees a measurable rate",
        "No, because a negative value means the process cannot occur",
        "Only when the value is more negative than 100 kJ/mol"],
      ans=0,
      why="EK 9.4.A.1 states that many thermodynamically favored processes do not occur to "
          "any measurable extent or occur at extremely slow rates, so favorability and "
          "speed are separate questions and the size of the free energy change settles "
          "only the first of them."),

 dict(q="A process has a standard free energy change of \\( -210.0 \\) kJ/mol and shows no "
        "detectable change after an hour. Which conclusion does the framework support?",
      choices=[
        "The process is thermodynamically favored and under kinetic control",
        "The process is at equilibrium, since nothing is changing",
        "The reported free energy change must be wrong",
        "The process is thermodynamically unfavored despite the reported value",
        "The process will never occur under any conditions"],
      ans=0,
      why="EK 9.4.A.2's closing inference applies exactly here: the process is known to be "
          "favored, since its free energy change is below zero, and it does not occur at a "
          "measurable rate, so it is reasonable to conclude kinetic control. The same "
          "statement forbids reading the absence of change as equilibrium."),

 dict(q="The table gives four processes with their standard free energy changes and what "
        "was observed. Which processes are under kinetic control?",
      table=_T_OBS,
      choices=[
        "Processes 1 and 4, which are favored yet show no detectable change",
        "Processes 1, 3 and 4, which all show no detectable change",
        "Process 3 alone, because nothing is happening to it",
        "Process 2 alone, because it is the one that is changing",
        "None of them, since kinetic control cannot be told from such data"],
      ans=0,
      why="EK 9.4.A.2 defines kinetic control for processes that are thermodynamically "
          "favored but do not proceed at a measurable rate, so both conditions must hold. "
          "The tabulated process with a positive free energy change fails the first "
          "condition however little it changes."),

 dict(q="Using the same table, which process is both thermodynamically favored and "
        "proceeding at a measurable rate?",
      table=_T_OBS,
      choices=["Process 2", "Process 1", "Process 3", "Process 4",
               "Processes 1 and 2 together"],
      ans=0,
      why="EK 9.3.A.2 makes a free energy change below zero the mark of a favored process, "
          "and exactly one tabulated row pairs such a value with a substantial observed "
          "change, so that row is neither unfavored nor under kinetic control."),

 dict(q="Using the tabulated data once more, for which process is the absence of change "
        "explained by thermodynamics rather than by kinetics?",
      table=_T_OBS,
      choices=["Process 3", "Process 1", "Process 4", "Process 2",
               "Processes 1 and 4 together"],
      ans=0,
      why="Exactly one tabulated process has a free energy change above zero, so it is not "
          "thermodynamically favored and there is nothing for kinetics to explain. EK "
          "9.4.A.2 reserves kinetic control for processes that are favored."),

 dict(q="Which tabulated process cannot be under kinetic control whatever its activation "
        "energy turns out to be, and why?",
      table=_T_OBS,
      choices=[
        "Process 3, because kinetic control is defined only for a favored process",
        "Process 2, because it is already proceeding quickly",
        "Process 1, because its free energy change is the most negative",
        "Process 4, because its free energy change is the least negative",
        "None of them, because any process may be under kinetic control"],
      ans=0,
      why="EK 9.4.A.2 defines kinetic control for processes that are thermodynamically "
          "favored but do not proceed at a measurable rate, so a process whose free "
          "energy change is above zero is excluded by the definition itself, not by any "
          "fact about its activation energy."),

 dict(q="The table gives four reactions with their standard free energy changes and "
        "activation energies. Which is most likely to be under kinetic control?",
      table=_T_EA,
      choices=["Reaction W", "Reaction X", "Reaction Y", "Reaction Z",
               "Reactions W and Y equally"],
      ans=0,
      why="EK 9.4.A.2 names high activation energy as a common reason for kinetic "
          "control, and EK 9.4.A.2 restricts kinetic control to favored processes, so the "
          "reaction wanted is the one that is favored AND carries much the largest "
          "activation energy."),

 dict(q="Using the same table of free energy changes and activation energies, which "
        "reaction is not thermodynamically favored?",
      table=_T_EA,
      choices=["Reaction Y", "Reaction W", "Reaction X", "Reaction Z",
               "Reactions W and Y together"],
      ans=0,
      why="EK 9.3.A.2 makes a standard free energy change above zero the mark of a process "
          "that is not thermodynamically favored, and exactly one tabulated reaction has "
          "such a value. Its modest activation energy does not change that."),

 dict(q="Two of the tabulated reactions have the same standard free energy change but "
        "behave very differently. What accounts for the difference?",
      table=_T_EA,
      choices=[
        "Their activation energies differ, and a high one is a common reason for kinetic "
        "control",
        "Their free energy changes must in fact differ, since the behaviour differs",
        "One of them has reached equilibrium and the other has not",
        "One of them is thermodynamically favored and the other is not",
        "The difference cannot be accounted for from the tabulated information"],
      ans=0,
      why="EK 9.4.A.1 allows two equally favored processes to differ entirely in whether "
          "they are observed, and EK 9.4.A.2 names high activation energy as the common "
          "reason. The two tabulated reactions share a free energy change and differ only "
          "in activation energy."),

 dict(q="A student sees no change in a reaction mixture for a week and concludes that the "
        "mixture must be at equilibrium. What is wrong with the conclusion?",
      choices=[
        "The mixture may instead be a favored process held up by a high activation energy",
        "Nothing is wrong: an unchanging mixture is at equilibrium by definition",
        "The conclusion is wrong because equilibrium requires equal concentrations",
        "The conclusion is wrong because a week is not long enough to judge",
        "The conclusion is wrong because equilibrium applies only to gases"],
      ans=0,
      why="EK 9.4.A.2 states that the fact that a process does not proceed at a noticeable "
          "rate does not mean that the chemical system is at equilibrium, and names high "
          "activation energy as the common alternative explanation."),

 dict(q="A student sees that a reaction is extremely slow and concludes that it must be "
        "thermodynamically unfavored. What is wrong with the conclusion?",
      choices=[
        "Many thermodynamically favored processes occur at extremely slow rates",
        "Nothing is wrong: a slow reaction is an unfavored reaction",
        "The conclusion is wrong because every reaction is favored in one direction",
        "The conclusion is wrong because rates cannot be measured at all",
        "The conclusion is wrong only if a product has already appeared"],
      ans=0,
      why="EK 9.4.A.1 says that many processes that are thermodynamically favored do not "
          "occur to any measurable extent, or occur at extremely slow rates, so slowness "
          "is no evidence at all about favorability."),

 dict(q="What must already be known about a process before it can properly be described as "
        "under kinetic control?",
      choices=[
        "That it is thermodynamically favored",
        "That its activation energy has been measured",
        "That it has reached equilibrium",
        "That it involves at least one gas",
        "That its standard free energy change is above zero"],
      ans=0,
      why="EK 9.4.A.2 defines kinetic control for processes that are thermodynamically "
          "favored but do not proceed at a measurable rate, so favorability is part of "
          "the definition. The framework's inference names a high activation energy as a "
          "likely explanation rather than as a prior requirement."),

 dict(q="Which statement about a thermodynamically favored process does the framework "
        "support?",
      choices=[
        "It may occur at a rate too slow to measure",
        "It must occur quickly once the reactants are combined",
        "It must reach equilibrium within a measurable time",
        "It must have a low activation energy",
        "It cannot be described as being under kinetic control"],
      ans=0,
      why="EK 9.4.A.1 states that many thermodynamically favored processes do not occur to "
          "any measurable extent or occur at extremely slow rates, and EK 9.4.A.2 gives "
          "such a process the name kinetic control rather than excluding it."),

 dict(q="Which explanation does the framework offer, in terms of kinetics, for a favored "
        "reaction that is not observed to occur?",
      choices=[
        "A high activation energy commonly holds such a reaction up",
        "The reactants must have been impure",
        "The free energy change must have been measured under the wrong conditions",
        "The reaction has already gone to completion unnoticed",
        "The products are less stable than the reactants after all"],
      ans=0,
      why="Learning objective 9.4.A asks for exactly this explanation in terms of "
          "kinetics, and EK 9.4.A.2 supplies it: high activation energy is a common "
          "reason for a process to be under kinetic control."),

 dict(q="Which pair of questions does this topic treat as separate questions about any "
        "process?",
      choices=[
        "Whether the process is thermodynamically favored, and whether it proceeds at a "
        "measurable rate",
        "Whether the process is exothermic, and whether it produces a gas",
        "Whether the process is reversible, and whether it involves a solid",
        "Whether the process has been observed, and whether it has been named",
        "Whether the reactants are pure, and whether the products are stable"],
      ans=0,
      why="EK 9.4.A.1 and EK 9.4.A.2 exist precisely because the two questions come apart: "
          "many favored processes are not observed, and the framework gives that "
          "combination its own name rather than treating either answer as settling the "
          "other."),

 dict(q="A process under kinetic control is described. What follows about its standard "
        "free energy change?",
      choices=[
        "It is below zero, because kinetic control is defined for a favored process",
        "It is above zero, because the process is not occurring",
        "It is exactly zero, because nothing is changing",
        "It cannot be inferred from the description",
        "It is below zero, but only if the activation energy is also low"],
      ans=0,
      why="EK 9.4.A.2 defines kinetic control for processes that are thermodynamically "
          "favored but do not proceed at a measurable rate, and EK 9.3.A.2 makes a "
          "favored process one whose standard free energy change is below zero, so the "
          "description carries that consequence with it."),

 dict(q="A process has a standard free energy change of \\( +130.0 \\) kJ/mol and shows no "
        "detectable change. Is it under kinetic control?",
      choices=[
        "No, because it is not thermodynamically favored in the first place",
        "Yes, because it shows no detectable change",
        "Yes, because a positive free energy change implies a high activation energy",
        "Only if its activation energy is also known to be high",
        "Yes, because kinetic control applies to any process that is not observed"],
      ans=0,
      why="EK 9.4.A.2 restricts kinetic control to processes that are thermodynamically "
          "favored, and EK 9.3.A.2 makes a free energy change above zero the mark of one "
          "that is not. The absence of change here is explained without appealing to "
          "kinetics at all."),

 dict(q="What observation would show that a thermodynamically favored process is NOT under "
        "kinetic control?",
      choices=[
        "The process is seen to proceed at a measurable rate",
        "The process shows no detectable change over a long period",
        "The standard free energy change is found to be very negative",
        "The temperature of the system stays constant",
        "The system is found to contain no products at all"],
      ans=0,
      why="EK 9.4.A.2 makes failing to proceed at a measurable rate one of the two "
          "conditions for kinetic control, so a favored process that is observed to "
          "proceed fails that condition. A very negative free energy change speaks only "
          "to the other condition."),

 dict(q="Reaction J is thermodynamically favored and reaction K is not, and neither is "
        "observed to change. Which is under kinetic control?",
      choices=[
        "Reaction J only, since kinetic control requires a favored process",
        "Reaction K only, since it is the one thermodynamics cannot explain",
        "Both, since neither is observed to change",
        "Neither, since neither is observed to change",
        "It cannot be decided without both activation energies"],
      ans=0,
      why="EK 9.4.A.2's definition takes two conditions together: thermodynamically "
          "favored, and not proceeding at a measurable rate. Only the favored reaction "
          "meets both, and the framework's inference is licensed without any measurement "
          "of activation energy."),

 dict(q="Why does the course framework place this topic immediately after the free energy "
        "topics rather than in the kinetics unit?",
      choices=[
        "Because it asks what a favored process does NOT tell you, which needs the free "
        "energy idea first",
        "Because activation energy is introduced for the first time here",
        "Because kinetic control applies only to reactions with a known free energy change "
        "of zero",
        "Because the free energy change is calculated from the activation energy",
        "Because favorability and rate are two names for the same property"],
      ans=0,
      why="Learning objective 9.4.A asks the student to explain, in terms of kinetics, why "
          "a THERMODYNAMICALLY FAVORED reaction might not occur at a measurable rate, so "
          "the free energy idea is the premise of the question. Nothing in EK 9.4.A.1 or "
          "9.4.A.2 computes one quantity from the other."),

 dict(q="Which description matches a process that is thermodynamically favored, has a very "
        "high activation energy, and has been left standing for a year with no change?",
      choices=[
        "A process under kinetic control",
        "A process at equilibrium",
        "A thermodynamically unfavored process",
        "A process whose free energy change must be zero",
        "A process that has already gone to completion"],
      ans=0,
      why="EK 9.4.A.2 gives this exact combination its name: favored, not proceeding at a "
          "measurable rate, and commonly held up by a high activation energy. Its middle "
          "sentence forbids calling the unchanging system an equilibrium."),

 dict(q="Two mixtures are unchanging. One is at equilibrium and the other is under kinetic "
        "control. What distinguishes them?",
      choices=[
        "The one under kinetic control is still thermodynamically favored to change",
        "The one at equilibrium has a positive standard free energy change",
        "The one under kinetic control contains no products at all",
        "The one at equilibrium is the colder of the two",
        "Nothing distinguishes them, since both are unchanging"],
      ans=0,
      why="EK 9.4.A.2 insists that a process failing to proceed at a noticeable rate is "
          "not thereby at equilibrium, and it reserves kinetic control for processes that "
          "ARE thermodynamically favored, so the tendency to change is still present in "
          "one case and not the other."),

 dict(q="Which of these would NOT, on the framework's account, explain why a favored "
        "reaction is not observed to occur?",
      choices=[
        "The reaction has a standard free energy change above zero",
        "The reaction has a very high activation energy",
        "The reaction occurs at an extremely slow rate",
        "The reaction does not occur to any measurable extent",
        "The reaction is under kinetic control"],
      ans=0,
      why="A free energy change above zero would contradict the premise that the reaction "
          "is favored, which EK 9.3.A.2 ties to a value below zero. Every other option is "
          "language EK 9.4.A.1 or EK 9.4.A.2 uses for exactly this situation."),

 dict(q="A chemist reports that a favored reaction has an immeasurably small rate. What "
        "does the framework allow the chemist to conclude, and what does it forbid?",
      choices=[
        "Kinetic control may be concluded; equilibrium may not be",
        "Equilibrium may be concluded; kinetic control may not be",
        "Both conclusions are permitted by the framework",
        "Neither conclusion is permitted without an activation energy",
        "Only that the reported free energy change must be re-measured"],
      ans=0,
      why="EK 9.4.A.2 says it is reasonable to conclude kinetic control in exactly this "
          "case, and in the same statement denies that a process failing to proceed at a "
          "noticeable rate means the system is at equilibrium."),

 dict(q="Which single sentence best states what this topic adds to the free energy topics "
        "before it?",
      choices=[
        "Favorability says whether a process is downhill, not whether it will be seen to "
        "happen",
        "Favorability and speed are two measurements of the same underlying quantity",
        "A favored process is one that has been observed to occur at a measurable rate",
        "An unfavored process may still be observed if its activation energy is low",
        "The free energy change fixes the activation energy of a process"],
      ans=0,
      why="EK 9.4.A.1 and EK 9.4.A.2 together separate the two questions: many favored "
          "processes are not observed at all, and the framework names that case rather "
          "than treating favorability as a prediction about rate. Nothing in the topic "
          "lets an unfavored process become favored through kinetics."),

]
