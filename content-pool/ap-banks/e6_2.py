# AP ENVIRONMENTAL SCIENCE 6.2 Global Energy Consumption
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objective ENG-3.B, describe trends in energy consumption.
# Suggested skill 6.C, calculate an accurate numeric answer with appropriate units.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.B.1  The use of energy resources is not evenly distributed between developed and
#              developing countries.
#   ENG-3.B.2  The most widely used sources of energy globally are fossil fuels.
#   ENG-3.B.3  As developing countries become more developed, their reliance on fossil
#              fuels for energy increases.
#   ENG-3.B.4  As the world becomes more industrialized, the demand for energy increases.
#   ENG-3.B.5  Availability, price, and governmental regulations influence which energy
#              sources people use and how they use them.
#
# SCOPE. Five statements, every one of them a DIRECTION rather than a quantity. The
# framework gives no percentage, no per-person figure, no country and no year anywhere in
# this topic, so nothing here quotes a real statistic; fourteen items print their own data
# in a table and the arithmetic is recomputed in verify_e6_2.py from that table alone.
# The suggested skill is 6.C, calculate an accurate numeric answer with appropriate units,
# which is why this module carries more arithmetic than any other in the unit.
#
# THE TWO STATEMENTS THAT ARE EASY TO MERGE. ENG-3.B.3 is about DEVELOPING COUNTRIES and
# their RELIANCE ON FOSSIL FUELS; ENG-3.B.4 is about THE WORLD and its TOTAL DEMAND FOR
# ENERGY. Different subject, different quantity. One item keys the distinction and the
# distractors are the four possible mixings of the two.
#
# THE DIRECTION THAT IS EASY TO INVERT. ENG-3.B.3 has reliance on fossil fuels RISING as
# a developing country develops, which is the opposite of what a student expects. Two
# items turn on it and their anchors carry the direction word.
#
# BOUNDARY WITH 6.1 AND 6.4. Whether a source is renewable is ENG-3.A in topic 6.1 and is
# never keyed here. Where resources OCCUR, and the geologic history behind it, is
# ENG-3.D.1 in topic 6.4; this topic is about who USES energy, not where it lies.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e6_2.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.2", "Global Energy Consumption", 6)

_T_PERCAP = dict(
    headers=["Group of countries",
             "People (millions)",
             "Energy used in a year (billion energy units)"],
    rows=[["Developed countries", "1,000", "4,000"],
          ["Developing countries", "5,000", "4,000"]])

_T_MIX = dict(
    headers=["Source of the world's energy",
             "Share of world energy supply (percent)"],
    rows=[["Coal", "26"],
          ["Crude oil and its products", "31"],
          ["Natural gas", "23"],
          ["Nuclear power", "4"],
          ["All other sources together", "16"]])

_T_DEVELOP = dict(
    headers=["Decade of the country's record",
             "Industrial output (index)",
             "Energy used per person (energy units)",
             "Share of that energy from fossil fuels (percent)"],
    rows=[["First", "20", "0.6", "38"],
          ["Second", "55", "1.4", "57"],
          ["Third", "110", "3.0", "74"]])

_T_DEMAND = dict(
    headers=["Decade of the world record",
             "World industrial output (index)",
             "World energy demand (billion energy units)"],
    rows=[["First", "100", "3,000"],
          ["Second", "150", "4,200"],
          ["Third", "210", "5,700"],
          ["Fourth", "300", "7,800"]])

_T_PRICE = dict(
    headers=["District surveyed",
             "Price of the fuel (currency units per energy unit)",
             "Households using that fuel (percent)"],
    rows=[["District 1", "2", "78"],
          ["District 2", "5", "46"],
          ["District 3", "9", "19"]])

_T_RULE = dict(
    headers=["Stage of the record",
             "Sulfur permitted in household fuel (percent by mass)",
             "Households still using the high sulfur fuel (percent)"],
    rows=[["Before the regulation", "5.0", "64"],
          ["Two years after the regulation", "2.0", "35"],
          ["Five years after the regulation", "1.0", "12"]])

QUESTIONS = [

 dict(q="What does the course framework say about how the use of energy resources is spread "
        "between developed and developing countries?",
      choices=[
        "It is not evenly distributed between them",
        "It is evenly distributed between them",
        "It is evenly distributed within each group but not between the groups' regions",
        "It cannot be compared between the two groups",
        "The framework makes no statement about how energy use is spread"],
      ans=0,
      why="ENG-3.B.1 states that the use of energy resources IS NOT EVENLY DISTRIBUTED between "
          "developed and developing countries. The rejected options reverse the claim, restrict "
          "it, or deny that it is made."),

 dict(q="Which sources does the framework name as the most widely used globally?",
      choices=[
        "Fossil fuels",
        "Nuclear power",
        "Wind and solar energy",
        "Hydroelectric power",
        "Biomass in the form of firewood and charcoal"],
      ans=0,
      why="ENG-3.B.2 states that THE MOST WIDELY USED SOURCES OF ENERGY GLOBALLY ARE FOSSIL "
          "FUELS. The framework treats them as nonrenewable in the same unit, which is exactly "
          "why the unit overview asks why they are nevertheless the most widely used."),

 dict(q="According to the framework, what happens to a developing country's reliance on fossil "
        "fuels as it becomes more developed?",
      choices=[
        "It increases",
        "It decreases",
        "It stays exactly where it was",
        "It changes only where the country has no fossil fuel of its own",
        "The framework makes no statement about it"],
      ans=0,
      why="ENG-3.B.3 states that AS DEVELOPING COUNTRIES BECOME MORE DEVELOPED, THEIR RELIANCE "
          "ON FOSSIL FUELS FOR ENERGY INCREASES. The direction is upward, which is the opposite "
          "of what many students expect, and the framework attaches no condition to it."),

 dict(q="According to the framework, what happens to the demand for energy as the world becomes "
        "more industrialized?",
      choices=[
        "It increases",
        "It decreases",
        "It stays level, because industry uses energy more efficiently",
        "It rises in developed countries and falls in developing ones",
        "The framework makes no statement about it"],
      ans=0,
      why="ENG-3.B.4 states that AS THE WORLD BECOMES MORE INDUSTRIALIZED, THE DEMAND FOR ENERGY "
          "INCREASES. The statement is about the world as a whole and it attaches no efficiency "
          "offset and no split between the two groups of countries."),

 dict(q="Which three things does the framework say influence which energy sources people use "
        "and how they use them?",
      choices=[
        "Availability, price, and governmental regulations",
        "Availability, climate, and population growth",
        "Price, climate, and the age of the equipment",
        "Governmental regulations, rainfall, and soil type",
        "Availability, price, and the distance to the nearest coast"],
      ans=0,
      why="ENG-3.B.5 names AVAILABILITY, PRICE, AND GOVERNMENTAL REGULATIONS. Climate, "
          "population, rainfall, soil and distance appear nowhere in the statement."),

 dict(q="Which of the following is NOT among the influences the framework names in that "
        "statement?",
      choices=[
        "The climate of the region",
        "How available the source is",
        "What a unit of the source costs",
        "The regulations a government sets on its use",
        "Whether a government permits its use at all"],
      ans=0,
      why="ENG-3.B.5's three influences are availability, price and governmental regulations. "
          "Climate is not one of them. Two rejected options restate governmental regulation, one "
          "restates availability and one restates price."),

 dict(q="Which of the following correctly separates two of the framework's statements about "
        "trends?",
      choices=[
        "One says a developing country's reliance on fossil fuels rises as it develops; the "
        "other says the world's total demand for energy rises as it industrializes",
        "One says the world's total demand for energy rises as it industrializes; the other "
        "says a developing country's reliance on fossil fuels falls as it develops",
        "One says a developing country's total demand for energy falls as it develops; the "
        "other says the world's reliance on fossil fuels falls as it industrializes",
        "Both statements are about a developing country's reliance on fossil fuels",
        "Both statements are about the world's total demand for energy"],
      ans=0,
      why="ENG-3.B.3 is about DEVELOPING COUNTRIES and their RELIANCE ON FOSSIL FUELS, while "
          "ENG-3.B.4 is about THE WORLD and its TOTAL DEMAND FOR ENERGY. They differ in both "
          "subject and quantity, and each rejected option mixes the two or reverses a direction."),

 dict(q="Two groups of countries were compared on population and on energy used. Which "
        "statement of the framework do the values illustrate?",
      table=_T_PERCAP,
      choices=[
        "That the use of energy resources is not evenly distributed, since the two groups "
        "use the same total energy while one holds five times the people of the other",
        "That the use of energy resources is evenly distributed, since the two groups use "
        "the same total energy",
        "That the use of energy resources is not evenly distributed, since the developing "
        "countries use far more energy in total",
        "That fossil fuels are the most widely used sources of energy globally",
        "That governmental regulations influence which energy sources people use"],
      ans=0,
      why="Both groups use 4,000 billion energy units, but the developed group holds 1,000 "
          "million people against 5,000 million. ENG-3.B.1 states that the use of energy "
          "resources IS NOT EVENLY DISTRIBUTED between developed and developing countries, and "
          "an equal total spread over unequal populations is exactly that."),

 dict(q="Using the same two groups, how much energy does a person in the developed countries "
        "use compared with a person in the developing countries?",
      table=_T_PERCAP,
      choices=[
        "Five times as much",
        "Four times as much",
        "Two times as much",
        "Eight times as much",
        "The same amount"],
      ans=0,
      why="Dividing each group's energy by its population gives 4,000 over 1,000 against 4,000 "
          "over 5,000, which is 4.0 against 0.8 energy units per person, a ratio of 5. The "
          "rejected values misdivide one of the two rows or deny that they differ."),

 dict(q="Using the same two groups, what share of the world's people live in the developed "
        "countries, and what share of the energy do they use?",
      table=_T_PERCAP,
      choices=[
        "A sixth of the people, using half of the energy",
        "Half of the people, using a sixth of the energy",
        "A sixth of the people, using a sixth of the energy",
        "Half of the people, using half of the energy",
        "Five sixths of the people, using half of the energy"],
      ans=0,
      why="The developed group holds 1,000 of the 6,000 million people, which is a sixth, and "
          "uses 4,000 of the 8,000 billion energy units, which is a half. ENG-3.B.1's uneven "
          "distribution is exactly the gap between those two fractions."),

 dict(q="The world's energy supply is broken down by source in the table. Which conclusion "
        "matches the framework's statement about global energy use?",
      table=_T_MIX,
      choices=[
        "Coal, crude oil and natural gas together supply the largest part of the world's "
        "energy, which is the framework's claim about fossil fuels.",
        "Nuclear power supplies the largest part of the world's energy, which is the "
        "framework's claim about fossil fuels.",
        "The sources other than coal, crude oil and natural gas supply more of the world's "
        "energy than those three do.",
        "The five sources each supply about the same share of the world's energy.",
        "Coal alone supplies more than half of the world's energy."],
      ans=0,
      why="Coal, crude oil and natural gas supply 26, 31 and 23 percent, which is 80 percent "
          "between them, against 4 percent from nuclear power and 16 from everything else. "
          "ENG-3.B.2 states that the most widely used sources of energy globally are fossil "
          "fuels."),

 dict(q="Using the same breakdown, what share of the world's energy comes from the three fossil "
        "fuels listed?",
      table=_T_MIX,
      choices=[
        "80 percent",
        "57 percent",
        "84 percent",
        "26 percent",
        "16 percent"],
      ans=0,
      why="Adding the three tabulated shares gives 26 plus 31 plus 23, which is 80 percent. The "
          "rejected values leave out natural gas, add nuclear power to the three, quote coal "
          "alone, or quote the unclassified remainder."),

 dict(q="One developing country's record across three decades is given in the table. Which two "
        "of the framework's statements do the values illustrate together?",
      table=_T_DEVELOP,
      choices=[
        "That energy demand rises with industrialization, and that reliance on fossil fuels "
        "rises as a developing country develops",
        "That energy demand falls with industrialization, and that reliance on fossil fuels "
        "falls as a developing country develops",
        "That energy demand rises with industrialization, but that reliance on fossil fuels "
        "falls as a developing country develops",
        "That energy use is evenly distributed between developed and developing countries",
        "That availability, price and governmental regulations are the only influences on "
        "energy use"],
      ans=0,
      why="Industrial output runs 20, 55 and 110 while energy per person runs 0.6, 1.4 and 3.0 "
          "and the fossil share runs 38, 57 and 74 percent. ENG-3.B.4 has demand rising with "
          "industrialization and ENG-3.B.3 has reliance on fossil fuels rising as a developing "
          "country develops."),

 dict(q="Using the same country, by how much did the share of its energy coming from fossil "
        "fuels rise across the three decades?",
      table=_T_DEVELOP,
      choices=[
        "By 36 percentage points",
        "By 74 percentage points",
        "By 112 percentage points",
        "By 19 percentage points",
        "By 17 percentage points"],
      ans=0,
      why="Subtracting the two tabulated shares gives 74 minus 38, which is 36 percentage "
          "points. The rejected values quote the final share alone, add the two, or take one of "
          "the two decade-to-decade steps."),

 dict(q="Using the same country, how much energy did each person use in the third decade "
        "compared with the first?",
      table=_T_DEVELOP,
      choices=[
        "Five times as much",
        "Four times as much",
        "Two times as much",
        "Ten times as much",
        "The same amount"],
      ans=0,
      why="Dividing the two tabulated figures gives 3.0 divided by 0.6, which is 5. The rejected "
          "values come from the middle decade, from the industrial output column, or from "
          "denying that the decades differ."),

 dict(q="World industrial output and world energy demand were recorded once a decade. Which of "
        "the framework's statements do the values support?",
      table=_T_DEMAND,
      choices=[
        "That the demand for energy increases as the world becomes more industrialized",
        "That the demand for energy decreases as the world becomes more industrialized",
        "That the demand for energy is unrelated to how industrialized the world is",
        "That fossil fuels are the most widely used sources of energy globally",
        "That energy use is evenly distributed between developed and developing countries"],
      ans=0,
      why="Industrial output runs 100, 150, 210 and 300 while energy demand runs 3,000, 4,200, "
          "5,700 and 7,800 billion units, rising together throughout. ENG-3.B.4 states that as "
          "the world becomes more industrialized, the demand for energy increases."),

 dict(q="Using the same world record, by how much did energy demand grow across the four "
        "decades?",
      table=_T_DEMAND,
      choices=[
        "By 4,800 billion energy units",
        "By 7,800 billion energy units",
        "By 10,800 billion energy units",
        "By 2,700 billion energy units",
        "By 200 billion energy units"],
      ans=0,
      why="Subtracting the two tabulated demands gives 7,800 minus 3,000, which is 4,800 billion "
          "energy units. The rejected values quote the final decade alone, add the two, take one "
          "of the shorter intervals, or take the rise in the industrial output column."),

 dict(q="Three districts were surveyed for the price of one fuel and for how many households "
        "used it. Which of the framework's named influences do the values illustrate?",
      table=_T_PRICE,
      choices=[
        "Price, since the share of households using the fuel falls as its price rises",
        "Price, since the share of households using the fuel rises as its price rises",
        "Governmental regulations, since the share using the fuel falls as its price rises",
        "Availability, since the fuel is on sale in all three districts",
        "None of the framework's influences, since price is not one of them"],
      ans=0,
      why="Prices run 2, 5 and 9 currency units per energy unit while the share of households "
          "using the fuel runs 78, 46 and 19 percent. ENG-3.B.5 names PRICE among the three "
          "things that influence which energy sources people use."),

 dict(q="Using the same three districts, how much smaller is the share of households using the "
        "fuel where it costs most than where it costs least?",
      table=_T_PRICE,
      choices=[
        "59 percentage points smaller",
        "78 percentage points smaller",
        "97 percentage points smaller",
        "32 percentage points smaller",
        "27 percentage points smaller"],
      ans=0,
      why="Subtracting the two tabulated shares gives 78 minus 19, which is 59 percentage "
          "points. The rejected values quote the cheapest district alone, add the two, or take "
          "one of the two steps between adjacent districts."),

 dict(q="A government tightened the sulfur allowed in household fuel and the effect was "
        "recorded. Which of the framework's named influences do the values illustrate?",
      table=_T_RULE,
      choices=[
        "Governmental regulations, since fewer households used the high sulfur fuel as the "
        "permitted level was cut",
        "Governmental regulations, since more households used the high sulfur fuel as the "
        "permitted level was cut",
        "Price, since fewer households used the high sulfur fuel as the permitted level was "
        "cut",
        "Availability, since the fuel remained on sale throughout",
        "None of the framework's influences, since regulation is not one of them"],
      ans=0,
      why="The permitted sulfur falls from 5.0 to 2.0 to 1.0 percent by mass while the share of "
          "households still using the high sulfur fuel falls from 64 to 35 to 12 percent. "
          "ENG-3.B.5 names GOVERNMENTAL REGULATIONS among the three influences on which energy "
          "sources people use."),

 dict(q="Using the same record, by how much did the share of households using the high sulfur "
        "fuel fall across the five years?",
      table=_T_RULE,
      choices=[
        "By 52 percentage points",
        "By 64 percentage points",
        "By 76 percentage points",
        "By 29 percentage points",
        "By 23 percentage points"],
      ans=0,
      why="Subtracting the two tabulated shares gives 64 minus 12, which is 52 percentage "
          "points. The rejected values quote the opening share alone, add the two, or take one "
          "of the two steps within the record."),

 dict(q="A student writes that the framework describes energy use as spread evenly across the "
        "world. Which correction is required?",
      choices=[
        "The framework states that use is NOT evenly distributed between developed and "
        "developing countries",
        "The framework states that use is evenly distributed, so the student is correct",
        "The framework states that use is evenly distributed within the developing countries "
        "only",
        "The framework states that use cannot be compared between countries",
        "The framework makes no statement about the distribution of energy use"],
      ans=0,
      why="ENG-3.B.1 is a flat denial of even distribution between developed and developing "
          "countries. The rejected options accept the student's claim, narrow it, or deny that "
          "the framework speaks to it."),

 dict(q="A second student writes that a country's reliance on fossil fuels falls as it becomes "
        "more developed. Which correction is required?",
      choices=[
        "The framework has that reliance INCREASING as a developing country becomes more "
        "developed",
        "The framework has that reliance decreasing, so the student is correct",
        "The framework has that reliance unchanged as a country develops",
        "The framework speaks only about developed countries, not developing ones",
        "The framework makes no statement about reliance on fossil fuels"],
      ans=0,
      why="ENG-3.B.3 states that AS DEVELOPING COUNTRIES BECOME MORE DEVELOPED, THEIR RELIANCE "
          "ON FOSSIL FUELS FOR ENERGY INCREASES. The direction is the whole content of the "
          "statement, which is why the mistake is worth naming."),

 dict(q="Which single comparison would most directly report the unevenness the framework "
        "names?",
      choices=[
        "Energy used for each person in developed countries set beside energy used for each "
        "person in developing countries",
        "Total energy used by developed countries set beside their total industrial output",
        "The price of fuel in developed countries set beside its price in developing "
        "countries",
        "The number of energy sources available in each group of countries",
        "The year in which each country first used fossil fuels"],
      ans=0,
      why="ENG-3.B.1 is about the distribution of use between the two groups, and a per-person "
          "comparison is what shows it while totals alone can conceal it. Price, source counts "
          "and dates are outside the statement."),

 dict(q="Which single observation would most directly report the trend ENG-3.B.4 describes?",
      choices=[
        "World energy demand rising over the same decades in which world industrial output "
        "rose",
        "World energy demand rising over decades in which world industrial output fell",
        "One developed country's energy demand rising while its industrial output fell",
        "The price of one fuel rising in one district over one decade",
        "The share of one country's energy that comes from fossil fuels rising"],
      ans=0,
      why="ENG-3.B.4 ties rising demand for energy to the world becoming more industrialized, so "
          "the two quantities must move together and both must be measured for the world. The "
          "last rejected option reports ENG-3.B.3 instead, which is a different statement."),

 dict(q="A district switches from one fuel to another after the national government forbids the "
        "first. Which of the framework's influences does that illustrate?",
      choices=[
        "Governmental regulations",
        "The price of the fuel",
        "How much of the fuel is available nearby",
        "The climate of the district",
        "None of the three influences the framework names, since a prohibition is not one"],
      ans=0,
      why="ENG-3.B.5 names availability, price and GOVERNMENTAL REGULATIONS as the three "
          "influences on which energy sources people use and how they use them, and a national "
          "prohibition is a governmental regulation. Nothing in the case turns on cost or on "
          "whether the fuel exists nearby."),

 dict(q="A second district switches away from a fuel after its cost for each unit of energy "
        "doubles. Which of the framework's influences does that illustrate?",
      choices=[
        "The price of the fuel",
        "Governmental regulations",
        "How much of the fuel is available nearby",
        "The age of the equipment that burns it",
        "None of the three influences the framework names, since cost is not one of them"],
      ans=0,
      why="ENG-3.B.5 names availability, PRICE and governmental regulations, and a change in "
          "cost for each unit of energy is a change in price. No rule was made and no supply "
          "disappeared in the case described."),

 dict(q="Which of the following does this topic's five statements NOT supply?",
      choices=[
        "A figure for how much more energy a developed country uses than a developing one",
        "The claim that energy use is unevenly distributed between the two groups",
        "The claim that fossil fuels are the most widely used sources globally",
        "The claim that industrialization raises the demand for energy",
        "The claim that availability, price and regulation influence which sources are used"],
      ans=0,
      why="ENG-3.B.1 through B.5 give directions and lists and not one number: no percentage, no "
          "per-person figure, no country and no year appears in any of them. Each rejected "
          "option quotes a claim the statements do make."),

 dict(q="How do this topic's five statements stand in relation to one another?",
      choices=[
        "Two describe how use is spread and what dominates it, two describe how use changes "
        "as countries and the world develop, and one names what influences the choice of "
        "source",
        "All five describe how energy use is spread between developed and developing "
        "countries",
        "All five describe what influences the choice of energy source",
        "Four give numerical estimates and the fifth gives a definition",
        "The five statements concern five different countries and cannot be applied together"],
      ans=0,
      why="ENG-3.B.1 and B.2 describe the present pattern, B.3 and B.4 describe change over "
          "time in a country and in the world, and B.5 names availability, price and "
          "governmental regulations as the influences. None of the five supplies a number."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Energy use is unevenly distributed between developed and developing countries; "
        "fossil fuels are the most widely used sources globally; reliance on fossil fuels "
        "rises as a developing country develops; demand rises as the world industrializes; "
        "and availability, price and regulation influence which sources people use.",
        "Energy use is evenly distributed between developed and developing countries, and "
        "fossil fuels are the least used sources globally.",
        "Reliance on fossil fuels falls as a developing country develops, and world demand "
        "falls as the world industrializes.",
        "Climate and population are what influence which energy sources people use, and the "
        "framework names no trend in demand.",
        "The framework supplies exact figures for energy use in each group of countries."],
      ans=0,
      why="The keyed summary carries all five statements in the framework's own directions and "
          "adds nothing. Each rejected summary reverses a direction, substitutes influences the "
          "framework never names, or claims figures the framework does not give."),
]
