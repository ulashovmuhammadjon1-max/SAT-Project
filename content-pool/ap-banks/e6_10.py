# AP ENVIRONMENTAL SCIENCE 6.10 Geothermal Energy
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.N, describe the use of geothermal energy in power generation; and
# ENG-3.O, describe the effects of the use of geothermal energy in power generation on the
# environment.
# Suggested skill 1.B, explain environmental concepts and processes.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.N.1  Geothermal energy is obtained by using the heat stored in the Earth's
#              interior to heat up water, which is brought back to the surface as steam. The
#              steam is used to drive an electric generator.
#   ENG-3.O.1  The cost of accessing geothermal energy can be prohibitively expensive, as is
#              not easily accessible in many parts of the world. In addition, it can cause
#              the release of hydrogen sulfide.
#
# TWO STATEMENTS AND NOTHING ELSE. Everything keyed here comes out of the four steps of
# ENG-3.N.1 -- heat stored in the Earth's interior, water heated by it, the water returned
# to the surface AS STEAM, and the steam driving an electric generator -- or out of the
# three drawbacks in ENG-3.O.1: a cost that can be PROHIBITIVELY expensive, a resource NOT
# EASILY ACCESSIBLE IN MANY PARTS OF THE WORLD, and the possible release of HYDROGEN
# SULFIDE.
#
# THE FRAMEWORK NAMES NO ADVANTAGE FOR GEOTHERMAL ENERGY. It gives wind two adjectives
# (ENG-3.S.1), solar two (ENG-3.K.1) and hydroelectricity a denial of air pollution and
# waste (ENG-3.M.1); for geothermal energy it describes the process and lists three
# drawbacks. One item keys that absence honestly rather than inventing an advantage from
# what a student may expect, and no other item asserts one.
#
# NO FUEL IS BURNED HERE. The heat is STORED IN THE EARTH'S INTERIOR, not released by
# combustion or by fission. Two items key the correction, because the steam in this
# statement looks exactly like the steam in ENG-3.E.2 and ENG-3.G.1 and the source of the
# heat is the whole difference.
#
# BOTH HEDGES ARE KEYED. The cost CAN BE prohibitively expensive and the plant CAN CAUSE the
# release of hydrogen sulfide. Neither is stated as certain, and one item keys what
# PROHIBITIVELY adds beyond merely high.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_10.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.10", "Geothermal Energy", 6)

_T_STAGE = dict(
    headers=["Stage reached at the geothermal plant",
             "Energy still available at that stage (energy units)"],
    rows=[["Heat drawn from the hot rock below", "1,000"],
          ["Heat carried by the steam at the surface", "720"],
          ["Electricity leaving the generator", "150"]])

_T_ACCESS = dict(
    headers=["Region surveyed",
             "Depth to rock hot enough to raise steam (meters)",
             "Cost of drilling to that depth (million currency units)"],
    rows=[["Region 1", "800", "4"],
          ["Region 2", "2,400", "12"],
          ["Region 3", "6,000", "30"]])

_T_SULFIDE = dict(
    headers=["Sampling point",
             "Distance from the geothermal plant (kilometers)",
             "Hydrogen sulfide in the air (parts per billion)"],
    rows=[["Point 1", "0.5", "180"],
          ["Point 2", "2", "60"],
          ["Point 3", "10", "8"],
          ["Point 4", "25", "2"]])

_T_SITE = dict(
    headers=["Site considered for a geothermal plant",
             "Depth to the hot rock (meters)",
             "Cost of the whole project (million currency units)",
             "Funds the community can raise (million currency units)"],
    rows=[["Site A", "900", "5", "20"],
          ["Site B", "5,600", "28", "20"]])

QUESTIONS = [

 dict(q="Where does the framework say the heat used for geothermal energy is stored?",
      choices=[
        "In the Earth's interior",
        "In the fuel rods of a reactor",
        "In the carbon bonds of a fossil fuel",
        "In the upper atmosphere",
        "In a tank of liquid heated by the sun"],
      ans=0,
      why="ENG-3.N.1 states that geothermal energy is obtained by using THE HEAT STORED IN THE "
          "EARTH'S INTERIOR. Fuel rods belong to nuclear power in topic 6.6, chemical energy in a "
          "fuel to fossil fuels in 6.5, and a heated tank to an active solar system in 6.8."),

 dict(q="What does the framework say that stored heat is used to do?",
      choices=[
        "Heat up water",
        "Split atoms of Uranium-235",
        "Burn a fuel more completely",
        "Charge a bank of batteries",
        "Warm the air inside a building with no equipment"],
      ans=0,
      why="ENG-3.N.1 states that the heat stored in the Earth's interior is used TO HEAT UP WATER. "
          "Splitting atoms is fission in topic 6.6, and warming a building directly with no "
          "equipment is a passive solar system in topic 6.8."),

 dict(q="In what form does the framework say the water comes back to the surface?",
      choices=[
        "As steam",
        "As liquid water at the temperature it went down",
        "As a mixture of gases that is then burned",
        "As ice that is melted at the surface",
        "It does not come back to the surface at all"],
      ans=0,
      why="ENG-3.N.1 states that the water IS BROUGHT BACK TO THE SURFACE AS STEAM. The statement "
          "plainly has the water returning, and nothing in it is burned."),

 dict(q="What does the framework say the steam is used to do?",
      choices=[
        "Drive an electric generator",
        "Heat a liquid for storage in a tank",
        "Melt the rock so that more heat can be reached",
        "Carry hydrogen sulfide away from the plant",
        "Be burned as a fuel in its own right"],
      ans=0,
      why="ENG-3.N.1 ends by stating that THE STEAM IS USED TO DRIVE AN ELECTRIC GENERATOR. "
          "Heating a liquid for storage is an active solar system in topic 6.8, and steam is a "
          "working fluid rather than a fuel."),

 dict(q="Which sequence matches the framework's account of how geothermal energy is obtained?",
      choices=[
        "Heat stored in the Earth's interior heats water, the water returns to the surface as "
        "steam, and the steam drives an electric generator",
        "Heat stored in the Earth's interior drives an electric generator, and the electricity "
        "then heats water into steam",
        "Water is heated at the surface, sent down as steam, and used to warm the rock below",
        "A fuel is burned at the surface to heat water, and the steam drives an electric "
        "generator",
        "Steam rises from the rock without any water being heated, and is then burned"],
      ans=0,
      why="ENG-3.N.1 gives the whole sequence in one sentence: the heat stored in the Earth's "
          "interior heats up water, the water is brought back to the surface as steam, and the "
          "steam drives an electric generator. Each rejected sequence reverses two steps, sends "
          "the water the wrong way, or introduces a fuel the statement does not have."),

 dict(q="A student writes that a geothermal plant burns a fuel to raise its steam. What "
        "correction does the framework require?",
      choices=[
        "The heat comes from the Earth's interior, and nothing is burned",
        "The heat comes from splitting atoms, and nothing is burned",
        "The heat comes from burning a fuel, so the student is correct",
        "The heat comes from sunlight absorbed at the surface",
        "The framework does not say where the heat comes from"],
      ans=0,
      why="ENG-3.N.1 makes the source THE HEAT STORED IN THE EARTH'S INTERIOR, which is neither a "
          "combustion nor a fission. Sunlight absorbed at the surface is solar energy in topic "
          "6.8, and the framework certainly does name the source."),

 dict(q="A second student writes that the heat from the Earth's interior is turned straight into "
        "electricity. What correction does the framework require?",
      choices=[
        "The heat first heats water, which returns as steam and drives an electric generator",
        "The heat first drives an electric generator, which then makes the steam",
        "The heat is turned straight into electricity, so the student is correct",
        "The heat is used to warm buildings and never makes electricity",
        "The heat is stored in a tank until demand is high enough"],
      ans=0,
      why="ENG-3.N.1 puts water and steam between the stored heat and the generator. Transforming "
          "energy directly into electricity is what photovoltaic cells do in topic 6.8, and "
          "storing energy in a tank is an active solar system there."),

 dict(q="What does the framework say about the cost of accessing geothermal energy?",
      choices=[
        "That it can be prohibitively expensive",
        "That it is always the cheapest option available",
        "That it is prohibitively expensive everywhere without exception",
        "That the framework makes no claim about the cost",
        "That the cost falls as the depth to the hot rock increases"],
      ans=0,
      why="ENG-3.O.1 states that THE COST OF ACCESSING GEOTHERMAL ENERGY CAN BE PROHIBITIVELY "
          "EXPENSIVE. The word can makes it a possibility rather than a universal, and the "
          "framework does make the claim rather than withholding it."),

 dict(q="What does the framework say about where geothermal energy can be reached?",
      choices=[
        "That it is not easily accessible in many parts of the world",
        "That it is easily accessible everywhere in the world",
        "That it is accessible only at the poles",
        "That accessibility depends on the availability of sunlight",
        "That the framework makes no claim about accessibility"],
      ans=0,
      why="ENG-3.O.1 states that geothermal energy IS NOT EASILY ACCESSIBLE IN MANY PARTS OF THE "
          "WORLD. The availability of sunlight limits photovoltaic cells in topic 6.8, not "
          "geothermal energy, and no region of the world is singled out."),

 dict(q="Which substance does the framework say the use of geothermal energy can release?",
      choices=[
        "Hydrogen sulfide",
        "Sulfur dioxide",
        "Volatile organic compounds",
        "Hazardous solid waste",
        "Nitrogen oxides"],
      ans=0,
      why="ENG-3.O.1 ends by stating that it CAN CAUSE THE RELEASE OF HYDROGEN SULFIDE. Volatile "
          "organic compounds belong to fracking in topic 6.5, hazardous solid waste to nuclear "
          "power in 6.6, and nitrogen oxides to burning biomass in 6.7."),

 dict(q="Which of the following is NOT among the drawbacks the framework attaches to geothermal "
        "energy?",
      choices=[
        "The production of hazardous solid waste",
        "A cost of access that can be prohibitively expensive",
        "A resource that is not easily accessible in many parts of the world",
        "The possible release of hydrogen sulfide",
        "An access cost high enough to stop a project going ahead"],
      ans=0,
      why="ENG-3.O.1 names a prohibitively expensive cost, poor accessibility in many parts of the "
          "world, and the possible release of hydrogen sulfide. Hazardous solid waste is what "
          "ENG-3.G.4 attaches to nuclear power, and every rejected option restates one of the "
          "three the framework does give."),

 dict(q="What does the word PROHIBITIVELY add to the framework's claim about cost?",
      choices=[
        "That the cost can be high enough to prevent access altogether, not merely high",
        "That the cost is forbidden by law in some countries",
        "That the cost is high only in the first year of a project",
        "That the cost is lower than for any other energy source",
        "It adds nothing; the word is a synonym for expensive"],
      ans=0,
      why="A prohibitive cost is one that stops the thing being done, so ENG-3.O.1's phrase makes "
          "the expense a barrier to access rather than a large number. Nothing in the statement "
          "concerns law, timing, or a comparison with other sources."),

 dict(q="What do the words CAN BE and CAN CAUSE establish in the framework's statement about the "
        "effects of geothermal energy?",
      choices=[
        "That the prohibitive cost and the release of hydrogen sulfide are possible rather than "
        "certain",
        "That the prohibitive cost and the release of hydrogen sulfide follow from every project",
        "That neither the cost nor the release has ever been recorded",
        "That the two effects apply only where the rock is shallow",
        "That the framework is unsure whether geothermal energy exists"],
      ans=0,
      why="ENG-3.O.1 hedges both clauses, saying the cost CAN BE prohibitively expensive and that "
          "geothermal energy CAN CAUSE the release of hydrogen sulfide. The accessibility clause "
          "is stated without a hedge and is not restricted to shallow rock."),

 dict(q="Which advantage does the framework state for geothermal energy in this topic?",
      choices=[
        "None; it describes the process and then names three drawbacks",
        "That it is a renewable, clean source of energy",
        "That it generates no air pollution and no waste",
        "That it has low environmental impact and produces clean energy",
        "That it produces heat for energy at a relatively low cost"],
      ans=0,
      why="ENG-3.N.1 explains how geothermal energy is obtained and ENG-3.O.1 gives cost, "
          "accessibility and hydrogen sulfide. The rejected options quote the advantages the "
          "framework grants to wind in ENG-3.S.1, hydroelectricity in ENG-3.M.1, solar energy in "
          "ENG-3.K.1 and biomass in ENG-3.I.1."),

 dict(q="What does the framework's geothermal account have in common with its accounts of fossil "
        "fuel and nuclear generation?",
      choices=[
        "In all three, heat turns water into steam and the steam drives the generation of "
        "electricity",
        "In all three, a fuel is burned to release the heat",
        "In all three, atoms are split to release the heat",
        "In all three, light is transformed directly into electrical energy",
        "In all three, the energy is stored in a tank before it is used"],
      ans=0,
      why="ENG-3.N.1, ENG-3.E.2 and ENG-3.G.1 all run through steam on the way to electricity. "
          "Only the fossil fuel account burns a fuel, only the nuclear account splits atoms, and "
          "transforming light directly is photovoltaic solar energy in topic 6.8."),

 dict(q="What distinguishes the geothermal heat source from the fossil fuel one in the "
        "framework's accounts?",
      choices=[
        "The geothermal heat is already stored in the Earth's interior; the fossil fuel heat is "
        "released by a chemical reaction with oxygen",
        "The geothermal heat is released by a chemical reaction with oxygen; the fossil fuel "
        "heat is already stored in the Earth's interior",
        "Both heats are released by burning, and only the temperature differs",
        "Both heats are already stored in the Earth's interior, and only the depth differs",
        "The framework does not say where either heat comes from"],
      ans=0,
      why="ENG-3.N.1 uses THE HEAT STORED IN THE EARTH'S INTERIOR while ENG-3.E.1 makes combustion "
          "A CHEMICAL REACTION BETWEEN THE FUEL AND OXYGEN that releases energy. One rejected "
          "option is the exact swap of the two sources."),

 dict(q="Which observation would most directly report the framework's claim about what geothermal "
        "energy can release?",
      choices=[
        "Measuring hydrogen sulfide in the air around a working geothermal plant",
        "Measuring the depth to the hot rock beneath several regions",
        "Recording the cost of drilling a geothermal well",
        "Measuring the temperature of the steam reaching the generator",
        "Counting the geothermal plants built in a country over a decade"],
      ans=0,
      why="ENG-3.O.1 names the release of HYDROGEN SULFIDE, so measuring that gas around a plant "
          "is what bears on it. Depth and drilling cost bear on the accessibility and cost "
          "clauses, and steam temperature and plant counts on neither."),

 dict(q="Which observation would most directly report the framework's claim about accessibility?",
      choices=[
        "Measuring, across many regions, how deep one must drill to reach rock hot enough to "
        "raise steam",
        "Measuring hydrogen sulfide in the air downwind of one plant",
        "Measuring the electricity one generator delivers in a year",
        "Recording the number of households a plant supplies",
        "Measuring the temperature of the water before it is sent underground"],
      ans=0,
      why="ENG-3.O.1 says geothermal energy is NOT EASILY ACCESSIBLE IN MANY PARTS OF THE WORLD, "
          "which is a claim about how the resource varies from place to place, so the observation "
          "must cover many regions. Hydrogen sulfide bears on the third clause and the rest on "
          "neither."),

 dict(q="The energy at each stage of a geothermal plant was logged. Which order do the stages in "
        "the record follow?",
      table=_T_STAGE,
      choices=[
        "The framework's own: heat from the rock, then steam at the surface, then electricity "
        "from the generator",
        "The framework's own reversed: electricity, then steam at the surface, then heat from "
        "the rock",
        "An order the framework does not give: steam first, then heat from the rock, then "
        "electricity",
        "An order the framework does not give: electricity first, then heat from the rock, then "
        "steam",
        "No order at all, since the framework gives no sequence for a geothermal plant"],
      ans=0,
      why="The record runs from the heat drawn out of the hot rock, to the heat carried by the "
          "steam at the surface, to the electricity leaving the generator, and the energy still "
          "available falls at every step. ENG-3.N.1 gives exactly that sequence."),

 dict(q="Using the same record, what share of the heat drawn from the rock leaves the plant as "
        "electricity?",
      table=_T_STAGE,
      choices=[
        "15 percent",
        "72 percent",
        "28 percent",
        "85 percent",
        "100 percent"],
      ans=0,
      why="Dividing the two tabulated values gives 150 out of 1,000 energy units, which is 15 "
          "percent. The rejected values quote the intermediate stage, take the share lost rather "
          "than the share delivered, or assume nothing is lost."),

 dict(q="Using the same record, how much energy is lost between the hot rock and the steam "
        "arriving at the surface?",
      table=_T_STAGE,
      choices=[
        "280 energy units",
        "850 energy units",
        "570 energy units",
        "720 energy units",
        "150 energy units"],
      ans=0,
      why="Subtracting the two tabulated values gives 1,000 minus 720, which is 280 energy units. "
          "The rejected values take the whole loss across the plant, take the later step, or quote "
          "the energy remaining rather than the amount lost."),

 dict(q="Three regions were surveyed for how deep the hot rock lies and what drilling to it "
        "costs. Which of the framework's claims do the values illustrate?",
      table=_T_ACCESS,
      choices=[
        "That geothermal energy is not easily accessible in many parts of the world, and that "
        "the cost of access can be prohibitively expensive",
        "That geothermal energy is easily accessible everywhere, and that the cost of access is "
        "always low",
        "That geothermal energy can cause the release of hydrogen sulfide",
        "That the steam raised is used to drive an electric generator",
        "That the cost of access falls as the depth to the hot rock rises"],
      ans=0,
      why="The depth to usable rock runs 800, 2,400 and 6,000 meters and the drilling cost 4, 12 "
          "and 30 million currency units, so what is shallow and cheap in one region is deep and "
          "dear in another. ENG-3.O.1 names both the accessibility and the cost."),

 dict(q="Using the same three regions, what does drilling cost for each thousand meters of depth?",
      table=_T_ACCESS,
      choices=[
        "5 million currency units, the same in all three regions",
        "4 million currency units, the same in all three regions",
        "12 million currency units, the same in all three regions",
        "A different amount in each region, rising with depth",
        "The cost for each thousand meters cannot be worked out from the record"],
      ans=0,
      why="Dividing cost by depth gives 4 over 800, 12 over 2,400 and 30 over 6,000, which is 5 "
          "million currency units for each thousand meters in every region. The rejected values "
          "quote a whole project cost or deny an arithmetic the record plainly allows."),

 dict(q="Using the same three regions, how much more does drilling cost in the deepest region "
        "than in the shallowest?",
      table=_T_ACCESS,
      choices=[
        "26 million currency units",
        "30 million currency units",
        "34 million currency units",
        "18 million currency units",
        "12 million currency units"],
      ans=0,
      why="Subtracting the two tabulated costs gives 30 minus 4, which is 26 million currency "
          "units. The rejected values quote the deepest region alone, add the two, take the step "
          "between the two deeper regions, or quote the middle region's cost."),

 dict(q="The air around a geothermal plant was sampled at four distances. Which of the "
        "framework's claims do the values support?",
      table=_T_SULFIDE,
      choices=[
        "That the use of geothermal energy can cause the release of hydrogen sulfide",
        "That the use of geothermal energy cannot cause the release of hydrogen sulfide",
        "That geothermal energy releases sulfur dioxide rather than hydrogen sulfide",
        "That geothermal energy is not easily accessible in many parts of the world",
        "That the cost of accessing geothermal energy can be prohibitively expensive"],
      ans=0,
      why="Hydrogen sulfide reads 180 parts per billion half a kilometer from the plant and falls "
          "to 2 parts per billion at twenty-five kilometers. ENG-3.O.1 states that geothermal "
          "energy CAN CAUSE THE RELEASE OF HYDROGEN SULFIDE, and the gas measured is that one."),

 dict(q="Using the same sampling, what in the record points to the plant as the source of the "
        "gas?",
      table=_T_SULFIDE,
      choices=[
        "The reading is highest closest to the plant and falls steadily with distance from it",
        "The reading is highest farthest from the plant and falls towards it",
        "The reading is the same at all four sampling points",
        "The reading is zero at every sampling point",
        "The record gives no distances, so nothing can be said about the source"],
      ans=0,
      why="The readings run 180, 60, 8 and 2 parts per billion at 0.5, 2, 10 and 25 kilometers, so "
          "the gas is concentrated where the plant is. A gradient pointing at one place is what "
          "ties a release to a source."),

 dict(q="Using the same sampling, how much higher is the reading at the nearest point than at the "
        "farthest?",
      table=_T_SULFIDE,
      choices=[
        "178 parts per billion higher",
        "180 parts per billion higher",
        "182 parts per billion higher",
        "120 parts per billion higher",
        "6 parts per billion higher"],
      ans=0,
      why="Subtracting the two tabulated readings gives 180 minus 2, which is 178 parts per "
          "billion. The rejected values quote the nearest point alone, add the two, or take one of "
          "the steps between adjacent points."),

 dict(q="Two sites were assessed for a geothermal project by a community. At which site would the "
        "framework's phrase about cost apply, and why?",
      table=_T_SITE,
      choices=[
        "The second site, because the project would cost more than the community can raise",
        "The first site, because the project would cost more than the community can raise",
        "The second site, because the hot rock there lies closer to the surface",
        "Both sites, because both projects cost more than the community can raise",
        "Neither site, because the framework attaches no cost claim to geothermal energy"],
      ans=0,
      why="The second site would cost 28 million currency units against the 20 million the "
          "community can raise, while the first would cost 5 million. ENG-3.O.1 calls the cost of "
          "access PROHIBITIVELY expensive, which is a cost that stops the project rather than "
          "merely a large one."),

 dict(q="Using the same two sites, by how much would the dearer project exceed the funds "
        "available?",
      table=_T_SITE,
      choices=[
        "By 8 million currency units",
        "By 28 million currency units",
        "By 48 million currency units",
        "By 23 million currency units",
        "By 15 million currency units"],
      ans=0,
      why="Subtracting the tabulated figures gives 28 minus 20, which is 8 million currency units. "
          "The rejected values quote the project cost alone, add the two, or subtract the cheaper "
          "project instead."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Heat stored in the Earth's interior heats water, which returns to the surface as steam "
        "and drives an electric generator; the cost of access can be prohibitively expensive, "
        "geothermal energy is not easily accessible in many parts of the world, and its use can "
        "release hydrogen sulfide.",
        "A fuel is burned to heat water, the steam drives an electric generator, and the "
        "framework names no drawbacks at all.",
        "Heat stored in the Earth's interior is turned straight into electricity, and the only "
        "drawback is the release of hazardous solid waste.",
        "Geothermal energy is easily accessible everywhere, is always cheap, and releases "
        "nothing.",
        "Geothermal energy is a renewable, clean source of energy, which is what this topic "
        "establishes."],
      ans=0,
      why="The keyed summary carries ENG-3.N.1 and ENG-3.O.1 in the framework's own terms, "
          "including all three drawbacks and both hedges. Each rejected summary introduces a fuel, "
          "removes the water and steam, substitutes a drawback from another topic, denies the "
          "drawbacks, or grants an advantage the framework gives to wind rather than to geothermal "
          "energy."),
]
