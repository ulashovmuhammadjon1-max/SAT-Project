# AP ENVIRONMENTAL SCIENCE 9.9 Endangered Species
# CED effective Fall 2026, Unit 9 Global Change.
# Enduring understanding EIN-4: The health of a species is closely tied to its ecosystem,
# and minor environmental changes can have a large impact.
# Learning objective EIN-4.B: explain how species become endangered and strategies to
# combat the problem. Suggested skill 7.D, use data and evidence to support a potential
# solution.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-4.B.1  A variety of factors can lead to a species becoming threatened with
#              extinction, such as being extensively hunted, having limited diet, being
#              outcompeted by invasive species, or having specific and limited habitat
#              requirements.
#   EIN-4.B.2  Not all species will be in danger of extinction when exposed to the same
#              changes in their ecosystem. Species that are able to adapt to changes in
#              their environment or that are able to move to a new environment are less
#              likely to face extinction.
#   EIN-4.B.3  Selective pressures are any factors that change the behaviors and fitness of
#              organisms within an environment.
#   EIN-4.B.4  Species in a given ecosystem compete for resources like territory, food,
#              mates, and habitat, and this competition may lead to endangerment or
#              extinction.
#   EIN-4.B.5  Strategies to protect animal populations include criminalizing poaching,
#              protecting animal habitats, and legislation.
#
# THIS TOPIC OVERLAPS UNIT 2 AND TOPIC 9.8, AND THE OVERLAP IS HANDLED BY CITATION AND BY
# ANGLE. Habitat loss removing specialists is ERT-2.A.4 (topic 2.1); natural selection and
# adaptation are ERT-2.H (topic 2.6); what an invasive species is, and that it may
# outcompete natives, is EIN-4.A (topic 9.8). Every key here rests on an EIN-4.B statement
# and asks about EXTINCTION RISK -- which species is threatened, and what protects it --
# rather than about the mechanism the other topics own. No item here defines an invasive
# species, defines a specialist, or explains natural selection.
#
# WHAT IS DELIBERATELY NOT KEYED. EIN-4.B.1 offers its four factors with SUCH AS, so item
# 17 keys that they are examples rather than a closed set. EIN-4.B.4 says competition MAY
# lead to endangerment or extinction, so item 10 keys the hedge. EIN-4.B.5 names three
# strategies and gives no measure of how well any of them works, so no key ranks them --
# the protection table reads its own record instead.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("9.9", "Endangered Species", 9)

_T_FACTORS = dict(
    headers=["Species", "Number of different foods it eats",
             "Number of habitat types it can occupy",
             "Percent decline over fifty years"],
    rows=[["Species 1", "1", "1", "78"],
          ["Species 2", "3", "2", "51"],
          ["Species 3", "12", "5", "19"],
          ["Species 4", "26", "9", "3"]])

_T_HUNTING = dict(
    headers=["Species", "Animals taken by hunters each year",
             "Percent change in the population over twenty years"],
    rows=[["Species A", "12,000", "-71"],
          ["Species B", "6,400", "-44"],
          ["Species C", "1,800", "-15"],
          ["Species D", "90", "4"]])

_T_INVASIVE = dict(
    headers=["Stage of the record", "Years since the introduced competitor arrived",
             "Percent of the native population remaining"],
    rows=[["Stage 1", "2", "88"],
          ["Stage 2", "7", "54"],
          ["Stage 3", "14", "23"],
          ["Stage 4", "26", "6"]])

_T_ADAPT = dict(
    headers=["Species", "Range of temperatures it can tolerate (degrees Celsius)",
             "Distance it can disperse in one generation (kilometres)",
             "Percent decline after the same warming"],
    rows=[["Species W", "2", "1", "84"],
          ["Species X", "5", "6", "57"],
          ["Species Y", "11", "40", "22"],
          ["Species Z", "19", "300", "2"]])

_T_COMPETITION = dict(
    headers=["Resource competed for in one ecosystem",
             "Share of it secured by the declining species (percent)",
             "Share of it secured by the competing species (percent)"],
    rows=[["Territory", "18", "62"],
          ["Food", "24", "71"],
          ["Mates", "15", "58"],
          ["Habitat", "21", "66"]])

_T_PRESSURE = dict(
    headers=["Stage of one environment's record",
             "Percent of animals showing the changed behaviour",
             "Mean number of surviving offspring per animal"],
    rows=[["Before the factor appeared", "4", "3.8"],
          ["Five years after", "31", "3.1"],
          ["Ten years after", "62", "2.4"],
          ["Twenty years after", "89", "1.7"]])

_T_PROTECTION = dict(
    headers=["Country", "Years since poaching was made a crime there",
             "Area of protected habitat (thousands of hectares)",
             "Percent change in the protected animal population"],
    rows=[["Country 1", "0", "0", "-38"],
          ["Country 2", "4", "120", "-9"],
          ["Country 3", "9", "430", "17"],
          ["Country 4", "16", "910", "44"]])

QUESTIONS = [

 dict(q="Which factors does the framework name as able to lead to a species becoming "
        "threatened with extinction?",
      choices=[
        "Being extensively hunted, having a limited diet, being outcompeted by invasive "
        "species, and having specific and limited habitat requirements.",
        "Being extensively hunted, having a broad diet, outcompeting invasive species, and "
        "having wide habitat requirements.",
        "Having a limited diet and nothing else that the framework names.",
        "Being extensively hunted and nothing else that the framework names.",
        "Having a large territory, a long life span and few natural predators."],
      ans=0,
      why="EIN-4.B.1 states that a variety of factors can lead to a species becoming "
          "threatened with extinction, such as being extensively hunted, having limited "
          "diet, being outcompeted by invasive species, or having specific and limited "
          "habitat requirements."),

 dict(q="A revision card lists five factors and calls all five framework factors leading "
        "to a species becoming threatened with extinction. Which one is not?",
      choices=[
        "Having an unusually long life span.",
        "Being extensively hunted.",
        "Having a limited diet.",
        "Being outcompeted by invasive species.",
        "Having specific and limited habitat requirements."],
      ans=0,
      why="EIN-4.B.1 names four factors, each of which the four rejected options restates. "
          "Life span appears nowhere in this topic's statements."),

 dict(q="What does the framework say about species exposed to the same changes in their "
        "ecosystem?",
      choices=[
        "Not all of them will be in danger of extinction.",
        "All of them will be in equal danger of extinction.",
        "None of them will be in danger of extinction.",
        "Only the most numerous of them will be in danger of extinction.",
        "Only the species with the broadest diets will be in danger of extinction."],
      ans=0,
      why="EIN-4.B.2 opens by stating that not all species will be in danger of extinction "
          "when exposed to the same changes in their ecosystem, so the same change does "
          "not carry the same risk for every species present."),

 dict(q="Which species does the framework say are less likely to face extinction?",
      choices=[
        "Those able to adapt to changes in their environment, or able to move to a new "
        "environment.",
        "Those unable to adapt to changes in their environment and unable to move to a new "
        "one.",
        "Those with the most specific habitat requirements.",
        "Those that are most extensively hunted.",
        "Those that secure the smallest share of the resources they compete for."],
      ans=0,
      why="EIN-4.B.2 states that species that are able to adapt to changes in their "
          "environment or that are able to move to a new environment are less likely to "
          "face extinction, which names both routes to a lower risk."),

 dict(q="What does the framework say selective pressures are?",
      choices=[
        "Any factors that change the behaviours and fitness of organisms within an "
        "environment.",
        "Any factors that leave the behaviours and fitness of organisms unchanged.",
        "The strategies people use to protect animal populations.",
        "The resources that species in an ecosystem compete for.",
        "The species that have already been driven to extinction in an ecosystem."],
      ans=0,
      why="EIN-4.B.3 states that selective pressures are any factors that change the "
          "behaviors and fitness of organisms within an environment, which makes both the "
          "behaviour and the fitness part of the definition."),

 dict(q="Which resources does the framework say species in an ecosystem compete for?",
      choices=[
        "Territory, food, mates and habitat.",
        "Territory, sunlight, rainfall and soil.",
        "Food, minerals, oxygen and daylight.",
        "Mates and nothing else that the framework names.",
        "Habitat and nothing else that the framework names."],
      ans=0,
      why="EIN-4.B.4 states that species in a given ecosystem compete for resources like "
          "territory, food, mates, and habitat, which is the set the keyed option names in "
          "full."),

 dict(q="What does the framework say that competition may lead to?",
      choices=[
        "Endangerment or extinction.",
        "An increase in the number of species present.",
        "An increase in the resources available.",
        "The arrival of new invasive species.",
        "The criminalizing of poaching."],
      ans=0,
      why="EIN-4.B.4 states that competition for territory, food, mates and habitat may "
          "lead to endangerment or extinction, and attaches no other outcome to it."),

 dict(q="Which strategies to protect animal populations does the framework name?",
      choices=[
        "Criminalizing poaching, protecting animal habitats, and legislation.",
        "Criminalizing poaching, introducing new competitors, and clearing habitat.",
        "Protecting animal habitats and nothing else that the framework names.",
        "Legislation and nothing else that the framework names.",
        "Removing the native species that compete with the protected animal."],
      ans=0,
      why="EIN-4.B.5 states that strategies to protect animal populations include "
          "criminalizing poaching, protecting animal habitats, and legislation, which is "
          "the set the keyed option names."),

 dict(q="A revision card lists four strategies and calls all four framework strategies for "
        "protecting animal populations. Which one is not?",
      choices=[
        "Introducing a competitor to reduce the protected animal's numbers.",
        "Criminalizing poaching.",
        "Protecting animal habitats.",
        "Passing legislation.",
        "Making the killing of the animal a crime."],
      ans=0,
      why="EIN-4.B.5 names criminalizing poaching, protecting animal habitats and "
          "legislation, which the four rejected options restate in one wording or another. "
          "Introducing a competitor appears nowhere among them."),

 dict(q="EIN-4.B.4 says competition MAY lead to endangerment or extinction. What does that "
        "wording establish?",
      choices=[
        "A possible outcome of competition rather than one that always follows.",
        "An outcome that follows from competition in every case.",
        "An outcome the framework treats as ruled out.",
        "An outcome that concerns plants but not animals.",
        "An outcome that follows only where poaching has not been criminalized."],
      ans=0,
      why="The word MAY in EIN-4.B.4 marks endangerment or extinction as a possible "
          "consequence of competition rather than a certain one, so the framework neither "
          "guarantees it nor excludes it."),

 dict(q="A student writes that every species in an ecosystem faces the same risk of "
        "extinction from a given change. What is the clearest correction from the "
        "framework?",
      choices=[
        "Not all species will be in danger of extinction when exposed to the same changes.",
        "Every species will be in danger of extinction when exposed to the same changes, "
        "so the student is right.",
        "No species is ever in danger of extinction from a change in its ecosystem.",
        "Only species that can move to a new environment are in danger.",
        "The framework makes no statement about how risk differs between species."],
      ans=0,
      why="EIN-4.B.2 opens with exactly that denial, and then explains it by pointing to "
          "the species able to adapt or to move, which are less likely to face "
          "extinction."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "A species with a broad diet is more likely to become threatened than one with a "
        "limited diet.",
        "Being extensively hunted can lead to a species becoming threatened with "
        "extinction.",
        "Species able to move to a new environment are less likely to face extinction.",
        "Competition for territory, food, mates and habitat may lead to endangerment.",
        "Criminalizing poaching is among the strategies for protecting animal "
        "populations."],
      ans=0,
      why="EIN-4.B.1 names having limited diet, not a broad one, among the factors leading "
          "to a species becoming threatened, so the keyed option reverses the framework. "
          "The four rejected options restate EIN-4.B.1, EIN-4.B.2, EIN-4.B.4 and "
          "EIN-4.B.5."),

 dict(q="A bird eats one kind of insect only and nests only in one kind of wetland. Which "
        "of the framework's named factors apply to it?",
      choices=[
        "Having a limited diet, and having specific and limited habitat requirements.",
        "Being extensively hunted, and being outcompeted by invasive species.",
        "Having a limited diet only; the framework names nothing about its habitat.",
        "Having specific habitat requirements only; the framework names nothing about "
        "diet.",
        "None of the framework's named factors applies to a bird."],
      ans=0,
      why="EIN-4.B.1 names having limited diet and having specific and limited habitat "
          "requirements among the factors that can lead to a species becoming threatened "
          "with extinction, and this bird is described as carrying both."),

 dict(q="A new predator arrives in a wood. The prey animals begin feeding at different "
        "hours than before, and each raises fewer young than it once did. What is that "
        "predator, in the framework's terms?",
      choices=[
        "A selective pressure, because it is a factor changing both the behaviours and the "
        "fitness of organisms in that environment.",
        "A selective pressure, because it is a factor leaving both the behaviours and the "
        "fitness of organisms unchanged.",
        "A protective strategy, because it is a factor introduced into the environment.",
        "A resource, because the prey animals compete for it.",
        "Nothing the framework names, because the prey animals have not gone extinct."],
      ans=0,
      why="EIN-4.B.3 defines selective pressures as any factors that change the behaviors "
          "and fitness of organisms within an environment, and the account reports a change "
          "in both."),

 dict(q="A country passes a law making it a crime to kill a rare animal. Which of the "
        "framework's named strategies does that measure use?",
      choices=[
        "Criminalizing poaching, and legislation.",
        "Protecting animal habitats, and nothing else.",
        "Introducing a competitor for the rare animal.",
        "Removing the rare animal to a new environment.",
        "None of the framework's named strategies."],
      ans=0,
      why="EIN-4.B.5 names criminalizing poaching and legislation among the strategies to "
          "protect animal populations, and a law making the killing of an animal a crime "
          "is both at once."),

 dict(q="Which evidence would test EIN-4.B.2's claim most directly?",
      choices=[
        "Records of how several species of the same ecosystem fared after one and the same "
        "change, alongside how far each could move or tolerate new conditions.",
        "Records of a single species after a single change.",
        "Records of how many animals of one species hunters take each year.",
        "Records of the resources two species compete for in one ecosystem.",
        "Records of the laws a country has passed to protect its animals."],
      ans=0,
      why="EIN-4.B.2 asserts that species differ in their danger from the same change, and "
          "that the ability to adapt or to move lowers the danger, so the evidence bearing "
          "on it compares several species under one change and measures those two "
          "abilities."),

 dict(q="EIN-4.B.1 introduces its four factors with the words SUCH AS. What does that "
        "establish?",
      choices=[
        "The four are examples of a variety of factors rather than a closed list.",
        "The four are the only factors that can lead to a species becoming threatened.",
        "The four are factors the framework treats as unlikely.",
        "The four apply to plants but not to animals.",
        "The four apply only where poaching has been criminalized."],
      ans=0,
      why="EIN-4.B.1 opens with a variety of factors and then offers four SUCH AS "
          "examples, so the list is illustrative rather than exhaustive and none of the "
          "four is dismissed."),

 dict(q="Four species of one ecosystem were recorded for diet, habitat and decline. What "
        "does the record establish?",
      table=_T_FACTORS,
      choices=[
        "The species with the fewest foods and the fewest habitat types declined the most.",
        "The species with the fewest foods and the fewest habitat types declined the "
        "least.",
        "Diet and habitat breadth are unrelated to decline in this record.",
        "Every species in the record declined by the same amount.",
        "The species eating the most foods declined the most."],
      ans=0,
      why="Sorting the species by the number of foods they eat, and then by the number of "
          "habitat types they occupy, leaves the decline strictly falling each time. "
          "EIN-4.B.1 names having limited diet and having specific and limited habitat "
          "requirements among the factors leading to a species becoming threatened."),

 dict(q="Which of those four species carries the two framework factors this record "
        "measures most strongly?",
      table=_T_FACTORS,
      choices=[
        "Species 1, which eats the fewest foods and occupies the fewest habitat types.",
        "Species 4, which eats the most foods and occupies the most habitat types.",
        "Species 2, which stands second from the bottom on both measures.",
        "Species 3, which stands third on both measures.",
        "All four carry them equally."],
      ans=0,
      why="The smallest entry in the diet column and the smallest in the habitat column "
          "fall in the same row, and so does the largest decline. EIN-4.B.1 names limited "
          "diet and specific and limited habitat requirements among the factors leading to "
          "a species becoming threatened with extinction."),

 dict(q="Four species were recorded for the numbers hunters take each year and for how "
        "their populations changed. What does the record establish?",
      table=_T_HUNTING,
      choices=[
        "The species taken in the largest numbers fell the furthest.",
        "The species taken in the largest numbers rose the furthest.",
        "The numbers taken and the change in population are unrelated in this record.",
        "Every species in the record fell in number.",
        "Every species in the record rose in number."],
      ans=0,
      why="Sorting the species by the numbers hunters take leaves the change in population "
          "strictly falling. EIN-4.B.1 names being extensively hunted among the factors "
          "that can lead to a species becoming threatened with extinction."),

 dict(q="Which of those four hunted species did not fall in number over the twenty years?",
      table=_T_HUNTING,
      choices=[
        "Species D, from which hunters take the smallest number each year.",
        "Species A, from which hunters take the largest number each year.",
        "Species B, from which hunters take the second largest number each year.",
        "Species C, from which hunters take the third largest number each year.",
        "All four fell in number over the twenty years."],
      ans=0,
      why="Exactly one row of the record shows a rise rather than a fall, and it belongs "
          "to the species taken in the smallest numbers. EIN-4.B.1 names extensive hunting "
          "among the factors leading to a species becoming threatened."),

 dict(q="One native species was followed at four stages after an introduced competitor "
        "arrived. What does the record establish?",
      table=_T_INVASIVE,
      choices=[
        "The longer the competitor had been present, the less of the native population "
        "remained.",
        "The longer the competitor had been present, the more of the native population "
        "remained.",
        "The native population held steady across the four stages.",
        "The native population recovered after the second stage.",
        "The competitor had been present for the same time at every stage."],
      ans=0,
      why="Reading down the two columns in stage order, the years rise at every step and "
          "the share of the native population remaining falls at every step. EIN-4.B.1 "
          "names being outcompeted by invasive species among the factors that can lead to "
          "a species becoming threatened with extinction."),

 dict(q="At which stage of that same record is the native population smallest, and what "
        "accompanies it?",
      table=_T_INVASIVE,
      choices=[
        "Stage 4, at which the competitor had been present longest.",
        "Stage 1, at which the competitor had been present for the shortest time.",
        "Stage 2, at which the competitor had been present for seven years.",
        "Stage 3, at which more than a fifth of the native population remained.",
        "The native population is the same size at every stage."],
      ans=0,
      why="The smallest share remaining and the longest time since the competitor arrived "
          "fall in the same row. EIN-4.B.1 names being outcompeted by invasive species "
          "among the factors leading to a species becoming threatened."),

 dict(q="Four species of one ecosystem met the same warming and were recorded for what "
        "they can tolerate, how far they can move, and how far they fell. What does the "
        "record establish?",
      table=_T_ADAPT,
      choices=[
        "The species able to bear a wider range of conditions and to move further fell "
        "least, so the same change did not endanger all four alike.",
        "The species able to bear a wider range of conditions and to move further fell "
        "most, so the same change endangered them alike.",
        "All four species fell by the same amount under the same warming.",
        "Tolerance and dispersal are unrelated to the decline in this record.",
        "The species able to move furthest fell the furthest."],
      ans=0,
      why="Sorting the species by the range of conditions they tolerate, and then by how "
          "far they can disperse, leaves the decline strictly falling each time, and the "
          "four declines differ. EIN-4.B.2 states that not all species will be in danger "
          "of extinction from the same change, and that species able to adapt or to move "
          "are less likely to face extinction."),

 dict(q="Which of those four species does the framework place at the lowest risk of "
        "extinction?",
      table=_T_ADAPT,
      choices=[
        "Species Z, which bears the widest range of conditions and disperses furthest.",
        "Species W, which bears the narrowest range of conditions and disperses least.",
        "Species X, which stands second from the bottom on both measures.",
        "Species Y, which stands third on both measures.",
        "All four stand at the same risk, because all four met the same warming."],
      ans=0,
      why="EIN-4.B.2 states that species able to adapt to changes in their environment or "
          "able to move to a new environment are less likely to face extinction, and one "
          "row of the record leads on both abilities and shows the smallest decline."),

 dict(q="Two species of one ecosystem were compared for the share each secured of four "
        "resources. What does the record establish?",
      table=_T_COMPETITION,
      choices=[
        "The declining species secured a smaller share than its competitor of every "
        "resource recorded.",
        "The declining species secured a larger share than its competitor of every "
        "resource recorded.",
        "The two species secured equal shares of every resource recorded.",
        "The declining species secured the larger share of the food but not of the "
        "others.",
        "The record covers only one resource, so no comparison can be drawn."],
      ans=0,
      why="Reading across each row, the declining species' share is the smaller in every "
          "case, and the four resources are the ones EIN-4.B.4 names: territory, food, "
          "mates and habitat. That statement adds that such competition may lead to "
          "endangerment or extinction."),

 dict(q="One environment was recorded before and after a new factor appeared, for the "
        "behaviour of its animals and for the young they raise. What does the record "
        "establish?",
      table=_T_PRESSURE,
      choices=[
        "The factor changed both the behaviour of the animals and the number of young they "
        "raise, which is what the framework calls a selective pressure.",
        "The factor changed the behaviour of the animals but left the number of young they "
        "raise unchanged.",
        "The factor changed the number of young the animals raise but left their behaviour "
        "unchanged.",
        "The factor left both the behaviour and the number of young unchanged.",
        "The factor raised both the share showing the changed behaviour and the number of "
        "young raised."],
      ans=0,
      why="Reading down the two columns in stage order, the share showing the changed "
          "behaviour rises at every step while the surviving offspring fall at every step. "
          "EIN-4.B.3 defines selective pressures as any factors that change the behaviors "
          "and fitness of organisms within an environment."),

 dict(q="Four countries were recorded for how long poaching has been a crime there, how "
        "much habitat they protect, and how their protected animal populations changed. "
        "What does the record establish?",
      table=_T_PROTECTION,
      choices=[
        "The countries that have criminalized poaching for longer and protect more habitat "
        "record the better outcomes for the animals.",
        "The countries that have criminalized poaching for longer and protect more habitat "
        "record the worse outcomes for the animals.",
        "The length of the ban and the area protected are unrelated to the outcome here.",
        "Every country in the record shows a rise in its protected animal population.",
        "Every country in the record shows a fall in its protected animal population."],
      ans=0,
      why="Sorting the countries by the years since poaching was criminalized, and then by "
          "the area of protected habitat, leaves the change in the animal population "
          "strictly rising each time. EIN-4.B.5 names criminalizing poaching and "
          "protecting animal habitats among the strategies to protect animal populations."),

 dict(q="Which of those four countries records the largest rise in its protected animal "
        "population?",
      table=_T_PROTECTION,
      choices=[
        "Country 4, which has criminalized poaching longest and protects the most habitat.",
        "Country 1, which has not criminalized poaching and protects no habitat.",
        "Country 2, which has criminalized poaching for four years.",
        "Country 3, which protects four hundred and thirty thousand hectares.",
        "All four record the same change in their populations."],
      ans=0,
      why="The largest change in the population column, the longest ban and the largest "
          "protected area all fall in the same row. EIN-4.B.5 names both of those measures "
          "among the strategies to protect animal populations."),

 dict(q="Which single sentence collects what this topic's five statements assert and "
        "nothing further?",
      choices=[
        "A variety of factors, such as heavy hunting, a limited diet, being outcompeted by "
        "invasive species and specific habitat requirements, can leave a species threatened "
        "with extinction; not all species face the same danger from one change, and those "
        "able to adapt or to move face less; selective pressures are factors changing "
        "behaviour and fitness; competition for territory, food, mates and habitat may "
        "lead to endangerment or extinction; and criminalizing poaching, protecting "
        "habitats and legislation are strategies for protecting animals.",
        "Only heavy hunting can leave a species threatened with extinction; every species "
        "faces the same danger from one change; selective pressures leave behaviour "
        "unchanged; competition always leads to extinction; and the framework names no "
        "strategy for protecting animals.",
        "A limited diet protects a species from extinction, and species unable to move are "
        "the least likely to face it.",
        "The framework names the factors leading to extinction but says nothing about how "
        "species differ in their danger or how they might be protected.",
        "Competition for resources is the only factor the framework names, and legislation "
        "is the only strategy it names."],
      ans=0,
      why="EIN-4.B.1 supplies the four illustrative factors, EIN-4.B.2 the difference in "
          "danger and the two things that lower it, EIN-4.B.3 the definition of a "
          "selective pressure, EIN-4.B.4 the resources competed for and the possible "
          "outcome, and EIN-4.B.5 the three strategies."),
]
