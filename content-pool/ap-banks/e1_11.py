# AP ENVIRONMENTAL SCIENCE 1.11 Food Chains and Food Webs
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ENG-1: Energy can be converted from one form to another.
# Learning objective ENG-1.D: describe food chains and food webs, and their constituent
# members by trophic level. Suggested skill 2.A.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-1.D.1  A food chain depicts the flow of energy and matter from producers
#              (autotrophs) to primary consumers (herbivores) and secondary and tertiary
#              consumers (omnivores and carnivores). Detritivores and decomposers play an
#              essential role in food chains and food webs by returning nutrients to the
#              soil. A food web is a model of an interlocking pattern of food chains that
#              depicts the flow of energy and matter in two or more food chains.
#   ENG-1.D.2  Positive and negative feedback loops can each play a role in food webs.
#              When one species is removed from or added to a specific food web, the rest
#              of the food web can be affected.
#
# WHAT IS DELIBERATELY NOT ASKED. ENG-1.D.2 NAMES positive and negative feedback loops
# and defines neither, and no other statement in units 1 to 4 defines them. So no item
# here asks a student to classify a loop as positive or negative. The feedback items key
# only what ENG-1.D.2 actually asserts: that both kinds can play a role in food webs, and
# that removing or adding one species can affect the rest of the web.
#
# THE CATEGORY NAMES ARE THE FRAMEWORK'S OWN. ENG-1.D.1 supplies each pairing in
# parentheses -- producers are autotrophs, primary consumers are herbivores, secondary and
# tertiary consumers are omnivores and carnivores -- so an item that assigns an organism
# to a category from a table stating what it eats is applying the framework's own labels.
# This is what separates this topic from 1.9, whose items deliberately avoid the category
# names and turn only on the DIRECTION of energy flow.
#
# NO FIGURES ARE REFERENCED. A food web appears as a table of who eats whom, never as a
# diagram the bank cannot show.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.11", "Food Chains and Food Webs", 1)

_T_WEB = dict(
    headers=["Species in one meadow", "What it feeds on"],
    rows=[["Species A", "Sunlight, water and carbon dioxide"],
          ["Species B", "Sunlight, water and carbon dioxide"],
          ["Species C", "Species A and Species B"],
          ["Species D", "Species A only"],
          ["Species E", "Species C and Species D"],
          ["Species F", "Dead remains of every other species"]])

_T_REMOVAL = dict(
    headers=["Species in one pond", "Population before Species K was removed",
             "Population two years after Species K was removed"],
    rows=[["Species J, eaten by Species K", "120", "640"],
          ["Species L, eaten by Species K", "90", "410"],
          ["Species M, the plant eaten by Species J", "2200", "480"],
          ["Species N, unconnected to this chain", "300", "290"]])

_T_DECOMP = dict(
    headers=["Forest plot", "Nutrients returned to the soil in one year "
                            "(kilograms per hectare)",
             "Depth of undecayed litter after five years (centimeters)"],
    rows=[["Untreated plot", "88", "3"],
          ["Plot where decomposers were suppressed", "9", "27"]])

_T_INTRODUCED = dict(
    headers=["Species in one lake", "Population before a new predator was introduced",
             "Population three years after the new predator was introduced"],
    rows=[["Small fish eaten by the new predator", "4800", "700"],
          ["Insect eaten by the small fish", "15000", "62000"],
          ["Plant eaten by the insect", "820", "150"]])

_T_SHAREDPREY = dict(
    headers=["Predator in one grassland", "Share of its diet made up of the same rodent "
                                          "(percent)"],
    rows=[["Predator 1", "71"],
          ["Predator 2", "44"],
          ["Predator 3", "18"]])

_T_DIET = dict(
    headers=["Animal in one woodland", "Percent of its diet that is plant material",
             "Percent of its diet that is animal material"],
    rows=[["Animal 1", "100", "0"],
          ["Animal 2", "55", "45"],
          ["Animal 3", "0", "100"]])

_T_CHAINCOUNT = dict(
    headers=["Feeding link recorded in one estuary", "Who eats whom"],
    rows=[["Link 1", "Species P eats the algae"],
          ["Link 2", "Species Q eats the algae"],
          ["Link 3", "Species R eats Species P"],
          ["Link 4", "Species R eats Species Q"]])

QUESTIONS = [

 dict(q="What does the framework say a food chain depicts?",
      choices=[
        "The flow of energy and matter from producers to primary consumers and then to "
        "secondary and tertiary consumers.",
        "The flow of energy alone, with no movement of matter.",
        "The flow of matter alone, with no movement of energy.",
        "The order in which species arrived in an ecosystem.",
        "The total mass of every species in an ecosystem at one instant."],
      ans=0,
      why="ENG-1.D.1 states that a food chain depicts the flow of energy and matter from "
          "producers to primary consumers and secondary and tertiary consumers, so both "
          "energy and matter are part of what a chain shows."),

 dict(q="Which term does the framework pair with producers?",
      choices=[
        "Autotrophs.",
        "Herbivores.",
        "Omnivores.",
        "Decomposers.",
        "Detritivores."],
      ans=0,
      why="ENG-1.D.1 writes producers with autotrophs in parentheses, which is the "
          "framework's own pairing of the two terms."),

 dict(q="Which term does the framework pair with primary consumers?",
      choices=[
        "Herbivores.",
        "Autotrophs.",
        "Carnivores.",
        "Decomposers.",
        "Detritivores."],
      ans=0,
      why="ENG-1.D.1 writes primary consumers with herbivores in parentheses. Carnivores "
          "appear in the same sentence but are paired with the secondary and tertiary "
          "consumers instead."),

 dict(q="Which terms does the framework pair with secondary and tertiary consumers?",
      choices=[
        "Omnivores and carnivores.",
        "Autotrophs and producers.",
        "Herbivores and autotrophs.",
        "Detritivores and decomposers.",
        "Producers and herbivores."],
      ans=0,
      why="ENG-1.D.1 writes secondary and tertiary consumers with omnivores and carnivores "
          "in parentheses, which is the framework's own pairing."),

 dict(q="What essential role does the framework assign to detritivores and decomposers?",
      choices=[
        "Returning nutrients to the soil.",
        "Converting sunlight into organic compounds.",
        "Occupying the highest trophic level in every food chain.",
        "Removing energy from the ecosystem permanently.",
        "Preventing any species from being added to a food web."],
      ans=0,
      why="ENG-1.D.1 states that detritivores and decomposers play an essential role in "
          "food chains and food webs by returning nutrients to the soil."),

 dict(q="How does the framework define a food web?",
      choices=[
        "As a model of an interlocking pattern of food chains that depicts the flow of "
        "energy and matter in two or more food chains.",
        "As a single food chain drawn with more species in it.",
        "As a list of every species in an ecosystem in order of size.",
        "As a map of where each species lives within an ecosystem.",
        "As a record of how many individuals of each species are present."],
      ans=0,
      why="ENG-1.D.1 states that a food web is a model of an interlocking pattern of food "
          "chains that depicts the flow of energy and matter in two or more food chains."),

 dict(q="At minimum, how many food chains does the framework say a food web depicts?",
      choices=[
        "Two or more.",
        "Exactly one.",
        "Exactly three.",
        "At least ten.",
        "The framework sets no minimum and allows a web with none."],
      ans=0,
      why="ENG-1.D.1 states that a food web depicts the flow of energy and matter in two "
          "or more food chains, which sets the minimum at two."),

 dict(q="What does the framework say about feedback loops in food webs?",
      choices=[
        "Positive and negative feedback loops can each play a role in them.",
        "Only positive feedback loops can play a role in them.",
        "Only negative feedback loops can play a role in them.",
        "Feedback loops play no role in food webs.",
        "Feedback loops replace the flow of energy in food webs."],
      ans=0,
      why="ENG-1.D.2 states that positive and negative feedback loops can each play a role "
          "in food webs, so both kinds are allowed and neither is excluded."),

 dict(q="What does the framework say happens when one species is removed from or added to "
        "a specific food web?",
      choices=[
        "The rest of the food web can be affected.",
        "Only that species is affected, and the rest of the web is unchanged.",
        "The web immediately collapses in every case.",
        "The web gains an extra trophic level in every case.",
        "The direction of energy flow through the web reverses."],
      ans=0,
      why="ENG-1.D.2 states that when one species is removed from or added to a specific "
          "food web, the rest of the food web can be affected. The word can allows an "
          "effect without asserting a collapse in every case."),

 dict(q="The table records what six meadow species feed on. Which species are the "
        "producers?",
      table=_T_WEB,
      choices=[
        "Species A and Species B, which feed on sunlight, water and carbon dioxide.",
        "Species C and Species D, which feed on other species.",
        "Species E only, which feeds on two other consumers.",
        "Species F only, which feeds on dead remains.",
        "All six species, because all of them obtain energy."],
      ans=0,
      why="ENG-1.D.1 places producers, the autotrophs, at the start of a food chain, and "
          "the table identifies exactly two species that build from sunlight, water and "
          "carbon dioxide rather than from another organism."),

 dict(q="Using the same meadow table, which species are best described as primary "
        "consumers?",
      table=_T_WEB,
      choices=[
        "Species C and Species D, whose listed foods are producers and nothing else.",
        "Species A and Species B, which feed on sunlight, water and carbon dioxide.",
        "Species E alone, which feeds on two consumers.",
        "Species F alone, which feeds on dead remains.",
        "Species E and Species F, which feed on other organisms rather than on "
        "producers."],
      ans=0,
      why="ENG-1.D.1 pairs primary consumers with herbivores and places them directly "
          "above the producers, so the species whose listed foods are producers and "
          "nothing else occupy that position. Two species in the table do."),

 dict(q="Using the same meadow table, which species feeds only on other consumers?",
      table=_T_WEB,
      choices=[
        "Species E.",
        "Species C.",
        "Species D.",
        "Species A.",
        "Species B."],
      ans=0,
      why="ENG-1.D.1 places secondary and tertiary consumers above the primary consumers, "
          "and the table shows exactly one species whose listed food items are themselves "
          "consumers rather than producers or dead remains."),

 dict(q="Using the same meadow table, which species is playing the role the framework "
        "assigns to detritivores and decomposers?",
      table=_T_WEB,
      choices=[
        "Species F, which feeds on the dead remains of the others.",
        "Species A, which feeds on sunlight, water and carbon dioxide.",
        "Species C, which feeds on two producers.",
        "Species D, which feeds on one producer.",
        "Species E, which feeds on two consumers."],
      ans=0,
      why="ENG-1.D.1 states that detritivores and decomposers play their essential role by "
          "returning nutrients to the soil, and the species feeding on dead remains is the "
          "one positioned to do that."),

 dict(q="Using the same meadow table, why is the set of feeding relationships best "
        "described as a food web rather than a single food chain?",
      table=_T_WEB,
      choices=[
        "Because more than one chain runs from the producers upward and the chains "
        "interlock through shared species.",
        "Because it contains exactly one chain of six species.",
        "Because every species feeds on every other species.",
        "Because no species feeds on any other species.",
        "Because the species are listed in alphabetical order."],
      ans=0,
      why="ENG-1.D.1 defines a food web as a model of an interlocking pattern of food "
          "chains depicting the flow of energy and matter in two or more food chains, and "
          "the table shows two producers feeding into consumers that share a predator."),

 dict(q="A pond was surveyed before and after one species was removed, as shown. Which "
        "conclusion is best supported?",
      table=_T_REMOVAL,
      choices=[
        "Removing one species changed the populations of several others, while a species "
        "outside that chain barely changed.",
        "Removing one species left every other population unchanged.",
        "Removing one species changed only the population of the plant.",
        "Removing one species raised the population of every other species.",
        "The species unconnected to the chain changed more than the others did."],
      ans=0,
      why="Three tabulated populations moved substantially while the species stated to be "
          "unconnected barely moved. ENG-1.D.2 states that when one species is removed "
          "from a specific food web, the rest of the food web can be affected."),

 dict(q="Using the same pond table, which pattern of change do the two species eaten by "
        "the removed species show?",
      table=_T_REMOVAL,
      choices=[
        "Both rose sharply once the species that ate them was gone.",
        "Both fell sharply once the species that ate them was gone.",
        "One rose and the other fell.",
        "Neither changed measurably.",
        "Both fell to zero within two years."],
      ans=0,
      why="Both tabulated prey populations increased several-fold after the removal. "
          "ENG-1.D.2 states that removing one species from a specific food web can affect "
          "the rest of it, and these are the species it fed on."),

 dict(q="Using the same pond table, what happened to the plant at the base of that chain?",
      table=_T_REMOVAL,
      choices=[
        "It fell substantially, which is consistent with more of the animals that eat it "
        "being present.",
        "It rose substantially, which is consistent with fewer of the animals that eat it "
        "being present.",
        "It was unchanged, because plants are not part of a food web.",
        "It rose to the same level as the species that eats it.",
        "It fell to zero within two years."],
      ans=0,
      why="The plant's tabulated population fell while the population of the species "
          "eating it rose. ENG-1.D.2 states that removing one species from a food web can "
          "affect the rest of the web, and the effect here reaches two links away."),

 dict(q="Two forest plots were compared as shown. Which conclusion is best supported?",
      table=_T_DECOMP,
      choices=[
        "Suppressing decomposers reduced the nutrients returned to the soil and left "
        "undecayed litter piling up.",
        "Suppressing decomposers raised the nutrients returned to the soil.",
        "Suppressing decomposers had no measurable effect on either quantity.",
        "The plot where decomposers were suppressed had the shallower litter layer.",
        "Both plots returned the same quantity of nutrients to the soil."],
      ans=0,
      why="The suppressed plot returned far fewer nutrients and accumulated far deeper "
          "litter. ENG-1.D.1 states that detritivores and decomposers play an essential "
          "role by returning nutrients to the soil."),

 dict(q="A predator new to a lake was introduced and the lake was surveyed as shown. Which "
        "conclusion is best supported?",
      table=_T_INTRODUCED,
      choices=[
        "Adding one species changed populations at more than one level of the web.",
        "Adding one species changed only the population it fed on directly.",
        "Adding one species left every population unchanged.",
        "Adding one species raised every population in the lake.",
        "Adding one species lowered every population in the lake."],
      ans=0,
      why="Three tabulated populations moved, and they sit at three different positions in "
          "the chain. ENG-1.D.2 states that when one species is added to a specific food "
          "web, the rest of the food web can be affected."),

 dict(q="Using the same lake table, which pair of changes did the introduction produce "
        "further down the chain?",
      table=_T_INTRODUCED,
      choices=[
        "The insect eaten by the small fish rose, and the plant eaten by the insect fell.",
        "The insect eaten by the small fish fell, and the plant eaten by the insect rose.",
        "Both the insect and the plant rose.",
        "Both the insect and the plant fell.",
        "Neither the insect nor the plant changed."],
      ans=0,
      why="The tabulated insect population rose and the tabulated plant population fell "
          "over the same period. ENG-1.D.2 allows the effect of adding a species to reach "
          "the rest of the web rather than stopping at its prey."),

 dict(q="A student writes that a food web is simply a food chain with more species in it. "
        "What is the best correction?",
      choices=[
        "A food web is an interlocking pattern of two or more chains, not one longer "
        "chain.",
        "A food web is a single chain that includes decomposers, unlike a food chain.",
        "A food web depicts matter only, while a food chain depicts energy only.",
        "A food web contains no producers, unlike a food chain.",
        "A food web and a food chain are two names for the same model."],
      ans=0,
      why="ENG-1.D.1 defines a food web as a model of an INTERLOCKING PATTERN of food "
          "chains depicting the flow of energy and matter in two or more food chains, so "
          "the difference is the number of chains and how they connect, not the length of "
          "one chain."),

 dict(q="The diets of three woodland animals are shown. Which animal best matches the "
        "term the framework pairs with primary consumers?",
      table=_T_DIET,
      choices=[
        "Animal 1, whose diet is entirely plant material.",
        "Animal 2, whose diet is about half plant and half animal material.",
        "Animal 3, whose diet is entirely animal material.",
        "All three, because all three consume other organisms.",
        "None of the three, because primary consumers eat only producers that are not "
        "plants."],
      ans=0,
      why="ENG-1.D.1 pairs primary consumers with herbivores, and the table identifies "
          "exactly one animal whose diet is entirely plant material. The mixed diet and "
          "the wholly animal diet correspond to the two terms the framework attaches to "
          "the levels above."),

 dict(q="Using the same diet table, which animal best matches the term omnivore as the "
        "framework uses it?",
      table=_T_DIET,
      choices=[
        "Animal 2, which takes a substantial share of both plant and animal material.",
        "Animal 1, which takes plant material only.",
        "Animal 3, which takes animal material only.",
        "All three animals equally.",
        "None of the three, because an omnivore must eat decomposers."],
      ans=0,
      why="ENG-1.D.1 lists omnivores and carnivores together as the terms for secondary "
          "and tertiary consumers, and what distinguishes the first is a diet drawn from "
          "both plant and animal material, which exactly one tabulated animal has."),

 dict(q="Four feeding links recorded in one estuary are shown. Which statement about this "
        "set of links is best supported?",
      table=_T_CHAINCOUNT,
      choices=[
        "The links form more than one chain from the algae upward, and the chains "
        "interlock at a shared predator.",
        "The links form exactly one chain from the algae upward.",
        "The links form no chain at all, because the algae are not eaten.",
        "The links show two predators that never share a food source.",
        "The links show that the algae eat the other species."],
      ans=0,
      why="Two separate species feed on the algae and a single species feeds on both of "
          "them, which is two chains meeting at one point. ENG-1.D.1 defines a food web as "
          "an interlocking pattern of two or more food chains."),

 dict(q="Three predators in one grassland were found to depend on a single rodent to the "
        "extents shown. Which prediction does the framework support if that rodent were "
        "removed?",
      table=_T_SHAREDPREY,
      choices=[
        "All three predators could be affected, with the one most dependent on the rodent "
        "affected most.",
        "Only the predator least dependent on the rodent could be affected.",
        "No predator could be affected, because each has other food.",
        "The predators would be unaffected but the rodent's own food would decline.",
        "Every predator would be affected equally, regardless of its diet."],
      ans=0,
      why="ENG-1.D.2 states that when one species is removed from a specific food web, the "
          "rest of the food web can be affected, and the tabulated dietary shares are what "
          "rank how much of each predator's food supply is at stake."),

 dict(q="Why does the framework describe a food chain as depicting the flow of matter as "
        "well as energy?",
      choices=[
        "Because the material of one organism becomes the material of the organism that "
        "eats it, alongside the energy transferred.",
        "Because matter is created at each step of the chain.",
        "Because energy is a form of matter.",
        "Because a chain depicts matter only in aquatic ecosystems.",
        "Because matter moves in the opposite direction to energy along a chain."],
      ans=0,
      why="ENG-1.D.1 states that a food chain depicts the flow of energy AND MATTER from "
          "producers upward, so feeding moves both quantities along the same links."),

 dict(q="Which observation would best support the claim that decomposers are essential to "
        "an ecosystem in the way the framework describes?",
      choices=[
        "Soils in plots where decomposers are absent receive far fewer nutrients from "
        "dead material than soils where they are present.",
        "Plots where decomposers are absent contain fewer predator species.",
        "Decomposers are present in every ecosystem that has been surveyed.",
        "Decomposers are smaller than the organisms whose remains they use.",
        "Decomposers reproduce more quickly than producers do."],
      ans=0,
      why="ENG-1.D.1 states the essential role of detritivores and decomposers "
          "specifically as returning nutrients to the soil, so the evidence bearing on it "
          "is a measured difference in nutrients returned when they are absent."),

 dict(q="Which statement correctly relates the two claims ENG-1.D.2 makes about food webs?",
      choices=[
        "Both positive and negative feedback loops can operate in a web, and a change to "
        "one species can affect the rest of it.",
        "Only negative feedback loops operate in a web, and a change to one species "
        "affects nothing else.",
        "Feedback loops operate only when a species is removed, never when one is added.",
        "A change to one species affects the rest of the web only if no feedback loops "
        "are present.",
        "Feedback loops and species changes are alternatives, and only one can occur in a "
        "given web."],
      ans=0,
      why="ENG-1.D.2 makes two separate assertions in one statement: positive and negative "
          "feedback loops can each play a role in food webs, and when one species is "
          "removed from or added to a specific food web the rest of the web can be "
          "affected."),

 dict(q="An ecologist wants to model an ecosystem in which several predators share prey "
        "and several prey species share a producer. Which model does the framework "
        "provide for this?",
      choices=[
        "A food web, which models an interlocking pattern of two or more food chains.",
        "A single food chain, which models one linear sequence of feeding.",
        "An age structure diagram, which models the ages of one population.",
        "A biogeochemical cycle, which models the movement of one element.",
        "A climatogram, which models temperature and rainfall through a year."],
      ans=0,
      why="ENG-1.D.1 defines a food web as a model of an interlocking pattern of food "
          "chains depicting the flow of energy and matter in two or more food chains, "
          "which is precisely the situation described."),

 dict(q="Which of the following correctly lists the framework's own pairings of trophic "
        "position with organism type?",
      choices=[
        "Producers with autotrophs, primary consumers with herbivores, and secondary and "
        "tertiary consumers with omnivores and carnivores.",
        "Producers with herbivores, primary consumers with autotrophs, and secondary and "
        "tertiary consumers with decomposers.",
        "Producers with decomposers, primary consumers with carnivores, and secondary and "
        "tertiary consumers with autotrophs.",
        "Producers with omnivores, primary consumers with detritivores, and secondary and "
        "tertiary consumers with herbivores.",
        "Producers with carnivores, primary consumers with omnivores, and secondary and "
        "tertiary consumers with autotrophs."],
      ans=0,
      why="ENG-1.D.1 supplies each pairing in parentheses as it names the levels of a food "
          "chain, and the keyed option reproduces the framework's own three pairings in "
          "the order the sentence gives them."),
]
