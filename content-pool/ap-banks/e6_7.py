# AP ENVIRONMENTAL SCIENCE 6.7 Energy from Biomass
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objective ENG-3.I, describe the effects of the use of biomass in power
# generation on the environment.
# Suggested skill 7.B, describe potential responses or approaches to environmental problems.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.I.1  Burning of biomass produces heat for energy at a relatively low cost, but it
#              also produces carbon dioxide, carbon monoxide, nitrogen oxides, particulates,
#              and volatile organic compounds. The overharvesting of trees for fuel also
#              causes deforestation.
#   ENG-3.I.2  Ethanol can be used as a substitute for gasoline. Burning ethanol does not
#              introduce additional carbon into the atmosphere via combustion, but the
#              energy return on energy investment for ethanol is low.
#
# BOTH STATEMENTS ARE BUILT AS A TRADE-OFF, and the word BUT is doing the work in each.
# Biomass gives heat cheaply BUT emits five named substances; ethanol substitutes for
# gasoline and adds no additional carbon via combustion BUT returns little energy on the
# energy invested. Every summary item and every scenario item here keys both halves, and
# the anchors carry both, because keeping only the favourable half is the way these two
# statements are usually misreported.
#
# THE FIVE SUBSTANCES ARE A CLOSED LIST IN THIS STATEMENT: carbon dioxide, carbon monoxide,
# nitrogen oxides, particulates, and volatile organic compounds. Sulfur dioxide is not among
# them, so one item keys which of six is absent from the framework's own list -- a question
# about the sentence rather than about what any particular furnace emits.
#
# THE CARBON CLAIM IS HEDGED TWICE. ENG-3.I.2 says burning ethanol does not introduce
# ADDITIONAL carbon into the atmosphere VIA COMBUSTION. It does not say ethanol is carbon
# free, and it does not say the whole production chain is. One item keys the correction to
# a student who drops the hedge, and no key anywhere states the stronger claim.
#
# BIOMASS IS NOT CLASSIFIED HERE. The framework labels nuclear power nonrenewable
# (ENG-3.G.4) and wind renewable (ENG-3.S.1); it never labels biomass either way. One item
# keys that absence and no other item treats biomass as classified.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_7.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.7", "Energy from Biomass", 6)

_T_EMIT = dict(
    headers=["Substance measured as the biomass burns",
             "Amount released for each unit of energy (grams)"],
    rows=[["Carbon dioxide", "105"],
          ["Carbon monoxide", "4.2"],
          ["Nitrogen oxides", "0.9"],
          ["Particulates", "1.6"],
          ["Volatile organic compounds", "0.5"]])

_T_COST = dict(
    headers=["Fuel a household could use for heat",
             "Cost of the fuel for each unit of energy (currency units)"],
    rows=[["Biomass gathered locally", "1"],
          ["Bottled gas", "6"],
          ["Electricity from the grid", "9"]])

_T_FOREST = dict(
    headers=["Decade of the record",
             "Wood cut for fuel each year (thousand tonnes)",
             "Wood regrowing each year (thousand tonnes)",
             "Forest area remaining (thousand hectares)"],
    rows=[["First", "40", "55", "900"],
          ["Second", "90", "55", "760"],
          ["Third", "150", "55", "520"]])

_T_RETURN = dict(
    headers=["Fuel compared",
             "Energy the fuel delivers (energy units)",
             "Energy invested to produce the fuel (energy units)"],
    rows=[["Ethanol from a crop", "150", "100"],
          ["Gasoline from crude oil", "1,200", "100"]])

QUESTIONS = [

 dict(q="What does the framework say the burning of biomass produces, and on what terms?",
      choices=[
        "Heat for energy at a relatively low cost",
        "Heat for energy at a relatively high cost",
        "Electricity directly, at a relatively low cost",
        "Heat for energy with no cost of any kind",
        "Nothing useful, only pollutants"],
      ans=0,
      why="ENG-3.I.1 opens by stating that BURNING OF BIOMASS PRODUCES HEAT FOR ENERGY AT A "
          "RELATIVELY LOW COST. The word relatively makes it a comparison rather than a claim that "
          "the fuel is free, and the statement plainly grants that something useful is produced."),

 dict(q="Which five substances does the framework say the burning of biomass also produces?",
      choices=[
        "Carbon dioxide, carbon monoxide, nitrogen oxides, particulates, and volatile organic "
        "compounds",
        "Carbon dioxide, sulfur dioxide, nitrogen oxides, particulates, and ozone",
        "Carbon monoxide, sulfur dioxide, methane, particulates, and volatile organic compounds",
        "Carbon dioxide, carbon monoxide, methane, radon, and particulates",
        "Nitrogen oxides, sulfur dioxide, ozone, particulates, and volatile organic compounds"],
      ans=0,
      why="ENG-3.I.1 lists CARBON DIOXIDE, CARBON MONOXIDE, NITROGEN OXIDES, PARTICULATES, AND "
          "VOLATILE ORGANIC COMPOUNDS. Sulfur dioxide, ozone, methane and radon appear nowhere in "
          "that list, though some of them are treated in the atmospheric pollution unit."),

 dict(q="Which of the following is NOT on the framework's list of what burning biomass produces?",
      choices=[
        "Sulfur dioxide",
        "Carbon monoxide",
        "Nitrogen oxides",
        "Particulates",
        "Volatile organic compounds"],
      ans=0,
      why="ENG-3.I.1 names carbon dioxide, carbon monoxide, nitrogen oxides, particulates and "
          "volatile organic compounds, and sulfur dioxide is not among them. Every rejected option "
          "quotes the statement directly, so the question is about the sentence rather than about "
          "what any particular furnace emits."),

 dict(q="What further problem does the framework attach to taking trees for fuel?",
      choices=[
        "Overharvesting of trees for fuel causes deforestation",
        "Overharvesting of trees for fuel causes groundwater contamination",
        "Taking trees for fuel releases hazardous solid waste",
        "Taking trees for fuel releases hydrogen sulfide",
        "The framework attaches no further problem to taking trees for fuel"],
      ans=0,
      why="ENG-3.I.1 ends by stating that THE OVERHARVESTING OF TREES FOR FUEL ALSO CAUSES "
          "DEFORESTATION. Groundwater contamination belongs to fracking in topic 6.5, hazardous "
          "solid waste to nuclear power in 6.6, and hydrogen sulfide to geothermal energy in "
          "6.10."),

 dict(q="What does the framework say ethanol can be used as?",
      choices=[
        "A substitute for gasoline",
        "A substitute for coal in power stations",
        "A substitute for uranium in fuel rods",
        "A substitute for natural gas in home heating",
        "A material that cannot be burned as a fuel at all"],
      ans=0,
      why="ENG-3.I.2 opens by stating that ETHANOL CAN BE USED AS A SUBSTITUTE FOR GASOLINE. The "
          "statement names no other fuel it replaces, and it plainly treats ethanol as something "
          "that is burned."),

 dict(q="What does the framework say about the carbon that burning ethanol puts into the "
        "atmosphere?",
      choices=[
        "That burning it does not introduce additional carbon into the atmosphere by way of the "
        "combustion",
        "That burning it introduces more carbon into the atmosphere than gasoline does",
        "That burning it removes carbon from the atmosphere",
        "That ethanol contains no carbon at any stage",
        "That the framework says nothing about carbon and ethanol"],
      ans=0,
      why="ENG-3.I.2 states that BURNING ETHANOL DOES NOT INTRODUCE ADDITIONAL CARBON INTO THE "
          "ATMOSPHERE VIA COMBUSTION. The claim is about additional carbon and about combustion "
          "in particular; it does not say carbon is removed, and it does not say ethanol is "
          "carbon free."),

 dict(q="What reservation does the framework attach to ethanol in the same statement?",
      choices=[
        "The energy return on energy investment for ethanol is low",
        "The energy return on energy investment for ethanol is high",
        "Ethanol releases sulfur dioxide when it is burned",
        "Ethanol cannot be transported in existing pipelines",
        "The framework attaches no reservation to ethanol"],
      ans=0,
      why="ENG-3.I.2 ends by stating that THE ENERGY RETURN ON ENERGY INVESTMENT FOR ETHANOL IS "
          "LOW. Sulfur dioxide and transport are not in the statement, and the reservation is "
          "certainly made rather than withheld."),

 dict(q="What does the phrase about energy return on energy investment compare?",
      choices=[
        "The energy the fuel delivers against the energy spent producing it",
        "The energy the fuel delivers against the money spent producing it",
        "The carbon the fuel releases against the carbon its crop absorbed",
        "The price of the fuel against the price of gasoline",
        "The land used to grow the crop against the land used to drill for oil"],
      ans=0,
      why="An energy return on energy investment sets energy delivered beside energy invested, "
          "which is why ENG-3.I.2 can call it low for ethanol without mentioning money. Price, "
          "carbon accounting and land use are separate matters the statement does not raise."),

 dict(q="How is the framework's statement about burning biomass built?",
      choices=[
        "As a trade-off: cheap heat on one side, five named emissions and deforestation on the "
        "other",
        "As an unqualified recommendation of biomass over every other fuel",
        "As an unqualified warning against biomass, with no benefit named",
        "As a comparison of biomass with nuclear power on cost alone",
        "As a definition of which energy sources count as renewable"],
      ans=0,
      why="ENG-3.I.1 grants cheap heat and then turns on the word but to five emissions, and it "
          "adds deforestation from overharvesting. Neither half stands alone, and the statement "
          "compares biomass with nothing in particular and defines nothing."),

 dict(q="A student writes that burning biomass releases carbon dioxide and nothing else. What "
        "correction does the framework require?",
      choices=[
        "It also produces carbon monoxide, nitrogen oxides, particulates and volatile organic "
        "compounds",
        "It produces carbon monoxide instead of carbon dioxide",
        "It produces no carbon dioxide at all, only particulates",
        "It produces sulfur dioxide as well as carbon dioxide",
        "No correction is needed, since carbon dioxide is the only product the framework names"],
      ans=0,
      why="ENG-3.I.1 names five substances and carbon dioxide is only the first of them. Sulfur "
          "dioxide is not on the list, and the statement does not replace carbon dioxide with "
          "anything or deny that it is produced."),

 dict(q="A second student writes that the framework treats biomass as an expensive way to get "
        "heat. What correction is required?",
      choices=[
        "The framework says biomass produces heat at a relatively low cost",
        "The framework says biomass produces heat at a relatively high cost, so the student is "
        "correct",
        "The framework makes no claim about the cost of heat from biomass",
        "The framework says biomass produces electricity rather than heat",
        "The framework says biomass produces heat at no cost at all"],
      ans=0,
      why="ENG-3.I.1 states that burning biomass produces heat for energy AT A RELATIVELY LOW "
          "COST. The word relatively keeps it a comparison rather than a claim of free heat, and "
          "the statement is about heat rather than electricity."),

 dict(q="A third student writes that burning ethanol puts no carbon at all into the atmosphere. "
        "What correction does the framework require?",
      choices=[
        "The claim is narrower: burning ethanol introduces no ADDITIONAL carbon by way of the "
        "combustion itself",
        "The claim is broader: ethanol removes carbon from the atmosphere when it burns",
        "The claim is reversed: burning ethanol introduces more carbon than gasoline does",
        "The framework makes no claim about ethanol and carbon",
        "No correction is needed, since ethanol contains no carbon"],
      ans=0,
      why="ENG-3.I.2 says burning ethanol DOES NOT INTRODUCE ADDITIONAL CARBON INTO THE ATMOSPHERE "
          "VIA COMBUSTION, which is a claim about what the combustion adds rather than a claim "
          "that ethanol is carbon free. Reading the hedge away overstates what the framework "
          "says."),

 dict(q="A village heated by bottled gas proposes gathering wood locally instead. Which pair of "
        "considerations does the framework put on the two sides of that decision?",
      choices=[
        "Cheaper heat on one side; five named emissions and the risk of deforestation on the "
        "other",
        "Cheaper heat on one side; a low energy return on energy investment on the other",
        "Cleaner air on one side; a higher cost of fuel on the other",
        "No emissions on one side; the loss of habitat behind a dam on the other",
        "A renewable classification on one side; a nonrenewable one on the other"],
      ans=0,
      why="ENG-3.I.1 supplies both sides for burning biomass: heat at a relatively low cost, but "
          "carbon dioxide, carbon monoxide, nitrogen oxides, particulates and volatile organic "
          "compounds, and deforestation where the trees are overharvested. The low energy return "
          "belongs to ethanol, and habitat loss behind a dam to hydroelectric power in topic 6.9."),

 dict(q="A government proposes replacing part of its gasoline supply with ethanol. Which pair of "
        "considerations does the framework put on the two sides of that decision?",
      choices=[
        "No additional carbon from the combustion on one side; a low energy return on energy "
        "investment on the other",
        "No additional carbon from the combustion on one side; the release of hydrogen sulfide "
        "on the other",
        "A high energy return on energy investment on one side; additional carbon from the "
        "combustion on the other",
        "Cheaper heat for households on one side; deforestation on the other",
        "The framework offers nothing to weigh on either side for ethanol"],
      ans=0,
      why="ENG-3.I.2 supplies both sides for ethanol: it substitutes for gasoline and its "
          "combustion introduces no additional carbon, but its energy return on energy investment "
          "is low. Hydrogen sulfide belongs to geothermal energy and the cheap heat and "
          "deforestation pair belongs to burning biomass."),

 dict(q="Which observation would most directly report the deforestation claim the framework "
        "makes?",
      choices=[
        "Measuring the forest area where wood is being cut for fuel faster than it regrows",
        "Measuring the carbon monoxide in the smoke from a wood stove",
        "Measuring the energy delivered by ethanol against the energy invested in making it",
        "Measuring the price of firewood against the price of bottled gas",
        "Counting the households in a district that own a wood stove"],
      ans=0,
      why="ENG-3.I.1 attaches deforestation to the OVERHARVESTING of trees for fuel, so the "
          "observation must compare what is taken with what grows back and watch the forest area. "
          "Smoke composition, energy return, price and stove counts each bear on a different part "
          "of this topic."),

 dict(q="Which observation would most directly report the framework's reservation about ethanol?",
      choices=[
        "Measuring the energy the ethanol delivers against the energy invested in producing it",
        "Measuring the carbon dioxide released when the ethanol is burned",
        "Measuring the price of ethanol at the pump against the price of gasoline",
        "Measuring the area of farmland given over to the crop",
        "Measuring the particulates released when biomass is burned for heat"],
      ans=0,
      why="ENG-3.I.2's reservation is that the ENERGY RETURN ON ENERGY INVESTMENT for ethanol is "
          "low, which is a ratio of energy out to energy in. Carbon released, price, farmland and "
          "particulates each belong to a different claim or to a different statement."),

 dict(q="Does the framework classify biomass as a renewable or a nonrenewable energy source in "
        "this topic?",
      choices=[
        "It does neither; the statements here describe effects rather than assigning a class",
        "It calls biomass a renewable source",
        "It calls biomass a nonrenewable source",
        "It classifies biomass as renewable wherever the trees are replanted",
        "It classifies biomass as nonrenewable wherever the trees are overharvested"],
      ans=0,
      why="ENG-3.I.1 and ENG-3.I.2 describe what burning biomass and ethanol produce and cost, and "
          "neither assigns a class. The framework does label nuclear power nonrenewable in "
          "ENG-3.G.4 and wind renewable in ENG-3.S.1, which shows it labels a source where it "
          "means to."),

 dict(q="Which of the two statements in this topic bears on a household choosing a heating fuel, "
        "and which on a country choosing a transport fuel?",
      choices=[
        "The statement about burning biomass bears on the heating choice; the statement about "
        "ethanol bears on the transport choice",
        "The statement about ethanol bears on the heating choice; the statement about burning "
        "biomass bears on the transport choice",
        "Both statements bear only on the heating choice",
        "Both statements bear only on the transport choice",
        "Neither statement bears on a choice of fuel at all"],
      ans=0,
      why="ENG-3.I.1 is about burning biomass for heat and the emissions and deforestation that "
          "follow, while ENG-3.I.2 makes ethanol a substitute for gasoline, which is a transport "
          "fuel. Each statement is addressed to a different decision."),

 dict(q="The gases and particles leaving a biomass furnace were measured. Which conclusion "
        "matches the framework's statement?",
      table=_T_EMIT,
      choices=[
        "All five of the substances the framework names are present, with carbon dioxide much "
        "the largest by mass",
        "Only carbon dioxide is present, as the framework says",
        "None of the substances the framework names is present in the record",
        "Volatile organic compounds are much the largest by mass",
        "The five substances are released in equal amounts"],
      ans=0,
      why="The record carries 105 grams of carbon dioxide and 4.2, 0.9, 1.6 and 0.5 grams of the "
          "other four for each unit of energy, so every substance ENG-3.I.1 names appears and "
          "carbon dioxide dominates the mass."),

 dict(q="Using the same measurements, how much of the four substances other than carbon dioxide "
        "is released for each unit of energy?",
      table=_T_EMIT,
      choices=[
        "7.2 grams",
        "105 grams",
        "112.2 grams",
        "4.2 grams",
        "6.7 grams"],
      ans=0,
      why="Adding the four tabulated amounts gives 4.2 plus 0.9 plus 1.6 plus 0.5, which is 7.2 "
          "grams. The rejected values quote carbon dioxide alone, add all five, quote the largest "
          "of the four, or drop one of them from the sum."),

 dict(q="Using the same measurements, which substance is released in the smallest amount, and "
        "does its small size take it off the framework's list?",
      table=_T_EMIT,
      choices=[
        "Volatile organic compounds, and no, the framework names them whatever the amount",
        "Volatile organic compounds, and yes, the framework names only the largest emissions",
        "Nitrogen oxides, and no, the framework names them whatever the amount",
        "Carbon monoxide, and yes, the framework names only the largest emissions",
        "Carbon dioxide, and no, the framework names it whatever the amount"],
      ans=0,
      why="Volatile organic compounds come in at 0.5 grams for each unit of energy, the smallest "
          "of the five, and ENG-3.I.1 lists them alongside the others without any threshold of "
          "size. A list of named products is not a ranking."),

 dict(q="Three fuels a household might use for heat were priced. Which of the framework's claims "
        "do the values illustrate?",
      table=_T_COST,
      choices=[
        "That burning biomass produces heat for energy at a relatively low cost",
        "That burning biomass produces heat for energy at a relatively high cost",
        "That burning biomass produces no emissions",
        "That the energy return on energy investment for ethanol is low",
        "That overharvesting trees for fuel causes deforestation"],
      ans=0,
      why="Biomass gathered locally costs 1 currency unit for each unit of energy against 6 for "
          "bottled gas and 9 for grid electricity. ENG-3.I.1 states that burning biomass produces "
          "heat for energy AT A RELATIVELY LOW COST, and relatively is exactly what a comparison "
          "like this establishes."),

 dict(q="Using the same three fuels, how many times as much does a unit of energy from the grid "
        "cost as the same unit from locally gathered biomass?",
      table=_T_COST,
      choices=[
        "Nine times as much",
        "Six times as much",
        "Three times as much",
        "Fifteen times as much",
        "The two cost the same"],
      ans=0,
      why="Dividing the two tabulated prices gives 9 divided by 1, which is 9. The rejected values "
          "quote the middle fuel, take the gap between the two dearer fuels, add the prices, or "
          "deny that they differ."),

 dict(q="A district's use of wood for fuel was recorded across three decades. In which decade did "
        "the cutting first exceed the regrowth?",
      table=_T_FOREST,
      choices=[
        "The second decade, when 90 thousand tonnes were cut against 55 regrowing",
        "The first decade, when 40 thousand tonnes were cut against 55 regrowing",
        "The third decade, when 150 thousand tonnes were cut against 55 regrowing",
        "None of them, since the regrowth exceeded the cutting throughout",
        "All three, since the cutting exceeded the regrowth from the start"],
      ans=0,
      why="Cutting runs 40, 90 and 150 thousand tonnes a year against a steady 55 regrowing, so "
          "the first decade is within the regrowth and the second is the first that is not. "
          "ENG-3.I.1 attaches deforestation to OVERHARVESTING, which is precisely cutting beyond "
          "what grows back."),

 dict(q="Using the same record, which of the framework's claims do the forest area values "
        "support?",
      table=_T_FOREST,
      choices=[
        "That the overharvesting of trees for fuel causes deforestation",
        "That the overharvesting of trees for fuel has no effect on forest area",
        "That burning biomass produces heat at a relatively low cost",
        "That burning ethanol introduces no additional carbon by way of the combustion",
        "That the energy return on energy investment for ethanol is low"],
      ans=0,
      why="Forest area falls from 900 to 760 to 520 thousand hectares over the same decades in "
          "which cutting rises past the steady regrowth. ENG-3.I.1 states that the overharvesting "
          "of trees for fuel causes deforestation, and the two columns move exactly as that "
          "claim requires."),

 dict(q="Using the same record, how much forest area was lost across the three decades?",
      table=_T_FOREST,
      choices=[
        "380 thousand hectares",
        "140 thousand hectares",
        "240 thousand hectares",
        "520 thousand hectares",
        "1,420 thousand hectares"],
      ans=0,
      why="Subtracting the two tabulated areas gives 900 minus 520, which is 380 thousand "
          "hectares. The rejected values take one of the two decade-to-decade steps, quote the "
          "area remaining, or add the three readings together."),

 dict(q="Ethanol and gasoline were compared on the energy each delivers and the energy invested "
        "in producing it. What is the energy return on energy investment for the ethanol?",
      table=_T_RETURN,
      choices=[
        "1.5 units of energy delivered for each unit invested",
        "150 units of energy delivered for each unit invested",
        "100 units of energy delivered for each unit invested",
        "0.67 units of energy delivered for each unit invested",
        "12 units of energy delivered for each unit invested"],
      ans=0,
      why="Dividing the two tabulated values gives 150 delivered over 100 invested, which is 1.5. "
          "The rejected values quote one column alone, invert the ratio, or give the figure for "
          "the other fuel in the record."),

 dict(q="Using the same comparison, how does the gasoline's return stand against the ethanol's?",
      table=_T_RETURN,
      choices=[
        "Eight times as large",
        "Two times as large",
        "Twelve times as large",
        "Eighty times as large",
        "Smaller than the ethanol's"],
      ans=0,
      why="Gasoline delivers 1,200 for 100 invested, a return of 12, against ethanol's 1.5, and 12 "
          "divided by 1.5 is 8. The rejected values quote the gasoline return itself, shift by a "
          "power of ten, or invert the comparison the record shows."),

 dict(q="Which of the framework's claims does that comparison bear out?",
      table=_T_RETURN,
      choices=[
        "That the energy return on energy investment for ethanol is low",
        "That the energy return on energy investment for ethanol is high",
        "That ethanol cannot be used as a substitute for gasoline",
        "That burning ethanol introduces additional carbon into the atmosphere",
        "That the overharvesting of trees for fuel causes deforestation"],
      ans=0,
      why="Ethanol returns 1.5 units of energy for each unit invested against gasoline's 12, so "
          "the ratio is low in exactly the comparative sense ENG-3.I.2 uses when it calls the "
          "energy return on energy investment for ethanol low. The record says nothing about "
          "substitution, carbon or forests."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Burning biomass gives heat cheaply but releases carbon dioxide, carbon monoxide, "
        "nitrogen oxides, particulates and volatile organic compounds, and overharvesting trees "
        "for fuel causes deforestation; ethanol can replace gasoline and its combustion adds no "
        "additional carbon, but its energy return on energy investment is low.",
        "Burning biomass gives heat cheaply and releases nothing, and ethanol replaces gasoline "
        "with a high energy return on energy investment.",
        "Burning biomass is expensive and releases sulfur dioxide, and ethanol cannot be used in "
        "place of gasoline.",
        "Burning biomass releases five substances and nothing else is said about it, and the "
        "framework makes no claim about ethanol.",
        "Biomass is a renewable energy source and ethanol is a nonrenewable one, which is what "
        "this topic establishes."],
      ans=0,
      why="The keyed summary carries ENG-3.I.1 and ENG-3.I.2 whole, including the deforestation "
          "clause and both halves of each trade-off. Each rejected summary drops the emissions, "
          "inverts the cost or the energy return, adds sulfur dioxide to a list that does not "
          "carry it, or assigns classes the framework never assigns to either fuel."),
]
