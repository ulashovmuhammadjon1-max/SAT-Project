# AP ENVIRONMENTAL SCIENCE 4.3 Soil Composition and Properties
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ERT-4: Earth's systems interact, resulting in a state of balance
# over time.
# Learning objective ERT-4.C: describe similarities and differences between properties of
# different soil types.
# Suggested skill 4.C, describe an aspect of a research method, design, and/or measure used.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-4.C.1  Water holding capacity, the total amount of water soil can hold, varies with
#              different soil types. Water retention contributes to land productivity and
#              fertility of soils.
#   ERT-4.C.2  The particle size and composition of each soil horizon can affect the
#              porosity, permeability, and fertility of the soil.
#   ERT-4.C.3  There are a variety of methods to test the chemical, physical, and biological
#              properties of soil that can aid in a variety of decisions, such as irrigation
#              and fertilizer requirements.
#   ERT-4.C.4  A soil texture triangle allows for the identification and comparison of soil
#              types based on their percentages of clay, silt, and sand. Loam consists of a
#              blend of clay, silt, and sand that can support a variety of crops.
#
# WHAT THE FRAMEWORK DOES AND DOES NOT SAY ABOUT SOIL TYPES. It says water holding capacity
# VARIES with soil type. It does NOT say which type holds the most, and no key here asserts
# one. Where a comparison between soil types is needed the measurements are TABULATED and
# the question is a reading of the table; the framework supplies only that such variation
# exists and what it contributes to.
#
# THE SAME CAUTION APPLIES TO POROSITY AND PERMEABILITY. ERT-4.C.2 says particle size and
# composition CAN AFFECT them; it does not say in which direction. Items 25 to 28 read a
# tabulated record and no key states a direction as a claim of the framework.
#
# LOAM. ERT-4.C.4 says loam consists of a BLEND of clay, silt, and sand. Item 22 keys the
# one tabulated sample in which no single component makes up more than half, which is a
# criterion the table settles arithmetically. No key assigns a named soil type to a
# percentage range, because the framework fixes none.
#
# NO FIGURES, and this topic is normally taught from one. A soil texture triangle cannot be
# shown here, so the percentages are put in a table= and every question about texture is
# asked of those numbers. The three percentages add to one hundred in every sample and the
# verifier recomputes that sum.
#
# NOT KEYED: any named horizon letter, any named soil order, a numerical boundary between
# soil types, and a mechanism by which particle size changes porosity.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.3", "Soil Composition and Properties", 4)

_T_WHC = dict(
    headers=["Soil type", "Water the soil can hold (centimeters of water per meter of soil)",
             "Grain yield recorded on it (tonnes per hectare)"],
    rows=[["Coarse sand", "60", "1.8"],
          ["Sandy loam", "110", "3.4"],
          ["Loam", "170", "5.1"],
          ["Clay loam", "190", "5.6"]])

_T_TEXTURE = dict(
    headers=["Soil sample", "Clay (percent)", "Silt (percent)", "Sand (percent)"],
    rows=[["Sample 1", "12", "20", "68"],
          ["Sample 2", "20", "40", "40"],
          ["Sample 3", "55", "30", "15"],
          ["Sample 4", "8", "78", "14"]])

_T_POROSITY = dict(
    headers=["Horizon sampled", "Typical particle diameter (millimeters)",
             "Porosity (percent of the volume that is pore space)",
             "Permeability (centimeters of water passing through per hour)"],
    rows=[["Horizon A", "0.60", "38", "22.0"],
          ["Horizon B", "0.05", "44", "1.6"],
          ["Horizon C", "0.002", "52", "0.05"]])

_T_TESTS = dict(
    headers=["Field tested", "Nitrogen found in the soil (kilograms per hectare)",
             "Water held by the soil at the time of the test (percent by volume)",
             "Fertilizer the grower then applied (kilograms per hectare)",
             "Irrigation the grower then applied (millimeters)"],
    rows=[["Field 1", "120", "31", "20", "10"],
          ["Field 2", "70", "24", "70", "40"],
          ["Field 3", "35", "16", "105", "90"]])

QUESTIONS = [

 dict(q="What does the framework say water holding capacity is?",
      choices=[
        "The total amount of water a soil can hold",
        "The rate at which water passes downward through a soil",
        "The depth of the water table lying beneath a soil",
        "The amount of water a crop takes up over one season",
        "The share of a soil that is made up of organic material"],
      ans=0,
      why="ERT-4.C.1 defines water holding capacity as the total amount of water soil can "
          "hold. A rate at which water passes through is permeability, which ERT-4.C.2 "
          "treats as a separate property."),

 dict(q="What does the framework say water holding capacity varies with?",
      choices=["The type of soil", "The season of the year", "The slope of the land",
               "The direction of the prevailing wind",
               "Nothing, since it is the same everywhere"],
      ans=0,
      why="ERT-4.C.1 states that water holding capacity varies with different soil types. "
          "The statement names no other thing it varies with, and it does not hold the "
          "capacity constant."),

 dict(q="What does the framework say water retention contributes to?",
      choices=[
        "Land productivity and the fertility of soils",
        "The speed of the wind blowing above the soil",
        "The number of horizons into which a soil is divided",
        "The distance from the field to the nearest plate boundary",
        "Nothing that the framework names"],
      ans=0,
      why="ERT-4.C.1 states that water retention contributes to land productivity and "
          "fertility of soils, naming both. The rejected options are quantities from other "
          "topics or a denial of the statement."),

 dict(q="Which properties does the framework say the particle size and composition of a "
        "soil horizon can affect?",
      choices=[
        "Porosity, permeability, and fertility",
        "Latitude, longitude, and elevation",
        "Temperature, rainfall, and wind speed",
        "Only porosity and permeability, and not fertility",
        "Only fertility, and neither porosity nor permeability"],
      ans=0,
      why="ERT-4.C.2 states that the particle size and composition of each soil horizon can "
          "affect the porosity, permeability, and fertility of the soil, naming all three. "
          "Two of the rejected options drop one or two of them."),

 dict(q="Which two features of a horizon does the framework say can affect those "
        "properties?",
      choices=[
        "Its particle size and its composition",
        "Its depth and its colour",
        "Its slope and its area",
        "Its temperature and its moisture",
        "Its age and the parent material beneath it"],
      ans=0,
      why="ERT-4.C.2 names the particle size and composition of each soil horizon. Slope "
          "and area belong to the watershed statement ERT-4.F.1, and the remaining pairs "
          "appear nowhere in this topic."),

 dict(q="Which kinds of soil properties does the framework say there are methods to test?",
      choices=[
        "Chemical, physical, and biological properties",
        "Only chemical properties",
        "Only physical properties",
        "Only biological properties",
        "Chemical and physical properties, but not biological ones"],
      ans=0,
      why="ERT-4.C.3 states that there are a variety of methods to test the chemical, "
          "physical, and biological properties of soil, naming all three kinds. Each "
          "rejected option drops at least one of them."),

 dict(q="Which decisions does the framework say those soil tests can aid?",
      choices=[
        "Decisions of a variety of kinds, such as irrigation and fertilizer requirements",
        "Only the choice of which crop to plant",
        "Only the decision of where to build a road",
        "Only the timing of the harvest",
        "The framework names no decision that they aid"],
      ans=0,
      why="ERT-4.C.3 states that the methods can aid in a variety of decisions, such as "
          "irrigation and fertilizer requirements. Those two are the examples the statement "
          "gives, and none of the rejected options appears in it."),

 dict(q="ERT-4.C.3 says the tests aid decisions SUCH AS irrigation and fertilizer "
        "requirements. What does that phrasing establish?",
      choices=[
        "Irrigation and fertilizer requirements are examples of the decisions rather than "
        "the whole list of them",
        "Irrigation and fertilizer requirements are the only decisions the tests can aid",
        "The tests aid no decision about irrigation",
        "The tests aid no decision about fertilizer",
        "The tests aid decisions only after a crop has failed"],
      ans=0,
      why="The statement says a variety of decisions, SUCH AS irrigation and fertilizer "
          "requirements, so the two named are instances of a wider set. Treating them as "
          "the whole set is stronger than the statement and excluding them is weaker."),

 dict(q="What does the framework say a soil texture triangle allows?",
      choices=[
        "The identification and comparison of soil types by their percentages of clay, "
        "silt, and sand",
        "The measurement of the depth of each horizon in a soil",
        "The prediction of the rainfall a region will receive next season",
        "The dating of the parent material beneath a soil",
        "The counting of the organisms living in a soil"],
      ans=0,
      why="ERT-4.C.4 states that a soil texture triangle allows for the identification and "
          "comparison of soil types based on their percentages of clay, silt, and sand. It "
          "offers an identification and a comparison, not a depth, a forecast, an age or a "
          "count."),

 dict(q="Which three components does the framework say those percentages are of?",
      choices=["Clay, silt, and sand", "Clay, silt, and organic matter",
               "Sand, gravel, and clay", "Silt, sand, and water", "Clay, sand, and air"],
      ans=0,
      why="ERT-4.C.4 names the percentages of clay, silt, and sand. Organic material belongs "
          "to ERT-4.B.2 and the horizon categories, and gravel, water and air appear nowhere "
          "in this statement."),

 dict(q="What does the framework say loam consists of?",
      choices=["A blend of clay, silt, and sand", "Clay alone", "Sand alone",
               "Organic material alone", "A blend of sand and gravel with no clay"],
      ans=0,
      why="ERT-4.C.4 states that loam consists of a blend of clay, silt, and sand. Each "
          "rejected option removes at least two of the three components or substitutes one "
          "the statement does not name."),

 dict(q="What does the framework say loam can do?",
      choices=["Support a variety of crops", "Support one crop and no other",
               "Prevent water from entering it at all", "Hold no water whatever",
               "Form without any parent material"],
      ans=0,
      why="ERT-4.C.4 states that loam consists of a blend of clay, silt, and sand that can "
          "support a variety of crops. The statement attributes no other capability to it, "
          "and ERT-4.B.1 requires parent material for any soil to form."),

 dict(q="A grower has a soil analysed before deciding how much fertilizer to spread. Which "
        "framework statement covers that use of an analysis?",
      choices=[
        "There are a variety of methods to test the properties of soil that can aid "
        "decisions such as fertilizer requirements",
        "Water holding capacity is the total amount of water a soil can hold",
        "The particle size and composition of each horizon can affect porosity, "
        "permeability, and fertility",
        "A soil texture triangle allows soil types to be identified and compared",
        "Loam consists of a blend of clay, silt, and sand"],
      ans=0,
      why="ERT-4.C.3 states that the methods for testing soil properties can aid in a "
          "variety of decisions, such as irrigation and fertilizer requirements, which is "
          "the decision being made. The remaining statements define a property, say what "
          "affects other properties, or describe a soil type."),

 dict(q="Which measurement bears most directly on how much a field will need to be "
        "irrigated?",
      choices=[
        "The total amount of water the soil can hold",
        "The number of horizons found in the soil",
        "The distance from the field to the nearest stream",
        "The colour of the parent material beneath the field",
        "The area of the field measured in hectares"],
      ans=0,
      why="ERT-4.C.1 defines water holding capacity as the total amount of water soil can "
          "hold and ERT-4.C.3 names irrigation requirements among the decisions a soil test "
          "can aid, so the capacity is the quantity that bears on the decision. None of the "
          "rejected measurements is connected to irrigation in the framework."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "That every soil type holds the same amount of water",
        "That water holding capacity varies with different soil types",
        "That water retention contributes to land productivity",
        "That the particle size of a horizon can affect its porosity",
        "That loam can support a variety of crops"],
      ans=0,
      why="ERT-4.C.1, ERT-4.C.2 and ERT-4.C.4 supply the four rejected statements in their "
          "own words. ERT-4.C.1 says the capacity VARIES with soil type, which rules out its "
          "being the same in every type."),

 dict(q="ERT-4.C.2 says particle size and composition CAN AFFECT porosity, permeability and "
        "fertility. What does that phrasing establish?",
      choices=[
        "Particle size and composition are able to change those properties, without every "
        "difference in them changing all three",
        "Every difference in particle size changes all three properties by the same amount",
        "Particle size never has any effect on those properties",
        "Only composition has an effect, and particle size has none",
        "Those three properties are fixed and cannot change at all"],
      ans=0,
      why="CAN AFFECT commits the framework to the connection while stopping short of "
          "asserting that every difference works through all three properties at once. "
          "Hardening it is stronger than the statement and denying it is weaker."),

 dict(q="Four soil types were measured for the water each can hold. What does the record "
        "establish?",
      table=_T_WHC,
      choices=[
        "The amount of water a soil can hold differs from one soil type to another",
        "The four soil types all hold the same amount of water",
        "None of the four soil types holds any water",
        "The record reports the yield but not the water each soil can hold",
        "The amount of water a soil can hold is fixed by the crop grown on it"],
      ans=0,
      why="The four capacities are 60, 110, 170 and 190 centimeters of water per meter of "
          "soil, all different and all above zero. ERT-4.C.1 states that water holding "
          "capacity varies with different soil types."),

 dict(q="Which of those four soil types holds the most water?",
      table=_T_WHC,
      choices=["The clay loam", "The coarse sand", "The sandy loam", "The loam",
               "All four hold the same amount"],
      ans=0,
      why="The largest capacity in the record is unique and belongs to one soil type. "
          "ERT-4.C.1 states that water holding capacity varies with different soil types "
          "without saying which type holds most, so the comparison has to be read from the "
          "measurements."),

 dict(q="How much more water can the loam hold than the coarse sand, according to that "
        "record?",
      table=_T_WHC,
      choices=[
        "110 centimeters per meter more", "170 centimeters per meter more",
        "60 centimeters per meter more", "80 centimeters per meter more",
        "The record does not allow that comparison"],
      ans=0,
      why="The two capacities are 170 and 60 centimeters of water per meter of soil, and "
          "170 less 60 is 110. The rejected values are the two capacities themselves and "
          "the difference between a different pair of rows."),

 dict(q="What does the same record establish about the yields grown on those soils?",
      table=_T_WHC,
      choices=[
        "The soils that can hold more water recorded the higher yields",
        "The soils that can hold more water recorded the lower yields",
        "The four soils recorded the same yield",
        "No yield was recorded on any of the four soils",
        "Yield and the water a soil can hold are unrelated in the record"],
      ans=0,
      why="Ordered by the water each soil can hold the yields run 1.8, 3.4, 5.1 and 5.6 "
          "tonnes per hectare, rising at every step. ERT-4.C.1 states that water retention "
          "contributes to land productivity and fertility of soils."),

 dict(q="Four soil samples were analysed for their texture. What do the three composition "
        "columns account for in each sample?",
      table=_T_TEXTURE,
      choices=[
        "The whole of the sample, since the three percentages add to one hundred in every "
        "one",
        "About half of the sample, with the remainder unreported",
        "More than the whole sample, since the three percentages add to more than one "
        "hundred",
        "Only the first sample, since the others are incomplete",
        "Nothing, since the three columns are measured in different units"],
      ans=0,
      why="Adding the clay, silt and sand percentages gives one hundred in each of the four "
          "samples. ERT-4.C.4 states that soil types are identified and compared by their "
          "percentages of clay, silt, and sand, which are shares of the same whole."),

 dict(q="Which of those samples is the blend of clay, silt and sand that the framework calls "
        "loam?",
      table=_T_TEXTURE,
      choices=[
        "Sample 2, in which no one of the three makes up more than half",
        "Sample 1, in which the sand alone makes up more than half",
        "Sample 3, in which the clay alone makes up more than half",
        "Sample 4, in which the silt alone makes up more than half",
        "All four equally, since every sample contains some of all three"],
      ans=0,
      why="In three of the four samples a single component exceeds fifty percent, and in "
          "exactly one none does. ERT-4.C.4 states that loam consists of a BLEND of clay, "
          "silt, and sand, which the sample with no dominant component is and the others "
          "are not."),

 dict(q="Which of those samples holds the largest share of clay?",
      table=_T_TEXTURE,
      choices=["Sample 3", "Sample 1", "Sample 2", "Sample 4",
               "The four samples hold equal shares of clay"],
      ans=0,
      why="The clay percentages are 12, 20, 55 and 8 and the largest is unique. ERT-4.C.4 "
          "makes the percentages of clay, silt, and sand the basis on which soil types are "
          "identified and compared."),

 dict(q="By how many percentage points does the siltiest of those samples exceed the least "
        "silty?",
      table=_T_TEXTURE,
      choices=["By 58 points", "By 78 points", "By 20 points", "By 38 points",
               "The record does not report silt"],
      ans=0,
      why="The silt percentages run from 78 down to 20, and 78 less 20 is 58. The rejected "
          "values are the two endpoints themselves and a difference between a different "
          "pair of samples."),

 dict(q="Three horizons of one soil were measured for particle size and for how fast water "
        "passes through them. What does the record establish?",
      table=_T_POROSITY,
      choices=[
        "Water passes through more slowly where the particles are finer",
        "Water passes through more quickly where the particles are finer",
        "Water passes through all three horizons at the same speed",
        "Water passes through none of the three horizons",
        "Particle size and the speed of the water are unrelated in the record"],
      ans=0,
      why="Ordered by particle diameter the permeabilities run 0.05, 1.6 and 22.0 "
          "centimeters an hour, rising with the size of the particles. ERT-4.C.2 states that "
          "the particle size and composition of each soil horizon can affect the porosity, "
          "permeability, and fertility of the soil, and the record shows one such effect."),

 dict(q="Using those same three horizons, what happens to the pore space as the particles "
        "become finer?",
      table=_T_POROSITY,
      choices=[
        "The share of the volume that is pore space rises",
        "The share of the volume that is pore space falls",
        "The share of the volume that is pore space is unchanged",
        "The record reports permeability but not pore space",
        "The pore space falls to zero in the finest horizon"],
      ans=0,
      why="Ordered by particle diameter the porosities run 52, 44 and 38 percent, so the "
          "finest horizon carries the largest share of pore space. ERT-4.C.2 states that "
          "particle size can affect the porosity of the soil."),

 dict(q="Taken together, what do those two measurements show about porosity and "
        "permeability?",
      table=_T_POROSITY,
      choices=[
        "They are different properties, since the horizon with the most pore space is the "
        "one water passes through most slowly",
        "They are the same property measured in two ways, since they rise and fall together",
        "The horizon with the most pore space is also the one water passes through most "
        "quickly",
        "Neither property varies from horizon to horizon in the record",
        "The record reports pore space but not the speed of the water"],
      ans=0,
      why="The largest porosity and the smallest permeability fall on the same horizon, so "
          "the two columns rank the horizons in opposite orders. ERT-4.C.2 names porosity "
          "and permeability as two of the three properties that particle size and "
          "composition can affect, listing them separately."),

 dict(q="Through which of those horizons does water pass fastest?",
      table=_T_POROSITY,
      choices=[
        "The horizon with the coarsest particles",
        "The horizon with the finest particles",
        "The horizon with the most pore space",
        "Water passes through all three at the same speed",
        "The record does not report how fast water passes through"],
      ans=0,
      why="The largest permeability in the record is unique and belongs to the horizon with "
          "the largest particle diameter, which is also the horizon with the least pore "
          "space. ERT-4.C.2 states that particle size can affect the permeability of the "
          "soil."),

 dict(q="Three fields were tested before the grower decided how to treat them. What does "
        "the record establish?",
      table=_T_TESTS,
      choices=[
        "Where the test found more nitrogen the grower applied less fertilizer, and where "
        "it found more water the grower applied less irrigation",
        "Where the test found more nitrogen the grower applied more fertilizer, and where "
        "it found more water the grower applied more irrigation",
        "The grower applied the same fertilizer and the same irrigation to all three fields",
        "The grower applied fertilizer but no irrigation to any field",
        "The results of the tests and the treatments applied are unrelated in the record"],
      ans=0,
      why="Nitrogen runs 120, 70 and 35 kilograms per hectare while fertilizer runs 20, 70 "
          "and 105, and the water held runs 31, 24 and 16 percent while irrigation runs 10, "
          "40 and 90 millimeters. ERT-4.C.3 states that methods for testing soil properties "
          "can aid in a variety of decisions, such as irrigation and fertilizer "
          "requirements."),

 dict(q="Which single sentence collects what this topic's four statements assert and nothing "
        "further?",
      choices=[
        "Water holding capacity is the total water a soil can hold and varies with soil "
        "type, and water retention contributes to land productivity and fertility; particle "
        "size and composition can affect porosity, permeability and fertility; a variety of "
        "methods test chemical, physical and biological properties and aid decisions such "
        "as irrigation and fertilizer; and soil types are identified by their percentages "
        "of clay, silt and sand, loam being a blend of the three that supports a variety "
        "of crops",
        "Water holding capacity is the same in every soil type; particle size affects "
        "nothing; soil tests measure only chemical properties; and loam is clay alone",
        "Water holding capacity is the total water a soil can hold and varies with soil "
        "type; particle size and composition can affect porosity, permeability and "
        "fertility; a variety of methods test chemical, physical and biological properties; "
        "and loam is a blend of clay, silt and sand that supports only one crop",
        "Water holding capacity is the rate at which water passes through a soil; water "
        "retention contributes to land productivity and fertility; soil tests aid decisions "
        "such as irrigation and fertilizer; and loam is a blend of clay, silt and sand",
        "Water holding capacity is the total water a soil can hold and varies with soil "
        "type, and water retention lowers land productivity; particle size and composition "
        "can affect porosity, permeability and fertility; soil tests aid decisions such as "
        "irrigation and fertilizer; and loam is a blend of clay, silt and sand"],
      ans=0,
      why="ERT-4.C.1 supplies the definition, the variation with soil type and the "
          "contribution to productivity and fertility, ERT-4.C.2 the three properties "
          "particle size and composition can affect, ERT-4.C.3 the three kinds of test and "
          "the two example decisions, and ERT-4.C.4 the basis of identification and the "
          "description of loam. Each rejected summary redefines the capacity, drops a kind "
          "of test, reverses the contribution of water retention, or narrows what loam can "
          "support."),
]
