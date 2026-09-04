# AP ENVIRONMENTAL SCIENCE 5.17 Sustainable Forestry
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding STB-1: humans can mitigate their impact on land and water
# resources through sustainable use.
# Learning objective STB-1.G, describe methods for mitigating human impact on forests.
# Suggested skill 7.F, justify a proposed solution, by explaining potential advantages.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-1.G.1  Some of the methods for mitigating deforestation include reforestation,
#              using and buying wood harvested by ecologically sustainable forestry
#              techniques, and reusing wood.
#   STB-1.G.2  Methods to protect forests from pathogens and insects include integrated
#              pest management (IPM) and the removal of affected trees.
#   STB-1.G.3  Prescribed burn is a method by which forests are set on fire under
#              controlled conditions in order to reduce the occurrence of natural fires.
#
# SCOPE. Three statements, three lists or definitions, and no mechanism for any of them.
# The framework does not say HOW reforestation restores a forest, how removing affected
# trees checks a pathogen, or how a controlled fire reduces natural ones. Nothing here
# keys a mechanism; the methods are keyed by which statement names them and by what a
# table of measurements shows, and one item keys the absence of any explanation directly.
#
# THE DOUBLE HEDGE IN STB-1.G.1. It reads SOME OF THE METHODS ... INCLUDE, which hedges
# twice over: the list is partial and it is offered as examples. One item keys that, and
# no item here says the three are the only ways to mitigate deforestation.
#
# THE CLAUSE THAT IS EASY TO HALVE. STB-1.G.1 says USING AND BUYING wood harvested by
# ecologically sustainable forestry techniques -- what a person does with the wood and
# what a person pays for. One item turns on it and its anchor carries both verbs.
#
# BOUNDARY WITH 5.2 AND 5.14. Clearcutting and its consequences are EIN-2.C in topic 5.2;
# this topic is the mitigation. Integrated pest management is defined in STB-1.C.1 in
# topic 5.14, where its methods, benefits and drawbacks belong; here it appears only as
# one of the two things STB-1.G.2 names for protecting forests, and one item separates
# the two roles.
#
# BOUNDARY WITH 5.12. Topic 5.12's worked setting for sustainable yield is a forest estate
# compared on annual growth against annual cut. Nothing here reuses that table or that
# question shape; the settings here are a replanting record, a certified against an
# uncertified estate, a timber reuse record, an infestation record, and two prescribed
# burn records.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_17.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.17", "Sustainable Forestry", 5)

_T_REFOREST = dict(
    headers=["Stage of the district record",
             "Forest area (thousand hectares)",
             "Trees planted during the period (millions)"],
    rows=[["Before the programme began", "120", "0"],
          ["Ten years after it began", "148", "31"],
          ["Twenty years after it began", "183", "36"]])

_T_CERTIFIED = dict(
    headers=["Estate supplying the timber",
             "Share of the logged area replanted within two years (percent)",
             "Streams on the estate meeting the water quality standard (percent)"],
    rows=[["Estate selling uncertified timber", "18", "35"],
          ["Estate selling certified timber", "94", "88"]])

_T_REUSE = dict(
    headers=["Practice of the district's building trade",
             "Reclaimed timber used each year (thousand cubic meters)",
             "Newly felled timber bought each year (thousand cubic meters)"],
    rows=[["No old timber reused", "0", "240"],
          ["Some old timber reused", "60", "180"],
          ["Most old timber reused", "150", "90"]])

_T_REMOVAL = dict(
    headers=["Management of the stand after the infestation was found",
             "Affected trees removed in the first season (percent)",
             "Trees infested three seasons later (percent)"],
    rows=[["No affected trees removed", "0", "64"],
          ["Half the affected trees removed", "50", "29"],
          ["Nearly all affected trees removed", "95", "6"]])

_T_BURN = dict(
    headers=["Management of the forest block",
             "Dead wood and litter on the ground (tonnes per hectare)",
             "Area burned by natural fires over ten years (percent of the block)"],
    rows=[["No prescribed burning", "46", "38"],
          ["Prescribed burning carried out", "12", "7"]])

_T_BURN_FREQ = dict(
    headers=["Interval between prescribed burns",
             "Dead wood and litter on the ground (tonnes per hectare)",
             "Natural fires recorded in twenty years"],
    rows=[["No prescribed burns at all", "52", "15"],
          ["A burn every ten years", "27", "6"],
          ["A burn every four years", "11", "3"]])

QUESTIONS = [

 dict(q="Which methods does the course framework name for mitigating deforestation?",
      choices=[
        "Reforestation, using and buying wood harvested by ecologically sustainable "
        "forestry techniques, and reusing wood",
        "Clearcutting, burning the slash, and replacing the forest with pasture",
        "Reforestation, clearcutting, and the removal of affected trees",
        "Contour plowing, terracing, and strip cropping",
        "Biocontrol, intercropping, and crop rotation"],
      ans=0,
      why="STB-1.G.1 names reforestation, using and buying wood harvested by ecologically "
          "sustainable forestry techniques, and reusing wood. Clearcutting is the impact "
          "EIN-2.C describes rather than a mitigation, and the last two lists are STB-1.E.1's "
          "soil conservation methods and STB-1.C.1's pest management methods."),

 dict(q="Which of the following is NOT one of the methods the framework names for mitigating "
        "deforestation?",
      choices=[
        "Clearing a further area of forest to plant a faster-growing crop",
        "Reforestation",
        "Using wood harvested by ecologically sustainable forestry techniques",
        "Buying wood harvested by ecologically sustainable forestry techniques",
        "Reusing wood"],
      ans=0,
      why="STB-1.G.1's methods are reforestation, using and buying sustainably harvested wood, "
          "and reusing wood. Clearing more forest is the deforestation the statement sets out to "
          "mitigate, and every rejected option is quoted from the statement itself."),

 dict(q="The framework's second method for mitigating deforestation names two things a person "
        "may do with sustainably harvested wood. What are they?",
      choices=[
        "Using it and buying it",
        "Using it, but never buying it",
        "Buying it, but never using it",
        "Burning it and replanting it",
        "Exporting it and taxing it"],
      ans=0,
      why="STB-1.G.1 names USING AND BUYING wood harvested by ecologically sustainable forestry "
          "techniques, so the method covers both what a person does with the wood and what a "
          "person pays for. The first two rejected options each keep one and deny the other."),

 dict(q="What does the framework's third method for mitigating deforestation consist of?",
      choices=[
        "Reusing wood",
        "Burning wood for fuel rather than building with it",
        "Replacing wood with concrete in every building",
        "Storing wood without ever using it again",
        "Exporting wood to districts that have none"],
      ans=0,
      why="STB-1.G.1 names REUSING WOOD as its third method. Burning, replacing, storing and "
          "exporting are none of them, and the framework names no substitute material anywhere "
          "in this topic."),

 dict(q="Which methods does the framework name for protecting forests from pathogens and "
        "insects?",
      choices=[
        "Integrated pest management and the removal of affected trees",
        "Prescribed burning and the removal of affected trees",
        "Reforestation and the reuse of wood",
        "Clearcutting and replanting with a single species",
        "Contour plowing and terracing"],
      ans=0,
      why="STB-1.G.2 states that methods to protect forests from pathogens and insects include "
          "INTEGRATED PEST MANAGEMENT (IPM) AND THE REMOVAL OF AFFECTED TREES. Prescribed burning "
          "belongs to STB-1.G.3, whose stated purpose is reducing natural fires rather than "
          "controlling pathogens."),

 dict(q="Which of the following is NOT one of the methods the framework names for protecting "
        "forests from pathogens and insects?",
      choices=[
        "Prescribed burning",
        "Integrated pest management",
        "The removal of affected trees",
        "Taking out the trees an inspection finds to be infested",
        "Combining biological, physical and limited chemical methods against the insects"],
      ans=0,
      why="STB-1.G.2 names integrated pest management and the removal of affected trees. "
          "Prescribed burning is STB-1.G.3, and the framework gives its purpose as reducing the "
          "occurrence of natural fires, not as protecting a forest from pathogens or insects."),

 dict(q="How does the framework define a prescribed burn?",
      choices=[
        "A method by which forests are set on fire under controlled conditions",
        "A method by which natural fires are allowed to run until they die out",
        "A method by which felled timber is burned after it leaves the forest",
        "A method by which affected trees are removed and burned off site",
        "A method by which a forest is cleared entirely and replanted"],
      ans=0,
      why="STB-1.G.3 states that a prescribed burn is a method by which FORESTS ARE SET ON FIRE "
          "UNDER CONTROLLED CONDITIONS. The fire is deliberately set and controlled, which is "
          "what separates it from a natural fire being left to run."),

 dict(q="What purpose does the framework attach to a prescribed burn?",
      choices=[
        "To reduce the occurrence of natural fires",
        "To increase the occurrence of natural fires",
        "To protect the forest from pathogens and insects",
        "To clear ground for planting a crop",
        "To raise the amount of timber a forest yields each year"],
      ans=0,
      why="STB-1.G.3 states that the fire is set IN ORDER TO REDUCE THE OCCURRENCE OF NATURAL "
          "FIRES. Protecting a forest from pathogens and insects is the purpose STB-1.G.2 "
          "attaches to its own two methods, and the framework names no agricultural or yield "
          "purpose here."),

 dict(q="Integrated pest management appears in this topic and has a topic of its own. What "
        "does it do in each place?",
      choices=[
        "Here it is one of two methods for protecting forests from pathogens and insects; "
        "there it is defined as a combination of biological, physical and limited chemical "
        "methods",
        "Here it is defined as a combination of biological, physical and limited chemical "
        "methods; there it is one of two methods for protecting forests",
        "In both places it is a method for mitigating deforestation",
        "In both places it is a method for reducing the occurrence of natural fires",
        "The framework mentions integrated pest management in only one of the two topics"],
      ans=0,
      why="STB-1.G.2 names IPM as one of two methods for protecting forests from pathogens and "
          "insects, while STB-1.C.1 in topic 5.14 supplies its definition and its component "
          "methods. The swap of the naming and the definition is the error worth guarding "
          "against."),

 dict(q="A district's forest was recorded before and after a planting programme. What do the "
        "values show?",
      table=_T_REFOREST,
      choices=[
        "The forest area grew across the record as trees continued to be planted.",
        "The forest area shrank across the record as trees continued to be planted.",
        "The forest area stayed the same across the record.",
        "The forest area grew although no trees were planted at any point.",
        "The largest forest area was recorded before the programme began."],
      ans=0,
      why="Forest area runs 120, 148 and 183 thousand hectares while trees planted run 0, 31 and "
          "36 million across the periods. STB-1.G.1 names reforestation among the methods for "
          "mitigating deforestation."),

 dict(q="Using the same district record, by how much did the forest area grow across the "
        "twenty years?",
      table=_T_REFOREST,
      choices=[
        "By 63 thousand hectares",
        "By 183 thousand hectares",
        "By 303 thousand hectares",
        "By 28 thousand hectares",
        "By 35 thousand hectares"],
      ans=0,
      why="Subtracting the two tabulated areas gives 183 minus 120, which is 63 thousand "
          "hectares. The rejected values quote the final area alone, add the two, or take the "
          "growth over one of the two ten-year intervals."),

 dict(q="Two estates selling timber were compared on how they work their land. Which reading "
        "supports the framework's method of buying sustainably harvested wood?",
      table=_T_CERTIFIED,
      choices=[
        "The certified estate replants far more of what it logs and keeps far more of its "
        "streams within the standard.",
        "The certified estate replants far less of what it logs and keeps far fewer of its "
        "streams within the standard.",
        "The certified estate replants far more of what it logs but keeps far fewer of its "
        "streams within the standard.",
        "The two estates replant the same share of what they log.",
        "The uncertified estate keeps more of its streams within the standard."],
      ans=0,
      why="The certified estate replants 94 percent of the logged area against 18, and 88 "
          "percent of its streams meet the standard against 35. STB-1.G.1 names using and buying "
          "wood harvested by ecologically sustainable forestry techniques as a method for "
          "mitigating deforestation."),

 dict(q="Using the same two estates, how much greater is the share of the logged area the "
        "certified estate replants within two years?",
      table=_T_CERTIFIED,
      choices=[
        "76 percentage points greater",
        "94 percentage points greater",
        "112 percentage points greater",
        "53 percentage points greater",
        "18 percentage points greater"],
      ans=0,
      why="Subtracting the two tabulated shares gives 94 minus 18, which is 76 percentage "
          "points. The rejected values quote the certified estate alone, add the two, take the "
          "difference in the stream column, or quote the uncertified estate alone."),

 dict(q="A district's building trade was recorded under three practices. What relationship do "
        "the values show?",
      table=_T_REUSE,
      choices=[
        "The more reclaimed timber the trade used, the less newly felled timber it bought.",
        "The more reclaimed timber the trade used, the more newly felled timber it bought.",
        "The trade bought the same amount of newly felled timber under all three practices.",
        "The practice using no reclaimed timber bought the least newly felled timber.",
        "Reclaimed timber and newly felled timber cannot be compared in the same units."],
      ans=0,
      why="Reclaimed timber runs 0, 60 and 150 thousand cubic meters while newly felled timber "
          "bought runs 240, 180 and 90. STB-1.G.1 names reusing wood among the methods for "
          "mitigating deforestation."),

 dict(q="Using the same district, how much less newly felled timber is bought each year under "
        "the most thorough reuse than under none at all?",
      table=_T_REUSE,
      choices=[
        "150 thousand cubic meters less",
        "240 thousand cubic meters less",
        "330 thousand cubic meters less",
        "60 thousand cubic meters less",
        "90 thousand cubic meters less"],
      ans=0,
      why="Subtracting the two tabulated purchases gives 240 minus 90, which is 150 thousand "
          "cubic meters. The rejected values quote the unreused case alone, add the two, take "
          "one of the intermediate steps, or quote the reused case alone."),

 dict(q="Three stands in which the same infestation was found were managed differently. What "
        "do the values show?",
      table=_T_REMOVAL,
      choices=[
        "The more of the affected trees were removed at the outset, the fewer trees were "
        "infested three seasons later.",
        "The more of the affected trees were removed at the outset, the more trees were "
        "infested three seasons later.",
        "The share of trees infested three seasons later was the same in all three stands.",
        "The stand from which no affected trees were removed had the fewest infested trees "
        "three seasons later.",
        "Removing affected trees has no measurable effect that could be recorded."],
      ans=0,
      why="Removal runs 0, 50 and 95 percent while the share infested three seasons later runs "
          "64, 29 and 6 percent. STB-1.G.2 names the removal of affected trees among the methods "
          "to protect forests from pathogens and insects."),

 dict(q="Using the same three stands, how much smaller was the share of infested trees where "
        "nearly all affected trees had been removed than where none had?",
      table=_T_REMOVAL,
      choices=[
        "58 percentage points smaller",
        "64 percentage points smaller",
        "70 percentage points smaller",
        "35 percentage points smaller",
        "95 percentage points smaller"],
      ans=0,
      why="Subtracting the two tabulated shares gives 64 minus 6, which is 58 percentage points. "
          "The rejected values quote the untreated stand alone, add the two, compare the wrong "
          "pair of stands, or take a reading from the removal column."),

 dict(q="Two forest blocks of the same kind were managed differently for ten years. Which "
        "reading supports the purpose the framework attaches to a prescribed burn?",
      table=_T_BURN,
      choices=[
        "The block given prescribed burns carried less dead wood and litter and lost less "
        "area to natural fires.",
        "The block given prescribed burns carried more dead wood and litter and lost more "
        "area to natural fires.",
        "The block given prescribed burns carried less dead wood and litter but lost more "
        "area to natural fires.",
        "The two blocks lost the same share of their area to natural fires.",
        "The block with no prescribed burning lost the smaller share of its area to natural "
        "fires."],
      ans=0,
      why="The burned block carries 12 tonnes of dead wood and litter per hectare against 46, "
          "and loses 7 percent of its area to natural fires against 38. STB-1.G.3 gives reducing "
          "the occurrence of natural fires as the purpose of a prescribed burn."),

 dict(q="Using the same two blocks, how much less of its area did the block given prescribed "
        "burns lose to natural fires?",
      table=_T_BURN,
      choices=[
        "31 percentage points less",
        "38 percentage points less",
        "45 percentage points less",
        "34 percentage points less",
        "7 percentage points less"],
      ans=0,
      why="Subtracting the two tabulated shares gives 38 minus 7, which is 31 percentage points. "
          "The rejected values quote the unburned block alone, add the two, take the difference "
          "in the litter column, or quote the burned block alone."),

 dict(q="Three blocks burned at different intervals were watched for twenty years. What "
        "relationship do the values show?",
      table=_T_BURN_FREQ,
      choices=[
        "The more often prescribed burns were carried out, the less litter lay on the ground "
        "and the fewer natural fires were recorded.",
        "The more often prescribed burns were carried out, the more litter lay on the ground "
        "and the more natural fires were recorded.",
        "The three blocks recorded the same number of natural fires.",
        "The block never given a prescribed burn recorded the fewest natural fires.",
        "The litter on the ground fell with more frequent burning but the natural fires rose."],
      ans=0,
      why="Litter runs 52, 27 and 11 tonnes per hectare and natural fires run 15, 6 and 3 as the "
          "interval shortens from never to ten years to four. STB-1.G.3 gives reducing the "
          "occurrence of natural fires as the purpose of a prescribed burn."),

 dict(q="Using the same three blocks, how many natural fires did the unburned block record "
        "compared with the block burned every four years?",
      table=_T_BURN_FREQ,
      choices=[
        "Five times as many",
        "Two times as many",
        "Three times as many",
        "Twelve times as many",
        "The same number"],
      ans=0,
      why="Dividing the two tabulated counts gives 15 divided by 3, which is 5. The rejected "
          "values come from the block burned every ten years, from the difference rather than "
          "the ratio, or from denying that the blocks differ."),

 dict(q="A student writes that a prescribed burn means standing back and letting a wildfire "
        "take its course. Which correction is required?",
      choices=[
        "The framework describes a fire that people set deliberately under controlled "
        "conditions",
        "The framework describes a fire that starts naturally and is left to run, and the "
        "student is correct",
        "The framework describes the burning of timber after it has been taken out of the "
        "forest",
        "The framework describes burning as a way of protecting forests from pathogens",
        "The framework offers no definition of a prescribed burn"],
      ans=0,
      why="STB-1.G.3 states that forests ARE SET ON FIRE UNDER CONTROLLED CONDITIONS, so the "
          "fire is deliberate and managed. Protecting forests from pathogens and insects is "
          "STB-1.G.2's purpose for its own two methods, not this one's."),

 dict(q="A second student writes that the framework's three methods for mitigating "
        "deforestation are the only ones there are. What does the wording of the statement "
        "establish?",
      choices=[
        "The statement gives SOME of the methods and says they INCLUDE these three, so it is "
        "doubly marked as partial",
        "The statement gives all of the methods, so the student is correct",
        "The statement gives one method and treats the other two as examples of it",
        "The statement gives methods for protecting forests from pathogens rather than for "
        "deforestation",
        "The statement gives no methods at all"],
      ans=0,
      why="STB-1.G.1 opens with SOME OF THE METHODS and then says they INCLUDE the three it "
          "names, which marks the list as partial twice over. Nothing in the wording claims "
          "completeness, and the pathogen methods are a separate statement, STB-1.G.2."),

 dict(q="Which observation would most directly show that a reforestation programme had done "
        "what the framework names it for?",
      choices=[
        "The area under forest in the district grew over the years trees were planted",
        "The number of sawmills operating in the district grew over the same years",
        "The price paid for timber in the district rose over the same years",
        "The number of natural fires in the district fell over the same years",
        "The share of trees carrying a pathogen in the district fell over the same years"],
      ans=0,
      why="STB-1.G.1 names reforestation among the methods for mitigating DEFORESTATION, so the "
          "area under forest is the quantity that reports success. Fires belong to STB-1.G.3 and "
          "pathogens to STB-1.G.2, and mills and prices measure neither."),

 dict(q="Which observation would most directly show that prescribed burning had achieved the "
        "purpose the framework gives it?",
      choices=[
        "Fewer natural fires occurred in the block afterwards than had occurred before",
        "More natural fires occurred in the block afterwards than had occurred before",
        "More timber was cut from the block afterwards than had been cut before",
        "Fewer trees in the block carried the pathogen afterwards than before",
        "The area of the block under forest grew afterwards"],
      ans=0,
      why="STB-1.G.3 gives the purpose as reducing THE OCCURRENCE OF NATURAL FIRES, so the count "
          "of natural fires is the quantity that reports success. Timber cut, pathogen loads and "
          "forest area answer to other statements."),

 dict(q="Which pair of measurements would together test the framework's method of removing "
        "affected trees?",
      choices=[
        "The share of affected trees taken out at the outset, and the share of trees infested "
        "some seasons later",
        "The share of affected trees taken out at the outset, and the price the timber "
        "fetched",
        "The share of trees infested some seasons later, and the number of natural fires in "
        "the block",
        "The area of the stand in hectares, and the number of years since it was planted",
        "The dead wood lying on the ground, and the share of the logged area replanted"],
      ans=0,
      why="STB-1.G.2 names the removal of affected trees as a method to protect forests from "
          "pathogens and insects, so a test needs a measure of the removal AND a measure of the "
          "infestation afterwards. Each rejected pair supplies at most one of the two, or tests "
          "a different statement."),

 dict(q="A builder wants to act on the framework's methods for mitigating deforestation "
        "without planting anything. Which course does the framework support?",
      choices=[
        "Buying wood harvested by ecologically sustainable forestry techniques, and reusing "
        "old wood",
        "Buying whichever wood is cheapest, regardless of how it was harvested",
        "Buying wood from the estate that clears the largest area each year",
        "Setting fire to a forest under controlled conditions before buying timber from it",
        "Refusing to use wood of any kind in any building"],
      ans=0,
      why="STB-1.G.1's three methods are reforestation, using and buying sustainably harvested "
          "wood, and reusing wood, so the second and third are open to someone who plants "
          "nothing. Prescribed burning is STB-1.G.3 and serves a different purpose, and the "
          "framework nowhere calls for abandoning wood."),

 dict(q="Which of the following does the framework's statement about prescribed burns NOT "
        "supply?",
      choices=[
        "An account of how a controlled fire reduces the occurrence of natural fires",
        "A definition of what a prescribed burn is",
        "The condition that the fire is set under controlled conditions",
        "The purpose the burn is meant to serve",
        "The fact that it is forests that are set on fire"],
      ans=0,
      why="STB-1.G.3 defines the practice, states the condition and gives the purpose, and stops "
          "there. It offers no mechanism, so an account of how a controlled fire reduces natural "
          "ones would be added rather than read. Each rejected option quotes something the "
          "statement does supply."),

 dict(q="How do this topic's three statements stand in relation to one another?",
      choices=[
        "One lists methods against deforestation, one lists methods against pathogens and "
        "insects, and one defines a burning practice and gives its purpose",
        "One defines a burning practice, one lists methods against deforestation, and the "
        "third repeats the first",
        "All three list methods against deforestation",
        "All three concern pathogens and insects",
        "The three statements concern three different forests and cannot be applied to one "
        "place"],
      ans=0,
      why="STB-1.G.1 addresses deforestation, STB-1.G.2 addresses pathogens and insects, and "
          "STB-1.G.3 defines a prescribed burn and gives reducing natural fires as its purpose. "
          "They are three different threats and one forest can face all three."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Some methods against deforestation include reforestation, using and buying "
        "sustainably harvested wood, and reusing wood; forests are protected from pathogens "
        "and insects by integrated pest management and the removal of affected trees; and a "
        "prescribed burn sets a forest alight under controlled conditions to reduce the "
        "occurrence of natural fires.",
        "The only method against deforestation is reforestation, and a prescribed burn is a "
        "natural fire left to run its course.",
        "Forests are protected from pathogens by prescribed burning, and deforestation is "
        "mitigated by clearcutting.",
        "A prescribed burn is carried out in order to increase the occurrence of natural "
        "fires, and no method against deforestation is named.",
        "The framework names methods against deforestation but attaches no purpose to a "
        "prescribed burn."],
      ans=0,
      why="The keyed summary carries STB-1.G.1's three methods with its hedged wording, "
          "STB-1.G.2's two protection methods, and STB-1.G.3's definition and purpose. Each "
          "rejected summary shortens a list, moves a method to the wrong statement, reverses the "
          "purpose, or denies that a purpose is given."),
]
