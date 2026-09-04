# AP ENVIRONMENTAL SCIENCE 6.13 Energy Conservation
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objective ENG-3.T, describe methods for conserving energy.
# Suggested skill 6.C, calculate an accurate numeric answer with appropriate units --
# which is why thirteen items here carry a table and ask for a figure with its unit.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.T.1  Some of the methods for conserving energy around a home include adjusting
#              the thermostat to reduce the use of heat and air conditioning, conserving
#              water, use of energy-efficient appliances, and conservation landscaping.
#   ENG-3.T.2  Methods for conserving energy on a large scale include improving fuel
#              economy for vehicles, using BEVs (battery electric vehicles) and hybrid
#              vehicles, using public transportation, and implementing green building
#              design features.
#
# SCOPE, AND WHAT THIS TOPIC IS NOT. Two statements, two lists, eight named methods and
# NOT ONE NUMBER. The framework gives no saving, no cost, no ranking and no mechanism for
# any method except the thermostat, whose purpose clause it does supply -- TO REDUCE THE
# USE OF HEAT AND AIR CONDITIONING. So no key here says how much a method saves or which
# method saves the most. Where an item asks that, the answer comes from a table printed
# with the question and the claim says in so many words that the ranking is the record's
# and not the framework's.
#
# THE AXIS THIS TOPIC IS EASIEST TO GET WRONG IS SCALE. Four methods are AROUND A HOME
# and four are ON A LARGE SCALE, and two of the eight sit where a student does not expect
# them: CONSERVING WATER is an energy conservation method around a home, and GREEN
# BUILDING DESIGN FEATURES is on the large-scale list rather than the home one. Six items
# turn on which list a method is on, and where an option is the exact swap of the key the
# anchor carries both clauses.
#
# THE WORD THAT LIMITS BOTH LISTS, AND WHY NO ITEM ASKS ABOUT IT. ENG-3.T.1 opens SOME OF
# THE METHODS ... INCLUDE and ENG-3.T.2 says METHODS ... INCLUDE, so neither list is
# offered as complete. An item keying that hedge was drafted and CUT: e6_4 q5 and e9_9 q17
# already ask it of SUCH AS in their own statements, and a third near-copy of one shape is
# what the dedupe rule exists to stop. The property is instead enforced negatively -- no
# key anywhere in this module treats a method the framework does not name as ruled out.
# The item written in its place keys a fact peculiar to this topic: of the eight methods
# only the thermostat carries a stated purpose.
#
# CONSERVING IS NOT GENERATING. Neither statement names a single energy source: they name
# ways of using less of whatever energy is used. Two items hold that boundary, one against
# the sources of topics 6.3 to 6.12 generally and one against ENG-3.R.1's wind turbine,
# which PRODUCES ELECTRICITY and is therefore generation rather than conservation.
#
# BOUNDARY WITH 5.13. STB-1.B.1 also names increased use of public transportation, but
# there it is a method to INCREASE WATER INFILTRATION and it sits beside permeable
# pavement and tree planting. Here it is a method for CONSERVING ENERGY on a large scale.
# One item keys that a method can appear on two different lists for two different
# purposes, and permeable pavement is used as a distractor exactly once, where the
# question is about what ENG-3.T.1 names.
#
# BOUNDARY WITH 5.11, 6.1 AND 6.2. An ecological footprint compares resource demands with
# waste production (EIN-2.N.1) and no item here computes one. Whether a source is
# renewable is ENG-3.A in topic 6.1, and who uses how much energy is ENG-3.B in topic 6.2;
# neither is keyed here. This topic is about the methods, and about arithmetic done on
# records of them.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_13.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.13", "Energy Conservation", 6)

_T_HOME = dict(
    headers=["Part of one home's energy use, and the method trialled on it",
             "Energy that part used in the year before the method (energy units)",
             "Energy that part used in the year with the method (energy units)"],
    rows=[["Heating and air conditioning, thermostat adjusted", "4,000", "3,400"],
          ["Appliances, replaced with energy-efficient ones", "2,000", "1,600"],
          ["Heating and pumping water, water use reduced", "1,200", "1,080"],
          ["Grounds around the house, conservation landscaping", "800", "720"]])

_T_ECON = dict(
    headers=["Vehicle in a delivery fleet",
             "Distance travelled in the year (distance units)",
             "Fuel used in that year (fuel units)"],
    rows=[["Vehicle 1", "12,000", "600"],
          ["Vehicle 2", "12,000", "400"],
          ["Vehicle 3", "12,000", "300"],
          ["Vehicle 4", "12,000", "240"]])

_T_MODE = dict(
    headers=["Way of making the same journey",
             "Energy the journey uses in total (energy units)",
             "Passengers carried"],
    rows=[["One person driving a car alone", "60", "1"],
          ["A bus", "480", "40"],
          ["A train", "1,600", "200"]])

_T_BUILD = dict(
    headers=["Stage of the record for one office building",
             "Energy the building used in the year (thousand energy units)"],
    rows=[["Before the design features", "500"],
          ["First year after the design features", "410"],
          ["Second year after the design features", "400"]])

QUESTIONS = [

 dict(q="Which method for conserving energy around a home does the framework name?",
      choices=[
        "Adjusting the thermostat to reduce the use of heat and air conditioning",
        "Adjusting the thermostat to increase the use of heat and air conditioning",
        "Installing a larger air conditioning unit so that it runs for less of the day",
        "Opening the windows while the heating runs so that the air stays fresh",
        "Moving the thermostat nearer the heating unit so that it reads a higher "
        "temperature"],
      ans=0,
      why="ENG-3.T.1 names ADJUSTING THE THERMOSTAT TO REDUCE THE USE OF HEAT AND AIR "
          "CONDITIONING first among its home methods. Adjusting it the other way increases the "
          "use the statement asks to reduce, and no larger unit, open window or moved thermostat "
          "appears anywhere in the framework."),

 dict(q="What does the framework say adjusting the thermostat is meant to reduce?",
      choices=[
        "The use of heat and air conditioning",
        "The use of lighting through the evening",
        "The volume of hot water drawn for washing",
        "The fuel used by the household's vehicles",
        "The solid waste the household sends away"],
      ans=0,
      why="ENG-3.T.1 attaches a purpose to this one method and to no other: adjusting the "
          "thermostat TO REDUCE THE USE OF HEAT AND AIR CONDITIONING. Lighting and solid waste "
          "appear nowhere in the statement, and vehicle fuel belongs to the large-scale list in "
          "ENG-3.T.2."),

 dict(q="The framework names one home method that concerns water. Which is it?",
      choices=[
        "Conserving water",
        "Heating water with an electric immersion rather than with gas",
        "Collecting rainwater to drink",
        "Replacing traditional pavement with permeable pavement",
        "Treating wastewater before it leaves the home"],
      ans=0,
      why="ENG-3.T.1 lists CONSERVING WATER among the methods for conserving energy around a "
          "home, without explaining the link between the two. Permeable pavement is STB-1.B.1 in "
          "topic 5.13, a method to increase water infiltration rather than to conserve energy, "
          "and the other options appear nowhere in the framework."),

 dict(q="Which claim about appliances does the framework make?",
      choices=[
        "That using energy-efficient appliances is among the methods for conserving energy "
        "around a home",
        "That using energy-efficient appliances is among the methods for conserving energy on a "
        "large scale",
        "That appliances should be replaced every ten years whatever their efficiency",
        "That efficient appliances use more energy than older ones but last longer",
        "That the framework makes no claim about appliances"],
      ans=0,
      why="ENG-3.T.1 names USE OF ENERGY-EFFICIENT APPLIANCES among the home methods, and "
          "ENG-3.T.2's large-scale list names vehicles, public transportation and green building "
          "design instead. The framework sets no replacement interval and makes no claim that an "
          "efficient appliance uses more."),

 dict(q="What does the framework establish about conservation landscaping?",
      choices=[
        "That it is among the methods for conserving energy around a home, with no description "
        "of what it involves",
        "That it is among the methods for conserving energy on a large scale, with no "
        "description of what it involves",
        "That it means replacing lawn with native plants that need no watering",
        "That it means planting trees so that rainwater soaks into the ground",
        "That it saves more energy than any other method around a home"],
      ans=0,
      why="ENG-3.T.1 ends its home list with CONSERVATION LANDSCAPING and describes it no "
          "further, so a definition offered for it comes from outside the framework. Planting "
          "trees to increase infiltration is STB-1.B.1 in topic 5.13, and the framework ranks no "
          "method against another anywhere in this topic."),

 dict(q="Which set is the framework's list of methods around a home?",
      choices=[
        "Adjusting the thermostat, conserving water, using energy-efficient appliances, and "
        "conservation landscaping",
        "Adjusting the thermostat, conserving water, using public transportation, and "
        "conservation landscaping",
        "Improving fuel economy, using hybrid vehicles, using public transportation, and green "
        "building design features",
        "Conserving water, using energy-efficient appliances, and installing a wind turbine",
        "Adjusting the thermostat, conserving water, and using energy-efficient appliances, "
        "with no fourth method named"],
      ans=0,
      why="ENG-3.T.1 names four methods around a home: the thermostat, conserving water, "
          "energy-efficient appliances and conservation landscaping. Public transportation and "
          "the whole of the third set belong to ENG-3.T.2's large-scale list, a wind turbine "
          "appears in neither, and the fourth method is named rather than absent."),

 dict(q="At which scale does the framework place improving fuel economy for vehicles?",
      choices=[
        "Among the methods for conserving energy on a large scale",
        "Among the methods for conserving energy around a home",
        "Among the methods for increasing water infiltration in a city",
        "Among the methods for generating electricity without fossil fuels",
        "The framework does not name improving fuel economy at all"],
      ans=0,
      why="ENG-3.T.2 opens its list with IMPROVING FUEL ECONOMY FOR VEHICLES, and ENG-3.T.1's "
          "home list names the thermostat, water, appliances and landscaping instead. Water "
          "infiltration is STB-1.B.1 in topic 5.13, and nothing about fuel economy generates "
          "electricity."),

 dict(q="The framework writes BEVs, expanded as battery electric vehicles, in its large-scale "
        "list. What does it establish about them?",
      choices=[
        "That using them is one of the named methods, and nothing about how they work",
        "That using them is one of the named methods, and that they are to be preferred to "
        "hybrid vehicles",
        "That they run on hydrogen combined with oxygen from the air",
        "That they are the framework's own name for hybrid vehicles",
        "That they save more energy than any other large-scale method"],
      ans=0,
      why="ENG-3.T.2 names USING BEVs (BATTERY ELECTRIC VEHICLES) AND HYBRID VEHICLES and says "
          "nothing further about either. Hydrogen combined with oxygen from the air is the fuel "
          "cell of ENG-3.P.1 in topic 6.11, hybrids are named separately in the same clause, and "
          "the framework ranks no method against another."),

 dict(q="What follows from the framework naming battery electric vehicles and hybrid vehicles "
        "separately in one clause?",
      choices=[
        "That both are named methods, and that the framework treats them as two kinds rather "
        "than one",
        "That only battery electric vehicles are a named method",
        "That only hybrid vehicles are a named method",
        "That a hybrid vehicle is what the framework means by a battery electric vehicle",
        "That neither is a named method, since only public transportation is named"],
      ans=0,
      why="ENG-3.T.2 writes USING BEVs (BATTERY ELECTRIC VEHICLES) AND HYBRID VEHICLES, joining "
          "two named kinds with AND rather than defining one by the other. Dropping either leaves "
          "the clause incomplete, and public transportation is a further item in the same list "
          "rather than the only one."),

 dict(q="A city puts increased use of public transportation into two plans, one to conserve "
        "energy and one to increase the water soaking into its ground. Which plan does the "
        "framework support?",
      choices=[
        "Both, since it names public transportation for each of those two purposes in two "
        "separate statements",
        "The energy plan only, since the framework names public transportation for no other "
        "purpose",
        "The water plan only, since the framework names public transportation for no other "
        "purpose",
        "Neither, since the framework does not name public transportation anywhere",
        "Both, but only once the city is large enough for a large-scale method to apply"],
      ans=0,
      why="ENG-3.T.2 names USING PUBLIC TRANSPORTATION among the methods for conserving energy on "
          "a large scale, and STB-1.B.1 in topic 5.13 names increased use of public "
          "transportation among the methods to increase water infiltration. Two statements, two "
          "purposes, and neither of them attaches a condition about the size of the place."),

 dict(q="A student places green building design features among the methods for conserving energy "
        "around a home. What correction does the framework require?",
      choices=[
        "The framework names green building design features on its large-scale list, not among "
        "the home methods",
        "The framework names green building design features among the home methods, not on its "
        "large-scale list",
        "The framework names green building design features on both of its lists",
        "The framework does not name green building design features at all",
        "No correction is needed, since the framework gives only one list of methods"],
      ans=0,
      why="ENG-3.T.2 ends with IMPLEMENTING GREEN BUILDING DESIGN FEATURES, and ENG-3.T.1's home "
          "list stops at conservation landscaping. One rejected option is the exact reversal of "
          "the two lists, and the framework plainly gives two of them."),

 dict(q="The framework attaches a stated purpose to exactly one of its eight named methods. "
        "Which one, and what is the purpose?",
      choices=[
        "The thermostat, which is adjusted to reduce the use of heat and air conditioning",
        "Conserving water, which is done to reduce the energy spent heating and pumping it",
        "Energy-efficient appliances, which are chosen to reduce the energy each appliance draws",
        "Using public transportation, which is done to reduce the fuel burned for each passenger",
        "Green building design features, which are implemented to reduce a building's heating "
        "needs"],
      ans=0,
      why="ENG-3.T.1 writes ADJUSTING THE THERMOSTAT TO REDUCE THE USE OF HEAT AND AIR "
          "CONDITIONING, and that clause is the only purpose either statement supplies for any "
          "method. Each rejected option states a purpose that is reasonable and that the "
          "framework does not give: those four methods are named and left unexplained."),

 dict(q="Which set is the framework's list of methods on a large scale?",
      choices=[
        "Improving fuel economy for vehicles, using battery electric and hybrid vehicles, using "
        "public transportation, and implementing green building design features",
        "Improving fuel economy for vehicles, using battery electric and hybrid vehicles, "
        "conserving water, and implementing green building design features",
        "Adjusting the thermostat, conserving water, using energy-efficient appliances, and "
        "conservation landscaping",
        "Improving fuel economy for vehicles and using public transportation, with no other "
        "method named",
        "Building nuclear power stations, installing wind turbines, and using hydrogen fuel "
        "cells"],
      ans=0,
      why="ENG-3.T.2 names four large-scale methods: fuel economy, battery electric and hybrid "
          "vehicles, public transportation, and green building design features. Conserving water "
          "and the whole of the third set belong to ENG-3.T.1's home list, and the sources in the "
          "last set are the subject of topics 6.6, 6.11 and 6.12 rather than of this one."),

 dict(q="Which pairing puts each method on the framework's own list?",
      choices=[
        "Conserving water around a home; improving fuel economy on a large scale",
        "Improving fuel economy around a home; conserving water on a large scale",
        "Both conserving water and improving fuel economy around a home",
        "Both conserving water and improving fuel economy on a large scale",
        "Neither method is named on either list"],
      ans=0,
      why="ENG-3.T.1 names conserving water among the methods around a home and ENG-3.T.2 names "
          "improving fuel economy for vehicles among the methods on a large scale. One rejected "
          "pairing is the exact exchange of the two and the others move both to one list or off "
          "the lists altogether."),

 dict(q="A student reads the two statements as a list of energy sources to switch to. What "
        "correction does the framework require?",
      choices=[
        "Both statements name methods for conserving energy, and neither names a source of "
        "energy",
        "Both statements name sources of energy, and neither names a method for conserving "
        "energy",
        "The home statement names sources of energy and the large-scale statement names methods "
        "for conserving it",
        "The large-scale statement names sources of energy and the home statement names methods "
        "for conserving it",
        "No correction is needed, since both statements are lists of energy sources"],
      ans=0,
      why="ENG-3.T.1 and ENG-3.T.2 name a thermostat setting, water use, appliances, "
          "landscaping, fuel economy, two kinds of vehicle, public transportation and building "
          "design, and not one of the eight is a source of energy. The sources are the subject of "
          "topics 6.3 to 6.12, and one rejected option is the exact reversal of the key."),

 dict(q="A student lists installing a wind turbine at the house among the framework's methods "
        "for conserving energy around a home. What correction does the framework require?",
      choices=[
        "The home methods are the thermostat, water, appliances and landscaping, and a turbine "
        "produces electricity rather than conserving energy",
        "The home methods are the thermostat, water, appliances and landscaping, and a turbine "
        "is named on the large-scale list instead",
        "The framework names installing a wind turbine among the home methods, so the student "
        "is correct",
        "The framework names no methods for conserving energy around a home",
        "The home methods are all concerned with vehicles, so a turbine does not belong among "
        "them"],
      ans=0,
      why="ENG-3.T.1 names four home methods and a turbine is not among them, and ENG-3.T.2 does "
          "not name one either. ENG-3.R.1 in topic 6.12 has a wind turbine spinning a generator "
          "and PRODUCING ELECTRICITY, which is generation; the two lists here are about using "
          "less of the energy a household or a society already draws."),

 dict(q="The four parts below are the whole of one home's energy use, and one method was "
        "trialled on each. Which method saved the most energy in the year?",
      table=_T_HOME,
      choices=[
        "Adjusting the thermostat, which saved 600 energy units",
        "Replacing the appliances, which saved 400 energy units",
        "Reducing water use, which saved 120 energy units",
        "Conservation landscaping, which saved 80 energy units",
        "All four saved the same amount of energy"],
      ans=0,
      why="Subtracting each part's two readings gives 600, 400, 120 and 80 energy units saved, so "
          "the thermostat saved the most. ENG-3.T.1 names all four methods and ranks none of "
          "them, so the ranking here is the record's alone."),

 dict(q="Using the same four parts, which method saved the largest share of the energy its own "
        "part had been using?",
      table=_T_HOME,
      choices=[
        "Replacing the appliances, at 20 percent of that part's former use",
        "Adjusting the thermostat, at 15 percent of that part's former use",
        "Reducing water use, at 10 percent of that part's former use",
        "Conservation landscaping, at 10 percent of that part's former use",
        "The shares cannot be worked out from the record"],
      ans=0,
      why="Dividing each saving by that part's former use gives 15 percent for the thermostat, 20 "
          "for the appliances and 10 for each of the other two, so the largest share and the "
          "largest quantity belong to different methods. Every option states its own method's "
          "share correctly; only one of them is the largest."),

 dict(q="Using the same four parts, how much energy did the four methods save the home in the "
        "year altogether?",
      table=_T_HOME,
      choices=[
        "1,200 energy units",
        "600 energy units",
        "6,800 energy units",
        "8,000 energy units",
        "1,120 energy units"],
      ans=0,
      why="Adding the four savings, or subtracting the two column totals, gives 8,000 minus 6,800, "
          "which is 1,200 energy units. The rejected values quote the largest single saving, one "
          "of the two column totals, or a sum that leaves out the smallest method."),

 dict(q="Using the same four parts, what share of the home's total energy use did the four "
        "methods save between them?",
      table=_T_HOME,
      choices=[
        "15 percent",
        "10 percent",
        "20 percent",
        "85 percent",
        "The share cannot be worked out from the record"],
      ans=0,
      why="The home used 8,000 energy units before the methods and 6,800 with them, so the 1,200 "
          "saved is 15 percent of the total. The rejected values quote the share saved on one "
          "part of the home's use rather than on the whole of it, take the share still used, or "
          "deny an arithmetic the record plainly allows."),

 dict(q="Which of the framework's lists do the four trialled methods come from, and what does "
        "the record add?",
      table=_T_HOME,
      choices=[
        "All four are named around a home, and the record adds a ranking the framework itself "
        "does not give",
        "All four are named around a home, and the record confirms a ranking the framework "
        "itself gives",
        "All four are named on the large-scale list, and the record adds a ranking the framework "
        "does not give",
        "Two are named around a home and two on the large-scale list",
        "None of the four methods is named by the framework"],
      ans=0,
      why="The thermostat, energy-efficient appliances, conserving water and conservation "
          "landscaping are the four methods ENG-3.T.1 names around a home. The savings differ, so "
          "the record does rank them, and the framework itself ranks nothing and gives no figure "
          "anywhere in this topic."),

 dict(q="Every vehicle in this fleet travelled the same distance in the year. Which has the best "
        "fuel economy, and what is it?",
      table=_T_ECON,
      choices=[
        "Vehicle 4, at 50 distance units for each fuel unit",
        "Vehicle 1, at 20 distance units for each fuel unit",
        "Vehicle 4, at 20 distance units for each fuel unit",
        "Vehicle 1, at 50 distance units for each fuel unit",
        "All four are equal, since all four travelled the same distance"],
      ans=0,
      why="Dividing distance by fuel gives 20, 30, 40 and 50 distance units for each fuel unit, so "
          "the vehicle burning the least fuel over the same distance has the best economy. Equal "
          "distances make the fuel column the whole of the comparison rather than making the four "
          "equal."),

 dict(q="Using the same fleet, how much fuel would be saved in the year by replacing Vehicle 1 "
        "with a vehicle matching Vehicle 4?",
      table=_T_ECON,
      choices=[
        "360 fuel units",
        "600 fuel units",
        "840 fuel units",
        "240 fuel units",
        "None, since both vehicles would travel the same distance"],
      ans=0,
      why="Subtracting the two tabulated fuel figures gives 600 minus 240, which is 360 fuel units "
          "over the same distance. The rejected values quote one vehicle alone, add the two, or "
          "treat equal distances as equal fuel, which is what ENG-3.T.2's improving fuel economy "
          "for vehicles denies."),

 dict(q="Using the same fleet, how much fuel would the whole fleet have used in the year if "
        "every vehicle had matched the best economy?",
      table=_T_ECON,
      choices=[
        "960 fuel units",
        "1,540 fuel units",
        "580 fuel units",
        "240 fuel units",
        "2,400 fuel units"],
      ans=0,
      why="The best economy is 50 distance units for each fuel unit and the fleet covers 48,000 "
          "distance units, so it would need 960 fuel units. The rejected values quote what the "
          "fleet actually used, the difference between the two, one vehicle's own figure, or what "
          "the fleet would need at the worst economy rather than the best."),

 dict(q="A fleet operator keeps the distance each vehicle travels in a year and the fuel it uses "
        "in that year. Which of the framework's named methods can that record be used to judge?",
      table=_T_ECON,
      choices=[
        "Improving fuel economy for vehicles",
        "Using public transportation",
        "Implementing green building design features",
        "Conserving water around a home",
        "Adjusting the thermostat around a home"],
      ans=0,
      why="Fuel economy is distance travelled for each unit of fuel, which is exactly what the two "
          "columns allow to be computed, and ENG-3.T.2 names IMPROVING FUEL ECONOMY FOR VEHICLES "
          "among the large-scale methods. No column here counts passengers, buildings or water."),

 dict(q="One journey can be made in three ways. Which way uses the least energy for each "
        "passenger carried, and which named method does that support?",
      table=_T_MODE,
      choices=[
        "The train, at 8 energy units for each passenger, which supports using public "
        "transportation",
        "The bus, at 12 energy units for each passenger, which supports using public "
        "transportation",
        "The car, at 60 energy units for each passenger, which supports using public "
        "transportation",
        "The train, at 8 energy units for each passenger, which supports conserving water around "
        "a home",
        "The car, at 60 energy units for each passenger, since one person uses less than a whole "
        "bus does"],
      ans=0,
      why="Dividing each journey's energy by the passengers carried gives 60 for the car, 12 for "
          "the bus and 8 for the train, so the largest total belongs to the smallest amount for "
          "each passenger. ENG-3.T.2 names USING PUBLIC TRANSPORTATION among the large-scale "
          "methods, and conserving water is on the other list."),

 dict(q="Using the same journey, how much less energy does each bus passenger account for than "
        "the person driving alone?",
      table=_T_MODE,
      choices=[
        "48 energy units",
        "12 energy units",
        "60 energy units",
        "52 energy units",
        "420 energy units"],
      ans=0,
      why="Each bus passenger accounts for 480 over 40, which is 12 energy units, against 60 for "
          "the person driving alone, a difference of 48. The rejected values quote one of the two "
          "amounts, take the train's figure instead of the bus's, or subtract the two totals "
          "without dividing by the passengers."),

 dict(q="An office building was recorded before and after a set of changes. Which named method "
        "does the record report on, and what did the building's yearly use do?",
      table=_T_BUILD,
      choices=[
        "Green building design features, and the building's yearly use fell",
        "Green building design features, and the building's yearly use rose",
        "Conservation landscaping, and the building's yearly use fell",
        "Improving fuel economy for vehicles, and the building's yearly use fell",
        "No method the framework names could be reported on by a record of this kind"],
      ans=0,
      why="The building used 500, then 410, then 400 thousand energy units, so its yearly use "
          "fell across the record. ENG-3.T.2 names IMPLEMENTING GREEN BUILDING DESIGN FEATURES "
          "among the large-scale methods, while landscaping is a home method and fuel economy "
          "concerns vehicles."),

 dict(q="Using the same building, by what share did its yearly energy use fall from before the "
        "design features to the second year after them?",
      table=_T_BUILD,
      choices=[
        "20 percent",
        "18 percent",
        "25 percent",
        "10 percent",
        "80 percent"],
      ans=0,
      why="The use falls from 500 to 400 thousand energy units, a fall of 100, which is 20 percent "
          "of the starting figure. The rejected values stop at the first year, divide by the "
          "final figure instead of the starting one, halve the fall, or quote the share still "
          "used."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Around a home the named methods are adjusting the thermostat to reduce heat and air "
        "conditioning, conserving water, energy-efficient appliances and conservation "
        "landscaping; on a large scale they are improving fuel economy, battery electric and "
        "hybrid vehicles, public transportation and green building design features.",
        "Around a home the named methods are improving fuel economy, battery electric and "
        "hybrid vehicles, public transportation and green building design features; on a large "
        "scale they are the thermostat, conserving water, energy-efficient appliances and "
        "conservation landscaping.",
        "The framework names four methods around a home and ranks them from the most to the "
        "least effective, and names no methods on any larger scale.",
        "The framework names methods for conserving energy around a home only, and treats "
        "conservation on a larger scale as a matter for the topics on energy sources.",
        "The framework names installing wind turbines and hydrogen fuel cells among the methods "
        "for conserving energy on a large scale."],
      ans=0,
      why="The keyed summary carries ENG-3.T.1 and ENG-3.T.2 in the framework's own terms, both "
          "lists complete and each on its own scale. Each rejected summary exchanges the two "
          "lists, invents a ranking the framework never gives, denies the large-scale list, or "
          "moves ways of generating electricity onto it."),
]
