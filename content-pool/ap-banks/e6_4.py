# AP ENVIRONMENTAL SCIENCE 6.4 Distribution of Natural Energy Resources
# CED effective Fall 2026, Unit 6 Energy Resources and Consumption.
# Enduring understanding ENG-3: humans use energy from a variety of sources, resulting in
# positive and negative consequences.
# Learning objective ENG-3.D, identify where natural energy resources occur.
# Suggested skill 2.B, explain relationships between different characteristics of
# environmental concepts, processes, or models represented visually, in theoretical and in
# applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-3.D.1  The global distribution of natural energy resources, such as ores, coal,
#              crude oil, and gas, is not uniform and depends on regions' geologic history.
#
# ONE SENTENCE, AND THAT IS THE WHOLE TOPIC. Everything keyed here comes out of its four
# parts and nothing else:
#   1. the subject is the GLOBAL DISTRIBUTION of natural energy resources,
#   2. the examples are ORES, COAL, CRUDE OIL, AND GAS, introduced by SUCH AS,
#   3. the distribution IS NOT UNIFORM,
#   4. it DEPENDS ON REGIONS' GEOLOGIC HISTORY.
#
# SUCH AS MEANS THE LIST IS OPEN. One item keys that the four named resources are examples
# rather than a complete list, so nothing here treats the list as exhaustive and no item
# asks a student to rule a resource out of it.
#
# THE BOUNDARY THAT MATTERS MOST. ENG-3.D.1 is about where resources OCCUR. ENG-3.B.1, in
# topic 6.2, is about how energy USE is spread between developed and developing countries.
# Both are statements about uneven distribution and they are easily merged, so two items
# key the difference and their anchors carry both halves.
#
# THE SUGGESTED SKILL IS 2.B and would normally be taught from a world resource map. THE
# BANK CANNOT CARRY IMAGES, so every spatial item prints its occurrence data in a table=
# and asks the question of the table. Nothing here refers to a picture.
#
# WHAT IS NOT KEYED. The framework attributes the pattern to geologic history and stops
# there; it names no mechanism by which particular rocks come to hold particular fuels, so
# no key asserts one. Where a table pairs a rock type with an occurrence, the conclusion
# keyed is that occurrence tracks the region's geology rather than its area, which is
# ENG-3.D.1's own claim and no more.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("6.4", "Distribution of Natural Energy Resources", 6)

_T_REGION = dict(
    headers=["Region",
             "Recoverable coal (billion energy units)",
             "Recoverable crude oil (billion energy units)",
             "Recoverable natural gas (billion energy units)"],
    rows=[["Region 1", "900", "40", "60"],
          ["Region 2", "30", "720", "500"],
          ["Region 3", "60", "10", "40"],
          ["Region 4", "10", "30", "0"]])

_T_HISTORY = dict(
    headers=["Region",
             "Rock underlying most of the region",
             "Recoverable crude oil (billion energy units)",
             "Area of the region (thousand square kilometers)"],
    rows=[["Region A", "Ancient marine sedimentary rock", "600", "200"],
          ["Region B", "Ancient marine sedimentary rock", "450", "150"],
          ["Region C", "Recent volcanic rock", "0", "600"],
          ["Region D", "Recent volcanic rock", "0", "300"]])

_T_SUPPLY = dict(
    headers=["Country",
             "Natural gas produced at home in a year (billion energy units)",
             "Natural gas used in a year (billion energy units)"],
    rows=[["Country 1", "300", "120"],
          ["Country 2", "0", "180"],
          ["Country 3", "40", "200"]])

QUESTIONS = [

 dict(q="What does the course framework say about the global distribution of natural energy "
        "resources?",
      choices=[
        "That it is not uniform",
        "That it is uniform across the world",
        "That it is uniform within each continent but not between continents",
        "That it cannot be described at a global scale",
        "The framework makes no statement about how those resources are distributed"],
      ans=0,
      why="ENG-3.D.1 states that the global distribution of natural energy resources IS NOT "
          "UNIFORM. The rejected options reverse the claim, restrict it to a scale the statement "
          "does not use, or deny that the framework speaks to the question."),

 dict(q="On what does the framework say that distribution depends?",
      choices=[
        "The geologic history of the regions",
        "The size of each region's population",
        "How much energy each region uses in a year",
        "The wealth of the countries in each region",
        "The energy policies each government has adopted"],
      ans=0,
      why="ENG-3.D.1 states that the distribution DEPENDS ON REGIONS' GEOLOGIC HISTORY. "
          "Population, consumption, wealth and policy are each treated somewhere in this unit, "
          "but none of them appears in this statement."),

 dict(q="Which resources does that statement give as its examples?",
      choices=[
        "Ores, coal, crude oil, and gas",
        "Sunlight, wind, flowing water, and heat from the Earth's interior",
        "Coal, peat, firewood, and charcoal",
        "Ores, uranium, sunlight, and wind",
        "Crude oil, gas, ethanol, and hydrogen"],
      ans=0,
      why="ENG-3.D.1 names ORES, COAL, CRUDE OIL, AND GAS as its examples of natural energy "
          "resources. The rejected lists are drawn from other topics of this unit, which treat "
          "sunlight, wind, water, biomass and hydrogen separately."),

 dict(q="Which of the following is NOT one of the four resources that statement names?",
      choices=[
        "Flowing water in rivers",
        "Ores",
        "Coal",
        "Crude oil",
        "Gas"],
      ans=0,
      why="ENG-3.D.1's four examples are ores, coal, crude oil and gas. Flowing water is treated "
          "in the framework's statements about hydroelectric power rather than in this one, and "
          "each rejected option quotes the statement directly."),

 dict(q="The statement introduces its four resources with the words such as. What does that "
        "establish?",
      choices=[
        "That the four are examples of natural energy resources rather than a complete list",
        "That the four are the only natural energy resources there are",
        "That the four are the only resources whose distribution is uneven",
        "That the four resources are found together wherever any of them occurs",
        "That the four resources are listed in order of how unevenly they are distributed"],
      ans=0,
      why="The words SUCH AS mark a list as illustrative, so ENG-3.D.1 offers ores, coal, crude "
          "oil and gas as examples and does not close the category. Nothing in the statement "
          "orders the four or claims they occur together."),

 dict(q="What does the phrase about uniformity establish about how much of a resource different "
        "regions hold?",
      choices=[
        "Some regions hold far more of a given resource than other regions do",
        "Every region holds about the same amount of each resource",
        "No region holds any appreciable amount of any resource",
        "Every resource is confined to a single region of the world",
        "The amount a region holds changes from one year to the next"],
      ans=0,
      why="ENG-3.D.1 denies uniformity, which is a claim that the amounts differ across regions. "
          "It does not say the amounts are equal, that they are everywhere negligible, that a "
          "resource sits in one region only, or that a region's endowment varies by year."),

 dict(q="Two statements in this unit describe something as unevenly distributed. How do they "
        "differ?",
      choices=[
        "One is about where natural energy resources occur; the other is about how energy use "
        "is spread between developed and developing countries",
        "One is about how energy use is spread between developed and developing countries; the "
        "other is about how evenly the world's population is spread",
        "One is about where natural energy resources occur; the other is about which fuels "
        "burn most cleanly",
        "Both are about where natural energy resources occur",
        "Both are about how energy use is spread between developed and developing countries"],
      ans=0,
      why="ENG-3.D.1 is about the occurrence of resources and rests on geologic history, while "
          "ENG-3.B.1 in topic 6.2 is about the distribution of energy USE between developed and "
          "developing countries. Different subject, different explanation, and neither concerns "
          "population or the cleanliness of a fuel."),

 dict(q="Which question does the framework's statement about occurrence answer?",
      choices=[
        "Where the world's natural energy resources are found",
        "How much energy each group of countries consumes",
        "Which of the fossil fuels burns most cleanly",
        "Whether a given energy source is renewable",
        "What a government should do about its energy supply"],
      ans=0,
      why="ENG-3.D.1 sits under the learning objective identify where natural energy resources "
          "occur, so it answers a question about location. Consumption is ENG-3.B, cleanliness is "
          "ENG-3.C.4, and whether a source is renewable is ENG-3.A in topic 6.1."),

 dict(q="A region is found to hold no coal at all. What does the framework's statement license a "
        "student to conclude?",
      choices=[
        "That coal is not uniformly distributed, and nothing about the region's other resources",
        "That the region holds no natural energy resources of any kind",
        "That the region must import all of the energy it uses",
        "That the region's geologic history is the same as its neighbours'",
        "That the region will hold coal again within a few decades"],
      ans=0,
      why="ENG-3.D.1 asserts an uneven distribution that depends on geologic history and says "
          "nothing about any one region's full endowment, its trade, or how its history compares "
          "with a neighbour's. A single absence is an instance of the unevenness and no more."),

 dict(q="Two neighbouring countries share a border; one has large gas fields and the other has "
        "none. Which of the framework's claims does the contrast illustrate?",
      choices=[
        "That the global distribution of natural energy resources is not uniform and depends on "
        "geologic history",
        "That the global distribution of natural energy resources is uniform once a large "
        "enough area is considered",
        "That energy use is not evenly distributed between developed and developing countries",
        "That the most widely used sources of energy globally are fossil fuels",
        "That availability, price and governmental regulations influence which sources people "
        "use"],
      ans=0,
      why="Two adjoining areas differing sharply in what they hold is exactly the unevenness "
          "ENG-3.D.1 describes, and the statement attributes such differences to the regions' "
          "geologic history. The rejected options quote statements about use rather than about "
          "occurrence."),

 dict(q="A geologist accounts for one country's crude oil by the conditions under which the "
        "rocks beneath it were laid down. Is that consistent with the framework?",
      choices=[
        "Yes, because the framework makes occurrence depend on the geologic history of regions",
        "Yes, but only because the country also uses a great deal of energy",
        "No, because the framework makes occurrence depend on how much energy a region uses",
        "No, because the framework makes occurrence depend on a region's climate",
        "The framework gives no account of why resources occur where they do"],
      ans=0,
      why="ENG-3.D.1 states that the distribution DEPENDS ON REGIONS' GEOLOGIC HISTORY, which is "
          "an account in terms of how the rocks of a place came to be. Consumption, climate and "
          "wealth are not part of the statement, and it plainly does give an account."),

 dict(q="Which account of why a country holds crude oil is NOT consistent with the framework's "
        "statement?",
      choices=[
        "The country holds oil because its people consume a great deal of energy",
        "The rocks beneath the country formed under conditions that left oil in them",
        "The country's geologic history differs from that of its neighbour, which holds none",
        "The world's oil is not uniformly distributed, and this country lies where some of it "
        "is",
        "Different regions have different geologic histories, and this one has oil"],
      ans=0,
      why="ENG-3.D.1 makes occurrence depend on geologic history, so an explanation from the "
          "level of consumption reverses cause and effect and imports a statement about use into "
          "a statement about occurrence. Every rejected option is a restatement of the framework's "
          "own account."),

 dict(q="Which observation would most directly report the claim ENG-3.D.1 makes?",
      choices=[
        "The recoverable amount of one resource measured in each of several regions and "
        "compared across them",
        "The amount of energy consumed for each person in each of several countries",
        "The price of one fuel recorded in several markets over one year",
        "The share of one country's electricity that comes from fossil fuels",
        "The number of years a country's government has regulated its fuel market"],
      ans=0,
      why="ENG-3.D.1 is a claim about how much of a resource occurs in one place against another, "
          "so measuring the endowment region by region is what tests it. Consumption, price, fuel "
          "mix and regulation belong to other statements in this unit."),

 dict(q="A student writes that natural energy resources are spread evenly across the world. "
        "Which correction is required?",
      choices=[
        "The framework states that the global distribution is NOT uniform",
        "The framework states that the distribution is uniform, so the student is correct",
        "The framework states that the distribution is uniform within each region",
        "The framework states that the distribution cannot be described",
        "The framework makes no statement about the distribution of those resources"],
      ans=0,
      why="ENG-3.D.1 denies uniformity in so many words. The rejected corrections accept the "
          "student's sentence, narrow the claim to a scale the statement does not use, or deny "
          "that the framework addresses the question at all."),

 dict(q="A second student writes that a region holds the resources it does because of how much "
        "energy its people use. Which correction is required?",
      choices=[
        "The framework makes occurrence depend on the geologic history of the region",
        "The framework makes occurrence depend on the region's level of consumption, so the "
        "student is correct",
        "The framework makes occurrence depend on the region's rainfall and climate",
        "The framework makes occurrence depend on the wealth of the region",
        "The framework offers no explanation of occurrence at all"],
      ans=0,
      why="ENG-3.D.1 attributes the pattern to REGIONS' GEOLOGIC HISTORY. Consumption is the "
          "subject of ENG-3.B in topic 6.2 and is an effect of what people do rather than a cause "
          "of what lies underground."),

 dict(q="Which further statement in this unit connects an uneven endowment to what people "
        "actually end up burning?",
      choices=[
        "That availability, price and governmental regulations influence which energy sources "
        "people use",
        "That nuclear power generation is a nonrenewable energy source",
        "That wind energy is a renewable, clean source of energy",
        "That natural gas is the cleanest of the fossil fuels",
        "That cogeneration yields both useful heat and electricity from one fuel source"],
      ans=0,
      why="ENG-3.B.5 names availability among the three influences on which energy sources people "
          "use, and what a region holds is what is available there. The rejected statements "
          "classify or describe particular sources without bearing on the choice between them."),

 dict(q="Which statement restates ENG-3.D.1 without adding to it or leaving anything out?",
      choices=[
        "The global distribution of natural energy resources, ores, coal, crude oil and gas "
        "among them, is not uniform and depends on the geologic history of regions",
        "The global distribution of natural energy resources is not uniform and depends on how "
        "much energy each region consumes",
        "The global distribution of natural energy resources is uniform and depends on the "
        "geologic history of regions",
        "Ores, coal, crude oil and gas are the only natural energy resources, and each is "
        "confined to one region",
        "The global distribution of natural energy resources cannot be established, because "
        "geologic history is unknown"],
      ans=0,
      why="The keyed sentence carries all four parts of ENG-3.D.1: the subject, the four examples "
          "offered as examples, the denial of uniformity and the dependence on geologic history. "
          "Each rejected version swaps the explanation, reverses the uniformity claim, closes the "
          "open list, or denies that the claim can be made."),

 dict(q="Why is a claim about where resources occur worth stating separately from a claim about "
        "who uses energy?",
      choices=[
        "Because a region may hold a great deal of a resource and use little energy, or hold "
        "none and use a great deal",
        "Because the two claims are the same claim expressed in different words",
        "Because the framework states that the two always move together",
        "Because occurrence and use are both explained by geologic history",
        "Because the framework makes no claim about who uses energy"],
      ans=0,
      why="ENG-3.D.1 and ENG-3.B.1 are separate statements with separate subjects, so nothing in "
          "the framework ties a region's endowment to its consumption. Geologic history explains "
          "occurrence only, and the framework does address consumption, at length."),

 dict(q="Four regions were surveyed for the amounts of three resources each can recover. Which "
        "conclusion do the values support?",
      table=_T_REGION,
      choices=[
        "The three resources are unevenly distributed, and the region richest in one is not "
        "the region richest in another",
        "The three resources are evenly distributed across the four regions",
        "One region holds the largest amount of all three resources",
        "The four regions hold equal amounts of coal and differ only in crude oil",
        "No region holds any appreciable amount of natural gas"],
      ans=0,
      why="Coal runs 900, 30, 60 and 10 billion energy units, crude oil runs 40, 720, 10 and 30, "
          "and natural gas runs 60, 500, 40 and 0, so the leader differs between coal and the "
          "other two. ENG-3.D.1 states that the global distribution of such resources is not "
          "uniform."),

 dict(q="Using the same four regions, what share of the recoverable coal lies in the region that "
        "holds the most of it?",
      table=_T_REGION,
      choices=[
        "90 percent",
        "50 percent",
        "30 percent",
        "9 percent",
        "25 percent"],
      ans=0,
      why="The four coal figures are 900, 30, 60 and 10 billion energy units, which total 1,000, "
          "and 900 of 1,000 is 90 percent. The rejected values assume an even split between two "
          "or four regions, drop a power of ten, or take a third."),

 dict(q="Using the same four regions, how many times as much recoverable coal does the richest "
        "hold as the region with the second largest amount?",
      table=_T_REGION,
      choices=[
        "Fifteen times as much",
        "Thirty times as much",
        "Ninety times as much",
        "Three times as much",
        "The two hold the same amount"],
      ans=0,
      why="The two largest coal figures are 900 and 60 billion energy units, and 900 divided by "
          "60 is 15. The rejected values divide by the wrong row, drop a power of ten, or deny "
          "that the amounts differ."),

 dict(q="Using the same four regions, which one holds the most crude oil while holding almost "
        "none of the coal?",
      table=_T_REGION,
      choices=[
        "The second region, with 720 billion energy units of crude oil against 30 of coal",
        "The first region, with 900 billion energy units of coal against 40 of crude oil",
        "The third region, with 10 billion energy units of crude oil against 60 of coal",
        "The fourth region, with 30 billion energy units of crude oil against 10 of coal",
        "No region holds much of one resource and little of another"],
      ans=0,
      why="The second region holds 720 billion energy units of crude oil, the largest of the four, "
          "and 30 of coal, the second smallest. That a region can lead in one resource and trail "
          "in another is what ENG-3.D.1's denial of uniformity amounts to."),

 dict(q="Using the same four regions, which holds no recoverable natural gas at all?",
      table=_T_REGION,
      choices=[
        "The fourth region",
        "The first region",
        "The second region",
        "The third region",
        "Every region holds some recoverable natural gas"],
      ans=0,
      why="The natural gas figures are 60, 500, 40 and 0 billion energy units, so only the fourth "
          "region has none. An endowment of nothing beside a neighbour's 500 is the sharpest form "
          "of the unevenness ENG-3.D.1 describes."),

 dict(q="Four other regions were logged with the rock beneath them, the crude oil they can "
        "recover and their area. Which conclusion do the values support?",
      table=_T_HISTORY,
      choices=[
        "Crude oil occurs in the regions with one kind of rock and not in the others, while the "
        "area of a region does not track what it holds",
        "Crude oil occurs in the regions with the largest area, whatever rock lies beneath them",
        "Crude oil occurs in every region, in amounts that rise with area",
        "The kind of rock beneath a region and what it holds are unrelated in this record",
        "The two regions of recent volcanic rock hold the most crude oil"],
      ans=0,
      why="The two regions of ancient marine sedimentary rock hold 600 and 450 billion energy "
          "units of crude oil while the two of recent volcanic rock hold none, and the largest "
          "region by area holds none. ENG-3.D.1 makes occurrence depend on the geologic history "
          "of regions rather than on their size."),

 dict(q="Using those same four regions, how much crude oil in total lies under the ancient marine "
        "sedimentary rock?",
      table=_T_HISTORY,
      choices=[
        "1,050 billion energy units",
        "600 billion energy units",
        "450 billion energy units",
        "150 billion energy units",
        "None, because that rock holds no crude oil"],
      ans=0,
      why="Adding the two tabulated amounts gives 600 plus 450, which is 1,050 billion energy "
          "units. The rejected values quote one region alone, take the difference between them, "
          "or deny an occurrence the record plainly shows."),

 dict(q="Using those same four regions, how much of the surveyed area holds no recoverable crude "
        "oil at all?",
      table=_T_HISTORY,
      choices=[
        "900 thousand square kilometers",
        "350 thousand square kilometers",
        "600 thousand square kilometers",
        "300 thousand square kilometers",
        "None of it, since every region holds some crude oil"],
      ans=0,
      why="The two regions holding no crude oil cover 600 and 300 thousand square kilometers, "
          "which is 900 between them, and they are the larger part of the surveyed area. The "
          "rejected values quote one of those regions alone or add the two that do hold oil."),

 dict(q="Three countries were compared on the natural gas each produces at home and the amount "
        "each uses. Which country must obtain all of its gas from beyond its own borders?",
      table=_T_SUPPLY,
      choices=[
        "The second country, which produces none and uses 180 billion energy units",
        "The first country, which produces 300 billion energy units and uses 120",
        "The third country, which produces 40 billion energy units and uses 200",
        "Every country in the record, since none produces as much as it uses",
        "No country in the record, since each produces some of what it uses"],
      ans=0,
      why="The second country produces nothing and uses 180 billion energy units, so all of it "
          "must come from elsewhere, while the third produces part of what it uses and the first "
          "produces more than it uses. ENG-3.D.1's uneven endowment is what puts countries in "
          "such different positions."),

 dict(q="Using the same three countries, how much more natural gas does the third use in a year "
        "than it produces?",
      table=_T_SUPPLY,
      choices=[
        "160 billion energy units",
        "200 billion energy units",
        "240 billion energy units",
        "180 billion energy units",
        "It produces more than it uses"],
      ans=0,
      why="Subtracting the two tabulated amounts gives 200 minus 40, which is 160 billion energy "
          "units. The rejected values quote its consumption alone, add the two, quote another "
          "country's consumption, or invert the direction the record shows."),

 dict(q="Using the same three countries, which produces more natural gas than it uses, and by how "
        "much?",
      table=_T_SUPPLY,
      choices=[
        "The first country, by 180 billion energy units",
        "The first country, by 420 billion energy units",
        "The second country, by 180 billion energy units",
        "The third country, by 160 billion energy units",
        "No country produces more than it uses"],
      ans=0,
      why="The first country produces 300 billion energy units and uses 120, a surplus of 180, "
          "while the other two use more than they produce. The rejected values add the two "
          "amounts instead of subtracting them or attach the surplus to the wrong country."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "The global distribution of natural energy resources, among them ores, coal, crude oil "
        "and gas, is not uniform, and it depends on the geologic history of regions.",
        "The global distribution of natural energy resources is uniform, and any apparent "
        "difference between regions comes from how much each one uses.",
        "The global distribution of natural energy resources is not uniform, and it depends on "
        "the wealth and the population of each region.",
        "Ores, coal, crude oil and gas are the only natural energy resources, and each occurs "
        "in exactly one region of the world.",
        "The framework gives figures for how much of each resource every region holds."],
      ans=0,
      why="The keyed summary carries ENG-3.D.1 whole: the subject, the four examples, the denial "
          "of uniformity and the dependence on geologic history. Each rejected summary reverses "
          "the uniformity claim, swaps the explanation, closes a list the framework leaves open, "
          "or claims figures the framework never supplies."),
]
