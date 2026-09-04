# AP ENVIRONMENTAL SCIENCE 4.6 Watersheds
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ERT-4: Earth's systems interact, resulting in a state of balance
# over time.
# Learning objective ERT-4.F: describe the characteristics of a watershed.
# Suggested skill 1.C, explain environmental concepts, processes, or models in applied
# contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-4.F.1  Characteristics of a given watershed include its area, length, slope, soil,
#              vegetation types, and divides with adjoining watersheds.
#
# THAT ONE SENTENCE IS THE WHOLE OF THIS TOPIC, and it is a list of six characteristics:
#   area                                length
#   slope                               soil
#   vegetation types                    divides with adjoining watersheds
# Every conceptual item here keys one entry of that list, the number of entries, the word
# INCLUDE that opens it, or something the list leaves out.
#
# WHAT THE STATEMENT DOES NOT DO. It does not say what a watershed is, it does not say how
# any characteristic affects the water leaving the watershed, and it gives no value for any
# of the six. Item 15 keys that first absence rather than filling it, and no key anywhere
# asserts that a steeper watershed sheds water faster, that a forested one loses less soil,
# or anything else of that shape -- those belong to statements in other topics.
#
# THE SUGGESTED SKILL IS 1.C, EXPLAIN IN APPLIED CONTEXTS, so items 11, 12 and 13 put a
# surveyor or a planner in front of a real task and ask which of the six named
# characteristics the task concerns.
#
# NO FIGURES. A watershed is normally taught from a picture of a basin and its boundary,
# and the bank carries no images, so the areas, lengths, slopes, land cover shares, adjoining
# counts and divide lengths are tabulated and every question is asked of those numbers. The
# land cover shares add to one hundred percent in every watershed and the verifier
# recomputes that sum.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.6", "Watersheds", 4)

_T_CHARS = dict(
    headers=["Watershed", "Area (square kilometers)",
             "Length from the head to the outlet (kilometers)",
             "Average slope (meters of fall per kilometer)"],
    rows=[["Watershed A", "120", "26", "8"],
          ["Watershed B", "310", "44", "15"],
          ["Watershed C", "75", "19", "31"]])

_T_COVER = dict(
    headers=["Watershed", "Share of the surface under forest (percent)",
             "Share of the surface under grassland (percent)",
             "Share of the surface where the soil is thin or absent (percent)"],
    rows=[["Watershed A", "62", "31", "7"],
          ["Watershed B", "18", "74", "8"],
          ["Watershed C", "40", "12", "48"]])

_T_DIVIDES = dict(
    headers=["Watershed", "Number of watersheds adjoining it",
             "Length of the divide it shares with them (kilometers)",
             "River its water reaches"],
    rows=[["Watershed A", "3", "58", "The northern river"],
          ["Watershed B", "2", "71", "The southern river"],
          ["Watershed C", "4", "46", "The northern river"]])

QUESTIONS = [

 dict(q="Which characteristics does the framework list for a given watershed?",
      choices=[
        "Its area, length, slope, soil, vegetation types, and divides with adjoining "
        "watersheds",
        "Its area, length, and slope, and nothing further",
        "Its soil and vegetation types, and nothing further",
        "Its area, length, slope, soil, vegetation types, and the number of people living "
        "in it",
        "Its latitude, longitude, elevation, and rainfall"],
      ans=0,
      why="ERT-4.F.1 states that characteristics of a given watershed include its area, "
          "length, slope, soil, vegetation types, and divides with adjoining watersheds. "
          "Two rejected lists drop half the entries, one adds a population the statement "
          "never names, and one replaces the list altogether."),

 dict(q="How many characteristics does that list name?",
      choices=["Six", "Two", "Three", "Four", "Nine"],
      ans=0,
      why="ERT-4.F.1 names area, length, slope, soil, vegetation types, and divides with "
          "adjoining watersheds, which is six entries in one list."),

 dict(q="Which of these is NOT among the characteristics the framework names for a "
        "watershed?",
      choices=["The number of people living in it", "Its area", "Its slope", "Its soil",
               "Its vegetation types"],
      ans=0,
      why="ERT-4.F.1 names area, length, slope, soil, vegetation types, and divides with "
          "adjoining watersheds. A human population appears nowhere in the statement."),

 dict(q="And which of these is also absent from that list of characteristics?",
      choices=["The depth of the groundwater beneath it", "Its length",
               "Its divides with adjoining watersheds", "Its area", "Its slope"],
      ans=0,
      why="ERT-4.F.1's six entries are area, length, slope, soil, vegetation types, and "
          "divides with adjoining watersheds. The depth of the groundwater is not one of "
          "them, and the statement mentions no water beneath the surface at all."),

 dict(q="Which characteristic in the framework's list refers to a boundary?",
      choices=["Its divides with adjoining watersheds", "Its area", "Its slope", "Its soil",
               "Its vegetation types"],
      ans=0,
      why="ERT-4.F.1 names divides with adjoining watersheds among the characteristics, and "
          "a divide is what lies between one watershed and the next. The other five entries "
          "describe the watershed itself rather than its edge."),

 dict(q="What does the phrase DIVIDES WITH ADJOINING WATERSHEDS indicate about a watershed?",
      choices=[
        "That it has neighbouring watersheds and a boundary it shares with them",
        "That it is divided into smaller parts by its own streams",
        "That it has no neighbouring watersheds at all",
        "That its boundary is fixed by a political border",
        "That its area is divided among the people who own the land"],
      ans=0,
      why="ERT-4.F.1 speaks of divides WITH ADJOINING watersheds, which puts other "
          "watersheds beside this one and makes the divide the thing they share. The "
          "statement neither divides a watershed internally nor mentions ownership or "
          "politics."),

 dict(q="The framework says the characteristics of a given watershed INCLUDE those six. "
        "What does that phrasing establish?",
      choices=[
        "Those six are the characteristics the statement supplies, without its claiming "
        "that nothing else about a watershed can be described",
        "The statement claims that a watershed has no other describable feature whatever",
        "The statement supplies only two of the characteristics",
        "The statement supplies no characteristics at all",
        "The statement supplies the characteristics but not which watershed they belong to"],
      ans=0,
      why="ERT-4.F.1 opens with characteristics of a given watershed INCLUDE, which commits "
          "the framework to those six while making no claim about features it does not "
          "discuss. The statement also fixes the characteristics to a GIVEN watershed, so "
          "an option denying that is false as well."),

 dict(q="A surveyor records how steeply the land falls from the head of a basin to its "
        "outlet. Which of the framework's named characteristics is that?",
      choices=["Its slope", "Its area", "Its length", "Its soil", "Its vegetation types"],
      ans=0,
      why="ERT-4.F.1 names slope among the characteristics of a given watershed, and a "
          "measure of how steeply the land falls is what a slope is. Area, length, soil and "
          "vegetation types are the other entries and are measured differently."),

 dict(q="A surveyor walks a basin identifying the plants growing across it. Which of the "
        "framework's named characteristics is being recorded?",
      choices=["Its vegetation types", "Its area", "Its length", "Its slope", "Its soil"],
      ans=0,
      why="ERT-4.F.1 names vegetation types among the characteristics of a given watershed, "
          "and a survey of the plants growing across the basin records exactly that."),

 dict(q="A surveyor digs down at several points and describes what the ground is made of. "
        "Which of the framework's named characteristics is being recorded?",
      choices=["Its soil", "Its area", "Its length", "Its slope", "Its vegetation types"],
      ans=0,
      why="ERT-4.F.1 names soil among the characteristics of a given watershed, and "
          "describing what the ground is made of at depth is a record of the soil rather "
          "than of anything growing on it."),

 dict(q="A hydrologist wants to know which of two rivers the rain falling on a particular "
        "hillside will eventually reach. Which of the framework's named characteristics "
        "settles that?",
      choices=[
        "The divides with adjoining watersheds, which are the boundaries between one "
        "watershed and the next",
        "The area of the watershed",
        "The soil of the watershed",
        "The vegetation types of the watershed",
        "The length of the watershed"],
      ans=0,
      why="ERT-4.F.1 names divides with adjoining watersheds among the characteristics, and "
          "a divide is what separates one watershed from its neighbour. Which side of the "
          "divide the hillside lies on is what decides which watershed the rain falls in."),

 dict(q="A planner comparing two basins finds that one drains twice as much land as the "
        "other. Which of the framework's named characteristics does that comparison use?",
      choices=["Their area", "Their slope", "Their soil", "Their vegetation types",
               "Their divides with adjoining watersheds"],
      ans=0,
      why="ERT-4.F.1 names area among the characteristics of a given watershed, and the "
          "amount of land a basin drains is its area. The other entries measure steepness, "
          "ground material, plant cover and the boundary with a neighbour."),

 dict(q="A hydrologist measures the distance from the highest point of a basin down to the "
        "point where its water leaves. Which of the framework's named characteristics is "
        "that?",
      choices=["Its length", "Its area", "Its slope", "Its soil", "Its vegetation types"],
      ans=0,
      why="ERT-4.F.1 names length among the characteristics of a given watershed, and a "
          "distance measured from one end of the basin to the other is a length rather than "
          "an area or a steepness."),

 dict(q="Which framework statement justifies describing a watershed by more than one "
        "property at once?",
      choices=[
        "Characteristics of a given watershed include its area, length, slope, soil, "
        "vegetation types, and divides with adjoining watersheds",
        "Soils are generally categorized by horizons based on their composition and organic "
        "material",
        "The layers of the atmosphere are based on temperature gradients",
        "Global wind patterns primarily result from the most intense solar radiation "
        "arriving at the equator",
        "Convergent boundaries can result in the creation of mountains and island arcs"],
      ans=0,
      why="ERT-4.F.1 is a list of six characteristics belonging to one watershed, so the "
          "framework itself treats a watershed as described by several properties together. "
          "The rejected statements are ERT-4.B.2, ERT-4.D.2, ERT-4.E.1 and ERT-4.A.1, none "
          "of which concerns a watershed."),

 dict(q="Which of these does the framework's watershed statement leave unstated?",
      choices=[
        "How each characteristic affects the water leaving the watershed",
        "That the area is a characteristic",
        "That the slope is a characteristic",
        "That the soil is a characteristic",
        "That the divides with adjoining watersheds are characteristics"],
      ans=0,
      why="ERT-4.F.1 lists six characteristics and attaches no consequence to any of them. "
          "What a slope or a soil does to the water leaving a basin would have to come from "
          "another statement or from a measurement."),

 dict(q="How does the framework's watershed statement differ from its statement that "
        "protecting soils can protect water quality?",
      choices=[
        "This statement lists what can be described about a watershed, while that one says "
        "what protecting a soil does for the water moving through it",
        "This statement says what protecting a soil does for the water moving through it, "
        "while that one lists what can be described about a watershed",
        "The two statements make the same claim in different words",
        "This statement concerns the atmosphere and that one concerns the soil",
        "Neither statement mentions soil at all"],
      ans=0,
      why="ERT-4.F.1 is a list of characteristics, with no consequence attached to any of "
          "them. ERT-4.B.3, in topic 4.2, states that protecting soils can protect water "
          "quality as soils effectively filter and clean water that moves through them, "
          "which is a consequence rather than a description. Both mention soil, so an "
          "option denying that is false as well."),

 dict(q="Three watersheds were surveyed and the results tabulated. Which of the framework's "
        "named characteristics does the record report?",
      table=_T_CHARS,
      choices=[
        "Its area, its length, and its slope",
        "Its soil, its vegetation types, and its divides with adjoining watersheds",
        "Its area alone",
        "Its vegetation types alone",
        "None of the characteristics the framework names"],
      ans=0,
      why="Beside the name of each watershed the record carries an area, a length and an "
          "average slope, and all three vary from one watershed to the next. ERT-4.F.1 "
          "names all three among the characteristics of a given watershed."),

 dict(q="Which of those three watersheds has the largest area?",
      table=_T_CHARS,
      choices=["Watershed B", "Watershed A", "Watershed C",
               "The three have equal areas", "The record does not report area"],
      ans=0,
      why="The three areas are 120, 310 and 75 square kilometers, all different, and the "
          "largest is unique. ERT-4.F.1 names area among the characteristics of a given "
          "watershed but supplies no value for it, so the comparison comes from the record."),

 dict(q="Which of those three watersheds falls most steeply?",
      table=_T_CHARS,
      choices=["Watershed C", "Watershed A", "Watershed B",
               "The three fall equally steeply", "The record does not report slope"],
      ans=0,
      why="The three slopes are 8, 15 and 31 meters of fall per kilometer, all different, "
          "and the steepest is unique. ERT-4.F.1 names slope among the characteristics of a "
          "given watershed without supplying a value, so the record settles the comparison."),

 dict(q="Do the largest and the steepest of those watersheds turn out to be the same one?",
      table=_T_CHARS,
      choices=[
        "No, so a watershed's area and its slope can rank the three differently",
        "Yes, so a watershed's area and its slope always rank the three alike",
        "Yes, and the shortest watershed is also the steepest",
        "The record reports area but not slope",
        "The record reports slope but not area"],
      ans=0,
      why="The largest area and the steepest slope belong to different watersheds, each "
          "unique in its own column. ERT-4.F.1 lists area and slope as separate "
          "characteristics of a given watershed and connects neither to the other."),

 dict(q="How much larger in area is the largest of those watersheds than the smallest?",
      table=_T_CHARS,
      choices=[
        "235 square kilometers larger", "310 square kilometers larger",
        "190 square kilometers larger", "45 square kilometers larger",
        "The record does not allow that comparison"],
      ans=0,
      why="The two areas are 310 and 75 square kilometers, and 310 less 75 is 235. The "
          "rejected values are the largest area itself and differences between other pairs "
          "of watersheds."),

 dict(q="The surface of each of those watersheds was classified by what covers it. What do "
        "the three columns account for?",
      table=_T_COVER,
      choices=[
        "The whole surface, since the three shares add to one hundred percent in every "
        "watershed",
        "About half the surface, with the remainder unreported",
        "More than the whole surface, since the three shares add to more than one hundred "
        "percent",
        "Only the first watershed, since the other two are incomplete",
        "Nothing, since the three columns are measured in different units"],
      ans=0,
      why="Adding the forested share, the grassland share and the share where the soil is "
          "thin or absent gives one hundred percent in each of the three watersheds. The "
          "three are shares of one surface."),

 dict(q="Which of those watersheds carries the largest share of its surface under forest?",
      table=_T_COVER,
      choices=["Watershed A", "Watershed B", "Watershed C",
               "The three carry equal shares under forest",
               "The record does not report forest cover"],
      ans=0,
      why="The three forested shares are 62, 18 and 40 percent, all different, and the "
          "largest is unique. ERT-4.F.1 names vegetation types among the characteristics of "
          "a given watershed without supplying a value, so the record settles it."),

 dict(q="Which two of the framework's named characteristics does that classification bear "
        "on?",
      table=_T_COVER,
      choices=[
        "Its vegetation types and its soil",
        "Its area and its length",
        "Its slope and its divides with adjoining watersheds",
        "Its length alone",
        "None of the characteristics the framework names"],
      ans=0,
      why="Two of the three columns record what is growing on the surface and the third "
          "records where the soil is thin or absent. ERT-4.F.1 names vegetation types and "
          "soil among the characteristics of a given watershed, and the record reports both "
          "and neither the area, the length, the slope nor the divides."),

 dict(q="The boundaries of those three watersheds were surveyed. What does the record "
        "establish?",
      table=_T_DIVIDES,
      choices=[
        "Every one of them adjoins other watersheds and shares a divide of measurable "
        "length with them",
        "None of them adjoins any other watershed",
        "Only one of them adjoins another watershed",
        "They all adjoin the same number of other watersheds",
        "The record reports the adjoining watersheds but not the length of any divide"],
      ans=0,
      why="Each watershed records at least two adjoining watersheds and a divide tens of "
          "kilometers long, and the counts differ from one another. ERT-4.F.1 names divides "
          "with adjoining watersheds among the characteristics of a given watershed."),

 dict(q="Which of those watersheds adjoins the most others?",
      table=_T_DIVIDES,
      choices=["Watershed C", "Watershed A", "Watershed B",
               "The three adjoin the same number of others",
               "The record does not report how many adjoin each"],
      ans=0,
      why="The three counts are 3, 2 and 4 adjoining watersheds, all different, and the "
          "largest is unique. ERT-4.F.1 names divides with adjoining watersheds among the "
          "characteristics without supplying a number, so the record settles it."),

 dict(q="How many of those three watersheds send their water to the northern river?",
      table=_T_DIVIDES,
      choices=["Two of the three", "Only one of them", "All three of them",
               "Not one of them", "The record does not report which river each reaches"],
      ans=0,
      why="Two of the three rows name the northern river and one names the southern, so "
          "the three basins do not all drain the same way. Each is separated from its "
          "neighbours by a divide tens of kilometers long, which is the characteristic "
          "ERT-4.F.1 names."),

 dict(q="Which of those watersheds shares the longest divide with its neighbours?",
      table=_T_DIVIDES,
      choices=["Watershed B", "Watershed A", "Watershed C",
               "The three share divides of equal length",
               "The record does not report the length of any divide"],
      ans=0,
      why="The three divide lengths are 58, 71 and 46 kilometers, all different, and the "
          "longest is unique. ERT-4.F.1 names divides with adjoining watersheds among the "
          "characteristics of a given watershed without supplying a length."),

 dict(q="Taken together, do the number of adjoining watersheds and the length of the divide "
        "rank those three alike?",
      table=_T_DIVIDES,
      choices=[
        "No, since the watershed adjoining the most others is not the one with the longest "
        "divide",
        "Yes, since the watershed adjoining the most others also has the longest divide",
        "Yes, since all three adjoin the same number of others",
        "The record reports the adjoining watersheds but not the divide lengths",
        "The record reports the divide lengths but not the adjoining watersheds"],
      ans=0,
      why="The largest count of adjoining watersheds and the longest divide belong to "
          "different watersheds, each unique in its own column. A basin can touch many "
          "neighbours along short stretches or few along long ones, and ERT-4.F.1 names the "
          "divides without saying anything about their number or their length."),

 dict(q="Which single sentence collects what this topic's statement asserts and nothing "
        "further?",
      choices=[
        "The characteristics of a given watershed include its area, its length, its slope, "
        "its soil, its vegetation types, and its divides with adjoining watersheds",
        "The characteristics of a given watershed include its area, its length, and its "
        "slope, and nothing else about it can be described",
        "The characteristics of a given watershed include its area, its length, its slope, "
        "its soil, its vegetation types, and the number of people living in it",
        "The characteristics of a given watershed include its soil and its vegetation "
        "types, and its boundary is fixed by a political border",
        "The characteristics of a given watershed include its area, its length, its slope, "
        "its soil, its vegetation types, and its divides with neighbouring basins, and a "
        "steeper watershed always sheds its water faster"],
      ans=0,
      why="ERT-4.F.1 supplies six characteristics of a given watershed and nothing beyond "
          "them. Each rejected summary shortens the list, adds a population or a political "
          "boundary the statement never names, or attaches a consequence to the slope that "
          "the statement does not."),
]
