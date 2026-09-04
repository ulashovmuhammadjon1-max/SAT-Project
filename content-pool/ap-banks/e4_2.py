# AP ENVIRONMENTAL SCIENCE 4.2 Soil Formation and Erosion
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ERT-4: Earth's systems interact, resulting in a state of balance
# over time.
# Learning objective ERT-4.B: describe the characteristics and formation of soil.
# Suggested skill 4.B, identify a research method, design, and/or measure used.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-4.B.1  Soils are formed when parent material is weathered, transported, and
#              deposited.
#   ERT-4.B.2  Soils are generally categorized by horizons based on their composition and
#              organic material.
#   ERT-4.B.3  Soils can be eroded by winds or water. Protecting soils can protect water
#              quality as soils effectively filter and clean water that moves through them.
#
# THE THREE STATEMENTS ARE SHORT AND EACH SPLITS CLEANLY:
#   ERT-4.B.1  a starting material (PARENT MATERIAL) and three processes in a stated ORDER
#              -- weathered, then transported, then deposited
#   ERT-4.B.2  the unit of categorisation (HORIZONS) and the two things the categories rest
#              on (COMPOSITION and ORGANIC MATERIAL), hedged with GENERALLY
#   ERT-4.B.3  two agents of erosion (WINDS or WATER); a consequence of protecting soils
#              (WATER QUALITY); and the reason for it (soils FILTER AND CLEAN water that
#              moves through them)
#
# THE SUGGESTED SKILL IS 4.B, IDENTIFY A RESEARCH METHOD, DESIGN OR MEASURE, so items 12,
# 13 and 14 ask which measurement or comparison would bear on one of these statements
# rather than what the statement says.
#
# NOT KEYED, because the framework does not state it: the letters used to name horizons,
# any particular kind of weathering, how long soil takes to form, how deep a soil is, and
# the mechanism by which a soil filters water. Item 16 keys that last absence rather than
# filling it, and no item asks a student to name a horizon by letter.
#
# BOUNDARY WITH 4.3. Water holding capacity, porosity, permeability, fertility and the soil
# texture triangle are ERT-4.C.1 to ERT-4.C.4 and belong to the next topic. Item 17 states
# the line rather than crossing it, and no key here asserts a property of a soil type.
#
# NO FIGURES. The layers, the plots, the water samples and the soil depths are all
# tabulated and the questions are asked of the tables.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.2", "Soil Formation and Erosion", 4)

_T_FORMATION = dict(
    headers=["Site", "Years since the parent material was first exposed",
             "Depth of soil formed (centimeters)"],
    rows=[["Site 1", "200", "3"],
          ["Site 2", "1000", "14"],
          ["Site 3", "5000", "62"],
          ["Site 4", "12000", "120"]])

_T_HORIZON = dict(
    headers=["Layer of the soil, from the surface downward",
             "Depth below the surface (centimeters)",
             "Organic material (percent by mass)",
             "Sand, silt and clay together (percent by mass)"],
    rows=[["Layer 1", "5", "62", "38"],
          ["Layer 2", "25", "9", "91"],
          ["Layer 3", "70", "3", "97"],
          ["Layer 4", "120", "1", "99"]])

_T_EROSION = dict(
    headers=["Plot", "Soil lost to wind (tonnes per hectare per year)",
             "Soil lost to running water (tonnes per hectare per year)",
             "Total soil lost (tonnes per hectare per year)"],
    rows=[["Bare and level", "6.0", "4.0", "10.0"],
          ["Bare and sloping", "5.0", "19.0", "24.0"],
          ["Covered and level", "0.5", "0.4", "0.9"],
          ["Covered and sloping", "0.6", "2.4", "3.0"]])

_T_FILTER = dict(
    headers=["Water sampled", "Sediment carried (milligrams per liter)",
             "Nitrate carried (milligrams per liter)"],
    rows=[["Rain as it falls on the surface", "12", "4.0"],
          ["Water that has moved down through intact soil", "2", "1.2"],
          ["Water running off ground whose soil has been stripped away", "140", "6.5"]])

QUESTIONS = [

 dict(q="According to the framework, what are soils formed from, and by what processes?",
      choices=[
        "Parent material that is weathered, transported, and deposited",
        "Organic material alone, with no mineral source involved",
        "Water moving downward through a soil that already exists",
        "Wind acting on bare rock, with no parent material involved",
        "Rock that is deposited first and only afterwards weathered"],
      ans=0,
      why="ERT-4.B.1 states that soils are formed when parent material is weathered, "
          "transported, and deposited. The rejected options remove the parent material, "
          "remove one of the processes, or put the deposition before the weathering."),

 dict(q="In what order does the framework place the three processes that form a soil?",
      choices=[
        "Weathered first, then transported, then deposited",
        "Deposited first, then transported, then weathered",
        "Transported first, then weathered, then deposited",
        "Deposited first, then weathered, then transported",
        "The framework names the three processes but gives no order among them"],
      ans=0,
      why="ERT-4.B.1 lists the processes as weathered, transported, and deposited, in that "
          "sequence. Each rejected option reverses the sequence or moves the deposition to "
          "the front."),

 dict(q="What does the framework call the starting material a soil is formed from?",
      choices=["Parent material", "Topsoil", "Loam", "Organic matter", "Groundwater"],
      ans=0,
      why="ERT-4.B.1 names parent material as the thing that is weathered, transported and "
          "deposited. Loam belongs to ERT-4.C.4 and is a blend of clay, silt and sand "
          "rather than the source a soil forms from."),

 dict(q="How does the framework say soils are generally categorized?",
      choices=[
        "By horizons, on the basis of their composition and organic material",
        "By the depth of the water table lying beneath them",
        "By the crops that are grown on them",
        "By the direction of the prevailing wind above them",
        "By the age of the parent material alone"],
      ans=0,
      why="ERT-4.B.2 states that soils are generally categorized by horizons based on their "
          "composition and organic material. The rejected options substitute a quantity the "
          "statement never mentions."),

 dict(q="On which two things does the framework say those horizon categories are based?",
      choices=[
        "Composition and organic material",
        "Temperature and rainfall",
        "Slope and area",
        "Colour and smell",
        "Depth and latitude"],
      ans=0,
      why="ERT-4.B.2 names composition and organic material as the basis of the horizons. "
          "Slope and area belong to the watershed statement ERT-4.F.1, and the remaining "
          "pairs appear nowhere in this topic."),

 dict(q="ERT-4.B.2 says soils are GENERALLY categorized by horizons. What does that word "
        "establish?",
      choices=[
        "That horizons are the usual basis of the categories rather than the only "
        "arrangement anyone has ever used",
        "That soils are never categorized by horizons in practice",
        "That every soil on Earth has exactly the same horizons",
        "That the categories change from one year to the next",
        "That horizons are used only for soils that have been eroded"],
      ans=0,
      why="GENERALLY commits the framework to horizons as the ordinary basis of the "
          "categories while stopping short of asserting it is the only one. Hardening it "
          "into every soil having identical horizons is stronger than the statement, and "
          "denying the practice is weaker."),

 dict(q="Which agents does the framework name as able to erode soils?",
      choices=["Winds or water", "Winds only", "Water only",
               "Earthquakes or volcanic eruptions", "Plant roots or burrowing animals"],
      ans=0,
      why="ERT-4.B.3 states that soils can be eroded by winds or water, naming both and "
          "requiring neither. Earthquakes and volcanoes belong to the plate boundary "
          "statements in topic 4.1 and are not named here."),

 dict(q="Besides the soil itself, what does the framework say protecting soils can protect?",
      choices=["Water quality", "Air quality", "The depth of the parent material",
               "The direction of the prevailing wind", "The number of plate boundaries"],
      ans=0,
      why="ERT-4.B.3 states that protecting soils can protect water quality. It names no "
          "other thing that soil protection protects, and the rejected options are "
          "quantities from other topics."),

 dict(q="What reason does the framework give for that connection between soils and water "
        "quality?",
      choices=[
        "Soils effectively filter and clean water that moves through them",
        "Soils prevent rain from ever reaching a river",
        "Soils store water permanently and never release any of it",
        "Soils add nutrients to water in order to improve it",
        "Soils have no effect at all on the water that moves through them"],
      ans=0,
      why="ERT-4.B.3 states that protecting soils can protect water quality AS soils "
          "effectively filter and clean water that moves through them, so the filtering and "
          "cleaning is the reason it gives. The statement neither stops the water nor holds "
          "it permanently."),

 dict(q="A land manager fences livestock away from a stream bank so that the soil there is "
        "no longer trampled and washed away. Beyond keeping the soil, what does the "
        "framework say this can protect?",
      choices=[
        "The quality of the water, because soils filter and clean the water moving through "
        "them",
        "The composition of the parent material lying beneath the soil",
        "The number of horizons into which the soil is divided",
        "The speed at which the wind blows across the field",
        "Nothing at all beyond the soil itself"],
      ans=0,
      why="ERT-4.B.3 states that protecting soils can protect water quality as soils "
          "effectively filter and clean water that moves through them, which is exactly "
          "what keeping the soil on a stream bank does. The statement attaches no other "
          "consequence to protecting a soil."),

 dict(q="Which of the following is NOT part of the framework's account of how a soil is "
        "formed?",
      choices=[
        "Filtration of water through the finished soil",
        "Weathering of parent material",
        "Transport of parent material",
        "Deposition of parent material",
        "The presence of parent material to begin with"],
      ans=0,
      why="ERT-4.B.1 names weathering, transport and deposition acting on parent material. "
          "Filtering and cleaning water is what ERT-4.B.3 says a soil already formed does, "
          "not a step in forming one."),

 dict(q="A researcher wants to test whether planting a cover crop reduces the soil a field "
        "loses to wind. Which measure should be taken?",
      choices=[
        "The mass of soil carried off each plot, on plots with the cover crop and on plots "
        "without it",
        "The number of horizons found in the soil on each plot",
        "The colour of the parent material lying under each plot",
        "The total rainfall over the whole region during the year",
        "The area of the watershed the field sits in"],
      ans=0,
      why="ERT-4.B.3 states that soils can be eroded by winds or water, so the quantity at "
          "issue is how much soil leaves, and the cover crop is the one thing that should "
          "differ between the plots compared. Each rejected measure records something that "
          "does not change with the treatment."),

 dict(q="A researcher wants to test the framework's claim that protecting soils protects "
        "water quality. Which design does that most directly?",
      choices=[
        "Compare the quality of water leaving plots where the soil is intact with the "
        "quality of water leaving plots where the soil has been stripped away",
        "Measure the depth of the soil on a single plot on one occasion",
        "Count the horizons visible in the soil of one plot",
        "Measure the speed of the wind above one plot through the year",
        "Record which crops are grown across the surrounding region"],
      ans=0,
      why="ERT-4.B.3 connects the presence of soil to the quality of the water moving "
          "through it, so a test has to vary the soil and measure the water. A single "
          "measurement on one plot varies nothing, and the remaining options measure "
          "neither the soil nor the water leaving it."),

 dict(q="Which measurements would show whether a soil is being categorized on the basis the "
        "framework names?",
      choices=[
        "The composition and the organic content of each layer in turn",
        "The temperature of the air above the soil through the year",
        "The area of the field measured in hectares",
        "The distance from the field to the nearest plate boundary",
        "The number of plant species growing on the surface"],
      ans=0,
      why="ERT-4.B.2 states that soils are generally categorized by horizons based on their "
          "composition and organic material, so those two quantities, measured layer by "
          "layer, are what the categories rest on. None of the rejected measurements is "
          "named in the statement."),

 dict(q="One field loses soil during a period of heavy rain and a neighbouring field loses "
        "soil during a dry windstorm. What does the framework say about the two cases?",
      choices=[
        "Both are erosion of soil, since the framework names winds and water as agents that "
        "can erode soils",
        "Only the case involving running water counts as erosion",
        "Only the case involving wind counts as erosion",
        "Neither counts as erosion, because erosion occurs only at a plate boundary",
        "The framework names neither wind nor water as an agent of erosion"],
      ans=0,
      why="ERT-4.B.3 states that soils can be eroded by winds or water, so both agents "
          "count and neither is required for the other to. The statement makes no reference "
          "to plate boundaries."),

 dict(q="Which of these does the framework's account of soil formation leave unstated?",
      choices=[
        "How long the weathering, transport and deposition take",
        "That parent material is weathered",
        "That parent material is transported",
        "That parent material is deposited",
        "That a soil is formed from parent material"],
      ans=0,
      why="ERT-4.B.1 supplies the starting material and the three processes and no "
          "timescale for any of them. The four rejected options are the statement's own "
          "content."),

 dict(q="How does the framework's claim about horizons differ from its separate claim about "
        "particle size and composition affecting porosity, permeability and fertility?",
      choices=[
        "This claim says horizons are the basis on which soils are categorized, while that "
        "one says what the particle size and composition of a horizon go on to affect",
        "This claim says what the particle size and composition of a horizon go on to "
        "affect, while that one says horizons are the basis on which soils are categorized",
        "The two claims say the same thing in different words",
        "This claim concerns water quality while that one concerns the wind",
        "Neither claim mentions a horizon at all"],
      ans=0,
      why="ERT-4.B.2 states that soils are generally categorized by horizons based on their "
          "composition and organic material. ERT-4.C.2, in the next topic, states that the "
          "particle size and composition of each horizon can affect the porosity, "
          "permeability and fertility of the soil. One statement sets up the unit and the "
          "other says what its properties do."),

 dict(q="Which of these does the framework NOT claim about soils and water?",
      choices=[
        "That a soil adds nutrients to the water passing through it",
        "That soils can be eroded by water",
        "That protecting soils can protect water quality",
        "That soils filter water that moves through them",
        "That soils clean water that moves through them"],
      ans=0,
      why="ERT-4.B.3 supplies the four rejected statements in its own words. It describes "
          "the soil as filtering and cleaning the water, which is a removal from the water, "
          "and it never describes a soil as adding anything to it."),

 dict(q="Soil depth was measured at four sites differing in how long their parent material "
        "had been exposed. What does the record establish?",
      table=_T_FORMATION,
      choices=[
        "More soil had formed at the sites whose parent material had been exposed longer",
        "More soil had formed at the sites whose parent material had been exposed for the "
        "shortest time",
        "The same depth of soil had formed at all four sites",
        "No soil had formed at any of the four sites",
        "The time of exposure and the depth of soil are unrelated across the four sites"],
      ans=0,
      why="Ordered by the time since exposure the soil depths run 3, 14, 62 and 120 "
          "centimeters, rising at every step. ERT-4.B.1 states that soils are formed when "
          "parent material is weathered, transported, and deposited, so a soil is something "
          "that accumulates on parent material rather than something present from the "
          "start."),

 dict(q="Using the same four sites, about how much soil had formed for each thousand years "
        "of exposure at the oldest site?",
      table=_T_FORMATION,
      choices=[
        "About 10 centimeters per thousand years",
        "About 120 centimeters per thousand years",
        "About 62 centimeters per thousand years",
        "About 14 centimeters per thousand years",
        "A rate cannot be formed from the record"],
      ans=0,
      why="The oldest site records 120 centimeters over 12,000 years, and 120 divided by "
          "12 is 10. The rejected values are the depth itself and the depths recorded at "
          "two of the other sites."),

 dict(q="A soil was sampled layer by layer from the surface downward. Which layer holds the "
        "most organic material?",
      table=_T_HORIZON,
      choices=[
        "The layer nearest the surface",
        "The layer deepest below the surface",
        "The second layer down from the surface",
        "All four layers hold the same amount of organic material",
        "The record reports depth but not organic material"],
      ans=0,
      why="The organic percentages are 62, 9, 3 and 1 and the largest is unique and belongs "
          "to the shallowest layer. ERT-4.B.2 makes organic material one of the two things "
          "the horizon categories are based on."),

 dict(q="What happens to the organic content of that soil as the depth below the surface "
        "increases?",
      table=_T_HORIZON,
      choices=[
        "It falls at every step down the record",
        "It rises at every step down the record",
        "It is unchanged from layer to layer",
        "It falls and then rises again in the deepest layer",
        "The record does not report organic content"],
      ans=0,
      why="Ordered by depth the organic percentages read 62, 9, 3 and 1, falling at every "
          "step. ERT-4.B.2 states that soils are generally categorized by horizons based on "
          "their composition and organic material, and a change of that size from layer to "
          "layer is what distinguishes one horizon from the next."),

 dict(q="In each layer of that same record, what do the two composition columns together "
        "account for?",
      table=_T_HORIZON,
      choices=[
        "The whole of the layer, since the two percentages add to one hundred in every layer",
        "About half of the layer, with the rest unreported",
        "Only the deepest layer, since the shallower ones are unreported",
        "Nothing, since the two columns are measured in different units",
        "More than the whole layer, since the two percentages add to more than one hundred"],
      ans=0,
      why="Adding the organic percentage to the mineral percentage gives one hundred in "
          "every one of the four layers. ERT-4.B.2 names composition and organic material "
          "as the two things the horizon categories rest on, and here they are reported as "
          "shares of the same whole."),

 dict(q="Which two quantities does that layer by layer record report about the soil?",
      table=_T_HORIZON,
      choices=[
        "Exactly the two the framework names as the basis of horizons: composition and "
        "organic material",
        "The slope of the ground and the area of the field",
        "The rainfall received and the wind speed above the surface",
        "The crop grown and the yield harvested",
        "The distance to the nearest stream and the depth of the water table"],
      ans=0,
      why="Beside the depth of each layer the record carries an organic percentage and a "
          "mineral percentage, which are organic material and composition. ERT-4.B.2 states "
          "that soils are generally categorized by horizons based on their composition and "
          "organic material."),

 dict(q="Four plots were watched for a year and the soil each lost was recorded by the "
        "agent that removed it. What does the record establish?",
      table=_T_EROSION,
      choices=[
        "Both wind and running water removed soil from every plot",
        "Wind removed soil but running water removed none",
        "Running water removed soil but wind removed none",
        "Neither agent removed any soil from any plot",
        "Only the sloping plots lost soil to either agent"],
      ans=0,
      why="Every plot records a loss above zero in both the wind column and the running "
          "water column. ERT-4.B.3 states that soils can be eroded by winds or water, "
          "naming both agents."),

 dict(q="Which of those four plots lost the most soil in total during the year?",
      table=_T_EROSION,
      choices=[
        "The bare sloping plot",
        "The bare level plot",
        "The covered sloping plot",
        "The covered level plot",
        "All four plots lost the same total"],
      ans=0,
      why="The totals are 10.0, 24.0, 0.9 and 3.0 tonnes per hectare and the largest is "
          "unique. ERT-4.B.3 names winds and water as agents that can erode soils, and the "
          "plot losing most is the one that is both bare and sloping."),

 dict(q="How much less soil did the covered sloping plot lose than the bare sloping plot?",
      table=_T_EROSION,
      choices=[
        "21.0 tonnes per hectare less",
        "24.0 tonnes per hectare less",
        "9.1 tonnes per hectare less",
        "3.0 tonnes per hectare less",
        "The record does not allow that comparison"],
      ans=0,
      why="The two totals are 24.0 and 3.0 tonnes per hectare, and 24.0 less 3.0 is 21.0. "
          "The rejected values are the two totals themselves and the difference between a "
          "different pair of plots."),

 dict(q="Three samples of water were compared for what they carried. What does the record "
        "establish?",
      table=_T_FILTER,
      choices=[
        "Water that had moved through intact soil carried less than the rain that fell, "
        "while runoff from stripped ground carried far more",
        "Water that had moved through intact soil carried more than the rain that fell, "
        "while runoff from stripped ground carried far less",
        "All three samples carried the same amounts",
        "The rain carried more than either of the other two samples",
        "The record reports sediment but not nitrate"],
      ans=0,
      why="Against the rain's 12 milligrams of sediment and 4.0 of nitrate per liter, the "
          "water that had passed through intact soil carries 2 and 1.2 while the runoff "
          "from stripped ground carries 140 and 6.5. ERT-4.B.3 states that protecting soils "
          "can protect water quality as soils effectively filter and clean water that moves "
          "through them."),

 dict(q="Using those same samples, how many times as much sediment does the runoff from "
        "stripped ground carry as the water that has passed through intact soil?",
      table=_T_FILTER,
      choices=["About 70 times as much", "About 12 times as much", "About 7 times as much",
               "About 2 times as much", "Less, rather than more"],
      ans=0,
      why="The two sediment readings are 140 and 2 milligrams per liter, and 140 divided by "
          "2 is 70. The rejected values are the sediment carried by the rain and smaller "
          "multiples that the two readings do not support."),

 dict(q="Which single sentence collects what this topic's three statements assert and "
        "nothing further?",
      choices=[
        "Soils form when parent material is weathered, then transported, then deposited; "
        "they are generally categorized by horizons based on composition and organic "
        "material; and they can be eroded by winds or water, so protecting them protects "
        "water quality because soils filter and clean the water moving through them",
        "Soils form when parent material is deposited, then transported, then weathered; "
        "they are categorized by the crops grown on them; and they can be eroded by wind "
        "alone",
        "Soils form when parent material is weathered, then transported, then deposited; "
        "they are generally categorized by horizons based on composition and organic "
        "material; and they can be eroded by water alone, so protecting them has no effect "
        "on water quality",
        "Soils form from organic material alone; they are categorized by horizons based on "
        "composition and organic material; and they can be eroded by winds or water",
        "Soils form when parent material is weathered, then transported, then deposited; "
        "they are generally categorized by horizons based on composition and organic "
        "material; and they can be eroded by winds or water, so protecting them protects "
        "water quality because soils add nutrients to the water moving through them"],
      ans=0,
      why="ERT-4.B.1 supplies the parent material and the three processes in order, "
          "ERT-4.B.2 the horizons and the two things they rest on with its hedge, and "
          "ERT-4.B.3 the two agents of erosion, the protection of water quality, and the "
          "filtering and cleaning that is its reason. Each rejected summary reverses the "
          "order of the processes, drops an agent of erosion, changes what the categories "
          "rest on, or replaces the filtering with an addition to the water."),
]
