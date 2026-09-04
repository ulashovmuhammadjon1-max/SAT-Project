# AP ENVIRONMENTAL SCIENCE 6.11 Hydrogen Fuel Cell
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objectives ENG-3.P, describe the use of hydrogen fuel cells in power generation;
# and ENG-3.Q, describe the effects of the use of hydrogen fuel cells in power generation on
# the environment.
# Suggested skill 1.C, explain environmental concepts, processes, or models in applied
# contexts -- which is why several items put a fuel cell to a real decision.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.P.1  Hydrogen fuel cells are an alternate to non-renewable fuel sources. They use
#              hydrogen as fuel, combining the hydrogen and oxygen in the air to form water
#              and release energy (electricity) in the process. Water is the product
#              (emission) of a fuel cell.
#   ENG-3.Q.1  Hydrogen fuel cells have low environmental impact and produce no carbon
#              dioxide when the hydrogen is produced from water. However, the technology is
#              expensive and energy is still needed to create the hydrogen gas used in the
#              fuel cell.
#
# THE CARBON DIOXIDE CLAIM IS CONDITIONAL, and that condition is the single most important
# thing in this topic. ENG-3.Q.1 says fuel cells produce NO CARBON DIOXIDE WHEN THE HYDROGEN
# IS PRODUCED FROM WATER. It does not say a fuel cell never produces carbon dioxide, and it
# does not say anything about hydrogen made another way. Three items key the condition and
# every anchor on the claim carries it, because the distractor that drops it is the one a
# prepared student reaches for.
#
# HYDROGEN IS NOT CLASSIFIED RENEWABLE. ENG-3.P.1 calls a fuel cell AN ALTERNATE TO
# NON-RENEWABLE FUEL SOURCES, which says what it is an alternative to and not what it is.
# The framework labels nuclear power nonrenewable (ENG-3.G.4) and wind renewable
# (ENG-3.S.1) and gives hydrogen no label at all. One item keys that absence, and this
# matches the boundary already recorded in e6_1.py, where hydrogen is deliberately left out
# of the classification items.
#
# WATER IS THE PRODUCT, AND THE FRAMEWORK SAYS SO TWICE -- once in the description of the
# reaction and once as the emission. Two items key it, and the fossil fuel comparison item
# turns on ENG-3.E.1 yielding carbon dioxide AND water where a fuel cell yields water alone.
#
# TWO RESERVATIONS, AND THE SECOND IS THE SUBTLE ONE. The technology is expensive, and
# ENERGY IS STILL NEEDED TO CREATE THE HYDROGEN GAS. The hydrogen has to be made before it
# can be used, so a fuel cell is not a source of energy in the way a coal seam is. Four
# items and a whole table turn on that.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_11.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.11", "Hydrogen Fuel Cell", 6)

_T_CELL = dict(
    headers=["Substance measured at the fuel cell",
             "Amount entering the cell each hour (units)",
             "Amount leaving the cell each hour (units)"],
    rows=[["Hydrogen", "4", "0"],
          ["Oxygen taken from the air", "2", "0"],
          ["Water", "0", "4"],
          ["Carbon dioxide", "0", "0"]])

_T_SOURCE = dict(
    headers=["Way the hydrogen is produced",
             "Energy invested to make one unit of hydrogen (energy units)",
             "Carbon dioxide released in making one unit of hydrogen (kilograms)"],
    rows=[["Produced from water", "55", "0"],
          ["Produced from a fossil fuel", "40", "28"]])

_T_FLEET = dict(
    headers=["Way of powering a delivery fleet",
             "Cost of the equipment for each vehicle (thousand currency units)",
             "Carbon dioxide released for each unit of distance (kilograms)"],
    rows=[["Hydrogen fuel cell, hydrogen produced from water", "72", "0"],
          ["Gasoline engine", "24", "0.9"]])

_T_CHAIN = dict(
    headers=["Step in the hydrogen chain",
             "Energy involved at that step (energy units)"],
    rows=[["Energy invested to create the hydrogen gas", "100"],
          ["Electricity the fuel cell delivers from that hydrogen", "62"]])

QUESTIONS = [

 dict(q="What does the framework call hydrogen fuel cells?",
      choices=[
        "An alternate to non-renewable fuel sources",
        "A non-renewable fuel source in their own right",
        "The most widely used source of energy globally",
        "A form of nuclear power generation",
        "A kind of passive solar energy system"],
      ans=0,
      why="ENG-3.P.1 opens by stating that HYDROGEN FUEL CELLS ARE AN ALTERNATE TO NON-RENEWABLE "
          "FUEL SOURCES. The most widely used sources globally are fossil fuels in ENG-3.B.2, and "
          "nuclear power and passive solar systems are treated in topics 6.6 and 6.8."),

 dict(q="Does the framework classify hydrogen itself as a renewable energy source?",
      choices=[
        "No; it says only what a fuel cell is an alternative to, and gives hydrogen no class",
        "Yes; it calls hydrogen a renewable energy source",
        "Yes; it calls hydrogen renewable so long as the hydrogen comes from water",
        "No; it calls hydrogen a nonrenewable energy source",
        "No; it says hydrogen cannot be used as a fuel at all"],
      ans=0,
      why="ENG-3.P.1 calls a fuel cell AN ALTERNATE TO NON-RENEWABLE FUEL SOURCES, which says what "
          "it stands beside rather than what it is. The framework labels nuclear power "
          "nonrenewable in ENG-3.G.4 and wind renewable in ENG-3.S.1, so it labels a source where "
          "it means to, and it plainly does treat hydrogen as a fuel."),

 dict(q="What does the framework say a hydrogen fuel cell uses as its fuel?",
      choices=[
        "Hydrogen",
        "Methane drawn from a natural gas supply",
        "Ethanol made from a crop",
        "Uranium-235 held in fuel rods",
        "Water, which the cell then splits"],
      ans=0,
      why="ENG-3.P.1 states that fuel cells USE HYDROGEN AS FUEL. Water is the product of the cell "
          "rather than its fuel, and methane, ethanol and Uranium-235 belong to topics 6.3, 6.7 "
          "and 6.6."),

 dict(q="What does the framework say the hydrogen is combined with inside the cell?",
      choices=[
        "Oxygen taken from the air",
        "Nitrogen taken from the air",
        "Carbon dioxide taken from the air",
        "More hydrogen, which is joined into heavier atoms",
        "Steam raised in a separate boiler"],
      ans=0,
      why="ENG-3.P.1 states that the cell combines THE HYDROGEN AND OXYGEN IN THE AIR. Joining "
          "atoms into heavier ones is fusion, which the framework never describes, and no boiler "
          "appears anywhere in this topic."),

 dict(q="What does the framework say that combination forms and releases?",
      choices=[
        "It forms water and releases energy in the form of electricity",
        "It forms carbon dioxide and releases energy in the form of heat",
        "It forms water and releases energy that must then drive a turbine",
        "It forms hydrogen peroxide and releases no energy",
        "It forms steam that is used to spin a generator"],
      ans=0,
      why="ENG-3.P.1 states that the cell combines the hydrogen and oxygen TO FORM WATER AND "
          "RELEASE ENERGY, and puts ELECTRICITY in brackets beside that energy. No turbine, "
          "generator or boiler appears in the framework's account of a fuel cell."),

 dict(q="What does the framework name as the product, or emission, of a fuel cell?",
      choices=[
        "Water",
        "Carbon dioxide",
        "Hydrogen that has not reacted",
        "Nitrogen oxides",
        "Nothing at all leaves the cell"],
      ans=0,
      why="ENG-3.P.1 ends by stating that WATER IS THE PRODUCT, or emission, OF A FUEL CELL. The "
          "framework names it twice in the same statement, once in the reaction and once as the "
          "emission, so something does leave the cell."),

 dict(q="Which sequence matches the framework's account of what happens in a fuel cell?",
      choices=[
        "Hydrogen is supplied as fuel, it combines with oxygen from the air, water forms, and "
        "electricity is released in the process",
        "Water is supplied as fuel, it splits into hydrogen and oxygen, and electricity is "
        "released in the process",
        "Hydrogen is burned to raise steam, the steam spins a turbine, and the turbine spins a "
        "generator",
        "Hydrogen combines with carbon dioxide from the air, and heat is released in the "
        "process",
        "Hydrogen atoms are joined into heavier atoms, and a large amount of heat is released"],
      ans=0,
      why="ENG-3.P.1 gives the whole account in one sentence: hydrogen as fuel, combined with "
          "oxygen in the air, forming water and releasing energy as electricity. Water is the "
          "product rather than the input, no steam or turbine appears, and joining atoms is "
          "fusion, which the framework never describes."),

 dict(q="What does the framework say about the environmental impact of hydrogen fuel cells?",
      choices=[
        "That it is low",
        "That it is high",
        "That the impact is low only where the technology is cheap",
        "That it is the same as that of a coal plant",
        "The framework makes no claim about their environmental impact"],
      ans=0,
      why="ENG-3.Q.1 opens by stating that HYDROGEN FUEL CELLS HAVE LOW ENVIRONMENTAL IMPACT. The "
          "same statement goes on to name two reservations, so low is not the same as none, and "
          "the claim is made rather than withheld."),

 dict(q="Under what condition does the framework say a fuel cell produces no carbon dioxide?",
      choices=[
        "When the hydrogen is produced from water",
        "Under every condition, whatever the hydrogen is made from",
        "When the technology is inexpensive",
        "When the oxygen is taken from the air rather than from a tank",
        "When the fuel cell is used in a vehicle rather than in a building"],
      ans=0,
      why="ENG-3.Q.1 states that fuel cells PRODUCE NO CARBON DIOXIDE WHEN THE HYDROGEN IS "
          "PRODUCED FROM WATER. The condition is part of the claim, and the statement attaches no "
          "condition about cost, about where the oxygen comes from, or about the use the cell is "
          "put to."),

 dict(q="A student writes that a hydrogen fuel cell can never produce carbon dioxide, whatever "
        "the source of its hydrogen. What correction does the framework require?",
      choices=[
        "The framework's claim holds when the hydrogen is produced from water, and it says "
        "nothing about hydrogen made another way",
        "The framework's claim holds whatever the source of the hydrogen, so the student is "
        "correct",
        "The framework says a fuel cell always produces carbon dioxide",
        "The framework says a fuel cell produces carbon dioxide only when the hydrogen comes "
        "from water",
        "The framework makes no claim about fuel cells and carbon dioxide"],
      ans=0,
      why="ENG-3.Q.1 attaches the words WHEN THE HYDROGEN IS PRODUCED FROM WATER to the carbon "
          "dioxide claim. Dropping the condition states more than the framework does, and "
          "reversing it states the opposite; the framework certainly does make the claim."),

 dict(q="Which two reservations does the framework attach to hydrogen fuel cells?",
      choices=[
        "That the technology is expensive, and that energy is still needed to create the "
        "hydrogen gas",
        "That the technology is expensive, and that the cell releases hydrogen sulfide",
        "That the technology is cheap, and that energy is still needed to create the hydrogen "
        "gas",
        "That the cell releases carbon monoxide, and that it produces hazardous solid waste",
        "The framework attaches no reservations to hydrogen fuel cells"],
      ans=0,
      why="ENG-3.Q.1 states that HOWEVER, THE TECHNOLOGY IS EXPENSIVE AND ENERGY IS STILL NEEDED "
          "TO CREATE THE HYDROGEN GAS USED IN THE FUEL CELL. Hydrogen sulfide belongs to "
          "geothermal energy in topic 6.10, carbon monoxide to burning biomass in 6.7, and "
          "hazardous solid waste to nuclear power in 6.6."),

 dict(q="What does the framework's second reservation establish about where the hydrogen comes "
        "from?",
      choices=[
        "That the hydrogen gas has to be made before it can be used, and making it takes energy",
        "That the hydrogen gas is mined from the ground like a fossil fuel",
        "That the hydrogen gas is produced inside the cell from the air",
        "That the hydrogen gas is produced by the cell as a by-product",
        "That the hydrogen gas requires no energy to obtain"],
      ans=0,
      why="ENG-3.Q.1 says ENERGY IS STILL NEEDED TO CREATE THE HYDROGEN GAS USED IN THE FUEL CELL, "
          "so the fuel is manufactured rather than found, and the manufacture is itself a call on "
          "energy. Nothing in this topic has the cell making its own fuel."),

 dict(q="A second student writes that the emission of a hydrogen fuel cell is carbon dioxide. "
        "What correction does the framework require?",
      choices=[
        "Water is the product, or emission, of a fuel cell",
        "Carbon monoxide is the product, or emission, of a fuel cell",
        "Hydrogen that has not reacted is the emission of a fuel cell",
        "The framework names no emission for a fuel cell",
        "Carbon dioxide is the emission, so the student is correct"],
      ans=0,
      why="ENG-3.P.1 states in so many words that WATER IS THE PRODUCT, or emission, OF A FUEL "
          "CELL, and names water twice, once in the reaction and once as the emission. Carbon "
          "monoxide belongs to burning biomass in topic 6.7."),

 dict(q="How does the product of a fuel cell differ from the products of burning a fossil fuel, "
        "in the framework's accounts?",
      choices=[
        "Burning a fossil fuel yields carbon dioxide and water; a fuel cell yields water alone",
        "Burning a fossil fuel yields water alone; a fuel cell yields carbon dioxide and water",
        "Both yield carbon dioxide and water, and only the amounts differ",
        "Both yield water alone, and only the rate differs",
        "The framework names no products for either of them"],
      ans=0,
      why="ENG-3.E.1 states that the combustion of fossil fuels YIELDS CARBON DIOXIDE AND WATER, "
          "while ENG-3.P.1 names WATER as the product of a fuel cell. One rejected option is the "
          "exact swap of those two, and both statements plainly name products."),

 dict(q="A city considering a hydrogen fuel cell fleet asks what advantage it may honestly claim. "
        "What does the framework license?",
      choices=[
        "Low environmental impact, and no carbon dioxide provided the hydrogen is produced from "
        "water",
        "Low environmental impact, and no carbon dioxide whatever the hydrogen is made from",
        "Low environmental impact, and a lower cost than any other technology",
        "No environmental impact of any kind, and no energy required to obtain the fuel",
        "No advantage at all, since the framework names none for fuel cells"],
      ans=0,
      why="ENG-3.Q.1 grants LOW ENVIRONMENTAL IMPACT and no carbon dioxide WHEN THE HYDROGEN IS "
          "PRODUCED FROM WATER, and in the same breath calls the technology expensive and notes "
          "that energy is still needed to make the hydrogen. Dropping the condition or the cost "
          "overstates the case."),

 dict(q="Which costs must that same city weigh, on the framework's account?",
      choices=[
        "That the technology is expensive, and that making the hydrogen gas itself takes energy",
        "That the technology is expensive, and that the cell emits carbon monoxide",
        "That the technology is cheap, but that the cell emits carbon dioxide",
        "That the fleet will release hydrogen sulfide into the air around the depot",
        "That the framework names no costs, so none need be weighed"],
      ans=0,
      why="ENG-3.Q.1's two reservations are the expense of the technology and the energy still "
          "needed to create the hydrogen gas. Carbon monoxide belongs to burning biomass in topic "
          "6.7 and hydrogen sulfide to geothermal energy in 6.10."),

 dict(q="Which observation would most directly report the framework's second reservation?",
      choices=[
        "Measuring the energy spent producing a quantity of hydrogen and setting it beside the "
        "electricity that hydrogen later yields",
        "Measuring the water leaving a fuel cell over an hour",
        "Measuring the oxygen a fuel cell draws from the air",
        "Recording the number of fuel cell vehicles registered in a city",
        "Measuring the carbon dioxide released by a gasoline engine"],
      ans=0,
      why="ENG-3.Q.1 says ENERGY IS STILL NEEDED TO CREATE THE HYDROGEN GAS, which is a claim "
          "about energy spent before the cell is used, so it is tested by comparing that "
          "investment with what comes back. Water and oxygen at the cell bear on ENG-3.P.1 "
          "instead."),

 dict(q="Which observation would most directly report the framework's carbon dioxide claim, and "
        "what must be recorded alongside it?",
      choices=[
        "The carbon dioxide released across the whole chain, recorded together with how the "
        "hydrogen was produced",
        "The carbon dioxide released at the cell alone, with no record of how the hydrogen was "
        "produced",
        "The water leaving the cell, recorded together with how the hydrogen was produced",
        "The cost of the equipment, recorded together with how the hydrogen was produced",
        "The oxygen entering the cell, with no other record needed"],
      ans=0,
      why="ENG-3.Q.1 conditions its claim on the hydrogen being PRODUCED FROM WATER, so the source "
          "of the hydrogen is part of what the claim is about and has to be recorded with the "
          "carbon dioxide. Water, cost and oxygen bear on other parts of this topic."),

 dict(q="The substances entering and leaving a working fuel cell were measured. Which conclusion "
        "matches the framework's account?",
      table=_T_CELL,
      choices=[
        "Hydrogen and oxygen enter, water leaves, and no carbon dioxide is involved on either "
        "side",
        "Water enters and hydrogen and oxygen leave, which is the reaction the framework "
        "describes",
        "Carbon dioxide leaves the cell alongside the water",
        "Hydrogen enters and leaves unchanged, and only oxygen is consumed",
        "Nothing enters or leaves the cell in the record"],
      ans=0,
      why="Hydrogen enters at 4 units an hour and oxygen at 2, water leaves at 4, and the carbon "
          "dioxide row reads zero on both sides. ENG-3.P.1 has the cell combining hydrogen and "
          "oxygen from the air to form water and release electricity."),

 dict(q="Using the same measurements, which substance is the product the framework names?",
      table=_T_CELL,
      choices=[
        "Water, the only substance leaving the cell",
        "Hydrogen, the substance entering in the largest amount",
        "Oxygen, the substance taken from the air",
        "Carbon dioxide, which the record shows leaving the cell",
        "There is no product, since nothing leaves the cell"],
      ans=0,
      why="Water is the only row with a figure above zero in the leaving column, at 4 units an "
          "hour. ENG-3.P.1 states that WATER IS THE PRODUCT, or emission, OF A FUEL CELL, and the "
          "hydrogen and oxygen are what enter rather than what leaves."),

 dict(q="Using the same measurements, how much water leaves the cell for every unit of hydrogen "
        "that enters it?",
      table=_T_CELL,
      choices=[
        "One unit of water for each unit of hydrogen",
        "Two units of water for each unit of hydrogen",
        "Half a unit of water for each unit of hydrogen",
        "Four units of water for each unit of hydrogen",
        "No water leaves the cell at all"],
      ans=0,
      why="Four units of hydrogen enter each hour and four units of water leave, so the ratio is "
          "one to one. The rejected values take the oxygen row for the hydrogen row, invert the "
          "ratio, quote a whole hour's output as a ratio, or deny an output the record shows."),

 dict(q="Two ways of producing the hydrogen were compared. Which conclusion matches the "
        "framework's claim about carbon dioxide?",
      table=_T_SOURCE,
      choices=[
        "No carbon dioxide is released where the hydrogen is produced from water, which is the "
        "condition the framework attaches to its claim",
        "No carbon dioxide is released whichever way the hydrogen is produced, so the framework "
        "attaches no condition",
        "No carbon dioxide is released where the hydrogen is produced from a fossil fuel, which "
        "is the condition the framework attaches",
        "Carbon dioxide is released both ways, so the framework's claim does not hold",
        "The record says nothing about carbon dioxide"],
      ans=0,
      why="Producing the hydrogen from water releases 0 kilograms of carbon dioxide for each unit "
          "while producing it from a fossil fuel releases 28. ENG-3.Q.1 makes its claim WHEN THE "
          "HYDROGEN IS PRODUCED FROM WATER, and the record shows why that condition is in the "
          "statement."),

 dict(q="Using the same two ways of producing hydrogen, which of the framework's reservations do "
        "the energy investments illustrate?",
      table=_T_SOURCE,
      choices=[
        "That energy is still needed to create the hydrogen gas, whichever way it is produced",
        "That energy is needed only where the hydrogen is produced from a fossil fuel",
        "That energy is needed only where the hydrogen is produced from water",
        "That no energy at all is needed to create the hydrogen gas",
        "That the technology of the fuel cell itself is expensive"],
      ans=0,
      why="Both routes carry an energy investment, 55 energy units for each unit of hydrogen from "
          "water and 40 from a fossil fuel. ENG-3.Q.1 states that ENERGY IS STILL NEEDED TO CREATE "
          "THE HYDROGEN GAS, without exempting either route."),

 dict(q="Using the same two ways of producing hydrogen, how much more energy does the route from "
        "water require for each unit of hydrogen?",
      table=_T_SOURCE,
      choices=[
        "15 energy units",
        "40 energy units",
        "95 energy units",
        "55 energy units",
        "The route from water requires less energy"],
      ans=0,
      why="Subtracting the two tabulated investments gives 55 minus 40, which is 15 energy units. "
          "The rejected values quote one route alone, add the two, or invert the comparison the "
          "record shows."),

 dict(q="Two ways of powering a delivery fleet were compared. Which conclusion matches the "
        "framework's statement about fuel cells?",
      table=_T_FLEET,
      choices=[
        "The fuel cell fleet releases no carbon dioxide with hydrogen from water, but its "
        "equipment costs the more",
        "The fuel cell fleet releases no carbon dioxide with hydrogen from water, and its "
        "equipment costs the less",
        "The fuel cell fleet releases more carbon dioxide than the gasoline fleet, and its "
        "equipment costs the more",
        "The gasoline fleet releases no carbon dioxide, but its equipment costs the more",
        "The two fleets release the same carbon dioxide and cost the same to equip"],
      ans=0,
      why="The fuel cell fleet shows 0 kilograms of carbon dioxide for each unit of distance "
          "against the gasoline fleet's 0.9, and equipment at 72 thousand currency units for each "
          "vehicle against 24. ENG-3.Q.1 grants the absence of carbon dioxide when the hydrogen "
          "comes from water and calls the technology expensive in the same statement."),

 dict(q="Using the same two fleets, how many times as much does the fuel cell equipment cost for "
        "each vehicle?",
      table=_T_FLEET,
      choices=[
        "Three times as much",
        "Two times as much",
        "Four times as much",
        "Thirty times as much",
        "The fuel cell equipment costs the less of the two"],
      ans=0,
      why="Dividing the two tabulated costs gives 72 divided by 24, which is 3. The rejected "
          "values quote a wrong division, shift the answer by a power of ten, or invert the "
          "comparison the record shows."),

 dict(q="The energy put into making a quantity of hydrogen was set beside the electricity the "
        "fuel cell later delivered from it. Which of the framework's reservations do the values "
        "illustrate?",
      table=_T_CHAIN,
      choices=[
        "That energy is still needed to create the hydrogen gas used in the fuel cell",
        "That the technology of the fuel cell is expensive to buy",
        "That the fuel cell produces no carbon dioxide when the hydrogen comes from water",
        "That water is the product, or emission, of a fuel cell",
        "That hydrogen fuel cells have low environmental impact"],
      ans=0,
      why="A hundred energy units go into creating the hydrogen and 62 come back as electricity, "
          "so the fuel had to be made before it could be used and the making was itself a call on "
          "energy. ENG-3.Q.1 states that ENERGY IS STILL NEEDED TO CREATE THE HYDROGEN GAS USED IN "
          "THE FUEL CELL."),

 dict(q="Using the same chain, what share of the energy invested comes back as electricity?",
      table=_T_CHAIN,
      choices=[
        "62 percent",
        "38 percent",
        "100 percent",
        "31 percent",
        "More than was invested, since the cell adds energy of its own"],
      ans=0,
      why="Dividing the two tabulated values gives 62 out of 100 energy units, which is 62 "
          "percent. The rejected values take the share lost rather than the share returned, assume "
          "nothing is lost, halve the answer, or claim a return the record does not show."),

 dict(q="Using the same chain, how much of the energy invested does not come back as electricity?",
      table=_T_CHAIN,
      choices=[
        "38 energy units",
        "62 energy units",
        "19 energy units",
        "100 energy units",
        "None of it, since all the energy comes back"],
      ans=0,
      why="Subtracting the two tabulated values gives 100 minus 62, which is 38 energy units. The "
          "rejected values quote the electricity delivered, halve the answer, quote the "
          "investment, or deny a shortfall the record plainly shows."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Fuel cells are an alternate to non-renewable fuel sources; they use hydrogen as fuel, "
        "combining it with oxygen from the air to form water and release electricity, and water "
        "is the emission; they have low environmental impact and produce no carbon dioxide when "
        "the hydrogen is produced from water, but the technology is expensive and energy is "
        "still needed to make the hydrogen.",
        "Fuel cells burn hydrogen to raise steam for a turbine, and their emission is carbon "
        "dioxide.",
        "Fuel cells produce no carbon dioxide whatever the hydrogen is made from, are cheap, "
        "and need no energy to obtain their fuel.",
        "Fuel cells are a renewable energy source that the framework classifies as such, and "
        "they emit nothing at all.",
        "Fuel cells combine hydrogen with nitrogen from the air, releasing heat, and the "
        "framework attaches no reservations to them."],
      ans=0,
      why="The keyed summary carries ENG-3.P.1 and ENG-3.Q.1 in the framework's own terms, "
          "including the condition on the carbon dioxide claim and both reservations. Each "
          "rejected summary introduces steam or a turbine, drops the condition, claims a class the "
          "framework never assigns, or names the wrong gas from the air."),
]
