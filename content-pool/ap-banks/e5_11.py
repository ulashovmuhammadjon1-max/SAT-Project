# AP ENVIRONMENTAL SCIENCE 5.11 Ecological Footprints
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.N, explain the variables measured in an ecological footprint.
# Suggested skill 5.E, explain what the data implies or illustrates about environmental
# issues.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.N.1  Ecological footprints compare resource demands and waste production
#              required for an individual or a society.
#
# SCOPE, AND WHY THIS TOPIC IS MOSTLY DATA. The framework gives ONE sentence, and it
# names exactly three things: the two variables compared -- RESOURCE DEMANDS and WASTE
# PRODUCTION -- and the two units the comparison can be made for -- AN INDIVIDUAL or A
# SOCIETY. That is the whole of the required content, so a bank of thirty recall
# questions cannot be written honestly. The suggested skill is 5.E, explain what data
# implies, and this module follows it: fourteen items carry a table and ask a question
# whose answer is settled by the numbers, and verify_e5_11.py recomputes every one of
# them from the table alone.
#
# WHAT IS DELIBERATELY NOT KEYED. The framework does not say that a footprint is
# expressed as an AREA of land, does not mention global hectares, biocapacity, overshoot
# or any national ranking, and names no country. Nothing here asserts any of that; the
# tables are therefore denominated in the underlying quantities the framework does name,
# resource units and waste units, rather than in an area. One item keys the absence
# directly, because a student who assumes a footprint is by definition an area of land
# is going beyond the statement.
#
# BOUNDARY WITH 5.12. Whether a level of use is SUSTAINABLE is STB-1.A.1 and STB-1.A.2 in
# topic 5.12, a separate statement with its own list of environmental indicators. A
# footprint under EIN-2.N.1 compares; it does not by itself pronounce a verdict. Two
# items turn on keeping the measure and the goal apart, and STB-1.A.1 appears here only
# as a named chain, never as the thing being tested.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_11.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.11", "Ecological Footprints", 5)

_T_FOUR = dict(
    headers=["Society surveyed",
             "Materials and energy used per person in a year (resource units)",
             "Waste produced per person in a year (waste units)"],
    rows=[["Society A", "120", "40"],
          ["Society B", "75", "25"],
          ["Society C", "40", "12"],
          ["Society D", "20", "6"]])

_T_TOTAL = dict(
    headers=["Country",
             "Footprint per person in a year (units)",
             "Population (millions)"],
    rows=[["Country W", "32", "5"],
          ["Country X", "8", "60"],
          ["Country Y", "16", "20"],
          ["Country Z", "4", "10"]])

_T_HOUSE = dict(
    headers=["Household studied",
             "Water, fuel and materials used in a year (resource units)",
             "Solid waste and wastewater produced in a year (waste units)"],
    rows=[["Household 1", "90", "10"],
          ["Household 2", "60", "55"]])

_T_CHANGE = dict(
    headers=["Stage of the record for one person",
             "Resources used in the year (resource units)",
             "Waste produced in the year (waste units)"],
    rows=[["Before the changes", "80", "20"],
          ["After the changes", "60", "10"]])

_T_TIME = dict(
    headers=["Decade of the record",
             "Resources used per person (resource units)",
             "Waste produced per person (waste units)"],
    rows=[["First", "30", "6"],
          ["Second", "45", "12"],
          ["Third", "60", "24"],
          ["Fourth", "75", "48"]])

_T_SPLIT = dict(
    headers=["Component measured for one year",
             "Person P",
             "Person Q"],
    rows=[["Food and materials used (resource units)", "50", "38"],
          ["Household energy used (resource units)", "30", "26"],
          ["Waste sent to landfill (waste units)", "8", "22"],
          ["Wastewater produced (waste units)", "4", "14"]])

QUESTIONS = [

 dict(q="Which two things does the course framework say an ecological footprint compares?",
      choices=[
        "Resource demands and waste production",
        "Resource demands and population growth rate",
        "Waste production and average life expectancy",
        "Land area and the number of species present",
        "Income per person and the price of energy"],
      ans=0,
      why="EIN-2.N.1 states that ecological footprints compare RESOURCE DEMANDS AND WASTE "
          "PRODUCTION required for an individual or a society. Each rejected pair keeps at most "
          "one of the two variables the statement names."),

 dict(q="For which units of analysis does the framework say a footprint can be worked out?",
      choices=[
        "For an individual or for a society",
        "For a society only, never for one person",
        "For an individual only, never for a whole society",
        "For a species, but not for people",
        "For an ecosystem, but not for the people living in it"],
      ans=0,
      why="EIN-2.N.1 says the comparison is of what is required FOR AN INDIVIDUAL OR A SOCIETY, "
          "so both scales are within the statement. The rejected options exclude one of the two "
          "the framework allows, or move the measure to a species or an ecosystem."),

 dict(q="A student writes that an ecological footprint measures only the resources a person "
        "uses. Which correction does the framework require?",
      choices=[
        "It compares waste production as well as resource demands",
        "It compares waste production instead of resource demands",
        "It compares resource demands for a society but not for a person",
        "It compares the resources a person uses with the resources a species uses",
        "The framework agrees that only resource demands are compared"],
      ans=0,
      why="EIN-2.N.1 names two variables joined by AND, so leaving out waste production drops "
          "half the measure. Replacing one variable with the other, rather than adding it, "
          "makes the same mistake in the opposite direction."),

 dict(q="A second student writes that a footprint can be worked out for a whole society but "
        "never for one person. Which correction does the framework require?",
      choices=[
        "The statement covers an individual as well as a society",
        "The statement covers an individual instead of a society",
        "The statement covers a society only when its population is known",
        "The statement covers neither an individual nor a society, only a region",
        "The framework agrees that a footprint applies only to a society"],
      ans=0,
      why="EIN-2.N.1 says the comparison is of what is required for AN INDIVIDUAL OR A SOCIETY, "
          "so the individual is inside the statement, not outside it. Substituting one scale "
          "for the other narrows the statement just as much as dropping one."),

 dict(q="Four societies were surveyed on the same basis, one person at a time. What do the "
        "values show?",
      table=_T_FOUR,
      choices=[
        "Society A places the largest demand on resources and produces the most waste per "
        "person, so it has the largest footprint on both measures.",
        "Society A places the largest demand on resources but produces the least waste per "
        "person, so the two measures disagree.",
        "Society D places the largest demand on resources and produces the most waste per "
        "person.",
        "The four societies place the same demand on resources per person.",
        "Resource demand and waste production cannot be compared across societies."],
      ans=0,
      why="Resource use runs 120, 75, 40 and 20 units per person while waste runs 40, 25, 12 "
          "and 6, so Society A leads on both columns and Society D trails on both. EIN-2.N.1 "
          "makes those two variables the content of the comparison."),

 dict(q="Using the same four societies, how much greater is the resource demand per person in "
        "the highest society than in the lowest?",
      table=_T_FOUR,
      choices=[
        "100 resource units greater",
        "120 resource units greater",
        "140 resource units greater",
        "34 resource units greater",
        "20 resource units greater"],
      ans=0,
      why="Subtracting the two tabulated demands gives 120 minus 20, which is 100 resource "
          "units per person. The rejected values quote the highest alone, add the two, take the "
          "difference in the waste column, or quote the lowest alone."),

 dict(q="Four countries' footprints per person and their populations are given in the table. "
        "Which conclusion do the values support?",
      table=_T_TOTAL,
      choices=[
        "The country with the largest footprint per person is not the country whose "
        "population as a whole carries the largest footprint.",
        "The country with the largest footprint per person is also the country whose "
        "population as a whole carries the largest footprint.",
        "The country with the smallest population carries the largest footprint as a whole.",
        "Every country's footprint as a whole is the same size.",
        "A country's footprint as a whole cannot be worked out from these two columns."],
      ans=0,
      why="Country W has the largest footprint per person at 32 units, but 32 times 5 million "
          "is 160 million units against Country X's 8 times 60 million, which is 480 million. "
          "EIN-2.N.1 allows the comparison for an individual OR a society, and the two scales "
          "need not rank countries the same way."),

 dict(q="Using the same four countries, what footprint does the population of Country X carry "
        "as a whole in one year?",
      table=_T_TOTAL,
      choices=[
        "480 million units",
        "68 million units",
        "160 million units",
        "320 million units",
        "8 million units"],
      ans=0,
      why="Multiplying the tabulated footprint per person by the tabulated population gives 8 "
          "times 60 million, which is 480 million units. The rejected values add the two columns "
          "instead of multiplying them, or give the whole-population footprint of another "
          "country."),

 dict(q="Two households were measured on both halves of the footprint. What do the values "
        "show?",
      table=_T_HOUSE,
      choices=[
        "The first household places the larger demand on resources while the second "
        "produces the larger amount of waste, so the two halves point in opposite "
        "directions.",
        "The first household places the larger demand on resources and also produces the "
        "larger amount of waste, so the two halves agree.",
        "The second household places the larger demand on resources and also produces the "
        "larger amount of waste.",
        "The two households are identical on both halves of the measure.",
        "Waste production tells you nothing that resource demand has not already told you."],
      ans=0,
      why="Household 1 uses 90 resource units against Household 2's 60, but produces 10 waste "
          "units against Household 2's 55. Because EIN-2.N.1 makes the footprint a comparison of "
          "BOTH variables, a household can lead on one and trail on the other."),

 dict(q="Using the same two households, how much more waste does the second produce in a year "
        "than the first?",
      table=_T_HOUSE,
      choices=[
        "45 waste units more",
        "55 waste units more",
        "65 waste units more",
        "30 waste units more",
        "10 waste units more"],
      ans=0,
      why="Subtracting the two tabulated waste amounts gives 55 minus 10, which is 45 waste "
          "units. The rejected values quote the larger figure alone, add the two, take the "
          "difference in the resource column, or quote the smaller figure alone."),

 dict(q="One person's resource use and waste were recorded before and after a set of changes "
        "at home. What do the values show?",
      table=_T_CHANGE,
      choices=[
        "Both halves of the footprint fell after the changes.",
        "Both halves of the footprint rose after the changes.",
        "Resource use fell but waste production rose after the changes.",
        "Waste production fell but resource use rose after the changes.",
        "Neither half of the footprint changed."],
      ans=0,
      why="Resource use falls from 80 to 60 units and waste from 20 to 10, so both variables "
          "EIN-2.N.1 names moved downward. The rejected options reverse one direction, both, or "
          "deny that anything changed."),

 dict(q="Using the same person's record, by what share did the two halves of the footprint "
        "fall together?",
      table=_T_CHANGE,
      choices=[
        "By 30 percent",
        "By 70 percent",
        "By 25 percent",
        "By 50 percent",
        "By 10 percent"],
      ans=0,
      why="The two columns total 100 units before the changes and 70 after, a fall of 30 of the "
          "original 100, which is 30 percent. The rejected values give the share remaining, the "
          "fall in the resource column alone, the fall in the waste column alone, or the fall "
          "in waste units taken as a percentage."),

 dict(q="A society's footprint per person was recorded once each decade. What do the values "
        "show about the two halves of the measure?",
      table=_T_TIME,
      choices=[
        "Both halves rose across the record, and the waste half rose the faster of the two.",
        "Both halves rose across the record, and the resource half rose the faster of "
        "the two.",
        "Both halves fell across the record.",
        "The resource half rose while the waste half fell.",
        "Neither half changed across the record."],
      ans=0,
      why="Resource use runs 30, 45, 60 and 75 units per person, so it grows by half again, "
          "while waste runs 6, 12, 24 and 48, doubling in every interval. Both variables "
          "EIN-2.N.1 names rise, and the waste variable rises faster."),

 dict(q="Using the same decades, how much waste per person was produced in the fourth decade "
        "compared with the first?",
      table=_T_TIME,
      choices=[
        "Eight times as much",
        "Two and a half times as much",
        "Four times as much",
        "Forty-two times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated waste amounts gives 48 divided by 6, which is 8. The "
          "rejected values come from the resource column, from halving the interval, from the "
          "difference rather than the ratio, or from denying that the two differ."),

 dict(q="Looking again at the four countries, which country carries the smallest footprint on "
        "both scales the framework allows?",
      table=_T_TOTAL,
      choices=[
        "Country Z, which is lowest both per person and for its population as a whole",
        "Country Z per person, but Country W for its population as a whole",
        "Country X, which is lowest both per person and for its population as a whole",
        "Country W, which is lowest both per person and for its population as a whole",
        "No country is lowest on both scales at once"],
      ans=0,
      why="Country Z uses 4 units per person, the lowest of the four, and 4 times 10 million is "
          "40 million units, also the lowest whole-population figure. EIN-2.N.1 licenses the "
          "comparison at both scales, and here they happen to agree."),

 dict(q="Comparing the two countries whose populations carry the largest and the smallest "
        "whole-population footprints in that table, how many times as large is the larger?",
      table=_T_TOTAL,
      choices=[
        "Twelve times as large",
        "Three times as large",
        "Eight times as large",
        "Two times as large",
        "About the same size"],
      ans=0,
      why="Country X's population carries 8 times 60 million, or 480 million units, and Country "
          "Z's carries 4 times 10 million, or 40 million, and 480 divided by 40 is 12. The "
          "rejected values compare the wrong pair of countries or divide the per-person column "
          "alone."),

 dict(q="Two people were measured component by component. Which reading of the values is "
        "correct?",
      table=_T_SPLIT,
      choices=[
        "Person P uses more resources but Person Q produces more waste, and Person Q's "
        "footprint is the larger when both halves are counted.",
        "Person P uses more resources but Person Q produces more waste, and Person P's "
        "footprint is the larger when both halves are counted.",
        "Person Q uses more resources and also produces more waste.",
        "Person P uses more resources and also produces more waste.",
        "The two people are identical on every component measured."],
      ans=0,
      why="Person P uses 50 plus 30, or 80 resource units, against Person Q's 38 plus 26, or 64; "
          "but Person P produces 8 plus 4, or 12 waste units, against Person Q's 22 plus 14, or "
          "36. Totalling both halves gives 92 for P and 100 for Q, so counting only one half "
          "would reverse the answer."),

 dict(q="Using the same two people, how much waste does the second produce compared with the "
        "first?",
      table=_T_SPLIT,
      choices=[
        "Three times as much",
        "Twice as much",
        "Four times as much",
        "Half as much",
        "The same amount"],
      ans=0,
      why="Person Q's waste components total 22 plus 14, or 36 units, against Person P's 8 plus "
          "4, or 12, and 36 divided by 12 is 3. The rejected values misadd one of the two "
          "columns or reverse which person produces more."),

 dict(q="Which of the following measurements belongs to the waste-production half of the "
        "framework's comparison?",
      choices=[
        "The mass of rubbish a household sends to landfill in a year",
        "The mass of food a household buys in a year",
        "The volume of fuel a household burns for heating in a year",
        "The area of floor space a household occupies",
        "The number of people living in the household"],
      ans=0,
      why="EIN-2.N.1 divides the measure into resource demands and waste production, and "
          "rubbish leaving the household is what it produces rather than what it draws in. Food, "
          "fuel and floor space are demands, and the number of residents is the denominator "
          "rather than either variable."),

 dict(q="Which of the following measurements belongs to the resource-demand half of the "
        "framework's comparison?",
      choices=[
        "The volume of fresh water a household draws in a year",
        "The volume of wastewater a household discharges in a year",
        "The mass of rubbish a household sets out for collection each week",
        "The volume of exhaust gas the household's vehicles emit in a year",
        "The mass of sewage sludge produced by treating the household's waste"],
      ans=0,
      why="EIN-2.N.1 puts resource demands on one side of the comparison and waste production on "
          "the other, and water drawn in is a demand. Wastewater, rubbish, exhaust and sludge "
          "are all things the household puts out, which is the other half."),

 dict(q="Why can two societies be ranked one way by footprint per person and the other way by "
        "the footprint their populations carry as a whole?",
      choices=[
        "Because the whole-population figure multiplies the per-person figure by the number "
        "of people, and a small per-person figure in a large population can outweigh a "
        "large one in a small population",
        "Because the whole-population figure adds the per-person figure to the number of "
        "people",
        "Because the per-person figure counts waste production and the whole-population "
        "figure counts only resource demands",
        "Because the per-person figure is measured in different units from the "
        "whole-population figure",
        "Because a society's footprint does not depend on how many people it contains"],
      ans=0,
      why="EIN-2.N.1 allows the comparison for an individual OR a society, and the two scales "
          "are related by population size. Each rejected option gets the relation between the "
          "scales wrong, or denies that the two scales differ at all."),

 dict(q="Which comparison does the framework's sentence directly license?",
      choices=[
        "The resource demands and waste production of one society against those of another",
        "The resource demands of one society against the life expectancy of another",
        "The waste production of one society against the land area of another",
        "The resource demands of a society against the number of species living in it",
        "The framework's sentence licenses no comparison between two societies"],
      ans=0,
      why="EIN-2.N.1 says footprints COMPARE resource demands and waste production required for "
          "an individual or a society, so like against like at either scale is exactly what the "
          "sentence supports. Each rejected option pairs one of the framework's variables with "
          "something the sentence does not name."),

 dict(q="A report states that because one society's footprint is smaller than another's, that "
        "society's use of resources must be sustainable. What is wrong with the inference?",
      choices=[
        "A footprint compares two societies with each other, while sustainability is a "
        "separate question about using resources without depleting them for future "
        "generations",
        "A footprint compares two societies with each other, and sustainability means "
        "nothing more than having the smaller of two footprints",
        "A footprint measures only waste production, so it cannot say anything about "
        "resource use at all",
        "A footprint can be worked out for an individual but never for a society, so no "
        "such comparison is possible",
        "There is nothing wrong with the inference, because the framework defines "
        "sustainability as a smaller footprint"],
      ans=0,
      why="EIN-2.N.1 makes a footprint a COMPARISON of resource demands and waste production. "
          "The question of whether use can continue without depletion for future generations is "
          "STB-1.A.1, a separate statement, so being lower than a neighbour settles nothing "
          "about it."),

 dict(q="What is the minimum a researcher must measure to state an ecological footprint for "
        "one person, as the framework defines it?",
      choices=[
        "The resources that person demands and the waste that person produces",
        "The resources that person demands and the size of the society they live in",
        "The waste that person produces and the number of years they have lived",
        "The resources that person demands and the resources their neighbours demand",
        "The land area that person occupies and the fuel they burn"],
      ans=0,
      why="EIN-2.N.1 names exactly two variables, resource demands and waste production, and "
          "allows the measure at the scale of an individual. Anything less than both variables "
          "is not the framework's measure, and society size, age and land area are none of them."),

 dict(q="An analyst has the whole-population footprint of a society and wants to compare it "
        "with one resident's footprint. What else is needed?",
      choices=[
        "The number of people in the society, so that the whole-population figure can be put "
        "on a per-person basis",
        "The land area of the society, so that the whole-population figure can be put on a "
        "per-hectare basis",
        "The number of species in the society's territory, so that the figure can be shared "
        "among them",
        "The society's average income, so that the figure can be adjusted for wealth",
        "Nothing further, because the two figures are already on the same basis"],
      ans=0,
      why="EIN-2.N.1 allows the comparison at the scale of an individual or of a society, and "
          "moving between those two scales is division by the number of people. Land area, "
          "species counts and income are not variables the statement names."),

 dict(q="A small country states that its footprint is small simply because few people live "
        "there. What does the framework's measure allow a reader to check?",
      choices=[
        "Whether the resource demands and waste production per person are also small, which "
        "is a different question from the size of the total",
        "Whether the resource demands per person are small, since waste production is not "
        "part of the measure",
        "Whether the country's land area is small, since that is what a footprint measures",
        "Nothing, because the framework allows a footprint to be stated only for a whole "
        "society",
        "Nothing, because the framework allows a footprint to be stated only for an "
        "individual"],
      ans=0,
      why="EIN-2.N.1 licenses the comparison for an individual as well as for a society, so the "
          "per-person figure is available and can be small or large independently of the total. "
          "The rejected options drop one variable, substitute land area, or deny one of the two "
          "scales the statement allows."),

 dict(q="Which of the following does the framework's statement about ecological footprints NOT "
        "assert?",
      choices=[
        "That a footprint is expressed as an area of land",
        "That a footprint compares resource demands",
        "That a footprint compares waste production",
        "That a footprint can be stated for an individual",
        "That a footprint can be stated for a society"],
      ans=0,
      why="EIN-2.N.1 names two variables and two scales and stops there. It says nothing about "
          "the units in which a footprint is expressed, so treating an area of land as part of "
          "the definition adds to the statement rather than reading it."),

 dict(q="A company reports the fuel, water and materials it consumed last year and calls the "
        "total its ecological footprint. What does the framework's definition require it to "
        "add?",
      choices=[
        "A measure of the waste the company produced",
        "A measure of the company's annual profit",
        "A measure of the land the company's buildings occupy",
        "A measure of the number of people the company employs",
        "Nothing, because consumption alone is the framework's measure"],
      ans=0,
      why="EIN-2.N.1 makes the footprint a comparison of resource demands AND waste production, "
          "so a consumption total is half the measure. Profit, land and headcount are not "
          "variables the statement names."),

 dict(q="How does this topic's statement relate to the framework's statement about "
        "sustainability?",
      choices=[
        "One supplies a way of measuring what is demanded and discarded; the other supplies "
        "the goal of using resources without depleting them for future generations",
        "One supplies the goal of using resources without depleting them; the other supplies "
        "a way of measuring what is demanded and discarded",
        "Both supply the same measure under two different names",
        "Both supply goals, and neither supplies any measurement",
        "The two statements concern different subjects and cannot be applied to one society"],
      ans=0,
      why="EIN-2.N.1 is a measure, comparing resource demands and waste production, while "
          "STB-1.A.1 states the goal of living on Earth and using resources without depletion "
          "for future generations. The exact swap of measure and goal is the error worth "
          "guarding against."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "An ecological footprint compares the resource demands and the waste production "
        "required for an individual or for a society.",
        "An ecological footprint compares the resource demands required for a society, and "
        "cannot be stated for an individual.",
        "An ecological footprint compares the waste production required for an individual, "
        "and takes no account of resources demanded.",
        "An ecological footprint measures the area of productive land a society occupies "
        "and nothing else.",
        "An ecological footprint states whether a society's use of resources can continue "
        "without depleting them."],
      ans=0,
      why="The keyed summary is EIN-2.N.1 with nothing removed and nothing added. Each rejected "
          "summary drops one of the two variables, drops one of the two scales, substitutes an "
          "area the statement never mentions, or replaces the measure with the separate "
          "sustainability goal of STB-1.A.1."),
]
