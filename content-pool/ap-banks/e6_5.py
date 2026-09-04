# AP ENVIRONMENTAL SCIENCE 6.5 Fossil Fuels
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.E, describe the use and methods of fossil fuels in power
# generation; and ENG-3.F, describe the effects of fossil fuels on the environment.
# Suggested skill 7.A, describe environmental problems.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.E.1  The combustion of fossil fuels is a chemical reaction between the fuel and
#              oxygen that yields carbon dioxide and water and releases energy.
#   ENG-3.E.2  Energy from fossil fuels is produced by burning those fuels to generate
#              heat, which then turns water into steam. That steam turns a turbine, which
#              spins a generator, producing electricity.
#   ENG-3.E.3  Humans use a variety of methods to extract fossil fuels from the earth for
#              energy generation.
#   ENG-3.F.1  Hydraulic fracturing (fracking) can cause groundwater contamination and the
#              release of volatile organic compounds.
#
# THE CHAIN IN ENG-3.E.2 IS ORDERED, and the order is the framework's own: burn the fuel,
# generate heat, turn water into steam, the steam turns a TURBINE, the turbine spins a
# GENERATOR, and the generator produces electricity. Five items turn on that order and
# their anchors carry the sequence rather than a single link, because the natural
# distractor is the chain with two links exchanged.
#
# ENG-3.E.3 NAMES NO METHOD. It says humans use A VARIETY OF METHODS and stops. So no key
# here asserts that the framework names drilling, surface mining, or any other technique;
# two items key the absence instead. The one extraction method the framework does name is
# hydraulic fracturing, and it names it only in ENG-3.F.1, only to attach two effects.
#
# THOSE TWO EFFECTS, AND NO OTHERS. ENG-3.F.1 attaches GROUNDWATER CONTAMINATION and THE
# RELEASE OF VOLATILE ORGANIC COMPOUNDS to fracking. Induced earthquakes, methane leakage
# and land subsidence are real subjects elsewhere but they are not in this statement, so no
# key asserts them and one item keys the correction.
#
# WHAT COMBUSTION YIELDS, exactly. ENG-3.E.1 names carbon dioxide and water and says the
# reaction releases energy. Sulfur dioxide, nitrogen oxides and particulates are treated in
# Unit 7 and in ENG-3.I.1 for biomass; they are not in this statement, so every item asking
# about products asks what the FRAMEWORK NAMES rather than what a furnace emits.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_5.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.5", "Fossil Fuels", 6)

_T_STAGE = dict(
    headers=["Stage reached inside the power plant",
             "Energy still available at that stage (energy units)"],
    rows=[["Chemical energy in the fuel burned", "1,000"],
          ["Heat carried by the steam", "880"],
          ["Mechanical energy turning the turbine", "400"],
          ["Electricity leaving the generator", "380"]])

_T_PRODUCT = dict(
    headers=["Fossil fuel burned",
             "Carbon dioxide released for each unit of energy (kilograms)",
             "Water released for each unit of energy (kilograms)"],
    rows=[["Coal", "95", "30"],
          ["Crude oil products", "73", "40"],
          ["Natural gas", "53", "60"]])

_T_FRACK = dict(
    headers=["Sampling round",
             "Wells within two kilometers of the site above the contaminant limit (percent)",
             "Wells more than ten kilometers away above the limit (percent)",
             "Volatile organic compounds in the air at the site (parts per billion)"],
    rows=[["Before fracking began", "4", "3", "5"],
          ["One year after fracking began", "26", "4", "41"],
          ["Three years after fracking began", "38", "3", "55"]])

QUESTIONS = [

 dict(q="How does the framework describe the combustion of fossil fuels?",
      choices=[
        "As a chemical reaction between the fuel and oxygen",
        "As a nuclear reaction inside the fuel",
        "As a physical change in which the fuel melts",
        "As a chemical reaction between the fuel and nitrogen",
        "As a reaction that consumes carbon dioxide from the air"],
      ans=0,
      why="ENG-3.E.1 states that the combustion of fossil fuels IS A CHEMICAL REACTION BETWEEN THE "
          "FUEL AND OXYGEN. Nuclear reactions belong to topic 6.6, nothing in the statement makes "
          "combustion a physical change, and the reacting gas named is oxygen."),

 dict(q="Which pair does the framework name as what that reaction yields?",
      choices=[
        "Carbon dioxide and water",
        "Carbon dioxide and sulfur dioxide",
        "Carbon monoxide and water",
        "Nitrogen oxides and water",
        "Carbon dioxide and ozone"],
      ans=0,
      why="ENG-3.E.1 states that the reaction YIELDS CARBON DIOXIDE AND WATER. Carbon monoxide, "
          "nitrogen oxides and particulates appear in the framework's statement about burning "
          "biomass and in the atmospheric pollution unit, not in this one."),

 dict(q="Besides yielding those two products, what else does the framework say the combustion "
        "reaction does?",
      choices=[
        "It releases energy",
        "It absorbs energy from its surroundings",
        "It leaves the total energy unchanged",
        "It releases oxygen back into the air",
        "It removes carbon dioxide from the air"],
      ans=0,
      why="ENG-3.E.1 ends by saying the reaction RELEASES ENERGY, which is why the fuel is burned "
          "at all. Oxygen is a reactant rather than a product in the statement, and carbon dioxide "
          "is produced rather than removed."),

 dict(q="In the framework's account of a fossil fuel power plant, what does the heat from burning "
        "the fuel do?",
      choices=[
        "It turns water into steam",
        "It spins the generator directly",
        "It turns the turbine directly, without any water",
        "It is released to the air before any electricity is made",
        "It splits atoms of the fuel into smaller parts"],
      ans=0,
      why="ENG-3.E.2 states that burning the fuel generates heat, WHICH THEN TURNS WATER INTO "
          "STEAM. The turbine and the generator come later in the framework's sequence, and "
          "splitting atoms is nuclear fission in topic 6.6."),

 dict(q="In that same account, what does the steam do?",
      choices=[
        "It turns a turbine",
        "It spins a generator without passing through a turbine",
        "It is converted directly into electricity",
        "It burns as a fuel in its own right",
        "It cools the fuel before the fuel is burned"],
      ans=0,
      why="ENG-3.E.2 states that THAT STEAM TURNS A TURBINE. The generator comes after the "
          "turbine in the framework's sequence, and steam is a working fluid rather than a fuel."),

 dict(q="In that same account, what does the turbine do?",
      choices=[
        "It spins a generator, which produces the electricity",
        "It produces the electricity itself, with no generator involved",
        "It turns the water back into fuel",
        "It heats the water so that more steam forms",
        "It burns the remaining fuel more completely"],
      ans=0,
      why="ENG-3.E.2 states that the steam turns a turbine, WHICH SPINS A GENERATOR, PRODUCING "
          "ELECTRICITY. The turbine and the generator are separate parts of the framework's "
          "sequence and the electricity comes from the second of them."),

 dict(q="Which sequence matches the framework's account from fuel to electricity?",
      choices=[
        "Burn the fuel to make heat, the heat turns water into steam, the steam turns a "
        "turbine, the turbine spins a generator, the generator produces electricity",
        "Burn the fuel to make heat, the heat turns water into steam, the steam spins a "
        "generator, the generator turns a turbine, the turbine produces electricity",
        "Burn the fuel to make heat, the heat spins a generator, the generator turns water into "
        "steam, the steam turns a turbine",
        "Burn the fuel to make electricity directly, and use the electricity to raise steam for "
        "the turbine",
        "Turn water into steam first, use the steam to burn the fuel, and let the heat spin the "
        "generator"],
      ans=0,
      why="ENG-3.E.2 gives the whole sequence in one sentence: burning generates heat, the heat "
          "turns water into steam, the steam turns a turbine, and the turbine spins a generator "
          "that produces electricity. Each rejected sequence exchanges two of those links."),

 dict(q="A student writes that in a coal plant the burning coal spins the turbine directly. What "
        "correction does the framework require?",
      choices=[
        "The heat turns water into steam, and it is the steam that turns the turbine",
        "The heat spins the generator, and the generator turns the turbine",
        "The burning coal spins the generator, and the generator turns the turbine",
        "The turbine is turned by the exhaust gases rather than by anything else",
        "No correction is needed, since the framework gives no sequence"],
      ans=0,
      why="ENG-3.E.2 puts steam between the heat and the turbine: the heat turns water into steam "
          "and THAT STEAM TURNS A TURBINE. The framework plainly does give a sequence, and the "
          "generator comes after the turbine rather than before it."),

 dict(q="A second student writes that the turbine itself is what produces the electricity. What "
        "correction does the framework require?",
      choices=[
        "The turbine spins a generator, and the generator is what produces the electricity",
        "The turbine produces the electricity and the generator stores it",
        "The steam produces the electricity and the turbine only cools it",
        "The heat produces the electricity before the turbine is reached",
        "No correction is needed, since the framework treats turbine and generator as one part"],
      ans=0,
      why="ENG-3.E.2 states that the steam turns a turbine, WHICH SPINS A GENERATOR, PRODUCING "
          "ELECTRICITY, so the two parts have different jobs and the electricity comes from the "
          "generator. Nothing in the statement gives the generator a storage role."),

 dict(q="What does the framework say about the ways humans get fossil fuels out of the earth?",
      choices=[
        "That humans use a variety of methods, without the framework naming which ones",
        "That humans use a single method, which the framework names",
        "That humans use two methods, drilling and surface mining, which the framework names",
        "That the framework names no methods because no fossil fuel is extracted from the "
        "earth",
        "That extraction methods are outside the scope of the framework entirely"],
      ans=0,
      why="ENG-3.E.3 states that HUMANS USE A VARIETY OF METHODS TO EXTRACT FOSSIL FUELS FROM THE "
          "EARTH FOR ENERGY GENERATION, and it lists none of them. Fossil fuels are certainly "
          "extracted, and the framework does address extraction, so the last two options are "
          "wrong on their face."),

 dict(q="The framework gives a purpose for which humans extract fossil fuels from the earth. "
        "What is that purpose?",
      choices=[
        "Energy generation",
        "The manufacture of plastics and other materials",
        "Export earnings for the countries that hold them",
        "The building of roads and other infrastructure",
        "The framework states no purpose for the extraction"],
      ans=0,
      why="ENG-3.E.3 states that humans use a variety of methods to extract fossil fuels from the "
          "earth FOR ENERGY GENERATION. Materials, trade and construction are not named in the "
          "statement, and the statement does supply a purpose."),

 dict(q="Which claim about extraction does the framework NOT support?",
      choices=[
        "The framework names drilling and surface mining as the two methods that are used",
        "Fossil fuels are extracted from the earth by humans",
        "The extraction described is carried out for energy generation",
        "More than one method of extraction is in use",
        "The framework singles out no one method as the usual one"],
      ans=0,
      why="ENG-3.E.3 says a variety of methods and names none, so any list of specific techniques "
          "comes from outside the framework. Each rejected option is a direct reading of that "
          "statement. The single extraction method the framework does name anywhere in this topic "
          "is hydraulic fracturing, and it names it only to attach two effects."),

 dict(q="Which two effects does the framework attach to hydraulic fracturing?",
      choices=[
        "Groundwater contamination and the release of volatile organic compounds",
        "Groundwater contamination and the release of radioactive waste",
        "Acid deposition and the release of volatile organic compounds",
        "Earthquakes and the contamination of surface water",
        "Thermal pollution and the release of particulates"],
      ans=0,
      why="ENG-3.F.1 states that hydraulic fracturing CAN CAUSE GROUNDWATER CONTAMINATION AND THE "
          "RELEASE OF VOLATILE ORGANIC COMPOUNDS. Radioactive waste belongs to nuclear power in "
          "topic 6.6 and the remaining effects are treated in other units."),

 dict(q="A student writes that the framework blames hydraulic fracturing for earthquakes. What "
        "correction is required?",
      choices=[
        "The framework attaches groundwater contamination and the release of volatile organic "
        "compounds to fracking, and nothing else",
        "The framework attaches earthquakes to fracking, so the student is correct",
        "The framework attaches earthquakes and groundwater contamination to fracking",
        "The framework attaches no effect at all to fracking",
        "The framework attaches only the release of volatile organic compounds to fracking"],
      ans=0,
      why="ENG-3.F.1 names exactly two possible effects and earthquakes is not among them. The "
          "statement does attach effects, so denying that it does is wrong in the other "
          "direction, and dropping the groundwater half leaves the statement incomplete."),

 dict(q="What does the word CAN do in the framework's statement about hydraulic fracturing?",
      choices=[
        "It marks the two effects as possible consequences rather than certain ones",
        "It marks the two effects as certain wherever fracking is used",
        "It marks the two effects as impossible under current practice",
        "It marks the statement as applying only to countries that permit fracking",
        "It has no effect on how the statement should be read"],
      ans=0,
      why="ENG-3.F.1 says fracking CAN CAUSE those two effects, which asserts that they are "
          "possible consequences rather than guaranteed ones. Reading the word away in either "
          "direction changes what the framework claims."),

 dict(q="A company drills a well, then injects fluid at high pressure to crack the rock and free "
        "the gas. Which environmental problems does the framework attach to that method?",
      choices=[
        "Contamination of groundwater and the release of volatile organic compounds",
        "Contamination of groundwater and the release of hazardous solid waste",
        "The killing of birds and bats and a loss of habitat",
        "The release of hydrogen sulfide and a high cost of access",
        "A loss of or change in habitats following the construction of a dam"],
      ans=0,
      why="The method described is hydraulic fracturing, and ENG-3.F.1 attaches groundwater "
          "contamination and the release of volatile organic compounds to it. The rejected "
          "options quote the effects the framework attaches to nuclear power, wind energy, "
          "geothermal energy and hydroelectric power."),

 dict(q="Which observation would most directly report the claim the framework makes about "
        "hydraulic fracturing?",
      choices=[
        "Testing wells near a fracking site for contaminants and measuring volatile organic "
        "compounds in the air there",
        "Counting the number of wells drilled in a country over a decade",
        "Measuring the carbon dioxide released when the extracted gas is later burned",
        "Recording the price the extracted gas fetches at market",
        "Comparing the energy content of gas with the energy content of coal"],
      ans=0,
      why="ENG-3.F.1 names groundwater contamination and the release of volatile organic "
          "compounds, so testing the groundwater and the air is what bears on it. Well counts, "
          "later combustion, price and energy content each belong to a different statement."),

 dict(q="Which statement of this topic concerns what leaves the plant rather than how the plant "
        "works?",
      choices=[
        "The one saying combustion yields carbon dioxide and water and releases energy",
        "The one saying the steam turns a turbine which spins a generator",
        "The one saying humans use a variety of methods to extract fossil fuels",
        "The one saying hydraulic fracturing can contaminate groundwater",
        "The one saying heat from burning turns water into steam"],
      ans=0,
      why="ENG-3.E.1 is about the products of the reaction, so it describes what the combustion "
          "puts out. ENG-3.E.2 describes the machinery, ENG-3.E.3 the getting of the fuel, and "
          "ENG-3.F.1 the effects of one extraction method rather than of the burning."),

 dict(q="Why does the framework's account of a power plant need water in it at all?",
      choices=[
        "Because the heat is transferred to water, and the steam that forms is what turns the "
        "turbine",
        "Because water is one of the reactants that combustion consumes",
        "Because water cools the generator so that it can spin faster",
        "Because water is burned alongside the fuel to raise the temperature",
        "Because water carries the electricity away from the generator"],
      ans=0,
      why="ENG-3.E.2 makes steam the link between the heat and the turbine: the heat turns water "
          "into steam and that steam turns the turbine. Water is a product of combustion in "
          "ENG-3.E.1 rather than a reactant, and it is not a fuel."),

 dict(q="A plant burns a fossil fuel and its record of energy at each stage was logged. Which "
        "order do the stages in the record follow?",
      table=_T_STAGE,
      choices=[
        "The framework's own: fuel, then steam, then turbine, then generator",
        "The framework's own reversed: generator, then turbine, then steam, then fuel",
        "An order the framework does not give: fuel, then turbine, then steam, then generator",
        "An order the framework does not give: fuel, then generator, then turbine, then steam",
        "No order at all, since the framework gives no sequence for a fossil fuel plant"],
      ans=0,
      why="The record runs from the chemical energy in the fuel to the heat in the steam, then to "
          "the mechanical energy at the turbine, then to the electricity leaving the generator. "
          "ENG-3.E.2 gives exactly that sequence, and the energy still available falls at every "
          "step."),

 dict(q="Using the same record, between which two stages is the most energy lost?",
      table=_T_STAGE,
      choices=[
        "Between the steam and the turbine, where 480 energy units are lost",
        "Between the fuel and the steam, where 120 energy units are lost",
        "Between the turbine and the generator, where 20 energy units are lost",
        "Between the fuel and the steam, where 480 energy units are lost",
        "The same amount is lost at every step of the record"],
      ans=0,
      why="The record falls from 1,000 to 880 to 400 to 380 energy units, so the three losses are "
          "120, 480 and 20. The largest is the fall from the steam to the turbine, and pairing "
          "that size with the wrong step is the mistake the rejected options make."),

 dict(q="Using the same record, what share of the energy in the fuel leaves the plant as "
        "electricity?",
      table=_T_STAGE,
      choices=[
        "38 percent",
        "88 percent",
        "40 percent",
        "62 percent",
        "100 percent"],
      ans=0,
      why="Dividing the two tabulated values gives 380 out of 1,000 energy units, which is 38 "
          "percent. The rejected values quote an intermediate stage, take the share that is lost "
          "rather than the share delivered, or assume nothing is lost."),

 dict(q="Using the same record, how much energy is lost turning the chemical energy of the fuel "
        "into the heat carried by the steam?",
      table=_T_STAGE,
      choices=[
        "120 energy units",
        "620 energy units",
        "480 energy units",
        "600 energy units",
        "880 energy units"],
      ans=0,
      why="Subtracting the two tabulated values gives 1,000 minus 880, which is 120 energy units. "
          "The rejected values take the whole loss across the plant, take a later step, run the "
          "loss all the way to the turbine, or quote the energy remaining rather than the amount "
          "lost."),

 dict(q="Three fossil fuels were measured for what their combustion releases. Which conclusion "
        "matches the framework's statement about that reaction?",
      table=_T_PRODUCT,
      choices=[
        "All three fuels release both carbon dioxide and water, which is what the framework "
        "says combustion yields",
        "Only coal releases carbon dioxide, and only natural gas releases water",
        "None of the three releases water, so the framework's statement is not borne out",
        "All three release carbon dioxide, but the framework names water as a reactant rather "
        "than a product",
        "The three release the same amount of carbon dioxide for each unit of energy"],
      ans=0,
      why="Every row carries a positive amount in both columns, 95 and 30 kilograms for coal, 73 "
          "and 40 for crude oil products and 53 and 60 for natural gas. ENG-3.E.1 states that "
          "combustion YIELDS CARBON DIOXIDE AND WATER, so both are products."),

 dict(q="Using the same three fuels, how much more carbon dioxide does coal release for each unit "
        "of energy than natural gas does?",
      table=_T_PRODUCT,
      choices=[
        "42 kilograms",
        "22 kilograms",
        "148 kilograms",
        "95 kilograms",
        "53 kilograms"],
      ans=0,
      why="Subtracting the two tabulated values gives 95 minus 53, which is 42 kilograms. The "
          "rejected values take the gap to crude oil products instead, add the two rows, or quote "
          "one row alone."),

 dict(q="Using the same three fuels, which releases the least carbon dioxide for each unit of "
        "energy, and how does that sit with the rest of the record?",
      table=_T_PRODUCT,
      choices=[
        "Natural gas, which also releases the most water for each unit of energy",
        "Natural gas, which also releases the least water for each unit of energy",
        "Coal, which also releases the most water for each unit of energy",
        "Crude oil products, which release the least of both",
        "The three release equal amounts of carbon dioxide, so none is least"],
      ans=0,
      why="Natural gas sits at 53 kilograms of carbon dioxide, the lowest of the three, and at 60 "
          "kilograms of water, the highest. ENG-3.E.1 names both as products of the same "
          "reaction, so a fuel can be lowest on one and highest on the other."),

 dict(q="Groundwater and air were sampled around a site before and after fracking began. Which of "
        "the framework's claims do the values illustrate?",
      table=_T_FRACK,
      choices=[
        "That hydraulic fracturing can cause groundwater contamination and the release of "
        "volatile organic compounds",
        "That hydraulic fracturing can cause groundwater contamination but not the release of "
        "volatile organic compounds",
        "That hydraulic fracturing can release volatile organic compounds but cannot "
        "contaminate groundwater",
        "That the combustion of fossil fuels yields carbon dioxide and water",
        "That humans use a variety of methods to extract fossil fuels from the earth"],
      ans=0,
      why="Wells near the site rise from 4 to 26 to 38 percent above the contaminant limit while "
          "volatile organic compounds in the air rise from 5 to 41 to 55 parts per billion. "
          "ENG-3.F.1 names both of those effects together."),

 dict(q="Using the same sampling, by how much did the share of nearby wells above the contaminant "
        "limit rise across the record?",
      table=_T_FRACK,
      choices=[
        "By 34 percentage points",
        "By 38 percentage points",
        "By 42 percentage points",
        "By 22 percentage points",
        "By 12 percentage points"],
      ans=0,
      why="Subtracting the two tabulated shares gives 38 minus 4, which is 34 percentage points. "
          "The rejected values quote the final round alone, add the two, or take one of the steps "
          "within the record."),

 dict(q="Using the same sampling, what does the column for wells more than ten kilometers away "
        "add to the case?",
      table=_T_FRACK,
      choices=[
        "It stays near where it began, so the rise is confined to the wells close to the site",
        "It rises as steeply as the nearby wells, so the rise is regional rather than local",
        "It falls sharply, so the distant wells improved as the nearby ones worsened",
        "It is the column that shows the release of volatile organic compounds",
        "It shows that no well anywhere exceeded the contaminant limit"],
      ans=0,
      why="The distant wells run 3, 4 and 3 percent above the limit while the nearby wells run 4, "
          "26 and 38 percent. A control that does not move is what ties the change to the site, "
          "which is the kind of evidence ENG-3.F.1's claim about groundwater contamination "
          "needs."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Combustion is a reaction between fuel and oxygen that yields carbon dioxide and water "
        "and releases energy; the heat raises steam, the steam turns a turbine, the turbine "
        "spins a generator that makes electricity; humans extract fossil fuels by a variety of "
        "methods; and hydraulic fracturing can contaminate groundwater and release volatile "
        "organic compounds.",
        "Combustion is a nuclear reaction that yields carbon dioxide and water; the steam spins "
        "a generator which then turns a turbine; and fracking causes earthquakes.",
        "Combustion releases energy without producing carbon dioxide; the framework names "
        "drilling as the single method of extraction; and fracking has no recorded effects.",
        "The framework gives no sequence for how a fossil fuel plant makes electricity and no "
        "effects for any extraction method.",
        "Fossil fuels are renewable because the carbon dioxide they release is taken up again "
        "at or near the rate of consumption."],
      ans=0,
      why="The keyed summary carries ENG-3.E.1, E.2, E.3 and F.1 in the framework's own terms and "
          "adds nothing. Each rejected summary misnames the reaction, exchanges two links of the "
          "sequence, invents an extraction method or an effect the framework does not name, or "
          "imports the renewable definition from topic 6.1."),
]
