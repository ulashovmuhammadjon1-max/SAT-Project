# AP ENVIRONMENTAL SCIENCE 1.2 Terrestrial Biomes
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.B: describe the global distribution and principal
# environmental aspects of terrestrial biomes. Suggested skill 1.B, explain
# environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.B.1  A biome contains characteristic communities of plants and animals that
#              result from, and are adapted to, its climate.
#   ERT-1.B.2  Major terrestrial biomes include taiga, temperate rainforests, temperate
#              seasonal forests, tropical rainforests, shrubland, temperate grassland,
#              savanna, desert, and tundra.
#   ERT-1.B.3  The global distribution of nonmineral terrestrial natural resources, such
#              as water and trees for lumber, varies because of some combination of
#              climate, geography, latitude and altitude, nutrient availability, and soil.
#   ERT-1.B.4  The worldwide distribution of biomes is dynamic; the distribution has
#              changed in the past and may again shift as a result of global climate
#              changes.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework NAMES nine terrestrial biomes and states
# that a biome's communities follow from its climate. It does NOT tabulate a temperature
# and rainfall envelope for each name. So no item here asks a student to read a
# climatogram and produce a biome name from memory. Where a biome name appears in a key,
# the content relied on is only what the name itself carries -- a temperate rainforest is
# by its name both moderate in temperature and high in rainfall, a desert is by its name
# dry -- and the verifier's claim says so for each such item. Everything else is asked as
# a relationship: climate to community, climate change to shifting distribution, and the
# six named factors to the distribution of a nonmineral resource.
#
# NO FIGURES ARE REFERENCED. A climatogram appears as a table of months against
# temperature and precipitation; nothing in a stem points at a picture the bank cannot
# show.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.2", "Terrestrial Biomes", 1)

_T_SITES = dict(
    headers=["Site", "Mean annual temperature (degrees Celsius)",
             "Mean annual precipitation (millimeters)"],
    rows=[["Site 1", "26", "2400"],
          ["Site 2", "25", "180"],
          ["Site 3", "24", "2200"],
          ["Site 4", "10", "550"],
          ["Site 5", "-9", "200"]])

_T_CLIMO = dict(
    headers=["Month at Site G", "Mean temperature (degrees Celsius)",
             "Mean precipitation (millimeters)"],
    rows=[["January", "22", "8"],
          ["April", "24", "15"],
          ["July", "27", "210"],
          ["October", "25", "95"]])

_T_TREELINE = dict(
    headers=["Survey decade", "Mean summer temperature (degrees Celsius)",
             "Latitude of the northern edge of the forest (degrees north)"],
    rows=[["First decade", "9.1", "66.4"],
          ["Third decade", "9.8", "66.9"],
          ["Fifth decade", "10.6", "67.7"],
          ["Seventh decade", "11.4", "68.6"]])

_T_LUMBER = dict(
    headers=["Region", "Mean annual precipitation (millimeters)",
             "Length of the frost-free growing season (days)",
             "Standing timber volume (cubic meters per hectare)"],
    rows=[["Region A", "2100", "240", "480"],
          ["Region B", "1150", "165", "260"],
          ["Region C", "420", "190", "35"],
          ["Region D", "760", "70", "90"]])

_T_MOUNTAIN = dict(
    headers=["Elevation on one mountain (meters)", "Mean annual temperature (degrees Celsius)",
             "Mean height of the tallest plants (meters)"],
    rows=[["300", "16", "34"],
          ["1200", "11", "22"],
          ["2100", "6", "9"],
          ["3000", "1", "0.4"]])

_T_SEASONAL = dict(
    headers=["Site", "Annual precipitation (millimeters)",
             "Percent of annual precipitation falling in the four warmest months"],
    rows=[["Site H", "900", "18"],
          ["Site J", "900", "76"]])

_T_POLLEN = dict(
    headers=["Depth in the sediment core (centimeters)",
             "Percent of pollen grains from cold-tolerant conifers",
             "Percent of pollen grains from warm-temperate broadleaf trees"],
    rows=[["20", "12", "77"],
          ["80", "35", "51"],
          ["140", "71", "18"],
          ["200", "89", "4"]])

_T_TRAITS = dict(
    headers=["Site", "Percent of plant species with deep water-storing tissue",
             "Percent of plant species that lose their leaves before winter"],
    rows=[["Site P", "62", "3"],
          ["Site Q", "2", "68"]])

_T_LIMIT = dict(
    headers=["Month at Site R", "Mean temperature (degrees Celsius)",
             "Mean precipitation (millimeters)", "Percent of yearly plant growth"],
    rows=[["January", "-14", "40", "0"],
          ["April", "1", "45", "6"],
          ["July", "14", "48", "80"],
          ["October", "2", "44", "14"]])

QUESTIONS = [

 dict(q="Which statement best expresses what the framework means when it says that a "
        "biome contains characteristic communities of plants and animals?",
      choices=[
        "The plants and animals found there result from, and are adapted to, the climate "
        "of that biome.",
        "The plants and animals found there determine what the climate of that biome will "
        "become.",
        "The plants and animals found there occur in that biome and nowhere else on "
        "Earth.",
        "The plants and animals found there are unrelated to any physical condition of "
        "the biome.",
        "The plants and animals found there are all of a single species."],
      ans=0,
      why="ERT-1.B.1 states that a biome contains characteristic communities of plants "
          "and animals that result from, and are adapted to, its climate. The direction "
          "of the relationship in that sentence runs from climate to community."),

 dict(q="Which of the following is named by the framework as one of the major terrestrial "
        "biomes?",
      choices=[
        "Taiga",
        "Coral reef",
        "Estuary",
        "Open ocean",
        "Marshland"],
      ans=0,
      why="ERT-1.B.2 lists taiga, temperate rainforests, temperate seasonal forests, "
          "tropical rainforests, shrubland, temperate grassland, savanna, desert and "
          "tundra as major terrestrial biomes. The rejected options are aquatic and are "
          "listed elsewhere in the framework."),

 dict(q="According to the framework, the global distribution of nonmineral terrestrial "
        "natural resources varies because of which of the following?",
      choices=[
        "Some combination of climate, geography, latitude and altitude, nutrient "
        "availability, and soil.",
        "Latitude alone, since every other physical condition follows from latitude.",
        "The total human population of the region, since resources are defined by use.",
        "The depth of the ore-bearing rock beneath the region.",
        "The number of animal species already living in the region."],
      ans=0,
      why="ERT-1.B.3 gives exactly that list of factors and says the distribution varies "
          "because of some combination of them, so no single factor is offered as "
          "sufficient on its own."),

 dict(q="Which statement about the worldwide distribution of biomes is supported by the "
        "framework?",
      choices=[
        "It is dynamic: it has changed in the past and may shift again as a result of "
        "global climate changes.",
        "It has been fixed since the biomes first formed and can change only if humans "
        "clear the vegetation.",
        "It changes only over a few years at a time and never over longer spans.",
        "It is determined by soil type alone and is therefore permanent.",
        "It has changed in the past but cannot change again, because the present climate "
        "is stable."],
      ans=0,
      why="ERT-1.B.4 states that the worldwide distribution of biomes is dynamic, that "
          "the distribution has changed in the past, and that it may again shift as a "
          "result of global climate changes."),

 dict(q="The table gives long-term climate averages for five terrestrial sites. Using "
        "only these data, which two sites should be expected to hold the most similar "
        "communities of plants and animals?",
      table=_T_SITES,
      choices=[
        "Site 1 and Site 3, because they are the closest pair on temperature and on "
        "precipitation at the same time.",
        "Site 1 and Site 2, because their mean temperatures are within one degree of "
        "each other.",
        "Site 2 and Site 5, because their precipitation totals are within a few tens of "
        "millimeters of each other.",
        "Site 4 and Site 5, because both lie below the mean temperature of the whole "
        "table.",
        "Site 1 and Site 5, because they lie at the two extremes of the table."],
      ans=0,
      why="ERT-1.B.1 makes the community a result of the climate, so the pair whose "
          "climate is closest should hold the most similar communities. Neither column "
          "alone is the climate: the pair matched on temperature differs by more than two "
          "thousand millimeters of rain, and the pair matched on rainfall differs by more "
          "than thirty degrees."),

 dict(q="Using the same table of five sites, the plants of which site must tolerate both "
        "low temperatures and low precipitation?",
      table=_T_SITES,
      choices=[
        "Site 5, which has the lowest mean temperature and one of the two lowest "
        "precipitation totals.",
        "Site 1, which has the highest precipitation total in the table.",
        "Site 2, which has the lowest precipitation total but one of the highest mean "
        "temperatures.",
        "Site 3, which has one of the highest mean temperatures and one of the highest "
        "precipitation totals.",
        "Site 4, which lies at the middle of the precipitation column."],
      ans=0,
      why="ERT-1.B.1 states that the community of a biome is adapted to its climate, so "
          "the tolerances required are read off both climate columns at once. Only one "
          "site is near the bottom of both."),

 dict(q="Sites 1 and 2 in the table have mean annual temperatures within about one degree "
        "of each other. What does the framework predict about their communities?",
      table=_T_SITES,
      choices=[
        "They should differ substantially, because climate includes precipitation and the "
        "two sites differ enormously in it.",
        "They should be nearly identical, because temperature is the only element of "
        "climate that shapes a community.",
        "They should be nearly identical, because both lie in the warm part of the "
        "table.",
        "They cannot be compared, because the framework treats each site as unique.",
        "They should differ, but only because the two sites lie at different longitudes."],
      ans=0,
      why="ERT-1.B.1 ties the community to the climate rather than to temperature alone, "
          "and the two sites differ by more than two thousand millimeters of annual "
          "precipitation, which is a large difference in climate."),

 dict(q="The table gives four months of climate data for one site. Which description of "
        "the pattern is best supported?",
      table=_T_CLIMO,
      choices=[
        "The site is warm all year and its rainfall is concentrated in part of the year "
        "rather than spread evenly.",
        "The site is warm all year and its rainfall is nearly the same in every month "
        "recorded.",
        "The site has a large annual temperature range and even rainfall.",
        "The site is cold for most of the year and dry throughout.",
        "The site has its wettest month in the coolest month recorded."],
      ans=0,
      why="Every tabulated temperature lies within a few degrees of the others, so the "
          "site is warm throughout, while the precipitation values differ by more than a "
          "factor of ten across the four months, which is the opposite of even."),

 dict(q="For the same site, a student claims that low temperature is what limits plant "
        "growth there. Which feature of the table most directly weakens that claim?",
      table=_T_CLIMO,
      choices=[
        "The coldest month recorded is still well above freezing, so no month is cold "
        "enough to stop growth.",
        "The wettest month recorded is also the warmest month recorded.",
        "The site records precipitation in every month of the table.",
        "The mean temperatures rise steadily from the first row to the last.",
        "The site has more than one month with precipitation below twenty millimeters."],
      ans=0,
      why="A limiting factor must reach a limiting value somewhere in the record. The "
          "lowest temperature in the table is more than twenty degrees above freezing, so "
          "the temperature column never approaches a value that would arrest growth."),

 dict(q="A forest edge in the far north was surveyed once every twenty years, with the "
        "results shown. Which conclusion is best supported?",
      table=_T_TREELINE,
      choices=[
        "The forest edge moved further north as mean summer temperature rose, which is "
        "the kind of shift in biome distribution the framework describes.",
        "The forest edge moved further south as mean summer temperature rose.",
        "The forest edge did not move over the period surveyed.",
        "Mean summer temperature fell over the period surveyed.",
        "The forest edge moved north while mean summer temperature stayed constant."],
      ans=0,
      why="Both tabulated columns increase from the first survey to the last, so the "
          "warming and the poleward movement occurred together. ERT-1.B.4 states that "
          "biome distribution may shift as a result of global climate changes."),

 dict(q="A region's mean annual precipitation is projected to fall by half over the next "
        "century while its temperature rises. What does the framework support predicting "
        "about the biome there?",
      choices=[
        "The biome present may be replaced over time, because biome distribution is "
        "dynamic and shifts with climate change.",
        "The biome present will remain unchanged, because biome boundaries are fixed "
        "features of the Earth.",
        "The biome present will keep its plants but lose all of its animals.",
        "The region will lose its climate but keep its biome.",
        "The biome present will expand, because drier conditions always support more "
        "plant growth."],
      ans=0,
      why="ERT-1.B.4 states that the worldwide distribution of biomes is dynamic and may "
          "shift as a result of global climate changes, and ERT-1.B.1 ties the community "
          "present to the climate, so a large change in climate is a reason to expect a "
          "change in the community."),

 dict(q="Two regions on different continents, thousands of kilometers apart, hold plants "
        "with strikingly similar forms and animals with similar habits. Which explanation "
        "does the framework most directly support?",
      choices=[
        "The two regions have similar climates, and a biome's community results from its "
        "climate.",
        "The two regions must recently have been joined into one landmass.",
        "The two regions must contain exactly the same species.",
        "The similarity must be coincidence, since climate has no bearing on community "
        "form.",
        "The two regions must share the same mineral resources."],
      ans=0,
      why="ERT-1.B.1 states that the characteristic communities of a biome result from, "
          "and are adapted to, its climate, so a shared climate is a sufficient "
          "explanation for shared community form without any shared history or shared "
          "species list."),

 dict(q="The table describes four regions being considered as a source of timber. Which "
        "region is best supported as the most productive source, and on what grounds?",
      table=_T_LUMBER,
      choices=[
        "Region A, because it has both the highest precipitation and the longest growing "
        "season, and it holds the largest standing volume.",
        "Region C, because its growing season is longer than that of one other region "
        "even though it is the driest.",
        "Region D, because its growing season is the shortest, which concentrates growth.",
        "Region B, because its values are closest to the middle of every column.",
        "All four regions are equally productive, because each has some precipitation and "
        "some growing season."],
      ans=0,
      why="ERT-1.B.3 attributes the distribution of nonmineral resources such as trees "
          "for lumber to a combination of factors including climate. The region leading "
          "on both tabulated climate columns also leads on the tabulated standing volume."),

 dict(q="ERT-1.B.3 concerns the distribution of nonmineral terrestrial natural resources. "
        "Which pair of resources falls under that statement?",
      choices=[
        "Fresh water and trees for lumber.",
        "Copper ore and iron ore.",
        "Coal seams and natural gas reservoirs.",
        "Phosphate rock and limestone.",
        "Gold deposits and bauxite."],
      ans=0,
      why="ERT-1.B.3 names water and trees for lumber as its examples of nonmineral "
          "terrestrial natural resources. Every rejected pair consists of mineral or "
          "fossil deposits, which the word nonmineral excludes."),

 dict(q="Data were collected at four elevations on a single mountain, as shown. Which "
        "conclusion is best supported?",
      table=_T_MOUNTAIN,
      choices=[
        "Temperature falls with elevation and the vegetation becomes shorter, so altitude "
        "is acting as a factor in what the site can support.",
        "Temperature rises with elevation and the vegetation becomes taller.",
        "Temperature is constant with elevation, so the change in vegetation must be "
        "caused by something else.",
        "The tallest plants occur at the highest elevation recorded.",
        "Elevation affects temperature but has no relationship with the vegetation."],
      ans=0,
      why="Reading the two columns together, temperature decreases and plant height "
          "decreases as elevation rises. ERT-1.B.3 names latitude and altitude among the "
          "factors behind the distribution of terrestrial resources."),

 dict(q="Why does latitude appear in the framework's list of factors behind the "
        "distribution of terrestrial natural resources?",
      choices=[
        "Because latitude is one of several factors whose combination sets the physical "
        "conditions a place offers.",
        "Because latitude alone fixes the resources of a place, making the other factors "
        "unnecessary.",
        "Because resources are measured in degrees of latitude.",
        "Because latitude determines the mineral content of the underlying rock.",
        "Because places at the same latitude always hold identical resources."],
      ans=0,
      why="ERT-1.B.3 says the distribution varies because of some combination of climate, "
          "geography, latitude and altitude, nutrient availability, and soil. The phrase "
          "some combination is what rules out treating any one of them as sufficient."),

 dict(q="Two neighboring areas share the same latitude, altitude and annual rainfall, but "
        "one supports dense timber and the other supports only sparse low plants. Which "
        "of the framework's listed factors best explains the difference?",
      choices=[
        "A difference in the soil and in nutrient availability between the two areas.",
        "A difference in latitude between the two areas.",
        "A difference in altitude between the two areas.",
        "A difference in annual rainfall between the two areas.",
        "No factor can explain it, because the two areas share their climate."],
      ans=0,
      why="ERT-1.B.3 lists nutrient availability and soil alongside climate, latitude and "
          "altitude. The stem holds every other listed factor constant, so the two that "
          "remain are the only candidates the statement offers."),

 dict(q="A biome is called a temperate rainforest. What do the two parts of that name "
        "together indicate about its climate?",
      choices=[
        "Moderate temperatures together with high precipitation.",
        "Moderate temperatures together with very low precipitation.",
        "Very high temperatures together with high precipitation.",
        "Very low temperatures together with low precipitation.",
        "Very high temperatures together with very low precipitation."],
      ans=0,
      why="The name itself carries the two climate elements: temperate is the moderate "
          "temperature range and rainforest is heavy precipitation. ERT-1.B.1 ties the "
          "community present to exactly those climate conditions."),

 dict(q="A student writes that the plants and animals of a region create the climate that "
        "region has. What is the best correction, according to the framework?",
      choices=[
        "The framework runs the relationship the other way: the community results from, "
        "and is adapted to, the climate.",
        "The framework treats the community and the climate as entirely independent of "
        "each other.",
        "The framework says the community creates the soil, which then creates the "
        "climate.",
        "The framework says the community creates the climate only in tropical regions.",
        "The student is correct, because vegetation is part of the climate system."],
      ans=0,
      why="ERT-1.B.1 states that the characteristic communities of a biome result from, "
          "and are adapted to, its climate. The stated direction of the relationship is "
          "climate to community."),

 dict(q="Two sites receive the same annual precipitation total but distribute it very "
        "differently across the year, as shown. What does the framework support "
        "concluding?",
      table=_T_SEASONAL,
      choices=[
        "The two sites may support different communities, because the timing of "
        "precipitation is part of the climate a community is adapted to.",
        "The two sites must support identical communities, because the annual totals are "
        "equal.",
        "The site with more of its rain in the warm months must be colder overall.",
        "Neither site can support plant life, because neither receives a thousand "
        "millimeters.",
        "The annual totals shown must be in error, because they are equal."],
      ans=0,
      why="ERT-1.B.1 makes the community a result of the climate, and the climate of a "
          "place includes when its precipitation falls, not only how much falls. The "
          "table separates the two sites on exactly that variable."),

 dict(q="Pollen grains preserved at four depths in a lake sediment core were counted, "
        "with the results shown. Deeper samples are older. Which conclusion is best "
        "supported?",
      table=_T_POLLEN,
      choices=[
        "The vegetation at this place changed over time from mostly cold-tolerant to "
        "mostly warm-temperate, so the biome present here has not been fixed.",
        "The vegetation at this place changed from mostly warm-temperate to mostly "
        "cold-tolerant over time.",
        "The vegetation at this place has been unchanged throughout the record.",
        "Only cold-tolerant conifers are represented anywhere in the core.",
        "The deepest sample contains the largest share of warm-temperate broadleaf "
        "pollen."],
      ans=0,
      why="Moving from the deepest sample to the shallowest, the conifer share falls and "
          "the broadleaf share rises, so the younger record is the warmer-adapted one. "
          "ERT-1.B.4 states that the distribution of biomes has changed in the past."),

 dict(q="Which finding would most directly support the framework's claim that the "
        "distribution of biomes has changed in the past?",
      choices=[
        "Preserved plant remains showing that a place now covered by tundra once carried "
        "forest.",
        "A survey showing that two present-day biomes contain different animal species.",
        "A map showing where the major biomes are found today.",
        "A measurement of how much lumber a present-day forest produces each year.",
        "A record showing that one species of tree grows faster in warm years."],
      ans=0,
      why="ERT-1.B.4 is a claim about change over time in where biomes occur, so the "
          "evidence that bears on it is evidence of a different community at a known "
          "place in the past. A present-day survey or map cannot show change."),

 dict(q="A student argues that because a biome is defined by its climate, biome "
        "boundaries can never move. Which part of the framework contradicts this?",
      choices=[
        "The statement that the worldwide distribution of biomes is dynamic and may shift "
        "with global climate changes.",
        "The statement that a biome contains characteristic communities of plants and "
        "animals.",
        "The statement listing taiga, savanna and tundra among the major biomes.",
        "The statement that nonmineral resources include water and trees for lumber.",
        "The statement that competition occurs where resources are limited."],
      ans=0,
      why="The student's reasoning would hold only if climate itself never moved. "
          "ERT-1.B.4 denies exactly that, stating that biome distribution has changed in "
          "the past and may shift again as the global climate changes."),

 dict(q="Plant traits were surveyed at two sites, as shown. Which pairing of site to "
        "climate is best supported?",
      table=_T_TRAITS,
      choices=[
        "The site whose species mostly store water in their tissues is the drier of the "
        "two.",
        "The site whose species mostly store water in their tissues is the wetter of the "
        "two.",
        "Both sites must have the same climate, because both support plants.",
        "The site whose species mostly drop their leaves before winter has no cold "
        "season.",
        "Neither site's traits carry any information about its climate."],
      ans=0,
      why="ERT-1.B.1 states that the community of a biome is adapted to its climate, so "
          "a community dominated by water-storing tissue points to a climate in which "
          "water is scarce, and a community dominated by leaf loss before winter points "
          "to a cold season."),

 dict(q="Two places are both classified as desert, although one is hot throughout the "
        "year and the other is cold for much of it. Which shared climatic feature best "
        "justifies giving them one name?",
      choices=[
        "Both receive very little precipitation.",
        "Both have very high mean annual temperatures.",
        "Both lie at the same latitude.",
        "Both have deep, nutrient-rich soils.",
        "Both have the same length of growing season."],
      ans=0,
      why="The name desert carries aridity rather than heat, and ERT-1.B.1 ties a biome's "
          "community to its climate, so the shared feature that supports one classifi"
          "cation across very different temperatures is the shared shortage of water."),

 dict(q="Monthly data from one site are shown together with the share of the year's plant "
        "growth occurring in each month. Which conclusion is best supported?",
      table=_T_LIMIT,
      choices=[
        "Growth is concentrated in the warmest month even though precipitation is nearly "
        "constant, so temperature rather than precipitation limits growth here.",
        "Growth is concentrated in the wettest month, so precipitation limits growth "
        "here.",
        "Growth is spread evenly through the year, so nothing limits it.",
        "Growth is greatest in the coldest month recorded.",
        "Precipitation varies by more than a factor of two across the months recorded."],
      ans=0,
      why="The precipitation column varies by only a few millimeters across the four "
          "months while the temperature column spans nearly thirty degrees, and growth "
          "tracks the temperature column. The variable that changes is the candidate for "
          "the limiting factor."),

 dict(q="A gardener moves a plant from the region where it grows naturally into a region "
        "with a very different climate, and the plant dies. Which framework statement "
        "best accounts for the outcome?",
      choices=[
        "The plants of a biome are adapted to the climate of that biome.",
        "The plants of a biome determine the climate of that biome.",
        "The distribution of biomes has changed in the past.",
        "Nonmineral resources include water and trees for lumber.",
        "Major terrestrial biomes include taiga, savanna and tundra."],
      ans=0,
      why="ERT-1.B.1 states that the characteristic communities of a biome result from, "
          "and are adapted to, its climate, so a plant carried outside the climate it is "
          "adapted to has no reason to survive there."),

 dict(q="Why is the world's supply of timber not spread evenly across the land surface?",
      choices=[
        "Because the physical conditions that trees require vary from place to place with "
        "climate, geography, latitude and altitude, nutrients, and soil.",
        "Because trees grow equally well anywhere and the difference is only in how much "
        "is cut.",
        "Because timber is a mineral resource and follows the distribution of ore bodies.",
        "Because latitude is the only factor that varies across the land surface.",
        "Because the distribution of biomes is fixed and has never varied."],
      ans=0,
      why="ERT-1.B.3 names trees for lumber as an example of a nonmineral terrestrial "
          "resource and attributes the uneven distribution of such resources to some "
          "combination of the six factors it lists."),

 dict(q="Which of the following is the best reason that a list of major terrestrial "
        "biomes includes both temperate grassland and savanna as separate entries?",
      choices=[
        "They are distinct biomes, each with its own characteristic community arising "
        "from its own climate.",
        "They are two names for the same biome, kept for historical reasons.",
        "One is a terrestrial biome and the other is an aquatic biome.",
        "One is defined by its soil and the other by its animals only.",
        "They differ only in the continent on which they are found."],
      ans=0,
      why="ERT-1.B.2 lists temperate grassland and savanna as separate major terrestrial "
          "biomes, and ERT-1.B.1 makes each biome's community a result of its own "
          "climate, which is what makes them distinct rather than interchangeable."),

 dict(q="Which combination of evidence would best support the claim that a shift in "
        "climate, rather than local land clearing, moved a biome boundary?",
      choices=[
        "The boundary moved in the same direction across many separate, unmanaged sites "
        "while regional temperature and precipitation changed.",
        "The boundary moved at one site where the land had recently been cleared.",
        "The boundary is currently in a different place from where a map put it.",
        "One species near the boundary became more abundant over a single year.",
        "Trees near the boundary are taller than trees far from it."],
      ans=0,
      why="ERT-1.B.4 attributes shifts in biome distribution to global climate changes, "
          "so the observation that separates that cause from a local one is a consistent "
          "movement across many unmanaged sites accompanied by a measured change in "
          "climate."),
]
