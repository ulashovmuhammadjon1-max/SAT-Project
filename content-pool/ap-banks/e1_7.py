# AP ENVIRONMENTAL SCIENCE 1.7 The Hydrologic (Water) Cycle
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.G: explain the steps and reservoir interactions in the
# hydrologic cycle. Suggested skill 2.B.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.G.1  The hydrologic cycle, which is powered by the sun, is the movement of
#              water in its various solid, liquid, and gaseous phases between sources
#              and sinks.
#   ERT-1.G.2  The oceans are the primary reservoir of water at the Earth's surface, with
#              ice caps and groundwater acting as much smaller reservoirs.
#
# THIS IS THE THINNEST TOPIC IN THE UNIT -- two statements for thirty items -- so the
# angles are deliberately spread across everything the two statements contain and NOTHING
# else. The framework does not name evaporation, condensation, precipitation, runoff,
# infiltration or transpiration in this topic, so no item asks a student to recall those
# terms as course content. Where an item turns on a phase change, the content presupposed
# is only what naming three phases requires: ice is the solid phase, liquid water the
# liquid phase, and water vapor the gaseous phase. Each such item is flagged in the
# verifier's claim.
#
# HOW THIS TOPIC IS KEPT DISTINCT FROM 1.4, 1.5 AND 1.6. The other three cycle topics
# never mention phases or the sun; this one never mentions residence times (a carbon
# statement), fixation or nitrogen's atmospheric reservoir (nitrogen statements), or the
# absence of an atmospheric component (a phosphorus statement). The bare sources-and-sinks
# definition is asked once in the bank, in 1.4; here the definition items turn on the
# phrase "powered by the sun" and on the three phases.
#
# NO FIGURES ARE REFERENCED. Reservoir volumes and fluxes are given as tables.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.7", "The Hydrologic (Water) Cycle", 1)

_T_WRESERVOIR = dict(
    headers=["Water reservoir", "Water held (thousands of cubic kilometers)"],
    rows=[["Oceans", "1338000"],
          ["Ice caps and glaciers", "24100"],
          ["Groundwater", "23400"],
          ["Lakes and rivers", "180"],
          ["Atmosphere", "13"]])

_T_SOLAR = dict(
    headers=["Evaporation pan site", "Sunlight received each day (megajoules per square meter)",
             "Water evaporated each day (millimeters)"],
    rows=[["Site 1", "4", "1.1"],
          ["Site 2", "9", "2.6"],
          ["Site 3", "17", "5.2"],
          ["Site 4", "26", "8.1"]])

_T_DAYNIGHT = dict(
    headers=["Period of the day", "Water evaporated from an open tank (millimeters)"],
    rows=[["Sunrise to midday", "2.9"],
          ["Midday to sunset", "3.4"],
          ["Sunset to midnight", "0.6"],
          ["Midnight to sunrise", "0.3"]])

_T_SNOW = dict(
    headers=["Month in a mountain basin", "Water held as snow on the ground (millimeters)",
             "Water leaving the basin in the stream (millimeters)"],
    rows=[["February", "410", "12"],
          ["April", "330", "58"],
          ["June", "40", "216"],
          ["August", "0", "44"]])

_T_VAPOR = dict(
    headers=["Air temperature (degrees Celsius)",
             "Greatest mass of water vapor the air can hold (grams per cubic meter)"],
    rows=[["0", "4.8"],
          ["10", "9.4"],
          ["20", "17.3"],
          ["30", "30.4"]])

_T_SALT = dict(
    headers=["Category of the Earth's water", "Share of all the water on Earth (percent)"],
    rows=[["Salt water in the oceans", "96.5"],
          ["Fresh water frozen in ice caps and glaciers", "1.74"],
          ["Fresh groundwater", "0.76"],
          ["Fresh water in lakes and rivers", "0.013"]])

_T_BASIN = dict(
    headers=["Year in one basin", "Rain and snow falling on the basin (millimeters)",
             "Water leaving as vapor (millimeters)", "Water leaving in the river (millimeters)"],
    rows=[["Year 1", "900", "540", "355"],
          ["Year 2", "1200", "610", "580"],
          ["Year 3", "640", "470", "175"]])

_T_ICE = dict(
    headers=["Survey decade", "Water stored in one region's ice caps (cubic kilometers)",
             "Mean summer air temperature (degrees Celsius)"],
    rows=[["First decade", "94000", "1.2"],
          ["Third decade", "91500", "1.9"],
          ["Fifth decade", "87200", "2.6"],
          ["Seventh decade", "81400", "3.5"]])

QUESTIONS = [

 dict(q="What does the framework identify as the source of energy that powers the "
        "hydrologic cycle?",
      choices=[
        "The sun.",
        "Heat rising from the Earth's interior.",
        "The gravitational pull of the moon.",
        "Chemical energy released by soil bacteria.",
        "Energy stored in ocean sediments."],
      ans=0,
      why="ERT-1.G.1 states that the hydrologic cycle is powered by the sun. The "
          "framework assigns the cycle no other energy source."),

 dict(q="In which phases does the framework say water moves through the hydrologic cycle?",
      choices=[
        "Solid, liquid and gaseous.",
        "Liquid alone.",
        "Liquid and gaseous, but not solid.",
        "Solid and liquid, but not gaseous.",
        "Gaseous alone."],
      ans=0,
      why="ERT-1.G.1 describes the hydrologic cycle as the movement of water in its "
          "various solid, liquid, and gaseous phases between sources and sinks, so all "
          "three are part of the cycle."),

 dict(q="Which does the framework identify as the primary reservoir of water at the "
        "Earth's surface?",
      choices=[
        "The oceans.",
        "The ice caps.",
        "Groundwater.",
        "The atmosphere.",
        "Lakes and rivers."],
      ans=0,
      why="ERT-1.G.2 states that the oceans are the primary reservoir of water at the "
          "Earth's surface, with ice caps and groundwater acting as much smaller "
          "reservoirs."),

 dict(q="How does the framework describe ice caps and groundwater in relation to the "
        "oceans?",
      choices=[
        "As much smaller reservoirs than the oceans.",
        "As reservoirs of about the same size as the oceans.",
        "As reservoirs larger than the oceans.",
        "As reservoirs that hold no water at all.",
        "As the primary reservoir of water at the Earth's surface."],
      ans=0,
      why="ERT-1.G.2 names ice caps and groundwater as acting as much smaller reservoirs "
          "than the oceans, which it calls the primary reservoir of water at the Earth's "
          "surface."),

 dict(q="The table gives the water held in five reservoirs. Which conclusion is best "
        "supported?",
      table=_T_WRESERVOIR,
      choices=[
        "The oceans hold far more water than the other four reservoirs combined.",
        "Ice caps and glaciers hold more water than the oceans do.",
        "Groundwater holds more water than the oceans do.",
        "The five reservoirs hold roughly equal amounts of water.",
        "The atmosphere holds more water than lakes and rivers do."],
      ans=0,
      why="The oceanic figure exceeds the sum of the other four by more than an order of "
          "magnitude, which is the quantitative form of ERT-1.G.2's claim that the oceans "
          "are the primary reservoir of water at the Earth's surface."),

 dict(q="Using the same table of five reservoirs, which comparison between ice caps, "
        "groundwater and the oceans is best supported?",
      table=_T_WRESERVOIR,
      choices=[
        "Ice caps and groundwater are each far smaller than the oceans but far larger "
        "than lakes and rivers.",
        "Ice caps and groundwater are each far larger than the oceans.",
        "Ice caps and groundwater are each smaller than lakes and rivers.",
        "Ice caps and groundwater together hold more than the oceans.",
        "Ice caps hold more water than the oceans, while groundwater holds less."],
      ans=0,
      why="Both intermediate reservoirs sit two orders of magnitude below the oceans and "
          "two orders above lakes and rivers, which is what ERT-1.G.2 describes when it "
          "calls them much smaller reservoirs than the primary one."),

 dict(q="Four evaporation pans were compared, as shown. Which relationship do the data "
        "support?",
      table=_T_SOLAR,
      choices=[
        "Sites receiving more sunlight evaporated more water each day.",
        "Sites receiving more sunlight evaporated less water each day.",
        "The daily evaporation was the same at all four sites.",
        "The site receiving the least sunlight evaporated the most water.",
        "All four sites received the same amount of sunlight."],
      ans=0,
      why="Sorting the sites by sunlight received leaves the daily evaporation strictly "
          "increasing. ERT-1.G.1 states that the hydrologic cycle is powered by the sun, "
          "and moving water from a liquid store into the air is part of that cycle."),

 dict(q="Water lost from an open tank was measured in four parts of one day, as shown. "
        "Which conclusion is best supported?",
      table=_T_DAYNIGHT,
      choices=[
        "Far more water left the tank during the daylight periods than during the dark "
        "periods.",
        "Far more water left the tank during the dark periods than during the daylight "
        "periods.",
        "The same amount of water left the tank in each of the four periods.",
        "No water left the tank during any daylight period.",
        "The period from midnight to sunrise lost the most water of the four."],
      ans=0,
      why="The two daylight figures are each several times larger than either dark "
          "figure. ERT-1.G.1 states that the hydrologic cycle is powered by the sun, and "
          "a daylight-dark difference of this size is what a sun-driven process shows."),

 dict(q="Snow on the ground and stream flow were measured through one year in a mountain "
        "basin, as shown. Which conclusion is best supported?",
      table=_T_SNOW,
      choices=[
        "Water stored on the ground in the solid phase later left the basin in the liquid "
        "phase.",
        "Water stored on the ground in the liquid phase later left the basin in the solid "
        "phase.",
        "The snow on the ground and the stream flow both rose through the year.",
        "The stream carried the most water in the month with the most snow on the ground.",
        "No water left the basin in the stream at any time of the year."],
      ans=0,
      why="Snow on the ground falls to nothing across the record while stream flow peaks "
          "as it does so. ERT-1.G.1 describes the cycle as the movement of water in its "
          "solid, liquid and gaseous phases, and snow is the solid phase while stream "
          "water is the liquid phase."),

 dict(q="The greatest mass of water vapor that air can hold was measured at four "
        "temperatures, as shown. Which conclusion is best supported?",
      table=_T_VAPOR,
      choices=[
        "Warmer air can hold more water in the gaseous phase than cooler air can.",
        "Warmer air can hold less water in the gaseous phase than cooler air can.",
        "Air at every temperature holds the same mass of water vapor.",
        "Air at zero degrees can hold the largest mass of water vapor of the four.",
        "The mass of water vapor the air can hold falls as the temperature rises."],
      ans=0,
      why="The tabulated capacity rises at every step up the temperature column. "
          "ERT-1.G.1 places the gaseous phase within the hydrologic cycle, and the table "
          "shows how much of that phase warm and cool air can carry."),

 dict(q="Which of the following is water in its solid phase as it occurs in the "
        "hydrologic cycle?",
      choices=[
        "An ice cap.",
        "A river.",
        "Water vapor in the air.",
        "Groundwater in a rock layer.",
        "The surface of the ocean."],
      ans=0,
      why="ERT-1.G.1 states that water moves through the cycle in solid, liquid and "
          "gaseous phases, and ERT-1.G.2 names ice caps as one of the reservoirs. Ice is "
          "the solid phase; every rejected option is liquid or gaseous."),

 dict(q="Which of the following is water in its gaseous phase as it occurs in the "
        "hydrologic cycle?",
      choices=[
        "Water vapor in the atmosphere.",
        "A glacier on a mountainside.",
        "Water stored in the pores of a rock layer.",
        "A freshwater lake.",
        "Sea ice floating on the ocean."],
      ans=0,
      why="ERT-1.G.1 states that water moves through the cycle in solid, liquid and "
          "gaseous phases. Water vapor is the gaseous phase; the rejected options are ice "
          "in the solid phase or liquid water in a reservoir."),

 dict(q="A student says the hydrologic cycle is driven by heat escaping from the Earth's "
        "interior. What is the best correction?",
      choices=[
        "The framework states that the cycle is powered by the sun.",
        "The framework states that the cycle requires no energy source at all.",
        "The framework states that the cycle is powered by the tides.",
        "The framework states that the cycle is powered by chemical reactions in "
        "sediments.",
        "The student is correct, because water is warmed only from below."],
      ans=0,
      why="ERT-1.G.1 names the sun as what powers the hydrologic cycle, and the framework "
          "offers no alternative energy source for it."),

 dict(q="If the amount of solar energy reaching a region fell substantially over many "
        "years, which change does the framework most directly support predicting?",
      choices=[
        "Less water would be moved through the region's hydrologic cycle, because the "
        "cycle is powered by the sun.",
        "More water would be moved through the region's hydrologic cycle, because less "
        "would be lost to sunlight.",
        "The region's water would stop changing phase but would keep moving.",
        "The oceans would cease to be the primary reservoir of water.",
        "Groundwater would become larger than the ocean reservoir."],
      ans=0,
      why="ERT-1.G.1 states that the hydrologic cycle is powered by the sun, so reducing "
          "the energy supplied reduces the work the cycle can do in moving water between "
          "sources and sinks."),

 dict(q="Water evaporating from the ocean surface and later falling as snow onto an ice "
        "cap has moved between which two reservoirs named by the framework?",
      choices=[
        "From the oceans to the ice caps.",
        "From the ice caps to the oceans.",
        "From groundwater to the oceans.",
        "From the ice caps to groundwater.",
        "From groundwater to the ice caps."],
      ans=0,
      why="ERT-1.G.2 names the oceans, ice caps and groundwater as reservoirs, and "
          "ERT-1.G.1 makes the cycle a movement between sources and sinks. The sequence "
          "described starts at the ocean surface and ends on an ice cap."),

 dict(q="Which sequence of phases does water pass through when ocean water becomes vapor, "
        "then falls as snow?",
      choices=[
        "Liquid, then gaseous, then solid.",
        "Solid, then liquid, then gaseous.",
        "Gaseous, then solid, then liquid.",
        "Liquid, then solid, then gaseous.",
        "Gaseous, then liquid, then solid."],
      ans=0,
      why="ERT-1.G.1 names solid, liquid and gaseous as the phases in which water moves "
          "through the cycle. Ocean water is liquid, vapor is gaseous and snow is solid, "
          "so the sequence follows the order in which the stem states the events."),

 dict(q="The shares of the Earth's water held in four categories are shown. Which "
        "conclusion is best supported?",
      table=_T_SALT,
      choices=[
        "The salt water of the oceans makes up the great majority of the Earth's water, "
        "with each freshwater category far smaller.",
        "Fresh water in lakes and rivers makes up the great majority of the Earth's "
        "water.",
        "Frozen fresh water makes up more of the Earth's water than the oceans do.",
        "The four categories hold roughly equal shares of the Earth's water.",
        "Fresh groundwater makes up more of the Earth's water than the oceans do."],
      ans=0,
      why="The oceanic share exceeds ninety percent while every other tabulated share is "
          "below two percent. ERT-1.G.2 makes the oceans the primary reservoir of water "
          "at the Earth's surface and the others much smaller reservoirs."),

 dict(q="A water balance was measured for one basin over three years, as shown. Which "
        "statement is best supported?",
      table=_T_BASIN,
      choices=[
        "The basin lost water both as vapor and in its river in every year recorded.",
        "The basin lost water only as vapor and never in its river.",
        "The basin lost water only in its river and never as vapor.",
        "The basin lost more water in its river than as vapor in every year recorded.",
        "The basin received no water at all in the driest year recorded."],
      ans=0,
      why="Both loss columns are positive in all three years. ERT-1.G.1 makes the cycle a "
          "movement of water in its various phases between sources and sinks, and a basin "
          "losing water both as vapor and as liquid is losing it in two phases at once."),

 dict(q="Ice storage and summer temperature were recorded in one region over several "
        "decades, as shown. Which conclusion is best supported?",
      table=_T_ICE,
      choices=[
        "The ice reservoir shrank as summer temperature rose, so water left the solid "
        "phase over the period.",
        "The ice reservoir grew as summer temperature rose.",
        "The ice reservoir was unchanged over the period recorded.",
        "Summer temperature fell over the period recorded.",
        "The ice reservoir shrank while summer temperature stayed constant."],
      ans=0,
      why="The stored ice falls and the summer temperature rises across the four surveys. "
          "ERT-1.G.2 names ice caps as a reservoir, and ERT-1.G.1 makes movement between "
          "phases part of the cycle, so a shrinking ice store is water leaving the solid "
          "phase."),

 dict(q="Which statement best explains why the hydrologic cycle is described as a cycle "
        "rather than as a one-way flow?",
      choices=[
        "Water moves between sources and sinks and can return to a reservoir it has "
        "already left.",
        "Water is created at its source and destroyed at its sink.",
        "Water travels in one direction only, from the oceans to the atmosphere.",
        "Water changes into another substance each time it moves.",
        "Water remains permanently in the first reservoir it enters."],
      ans=0,
      why="ERT-1.G.1 defines the hydrologic cycle as the movement of water between "
          "sources and sinks, which permits the same water to return rather than being "
          "consumed at either end."),

 dict(q="A student claims that essentially all the Earth's fresh water is held in lakes "
        "and rivers. Which part of the framework contradicts this?",
      choices=[
        "The statement that ice caps and groundwater act as reservoirs of water.",
        "The statement that the hydrologic cycle is powered by the sun.",
        "The statement that water moves in solid, liquid and gaseous phases.",
        "The statement that the oceans are the primary reservoir of water.",
        "The statement that the cycle moves water between sources and sinks."],
      ans=0,
      why="ERT-1.G.2 names ice caps and groundwater as reservoirs of water in their own "
          "right, so lakes and rivers cannot hold essentially all the fresh water even "
          "though those two are much smaller than the oceans."),

 dict(q="Which observation would best support the claim that solar energy drives "
        "evaporation at a given site?",
      choices=[
        "Water is lost from an open surface far faster on bright days than on overcast "
        "days of the same air temperature.",
        "Water is lost from an open surface at the same rate on bright and overcast days.",
        "The site is closer to the ocean than another site is.",
        "The water at the site contains dissolved salt.",
        "The site is at a lower elevation than another site."],
      ans=0,
      why="ERT-1.G.1 states that the hydrologic cycle is powered by the sun, and the way "
          "to test that at one site is to vary the sunlight while holding other "
          "conditions similar and watch what the water does."),

 dict(q="Which of the following best describes the movement of water the framework calls "
        "the hydrologic cycle?",
      choices=[
        "Water in solid, liquid and gaseous phases moving between sources and sinks, "
        "powered by the sun.",
        "Water moving only within the bodies of living organisms.",
        "Water moving in one phase only, between two reservoirs.",
        "Water being created in the atmosphere and destroyed in the oceans.",
        "Water moving without any input of energy from outside the Earth."],
      ans=0,
      why="ERT-1.G.1 contains all three elements in one sentence: the cycle is powered by "
          "the sun, it involves the various solid, liquid and gaseous phases, and it is a "
          "movement between sources and sinks."),

 dict(q="Two regions receive the same rainfall, but one is much sunnier and warmer. Which "
        "prediction does the framework most directly support?",
      choices=[
        "The sunnier region will return more of that water to the air, because the cycle "
        "is powered by the sun.",
        "The sunnier region will return less of that water to the air.",
        "The two regions must return identical amounts of water to the air, because "
        "rainfall is equal.",
        "Neither region will return any water to the air, because rainfall arrives as a "
        "liquid.",
        "The sunnier region will convert its water into another substance."],
      ans=0,
      why="ERT-1.G.1 states that the hydrologic cycle is powered by the sun, so the "
          "region receiving more solar energy has more of the energy the cycle uses to "
          "move water from a liquid store into the gaseous phase."),

 dict(q="Groundwater is described by the framework as which of the following?",
      choices=[
        "A reservoir of the hydrologic cycle that is much smaller than the oceans.",
        "The primary reservoir of water at the Earth's surface.",
        "A reservoir larger than the oceans but smaller than the ice caps.",
        "A phase of water rather than a reservoir.",
        "The energy source that powers the hydrologic cycle."],
      ans=0,
      why="ERT-1.G.2 names groundwater, alongside ice caps, as acting as a much smaller "
          "reservoir than the oceans, which it calls the primary reservoir of water at "
          "the Earth's surface."),

 dict(q="Which pair of framework claims about water is stated together in a single "
        "essential knowledge statement?",
      choices=[
        "That the oceans are the primary surface reservoir and that ice caps and "
        "groundwater are much smaller reservoirs.",
        "That the cycle is powered by the sun and that the oceans are the primary "
        "reservoir.",
        "That water moves in three phases and that ice caps are much smaller reservoirs.",
        "That groundwater is a reservoir and that the cycle is powered by the sun.",
        "That water moves between sources and sinks and that lakes are the primary "
        "reservoir."],
      ans=0,
      why="ERT-1.G.2 contains exactly those two claims in one sentence: the oceans are "
          "the primary reservoir of water at the Earth's surface, with ice caps and "
          "groundwater acting as much smaller reservoirs."),

 dict(q="A large ice cap melts entirely over a long period. Where does the framework most "
        "directly support saying that water goes?",
      choices=[
        "Into other reservoirs of the cycle, since the cycle moves water between sources "
        "and sinks rather than destroying it.",
        "Out of existence, since melting converts water into another substance.",
        "Into the sun, which powers the cycle.",
        "Into the solid phase in a different form.",
        "Nowhere, since a reservoir that empties leaves the cycle."],
      ans=0,
      why="ERT-1.G.1 defines the hydrologic cycle as the movement of water between "
          "sources and sinks, so water leaving one reservoir arrives at another rather "
          "than ceasing to exist."),

 dict(q="Which statement about the three phases of water in the cycle is best supported "
        "by the framework?",
      choices=[
        "All three phases take part in the cycle, and water can move between them.",
        "Only the liquid phase takes part in the cycle.",
        "Water in the solid phase leaves the cycle permanently.",
        "Water in the gaseous phase is not part of the hydrologic cycle.",
        "Water can occupy only one phase at any place on Earth."],
      ans=0,
      why="ERT-1.G.1 describes the hydrologic cycle as the movement of water in its "
          "various solid, liquid and gaseous phases between sources and sinks, so all "
          "three are inside the cycle and the movement is among them."),

 dict(q="Why does an increase in the ocean reservoir accompany a long-term loss from the "
        "ice caps, according to the framework's description of the cycle?",
      choices=[
        "Because the water is moved between reservoirs rather than lost, and the oceans "
        "are the primary reservoir at the surface.",
        "Because melting creates new water that did not exist before.",
        "Because the ice caps are larger than the oceans, so any loss must go somewhere "
        "smaller.",
        "Because the sun removes water from the ice caps and stores it.",
        "Because groundwater is the primary reservoir at the surface."],
      ans=0,
      why="ERT-1.G.1 makes the cycle a movement of water between sources and sinks, and "
          "ERT-1.G.2 makes the oceans the primary reservoir of water at the Earth's "
          "surface, so a transfer out of a much smaller reservoir lands in the large one."),

 dict(q="Which of the following would NOT be consistent with the framework's account of "
        "the hydrologic cycle?",
      choices=[
        "Water molecules being permanently consumed at the end of the cycle.",
        "Water moving from the ocean surface into the atmosphere.",
        "Water being stored for a long time in an ice cap.",
        "Water being stored underground as groundwater.",
        "Solar energy driving the movement of water between reservoirs."],
      ans=0,
      why="ERT-1.G.1 describes movement between sources and sinks, which no more consumes "
          "water than it creates it, while ERT-1.G.1 and ERT-1.G.2 between them supply "
          "the solar energy, the atmospheric movement, the ice cap and the groundwater "
          "that the rejected options describe."),
]
