# AP ENVIRONMENTAL SCIENCE 2.1 Introduction to Biodiversity
# CED effective Fall 2026, Unit 2 The Living World: Biodiversity.
# Enduring understanding ERT-2: Ecosystems have structure and diversity that change over
# time.
# Learning objective ERT-2.A: explain levels of biodiversity and their importance to
# ecosystems. Suggested skill 1.A.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-2.A.1  Biodiversity in an ecosystem includes genetic, species, and habitat
#              diversity.
#   ERT-2.A.2  The more genetically diverse a population is, the better it can respond to
#              environmental stressors. Additionally, a population bottleneck can lead to
#              a loss of genetic diversity.
#   ERT-2.A.3  Ecosystems that have a larger number of species are more likely to recover
#              from disruptions.
#   ERT-2.A.4  Loss of habitat leads to a loss of specialist species, followed by a loss
#              of generalist species. It also leads to reduced numbers of species that
#              have large territorial requirements.
#   ERT-2.A.5  Species richness refers to the number of different species found in an
#              ecosystem.
#
# THREE TOPICS TOUCH SPECIALISTS AND GENERALISTS, AND THEY ARE KEPT APART. Here the only
# claim used is ERT-2.A.4's ORDER under habitat loss: specialists are lost first, then
# generalists, and species with large territorial requirements fall in number. The island
# case -- limited resources and invasive generalists outcompeting specialists -- is
# ERT-2.E.1 and belongs to topic 2.3. Which of the two is advantaged in a constant or a
# changing habitat is ERT-3.A.1 and belongs to topic 3.1. No item here reaches into
# either.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework does not define a population bottleneck
# beyond stating that one can lead to a loss of genetic diversity, so no item asks what
# causes a bottleneck; the bottleneck items key only that consequence. It also gives no
# index or formula for diversity, so no item asks a student to compute one -- species
# richness is a count, which ERT-2.A.5 states outright.
#
# NO FIGURES ARE REFERENCED. Survey data are given as tables.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("2.1", "Introduction to Biodiversity", 2)

_T_RICHNESS = dict(
    headers=["Survey plot", "Number of different species recorded",
             "Total number of individuals recorded"],
    rows=[["Plot 1", "34", "620"],
          ["Plot 2", "12", "890"],
          ["Plot 3", "27", "410"],
          ["Plot 4", "8", "1150"]])

_T_GENETIC = dict(
    headers=["Population of one plant species",
             "Number of different genetic variants present",
             "Percent of individuals surviving a severe drought"],
    rows=[["Population 1", "42", "68"],
          ["Population 2", "26", "51"],
          ["Population 3", "11", "24"],
          ["Population 4", "4", "9"]])

_T_BOTTLENECK = dict(
    headers=["Stage in the history of one population", "Number of individuals",
             "Number of different genetic variants present"],
    rows=[["Before the crash", "9400", "58"],
          ["At the lowest point", "35", "12"],
          ["After fifty years of recovery in numbers", "8800", "14"]])

_T_RECOVERY = dict(
    headers=["Ecosystem", "Number of different species before a storm",
             "Years taken to return to the pre-storm community"],
    rows=[["Ecosystem 1", "96", "4"],
          ["Ecosystem 2", "61", "9"],
          ["Ecosystem 3", "38", "17"],
          ["Ecosystem 4", "15", "31"]])

_T_HABITAT = dict(
    headers=["Forest fragment", "Area remaining (hectares)",
             "Number of specialist species present", "Number of generalist species present"],
    rows=[["Fragment 1", "2400", "31", "22"],
          ["Fragment 2", "600", "17", "21"],
          ["Fragment 3", "80", "4", "19"],
          ["Fragment 4", "9", "0", "11"]])

_T_TERRITORY = dict(
    headers=["Animal species", "Territory one pair requires (hectares)",
             "Percent of small forest fragments in which it is still found"],
    rows=[["Species 1", "2", "84"],
          ["Species 2", "40", "46"],
          ["Species 3", "900", "7"],
          ["Species 4", "4000", "0"]])

_T_LEVELS = dict(
    headers=["Measurement made in one region", "What it counts"],
    rows=[["Measurement 1", "The number of different gene variants within one species"],
          ["Measurement 2", "The number of different species present"],
          ["Measurement 3", "The number of distinct habitat types present"]])

QUESTIONS = [

 dict(q="Which three levels of biodiversity does the framework name?",
      choices=[
        "Genetic, species and habitat diversity.",
        "Genetic, chemical and physical diversity.",
        "Species, trophic and climatic diversity.",
        "Habitat, mineral and atmospheric diversity.",
        "Genetic, seasonal and geological diversity."],
      ans=0,
      why="ERT-2.A.1 states that biodiversity in an ecosystem includes genetic, species "
          "and habitat diversity, which are exactly the three the keyed option names."),

 dict(q="What does species richness refer to, according to the framework?",
      choices=[
        "The number of different species found in an ecosystem.",
        "The total number of individual organisms found in an ecosystem.",
        "The number of gene variants found within one species.",
        "The number of habitat types found in a region.",
        "The mass of living material found in an ecosystem."],
      ans=0,
      why="ERT-2.A.5 states that species richness refers to the number of different "
          "species found in an ecosystem, which is a count of kinds rather than of "
          "individuals or of anything else."),

 dict(q="What does the framework say about a population that is more genetically diverse?",
      choices=[
        "It can respond better to environmental stressors.",
        "It responds less well to environmental stressors.",
        "It is unaffected by environmental stressors.",
        "It always contains more individuals than a less diverse population.",
        "It occupies more habitat types than a less diverse population."],
      ans=0,
      why="ERT-2.A.2 states that the more genetically diverse a population is, the better "
          "it can respond to environmental stressors. The claim is about the response, not "
          "about the size of the population or the area it occupies."),

 dict(q="What consequence does the framework attach to a population bottleneck?",
      choices=[
        "It can lead to a loss of genetic diversity.",
        "It can lead to a gain in genetic diversity.",
        "It leaves genetic diversity unchanged.",
        "It increases the number of species in the ecosystem.",
        "It increases the number of habitat types in the region."],
      ans=0,
      why="ERT-2.A.2 states that a population bottleneck can lead to a loss of genetic "
          "diversity. The framework attaches no other consequence to a bottleneck."),

 dict(q="What does the framework say about ecosystems that contain a larger number of "
        "species?",
      choices=[
        "They are more likely to recover from disruptions.",
        "They are less likely to recover from disruptions.",
        "They are equally likely to recover as ecosystems with fewer species.",
        "They never experience disruptions.",
        "They contain fewer individual organisms in total."],
      ans=0,
      why="ERT-2.A.3 states that ecosystems that have a larger number of species are more "
          "likely to recover from disruptions."),

 dict(q="In what order does the framework say species are lost as habitat is lost?",
      choices=[
        "Specialist species are lost first, followed by generalist species.",
        "Generalist species are lost first, followed by specialist species.",
        "Specialists and generalists are lost at the same rate.",
        "Only generalist species are lost; specialists are unaffected.",
        "Neither group is lost, because species simply move to new habitat."],
      ans=0,
      why="ERT-2.A.4 states that loss of habitat leads to a loss of specialist species, "
          "followed by a loss of generalist species, which gives the order directly."),

 dict(q="What further consequence of habitat loss does the framework name?",
      choices=[
        "Reduced numbers of species that have large territorial requirements.",
        "Increased numbers of species that have large territorial requirements.",
        "An increase in the genetic diversity of the remaining populations.",
        "An increase in the number of habitat types present.",
        "No change in any population, provided some habitat remains."],
      ans=0,
      why="ERT-2.A.4 states that loss of habitat also leads to reduced numbers of species "
          "that have large territorial requirements, alongside the loss of specialists and "
          "then generalists."),

 dict(q="Four plots were surveyed as shown. Which plot has the greatest species richness?",
      table=_T_RICHNESS,
      choices=[
        "Plot 1, which records the largest number of different species.",
        "Plot 4, which records the largest number of individuals.",
        "Plot 2, which records more individuals than Plot 3.",
        "Plot 3, which records fewer individuals than Plot 1.",
        "All four plots have the same species richness."],
      ans=0,
      why="ERT-2.A.5 defines species richness as the number of different species found in "
          "an ecosystem, so the answer is read from the species column and not from the "
          "column counting individuals."),

 dict(q="Using the same plot table, what is the best response to a student who says Plot 4 "
        "is the most biodiverse because it holds the most organisms?",
      table=_T_RICHNESS,
      choices=[
        "Species richness counts different species, and Plot 4 records the fewest of "
        "those.",
        "Species richness counts individuals, so the student is correct.",
        "Plot 4 records the fewest individuals, so the student has misread the table.",
        "Species richness counts habitat types, which the table does not record.",
        "Plot 4 records the most species as well as the most individuals."],
      ans=0,
      why="ERT-2.A.5 makes species richness a count of different species, and the plot "
          "with the largest number of individuals holds the smallest number of species in "
          "this table, so the two columns rank the plots differently."),

 dict(q="Four populations of one plant species were compared, as shown. Which conclusion "
        "is best supported?",
      table=_T_GENETIC,
      choices=[
        "Populations with more genetic variants survived the drought better.",
        "Populations with more genetic variants survived the drought worse.",
        "Survival was unrelated to the number of genetic variants.",
        "The population with the fewest genetic variants had the highest survival.",
        "All four populations survived the drought equally well."],
      ans=0,
      why="Sorting the populations by the number of genetic variants leaves the survival "
          "percentage strictly increasing. ERT-2.A.2 states that the more genetically "
          "diverse a population is, the better it can respond to environmental stressors."),

 dict(q="One population's history is shown. Which conclusion is best supported?",
      table=_T_BOTTLENECK,
      choices=[
        "The population recovered its numbers but not its genetic diversity.",
        "The population recovered both its numbers and its genetic diversity.",
        "The population recovered its genetic diversity but not its numbers.",
        "The population lost none of its genetic variants at the lowest point.",
        "The population held more genetic variants after recovery than before the crash."],
      ans=0,
      why="The individual count returns close to its starting value while the count of "
          "genetic variants stays near its low point. ERT-2.A.2 states that a population "
          "bottleneck can lead to a loss of genetic diversity."),

 dict(q="Four ecosystems struck by the same storm were followed, as shown. Which "
        "conclusion is best supported?",
      table=_T_RECOVERY,
      choices=[
        "Ecosystems holding more species returned to their pre-storm community sooner.",
        "Ecosystems holding more species took longer to return to their pre-storm "
        "community.",
        "The number of species was unrelated to the time taken to recover.",
        "The ecosystem with the fewest species recovered fastest.",
        "All four ecosystems recovered in the same number of years."],
      ans=0,
      why="Sorting the ecosystems by species number leaves the recovery time strictly "
          "decreasing. ERT-2.A.3 states that ecosystems with a larger number of species "
          "are more likely to recover from disruptions."),

 dict(q="Four forest fragments of different sizes were surveyed, as shown. Which pattern "
        "is best supported by the table?",
      table=_T_HABITAT,
      choices=[
        "Specialist species fall away faster than generalist species as the remaining area "
        "shrinks.",
        "Generalist species fall away faster than specialist species as the remaining area "
        "shrinks.",
        "Both groups fall away at the same rate as the remaining area shrinks.",
        "Specialist species increase as the remaining area shrinks.",
        "The smallest fragment holds the largest number of specialist species."],
      ans=0,
      why="Across the fragments the specialist count falls to nothing while the generalist "
          "count falls by about half. ERT-2.A.4 states that loss of habitat leads to a "
          "loss of specialist species FOLLOWED BY a loss of generalist species."),

 dict(q="Using the same fragment table, what does the smallest fragment show?",
      table=_T_HABITAT,
      choices=[
        "Specialists have gone entirely while some generalists remain.",
        "Generalists have gone entirely while some specialists remain.",
        "Both groups have gone entirely.",
        "Neither group has declined at all.",
        "Specialists outnumber generalists there."],
      ans=0,
      why="In the smallest tabulated fragment the specialist column has reached zero while "
          "the generalist column has not, which is the end state ERT-2.A.4 describes when "
          "it puts the loss of specialists before the loss of generalists."),

 dict(q="Four animal species were compared as shown. Which conclusion is best supported?",
      table=_T_TERRITORY,
      choices=[
        "Species needing more territory are found in fewer of the small fragments.",
        "Species needing more territory are found in more of the small fragments.",
        "Territory requirement is unrelated to persistence in small fragments.",
        "The species needing the most territory persists in the most fragments.",
        "All four species persist in the same share of small fragments."],
      ans=0,
      why="Sorting the species by territory required leaves the share of fragments "
          "occupied strictly decreasing. ERT-2.A.4 states that loss of habitat leads to "
          "reduced numbers of species that have large territorial requirements."),

 dict(q="Three measurements made in one region are described. Which measurement "
        "corresponds to genetic diversity as the framework uses the term?",
      table=_T_LEVELS,
      choices=[
        "Measurement 1, which counts gene variants within one species.",
        "Measurement 2, which counts different species.",
        "Measurement 3, which counts distinct habitat types.",
        "All three, because each counts something diverse.",
        "None of the three, because genetic diversity cannot be counted."],
      ans=0,
      why="ERT-2.A.1 names genetic, species and habitat diversity as three separate levels "
          "of biodiversity, so a count of gene variants within a species addresses the "
          "first while the other two counts address the other two levels."),

 dict(q="Using the same three measurements, which one corresponds to species richness?",
      table=_T_LEVELS,
      choices=[
        "Measurement 2, which counts different species.",
        "Measurement 1, which counts gene variants within one species.",
        "Measurement 3, which counts distinct habitat types.",
        "Measurements 1 and 3 together.",
        "None of the three, because species richness is a mass rather than a count."],
      ans=0,
      why="ERT-2.A.5 states that species richness refers to the number of different "
          "species found in an ecosystem, which is exactly the count the second "
          "measurement makes."),

 dict(q="Two ecosystems face the same disruption. One holds ninety species and the other "
        "holds twelve. Which prediction does the framework support?",
      choices=[
        "The ecosystem with ninety species is more likely to recover.",
        "The ecosystem with twelve species is more likely to recover.",
        "Both are equally likely to recover, because the disruption is the same.",
        "Neither can recover, because a disruption is permanent.",
        "The ecosystem with twelve species will gain species from the other one."],
      ans=0,
      why="ERT-2.A.3 states that ecosystems that have a larger number of species are more "
          "likely to recover from disruptions, and the two ecosystems differ in exactly "
          "that quantity."),

 dict(q="A conservation manager wants to preserve the ability of a population to respond "
        "to future environmental stress. Which measure does the framework most directly "
        "support?",
      choices=[
        "Keeping the population's genetic diversity high.",
        "Reducing the population to a small number of the healthiest individuals.",
        "Keeping the population in a single small area.",
        "Removing the habitat types the population does not currently use.",
        "Increasing the number of habitat types while allowing a bottleneck to occur."],
      ans=0,
      why="ERT-2.A.2 states that the more genetically diverse a population is, the better "
          "it can respond to environmental stressors, and that a bottleneck can lead to a "
          "loss of genetic diversity, so the two halves of the statement point the same "
          "way."),

 dict(q="Which statement correctly distinguishes species diversity from genetic diversity "
        "as the framework uses the terms?",
      choices=[
        "Species diversity concerns the different species in an ecosystem; genetic "
        "diversity concerns the variation within a population.",
        "Species diversity concerns the variation within a population; genetic diversity "
        "concerns the different species in an ecosystem.",
        "Both terms refer to the number of habitat types present.",
        "Both terms refer to the number of individual organisms present.",
        "The two terms are interchangeable names for the same quantity."],
      ans=0,
      why="ERT-2.A.1 lists genetic, species and habitat diversity as three separate levels, "
          "ERT-2.A.5 defines species richness as a count of different species, and "
          "ERT-2.A.2 discusses genetic diversity as a property of a population."),

 dict(q="A woodland is cleared until only a few small patches remain. Which sequence does "
        "the framework support expecting?",
      choices=[
        "Specialist species disappear first, then generalist species, and species needing "
        "large territories fall in number.",
        "Generalist species disappear first, then specialist species, and species needing "
        "large territories increase.",
        "All species disappear at once, regardless of their requirements.",
        "No species disappear as long as any patch of woodland remains.",
        "Species needing large territories increase while all others disappear."],
      ans=0,
      why="ERT-2.A.4 contains all three parts of the keyed sequence: loss of habitat leads "
          "to a loss of specialist species, followed by a loss of generalist species, and "
          "also to reduced numbers of species with large territorial requirements."),

 dict(q="Which observation would best support the claim that genetic diversity helps a "
        "population withstand stress?",
      choices=[
        "Populations of the same species with more gene variants suffer lower mortality in "
        "the same drought.",
        "Populations of the same species with more individuals occupy larger areas.",
        "Populations of the same species are found in more than one habitat type.",
        "Populations of different species contain different numbers of individuals.",
        "Populations of the same species have the same number of gene variants."],
      ans=0,
      why="ERT-2.A.2 claims a relationship between genetic diversity and the response to "
          "environmental stressors, so the evidence bearing on it compares populations "
          "differing in genetic diversity under the same stress."),

 dict(q="An ecosystem holds many individuals but only a handful of species. Which "
        "statement about it is supported by the framework?",
      choices=[
        "Its species richness is low, and it is less likely to recover from a disruption "
        "than a species-rich ecosystem.",
        "Its species richness is high, because richness counts individuals.",
        "Its species richness cannot be judged without knowing its genetic diversity.",
        "It is more likely to recover from a disruption than a species-rich ecosystem.",
        "It contains no biodiversity of any kind."],
      ans=0,
      why="ERT-2.A.5 makes species richness a count of different species rather than of "
          "individuals, and ERT-2.A.3 states that ecosystems with a larger number of "
          "species are more likely to recover from disruptions."),

 dict(q="Why does the framework treat habitat diversity as a level of biodiversity in its "
        "own right?",
      choices=[
        "Because biodiversity in an ecosystem is stated to include genetic, species and "
        "habitat diversity together.",
        "Because habitat diversity is another name for species richness.",
        "Because habitat diversity is a measure of genetic variation.",
        "Because habitat types are counted as species.",
        "Because habitat diversity replaces the other two levels in large ecosystems."],
      ans=0,
      why="ERT-2.A.1 lists the three levels together in one sentence, which is what makes "
          "habitat diversity a level of its own rather than a restatement of either of the "
          "other two."),

 dict(q="A population falls to a very small number of individuals and later recovers its "
        "numbers. Which outcome does the framework support expecting?",
      choices=[
        "Its genetic diversity may remain lower than before, because a bottleneck can lead "
        "to a loss of genetic diversity.",
        "Its genetic diversity will automatically return with its numbers.",
        "Its genetic diversity will exceed its original level once numbers recover.",
        "Its species richness will fall as its numbers recover.",
        "Its habitat diversity will fall as its numbers recover."],
      ans=0,
      why="ERT-2.A.2 states that a population bottleneck can lead to a loss of genetic "
          "diversity, and it attaches no mechanism by which the lost variants return when "
          "the count of individuals does."),

 dict(q="Which of the following is NOT a consequence of habitat loss that the framework "
        "names?",
      choices=[
        "An increase in the genetic diversity of the species that remain.",
        "A loss of specialist species.",
        "A subsequent loss of generalist species.",
        "Reduced numbers of species with large territorial requirements.",
        "A reduction in the habitat available to the community."],
      ans=0,
      why="ERT-2.A.4 names the loss of specialists, the subsequent loss of generalists and "
          "the reduced numbers of species with large territorial requirements. It makes no "
          "claim that genetic diversity rises, and ERT-2.A.2 gives no such mechanism."),

 dict(q="Two reserves are proposed for a species that needs a very large territory. Which "
        "consideration does the framework most directly support?",
      choices=[
        "A reserve that leaves only small fragments of habitat is unlikely to hold the "
        "species, because habitat loss reduces the numbers of such species.",
        "The size of the reserve is irrelevant, because habitat loss affects only "
        "specialists.",
        "A smaller reserve is preferable, because it concentrates the population.",
        "The species will adapt to a small reserve within a single generation.",
        "Habitat loss increases the numbers of species with large territorial "
        "requirements."],
      ans=0,
      why="ERT-2.A.4 states that loss of habitat leads to reduced numbers of species that "
          "have large territorial requirements, which is precisely the group the proposed "
          "reserve is meant to hold."),

 dict(q="Which pair of quantities would together give the fullest picture of an "
        "ecosystem's biodiversity as the framework defines it?",
      choices=[
        "The number of different species present and the genetic variation within those "
        "species, together with the range of habitat types.",
        "The number of individual organisms present and their total mass.",
        "The number of individual organisms present and the area of the ecosystem.",
        "The total mass of living material and the amount of rainfall received.",
        "The number of predators present and the number of prey animals present."],
      ans=0,
      why="ERT-2.A.1 states that biodiversity in an ecosystem includes genetic, species "
          "and habitat diversity, so a full account addresses all three levels rather "
          "than counting individuals or measuring mass."),

 dict(q="An ecologist reports that two ecosystems hold the same number of individual "
        "organisms but that one holds four times as many species. Which framework "
        "statement bears most directly on the difference?",
      choices=[
        "Species richness refers to the number of different species found in an "
        "ecosystem.",
        "A population bottleneck can lead to a loss of genetic diversity.",
        "Loss of habitat leads to a loss of specialist species.",
        "Biodiversity includes habitat diversity as one of its levels.",
        "The more genetically diverse a population is, the better it responds to "
        "stressors."],
      ans=0,
      why="The two ecosystems are matched on the number of individuals and differ in the "
          "number of different species, which is exactly the quantity ERT-2.A.5 defines as "
          "species richness."),

 dict(q="Which combination of framework statements explains why protecting large "
        "continuous areas of habitat protects biodiversity at more than one level?",
      choices=[
        "Habitat loss removes specialists and then generalists and reduces species with "
        "large territories, and a smaller surviving population risks losing genetic "
        "diversity.",
        "Habitat loss increases species richness while lowering genetic diversity.",
        "Habitat loss affects only the number of habitat types and nothing else.",
        "Habitat loss raises the recovery ability of the remaining ecosystem.",
        "Habitat loss affects genetic diversity only and leaves species richness "
        "unchanged."],
      ans=0,
      why="ERT-2.A.4 supplies the species-level and territory-level consequences of habitat "
          "loss, and ERT-2.A.2 supplies the genetic-level one by tying a bottleneck to a "
          "loss of genetic diversity, so the two statements together span more than one "
          "level of ERT-2.A.1."),
]
