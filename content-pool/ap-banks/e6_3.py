# AP ENVIRONMENTAL SCIENCE 6.3 Fuel Types and Uses
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objective ENG-3.C, identify types of fuels and their uses.
# Suggested skill 1.A, describe environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.C.1  Wood is commonly used as fuel in the forms of firewood and charcoal. It is
#              often used in developing countries because it is easily accessible.
#   ENG-3.C.2  Peat is partially decomposed organic material that can be burned for fuel.
#   ENG-3.C.3  Three types of coal used for fuel are lignite, bituminous, and anthracite.
#              Heat, pressure, and depth of burial contribute to the development of
#              various coal types and their qualities.
#   ENG-3.C.4  Natural gas, the cleanest of the fossil fuels, is mostly methane.
#   ENG-3.C.5  Crude oil can be recovered from tar sands, which are a combination of clay,
#              sand, water, and bitumen.
#   ENG-3.C.6  Fossil fuels can be made into specific fuel types for specialized uses
#              (e.g., in motor vehicles).
#   ENG-3.C.7  Cogeneration occurs when a fuel source is used to generate both useful heat
#              and electricity.
#
# WHAT THE FRAMEWORK DOES NOT SAY, and is therefore never keyed here. ENG-3.C.3 NAMES three
# coals and names three things that contribute to their development and qualities. It does
# NOT rank lignite, bituminous and anthracite by carbon content, by energy released or by
# age, so no item keys such a ranking from memory. One item keys the absence itself. Where
# a coal ranking is needed for arithmetic the numbers are printed in the item's own table
# and the conclusion is drawn from that table, with ENG-3.C.3 supplying only the licence to
# relate depth of burial to quality.
#
# PEAT IS NOT A COAL HERE. ENG-3.C.2 gives peat its own statement and calls it partially
# decomposed organic material; ENG-3.C.3's three coals do not include it. Two items turn on
# that separation.
#
# CLEANEST IS THE FRAMEWORK'S OWN WORD for natural gas (ENG-3.C.4) and is used of no other
# fuel in this topic. One data item pairs the verdict with the framework's attribution, so
# its anchor carries both clauses -- the swapped distractor keeps the correct data reading
# and attaches it to the wrong statement.
#
# BOUNDARY. How fossil fuels are burned to make electricity is ENG-3.E in topic 6.5, and
# fracking is ENG-3.F.1 there; neither is keyed here. Whether a fuel is renewable is
# ENG-3.A in topic 6.1.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_3.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.3", "Fuel Types and Uses", 6)

_T_COAL = dict(
    headers=["Coal sample",
             "Depth at which the seam was buried (meters)",
             "Energy released by one kilogram (energy units)"],
    rows=[["Sample 1", "300", "16"],
          ["Sample 2", "900", "24"],
          ["Sample 3", "2,700", "32"]])

_T_CLEAN = dict(
    headers=["Fossil fuel burned",
             "Sulfur dioxide released for each unit of energy (grams)",
             "Particulates released for each unit of energy (grams)"],
    rows=[["Coal", "1,200", "60"],
          ["Crude oil products", "500", "18"],
          ["Natural gas", "2", "0.2"]])

_T_COGEN = dict(
    headers=["Plant studied",
             "Fuel energy put in (energy units)",
             "Electricity produced (energy units)",
             "Useful heat delivered to buildings (energy units)"],
    rows=[["Plant 1", "100", "35", "0"],
          ["Plant 2", "100", "30", "45"]])

_T_TAR = dict(
    headers=["Component of the tar sand",
             "Share of the deposit by mass (percent)"],
    rows=[["Clay", "20"],
          ["Sand", "55"],
          ["Water", "5"],
          ["Bitumen", "20"]])

_T_WOOD = dict(
    headers=["Group of countries surveyed",
             "Households whose main fuel is firewood or charcoal (percent)",
             "Households connected to an electricity supply (percent)"],
    rows=[["Developed countries", "3", "99"],
          ["Developing countries", "61", "54"]])

QUESTIONS = [

 dict(q="In which two forms does the framework say wood is commonly used as a fuel?",
      choices=[
        "Firewood and charcoal",
        "Peat and lignite",
        "Bitumen and tar",
        "Methane and ethanol",
        "Sawdust pellets and paper"],
      ans=0,
      why="ENG-3.C.1 states that WOOD IS COMMONLY USED AS FUEL IN THE FORMS OF FIREWOOD AND "
          "CHARCOAL. Peat and the three coals have their own statements, bitumen belongs to the "
          "description of tar sands, and methane is what natural gas is mostly made of."),

 dict(q="The framework gives one reason wood is often used as a fuel in developing countries. "
        "What is that reason?",
      choices=[
        "Because it is easily accessible",
        "Because one kilogram of it releases more energy than one kilogram of coal",
        "Because burning it releases no carbon dioxide",
        "Because governments there require households to burn it",
        "Because the framework calls it the cleanest of the fuels named in this topic"],
      ans=0,
      why="ENG-3.C.1 states that wood IS OFTEN USED IN DEVELOPING COUNTRIES BECAUSE IT IS EASILY "
          "ACCESSIBLE. The framework makes no energy comparison for wood, calls natural gas rather "
          "than wood the cleanest of the fossil fuels, and names no requirement to burn it."),

 dict(q="How does the framework describe peat?",
      choices=[
        "Partially decomposed organic material that can be burned for fuel",
        "Fully decomposed organic material that can no longer be burned",
        "One of the three types of coal used for fuel",
        "A combination of clay, sand, water and bitumen",
        "A gas that is mostly methane"],
      ans=0,
      why="ENG-3.C.2 states that PEAT IS PARTIALLY DECOMPOSED ORGANIC MATERIAL THAT CAN BE BURNED "
          "FOR FUEL. The three coals of ENG-3.C.3 do not include peat, the combination described "
          "is a tar sand, and the gas described is natural gas."),

 dict(q="Which three types of coal does the framework name as fuels?",
      choices=[
        "Lignite, bituminous, and anthracite",
        "Lignite, bituminous, and peat",
        "Peat, charcoal, and anthracite",
        "Bitumen, lignite, and methane",
        "Charcoal, coke, and anthracite"],
      ans=0,
      why="ENG-3.C.3 states that THREE TYPES OF COAL USED FOR FUEL ARE LIGNITE, BITUMINOUS, AND "
          "ANTHRACITE. Peat, charcoal, bitumen and methane each belong to a different statement "
          "in this topic, and coke appears in none of them."),

 dict(q="Which three things does the framework say contribute to the development of the various "
        "coal types and their qualities?",
      choices=[
        "Heat, pressure, and depth of burial",
        "Heat, rainfall, and the age of the forest above",
        "Pressure, salinity, and the depth of ocean water above",
        "Depth of burial, wind speed, and soil type",
        "Heat, pressure, and the amount of sulfur present"],
      ans=0,
      why="ENG-3.C.3 states that HEAT, PRESSURE, AND DEPTH OF BURIAL CONTRIBUTE to the development "
          "of various coal types and their qualities. Rainfall, salinity, wind, soil and sulfur "
          "content appear nowhere in the statement."),

 dict(q="Which fossil fuel does the framework call the cleanest?",
      choices=[
        "Natural gas",
        "Anthracite coal",
        "Crude oil recovered from tar sands",
        "Lignite coal",
        "Peat cut from a bog"],
      ans=0,
      why="ENG-3.C.4 opens by calling NATURAL GAS THE CLEANEST OF THE FOSSIL FUELS. The framework "
          "applies that word to no other fuel in this topic, and peat is not even treated as one "
          "of the fossil fuels there."),

 dict(q="What is natural gas mostly made of, according to the framework?",
      choices=[
        "Methane",
        "Bitumen",
        "Carbon monoxide",
        "Ethanol",
        "Hydrogen sulfide"],
      ans=0,
      why="ENG-3.C.4 states that natural gas IS MOSTLY METHANE. Bitumen belongs to the description "
          "of tar sands, and none of the other three is named as a constituent of natural gas "
          "anywhere in this topic."),

 dict(q="Besides a conventional well, from what does the framework say crude oil can be "
        "recovered?",
      choices=[
        "Tar sands",
        "Peat bogs",
        "Anthracite seams",
        "Charcoal kilns",
        "Beds of methane hydrate"],
      ans=0,
      why="ENG-3.C.5 states that CRUDE OIL CAN BE RECOVERED FROM TAR SANDS. Peat, anthracite and "
          "charcoal are each named in this topic as fuels in their own right rather than as "
          "sources of crude oil, and methane hydrate is named nowhere in it."),

 dict(q="The framework describes a tar sand as a combination of which materials?",
      choices=[
        "Clay, sand, water, and bitumen",
        "Clay, sand, water, and methane",
        "Sand, water, bitumen, and sulfur",
        "Clay, peat, water, and bitumen",
        "Sand, gravel, water, and charcoal"],
      ans=0,
      why="ENG-3.C.5 states that tar sands ARE A COMBINATION OF CLAY, SAND, WATER, AND BITUMEN. "
          "Each rejected list swaps one of those four for a material the statement does not "
          "name."),

 dict(q="What does the framework say fossil fuels can be made into?",
      choices=[
        "Specific fuel types for specialized uses, such as fuels for motor vehicles",
        "Renewable fuels that are replenished at or near the rate they are consumed",
        "A single general fuel that serves every use equally well",
        "Fuels that release no carbon dioxide when they are burned",
        "Materials that can no longer be burned once they have been processed"],
      ans=0,
      why="ENG-3.C.6 states that FOSSIL FUELS CAN BE MADE INTO SPECIFIC FUEL TYPES FOR SPECIALIZED "
          "USES, and gives motor vehicles as its own example. Processing a fossil fuel does not "
          "make it renewable, and the statement claims nothing about emissions."),

 dict(q="What does the framework say cogeneration is?",
      choices=[
        "One fuel source used to generate both useful heat and electricity",
        "One fuel source used to generate electricity alone, at a higher efficiency",
        "Two different fuels burned together in the same furnace",
        "Electricity generated at two separate plants and combined on one grid",
        "Heat taken from the interior of the Earth and used to warm buildings"],
      ans=0,
      why="ENG-3.C.7 states that COGENERATION OCCURS WHEN A FUEL SOURCE IS USED TO GENERATE BOTH "
          "USEFUL HEAT AND ELECTRICITY. The number of fuels and the number of plants are not what "
          "the statement turns on, and heat from the Earth's interior is geothermal energy."),

 dict(q="A power station burns gas, sends out electricity, and vents the leftover heat to the "
        "air. Does the framework's term for combined generation apply to it?",
      choices=[
        "No, because only one of the two useful outputs described is produced",
        "Yes, because a single fuel source is used at the station",
        "Yes, because heat is certainly produced at the station",
        "No, because the station burns gas rather than coal",
        "The term applies to any station that sends out electricity"],
      ans=0,
      why="ENG-3.C.7 requires BOTH useful heat AND electricity from the one fuel source. Heat that "
          "is vented is not delivered as useful heat, so one of the two outputs is missing. "
          "Nothing in the statement turns on which fuel is burned."),

 dict(q="How does the framework place peat in relation to the three coals?",
      choices=[
        "Peat is partially decomposed organic material, and the three coals named are lignite, "
        "bituminous and anthracite",
        "Peat is one of the three coals named, alongside lignite and bituminous",
        "Anthracite is partially decomposed organic material and peat is one of the coals",
        "The framework names four coals, of which peat is the least decomposed",
        "The framework treats peat and charcoal as the same material"],
      ans=0,
      why="ENG-3.C.2 gives peat its own statement as partially decomposed organic material, while "
          "ENG-3.C.3 names lignite, bituminous and anthracite as the three types of coal used for "
          "fuel. Charcoal belongs to ENG-3.C.1, which is about wood."),

 dict(q="Which claim about the three named coals does the framework NOT make?",
      choices=[
        "It ranks them by the energy each releases when it is burned",
        "It names them as three types of coal used for fuel",
        "It says heat contributes to their development",
        "It says pressure contributes to their development",
        "It says depth of burial contributes to their qualities"],
      ans=0,
      why="ENG-3.C.3 names the three coals and names heat, pressure and depth of burial as "
          "contributors to their development and qualities. It sets no order among the three by "
          "energy content, so a ranking would have to come from outside the framework."),

 dict(q="A household in a developing country cuts nearby wood for its stove and turns the rest "
        "into charcoal. Which of the framework's statements does the case illustrate?",
      choices=[
        "That wood is commonly used as firewood and charcoal, and often in developing countries "
        "because it is easily accessible",
        "That fossil fuels can be made into specific fuel types for specialized uses",
        "That cogeneration produces both useful heat and electricity from one fuel source",
        "That natural gas is the cleanest of the fossil fuels and is mostly methane",
        "That crude oil can be recovered from tar sands"],
      ans=0,
      why="ENG-3.C.1 covers both halves of the case: the two forms wood is used in, and the reason "
          "it is often the fuel in developing countries. Each rejected option quotes a different "
          "statement in the topic that the case does not touch."),

 dict(q="A refinery takes crude oil and produces a fuel blended for motor vehicle engines. Which "
        "statement does that illustrate?",
      choices=[
        "That fossil fuels can be made into specific fuel types for specialized uses",
        "That crude oil can be recovered from tar sands",
        "That natural gas is mostly methane",
        "That cogeneration generates both useful heat and electricity",
        "That wood is commonly used as a fuel in the forms of firewood and charcoal"],
      ans=0,
      why="ENG-3.C.6 states that fossil fuels can be made into specific fuel types for specialized "
          "uses and offers motor vehicles as the example. Recovery from tar sands is where crude "
          "oil comes from, not what it is made into."),

 dict(q="A factory burns one fuel, drives a generator with the steam, and then pipes that steam "
        "into its buildings for heating. What does the framework call this?",
      choices=[
        "Cogeneration",
        "Refining crude oil into specialized fuels",
        "Making charcoal from wood",
        "Recovering crude oil from tar sands",
        "Burying organic material so that it becomes coal"],
      ans=0,
      why="ENG-3.C.7 defines cogeneration as one fuel source used to generate both useful heat and "
          "electricity, which is exactly what the factory does with its steam. The rejected terms "
          "belong to other statements in this topic and none of them describes the case."),

 dict(q="Which comparison would most directly report the framework's claim about natural gas?",
      choices=[
        "The pollutants released for each unit of energy by natural gas set beside those "
        "released by the other fossil fuels",
        "The price of natural gas set beside the price of coal",
        "The depth at which natural gas is found set beside the depth of a coal seam",
        "The number of countries holding natural gas set beside the number holding coal",
        "The share of a barrel of crude oil that is made into motor vehicle fuel"],
      ans=0,
      why="ENG-3.C.4 calls natural gas the cleanest of the fossil fuels, which is a comparison "
          "about what burning releases and can only be reported by measuring that. Price, depth "
          "and the number of holders are outside the statement."),

 dict(q="Three coal samples were logged with the depth at which their seam was buried and the "
        "energy one kilogram of each releases. Which conclusion do the values support?",
      table=_T_COAL,
      choices=[
        "Coal from the more deeply buried seams released more energy for each kilogram, which "
        "is consistent with depth of burial contributing to coal quality",
        "Coal from the more deeply buried seams released less energy for each kilogram",
        "Depth of burial and energy released are unrelated across the three samples",
        "All three samples released the same energy for each kilogram",
        "The record shows that peat releases more energy than any of the three samples"],
      ans=0,
      why="The seams were buried at 300, 900 and 2,700 meters and one kilogram released 16, 24 and "
          "32 energy units, rising together. ENG-3.C.3 names DEPTH OF BURIAL among the things "
          "that contribute to coal types and their qualities, and the record carries no peat."),

 dict(q="Using the same three samples, how much more energy does one kilogram from the deepest "
        "seam release than one kilogram from the shallowest?",
      table=_T_COAL,
      choices=[
        "16 energy units",
        "32 energy units",
        "48 energy units",
        "24 energy units",
        "72 energy units"],
      ans=0,
      why="Subtracting the two tabulated values gives 32 minus 16, which is 16 energy units. The "
          "rejected values quote the deepest sample alone, add the deepest and the shallowest, "
          "quote the middle sample, or add all three."),

 dict(q="Using the same three samples, how many times as deep was the deepest seam buried as the "
        "shallowest?",
      table=_T_COAL,
      choices=[
        "Nine times as deep",
        "Three times as deep",
        "Two times as deep",
        "Twenty-seven times as deep",
        "The two seams were buried at the same depth"],
      ans=0,
      why="Dividing the two tabulated depths gives 2,700 divided by 300, which is 9. The rejected "
          "values come from the step between adjacent samples, from the ratio of the energy "
          "column, or from denying that the depths differ."),

 dict(q="Three fossil fuels were measured for what they release for each unit of energy. Which "
        "fuel do the values pick out as the cleanest, and how does that stand with the framework?",
      table=_T_CLEAN,
      choices=[
        "Natural gas, and it agrees with the framework, which calls natural gas the cleanest of "
        "the fossil fuels",
        "Coal, and it agrees with the framework, which calls natural gas the cleanest of the "
        "fossil fuels",
        "Natural gas, although the framework calls coal the cleanest of the fossil fuels",
        "Crude oil products, which the framework calls the cleanest of the fossil fuels",
        "No fuel, because the three release the same amounts for each unit of energy"],
      ans=0,
      why="Natural gas releases 2 grams of sulfur dioxide and 0.2 grams of particulates for each "
          "unit of energy, the least on both counts, against 1,200 and 60 for coal. ENG-3.C.4 "
          "calls NATURAL GAS THE CLEANEST OF THE FOSSIL FUELS, so the reading and the framework "
          "agree."),

 dict(q="Using the same three fuels, how many times as much sulfur dioxide does coal release for "
        "each unit of energy as natural gas does?",
      table=_T_CLEAN,
      choices=[
        "600 times as much",
        "60 times as much",
        "1,200 times as much",
        "300 times as much",
        "6 times as much"],
      ans=0,
      why="Dividing the two tabulated values gives 1,200 divided by 2, which is 600. The rejected "
          "values quote the particulate column, quote the coal figure alone, halve the answer, or "
          "drop two powers of ten."),

 dict(q="Using the same three fuels, how much more particulate matter does coal release for each "
        "unit of energy than crude oil products do?",
      table=_T_CLEAN,
      choices=[
        "42 grams",
        "60 grams",
        "78 grams",
        "18 grams",
        "Coal releases less than crude oil products do"],
      ans=0,
      why="Subtracting the two tabulated values gives 60 minus 18, which is 42 grams. The rejected "
          "values quote one of the two rows alone, add them, or invert the comparison the table "
          "actually shows."),

 dict(q="Two plants burning the same fuel were compared. Which plant meets the framework's "
        "description of cogeneration, and on what ground?",
      table=_T_COGEN,
      choices=[
        "The second plant, because one fuel source there yields both useful heat and electricity",
        "The first plant, because one fuel source there yields both useful heat and electricity",
        "The second plant, because it produces less electricity than the first does",
        "Both plants, because each burns a fuel and sends out electricity",
        "Neither plant, because the framework's term requires two different fuels"],
      ans=0,
      why="The second plant delivers 30 energy units of electricity and 45 of useful heat from the "
          "same 100 units of fuel, while the first delivers 35 of electricity and no useful heat. "
          "ENG-3.C.7 requires BOTH outputs from one fuel source, and it sets no condition about "
          "how much electricity is produced or how many fuels are burned."),

 dict(q="Using the same two plants, what share of the fuel energy put into the cogeneration plant "
        "leaves it as either useful heat or electricity?",
      table=_T_COGEN,
      choices=[
        "75 percent",
        "30 percent",
        "45 percent",
        "35 percent",
        "100 percent"],
      ans=0,
      why="Adding the two useful outputs gives 30 plus 45, which is 75 of the 100 energy units put "
          "in. The rejected values quote one output alone, quote the other plant's electricity, or "
          "assume nothing at all is lost."),

 dict(q="Using the same two plants, how much larger is that share than the share of its fuel "
        "energy the electricity-only plant turns into electricity?",
      table=_T_COGEN,
      choices=[
        "40 percentage points",
        "75 percentage points",
        "110 percentage points",
        "30 percentage points",
        "45 percentage points"],
      ans=0,
      why="The cogeneration plant delivers 75 of its 100 energy units usefully and the other plant "
          "delivers 35, so the gap is 40 percentage points. The rejected values quote the "
          "cogeneration plant alone, add the two shares, or quote just one of that plant's two "
          "useful outputs."),

 dict(q="A tar sand deposit was broken down by mass. How much of the deposit must be handled to "
        "obtain one tonne of bitumen?",
      table=_T_TAR,
      choices=[
        "Five tonnes",
        "Twenty tonnes",
        "Two tonnes",
        "One tonne",
        "Eighty tonnes"],
      ans=0,
      why="Bitumen is 20 percent of the deposit by mass, or one part in five, so five tonnes of "
          "the deposit hold one tonne of bitumen. ENG-3.C.5 lists bitumen as one of the four "
          "materials a tar sand combines, the other three being clay, sand and water."),

 dict(q="Two groups of countries were surveyed for the share of households whose main fuel is "
        "firewood or charcoal. Which of the framework's statements do the values illustrate?",
      table=_T_WOOD,
      choices=[
        "That wood is often used as a fuel in developing countries because it is easily "
        "accessible",
        "That wood is often used as a fuel in developed countries because it is easily "
        "accessible",
        "That natural gas is the cleanest of the fossil fuels",
        "That fossil fuels can be made into specific fuel types for specialized uses",
        "That cogeneration generates both useful heat and electricity from one fuel source"],
      ans=0,
      why="Firewood or charcoal is the main fuel for 61 percent of households in the developing "
          "group against 3 percent in the developed group. ENG-3.C.1 states that wood is often "
          "used in developing countries because it is easily accessible."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Wood is burned as firewood and charcoal and is common in developing countries because "
        "it is easily accessible; peat is partially decomposed organic material; the three "
        "coals are lignite, bituminous and anthracite; natural gas is the cleanest fossil fuel "
        "and is mostly methane; crude oil can come from tar sands; fossil fuels can be made "
        "into specialized fuels; and cogeneration yields both useful heat and electricity.",
        "Peat is one of the three coals, natural gas is the dirtiest of the fossil fuels, and "
        "cogeneration means burning two fuels at once.",
        "Wood is used mainly in developed countries, crude oil cannot be recovered from tar "
        "sands, and coal quality depends only on the age of the seam.",
        "The framework ranks lignite, bituminous and anthracite by the energy each releases and "
        "gives a figure for each.",
        "Every fuel named in this topic is renewable, since each can be replenished at or near "
        "the rate at which it is consumed."],
      ans=0,
      why="The keyed summary carries ENG-3.C.1 through C.7 in the framework's own terms and adds "
          "nothing. Each rejected summary misplaces peat, inverts the claim about natural gas, "
          "moves wood to the wrong group of countries, invents a ranking the framework does not "
          "give, or imports the renewable definition from another topic."),
]
