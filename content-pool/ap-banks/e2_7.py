# AP ENVIRONMENTAL SCIENCE 2.7 Ecological Succession
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: ecosystems have structure and diversity that change over
# time.
# Learning objectives ERT-2.I, describe ecological succession, and ERT-2.J, describe the
# effect of ecological succession on ecosystems. Suggested skill 5.C, explain patterns and
# trends in data to draw conclusions.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.I.1  There are two main types of ecological succession: primary and secondary
#              succession.
#   ERT-2.I.2  A keystone species in an ecosystem is a species whose activities have a
#              particularly significant role in determining community structure.
#   ERT-2.I.3  An indicator species is a plant or animal that, by its presence, abundance,
#              scarcity, or chemical composition, demonstrates that some distinctive aspect
#              of the character or quality of an ecosystem is present.
#   ERT-2.J.1  Pioneer members of an early successional species commonly move into
#              unoccupied habitat and over time adapt to its particular conditions, which
#              may result in the origin of new species.
#   ERT-2.J.2  Succession in a disturbed ecosystem will affect the total biomass, species
#              richness, and net productivity over time.
# Unit 2 overview, same CED: "Ecological succession can occur in terrestrial and aquatic
# ecosystems in both developed and developing areas."
#
# THE BIGGEST TRAP IN THIS TOPIC IS WHAT ERT-2.I.1 DOES NOT SAY. It names two main types,
# primary and secondary, and it DEFINES NEITHER. It says nothing about bare rock, about
# soil being present or absent, or about which type follows which kind of disturbance. So
# no item here asks a student to sort a case into primary or secondary succession, and no
# key states a distinguishing feature. Items 1 and 2 ask only what the two are called.
#
# ERT-2.J.2 NAMES EXACTLY THREE QUANTITIES -- total biomass, species richness, and net
# productivity -- and says succession WILL affect them over time. It does not say in which
# direction any of the three moves, so every keyed direction here is read off the table in
# front of the student and the claim says so.
#
# ERT-2.J.1's hedges are load-bearing: pioneers COMMONLY move into unoccupied habitat, and
# the adaptation MAY result in the origin of new species. Item 10 keys that.
#
# KEYSTONE AND INDICATOR INVITE THE SWAP, and the unit overview singles the pair out as a
# distinction students confuse. The anchor for item 7 in verify_e2_7.py therefore carries
# BOTH clauses, because either alone matches the swapped distractor as readily as the key.
#
# NO FIGURES. Every quantitative item carries a table=, recomputed in verify_e2_7.py from
# that table alone.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("2.7", "Ecological Succession", 2)

_T_SUCCESSION = dict(
    headers=["Years since the disturbance", "Total biomass (tonnes per hectare)",
             "Species richness (number of species present)",
             "Net primary productivity (grams per square metre per year)"],
    rows=[["1", "2", "9", "150"],
          ["10", "28", "31", "640"],
          ["40", "96", "58", "1120"],
          ["80", "210", "47", "880"]])

_T_KEYSTONE = dict(
    headers=["Stage of the removal experiment", "Species present on the shore",
             "Percent of the rock covered by one mussel"],
    rows=[["Before the predator was removed", "15", "28"],
          ["Two years after it was removed", "8", "71"],
          ["Five years after it was removed", "5", "89"]])

_T_TWOREMOVALS = dict(
    headers=["Species removed from a stretch of the same shore",
             "Species present before the removal",
             "Species present three years after the removal"],
    rows=[["Species P", "15", "5"],
          ["Species Q", "15", "14"],
          ["Species R", "15", "15"]])

_T_LICHEN = dict(
    headers=["Site", "Sulfur dioxide in the air (micrograms per cubic metre)",
             "Lichen thalli counted on ten trees"],
    rows=[["Site 1", "4", "240"],
          ["Site 2", "18", "96"],
          ["Site 3", "45", "21"],
          ["Site 4", "90", "0"]])

_T_MERCURY = dict(
    headers=["Lake", "Mercury in the lake sediment (milligrams per kilogram)",
             "Mercury in the tissue of one fish species (milligrams per kilogram)"],
    rows=[["Lake 1", "0.05", "0.2"],
          ["Lake 2", "0.30", "1.1"],
          ["Lake 3", "0.90", "3.4"],
          ["Lake 4", "2.10", "7.8"]])

_T_PIONEER = dict(
    headers=["Years since the lava flow cooled", "Plant species growing on it"],
    rows=[["3", "2"],
          ["15", "11"],
          ["50", "29"],
          ["120", "46"]])

QUESTIONS = [

 dict(q="How many main types of ecological succession does the framework name, and what "
        "are they called?",
      choices=[
        "Two, called primary and secondary succession.",
        "Three, called primary, secondary and tertiary succession.",
        "Two, called pioneer and climax succession.",
        "Four, called primary, secondary, aquatic and terrestrial succession.",
        "One, called ecological succession."],
      ans=0,
      why="ERT-2.I.1 states that there are two main types of ecological succession: primary "
          "and secondary succession. The framework gives the count and the two names and "
          "nothing more."),

 dict(q="A revision card lists three types of ecological succession and calls all three "
        "framework types. Which one is not?",
      choices=["Tertiary succession", "Primary succession", "Secondary succession",
               "Both primary and secondary are framework types",
               "Neither primary nor secondary is a framework type"],
      ans=0,
      why="ERT-2.I.1 names two main types, primary and secondary. Tertiary succession is "
          "not among them, so a card carrying three names has one too many."),

 dict(q="What does the framework say a keystone species is?",
      choices=[
        "A species whose activities have a particularly significant role in determining "
        "community structure.",
        "A species that makes up the largest share of the biomass in its ecosystem.",
        "A species that is found in no other ecosystem.",
        "A species whose presence or scarcity reveals the quality of its ecosystem.",
        "A species that arrives first when bare ground becomes available."],
      ans=0,
      why="ERT-2.I.2 states that a keystone species is a species whose activities have a "
          "particularly significant role in determining community structure. The criterion "
          "is the effect of its activities, not its abundance, its rarity, its usefulness "
          "as a signal or the order in which it arrives."),

 dict(q="What does the framework say an indicator species is?",
      choices=[
        "A plant or animal that demonstrates that some distinctive aspect of the character "
        "or quality of an ecosystem is present.",
        "A plant or animal whose activities determine the structure of its community.",
        "A plant or animal that is the first to colonise unoccupied ground.",
        "A plant or animal that has no close relatives anywhere else.",
        "A plant or animal that contributes most of an ecosystem's net productivity."],
      ans=0,
      why="ERT-2.I.3 states that an indicator species is a plant or animal that "
          "demonstrates that some distinctive aspect of the character or quality of an "
          "ecosystem is present. Its role is to reveal a condition, not to determine the "
          "community or to colonise first."),

 dict(q="By which properties does the framework say an indicator species can demonstrate "
        "that condition?",
      choices=[
        "Its presence, abundance, scarcity or chemical composition.",
        "Its presence, its size and its lifespan.",
        "Its abundance, its migration distance and its diet.",
        "Its chemical composition and its position in the food web only.",
        "Its scarcity and the number of offspring it produces."],
      ans=0,
      why="ERT-2.I.3 lists presence, abundance, scarcity, and chemical composition as the "
          "four properties by which an indicator species demonstrates something about its "
          "ecosystem. Each rejected set replaces at least one of the four."),

 dict(q="What is it that an indicator species demonstrates, according to the framework?",
      choices=[
        "That some distinctive aspect of the character or quality of an ecosystem is "
        "present.",
        "That the ecosystem has reached the end of succession.",
        "That the ecosystem holds more species than a neighbouring one.",
        "That the ecosystem's community structure is determined by that species.",
        "That the ecosystem will recover from any disturbance."],
      ans=0,
      why="ERT-2.I.3 states that an indicator species demonstrates that some distinctive "
          "aspect of the character or quality of an ecosystem is present. It is a signal "
          "about a condition, and the framework attaches no other conclusion to it."),

 dict(q="How do the framework's two definitions separate a keystone species from an "
        "indicator species?",
      choices=[
        "A keystone species has a significant role in determining community structure, "
        "while an indicator species demonstrates a condition of the ecosystem.",
        "A keystone species demonstrates a condition of the ecosystem, while an indicator "
        "species has a significant role in determining community structure.",
        "Both determine community structure, and they differ only in size.",
        "Both demonstrate a condition of the ecosystem, and they differ only in whether they "
        "are plants or animals.",
        "A keystone species determines community structure, while an indicator species is "
        "always the most abundant species present."],
      ans=0,
      why="ERT-2.I.2 defines a keystone species by the significant role its activities play "
          "in determining community structure, and ERT-2.I.3 defines an indicator species "
          "by its demonstrating that some distinctive aspect of an ecosystem is present. "
          "The rejected options exchange the two definitions or collapse them together."),

 dict(q="What does the framework say pioneer members of an early successional species "
        "commonly do?",
      choices=[
        "They move into unoccupied habitat and over time adapt to its particular "
        "conditions.",
        "They move into habitat already fully occupied and displace what is there.",
        "They remain where they are and wait for conditions to change around them.",
        "They move into unoccupied habitat and leave it unchanged for many centuries.",
        "They move between habitats each season without settling in either."],
      ans=0,
      why="ERT-2.J.1 states that pioneer members of an early successional species commonly "
          "move into unoccupied habitat and over time adapt to its particular conditions. "
          "Both the unoccupied habitat and the adaptation over time are the framework's own "
          "words."),

 dict(q="What does the framework say that adaptation by pioneer members may result in?",
      choices=[
        "The origin of new species.",
        "The extinction of every species already present.",
        "A permanent halt to further succession.",
        "The return of the habitat to bare ground.",
        "An immediate rise in the ecosystem's net productivity."],
      ans=0,
      why="ERT-2.J.1 states that pioneers move into unoccupied habitat and over time adapt "
          "to its particular conditions, which may result in the origin of new species. "
          "That is the only outcome the statement attaches to the adaptation."),

 dict(q="ERT-2.J.1 says pioneers COMMONLY move into unoccupied habitat and that the "
        "adaptation MAY result in new species. What do those two words establish?",
      choices=[
        "That the movement is usual rather than universal, and that the new species is "
        "possible rather than certain.",
        "That the movement is universal and the new species certain.",
        "That the movement is rare and the new species certain.",
        "That neither the movement nor the new species has ever been observed.",
        "That the movement is usual and that new species never arise from it."],
      ans=0,
      why="Commonly describes what usually happens without covering every case, and may "
          "asserts possibility rather than necessity. Each rejected option hardens one of "
          "the two hedges or denies the claim outright."),

 dict(q="Which three quantities does the framework say succession in a disturbed ecosystem "
        "will affect over time?",
      choices=[
        "Total biomass, species richness and net productivity.",
        "Total biomass, soil depth and rainfall.",
        "Species richness, net productivity and the number of predators.",
        "Total biomass, species richness and the area of the ecosystem.",
        "Net productivity, soil pH and the length of the growing season."],
      ans=0,
      why="ERT-2.J.2 states that succession in a disturbed ecosystem will affect the total "
          "biomass, species richness, and net productivity over time. Those three are the "
          "statement's own list, and each rejected set swaps at least one of them."),

 dict(q="Which of these is NOT one of the quantities ERT-2.J.2 says succession will affect?",
      choices=[
        "The mineral composition of the bedrock beneath the ecosystem.",
        "The total biomass of the ecosystem.",
        "The species richness of the ecosystem.",
        "The net productivity of the ecosystem.",
        "All four are named by the statement."],
      ans=0,
      why="ERT-2.J.2 names total biomass, species richness and net productivity. The "
          "geology beneath the ecosystem is not among the three, so it is the quantity the "
          "statement does not cover."),

 dict(q="Where does this unit of the framework say ecological succession can occur?",
      choices=[
        "In terrestrial and aquatic ecosystems alike, and in developed as well as "
        "developing areas.",
        "In terrestrial ecosystems only, and only in developing areas.",
        "In aquatic ecosystems only, and only in developed areas.",
        "Only in ecosystems that have never been disturbed by people.",
        "Only in ecosystems lying outside any country's borders."],
      ans=0,
      why="The unit's own overview states that ecological succession can occur in "
          "terrestrial and aquatic ecosystems in both developed and developing areas, which "
          "places no restriction of habitat or of country on where it happens."),

 dict(q="One disturbed ecosystem was measured four times over eighty years. What does the "
        "record establish about the three quantities?",
      table=_T_SUCCESSION,
      choices=[
        "All three changed over the eighty years rather than holding steady.",
        "All three held steady over the eighty years.",
        "Only the total biomass changed; the other two held steady.",
        "Only the species richness changed; the other two held steady.",
        "The record reports none of the three quantities."],
      ans=0,
      why="Biomass runs 2, 28, 96 and 210 tonnes per hectare, richness runs 9, 31, 58 and "
          "47 species, and net productivity runs 150, 640, 1,120 and 880 grams per square "
          "metre per year, so none of the three is constant. ERT-2.J.2 states that "
          "succession in a disturbed ecosystem will affect exactly those three quantities "
          "over time."),

 dict(q="By how much did the total biomass of that ecosystem change between the first "
        "measurement and the last?",
      table=_T_SUCCESSION,
      choices=["It rose by 208 tonnes per hectare", "It rose by 210 tonnes per hectare",
               "It rose by 114 tonnes per hectare", "It fell by 208 tonnes per hectare",
               "It did not change"],
      ans=0,
      why="Biomass stands at 2 tonnes per hectare after one year and 210 after eighty, and "
          "210 less 2 is 208. ERT-2.J.2 names total biomass among the quantities succession "
          "affects, and the size of the change is read from the record."),

 dict(q="At which measurement was the species richness of that recovering ecosystem "
        "highest?",
      table=_T_SUCCESSION,
      choices=["At forty years", "At one year", "At ten years", "At eighty years",
               "Richness was the same at every measurement"],
      ans=0,
      why="The richness figures are 9, 31, 58 and 47 species, and the largest is the third "
          "of them. ERT-2.J.2 says succession will affect species richness over time but "
          "gives no direction, so the direction is read from the record."),

 dict(q="Between the fortieth and the eightieth year of that record, which of the three "
        "quantities rose and which fell?",
      table=_T_SUCCESSION,
      choices=[
        "Total biomass rose while species richness and net productivity both fell.",
        "All three rose.",
        "All three fell.",
        "Species richness rose while total biomass and net productivity both fell.",
        "Net productivity rose while total biomass and species richness both fell."],
      ans=0,
      why="Between those two measurements biomass moves from 96 to 210 tonnes per hectare, "
          "richness from 58 to 47 species and net productivity from 1,120 to 880 grams per "
          "square metre per year. ERT-2.J.2 states that succession affects all three but "
          "assigns no direction to any of them, so each direction here is taken from the "
          "record."),

 dict(q="A predator was removed from a rocky shore and the shore was surveyed twice "
        "afterwards. What does the record establish?",
      table=_T_KEYSTONE,
      choices=[
        "The number of species fell while a single mussel took over more and more of the "
        "rock.",
        "The number of species rose while a single mussel took over more and more of the "
        "rock.",
        "The number of species fell while the mussel's cover also fell.",
        "Neither the number of species nor the mussel's cover changed.",
        "The mussel disappeared from the shore after the predator was removed."],
      ans=0,
      why="Species present run 15, 8 and 5 while the mussel's cover runs 28, 71 and 89 "
          "percent, so one falls throughout and the other rises throughout. ERT-2.I.2 "
          "defines a keystone species by the particularly significant role its activities "
          "play in determining community structure, which is what the removal reveals here."),

 dict(q="Across that removal experiment, by what share did the number of species on the "
        "shore fall?",
      table=_T_KEYSTONE,
      choices=["By two thirds", "By one third", "By one half", "By nine tenths",
               "It did not fall"],
      ans=0,
      why="The shore holds 15 species before the removal and 5 five years after, so ten of "
          "the fifteen are gone. The share is arithmetic on two entries in one column."),

 dict(q="Three species were removed one at a time from comparable stretches of the same "
        "shore. Which removal points to a keystone species as the framework defines one?",
      table=_T_TWOREMOVALS,
      choices=["The removal of Species P", "The removal of Species Q",
               "The removal of Species R", "All three removals equally",
               "None of the three removals"],
      ans=0,
      why="Removing the first species leaves 5 of the original 15, removing the second "
          "leaves 14 and removing the third leaves all 15. ERT-2.I.2 defines a keystone "
          "species by the particularly significant role its activities play in determining "
          "community structure, and only one of these three removals changes the community "
          "substantially."),

 dict(q="Lichens were counted at four sites differing in air quality. What does the record "
        "establish?",
      table=_T_LICHEN,
      choices=[
        "Fewer lichens were counted where the sulfur dioxide concentration was higher.",
        "More lichens were counted where the sulfur dioxide concentration was higher.",
        "The same number of lichens was counted at every site.",
        "Lichen counts and sulfur dioxide concentrations are unrelated across the sites.",
        "The site with the most sulfur dioxide carried the most lichens."],
      ans=0,
      why="Ordered by sulfur dioxide the lichen counts run 240, 96, 21 and 0, falling at "
          "every step. ERT-2.I.3 states that an indicator species demonstrates by its "
          "abundance or scarcity that some distinctive aspect of the quality of an "
          "ecosystem is present."),

 dict(q="Judging by the lichen counts alone, which of those sites has the cleanest air?",
      table=_T_LICHEN,
      choices=["Site 1", "Site 2", "Site 3", "Site 4",
               "The lichen counts give no basis for the judgement"],
      ans=0,
      why="The lichen counts are 240, 96, 21 and 0, and the largest belongs to the site with "
          "the lowest sulfur dioxide reading. ERT-2.I.3 makes the abundance of an indicator "
          "species a demonstration of an aspect of an ecosystem's quality."),

 dict(q="Four lakes were sampled for mercury in the sediment and in the tissue of one fish "
        "species. What does the record establish?",
      table=_T_MERCURY,
      choices=[
        "Fish from the lakes with more mercury in the sediment carried more mercury in "
        "their tissue.",
        "Fish from the lakes with more mercury in the sediment carried less mercury in "
        "their tissue.",
        "Every lake's fish carried the same amount of mercury in their tissue.",
        "The sediment readings were the same in all four lakes.",
        "Mercury was found in the sediment but not in any fish tissue."],
      ans=0,
      why="Ordered by sediment mercury the tissue readings run 0.2, 1.1, 3.4 and 7.8 "
          "milligrams per kilogram, rising at every step. ERT-2.I.3 names chemical "
          "composition as one of the properties by which an indicator species demonstrates "
          "an aspect of its ecosystem."),

 dict(q="In that lake study, which reading is the indicator and which is the condition it "
        "demonstrates?",
      table=_T_MERCURY,
      choices=[
        "The mercury in the fish tissue is the indicator reading and the mercury in the "
        "sediment is the condition it demonstrates.",
        "The mercury in the sediment is the indicator reading and the mercury in the fish "
        "tissue is the condition it demonstrates.",
        "Both readings are conditions, and no indicator is involved.",
        "Both readings are indicators, and no condition is involved.",
        "Neither reading bears on the character or quality of the lake."],
      ans=0,
      why="ERT-2.I.3 makes an indicator species a plant or animal whose chemical "
          "composition demonstrates that some distinctive aspect of the character or quality "
          "of an ecosystem is present. The fish is the organism and the lake's sediment is "
          "the aspect of the lake, and in every lake the tissue reading is the larger of the "
          "two."),

 dict(q="A cooled lava flow was surveyed for plants four times over one hundred and twenty "
        "years. What does the record establish?",
      table=_T_PIONEER,
      choices=[
        "Plants accumulated on ground that had none, adding species at every survey.",
        "Plants were present in full at the first survey and did not increase.",
        "Plants were lost from the flow at every survey.",
        "The number of plant species was the same at every survey.",
        "The flow held no plants at any survey."],
      ans=0,
      why="The species counts run 2, 11, 29 and 46 across the surveys, rising at every one. "
          "ERT-2.J.1 states that pioneer members of an early successional species commonly "
          "move into unoccupied habitat and over time adapt to its particular conditions."),

 dict(q="How many more plant species were growing on that lava flow at the last survey than "
        "at the second?",
      table=_T_PIONEER,
      choices=["Thirty-five", "Forty-four", "Seventeen", "Forty-six", "Eleven"],
      ans=0,
      why="The last survey records 46 species and the second records 11, and 46 less 11 is "
          "35. The rejected values are the two entries themselves or differences between "
          "other pairs of surveys."),

 dict(q="Which observation would best support a claim that one species on a shore is a "
        "keystone species?",
      choices=[
        "The community changes substantially when that species is removed and changes little "
        "when comparable species are removed.",
        "That species makes up more of the shore's biomass than any other.",
        "That species is found on no other shore in the region.",
        "That species is the first to appear on newly cleared rock.",
        "That species carries a higher concentration of a pollutant than the others do."],
      ans=0,
      why="ERT-2.I.2 defines a keystone species by the particularly significant role its "
          "activities play in determining community structure, so the evidence has to be a "
          "change in the community traceable to that species and not to any comparable one. "
          "Abundance, rarity, arrival order and pollutant load are each something else."),

 dict(q="A student calls a species a keystone species because it is the most abundant "
        "organism on the shore. What is wrong with that reasoning?",
      choices=[
        "The framework's criterion is a particularly significant role in determining "
        "community structure, not abundance.",
        "The framework's criterion is abundance, but only in aquatic ecosystems.",
        "The framework's criterion is scarcity rather than abundance.",
        "The framework applies the term only to plants, not to animals.",
        "The framework applies the term only to species that arrive first after a "
        "disturbance."],
      ans=0,
      why="ERT-2.I.2 defines a keystone species by what its activities do to community "
          "structure. Abundance is not the test, and the framework attaches no restriction "
          "of habitat, of kingdom or of arrival order to the term."),

 dict(q="Which of these uses the term indicator species as the framework defines it?",
      choices=[
        "A moss whose scarcity in a valley demonstrates that the air there carries a "
        "particular pollutant.",
        "A tree whose removal causes most of the other species in a wood to disappear.",
        "A grass that is the first plant to grow on newly exposed ground.",
        "A fish that accounts for most of a lake's total biomass.",
        "A bird that migrates further than any other species in the region."],
      ans=0,
      why="ERT-2.I.3 makes an indicator species a plant or animal that, by its presence, "
          "abundance, scarcity or chemical composition, demonstrates that some distinctive "
          "aspect of the character or quality of an ecosystem is present. The rejected "
          "options describe a keystone role, a pioneer, a dominant and a long migrant."),

 dict(q="Which single sentence collects what this topic's statements assert and nothing "
        "further?",
      choices=[
        "There are two main types of succession, primary and secondary; a keystone species "
        "shapes community structure and an indicator species demonstrates a condition; "
        "pioneers commonly move into unoccupied habitat and may in time give rise to new "
        "species; and succession in a disturbed ecosystem affects biomass, species richness "
        "and net productivity.",
        "There are three main types of succession; a keystone species demonstrates a "
        "condition and an indicator species shapes community structure; pioneers always "
        "give rise to new species; and succession affects only biomass.",
        "There are two main types of succession, primary and secondary; a keystone species "
        "shapes community structure and an indicator species demonstrates a condition; "
        "pioneers never colonise unoccupied habitat; and succession leaves biomass, species "
        "richness and net productivity unchanged.",
        "There are two main types of succession, primary and secondary; both keystone and "
        "indicator species are defined by their abundance; pioneers commonly move into "
        "unoccupied habitat; and succession affects biomass, species richness and net "
        "productivity.",
        "There are two main types of succession, primary and secondary; a keystone species "
        "shapes community structure and an indicator species demonstrates a condition; "
        "pioneers commonly move into unoccupied habitat and always give rise to new species; "
        "and succession affects only species richness."],
      ans=0,
      why="ERT-2.I.1 supplies the count and the two names, ERT-2.I.2 and ERT-2.I.3 supply "
          "the two definitions in their own directions, ERT-2.J.1 supplies the hedged "
          "pioneer claim, and ERT-2.J.2 supplies the three quantities. Each rejected summary "
          "changes the count, swaps the two definitions, hardens a hedge, or drops one or "
          "more of the three quantities."),
]
