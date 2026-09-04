# AP ENVIRONMENTAL SCIENCE 8.12 Lethal Dose 50% (LD50)
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding EIN-3, pollutants can have both direct and indirect impacts on the health
# of organisms, including humans. Learning objective EIN-3.A: define lethal dose 50%
# (LD50). Suggested skill 6.A, determine an approach or method aligned with the problem
# to be solved.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-3.A.1  Lethal dose 50% (LD50) is the dose of a chemical that is lethal to 50% of
#              the population of a particular species.
#
# THAT IS THE WHOLE OF THE FRAMEWORK'S CONTENT FOR THIS TOPIC. One sentence. So the
# thirty items here do one of exactly three things, and nothing else:
#   (a) state or apply the definition itself;
#   (b) reason from the definition -- a smaller lethal dose for half the population means
#       a more toxic chemical, a value belongs to the species it was measured in, a value
#       cannot be read from data in which mortality never reaches half;
#   (c) read or compute a number from a table given in the item, which
#       verify_e8_12.py recomputes from that table alone.
# Nothing is keyed to a toxicity threshold, a regulatory limit, a real chemical's LD50,
# a route of exposure, or a sublethal effect. The framework states none of them.
#
# ON THE FIGURES. This topic is normally taught from a dose response graph and the bank
# carries no images, so every dose response here is a TABLE. Each table that asks for an
# LD50 contains a row at exactly 50 percent mortality, so the value asked for is
# genuinely readable from the rows given rather than guessed between them. Where no row
# reaches 50 percent that is the point of the item, and the key says so.
#
# ON SCOPE. Topic 8.13 keys the dose response curve itself (EIN-3.B.1) and topic 8.14
# keys the difficulty of establishing cause and effect for human health (EIN-3.C.1).
# Nothing here restates either.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.12", "Lethal Dose 50% (LD50)", 8)

_T_BASIC = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Percent of the group that died"],
    rows=[["0", "0"],
          ["10", "5"],
          ["20", "20"],
          ["40", "50"],
          ["80", "85"],
          ["160", "100"]])

_T_TWO_SPECIES = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Percent of species A that died", "Percent of species B that died"],
    rows=[["3", "5", "0"],
          ["12", "50", "2"],
          ["60", "92", "10"],
          ["300", "100", "50"],
          ["900", "100", "88"]])

_T_FOUR_CHEMICALS = dict(
    headers=["Chemical tested on the same species",
             "LD50 measured for that species (milligrams per kilogram of body mass)"],
    rows=[["Chemical W", "5.0"],
          ["Chemical X", "90"],
          ["Chemical Y", "1200"],
          ["Chemical Z", "8000"]])

_T_BODY_MASS = dict(
    headers=["Species tested",
             "LD50 measured for that species (milligrams per kilogram of body mass)",
             "Body mass of one individual (kilograms)"],
    rows=[["Species M", "20", "3.0"],
          ["Species N", "50", "0.40"],
          ["Species P", "8.0", "12"]])

_T_INCOMPLETE = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Percent of the group that died"],
    rows=[["1.0", "0"],
          ["2.0", "2"],
          ["4.0", "6"],
          ["8.0", "15"]])

_T_AGE_GROUPS = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Percent of the young animals that died",
             "Percent of the adult animals that died"],
    rows=[["5.0", "20", "2"],
          ["10", "50", "8"],
          ["25", "78", "24"],
          ["50", "96", "50"],
          ["100", "100", "90"]])

_T_THREE_POINTS = dict(
    headers=["Chemical tested on the same species",
             "Dose at which 10 percent died (milligrams per kilogram)",
             "Dose at which 50 percent died (milligrams per kilogram)",
             "Dose at which 90 percent died (milligrams per kilogram)"],
    rows=[["Chemical P", "4.0", "15", "60"],
          ["Chemical Q", "40", "150", "600"]])

_T_FINE = dict(
    headers=["Dose given to each group (milligrams per kilogram of body mass)",
             "Percent of the group that died"],
    rows=[["0", "0"],
          ["25", "4"],
          ["50", "15"],
          ["75", "33"],
          ["100", "50"],
          ["125", "71"],
          ["150", "88"]])

QUESTIONS = [

 dict(q="How does the framework define lethal dose 50 percent?",
      choices=[
        "The dose of a chemical that is lethal to half of the population of a particular "
        "species",
        "The dose of a chemical that is lethal to every member of a population",
        "The dose of a chemical below which no member of a population is harmed",
        "The share of a population that survives any dose of a chemical",
        "The length of time a chemical remains in the body of an organism"],
      ans=0,
      why="EIN-3.A.1 states that lethal dose 50 percent is the dose of a chemical that is "
          "lethal to 50 percent of the population of a particular species. Each rejected "
          "option changes the fraction, reverses the meaning, or measures something other "
          "than a dose."),

 dict(q="What does the number in the name of this measure refer to?",
      choices=[
        "The percentage of the exposed population that the dose kills",
        "The percentage of the chemical that is absorbed by the body",
        "The number of milligrams in the dose",
        "The number of individuals tested in the study",
        "The percentage of the dose that remains in the body after a day"],
      ans=0,
      why="EIN-3.A.1 defines the measure as the dose lethal to 50 percent of the "
          "population of a particular species, so the number describes the share of the "
          "population killed rather than any property of the chemical or of the study."),

 dict(q="Groups of one species were each given a different dose and the deaths were "
        "recorded.",
      table=_T_BASIC,
      choices=[
        "The LD50 for this species is 40 milligrams per kilogram of body mass",
        "The LD50 for this species is 20 milligrams per kilogram of body mass",
        "The LD50 for this species is 80 milligrams per kilogram of body mass",
        "The LD50 for this species is 160 milligrams per kilogram of body mass",
        "The LD50 cannot be determined because no group reached 50 percent"],
      ans=0,
      why="One row of the table records exactly half the group dying, and the dose in that "
          "row is the keyed value. EIN-3.A.1 defines the LD50 as the dose lethal to 50 "
          "percent of the population of a particular species."),

 dict(q="Why does the framework's definition specify a particular species?",
      choices=[
        "The dose that kills half of one species need not be the dose that kills half of "
        "another, so a value belongs to the species it was measured in",
        "Only one species can be tested with any given chemical",
        "Every species is killed by the same dose, so naming the species is a formality",
        "The species determines the units in which the dose is reported",
        "A chemical has no effect on any species other than the one tested"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as lethal to 50 percent of the population of a "
          "particular species, which ties the value to the species tested. Nothing in the "
          "framework says the value carries over unchanged or that other species are "
          "unaffected."),

 dict(q="Two species were exposed to the same chemical at the same doses.",
      table=_T_TWO_SPECIES,
      choices=[
        "The chemical is far more toxic to species A, whose LD50 is a small fraction of "
        "the dose that kills half of species B",
        "The chemical is far more toxic to species B, whose LD50 is the smaller of the two",
        "The two species have the same LD50 for this chemical",
        "Neither species reaches 50 percent mortality at any dose tested",
        "The LD50 for species A is the highest dose in the table"],
      ans=0,
      why="Each species has a row at exactly half its group dying, and the dose in the "
          "row for the first species is many times smaller than the dose in the row for "
          "the second. EIN-3.A.1 defines the LD50 as the dose lethal to half the "
          "population of a particular species, so the smaller value marks the greater "
          "toxicity to that species."),

 dict(q="What does a smaller LD50 tell you about a chemical, given the framework's "
        "definition?",
      choices=[
        "A smaller dose is enough to kill half the population, so the chemical is more "
        "toxic to that species",
        "A larger dose is required to kill half the population, so the chemical is less "
        "toxic",
        "The chemical remains in the environment for a shorter time",
        "The chemical affects a smaller number of body systems",
        "The chemical is absorbed more slowly by the organisms exposed to it"],
      ans=0,
      why="EIN-3.A.1 makes the LD50 the dose lethal to 50 percent of the population, so a "
          "smaller value means less of the chemical is needed to reach that outcome. "
          "Persistence, the number of systems affected and the rate of absorption are "
          "different quantities the definition says nothing about."),

 dict(q="Which approach would a researcher use to determine the LD50 of a chemical for "
        "one species?",
      choices=[
        "Expose several equal groups of that species to a range of doses and find the dose "
        "at which half the group dies",
        "Expose a single individual to one dose and record whether it survives",
        "Measure how long the chemical remains detectable in soil",
        "Ask how many people believe the chemical to be dangerous",
        "Compare the price of the chemical with that of a similar chemical"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as a dose associated with half a population dying, "
          "so the method must expose groups at several doses and locate that dose. A "
          "single individual gives no percentage, and the other options measure something "
          "other than lethality."),

 dict(q="Four chemicals were tested on the same species.",
      table=_T_FOUR_CHEMICALS,
      choices=[
        "The chemical with the smallest listed value is the most toxic to this species, "
        "and the one with the largest listed value is the least toxic",
        "The chemical with the largest listed value is the most toxic to this species",
        "All four chemicals are equally toxic to this species",
        "The listed values say nothing about how toxic the chemicals are",
        "The two chemicals with the middle values are the most toxic"],
      ans=0,
      why="The listed values are the doses at which half the population dies, so the "
          "smallest value marks the chemical that reaches that outcome with the least "
          "material and the largest value the one that needs the most. EIN-3.A.1 supplies "
          "that meaning for the number."),

 dict(q="Which statement misstates what an LD50 value means?",
      choices=[
        "It is the dose below which the chemical produces no effect of any kind",
        "It is a dose measured for a particular species",
        "It is the dose associated with half of an exposed population dying",
        "It is a value that can differ from one species to another",
        "It is smaller for a chemical that is more toxic to the species tested"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 only as the dose lethal to 50 percent of the "
          "population of a particular species, so it makes no claim about doses below "
          "which nothing happens. The four rejected statements follow from that "
          "definition."),

 dict(q="An LD50 and a body mass are given for each of three species.",
      table=_T_BODY_MASS,
      choices=[
        "For one individual of the first species listed, the LD50 dose is about 60 "
        "milligrams of the chemical",
        "For one individual of the first species listed, the LD50 dose is about 20 "
        "milligrams of the chemical",
        "For one individual of the first species listed, the LD50 dose is about 6.7 "
        "milligrams of the chemical",
        "For one individual of the first species listed, the LD50 dose is about 600 "
        "milligrams of the chemical",
        "For one individual of the first species listed, the LD50 dose is about 3 "
        "milligrams of the chemical"],
      ans=0,
      why="The table gives the dose per kilogram of body mass and the body mass of one "
          "individual, and multiplying the two gives the amount of chemical in that "
          "individual's dose. EIN-3.A.1 defines that dose as the one lethal to half the "
          "population of the species."),

 dict(q="Why is an LD50 reported as a dose rather than as an amount of chemical released "
        "into an ecosystem?",
      choices=[
        "The definition concerns how much of the chemical an organism receives, which is "
        "what determines whether half the population dies",
        "The definition concerns how much of the chemical is manufactured each year",
        "The definition concerns how long the chemical persists after it is released",
        "The definition concerns how far the chemical travels from its source",
        "The definition concerns how much of the chemical dissolves in water"],
      ans=0,
      why="EIN-3.A.1 makes the LD50 a dose of a chemical that is lethal to half of a "
          "population, so the quantity is what reaches the organisms. Production, "
          "persistence, transport and solubility are treated in other topics."),

 dict(q="One chemical was tested on a species at four doses.",
      table=_T_INCOMPLETE,
      choices=[
        "The LD50 cannot be read from these data because no dose tested killed as many as "
        "half the group",
        "The LD50 is the highest dose in the table, since it produced the most deaths",
        "The LD50 is the lowest dose in the table, since it produced no deaths",
        "The LD50 is the middle dose in the table",
        "The LD50 is zero, since one group had no deaths at all"],
      ans=0,
      why="The largest percentage in the table is well below half, so no row records the "
          "outcome EIN-3.A.1 defines, and the dose that would produce it lies above every "
          "dose tested. Naming any tested dose as the LD50 would assert something the data "
          "do not show."),

 dict(q="A student says a chemical with an LD50 of 500 milligrams per kilogram is safe at "
        "any dose below that value. What is the clearest correction?",
      choices=[
        "The value marks only the dose at which half the population dies and says nothing "
        "about what smaller doses do",
        "The value marks the dose below which the chemical is certainly harmless",
        "The value marks the dose above which every individual survives",
        "The value marks the share of the chemical absorbed rather than a dose",
        "The value applies to every species equally, so it can be used for any organism"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population "
          "of a particular species and states nothing about lower doses, so treating it as "
          "a safety threshold reads into the definition something it does not contain."),

 dict(q="Which of the following would make a comparison of two chemicals' LD50 values "
        "meaningful?",
      choices=[
        "Both values were measured on the same species",
        "Both values were measured in the same year",
        "Both chemicals were manufactured by the same company",
        "Both chemicals were sold at the same price",
        "Both values were reported in the same journal"],
      ans=0,
      why="EIN-3.A.1 ties the value to a particular species, so two values are comparable "
          "when they belong to the same species. The year, the manufacturer, the price and "
          "the place of publication have no bearing on the definition."),

 dict(q="Young and adult animals of the same species were tested at the same doses.",
      table=_T_AGE_GROUPS,
      choices=[
        "Half the young animals died at a dose far smaller than the dose at which half the "
        "adults died",
        "Half the adults died at a dose far smaller than the dose at which half the young "
        "animals died",
        "The two groups reached half mortality at the same dose",
        "Neither group reached half mortality at any dose tested",
        "The young animals never reached half mortality at any dose tested"],
      ans=0,
      why="Each group has a row at exactly half of it dying, and the dose in the row for "
          "the young animals is several times smaller than the dose in the row for the "
          "adults. EIN-3.A.1 defines that dose as the LD50 for the population tested."),

 dict(q="Why can two groups of the same species yield different LD50 values in different "
        "studies?",
      choices=[
        "The value is a property of the population tested under the conditions of the "
        "test, so a different population or a different test can give a different number",
        "The value is fixed by the chemical alone and can never differ",
        "The value depends only on the price of the chemical used",
        "The value depends only on the number of researchers involved",
        "The value is chosen by the researchers before the test begins"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 in terms of the population of a particular species "
          "that is exposed, so it is measured from that population rather than fixed by "
          "the chemical alone. Nothing in the framework makes it a chosen value."),

 dict(q="Which of the following is the best reason to test several doses rather than one "
        "when determining an LD50?",
      choices=[
        "The dose that produces half mortality is not known in advance, so a range of "
        "doses is needed to find it",
        "A single dose would kill the entire population no matter how small it was",
        "A single dose is impossible to administer to a group of animals",
        "Testing several doses reduces the cost of the study",
        "Testing several doses makes the chemical less toxic"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as a particular point on the relationship between "
          "dose and mortality, and locating that point requires observing mortality at "
          "more than one dose."),

 dict(q="Two chemicals were tested on the same species and three points were recorded for "
        "each.",
      table=_T_THREE_POINTS,
      choices=[
        "The dose that kills half the population is ten times larger for the second "
        "chemical than for the first",
        "The dose that kills half the population is ten times larger for the first "
        "chemical than for the second",
        "The two chemicals kill half the population at the same dose",
        "Neither chemical has a dose at which half the population dies",
        "The dose that kills half the population is smaller for the second chemical"],
      ans=0,
      why="Dividing the second chemical's fifty percent dose by the first chemical's gives "
          "a factor of ten. EIN-3.A.1 defines that column as the LD50 for the species "
          "tested."),

 dict(q="A regulator has LD50 values for a chemical in rats and wants to know its effect "
        "on fish. What does the framework's definition allow?",
      choices=[
        "The rat value describes the rat population tested and does not by itself give the "
        "dose that kills half a fish population",
        "The rat value applies unchanged to fish, since an LD50 is a property of the "
        "chemical alone",
        "The rat value shows that fish are unaffected by the chemical",
        "The rat value can be converted to the fish value by dividing by the number of "
        "species",
        "The framework says LD50 values cannot be measured in any species"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population "
          "of a particular species, so a value measured in one species is a statement "
          "about that species. The framework offers no rule for transferring it."),

 dict(q="Which pairing of a description with the framework's measure is correct?",
      choices=[
        "The dose lethal to half of the exposed population of one species, paired with the "
        "name lethal dose 50 percent",
        "The dose lethal to every member of an exposed population, paired with the name "
        "lethal dose 50 percent",
        "The share of a chemical that dissolves in fat, paired with the name lethal dose "
        "50 percent",
        "The time a chemical persists in soil, paired with the name lethal dose 50 percent",
        "The distance a chemical travels on the wind, paired with the name lethal dose 50 "
        "percent"],
      ans=0,
      why="EIN-3.A.1 states that lethal dose 50 percent is the dose of a chemical that is "
          "lethal to 50 percent of the population of a particular species. The rejected "
          "pairings attach the name to complete lethality, to fat solubility, to "
          "persistence and to transport, which belong to other statements."),

 dict(q="Doses and deaths for one species are recorded at closely spaced intervals.",
      table=_T_FINE,
      choices=[
        "The LD50 for this species is 100 milligrams per kilogram of body mass",
        "The LD50 for this species is 75 milligrams per kilogram of body mass",
        "The LD50 for this species is 125 milligrams per kilogram of body mass",
        "The LD50 for this species is 50 milligrams per kilogram of body mass",
        "The LD50 lies between two of the doses tested and cannot be read exactly"],
      ans=0,
      why="One row records exactly half the group dying, so the dose in that row is the "
          "value EIN-3.A.1 defines and no interpolation between rows is required."),

 dict(q="Why is an LD50 described as a property of a population rather than of an "
        "individual?",
      choices=[
        "It is defined by the fraction of a group that dies, which requires a group to "
        "measure",
        "It is defined by the largest individual in the group",
        "It is defined by the first individual in the group to die",
        "It is defined by the body mass of a single organism",
        "It is defined by the average lifespan of the species"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 in terms of 50 percent of the population of a "
          "particular species, and a percentage of a population cannot be observed in one "
          "organism."),

 dict(q="A team reports that a chemical killed 50 percent of the beetles it tested at a "
        "given dose. Which statement follows from the framework?",
      choices=[
        "That dose is the LD50 for the beetle population tested",
        "That dose is the LD50 for every insect species",
        "That dose is the highest dose at which any beetle survives",
        "That dose is the lowest dose at which any beetle dies",
        "That dose is the amount of the chemical released into the environment"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as the dose lethal to 50 percent of the population "
          "of a particular species, which is exactly what the team observed. The rejected "
          "statements extend the result beyond the species tested or describe a different "
          "quantity."),

 dict(q="Which additional information would a researcher most need in order to report an "
        "LD50 usefully?",
      choices=[
        "The species whose population was exposed",
        "The color of the container the chemical was stored in",
        "The name of the laboratory technician",
        "The month in which the study began",
        "The number of pages in the final report"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as belonging to a particular species, so the species "
          "is part of the reported value. Storage, staffing, timing and report length bear "
          "on none of the definition."),

 dict(q="Which of the following results would show that one chemical is more toxic than "
        "another to the same species?",
      choices=[
        "Half the population dies at a much smaller dose of the first chemical than of the "
        "second",
        "The first chemical is present in the environment for longer than the second",
        "The first chemical is produced in larger quantities than the second",
        "The first chemical dissolves in water and the second does not",
        "The first chemical was discovered earlier than the second"],
      ans=0,
      why="EIN-3.A.1 makes the LD50 the dose lethal to half the population of a species, "
          "so a smaller such dose means the outcome is reached with less material. "
          "Persistence, production, solubility and history are different properties."),

 dict(q="An investigator wants to compare how dangerous a chemical is to two species. "
        "Which method is aligned with the framework's measure?",
      choices=[
        "Determine the dose at which half the population dies separately for each species "
        "and compare the two doses",
        "Determine the dose at which half the population dies for one species and assume "
        "it holds for the other",
        "Count how many individuals of each species live in the study area",
        "Measure how long the chemical stays in the soil at each site",
        "Record which species is easier to catch for testing"],
      ans=0,
      why="EIN-3.A.1 ties the value to a particular species, so a comparison requires the "
          "value to be measured in each. Assuming the value carries over, counting "
          "individuals, timing persistence and noting convenience do not produce a "
          "comparable pair of doses."),

 dict(q="Why does knowing an LD50 not by itself tell a scientist whether a chemical is "
        "harming a wild population?",
      choices=[
        "The value states the dose at which half the population would die, not how much of "
        "the chemical the wild animals are actually receiving",
        "The value cannot be measured for any species that lives in the wild",
        "The value applies only to chemicals that are manufactured rather than natural",
        "The value describes the number of individuals in a population rather than a dose",
        "The value changes every time the population is counted"],
      ans=0,
      why="EIN-3.A.1 defines a dose associated with half a population dying, so applying "
          "it to a wild population also requires knowing the dose those animals receive. "
          "The definition itself says nothing about exposure in the field."),

 dict(q="Which statement about two chemicals with LD50 values of 5 and 5000 milligrams "
        "per kilogram in the same species is best supported?",
      choices=[
        "It takes a thousand times as much of the second chemical to kill half the "
        "population as it does of the first",
        "It takes a thousand times as much of the first chemical to kill half the "
        "population as it does of the second",
        "The two chemicals kill half the population at the same dose",
        "The second chemical kills the whole population at a lower dose",
        "Neither chemical can kill half of any population"],
      ans=0,
      why="EIN-3.A.1 makes each value the dose lethal to half the population, and one "
          "value divided by the other gives the factor between them. The comparison "
          "concerns the dose needed rather than any other property."),

 dict(q="A study reports that a dose killed 90 percent of an exposed group. What can be "
        "said about the LD50 for that population?",
      choices=[
        "The dose that kills half the group is smaller than the dose reported, since a "
        "smaller share dies at a smaller dose",
        "The dose reported is the LD50, since it killed most of the group",
        "The LD50 must be larger than the dose reported",
        "The LD50 cannot exist for this population",
        "The LD50 equals nine tenths of the dose reported"],
      ans=0,
      why="EIN-3.A.1 defines the LD50 as the dose at which half the population dies, and "
          "the reported dose already exceeds that level of mortality, so the fifty percent "
          "point lies at a smaller dose. The framework provides no formula relating the "
          "two."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Lethal dose 50 percent is the dose of a chemical that kills half of an exposed "
        "population of one named species, so a smaller value marks a chemical that is more "
        "toxic to that species and a value measured in one species does not transfer to "
        "another",
        "Lethal dose 50 percent is the dose below which a chemical is safe for every "
        "species",
        "Lethal dose 50 percent is the share of a chemical that an organism absorbs",
        "Lethal dose 50 percent is the same number for every species exposed to a given "
        "chemical",
        "Lethal dose 50 percent is the length of time a chemical remains lethal in the "
        "environment"],
      ans=0,
      why="The keyed summary states EIN-3.A.1 and the two consequences that follow "
          "directly from it. Every rejected summary turns the value into a safety "
          "threshold, an absorbed fraction, a species-independent constant, or a duration."),
]
