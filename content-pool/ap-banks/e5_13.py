# AP ENVIRONMENTAL SCIENCE 5.13 Methods to Reduce Urban Runoff
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding STB-1: humans can mitigate their impact on land and water
# resources through sustainable use.
# Learning objective STB-1.B, describe methods for mitigating problems related to urban
# runoff.
# Suggested skill 4.B, identify a research method, design, and/or measure used.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-1.B.1  Methods to increase water infiltration include replacing traditional
#              pavement with permeable pavement, planting trees, increased use of public
#              transportation, and building up, not out.
#
# SCOPE. One statement, one purpose and four named methods. The purpose is to INCREASE
# WATER INFILTRATION. The methods are permeable pavement in place of traditional
# pavement, planting trees, increased use of public transportation, and building up, not
# out. The framework gives no mechanism for any of them, no cost, no ranking and no
# figure, so nothing here says one method infiltrates more than another and nothing here
# explains WHY public transport or building upward should help -- only that the framework
# lists them. Where an item reasons about the underlying mechanism it chains to EIN-2.M.3
# and the chain is named in the claim.
#
# THE WORD THAT LIMITS THE LIST. The statement's verb is INCLUDE, so the four are not
# presented as the complete set. One item keys that directly: a method the framework does
# not name is neither endorsed nor ruled out by it.
#
# THE SUGGESTED SKILL IS 4.B, identify a research method, design, or measure. Four items
# follow it -- a paired-plot design, the measure that reports infiltration directly, what
# must be held constant, and a before-and-after comparison across two different streets
# that fails to isolate the planting.
#
# BOUNDARY WITH 5.10. The PROBLEM -- impervious surfaces that do not allow water to reach
# the soil, leading to flooding -- is EIN-2.M.3 in topic 5.10, and so is urban sprawl.
# This topic is the mitigation. No table here repeats one used there: 5.10 works from
# catchment cover, storm peak flow and a grass-gravel-asphalt plot trial, while the
# settings here are a paved surface trial, a repaved car park, tree canopy by
# neighbourhood, transport pattern and land use, and two development plans.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_13.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.13", "Methods to Reduce Urban Runoff", 5)

_T_PAVE = dict(
    headers=["Surface tested",
             "Rain soaking through in one hour (millimeters)",
             "Rain running off in one hour (millimeters)"],
    rows=[["Traditional asphalt", "2", "28"],
          ["Traditional concrete", "3", "27"],
          ["Permeable paving blocks", "21", "9"],
          ["Permeable porous asphalt", "24", "6"]])

_T_CARPARK = dict(
    headers=["Stage of the car park record",
             "Rain falling on the car park in the storm (millimeters)",
             "Runoff leaving the car park in the storm (millimeters)"],
    rows=[["Before repaving, traditional surface", "40", "34"],
          ["After repaving with a permeable surface", "40", "11"]])

_T_CANOPY = dict(
    headers=["Neighbourhood surveyed",
             "Tree canopy cover (percent of the ground)",
             "Rainfall reaching the drains as runoff (percent)"],
    rows=[["Neighbourhood 1", "6", "62"],
          ["Neighbourhood 2", "15", "54"],
          ["Neighbourhood 3", "28", "41"],
          ["Neighbourhood 4", "44", "30"]])

_T_TRANSPORT = dict(
    headers=["City transport pattern",
             "Trips made by public transport (percent)",
             "City land given to roads and parking (percent)"],
    rows=[["City with little public transport", "8", "38"],
          ["City with heavy public transport", "46", "19"]])

_T_UPOUT = dict(
    headers=["Plan for housing the same 900 dwellings",
             "Storeys in each building",
             "Ground covered by buildings, roads and parking (hectares)",
             "Ground left unpaved (hectares)"],
    rows=[["Plan that builds outward", "2", "36", "4"],
          ["Plan that builds upward", "8", "12", "28"]])

QUESTIONS = [

 dict(q="Which set of methods does the course framework give for increasing water "
        "infiltration in a built-up area?",
      choices=[
        "Replacing traditional pavement with permeable pavement, planting trees, increased "
        "use of public transportation, and building up, not out",
        "Replacing permeable pavement with traditional pavement, felling trees, increased "
        "use of private cars, and building out, not up",
        "Widening storm drains, lining channels with concrete, and piping runoff to the "
        "nearest river",
        "Raising the height of kerbs, resurfacing roads more often, and clearing gutters "
        "after every storm",
        "Irrigating parks, watering street trees, and washing streets in dry weather"],
      ans=0,
      why="STB-1.B.1 lists replacing traditional pavement with permeable pavement, planting "
          "trees, increased use of public transportation, and building up, not out. The first "
          "rejected option is that list with every item reversed; the others substitute drainage "
          "or maintenance measures the statement never names."),

 dict(q="What does the framework say those methods are for?",
      choices=[
        "Increasing water infiltration",
        "Increasing the speed at which runoff reaches a river",
        "Increasing the amount of rain that falls on a city",
        "Increasing the salinity of coastal groundwater",
        "Increasing the carbon dioxide a city releases"],
      ans=0,
      why="STB-1.B.1 introduces its list as METHODS TO INCREASE WATER INFILTRATION, so the aim "
          "is to get more of the rain into the ground rather than to move it faster or to change "
          "the weather. The rejected aims belong to other statements or to no statement at all."),

 dict(q="Which of the following is NOT one of the methods the framework names in this "
        "statement?",
      choices=[
        "Channelling runoff into concrete storm drains",
        "Replacing traditional pavement with permeable pavement",
        "Planting trees",
        "Increased use of public transportation",
        "Building up, not out"],
      ans=0,
      why="STB-1.B.1 names permeable pavement, planting trees, public transportation and "
          "building up rather than out. Concrete storm drains move water away from a surface "
          "rather than into the soil, and the statement does not list them."),

 dict(q="What does the framework say permeable pavement should replace?",
      choices=[
        "Traditional pavement",
        "Planted trees",
        "Public transport routes",
        "Multi-storey buildings",
        "Bare soil"],
      ans=0,
      why="STB-1.B.1 names REPLACING TRADITIONAL PAVEMENT WITH PERMEABLE PAVEMENT. The method "
          "substitutes one paved surface for another, so nothing in it calls for removing trees, "
          "transport routes, buildings or soil."),

 dict(q="What does the framework's phrase about building up rather than out describe?",
      choices=[
        "Housing the same activity on a smaller area of ground by building upward rather "
        "than spreading outward",
        "Spreading the same activity over a larger area of ground rather than building "
        "upward",
        "Raising buildings on stilts so that water can pass beneath them",
        "Restricting every new building to a single storey",
        "Building on higher ground so that runoff drains away from the settlement"],
      ans=0,
      why="STB-1.B.1's phrase is BUILDING UP, NOT OUT, which on its plain reading means "
          "upward on less ground rather than outward across more. The framework offers no "
          "further gloss, so nothing about stilts, storey limits or elevation may be read in."),

 dict(q="Four paved surfaces were given the same rainfall for one hour. What do the values "
        "show?",
      table=_T_PAVE,
      choices=[
        "Both permeable surfaces let far more rain through into the soil than either "
        "traditional surface did.",
        "Both traditional surfaces let far more rain through into the soil than either "
        "permeable surface did.",
        "All four surfaces let about the same depth of rain through into the soil.",
        "The permeable surfaces shed more rain as runoff than the traditional surfaces did.",
        "The depth soaking through cannot be compared between surfaces given the same "
        "rainfall."],
      ans=0,
      why="The traditional surfaces take 2 and 3 millimeters through while the permeable ones "
          "take 21 and 24, and the runoff runs the other way. STB-1.B.1 offers replacing "
          "traditional pavement with permeable pavement as a method to increase water "
          "infiltration."),

 dict(q="Using the same four surfaces, how much more rain soaked through the best permeable "
        "surface than through the traditional asphalt in the hour?",
      table=_T_PAVE,
      choices=[
        "22 millimeters more",
        "24 millimeters more",
        "26 millimeters more",
        "18 millimeters more",
        "2 millimeters more"],
      ans=0,
      why="Subtracting the two tabulated depths gives 24 minus 2, which is 22 millimeters. The "
          "rejected values quote the permeable surface alone, add the two, compare the wrong "
          "pair of surfaces, or quote the traditional surface alone."),

 dict(q="A car park was gauged in storms of the same size before and after it was repaved. "
        "Which conclusion do the values support?",
      table=_T_CARPARK,
      choices=[
        "The same rain fell in both storms, so the fall in runoff is attributable to the new "
        "surface rather than to the weather.",
        "Less rain fell in the second storm, so the fall in runoff is attributable to the "
        "weather rather than to the new surface.",
        "More runoff left the car park after repaving than before.",
        "The rain and the runoff were equal to each other before repaving.",
        "Nothing can be concluded, because the two storms were of different sizes."],
      ans=0,
      why="Rainfall reads 40 millimeters in both storms while runoff falls from 34 to 11, so the "
          "one variable that changed is the surface. STB-1.B.1 gives permeable pavement as a "
          "method to increase water infiltration."),

 dict(q="Using the same car park, by how much did the runoff from a storm of that size fall "
        "after the repaving?",
      table=_T_CARPARK,
      choices=[
        "By 23 millimeters",
        "By 34 millimeters",
        "By 45 millimeters",
        "By 29 millimeters",
        "By 11 millimeters"],
      ans=0,
      why="Subtracting the two tabulated runoff depths gives 34 minus 11, which is 23 "
          "millimeters. The rejected values quote the earlier storm alone, add the two, use the "
          "rainfall in place of one of the runoff figures, or quote the later storm alone."),

 dict(q="Four neighbourhoods of one city were surveyed for tree cover and for the share of "
        "rainfall reaching the drains. What relationship do the values show?",
      table=_T_CANOPY,
      choices=[
        "The neighbourhoods with more tree canopy sent a smaller share of the rainfall to "
        "the drains.",
        "The neighbourhoods with more tree canopy sent a larger share of the rainfall to the "
        "drains.",
        "All four neighbourhoods sent the same share of the rainfall to the drains.",
        "The neighbourhood with the least tree canopy sent the smallest share of the "
        "rainfall to the drains.",
        "Tree canopy and runoff cannot be compared between neighbourhoods of one city."],
      ans=0,
      why="Canopy runs 6, 15, 28 and 44 percent while the share reaching the drains runs 62, 54, "
          "41 and 30 percent, moving in opposite directions throughout. STB-1.B.1 lists planting "
          "trees among the methods to increase water infiltration."),

 dict(q="Using the same neighbourhoods, how much smaller is the share of rainfall reaching the "
        "drains in the most wooded neighbourhood than in the least wooded one?",
      table=_T_CANOPY,
      choices=[
        "32 percentage points smaller",
        "62 percentage points smaller",
        "92 percentage points smaller",
        "38 percentage points smaller",
        "30 percentage points smaller"],
      ans=0,
      why="Subtracting the two tabulated shares gives 62 minus 30, which is 32 percentage "
          "points. The rejected values quote the least wooded neighbourhood alone, add the two, "
          "take the difference in canopy cover, or quote the most wooded neighbourhood alone."),

 dict(q="Two cities of similar population and rainfall are compared in the table. Which "
        "conclusion do the values support?",
      table=_T_TRANSPORT,
      choices=[
        "The city where more trips are made by public transport gives a smaller share of its "
        "land to roads and parking.",
        "The city where more trips are made by public transport gives a larger share of its "
        "land to roads and parking.",
        "The two cities give the same share of their land to roads and parking.",
        "The city with the least public transport gives the smallest share of its land to "
        "roads and parking.",
        "The share of land given to roads and parking is unrelated to anything that can be "
        "measured."],
      ans=0,
      why="Public transport carries 8 percent of trips in one city and 46 in the other, against "
          "38 and 19 percent of the land given to roads and parking. STB-1.B.1 lists increased "
          "use of public transportation among its methods, and EIN-2.M.3 makes roads and parking "
          "lots impervious surfaces."),

 dict(q="Using the same two cities, how much smaller a share of its land does the city with "
        "heavy public transport give to roads and parking?",
      table=_T_TRANSPORT,
      choices=[
        "19 percentage points smaller",
        "38 percentage points smaller",
        "57 percentage points smaller",
        "46 percentage points smaller",
        "8 percentage points smaller"],
      ans=0,
      why="Subtracting the two tabulated shares gives 38 minus 19, which is 19 percentage "
          "points. The rejected values quote the first city alone, add the two, take a reading "
          "from the transport column, or quote the smaller transport share."),

 dict(q="Two plans would house the same number of dwellings on the same site. Which reading of "
        "the values matches the framework's phrase about building upward?",
      table=_T_UPOUT,
      choices=[
        "The taller plan covers a third of the ground the outward plan covers and leaves "
        "seven times as much of the site unpaved.",
        "The taller plan covers three times the ground the outward plan covers and leaves a "
        "seventh as much of the site unpaved.",
        "The two plans cover the same amount of ground and leave the same amount unpaved.",
        "The outward plan leaves more of the site unpaved than the taller plan does.",
        "The number of storeys has no bearing on how much ground a plan covers."],
      ans=0,
      why="The outward plan covers 36 hectares and leaves 4 unpaved, while the upward plan "
          "covers 12 and leaves 28, for the same 900 dwellings. STB-1.B.1's phrase is building "
          "up, not out, and less ground covered is more ground left for water to enter."),

 dict(q="Using the same two plans, how much more of the site does the taller plan leave "
        "unpaved?",
      table=_T_UPOUT,
      choices=[
        "24 hectares more",
        "28 hectares more",
        "32 hectares more",
        "12 hectares more",
        "4 hectares more"],
      ans=0,
      why="Subtracting the two tabulated unpaved areas gives 28 minus 4, which is 24 hectares. "
          "The rejected values quote the taller plan alone, add the two, take the difference in "
          "ground covered, or quote the outward plan alone."),

 dict(q="Which design would best test whether permeable pavement increases infiltration?",
      choices=[
        "Lay the two surfaces on adjacent plots of the same soil and slope, apply the same "
        "rainfall to each, and measure what soaks in",
        "Lay permeable pavement on one plot, measure what soaks in, and compare it with no "
        "other plot",
        "Compare a permeable plot measured in a wet month with a traditional plot measured "
        "in a dry month",
        "Compare a permeable plot laid over sand with a traditional plot laid over clay",
        "Ask the residents of two streets which surface they believe drains better"],
      ans=0,
      why="A comparison isolates the surface only when everything else is matched, so the "
          "adjacent plots share soil, slope and rainfall. Each rejected design leaves no "
          "comparison at all, or lets the weather or the soil vary alongside the surface, or "
          "collects opinion rather than measurement."),

 dict(q="Which measurement reports infiltration most directly?",
      choices=[
        "The depth of water that passes through the surface into the soil in a given time",
        "The depth of water standing on the surface when the storm ends",
        "The number of vehicles that use the street each day",
        "The height of the buildings along the street",
        "The area of the street in square meters"],
      ans=0,
      why="STB-1.B.1's stated aim is to INCREASE WATER INFILTRATION, and water passing through "
          "the surface into the soil is that quantity itself. Standing water, traffic, building "
          "height and street area are at best indirect and at worst unrelated."),

 dict(q="In a paired comparison of two pavements, which conditions must be held the same for "
        "any difference to be attributable to the surface?",
      choices=[
        "The rainfall applied to each plot and the soil lying beneath each plot",
        "The type of pavement on each plot and the date each plot was laid",
        "The colour of each pavement and the number of people who walk on it",
        "The number of trees planted beside each plot and the height of the nearest building",
        "Nothing needs to be held the same, because the surfaces differ"],
      ans=0,
      why="A difference can be assigned to the surface only when the surface is the one thing "
          "that differs, so the water applied and the ground receiving it must match. Holding "
          "the pavement type the same would remove the comparison itself."),

 dict(q="A council may alter the surface of its car parks but may not change anything else. "
        "Which of the framework's methods is open to it?",
      choices=[
        "Replacing the traditional pavement with permeable pavement",
        "Increased use of public transportation",
        "Building up, not out",
        "Planting trees across the whole district",
        "None of the framework's methods, since all of them require new buildings"],
      ans=0,
      why="STB-1.B.1 lists four methods, and the only one that consists of changing a paved "
          "surface is replacing traditional pavement with permeable pavement. The others require "
          "changes to travel, to buildings, or to land the council may not alter."),

 dict(q="A second council may plant on public land but may not alter any paved surface or any "
        "building. Which of the framework's methods is open to it?",
      choices=[
        "Planting trees",
        "Replacing traditional pavement with permeable pavement",
        "Building up, not out",
        "Widening the storm drains beneath the streets",
        "None of the framework's methods, since all of them require repaving"],
      ans=0,
      why="STB-1.B.1 lists planting trees as a method in its own right, and it requires neither "
          "repaving nor new building. Widening storm drains is not on the framework's list at "
          "all."),

 dict(q="A student writes that the framework's methods work by reducing the rain that falls on "
        "a city. Which correction is required?",
      choices=[
        "The methods are given as ways to increase infiltration, not as ways to change how "
        "much rain falls",
        "The methods are given as ways to change how much rain falls, and the student has "
        "stated the framework correctly",
        "The methods are given as ways to move runoff to a river more quickly",
        "The methods are given as ways to raise the salinity of coastal groundwater",
        "The framework gives no purpose for the methods at all"],
      ans=0,
      why="STB-1.B.1 introduces the four as METHODS TO INCREASE WATER INFILTRATION, which is "
          "about where the rain goes once it has fallen. Nothing in the statement concerns "
          "rainfall itself, drainage speed or groundwater salinity."),

 dict(q="A second student writes that replacing traditional pavement with permeable pavement "
        "means removing the pavement and leaving bare ground. Which correction is required?",
      choices=[
        "The method substitutes one paved surface for another rather than removing paving "
        "altogether",
        "The method removes paving altogether, and the student has stated it correctly",
        "The method covers bare ground with traditional pavement",
        "The method applies only to ground that has never been paved",
        "The framework does not mention pavement of any kind"],
      ans=0,
      why="STB-1.B.1 names REPLACING traditional pavement WITH permeable pavement, so a surface "
          "remains in place after the change. The statement says nothing about stripping paving "
          "or about paving ground that is currently bare."),

 dict(q="Which statement identifies the problem that this topic's methods are meant to "
        "mitigate?",
      choices=[
        "Built surfaces that keep rainfall from soaking into the ground cause water to "
        "collect and flood",
        "Built surfaces that let rainfall soak into the ground cause water to collect and "
        "flood",
        "Rainfall over cities has been falling steadily for several decades",
        "Groundwater beneath cities has become too fresh for use",
        "Cities produce less carbon dioxide than the rural land around them"],
      ans=0,
      why="EIN-2.M.3 states that impervious surfaces are human-made structures that do not allow "
          "water to reach the soil, leading to flooding, and STB-1.B.1's methods all work on "
          "infiltration. The rejected options reverse that mechanism or describe conditions the "
          "framework never asserts."),

 dict(q="Which observation would most directly show that one of these methods had done what "
        "the framework says such methods do?",
      choices=[
        "A larger share of the rain falling on the treated area soaked into the ground than "
        "before the change",
        "Less rain fell on the treated area in the year after the change than in the year "
        "before",
        "More vehicles used the treated street after the change than before",
        "The treated surface was laid in a different colour from the one it replaced",
        "The buildings beside the treated area were taller after the change than before"],
      ans=0,
      why="STB-1.B.1's stated purpose is to increase water infiltration, so the outcome to look "
          "for is a larger share of the rain entering the ground. Rainfall, traffic, colour and "
          "building height are not the quantity the statement is about."),

 dict(q="A researcher measures runoff from one street before trees are planted and from a "
        "different street after trees are planted, and credits the difference to the planting. "
        "What is the flaw?",
      choices=[
        "The two streets may differ in soil, slope, paving or rainfall, so the comparison "
        "does not isolate the planting",
        "The two streets cannot both have been measured, so no comparison exists",
        "Runoff is not a measurable quantity, so no design could work",
        "The planting should have been measured rather than the runoff",
        "There is no flaw, because trees were the only thing that changed"],
      ans=0,
      why="A before-and-after comparison across two different sites confounds the treatment with "
          "every other difference between the sites. The fix is to measure the same street "
          "before and after, or two matched streets at the same time."),

 dict(q="Which of the following does the framework's statement about these methods NOT "
        "supply?",
      choices=[
        "A ranking of the four methods by how much infiltration each one produces",
        "The naming of permeable pavement as a replacement for traditional pavement",
        "The naming of tree planting as a method",
        "The naming of increased public transportation as a method",
        "The naming of building up rather than out as a method"],
      ans=0,
      why="STB-1.B.1 gives four methods in an unordered list and attaches no quantity to any of "
          "them, so a ranking would be added rather than read. Each rejected option quotes "
          "something the statement does supply."),

 dict(q="A city proposes rain gardens, which the framework's list does not name. What follows "
        "from the wording of the statement?",
      choices=[
        "The list is introduced by the word include, so it is not offered as complete, and "
        "the framework neither endorses nor rules out a method it does not name",
        "The list is complete, so any method it does not name must be ineffective",
        "The framework endorses whatever method a city proposes",
        "Rain gardens must be one of the four named methods under a different name",
        "The framework's methods apply only to rural land, so the proposal is out of scope"],
      ans=0,
      why="STB-1.B.1 says methods to increase water infiltration INCLUDE the four it names, and "
          "a list introduced that way is not presented as exhaustive. Reading it as complete, or "
          "as a blanket endorsement, both go past the wording."),

 dict(q="Two of the framework's four methods concern how people travel and how buildings are "
        "arranged rather than the surface underfoot. Which two?",
      choices=[
        "Increased use of public transportation, and building up, not out",
        "Replacing traditional pavement with permeable pavement, and planting trees",
        "Planting trees, and increased use of public transportation",
        "Replacing traditional pavement with permeable pavement, and building up, not out",
        "Planting trees, and building up, not out"],
      ans=0,
      why="STB-1.B.1's four methods split into two that change a surface, permeable pavement and "
          "tree planting, and two that change travel and building form, public transportation "
          "and building up rather than out. Each rejected pair mixes one from each group."),

 dict(q="How does this topic stand in relation to the framework's statement about impervious "
        "surfaces?",
      choices=[
        "The other statement names the problem, surfaces that keep water from the soil; this "
        "one names methods for increasing the water that gets in",
        "This one names the problem, surfaces that keep water from the soil; the other names "
        "methods for increasing the water that gets in",
        "Both statements name problems, and neither names a method",
        "Both statements name methods, and neither names a problem",
        "The two statements concern different cities and cannot be applied together"],
      ans=0,
      why="EIN-2.M.3 defines impervious surfaces and attaches flooding to them, while STB-1.B.1 "
          "lists methods to increase water infiltration. One is the impact and the other the "
          "mitigation, and the exact swap of the two is the error worth guarding against."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Methods to increase water infiltration include replacing traditional pavement with "
        "permeable pavement, planting trees, increasing the use of public transportation, "
        "and building up rather than out.",
        "Methods to increase water infiltration are limited to replacing traditional "
        "pavement with permeable pavement, and the framework ranks it first.",
        "Methods to speed runoff to the nearest river include widening storm drains and "
        "lining channels with concrete.",
        "Methods to reduce the rain falling on a city include planting trees and using "
        "public transport.",
        "The framework names methods for reducing urban runoff but gives no purpose for "
        "them."],
      ans=0,
      why="The keyed summary is STB-1.B.1 with its purpose and all four methods and nothing "
          "else. Each rejected summary shortens the list and adds a ranking, changes the "
          "purpose to drainage or to rainfall, or denies that a purpose is stated."),
]
