# AP ENVIRONMENTAL SCIENCE 2.6 Adaptations
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: ecosystems have structure and diversity that change over
# time.
# Learning objective ERT-2.H: explain how populations respond to changes in their
# environment. Suggested skill 5.B, describe relationships among variables in data
# represented.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.H.1  Natural selection acts on heritable traits, causing populations to adapt to
#              their environment over generations via incremental changes at the genetic
#              level.
#   ERT-2.H.2  Environmental changes, either sudden or gradual, may threaten a species'
#              survival, requiring individuals to alter behaviors, move, or perish.
#
# ERT-2.H.1 HAS FIVE PARTS AND EVERY KEY DRAWN FROM IT USES ONE: selection acts on
# HERITABLE traits; what adapts is the POPULATION, not the individual; adaptation happens
# OVER GENERATIONS; the changes are INCREMENTAL; and they are AT THE GENETIC LEVEL. The
# commonest wrong answer in this area is that an individual adapts within its own lifetime,
# which the statement's own words rule out, and items 4, 10, 17 and 27 are built on that.
#
# ERT-2.H.2 HAS THREE PARTS: the change may be SUDDEN OR GRADUAL; it MAY threaten a
# species' survival; and it requires individuals to ALTER BEHAVIORS, MOVE, OR PERISH. The
# list of three is the framework's own and is exhaustive as written, so no key adds a
# fourth response and none drops one of the three.
#
# WHAT THE FRAMEWORK DOES NOT SAY, AND SO IS NOT ASKED. It does not define heritable, does
# not name a mechanism of inheritance, does not give any rate of adaptation, and does not
# say that adaptation will keep pace with a change. Item 28 asks which description of a
# trait fits the framework's own phrase "at the genetic level"; the claim in verify_e2_6.py
# says that it rests on that phrase plus the ordinary meaning of the word, and nothing here
# asks a student to classify a borderline case.
#
# BOUNDARY WITH 2.5 AND 3.1. The kinds and time scales of natural disruption are ERT-2.G in
# topic 2.5 and appear here only as the environmental change ERT-2.H.2 responds to. Which
# of specialist and generalist is advantaged in a constant or a changing habitat is
# ERT-3.A.1 in topic 3.1, and nothing here reaches into it.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e2_6.py from
# that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("2.6", "Adaptations", 2)

_T_MOTH = dict(
    headers=["Generation of the moth population",
             "Percent of the population that is the dark form"],
    rows=[["Generation 1", "2"],
          ["Generation 5", "9"],
          ["Generation 10", "26"],
          ["Generation 20", "58"],
          ["Generation 40", "91"]])

_T_HERIT = dict(
    headers=["Trait measured in one population",
             "Percent of the trait's variation that is heritable",
             "Change in the population mean over twenty generations (percent)"],
    rows=[["Trait 1", "78", "34"],
          ["Trait 2", "55", "21"],
          ["Trait 3", "9", "3"],
          ["Trait 4", "2", "1"]])

_T_BEAK = dict(
    headers=["Generation of the finch population", "Mean beak depth (millimetres)"],
    rows=[["Generation 1", "9.2"],
          ["Generation 5", "9.6"],
          ["Generation 10", "10.1"],
          ["Generation 15", "10.5"],
          ["Generation 20", "10.9"]])

_T_INDIV = dict(
    headers=["Measurement made in the same finch population",
             "First year of the study (millimetres)",
             "Fifth year of the study (millimetres)"],
    rows=[["Beak depth of one marked bird", "9.4", "9.4"],
          ["Beak depth of a second marked bird", "10.2", "10.2"],
          ["Beak depth of a third marked bird", "9.8", "9.8"],
          ["Mean beak depth of the whole population", "9.7", "10.4"]])

_T_RESPONSE = dict(
    headers=["What the individuals present did when the lake dried",
             "Number of individuals"],
    rows=[["Altered their behaviour and fed on other prey", "410"],
          ["Moved to another lake", "260"],
          ["Perished", "330"]])

_T_RATE = dict(
    headers=["Environmental change recorded in one region",
             "Time over which it took place (years)",
             "Rise in mean annual temperature (degrees Celsius)"],
    rows=[["Change 1", "1", "4"],
          ["Change 2", "300", "4"]])

_T_RESIST = dict(
    headers=["Generation of the beetle population",
             "Percent surviving the same dose of one insecticide"],
    rows=[["Generation 1", "4"],
          ["Generation 3", "12"],
          ["Generation 6", "35"],
          ["Generation 10", "68"],
          ["Generation 15", "92"]])

_T_THREAT = dict(
    headers=["Population facing the same drought",
             "Percent of its individuals that moved to new ground",
             "Percent that altered their feeding behaviour", "Percent that perished"],
    rows=[["Population 1", "20", "50", "30"],
          ["Population 2", "5", "15", "80"],
          ["Population 3", "60", "30", "10"]])

QUESTIONS = [

 dict(q="What kind of trait does the framework say natural selection acts on?",
      choices=[
        "Heritable traits.",
        "Traits acquired by an individual during its own life.",
        "Traits shared by every species in an ecosystem.",
        "Traits that appear only in the largest individuals.",
        "Traits that have no effect on survival."],
      ans=0,
      why="ERT-2.H.1 states that natural selection acts on heritable traits. The word "
          "heritable is the framework's own restriction on which traits are involved."),

 dict(q="What does the framework say natural selection causes?",
      choices=[
        "Populations to adapt to their environment over generations.",
        "Individuals to adapt to their environment within one lifetime.",
        "Ecosystems to hold a constant number of species.",
        "Environments to change to suit the organisms living in them.",
        "Species to become identical to one another over time."],
      ans=0,
      why="ERT-2.H.1 states that natural selection acts on heritable traits, causing "
          "POPULATIONS to adapt to their environment OVER GENERATIONS. Both the level and "
          "the timescale are the framework's own words."),

 dict(q="Through what kind of change does the framework say that adaptation happens?",
      choices=[
        "Incremental changes at the genetic level.",
        "A single large change in one generation.",
        "Changes in the behaviour of individuals only.",
        "Changes in the physical environment rather than the organisms.",
        "Changes that leave the genes of the population untouched."],
      ans=0,
      why="ERT-2.H.1 states that populations adapt over generations via incremental changes "
          "at the genetic level. Both incremental and genetic are the framework's own "
          "words, and neither is optional."),

 dict(q="According to the framework, what is it that adapts to the environment?",
      choices=[
        "The population, across generations.",
        "The individual, within its own lifetime.",
        "The ecosystem, within one season.",
        "The habitat, over geological time.",
        "The climate, over generations."],
      ans=0,
      why="ERT-2.H.1 states that natural selection causes POPULATIONS to adapt to their "
          "environment OVER GENERATIONS. An individual is not the unit the statement names "
          "and one lifetime is not the interval."),

 dict(q="A trait an animal develops during its own life and does not pass on is described. "
        "Does the framework put natural selection to work on it?",
      choices=[
        "No, because the statement restricts natural selection to heritable traits.",
        "Yes, because every trait an organism has is available to natural selection.",
        "Yes, but only if the animal survives to old age.",
        "No, because natural selection acts only on whole ecosystems.",
        "No, because natural selection acts only on traits that appear suddenly."],
      ans=0,
      why="ERT-2.H.1 states that natural selection acts on HERITABLE traits, so a trait "
          "that is not passed on falls outside what the statement describes. The rejected "
          "options either remove the restriction or replace it with one the framework does "
          "not state."),

 dict(q="What does the framework say environmental change may do to a species?",
      choices=[
        "It may threaten the species' survival.",
        "It always ends the species' existence.",
        "It always improves the species' prospects.",
        "It has no bearing on the species' survival.",
        "It changes the species into a different one within one generation."],
      ans=0,
      why="ERT-2.H.2 states that environmental changes may threaten a species' survival. "
          "The word may makes the threat possible rather than certain, and no other outcome "
          "is asserted."),

 dict(q="Which three things does the framework say environmental change may require "
        "individuals to do?",
      choices=[
        "Alter their behaviours, move, or perish.",
        "Alter their behaviours, reproduce faster, or move.",
        "Move, perish, or change their genes within their own lifetime.",
        "Alter their behaviours, perish, or become a new species.",
        "Move, reproduce faster, or hibernate."],
      ans=0,
      why="ERT-2.H.2 states that environmental changes may threaten a species' survival, "
          "requiring individuals to alter behaviors, move, or perish. Those three are the "
          "framework's own list, and each rejected set drops one of them or adds something "
          "the statement does not name."),

 dict(q="What pace of environmental change does the framework include in that statement?",
      choices=[
        "Both sudden and gradual change.",
        "Sudden change only.",
        "Gradual change only.",
        "Change that lasts exactly one generation.",
        "Change that repeats on a regular cycle."],
      ans=0,
      why="ERT-2.H.2 opens with environmental changes, either sudden or gradual, so both "
          "paces are inside the statement and neither is singled out."),

 dict(q="ERT-2.H.2 says environmental change MAY threaten a species' survival. What does "
        "that word settle?",
      choices=[
        "That the threat is a possible outcome rather than a certain one.",
        "That the threat arrives only after several generations.",
        "That the threat applies to individuals but never to a species.",
        "That the framework is unsure whether environments change at all.",
        "That the threat applies only where the change is sudden."],
      ans=0,
      why="The statement is written with may, which asserts possibility rather than "
          "necessity, so a case in which a species came through a change unharmed does not "
          "contradict it."),

 dict(q="Over what interval does the framework place the adaptation of a population?",
      choices=[
        "Across generations, rather than within a single lifetime.",
        "Within a single lifetime, rather than across generations.",
        "Within a single season, whatever the species.",
        "Across geological time only, never within recorded history.",
        "The framework gives no interval at all."],
      ans=0,
      why="ERT-2.H.1 states that natural selection causes populations to adapt to their "
          "environment OVER GENERATIONS. The interval is stated, and it is longer than one "
          "individual's life."),

 dict(q="A moth population was scored for colour over forty generations. What does the "
        "table establish?",
      table=_T_MOTH,
      choices=[
        "The dark form rose in the population step by step across the generations.",
        "The dark form appeared in full at the first generation scored.",
        "The dark form fell in the population across the generations.",
        "The dark form held the same share in every generation scored.",
        "The dark form disappeared from the population by the fortieth generation."],
      ans=0,
      why="The dark form runs 2, 9, 26, 58 and 91 percent across the generations scored, "
          "rising at every step and never in one jump from nothing to everything. ERT-2.H.1 "
          "describes adaptation as incremental changes at the genetic level over "
          "generations."),

 dict(q="By how many percentage points did the dark form's share of that moth population "
        "change between the first and the fortieth generation?",
      table=_T_MOTH,
      choices=["Eighty-nine points", "Ninety-one points", "Fifty-eight points",
               "Thirty-three points", "Two points"],
      ans=0,
      why="The dark form stands at 2 percent in the first generation scored and 91 percent "
          "in the fortieth, and 91 less 2 is 89. The rejected values are the two endpoints "
          "themselves or differences between other pairs of rows."),

 dict(q="Four traits in one population were measured for heritable variation and for change "
        "over twenty generations. What does the table establish?",
      table=_T_HERIT,
      choices=[
        "The traits whose variation is more heritable changed more over the generations.",
        "The traits whose variation is more heritable changed less over the generations.",
        "All four traits changed by the same amount.",
        "None of the four traits changed at all.",
        "The trait with the least heritable variation changed the most."],
      ans=0,
      why="Ordered by heritable variation the changes run 1, 3, 21 and 34 percent, rising "
          "with the heritability. ERT-2.H.1 states that natural selection acts on heritable "
          "traits, which is the property this record varies."),

 dict(q="Which of those four traits changed least over the twenty generations?",
      table=_T_HERIT,
      choices=["Trait 4", "Trait 1", "Trait 2", "Trait 3",
               "All four changed by the same amount"],
      ans=0,
      why="The changes recorded are 34, 21, 3 and 1 percent, and the smallest belongs to "
          "the trait whose variation is least heritable. ERT-2.H.1 makes heritable variation "
          "what natural selection acts on."),

 dict(q="A finch population was measured for mean beak depth every five generations. What "
        "does the table establish?",
      table=_T_BEAK,
      choices=[
        "The population mean shifted a little at each measurement rather than all at once.",
        "The population mean was unchanged across the twenty generations.",
        "The population mean fell across the twenty generations.",
        "The population mean doubled between the first and the last measurement.",
        "The population mean changed only between the last two measurements."],
      ans=0,
      why="The means run 9.2, 9.6, 10.1, 10.5 and 10.9 millimetres, each a small step above "
          "the one before. ERT-2.H.1 describes adaptation as INCREMENTAL changes at the "
          "genetic level over generations."),

 dict(q="How much did the mean beak depth of that finch population change in total over the "
        "twenty generations?",
      table=_T_BEAK,
      choices=["1.7 millimetres", "0.4 millimetres", "10.9 millimetres",
               "9.2 millimetres", "20.1 millimetres"],
      ans=0,
      why="The mean runs from 9.2 to 10.9 millimetres, and 10.9 less 9.2 is 1.7. The "
          "rejected values are the two endpoints, one single step, or their sum."),

 dict(q="Three marked birds and the whole population were measured in the first and the "
        "fifth year of one study. What does the table establish?",
      table=_T_INDIV,
      choices=[
        "Each marked bird kept the beak depth it started with while the population mean "
        "shifted.",
        "Each marked bird changed its beak depth while the population mean stayed put.",
        "Both the marked birds and the population mean stayed put.",
        "Both the marked birds and the population mean shifted by the same amount.",
        "The marked birds and the population cannot be compared in one record."],
      ans=0,
      why="The three marked birds read 9.4, 10.2 and 9.8 millimetres in both years while "
          "the population mean moves from 9.7 to 10.4. ERT-2.H.1 makes the POPULATION the "
          "thing that adapts, over generations, rather than the individual within its own "
          "life."),

 dict(q="When one lake dried, the individuals present were followed. Which outcome "
        "accounted for the largest number of them?",
      table=_T_RESPONSE,
      choices=[
        "Altering their behaviour and feeding on other prey",
        "Moving to another lake",
        "Perishing",
        "The three outcomes were equally common",
        "None of the three outcomes was recorded"],
      ans=0,
      why="The three counts are 410, 260 and 330 individuals, and the largest belongs to "
          "those that changed what they fed on. ERT-2.H.2 names altering behaviours, moving "
          "and perishing as the three things individuals may be required to do."),

 dict(q="Out of all the individuals followed at that lake, roughly what share perished?",
      table=_T_RESPONSE,
      choices=["About one third", "About one tenth", "About one half",
               "About two thirds", "None of them"],
      ans=0,
      why="The three outcomes account for 1,000 individuals in total and 330 of them "
          "perished, which is close to a third. Perishing is one of the three outcomes "
          "ERT-2.H.2 names."),

 dict(q="Two environmental changes in one region were recorded for size and for speed. What "
        "does the table establish?",
      table=_T_RATE,
      choices=[
        "A change of the same size arrived suddenly in one case and gradually in the other.",
        "The change that took longer was also the larger of the two.",
        "The change that took less time was the larger of the two.",
        "The two changes took the same length of time as each other.",
        "Neither change altered the mean annual temperature."],
      ans=0,
      why="Both changes raise the mean annual temperature by 4 degrees Celsius, but one "
          "takes a single year and the other three hundred. ERT-2.H.2 covers environmental "
          "changes that are either sudden or gradual, and this record holds one of each."),

 dict(q="A beetle population was tested against the same dose of one insecticide every few "
        "generations. By how many percentage points did survival change between the first "
        "and the tenth generation?",
      table=_T_RESIST,
      choices=["Sixty-four points", "Sixty-eight points", "Eighty-eight points",
               "Thirty-three points", "Four points"],
      ans=0,
      why="Survival stands at 4 percent in the first generation tested and 68 percent in the "
          "tenth, and 68 less 4 is 64. ERT-2.H.1 places such a change across generations "
          "rather than within one individual's life."),

 dict(q="In that beetle record, which is the first generation tested at which more than "
        "half the population survived the dose?",
      table=_T_RESIST,
      choices=["Generation 10", "Generation 1", "Generation 3", "Generation 6",
               "No tested generation exceeded one half"],
      ans=0,
      why="The survival figures are 4, 12, 35, 68 and 92 percent, and the first above 50 is "
          "the fourth entry. The reading is a search along one column in the order the "
          "generations were tested."),

 dict(q="Three populations met the same drought. Which lost the largest share of its "
        "individuals?",
      table=_T_THREAT,
      choices=["Population 2", "Population 1", "Population 3",
               "All three lost the same share", "None of the three lost any individuals"],
      ans=0,
      why="The shares that perished are 30, 80 and 10 percent, and the largest belongs to "
          "the population that also moved and altered behaviour least. ERT-2.H.2 names "
          "perishing as one of the three things a threatened individual may be required to "
          "do."),

 dict(q="Taking those three drought-struck populations together, what does the record show "
        "about the responses of their individuals?",
      table=_T_THREAT,
      choices=[
        "All three of the framework's responses occurred in every population, in different "
        "proportions.",
        "Only one of the framework's responses occurred, and it was the same in every "
        "population.",
        "Two of the framework's responses occurred and the third occurred nowhere.",
        "Every population divided its individuals equally between the three responses.",
        "The record does not report what any individual did."],
      ans=0,
      why="Every row records a non-zero share for moving, for altering feeding behaviour and "
          "for perishing, and the three shares differ from row to row. ERT-2.H.2 names "
          "exactly those three as what environmental change may require individuals to do."),

 dict(q="Which set of observations would show that natural selection is acting on a trait "
        "as the framework describes it?",
      choices=[
        "The trait varies among individuals, the variation is passed to offspring, and the "
        "population mean shifts across generations.",
        "The trait varies among individuals and the population mean is the same in every "
        "generation.",
        "The trait is identical in every individual and is passed to offspring.",
        "The trait varies among individuals but is not passed to offspring.",
        "The trait changes within each individual's own lifetime and is not passed on."],
      ans=0,
      why="ERT-2.H.1 requires heritable traits, a population and a change over generations. "
          "Each rejected set is missing the heritability, the variation, or the "
          "generational shift, so none of them is what the statement describes."),

 dict(q="A river's flow changes within a month and the fish population responds in three "
        "ways. Which set of responses matches the framework's own list?",
      choices=[
        "Some alter their behaviour, some move, and some perish.",
        "Some alter their behaviour, some move, and some change their own genes.",
        "Some alter their behaviour, some reproduce faster, and some perish.",
        "Some move, some perish, and some become a new species within the month.",
        "Some hibernate, some move, and some perish."],
      ans=0,
      why="ERT-2.H.2 states that environmental change may require individuals to alter "
          "behaviors, move, or perish. Each rejected set swaps one of the three for "
          "something the statement does not name, and one of them attributes a genetic "
          "change to an individual, which ERT-2.H.1 places in the population across "
          "generations."),

 dict(q="Which of these does the framework NOT claim?",
      choices=[
        "That an individual alters its own genes in response to the environment it meets.",
        "That natural selection acts on heritable traits.",
        "That populations adapt over generations.",
        "That adaptation proceeds by incremental changes at the genetic level.",
        "That environmental change may require individuals to move."],
      ans=0,
      why="ERT-2.H.1 places the genetic change in the population and spreads it over "
          "generations, and ERT-2.H.2 gives individuals three responses of which changing "
          "their own genes is not one. The other four options are the statements' own "
          "words."),

 dict(q="Which description of a trait matches what the framework has natural selection act "
        "on?",
      choices=[
        "One passed from parents to offspring, so that a change in it is a change at the "
        "genetic level.",
        "One learned by watching other members of the group.",
        "One caused by an injury during the individual's life.",
        "One that differs only because some individuals ate more than others.",
        "One that every member of the species shares identically."],
      ans=0,
      why="ERT-2.H.1 acts on HERITABLE traits and locates the changes AT THE GENETIC LEVEL, "
          "so the trait it is about is one carried from parents to offspring. A learned "
          "skill, an injury and a difference in feeding are not carried that way, and a "
          "trait with no variation offers nothing to select between."),

 dict(q="Two accounts of a population living through a warming climate are offered. Which "
        "stays within what the framework asserts?",
      choices=[
        "The warming may threaten the species, individuals alter behaviour, move or perish, "
        "and any adaptation appears in the population over generations.",
        "The warming certainly ends the species, and no individual response is possible.",
        "The warming may threaten the species, and each individual adapts its own genes "
        "within its lifetime.",
        "The warming may threaten the species, but adaptation appears within a single "
        "generation by a single large genetic change.",
        "The warming cannot threaten the species, because populations always adapt in time."],
      ans=0,
      why="ERT-2.H.2 supplies the possible threat and the three individual responses, and "
          "ERT-2.H.1 supplies adaptation of the population over generations by incremental "
          "genetic change. Each rejected account hardens may into certainty, moves the "
          "genetic change into the individual, replaces incremental with a single jump, or "
          "promises that adaptation will succeed."),

 dict(q="Which single sentence collects what this topic's two statements assert and nothing "
        "further?",
      choices=[
        "Natural selection acts on heritable traits so that populations adapt over "
        "generations by incremental genetic change, while environmental change, sudden or "
        "gradual, may threaten a species and require individuals to alter behaviour, move "
        "or perish.",
        "Natural selection acts on any trait an organism has so that individuals adapt "
        "within their lifetimes, while environmental change always destroys a species.",
        "Natural selection acts on heritable traits so that populations adapt over "
        "generations by one large genetic change, while only sudden environmental change "
        "threatens a species.",
        "Natural selection acts on heritable traits so that populations adapt over "
        "generations by incremental genetic change, and environmental change requires "
        "individuals only to move.",
        "Natural selection acts on heritable traits so that ecosystems adapt over seasons, "
        "while environmental change, sudden or gradual, may threaten a species."],
      ans=0,
      why="ERT-2.H.1 supplies heritable traits, the population, the generations and the "
          "incremental genetic change; ERT-2.H.2 supplies the two paces of change, the "
          "possible threat and the three responses. Each rejected summary moves adaptation "
          "into the individual or the ecosystem, replaces incremental with a jump, narrows "
          "the pace of change, or drops two of the three responses."),
]
