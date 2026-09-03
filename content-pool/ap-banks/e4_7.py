# AP ENVIRONMENTAL SCIENCE 4.7 Solar Radiation and Earth's Seasons
# CED effective Fall 2026, Unit 4 Earth Systems and Resources.
# Enduring understanding ENG-2: most of the Earth's atmospheric processes are driven
# by input of energy from the sun.
# Learning objective ENG-2.A: explain how the sun's energy affects the Earth's surface.
# Suggested skill 2.A, describe characteristics of an environmental concept, process,
# or model represented visually.
#
# Essential knowledge relied on, in the framework's own words:
#   ENG-2.A.1  Incoming solar radiation (insolation) is the Earth's main source of
#              energy and is dependent on season and latitude.
#   ENG-2.A.2  The angle of the sun's rays determines the intensity of the solar
#              radiation. Due to the shape of the Earth, the latitude that is directly
#              horizontal to the solar radiation receives the most intensity.
#   ENG-2.A.3  The highest solar radiation per unit area is received at the equator and
#              decreases toward the poles.
#   ENG-2.A.4  The solar radiation received at a location on the Earth's surface varies
#              seasonally, with the most radiation received during the location's
#              longest summer day and the least on the shortest winter day.
#   ENG-2.A.5  The tilt of Earth's axis of rotation causes the Earth's seasons and the
#              number of hours of daylight in a particular location on the Earth's
#              surface.
#
# SCOPE. The framework states that the angle of the rays sets the intensity and that
# the tilt causes both the seasons and the hours of daylight. It states no formula, no
# solar constant and no named date beyond "longest summer day" and "shortest winter
# day", so no key here rests on a cosine law or on a remembered number. Every
# quantitative claim is read from the table printed with the question and recomputed
# in verify_e4_7.py from that table alone.
#
# NO FIGURES. The suggested skill is visual, and the bank cannot carry images, so each
# visual item is served by a table= instead of a described picture.
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("4.7", "Solar Radiation and Earth's Seasons", 4)

_T_LATITUDE = dict(
    headers=["Latitude",
             "Average solar radiation received per unit area over a year "
             "(watts per square meter)"],
    rows=[["0 degrees", "275"],
          ["20 degrees", "263"],
          ["40 degrees", "204"],
          ["60 degrees", "131"],
          ["80 degrees", "86"]])

_T_ANGLE = dict(
    headers=["Angle of the sun above the horizon at noon (degrees)",
             "Solar energy reaching one square meter of level ground (watts)"],
    rows=[["90", "1000"],
          ["60", "866"],
          ["45", "707"],
          ["30", "500"],
          ["10", "174"]])

_T_DAYLIGHT = dict(
    headers=["Site", "Hours of daylight on June 21", "Hours of daylight on December 21"],
    rows=[["Site at the equator", "12.1", "12.1"],
          ["Site at 30 degrees north", "13.9", "10.2"],
          ["Site at 50 degrees north", "16.4", "8.1"],
          ["Site at 66 degrees north", "24.0", "0.0"]])

_T_MONTH = dict(
    headers=["Month", "Hours of daylight",
             "Solar radiation received per unit area (watts per square meter)"],
    rows=[["March", "12.1", "182"],
          ["June", "15.4", "291"],
          ["September", "12.2", "176"],
          ["December", "8.7", "71"]])

_T_TWOSITE = dict(
    headers=["Site",
             "Solar radiation per unit area in June (watts per square meter)",
             "Solar radiation per unit area in December (watts per square meter)"],
    rows=[["Site A, 5 degrees north", "268", "246"],
          ["Site B, 48 degrees north", "241", "58"]])

_T_NOON = dict(
    headers=["Latitude",
             "Angle of the sun above the horizon at noon on the March equinox (degrees)"],
    rows=[["0 degrees", "90"],
          ["23 degrees north", "67"],
          ["45 degrees north", "45"],
          ["66 degrees north", "24"],
          ["90 degrees north", "0"]])

_T_HEMI = dict(
    headers=["Site", "Hours of daylight in June", "Hours of daylight in December"],
    rows=[["Site P, 40 degrees north", "15.0", "9.3"],
          ["Site Q, 40 degrees south", "9.3", "15.0"]])

QUESTIONS = [

 dict(q="A textbook states that incoming solar radiation, or insolation, is the Earth's "
        "main source of energy. Which of the following best expresses what that "
        "statement claims?",
      choices=[
        "Radiation arriving from the sun supplies more of the energy that drives Earth's "
        "surface and atmospheric processes than any other source does.",
        "Radiation arriving from the sun is the only form of energy that ever reaches the "
        "Earth's surface.",
        "Heat rising from the Earth's interior supplies most of the energy that reaches "
        "the surface, and sunlight supplies the remainder.",
        "The energy released by burning fossil fuels now exceeds the energy the Earth "
        "receives from the sun.",
        "Every location on Earth receives the same quantity of energy from the sun each "
        "year, which is why sunlight is called the main source."],
      ans=0,
      why="ENG-2.A.1 states that incoming solar radiation, insolation, is the Earth's main "
          "source of energy. Main source means largest source, not sole source, so the "
          "exclusive reading overstates it. The framework does not put the interior or "
          "combustion above sunlight, and ENG-2.A.1 also states that insolation depends on "
          "season and latitude, which rules out an equal share everywhere."),

 dict(q="According to the course framework, the amount of incoming solar radiation a "
        "place receives depends on which of the following?",
      choices=[
        "The season and the latitude of that place",
        "The longitude of that place and the local time zone",
        "The elevation of that place and the depth of the soil beneath it",
        "The size of the human population living at that place",
        "The average wind speed and the direction of prevailing winds at that place"],
      ans=0,
      why="ENG-2.A.1 states that insolation is dependent on season and latitude. Longitude "
          "sets clock time rather than the angle of the sun's rays, and none of elevation, "
          "population or wind is named by the framework as a control on how much radiation "
          "arrives."),

 dict(q="Two identical flat panels of the same area are laid on level ground at noon, one "
        "where the sun stands nearly overhead and one where the sun stands low above the "
        "horizon. What accounts for the difference in the energy each panel receives?",
      choices=[
        "The angle at which the sun's rays strike the surface determines the intensity of "
        "the radiation, so the panel under a higher sun receives more energy per unit area.",
        "The sun emits more radiation at the moment it stands overhead than it emits at "
        "any other moment of the day.",
        "The panel under the lower sun is farther from the sun by a distance large enough "
        "to reduce the energy it intercepts.",
        "Air is denser under a high sun, so more radiation is trapped near the ground "
        "before it reaches the panel.",
        "The two panels receive equal energy, and any measured difference must come from "
        "instrument error rather than from the sun."],
      ans=0,
      why="ENG-2.A.2 states that the angle of the sun's rays determines the intensity of the "
          "solar radiation. The sun's output does not change from hour to hour in the "
          "framework's account, the change in Earth-sun distance across a day is not offered "
          "as a cause, and a real and repeatable difference is not instrument error."),

 dict(q="The framework explains that because of the shape of the Earth, one latitude at a "
        "time is directly horizontal to the incoming solar radiation. What is true of "
        "that latitude?",
      choices=[
        "It receives the most intense solar radiation of any latitude at that time.",
        "It receives the least intense solar radiation, because the rays pass through more "
        "atmosphere to reach it.",
        "It receives exactly twelve hours of daylight on every day of the year.",
        "It lies at one of the two poles, since only the poles face the sun squarely.",
        "It is the only latitude receiving any solar radiation at all on that date."],
      ans=0,
      why="ENG-2.A.2 states that, due to the shape of the Earth, the latitude that is directly "
          "horizontal to the solar radiation receives the most intensity. The remaining "
          "options invert that claim, attach an unrelated day-length rule to it, place it at "
          "the poles, or extend it into a statement the framework never makes."),

 dict(q="The table gives the average solar radiation received per unit area over a year at "
        "five latitudes. Which conclusion is best supported by these values?",
      table=_T_LATITUDE,
      choices=[
        "Radiation received per unit area is greatest at the equator and falls steadily "
        "with distance from it.",
        "Radiation received per unit area is greatest at 40 degrees and falls off in both "
        "directions from there.",
        "Radiation received per unit area rises steadily as latitude increases.",
        "Radiation received per unit area is the same at every latitude once a full year "
        "is averaged.",
        "Radiation received per unit area is greatest at 80 degrees because the sun is "
        "above the horizon there for months at a time."],
      ans=0,
      why="ENG-2.A.3 states that the highest solar radiation per unit area is received at the "
          "equator and decreases toward the poles, and the tabulated values fall from 275 at "
          "0 degrees to 86 at 80 degrees without a single reversal. The other four readings "
          "each contradict the printed numbers."),

 dict(q="Using the same table of annual radiation per unit area, how much more radiation "
        "does a square meter at the equator receive than a square meter at 60 degrees?",
      table=_T_LATITUDE,
      choices=[
        "144 watts per square meter",
        "131 watts per square meter",
        "189 watts per square meter",
        "59 watts per square meter",
        "406 watts per square meter"],
      ans=0,
      why="Reading the two rows and subtracting gives 275 minus 131, which is 144 watts per "
          "square meter. The rejected values are the 60 degree figure itself, the difference "
          "taken against the wrong row, the 20 degree gap, and the sum of the two rows "
          "instead of their difference."),

 dict(q="A class measures the energy reaching one square meter of level ground at noon "
        "under five different sun angles and records the results in the table. What "
        "relationship do the data show?",
      table=_T_ANGLE,
      choices=[
        "Energy received per square meter increases as the sun stands higher above the "
        "horizon.",
        "Energy received per square meter increases as the sun sinks toward the horizon.",
        "Energy received per square meter is unrelated to how high the sun stands.",
        "Energy received per square meter is exactly proportional to the angle, so halving "
        "the angle halves the energy.",
        "Energy received per square meter reaches its largest value at an angle of about "
        "45 degrees."],
      ans=0,
      why="Sorted by angle the tabulated energies are 174, 500, 707, 866 and 1000 watts, "
          "rising without exception as the angle rises, which is the relationship ENG-2.A.2 "
          "asserts. Halving 60 degrees to 30 degrees takes 866 to 500 rather than to 433, so "
          "the strict proportion fails on the same numbers."),

 dict(q="The table lists the hours of daylight at four sites on June 21 and on December 21. "
        "Which site shows the largest change in day length between those two dates?",
      table=_T_DAYLIGHT,
      choices=[
        "The site at 66 degrees north",
        "The site at 50 degrees north",
        "The site at 30 degrees north",
        "The site at the equator",
        "All four sites show the same change, since each has a June and a December value"],
      ans=0,
      why="The June minus December differences are 0.0, 3.7, 8.3 and 24.0 hours, so the "
          "highest-latitude site changes most. ENG-2.A.5 attributes the number of hours of "
          "daylight at a location to the tilt of the Earth's axis of rotation."),

 dict(q="At a place in the Northern Hemisphere, on which day of the year does the framework "
        "say the location receives the most solar radiation?",
      choices=[
        "On its longest summer day",
        "On the day the Earth is nearest the sun in its orbit",
        "On the first cloudless day that follows the spring thaw",
        "On the day when the sun rises exactly due east",
        "On its shortest winter day, because the atmosphere is thinnest then"],
      ans=0,
      why="ENG-2.A.4 states that the solar radiation received at a location varies seasonally, "
          "with the most radiation received during the location's longest summer day and the "
          "least on the shortest winter day. The framework attributes the seasonal pattern to "
          "axial tilt in ENG-2.A.5, not to orbital distance, weather or sunrise direction."),

 dict(q="Which statement correctly identifies the least amount of solar radiation a "
        "particular location receives during a year?",
      choices=[
        "The least arrives on that location's shortest winter day.",
        "The least arrives on the two days each year when day and night are equal.",
        "The least arrives on whichever day has the coldest recorded air temperature.",
        "The least arrives on the day the location is farthest from the equator.",
        "The least arrives in the middle of the night on the longest summer day."],
      ans=0,
      why="ENG-2.A.4 pairs the maximum with the longest summer day and the minimum with the "
          "shortest winter day. A location's latitude does not change through the year, and "
          "the framework ties the amount received to season and latitude rather than to the "
          "day that happens to feel coldest."),

 dict(q="What does the course framework identify as the cause of the Earth's seasons and of "
        "the changing number of daylight hours at a given place?",
      choices=[
        "The tilt of the Earth's axis of rotation",
        "The changing distance between the Earth and the sun through the year",
        "The slow drift of the continents across the Earth's surface",
        "Changes in the total amount of energy the sun emits from year to year",
        "The rotation of the Earth once on its axis every twenty four hours"],
      ans=0,
      why="ENG-2.A.5 states that the tilt of Earth's axis of rotation causes the Earth's "
          "seasons and the number of hours of daylight in a particular location. Rotation "
          "produces day and night rather than the annual cycle, and the framework attributes "
          "the seasons to neither orbital distance nor continental drift nor solar output."),

 dict(q="A student argues that summer is warm because the Earth is closer to the sun in "
        "summer than in winter. How should the argument be corrected using the course "
        "framework?",
      choices=[
        "The framework attributes the seasons to the tilt of the Earth's axis, which changes "
        "the angle of the sun's rays and the hours of daylight at a location.",
        "The framework attributes the seasons to the Earth's rotation on its axis, which "
        "carries each place into and out of sunlight.",
        "The framework attributes the seasons to changes in the amount of energy the sun "
        "emits over the course of a year.",
        "The framework attributes the seasons to the thickness of the atmosphere, which "
        "grows in winter and shrinks in summer.",
        "The argument needs no correction, because the framework gives orbital distance as "
        "the cause of the seasons."],
      ans=0,
      why="ENG-2.A.5 names axial tilt as the cause of the seasons and of the hours of daylight, "
          "and ENG-2.A.2 ties intensity to the angle of the rays. Nothing in the framework "
          "makes distance, solar output, rotation or atmospheric thickness the seasonal cause."),

 dict(q="The table reports solar radiation per unit area in June and in December at two "
        "sites. What does the comparison show about how latitude relates to seasonal "
        "variation?",
      table=_T_TWOSITE,
      choices=[
        "The higher-latitude site varies far more between June and December than the "
        "near-equatorial site does.",
        "The near-equatorial site varies far more between June and December than the "
        "higher-latitude site does.",
        "Both sites vary by about the same amount between the two months.",
        "Neither site varies between the two months, so latitude has no seasonal effect.",
        "The higher-latitude site receives more radiation than the near-equatorial site in "
        "both months."],
      ans=0,
      why="Site A changes by 268 minus 246, which is 22 watts per square meter, while Site B "
          "changes by 241 minus 58, which is 183. ENG-2.A.4 states that radiation at a "
          "location varies seasonally and ENG-2.A.1 makes that variation depend on latitude "
          "as well as season."),

 dict(q="A weather station in the Northern Hemisphere recorded the values in the table. "
        "Which month's pair of values best illustrates the framework's statement about the "
        "longest summer day?",
      table=_T_MONTH,
      choices=[
        "June, with the most daylight hours and the most radiation per unit area",
        "December, with the fewest daylight hours and the most radiation per unit area",
        "March, with about twelve hours of daylight and the most radiation per unit area",
        "September, with the most daylight hours and the least radiation per unit area",
        "June, with the fewest daylight hours and the least radiation per unit area"],
      ans=0,
      why="In the table June carries both the largest daylight figure, 15.4 hours, and the "
          "largest radiation figure, 291 watts per square meter, which is the pairing "
          "ENG-2.A.4 describes when it puts the maximum radiation on the longest summer day. "
          "Each rejected option pairs a month with a value the table does not give it."),

 dict(q="Why does a square meter of ground near a pole receive less solar energy than a "
        "square meter near the equator, even on a clear day?",
      choices=[
        "Near the pole the sun's rays strike the curved surface at a lower angle, so the "
        "same beam is spread over more ground.",
        "Near the pole the ground is closer to the sun, so the rays arrive already weakened "
        "by the shorter path.",
        "Near the pole the sun emits a different kind of radiation that carries less energy.",
        "Near the pole the day is always shorter than twelve hours in every month of "
        "the year.",
        "Near the pole the Earth rotates more slowly, so each square meter turns away from "
        "the sun sooner."],
      ans=0,
      why="ENG-2.A.2 attributes intensity to the angle of the sun's rays and traces the "
          "difference between latitudes to the shape of the Earth, and ENG-2.A.3 states that "
          "radiation per unit area is highest at the equator and decreases toward the poles. "
          "The sun's emission does not vary by target, and polar day length exceeds twelve "
          "hours for part of the year."),

 dict(q="Suppose the Earth's axis of rotation had no tilt at all, while everything else "
        "about the planet stayed the same. Which outcome follows from the course framework?",
      choices=[
        "A given location would no longer see its daylight hours change through the year, "
        "and the seasonal cycle would not occur.",
        "A given location would still see the same seasons, because seasons are produced by "
        "the Earth's changing distance from the sun.",
        "Every location on Earth would receive exactly the same radiation per unit area, "
        "since latitude would stop mattering.",
        "Day and night would no longer alternate anywhere on the planet.",
        "The poles would begin to receive more radiation per unit area than the equator "
        "does."],
      ans=0,
      why="ENG-2.A.5 makes axial tilt the cause of the seasons and of the number of daylight "
          "hours at a location, so removing the tilt removes both. ENG-2.A.3 keeps the "
          "equator-to-pole gradient, which comes from the shape of the Earth, and rotation is "
          "what alternates day with night."),

 dict(q="A student says that latitude alone is enough to predict how much solar radiation a "
        "place receives. What is missing from that claim?",
      choices=[
        "The season, which the framework names alongside latitude as a control on insolation",
        "The longitude, which the framework names alongside latitude as a control on "
        "insolation",
        "The altitude of the site, which the framework names as the second control on "
        "insolation",
        "Nothing is missing, since the framework makes latitude the sole control on "
        "insolation",
        "The colour of the ground surface, which the framework names as the second control "
        "on insolation"],
      ans=0,
      why="ENG-2.A.1 states that insolation is dependent on season and latitude, so a "
          "prediction from latitude alone leaves out the seasonal half of that statement. "
          "Longitude, altitude and surface colour are not given by the framework as controls "
          "on how much radiation arrives."),

 dict(q="The table gives the noon angle of the sun above the horizon at five latitudes on "
        "the March equinox. Which statement is supported?",
      table=_T_NOON,
      choices=[
        "The sun stands directly overhead at the equator on that date and lower in the sky "
        "at every latitude farther north.",
        "The sun stands directly overhead at 45 degrees north on that date and lower in the "
        "sky in both directions from there.",
        "The noon angle is the same at every latitude on that date.",
        "The noon angle rises steadily as latitude increases toward the north pole.",
        "The sun does not rise at all at any of the five latitudes on that date."],
      ans=0,
      why="The tabulated angles fall from 90 degrees at 0 degrees to 0 degrees at 90 degrees "
          "north without a reversal, and 90 degrees means the rays arrive squarely. ENG-2.A.2 "
          "identifies the latitude lying directly horizontal to the radiation as the one "
          "receiving the greatest intensity."),

 dict(q="An engineer must site a large solar array and wants the greatest average radiation "
        "per unit area over a year. Which consideration follows most directly from the "
        "framework?",
      choices=[
        "Sites at lower latitudes receive more radiation per unit area over a year than "
        "sites nearer the poles.",
        "Sites at higher latitudes receive more radiation per unit area over a year because "
        "their summer days are longer.",
        "Radiation per unit area is the same everywhere over a full year, so latitude does "
        "not enter the decision.",
        "Radiation per unit area depends on the longitude of the site rather than on its "
        "latitude.",
        "Radiation per unit area is greatest wherever the annual air temperature range is "
        "widest."],
      ans=0,
      why="ENG-2.A.3 states that the highest solar radiation per unit area is received at the "
          "equator and decreases toward the poles, which is a statement about the annual "
          "figure. The long polar summer day is real but ENG-2.A.3 still puts the annual "
          "maximum at the equator, and neither longitude nor temperature range is offered as "
          "a control."),

 dict(q="Which measurement best captures what the framework means by the intensity of solar "
        "radiation at a place?",
      choices=[
        "The energy arriving on each square meter of surface",
        "The total energy arriving on the whole hemisphere facing the sun",
        "The number of hours between sunrise and sunset",
        "The highest air temperature recorded during the afternoon",
        "The number of days in the year on which the sky is clear"],
      ans=0,
      why="ENG-2.A.3 speaks of solar radiation per unit area, and ENG-2.A.2 makes that "
          "quantity depend on the angle of the rays. A hemisphere-wide total, a count of "
          "daylight hours, an air temperature and a count of clear days are each affected by "
          "other things besides the concentration of the beam."),

 dict(q="Using the table of hours of daylight on June 21 and December 21, what is true of "
        "the site at the equator?",
      table=_T_DAYLIGHT,
      choices=[
        "Its day length is essentially unchanged between the two dates, while the other "
        "three sites change.",
        "Its day length changes more between the two dates than that of any other site "
        "listed.",
        "It has no daylight at all on December 21, as the table shows for the "
        "highest-latitude site.",
        "It has the longest June day of the four sites listed.",
        "Its December day is longer than its June day by more than three hours."],
      ans=0,
      why="The equatorial row reads 12.1 hours on both dates, a change of 0.0, while the other "
          "three change by 3.7, 8.3 and 24.0 hours. ENG-2.A.5 attributes the changing number "
          "of daylight hours at a location to the tilt of the Earth's axis, and that change "
          "is smallest at the equator on these data."),

 dict(q="The same weather station table lists daylight hours and radiation for four months. "
        "By how much does radiation per unit area in June exceed radiation per unit area in "
        "December at this station?",
      table=_T_MONTH,
      choices=[
        "220 watts per square meter",
        "291 watts per square meter",
        "109 watts per square meter",
        "115 watts per square meter",
        "362 watts per square meter"],
      ans=0,
      why="Subtracting the two tabulated figures gives 291 minus 71, which is 220 watts per "
          "square meter. The rejected values are the June figure alone, the June to March "
          "gap, the March to December gap, and the sum of the two months rather than the "
          "difference."),

 dict(q="On June 21 a site at 66 degrees north has the sun above the horizon for the full "
        "twenty four hours, yet the radiation arriving on each square meter at noon is "
        "smaller there than at the equator. Which explanation fits the framework?",
      choices=[
        "The sun stands lower above the horizon there, and the angle of the rays sets the "
        "intensity of the radiation.",
        "The sun is above the horizon for so long that the ground reflects most of the "
        "radiation back into space.",
        "Radiation per unit area depends only on the number of daylight hours, so the two "
        "sites must actually be equal.",
        "The site is farther from the sun by enough distance to lower the intensity at "
        "noon.",
        "The framework states that intensity is greatest wherever the day is longest, so "
        "the observation must be a measurement error."],
      ans=0,
      why="ENG-2.A.2 states that the angle of the sun's rays determines the intensity, and "
          "ENG-2.A.3 puts the greatest radiation per unit area at the equator. Day length and "
          "intensity are separate quantities in the framework, so a long day does not by "
          "itself raise the energy on each square meter."),

 dict(q="Which pair of quantities does the tilt of the Earth's axis control, according to "
        "the framework?",
      choices=[
        "The seasons and the number of daylight hours at a location",
        "The length of the day and the length of the year",
        "The distance from the Earth to the sun and the speed of the Earth in its orbit",
        "The thickness of the atmosphere and the composition of the air",
        "The latitude of a location and the longitude of that same location"],
      ans=0,
      why="ENG-2.A.5 names exactly two consequences of axial tilt, the Earth's seasons and the "
          "number of hours of daylight in a particular location. The other pairs attach the "
          "tilt to quantities the framework never links to it."),

 dict(q="The table compares two sites at the same distance from the equator, one north and "
        "one south. What conclusion do the values support?",
      table=_T_HEMI,
      choices=[
        "The two sites reach their long days in opposite months of the year.",
        "The two sites reach their long days in the same month of the year.",
        "The northern site has more daylight than the southern site in both months listed.",
        "Neither site shows any change in daylight between the two months listed.",
        "The southern site has a longer June day than the northern site does."],
      ans=0,
      why="Site P reads 15.0 hours in June against 9.3 in December, while Site Q reads 9.3 in "
          "June against 15.0 in December, so each site's long month is the other's short "
          "month. ENG-2.A.5 attributes the number of daylight hours at a location to the tilt "
          "of the Earth's axis of rotation."),

 dict(q="A greenhouse operator wants the largest possible amount of natural light in "
        "midwinter and can build at any latitude. Which reasoning follows from the "
        "framework?",
      choices=[
        "Build nearer the equator, where the winter day is longer and the rays arrive at a "
        "higher angle than at high latitudes.",
        "Build nearer a pole, where the winter day is longer than the equatorial day.",
        "Build at a high latitude, because the framework puts the greatest radiation per "
        "unit area toward the poles.",
        "Latitude cannot help, because winter radiation is identical at every latitude.",
        "Build wherever the longitude places the site closest to the sun at noon in "
        "December."],
      ans=0,
      why="ENG-2.A.3 puts the greatest radiation per unit area at the equator, and the day "
          "length data behind ENG-2.A.5 show the equatorial day holding near twelve hours "
          "while the high-latitude winter day shortens. Longitude sets clock time rather than "
          "the angle of the rays."),

 dict(q="Which observation would most directly support the claim in ENG-2.A.2 that the angle "
        "of the sun's rays sets the intensity of solar radiation?",
      choices=[
        "Identical sensors on level ground record more energy per square meter as the sun "
        "climbs higher through the morning.",
        "Identical sensors record the same energy per square meter all day regardless of "
        "the sun's height.",
        "A sensor records more energy on a cloudy day than on a clear day at the same hour.",
        "A sensor records the same energy in December as in June at a high-latitude site.",
        "A sensor at the top of a mountain records less energy than one at sea level "
        "directly below it."],
      ans=0,
      why="The claim links a rising sun angle to a rising intensity, so the observation that "
          "tests it must vary the angle and watch the energy per unit area respond. The "
          "rejected observations either hold the energy constant while the angle changes or "
          "change something other than the angle."),

 dict(q="Two students describe why radiation per unit area falls from the equator toward "
        "the poles. The first says the Earth's curved shape means the rays meet high "
        "latitudes at a shallower angle. The second says the poles are simply farther from "
        "the sun. Which evaluation is correct?",
      choices=[
        "The first student is correct, because the framework traces the difference to the "
        "shape of the Earth and to the angle of the rays.",
        "The second student is correct, because the framework traces the difference to the "
        "distance between each latitude and the sun.",
        "Both students are correct, because the framework gives shape and distance as two "
        "equally weighted causes.",
        "Neither student is correct, because the framework denies that radiation per unit "
        "area varies with latitude at all.",
        "The second student is correct, because the framework puts the greatest radiation "
        "per unit area at the poles."],
      ans=0,
      why="ENG-2.A.2 attributes the pattern to the shape of the Earth and to the angle at "
          "which the rays arrive, and ENG-2.A.3 records the resulting decrease from the "
          "equator toward the poles. The framework nowhere makes the pole-to-sun distance a "
          "cause."),

 dict(q="Which of the following is the best summary of how season and latitude work together "
        "to set the solar radiation a place receives?",
      choices=[
        "Latitude fixes how directly the rays can ever arrive, and season shifts the arriving "
        "angle and the daylight hours across the year.",
        "Latitude fixes the total radiation for the year, and season merely redistributes "
        "cloud cover without changing the arriving energy.",
        "Season fixes the total radiation for the year, and latitude only changes the local "
        "clock time of sunrise.",
        "Latitude and season act on different planets' orbits and have no combined effect on "
        "any one location.",
        "Neither latitude nor season changes the radiation received, which is set by the "
        "energy the sun emits alone."],
      ans=0,
      why="ENG-2.A.1 makes insolation depend on both season and latitude, ENG-2.A.2 ties "
          "intensity to the arriving angle, and ENG-2.A.5 ties the seasonal change in that "
          "angle and in daylight hours to the tilt of the axis. The other summaries drop one "
          "of the two named controls or replace it with something the framework does not name."),

 dict(q="Over the course of one year, which single change would most increase the solar "
        "radiation received per unit area at a research station, according to the framework?",
      choices=[
        "Relocating the station to a latitude much closer to the equator",
        "Relocating the station to a latitude much closer to the pole",
        "Moving the station a few hundred kilometers east along the same latitude",
        "Repainting the station's roof a darker colour",
        "Rescheduling the station's measurements to the middle of the night"],
      ans=0,
      why="ENG-2.A.3 states that radiation per unit area is greatest at the equator and "
          "decreases toward the poles, so moving toward the equator raises the annual figure "
          "and moving toward the pole lowers it. Moving along a latitude changes longitude "
          "only, and roof colour and measurement schedule are not controls on how much "
          "radiation arrives."),
]
