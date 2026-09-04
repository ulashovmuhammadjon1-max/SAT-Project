# AP ENVIRONMENTAL SCIENCE 6.8 Solar Energy
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.J, describe the use of solar energy in power generation; and
# ENG-3.K, describe the effects of the use of solar energy in power generation on the
# environment.
# Suggested skill 5.C, explain patterns and trends in data to draw conclusions -- which is
# why thirteen of the thirty items here carry a table and ask for a trend or a comparison.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.J.1  Photovoltaic solar cells capture light energy from the sun and transform it
#              directly into electrical energy. Their use is limited by the availability of
#              sunlight.
#   ENG-3.J.2  Active solar energy systems use solar energy to heat a liquid through
#              mechanical and electric equipment to collect and store the energy captured
#              from the sun.
#   ENG-3.J.3  Passive solar energy systems absorb heat directly from the sun without the
#              use of mechanical and electric equipment, and energy cannot be collected or
#              stored.
#   ENG-3.K.1  Solar energy systems have low environmental impact and produce clean energy,
#              but they can be expensive. Large solar energy farms may negatively impact
#              desert ecosystems.
#
# ACTIVE AND PASSIVE ARE THE SWAP THIS TOPIC INVITES, and it is the sharpest one in the
# unit because the two statements are built from the same three parts with the values
# reversed: mechanical and electric equipment yes or no, a liquid heated or heat absorbed
# directly, energy collected and stored or not collected and not stored. Every anchor that
# names one system therefore carries the property as well as the name, and the items that
# compare them carry both clauses. An anchor reading only "the active system" would match
# the distractor that attaches the passive properties to it.
#
# THREE SEPARATE THINGS ARE CALLED DIRECT IN THIS TOPIC and they are not the same. A
# photovoltaic cell transforms light DIRECTLY INTO ELECTRICAL ENERGY (ENG-3.J.1); a passive
# system absorbs heat DIRECTLY FROM THE SUN (ENG-3.J.3). Nothing here keys one as though it
# were the other, and the item comparing photovoltaic cells with active systems names what
# each produces rather than leaning on the word.
#
# TWO HEDGES, BOTH KEYED. ENG-3.K.1 says solar systems CAN BE expensive and that large
# farms MAY negatively impact desert ecosystems. Neither is stated as certain, and the
# desert clause is restricted to LARGE farms and to DESERT ecosystems. Two items key the
# hedges and no key anywhere states either claim without them.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_8.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.8", "Solar Energy", 6)

_T_SUN = dict(
    headers=["Site with the same array installed",
             "Hours of sunlight in an average day",
             "Electricity the array delivers each day (energy units)"],
    rows=[["Site 1", "3", "150"],
          ["Site 2", "5", "250"],
          ["Site 3", "8", "400"],
          ["Site 4", "10", "500"]])

_T_SYSTEM = dict(
    headers=["Solar system installed on a house",
             "Pieces of mechanical and electric equipment fitted",
             "Heated liquid held for use after dark (litres)",
             "Heat delivered to the house on a sunny day (energy units)"],
    rows=[["System 1", "6", "400", "500"],
          ["System 2", "0", "0", "300"]])

_T_COST = dict(
    headers=["Way of generating electricity",
             "Cost to build for each unit of capacity (currency units)",
             "Air pollutants released for each unit of electricity (grams)"],
    rows=[["Solar array", "2,700", "0"],
          ["Gas plant", "900", "310"]])

_T_DESERT = dict(
    headers=["Desert plot surveyed",
             "Area under solar panels (hectares)",
             "Native plant species recorded",
             "Reptile species recorded"],
    rows=[["Plot 1, with no farm", "0", "34", "11"],
          ["Plot 2, with a small farm", "120", "27", "8"],
          ["Plot 3, with a large farm", "900", "15", "4"]])

QUESTIONS = [

 dict(q="What does the framework say photovoltaic solar cells do?",
      choices=[
        "They capture light energy from the sun and transform it directly into electrical "
        "energy",
        "They capture light energy from the sun and use it to heat a liquid",
        "They absorb heat directly from the sun without any equipment",
        "They store heat in a tank for use after dark",
        "They burn a fuel to raise steam for a turbine"],
      ans=0,
      why="ENG-3.J.1 states that PHOTOVOLTAIC SOLAR CELLS CAPTURE LIGHT ENERGY FROM THE SUN AND "
          "TRANSFORM IT DIRECTLY INTO ELECTRICAL ENERGY. Heating a liquid is what an active system "
          "does in ENG-3.J.2, and absorbing heat without equipment is a passive system in "
          "ENG-3.J.3."),

 dict(q="What does the framework say limits the use of photovoltaic solar cells?",
      choices=[
        "The availability of sunlight",
        "The availability of water for cooling",
        "The availability of mechanical and electric equipment",
        "The availability of desert land",
        "The framework names no limit on their use"],
      ans=0,
      why="ENG-3.J.1 states that THEIR USE IS LIMITED BY THE AVAILABILITY OF SUNLIGHT. Water, "
          "equipment and land appear nowhere in that clause, and the limit is stated rather than "
          "withheld."),

 dict(q="What does the framework say an active solar energy system uses solar energy to do?",
      choices=[
        "Heat a liquid, through mechanical and electric equipment, so the energy can be "
        "collected and stored",
        "Heat a liquid, without any mechanical or electric equipment, so the energy warms the "
        "house at once",
        "Transform light directly into electrical energy",
        "Absorb heat directly from the sun, with no liquid involved",
        "Drive a turbine that spins a generator"],
      ans=0,
      why="ENG-3.J.2 states that ACTIVE SOLAR ENERGY SYSTEMS USE SOLAR ENERGY TO HEAT A LIQUID "
          "THROUGH MECHANICAL AND ELECTRIC EQUIPMENT TO COLLECT AND STORE THE ENERGY CAPTURED FROM "
          "THE SUN. Doing it without equipment, and without collection or storage, is the passive "
          "system of ENG-3.J.3."),

 dict(q="What does the framework say a passive solar energy system does?",
      choices=[
        "It absorbs heat directly from the sun without the use of mechanical and electric "
        "equipment",
        "It absorbs heat directly from the sun using mechanical and electric equipment",
        "It transforms light directly into electrical energy",
        "It heats a liquid and pumps it into a storage tank",
        "It concentrates sunlight to raise steam for a turbine"],
      ans=0,
      why="ENG-3.J.3 states that PASSIVE SOLAR ENERGY SYSTEMS ABSORB HEAT DIRECTLY FROM THE SUN "
          "WITHOUT THE USE OF MECHANICAL AND ELECTRIC EQUIPMENT. Equipment, a pumped liquid and "
          "electrical output all belong to the other two statements in this topic."),

 dict(q="What does the framework say a passive solar energy system cannot do?",
      choices=[
        "Collect or store the energy it absorbs",
        "Absorb any heat from the sun at all",
        "Warm a building on a sunny day",
        "Work without a pump and a controller",
        "Reduce the fuel a household would otherwise burn"],
      ans=0,
      why="ENG-3.J.3 ends by stating that ENERGY CANNOT BE COLLECTED OR STORED in a passive "
          "system. The same statement says it does absorb heat directly from the sun, so the "
          "options denying that it works at all contradict it."),

 dict(q="Which comparison of the two kinds of solar heating system does the framework draw?",
      choices=[
        "The active system uses mechanical and electric equipment and can collect and store the "
        "energy; the passive system uses none and cannot",
        "The passive system uses mechanical and electric equipment and can collect and store the "
        "energy; the active system uses none and cannot",
        "Both systems use mechanical and electric equipment, and only the passive one can store "
        "the energy",
        "Neither system uses mechanical and electric equipment, and both can store the energy",
        "The framework draws no comparison between the two kinds of system"],
      ans=0,
      why="ENG-3.J.2 gives the active system equipment and the ability to collect and store, while "
          "ENG-3.J.3 gives the passive system neither. The two statements are built from the same "
          "properties with the values reversed, so the whole difference has to be stated to state "
          "it correctly."),

 dict(q="A house is fitted with a system that has no pump, no controller and no tank, and its "
        "south wall warms the rooms on a sunny day. Which kind of system is it, and why?",
      choices=[
        "Passive, because it absorbs heat directly from the sun without mechanical and electric "
        "equipment",
        "Active, because it absorbs heat directly from the sun without mechanical and electric "
        "equipment",
        "Passive, because it uses mechanical and electric equipment to collect and store the "
        "energy",
        "Photovoltaic, because it transforms light directly into electrical energy",
        "Neither, because the framework describes no system without equipment"],
      ans=0,
      why="ENG-3.J.3 describes exactly this arrangement: heat absorbed directly from the sun with "
          "no mechanical or electric equipment, and no collection or storage. ENG-3.J.2 reserves "
          "the equipment and the storage for an active system."),

 dict(q="How do photovoltaic cells differ from active solar energy systems in what they produce?",
      choices=[
        "The cells produce electrical energy, while the active system heats a liquid",
        "The cells heat a liquid, while the active system produces electrical energy",
        "Both produce electrical energy, and only the active system stores it",
        "Both heat a liquid, and only the cells store the energy",
        "The framework does not say what either of them produces"],
      ans=0,
      why="ENG-3.J.1 has photovoltaic cells transforming light DIRECTLY INTO ELECTRICAL ENERGY, "
          "while ENG-3.J.2 has an active system heating A LIQUID so the energy can be collected "
          "and stored. Each statement names its own output and they are different."),

 dict(q="What does the framework say about the environmental impact of solar energy systems?",
      choices=[
        "They have low environmental impact and produce clean energy",
        "They have high environmental impact but produce clean energy",
        "They have low environmental impact but produce dirty energy",
        "They have no impact of any kind on any ecosystem",
        "The framework makes no claim about their environmental impact"],
      ans=0,
      why="ENG-3.K.1 opens by stating that SOLAR ENERGY SYSTEMS HAVE LOW ENVIRONMENTAL IMPACT AND "
          "PRODUCE CLEAN ENERGY. The same statement goes on to name an impact on desert "
          "ecosystems, so low is not the same as none."),

 dict(q="What reservation does the framework attach to solar energy systems in that same "
        "statement?",
      choices=[
        "That they can be expensive",
        "That they release hazardous solid waste",
        "That they release volatile organic compounds",
        "That they cannot be built in sunny regions",
        "That they raise the temperature of nearby rivers"],
      ans=0,
      why="ENG-3.K.1 states that solar energy systems CAN BE EXPENSIVE. Hazardous solid waste "
          "belongs to nuclear power in topic 6.6, volatile organic compounds to fracking in 6.5, "
          "and thermal pollution to nuclear power as well."),

 dict(q="What does the framework say about large solar energy farms in particular?",
      choices=[
        "They may negatively impact desert ecosystems",
        "They will certainly destroy any desert ecosystem they are built in",
        "They improve desert ecosystems by providing shade",
        "They may negatively impact wetland ecosystems",
        "The framework says nothing about large solar energy farms"],
      ans=0,
      why="ENG-3.K.1 ends by stating that LARGE SOLAR ENERGY FARMS MAY NEGATIVELY IMPACT DESERT "
          "ECOSYSTEMS. The claim is hedged with may, it is about desert ecosystems rather than "
          "wetlands, and it is made rather than withheld."),

 dict(q="What do the words CAN BE and MAY establish in the framework's statement about the "
        "effects of solar energy?",
      choices=[
        "That the high cost and the harm to desert ecosystems are possible rather than certain",
        "That the high cost and the harm to desert ecosystems are certain wherever solar is used",
        "That neither the cost nor the harm has ever been observed",
        "That the statement applies only to photovoltaic cells and not to other systems",
        "That the framework is uncertain whether solar energy is clean"],
      ans=0,
      why="ENG-3.K.1 says solar systems CAN BE expensive and that large farms MAY negatively "
          "impact desert ecosystems, which asserts possibility in both cases. Neither hedge "
          "touches the claim that the energy produced is clean, which the same sentence states "
          "flatly."),

 dict(q="A student writes that a passive solar system keeps the day's heat in a tank for the "
        "evening. What correction does the framework require?",
      choices=[
        "In a passive system the energy cannot be collected or stored; it is an active system "
        "that collects and stores",
        "In a passive system the energy is collected and stored, so the student is correct",
        "In an active system the energy cannot be collected or stored; it is a passive system "
        "that collects and stores",
        "Neither kind of system can collect or store energy",
        "Both kinds of system collect and store energy, so the distinction does not matter"],
      ans=0,
      why="ENG-3.J.3 states that energy CANNOT BE COLLECTED OR STORED in a passive system, while "
          "ENG-3.J.2 gives collection and storage to the active system. One rejected correction is "
          "the exact swap of those two, which is why both halves have to be stated."),

 dict(q="A second student writes that photovoltaic cells work by heating a liquid. What "
        "correction does the framework require?",
      choices=[
        "Photovoltaic cells transform light directly into electrical energy; heating a liquid is "
        "what an active system does",
        "Photovoltaic cells heat a liquid, so the student is correct",
        "Photovoltaic cells absorb heat directly from the sun, which is what a passive system "
        "does",
        "Photovoltaic cells drive a turbine that spins a generator",
        "The framework does not describe how photovoltaic cells work"],
      ans=0,
      why="ENG-3.J.1 has the cells transforming light directly into electrical energy, and "
          "ENG-3.J.2 gives the heated liquid to an active system. Absorbing heat directly is the "
          "passive system, and no statement in this topic gives solar energy a turbine."),

 dict(q="A household in a persistently cloudy region asks whether photovoltaic panels will serve "
        "its needs. Which of the framework's statements bears most directly on the question?",
      choices=[
        "That the use of photovoltaic cells is limited by the availability of sunlight",
        "That solar energy systems produce clean energy",
        "That large solar energy farms may negatively impact desert ecosystems",
        "That a passive system cannot collect or store the energy it absorbs",
        "That an active system heats a liquid through mechanical and electric equipment"],
      ans=0,
      why="ENG-3.J.1 names THE AVAILABILITY OF SUNLIGHT as what limits the use of photovoltaic "
          "cells, which is precisely what a cloudy region lacks. The other statements concern "
          "cleanliness, deserts and the two kinds of heating system."),

 dict(q="Which observation would most directly report the framework's claim about large solar "
        "energy farms?",
      choices=[
        "Surveying desert plots with and without a large farm and comparing what lives in them",
        "Measuring the electricity a photovoltaic array delivers on a cloudy day",
        "Measuring the temperature of the liquid in an active system's storage tank",
        "Recording the cost of building an array against the cost of a gas plant",
        "Counting the households in a region that own solar panels"],
      ans=0,
      why="ENG-3.K.1 restricts the claim to LARGE SOLAR ENERGY FARMS and to DESERT ECOSYSTEMS, so "
          "the observation has to compare desert land with and without such a farm. Output, "
          "storage temperature, cost and ownership each bear on a different statement."),

 dict(q="The same array was installed at four sites and its output logged. Which conclusion do "
        "the values support?",
      table=_T_SUN,
      choices=[
        "The array delivers more where there is more sunlight, which is the limit the framework "
        "names on photovoltaic cells",
        "The array delivers less where there is more sunlight",
        "The output of the array is unrelated to the hours of sunlight",
        "The array delivers the same amount at all four sites",
        "The array delivers nothing at the site with the fewest hours of sunlight"],
      ans=0,
      why="Sunlight runs 3, 5, 8 and 10 hours a day while the output runs 150, 250, 400 and 500 "
          "energy units, rising together. ENG-3.J.1 states that the use of photovoltaic cells IS "
          "LIMITED BY THE AVAILABILITY OF SUNLIGHT, which is what a record like this shows."),

 dict(q="Using the same four sites, how much electricity does the array deliver for each hour of "
        "sunlight?",
      table=_T_SUN,
      choices=[
        "50 energy units, the same at every site",
        "50 energy units at the sunniest site and less at the others",
        "A whole day's output of 150 energy units at every site",
        "30 energy units, the same at every site",
        "The amount for each hour cannot be worked out from the record"],
      ans=0,
      why="Dividing output by sunlight hours gives 150 over 3, 250 over 5, 400 over 8 and 500 over "
          "10, which is 50 energy units for each hour at every site. The rejected values quote a "
          "whole day's output, divide the wrong way round, or deny an arithmetic the record plainly "
          "allows."),

 dict(q="A fifth site with the same array averages six hours of sunlight a day. What daily output "
        "does the record lead you to expect there?",
      table=_T_SUN,
      choices=[
        "300 energy units",
        "250 energy units",
        "400 energy units",
        "600 energy units",
        "150 energy units"],
      ans=0,
      why="The record delivers 50 energy units for each hour of sunlight at every site, so six "
          "hours gives 300. The rejected values quote a neighbouring site's output, double the "
          "hours instead of multiplying by the rate, or quote the least sunny site."),

 dict(q="Using the same four sites, how much more does the array deliver at the sunniest site "
        "than at the least sunny?",
      table=_T_SUN,
      choices=[
        "350 energy units",
        "500 energy units",
        "650 energy units",
        "100 energy units",
        "250 energy units"],
      ans=0,
      why="Subtracting the two tabulated outputs gives 500 minus 150, which is 350 energy units. "
          "The rejected values quote the sunniest site alone, add the two, or take one of the "
          "steps between adjacent sites."),

 dict(q="Two solar systems on two houses were compared. Which is the active system and which the "
        "passive?",
      table=_T_SYSTEM,
      choices=[
        "The first is active, because it has mechanical and electric equipment and stores heated "
        "liquid; the second is passive, because it has neither",
        "The first is passive, because it has mechanical and electric equipment and stores "
        "heated liquid; the second is active, because it has neither",
        "Both are active, because both deliver heat to the house on a sunny day",
        "Both are passive, because neither transforms light into electrical energy",
        "Neither can be classified, because the framework describes only photovoltaic cells"],
      ans=0,
      why="The first house carries 6 pieces of mechanical and electric equipment and holds 400 "
          "litres of heated liquid for use after dark; the second carries none and holds none. "
          "ENG-3.J.2 gives equipment and storage to the active system and ENG-3.J.3 denies both to "
          "the passive one."),

 dict(q="Using those same two houses, which of the framework's statements does the second house "
        "illustrate?",
      table=_T_SYSTEM,
      choices=[
        "That a passive system absorbs heat directly from the sun but cannot collect or store it",
        "That a passive system absorbs heat directly from the sun and stores it for later",
        "That an active system absorbs heat directly from the sun but cannot collect or store it",
        "That photovoltaic cells transform light directly into electrical energy",
        "That solar energy systems may negatively impact desert ecosystems"],
      ans=0,
      why="The second house delivers 300 energy units of heat on a sunny day while holding no "
          "heated liquid at all and carrying no equipment. ENG-3.J.3 says exactly this: heat "
          "absorbed directly from the sun, and energy that cannot be collected or stored."),

 dict(q="Using those same two houses, how much more heat does the house with the equipment "
        "deliver on a sunny day?",
      table=_T_SYSTEM,
      choices=[
        "200 energy units",
        "500 energy units",
        "800 energy units",
        "400 energy units",
        "300 energy units"],
      ans=0,
      why="Subtracting the two tabulated deliveries gives 500 minus 300, which is 200 energy "
          "units. The rejected values quote one house alone, add the two, or quote the litres of "
          "stored liquid as though they were energy units."),

 dict(q="A solar array and a gas plant were compared on what each costs to build and what each "
        "releases. Which conclusion matches the framework's statement about solar energy?",
      table=_T_COST,
      choices=[
        "The array produces clean energy but is the more expensive to build, which is the "
        "trade-off the framework names",
        "The array produces clean energy and is the cheaper to build, so the framework names no "
        "trade-off",
        "The array is the more expensive to build and releases more air pollutants than the gas "
        "plant",
        "The gas plant produces clean energy and is the more expensive to build",
        "The two release the same air pollutants for each unit of electricity"],
      ans=0,
      why="The array releases 0 grams of air pollutants for each unit of electricity against the "
          "gas plant's 310, and costs 2,700 currency units for each unit of capacity against 900. "
          "ENG-3.K.1 states that solar energy systems produce clean energy BUT CAN BE EXPENSIVE."),

 dict(q="Using the same two ways of generating, how many times as much does the array cost to "
        "build for each unit of capacity?",
      table=_T_COST,
      choices=[
        "Three times as much",
        "Two times as much",
        "Nine times as much",
        "Thirty times as much",
        "The array is the cheaper of the two"],
      ans=0,
      why="Dividing the two tabulated costs gives 2,700 divided by 900, which is 3. The rejected "
          "values shift the answer by a power of ten, quote a wrong division, or invert the "
          "comparison the record shows."),

 dict(q="Using the same two ways of generating, which of the framework's words does the "
        "pollutant column bear out?",
      table=_T_COST,
      choices=[
        "That solar energy systems produce clean energy",
        "That solar energy systems can be expensive",
        "That large solar farms may negatively impact desert ecosystems",
        "That the use of photovoltaic cells is limited by the availability of sunlight",
        "That an active system collects and stores the energy it captures"],
      ans=0,
      why="The array releases 0 grams of air pollutants for each unit of electricity against 310 "
          "from the gas plant, which speaks to cleanliness rather than to cost, deserts, sunlight "
          "or storage. ENG-3.K.1 states that solar energy systems PRODUCE CLEAN ENERGY."),

 dict(q="Three desert plots were surveyed for what lives in them. Which of the framework's claims "
        "do the values support?",
      table=_T_DESERT,
      choices=[
        "That large solar energy farms may negatively impact desert ecosystems",
        "That large solar energy farms improve desert ecosystems",
        "That solar energy farms have no effect on desert ecosystems of any size",
        "That solar energy systems can be expensive to build",
        "That photovoltaic cells transform light directly into electrical energy"],
      ans=0,
      why="Native plant species fall from 34 to 27 to 15 and reptile species from 11 to 8 to 4 as "
          "the area under panels rises from none to 120 to 900 hectares. ENG-3.K.1 states that "
          "large solar energy farms MAY NEGATIVELY IMPACT DESERT ECOSYSTEMS."),

 dict(q="Using the same three plots, by how many species did the native plant count fall between "
        "the plot with no farm and the plot with the large farm?",
      table=_T_DESERT,
      choices=[
        "By 19 species",
        "By 34 species",
        "By 49 species",
        "By 7 species",
        "By 12 species"],
      ans=0,
      why="Subtracting the two tabulated counts gives 34 minus 15, which is 19 species. The "
          "rejected values quote the undisturbed plot alone, add the two, or take one of the steps "
          "between adjacent plots."),

 dict(q="Does that survey establish that every solar farm harms the ecosystem it is built in?",
      table=_T_DESERT,
      choices=[
        "No, because the framework's claim is hedged and is about large farms in desert "
        "ecosystems",
        "Yes, because the framework's claim about solar farms is stated without qualification",
        "Yes, because the survey covers three plots rather than one",
        "No, because the framework denies that solar farms have any effect on ecosystems",
        "No, because the survey shows the species counts rising with the area under panels"],
      ans=0,
      why="ENG-3.K.1 says large solar energy farms MAY negatively impact DESERT ecosystems, which "
          "is a hedged claim restricted to a size and a habitat. The survey is consistent with it "
          "and the counts do fall, but neither the framework nor three plots supports a universal "
          "claim."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Photovoltaic cells turn light directly into electricity and are limited by the "
        "sunlight available; active systems heat a liquid through mechanical and electric "
        "equipment so the energy can be collected and stored; passive systems absorb heat "
        "directly with no such equipment and cannot collect or store it; and solar systems "
        "have low impact and give clean energy but can be expensive, with large farms possibly "
        "harming desert ecosystems.",
        "Photovoltaic cells heat a liquid; active systems absorb heat with no equipment and "
        "cannot store it; passive systems use equipment and store the energy; and solar is "
        "always the cheapest option.",
        "Photovoltaic cells turn light into electricity without limit; both kinds of heating "
        "system store the energy they capture; and solar farms have no effect on any ecosystem.",
        "Solar energy systems produce dirty energy at high environmental cost, and the "
        "framework distinguishes no kinds of system.",
        "The framework gives figures for the output of every kind of solar system and for the "
        "species lost to every solar farm."],
      ans=0,
      why="The keyed summary carries ENG-3.J.1, J.2, J.3 and K.1 in the framework's own terms, "
          "including both hedges. Each rejected summary exchanges the active and passive "
          "properties, drops the sunlight limit, denies the desert clause, reverses the "
          "environmental verdict, or claims figures the framework never supplies."),
]
