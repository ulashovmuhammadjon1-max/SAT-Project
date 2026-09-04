# AP ENVIRONMENTAL SCIENCE 4.5 Global Wind Patterns
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ERT-4: Earth's systems interact, resulting in a state of balance
# over time.
# Learning objective ERT-4.E: explain how environmental factors can result in atmospheric
# circulation.
# Suggested skill 2.B, explain relationships between different characteristics of
# environmental concepts, processes, or models represented visually, in theoretical and in
# applied contexts.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-4.E.1  Global wind patterns primarily result from the most intense solar radiation
#              arriving at the equator, resulting in density differences and the Coriolis
#              effect.
#
# THAT ONE SENTENCE IS THE WHOLE OF THIS TOPIC. It splits into five separable claims and
# nothing here keys anything else:
#   (a) the patterns are GLOBAL
#   (b) they PRIMARILY result from the stated cause, which is a hedge and is keyed as one
#   (c) the most intense solar radiation arrives at the EQUATOR, not anywhere else
#   (d) that results in DENSITY DIFFERENCES
#   (e) and in the CORIOLIS EFFECT, named alongside the density differences and not
#       instead of them
#
# WHAT THE SENTENCE DOES NOT SAY, and what this module therefore never keys as framework
# content: the DIRECTION in which the Coriolis effect deflects a moving parcel of air; the
# names of the prevailing winds in any band of latitude; any circulation cell; any figure
# for the solar radiation, the air density or the deflection. Items 12 and 13 key those
# absences rather than filling them.
#
# THE HEMISPHERIC DIRECTIONS ENTER ONLY AS TABULATED OBSERVATIONS. Items 23, 24, 26, 27 and
# 29 read a record of measured deflections and measured prevailing quarters. Their claims in
# verify_e4_5.py say plainly that the framework licenses the question, by naming the
# Coriolis effect among the results, while the table settles the answer.
#
# THE NORTH-SOUTH SWAP IS THE TRAP THIS TOPIC INVITES, so every item contrasting the two
# hemispheres carries an anchor naming BOTH clauses. An anchor reading only "to the right
# in the northern hemisphere" would match the swapped distractor as well as the key.
#
# NO FIGURES. This topic is normally taught from a circulation picture and the bank carries
# no images, so the latitude bands, the prevailing quarters, the solar radiation and the
# air densities are all tabulated and every question is asked of the numbers.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("4.5", "Global Wind Patterns", 4)

_T_SOLAR = dict(
    headers=["Latitude band", "Middle of the band (degrees of latitude)",
             "Solar radiation received (watts per square meter, annual average)"],
    rows=[["Band at 5 degrees", "5", "300"],
          ["Band at 25 degrees", "25", "270"],
          ["Band at 45 degrees", "45", "200"],
          ["Band at 65 degrees", "65", "130"],
          ["Band at 85 degrees", "85", "90"]])

_T_DENSITY = dict(
    headers=["Air mass", "Temperature (degrees Celsius)",
             "Density (kilograms per cubic meter)"],
    rows=[["Air mass 1", "30", "1.16"],
          ["Air mass 2", "20", "1.20"],
          ["Air mass 3", "10", "1.25"],
          ["Air mass 4", "0", "1.29"]])

_T_DEFLECT = dict(
    headers=["Trial", "Hemisphere in which the parcel was released",
             "Direction the parcel was moving when it was released",
             "Side to which its path curved",
             "Degrees by which its path had turned after one thousand kilometers"],
    rows=[["Trial 1", "Northern", "Toward the north", "The right", "12"],
          ["Trial 2", "Northern", "Toward the south", "The right", "9"],
          ["Trial 3", "Southern", "Toward the north", "The left", "11"],
          ["Trial 4", "Southern", "Toward the south", "The left", "8"]])

_T_WINDS = dict(
    headers=["Latitude band", "Quarter the prevailing surface wind blew from",
             "Days in the year it blew from that quarter"],
    rows=[["Band from 5 to 25 degrees north", "The northeast", "268"],
          ["Band from 5 to 25 degrees south", "The southeast", "271"],
          ["Band from 35 to 55 degrees north", "The southwest", "254"],
          ["Band from 35 to 55 degrees south", "The northwest", "259"]])

QUESTIONS = [

 dict(q="What does the framework say global wind patterns primarily result from?",
      choices=[
        "The most intense solar radiation arriving at the equator",
        "The most intense solar radiation arriving at the poles",
        "The rotation of the Earth alone, with no part played by solar radiation",
        "The difference in altitude between the land and the sea",
        "The relative abundance of the gases making up the atmosphere"],
      ans=0,
      why="ERT-4.E.1 states that global wind patterns primarily result from the most "
          "intense solar radiation arriving at the equator. The rejected options move that "
          "radiation to the poles, remove it altogether, or substitute a quantity from "
          "another statement."),

 dict(q="Where does the framework say the most intense solar radiation arrives?",
      choices=["At the equator", "At the poles", "At the middle latitudes",
               "At the top of the atmosphere only",
               "The framework does not say where it arrives"],
      ans=0,
      why="ERT-4.E.1 places the most intense solar radiation at the equator, and that "
          "placement is what the rest of the statement follows from."),

 dict(q="What two things does the framework say that intense equatorial radiation results "
        "in?",
      choices=[
        "Density differences and the Coriolis effect",
        "Density differences, and nothing further",
        "The Coriolis effect, and nothing further",
        "Ocean currents and tides",
        "Temperature gradients between the layers of the atmosphere"],
      ans=0,
      why="ERT-4.E.1 states that the radiation results in density differences AND the "
          "Coriolis effect, naming both. Two rejected options keep one and drop the other, "
          "and temperature gradients belong to ERT-4.D.2 and the layers of the atmosphere."),

 dict(q="The framework says global wind patterns PRIMARILY result from that cause. What "
        "does that word establish?",
      choices=[
        "That the stated cause is the main one, without the framework excluding every other "
        "influence",
        "That the stated cause is one of many and no more important than the rest",
        "That the stated cause has no effect on the wind patterns",
        "That the wind patterns have no cause the framework is willing to name",
        "That the stated cause operates only in one hemisphere"],
      ans=0,
      why="PRIMARILY commits the framework to the stated cause being the principal one "
          "while stopping short of ruling out anything else. Demoting it to one among "
          "equals is weaker than the statement and denying it outright contradicts it."),

 dict(q="Which of these does the framework NOT name as following from the intense "
        "equatorial solar radiation?",
      choices=[
        "A change in the length of the day",
        "Density differences",
        "The Coriolis effect",
        "Global wind patterns",
        "The two named results taken together"],
      ans=0,
      why="ERT-4.E.1 names density differences and the Coriolis effect as what the "
          "radiation results in, and makes the global wind patterns the thing that "
          "primarily results from all of it. The length of the day appears nowhere in the "
          "statement."),

 dict(q="What does the framework say about the relationship between the two results it "
        "names?",
      choices=[
        "Both follow from the same cause, and the statement names them together",
        "Only the density differences follow from that cause",
        "Only the Coriolis effect follows from that cause",
        "The two are alternatives, and only one of them occurs in any given case",
        "Neither of them follows from that cause"],
      ans=0,
      why="ERT-4.E.1 puts density differences and the Coriolis effect in one clause "
          "following one cause, so the statement gives both together rather than choosing "
          "between them."),

 dict(q="Which framework statement accounts for why the winds blow at all?",
      choices=[
        "That global wind patterns primarily result from the most intense solar radiation "
        "arriving at the equator",
        "That the atmosphere is made up of major gases, each with its own relative abundance",
        "That the layers of the atmosphere are based on temperature gradients",
        "That soils are generally categorized by horizons",
        "That the characteristics of a watershed include its area and its slope"],
      ans=0,
      why="ERT-4.E.1 is the statement that gives a cause for the wind patterns. The "
          "rejected statements are ERT-4.D.1, ERT-4.D.2, ERT-4.B.2 and ERT-4.F.1, none of "
          "which mentions wind."),

 dict(q="A student says the winds are caused mainly by the turning of the Earth and that "
        "solar radiation plays no part. What does the framework say?",
      choices=[
        "That the wind patterns primarily result from solar radiation arriving at the "
        "equator, with the Coriolis effect among the results rather than the whole cause",
        "That the student is right, and solar radiation plays no part in the wind patterns",
        "That the Coriolis effect is the only thing the framework names in this statement",
        "That the framework names no cause for the wind patterns at all",
        "That the wind patterns result from density differences and nothing else"],
      ans=0,
      why="ERT-4.E.1 makes the intense equatorial radiation the primary cause and lists the "
          "Coriolis effect among what that radiation results in. The student has promoted a "
          "result into the cause and dropped the cause the statement gives."),

 dict(q="Which measurement would bear on the framework's claim that the most intense solar "
        "radiation arrives at the equator?",
      choices=[
        "The solar radiation received per square meter at a range of latitudes",
        "The temperature of the ocean at one place through the year",
        "The number of days of rain recorded at the equator",
        "The height above the poles at which one layer of the atmosphere ends",
        "The share of nitrogen in a sample of the atmosphere"],
      ans=0,
      why="ERT-4.E.1 asserts that the radiation is most intense at one place rather than "
          "another, so a comparison across latitudes is what tests it. A single site, a "
          "rainfall count, a layer boundary and a gas share each measure something else."),

 dict(q="Which measurement would bear on the framework's claim that density differences "
        "follow?",
      choices=[
        "The density of air masses that differ in how much they have been heated",
        "The direction of the wind at one place on one day",
        "The share of argon in a sample of the atmosphere",
        "The depth of the soil beneath the measuring station",
        "The area of the watershed the measuring station stands in"],
      ans=0,
      why="ERT-4.E.1 states that the intense radiation results in density differences, so a "
          "record of density against heating is what bears on it. The rejected measurements "
          "belong to other statements or to no statement in the topic."),

 dict(q="Which measurement would bear on the framework's claim that the Coriolis effect "
        "follows?",
      choices=[
        "The side to which a moving parcel of air curves, recorded in both hemispheres",
        "The temperature of the parcel of air when it was released",
        "The mass of the parcel of air",
        "The time of day at which the parcel was released",
        "The altitude of the ground beneath the parcel"],
      ans=0,
      why="ERT-4.E.1 names the Coriolis effect among the results of the intense equatorial "
          "radiation, and a curving of a moving parcel is what that effect is observed as. "
          "None of the rejected quantities records a curving at all."),

 dict(q="Which of these does the framework leave unstated in this topic?",
      choices=[
        "The direction in which the Coriolis effect deflects a moving parcel of air",
        "That global wind patterns primarily result from solar radiation",
        "That the most intense solar radiation arrives at the equator",
        "That density differences result from that radiation",
        "That the Coriolis effect results from that radiation"],
      ans=0,
      why="ERT-4.E.1 supplies the four rejected options in its own words. It names the "
          "Coriolis effect without saying which way it turns a moving parcel, so that "
          "direction has to come from a measurement rather than from the statement."),

 dict(q="And which of these is also left unstated by the framework here?",
      choices=[
        "The names of the prevailing winds in each band of latitude",
        "That the wind patterns the statement accounts for are global",
        "That density differences follow from the intense equatorial radiation",
        "That the Coriolis effect follows from the intense equatorial radiation",
        "That the radiation is most intense at the equator"],
      ans=0,
      why="ERT-4.E.1 gives the cause, the two results and the global scale of the patterns, "
          "and names no wind and no band of latitude. A named prevailing wind would have to "
          "come from a record of observations."),

 dict(q="A meteorologist explains a band of steady surface winds by pointing to the uneven "
        "heating between the equator and higher latitudes and to the turning of the moving "
        "air. Which framework statement covers that explanation?",
      choices=[
        "Global wind patterns primarily result from the most intense solar radiation "
        "arriving at the equator, resulting in density differences and the Coriolis effect",
        "The layers of the atmosphere are based on temperature gradients",
        "The atmosphere is made up of major gases, each with its own relative abundance",
        "Soils can be eroded by winds or water",
        "Characteristics of a given watershed include its area, length, and slope"],
      ans=0,
      why="Uneven heating between the equator and higher latitudes is the density "
          "difference and the turning of moving air is the Coriolis effect, and ERT-4.E.1 "
          "names both as results of the intense equatorial radiation from which the wind "
          "patterns primarily follow."),

 dict(q="How does the framework order the cause and the results in this statement?",
      choices=[
        "The intense equatorial radiation comes first, the density differences and the "
        "Coriolis effect follow from it, and the global wind patterns follow from those",
        "The global wind patterns come first, the intense equatorial radiation follows from "
        "them, and the density differences follow from that",
        "The Coriolis effect comes first and the intense equatorial radiation follows from "
        "it",
        "The density differences come first and the intense equatorial radiation follows "
        "from them",
        "The framework places the three in no order at all"],
      ans=0,
      why="ERT-4.E.1 reads that global wind patterns primarily result from the most intense "
          "solar radiation arriving at the equator, RESULTING IN density differences and "
          "the Coriolis effect, so the radiation stands at the causal end and the wind "
          "patterns at the other. Each rejected option reverses a link in that chain."),

 dict(q="What does the framework claim about the scale of the wind patterns it accounts "
        "for?",
      choices=[
        "That the patterns are global",
        "That the patterns are confined to a single continent",
        "That the patterns are confined to a single ocean basin",
        "That the patterns last a single day",
        "That the framework makes no claim about their scale"],
      ans=0,
      why="ERT-4.E.1 opens with GLOBAL wind patterns, so the scale is part of the statement "
          "rather than an addition to it. No option narrowing the patterns to one continent, "
          "one basin or one day appears in the framework."),

 dict(q="Solar radiation was measured at five bands of latitude. What does the record "
        "establish?",
      table=_T_SOLAR,
      choices=[
        "The radiation received falls steadily as the latitude rises",
        "The radiation received rises steadily as the latitude rises",
        "The radiation received is the same in every band",
        "The radiation received rises and then falls again toward the pole",
        "The record reports latitude but not radiation"],
      ans=0,
      why="Ordered by latitude the readings run 300, 270, 200, 130 and 90 watts per square "
          "meter, falling at every step. ERT-4.E.1 states that the most intense solar "
          "radiation arrives at the equator, and a record falling away from low latitudes "
          "is what that looks like in numbers."),

 dict(q="Which of those bands receives the most solar radiation?",
      table=_T_SOLAR,
      choices=[
        "The band of lowest latitude, nearest the equator",
        "The band of highest latitude, nearest the pole",
        "The band in the middle of the range",
        "The band at 25 degrees",
        "All five bands receive the same amount"],
      ans=0,
      why="The largest reading in the record is unique and belongs to the band of lowest "
          "latitude. ERT-4.E.1 states that the most intense solar radiation arrives at the "
          "equator."),

 dict(q="How much more solar radiation does the lowest of those bands receive than the "
        "highest?",
      table=_T_SOLAR,
      choices=[
        "210 watts per square meter more", "300 watts per square meter more",
        "90 watts per square meter more", "170 watts per square meter more",
        "The record does not allow that comparison"],
      ans=0,
      why="The two readings are 300 and 90 watts per square meter, and 300 less 90 is 210. "
          "The rejected values are the two readings themselves and a difference between a "
          "different pair of bands."),

 dict(q="Four air masses were measured for temperature and density. What does the record "
        "establish?",
      table=_T_DENSITY,
      choices=[
        "The warmer an air mass is, the lower its density",
        "The warmer an air mass is, the higher its density",
        "All four air masses have the same density",
        "Temperature and density are unrelated across the four air masses",
        "The record reports temperature but not density"],
      ans=0,
      why="Ordered by temperature the densities run 1.29, 1.25, 1.20 and 1.16 kilograms per "
          "cubic meter, falling at every step. ERT-4.E.1 states that the intense equatorial "
          "radiation results in density differences, and uneven heating is what produces "
          "the differences the record shows."),

 dict(q="Which of those four air masses is the densest?",
      table=_T_DENSITY,
      choices=["The coldest of the four", "The warmest of the four",
               "The one at twenty degrees Celsius", "The one at ten degrees Celsius",
               "The four are of equal density"],
      ans=0,
      why="The largest density in the record is unique and belongs to the air mass with the "
          "lowest temperature. ERT-4.E.1 names density differences among the results of "
          "uneven solar heating without saying which way they run, so the record settles it."),

 dict(q="By how much do the densities of the warmest and the coldest of those air masses "
        "differ?",
      table=_T_DENSITY,
      choices=[
        "By 0.13 kilograms per cubic meter", "By 1.29 kilograms per cubic meter",
        "By 1.16 kilograms per cubic meter", "By 0.09 kilograms per cubic meter",
        "The record does not allow that comparison"],
      ans=0,
      why="The two densities are 1.29 and 1.16 kilograms per cubic meter, and the "
          "difference between them is 0.13. The rejected values are the two densities "
          "themselves and a difference between a different pair of air masses."),

 dict(q="Parcels of air were released in four trials and the curving of each path was "
        "recorded. What does the record establish?",
      table=_T_DEFLECT,
      choices=[
        "Parcels released in the northern hemisphere curved to the right, and those "
        "released in the southern hemisphere curved to the left",
        "Parcels released in the northern hemisphere curved to the left, and those released "
        "in the southern hemisphere curved to the right",
        "Every parcel curved to the right, whichever hemisphere it was released in",
        "Every parcel curved to the left, whichever hemisphere it was released in",
        "No parcel curved at all in any of the four trials"],
      ans=0,
      why="The two trials in one hemisphere both curved to one side and the two in the "
          "other hemisphere both curved to the other, and every path turned by several "
          "degrees. ERT-4.E.1 names the Coriolis effect among the results of the intense "
          "equatorial radiation without stating which way it turns a parcel, so the "
          "direction is read from the record."),

 dict(q="Did the side to which those parcels curved depend on the direction in which they "
        "were travelling?",
      table=_T_DEFLECT,
      choices=[
        "No, since within each hemisphere the parcel moving north and the parcel moving "
        "south curved to the same side",
        "Yes, since parcels moving north curved to one side and parcels moving south to the "
        "other",
        "Yes, since only the parcels moving north curved at all",
        "Yes, since only the parcels moving south curved at all",
        "The record does not report the direction in which the parcels were travelling"],
      ans=0,
      why="In each hemisphere both the northward and the southward parcel curved to the "
          "same side, and both turned by several degrees. What differs between the trials "
          "that curved oppositely is the hemisphere, not the heading."),

 dict(q="Which term from the framework names the effect that record is measuring?",
      table=_T_DEFLECT,
      choices=["The Coriolis effect", "A density difference", "A temperature gradient",
               "A relative abundance", "A watershed divide"],
      ans=0,
      why="ERT-4.E.1 names the Coriolis effect as one of the two things the intense "
          "equatorial radiation results in, and a curving of a moving parcel of air is what "
          "the record shows. Density differences are the other result, and the remaining "
          "terms belong to ERT-4.D.2, ERT-4.D.1 and ERT-4.F.1."),

 dict(q="Prevailing surface winds were recorded in four bands of latitude. What do the two "
        "bands nearer the equator show?",
      table=_T_WINDS,
      choices=[
        "In the northern band the wind blew from the northeast, and in the southern band it "
        "blew from the southeast",
        "In the northern band the wind blew from the southeast, and in the southern band it "
        "blew from the northeast",
        "In both bands the wind blew from the northeast",
        "In both bands the wind blew from the southeast",
        "Neither band had a prevailing wind"],
      ans=0,
      why="The two bands nearer the equator record different quarters from one another, and "
          "each recorded its quarter on more than half the days of the year. ERT-4.E.1 "
          "names no wind and no band, so the quarters come from the record."),

 dict(q="And what do the two bands of middle latitude show in that same record?",
      table=_T_WINDS,
      choices=[
        "In the northern band the wind blew from the southwest, and in the southern band it "
        "blew from the northwest",
        "In the northern band the wind blew from the northwest, and in the southern band it "
        "blew from the southwest",
        "In both bands the wind blew from the southwest",
        "In both bands the wind blew from the northwest",
        "Neither band had a prevailing wind"],
      ans=0,
      why="The two middle latitude bands record different quarters from one another, and "
          "each recorded its quarter on more than half the days of the year. ERT-4.E.1 "
          "names no prevailing wind, so the quarters come from the record."),

 dict(q="How often did the wind blow from the recorded quarter in each of those four bands?",
      table=_T_WINDS,
      choices=[
        "On more than half the days of the year in every band",
        "On fewer than half the days of the year in every band",
        "On more than half the days in one band only",
        "On every day of the year in every band",
        "The record does not report how often the wind blew from each quarter"],
      ans=0,
      why="Each of the four bands records its quarter on more than 182 days and on fewer "
          "than 365, so each has a prevailing wind without the wind being constant. That is "
          "what makes the quarter recorded a pattern rather than a single observation."),

 dict(q="What does the mirroring between the northern and southern bands in that record "
        "bear on?",
      table=_T_WINDS,
      choices=[
        "The Coriolis effect, which the framework names among the results of the intense "
        "equatorial radiation",
        "The relative abundance of the gases in the atmosphere",
        "The categorisation of soils by horizons",
        "The area and slope of a watershed",
        "Nothing that the framework names"],
      ans=0,
      why="In each pair of bands the northern and southern quarters differ from one "
          "another while both are prevailing, which is a difference between the hemispheres "
          "rather than between the latitudes. ERT-4.E.1 names the Coriolis effect among the "
          "results of the intense equatorial radiation, and the remaining options belong to "
          "ERT-4.D.1, ERT-4.B.2 and ERT-4.F.1."),

 dict(q="Which single sentence collects what this topic's statement asserts and nothing "
        "further?",
      choices=[
        "Global wind patterns primarily result from the most intense solar radiation "
        "arriving at the equator, which results in density differences and the Coriolis "
        "effect",
        "Global wind patterns entirely result from the most intense solar radiation "
        "arriving at the poles, which results in density differences alone",
        "Global wind patterns primarily result from the most intense solar radiation "
        "arriving at the equator, which results in the Coriolis effect alone",
        "Local wind patterns primarily result from the most intense solar radiation "
        "arriving at the equator, which results in density differences and the Coriolis "
        "effect",
        "Global wind patterns primarily result from density differences, which result in "
        "the most intense solar radiation arriving at the equator"],
      ans=0,
      why="ERT-4.E.1 supplies the global scale, the hedge PRIMARILY, the equatorial "
          "placement of the most intense radiation, and both named results. Each rejected "
          "summary hardens the hedge, moves the radiation to the poles, drops one of the "
          "two results, narrows the scale, or reverses the direction of the causation."),
]
