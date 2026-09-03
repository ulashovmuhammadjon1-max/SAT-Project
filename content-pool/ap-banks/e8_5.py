# AP ENVIRONMENTAL SCIENCE 8.5 Eutrophication
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.F: explain the environmental effects of
# excessive use of fertilizers and detergents on aquatic ecosystems. Suggested skill
# 2.C, explain how environmental concepts and processes represented visually relate to
# broader environmental issues.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.F.1  Eutrophication occurs when a body of water is enriched in nutrients.
#   STB-3.F.2  The increase in nutrients in eutrophic aquatic environments causes an
#              algal bloom. When the algal bloom dies, microbes digest the algae, along
#              with the oxygen in the water, leading to a decrease in the dissolved
#              oxygen levels in the water. The lack of dissolved oxygen can result in
#              large die-offs of fish and other aquatic organisms.
#   STB-3.F.3  Hypoxic waterways are those bodies of water that are low in dissolved
#              oxygen.
#   STB-3.F.4  Compared to eutrophic waterways, oligotrophic waterways have very low
#              amounts of nutrients, stable algae populations, and high dissolved
#              oxygen.
#   STB-3.F.5  Anthropogenic causes of eutrophication are agricultural runoff and
#              wastewater release.
#
# ON SCOPE, because two neighbouring topics touch the same water. Topic 8.2 keys the
# oceanic dead zone as an area of low oxygen caused by nutrient pollution and the
# oxygen sag curve as a plot against distance; this topic keys the SEQUENCE in
# STB-3.F.2 and the three-way vocabulary of eutrophic, hypoxic and oligotrophic. Topic
# 8.6 keys the temperature control on dissolved oxygen; nothing here attributes an
# oxygen change to temperature.
#
# ON THE FIGURES. Suggested skill 2.C is about visual representations and the bank
# carries no images, so every representation here is a table and every keyed reading is
# recomputed in verify_e8_5.py from that table alone. No stem refers to a figure.
#
# NOT KEYED: no nutrient limit, no oxygen threshold in milligrams per liter as a
# criterion for hypoxia, no named water body. The framework states none.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.5", "Eutrophication", 8)

_T_SEQUENCE = dict(
    headers=["Week of the study", "Nitrate in the lake (milligrams per liter)",
             "Algae measured as chlorophyll (micrograms per liter)",
             "Dissolved oxygen (milligrams per liter)"],
    rows=[["Week 1", "0.4", "5", "9.1"],
          ["Week 3", "3.8", "9", "8.8"],
          ["Week 5", "3.1", "62", "8.2"],
          ["Week 7", "1.2", "58", "3.4"],
          ["Week 9", "0.9", "12", "2.1"]])

_T_TROPHIC = dict(
    headers=["Lake", "Total nutrients (micrograms per liter)",
             "Algae measured as chlorophyll (micrograms per liter)",
             "Dissolved oxygen at depth (milligrams per liter)"],
    rows=[["Lake M", "6", "2", "9.6"],
          ["Lake N", "18", "7", "8.4"],
          ["Lake P", "70", "40", "4.0"],
          ["Lake Q", "150", "88", "1.5"]])

_T_LANDUSE = dict(
    headers=["Sub-basin draining to the estuary",
             "Land in row crops and treated wastewater outfalls",
             "Nitrogen delivered each year (tons)"],
    rows=[["Sub-basin 1", "cropland with two wastewater outfalls", "900"],
          ["Sub-basin 2", "cropland with no outfall", "540"],
          ["Sub-basin 3", "forest with no outfall", "60"]])

_T_KILL = dict(
    headers=["Night of sampling", "Dissolved oxygen before dawn (milligrams per liter)",
             "Dead fish counted the following morning"],
    rows=[["Night 1", "7.8", "0"],
          ["Night 2", "5.1", "3"],
          ["Night 3", "2.4", "140"],
          ["Night 4", "1.1", "610"]])

_T_TREAT = dict(
    headers=["Stage of a nutrient reduction program",
             "Phosphorus reaching the lake each year (tons)",
             "Summer algae measured as chlorophyll (micrograms per liter)",
             "Lowest summer dissolved oxygen (milligrams per liter)"],
    rows=[["Before the program", "120", "75", "1.9"],
          ["Five years in", "60", "38", "4.2"],
          ["Ten years in", "22", "14", "7.0"]])

_T_DEPTH = dict(
    headers=["Depth in a eutrophic lake in late summer (meters)",
             "Dissolved oxygen (milligrams per liter)"],
    rows=[["1", "8.6"],
          ["5", "6.2"],
          ["10", "2.0"],
          ["15", "0.4"]])

QUESTIONS = [

 dict(q="How does the framework define eutrophication?",
      choices=[
        "It occurs when a body of water is enriched in nutrients",
        "It occurs when a body of water is heated by an industrial discharge",
        "It occurs when a body of water loses all of its sediment",
        "It occurs when a body of water becomes more acidic",
        "It occurs when a body of water is stripped of nutrients"],
      ans=0,
      why="The framework states that eutrophication occurs when a body of water is "
          "enriched in nutrients. Heating, sediment loss, acidification and nutrient "
          "removal are different processes described elsewhere in the course."),

 dict(q="Which sequence does the framework give for what happens after nutrients "
        "increase in a eutrophic aquatic environment?",
      choices=[
        "An algal bloom forms; when it dies, microbes digest the algae along with the "
        "oxygen in the water, lowering dissolved oxygen and causing die-offs of fish and "
        "other organisms",
        "The water immediately becomes acidic and dissolves the shells of organisms",
        "The algae absorb the nutrients and dissolved oxygen rises permanently",
        "The nutrients settle to the bottom and no organism is affected",
        "The water warms until fish can no longer survive in it"],
      ans=0,
      why="Each step of the keyed sequence is the framework's own: nutrients cause an "
          "algal bloom, microbes digesting the dead bloom consume the oxygen, dissolved "
          "oxygen falls, and the lack of oxygen can cause large die-offs."),

 dict(q="Measurements from one lake through a season are shown.",
      table=_T_SEQUENCE,
      choices=[
        "Nitrate rose first, the algae rose afterward, and the dissolved oxygen fell "
        "after the algae had passed their peak",
        "The dissolved oxygen fell before the nitrate rose",
        "The algae reached their peak before the nitrate rose",
        "Nitrate, algae and dissolved oxygen all peaked in the same week",
        "The dissolved oxygen rose throughout the study"],
      ans=0,
      why="The nitrate maximum comes first in the record, the algal maximum later, and "
          "the largest fall in dissolved oxygen later still. That order matches the "
          "framework's sequence in which the bloom follows the nutrients and the oxygen "
          "falls as microbes digest the dead bloom."),

 dict(q="What does the framework mean by a hypoxic waterway?",
      choices=[
        "A body of water that is low in dissolved oxygen",
        "A body of water that is high in dissolved oxygen",
        "A body of water that contains no nutrients",
        "A body of water that has been warmed by a power plant",
        "A body of water with an unusually low pH"],
      ans=0,
      why="The framework defines hypoxic waterways as those bodies of water that are low "
          "in dissolved oxygen. High oxygen, absent nutrients, warming and acidity are "
          "different conditions with different names in the course."),

 dict(q="How does the framework contrast oligotrophic waterways with eutrophic ones?",
      choices=[
        "Oligotrophic waterways have very low amounts of nutrients, stable algae "
        "populations, and high dissolved oxygen",
        "Oligotrophic waterways have very high nutrients and very low oxygen",
        "Oligotrophic waterways have unstable algae populations and no oxygen",
        "Oligotrophic waterways are simply eutrophic waterways at a warmer temperature",
        "Oligotrophic waterways contain no living organisms of any kind"],
      ans=0,
      why="The framework states that compared to eutrophic waterways, oligotrophic "
          "waterways have very low amounts of nutrients, stable algae populations, and "
          "high dissolved oxygen. Each rejected option reverses at least one of those "
          "three."),

 dict(q="Four lakes are compared.",
      table=_T_TROPHIC,
      choices=[
        "The lakes with the lowest nutrients also carry the least algae and the highest "
        "dissolved oxygen",
        "The lakes with the lowest nutrients carry the most algae",
        "Dissolved oxygen rises as nutrients rise across the four lakes",
        "All four lakes carry the same amount of algae",
        "The lake with the most nutrients carries the highest dissolved oxygen"],
      ans=0,
      why="Ordering the lakes by nutrients puts the algae in the same order and the "
          "dissolved oxygen in the opposite order. That is the contrast the framework "
          "draws between oligotrophic and eutrophic waterways."),

 dict(q="Which anthropogenic causes of eutrophication does the framework name?",
      choices=[
        "Agricultural runoff and wastewater release",
        "Volcanic eruptions and forest fires",
        "Thermal discharges from power stations",
        "Sediment from natural riverbank erosion",
        "Acid deposition from coal-burning power plants"],
      ans=0,
      why="The framework states that anthropogenic causes of eutrophication are "
          "agricultural runoff and wastewater release. Eruptions, fires, thermal "
          "discharge, natural erosion and acid deposition are treated in other "
          "statements and are not given as causes here."),

 dict(q="Nitrogen delivered to one estuary from three sub-basins is shown.",
      table=_T_LANDUSE,
      choices=[
        "The two sub-basins with cropland deliver far more nitrogen than the forested "
        "one, and the one that also has wastewater outfalls delivers the most",
        "The forested sub-basin delivers the most nitrogen",
        "All three sub-basins deliver the same amount of nitrogen",
        "The sub-basin with wastewater outfalls delivers the least nitrogen",
        "Cropland and wastewater make no difference to the nitrogen delivered"],
      ans=0,
      why="The forested sub-basin carries the smallest figure by an order of magnitude, "
          "and the cropland sub-basin that also receives wastewater carries the largest. "
          "Agricultural runoff and wastewater release are the two anthropogenic causes "
          "the framework names."),

 dict(q="Why does dissolved oxygen fall after an algal bloom dies rather than while the "
        "bloom is growing?",
      choices=[
        "Microbes digest the dead algae and consume the oxygen in the water as they do so",
        "The dead algae release acid that destroys the oxygen",
        "The dead algae absorb oxygen directly from the atmosphere",
        "The water cools when the bloom dies, releasing its oxygen",
        "The dead algae block sunlight and prevent oxygen from dissolving"],
      ans=0,
      why="The framework's own step is that when the algal bloom dies, microbes digest "
          "the algae along with the oxygen in the water, which lowers dissolved oxygen. "
          "It gives no acid, no atmospheric absorption and no cooling role here."),

 dict(q="Overnight oxygen and fish counts from one pond are shown.",
      table=_T_KILL,
      choices=[
        "The nights with the lowest dissolved oxygen were followed by the largest "
        "numbers of dead fish",
        "The nights with the highest dissolved oxygen were followed by the largest "
        "numbers of dead fish",
        "The number of dead fish was the same after every night",
        "No fish died on any of the four nights",
        "Dissolved oxygen and fish deaths are unrelated in these data"],
      ans=0,
      why="Ordering the nights by dissolved oxygen puts the fish counts in the opposite "
          "order, with hundreds dead on the two lowest-oxygen nights and none on the "
          "highest. The framework states that a lack of dissolved oxygen can result in "
          "large die-offs of fish and other aquatic organisms."),

 dict(q="A lake receives heavy fertilizer runoff each spring. Which framework statement "
        "identifies that runoff as a cause of eutrophication?",
      choices=[
        "Anthropogenic causes of eutrophication are agricultural runoff and wastewater "
        "release",
        "Hypoxic waterways are those low in dissolved oxygen",
        "Oligotrophic waterways have stable algae populations",
        "Eutrophication occurs when a body of water is enriched in nutrients",
        "The lack of dissolved oxygen can result in die-offs of fish"],
      ans=0,
      why="The question asks which statement identifies the cause, and the framework "
          "names agricultural runoff and wastewater release as the anthropogenic causes. "
          "The other statements define a condition or describe a consequence rather than "
          "naming a cause."),

 dict(q="Results from a program that reduced phosphorus reaching a lake are shown.",
      table=_T_TREAT,
      choices=[
        "As the phosphorus reaching the lake fell, the summer algae fell and the lowest "
        "summer dissolved oxygen rose",
        "As the phosphorus fell, the summer algae rose",
        "As the phosphorus fell, the lowest dissolved oxygen fell further",
        "None of the three measurements changed during the program",
        "The phosphorus reaching the lake rose during the program"],
      ans=0,
      why="The phosphorus and the algae both fall at every stage while the lowest "
          "dissolved oxygen rises at every stage. That is the reverse of the framework's "
          "sequence from nutrient enrichment to algal bloom to oxygen depletion."),

 dict(q="Which of the following best describes a eutrophic waterway on the framework's "
        "own contrast?",
      choices=[
        "One that is enriched in nutrients, in contrast with an oligotrophic waterway's "
        "very low nutrients and high dissolved oxygen",
        "One with very low nutrients and stable algae populations",
        "One that is defined by its temperature rather than its nutrients",
        "One in which no algae are present at any time of year",
        "One that has been acidified by deposition from the atmosphere"],
      ans=0,
      why="The framework defines eutrophication as enrichment in nutrients and contrasts "
          "eutrophic with oligotrophic waterways, which have very low nutrients, stable "
          "algae and high dissolved oxygen. The rejected options describe the "
          "oligotrophic case or a different process."),

 dict(q="Oxygen measured at several depths in a eutrophic lake in late summer is shown.",
      table=_T_DEPTH,
      choices=[
        "Dissolved oxygen falls with depth, and the deepest water sampled is the lowest "
        "in oxygen",
        "Dissolved oxygen rises with depth",
        "Dissolved oxygen is the same at every depth sampled",
        "The shallowest water sampled is the lowest in oxygen",
        "The measurements show that depth and oxygen are unrelated"],
      ans=0,
      why="The oxygen values decrease at every step downward and the deepest sample "
          "carries the smallest value. A body of water low in dissolved oxygen is what "
          "the framework calls hypoxic."),

 dict(q="A treatment plant discharges nutrient-rich water into a river. Which framework "
        "cause of eutrophication does this represent?",
      choices=[
        "Wastewater release",
        "Agricultural runoff",
        "Thermal pollution",
        "Acid deposition",
        "Sediment runoff from construction"],
      ans=0,
      why="Wastewater release is one of the two anthropogenic causes of eutrophication "
          "the framework names, and a discharge from a treatment plant is wastewater. "
          "Agricultural runoff is the other cause, and the remaining options belong to "
          "different topics."),

 dict(q="Which statement best explains why a fish kill can follow an algal bloom even "
        "though algae are not toxic to fish in the framework's account?",
      choices=[
        "The oxygen the fish need is consumed by the microbes that digest the dead algae",
        "The algae eat the fish directly",
        "The algae raise the temperature of the water beyond the fish's tolerance",
        "The algae remove all the nutrients the fish require",
        "The algae make the water more acidic than the fish can tolerate"],
      ans=0,
      why="The framework's chain runs from the dying bloom to microbial digestion that "
          "consumes the oxygen in the water and then to die-offs of fish and other "
          "organisms. It attributes the deaths to the lack of dissolved oxygen rather "
          "than to any direct action of the algae."),

 dict(q="Which measurement would best show that a lake has become hypoxic?",
      choices=[
        "The concentration of dissolved oxygen in the water",
        "The concentration of nutrients in the water",
        "The number of algae visible at the surface",
        "The temperature of the water at the surface",
        "The depth of the lake at its deepest point"],
      ans=0,
      why="The framework defines a hypoxic waterway as one low in dissolved oxygen, so "
          "the measurement that identifies the condition is dissolved oxygen itself. "
          "Nutrients, algae, temperature and depth are related quantities but are not "
          "the definition."),

 dict(q="Which of the following would be expected in an oligotrophic lake, according to "
        "the framework's contrast?",
      choices=[
        "Very low nutrients, a stable algae population, and high dissolved oxygen",
        "High nutrients, a large algal bloom, and low dissolved oxygen",
        "High nutrients and high dissolved oxygen together",
        "Very low nutrients and very low dissolved oxygen together",
        "A large algal bloom followed by a fish kill every summer"],
      ans=0,
      why="Those three properties are exactly what the framework attributes to "
          "oligotrophic waterways in its comparison with eutrophic ones. Each rejected "
          "option pairs the nutrient level with the wrong oxygen level or describes the "
          "eutrophic case."),

 dict(q="A student says that adding nutrients to a lake must help the organisms living "
        "in it because nutrients support growth. Which framework statement most directly "
        "challenges that reasoning?",
      choices=[
        "The bloom that follows dies and is digested by microbes that consume the oxygen, "
        "which can cause large die-offs of fish and other organisms",
        "Nutrients cannot enter a lake from human activity",
        "Algae cannot grow in a lake that receives nutrients",
        "Dissolved oxygen is unaffected by anything living in the water",
        "Fish do not require dissolved oxygen"],
      ans=0,
      why="The framework's sequence turns the nutrient increase into an algal bloom, "
          "then into oxygen depletion when the bloom dies and is digested, and then into "
          "die-offs. The harm therefore arrives through the oxygen rather than through "
          "the nutrients directly."),

 dict(q="Which comparison would best test whether a river's low oxygen is associated "
        "with nutrient enrichment rather than with something else?",
      choices=[
        "Nutrient concentrations and dissolved oxygen measured together at several sites "
        "along the river",
        "Dissolved oxygen measured at one site on one day",
        "Nutrient concentrations measured without measuring oxygen",
        "The width of the river channel at each site",
        "The number of bridges crossing the river"],
      ans=0,
      why="The claim links two quantities, so the test needs both measured at the same "
          "sites. A single oxygen reading, nutrients alone, channel width and bridge "
          "counts each leave one side of the relationship unmeasured."),

 dict(q="Why does the framework name both agricultural runoff and wastewater release as "
        "causes rather than only one of them?",
      choices=[
        "Both deliver nutrients to a body of water, which is what its definition of "
        "eutrophication requires",
        "Only one of them actually delivers nutrients and the other is included by "
        "mistake",
        "They deliver different pollutants, neither of which is a nutrient",
        "Runoff delivers nutrients while wastewater removes them",
        "Wastewater delivers nutrients only after it has been treated to remove them"],
      ans=0,
      why="Eutrophication is defined as enrichment in nutrients, and the framework names "
          "these two as the anthropogenic causes, so both are routes by which nutrients "
          "reach the water. Nothing in it makes either a remover of nutrients."),

 dict(q="A pond shows abundant algae at the surface in midsummer and a large fish kill "
        "two weeks later. Which explanation is best supported by the framework?",
      choices=[
        "The bloom died, microbes digesting it consumed the dissolved oxygen, and the "
        "fish died from the lack of oxygen",
        "The algae poisoned the fish on contact while still growing",
        "The fish died of starvation because the algae ate their food",
        "The pond became acidic as the algae grew",
        "The pond warmed because the algae absorbed sunlight, killing the fish by heat"],
      ans=0,
      why="The two-week gap between the bloom and the kill is exactly the framework's "
          "sequence: the bloom dies, microbes digest it and consume the oxygen, and the "
          "lack of dissolved oxygen causes large die-offs."),

 dict(q="Which of the following describes the difference between a eutrophic and a "
        "hypoxic waterway as the framework uses the two terms?",
      choices=[
        "Eutrophic describes enrichment in nutrients, while hypoxic describes being low "
        "in dissolved oxygen",
        "Eutrophic describes low oxygen, while hypoxic describes high nutrients",
        "The two terms mean the same thing in the framework",
        "Eutrophic describes warm water, while hypoxic describes cold water",
        "Eutrophic describes salt water, while hypoxic describes fresh water"],
      ans=0,
      why="The framework defines eutrophication by nutrient enrichment and a hypoxic "
          "waterway by low dissolved oxygen, so the two terms name different quantities "
          "even though its sequence connects them. Neither term refers to temperature or "
          "salinity."),

 dict(q="A city upgrades its treatment plant so that far less nutrient leaves in the "
        "discharge. Which outcome does the framework's account predict for the river "
        "downstream?",
      choices=[
        "Less nutrient enrichment, so smaller algal blooms and less oxygen depletion when "
        "they die",
        "More frequent algal blooms, since the water is cleaner",
        "No change, since wastewater release is not a cause of eutrophication",
        "An immediate rise in nutrients from the plant",
        "A rise in the water temperature of the river"],
      ans=0,
      why="Wastewater release is one of the two anthropogenic causes the framework names, "
          "and its sequence runs from nutrients to bloom to oxygen depletion, so cutting "
          "the nutrient input works backward along that chain."),

 dict(q="Which of the following best explains why a lake can be rich in nutrients and "
        "still show high dissolved oxygen at the surface during the day?",
      choices=[
        "The framework's oxygen decline follows the death and microbial digestion of the "
        "bloom, so it need not appear at every place and time",
        "The framework says nutrient-rich lakes always have high oxygen",
        "The framework says dissolved oxygen never changes within a lake",
        "The framework says algae remove oxygen while they are growing",
        "The framework says oxygen cannot be measured at the surface"],
      ans=0,
      why="The framework places the fall in dissolved oxygen after the bloom dies and is "
          "digested by microbes, so it is a stage in a sequence rather than a constant "
          "condition of nutrient-rich water."),

 dict(q="Which pairing of a framework term with its defining property is correct?",
      choices=[
        "Oligotrophic, very low amounts of nutrients",
        "Oligotrophic, very high amounts of nutrients",
        "Hypoxic, very high dissolved oxygen",
        "Eutrophic, stripped of nutrients",
        "Hypoxic, enriched in sediment"],
      ans=0,
      why="The framework gives oligotrophic waterways very low amounts of nutrients, "
          "stable algae populations and high dissolved oxygen; hypoxic waterways low "
          "dissolved oxygen; and eutrophication enrichment in nutrients. Each rejected "
          "pairing reverses one of those."),

 dict(q="An estuary receives nutrient-rich water every spring and shows low oxygen every "
        "summer. Which additional evidence would most strengthen the claim that the two "
        "are connected?",
      choices=[
        "Years with larger spring nutrient loads are followed by summers with lower "
        "oxygen than years with smaller loads",
        "The estuary is deeper in some places than in others",
        "The estuary supports several species of fish",
        "The nutrient load is measured in tons rather than kilograms",
        "The estuary is larger than a neighboring estuary"],
      ans=0,
      why="A year-to-year correspondence between the size of the nutrient input and the "
          "depth of the oxygen decline is what tests the framework's sequence. Depth, "
          "species counts, units of measurement and comparative size do not."),

 dict(q="Why does the framework describe both fish and other aquatic organisms as "
        "affected by the lack of dissolved oxygen?",
      choices=[
        "Its statement names die-offs of fish and other aquatic organisms together",
        "Only fish are affected, and the phrase is figurative",
        "Only bottom-dwelling organisms are affected",
        "Only the algae themselves are affected",
        "Only organisms outside the water are affected"],
      ans=0,
      why="The framework's wording is that the lack of dissolved oxygen can result in "
          "large die-offs of fish and other aquatic organisms, so the effect is not "
          "confined to fish or to any one group."),

 dict(q="A lake manager wants a single measurement to track whether a nutrient reduction "
        "program is working over several years. Which pair would be most informative "
        "together?",
      choices=[
        "The nutrients reaching the lake each year and the lowest dissolved oxygen "
        "recorded each summer",
        "The number of visitors to the lake and the area of its surface",
        "The temperature of the inflowing stream and the depth of the lake",
        "The number of boats on the lake and the length of its shoreline",
        "The color of the water and the number of houses nearby"],
      ans=0,
      why="The framework's chain runs from nutrient enrichment to oxygen depletion, so "
          "the input and the oxygen minimum are the two ends of the process being "
          "managed. Visitors, area, boat counts and shoreline length track none of it."),

 dict(q="Which summary best captures this topic?",
      choices=[
        "Nutrient enrichment from agricultural runoff and wastewater causes algal blooms "
        "whose decay by microbes consumes dissolved oxygen, leaving hypoxic water and "
        "die-offs, in contrast with oligotrophic water that is low in nutrients and high "
        "in oxygen",
        "Nutrient enrichment raises dissolved oxygen and increases the number of fish a "
        "lake can support",
        "Eutrophication is caused by warming water and is unrelated to nutrients",
        "Hypoxic and oligotrophic waterways are two names for the same condition",
        "Algal blooms are caused by low nutrients and end when nutrients rise"],
      ans=0,
      why="Each clause of the keyed summary is one of the framework's five statements "
          "for this topic. Every rejected summary reverses the direction of the oxygen "
          "change, misattributes the cause, or conflates two of its terms."),
]
