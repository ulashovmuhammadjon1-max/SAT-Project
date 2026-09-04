# AP ENVIRONMENTAL SCIENCE 3.3 Survivorship Curves
# CED effective Fall 2026, Unit 3 Populations.
# Enduring understanding ERT-3: populations change over time in reaction to a variety of
# factors.
# Learning objective ERT-3.C: explain survivorship curves. Suggested skill 5.C, explain
# patterns and trends in data to draw conclusions.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-3.C.1  A survivorship curve is a line that displays the relative survival rates of a
#              cohort, a group of individuals of the same age, in a population, from birth
#              to the maximum age reached by any one cohort member. There are Type I,
#              Type II, and Type III curves.
#   ERT-3.C.2  Survivorship curves differ for K-selected and r-selected species, with
#              K-selected species typically following a Type I or Type II curve and
#              r-selected species following a Type III curve.
#
# THE CONSTRAINT THAT SHAPES THIS WHOLE MODULE: THE FRAMEWORK NAMES THE THREE TYPES AND
# DESCRIBES THE SHAPE OF NONE OF THEM. It does not say that a Type I curve means most of a
# cohort survives to old age, or that a Type III means heavy early loss. So NO ITEM HERE
# ASKS A STUDENT TO READ A TYPE OFF A COHORT TABLE. Item 10 keys that absence outright.
#
# WHERE A TYPE IS KEYED, IT IS REACHED THROUGH ERT-3.C.2 AND A NAMED CHAIN, never through a
# curve shape. Items 24 and 25 work like this: ERT-3.B.2 gives r-selected species MANY
# OFFSPRING and SHORT LIFE SPANS and ERT-3.B.1 gives K-selected species FEW OFFSPRING and
# LONG LIFE SPANS, so a table printing offspring number and maximum age identifies which
# profile a species has in the framework's own terms; ERT-3.C.2 then assigns the curve type.
# The claim for each of those items names the chain.
#
# EVERY OTHER DATA ITEM IS ARITHMETIC ON THE PRINTED COHORT: a share, a difference, a count
# at an age, the interval holding the largest loss. None of it needs a curve shape.
#
# NO FIGURES, AND THIS TOPIC IS THE ONE MOST OFTEN TAUGHT FROM A PICTURE. Not one stem here
# refers to a curve being shown. Cohort data are printed in a table= and every question is
# asked of the table.
#
# THE PAIRING IN ERT-3.C.2 INVITES THE SWAP, so the anchors in verify_e3_3.py for items 8,
# 23, 24 and 25 carry both halves of whatever they assert.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("3.3", "Survivorship Curves", 3)

_T_THREE = dict(
    headers=["Age class (years)", "Survivors in cohort A", "Survivors in cohort B",
             "Survivors in cohort C"],
    rows=[["0", "1000", "1000", "1000"],
          ["1", "990", "700", "60"],
          ["2", "975", "490", "28"],
          ["4", "950", "343", "12"],
          ["6", "900", "240", "5"],
          ["8", "700", "168", "2"],
          ["10", "120", "118", "1"]])

_T_MAXAGE = dict(
    headers=["Cohort followed from birth", "Individuals alive at the start",
             "Maximum age reached by any member (years)"],
    rows=[["Cohort 1", "1000", "62"],
          ["Cohort 2", "1000", "3"],
          ["Cohort 3", "1000", "19"]])

_T_DROP = dict(
    headers=["Age interval", "Survivors at the start of the interval",
             "Survivors at the end of the interval"],
    rows=[["Birth to one year", "1000", "410"],
          ["One year to two years", "410", "330"],
          ["Two years to four years", "330", "280"],
          ["Four years to eight years", "280", "150"]])

_T_RELATIVE = dict(
    headers=["Age (years)", "Individuals alive", "Percent of the original cohort alive"],
    rows=[["0", "2000", "100"],
          ["2", "1600", "80"],
          ["5", "1000", "50"],
          ["9", "400", "20"],
          ["12", "100", "5"]])

_T_TWOSPECIES = dict(
    headers=["Species", "Offspring produced per reproduction event",
             "Percent of the cohort surviving the first year",
             "Maximum age reached (years)"],
    rows=[["Species M", "2", "94", "38"],
          ["Species N", "5000", "1", "2"]])

QUESTIONS = [

 dict(q="What does the framework say a survivorship curve is?",
      choices=[
        "A line that displays the relative survival rates of a cohort in a population.",
        "A line that displays the total size of a population from year to year.",
        "A line that displays the number of offspring produced in each breeding season.",
        "A line that displays the largest population an environment can support.",
        "A line that displays the average age of the individuals in a population."],
      ans=0,
      why="ERT-3.C.1 states that a survivorship curve is a line that displays the relative "
          "survival rates of a cohort in a population. It is about one cohort's survival, "
          "not about population size, births, limits or averages."),

 dict(q="What does the framework say a cohort is?",
      choices=[
        "A group of individuals of the same age.",
        "A group of individuals of the same species in one place.",
        "A group of individuals born in different years but measured together.",
        "A group of species that share a habitat.",
        "A group of individuals of the same size."],
      ans=0,
      why="ERT-3.C.1 defines a cohort, in its own parenthesis, as a group of individuals of "
          "the same age. Shared species, shared habitat and shared size are not the "
          "criterion the framework gives."),

 dict(q="Over what span does the framework say a survivorship curve runs?",
      choices=[
        "From birth to the maximum age reached by any one cohort member.",
        "From birth to the average age reached by the cohort.",
        "From the age of first reproduction to death.",
        "From the founding of the population to the present day.",
        "From one breeding season to the next."],
      ans=0,
      why="ERT-3.C.1 states that the curve runs from birth to the maximum age reached by "
          "any one cohort member, so the end of the axis is set by the longest lived member "
          "rather than by an average or by a stage of life."),

 dict(q="How many types of survivorship curve does the framework name, and what are they "
        "called?",
      choices=[
        "Three, called Type I, Type II and Type III.",
        "Two, called Type I and Type II.",
        "Four, called Type I through to Type IV.",
        "Three, called Type A, Type B and Type C.",
        "One, called simply the survivorship curve."],
      ans=0,
      why="ERT-3.C.1 closes by stating that there are Type I, Type II, and Type III curves, "
          "which is three types with those names."),

 dict(q="A revision card lists four curve types and calls all four framework types. Which "
        "one is not?",
      choices=["The Type IV curve", "The Type I curve", "The Type II curve",
               "The Type III curve",
               "All of Type I, Type II and Type III are framework types"],
      ans=0,
      why="ERT-3.C.1 names Type I, Type II and Type III. A fourth type is not among them, "
          "so a card carrying four names has one too many."),

 dict(q="Which curve types does the framework say K-selected species typically follow?",
      choices=["Type I or Type II curves", "Type III curves alone",
               "Type II or Type III curves", "Type I curves alone", "Type IV curves"],
      ans=0,
      why="ERT-3.C.2 states that K-selected species typically follow a Type I or Type II "
          "curve. The statement offers two types for them, not one, and not the type it "
          "gives to r-selected species."),

 dict(q="Which curve type does the framework say r-selected species follow?",
      choices=["Type III curves", "Type I curves alone", "Type II curves alone",
               "Both Type I and Type II curves", "Type IV curves"],
      ans=0,
      why="ERT-3.C.2 states that r-selected species follow a Type III curve. The two types "
          "it offers to K-selected species are not the one it gives here."),

 dict(q="Which statement reproduces the framework's pairing of curve types with reproductive "
        "strategies in full?",
      choices=[
        "K-selected species typically follow a Type I or Type II curve, and r-selected "
        "species follow a Type III curve.",
        "K-selected species typically follow a Type III curve, and r-selected species follow "
        "a Type I or Type II curve.",
        "Both kinds of species follow a Type III curve.",
        "Both kinds of species follow a Type I curve.",
        "The framework does not connect the curve types to either kind of species."],
      ans=0,
      why="ERT-3.C.2 states that survivorship curves differ for K-selected and r-selected "
          "species, with K-selected species typically following a Type I or Type II curve "
          "and r-selected species following a Type III curve. The rejected options exchange "
          "the two, collapse them, or deny the connection."),

 dict(q="ERT-3.C.2 says K-selected species TYPICALLY follow one of those curves. What does "
        "that word establish?",
      choices=[
        "That the pairing is usual for K-selected species rather than universal.",
        "That the pairing holds for every K-selected species without exception.",
        "That the pairing holds only for species that have been studied.",
        "That the pairing holds only during a species' first generation.",
        "That the framework is unsure whether K-selected species exist."],
      ans=0,
      why="The statement is written with typically, which asserts what usually holds rather "
          "than a rule without exceptions. A K-selected species whose curve is neither Type "
          "I nor Type II is therefore not a contradiction."),

 dict(q="What does the framework supply about the three curve types themselves?",
      choices=[
        "It names the three types without describing the shape of any of them.",
        "It describes the shape of each of the three types in turn.",
        "It gives a formula for calculating each type from cohort data.",
        "It states how many species follow each of the three types.",
        "It states the age at which each type of curve begins to fall."],
      ans=0,
      why="ERT-3.C.1 states that there are Type I, Type II, and Type III curves and stops "
          "there, and ERT-3.C.2 attaches types to reproductive strategies without describing "
          "any curve's shape. No shape, formula, count or age is given anywhere in the "
          "statements."),

 dict(q="Why is a single census counting individuals of every age in a population not enough "
        "to build a survivorship curve?",
      choices=[
        "Because a survivorship curve follows a cohort, which is a group of individuals of "
        "the same age.",
        "Because a survivorship curve requires the population's total size at each census.",
        "Because a survivorship curve is drawn only for K-selected species.",
        "Because a survivorship curve requires the number of offspring produced each year.",
        "Because a survivorship curve cannot be built from counts of any kind."],
      ans=0,
      why="ERT-3.C.1 makes the survivorship curve a display of the relative survival rates "
          "of a COHORT, defined as a group of individuals of the same age, so the "
          "measurement follows one such group rather than sampling every age at one moment."),

 dict(q="What quantity does the framework say a survivorship curve displays?",
      choices=[
        "Relative survival rates.",
        "Absolute numbers of births.",
        "The total biomass of the population.",
        "The number of species in the community.",
        "The rate at which the habitat is changing."],
      ans=0,
      why="ERT-3.C.1 states that a survivorship curve displays the relative survival rates "
          "of a cohort. Births, biomass, species counts and habitat change are not what the "
          "line displays."),

 dict(q="Three cohorts of one thousand individuals each were followed from birth. Which "
        "cohort lost the largest share of its members in the first year?",
      table=_T_THREE,
      choices=["Cohort C", "Cohort A", "Cohort B",
               "All three lost the same share", "None of the three lost any members"],
      ans=0,
      why="Between the first two age classes the three cohorts fall from 1,000 to 990, to "
          "700 and to 60, which are losses of 1, 30 and 94 percent. The largest share is "
          "arithmetic on two rows of one column."),

 dict(q="At age eight, which of those three cohorts still has the most survivors?",
      table=_T_THREE,
      choices=["Cohort A", "Cohort B", "Cohort C",
               "All three have the same number of survivors",
               "None of the three has any survivors left"],
      ans=0,
      why="At that age class the three cohorts stand at 700, 168 and 2 survivors. The "
          "comparison is a direct reading of one row."),

 dict(q="What percent of the first of those cohorts was still alive at age six?",
      table=_T_THREE,
      choices=["Ninety percent", "Seventy percent", "Twelve percent",
               "Ninety-nine percent", "Twenty-four percent"],
      ans=0,
      why="That cohort begins with 1,000 individuals and stands at 900 in the age class for "
          "six years, and 900 out of 1,000 is 90 percent. ERT-3.C.1 makes the curve a "
          "display of RELATIVE survival rates, which is what a percent of the original "
          "cohort is."),

 dict(q="How many members of the third of those cohorts were still alive at age two?",
      table=_T_THREE,
      choices=["Twenty-eight", "Sixty", "Twelve", "Four hundred and ninety", "Two"],
      ans=0,
      why="The age class for two years records 28 survivors in that cohort. The rejected "
          "values are that cohort's counts at other ages or another cohort's count at the "
          "same age."),

 dict(q="Which of those three cohorts falls by roughly the same PROPORTION between one age "
        "class and the next, all the way along?",
      table=_T_THREE,
      choices=["Cohort B", "Cohort A", "Cohort C",
               "All three fall by the same proportion each time",
               "None of the three falls by a constant proportion"],
      ans=0,
      why="One cohort's successive counts stand at about seven tenths of the count before "
          "them at every step, while the others fall by a share that changes from step to "
          "step. The comparison is a set of divisions carried out on the three columns."),

 dict(q="Three cohorts were followed from birth. Whose survivorship curve would extend "
        "furthest along the age axis?",
      table=_T_MAXAGE,
      choices=["That of Cohort 1", "That of Cohort 2", "That of Cohort 3",
               "All three would extend equally far",
               "The record does not fix how far any of them extends"],
      ans=0,
      why="ERT-3.C.1 states that a survivorship curve runs from birth to the maximum age "
          "reached by any one cohort member, and the maximum ages recorded are 62, 3 and 19 "
          "years. The furthest is arithmetic on one column."),

 dict(q="Among those same three cohorts, whose survivorship curve would be the shortest "
        "along the age axis?",
      table=_T_MAXAGE,
      choices=["That of Cohort 2", "That of Cohort 1", "That of Cohort 3",
               "All three would be equally short",
               "The record does not fix how far any of them extends"],
      ans=0,
      why="The maximum ages recorded are 62, 3 and 19 years, and the smallest sets the "
          "shortest axis. ERT-3.C.1 ends the curve at the maximum age reached by any one "
          "cohort member."),

 dict(q="One cohort of a thousand was counted at the start and end of four age intervals. "
        "In which interval did it lose the largest NUMBER of individuals?",
      table=_T_DROP,
      choices=[
        "Birth to one year", "One year to two years", "Two years to four years",
        "Four years to eight years", "The four intervals lost equal numbers"],
      ans=0,
      why="The four intervals lose 590, 80, 50 and 130 individuals. The largest is "
          "arithmetic on the two columns, taken row by row."),

 dict(q="What share of that cohort was lost during its first year?",
      table=_T_DROP,
      choices=["Fifty-nine percent", "Forty-one percent", "Eight percent",
               "Thirteen percent", "Eighty-five percent"],
      ans=0,
      why="The cohort falls from 1,000 to 410 over that interval, a loss of 590, and 590 out "
          "of 1,000 is 59 percent. ERT-3.C.1 makes relative survival the quantity of "
          "interest, and a share lost is its complement."),

 dict(q="A cohort of two thousand was counted at five ages, alongside the share of the "
        "original cohort still alive. What does the record establish about the two right "
        "hand columns?",
      table=_T_RELATIVE,
      choices=[
        "The percent column is each count expressed as a share of the original cohort.",
        "The percent column is each count expressed as a share of the count before it.",
        "The percent column is unrelated to the counts beside it.",
        "The percent column gives the share of the cohort that died by that age.",
        "The percent column gives the share of the population, not of the cohort."],
      ans=0,
      why="Every row's percent equals its count divided by the 2,000 individuals alive at "
          "age zero: 1,600 gives 80, 1,000 gives 50, 400 gives 20 and 100 gives 5. "
          "ERT-3.C.1 makes a survivorship curve a display of RELATIVE survival rates, which "
          "is exactly this ratio to the original cohort."),

 dict(q="By what age had half of that cohort died?",
      table=_T_RELATIVE,
      choices=["By age five", "By age two", "By age nine", "By age twelve",
               "The cohort never fell to half its size"],
      ans=0,
      why="The share still alive falls to 50 percent at the third age recorded, which is "
          "five years, and it is above half at every earlier age. The reading is a search "
          "along one column."),

 dict(q="Two species were recorded for offspring number, first year survival and maximum "
        "age. Which of them carries the profile the framework gives r-selected species?",
      table=_T_TWOSPECIES,
      choices=[
        "Species N, which has many offspring and the shorter maximum age.",
        "Species M, which has many offspring and the shorter maximum age.",
        "Species N, which has few offspring and the longer maximum age.",
        "Species M, which has few offspring and the longer maximum age.",
        "Neither species carries that profile."],
      ans=0,
      why="ERT-3.B.2 gives r-selected species many offspring and short life spans, and one "
          "of these two produces 5,000 offspring per event and reaches two years while the "
          "other produces two and reaches thirty-eight. The rejected options attach the "
          "wrong traits to a species or the wrong species to the traits."),

 dict(q="Which curve type does the framework assign to the species in that record with many "
        "offspring and the shorter maximum age?",
      table=_T_TWOSPECIES,
      choices=["A Type III curve", "A Type I curve", "A Type II curve",
               "A Type I or Type II curve", "A Type IV curve"],
      ans=0,
      why="ERT-3.B.2 gives r-selected species many offspring and short life spans, which is "
          "the profile of the species producing 5,000 offspring and reaching two years, and "
          "ERT-3.C.2 states that r-selected species follow a Type III curve. The type is "
          "reached through those two statements, not from any shape."),

 dict(q="And which curve type or types does the framework assign to the other species in "
        "that record?",
      table=_T_TWOSPECIES,
      choices=["A Type I or a Type II curve", "A Type III curve", "A Type IV curve",
               "Type III and Type IV curves together",
               "The framework assigns no curve type to it"],
      ans=0,
      why="ERT-3.B.1 gives K-selected species few offspring and long life spans, which is "
          "the profile of the species producing two offspring and reaching thirty-eight "
          "years, and ERT-3.C.2 states that K-selected species typically follow a Type I or "
          "Type II curve. Two types are offered, not one."),

 dict(q="Taking the cohort counted across four age intervals, what share of it was still "
        "alive at eight years?",
      table=_T_DROP,
      choices=["Fifteen percent", "Fifty percent", "Twenty-eight percent",
               "Forty-one percent", "Eighty-five percent"],
      ans=0,
      why="The cohort begins at 1,000 and stands at 150 at the end of the last interval, and "
          "150 out of 1,000 is 15 percent. The share is arithmetic on the first and last "
          "entries of the two columns."),

 dict(q="A researcher wants to build a survivorship curve for a bird species. Which study "
        "design follows the framework's definition?",
      choices=[
        "Marking every chick hatched in one season and recording how many are still alive at "
        "each later age.",
        "Counting all the birds of every age present in the wood in one week.",
        "Counting the eggs laid in the wood over ten seasons.",
        "Recording the ages of the birds found dead in one winter.",
        "Measuring the total mass of birds in the wood each spring."],
      ans=0,
      why="ERT-3.C.1 defines the curve as a display of the relative survival rates of a "
          "cohort, a group of individuals of the same age, from birth onward. Only a group "
          "hatched together and followed through time is such a cohort."),

 dict(q="A student says a survivorship curve shows how the size of a population changes over "
        "the years. What is wrong with that?",
      choices=[
        "It shows the relative survival of one cohort, not the size of the whole population.",
        "It shows the size of the whole population, but only for K-selected species.",
        "It shows the number of offspring produced, not survival at all.",
        "It shows the maximum population an environment can support.",
        "It shows the ages of the individuals present at a single moment."],
      ans=0,
      why="ERT-3.C.1 makes the curve a display of the relative survival rates of a cohort "
          "from birth to the maximum age any member reaches. A population's total size "
          "includes individuals of every age and every birth year, which is not what the "
          "line follows."),

 dict(q="Which single sentence collects what this topic's two statements assert and nothing "
        "further?",
      choices=[
        "A survivorship curve displays the relative survival of a cohort from birth to the "
        "oldest age any member reaches; there are Type I, Type II and Type III curves; and "
        "K-selected species typically follow Type I or Type II while r-selected species "
        "follow Type III.",
        "A survivorship curve displays the size of a population over time; there are Type I, "
        "Type II and Type III curves; and K-selected species follow Type III while "
        "r-selected species follow Type I or Type II.",
        "A survivorship curve displays the relative survival of a cohort; there are four "
        "curve types; and every K-selected species follows a Type I curve.",
        "A survivorship curve displays the relative survival of a cohort from birth to the "
        "average age reached; there are three curve types; and the framework does not "
        "connect them to reproductive strategy.",
        "A survivorship curve displays the relative survival of a cohort from birth to the "
        "oldest age any member reaches; there are Type I, Type II and Type III curves; and "
        "the framework describes the shape of each of the three."],
      ans=0,
      why="ERT-3.C.1 supplies the definition, the cohort, the span and the three type names, "
          "and ERT-3.C.2 supplies the pairing with the two reproductive strategies. Each "
          "rejected summary changes what the line displays, changes the end of the span, "
          "adds a fourth type, reverses the pairing, denies it, or claims a description of "
          "the shapes that the framework never gives."),
]
