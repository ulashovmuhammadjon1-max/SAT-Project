# AP BIOLOGY 8.1 Responses to the Environment
# CED effective Fall 2025, Unit 8 Ecology. Big Idea 2 Energetics for LO 8.1.A
# and Big Idea 3 Information Storage and Transmission for LO 8.1.B.
# Learning objectives 8.1.A (explain how the behavioral and physiological
# response of an organism is related to changes in internal or external
# environment) and 8.1.B (explain how the behavioral responses of organisms
# affect their overall fitness and may contribute to the success of a
# population).
# Suggested skill 3.C, IDENTIFY EXPERIMENTAL PROCEDURES THAT ALIGN WITH THE
# QUESTION, including (i) identifying dependent and independent variables,
# (ii) identifying appropriate controls, (iii) justifying appropriate controls.
#
# Essential knowledge relied on, in the framework's own terms:
#   8.1.A.1  organisms respond to changes in their environment through
#            BEHAVIORAL AND PHYSIOLOGICAL mechanisms.
#   8.1.A.2  organisms EXCHANGE INFORMATION with one another in response to
#            internal changes and external cues, WHICH CAN CHANGE BEHAVIOR.
#   8.1.B.1  organisms communicate through various mechanisms (VISUAL, AUDIBLE,
#            TACTILE, ELECTRICAL, AND/OR CHEMICAL signals).
#              i. organisms have a variety of signaling behaviors that produce
#                 changes in the behavior of other organisms and can result in
#                 DIFFERENTIAL REPRODUCTIVE SUCCESS.
#             ii. animals use signals to INDICATE DOMINANCE, FIND FOOD,
#                 ESTABLISH TERRITORY, and ENSURE REPRODUCTIVE SUCCESS.
#   8.1.B.2  responses to information and communication of information are
#            VITAL TO NATURAL SELECTION AND EVOLUTION.
#              i. FITNESS FAVORS INNATE AND LEARNED BEHAVIORS that increase
#                 survival and reproductive success.
#             ii. COOPERATIVE BEHAVIOR TENDS TO INCREASE THE FITNESS OF THE
#                 INDIVIDUAL AND THE SURVIVAL OF THE POPULATION.
#
# THREE EXCLUSION STATEMENTS GOVERN THIS TOPIC, and they shape the whole module:
#   * knowledge of specific behavioral or physiological MECHANISMS is beyond the
#     scope of the AP Exam (under EK 8.1.A.1);
#   * knowledge of specific MECHANISMS OF COMMUNICATION is beyond the scope
#     (under EK 8.1.B.1);
#   * the DETAILS of the various communications and community behavioral systems
#     are beyond the scope (under EK 8.1.B.2).
# So NO key here requires a student to know how any particular response or
# signal works. Items classify a described signal by the MODE the framework
# names, or by the USE the framework names, or they ask about experimental
# design, which is what suggested skill 3.C makes this topic's own work.
#
# The CED's illustrative examples -- photoperiodism, taxis and kinesis,
# nocturnal and diurnal activity, territorial marking, bird songs, foraging by
# bees, herd and schooling behavior, kin selection and the rest -- are not
# assessable content, so no key depends on recognising one. Scenarios here are
# written generically for that reason.
#
# DELIBERATE OMISSIONS. Energy strategies for temperature regulation and
# reproduction are EK 8.2.A and are asked in b8_2. Predation, competition and
# symbiosis as community interactions are EK 8.5.B.4 and are asked in b8_5; the
# cooperative-behaviour items here are keyed to EK 8.1.B.2 on fitness and
# population survival, which is a different statement.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: this bank is exported
# untypeset.
TOPIC = ("8.1", "Responses to the Environment", 8)

_T_TRIAL = dict(
    headers=["Group", "Sound presented to the group", "Number of individuals tested",
             "Number that changed their behaviour within one minute"],
    rows=[["Group 1", "A recorded call of the same species", "40", "34"],
          ["Group 2", "A recorded call of a different species", "40", "8"],
          ["Group 3", "No sound", "40", "4"]])

_T_COOP = dict(
    headers=["Foraging condition", "Number of foraging attempts observed",
             "Number of attempts that obtained food"],
    rows=[["Individuals foraging alone", "200", "30"],
          ["Individuals foraging as a group", "200", "96"]])

QUESTIONS = [
 dict(q="According to the course framework, organisms respond to changes in their environment through which kinds of mechanism?",
   choices=["Behavioral and physiological mechanisms", "Geological mechanisms only",
            "Mechanisms that alter the DNA sequence of the individual responding",
            "Mechanisms available only to animals", "Mechanisms that operate only over evolutionary time"], ans=0,
   why="EK 8.1.A.1 states that organisms respond to changes in their environment through behavioral and physiological mechanisms. The statement is about the responding individual and is not restricted to animals or to evolutionary timescales."),

 dict(q="Which of the following best describes what the framework asks a student to know about the behavioral and physiological responses of organisms?",
   choices=[
     "That organisms respond through behavioral and physiological mechanisms, without requiring knowledge of any particular mechanism",
     "The molecular details of each response an organism can make",
     "The name of every hormone involved in every response",
     "That organisms cannot respond to internal changes at all",
     "That every species responds to a given change in exactly the same way"], ans=0,
   why="EK 8.1.A.1 states the general claim and carries an exclusion statement placing knowledge of specific behavioral or physiological mechanisms beyond the scope of the exam. What is assessable is that the two kinds of response exist and are responses to environmental change."),

 dict(q="According to the framework, organisms exchange information with one another in response to what?",
   choices=[
     "Internal changes and external cues",
     "External cues only, since internal states cannot be signalled",
     "Internal changes only, since external cues are not information",
     "Changes in the age of the rocks they inhabit",
     "Nothing, since information exchange occurs at random"], ans=0,
   why="EK 8.1.A.2 states that organisms exchange information with one another in response to internal changes and external cues, which can change behavior. The statement names both sources explicitly."),

 dict(q="What does the framework say can result when organisms exchange information with one another?",
   choices=["A change in behavior", "A change in the DNA sequence of the receiver",
            "An immediate change in the species to which the organisms belong",
            "The formation of a new habitat", "A permanent end to further communication"], ans=0,
   why="EK 8.1.A.2 states that organisms exchange information in response to internal changes and external cues, which can change behavior. Behavior is the outcome the statement names."),

 dict(q="Which list correctly names the kinds of signal through which the framework says organisms communicate?",
   choices=[
     "Visual, audible, tactile, electrical, and chemical",
     "Visual and audible only",
     "Chemical and electrical only",
     "Visual, audible, and geological",
     "Tactile signals only, since all communication requires contact"], ans=0,
   why="EK 8.1.B.1 states that organisms communicate through various mechanisms, naming visual, audible, tactile, electrical and chemical signals. Each of the other options drops kinds the statement includes or adds one it does not."),

 dict(q="One individual releases a substance into the water that another individual of the same species detects, after which the second individual moves away. This exchange is best classified as which kind of signal?",
   choices=["A chemical signal", "A visual signal", "An audible signal",
            "A tactile signal", "An electrical signal"], ans=0,
   why="EK 8.1.B.1 names chemical signals among the kinds through which organisms communicate. A released substance detected by another organism is a chemical signal whatever the detection mechanism, which the topic's exclusion statement places outside the scope."),

 dict(q="An individual raises a brightly coloured structure toward a second individual, which then changes its position. This exchange is best classified as which kind of signal?",
   choices=["A visual signal", "A chemical signal", "An audible signal",
            "A tactile signal", "An electrical signal"], ans=0,
   why="EK 8.1.B.1 names visual signals among the kinds through which organisms communicate. A display that must be seen to have its effect is a visual signal."),

 dict(q="An individual produces a repeated sound to which nearby individuals respond by approaching. This exchange is best classified as which kind of signal?",
   choices=["An audible signal", "A visual signal", "A chemical signal",
            "A tactile signal", "An electrical signal"], ans=0,
   why="EK 8.1.B.1 names audible signals among the kinds through which organisms communicate. A produced sound that changes the behaviour of those who hear it is an audible signal."),

 dict(q="An individual makes physical contact with another in a patterned way, and the second individual then follows it. This exchange is best classified as which kind of signal?",
   choices=["A tactile signal", "A chemical signal", "An audible signal",
            "A visual signal", "An electrical signal"], ans=0,
   why="EK 8.1.B.1 names tactile signals among the kinds through which organisms communicate. Patterned physical contact that changes the receiver's behaviour is a tactile signal."),

 dict(q="An aquatic organism generates a weak field that a second organism detects without any contact, sound or released substance. This exchange is best classified as which kind of signal?",
   choices=["An electrical signal", "A chemical signal", "A tactile signal",
            "An audible signal", "A visual signal"], ans=0,
   why="EK 8.1.B.1 names electrical signals among the kinds through which organisms communicate, and the scenario excludes each of the other four kinds by description. How the field is generated or detected is beyond the topic's scope by its own exclusion statement."),

 dict(q="According to the framework, what can the signaling behaviors of organisms result in?",
   choices=[
     "Changes in the behavior of other organisms and differential reproductive success",
     "Changes in the DNA sequence of the organism giving the signal",
     "An end to natural selection in the population",
     "A change in the physical boundaries of the habitat",
     "Identical reproductive success for every individual in the population"], ans=0,
   why="EK 8.1.B.1 states that organisms have a variety of signaling behaviors that produce changes in the behavior of other organisms and can result in differential reproductive success. Differential means unequal, which is the opposite of the last option."),

 dict(q="An individual performs a display in the presence of a rival, after which the rival withdraws and the displaying individual retains access to a feeding site. Which of the framework's named uses of signals does this best illustrate?",
   choices=["Indicating dominance", "Finding food", "Establishing territory",
            "Ensuring reproductive success", "Responding to an internal change with no signal"], ans=0,
   why="EK 8.1.B.1 states that animals use signals to indicate dominance, find food, establish territory, and ensure reproductive success. A display that causes a rival to withdraw in a contest over access is the first of those four."),

 dict(q="Individuals that have located a food source signal in a way that leads others of their group to the same source. Which of the framework's named uses of signals does this best illustrate?",
   choices=["Finding food", "Indicating dominance", "Establishing territory",
            "Ensuring reproductive success", "Responding to an external cue with no signal"], ans=0,
   why="EK 8.1.B.1 names finding food among the four uses animals make of signals. The signal changes the behaviour of the receivers so that they reach the resource, which is EK 8.1.B.1's first sub-point in action."),

 dict(q="An individual repeatedly signals at the edges of an area it occupies, and other individuals of the same species avoid entering that area. Which of the framework's named uses of signals does this best illustrate?",
   choices=["Establishing territory", "Finding food", "Indicating dominance",
            "Ensuring reproductive success", "Exchanging information about internal changes only"], ans=0,
   why="EK 8.1.B.1 names establishing territory among the four uses animals make of signals. A signal at the boundary of an occupied area that keeps others out is that use."),

 dict(q="Individuals signal in a way that attracts mates, and those that signal more effectively leave more offspring. Which two statements of the framework does this best illustrate together?",
   choices=[
     "That animals use signals to ensure reproductive success, and that signaling behaviors can result in differential reproductive success",
     "That animals use signals only to establish territory, and that signaling has no effect on reproduction",
     "That signals change the DNA of the receiver, and that reproduction is unaffected",
     "That cooperative behaviour reduces the fitness of the individual, and that signalling prevents it",
     "That responses to information are unrelated to natural selection"], ans=0,
   why="EK 8.1.B.1 names ensuring reproductive success among the four uses of signals and separately states that signaling behaviors can result in differential reproductive success. The scenario reports both: a use and an unequal outcome."),

 dict(q="Which of the following is NOT among the uses of signals the framework lists for animals?",
   choices=[
     "Changing the season in which a habitat receives rainfall",
     "Indicating dominance",
     "Finding food",
     "Establishing territory",
     "Ensuring reproductive success"], ans=0,
   why="EK 8.1.B.1 lists exactly four uses: indicating dominance, finding food, establishing territory and ensuring reproductive success. Altering the climate of a habitat is not among them and is not something a signal between organisms does."),

 dict(q="According to the framework, responses to information and the communication of information are vital to what?",
   choices=["Natural selection and evolution", "The formation of rock layers",
            "The chemical composition of the atmosphere", "The rate at which a habitat erodes",
            "The number of chromosomes an organism carries"], ans=0,
   why="EK 8.1.B.2 states that responses to information and communication of information are vital to natural selection and evolution. Behaviour affects survival and reproduction, which is what selection acts through."),

 dict(q="According to the framework, which behaviors does fitness favor?",
   choices=[
     "Innate and learned behaviors that increase survival and reproductive success",
     "Innate behaviors only, since learned behaviors are not inherited",
     "Learned behaviors only, since innate behaviors cannot change",
     "Behaviors that increase survival but reduce reproduction",
     "Behaviors that have no effect on survival or reproduction"], ans=0,
   why="EK 8.1.B.2 states that fitness favors innate and learned behaviors that increase survival and reproductive success. The statement names both kinds of behavior and both outcomes."),

 dict(q="Two behaviors in a population raise survival and reproductive success by the same amount, but one appears without any experience and the other is acquired through experience. What does the framework's account say about how fitness treats them?",
   choices=[
     "Fitness favors both, because the statement names innate and learned behaviors alike",
     "Fitness favors only the one that appears without experience",
     "Fitness favors only the one acquired through experience",
     "Fitness favors neither, because behavior is not heritable",
     "Fitness favors whichever behavior appears first in the lifetime of the individual"], ans=0,
   why="EK 8.1.B.2 states that fitness favors innate AND learned behaviors that increase survival and reproductive success. The statement distinguishes the two kinds and then treats them alike with respect to what fitness favours."),

 dict(q="According to the framework, cooperative behavior tends to increase which of the following?",
   choices=[
     "The fitness of the individual and the survival of the population",
     "The fitness of the individual only, at the expense of the population",
     "The survival of the population only, at the expense of every individual",
     "The mutation rate of the population",
     "Neither individual fitness nor population survival"], ans=0,
   why="EK 8.1.B.2 states that cooperative behavior tends to increase the fitness of the individual AND the survival of the population. The statement joins the two outcomes rather than trading one against the other."),

 dict(q="The table reports an experiment in which three groups of the same species were exposed to different sounds and observed. Which group serves as the control?",
   table=_T_TRIAL,
   choices=["Group 3", "Group 1", "Group 2", "All three groups equally",
            "The experiment includes no control group"], ans=0,
   why="Skill 3.C includes identifying appropriate controls. A control receives no treatment on the variable being manipulated, so the group presented with no sound is what the responses of the other two groups are measured against."),

 dict(q="In that same three-group experiment, what is the independent variable?",
   table=_T_TRIAL,
   choices=[
     "The kind of sound presented to each group",
     "The number of individuals that changed their behaviour",
     "The number of individuals tested in each group",
     "The time allowed for a response",
     "The species used in the experiment"], ans=0,
   why="Skill 3.C includes identifying dependent and independent variables. The independent variable is the one the investigator sets differently across groups, and the table shows exactly one column that differs from group to group by design."),

 dict(q="In that same three-group experiment, what is the dependent variable?",
   table=_T_TRIAL,
   choices=[
     "The number of individuals that changed their behaviour",
     "The kind of sound presented to each group",
     "The number of individuals tested in each group",
     "The species used in the experiment",
     "The order in which the groups were tested"], ans=0,
   why="Skill 3.C includes identifying dependent and independent variables. The dependent variable is what is measured as an outcome, and the table's final column records that outcome while the number tested is held constant."),

 dict(q="What percentage of the individuals presented with a recorded call of the same species changed their behaviour?",
   table=_T_TRIAL,
   choices=["85 percent", "20 percent", "10 percent", "34 percent", "40 percent"], ans=0,
   why="Skill 5.A includes percentages. The row the stem names supplies both a number tested and a number that responded, and the percentage is the second divided by the first."),

 dict(q="Which conclusion do the results of that three-group experiment best support?",
   table=_T_TRIAL,
   choices=[
     "The recorded call of the same species changed behaviour far more often than either the other call or silence",
     "Any sound at all produces the same change in behaviour",
     "The individuals responded to the number of others present rather than to sound",
     "Silence changed behaviour more often than either recorded call",
     "The three groups responded at the same rate"], ans=0,
   why="EK 8.1.A.2 states that organisms exchange information in response to external cues and that this can change behavior. The comparison the design supports is between the treatments, and the table records one treatment producing a much larger response than the control or the other treatment."),

 dict(q="The table reports foraging attempts by individuals of one species alone and in a group. What percentage of the attempts made by individuals foraging alone obtained food?",
   table=_T_COOP,
   choices=["15 percent", "48 percent", "30 percent", "33 percent", "96 percent"], ans=0,
   why="Skill 5.A includes percentages. The row the stem names supplies a number of attempts and a number that obtained food, and the percentage is the second divided by the first."),

 dict(q="Using the same foraging data, by how many percentage points does the success of group foraging exceed the success of foraging alone?",
   table=_T_COOP,
   choices=["33 percentage points", "66 percentage points", "48 percentage points",
            "15 percentage points", "30 percentage points"], ans=0,
   why="Skill 5.A includes percentages and percent changes. Each row yields a success percentage from its own two counts, and the answer is the difference between the two percentages."),

 dict(q="Which statement of the framework do those foraging results most directly illustrate?",
   table=_T_COOP,
   choices=[
     "Cooperative behavior tends to increase the fitness of the individual and the survival of the population",
     "Organisms communicate through electrical signals",
     "Fitness favors only innate behaviors",
     "Signals are used to indicate dominance",
     "Responses to information are unrelated to natural selection"], ans=0,
   why="EK 8.1.B.2 states that cooperative behavior tends to increase the fitness of the individual and the survival of the population. Individuals in the group obtained food on a far larger share of their attempts, which is an individual benefit from acting together."),

 dict(q="A colleague objects that the foraging comparison does not show that grouping caused the higher success. Which additional feature of the design would best answer that objection?",
   choices=[
     "Assigning comparable individuals at random to forage alone or in a group, at the same sites and times",
     "Observing more attempts by individuals foraging in groups only",
     "Observing the same individuals only when they choose to forage in groups",
     "Reporting the raw counts instead of the percentages",
     "Observing a second species instead of the first"], ans=0,
   why="Skill 3.C includes justifying appropriate controls. Individuals that choose to forage together may differ from those that do not, and the sites and times may differ too, so only assignment that breaks those links leaves grouping as the difference between the conditions."),

 dict(q="Why is a group presented with no sound at all a better comparison than a group presented with a quieter version of the same call?",
   choices=[
     "It shows how often the behaviour occurs when the manipulated variable is absent entirely",
     "It guarantees that the individuals will not respond",
     "It removes the need to count how many individuals were tested",
     "It makes the independent and dependent variables the same",
     "It shows that quieter sounds are more informative than louder ones"], ans=0,
   why="Skill 3.C includes justifying appropriate controls. A control establishes the baseline rate of the measured behaviour when the treatment is absent, and a quieter version of the same call is a smaller dose of the treatment rather than its absence."),
]
