# AP ENVIRONMENTAL SCIENCE 7.3 Thermal Inversion
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objective STB-2.C: describe thermal inversion and its relationship with
# pollution. Suggested skill 2.C, explain how environmental concepts and processes
# represented visually relate to broader environmental issues.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.C.1  During a thermal inversion, the normal temperature gradient in the
#              atmosphere is altered as the air temperature at the Earth's surface is
#              cooler than the air at higher altitudes.
#   STB-2.C.2  Thermal inversion traps pollution close to the ground, especially smog
#              and particulates.
#
# WHAT IS AND IS NOT KEYED. Two statements carry this topic, so every item here is one
# of three things: reading a temperature profile against the definition in STB-2.C.1,
# reasoning about the trapping in STB-2.C.2, or both together. Two consequences follow
# from STB-2.C.1 by simple logic and are used as such: if an inversion is the ALTERED
# case in which the surface is cooler than the air above, then the normal case is the
# surface warmer than the air above, and an inversion ends when that normal ordering
# returns.
#
# The framework gives NO cause for a thermal inversion -- no valley, no clear calm
# night, no cold air drainage, no season -- so no item here keys one, and no stem
# supplies a cause as if it were course content. It also gives no threshold
# concentration, no duration and no named episode. An illustrative example is not
# assessable.
#
# ON THE PROFILES. The bank carries no images, so every temperature profile is a
# table of altitude against temperature and every keyed reading is recomputed in
# verify_e7_3.py from that table alone. No stem refers to a figure.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII: export_units.py does not typeset
# ENV_SCI.
TOPIC = ("7.3", "Thermal Inversion", 7)

_T_INVERTED = dict(
    headers=["Height above the ground (meters)", "Air temperature (degrees Celsius)"],
    rows=[["0", "4"],
          ["100", "7"],
          ["200", "10"],
          ["300", "12"],
          ["600", "9"],
          ["1,000", "5"]])

_T_NORMAL = dict(
    headers=["Height above the ground (meters)", "Air temperature (degrees Celsius)"],
    rows=[["0", "22"],
          ["200", "20"],
          ["400", "18"],
          ["700", "15"],
          ["1,000", "12"]])

_T_TWO_CITIES = dict(
    headers=["City", "Temperature at ground level (degrees Celsius)",
             "Temperature at 400 meters (degrees Celsius)"],
    rows=[["City J", "3", "9"],
          ["City K", "17", "14"]])

_T_HOURS = dict(
    headers=["Hour", "Temperature at ground level (degrees Celsius)",
             "Temperature at 300 meters (degrees Celsius)",
             "Particulate matter at ground level (micrograms per cubic meter)"],
    rows=[["6 in the morning", "2", "8", "85"],
          ["9 in the morning", "6", "9", "70"],
          ["Noon", "14", "11", "30"],
          ["3 in the afternoon", "17", "13", "22"]])

_T_EPISODE = dict(
    headers=["Day of the week", "Inversion present at dawn",
             "Smog measured at ground level (parts per billion)",
             "Particulates measured at ground level (micrograms per cubic meter)"],
    rows=[["Monday", "yes", "95", "78"],
          ["Tuesday", "yes", "110", "90"],
          ["Wednesday", "no", "45", "30"],
          ["Thursday", "no", "40", "26"]])

_T_LAYERS = dict(
    headers=["Height above the ground (meters)", "Air temperature (degrees Celsius)",
             "Sulfur dioxide (parts per billion)"],
    rows=[["0", "5", "60"],
          ["150", "8", "55"],
          ["250", "11", "48"],
          ["350", "12", "6"],
          ["500", "10", "4"]])

_T_VALLEYS = dict(
    headers=["Site", "Temperature at ground level (degrees Celsius)",
             "Temperature at 200 meters (degrees Celsius)",
             "Particulates at ground level (micrograms per cubic meter)"],
    rows=[["Site 1", "1", "7", "92"],
          ["Site 2", "4", "8", "74"],
          ["Site 3", "11", "9", "35"],
          ["Site 4", "15", "12", "28"]])

QUESTIONS = [

 dict(q="Which statement describes the temperature arrangement during a thermal "
        "inversion?",
      choices=[
        "The air at the Earth's surface is cooler than the air at higher altitudes",
        "The air at the Earth's surface is warmer than the air at higher altitudes",
        "The air is the same temperature from the ground up to the stratosphere",
        "The air temperature falls steadily with height, as it usually does",
        "The air temperature depends only on the time of year and not on height"],
      ans=0,
      why="A thermal inversion is defined as the case in which the normal temperature "
          "gradient is altered so that surface air is cooler than the air above it. The "
          "rejected options describe the ordinary arrangement, a uniform column, or no "
          "relationship with height at all."),

 dict(q="A weather balloon returns the profile below. Which conclusion does it support?",
      table=_T_INVERTED,
      choices=[
        "A thermal inversion is present, because temperature rises with height through "
        "the lowest few hundred meters",
        "The profile is the ordinary one, because temperature falls with height "
        "throughout",
        "The profile shows no change of temperature with height",
        "A thermal inversion is present, because the air is coldest at the greatest "
        "height measured",
        "The profile cannot be interpreted without knowing the season"],
      ans=0,
      why="Reading up from the ground, the temperature increases through the lowest "
          "layers before falling again higher up, which places the cooler air at the "
          "surface and the warmer air above it. That is the altered gradient the "
          "framework calls a thermal inversion."),

 dict(q="A second balloon, released elsewhere on the same day, returns this profile.",
      table=_T_NORMAL,
      choices=[
        "No inversion is present, because the surface air is warmer than the air above it",
        "An inversion is present, because temperature changes with height",
        "An inversion is present, because the surface air is the coolest in the column",
        "The profile shows an inversion above 700 meters",
        "The profile shows that temperature is unrelated to height"],
      ans=0,
      why="Temperature falls at every step upward in this column, so the surface air is "
          "the warmest and the ordering is the ordinary one rather than the altered "
          "gradient. Any change with height is not by itself an inversion."),

 dict(q="Which pollutants does the framework single out as being trapped close to the "
        "ground by a thermal inversion?",
      choices=[
        "Smog and particulates",
        "Stratospheric ozone and chlorofluorocarbons",
        "Radon and asbestos fibers released indoors",
        "Nitrogen gas and argon",
        "Noise from transportation and construction"],
      ans=0,
      why="The framework states that thermal inversion traps pollution close to the "
          "ground, especially smog and particulates. Stratospheric chemicals, indoor "
          "pollutants, the inert constituents of air, and noise are not what it names "
          "here."),

 dict(q="Temperature and particulate measurements through one morning are shown.",
      table=_T_HOURS,
      choices=[
        "Particulates are highest in the hours when the ground is cooler than the air "
        "at 300 meters and fall once that ordering reverses",
        "Particulates are highest in the hours when the ground is warmer than the air "
        "above it",
        "Particulates stay the same throughout the morning",
        "Particulates rise steadily through the whole period",
        "The temperature measurements are unrelated to the particulate measurements in "
        "these data"],
      ans=0,
      why="In the first two hours the ground reading is below the reading at 300 meters "
          "and the particulate values are the two highest of the morning; once the "
          "ground becomes the warmer of the two the values drop. That is the trapping "
          "the framework attaches to an inversion."),

 dict(q="Why does a thermal inversion make air quality worse near the ground even "
        "though it does not create any new pollution?",
      choices=[
        "It traps the pollution already being released close to the ground instead of "
        "letting it disperse upward",
        "It converts nitrogen in the air into additional pollutants",
        "It increases the amount of fuel that vehicles burn",
        "It draws pollution downward out of the stratosphere",
        "It makes existing pollutants more toxic without changing their concentration"],
      ans=0,
      why="The framework's statement is about where the pollution goes: an inversion "
          "traps it close to the ground. The concentration people breathe rises because "
          "the same releases are confined to a shallower layer, not because new "
          "pollutants are made or existing ones altered."),

 dict(q="Air quality is measured at four heights during one episode.",
      table=_T_LAYERS,
      choices=[
        "Sulfur dioxide is far higher below 350 meters, where the temperature is still "
        "rising with height, than above it",
        "Sulfur dioxide is highest at the greatest height sampled",
        "Sulfur dioxide is the same at every height sampled",
        "Sulfur dioxide rises steadily with height throughout the column",
        "The sulfur dioxide measurements show no relationship to height"],
      ans=0,
      why="The pollutant readings are an order of magnitude larger at the three lowest "
          "heights, which lie beneath the level where the temperature stops increasing, "
          "than at the two heights above it. The pollution is therefore concentrated in "
          "the layer the inversion caps."),

 dict(q="Two cities report the measurements below on the same morning.",
      table=_T_TWO_CITIES,
      choices=[
        "Only City J shows the altered gradient, since its ground air is cooler than "
        "its air at 400 meters",
        "Only City K shows the altered gradient",
        "Both cities show the altered gradient",
        "Neither city shows the altered gradient",
        "The measurements cannot distinguish the two cities"],
      ans=0,
      why="An inversion is the case in which surface air is cooler than the air above. "
          "City J's ground reading is below its reading aloft, while City K's ground "
          "reading is above its reading aloft, so only City J meets the definition."),

 dict(q="Which single set of measurements would best allow an investigator to determine "
        "whether a thermal inversion is present over a city?",
      choices=[
        "Air temperature at the ground and at one or more heights above it, taken at "
        "the same time",
        "Air temperature at the ground alone, taken every hour for a week",
        "The concentration of particulates at the ground alone",
        "The number of vehicles entering the city that morning",
        "The daily rainfall total for the city"],
      ans=0,
      why="The definition compares the temperature at the surface with the temperature "
          "at higher altitude, so it takes readings at two or more heights at one time "
          "to test. A surface record alone, a pollutant count, a traffic count and a "
          "rainfall total leave the comparison unmade."),

 dict(q="What does the framework's phrase about the normal temperature gradient being "
        "altered tell a student about the usual state of the lower atmosphere?",
      choices=[
        "Air near the surface is usually warmer than the air above it",
        "Air near the surface is usually cooler than the air above it",
        "Air temperature usually does not change with height",
        "Air temperature usually rises with height in every layer",
        "Air near the surface usually holds no pollution at all"],
      ans=0,
      why="The framework calls an inversion the altered case and describes that case as "
          "the surface being cooler than the air above, which means the unaltered case "
          "is the reverse. The usual state is therefore surface air warmer than the air "
          "above it."),

 dict(q="Measurements from four sites on one winter morning are shown.",
      table=_T_VALLEYS,
      choices=[
        "The two sites where the ground is cooler than the air at 200 meters recorded "
        "the two highest particulate values",
        "The two sites where the ground is warmer than the air above recorded the two "
        "highest particulate values",
        "All four sites recorded the same particulate value",
        "Particulate values are highest where the temperature difference is smallest",
        "The temperature readings and the particulate readings are unrelated in these "
        "data"],
      ans=0,
      why="Sites 1 and 2 have ground readings below their readings at 200 meters, which "
          "is the inversion condition, and they hold the two largest particulate "
          "measurements; the two sites with the ordinary ordering hold the two "
          "smallest. That is the trapping the framework describes."),

 dict(q="A city's smog and particulate concentrations fall sharply by early afternoon "
        "on a day that began with an inversion, although traffic has not changed. Which "
        "explanation is best supported?",
      choices=[
        "The surface air has warmed above the air aloft, so the pollution is no longer "
        "held close to the ground",
        "The pollutants have chemically destroyed one another during the morning",
        "Vehicles stop releasing pollutants once the air warms",
        "The instruments become less sensitive as the day warms",
        "The pollutants have been absorbed by the pavement"],
      ans=0,
      why="An inversion is the arrangement in which surface air is cooler than the air "
          "above, and it is that arrangement which traps pollution near the ground. "
          "When the surface warms past the air aloft the arrangement is gone, so the "
          "same releases are no longer confined."),

 dict(q="A student says a thermal inversion is a kind of air pollution. What is the "
        "clearest correction?",
      choices=[
        "An inversion is an arrangement of air temperature with height, and its "
        "importance is that it traps pollution released by other sources",
        "An inversion is a pollutant released by vehicles in cold weather",
        "An inversion is a chemical reaction between smog and particulates",
        "An inversion is a measurement error caused by cold instruments",
        "An inversion is a form of precipitation that carries pollution to the ground"],
      ans=0,
      why="The framework defines an inversion by the temperature of the air at the "
          "surface relative to the air above, which is a physical arrangement rather "
          "than a substance. Its relationship with pollution is that it traps what "
          "other sources release."),

 dict(q="During a multi-day episode, ground-level readings are recorded alongside "
        "whether an inversion was present at dawn.",
      table=_T_EPISODE,
      choices=[
        "Both smog and particulates were higher on the days when an inversion was "
        "present than on the days when it was not",
        "Smog was higher on inversion days but particulates were lower",
        "Particulates were higher on inversion days but smog was lower",
        "Both were higher on the days without an inversion",
        "Neither pollutant differed between the two kinds of day"],
      ans=0,
      why="Each of the two inversion days carries larger values in both pollutant "
          "columns than either of the two days without an inversion. The framework "
          "names smog and particulates as the pollution an inversion especially traps "
          "close to the ground."),

 dict(q="A regional agency warns residents to limit outdoor activity when an inversion "
        "is forecast. Which reasoning best supports the warning?",
      choices=[
        "An inversion holds smog and particulates near the ground, so the air people "
        "breathe carries more of them than it otherwise would",
        "An inversion produces new pollutants that are more toxic than the originals",
        "An inversion lowers the oxygen content of the air near the ground",
        "An inversion raises the surface temperature to dangerous levels",
        "An inversion causes vehicles to release more pollution per kilometer"],
      ans=0,
      why="The framework's claim is that a thermal inversion traps pollution close to "
          "the ground, especially smog and particulates, which is exactly a rise in "
          "what people at ground level breathe. It says nothing about new toxicity, "
          "oxygen content, dangerous surface heat or vehicle emission rates."),

 dict(q="Which of the following changes to an air quality study would best show whether "
        "inversions are affecting a city's pollution levels?",
      choices=[
        "Record the temperature at two heights each morning alongside the existing "
        "ground-level pollutant readings",
        "Record the ground-level pollutant readings more precisely",
        "Record the pollutant readings only on days when no inversion is expected",
        "Record the pollutant readings at a rural site instead of in the city",
        "Record the number of hours of sunshine each day instead of the temperature"],
      ans=0,
      why="Testing the relationship requires the presence or absence of an inversion to "
          "be measured as well as the pollution, which needs temperatures at two "
          "heights. Greater precision on one variable, dropping the inversion days, "
          "moving the site, or substituting sunshine hours all leave the comparison "
          "impossible."),

 dict(q="Two mornings have identical vehicle traffic and identical emissions, but "
        "ground-level particulates are three times higher on the first morning. Which "
        "condition would best account for the difference?",
      choices=[
        "An inversion was present on the first morning and absent on the second",
        "The first morning had stronger sunlight than the second",
        "The first morning had a higher surface temperature than the second",
        "The second morning had more vehicles on the road than the first",
        "The instruments were replaced between the two mornings"],
      ans=0,
      why="With releases held equal, the concentration at ground level depends on "
          "whether the pollution is confined near the ground, and the framework "
          "attributes that confinement to a thermal inversion. The stem has already "
          "fixed traffic, and a change of instruments would not be a condition of the "
          "atmosphere."),

 dict(q="Which pair of readings taken at the same moment would demonstrate that no "
        "inversion is present?",
      choices=[
        "Twenty degrees Celsius at the ground and sixteen degrees Celsius at 500 meters",
        "Four degrees Celsius at the ground and ten degrees Celsius at 500 meters",
        "Two degrees Celsius at the ground and five degrees Celsius at 200 meters",
        "Zero degrees Celsius at the ground and three degrees Celsius at 100 meters",
        "One degree Celsius at the ground and nine degrees Celsius at 400 meters"],
      ans=0,
      why="An inversion requires the surface air to be cooler than the air above, so a "
          "pair in which the ground reading is the warmer of the two rules it out. In "
          "every rejected pair the ground reading is the cooler one, which is the "
          "inversion condition rather than its absence."),

 dict(q="A city with heavy industry reports its worst air quality on mornings when the "
        "air near the ground is coldest relative to the air above. How does this fit "
        "the framework?",
      choices=[
        "It matches the framework, because that temperature ordering is the inversion "
        "that traps pollution close to the ground",
        "It contradicts the framework, because cold air cannot hold pollution",
        "It is unrelated to the framework, because the framework treats only indoor air",
        "It matches the framework only if the pollution comes from vehicles rather than "
        "from industry",
        "It contradicts the framework, because pollution is always worst in the "
        "afternoon"],
      ans=0,
      why="The reported condition is the altered gradient the framework defines, and "
          "the reported consequence is the trapping of pollution near the ground it "
          "describes. The statement about trapping is not limited to a particular kind "
          "of source or a particular hour of the day."),

 dict(q="Which description of a thermal inversion would be accurate to give to someone "
        "who has only seen a temperature profile plotted against height?",
      choices=[
        "A layer in which temperature increases upward, lying above cooler air at the "
        "surface",
        "A layer in which temperature decreases upward more steeply than usual",
        "A layer of constant temperature at the very top of the atmosphere",
        "A layer in which the wind reverses direction with height",
        "A layer in which humidity rather than temperature increases with height"],
      ans=0,
      why="The framework defines the inversion by temperature: the surface air is "
          "cooler than the air at higher altitudes, which appears as temperature "
          "increasing upward above the cool surface layer. Wind and humidity are not "
          "part of the definition it gives."),

 dict(q="An analyst argues that reducing emissions is pointless because inversions will "
        "occur anyway. Which response is best supported by the framework?",
      choices=[
        "An inversion concentrates whatever pollution has been released, so smaller "
        "releases still mean less pollution trapped near the ground",
        "Inversions destroy pollutants, so emissions are irrelevant on those days",
        "Inversions release pollutants of their own, so emissions cannot be reduced",
        "Inversions occur only where emissions are already low",
        "Inversions raise emissions from vehicles, so reductions cannot succeed"],
      ans=0,
      why="The framework has the inversion trap pollution close to the ground; the "
          "quantity trapped is whatever the sources released. Reducing releases "
          "therefore reduces the amount confined, and the framework attributes to the "
          "inversion no destruction of pollutants and no source of its own."),

 dict(q="A monitoring program measures particulates only at 600 meters above a city "
        "during an inversion and reports that air quality is good. What is the flaw?",
      choices=[
        "The pollution is trapped close to the ground, so a measurement above the "
        "trapped layer misses it",
        "Particulates cannot be measured at that height with any instrument",
        "The reading should have been taken at night rather than during the day",
        "Particulates are not among the pollutants an inversion affects",
        "The program should have measured temperature instead of particulates"],
      ans=0,
      why="An inversion holds the pollution near the ground, so a sampler placed above "
          "that layer is not sampling the air the pollution is in. Particulates are "
          "among the pollutants the framework names as especially trapped."),

 dict(q="Which of the following best explains why smog is especially associated with "
        "inversions in the framework?",
      choices=[
        "Smog is one of the two kinds of pollution the framework names as being trapped "
        "close to the ground during an inversion",
        "Smog can only form when the surface air is cooler than the air above",
        "Smog is produced by the inversion itself rather than by any source",
        "Smog rises rapidly and so is unaffected by conditions near the ground",
        "Smog is a natural component of clean air that becomes visible when it is cold"],
      ans=0,
      why="The framework names smog and particulates as the pollution an inversion "
          "especially traps close to the ground. It does not make the inversion a "
          "condition for smog to form or a source of smog, and smog is not a component "
          "of clean air."),

 dict(q="A student is asked what would happen to ground-level pollution if the "
        "temperature at 300 meters fell below the temperature at the ground during an "
        "episode. Which prediction is best supported?",
      choices=[
        "The arrangement that traps pollution near the ground would be gone, so "
        "ground-level concentrations would be expected to fall",
        "The pollution would be trapped even more tightly than before",
        "The pollution would be converted into a different pollutant",
        "Ground-level concentrations would be unaffected by the change",
        "The pollution would be drawn upward into the stratosphere and destroyed"],
      ans=0,
      why="The trapping the framework describes belongs to the case in which the "
          "surface air is cooler than the air above. Reversing that ordering removes "
          "the condition, so the pollution released at the surface is no longer held in "
          "the shallow layer."),

 dict(q="Which statement about inversions and pollution sources is best supported by "
        "the framework?",
      choices=[
        "An inversion changes where released pollution goes, while the sources "
        "determine how much is released",
        "An inversion determines how much pollution is released, while the sources "
        "determine where it goes",
        "An inversion and the sources both determine only the color of the haze",
        "An inversion removes the need to identify pollution sources",
        "An inversion affects only pollution released above 300 meters"],
      ans=0,
      why="The framework's inversion statement is about the pollution being trapped "
          "close to the ground, which is a statement about where it goes. How much "
          "enters the air is a matter of the sources identified under the earlier "
          "learning objective."),

 dict(q="Air quality complaints in one city cluster on cold, still mornings. Which "
        "additional measurement would most strengthen the case that inversions are "
        "responsible?",
      choices=[
        "Paired temperature readings at the ground and aloft on complaint mornings and "
        "on comparable mornings without complaints",
        "The total number of complaints filed each year for the past decade",
        "The average temperature of the city over the whole year",
        "The number of residents living within the city limits",
        "The color of the haze reported by the people who complained"],
      ans=0,
      why="The claim is that the temperature ordering the framework defines is present "
          "when the air is worst, so the measurement that tests it is the paired "
          "reading on both kinds of morning. Annual totals, yearly averages, "
          "population and haze color leave the definition untested."),

 dict(q="Why does the framework treat a thermal inversion as relevant to human health "
        "even though it is a temperature phenomenon?",
      choices=[
        "Because it holds pollution in the layer of air where people live and breathe",
        "Because the temperature change itself is enough to cause illness",
        "Because it destroys the ozone layer above the affected city",
        "Because it converts particulates into gases that are easier to inhale",
        "Because it prevents rainfall from reaching the ground"],
      ans=0,
      why="The framework connects the inversion to pollution by having it trap that "
          "pollution close to the ground, which is where people are. It makes no claim "
          "about the temperature harming health directly, about stratospheric ozone, or "
          "about changing the physical state of particulates."),

 dict(q="Two profiles are described. In the first, temperature falls from the ground "
        "upward at every measured height. In the second, temperature rises from the "
        "ground up to 250 meters and then falls. Which comparison is correct?",
      choices=[
        "Only the second profile shows the altered gradient that traps pollution near "
        "the ground",
        "Only the first profile shows the altered gradient",
        "Both profiles show the altered gradient",
        "Neither profile shows the altered gradient",
        "The first profile shows an inversion above 250 meters"],
      ans=0,
      why="The altered gradient the framework defines has surface air cooler than the "
          "air above, which is the second description. The first is the ordinary "
          "arrangement, in which the surface holds the warmest air in the column."),

 dict(q="An industrial plant proposes to build a taller stack so that its exhaust is "
        "released above the height at which the temperature stops increasing during "
        "local inversions. What does the framework's statement about inversions suggest "
        "about ground-level concentrations near the plant?",
      choices=[
        "Exhaust released above that layer is not held close to the ground by the "
        "inversion, so ground-level concentrations near the plant would be expected to "
        "be lower",
        "Ground-level concentrations near the plant would rise, because taller stacks "
        "trap more pollution",
        "Ground-level concentrations would be unchanged, since stack height cannot "
        "affect where pollution goes",
        "The inversion would be destroyed by the taller stack",
        "The exhaust would be converted into smog by the inversion itself"],
      ans=0,
      why="What the framework attributes to an inversion is the trapping of pollution "
          "close to the ground, so exhaust that enters the air above the trapped layer "
          "is not subject to that confinement near the plant. The inversion is an "
          "arrangement of air temperature and is not created or destroyed by a stack."),

 dict(q="Which summary best states the relationship between thermal inversion and "
        "pollution as the framework gives it?",
      choices=[
        "When surface air is cooler than the air above it, the normal gradient is "
        "altered and pollution, especially smog and particulates, is held close to the "
        "ground",
        "When surface air is warmer than the air above it, pollution is held close to "
        "the ground and cannot disperse",
        "An inversion generates smog and particulates that would not otherwise exist",
        "An inversion moves pollution from the ground into the upper atmosphere, where "
        "it is destroyed",
        "An inversion affects the temperature of the air but has no relationship with "
        "pollution"],
      ans=0,
      why="The summary joins the framework's two statements in the order it gives them: "
          "the altered gradient with cooler surface air, and the trapping of pollution "
          "close to the ground, especially smog and particulates. Each rejected summary "
          "reverses one of those statements or denies it."),
]
