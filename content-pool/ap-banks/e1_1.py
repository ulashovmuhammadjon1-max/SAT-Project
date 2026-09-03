# AP ENVIRONMENTAL SCIENCE 1.1 Introduction to Ecosystems
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.A: explain how the availability of resources influences
# species interactions. Suggested skill 1.A, describe environmental concepts and
# processes.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.A.1  In a predator-prey relationship, the predator is an organism that eats
#              another organism (the prey).
#   ERT-1.A.2  Symbiosis is a close and long-term interaction between two species in an
#              ecosystem. Types of symbiosis include mutualism, commensalism, and
#              parasitism.
#   ERT-1.A.3  Competition can occur within or between species in an ecosystem where
#              there are limited resources. Resource partitioning -- using the resources
#              in different ways, places, or at different times -- can reduce the
#              negative impact of competition on survival.
#
# ON THE THREE NAMED TYPES OF SYMBIOSIS. ERT-1.A.2 names mutualism, commensalism and
# parasitism as three types of symbiosis and does not define them. Where an item turns
# on which of the three is at work, the presupposed content is only the minimum that
# naming them as DISTINCT types requires: mutualism benefits both species, commensalism
# benefits one while the other is unaffected, parasitism benefits one at the cost of the
# other. Nothing beyond that is keyed, and every such item is flagged in the verifier's
# claim. No item requires a student to recognise a named species.
#
# ON RESOURCE PARTITIONING. ERT-1.A.3 gives exactly three modes -- different ways,
# different places, different times -- and one consequence, a reduced negative impact of
# competition on survival. Items 5, 6, 7, 18 and 22 each key one mode; no item claims
# partitioning abolishes competition, which the framework does not say.
#
# ON THE DATA. Every table is labelled in the stem and every keyed conclusion is
# recoverable from the table alone and is recomputed in verify_e1_1.py.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science, so a backslash or a slash fraction would reach a student raw.
TOPIC = ("1.1", "Introduction to Ecosystems", 1)

_T_WARBLER = dict(
    headers=["Warbler species", "Mean foraging height in the canopy (meters)",
             "Percent of foraging time spent in the outer needles"],
    rows=[["Species W", "3", "12"],
          ["Species X", "9", "22"],
          ["Species Y", "15", "71"],
          ["Species Z", "17", "40"]])

_T_ACTIVITY = dict(
    headers=["Small mammal", "Captures between midnight and dawn",
             "Captures between dawn and midday"],
    rows=[["Mammal J", "146", "9"],
          ["Mammal K", "11", "132"]])

_T_SEEDS = dict(
    headers=["Finch species", "Mean seed width taken (millimeters)",
             "Percent of seeds taken that were wider than 6 millimeters"],
    rows=[["Finch P", "3.1", "4"],
          ["Finch Q", "8.4", "79"]])

_T_CYCLE = dict(
    headers=["Year of survey", "Hares counted per square kilometer",
             "Lynx counted per hundred square kilometers"],
    rows=[["Year 1", "12", "9"],
          ["Year 2", "48", "14"],
          ["Year 3", "95", "31"],
          ["Year 4", "37", "44"],
          ["Year 5", "10", "18"]])

_T_ALONE = dict(
    headers=["Culture", "Mean cell density of Species M after ten days (cells per milliliter)",
             "Mean cell density of Species N after ten days (cells per milliliter)"],
    rows=[["Species M grown alone", "820", "0"],
          ["Species N grown alone", "0", "760"],
          ["Both species grown together", "310", "290"]])

_T_ROOTS = dict(
    headers=["Prairie plant", "Percent of root mass above 20 centimeters depth",
             "Percent of root mass below 60 centimeters depth"],
    rows=[["Plant R", "88", "2"],
          ["Plant S", "9", "64"]])

_T_BARNACLE = dict(
    headers=["Barnacle species", "Percent cover in the upper shore zone",
             "Percent cover in the lower shore zone"],
    rows=[["Barnacle U", "74", "3"],
          ["Barnacle V", "5", "68"]])

_T_OUTCOME = dict(
    headers=["Pairing", "Change in growth of the first species when paired (percent)",
             "Change in growth of the second species when paired (percent)"],
    rows=[["Pairing 1", "31", "27"],
          ["Pairing 2", "24", "0"],
          ["Pairing 3", "19", "-38"]])

_T_MITE = dict(
    headers=["Group of host beetles", "Mean mites carried per beetle",
             "Mean eggs laid per female beetle"],
    rows=[["Mites removed weekly", "0", "42"],
          ["Mites left in place", "26", "17"]])

_T_FUNCTIONAL = dict(
    headers=["Prey offered per enclosure", "Mean prey eaten per predator per day"],
    rows=[["5", "2"],
          ["10", "5"],
          ["20", "8"],
          ["40", "10"],
          ["80", "11"]])

QUESTIONS = [

 dict(q="A hawk captures a mouse in a meadow and eats it. Which of the following best "
        "describes the relationship between the two organisms?",
      choices=[
        "It is a predator-prey relationship, and the hawk is the predator because it "
        "eats another organism.",
        "It is a predator-prey relationship, and the mouse is the predator because it "
        "was the organism sought.",
        "It is a form of symbiosis, because one organism obtains nutrition from another.",
        "It is a form of competition, because both organisms need energy from the meadow.",
        "It is resource partitioning, because the two organisms use the meadow "
        "differently."],
      ans=0,
      why="ERT-1.A.1 states that in a predator-prey relationship the predator is the "
          "organism that eats another organism, the prey. The hawk does the eating, so "
          "the hawk holds the predator role and the mouse holds the prey role."),

 dict(q="Two species of ant meet once at the edge of their ranges, fight briefly over a "
        "dropped seed, and then separate and do not interact again. A student calls this "
        "symbiosis. What is the best correction?",
      choices=[
        "Symbiosis requires a close and long-term interaction, and a single brief "
        "encounter is neither.",
        "Symbiosis requires that one species eat the other, which did not happen here.",
        "Symbiosis requires three or more species to be involved in the interaction.",
        "Symbiosis requires that the two species belong to the same trophic level.",
        "Symbiosis requires that neither species be harmed, and one ant was injured."],
      ans=0,
      why="ERT-1.A.2 defines symbiosis as a close and long-term interaction between two "
          "species. A one-off contest over a single seed fails the duration condition, "
          "so the label does not apply no matter what the outcome of the fight was."),

 dict(q="A pond holds a limited supply of dissolved oxygen. Which of the following "
        "situations does the framework treat as competition?",
      choices=[
        "Members of one fish species and members of a second fish species both drawing "
        "on the same limited oxygen supply.",
        "Only interactions between members of two different fish species, since members "
        "of one species share their resources.",
        "Only interactions among members of a single fish species, since different "
        "species never need the same resource.",
        "Any interaction in the pond in which one organism consumes another organism.",
        "Any close and long-term association between two of the pond species."],
      ans=0,
      why="ERT-1.A.3 states that competition can occur within or between species where "
          "there are limited resources. The keyed option is the only one that keeps both "
          "cases and ties them to a limited resource."),

 dict(q="Which of the following best describes what resource partitioning does for the "
        "species involved?",
      choices=[
        "It reduces the negative impact of competition on survival by using resources in "
        "different ways, places, or at different times.",
        "It removes competition completely by giving each species a resource no other "
        "species can use at all.",
        "It converts a competitive relationship into a predator-prey relationship.",
        "It increases the total amount of the limited resource present in the ecosystem.",
        "It forces one of the two competing species out of the ecosystem entirely."],
      ans=0,
      why="ERT-1.A.3 names three modes of partitioning, using the resources in different "
          "ways, places, or at different times, and states the effect as reducing the "
          "negative impact of competition on survival. It does not claim competition is "
          "abolished or that the resource base grows."),

 dict(q="The table shows where four warbler species that all eat insects forage in the "
        "same stand of trees. Which conclusion about resource partitioning is best "
        "supported by the table?",
      table=_T_WARBLER,
      choices=[
        "The species divide the same food supply by foraging in different places within "
        "the trees.",
        "The species divide the same food supply by foraging at different times of day.",
        "The species avoid competition by eating foods of completely different kinds.",
        "All four species forage at the same mean height, so no partitioning is shown.",
        "The species with the greatest mean height spends the least time in the outer "
        "needles."],
      ans=0,
      why="The tabulated variable is position within the canopy, so the only mode of "
          "partitioning the data can show is the one ERT-1.A.3 calls using the resource "
          "in different places. The table records no times and no food types."),

 dict(q="Trapping records for two small mammals that eat the same seeds are shown. Which "
        "mode of resource partitioning named in the framework do these data illustrate?",
      table=_T_ACTIVITY,
      choices=[
        "Using the resource at different times.",
        "Using the resource in different places.",
        "Using the resource in different ways.",
        "Neither mammal is partitioning, because both were captured in every period.",
        "Both mammals feed at the same time, so the data show direct competition only."],
      ans=0,
      why="Each mammal was caught overwhelmingly in one half of the day and scarcely in "
          "the other, so the axis on which the two are separated is time. ERT-1.A.3 "
          "names using the resources at different times as one of the three modes."),

 dict(q="Two finch species live on the same island and eat seeds from the same set of "
        "plants. The table gives the seeds each species actually takes. Which statement "
        "is best supported?",
      table=_T_SEEDS,
      choices=[
        "The two finches partition the seed supply by handling seeds of different sizes, "
        "a difference in the way the resource is used.",
        "The two finches partition the seed supply by feeding in different places on the "
        "island.",
        "The two finches partition the seed supply by feeding in different seasons.",
        "The two finches take seeds of the same mean width, so no partitioning occurs.",
        "The finch taking the narrower seeds takes the larger share of seeds wider than "
        "six millimeters."],
      ans=0,
      why="The table separates the two species only by the size of seed handled, which "
          "is a difference in how the shared resource is used rather than where or when. "
          "ERT-1.A.3 lists using the resources in different ways as one of the modes."),

 dict(q="A single population of deer in a fenced reserve grows until browse is scarce, "
        "and the largest animals begin to keep smaller ones away from the remaining "
        "shrubs. Which statement about this situation is accurate?",
      choices=[
        "Competition is occurring within a species, which the framework treats as one of "
        "the two places competition can occur.",
        "Competition cannot be occurring, because all the deer belong to a single "
        "species.",
        "This is symbiosis, because the deer live together over a long period.",
        "This is a predator-prey relationship, because the larger deer take food from "
        "the smaller ones.",
        "This is resource partitioning, because the shrubs are divided among the deer."],
      ans=0,
      why="ERT-1.A.3 states that competition can occur within or between species where "
          "there are limited resources. Browse has become limited and the contest is "
          "among members of one species, which is the within-species case."),

 dict(q="A flowering plant supplies nectar to an insect, and the insect carries pollen "
        "between plants of that species; the association has persisted for many "
        "generations. Which type of symbiosis does this describe?",
      choices=[
        "Mutualism, because both species gain from the association.",
        "Commensalism, because only the insect gains and the plant is unaffected.",
        "Parasitism, because the insect removes a resource from the plant.",
        "Predation, because the insect consumes material produced by the plant.",
        "Competition, because both species require the same nectar."],
      ans=0,
      why="ERT-1.A.2 names mutualism, commensalism and parasitism as distinct types of "
          "symbiosis, and the association described is close, long-term, and profitable "
          "to both partners, which is what distinguishes the first from the other two."),

 dict(q="A small plant grows attached to the bark of a large tree, taking no nutrients "
        "from the tree and causing it no measurable harm, while gaining better access to "
        "light. The association lasts for years. Which type of symbiosis is this?",
      choices=[
        "Commensalism, because one species gains and the other is not measurably "
        "affected.",
        "Mutualism, because the tree gains shelter from the small plant.",
        "Parasitism, because the small plant is attached to a living host.",
        "Predation, because the small plant obtains a resource from another organism.",
        "It is not symbiosis, because the two organisms are not both animals."],
      ans=0,
      why="ERT-1.A.2 makes symbiosis a close and long-term interaction between two "
          "species and names commensalism as one type. Attachment alone does not make an "
          "association parasitic; the stem states no cost to the tree and no benefit "
          "to it."),

 dict(q="A worm lives inside the gut of a mammal for the whole of the mammal's adult "
        "life, absorbing digested food and leaving the mammal thinner but alive. Why "
        "does the framework classify this as symbiosis rather than as predation?",
      choices=[
        "Because the interaction is close and long-term between two species, whereas "
        "predation is one organism eating another.",
        "Because the worm is smaller than the mammal, and predators are always larger "
        "than their prey.",
        "Because the mammal survives, and predation is defined by the death of one "
        "organism within a day.",
        "Because the worm and the mammal are competing for the same limited food supply.",
        "Because the two organisms occupy the same place, which predation never "
        "involves."],
      ans=0,
      why="ERT-1.A.2 defines symbiosis by closeness and duration, and ERT-1.A.1 defines "
          "the predator simply as an organism that eats another organism. The persistent "
          "association is what puts this case under the first statement."),

 dict(q="The table gives counts from five yearly surveys of a hare population and of the "
        "lynx that hunt them. Which statement is best supported by the counts?",
      table=_T_CYCLE,
      choices=[
        "The lynx count reached its highest value one year after the hares reached "
        "theirs.",
        "The lynx count reached its highest value in the same year the hares reached "
        "theirs.",
        "The lynx count reached its highest value one year before the hares reached "
        "theirs.",
        "The lynx count fell in every year of the survey.",
        "The hare count rose in every year of the survey."],
      ans=0,
      why="Reading the two columns, the hare maximum and the lynx maximum fall in "
          "different survey years, with the predator maximum the later of the two. The "
          "remaining options misstate the order or the direction of change."),

 dict(q="Which of the following best states how the availability of a resource "
        "influences competition, according to the framework?",
      choices=[
        "Competition arises where the resource is limited, so scarcity is a condition of "
        "the interaction.",
        "Competition arises only where a resource is unlimited, because more organisms "
        "can then gather.",
        "Competition is unaffected by how much of a resource is present.",
        "Competition occurs only between a predator and its prey over the same food.",
        "Competition occurs only where two species are already in a symbiosis."],
      ans=0,
      why="ERT-1.A.3 places competition in ecosystems where there are limited resources. "
          "The condition of scarcity is written into the statement, which is what the "
          "keyed option preserves and the others drop or reverse."),

 dict(q="Two algal species were grown separately and then together under identical "
        "conditions, with the results shown. Which conclusion is best supported?",
      table=_T_ALONE,
      choices=[
        "Each species reached a lower density when grown with the other than when grown "
        "alone, which is consistent with competition for a limited resource.",
        "Each species reached a higher density when grown with the other, which is "
        "consistent with mutualism.",
        "Species M was unaffected by the presence of Species N.",
        "Species N eliminated Species M from the mixed culture entirely.",
        "The mixed culture held more cells in total than either single culture."],
      ans=0,
      why="Both species fell when placed together relative to being grown alone, and "
          "ERT-1.A.3 makes competition the interaction that arises where two populations "
          "draw on the same limited resource. The other readings contradict the "
          "tabulated densities."),

 dict(q="A researcher wants to test whether two bird species partition a shared food "
        "supply rather than simply competing for it. Which observation would give the "
        "most direct evidence of partitioning?",
      choices=[
        "The two species take the food from different parts of the habitat, at different "
        "hours, or in different forms.",
        "The two species are present in the habitat in roughly equal numbers.",
        "The two species both decline in years when the food supply is small.",
        "One species is consistently larger in body size than the other.",
        "The two species build nests out of the same material."],
      ans=0,
      why="ERT-1.A.3 defines resource partitioning as using the resources in different "
          "ways, places, or at different times, so evidence of partitioning is evidence "
          "of separation along one of those three axes. Equal abundance and shared "
          "nesting material say nothing about how the food is divided."),

 dict(q="Which of the following interactions is NOT symbiosis as the framework defines "
        "it?",
      choices=[
        "A bird chases a second bird of its own species away from a feeding patch for a "
        "few minutes.",
        "A fungus and an alga live intertwined in one body for the life of both.",
        "A bacterium lives permanently in the root nodules of a legume.",
        "A mite spends its entire life cycle attached to a single beetle.",
        "A fish lives among the tentacles of a sea anemone throughout its adult life."],
      ans=0,
      why="ERT-1.A.2 requires a close and long-term interaction between two species. The "
          "keyed case is brief and involves a single species, so it fails both "
          "conditions; each of the others is persistent and involves two species."),

 dict(q="Two lizard species in one desert have partitioned their shared insect supply by "
        "hunting at different hours. A student concludes that the two species no longer "
        "compete at all. What is the best correction to this conclusion?",
      choices=[
        "Partitioning reduces the negative impact of competition on survival rather than "
        "removing competition.",
        "Partitioning always ends competition, so the student is correct as stated.",
        "Partitioning converts competition into a symbiosis between the two lizards.",
        "Partitioning is only possible between members of the same species.",
        "Partitioning increases the number of insects available in the desert."],
      ans=0,
      why="ERT-1.A.3 states that resource partitioning can reduce the negative impact of "
          "competition on survival. It claims a reduction in impact, not the "
          "disappearance of the interaction, and it makes no claim about resource supply."),

 dict(q="Root distribution data for two prairie plants growing in the same soil are "
        "shown. Which statement is best supported by these data?",
      table=_T_ROOTS,
      choices=[
        "The two plants draw water from different depths, which is partitioning the "
        "resource by place.",
        "The two plants draw water at different times of year, which is partitioning the "
        "resource by time.",
        "Both plants concentrate their roots at the same depth, so no partitioning "
        "is shown.",
        "The plant with more shallow roots also has more deep roots.",
        "Neither plant has any roots below sixty centimeters."],
      ans=0,
      why="The columns record only depth, so the axis along which the two plants differ "
          "is position in the soil. ERT-1.A.3 names using the resources in different "
          "places as one of the three modes of partitioning."),

 dict(q="In a lake, a predatory fish is removed and the population of the small fish it "
        "ate rises sharply. Which relationship does this outcome illustrate?",
      choices=[
        "A predator-prey relationship, in which removing the organism that eats the "
        "other releases the second population.",
        "A mutualistic symbiosis, in which each species raised the numbers of the other.",
        "Resource partitioning, in which the two fish had used the lake differently.",
        "Competition within a species, since both fish live in one lake.",
        "Commensalism, since the small fish were unaffected by the predatory fish."],
      ans=0,
      why="ERT-1.A.1 makes the predator the organism that eats another organism, so the "
          "predator's removal lifts the source of mortality on the prey. The tabulated "
          "outcome of the small fish rising is what that relationship predicts."),

 dict(q="Why does the framework treat a close, long-term association between two "
        "individuals of the SAME species as something other than symbiosis?",
      choices=[
        "Because symbiosis is defined as an interaction between two species.",
        "Because members of one species can never interact closely for long periods.",
        "Because interactions within a species are always predator-prey relationships.",
        "Because symbiosis requires that one partner be a plant and the other an animal.",
        "Because symbiosis requires that neither partner obtain any benefit."],
      ans=0,
      why="ERT-1.A.2 specifies two species in the definition of symbiosis, so a "
          "within-species association falls outside it. The framework does allow "
          "within-species interaction, but as competition under ERT-1.A.3."),

 dict(q="Percent cover of two barnacle species on the same rocky shore is shown. Which "
        "statement is best supported by the table?",
      table=_T_BARNACLE,
      choices=[
        "Each species holds most of its cover in a different shore zone, which is "
        "partitioning by place.",
        "Each species holds most of its cover in the same shore zone, so the two do not "
        "partition the shore.",
        "The species with more cover in the upper zone also has more cover in the lower "
        "zone.",
        "Neither species is present in the upper shore zone.",
        "The two species differ in the time of day at which they feed."],
      ans=0,
      why="The two species reach their high cover values in opposite zones of the same "
          "shore, and zone is a matter of position. ERT-1.A.3 names using the resource in "
          "different places as one mode of partitioning; the table records no times."),

 dict(q="Three pairings of species were followed and the change in growth of each partner "
        "when paired is shown. Which pairing best matches the type of symbiosis in which "
        "one species gains while the other is not measurably affected?",
      table=_T_OUTCOME,
      choices=[
        "Pairing 2, because one partner gained and the other showed no change.",
        "Pairing 1, because both partners gained.",
        "Pairing 3, because one partner gained and the other lost.",
        "Pairing 1, because the two gains were nearly equal in size.",
        "None of the pairings, because a gain of zero percent means no interaction "
        "occurred."],
      ans=0,
      why="ERT-1.A.2 names commensalism as a distinct type of symbiosis, and what "
          "distinguishes it from the other two named types is that one partner gains "
          "while the other is unaffected. Only one pairing in the table shows that "
          "pattern of outcomes."),

 dict(q="Beetles carrying a mite were compared with beetles from which the mite was "
        "removed each week. Which conclusion about the interaction is best supported?",
      table=_T_MITE,
      choices=[
        "The mite imposes a cost on the beetle, which fits the type of symbiosis in "
        "which one partner gains at the expense of the other.",
        "The mite benefits the beetle, which fits the type of symbiosis in which both "
        "partners gain.",
        "The mite has no measurable effect on the beetle, which fits the type of "
        "symbiosis in which one partner is unaffected.",
        "The beetle eats the mite, which makes the relationship a predator-prey "
        "relationship.",
        "The two organisms compete, because both were present on the same host."],
      ans=0,
      why="Beetles carrying the mite laid fewer eggs than beetles from which it was "
          "removed, so the association carries a measurable cost to the host. ERT-1.A.2 "
          "names parasitism as the type of symbiosis in which one partner gains at the "
          "other's expense."),

 dict(q="Which of the following is the clearest example of two species competing for a "
        "limited resource in an ecosystem?",
      choices=[
        "Two bird species that both require holes in dead trees for nesting, in a woodlot "
        "with few such holes.",
        "A bird species that nests in tree holes and a fish species that spawns in "
        "gravel in a nearby stream.",
        "A bird that eats insects and the insects it captures from tree bark.",
        "A bacterium living permanently in a bird's gut and assisting its digestion.",
        "Two bird species that migrate along the same route in different months."],
      ans=0,
      why="ERT-1.A.3 requires a shared resource that is limited. Only the keyed pair "
          "needs the same scarce structure; the other pairings describe unshared "
          "resources, a predator-prey relationship, or a symbiosis."),

 dict(q="The table records how many prey a single predator eats per day when different "
        "numbers of prey are made available. Which statement is best supported?",
      table=_T_FUNCTIONAL,
      choices=[
        "The number eaten rises as prey are made more available, but the rise gets "
        "smaller at the higher prey supplies.",
        "The number eaten rises in exact proportion to the number of prey offered "
        "throughout the range tested.",
        "The number eaten falls as more prey are made available.",
        "The number eaten is unchanged across the whole range of prey offered.",
        "The predator eats every prey animal offered at each supply level."],
      ans=0,
      why="Reading down the second column, consumption increases with supply but each "
          "doubling of the supply adds no more than the previous doubling did, so the "
          "response is rising and slowing rather than proportional, flat or falling."),

 dict(q="A biologist argues that resource availability is what determines whether two "
        "species in a habitat compete. Which finding, if true, would most directly "
        "support that argument?",
      choices=[
        "The two species show no measurable effect on each other in years when the shared "
        "food is plentiful, and each grows more slowly in years when it is scarce.",
        "The two species belong to different families and have different body sizes.",
        "The two species have coexisted in the habitat for many centuries.",
        "One of the two species is eaten by a predator that ignores the other.",
        "The two species produce their young in the same month of the year."],
      ans=0,
      why="ERT-1.A.3 conditions competition on limited resources, so the argument "
          "predicts that the effect of each species on the other should appear when the "
          "shared resource is scarce and fade when it is plentiful. Only the keyed "
          "finding tests that prediction."),

 dict(q="Which statement correctly distinguishes the interaction described in ERT-1.A.1 "
        "from the interaction described in ERT-1.A.3?",
      choices=[
        "One involves an organism eating another organism; the other involves organisms "
        "drawing on the same limited resource.",
        "One involves two species only; the other involves one species only.",
        "One requires a close and long-term association; the other requires a brief "
        "encounter.",
        "One occurs only in aquatic ecosystems; the other occurs only on land.",
        "One always benefits both organisms; the other always harms both organisms."],
      ans=0,
      why="ERT-1.A.1 defines predation by the act of eating another organism, while "
          "ERT-1.A.3 defines competition by a shared limited resource and allows it "
          "within or between species. Neither statement restricts the interaction by "
          "habitat or by duration."),

 dict(q="A student writes that mutualism, commensalism and parasitism are three separate "
        "kinds of relationship that have nothing in common. What is the best correction?",
      choices=[
        "All three are types of symbiosis, so all three are close and long-term "
        "interactions between two species.",
        "All three are types of competition, so all three require a limited resource.",
        "All three are types of predation, so in all three one organism eats another.",
        "All three are types of resource partitioning, so all three separate species in "
        "space or time.",
        "The three terms are interchangeable names for a single relationship."],
      ans=0,
      why="ERT-1.A.2 lists the three as types of symbiosis, and symbiosis is defined "
          "there as a close and long-term interaction between two species, so that "
          "definition is what all three share while their outcomes differ."),

 dict(q="A pond that had held one species of duckweed is colonized by a second species "
        "that floats at the same level and uses the same nutrients at the same times. "
        "Which outcome does the framework most directly support predicting?",
      choices=[
        "Competition for the limited nutrients, with no partitioning available to reduce "
        "its impact on survival.",
        "Immediate mutualism, because two species now share the pond surface.",
        "A predator-prey relationship, because one duckweed will consume the other.",
        "Resource partitioning by time, because two species cannot use a pond at once.",
        "No interaction at all, because both species are producers."],
      ans=0,
      why="The two populations draw on the same limited nutrients in the same place and "
          "at the same times, which is the condition ERT-1.A.3 sets for competition and "
          "is also the absence of every mode of partitioning that statement names."),

 dict(q="In one woodland a snake eats frogs, and the same snake is itself eaten by a "
        "hawk. Which statement about the snake is accurate?",
      choices=[
        "The snake is the predator with respect to the frog and the prey with respect to "
        "the hawk, because the roles follow from which organism does the eating.",
        "The snake is the prey in both relationships, because it is smaller than the "
        "hawk.",
        "The snake is the predator in both relationships, because it hunts actively.",
        "The snake is in a symbiosis with the frog, because both live in one woodland.",
        "The snake and the hawk are competitors, because both obtain energy from the "
        "woodland."],
      ans=0,
      why="ERT-1.A.1 assigns the predator role to the organism that eats another "
          "organism, so the role is a property of a particular relationship rather than "
          "of the animal, and one organism can hold either role in different pairings."),
]
