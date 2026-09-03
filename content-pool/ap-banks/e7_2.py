# AP ENVIRONMENTAL SCIENCE 7.2 Photochemical Smog
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objective STB-2.B: explain the causes and effects of photochemical smog and
# methods to reduce it. Suggested skill 5.B, describe relationships among variables in
# data represented.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.B.1  Photochemical smog is formed when nitrogen oxides and volatile organic
#              hydrocarbons react with heat and sunlight to produce a variety of
#              pollutants.
#   STB-2.B.2  Many environmental factors affect the formation of photochemical smog.
#   STB-2.B.3  Nitrogen oxide is produced early in the day. Ozone concentrations peak
#              in the afternoon and are higher in the summer because ozone is produced
#              by chemical reactions between oxygen and sunlight.
#   STB-2.B.4  Volatile Organic Compounds (VOCs), such as formaldehyde and gasoline,
#              evaporate or sublimate at room temperature. Trees are a natural source
#              of VOCs.
#   STB-2.B.5  Photochemical smog often forms in urban areas because of the large
#              number of motor vehicles there.
#   STB-2.B.6  Photochemical smog can be reduced through the reduction of nitrogen
#              oxide and VOCs.
#   STB-2.B.7  Photochemical smog can harm human health in several ways, including
#              causing respiratory problems and eye irritation.
#
# ON SCOPE. Topic 7.1 keys the sources of nitrogen oxides and the primary/secondary
# distinction; this topic keys the formation of smog, its daily and seasonal pattern,
# the VOCs, the urban setting, the two reduction levers, and the health effects. The
# control devices that achieve those reductions belong to 7.6 and are not keyed here.
# Nothing in this module names a city, an episode or a regulation: the framework names
# none, and an illustrative example is not assessable.
#
# ON THE TIME-OF-DAY DATA. STB-2.B.3 states the pattern the tables show -- nitrogen
# oxide early in the day, ozone peaking in the afternoon -- so no item asks a student
# to recall a concentration. Every keyed reading is recomputed in verify_e7_2.py from
# the table alone.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII: export_units.py does not typeset
# ENV_SCI.
TOPIC = ("7.2", "Photochemical Smog", 7)

_T_DAY = dict(
    headers=["Time of day", "Nitrogen oxide (parts per billion)",
             "Ozone (parts per billion)"],
    rows=[["6 in the morning", "70", "10"],
          ["9 in the morning", "50", "30"],
          ["Noon", "25", "70"],
          ["3 in the afternoon", "15", "95"],
          ["6 in the evening", "20", "60"]])

_T_SEASON = dict(
    headers=["Month of sampling", "Average daily sunlight hours",
             "Average afternoon ozone (parts per billion)"],
    rows=[["January", "5", "25"],
          ["April", "9", "45"],
          ["July", "13", "80"],
          ["October", "8", "40"]])

_T_SETTING = dict(
    headers=["Sampling area", "Motor vehicles counted per hour on nearby roads",
             "Afternoon ozone (parts per billion)"],
    rows=[["City center", "4,000", "90"],
          ["Suburban edge", "1,200", "60"],
          ["Rural valley", "150", "30"]])

_T_TEMP = dict(
    headers=["Day", "Afternoon air temperature (degrees Celsius)",
             "Afternoon ozone (parts per billion)"],
    rows=[["Day 1", "18", "35"],
          ["Day 2", "24", "55"],
          ["Day 3", "30", "80"],
          ["Day 4", "35", "100"]])

_T_CUT = dict(
    headers=["Modeled scenario for one city",
             "Nitrogen oxides released (tons per day)",
             "Volatile organic compounds released (tons per day)",
             "Peak afternoon ozone (parts per billion)"],
    rows=[["No change", "200", "160", "100"],
          ["Nitrogen oxides cut by half", "100", "160", "75"],
          ["Volatile organic compounds cut by half", "200", "80", "80"],
          ["Both cut by half", "100", "80", "55"]])

_T_HEALTH = dict(
    headers=["Ozone band for the afternoon (parts per billion)",
             "Clinic visits for breathing difficulty per 100,000 residents",
             "Clinic visits for eye irritation per 100,000 residents"],
    rows=[["Below 40", "12", "5"],
          ["40 to 69", "20", "9"],
          ["70 to 99", "34", "16"],
          ["100 and above", "51", "26"]])

_T_VOC = dict(
    headers=["Source sampled", "Volatile organic compounds released (kilograms per day)"],
    rows=[["Fuel storage and refueling", "900"],
          ["Solvent and paint use", "600"],
          ["Forested hillside", "250"],
          ["Water treatment ponds", "20"]])

QUESTIONS = [

 dict(q="Which combination does the framework identify as producing photochemical smog?",
      choices=[
        "Nitrogen oxides and volatile organic hydrocarbons reacting with heat and sunlight",
        "Sulfur dioxide and water vapor reacting in cold, dark conditions",
        "Carbon dioxide and methane accumulating above a city at night",
        "Radon and dust settling out of still air near the ground",
        "Chlorofluorocarbons breaking apart in the stratosphere"],
      ans=0,
      why="The framework has photochemical smog form when nitrogen oxides and volatile "
          "organic hydrocarbons react with heat and sunlight to produce a variety of "
          "pollutants. Sulfur chemistry in the dark, greenhouse gas accumulation, "
          "settling dust and stratospheric chemistry are all different processes."),

 dict(q="Measurements over one city on a clear summer day are shown.",
      table=_T_DAY,
      choices=[
        "Nitrogen oxide is highest early in the day, and ozone climbs to its highest "
        "value in the afternoon",
        "Ozone is highest early in the day and falls all afternoon",
        "The two substances reach their highest values at the same hour",
        "Nitrogen oxide climbs steadily from morning until evening",
        "Neither substance changes appreciably during the day"],
      ans=0,
      why="The tabulated nitrogen oxide is largest at the first sampling hour and the "
          "tabulated ozone is largest in the afternoon, which is the pattern the "
          "framework states. The two maxima therefore fall at different hours and "
          "neither series is flat."),

 dict(q="Why does the framework say ozone concentrations peak in the afternoon rather "
        "than at dawn?",
      choices=[
        "Ozone is produced by chemical reactions between oxygen and sunlight, so it "
        "builds up after the sun has been shining for hours",
        "Ozone is released from vehicle tailpipes only during the afternoon commute",
        "Ozone drifts down from the stratosphere when the ground cools",
        "Ozone is destroyed by moonlight and re-forms once the moon has set",
        "Ozone is heavier than air and rises to instrument height only in the afternoon"],
      ans=0,
      why="The framework attributes ozone to chemical reactions between oxygen and "
          "sunlight, so the concentration climbs while the sun is up and reaches its "
          "highest values in the afternoon. It is not emitted from tailpipes in the "
          "form measured and does not depend on moonlight or on rising through the air."),

 dict(q="Data from four months at one urban site are shown.",
      table=_T_SEASON,
      choices=[
        "Afternoon ozone is highest in the month with the most daily sunlight",
        "Afternoon ozone is highest in the month with the least daily sunlight",
        "Afternoon ozone is the same in all four months",
        "Afternoon ozone falls as daily sunlight rises",
        "The two variables are unrelated in these data"],
      ans=0,
      why="Ranking the months by sunlight hours puts the highest ozone with the "
          "longest days and the lowest ozone with the shortest, so the two rise "
          "together. That matches the framework's statement that ozone is higher in "
          "the summer because it is produced by reactions between oxygen and sunlight."),

 dict(q="Which of the following best describes volatile organic compounds as the "
        "framework defines them?",
      choices=[
        "Compounds such as formaldehyde and gasoline that evaporate or sublimate at "
        "room temperature",
        "Compounds that only enter the air when heated above the boiling point of water",
        "Metallic elements released as fine particles from industrial furnaces",
        "Acids formed in cloud droplets and returned to the ground in rain",
        "Inert gases that make up a fixed share of clean dry air"],
      ans=0,
      why="The framework's own examples are formaldehyde and gasoline, and it states "
          "that volatile organic compounds evaporate or sublimate at room temperature, "
          "which is why they enter the air without being burned. Metals, acids and "
          "inert gases are described elsewhere and are not organic compounds."),

 dict(q="A survey of volatile organic compound sources around one city is shown.",
      table=_T_VOC,
      choices=[
        "Most of the measured release comes from human uses of fuel and solvents, but "
        "the forested hillside is a natural source as well",
        "Every source measured is a human-made source",
        "The forested hillside releases more than all the other sources combined",
        "Only combustion can release volatile organic compounds",
        "The measurements show that volatile organic compounds cannot come from "
        "vegetation"],
      ans=0,
      why="The two human sources together exceed the other entries, while the forested "
          "hillside still records a substantial release, and the framework states that "
          "trees are a natural source of volatile organic compounds. Nothing here "
          "requires combustion, since these compounds evaporate at room temperature."),

 dict(q="Why does the framework associate photochemical smog particularly with urban "
        "areas?",
      choices=[
        "Urban areas hold a large number of motor vehicles",
        "Urban areas are colder than the countryside at every hour",
        "Urban areas receive more rainfall than surrounding areas",
        "Urban areas have more trees per unit area than rural areas",
        "Urban areas sit at higher elevations where sunlight is stronger"],
      ans=0,
      why="The framework states that photochemical smog often forms in urban areas "
          "because of the large number of motor vehicles there, which supply the "
          "nitrogen oxides and volatile organic compounds the reaction needs. Cooler "
          "temperatures, more rain, more trees and higher ground are not what it names."),

 dict(q="Measurements from three settings on the same afternoon are shown.",
      table=_T_SETTING,
      choices=[
        "Ozone rises with the number of motor vehicles counted nearby",
        "Ozone falls as the number of motor vehicles rises",
        "The rural valley recorded the highest ozone of the three areas",
        "Vehicle counts and ozone are identical in the three areas",
        "The suburban edge recorded higher ozone than the city center"],
      ans=0,
      why="Ordering the three areas by vehicle count gives the same order as ordering "
          "them by afternoon ozone, so the two increase together, and the framework "
          "ties urban smog to the large number of motor vehicles. The rural and "
          "suburban readings are both below the city center reading."),

 dict(q="Which two reductions does the framework name as ways to reduce photochemical "
        "smog?",
      choices=[
        "Reducing nitrogen oxide and reducing volatile organic compounds",
        "Reducing carbon dioxide and reducing water vapor",
        "Reducing sulfur dioxide and reducing radon",
        "Reducing particulate matter and reducing noise",
        "Reducing chlorofluorocarbons and reducing methane"],
      ans=0,
      why="Photochemical smog can be reduced through the reduction of nitrogen oxide "
          "and volatile organic compounds, which are the two reactants the framework "
          "puts into its formation. The other pairs name pollutants that are not "
          "ingredients of this reaction."),

 dict(q="A city models three control strategies. The results are shown.",
      table=_T_CUT,
      choices=[
        "Cutting both nitrogen oxides and volatile organic compounds lowers peak ozone "
        "more than cutting either one alone",
        "Cutting volatile organic compounds alone lowers peak ozone more than cutting "
        "both together",
        "Neither cut changes peak ozone at all",
        "Cutting nitrogen oxides alone raises peak ozone above the no-change case",
        "Only cuts to volatile organic compounds have any effect on peak ozone"],
      ans=0,
      why="The modeled peak ozone is lowest in the scenario that cuts both, and each "
          "single cut leaves a higher peak than the combined cut while still lowering "
          "it below the no-change case. That is what the framework's two named levers "
          "would be expected to do, since both are reactants."),

 dict(q="Which health effects does the framework attribute to photochemical smog?",
      choices=[
        "Respiratory problems and eye irritation",
        "Broken bones and joint injuries",
        "Tooth decay and gum disease",
        "Improved lung capacity in children",
        "Reduced risk of infectious disease"],
      ans=0,
      why="The framework states that photochemical smog can harm human health in "
          "several ways, including causing respiratory problems and eye irritation. "
          "Skeletal and dental harm are not among them, and no benefit to health is "
          "claimed anywhere for smog."),

 dict(q="Clinic records for one city are grouped by the afternoon ozone measured that "
        "day.",
      table=_T_HEALTH,
      choices=[
        "Visits for both breathing difficulty and eye irritation rise as the ozone band "
        "rises",
        "Visits for breathing difficulty rise while visits for eye irritation fall",
        "Visits for eye irritation are unrelated to the ozone band",
        "Visits of both kinds are highest in the lowest ozone band",
        "The two kinds of visit are equal in number in every band"],
      ans=0,
      why="Both columns increase from the lowest ozone band to the highest, which "
          "matches the framework's statement that photochemical smog can cause "
          "respiratory problems and eye irritation. Neither column falls, and the two "
          "columns differ in every band."),

 dict(q="A student writes that nitrogen oxide concentrations are usually highest early "
        "in the day. Which explanation is consistent with the framework?",
      choices=[
        "Nitrogen oxide is produced early in the day, before the sunlight-driven "
        "chemistry that builds ozone has had time to act",
        "Nitrogen oxide is produced only at night and destroyed at sunrise",
        "Nitrogen oxide is produced by the same reaction that produces ozone, so the "
        "two must peak together",
        "Nitrogen oxide is heavier than ozone and therefore settles overnight",
        "Nitrogen oxide is a natural component of clean air that varies with the tides"],
      ans=0,
      why="The framework states that nitrogen oxide is produced early in the day and "
          "that ozone peaks in the afternoon, so the two are separated in time rather "
          "than produced by one reaction. Nothing in the framework has nitrogen oxide "
          "made at night, settling by weight, or following the tides."),

 dict(q="On which day would photochemical smog be most likely to build up over a city, "
        "based on the conditions the framework names as necessary for its formation?",
      choices=[
        "A hot, sunny weekday with heavy traffic",
        "A cold, overcast weekday with heavy traffic",
        "A hot, sunny day when the roads are closed and traffic is absent",
        "A cold, overcast night with light traffic",
        "A mild, rainy weekend with light traffic"],
      ans=0,
      why="Formation requires nitrogen oxides and volatile organic compounds together "
          "with heat and sunlight, so the day that supplies all of them at once is the "
          "hot sunny day with heavy traffic. Removing the sunlight, the heat or the "
          "traffic removes an ingredient the framework names."),

 dict(q="A regional agency reports that smog forms on some warm sunny days and not on "
        "others, even though traffic is similar. Which statement from the framework "
        "best accounts for that variability?",
      choices=[
        "Many environmental factors affect the formation of photochemical smog",
        "Photochemical smog forms only in the absence of sunlight",
        "Photochemical smog forms at a fixed rate that never varies",
        "Photochemical smog is unrelated to the substances released by vehicles",
        "Photochemical smog forms only where there are no trees"],
      ans=0,
      why="The framework states plainly that many environmental factors affect the "
          "formation of photochemical smog, which is why days with similar traffic can "
          "differ. The other options contradict the formation conditions or the urban "
          "vehicle source the framework gives."),

 dict(q="Afternoon measurements on four days at one site are shown.",
      table=_T_TEMP,
      choices=[
        "Ozone rises as the afternoon temperature rises across these four days",
        "Ozone falls as the afternoon temperature rises",
        "Ozone is highest on the coolest of the four days",
        "Temperature and ozone show no consistent relationship in these data",
        "Ozone is the same on all four days despite the temperature difference"],
      ans=0,
      why="Sorting the four days by temperature puts the ozone values in increasing "
          "order as well, so the two rise together, and the framework has heat as one "
          "of the conditions under which nitrogen oxides and volatile organic "
          "compounds react to form smog."),

 dict(q="A city proposes to reduce photochemical smog by requiring vapor-tight fittings "
        "on fuel storage tanks and refueling equipment. Which reactant does that "
        "measure target?",
      choices=[
        "Volatile organic compounds, since gasoline evaporates at room temperature",
        "Nitrogen oxides, since fuel tanks emit them while standing",
        "Sulfur dioxide, since fuel tanks contain sulfur",
        "Ozone, since it is stored in the tank with the fuel",
        "Particulate matter, since fuel tanks shed rust"],
      ans=0,
      why="The framework names gasoline as a volatile organic compound that evaporates "
          "at room temperature, so sealing its vapors removes one of the two reactants "
          "that photochemical smog requires. Nitrogen oxides come from combustion "
          "rather than from a standing tank, and ozone is not stored anywhere."),

 dict(q="A researcher records ozone every hour for a week and reports only the daily "
        "average. A colleague objects that the report hides the effect the framework "
        "describes. Which change best answers the objection?",
      choices=[
        "Report the concentration by hour so that the afternoon peak is visible",
        "Report a single average for the whole week instead",
        "Report the lowest reading of each day instead of the average",
        "Report the readings rounded to the nearest hundred parts per billion",
        "Report only the readings taken before sunrise"],
      ans=0,
      why="The framework's claim is about when ozone peaks during the day, so the "
          "hour-by-hour record is what shows it and a daily average conceals it. "
          "Averaging further, reporting a minimum, coarse rounding and pre-dawn-only "
          "sampling all remove the afternoon information."),

 dict(q="Which statement best explains why photochemical smog is described as a mixture "
        "rather than a single substance?",
      choices=[
        "The reaction of nitrogen oxides and volatile organic compounds with heat and "
        "sunlight produces a variety of pollutants",
        "Smog is a single gas that appears in several colors",
        "Smog is simply airborne dust that has been warmed by the sun",
        "Smog is the name for nitrogen oxide once it has been diluted",
        "Smog is water vapor that has condensed around a single pollutant"],
      ans=0,
      why="The framework says the reaction produces a variety of pollutants, which is "
          "why the product is a mixture. It is not a single gas, not warmed dust, not "
          "diluted nitrogen oxide, and not condensed water."),

 dict(q="Two adjacent regions have similar vehicle traffic, but one is much sunnier "
        "through the summer. Which prediction follows from the framework?",
      choices=[
        "The sunnier region will tend to form more photochemical smog during those months",
        "The cloudier region will form more smog because sunlight destroys smog",
        "Neither region will form smog, because sunlight is not involved",
        "Both regions will form identical amounts, since traffic is the only factor",
        "Smog will form only after sunset in both regions"],
      ans=0,
      why="Sunlight and heat are part of the reaction that forms photochemical smog, "
          "and the framework attributes higher summer ozone to production by reactions "
          "between oxygen and sunlight. So with the vehicle sources similar, the "
          "sunnier region is the one expected to form more."),

 dict(q="A school moves outdoor athletic practice from mid-afternoon to early morning "
        "during the summer. Which reasoning best supports the change?",
      choices=[
        "Ozone concentrations peak in the afternoon, so exercising earlier reduces "
        "exposure to the pollutant most associated with respiratory irritation",
        "Ozone is a primary pollutant released only in the morning, so morning air is "
        "already free of it",
        "Ozone is destroyed by exercise, so morning practice removes it from the air",
        "Ozone is harmless, so the change is made for reasons unrelated to air quality",
        "Ozone concentrations are highest before sunrise, so an early practice avoids "
        "the evening buildup"],
      ans=0,
      why="The framework has ozone peaking in the afternoon and attributes respiratory "
          "problems and eye irritation to photochemical smog, so shifting activity away "
          "from the peak lowers exposure. The rejected options invert the daily pattern "
          "or deny the harm the framework states."),

 dict(q="Which of the following is the best evidence that trees can contribute to the "
        "chemistry that forms photochemical smog?",
      choices=[
        "Volatile organic compounds are one of the two reactants, and trees are a "
        "natural source of them",
        "Trees release nitrogen oxides in proportion to their leaf area",
        "Trees shade the ground and therefore raise the temperature of the air above them",
        "Trees release ozone directly from their leaves during the afternoon",
        "Trees absorb sunlight that would otherwise be reflected back to space"],
      ans=0,
      why="The framework names trees as a natural source of volatile organic compounds, "
          "and volatile organic compounds are one of the two reactants it puts into the "
          "formation of smog. It gives trees no emission of nitrogen oxides or ozone "
          "and no warming role of the kind described."),

 dict(q="An analyst claims that reducing only volatile organic compounds cannot "
        "possibly reduce photochemical smog because nitrogen oxides would still be "
        "released. Which response is best supported by the framework?",
      choices=[
        "Smog formation requires both reactants, so lowering either one can lower the "
        "amount of smog formed",
        "Reducing volatile organic compounds has no effect because sunlight is the only "
        "requirement",
        "The claim is right, because only nitrogen oxide reductions are named as a "
        "method of control",
        "Reducing volatile organic compounds converts them into nitrogen oxides",
        "Smog forms from a single pollutant, so reducing a second one is irrelevant"],
      ans=0,
      why="The framework names the reduction of nitrogen oxide AND volatile organic "
          "compounds as methods of reducing photochemical smog, and both are reactants "
          "in the formation it describes. Removing either therefore limits how much can "
          "form, and no conversion of one into the other is described."),

 dict(q="Which observation would most weaken a claim that a city's afternoon ozone "
        "comes from its own traffic rather than from air arriving from elsewhere?",
      choices=[
        "Ozone rises through the afternoon on days when the wind blows in from a large "
        "upwind urban area and stays low on otherwise similar days when it does not",
        "Ozone is higher in July than in January in the city",
        "Ozone is higher in the afternoon than at dawn in the city",
        "Nitrogen oxide is higher early in the morning than at midday",
        "Volatile organic compounds are released by the city's fuel handling"],
      ans=0,
      why="The competing explanation is transport from outside, so the observation that "
          "bears on it is one that ties the city's ozone to the wind bringing air from "
          "another source region. The other options are patterns the framework predicts "
          "for locally formed smog and so do not distinguish the two explanations."),

 dict(q="Why can a substance that is never released from a tailpipe still reach its "
        "highest concentration over a city full of vehicles?",
      choices=[
        "It is produced in the air by reactions among substances the vehicles do "
        "release, driven by heat and sunlight",
        "It is stored in road surfaces and released when they warm",
        "It is carried into the city by rain falling through clean air",
        "It is created inside measuring instruments during warm weather",
        "It is released by pedestrians rather than by vehicles"],
      ans=0,
      why="The framework has nitrogen oxides and volatile organic compounds react with "
          "heat and sunlight to produce a variety of pollutants, so the product forms "
          "in the air above the source of its ingredients. Pavement, rainfall, "
          "instruments and pedestrians are not given as sources."),

 dict(q="A city plans to cut smog by replacing part of its vehicle fleet. Which "
        "evidence would best support the plan?",
      choices=[
        "Measurements showing that the replacement vehicles release less nitrogen oxide "
        "and fewer volatile organic compounds than the vehicles they replace",
        "Measurements showing that the replacement vehicles are quieter than the "
        "vehicles they replace",
        "Measurements showing that the replacement vehicles cost less to maintain",
        "Measurements showing that the replacement vehicles are lighter in color",
        "Measurements showing that the replacement vehicles travel more kilometers each day"],
      ans=0,
      why="The framework names the reduction of nitrogen oxide and volatile organic "
          "compounds as the way to reduce photochemical smog, so the supporting "
          "evidence is a measured reduction in those two releases. Noise, cost, color "
          "and distance travelled do not speak to either reactant."),

 dict(q="An investigator samples ozone at one site for a single hour in January and "
        "concludes that the city has no summer smog problem. What is the clearest "
        "weakness of that conclusion?",
      choices=[
        "The sample was taken in the season and at a time of day when the framework "
        "predicts ozone to be lowest",
        "The sample was taken outdoors instead of indoors",
        "The sample measured a gas rather than particulate matter",
        "The sample was taken at only one site rather than two",
        "The sample was reported in parts per billion rather than in grams"],
      ans=0,
      why="Ozone peaks in the afternoon and is higher in summer, so a single winter "
          "hour is drawn from exactly the conditions in which the framework expects "
          "the lowest values, and it cannot support a claim about summer. The units, "
          "the setting and the choice of pollutant are not the flaw."),

 dict(q="A resident reports stinging eyes and difficulty breathing on the hottest, "
        "sunniest afternoons of the summer and no symptoms on cool overcast days. Which "
        "explanation is most consistent with the framework?",
      choices=[
        "Photochemical smog forms under heat and sunlight and can cause eye irritation "
        "and respiratory problems",
        "Cool overcast days carry more pollen, which relieves irritation",
        "Heat alone causes the symptoms and no pollutant is involved",
        "The symptoms are caused by radon entering the home through the foundation",
        "The symptoms are caused by noise from summer traffic"],
      ans=0,
      why="Both the conditions and the symptoms are the ones the framework names for "
          "photochemical smog: formation under heat and sunlight, and harm including "
          "respiratory problems and eye irritation. Radon and noise are pollutants "
          "with different sources and different effects."),

 dict(q="Which pair of variables would best allow a student to describe the "
        "relationship the framework states between sunlight and smog?",
      choices=[
        "Hours of sunlight received and the ozone concentration measured that afternoon",
        "The number of residents in the city and the ozone concentration measured",
        "The price of gasoline and the number of vehicles registered",
        "The height of the tallest building and the daytime temperature",
        "The number of clinic visits and the number of vehicles registered"],
      ans=0,
      why="The framework attributes ozone production to reactions between oxygen and "
          "sunlight, so the pair that tests it is sunlight received against ozone "
          "measured. Population, fuel prices, building height and clinic visits each "
          "leave out one of the two variables in the stated relationship."),

 dict(q="Which statement best summarizes the causal chain the framework gives for "
        "photochemical smog in a large city?",
      choices=[
        "Vehicles release nitrogen oxides and volatile organic compounds, heat and "
        "sunlight drive reactions among them, and the resulting mixture irritates eyes "
        "and airways",
        "Vehicles release ozone, which cools in the afternoon and settles as a haze "
        "that stains buildings",
        "Sunlight destroys nitrogen oxides, and the products of that destruction are "
        "harmless to people",
        "Cold air traps carbon dioxide near the ground, and the carbon dioxide irritates "
        "the eyes",
        "Trees release nitrogen oxides that combine with rainwater to make an acid mist"],
      ans=0,
      why="Each link is one of the framework's own statements: the large number of "
          "motor vehicles in urban areas, the reaction of nitrogen oxides and volatile "
          "organic compounds with heat and sunlight, and the respiratory problems and "
          "eye irritation that follow. Every rejected chain contradicts at least one "
          "of those statements."),
]
