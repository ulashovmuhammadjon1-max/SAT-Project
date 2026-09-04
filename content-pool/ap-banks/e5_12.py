# AP ENVIRONMENTAL SCIENCE 5.12 Introduction to Sustainability
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding STB-1: humans can mitigate their impact on land and water
# resources through sustainable use.
# Learning objective STB-1.A, explain the concept of sustainability.
# Suggested skill 5.E, explain what the data implies or illustrates about environmental
# issues.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-1.A.1  Sustainability refers to humans living on Earth and their use of resources
#              without depletion of the resources for future generations. Environmental
#              indicators that can guide humans to sustainability include biological
#              diversity, food production, average global surface temperatures and CO2
#              concentrations, human population, and resource depletion.
#   STB-1.A.2  Sustainable yield is the amount of a renewable resource that can be taken
#              without reducing the available supply.
#
# SCOPE. One definition, one list of indicators, one quantity. The list is biological
# diversity, food production, average global surface temperatures and CO2 concentrations,
# human population, and resource depletion -- and the framework's word is INCLUDE, so no
# item here says the list is exhaustive and no item counts it. The framework sets no
# numerical threshold, ranks no indicator above another, and names no country or year;
# one item keys that absence rather than working round it.
#
# BOUNDARY WITH 5.8. STB-1.A.2 is already the backbone of topic 5.8's causal items, where
# it is applied to a fish stock. Nothing here reuses that setting or that question shape:
# the yield items in this module ask which KIND of resource the definition is stated for,
# what the phrase "without reducing the available supply" requires of a harvest, and why
# the maximum a resource can physically produce is not the same thing. The worked
# settings are a forest and an aquifer, never a fishery.
#
# BOUNDARY WITH 5.11. An ecological footprint under EIN-2.N.1 is a MEASURE that compares
# resource demands and waste production. Sustainability under STB-1.A.1 is a GOAL. Two
# items turn on keeping the two apart, and EIN-2.N.1 appears here only as a named chain.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_12.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.12", "Introduction to Sustainability", 5)

_T_FOREST = dict(
    headers=["Estate",
             "New timber grown each year (thousand cubic meters)",
             "Timber cut each year (thousand cubic meters)"],
    rows=[["Estate 1", "40", "25"],
          ["Estate 2", "40", "40"],
          ["Estate 3", "40", "55"],
          ["Estate 4", "40", "70"]])

_T_AQUIFER = dict(
    headers=["District",
             "Water recharged to the aquifer each year (million cubic meters)",
             "Water pumped out each year (million cubic meters)"],
    rows=[["District 1", "18", "12"],
          ["District 2", "9", "14"],
          ["District 3", "25", "25"]])

_T_INDIC = dict(
    headers=["Reading taken in the region",
             "First survey",
             "Survey thirty years later"],
    rows=[["Bird species breeding in the region (number)", "180", "126"],
          ["Grain produced (million tonnes a year)", "9", "14"],
          ["Carbon dioxide in the atmosphere (parts per million)", "340", "420"],
          ["Human population (millions)", "20", "34"]])

_T_CLIMATE = dict(
    headers=["Decade of the record",
             "Average global surface temperature (degrees Celsius)",
             "Carbon dioxide in the atmosphere (parts per million)"],
    rows=[["First", "14.0", "330"],
          ["Second", "14.2", "350"],
          ["Third", "14.5", "375"],
          ["Fourth", "14.9", "410"]])

_T_FOOD = dict(
    headers=["Decade of the record",
             "Food produced (million tonnes a year)",
             "People to be fed (millions)"],
    rows=[["First", "30", "20"],
          ["Second", "42", "30"],
          ["Third", "50", "40"],
          ["Fourth", "54", "54"]])

QUESTIONS = [

 dict(q="How does the course framework define sustainability?",
      choices=[
        "Humans living on Earth and using resources without depleting those resources for "
        "future generations",
        "Humans living on Earth while leaving every natural resource entirely untouched",
        "Humans using resources at whatever rate the present generation can afford",
        "Humans replacing every natural resource with a manufactured substitute",
        "Humans depleting resources slowly enough that the depletion is not noticed"],
      ans=0,
      why="STB-1.A.1 states that sustainability refers to humans LIVING ON EARTH AND THEIR USE "
          "OF RESOURCES WITHOUT DEPLETION OF THE RESOURCES FOR FUTURE GENERATIONS. The rejected "
          "options either forbid use altogether or drop the requirement about future "
          "generations."),

 dict(q="What does the phrase about future generations add to the framework's definition?",
      choices=[
        "It makes the test whether the resources will still be there for people who come "
        "later, not only whether present needs are met",
        "It makes the test whether present needs are met, and says nothing about people who "
        "come later",
        "It restricts the definition to resources that will run out within one lifetime",
        "It requires that future generations use less than the present one does",
        "It sets a fixed number of generations after which depletion is permitted"],
      ans=0,
      why="STB-1.A.1 defines sustainability as use WITHOUT DEPLETION OF THE RESOURCES FOR FUTURE "
          "GENERATIONS, so the standard is set by what remains for later people. The framework "
          "sets no number of generations and imposes no rule on how much future generations "
          "may use."),

 dict(q="Which set of readings does the framework give as environmental indicators that can "
        "guide humans to sustainability?",
      choices=[
        "Biological diversity, food production, average global surface temperatures and "
        "carbon dioxide concentrations, human population, and resource depletion",
        "Average household income, employment, industrial output, and the price of energy",
        "Rainfall, wind speed, day length, and soil colour",
        "Biological diversity, average household income, employment, and the price of grain",
        "The framework names no indicators of any kind"],
      ans=0,
      why="STB-1.A.1 lists biological diversity, food production, average global surface "
          "temperatures and CO2 concentrations, human population, and resource depletion. Each "
          "rejected list substitutes economic or ordinary weather measurements the statement "
          "does not name."),

 dict(q="Which of the following is NOT among the environmental indicators the framework "
        "lists?",
      choices=[
        "Average household income",
        "Biological diversity",
        "Food production",
        "Human population",
        "Resource depletion"],
      ans=0,
      why="STB-1.A.1's list is biological diversity, food production, average global surface "
          "temperatures and CO2 concentrations, human population, and resource depletion. "
          "Household income appears nowhere in the statement, while each of the other four "
          "options is quoted from it directly."),

 dict(q="For which kind of resource is a sustainable yield defined?",
      choices=[
        "A renewable resource",
        "A nonrenewable resource",
        "Any resource, renewable or not",
        "Only a resource that is already depleted",
        "Only a resource that no one currently uses"],
      ans=0,
      why="STB-1.A.2 states that sustainable yield is the amount of A RENEWABLE RESOURCE that "
          "can be taken without reducing the available supply. A nonrenewable source exists in a "
          "fixed amount under ENG-3.A.1, so there is no rate at which taking it leaves the "
          "supply unreduced."),

 dict(q="What does the framework's definition of sustainable yield require of a harvest?",
      choices=[
        "That it leave the available supply undiminished",
        "That it be the largest harvest the resource could physically produce in one year",
        "That it reduce the available supply by a small fixed share each year",
        "That it be taken from a resource that exists in a fixed amount",
        "That it stop all use of the resource for a period of years"],
      ans=0,
      why="STB-1.A.2 defines sustainable yield as the amount that can be taken WITHOUT REDUCING "
          "THE AVAILABLE SUPPLY, so the condition is on what is left behind. A harvest that "
          "reduces the supply by any share, however small, fails that condition."),

 dict(q="Four forest estates of the same size are compared in the table. Which reading "
        "matches the framework's definition of a sustainable yield?",
      table=_T_FOREST,
      choices=[
        "The first two estates take no more timber than the forest grows in a year, while "
        "the other two take more than it grows.",
        "The first two estates take more timber than the forest grows in a year, while the "
        "other two take no more than it grows.",
        "All four estates take exactly what the forest grows in a year.",
        "All four estates take more timber than the forest grows in a year.",
        "The amount a forest grows in a year has no bearing on whether a cut is "
        "sustainable."],
      ans=0,
      why="Growth is 40 thousand cubic meters on every estate while the cut runs 25, 40, 55 and "
          "70. STB-1.A.2 makes the sustainable amount the one that can be taken without reducing "
          "the available supply, and only the first two estates satisfy that."),

 dict(q="Using the same estates, by how much does the heaviest cut exceed what the forest "
        "grows in a year?",
      table=_T_FOREST,
      choices=[
        "By 30 thousand cubic meters",
        "By 70 thousand cubic meters",
        "By 110 thousand cubic meters",
        "By 15 thousand cubic meters",
        "By 45 thousand cubic meters"],
      ans=0,
      why="Subtracting the tabulated growth from the tabulated cut gives 70 minus 40, which is "
          "30 thousand cubic meters. The rejected values quote the cut alone, add the two, take "
          "the lightest estate's shortfall, or pair the wrong estate."),

 dict(q="Three districts drawing on separate aquifers are compared in the table. Which "
        "district is taking more than the framework's definition allows?",
      table=_T_AQUIFER,
      choices=[
        "The second district, which pumps out more than is recharged each year",
        "The first district, which pumps out more than is recharged each year",
        "The third district, which pumps out more than is recharged each year",
        "All three districts, since each pumps out more than is recharged",
        "None of them, since pumping cannot reduce an aquifer's supply"],
      ans=0,
      why="The first district recharges 18 and pumps 12, the second recharges 9 and pumps 14, "
          "and the third recharges 25 and pumps 25. STB-1.A.2 allows the amount that can be "
          "taken without reducing the available supply, so only the second district is over it."),

 dict(q="Using the same three districts, by how much does the over-drawn district exceed its "
        "recharge each year?",
      table=_T_AQUIFER,
      choices=[
        "By 5 million cubic meters",
        "By 14 million cubic meters",
        "By 23 million cubic meters",
        "By 6 million cubic meters",
        "By 9 million cubic meters"],
      ans=0,
      why="Subtracting the tabulated recharge from the tabulated pumping gives 14 minus 9, which "
          "is 5 million cubic meters. The rejected values quote the pumping alone, add the two, "
          "give the first district's unused margin, or quote the recharge alone."),

 dict(q="Four readings were taken in one region thirty years apart. Which reading of the "
        "record is correct?",
      table=_T_INDIC,
      choices=[
        "Biological diversity fell while food production, carbon dioxide and human "
        "population all rose.",
        "Biological diversity rose while food production, carbon dioxide and human "
        "population all fell.",
        "All four readings fell across the thirty years.",
        "All four readings rose across the thirty years.",
        "Food production fell while biological diversity rose."],
      ans=0,
      why="Breeding bird species fall from 180 to 126 while grain rises from 9 to 14 million "
          "tonnes, carbon dioxide from 340 to 420 parts per million and population from 20 to 34 "
          "million. All four are indicators STB-1.A.1 names, and they do not all move the "
          "same way."),

 dict(q="Using the same region, how many breeding bird species were lost across the thirty "
        "years?",
      table=_T_INDIC,
      choices=[
        "54 species",
        "180 species",
        "306 species",
        "14 species",
        "126 species"],
      ans=0,
      why="Subtracting the two tabulated counts gives 180 minus 126, which is 54 species. The "
          "rejected values quote the first survey alone, add the two, take the rise in the "
          "population row, or quote the later survey alone."),

 dict(q="Two of the framework's indicators were recorded together once each decade. What do "
        "the values show?",
      table=_T_CLIMATE,
      choices=[
        "Average global surface temperature and carbon dioxide concentration both rose "
        "across the record.",
        "Average global surface temperature and carbon dioxide concentration both fell "
        "across the record.",
        "Average global surface temperature rose while carbon dioxide concentration fell.",
        "Carbon dioxide concentration rose while average global surface temperature fell.",
        "Neither reading changed across the record."],
      ans=0,
      why="Temperature runs 14.0, 14.2, 14.5 and 14.9 degrees Celsius while carbon dioxide runs "
          "330, 350, 375 and 410 parts per million, both rising throughout. STB-1.A.1 names "
          "average global surface temperatures and CO2 concentrations together in its list of "
          "indicators."),

 dict(q="Using the same decades, by how much did the carbon dioxide concentration rise across "
        "the whole record?",
      table=_T_CLIMATE,
      choices=[
        "By 80 parts per million",
        "By 410 parts per million",
        "By 740 parts per million",
        "By 35 parts per million",
        "By 330 parts per million"],
      ans=0,
      why="Subtracting the two tabulated concentrations gives 410 minus 330, which is 80 parts "
          "per million. The rejected values quote the final reading alone, add the two, take one "
          "decade's step, or quote the opening reading alone."),

 dict(q="Food production and the number of people to be fed were recorded once each decade. "
        "Which conclusion do the values support?",
      table=_T_FOOD,
      choices=[
        "Food production rose across the record, but the food available for each person "
        "fell.",
        "Food production rose across the record, and the food available for each person rose "
        "with it.",
        "Food production fell across the record, and the food available for each person fell "
        "with it.",
        "Food production fell across the record, but the food available for each person "
        "rose.",
        "The food available for each person cannot be worked out from these two columns."],
      ans=0,
      why="Production rises from 30 to 54 million tonnes while the people to be fed rise from 20 "
          "to 54 million, so the amount for each person falls from 1.5 to 1.0 tonnes. Food "
          "production and human population are both indicators STB-1.A.1 names, and reading "
          "either alone would mislead."),

 dict(q="Using the same decades, by how much did the food available for each person fall "
        "between the first decade and the fourth?",
      table=_T_FOOD,
      choices=[
        "By 0.5 tonnes per person",
        "By 1.5 tonnes per person",
        "By 1.0 tonnes per person",
        "By 0.25 tonnes per person",
        "By 0.1 tonnes per person"],
      ans=0,
      why="Dividing each decade's production by its population gives 30 over 20, or 1.5 tonnes "
          "per person, and 54 over 54, or 1.0, a fall of 0.5. The rejected values quote one of "
          "the two ratios alone or take the change over a single decade."),

 dict(q="A conservation body claims that a region's biological diversity is falling. Which of "
        "the framework's indicators does that claim rest on, and what would measure it?",
      choices=[
        "Biological diversity, measured by the number of species recorded in repeated "
        "surveys of the region",
        "Food production, measured by the grain harvested in the region each year",
        "Human population, measured by the number of people living in the region",
        "Resource depletion, measured by the tonnes of ore mined in the region each year",
        "Average global surface temperature, measured at stations across the region"],
      ans=0,
      why="STB-1.A.1 lists biological diversity as one of the indicators that can guide humans "
          "to sustainability, and a count of species present in repeated surveys measures it "
          "directly. Each rejected option names a different indicator from the same list."),

 dict(q="Which two readings does the framework name together as one item within its list of "
        "indicators?",
      choices=[
        "Average global surface temperatures and carbon dioxide concentrations",
        "Biological diversity and human population",
        "Food production and resource depletion",
        "Human population and average global surface temperatures",
        "Resource depletion and biological diversity"],
      ans=0,
      why="STB-1.A.1's list reads biological diversity, food production, average global surface "
          "temperatures and CO2 concentrations, human population, and resource depletion, so the "
          "temperature and the concentration are joined in a single item. Each rejected pair "
          "joins two items the statement lists separately."),

 dict(q="A student writes that sustainability, as the framework defines it, means using no "
        "natural resources at all. Which correction is required?",
      choices=[
        "The definition is about USE without depletion, not about abstaining from use",
        "The definition is about abstaining from use, and the student has stated it "
        "correctly",
        "The definition is about use without regard to what remains for later people",
        "The definition applies only to resources that cannot be renewed",
        "The framework offers no definition of sustainability at all"],
      ans=0,
      why="STB-1.A.1 speaks of humans living on Earth AND THEIR USE OF RESOURCES without "
          "depletion for future generations, so use is assumed and the condition is on "
          "depletion. Dropping the future-generations clause makes the opposite error."),

 dict(q="A forest manager says that a sustainable yield is simply the largest harvest a stand "
        "can physically produce in one year. Which correction does the framework require?",
      choices=[
        "The largest possible harvest may still reduce the available supply, and the "
        "framework's test is that the supply is not reduced",
        "The largest possible harvest can never reduce the available supply, so the manager "
        "is correct",
        "The framework defines the sustainable yield as half of the largest possible harvest",
        "The framework defines the sustainable yield only for nonrenewable resources",
        "The framework gives no test for how much may be taken"],
      ans=0,
      why="STB-1.A.2 sets the test as taking WITHOUT REDUCING THE AVAILABLE SUPPLY, which is a "
          "condition on the stock left behind rather than on what the stand could yield if "
          "pushed. The framework supplies no fraction and no exemption for nonrenewables."),

 dict(q="Why is the framework's definition of the yield stated for a renewable resource in "
        "particular?",
      choices=[
        "A renewable resource is replenished naturally at or near the rate of consumption, "
        "so there is a rate of taking that leaves the supply unreduced",
        "A renewable resource exists in a fixed amount, so any taking at all leaves the "
        "supply unreduced",
        "A renewable resource cannot be depleted no matter how fast it is taken",
        "A nonrenewable resource is replenished faster than it is consumed",
        "The framework applies the definition equally to both kinds of resource"],
      ans=0,
      why="STB-1.A.2 states the yield for a renewable resource, and ENG-3.A.2 defines renewable "
          "sources as those replenished naturally at or near the rate of consumption, which is "
          "what makes a non-depleting rate of taking possible. ENG-3.A.1 puts nonrenewable "
          "sources in a fixed amount."),

 dict(q="A rangeland manager wants to set an annual take of hay that meets the framework's "
        "test. Which two quantities are the minimum needed?",
      choices=[
        "How much the rangeland grows back each year, and how much is cut each year",
        "How much is cut each year, and how many people the hay will feed",
        "How much the rangeland grows back each year, and the market price of hay",
        "The area of the rangeland, and the number of years it has been in use",
        "The rainfall over the rangeland, and the number of livestock in the district"],
      ans=0,
      why="STB-1.A.2 compares what is taken with what leaves the available supply unreduced, so "
          "the test needs the regrowth and the take. Price, area, rainfall and headcount say "
          "nothing about whether the supply is being reduced."),

 dict(q="What does the framework say its environmental indicators do?",
      choices=[
        "They can guide humans to sustainability",
        "They prove that any given society is already sustainable",
        "They replace the need to measure resource depletion",
        "They set the maximum amount of any resource that may be taken",
        "They apply only after a resource has already been depleted"],
      ans=0,
      why="STB-1.A.1 says environmental indicators CAN GUIDE HUMANS TO SUSTAINABILITY, which is "
          "a hedged, forward-looking role. Nothing in the statement makes an indicator a proof, "
          "a limit or a substitute for resource depletion, which the same list names in its own "
          "right."),

 dict(q="Which observation would most directly report the framework's indicator of resource "
        "depletion?",
      choices=[
        "The quantity of a resource still available falling year after year as it is used",
        "The market price of a resource rising year after year",
        "The number of workers employed in extracting a resource rising year after year",
        "The number of countries importing a resource rising year after year",
        "The number of uses found for a resource rising year after year"],
      ans=0,
      why="STB-1.A.1 lists resource depletion among its indicators, and depletion is a fall in "
          "what remains available. Price, employment, trade and applications may accompany "
          "depletion but none of them measures the remaining stock."),

 dict(q="A town council has one number for its water: the amount pumped from its aquifer last "
        "year. What must it be compared with to apply the framework's test?",
      choices=[
        "The amount recharged to the aquifer over the same period",
        "The amount pumped by the neighbouring town over the same period",
        "The amount of rain that fell on the town over the same period",
        "The number of households connected to the supply",
        "Nothing further, because the amount pumped settles the question by itself"],
      ans=0,
      why="STB-1.A.2 makes the sustainable amount the one that can be taken without reducing the "
          "available supply, so the take must be set beside what replaces it. A neighbour's "
          "pumping, total rainfall and the number of households leave the comparison "
          "unmade."),

 dict(q="Which of the following goes beyond what the framework's statements actually say?",
      choices=[
        "That the framework ranks its environmental indicators in order of importance",
        "That the framework lists biological diversity among its environmental indicators",
        "That the framework defines sustainability in terms of future generations",
        "That the framework defines a sustainable yield for a renewable resource",
        "That the framework says indicators can guide humans to sustainability"],
      ans=0,
      why="STB-1.A.1 gives its indicators as an unordered list introduced by the word include, "
          "so no order of importance is stated and none may be inferred. Each rejected option "
          "quotes something the two statements do assert."),

 dict(q="Which of the following correctly separates the two ideas this topic introduces?",
      choices=[
        "Sustainability is the goal of using resources without depleting them for future "
        "generations; a sustainable yield is the amount that can be taken without reducing "
        "the supply",
        "A sustainable yield is the goal of using resources without depleting them for "
        "future generations; sustainability is the amount that can be taken without "
        "reducing the supply",
        "Both terms name the same amount of a resource under two different words",
        "Both terms name goals, and neither of them names an amount",
        "Sustainability concerns renewable resources and a sustainable yield concerns "
        "nonrenewable ones"],
      ans=0,
      why="STB-1.A.1 states a goal about use without depletion for future generations, while "
          "STB-1.A.2 states an amount that may be taken from a renewable resource. The exact "
          "swap of the goal and the amount is the error worth guarding against."),

 dict(q="Two villages each take 50 tonnes of reeds a year. One bed regrows 80 tonnes a year "
        "and the other regrows 30. What does the framework's test say about the two takes?",
      choices=[
        "The take from the faster-growing bed is within the sustainable yield and the take "
        "from the slower-growing bed is not",
        "The take from the slower-growing bed is within the sustainable yield and the take "
        "from the faster-growing bed is not",
        "Both takes are within the sustainable yield, because both are the same size",
        "Neither take is within the sustainable yield, because both remove reeds",
        "The framework's test cannot be applied without knowing the area of each bed"],
      ans=0,
      why="STB-1.A.2 sets the test by whether the available supply is reduced, so the same take "
          "can pass on one bed and fail on another. Equal takes do not imply equal outcomes, and "
          "removing some of a renewable resource is not by itself a breach of the definition."),

 dict(q="Why does the framework place its statement about a sustainable yield in a topic "
        "introducing sustainability?",
      choices=[
        "The yield puts the definition's requirement into a quantity: it is how much may be "
        "taken while leaving the resource undepleted",
        "The yield replaces the definition, which the framework treats as too vague to use",
        "The yield concerns a different subject and is placed here only for convenience",
        "The yield states the maximum a resource can produce, which is what the definition "
        "requires",
        "The yield applies to future generations while the definition applies only to the "
        "present one"],
      ans=0,
      why="STB-1.A.1 gives the requirement, that resources not be depleted for future "
          "generations, and STB-1.A.2 gives the amount that satisfies it for a renewable "
          "resource. One is the standard and the other is the standard expressed as a quantity."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Sustainability is humans using resources without depleting them for future "
        "generations; indicators including biological diversity, food production, "
        "temperature and carbon dioxide, human population and resource depletion can guide "
        "them to it; and a sustainable yield is the amount of a renewable resource that can "
        "be taken without reducing the supply.",
        "Sustainability is humans leaving all resources untouched, and a sustainable yield "
        "is the largest amount a resource can produce in a year.",
        "Sustainability is meeting present needs with no regard for later generations, and "
        "the framework names no indicators.",
        "Sustainability is a set of economic indicators, and a sustainable yield applies to "
        "nonrenewable resources.",
        "Sustainability is a goal the framework declines to define, and a sustainable yield "
        "is left undefined as well."],
      ans=0,
      why="The keyed summary carries STB-1.A.1's definition and its list of indicators together "
          "with STB-1.A.2's amount for a renewable resource. Each rejected summary forbids use, "
          "drops the future-generations clause, swaps the indicators for economic ones, or "
          "denies that the framework defines the terms."),
]
