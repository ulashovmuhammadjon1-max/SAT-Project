# AP ENVIRONMENTAL SCIENCE 5.10 Impacts of Urbanization
# CED effective Fall 2026, Unit 5 Land and Water Use.
# Enduring understanding EIN-2: when humans use natural resources, they alter natural
# systems.
# Learning objective EIN-2.M, describe the effects of urbanization on the environment.
# Suggested skill 7.C, describe disadvantages, advantages, or unintended consequences
# for potential solutions.
#
# Essential knowledge relied on, in the framework's own words:
#   EIN-2.M.1  Urbanization can lead to depletion of resources and saltwater intrusion
#              in the hydrologic cycle.
#   EIN-2.M.2  Urbanization, through the burning of fossil fuels and landfills, affects
#              the carbon cycle by increasing the amount of carbon dioxide in the
#              atmosphere.
#   EIN-2.M.3  Impervious surfaces are human-made structures -- such as roads, buildings,
#              sidewalks, and parking lots -- that do not allow water to reach the soil,
#              leading to flooding.
#   EIN-2.M.4  Urban sprawl is the change in population distribution from high population
#              density areas to low density suburbs that spread into rural lands, leading
#              to potential environmental problems.
#
# SCOPE. Four statements, and nothing else. Two named effects in the hydrologic cycle,
# two named routes into the carbon cycle with one named direction of change, one
# definition with a four-item example list and one named consequence, and one definition
# of a population shift with a HEDGED consequence. The framework names no city, no
# country, no year and no figure, so every quantitative item here prints its data in a
# table and the arithmetic is recomputed in verify_e5_10.py from that table alone.
#
# THE WORD THAT MUST NOT BE STRENGTHENED. EIN-2.M.4 says sprawl leads to POTENTIAL
# environmental problems. One item turns on that hedge, and no key here says a named
# problem must follow from sprawl.
#
# THE DIRECTION THAT IS EASY TO INVERT. EIN-2.M.4 runs FROM high population density
# areas TO low density suburbs. The swap is the distractor a prepared student reaches
# for, so every anchor on that statement carries both ends of the movement.
#
# BOUNDARY WITH 5.13. Permeable pavement, planting trees, public transportation and
# building up rather than out are STB-1.B.1 in topic 5.13, the mitigation topic. This
# topic is the impact; the remedies appear here only as rejected options.
#
# NO FIGURES. Every quantitative item carries a table=; all arithmetic is recomputed in
# verify_e5_10.py from that table alone and is calculator-free.
# FIVE choices (A-E). No LaTeX: export_units.py does not typeset Environmental Science.
TOPIC = ("5.10", "Impacts of Urbanization", 5)

_T_COVER = dict(
    headers=["Catchment gauged",
             "Impervious cover (percent of the catchment)",
             "Rainfall that runs off the surface (percent)"],
    rows=[["Catchment 1", "5", "10"],
          ["Catchment 2", "20", "22"],
          ["Catchment 3", "45", "40"],
          ["Catchment 4", "80", "65"]])

_T_FLOOD = dict(
    headers=["Condition of the catchment",
             "Impervious cover (percent of the catchment)",
             "Peak stream flow after a storm of the same size "
             "(cubic meters per second)"],
    rows=[["Before development", "6", "12"],
          ["After development", "54", "48"]])

_T_SALT = dict(
    headers=["Year of the record",
             "Water pumped from the coastal aquifer (million cubic meters)",
             "Chloride in the town's well water (milligrams per litre)"],
    rows=[["Year 1", "10", "40"],
          ["Year 10", "25", "180"],
          ["Year 20", "40", "460"],
          ["Year 30", "55", "900"]])

_T_CARBON = dict(
    headers=["Source within the city boundary",
             "Carbon dioxide released in one year (thousand tonnes)"],
    rows=[["Burning of fossil fuels for transport, heating and power", "820"],
          ["Landfills serving the city", "160"],
          ["All other sources combined", "20"]])

_T_SPRAWL = dict(
    headers=["Part of the metropolitan area",
             "Population in the first year (thousands)",
             "Population thirty years later (thousands)",
             "People per square kilometer thirty years later"],
    rows=[["Central city", "600", "420", "5,200"],
          ["Outer suburbs on former farmland", "150", "540", "700"]])

_T_INFILT = dict(
    headers=["Surface of the plot",
             "Rain soaking into the soil in one hour (millimeters)",
             "Rain running off the surface in one hour (millimeters)"],
    rows=[["Grass over deep soil", "22", "3"],
          ["Gravel", "14", "11"],
          ["Asphalt paving", "1", "24"]])

QUESTIONS = [

 dict(q="What two effects does the course framework attach to urbanization within the "
        "hydrologic cycle?",
      choices=[
        "Depletion of resources and saltwater intrusion",
        "Replenishment of resources and the exclusion of saltwater from coastal aquifers",
        "Depletion of resources, but no change in the salinity of coastal groundwater",
        "Saltwater intrusion, but an increase in the resources available",
        "Neither depletion of resources nor any movement of saltwater"],
      ans=0,
      why="EIN-2.M.1 states that urbanization can lead to depletion of resources and saltwater "
          "intrusion in the hydrologic cycle. Each rejected option reverses one of the two "
          "effects, drops one, or denies both."),

 dict(q="Within which of Earth's cycles does the framework place the depletion of resources "
        "and the saltwater intrusion it attributes to urbanization?",
      choices=[
        "The hydrologic cycle",
        "The carbon cycle",
        "The nitrogen cycle",
        "The phosphorus cycle",
        "The rock cycle"],
      ans=0,
      why="EIN-2.M.1 places both effects in the hydrologic cycle by name. The framework's "
          "separate statement about urbanization and the carbon cycle, EIN-2.M.2, concerns "
          "carbon dioxide in the atmosphere rather than water."),

 dict(q="Through what two things does the framework say urbanization acts on the carbon "
        "cycle?",
      choices=[
        "The burning of fossil fuels and landfills",
        "The burning of fossil fuels and the paving over of soil",
        "Landfills and the pumping of coastal groundwater",
        "The construction of sidewalks and parking lots",
        "The spread of low density suburbs into rural land"],
      ans=0,
      why="EIN-2.M.2 states that urbanization, THROUGH THE BURNING OF FOSSIL FUELS AND "
          "LANDFILLS, affects the carbon cycle. The rejected options substitute the impervious "
          "surfaces of EIN-2.M.3 or the sprawl of EIN-2.M.4 for one or both of the two named "
          "routes."),

 dict(q="What does the framework say that action on the carbon cycle amounts to?",
      choices=[
        "An increase in the amount of carbon dioxide in the atmosphere",
        "A decrease in the amount of carbon dioxide in the atmosphere",
        "An increase in the amount of methane in the atmosphere",
        "An increase in the amount of nitrous oxide in the atmosphere",
        "No net change in the composition of the atmosphere"],
      ans=0,
      why="EIN-2.M.2 states that urbanization affects the carbon cycle BY INCREASING THE AMOUNT "
          "OF CARBON DIOXIDE IN THE ATMOSPHERE. The framework names carbon dioxide here, not "
          "methane or nitrous oxide, and the direction it gives is an increase."),

 dict(q="How does the framework define an impervious surface?",
      choices=[
        "Human-made structures that do not allow water to reach the soil",
        "Natural outcrops of bare rock that shed water without absorbing it",
        "Human-made structures that allow water to pass through into the soil below",
        "Soil compacted by grazing animals until water can no longer enter it",
        "Any surface, natural or built, that is kept clear of vegetation"],
      ans=0,
      why="EIN-2.M.3 defines impervious surfaces as HUMAN-MADE structures that DO NOT ALLOW "
          "WATER TO REACH THE SOIL. The rejected options make them natural, reverse what they "
          "do to water, or widen the definition past what the framework states."),

 dict(q="Which set of examples does the framework give for impervious surfaces?",
      choices=[
        "Roads, buildings, sidewalks, and parking lots",
        "Wetlands, floodplains, riverbanks, and stream beds",
        "Forests, grasslands, croplands, and orchards",
        "Roads, buildings, wetlands, and floodplains",
        "Sand dunes, gravel bars, mudflats, and salt marshes"],
      ans=0,
      why="EIN-2.M.3 gives roads, buildings, sidewalks and parking lots as its examples. Every "
          "rejected list contains at least one natural surface, which cannot satisfy the "
          "framework's requirement that the structure be human-made."),

 dict(q="What consequence does the framework attach directly to impervious surfaces?",
      choices=[
        "Flooding, because the water cannot reach the soil",
        "Drought, because the water is held in the soil for longer",
        "Saltwater intrusion, because the coastal water table rises",
        "Waterlogging of the soil lying beneath the pavement",
        "A rise in the amount of water soaking into the ground"],
      ans=0,
      why="EIN-2.M.3 ends by stating that impervious surfaces do not allow water to reach the "
          "soil, LEADING TO FLOODING. Saltwater intrusion belongs to EIN-2.M.1 and waterlogging "
          "to EIN-2.F.1 in the irrigation topic."),

 dict(q="How does the framework define urban sprawl?",
      choices=[
        "A change in population distribution from high population density areas to low "
        "density suburbs that spread into rural lands",
        "A change in population distribution from low density suburbs to high population "
        "density central areas",
        "An increase in a city's population with no change in the area the city covers",
        "The abandonment of farmland as its rural population is replaced by wildlife",
        "The concentration of a whole region's population into one dense settlement"],
      ans=0,
      why="EIN-2.M.4 defines urban sprawl as the change in population distribution FROM high "
          "population density areas TO low density suburbs that spread into rural lands. The "
          "first rejected option is that movement run backwards, which is the error the "
          "definition most often invites."),

 dict(q="Over thirty years a metropolitan area's central neighbourhoods lose population while "
        "new low density housing spreads outward across former farmland. Which framework term "
        "names this pattern?",
      choices=[
        "Urban sprawl",
        "Saltwater intrusion",
        "Sustainable yield",
        "Rotational grazing",
        "Clearcutting"],
      ans=0,
      why="EIN-2.M.4 defines urban sprawl as exactly this change in population distribution, "
          "from high density areas to low density suburbs spreading into rural lands. Saltwater "
          "intrusion is EIN-2.M.1, sustainable yield STB-1.A.2, rotational grazing STB-1.E.3 "
          "and clearcutting EIN-2.C."),

 dict(q="Four catchments of the same size and rainfall differ in how much of their surface is "
        "paved or built on. What do the values show?",
      table=_T_COVER,
      choices=[
        "As the share of the catchment covered by impervious surfaces rises, the share of "
        "rainfall that runs off the surface rises.",
        "As the share of the catchment covered by impervious surfaces rises, the share of "
        "rainfall that runs off the surface falls.",
        "The share of rainfall that runs off is the same in all four catchments.",
        "The catchment with the least impervious cover sheds the most rainfall as runoff.",
        "The share of rainfall running off depends on the catchment's area rather than on "
        "its impervious cover."],
      ans=0,
      why="Impervious cover runs 5, 20, 45 and 80 percent while runoff runs 10, 22, 40 and 65 "
          "percent, rising together without exception. EIN-2.M.3 states that impervious "
          "surfaces do not allow water to reach the soil, leading to flooding."),

 dict(q="Using the same four catchments, how much greater is the share of rainfall running off "
        "the most heavily paved catchment than the share running off the least paved one?",
      table=_T_COVER,
      choices=[
        "55 percentage points greater",
        "65 percentage points greater",
        "75 percentage points greater",
        "43 percentage points greater",
        "10 percentage points greater"],
      ans=0,
      why="Subtracting the two tabulated shares gives 65 minus 10, which is 55 percentage "
          "points. The rejected values quote the heaviest catchment alone, add the two, take "
          "the difference in impervious cover, or quote the lightest catchment alone."),

 dict(q="One stream was gauged after storms of the same size before and after its catchment "
        "was built over. Which conclusion do the values support?",
      table=_T_FLOOD,
      choices=[
        "Building over the catchment raised the peak flow after an identical storm several "
        "times over.",
        "Building over the catchment lowered the peak flow after an identical storm.",
        "The peak flow after an identical storm was unchanged by the development.",
        "The peak flow rose because the storms after development were larger than those "
        "before it.",
        "The impervious cover of the catchment fell as the development proceeded."],
      ans=0,
      why="Impervious cover rose from 6 to 54 percent and the peak flow from 12 to 48 cubic "
          "meters per second for a storm of the same size, so the storm cannot explain the "
          "rise. EIN-2.M.3 attaches flooding to surfaces that do not let water reach the soil."),

 dict(q="Using the same stream, how large was the peak flow after development compared with "
        "the peak flow before it?",
      table=_T_FLOOD,
      choices=[
        "Four times as large",
        "Two times as large",
        "Three times as large",
        "Nine times as large",
        "About the same size"],
      ans=0,
      why="Dividing the two tabulated peak flows gives 48 divided by 12, which is 4. The "
          "rejected values come from halving rather than dividing, from the impervious cover "
          "column, or from denying that the two differ."),

 dict(q="A coastal town's records of groundwater pumping and well water quality are given in "
        "the table. Which conclusion is best supported?",
      table=_T_SALT,
      choices=[
        "As more water was pumped from the coastal aquifer, the chloride in the well water "
        "rose, which is the pattern saltwater intrusion produces.",
        "As more water was pumped from the coastal aquifer, the chloride in the well water "
        "fell, which is the pattern saltwater intrusion produces.",
        "The chloride in the well water did not change as the pumping increased.",
        "The chloride rose while the pumping fell, so the two records are unrelated.",
        "Chloride in well water cannot show whether seawater has entered an aquifer."],
      ans=0,
      why="Pumping runs 10, 25, 40 and 55 million cubic meters while chloride runs 40, 180, 460 "
          "and 900 milligrams per litre, rising together. EIN-2.M.1 states that urbanization can "
          "lead to depletion of resources and saltwater intrusion in the hydrologic cycle, and "
          "chloride is the salt in seawater."),

 dict(q="Using the same coastal records, by how much did the chloride in the well water rise "
        "between the first year and the thirtieth?",
      table=_T_SALT,
      choices=[
        "860 milligrams per litre higher",
        "900 milligrams per litre higher",
        "940 milligrams per litre higher",
        "460 milligrams per litre higher",
        "540 milligrams per litre higher"],
      ans=0,
      why="Subtracting the two tabulated concentrations gives 900 minus 40, which is 860 "
          "milligrams per litre. The rejected values quote the final reading alone, add the "
          "two, or take a reading from the middle of the record."),

 dict(q="A city totalled the carbon dioxide released within its boundary in one year by "
        "source. Which reading matches the framework's account of urbanization and the "
        "carbon cycle?",
      table=_T_CARBON,
      choices=[
        "The burning of fossil fuels and the landfills together account for nearly all of "
        "the release, and those are the two routes the framework names.",
        "The landfills alone account for nearly all of the release, and landfills are the "
        "only route the framework names.",
        "Sources other than fossil fuel burning and landfills account for nearly all of "
        "the release.",
        "The burning of fossil fuels accounts for none of the release.",
        "The three sources release carbon dioxide in about equal amounts."],
      ans=0,
      why="The tabulated masses are 820, 160 and 20 thousand tonnes, so the two routes the "
          "framework names supply 980 of the 1,000 thousand tonnes. EIN-2.M.2 names the burning "
          "of fossil fuels AND landfills as the routes by which urbanization raises atmospheric "
          "carbon dioxide."),

 dict(q="Using the same city totals, what share of the year's carbon dioxide came from the "
        "two routes the framework names?",
      table=_T_CARBON,
      choices=[
        "98 percent",
        "82 percent",
        "16 percent",
        "84 percent",
        "50 percent"],
      ans=0,
      why="Adding 820 and 160 gives 980 of a total of 1,000 thousand tonnes, which is 98 "
          "percent. The rejected values quote the fossil fuel share alone, the landfill share "
          "alone, the fossil fuel share with the unnamed sources instead of the landfills, or "
          "an even split."),

 dict(q="A metropolitan area's population was recorded in two parts thirty years apart. Which "
        "framework statement do the values illustrate?",
      table=_T_SPRAWL,
      choices=[
        "Urban sprawl, because population moved from the dense centre out to low density "
        "suburbs spreading over former farmland.",
        "Urban sprawl, because population moved from the low density suburbs in to the "
        "dense centre.",
        "Saltwater intrusion, because a coastal aquifer was drawn down.",
        "The effect of impervious surfaces on flooding, because more rainfall ran off.",
        "The framework describes no pattern that these values could illustrate."],
      ans=0,
      why="The central city falls from 600 to 420 thousand while the outer suburbs rise from "
          "150 to 540 thousand, and the suburbs hold 700 people per square kilometer against "
          "the centre's 5,200. EIN-2.M.4 defines urban sprawl as exactly that movement from "
          "high density areas to low density suburbs spreading into rural lands."),

 dict(q="Using the same two parts of the metropolitan area, how much population did the outer "
        "suburbs gain across the thirty years?",
      table=_T_SPRAWL,
      choices=[
        "390 thousand people",
        "180 thousand people",
        "540 thousand people",
        "210 thousand people",
        "120 thousand people"],
      ans=0,
      why="Subtracting the two tabulated suburban populations gives 540 minus 150, which is 390 "
          "thousand. The rejected values give the loss from the centre, the final suburban "
          "total alone, the net change across both parts, or neither."),

 dict(q="Which of the following correctly distinguishes impervious surfaces from urban "
        "sprawl?",
      choices=[
        "Impervious surfaces are built structures that keep water from the soil; urban "
        "sprawl is a movement of population from dense areas out to low density suburbs.",
        "Urban sprawl is a built structure that keeps water from the soil; impervious "
        "surfaces are a movement of population from dense areas out to low density suburbs.",
        "Both terms name built structures that keep water from reaching the soil.",
        "Both terms name a movement of population from dense areas out to low density "
        "suburbs.",
        "Impervious surfaces occur only in rural land and urban sprawl only in city "
        "centres."],
      ans=0,
      why="EIN-2.M.3 defines impervious surfaces as human-made structures that do not allow "
          "water to reach the soil, while EIN-2.M.4 defines urban sprawl as a change in "
          "population distribution. One is a surface and the other a movement of people, and "
          "the exact swap of the two is the error worth guarding against."),

 dict(q="A student writes that the framework treats urbanization as affecting the carbon cycle "
        "and nothing else. Which correction is required?",
      choices=[
        "The framework also places depletion of resources and saltwater intrusion in the "
        "hydrologic cycle.",
        "The framework mentions the hydrologic cycle but attributes no effect on it to "
        "urbanization.",
        "The framework treats urbanization as affecting the nitrogen cycle rather than the "
        "carbon cycle.",
        "The framework says urbanization removes carbon dioxide from the atmosphere.",
        "The framework attributes no effect on any of Earth's cycles to urbanization."],
      ans=0,
      why="EIN-2.M.1 assigns urbanization two effects in the hydrologic cycle, and EIN-2.M.2 "
          "assigns it one in the carbon cycle, so the framework names both. The rejected "
          "options deny a statement the framework makes or reverse its direction."),

 dict(q="Which observation would most directly support a claim that a coastal city is "
        "experiencing the second effect EIN-2.M.1 names?",
      choices=[
        "Wells near the coast growing steadily saltier as withdrawals from the aquifer "
        "increase",
        "Wells near the coast growing steadily fresher as withdrawals from the aquifer "
        "increase",
        "Rainfall over the city rising from one decade to the next",
        "The number of parking lots in the city increasing each year",
        "The city's landfills releasing more gas each year than they did before"],
      ans=0,
      why="EIN-2.M.1 names saltwater intrusion, so the evidence is salt appearing in fresh "
          "groundwater as it is drawn down. Rainfall says nothing about salt, and parking lots "
          "and landfills belong to EIN-2.M.3 and EIN-2.M.2 respectively."),

 dict(q="Which pair of measurements would together best test the consequence the framework "
        "attaches to impervious surfaces?",
      choices=[
        "The share of a catchment covered by pavement and buildings, and the peak stream "
        "flow after a storm",
        "The share of a catchment covered by pavement and buildings, and the number of "
        "people living in it",
        "The peak stream flow after a storm, and the distance from the catchment to the "
        "nearest coast",
        "The chloride in the city's wells, and the number of landfills serving the city",
        "The area of rural land built over, and the carbon dioxide released by the city's "
        "traffic"],
      ans=0,
      why="EIN-2.M.3 claims that impervious surfaces keep water from the soil and thereby lead "
          "to flooding, so the test needs a measure of the surface and a measure of the flood "
          "response. Each rejected pair supplies at most one of the two, or tests a different "
          "statement altogether."),

 dict(q="A city proposes to pave a large area of ground that now absorbs rainfall. Which "
        "framework statement most directly predicts the consequence?",
      choices=[
        "Impervious surfaces do not allow water to reach the soil, leading to flooding.",
        "Urban sprawl is the change in population distribution from high density areas to "
        "low density suburbs.",
        "Urbanization affects the carbon cycle by increasing atmospheric carbon dioxide.",
        "Urbanization can lead to saltwater intrusion in the hydrologic cycle.",
        "Sustainable yield is the amount of a renewable resource that can be taken without "
        "reducing the supply."],
      ans=0,
      why="Paving ground that now absorbs rainfall creates exactly the human-made surface "
          "EIN-2.M.3 describes, and the statement's own consequence is flooding. The other "
          "statements are the framework's, but none of them is about a surface."),

 dict(q="The same rainfall was applied to three plots differing only in their ground surface, "
        "and what soaked in and what ran off were measured. What do the values show?",
      table=_T_INFILT,
      choices=[
        "Almost none of the rain reaches the soil under the asphalt, and almost all of it "
        "runs off.",
        "Almost all of the rain reaches the soil under the asphalt, and almost none of it "
        "runs off.",
        "The three surfaces let the same depth of rain reach the soil.",
        "The grass plot sheds more rain as runoff than the asphalt plot does.",
        "Rain that runs off a surface has also soaked into the soil beneath it."],
      ans=0,
      why="Under asphalt 1 millimeter soaks in and 24 run off, against 22 and 3 under grass. "
          "EIN-2.M.3 defines an impervious surface as one that does not allow water to reach "
          "the soil, and asphalt paving behaves that way here."),

 dict(q="Using the same three plots, how much more rain ran off the asphalt in the hour than "
        "ran off the grass?",
      table=_T_INFILT,
      choices=[
        "21 millimeters more",
        "24 millimeters more",
        "27 millimeters more",
        "11 millimeters more",
        "3 millimeters more"],
      ans=0,
      why="Subtracting the two tabulated runoff depths gives 24 minus 3, which is 21 "
          "millimeters. The rejected values quote the asphalt alone, add the two, take the "
          "gravel reading, or quote the grass alone."),

 dict(q="Which of the following would NOT count as an impervious surface as the framework "
        "defines the term?",
      choices=[
        "A meadow of deep soil under grass",
        "A supermarket parking lot",
        "A concrete sidewalk",
        "The roof of a building",
        "An asphalt road"],
      ans=0,
      why="EIN-2.M.3 requires the surface to be a HUMAN-MADE structure that does not allow "
          "water to reach the soil, and names roads, buildings, sidewalks and parking lots. A "
          "meadow is neither human-made nor a barrier to infiltration."),

 dict(q="The framework says urban sprawl leads to POTENTIAL environmental problems. What does "
        "that wording establish about the claim?",
      choices=[
        "It names sprawl as a source of possible problems without asserting that any "
        "particular problem must follow",
        "It asserts that every case of sprawl produces the same set of problems",
        "It denies that sprawl has any environmental consequences at all",
        "It confines the problems of sprawl to the hydrologic cycle",
        "It states that the problems are certain and only their timing is unknown"],
      ans=0,
      why="EIN-2.M.4 hedges with the word potential, so the framework asserts a risk rather "
          "than a list of certain outcomes. Reading the statement as a guarantee, or as a "
          "denial, both go past what it says."),

 dict(q="Which statement correctly relates the four essential knowledge statements of this "
        "topic to one another?",
      choices=[
        "One names two effects in the water cycle, one an effect on the carbon cycle, one a "
        "kind of surface and the flooding it causes, and one a change in where people live.",
        "All four name effects within the water cycle.",
        "All four name effects on the carbon cycle.",
        "Three of them name kinds of surface and the fourth names a fuel.",
        "The four describe four separate cities and cannot be applied to one place "
        "together."],
      ans=0,
      why="EIN-2.M.1 is the hydrologic pair, EIN-2.M.2 the carbon dioxide increase, EIN-2.M.3 "
          "impervious surfaces and flooding, and EIN-2.M.4 the population shift. They are four "
          "different kinds of effect, and one city can show all four at once."),

 dict(q="Which summary states this topic as the framework does, without adding to it?",
      choices=[
        "Urbanization depletes resources and brings saltwater intrusion in the water cycle, "
        "raises atmospheric carbon dioxide through fossil fuel burning and landfills, "
        "spreads impervious surfaces that keep water from the soil and cause flooding, and "
        "shifts population outward into rural land.",
        "Urbanization replenishes resources and keeps saltwater out of coastal aquifers, "
        "and lowers atmospheric carbon dioxide.",
        "Urbanization affects only the carbon cycle, and impervious surfaces help rainfall "
        "reach the soil.",
        "Urbanization moves population from low density suburbs into dense city centres and "
        "leaves rural land untouched.",
        "Urbanization has no measurable effect on water, on the atmosphere or on where "
        "people live."],
      ans=0,
      why="The keyed summary carries EIN-2.M.1's two hydrologic effects, EIN-2.M.2's route and "
          "direction, EIN-2.M.3's definition and consequence, and EIN-2.M.4's movement of "
          "population. Each rejected summary reverses a direction or drops a whole statement."),
]
