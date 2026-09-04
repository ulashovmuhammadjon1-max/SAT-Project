# AP ENVIRONMENTAL SCIENCE 9.10 Human Impacts on Biodiversity
# CED effective Fall 2026, Unit 9 Global Change.
# Enduring understanding EIN-4: The health of a species is closely tied to its ecosystem,
# and minor environmental changes can have a large impact.
# Learning objective EIN-4.C: explain how human activities affect biodiversity and
# strategies to combat the problem. Suggested skill 7.C, describe disadvantages,
# advantages, or unintended consequences for potential solutions.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-4.C.1  HIPPCO (habitat destruction, invasive species, population growth,
#              pollution, climate change, and over exploitation) describes the main
#              factors leading to a decrease in biodiversity.
#   EIN-4.C.2  Habitat fragmentation occurs when large habitats are broken into smaller,
#              isolated areas. Causes of habitat fragmentation include the construction of
#              roads and pipelines, clearing for agriculture or development, and logging.
#   EIN-4.C.3  The scale of habitat fragmentation that has an adverse effect on the
#              inhabitants of a given ecosystem will vary from species to species within
#              that ecosystem.
#   EIN-4.C.4  Global climate change can cause habitat loss via changes in temperature,
#              precipitation, and sea level rise.
#   EIN-4.C.5  Some organisms have been somewhat or completely domesticated and are now
#              managed for economic returns, such as honeybee colonies and domestic
#              livestock. This domestication can have a negative impact on the
#              biodiversity of that organism.
#   EIN-4.C.6  Some ways humans can mitigate the impact of loss of biodiversity include
#              creating protected areas, use of habitat corridors, promoting sustainable
#              land use practices, and restoring lost habitats.
#
# THIS TOPIC OVERLAPS UNIT 2 AND TOPIC 9.8 AND IS KEPT OUT OF BOTH. That biodiversity has
# genetic, species and habitat levels, and that habitat loss removes specialists before
# generalists, are ERT-2.A (topic 2.1). What an invasive species is, and that it may
# outcompete natives, is EIN-4.A (topic 9.8). How a species becomes endangered and the
# strategies protecting an ANIMAL POPULATION are EIN-4.B (topic 9.9). No key here defines
# biodiversity, defines an invasive species, or names EIN-4.B.5's poaching and legislation
# strategies. What this topic owns is HIPPCO as a list, fragmentation and its causes, the
# species-by-species scale of its effect, climate change as a route to habitat loss,
# domestication, and EIN-4.C.6's four mitigations.
#
# EIN-4.C.3 IS THE STATEMENT THIS TOPIC IS MOST LIKELY TO BE MISREAD ON: the scale of
# fragmentation that harms varies FROM SPECIES TO SPECIES. Items 6, 14, 23 and 24 keep
# that variation in front of the student, and no key here states a fragment size at which
# fragmentation becomes harmful, because the framework states none.
#
# THE FRAMEWORK RANKS NOTHING. It gives no order among the six HIPPCO factors and no
# order among the four mitigations, so no key ranks them; the data items 20 and 29 read
# their own records instead and say so.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("9.10", "Human Impacts on Biodiversity", 9)

_T_HIPPCO = dict(
    headers=["Factor recorded across one region",
             "Species losses in the region attributed to it"],
    rows=[["Habitat destruction", "41"],
          ["Invasive species", "22"],
          ["Population growth", "14"],
          ["Pollution", "18"],
          ["Climate change", "26"],
          ["Over exploitation", "31"]])

_T_FRAGMENT = dict(
    headers=["Landscape", "Separate pieces the habitat has been broken into",
             "Mean area of one piece (hectares)", "Number of species still present"],
    rows=[["Landscape 1", "1", "5,000", "84"],
          ["Landscape 2", "6", "820", "61"],
          ["Landscape 3", "19", "240", "38"],
          ["Landscape 4", "47", "70", "17"]])

_T_SCALE = dict(
    headers=["Species", "Smallest piece of habitat in which it still breeds (hectares)",
             "Percent of the region's pieces large enough for it"],
    rows=[["Species 1", "4", "91"],
          ["Species 2", "60", "54"],
          ["Species 3", "400", "17"],
          ["Species 4", "2,500", "2"]])

_T_CAUSES = dict(
    headers=["Activity carried out in one landscape",
             "Kilometres of new habitat edge it created",
             "Separate pieces of habitat it created"],
    rows=[["Construction of roads and pipelines", "310", "22"],
          ["Clearing for agriculture or development", "480", "31"],
          ["Logging", "260", "18"],
          ["Designation of a protected area", "0", "0"]])

_T_CLIMATE = dict(
    headers=["Site", "Rise in mean temperature (degrees Celsius)",
             "Change in yearly precipitation (millimetres)",
             "Rise in sea level (centimetres)", "Habitat lost (hectares)"],
    rows=[["Site 1", "0.5", "-40", "6", "120"],
          ["Site 2", "1.2", "-110", "14", "460"],
          ["Site 3", "1.9", "-190", "23", "980"],
          ["Site 4", "2.7", "-280", "35", "1,740"]])

_T_DOMESTIC = dict(
    headers=["Managed population", "Generations under human management",
             "Distinct genetic lines remaining in it"],
    rows=[["Population 1", "0", "180"],
          ["Population 2", "20", "96"],
          ["Population 3", "60", "41"],
          ["Population 4", "140", "9"]])

_T_MITIGATE = dict(
    headers=["Measure applied in one region", "Area it covers (thousands of hectares)",
             "Percent change in the species count after ten years"],
    rows=[["Creating a protected area", "220", "18"],
          ["Use of habitat corridors", "40", "12"],
          ["Promoting sustainable land use practices", "310", "9"],
          ["Restoring lost habitat", "85", "21"]])

QUESTIONS = [

 dict(q="What does the framework say HIPPCO describes?",
      choices=[
        "The main factors leading to a decrease in biodiversity.",
        "The main strategies for restoring biodiversity that has been lost.",
        "The stages through which a disturbed ecosystem recovers.",
        "The levels at which biodiversity can be measured.",
        "The organisms that people have domesticated for economic return."],
      ans=0,
      why="EIN-4.C.1 states that HIPPCO describes the main factors leading to a decrease "
          "in biodiversity, so it names causes of loss rather than remedies, stages or "
          "levels."),

 dict(q="Which set of factors does the framework give under that name?",
      choices=[
        "Habitat destruction, invasive species, population growth, pollution, climate "
        "change and over exploitation.",
        "Habitat destruction, insects, precipitation, pollution, corridors and "
        "overfishing.",
        "Hunting, irrigation, pesticides, ploughing, cattle and overgrazing.",
        "Habitat corridors, protected areas, sustainable land use and habitat "
        "restoration.",
        "Temperature, precipitation, sea level rise and domestication."],
      ans=0,
      why="EIN-4.C.1 spells out HIPPCO as habitat destruction, invasive species, "
          "population growth, pollution, climate change, and over exploitation, which is "
          "the set the keyed option names in full."),

 dict(q="A revision card lists seven items and calls all seven parts of HIPPCO. Which one "
        "is not?",
      choices=[
        "The use of habitat corridors.",
        "Habitat destruction.",
        "Invasive species.",
        "Pollution.",
        "Over exploitation."],
      ans=0,
      why="EIN-4.C.1 names six factors and habitat corridors is not among them; EIN-4.C.6 "
          "lists corridors instead as one of the ways of mitigating biodiversity loss, "
          "which is the opposite kind of thing."),

 dict(q="What does the framework say habitat fragmentation is?",
      choices=[
        "What occurs when large habitats are broken into smaller, isolated areas.",
        "What occurs when small habitats are joined into one large continuous area.",
        "What occurs when a habitat is restored to its former extent.",
        "What occurs when a new species is introduced into a habitat.",
        "What occurs when a habitat is designated as a protected area."],
      ans=0,
      why="EIN-4.C.2 states that habitat fragmentation occurs when large habitats are "
          "broken into smaller, isolated areas, which fixes the direction of the change."),

 dict(q="Which causes of habitat fragmentation does the framework name?",
      choices=[
        "The construction of roads and pipelines, clearing for agriculture or development, "
        "and logging.",
        "The creation of protected areas, the use of habitat corridors, and habitat "
        "restoration.",
        "The introduction of invasive species, pollution, and over exploitation.",
        "Changes in temperature, precipitation, and sea level rise.",
        "The domestication of honeybee colonies and domestic livestock."],
      ans=0,
      why="EIN-4.C.2 states that causes of habitat fragmentation include the construction "
          "of roads and pipelines, clearing for agriculture or development, and logging, "
          "which is the set the keyed option names."),

 dict(q="What does the framework say about the scale of fragmentation that has an adverse "
        "effect on the inhabitants of an ecosystem?",
      choices=[
        "It varies from species to species within that ecosystem.",
        "It is the same for every species within that ecosystem.",
        "It is the same in every ecosystem on Earth.",
        "It has no adverse effect on any species at any scale.",
        "It depends only on the total area of the ecosystem."],
      ans=0,
      why="EIN-4.C.3 states that the scale of habitat fragmentation that has an adverse "
          "effect on the inhabitants of a given ecosystem will vary from species to "
          "species within that ecosystem."),

 dict(q="Through which changes does the framework say global climate change can cause "
        "habitat loss?",
      choices=[
        "Changes in temperature, in precipitation, and a rise in sea level.",
        "Changes in temperature alone, with no other route named.",
        "Changes in the number of invasive species and in the amount of pollution.",
        "Changes in the number of people and in the amount of land farmed.",
        "Changes in the number of organisms that have been domesticated."],
      ans=0,
      why="EIN-4.C.4 states that global climate change can cause habitat loss via changes "
          "in temperature, precipitation, and sea level rise, naming all three routes "
          "together."),

 dict(q="What does the framework say about organisms that have been domesticated?",
      choices=[
        "Some have been somewhat or completely domesticated and are now managed for "
        "economic returns.",
        "All of them have been completely domesticated and none is managed for economic "
        "return.",
        "They are managed only where the wild population has already gone extinct.",
        "They are the organisms HIPPCO names as causes of biodiversity loss.",
        "They can no longer be affected by any change in their environment."],
      ans=0,
      why="EIN-4.C.5 states that some organisms have been somewhat or completely "
          "domesticated and are now managed for economic returns, which allows a partial "
          "as well as a complete case."),

 dict(q="Which examples of such organisms does the framework give?",
      choices=[
        "Honeybee colonies and domestic livestock.",
        "Invasive species and species with limited diets.",
        "Coral colonies and deep sea communities.",
        "Protected areas and habitat corridors.",
        "Roads, pipelines and logging operations."],
      ans=0,
      why="EIN-4.C.5 gives honeybee colonies and domestic livestock as its examples of "
          "organisms somewhat or completely domesticated and managed for economic "
          "returns."),

 dict(q="What impact does the framework attach to that domestication?",
      choices=[
        "A negative impact on the biodiversity of that organism.",
        "A positive impact on the biodiversity of that organism.",
        "No impact on the biodiversity of that organism.",
        "An impact on the biodiversity of every other organism except that one.",
        "An impact on the climate rather than on any organism."],
      ans=0,
      why="EIN-4.C.5 ends by stating that this domestication can have a negative impact on "
          "the biodiversity of that organism, so the effect falls on the domesticated "
          "organism itself and its direction is downward."),

 dict(q="Which ways of mitigating the impact of biodiversity loss does the framework name?",
      choices=[
        "Creating protected areas, using habitat corridors, promoting sustainable land use "
        "practices, and restoring lost habitats.",
        "Building roads and pipelines, clearing for agriculture, and logging.",
        "Introducing invasive species, allowing population growth, and permitting "
        "pollution.",
        "Domesticating more organisms and managing them for economic returns.",
        "Raising temperatures, altering precipitation, and allowing sea levels to rise."],
      ans=0,
      why="EIN-4.C.6 states that some ways humans can mitigate the impact of loss of "
          "biodiversity include creating protected areas, use of habitat corridors, "
          "promoting sustainable land use practices, and restoring lost habitats."),

 dict(q="A revision card lists five measures and calls all five framework ways of "
        "mitigating biodiversity loss. Which one is not?",
      choices=[
        "Clearing land for development.",
        "Creating protected areas.",
        "Using habitat corridors.",
        "Promoting sustainable land use practices.",
        "Restoring lost habitats."],
      ans=0,
      why="EIN-4.C.6 names four mitigations, each of which the four rejected options "
          "restates. EIN-4.C.2 lists clearing for development instead among the causes of "
          "habitat fragmentation, so it belongs on the other side of this topic."),

 dict(q="EIN-4.C.5 says organisms have been SOMEWHAT OR COMPLETELY domesticated. What does "
        "that wording establish?",
      choices=[
        "That the framework allows partial domestication as well as complete "
        "domestication.",
        "That the framework recognises only complete domestication.",
        "That the framework recognises only partial domestication.",
        "That domestication is reversed once management stops.",
        "That domestication applies only to honeybee colonies."],
      ans=0,
      why="The phrase SOMEWHAT OR COMPLETELY in EIN-4.C.5 covers both a partial and a "
          "complete case, so neither is excluded, and the statement gives two examples "
          "rather than restricting itself to one."),

 dict(q="A student writes that a given amount of fragmentation harms every species in an "
        "ecosystem to the same degree. What is the clearest correction from the framework?",
      choices=[
        "The scale of fragmentation that has an adverse effect varies from species to "
        "species within an ecosystem.",
        "The scale of fragmentation that has an adverse effect is the same for every "
        "species, so the student is right.",
        "Fragmentation has no adverse effect on any species.",
        "Fragmentation affects only the species that people have domesticated.",
        "The framework gives a fragment size below which every species is harmed."],
      ans=0,
      why="EIN-4.C.3 states that the scale of habitat fragmentation having an adverse "
          "effect will vary from species to species within a given ecosystem, and it "
          "supplies no size at which the effect begins for all of them."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "The use of habitat corridors is among the main factors leading to a decrease in "
        "biodiversity.",
        "Logging is among the causes of habitat fragmentation.",
        "Global climate change can cause habitat loss through a rise in sea level.",
        "Domestication can have a negative impact on the biodiversity of the domesticated "
        "organism.",
        "Creating protected areas is among the ways of mitigating biodiversity loss."],
      ans=0,
      why="EIN-4.C.6 names the use of habitat corridors as a way of mitigating "
          "biodiversity loss, not as a cause of it, and EIN-4.C.1's six factors do not "
          "include it. The four rejected options restate EIN-4.C.2, EIN-4.C.4, EIN-4.C.5 "
          "and EIN-4.C.6."),

 dict(q="A pipeline is cut through a continuous forest, leaving three separate blocks of "
        "woodland where one stood before. Which framework statement covers that?",
      choices=[
        "The one making the construction of pipelines a cause of habitat fragmentation, "
        "the breaking of large habitats into smaller isolated areas.",
        "The one making the use of habitat corridors a way of mitigating biodiversity "
        "loss.",
        "The one making domestication a negative influence on an organism's biodiversity.",
        "The one making climate change a cause of habitat loss.",
        "No statement in this topic covers the building of a pipeline."],
      ans=0,
      why="EIN-4.C.2 defines habitat fragmentation as large habitats being broken into "
          "smaller, isolated areas and names the construction of roads and pipelines among "
          "its causes, which is exactly what the account describes."),

 dict(q="A rise in sea level floods a coastal marsh, and the marsh community is lost. "
        "Which framework statement covers that?",
      choices=[
        "The one making global climate change a cause of habitat loss through sea level "
        "rise.",
        "The one making logging a cause of habitat fragmentation.",
        "The one making honeybee colonies an example of a domesticated organism.",
        "The one listing restoration of lost habitat among the mitigations.",
        "No statement in this topic covers a change in sea level."],
      ans=0,
      why="EIN-4.C.4 states that global climate change can cause habitat loss via changes "
          "in temperature, precipitation, and sea level rise, and the account reports "
          "habitat lost to the last of those three."),

 dict(q="A conservation agency plants a strip of woodland joining two reserves that had "
        "been isolated from one another. Which of the framework's named measures is that?",
      choices=[
        "The use of habitat corridors.",
        "The creation of a protected area.",
        "The promotion of sustainable land use practices.",
        "The restoration of a lost habitat to its full former extent.",
        "The domestication of the species living in the reserves."],
      ans=0,
      why="EIN-4.C.6 names the use of habitat corridors among the ways humans can mitigate "
          "the impact of biodiversity loss, and a strip joining two isolated areas is such "
          "a corridor rather than a new reserve or a land use policy."),

 dict(q="Species losses across one region were attributed to a set of factors. What does "
        "the record establish?",
      table=_T_HIPPCO,
      choices=[
        "The factors recorded are the six the framework names, and every one of them is "
        "credited with some of the loss.",
        "The factors recorded are the four the framework names as mitigations.",
        "One of the factors recorded is credited with none of the loss.",
        "Every factor recorded is credited with the same number of losses.",
        "The record covers only the factors that arise from climate."],
      ans=0,
      why="The six rows are the six factors EIN-4.C.1 spells out under HIPPCO, and each "
          "carries a positive count that differs from the others. The framework calls them "
          "the main factors leading to a decrease in biodiversity."),

 dict(q="Which of those factors is credited with the most species lost in that region?",
      table=_T_HIPPCO,
      choices=[
        "Habitat destruction.",
        "Invasive species.",
        "Population growth.",
        "Pollution.",
        "Climate change."],
      ans=0,
      why="The largest entry in the losses column belongs to one factor alone. EIN-4.C.1 "
          "lists the six factors without ranking them, so the order has to be read from "
          "this record rather than from the framework."),

 dict(q="Four landscapes were recorded for how far their habitat has been broken up and "
        "for the species still present. What does the record establish?",
      table=_T_FRAGMENT,
      choices=[
        "The landscapes broken into more and smaller pieces hold fewer species.",
        "The landscapes broken into more and smaller pieces hold more species.",
        "The number of pieces and the species present are unrelated in this record.",
        "Every landscape in the record holds the same number of species.",
        "The landscape broken into the most pieces holds the largest pieces."],
      ans=0,
      why="Reading down the columns, the number of pieces rises while the mean size of a "
          "piece and the species present both fall. EIN-4.C.2 defines habitat "
          "fragmentation as large habitats broken into smaller, isolated areas, and "
          "EIN-4.C.1 names habitat destruction among the main factors leading to a "
          "decrease in biodiversity."),

 dict(q="Which of those four landscapes is the most broken up, and what accompanies that?",
      table=_T_FRAGMENT,
      choices=[
        "Landscape 4, which holds the most pieces, the smallest pieces and the fewest "
        "species.",
        "Landscape 1, which holds the fewest pieces, the largest pieces and the fewest "
        "species.",
        "Landscape 2, which stands second from the top on the number of pieces.",
        "Landscape 3, which stands third on the number of pieces.",
        "All four landscapes are equally broken up."],
      ans=0,
      why="The largest number of pieces, the smallest mean piece and the smallest species "
          "count all fall in the same row. EIN-4.C.2 describes fragmentation as large "
          "habitats broken into smaller, isolated areas."),

 dict(q="Four species of one ecosystem were recorded for the smallest piece of habitat in "
        "which each still breeds. What does the record establish?",
      table=_T_SCALE,
      choices=[
        "The four differ in the size of piece they need, so a given degree of "
        "fragmentation does not affect them alike.",
        "The four need pieces of the same size, so a given degree of fragmentation affects "
        "them alike.",
        "The species needing the largest pieces finds the most pieces large enough for "
        "it.",
        "Every species in the record finds every piece large enough for it.",
        "No species in the record finds any piece large enough for it."],
      ans=0,
      why="The four thresholds differ from one another and the share of pieces large "
          "enough falls as the threshold rises. EIN-4.C.3 states that the scale of habitat "
          "fragmentation having an adverse effect will vary from species to species within "
          "an ecosystem."),

 dict(q="Which of those four species is the first to be affected as the habitat is broken "
        "into smaller pieces?",
      table=_T_SCALE,
      choices=[
        "Species 4, which needs the largest piece and finds the fewest large enough.",
        "Species 1, which needs the smallest piece and finds the most large enough.",
        "Species 2, which needs the second smallest piece of the four.",
        "Species 3, which needs the second largest piece of the four.",
        "All four are affected at the same point."],
      ans=0,
      why="The largest breeding threshold and the smallest share of pieces large enough "
          "fall in the same row, so that species runs out of usable habitat before the "
          "others do. EIN-4.C.3 makes the scale at which fragmentation harms vary from "
          "species to species."),

 dict(q="Four activities in one landscape were recorded for the habitat edge and the "
        "separate pieces each created. What does the record establish?",
      table=_T_CAUSES,
      choices=[
        "Three of the four are the causes of fragmentation the framework names, and each "
        "of those three created separate pieces of habitat, while the fourth created "
        "none.",
        "All four are causes of fragmentation the framework names, and each created "
        "separate pieces of habitat.",
        "None of the four is a cause of fragmentation the framework names.",
        "The activity that created the most edge created the fewest separate pieces.",
        "Every activity in the record created the same number of separate pieces."],
      ans=0,
      why="EIN-4.C.2 names the construction of roads and pipelines, clearing for "
          "agriculture or development, and logging as causes of habitat fragmentation. "
          "Three rows of the record are those three and each created edge and pieces, "
          "while the remaining row created neither."),

 dict(q="Four sites were recorded for three climate changes and for the habitat they lost. "
        "What does the record establish?",
      table=_T_CLIMATE,
      choices=[
        "The habitat lost grows as the temperature rise, the fall in precipitation and the "
        "sea level rise all grow.",
        "The habitat lost shrinks as the temperature rise, the fall in precipitation and "
        "the sea level rise all grow.",
        "Only the sea level column moves with the habitat lost; the other two do not.",
        "Precipitation rose at every site in the record.",
        "Every site in the record lost the same area of habitat."],
      ans=0,
      why="Sorting the sites by the temperature rise, by the fall in precipitation and by "
          "the sea level rise in turn each leaves the habitat lost strictly increasing. "
          "EIN-4.C.4 states that global climate change can cause habitat loss via changes "
          "in temperature, precipitation, and sea level rise."),

 dict(q="Across those same four sites, how much more habitat was lost at the site with the "
        "largest changes than at the site with the smallest?",
      table=_T_CLIMATE,
      choices=[
        "1,620 hectares more.",
        "120 hectares more.",
        "1,740 hectares more.",
        "760 hectares more.",
        "1,860 hectares more."],
      ans=0,
      why="The largest and smallest entries in the habitat lost column are subtracted. "
          "EIN-4.C.4 makes habitat loss the outcome that changes in temperature, "
          "precipitation and sea level can bring about."),

 dict(q="Four managed populations were recorded for how long they have been under "
        "management and for the genetic lines remaining in them. What does the record "
        "establish?",
      table=_T_DOMESTIC,
      choices=[
        "The longer a population has been managed, the fewer distinct genetic lines it "
        "retains.",
        "The longer a population has been managed, the more distinct genetic lines it "
        "retains.",
        "Management and the genetic lines remaining are unrelated in this record.",
        "Every population in the record retains the same number of genetic lines.",
        "Every population in the record has been managed for the same number of "
        "generations."],
      ans=0,
      why="Reading down the columns, the generations under management rise while the "
          "distinct genetic lines fall, and the first row has not been managed at all. "
          "EIN-4.C.5 states that domestication can have a negative impact on the "
          "biodiversity of that organism."),

 dict(q="Four measures were applied across one region and the species count followed for "
        "ten years. What does the record establish?",
      table=_T_MITIGATE,
      choices=[
        "All four measures are ones the framework names, and each is followed by a rise in "
        "the species count.",
        "All four measures are ones the framework names as causes of fragmentation.",
        "One of the four measures is followed by a fall in the species count.",
        "The measure covering the largest area is followed by the largest rise.",
        "Every measure is followed by the same change in the species count."],
      ans=0,
      why="The four rows are the four mitigations EIN-4.C.6 names, and each records a "
          "positive change of a different size. The framework ranks none of the four, so "
          "the sizes are a property of this record rather than of the statement."),

 dict(q="Which single sentence collects what this topic's statements assert and nothing "
        "further?",
      choices=[
        "HIPPCO names habitat destruction, invasive species, population growth, pollution, "
        "climate change and over exploitation as the main factors decreasing biodiversity; "
        "fragmentation breaks large habitats into smaller isolated areas through roads, "
        "pipelines, clearing and logging, at a scale that harms different species "
        "differently; climate change causes habitat loss through temperature, "
        "precipitation and sea level; domestication can lower the biodiversity of the "
        "organism domesticated; and protected areas, corridors, sustainable land use and "
        "habitat restoration can mitigate the loss.",
        "HIPPCO names the ways humans can mitigate biodiversity loss; fragmentation joins "
        "small habitats into large ones; climate change has no effect on habitat; and "
        "domestication raises the biodiversity of the organism domesticated.",
        "The framework names the causes of biodiversity loss but no way of mitigating it.",
        "The framework gives a single fragment size below which every species in an "
        "ecosystem is harmed.",
        "Habitat corridors and protected areas are among the main factors leading to a "
        "decrease in biodiversity."],
      ans=0,
      why="EIN-4.C.1 supplies HIPPCO, EIN-4.C.2 the definition of fragmentation and its "
          "causes, EIN-4.C.3 the species-by-species scale, EIN-4.C.4 the three climate "
          "routes to habitat loss, EIN-4.C.5 the effect of domestication, and EIN-4.C.6 "
          "the four mitigations. No statement gives a single harmful fragment size or puts "
          "a mitigation among the causes."),
]
