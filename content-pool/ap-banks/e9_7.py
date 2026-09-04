# AP ENVIRONMENTAL SCIENCE 9.7 Ocean Acidification
# CED effective Fall 2026, Unit 9 Global Change.
# Enduring understanding STB-4: Local and regional human activities can have impacts at
# the global level.
# Learning objective STB-4.H: explain the causes and effects of ocean acidification.
# Suggested skill 1.C, explain environmental concepts, processes, or models in applied
# contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-4.H.1  Ocean acidification is the decrease in pH of the oceans, primarily due to
#              increased CO2 concentrations in the atmosphere, and can be expressed as
#              chemical equations.
#   STB-4.H.2  As more CO2 is released into the atmosphere, the oceans, which absorb a
#              large part of that CO2, become more acidic.
#   STB-4.H.3  Anthropogenic activities that contribute to ocean acidification are those
#              that lead to increased CO2 concentrations in the atmosphere: burning of
#              fossil fuels, vehicle emissions, and deforestation.
#   STB-4.H.4  Ocean acidification damages coral because acidification makes it difficult
#              for them to form shells, due to the loss of calcium carbonate.
#
# ACIDIFICATION AND WARMING ARE DIFFERENT MECHANISMS AND ARE ROUTINELY CONFUSED. The
# framework keeps them apart and so does this module. Acidification is a DECREASE IN pH
# and it damages coral by making SHELL FORMATION DIFFICULT through the LOSS OF CALCIUM
# CARBONATE (STB-4.H.4). Ocean warming causes BLEACHING, the LOSS OF ALGAE within the
# coral (STB-4.G.3), and that belongs to topic 9.6. Items 13, 14 and 29 put both accounts
# in front of the student with a distractor that swaps them, and every anchor on those
# items carries BOTH the process AND its mechanism, never the process alone.
#
# NO CHEMICAL EQUATION IS WRITTEN ANYWHERE HERE. STB-4.H.1 says acidification CAN BE
# EXPRESSED as chemical equations and supplies none, and Environmental Science is exported
# as prose with no typesetting, so a hand-written equation would reach a student as raw
# characters. Item 3 keys what the framework says about the equations without writing one.
#
# WHAT IS DELIBERATELY NOT KEYED. STB-4.H.1's hedge PRIMARILY is kept (item 9) rather than
# hardened into a sole cause. STB-4.H.3 names three activities and says only that they
# lead to increased CO2 concentrations; it explains no further mechanism, so item 8 keys
# what the three have in common and no item explains how deforestation raises atmospheric
# carbon dioxide. STB-4.H.2 says the oceans absorb A LARGE PART and gives no figure, so
# no key states a share -- the data item 22 reads its share from its own record.
#
# NO FIGURES ARE REFERENCED. Every record is supplied as a table.
#
# BOUNDARIES. The greenhouse gases and their potencies are STB-4.C and STB-4.D (topic
# 9.3), the problems posed by their increase STB-4.E.1 (topic 9.4), the effects of climate
# change on ecosystems STB-4.F (topic 9.5), and ocean warming STB-4.G (topic 9.6).
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("9.7", "Ocean Acidification", 9)

_T_PH = dict(
    headers=["Decade of the record", "Atmospheric carbon dioxide (parts per million)",
             "Mean pH of the ocean surface"],
    rows=[["Decade 1", "316", "8.11"],
          ["Decade 2", "338", "8.09"],
          ["Decade 3", "369", "8.06"],
          ["Decade 4", "414", "8.03"]])

_T_ABSORB = dict(
    headers=["Year of the record",
             "Carbon dioxide released to the atmosphere (billions of tonnes)",
             "Carbon dioxide taken up by the ocean (billions of tonnes)"],
    rows=[["Year 1", "20", "6"],
          ["Year 2", "30", "9"],
          ["Year 3", "40", "12"],
          ["Year 4", "50", "15"]])

_T_SOURCES = dict(
    headers=["Activity recorded in one country",
             "Carbon dioxide added to the atmosphere (millions of tonnes each year)"],
    rows=[["Burning fossil fuels in power stations", "480"],
          ["Vehicle emissions", "210"],
          ["Deforestation", "95"],
          ["Generating electricity from wind and sunlight", "0"]])

_T_SHELL = dict(
    headers=["Tank", "pH of the seawater",
             "Calcium carbonate available to the corals (relative index)",
             "New skeleton laid down in ninety days (grams)"],
    rows=[["Tank 1", "8.15", "100", "4.8"],
          ["Tank 2", "8.05", "82", "3.5"],
          ["Tank 3", "7.95", "61", "2.1"],
          ["Tank 4", "7.85", "44", "0.9"]])

_T_REEFS = dict(
    headers=["Reef", "Mean pH of the surrounding water",
             "New coral skeleton laid down (millimetres each year)"],
    rows=[["Reef 1", "8.14", "12.6"],
          ["Reef 2", "8.06", "9.4"],
          ["Reef 3", "7.98", "6.1"],
          ["Reef 4", "7.90", "3.2"]])

_T_TWO_STRESSES = dict(
    headers=["Tank", "Water temperature (degrees Celsius)", "pH of the water",
             "Percent of colonies turned white",
             "New skeleton laid down in ninety days (grams)"],
    rows=[["Tank W", "31.0", "8.12", "76", "4.6"],
          ["Tank A", "26.0", "7.86", "5", "1.1"],
          ["Tank C", "26.0", "8.12", "4", "4.7"]])

QUESTIONS = [

 dict(q="What does the framework say ocean acidification is?",
      choices=[
        "The decrease in pH of the oceans.",
        "The increase in pH of the oceans.",
        "The increase in temperature of the oceans.",
        "The rise in the level of the oceans.",
        "The loss of algae from within corals."],
      ans=0,
      why="STB-4.H.1 states that ocean acidification is the decrease in pH of the oceans, "
          "which fixes both the quantity and the direction in which it moves."),

 dict(q="What does the framework give as the primary cause of that change?",
      choices=[
        "Increased carbon dioxide concentrations in the atmosphere.",
        "Decreased carbon dioxide concentrations in the atmosphere.",
        "The melting of sea ice at the poles.",
        "The loss of calcium carbonate from coral skeletons.",
        "The warming of the upper ocean by sunlight."],
      ans=0,
      why="STB-4.H.1 states that the decrease in pH is primarily due to increased CO2 "
          "concentrations in the atmosphere. The loss of calcium carbonate is a consequence "
          "the framework attaches to acidification rather than its cause."),

 dict(q="What does STB-4.H.1 say about how ocean acidification can be represented?",
      choices=[
        "It can be expressed as chemical equations.",
        "It can be expressed only as a single number for the whole ocean.",
        "It cannot be represented in any form.",
        "It can be expressed only as a map of the sea floor.",
        "It can be expressed only as a count of the corals affected."],
      ans=0,
      why="STB-4.H.1 ends by stating that ocean acidification can be expressed as chemical "
          "equations. The statement itself supplies none of those equations, so nothing "
          "beyond the fact that it can be so expressed is available to key."),

 dict(q="According to the framework, what happens to the oceans as more carbon dioxide is "
        "released into the atmosphere?",
      choices=[
        "They become more acidic.",
        "They become less acidic.",
        "Their acidity is unchanged, because the gas stays in the air.",
        "They rise in level without any change in acidity.",
        "They cool, because the gas blocks sunlight."],
      ans=0,
      why="STB-4.H.2 states that as more CO2 is released into the atmosphere, the oceans, "
          "which absorb a large part of that CO2, become more acidic."),

 dict(q="What does the framework say the oceans do with the carbon dioxide released into "
        "the atmosphere?",
      choices=[
        "They absorb a large part of it.",
        "They absorb none of it.",
        "They release an equal amount back into the air.",
        "They convert it into calcium carbonate for the corals.",
        "They hold it at the surface without taking any of it in."],
      ans=0,
      why="STB-4.H.2 describes the oceans as absorbing a large part of the carbon dioxide "
          "released into the atmosphere, which is why a change in the air reaches the "
          "water at all."),

 dict(q="Which anthropogenic activities does the framework name as contributing to ocean "
        "acidification?",
      choices=[
        "Burning of fossil fuels, vehicle emissions, and deforestation.",
        "Burning of fossil fuels, overfishing, and the dumping of plastic waste.",
        "Vehicle emissions, the draining of wetlands, and the mining of sand.",
        "Deforestation, the building of dams, and the introduction of new species.",
        "The generation of electricity from wind, sunlight and moving water."],
      ans=0,
      why="STB-4.H.3 names burning of fossil fuels, vehicle emissions, and deforestation "
          "as the anthropogenic activities contributing to ocean acidification, and names "
          "no others in this topic."),

 dict(q="A revision card lists four activities and calls all four framework contributors "
        "to ocean acidification. Which one is not?",
      choices=[
        "The dumping of plastic waste at sea.",
        "The burning of fossil fuels.",
        "Emissions from vehicles.",
        "Deforestation.",
        "The burning of coal in power stations."],
      ans=0,
      why="STB-4.H.3 names burning of fossil fuels, vehicle emissions and deforestation, "
          "which the four rejected options restate. Plastic waste appears nowhere in this "
          "topic's statements."),

 dict(q="What does the framework say the three activities it names have in common?",
      choices=[
        "They lead to increased carbon dioxide concentrations in the atmosphere.",
        "They remove calcium carbonate from seawater directly.",
        "They raise the temperature of the ocean without changing its chemistry.",
        "They take place only in countries with a coastline.",
        "They release algae from within the corals."],
      ans=0,
      why="STB-4.H.3 describes the anthropogenic activities contributing to ocean "
          "acidification as those that lead to increased CO2 concentrations in the "
          "atmosphere, and then names three of them."),

 dict(q="STB-4.H.1 says the decrease in pH is PRIMARILY due to increased carbon dioxide "
        "concentrations. What does that wording establish?",
      choices=[
        "The chief cause, without ruling out that anything else contributes.",
        "The only cause, with every other contribution ruled out.",
        "A cause the framework treats as doubtful.",
        "A cause that operates only in the deep ocean.",
        "A cause that operates only where corals grow."],
      ans=0,
      why="The hedge PRIMARILY in STB-4.H.1 marks increased atmospheric carbon dioxide as "
          "the chief cause of the decrease in pH without asserting that it is the sole "
          "one, and without casting doubt on it."),

 dict(q="What does the framework say ocean acidification does to coral?",
      choices=[
        "It damages coral by making it difficult for them to form shells.",
        "It damages coral by causing them to lose the algae within them.",
        "It helps coral by supplying extra material for their skeletons.",
        "It moves coral into deeper water where the pH is higher.",
        "It leaves coral unaffected while damaging other marine life."],
      ans=0,
      why="STB-4.H.4 states that ocean acidification damages coral because acidification "
          "makes it difficult for them to form shells. The loss of algae within corals is "
          "what the framework's separate statement on ocean warming calls bleaching."),

 dict(q="What reason does the framework give for that difficulty in forming shells?",
      choices=[
        "The loss of calcium carbonate.",
        "The loss of the algae living within the coral tissue.",
        "The rise in the temperature of the surrounding water.",
        "The rise in the level of the sea above the reef.",
        "The arrival of species that compete with the coral."],
      ans=0,
      why="STB-4.H.4 attributes the difficulty in forming shells to the loss of calcium "
          "carbonate. The loss of algae belongs to the framework's account of bleaching "
          "under ocean warming, which is a different process."),

 dict(q="A student writes that ocean acidification means the pH of the ocean is rising. "
        "What is the clearest correction from the framework?",
      choices=[
        "The framework defines ocean acidification as a decrease in the pH of the oceans.",
        "The framework defines ocean acidification as an increase in the pH of the oceans, "
        "so the student is right.",
        "The framework defines ocean acidification as a rise in the temperature of the "
        "oceans.",
        "The framework gives no definition of ocean acidification.",
        "The framework defines ocean acidification as a rise in the level of the oceans."],
      ans=0,
      why="STB-4.H.1 states that ocean acidification is the decrease in pH of the oceans, "
          "so the direction in the student's account is the reverse of the framework's."),

 dict(q="A student writes that ocean acidification is what turns corals white. What is the "
        "clearest correction from the framework?",
      choices=[
        "Turning white is bleaching, which the framework attributes to warming through the "
        "loss of algae; acidification instead makes shell formation difficult through the "
        "loss of calcium carbonate.",
        "Turning white is bleaching, which the framework attributes to acidification "
        "through the loss of calcium carbonate; warming instead makes shell formation "
        "difficult through the loss of algae.",
        "Turning white and failing to form shells are the same damage under two names.",
        "The framework attributes both turning white and failing to form shells to "
        "acidification alone.",
        "The framework attributes no damage to corals from either process."],
      ans=0,
      why="STB-4.G.3 makes bleaching, the loss of algae within corals, the damage caused by "
          "ocean warming, while STB-4.H.4 makes the difficulty in forming shells, through "
          "the loss of calcium carbonate, the damage caused by acidification. Each process "
          "has its own mechanism in the framework."),

 dict(q="Two damaged reefs are described. On the first the colonies have turned white; on "
        "the second they are failing to build their skeletons. Which change does the "
        "framework attribute to each?",
      choices=[
        "The whitened reef to ocean warming through the loss of algae, and the "
        "skeleton-poor reef to acidification through the loss of calcium carbonate.",
        "The whitened reef to acidification through the loss of calcium carbonate, and the "
        "skeleton-poor reef to ocean warming through the loss of algae.",
        "Both reefs to acidification, since the framework gives warming no effect on "
        "coral.",
        "Both reefs to ocean warming, since the framework gives acidification no effect on "
        "coral.",
        "Neither reef to either process, since the framework names no damage to coral."],
      ans=0,
      why="STB-4.G.3 attributes bleaching, corals turning white through the loss of algae, "
          "to ocean warming, and STB-4.H.4 attributes the difficulty in forming shells, "
          "through the loss of calcium carbonate, to acidification. The two accounts pair "
          "one observation with each process."),

 dict(q="Which of these does the framework NOT claim in this topic?",
      choices=[
        "Ocean acidification is caused primarily by a rise in the temperature of the "
        "ocean.",
        "Ocean acidification is the decrease in pH of the oceans.",
        "The oceans absorb a large part of the carbon dioxide released into the "
        "atmosphere.",
        "Burning fossil fuels contributes to ocean acidification.",
        "Acidification makes it difficult for corals to form shells."],
      ans=0,
      why="STB-4.H.1 attributes the decrease in pH primarily to increased carbon dioxide "
          "concentrations in the atmosphere, not to a rise in temperature, and the four "
          "rejected options restate STB-4.H.1, STB-4.H.2, STB-4.H.3 and STB-4.H.4."),

 dict(q="A country closes its coal fired power stations and replaces them with wind "
        "turbines. Which framework statement bears on that country's contribution to ocean "
        "acidification?",
      choices=[
        "The one naming burning of fossil fuels among the activities that lead to "
        "increased atmospheric carbon dioxide.",
        "The one stating that acidification makes it difficult for corals to form shells.",
        "The one stating that acidification can be expressed as chemical equations.",
        "The one stating that the loss of calcium carbonate damages coral.",
        "No statement in this topic bears on how electricity is generated."],
      ans=0,
      why="STB-4.H.3 names burning of fossil fuels among the anthropogenic activities that "
          "contribute to ocean acidification by leading to increased CO2 concentrations in "
          "the atmosphere, and coal fired generation is such burning."),

 dict(q="Which observations would test STB-4.H.2's claim most directly?",
      choices=[
        "Records of the carbon dioxide released into the atmosphere and of the pH of the "
        "ocean over the same years.",
        "Records of the pH of the ocean alone on a single occasion.",
        "Records of the carbon dioxide released into the atmosphere alone.",
        "Records of the number of coral species present at one reef.",
        "Records of the depth of the ocean at several places."],
      ans=0,
      why="STB-4.H.2 asserts that the oceans grow more acidic as more carbon dioxide is "
          "released into the atmosphere, so the evidence bearing on it follows both "
          "quantities over the same period rather than either one alone."),

 dict(q="Which single measurement would show most directly that acidification has occurred "
        "at a site, as the framework defines it?",
      choices=[
        "The pH of the water at that site, measured over a period of years.",
        "The temperature of the water at that site, measured over a period of years.",
        "The depth of the water at that site, measured over a period of years.",
        "The number of fish caught at that site each year.",
        "The share of the sky covered by cloud above that site."],
      ans=0,
      why="STB-4.H.1 defines ocean acidification as the decrease in pH of the oceans, so a "
          "record of pH over time is the measurement that speaks to the definition "
          "directly."),

 dict(q="Atmospheric carbon dioxide and the pH of the ocean surface were recorded over "
        "four decades. What does the record establish?",
      table=_T_PH,
      choices=[
        "As the carbon dioxide rises the pH falls at every decade.",
        "As the carbon dioxide rises the pH rises at every decade.",
        "The carbon dioxide rises while the pH holds steady across the record.",
        "The carbon dioxide falls while the pH rises across the record.",
        "Neither column changes across the four decades."],
      ans=0,
      why="Reading down the two columns in decade order, one rises at every step and the "
          "other falls. STB-4.H.1 defines acidification as a decrease in pH primarily due "
          "to increased carbon dioxide concentrations in the atmosphere."),

 dict(q="Across those same four decades, by how much did the pH of the ocean surface "
        "change?",
      table=_T_PH,
      choices=[
        "It fell by 0.08.",
        "It rose by 0.08.",
        "It fell by 0.03.",
        "It fell by 0.11.",
        "It did not change."],
      ans=0,
      why="The first and last entries in the pH column are subtracted. STB-4.H.1 makes a "
          "decrease in pH the definition of ocean acidification, so the direction of that "
          "movement is what matters."),

 dict(q="Carbon dioxide released to the atmosphere and taken up by the ocean was recorded "
        "over four years. What does the record establish?",
      table=_T_ABSORB,
      choices=[
        "The more that is released, the more the ocean takes up.",
        "The more that is released, the less the ocean takes up.",
        "The ocean takes up the same amount whatever is released.",
        "The ocean takes up more than is released in every year.",
        "The ocean takes up none of what is released."],
      ans=0,
      why="Sorting the years by the amount released leaves the amount taken up strictly "
          "increasing. STB-4.H.2 describes the oceans as absorbing a large part of the "
          "carbon dioxide released into the atmosphere."),

 dict(q="In each year of that same record, what share of the released carbon dioxide did "
        "the ocean take up?",
      table=_T_ABSORB,
      choices=[
        "30 percent, the same share in every year.",
        "70 percent, the same share in every year.",
        "A share that rises from 30 percent to 70 percent across the years.",
        "A share that falls from 70 percent to 30 percent across the years.",
        "A share too small to express as a percentage."],
      ans=0,
      why="The uptake in each year is divided by the release in that year. STB-4.H.2 "
          "states that the oceans absorb a large part of the carbon dioxide released "
          "without giving a figure, so the share has to be read from the record."),

 dict(q="Four activities in one country were recorded for the carbon dioxide they add to "
        "the atmosphere. Which adds the most?",
      table=_T_SOURCES,
      choices=[
        "Burning fossil fuels in power stations.",
        "Emissions from the country's vehicles.",
        "The clearing of the country's forests.",
        "The generation of electricity from wind and sunlight.",
        "All four add the same amount."],
      ans=0,
      why="The largest entry in the emissions column belongs to one activity alone. "
          "STB-4.H.3 names burning of fossil fuels among the activities that contribute to "
          "ocean acidification by raising atmospheric carbon dioxide."),

 dict(q="Which of the four activities in that same record is not one the framework names "
        "as contributing to ocean acidification?",
      table=_T_SOURCES,
      choices=[
        "Generating electricity from wind and sunlight, which the record shows adding "
        "none.",
        "Burning fossil fuels in power stations, which the record shows adding the most.",
        "Vehicle emissions, which the record shows adding the second largest amount.",
        "Deforestation, which the record shows adding the third largest amount.",
        "All four are named by the framework."],
      ans=0,
      why="STB-4.H.3 names burning of fossil fuels, vehicle emissions and deforestation, "
          "and describes them as activities that lead to increased CO2 concentrations in "
          "the atmosphere. The remaining activity in the record adds none and is not among "
          "the three."),

 dict(q="Corals were held in four tanks of different pH and measured for the calcium "
        "carbonate available to them and the skeleton they laid down. What does the record "
        "establish?",
      table=_T_SHELL,
      choices=[
        "As the pH falls, less calcium carbonate is available and less skeleton is laid "
        "down.",
        "As the pH falls, more calcium carbonate is available and more skeleton is laid "
        "down.",
        "As the pH falls, less calcium carbonate is available but the skeleton laid down "
        "is unchanged.",
        "The pH and the calcium carbonate available are unrelated in this record.",
        "Every tank laid down the same amount of skeleton."],
      ans=0,
      why="Sorting the tanks by pH leaves both the calcium carbonate available and the "
          "skeleton laid down strictly increasing. STB-4.H.4 states that acidification "
          "makes it difficult for corals to form shells due to the loss of calcium "
          "carbonate."),

 dict(q="Which of those four tanks laid down the least skeleton, and what was its water "
        "like?",
      table=_T_SHELL,
      choices=[
        "Tank 4, which held the lowest pH and the least available calcium carbonate.",
        "Tank 1, which held the highest pH and the most available calcium carbonate.",
        "Tank 2, which held the second highest pH of the four.",
        "Tank 3, which held the second lowest pH of the four.",
        "All four laid down the same amount of skeleton."],
      ans=0,
      why="The smallest entry in the skeleton column, the smallest pH and the smallest "
          "calcium carbonate index all fall in the same row, which is the pairing "
          "STB-4.H.4's account predicts."),

 dict(q="Four reefs were recorded for the pH of their water and the skeleton their corals "
        "lay down each year. What does the record establish?",
      table=_T_REEFS,
      choices=[
        "The reefs in the lowest pH water lay down the least skeleton each year.",
        "The reefs in the lowest pH water lay down the most skeleton each year.",
        "The pH of the water and the skeleton laid down are unrelated across these reefs.",
        "Every reef in the record lays down the same amount of skeleton.",
        "Every reef in the record sits in water of the same pH."],
      ans=0,
      why="Sorting the reefs by the pH of their water leaves the skeleton laid down "
          "strictly increasing. STB-4.H.4 states that acidification makes it difficult for "
          "corals to form shells due to the loss of calcium carbonate."),

 dict(q="Across those same four reefs, how much more skeleton does the reef in the highest "
        "pH water lay down than the reef in the lowest?",
      table=_T_REEFS,
      choices=[
        "9.4 millimetres more each year.",
        "3.2 millimetres more each year.",
        "12.6 millimetres more each year.",
        "6.1 millimetres more each year.",
        "0.24 millimetres more each year."],
      ans=0,
      why="The skeleton figures for the reefs in the highest and lowest pH water are "
          "subtracted. STB-4.H.4 ties the difficulty in forming shells to acidification, "
          "which is what makes that comparison the relevant one."),

 dict(q="Corals were held in three tanks: one warmed, one held at a lowered pH, and one "
        "left at both the usual temperature and the usual pH. What does the record "
        "establish?",
      table=_T_TWO_STRESSES,
      choices=[
        "The warmed tank turned white while laying down normal skeleton, and the lowered "
        "pH tank laid down little skeleton while staying its usual colour.",
        "The lowered pH tank turned white while laying down normal skeleton, and the "
        "warmed tank laid down little skeleton while staying its usual colour.",
        "Both the warmed tank and the lowered pH tank turned white and laid down little "
        "skeleton.",
        "Neither the warmed tank nor the lowered pH tank differed from the untreated one.",
        "The untreated tank turned white and laid down the least skeleton of the three."],
      ans=0,
      why="Reading across the rows, one tank differs from the untreated one in colour "
          "alone and the other in skeleton alone. STB-4.G.3 attributes the turning white "
          "to ocean warming through the loss of algae, and STB-4.H.4 attributes the "
          "difficulty in forming shells to acidification through the loss of calcium "
          "carbonate."),

 dict(q="Which single sentence collects what this topic's four statements assert and "
        "nothing further?",
      choices=[
        "Ocean acidification is the decrease in pH of the oceans, primarily due to "
        "increased atmospheric carbon dioxide, which the oceans absorb in large part; the "
        "activities contributing to it are those raising atmospheric carbon dioxide, "
        "namely burning fossil fuels, vehicle emissions and deforestation; and it damages "
        "coral by making shell formation difficult through the loss of calcium carbonate.",
        "Ocean acidification is the increase in pH of the oceans, primarily due to a rise "
        "in their temperature; the activities contributing to it are overfishing and "
        "plastic waste; and it damages coral by causing them to lose the algae within "
        "them.",
        "Ocean acidification has no named cause in the framework, and the framework "
        "attaches no consequence to it for corals.",
        "Ocean acidification is the decrease in pH of the oceans and is the only cause of "
        "every kind of damage to coral the framework names.",
        "Ocean acidification is caused by the loss of calcium carbonate from coral "
        "skeletons, which then makes it difficult for them to form shells."],
      ans=0,
      why="STB-4.H.1 supplies the definition and the primary cause, STB-4.H.2 the "
          "absorption of a large part of the released carbon dioxide, STB-4.H.3 the three "
          "named activities and what they have in common, and STB-4.H.4 the damage to "
          "coral and its mechanism. Bleaching belongs to the framework's separate "
          "statement on ocean warming."),
]
