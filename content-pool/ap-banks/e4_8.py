# AP ENVIRONMENTAL SCIENCE 4.8 Earth's Geography and Climate
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ENG-2: most of the Earth's atmospheric processes are driven
# by input of energy from the sun.
# Learning objective ENG-2.B: describe how the Earth's geography affects weather and
# climate.
# Suggested skill 2.B, explain relationships between different characteristics of
# environmental concepts, processes, or models represented visually.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-2.B.1  Weather and climate are affected not only by the sun's energy but by
#              geologic and geographic factors, such as mountains and ocean
#              temperature.
#   ENG-2.B.2  A rain shadow is a region of land that has become drier because a higher
#              elevation area blocks precipitation from reaching the land.
#
# SCOPE. The framework gives two sentences and no mechanism. It does NOT state that
# air cools as it rises, does not name a lapse rate, does not use the words windward or
# leeward, and does not say which way a current flows past any named coast. So no key
# here rests on any of that. Each item either restates one of the two sentences applied
# to a described case, or reads a conclusion off a table printed with the question --
# and every tabulated conclusion is recomputed in verify_e4_8.py from that table alone.
# Where a stem needs a wind direction or a moisture source, the stem states it; the
# student is never asked to supply it from outside the framework.
#
# BOUNDARY WITH 4.9. Ocean temperature appears here only as a standing geographic
# feature of a coast. The changing Pacific surface temperatures of El Nino and La Nina,
# ENG-2.C.1 and ENG-2.C.2, belong to topic 4.9 and are not asked here.
#
# NO FIGURES. The suggested skill is visual and the bank cannot carry images, so every
# visual item is served by a table= instead of a described picture.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.8", "Earth’s Geography and Climate", 4)

_T_TRANSECT = dict(
    headers=["Site along a west to east transect", "Elevation (meters)",
             "Average annual precipitation (millimeters)"],
    rows=[["Site 1, plain west of the range", "50", "1850"],
          ["Site 2, western slope", "900", "2400"],
          ["Site 3, crest of the range", "2600", "1500"],
          ["Site 4, eastern slope", "1100", "520"],
          ["Site 5, plain east of the range", "300", "210"]])

_T_COASTINLAND = dict(
    headers=["Town", "Distance from the ocean (kilometers)",
             "Mean temperature of the warmest month (degrees Celsius)",
             "Mean temperature of the coldest month (degrees Celsius)"],
    rows=[["Harbour town", "2", "19", "8"],
          ["Valley town", "120", "26", "2"],
          ["Plains town", "400", "30", "-6"]])

_T_OFFSHORE = dict(
    headers=["Coastal city", "Mean temperature of the water just offshore (degrees Celsius)",
             "Mean annual air temperature of the city (degrees Celsius)"],
    rows=[["City J", "6", "9"],
          ["City K", "12", "14"],
          ["City L", "18", "20"],
          ["City M", "25", "26"]])

_T_UPWIND = dict(
    headers=["City", "Average annual precipitation (millimeters)",
             "Height of the land the moist winds must cross before reaching the city "
             "(meters)"],
    rows=[["City R", "1720", "40"],
          ["City S", "260", "3100"],
          ["City T", "980", "700"]])

_T_SLOPES = dict(
    headers=["Weather station", "Average annual precipitation (millimeters)",
             "Elevation (meters)"],
    rows=[["Station on the side the moist ocean winds reach first", "2100", "800"],
          ["Station on the crest of the range", "1400", "2500"],
          ["Station on the far side of the crest", "300", "750"]])

_T_COASTS = dict(
    headers=["Coast", "Mean temperature of the offshore water (degrees Celsius)",
             "Mean annual precipitation of the coastal strip (millimeters)"],
    rows=[["Coast W", "10", "300"],
          ["Coast X", "15", "620"],
          ["Coast Y", "20", "980"],
          ["Coast Z", "26", "1450"]])

_T_LAKE = dict(
    headers=["Site", "Distance from the large lake (kilometers)",
             "Mean temperature of the warmest month (degrees Celsius)",
             "Mean temperature of the coldest month (degrees Celsius)"],
    rows=[["Lakeside site", "1", "22", "4"],
          ["Middle site", "40", "27", "0"],
          ["Far site", "150", "31", "-3"]])

_T_PAIR = dict(
    headers=["Town", "Latitude (degrees north)",
             "Average annual precipitation (millimeters)"],
    rows=[["Town of Ardale", "44", "1980"],
          ["Town of Belmar", "44", "240"]])

QUESTIONS = [

 dict(q="According to the course framework, weather and climate are shaped by the sun's "
        "energy together with which additional set of influences?",
      choices=[
        "Geologic and geographic factors, such as mountains and the temperature of "
        "the ocean",
        "Only the chemical composition of the soil beneath each location",
        "Only the density of the human population living in each region",
        "The magnetic field of the Earth and the phase of the moon",
        "Nothing further, because the sun's energy alone accounts for weather and climate"],
      ans=0,
      why="ENG-2.B.1 states that weather and climate are affected not only by the sun's "
          "energy but by geologic and geographic factors, such as mountains and ocean "
          "temperature. The framework names those two examples and does not name soil "
          "chemistry, population, magnetism or lunar phase."),

 dict(q="Which of the following is the framework's definition of a rain shadow?",
      choices=[
        "A region of land that has become drier because a higher elevation area blocks "
        "precipitation from reaching it",
        "A region of land that has become wetter because a higher elevation area "
        "concentrates precipitation onto it",
        "The band of cloud that forms directly above the highest peaks of a range",
        "The area of ground that lies in the literal shade of a mountain for part of "
        "each day",
        "A stretch of coastline that receives less sunlight because offshore water is "
        "unusually cold"],
      ans=0,
      why="ENG-2.B.2 defines a rain shadow as a region of land that has become drier "
          "because a higher elevation area blocks precipitation from reaching the land. The "
          "rejected options reverse the direction of the effect or substitute an optical "
          "shadow, a cloud band, or an ocean effect for the blocking of precipitation."),

 dict(q="Moist air moves from west to east across the region described in the table. "
        "Which site lies in the rain shadow of the range?",
      table=_T_TRANSECT,
      choices=[
        "Site 5, plain east of the range",
        "Site 1, plain west of the range",
        "Site 2, western slope",
        "Site 3, crest of the range",
        "None of the sites, because every site receives some precipitation"],
      ans=0,
      why="The moist air arrives from the west, so the higher ground of the crest lies "
          "between the moisture and the eastern plain, and the eastern plain records the "
          "smallest precipitation in the table at 210 millimeters. ENG-2.B.2 defines the "
          "rain shadow as the land made drier because a higher elevation area blocks "
          "precipitation from reaching it."),

 dict(q="Using the same west to east transect, how much more precipitation does the "
        "western slope receive each year than the plain east of the range?",
      table=_T_TRANSECT,
      choices=[
        "2,190 millimeters",
        "1,640 millimeters",
        "1,290 millimeters",
        "310 millimeters",
        "2,610 millimeters"],
      ans=0,
      why="Reading the two rows and subtracting gives 2,400 minus 210, which is 2,190 "
          "millimeters. The rejected values come from pairing the wrong rows or from adding "
          "the two figures rather than taking their difference."),

 dict(q="The table gives the distance from the ocean and the monthly mean temperatures of "
        "three towns at the same latitude. Which conclusion is best supported?",
      table=_T_COASTINLAND,
      choices=[
        "The spread between the warmest and coldest months widens as a town lies farther "
        "from the ocean.",
        "The spread between the warmest and coldest months narrows as a town lies farther "
        "from the ocean.",
        "The three towns show the same spread between their warmest and coldest months.",
        "The town nearest the ocean records the highest warmest-month temperature of "
        "the three.",
        "The town farthest from the ocean records the highest coldest-month temperature of "
        "the three."],
      ans=0,
      why="The warmest minus coldest spreads are 11, 24 and 36 degrees Celsius at 2, 120 "
          "and 400 kilometers from the coast, so the spread widens with distance. ENG-2.B.1 "
          "names ocean temperature among the geographic factors that affect weather "
          "and climate."),

 dict(q="From the same three towns, what is the difference between the warmest month and "
        "the coldest month at the town lying 400 kilometers inland?",
      table=_T_COASTINLAND,
      choices=[
        "36 degrees Celsius",
        "24 degrees Celsius",
        "30 degrees Celsius",
        "11 degrees Celsius",
        "Negative 6 degrees Celsius"],
      ans=0,
      why="The plains town reads 30 degrees Celsius in its warmest month and negative 6 "
          "degrees in its coldest, and the difference between them is 36 degrees Celsius. "
          "The rejected values are the other towns' spreads or one of the two tabulated "
          "temperatures on its own."),

 dict(q="Four coastal cities report the mean temperature of the water just offshore and "
        "their own mean annual air temperature. What pattern do the values show?",
      table=_T_OFFSHORE,
      choices=[
        "Cities beside warmer offshore water have warmer mean annual air temperatures.",
        "Cities beside warmer offshore water have cooler mean annual air temperatures.",
        "Offshore water temperature and city air temperature are unrelated in these data.",
        "Every city's air temperature is exactly equal to the temperature of its "
        "offshore water.",
        "The coldest offshore water is paired with the warmest air temperature of the four."],
      ans=0,
      why="Sorted by water temperature the tabulated air temperatures are 9, 14, 20 and 26 "
          "degrees Celsius, rising without exception. ENG-2.B.1 names ocean temperature as "
          "one of the geographic factors affecting weather and climate, and no pair in the "
          "table is equal."),

 dict(q="Three cities lie at the same latitude and receive moist winds from the same "
        "direction. Using the table, which city best fits the framework's description of a "
        "rain shadow?",
      table=_T_UPWIND,
      choices=[
        "City S, the driest of the three, which the winds reach only after crossing the "
        "highest land",
        "City R, the wettest of the three, which the winds reach after crossing the "
        "lowest land",
        "City T, which lies between the other two in both precipitation and barrier height",
        "All three cities equally, because each receives winds from the same direction",
        "None of the three, because a rain shadow requires the cities to lie at different "
        "latitudes"],
      ans=0,
      why="City S records the least precipitation, 260 millimeters, and the highest upwind "
          "barrier, 3,100 meters, which is exactly the pairing ENG-2.B.2 describes when it "
          "makes a rain shadow the land left drier because a higher elevation area blocks "
          "precipitation from reaching it. Latitude is held constant by the stem."),

 dict(q="A range of hills runs along a coast, and moist winds blow in from the ocean. "
        "Which station in the table is in the rain shadow?",
      table=_T_SLOPES,
      choices=[
        "The station on the far side of the crest",
        "The station on the side the moist ocean winds reach first",
        "The station on the crest of the range",
        "Every station equally, since all three lie on the same range",
        "No station, because the highest station receives less than the lowest one"],
      ans=0,
      why="The station beyond the crest records 300 millimeters against 2,100 on the side "
          "the winds reach first and 1,400 at the crest, so it is the land the higher "
          "elevation has left driest. ENG-2.B.2 places the rain shadow on the land whose "
          "precipitation the higher elevation area blocks."),

 dict(q="Four stretches of coast report the mean temperature of the offshore water and the "
        "mean annual precipitation of the coastal strip. Which statement do the data "
        "support?",
      table=_T_COASTS,
      choices=[
        "Coastal strips beside warmer offshore water receive more precipitation in "
        "these data.",
        "Coastal strips beside warmer offshore water receive less precipitation in "
        "these data.",
        "Precipitation is the same along all four stretches of coast.",
        "The stretch beside the coldest water receives the most precipitation of the four.",
        "Precipitation along a coast cannot be related to the ocean, so the pattern must "
        "be coincidence."],
      ans=0,
      why="Sorted by water temperature the tabulated precipitation figures are 300, 620, 980 "
          "and 1,450 millimeters, rising without exception. ENG-2.B.1 names ocean temperature "
          "as a geographic factor that affects weather and climate, so a relationship between "
          "the two is exactly what the framework leads a student to look for."),

 dict(q="Three sites lie at increasing distances from a very large lake. Which reading of "
        "the table is accurate?",
      table=_T_LAKE,
      choices=[
        "The site closest to the lake has the narrowest gap between its warmest and "
        "coldest months.",
        "The site closest to the lake has the widest gap between its warmest and "
        "coldest months.",
        "The site farthest from the lake has the coolest warmest-month temperature.",
        "All three sites have the same gap between their warmest and coldest months.",
        "The site closest to the lake records the highest warmest-month temperature."],
      ans=0,
      why="The warmest minus coldest gaps are 18, 27 and 34 degrees Celsius at 1, 40 and 150 "
          "kilometers from the lake, so the lakeside site has the narrowest. ENG-2.B.1 puts "
          "the temperature of a large body of water among the geographic factors that affect "
          "weather and climate."),

 dict(q="A student writes that a rain shadow region is dry because the mountains beside it "
        "produce no rain of their own. How should that reasoning be corrected?",
      choices=[
        "The region is dry because the higher elevation area blocks precipitation from "
        "reaching it, not because the high ground itself is dry.",
        "The region is dry because the high ground reflects sunlight onto it and "
        "evaporates the water that arrives.",
        "The region is dry because mountains are always warmer than the land around them.",
        "The reasoning needs no correction, since the framework defines a rain shadow as a "
        "region without nearby mountains.",
        "The region is dry because the mountains are made of rock that absorbs rainfall "
        "before it can fall."],
      ans=0,
      why="ENG-2.B.2 attributes the dryness to a higher elevation area blocking precipitation "
          "from reaching the land beyond it. High ground in a rain shadow setting typically "
          "records substantial precipitation of its own, and the framework offers no "
          "reflection, absorption or warming mechanism."),

 dict(q="Two towns sit at the same latitude, so they receive comparable solar radiation "
        "through the year, yet the table shows very different rainfall. Which framework "
        "statement best accounts for the contrast?",
      table=_T_PAIR,
      choices=[
        "Weather and climate are affected not only by the sun's energy but also by "
        "geologic and geographic factors.",
        "Incoming solar radiation is the Earth's main source of energy and depends on "
        "season and latitude.",
        "The angle of the sun's rays determines the intensity of the solar radiation "
        "reaching a surface.",
        "The tilt of the Earth's axis of rotation causes the seasons and the number of "
        "daylight hours.",
        "The highest solar radiation per unit area is received at the equator and "
        "decreases toward the poles."],
      ans=0,
      why="The two towns share a latitude of 44 degrees north but record 1,980 and 240 "
          "millimeters of precipitation, a gap of 1,740 millimeters that latitude cannot "
          "explain. ENG-2.B.1 is the statement that admits factors beyond the sun's energy; "
          "the four rejected statements are all about solar radiation, which the stem holds "
          "constant."),

 dict(q="Which claim about the sun's role in climate is consistent with the course "
        "framework?",
      choices=[
        "The sun's energy matters, and geologic and geographic factors act alongside it.",
        "The sun's energy is irrelevant once mountains and oceans are taken into account.",
        "The sun's energy fully determines climate, so two places at one latitude must "
        "have the same climate.",
        "The sun's energy affects weather but has no effect on climate.",
        "The sun's energy affects climate but has no effect on weather."],
      ans=0,
      why="ENG-2.B.1 says weather and climate are affected NOT ONLY by the sun's energy BUT "
          "ALSO by geologic and geographic factors, which asserts that both sets of "
          "influences operate. The rejected options each drop one side of that sentence or "
          "split weather from climate in a way the framework does not."),

 dict(q="Which of the following is named in the framework as an example of a geologic or "
        "geographic factor affecting weather and climate?",
      choices=[
        "The presence of mountains",
        "The average age of the bedrock",
        "The number of hours of daylight",
        "The tilt of the Earth's axis of rotation",
        "The concentration of nitrogen in the atmosphere"],
      ans=0,
      why="ENG-2.B.1 gives mountains and ocean temperature as its two examples of geologic "
          "and geographic factors. Daylight hours and axial tilt belong to ENG-2.A.5, which "
          "is about the sun's energy rather than about geography, and neither bedrock age "
          "nor atmospheric nitrogen is offered as an example."),

 dict(q="Suppose the range in a rain shadow region were somehow leveled to the height of "
        "the surrounding plain while the winds continued to arrive from the same "
        "direction. What does the framework's definition predict for the formerly dry land?",
      choices=[
        "It would no longer be kept dry by blocked precipitation, since the blocking "
        "higher elevation would be gone.",
        "It would become drier still, because the missing range would no longer shelter "
        "it from the wind.",
        "It would be unchanged, because the framework makes the dryness a property of the "
        "land itself.",
        "It would become drier, because precipitation only falls where the ground is "
        "steeply sloped.",
        "It would receive precipitation only in winter, because the framework restricts "
        "rain shadows to one season."],
      ans=0,
      why="ENG-2.B.2 makes the higher elevation area the cause of the dryness, so removing "
          "the cause removes the effect the framework attributes to it. The framework "
          "attaches the dryness to the blocking of precipitation rather than to the land "
          "itself, to slope, or to a season."),

 dict(q="Which observation would be the strongest single piece of evidence that a dry "
        "basin is a rain shadow rather than dry for some other reason?",
      choices=[
        "Land on the other side of the higher ground upwind of the basin receives several "
        "times as much precipitation as the basin does.",
        "The basin has a lower average elevation than the higher ground beside it.",
        "The basin supports fewer tree species than the wetter land beyond the range.",
        "The basin lies at a latitude where solar radiation per unit area is high.",
        "The basin has warmer summers than the higher ground beside it."],
      ans=0,
      why="ENG-2.B.2 makes a rain shadow the land left drier because a higher elevation area "
          "blocks precipitation, so the diagnostic comparison is between the basin and the "
          "land on the far side of that blocking ground. Elevation, species count, latitude "
          "and summer warmth are all consistent with dryness produced some other way."),

 dict(q="Along the west to east transect, which site records the most precipitation, and "
        "what does its position show?",
      table=_T_TRANSECT,
      choices=[
        "Site 2 on the western slope, which the moist winds reach before crossing "
        "the crest",
        "Site 5 on the eastern plain, which the moist winds reach after crossing the crest",
        "Site 3 at the crest, which is the highest point on the transect",
        "Site 1 on the western plain, which is the lowest point on the transect",
        "Site 4 on the eastern slope, which lies partway down from the crest"],
      ans=0,
      why="The tabulated precipitation figures are 1,850, 2,400, 1,500, 520 and 210 "
          "millimeters, so the western slope holds the maximum and it lies on the side the "
          "moist air reaches first. ENG-2.B.2 places the drier land beyond the higher "
          "elevation area rather than before it."),

 dict(q="A farm cooperative on the dry eastern plain of the transect region asks why its "
        "land needs irrigation while land the same distance west of the crest does not. "
        "Which answer follows from the framework?",
      table=_T_TRANSECT,
      choices=[
        "The crest between them blocks precipitation from reaching the eastern plain, "
        "which receives 210 millimeters against 1,850 on the western plain.",
        "The eastern plain lies at a higher elevation than the western plain, which is why "
        "it receives less precipitation.",
        "The eastern plain lies at a lower latitude than the western plain, which reduces "
        "the precipitation it receives.",
        "The eastern plain receives less solar radiation per unit area than the western "
        "plain does.",
        "The two plains receive the same precipitation, so the difference must lie in the "
        "soil rather than the climate."],
      ans=0,
      why="The two plains read 210 and 1,850 millimeters with the crest between them, which "
          "is the situation ENG-2.B.2 defines as a rain shadow. The eastern plain is at 300 "
          "meters against 50, a difference far too small to be the explanation the framework "
          "offers, and the stem places both on one transect at one latitude."),

 dict(q="Two coastal cities lie at the same latitude, but the water offshore of one is much "
        "colder than the water offshore of the other. What does the framework allow a "
        "student to conclude?",
      choices=[
        "Their climates can differ, because ocean temperature is a geographic factor "
        "affecting climate.",
        "Their climates must be identical, because latitude fixes climate completely.",
        "Their climates can differ only if one of them also lies beside mountains.",
        "The city beside the colder water must receive more precipitation, since cold "
        "water always increases rainfall.",
        "The city beside the colder water must lie at a higher elevation, since elevation "
        "and water temperature are linked."],
      ans=0,
      why="ENG-2.B.1 names ocean temperature among the geologic and geographic factors that "
          "affect weather and climate, so a difference in offshore water temperature is a "
          "difference the framework recognises. It states no fixed direction for the effect "
          "and links water temperature to neither mountains nor elevation."),

 dict(q="Which of these pairs of places would be expected to show the smallest difference "
        "in climate, if the framework's two named geographic factors are the only ones "
        "that differ?",
      choices=[
        "Two towns at the same latitude, both on flat ground beside water of the same "
        "temperature",
        "Two towns at the same latitude, one beside warm water and one far inland",
        "Two towns at the same latitude, one on each side of a high mountain range",
        "Two towns at the same latitude, one beside cold water and one beside warm water",
        "Two towns at the same latitude, one on a high plateau blocking the other's "
        "moist winds"],
      ans=0,
      why="ENG-2.B.1 names mountains and ocean temperature as the geographic factors, and the "
          "keyed pair holds both of those constant along with latitude. Each rejected pair "
          "varies one of the two named factors, and ENG-2.B.2 makes the blocking case a rain "
          "shadow, which is a large difference rather than a small one."),

 dict(q="At the crest of the transect range the land is the highest on the transect, yet "
        "the crest is not the driest site. What does that show about the framework's "
        "definition?",
      table=_T_TRANSECT,
      choices=[
        "Being high is not what makes land dry; being cut off from precipitation by higher "
        "ground upwind is.",
        "Being high is what makes land dry, and the crest reading must therefore be an "
        "error.",
        "Precipitation always increases with elevation, so the crest should have been the "
        "wettest site.",
        "Elevation has no effect at all on where precipitation falls in the framework's "
        "account.",
        "The crest is the driest site, so the table contradicts itself."],
      ans=0,
      why="The crest at 2,600 meters records 1,500 millimeters while the eastern plain at 300 "
          "meters records 210, so height and dryness do not track each other here. ENG-2.B.2 "
          "makes the cause of a rain shadow the blocking of precipitation by higher ground, "
          "not the elevation of the dry land itself."),

 dict(q="Which comparison would best test whether the ocean is influencing the climate of a "
        "coastal town?",
      choices=[
        "Compare the town's monthly temperature range with that of an inland town at the "
        "same latitude and elevation.",
        "Compare the town's monthly temperature range with that of a town at a much higher "
        "latitude on the same coast.",
        "Compare the town's rainfall with the rainfall of a town on the far side of a "
        "mountain range.",
        "Compare the town's temperature in one year with its temperature in the "
        "following year.",
        "Compare the number of sunny days in the town with the number in a town on "
        "another continent."],
      ans=0,
      why="A test of one factor must vary that factor while holding the others fixed, and "
          "ENG-2.B.1 names ocean temperature and mountains as the two geographic factors and "
          "ENG-2.A.1 makes latitude a control on insolation. Only the keyed comparison "
          "changes proximity to the ocean alone."),

 dict(q="A traveller crosses a high range and finds dense moist forest on one side and open "
        "dry scrub on the other, with no change in latitude. Which explanation does the "
        "framework support?",
      choices=[
        "The range blocks precipitation from reaching the scrub side, leaving it drier "
        "than the forest side.",
        "The two sides receive different amounts of solar radiation because they face "
        "different directions.",
        "The scrub side has lost its forest to fire, which is why it is dry.",
        "The forest side lies at a lower latitude, which is why it receives more rain.",
        "The two sides have identical climates, and the vegetation differs only because of "
        "soil type."],
      ans=0,
      why="ENG-2.B.2 defines a rain shadow as land made drier because a higher elevation area "
          "blocks precipitation from reaching it, which is the described contrast across a "
          "single range. The stem holds latitude constant, and neither fire history nor soil "
          "type is a factor the framework names here."),

 dict(q="Which statement correctly distinguishes what the framework attributes to the sun "
        "from what it attributes to geography?",
      choices=[
        "The sun supplies the energy that drives atmospheric processes, while mountains and "
        "ocean temperature shape how that energy plays out at a place.",
        "The sun supplies the moisture for precipitation, while mountains supply the energy "
        "that drives atmospheric processes.",
        "Geography supplies the energy that drives atmospheric processes, while the sun "
        "determines only the length of the day.",
        "The sun affects only temperature, while geography affects only precipitation, and "
        "the two never interact.",
        "Neither the sun nor geography affects climate, which is set by the composition of "
        "the atmosphere alone."],
      ans=0,
      why="The enduring understanding ENG-2 states that most of the Earth's atmospheric "
          "processes are driven by input of energy from the sun, and ENG-2.B.1 adds geologic "
          "and geographic factors as further influences on weather and climate. The rejected "
          "options swap the two roles or partition them in ways the framework does not."),

 dict(q="Using the four coastal cities and their offshore water temperatures, what is the "
        "difference in mean annual air temperature between the city beside the warmest "
        "water and the city beside the coldest water?",
      table=_T_OFFSHORE,
      choices=[
        "17 degrees Celsius",
        "19 degrees Celsius",
        "12 degrees Celsius",
        "6 degrees Celsius",
        "35 degrees Celsius"],
      ans=0,
      why="The city beside the 25 degree water has a mean air temperature of 26 degrees and "
          "the city beside the 6 degree water has 9 degrees, and 26 minus 9 is 17 degrees "
          "Celsius. The rejected values come from differencing the water temperatures "
          "instead, from the wrong pair of cities, or from adding rather than subtracting."),

 dict(q="An atlas describes a plateau as lying in the rain shadow of a range to its west. "
        "What does that description imply about the winds that bring moisture to "
        "the region?",
      choices=[
        "They arrive from the west and must cross the range before reaching the plateau.",
        "They arrive from the east and reach the plateau before reaching the range.",
        "They arrive from directly overhead and are unaffected by the range.",
        "They arrive only in the season when the plateau is warmest.",
        "They arrive from the west but pass around the range without crossing it."],
      ans=0,
      why="ENG-2.B.2 puts the rain shadow on the land whose precipitation a higher elevation "
          "area blocks, so the moisture must reach the range before it would reach the "
          "plateau, which places the source on the far side of the range from the plateau. "
          "Winds passing around the range would not block anything."),

 dict(q="A regional planner claims that because two districts share a latitude, they will "
        "need the same water supply per hectare of farmland. Which is the best evaluation "
        "of that claim?",
      choices=[
        "It is unsound, because geologic and geographic factors can give places at one "
        "latitude very different precipitation.",
        "It is sound, because latitude is the only control the framework places on "
        "precipitation.",
        "It is unsound, because the framework states that precipitation is unrelated "
        "to latitude.",
        "It is sound, provided both districts lie at the same elevation above sea level.",
        "It is unsound, because water supply per hectare depends only on the crop grown "
        "and not on climate."],
      ans=0,
      why="ENG-2.B.1 states that weather and climate are affected not only by the sun's energy "
          "but by geologic and geographic factors, and ENG-2.B.2 gives a mechanism by which "
          "one district can be far drier than its neighbour. The framework does not deny a "
          "role for latitude, so the option calling precipitation unrelated to it overshoots."),

 dict(q="Which of the following best describes the relationship between the two "
        "statements the framework makes about geography and climate?",
      choices=[
        "The second describes one specific way that one of the factors named in the first "
        "changes the climate of a region.",
        "The second contradicts the first by removing mountains from the list of factors.",
        "The two statements describe the same effect using different words.",
        "The second applies only to coasts, while the first applies only to inland areas.",
        "The two statements apply to different planets and cannot be combined."],
      ans=0,
      why="ENG-2.B.1 names mountains among the geographic factors affecting weather and "
          "climate, and ENG-2.B.2 then defines the rain shadow, which is a specific "
          "consequence of higher elevation land. The second therefore develops the first "
          "rather than contradicting or restating it."),

 dict(q="On the coast comparison, which stretch of coast has both the coolest offshore "
        "water and the least precipitation?",
      table=_T_COASTS,
      choices=[
        "Coast W",
        "Coast X",
        "Coast Y",
        "Coast Z",
        "No stretch holds both extremes at once"],
      ans=0,
      why="The first row carries the lowest water temperature at 10 degrees Celsius and the "
          "lowest precipitation at 300 millimeters, so one stretch holds both minima. "
          "ENG-2.B.1 names ocean temperature among the geographic factors affecting weather "
          "and climate, which is why the pairing is worth reading off the data."),
]
