# AP ENVIRONMENTAL SCIENCE 4.9 El Nino and La Nina
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ENG-2: most of the Earth's atmospheric processes are driven
# by input of energy from the sun.
# Learning objective ENG-2.C: describe the environmental changes and effects that
# result from El Nino or La Nina events (El Nino-Southern Oscillation).
# Suggested skill 7.A, describe environmental problems.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-2.C.1  El Nino and La Nina are phenomena associated with changing ocean surface
#              temperatures in the Pacific Ocean. These phenomena can cause global
#              changes to rainfall, wind, and ocean circulation patterns.
#   ENG-2.C.2  El Nino and La Nina are influenced by geological and geographic factors
#              and can affect different locations in different ways.
#
# SCOPE, AND THE ONE THING THIS TOPIC IS EASY TO GET WRONG. The framework does NOT say
# which of the two phases warms the eastern Pacific and which cools it, does not name a
# trade wind, a thermocline or an upwelling, and does not attach a named consequence to
# a named country. So NO key here requires a student to recall the direction of a
# phase. Where a direction is needed, the STEM SUPPLIES IT, exactly as the CED's own
# sample question 15 does when it opens "During an El Nino event, warm surface water
# moves from the western equatorial Pacific Ocean to the eastern equatorial region."
# Everything the student must add is either one of the two sentences above or a
# conclusion recomputed from the table printed with the question.
#
# BOUNDARY WITH 4.8. Topic 4.8 treats ocean temperature as a standing geographic
# feature of a coast under ENG-2.B.1. Every item here turns on CHANGING Pacific surface
# temperatures and on the framework's claim that different locations are affected in
# different ways, which 4.8 does not touch.
#
# NO FIGURES. Every quantitative item carries a table= rather than a described picture.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.9", "El Niño and La Niña", 4)

_T_ANOM = dict(
    headers=["Region",
             "Sea surface temperature during the event compared with the long term "
             "average (degrees Celsius)",
             "Rainfall during the event as a percentage of the long term average (%)"],
    rows=[["Eastern equatorial Pacific coast", "2.3", "260"],
          ["Western equatorial Pacific", "-1.1", "55"],
          ["Interior of a southern continent", "0.0", "70"],
          ["Northern mid latitude coast", "0.4", "125"]])

_T_PHASE = dict(
    headers=["Group of years",
             "Mean sea surface temperature of the eastern equatorial Pacific "
             "(degrees Celsius)",
             "Rainfall at a station on the eastern Pacific coast (millimeters)"],
    rows=[["Neutral years", "24.0", "300"],
          ["Warm phase years", "27.5", "900"],
          ["Cool phase years", "22.5", "120"]])

_T_CATCH = dict(
    headers=["Year",
             "Sea surface temperature above the long term average in the eastern "
             "equatorial Pacific (degrees Celsius)",
             "Fish landed by the coastal fishery (thousands of tonnes)"],
    rows=[["Year 1", "0.1", "820"],
          ["Year 2", "2.4", "180"],
          ["Year 3", "0.3", "790"],
          ["Year 4", "1.8", "310"]])

_T_WIND = dict(
    headers=["Section of the equatorial Pacific",
             "Mean surface wind speed in neutral years (meters per second)",
             "Mean surface wind speed during the event (meters per second)"],
    rows=[["Western section", "6.5", "3.1"],
          ["Central section", "5.8", "2.4"],
          ["Eastern section", "4.9", "2.2"]])

_T_GLOBAL = dict(
    headers=["Location",
             "Rainfall during the event as a percentage of that location's long term "
             "average (%)"],
    rows=[["Site in maritime southeast Asia", "62"],
          ["Site on the Pacific coast of South America", "245"],
          ["Site in eastern Africa", "150"],
          ["Site in southern Africa", "74"],
          ["Site in the central United States", "104"]])

_T_DEPTH = dict(
    headers=["Depth below the sea surface (meters)",
             "Water temperature in neutral years (degrees Celsius)",
             "Water temperature during the event (degrees Celsius)"],
    rows=[["0", "23", "30"],
          ["50", "18", "24"],
          ["100", "15", "19"],
          ["200", "13", "14"]])

_T_TWOEVENTS = dict(
    headers=["Region",
             "Rainfall in warm phase years as a percentage of the average (%)",
             "Rainfall in cool phase years as a percentage of the average (%)"],
    rows=[["Region 1", "230", "60"],
          ["Region 2", "55", "150"],
          ["Region 3", "105", "98"]])

QUESTIONS = [

 dict(q="El Nino and La Nina are described in the course framework as phenomena "
        "associated with which of the following?",
      choices=[
        "Changing ocean surface temperatures in the Pacific Ocean",
        "Changing salinity of the deep water of the Atlantic Ocean",
        "Changing thickness of the ozone layer above the poles",
        "Changing tilt of the Earth's axis of rotation over thousands of years",
        "Changing rates at which continents move apart along ocean ridges"],
      ans=0,
      why="ENG-2.C.1 states that El Nino and La Nina are phenomena associated with changing "
          "ocean surface temperatures in the Pacific Ocean. The framework attaches them to "
          "neither Atlantic salinity nor the ozone layer, and the tilt of the axis belongs to "
          "ENG-2.A.5 while plate motion belongs elsewhere in the unit."),

 dict(q="Which three patterns does the framework say these Pacific phenomena can change on "
        "a global scale?",
      choices=[
        "Rainfall, wind, and ocean circulation",
        "Rainfall, soil texture, and the length of the growing season",
        "Wind, atmospheric oxygen concentration, and volcanic activity",
        "Ocean circulation, the Earth's albedo, and the rate of continental drift",
        "Rainfall, the number of daylight hours, and the angle of the sun's rays"],
      ans=0,
      why="ENG-2.C.1 states that these phenomena can cause global changes to rainfall, wind, "
          "and ocean circulation patterns, and names exactly those three. Daylight hours and "
          "the angle of the sun's rays belong to ENG-2.A.5 and ENG-2.A.2, which are about "
          "solar input rather than about these events."),

 dict(q="A research team compiles the values in the table for a single event year. Which "
        "conclusion does the framework support?",
      table=_T_ANOM,
      choices=[
        "The event left some regions much wetter than usual and others much drier, so it "
        "affected different locations in different ways.",
        "The event left every region wetter than usual by about the same proportion.",
        "The event left every region drier than usual by about the same proportion.",
        "The event changed sea surface temperature but left rainfall unchanged everywhere.",
        "The event changed rainfall only in regions whose sea surface temperature was "
        "unchanged."],
      ans=0,
      why="The rainfall column runs 260, 55, 70 and 125 percent of the long term average, so "
          "two regions are wetter and two are drier in the same year. ENG-2.C.2 states that "
          "El Nino and La Nina can affect different locations in different ways, which is "
          "exactly the pattern in the table."),

 dict(q="From the same event year data, which region departed furthest from its long term "
        "rainfall average?",
      table=_T_ANOM,
      choices=[
        "The eastern equatorial Pacific coast, at 160 percentage points above average",
        "The western equatorial Pacific, at 45 percentage points below average",
        "The interior of the southern continent, at 30 percentage points below average",
        "The northern mid latitude coast, at 25 percentage points above average",
        "All four regions departed by the same amount"],
      ans=0,
      why="Taking each rainfall figure away from 100 gives departures of 160, 45, 30 and 25 "
          "percentage points, so the largest belongs to the eastern equatorial Pacific coast. "
          "ENG-2.C.2 leads a student to expect exactly this kind of unequal response across "
          "locations."),

 dict(q="A station on the eastern Pacific coast reports the values in the table for three "
        "groups of years. What relationship do the data show?",
      table=_T_PHASE,
      choices=[
        "Years with warmer eastern Pacific surface water are years with more rainfall at "
        "this station.",
        "Years with warmer eastern Pacific surface water are years with less rainfall at "
        "this station.",
        "Rainfall at this station is the same in all three groups of years.",
        "Rainfall at this station is highest in the group with the coolest surface water.",
        "Sea surface temperature at this station is the same in all three groups of years."],
      ans=0,
      why="Ordered by sea surface temperature the rainfall figures run 120, 300 and 900 "
          "millimeters, rising without exception. ENG-2.C.1 makes changing Pacific surface "
          "temperatures the thing these phenomena are associated with and names rainfall "
          "among the patterns they can change."),

 dict(q="Using the same three groups of years, how much more rain falls at that coastal "
        "station in warm phase years than in cool phase years?",
      table=_T_PHASE,
      choices=[
        "780 millimeters",
        "600 millimeters",
        "180 millimeters",
        "900 millimeters",
        "1,020 millimeters"],
      ans=0,
      why="Subtracting the two tabulated figures gives 900 minus 120, which is 780 "
          "millimeters. The rejected values come from pairing the warm phase with the neutral "
          "years, from the neutral to cool gap, from one figure standing alone, and from "
          "adding rather than subtracting."),

 dict(q="During an El Nino event, warm surface water moves from the western equatorial "
        "Pacific Ocean to the eastern equatorial region. What does that statement, together "
        "with the framework, allow a student to expect?",
      choices=[
        "Sea surface temperatures on the two sides of the Pacific change in opposite "
        "directions, and the changes can alter rainfall and wind patterns.",
        "Sea surface temperatures rise everywhere in the Pacific at once, so no east to "
        "west difference remains.",
        "Sea surface temperatures are unaffected, because moving water carries no heat "
        "with it.",
        "Rainfall and wind patterns stay fixed, because the framework restricts these "
        "events to the ocean.",
        "Ocean circulation changes but rainfall cannot, because rainfall is set by "
        "latitude alone."],
      ans=0,
      why="The stem supplies the movement of warm water from the western to the eastern "
          "equatorial Pacific, and ENG-2.C.1 makes these phenomena a matter of changing "
          "Pacific surface temperatures that can cause global changes to rainfall, wind, and "
          "ocean circulation patterns. Moving warm water away from one region and toward "
          "another moves the two temperatures oppositely."),

 dict(q="A coastal fishery records the values in the table over four years. What "
        "association do the data show?",
      table=_T_CATCH,
      choices=[
        "Years in which the eastern Pacific surface was much warmer than average were years "
        "of much smaller catches.",
        "Years in which the eastern Pacific surface was much warmer than average were years "
        "of much larger catches.",
        "Catch size was the same in all four years regardless of surface temperature.",
        "The warmest year of the four produced the largest catch of the four.",
        "Surface temperature was the same in all four years, so no association can be read."],
      ans=0,
      why="Ordered by temperature departure the catches run 820, 790, 310 and 180 thousand "
          "tonnes, falling without exception as the departure grows. The framework's claim "
          "here is only that these events involve changing Pacific surface temperatures "
          "(ENG-2.C.1) and affect different locations in different ways (ENG-2.C.2); the "
          "direction of the association is read from the data, not assumed."),

 dict(q="Wind speeds along three sections of the equatorial Pacific were measured in "
        "neutral years and again during an event. What do the values show?",
      table=_T_WIND,
      choices=[
        "Surface winds were weaker in every section during the event than in neutral years.",
        "Surface winds were stronger in every section during the event than in "
        "neutral years.",
        "Surface winds were unchanged in every section during the event.",
        "Surface winds weakened in the western section but strengthened in the eastern "
        "section.",
        "Surface winds can be compared only within one section, so the table supports "
        "no conclusion."],
      ans=0,
      why="Each section falls from its neutral value to its event value, 6.5 to 3.1, 5.8 to "
          "2.4 and 4.9 to 2.2 meters per second. ENG-2.C.1 names wind among the patterns "
          "these phenomena can change, so a uniform weakening across the basin is a change "
          "the framework recognises."),

 dict(q="Rainfall was recorded at five widely separated locations during one event and "
        "compared with each location's own long term average. Which statement is best "
        "supported?",
      table=_T_GLOBAL,
      choices=[
        "The event was associated with wetter conditions at some locations, drier "
        "conditions at others, and almost no change at one.",
        "The event was associated with wetter conditions at every location listed.",
        "The event was associated with drier conditions at every location listed.",
        "The event was associated with a change only at locations bordering the "
        "Pacific Ocean.",
        "The event was associated with identical percentage changes at all five locations."],
      ans=0,
      why="The five figures are 62, 245, 150, 74 and 104 percent of average, so two are well "
          "below 100, two are well above, and one is within a few points of it. ENG-2.C.2 "
          "states that these phenomena can affect different locations in different ways, and "
          "the eastern African and southern African sites show that the changes are not "
          "confined to the Pacific rim."),

 dict(q="Which statement about the reach of these events matches the framework?",
      choices=[
        "Although the temperature change is in the Pacific, the framework says the changes "
        "in rainfall, wind, and ocean circulation can be global.",
        "The framework confines every effect of these events to the Pacific Ocean itself.",
        "The framework confines every effect of these events to the Southern Hemisphere.",
        "The framework says the effects are global but identical everywhere on Earth.",
        "The framework says the effects appear only in years when the temperature change "
        "exceeds five degrees Celsius."],
      ans=0,
      why="ENG-2.C.1 places the changing surface temperatures in the Pacific Ocean and then "
          "says these phenomena can cause GLOBAL changes to rainfall, wind, and ocean "
          "circulation patterns. ENG-2.C.2 adds that different locations are affected in "
          "different ways, which rules out an identical global response."),

 dict(q="What does the framework say influences El Nino and La Nina themselves?",
      choices=[
        "Geological and geographic factors",
        "The chemical composition of rainfall over the tropics",
        "The total number of hours of daylight received at the equator",
        "The rate at which humans withdraw groundwater from coastal aquifers",
        "Nothing at all, since the framework treats them as entirely random"],
      ans=0,
      why="ENG-2.C.2 states that El Nino and La Nina are influenced by geological and "
          "geographic factors and can affect different locations in different ways. The "
          "framework names no chemical, solar, or human control on the events themselves in "
          "this topic."),

 dict(q="Water temperature was measured at four depths in the eastern equatorial Pacific in "
        "neutral years and again during an event. What do the two columns show?",
      table=_T_DEPTH,
      choices=[
        "The warming during the event was largest at the surface and smallest at the "
        "greatest depth measured.",
        "The warming during the event was largest at the greatest depth and smallest at "
        "the surface.",
        "The warming during the event was the same at all four depths.",
        "The water was cooler at every depth during the event than in neutral years.",
        "Only the deepest measurement changed between the two sets of years."],
      ans=0,
      why="The event minus neutral differences are 7, 6, 4 and 1 degrees Celsius at 0, 50, "
          "100 and 200 meters, so the change falls steadily with depth and is only one degree "
          "at 200 meters. ENG-2.C.1 identifies these phenomena with changing ocean SURFACE "
          "temperatures, and the data show the change concentrated near the surface."),

 dict(q="Rainfall in three regions is compared between warm phase years and cool phase "
        "years. Which reading of the table is accurate?",
      table=_T_TWOEVENTS,
      choices=[
        "Two regions swing in opposite directions between the two phases, while the third "
        "barely moves.",
        "All three regions are wetter in warm phase years than in cool phase years.",
        "All three regions are drier in warm phase years than in cool phase years.",
        "The region that barely moves is the one with the largest warm phase figure.",
        "The two phases produce the same rainfall in every region listed."],
      ans=0,
      why="Region 1 goes from 230 to 60 percent of average while Region 2 goes from 55 to 150, "
          "and Region 3 moves only from 105 to 98. ENG-2.C.2 states that these phenomena can "
          "affect different locations in different ways, which is what opposite swings in two "
          "regions and near-indifference in a third amount to."),

 dict(q="A student claims that because El Nino begins in the Pacific, a farmer in the "
        "interior of Africa has no reason to follow forecasts of it. How should the claim "
        "be evaluated using the framework?",
      choices=[
        "It is unsound, because the framework says these phenomena can cause global changes "
        "to rainfall.",
        "It is sound, because the framework confines the effects of these phenomena to the "
        "Pacific basin.",
        "It is sound, because the framework says rainfall is controlled only by latitude.",
        "It is unsound, because the framework says these phenomena change the tilt of the "
        "Earth's axis.",
        "It is unsound, because the framework says every location experiences the same "
        "change at the same time."],
      ans=0,
      why="ENG-2.C.1 states that these phenomena can cause global changes to rainfall, wind, "
          "and ocean circulation patterns, so a location far from the Pacific is not "
          "automatically outside their reach. ENG-2.C.2 adds that locations are affected in "
          "different ways, which is not the same as all being affected identically."),

 dict(q="Which pair of observations, taken together, would best identify a year as one of "
        "these events according to the framework's own description?",
      choices=[
        "A marked departure of Pacific sea surface temperature from its long term average, "
        "together with unusual rainfall and wind patterns in several regions",
        "A marked departure of Atlantic sea surface temperature from its average, together "
        "with unusual snowfall in one region",
        "An unusual number of earthquakes around the Pacific rim, together with a change in "
        "sea level",
        "A change in the length of the day, together with a change in the number of "
        "daylight hours at the equator",
        "An increase in the concentration of carbon dioxide in the atmosphere, together "
        "with a rise in global mean temperature"],
      ans=0,
      why="ENG-2.C.1 defines these phenomena by changing ocean surface temperatures in the "
          "Pacific and by the global changes to rainfall, wind, and ocean circulation they "
          "can cause, so the diagnostic pair is a Pacific temperature departure plus those "
          "pattern changes. The rejected pairs describe other phenomena entirely."),

 dict(q="Two coastal communities on opposite sides of the Pacific both prepare for the same "
        "event. What does the framework suggest about the preparations they need?",
      choices=[
        "Their preparations may need to differ, because the same event can affect different "
        "locations in different ways.",
        "Their preparations should be identical, because a single event produces one effect "
        "worldwide.",
        "Only the eastern community needs to prepare, because the framework restricts the "
        "effects to one side of the ocean.",
        "Neither community needs to prepare, because the framework describes these events "
        "as ocean phenomena with no effect on land.",
        "Their preparations should depend only on their latitude, because latitude fixes "
        "the effect of an event."],
      ans=0,
      why="ENG-2.C.2 states plainly that El Nino and La Nina can affect different locations in "
          "different ways, so one plan cannot be assumed to fit both coasts. ENG-2.C.1 makes "
          "the changes global rather than confined to one side of the ocean or to the water "
          "itself."),

 dict(q="Using the event year table, what is the difference in sea surface temperature "
        "departure between the eastern equatorial Pacific coast and the western "
        "equatorial Pacific?",
      table=_T_ANOM,
      choices=[
        "3.4 degrees Celsius",
        "1.2 degrees Celsius",
        "2.3 degrees Celsius",
        "1.9 degrees Celsius",
        "1.1 degrees Celsius"],
      ans=0,
      why="The eastern coast is 2.3 degrees Celsius above its average and the western Pacific "
          "is 1.1 degrees below, so the two departures are 3.4 degrees Celsius apart. The "
          "rejected values subtract instead of spanning the two signs, or quote one departure "
          "on its own."),

 dict(q="Which statement best describes what the framework means when it calls these "
        "phenomena an oscillation between two named states?",
      choices=[
        "Pacific surface temperatures depart from their average in one direction, and in "
        "other periods in the other direction.",
        "Pacific surface temperatures rise steadily year after year without ever returning "
        "toward their average.",
        "Pacific surface temperatures are held exactly constant by the depth of the ocean.",
        "Pacific surface temperatures change only where a river enters the ocean.",
        "Pacific surface temperatures change in step with the phases of the moon each month."],
      ans=0,
      why="ENG-2.C.1 associates both El Nino and La Nina with CHANGING ocean surface "
          "temperatures in the Pacific, and the learning objective names the pair as the El "
          "Nino-Southern Oscillation, which is a back and forth rather than a one way trend. "
          "The framework offers no lunar or river control."),

 dict(q="Which of the following is the most defensible use of the fishery data recorded "
        "over the four years in the table?",
      table=_T_CATCH,
      choices=[
        "The four years show an association between larger surface temperature departures "
        "and smaller catches, which supports further investigation rather than a "
        "settled cause.",
        "The four years prove that surface temperature is the only thing that determines "
        "the size of a fish catch.",
        "The four years show no association at all, so nothing further need be examined.",
        "The four years prove that fishing effort rose in the two warmest years.",
        "The four years show that catches rise as surface temperature departures grow "
        "larger."],
      ans=0,
      why="Ordered by departure the catches fall from 820 to 180 thousand tonnes, which is an "
          "association, and four years of two variables cannot establish a sole cause or "
          "measure fishing effort, which the table does not report. The framework claims only "
          "that these events involve changing Pacific surface temperatures and affect "
          "locations in different ways."),

 dict(q="A textbook lists three consequences of a strong event: heavier rain on one "
        "continental coast, drought on another, and a shift in surface currents. Which "
        "framework statement covers all three at once?",
      choices=[
        "These phenomena can cause global changes to rainfall, wind, and ocean "
        "circulation patterns.",
        "Weather and climate are affected by geologic and geographic factors such as "
        "mountains.",
        "A rain shadow is a region made drier because higher elevation land blocks "
        "precipitation.",
        "Incoming solar radiation is the Earth's main source of energy and depends on "
        "season and latitude.",
        "The tilt of the Earth's axis of rotation causes the seasons and the hours "
        "of daylight."],
      ans=0,
      why="Heavier rain and drought are rainfall changes and a shift in surface currents is a "
          "change in ocean circulation, and ENG-2.C.1 names rainfall, wind, and ocean "
          "circulation patterns together. The rejected statements belong to topics 4.7 and "
          "4.8 and cover none of the three."),

 dict(q="In which way does ENG-2.C.2 go beyond ENG-2.C.1?",
      choices=[
        "It adds that these phenomena are themselves influenced by geological and "
        "geographic factors, and that their effects vary from place to place.",
        "It adds that these phenomena occur in the Atlantic Ocean as well as the Pacific.",
        "It adds that these phenomena affect ocean circulation but not rainfall.",
        "It withdraws the claim that these phenomena have any global effect.",
        "It adds that these phenomena occur on a fixed schedule of exactly seven years."],
      ans=0,
      why="ENG-2.C.1 states what the phenomena are associated with and what they can change; "
          "ENG-2.C.2 then states that they are influenced by geological and geographic factors "
          "and can affect different locations in different ways. It adds a cause and a "
          "qualification rather than moving the ocean, dropping a pattern, or fixing a period."),

 dict(q="Which observation would most weaken a claim that a particular drought was "
        "connected to one of these Pacific events?",
      choices=[
        "Droughts of the same severity occurred at that location in years when Pacific "
        "surface temperatures were close to their long term average.",
        "The Pacific surface temperature departed from its average during the drought year.",
        "Rainfall in other regions also departed from average during the same year.",
        "The location lies far from the Pacific Ocean.",
        "Surface winds over the equatorial Pacific were unusual during the drought year."],
      ans=0,
      why="If the same droughts occur without any Pacific temperature departure, the departure "
          "is not doing the work the claim assigns it. Distance from the Pacific weakens "
          "nothing, because ENG-2.C.1 makes the changes global, and the other three "
          "observations are consistent with the claim rather than against it."),

 dict(q="Using the wind speed comparison, by how much did the mean surface wind speed of the "
        "western section fall between neutral years and the event?",
      table=_T_WIND,
      choices=[
        "3.4 meters per second",
        "2.7 meters per second",
        "3.1 meters per second",
        "1.6 meters per second",
        "9.6 meters per second"],
      ans=0,
      why="The western section reads 6.5 meters per second in neutral years and 3.1 during the "
          "event, so the fall is 3.4 meters per second. The rejected values come from the "
          "other sections, from the event value alone, or from adding the two figures."),

 dict(q="Which experimental or observational design would best show whether a change in "
        "Pacific surface temperature is associated with rainfall changes in a distant "
        "region, as the framework claims?",
      choices=[
        "Compare that region's rainfall in many years of large Pacific temperature "
        "departures with its rainfall in many years of small departures.",
        "Compare that region's rainfall in a single event year with its rainfall in the "
        "year immediately after.",
        "Compare that region's rainfall with the rainfall of a neighbouring region in the "
        "same year.",
        "Compare Pacific surface temperature in one year with Pacific surface temperature "
        "ten years later.",
        "Compare that region's average temperature with the average temperature of the "
        "Pacific Ocean."],
      ans=0,
      why="The claim links a Pacific temperature departure to a rainfall response elsewhere, so "
          "the design must group many years by the size of the departure and compare the "
          "rainfall that follows. A single pair of years cannot separate the association from "
          "ordinary year to year variation, and the other comparisons omit one of the two "
          "variables."),

 dict(q="Which conclusion about the interior of the southern continent is supported by the "
        "event year table, and which is not?",
      table=_T_ANOM,
      choices=[
        "Its rainfall fell well below average even though the sea surface temperature beside "
        "it was unchanged, so the effect reached it without a local temperature change.",
        "Its rainfall rose well above average, which shows that inland regions always get "
        "wetter during these events.",
        "Its rainfall was unchanged, which shows that inland regions are never affected.",
        "Its sea surface temperature departure was the largest in the table, which explains "
        "its rainfall.",
        "Its rainfall and its sea surface temperature both fell, which shows the two always "
        "move together."],
      ans=0,
      why="That row reads a temperature departure of 0.0 degrees Celsius with rainfall at 70 "
          "percent of the long term average, so rainfall fell while the local sea surface "
          "temperature did not. ENG-2.C.1 makes the rainfall changes global rather than local "
          "to the water that warmed, and ENG-2.C.2 makes the response vary by location."),

 dict(q="What is the best reason the framework pairs El Nino and La Nina in a single topic "
        "rather than treating them separately?",
      choices=[
        "Both are associated with changing ocean surface temperatures in the same ocean and "
        "both can change rainfall, wind, and ocean circulation patterns.",
        "Both occur in the same calendar month of every year, so they can be studied "
        "together.",
        "Both are caused by human emissions of greenhouse gases, so they share a control.",
        "Both are confined to the same small stretch of coastline, so one description "
        "covers them.",
        "Both produce exactly the same effect in every location, so distinguishing them is "
        "unnecessary."],
      ans=0,
      why="ENG-2.C.1 names the two together as phenomena associated with changing ocean surface "
          "temperatures in the Pacific Ocean that can cause global changes to the same three "
          "patterns. ENG-2.C.2 makes their effects vary by location, which is the opposite of "
          "producing one identical effect."),

 dict(q="Using the rainfall comparison across five locations, how many of the listed "
        "locations recorded rainfall more than twenty percentage points away from their own "
        "long term average during the event?",
      table=_T_GLOBAL,
      choices=[
        "Four of the five",
        "Two of the five",
        "All five locations",
        "Exactly one of the five",
        "None of them"],
      ans=0,
      why="The departures from 100 percent are 38, 145, 50, 26 and 4 percentage points, so four "
          "exceed twenty and one does not. ENG-2.C.2 states that these phenomena can affect "
          "different locations in different ways, which the mixed set of departures shows."),

 dict(q="An analyst notes that the same event brought record rain to one river basin and "
        "record low flow to another. Which framework statement most directly accounts for "
        "that combination?",
      choices=[
        "El Nino and La Nina can affect different locations in different ways.",
        "El Nino and La Nina are confined to the surface waters of the Pacific Ocean.",
        "El Nino and La Nina change ocean circulation but never change rainfall.",
        "El Nino and La Nina occur only in years of unusually high solar radiation.",
        "El Nino and La Nina raise rainfall everywhere at once by the same proportion."],
      ans=0,
      why="ENG-2.C.2 states that these phenomena can affect different locations in different "
          "ways, which is precisely a record wet basin and a record dry basin in one event. "
          "ENG-2.C.1 already names rainfall among the patterns they change, so the option "
          "denying that is inconsistent with the framework."),

 dict(q="Which of the following best summarises the topic's two essential knowledge "
        "statements together?",
      choices=[
        "Pacific surface temperature changes drive global shifts in rainfall, wind, and "
        "ocean circulation, and those shifts are shaped by geography and differ from place "
        "to place.",
        "Pacific surface temperature changes drive global shifts in rainfall alone, and "
        "those shifts are identical in every location.",
        "Atlantic surface temperature changes drive local shifts in wind, and geography has "
        "no bearing on them.",
        "Pacific surface temperature is held constant by geography, so no global shifts "
        "occur at all.",
        "Global shifts in rainfall, wind, and circulation occur first and then change "
        "Pacific surface temperature, with no role for geography."],
      ans=0,
      why="ENG-2.C.1 supplies the Pacific surface temperature association and the three global "
          "patterns, and ENG-2.C.2 supplies the influence of geological and geographic factors "
          "and the different effects in different locations. The rejected summaries drop a "
          "pattern, move the ocean, or reverse the framework's order of description."),
]
