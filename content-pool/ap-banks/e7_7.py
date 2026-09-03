# AP ENVIRONMENTAL SCIENCE 7.7 Acid Rain
# CED effective Fall 2026, Unit 7 Atmospheric Pollution. Enduring understanding STB-2.
# Learning objectives STB-2.H, describe acid deposition, and STB-2.I, describe the
# effects of acid deposition on the environment. Suggested skill 4.B, identify a
# research method, design, and/or measure used.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-2.H.1  Acid rain and deposition is due to nitrogen oxides and sulfur oxides
#              from anthropogenic and natural sources in the atmosphere.
#   STB-2.H.2  Nitric oxides that cause acid deposition come from motor vehicles and
#              coal-burning power plants. Sulfur dioxides that cause acid deposition
#              come from coal-burning power plants.
#   STB-2.I.1  Acid deposition mainly affects communities that are downwind from
#              coal-burning power plants.
#   STB-2.I.2  Acid rain and deposition can lead to the acidification of soils and
#              bodies of water and corrosion of human-made structures.
#   STB-2.I.3  Regional differences in soils and bedrock affect the impact that acid
#              deposition has on the region -- such as limestone bedrock's ability to
#              neutralize the effect of acid rain on lakes and ponds.
#
# ON THE ONE MEASUREMENT CONVENTION USED. Several items report pH. The only thing
# presupposed about it is its direction: a lower pH is more acidic. The framework uses
# that convention itself in STB-4.H.1, where ocean acidification is defined as the
# DECREASE in pH of the oceans. No item asks for a pH value to be recalled, and every
# comparison is recomputed in verify_e7_7.py from the table in front of the student.
#
# ON SCOPE. Topic 7.1 keys the release of nitrogen oxides and their conversion to
# nitric acid; this topic keys the SOURCES the framework attaches to acid deposition,
# the downwind pattern, the three kinds of damage, and the buffering by bedrock. No
# item here re-asks how nitric acid forms.
#
# ON WHAT IS NOT KEYED. The framework names no region, no statute, no pH threshold and
# no species. Its statement about limestone is the only chemistry of neutralization it
# gives, and no key goes beyond it to a reaction or a formula.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("7.7", "Acid Rain", 7)

_T_DOWNWIND = dict(
    headers=["Sampling site relative to a coal-burning power plant",
             "Distance from the plant (kilometers)",
             "Average pH of rainfall"],
    rows=[["Downwind site 1", "20", "4.2"],
          ["Downwind site 2", "80", "4.6"],
          ["Downwind site 3", "200", "5.1"],
          ["Upwind site", "20", "5.6"]])

_T_BEDROCK = dict(
    headers=["Lake", "Bedrock of the surrounding basin",
             "Average pH of rainfall reaching the lake", "Average pH of the lake water"],
    rows=[["Lake W", "limestone", "4.4", "7.1"],
          ["Lake X", "limestone", "4.5", "6.9"],
          ["Lake Y", "granite", "4.4", "5.0"],
          ["Lake Z", "granite", "4.6", "5.2"]])

_T_STONE = dict(
    headers=["Solution the stone chips were soaked in for two weeks",
             "pH of the solution", "Mass lost by the chips (milligrams)"],
    rows=[["Solution 1", "3.0", "240"],
          ["Solution 2", "4.0", "95"],
          ["Solution 3", "5.0", "31"],
          ["Solution 4", "7.0", "2"]])

_T_SOURCES = dict(
    headers=["Region", "Coal-burning generating capacity (gigawatts)",
             "Motor vehicles registered (millions)",
             "Sulfur oxides released (thousand tons per year)",
             "Nitrogen oxides released (thousand tons per year)"],
    rows=[["Region 1", "12", "1", "410", "180"],
          ["Region 2", "1", "6", "40", "300"],
          ["Region 3", "0", "0.2", "5", "20"]])

_T_SOIL = dict(
    headers=["Forest plot", "Years of acid deposition recorded",
             "Soil pH at the start", "Soil pH at the end"],
    rows=[["Plot 1", "20", "5.8", "4.9"],
          ["Plot 2", "20", "5.6", "4.8"],
          ["Control plot sheltered from rainfall", "20", "5.7", "5.6"]])

_T_TREND = dict(
    headers=["Period", "Sulfur oxides released by regional power plants (thousand tons per year)",
             "Average pH of rainfall at a downwind station"],
    rows=[["Period 1", "900", "4.2"],
          ["Period 2", "600", "4.5"],
          ["Period 3", "300", "4.9"],
          ["Period 4", "120", "5.3"]])

QUESTIONS = [

 dict(q="Which substances does the framework identify as responsible for acid rain and "
        "acid deposition?",
      choices=[
        "Nitrogen oxides and sulfur oxides in the atmosphere",
        "Carbon dioxide and methane in the atmosphere",
        "Chlorofluorocarbons released from refrigeration equipment",
        "Radon and its decay products released from soil",
        "Ozone formed over cities on hot afternoons"],
      ans=0,
      why="The framework states that acid rain and deposition is due to nitrogen oxides "
          "and sulfur oxides from anthropogenic and natural sources in the atmosphere. "
          "The other substances are treated elsewhere in the course and are not given as "
          "the cause of acid deposition."),

 dict(q="According to the framework, where do the nitric oxides that cause acid "
        "deposition come from?",
      choices=[
        "Motor vehicles and coal-burning power plants",
        "Volcanic vents and hot springs only",
        "Fertilizer applied to farmland only",
        "The decay of uranium in bedrock",
        "Evaporation from oceans and lakes"],
      ans=0,
      why="The framework names motor vehicles and coal-burning power plants as the "
          "sources of the nitric oxides that cause acid deposition. It does not assign "
          "that role to volcanic vents alone, to fertilizer, to radioactive decay, or to "
          "evaporation."),

 dict(q="According to the framework, where do the sulfur dioxides that cause acid "
        "deposition come from?",
      choices=[
        "Coal-burning power plants",
        "Motor vehicle tailpipes",
        "Household refrigeration equipment",
        "The weathering of limestone bedrock",
        "Trees releasing volatile organic compounds"],
      ans=0,
      why="The framework attributes the sulfur dioxides that cause acid deposition to "
          "coal-burning power plants, while it attributes the nitric oxides to motor "
          "vehicles and coal plants together. Limestone appears in the framework as a "
          "neutralizer rather than a source."),

 dict(q="Which communities does the framework say acid deposition mainly affects?",
      choices=[
        "Communities downwind from coal-burning power plants",
        "Communities upwind from coal-burning power plants",
        "Communities directly above coal seams",
        "Communities on the coast regardless of wind direction",
        "Communities with no coal-burning power plants anywhere in the region"],
      ans=0,
      why="The framework states that acid deposition mainly affects communities that are "
          "downwind from coal-burning power plants, because the released oxides travel "
          "with the air away from the plant. Position over a coal seam or on a coast is "
          "not the pattern it gives."),

 dict(q="Rainfall measurements around one power plant are shown.",
      table=_T_DOWNWIND,
      choices=[
        "Rainfall is most acidic at the nearest downwind site and becomes less acidic "
        "with distance downwind, while the upwind site is the least acidic of all",
        "Rainfall is most acidic at the upwind site",
        "Rainfall acidity is the same at all four sites",
        "Rainfall becomes more acidic with distance downwind",
        "The upwind site and the nearest downwind site have the same acidity"],
      ans=0,
      why="The lowest pH, meaning the most acidic rainfall, is at the nearest downwind "
          "site, and the pH rises with distance downwind and is highest upwind. That is "
          "the downwind pattern the framework attaches to coal-burning power plants."),

 dict(q="Which three kinds of damage does the framework attribute to acid rain and "
        "deposition?",
      choices=[
        "Acidification of soils, acidification of bodies of water, and corrosion of "
        "human-made structures",
        "Depletion of stratospheric ozone, warming of the oceans, and sea level rise",
        "Hearing loss, eye irritation, and asphyxiation",
        "Loss of topsoil by wind erosion and the silting of rivers",
        "The formation of photochemical smog over cities"],
      ans=0,
      why="The framework states that acid rain and deposition can lead to the "
          "acidification of soils and bodies of water and the corrosion of human-made "
          "structures. The other lists belong to unit 9, to the health effects of other "
          "pollutants, or to land use."),

 dict(q="Four lakes receiving similarly acidic rainfall are compared.",
      table=_T_BEDROCK,
      choices=[
        "The lakes in limestone basins hold much less acidic water than the lakes in "
        "granite basins, although the rainfall reaching them is similarly acidic",
        "The lakes in granite basins hold the less acidic water",
        "All four lakes hold water of the same acidity",
        "The lake receiving the most acidic rainfall holds the least acidic water of the "
        "four",
        "The bedrock of the basin makes no difference to the lake water in these data"],
      ans=0,
      why="The two limestone lakes hold water well above the pH of the rainfall they "
          "receive, while the two granite lakes hold water close to it. The framework "
          "states that regional differences in soils and bedrock affect the impact of "
          "acid deposition, giving limestone's ability to neutralize as its example."),

 dict(q="What does the framework say about limestone bedrock and acid rain?",
      choices=[
        "Limestone bedrock can neutralize the effect of acid rain on lakes and ponds",
        "Limestone bedrock releases sulfur oxides that make acid rain worse",
        "Limestone bedrock prevents rain from reaching lakes and ponds",
        "Limestone bedrock has no effect on the acidity of lakes and ponds",
        "Limestone bedrock converts acid rain into nitrogen oxides"],
      ans=0,
      why="The framework gives limestone bedrock's ability to neutralize the effect of "
          "acid rain on lakes and ponds as its example of regional differences in soils "
          "and bedrock. It gives limestone no role as a source of the oxides and no "
          "effect on rainfall itself."),

 dict(q="Stone chips of the same kind are soaked in four solutions for two weeks.",
      table=_T_STONE,
      choices=[
        "The chips lost more mass in the more acidic solutions, with the greatest loss "
        "in the solution of lowest pH",
        "The chips lost more mass in the least acidic solutions",
        "The chips lost the same mass in all four solutions",
        "The chips gained mass in the most acidic solution",
        "The results show that acidity has no effect on stone"],
      ans=0,
      why="Ordering the solutions by pH puts the largest mass loss with the lowest pH "
          "and the smallest with the highest, so loss increases as acidity increases. "
          "The framework lists corrosion of human-made structures among the effects of "
          "acid deposition."),

 dict(q="Which measure would a researcher use to record how acidic rainfall is at a "
        "monitoring site?",
      choices=[
        "The pH of the collected rainwater",
        "The volume of rain that fell that day",
        "The temperature of the rainwater when collected",
        "The number of days on which rain fell that month",
        "The distance from the site to the nearest power plant"],
      ans=0,
      why="Acidity is what pH reports, so pH is the measure that answers the question "
          "asked. Volume, temperature, frequency of rainfall and distance to a source "
          "describe the sample or the setting rather than its acidity."),

 dict(q="Releases and rainfall acidity over four periods are shown.",
      table=_T_TREND,
      choices=[
        "As the sulfur oxides released fell, the rainfall at the downwind station became "
        "less acidic",
        "As the sulfur oxides released fell, the rainfall became more acidic",
        "The rainfall acidity did not change across the four periods",
        "The sulfur oxides released rose across the four periods",
        "The two measurements are unrelated in these data"],
      ans=0,
      why="The released sulfur oxides fall at every step of the record while the pH of "
          "the rainfall rises at every step, which is a fall in acidity. The framework "
          "attributes the sulfur oxides causing acid deposition to coal-burning power "
          "plants."),

 dict(q="Soil measurements from three forest plots are shown.",
      table=_T_SOIL,
      choices=[
        "Both plots exposed to rainfall became more acidic over the period, while the "
        "sheltered plot barely changed",
        "All three plots became more acidic by the same amount",
        "The sheltered plot became the most acidic of the three",
        "The exposed plots became less acidic over the period",
        "The measurements show that soil pH cannot change"],
      ans=0,
      why="The two exposed plots each fell by close to a full pH unit while the "
          "sheltered plot changed by a tenth, so the change tracks exposure to rainfall. "
          "The framework lists acidification of soils among the effects of acid "
          "deposition."),

 dict(q="A study compares the acidity of rainfall at sites arranged along the prevailing "
        "wind direction from a coal-burning power plant. Which aspect of the research "
        "design does the arrangement of sites represent?",
      choices=[
        "It varies distance and direction from a suspected source so that a pattern with "
        "position can be identified",
        "It holds distance and direction constant so that only the weather varies",
        "It measures the plant's fuel consumption rather than the rainfall",
        "It removes the need to measure pH at any site",
        "It ensures that every site receives exactly the same amount of rain"],
      ans=0,
      why="Suggested skill 4.B asks students to identify a research design. Placing "
          "sites at different distances along and against the wind is what allows a "
          "downwind pattern to be seen, which is the pattern the framework states for "
          "acid deposition."),

 dict(q="Emissions data for three regions are shown.",
      table=_T_SOURCES,
      choices=[
        "The region with the most coal-burning capacity releases the most sulfur oxides, "
        "while the region with the most vehicles releases the most nitrogen oxides",
        "The region with the most vehicles releases the most sulfur oxides",
        "The region with no coal-burning capacity releases the most of both oxides",
        "All three regions release the same amounts of both oxides",
        "The region with the most coal-burning capacity releases the most nitrogen "
        "oxides as well"],
      ans=0,
      why="The largest sulfur oxide figure belongs to the region with by far the most "
          "coal capacity and the largest nitrogen oxide figure to the region with the "
          "most vehicles. That matches the framework's assignment of sulfur dioxides to "
          "coal plants and nitric oxides to vehicles and coal plants."),

 dict(q="Two neighboring regions receive rainfall of the same acidity, but only one "
        "reports acidified lakes. Which explanation does the framework support?",
      choices=[
        "The regions differ in their soils and bedrock, and one region's bedrock can "
        "neutralize the acid reaching its lakes",
        "The regions differ in the amount of rain they receive, which changes the acidity "
        "of the rain",
        "One region's lakes are deeper, so acid cannot reach the water",
        "One region has no lakes, so no measurement was possible",
        "Acid deposition affects only regions upwind of a power plant"],
      ans=0,
      why="The framework states that regional differences in soils and bedrock affect "
          "the impact acid deposition has on a region, and gives limestone's "
          "neutralizing ability as its example. Rainfall amount, lake depth and upwind "
          "position are not what it names."),

 dict(q="Why does the framework describe acid deposition as arising from both "
        "anthropogenic and natural sources?",
      choices=[
        "Nitrogen oxides and sulfur oxides enter the atmosphere both from human "
        "activities and from processes that occur without them",
        "The acids themselves are manufactured and then released deliberately",
        "Rain is naturally acidic only when it falls on farmland",
        "The framework treats all air pollution as entirely human in origin",
        "Natural sources produce acids while human sources produce only particulates"],
      ans=0,
      why="The framework's own wording puts nitrogen oxides and sulfur oxides in the "
          "atmosphere from anthropogenic and natural sources. It does not describe acids "
          "being released ready-made, and it assigns particulates to human and natural "
          "sources alike elsewhere."),

 dict(q="A monument made of stone shows pitting and loss of detail in a region receiving "
        "acidic rainfall. Which framework statement does this observation illustrate?",
      choices=[
        "Acid deposition can lead to the corrosion of human-made structures",
        "Acid deposition can lead to the acidification of bodies of water",
        "Acid deposition mainly affects communities downwind of coal plants",
        "Nitric oxides that cause acid deposition come from motor vehicles",
        "Limestone bedrock can neutralize the effect of acid rain on lakes"],
      ans=0,
      why="The damaged object is a human-made structure, and corrosion of human-made "
          "structures is one of the three effects the framework lists. The other "
          "statements concern water, geography or sources rather than damage to a built "
          "object."),

 dict(q="Which comparison would best test whether a lake's acidity is being buffered by "
        "the bedrock of its basin?",
      choices=[
        "The pH of the rainfall entering the lake compared with the pH of the lake water "
        "itself",
        "The pH of the lake water compared with the air temperature above it",
        "The volume of the lake compared with the volume of a neighboring lake",
        "The number of streams flowing into the lake",
        "The pH of the rainfall compared with the pH of rainfall in another country"],
      ans=0,
      why="Buffering shows as a difference between what falls on the basin and what the "
          "water ends up at, so the two pH values are the comparison that reveals it. "
          "Temperature, volume, stream count and a distant rainfall reading leave that "
          "comparison unmade."),

 dict(q="A region cuts the sulfur oxide released by its coal-burning power plants by "
        "most of its former amount. Which outcome would the framework's statements lead "
        "a scientist to expect downwind?",
      choices=[
        "Less acidic rainfall downwind, since those plants are the source of the sulfur "
        "oxides that cause acid deposition there",
        "More acidic rainfall downwind, since the plants now release more nitrogen oxides",
        "No change downwind, since acid deposition has no relationship with released "
        "oxides",
        "A change upwind rather than downwind, since deposition mainly affects upwind "
        "communities",
        "Acidification of the lakes but not of the rainfall"],
      ans=0,
      why="The framework attributes the sulfur dioxides that cause acid deposition to "
          "coal-burning power plants and places the affected communities downwind of "
          "them, so cutting the release should reduce the acidity arriving downwind. "
          "Nothing in the framework makes a sulfur cut raise nitrogen oxides."),

 dict(q="Which of the following best explains why acid deposition can be a problem in a "
        "community that has no coal-burning power plant of its own?",
      choices=[
        "The oxides released by plants elsewhere travel through the atmosphere and are "
        "deposited downwind",
        "Acid deposition is produced inside homes by heating appliances",
        "Communities without power plants generate more traffic than others",
        "Acid rain forms only where there is no local source of pollution",
        "Rainfall is naturally acidic in communities without power plants"],
      ans=0,
      why="The framework locates the affected communities downwind of coal-burning power "
          "plants, which requires the pollution to travel from the plant to them. Local "
          "absence of a plant is therefore no protection."),

 dict(q="An investigator wants to know whether acid deposition is affecting a forest "
        "soil. Which measure is most directly relevant?",
      choices=[
        "The pH of the soil, measured over time at the same plots",
        "The height of the tallest tree in the forest",
        "The number of visitors to the forest each year",
        "The distance from the forest to the nearest city",
        "The average air temperature of the forest"],
      ans=0,
      why="Acidification of soils is one of the effects the framework names, and soil pH "
          "is the measure of that acidification. Tree height, visitor numbers, distance "
          "and temperature are not measures of soil acidity."),

 dict(q="Which of the following would be the strongest evidence that a particular power "
        "plant is contributing to the acidity of rainfall in a nearby valley?",
      choices=[
        "Rainfall is more acidic at valley sites downwind of the plant than at "
        "comparable sites upwind of it, measured over the same period",
        "The plant is the largest building in the region",
        "The valley receives more rain than the surrounding area",
        "Rainfall in the valley has been measured only once",
        "The plant burns the same fuel as plants in other regions"],
      ans=0,
      why="The framework's downwind pattern is what a paired downwind and upwind "
          "comparison tests, with the period held constant so the two are comparable. "
          "Building size, rainfall amount, a single measurement and fuel type elsewhere "
          "do not test it."),

 dict(q="Which statement best describes what the framework means by acid deposition as "
        "distinct from acid rain alone?",
      choices=[
        "Acid can reach surfaces by deposition as well as in falling rain, and both are "
        "attributed to the same oxides",
        "Deposition refers only to acid that falls on cities and rain only to acid that "
        "falls on farmland",
        "Deposition refers to acid released directly from a smokestack as a liquid",
        "Deposition and acid rain are caused by entirely different pollutants",
        "Deposition occurs only in regions with limestone bedrock"],
      ans=0,
      why="The framework treats acid rain and deposition together and attributes both to "
          "nitrogen oxides and sulfur oxides from anthropogenic and natural sources. It "
          "does not split them by land use, by bedrock, or by pollutant."),

 dict(q="A lake in a granite basin and a lake in a limestone basin receive rainfall of "
        "the same acidity. Which prediction follows from the framework?",
      choices=[
        "The lake in the limestone basin will be less affected, because limestone can "
        "neutralize the effect of the acid",
        "The lake in the granite basin will be less affected, because granite is harder "
        "than limestone",
        "The two lakes will be affected identically, because the rainfall is the same",
        "The lake in the limestone basin will become the more acidic of the two",
        "Neither lake will be affected, because bedrock prevents all acidification"],
      ans=0,
      why="The framework's stated example of regional differences is limestone bedrock's "
          "ability to neutralize the effect of acid rain on lakes and ponds, so the "
          "limestone basin is the one expected to be buffered. Hardness is not the "
          "property it names."),

 dict(q="Why is it useful to record the prevailing wind direction in a study of acid "
        "deposition around a power plant?",
      choices=[
        "The framework places the affected communities downwind of the plant, so wind "
        "direction identifies which sites should show the effect",
        "Wind direction determines the pH scale used for the measurements",
        "Wind direction changes the bedrock beneath the sampling sites",
        "Wind direction is the only measure of acidity available in the field",
        "Wind direction determines how much coal the plant burns"],
      ans=0,
      why="Suggested skill 4.B. Because the framework's pattern is a downwind one, "
          "knowing the wind direction is what tells the investigator which sites are "
          "expected to be affected and which serve as comparisons."),

 dict(q="A student claims that acid deposition affects every region equally because rain "
        "falls everywhere. Which framework statement most directly contradicts the claim?",
      choices=[
        "Regional differences in soils and bedrock affect the impact that acid "
        "deposition has on a region",
        "Acid rain and deposition is due to nitrogen oxides and sulfur oxides",
        "Sulfur dioxides that cause acid deposition come from coal-burning power plants",
        "Acid deposition can corrode human-made structures",
        "Nitric oxides come from motor vehicles as well as power plants"],
      ans=0,
      why="The claim is about uniformity across regions, and the framework's statement "
          "about regional differences in soils and bedrock, with limestone's "
          "neutralizing ability as the example, denies exactly that. The other "
          "statements concern sources or effects rather than regional variation."),

 dict(q="Which pair of sources does the framework connect to acid deposition through "
        "nitrogen oxides?",
      choices=[
        "Motor vehicles and coal-burning power plants",
        "Motor vehicles and household refrigerators",
        "Coal-burning power plants and limestone quarries",
        "Volcanic eruptions and municipal landfills",
        "Sewage treatment plants and farm irrigation"],
      ans=0,
      why="The framework states that the nitric oxides that cause acid deposition come "
          "from motor vehicles and coal-burning power plants. Refrigerators, quarries, "
          "landfills, treatment plants and irrigation are not given that role anywhere."),

 dict(q="A monitoring program reports the pH of rainfall at one site for a single storm "
        "and concludes that the region has an acid deposition problem. What is the "
        "clearest weakness?",
      choices=[
        "One storm at one site cannot show whether acidic rainfall is typical of the "
        "region",
        "The pH of rainfall cannot be measured during a storm",
        "The study should have measured the temperature of the rain instead",
        "The study should have been conducted upwind of every possible source",
        "Rainfall pH is unrelated to acid deposition"],
      ans=0,
      why="Suggested skill 4.B. A single sample at a single place has nothing to "
          "establish that the value is representative, which is what a claim about a "
          "region requires. The measure itself is the right one, and it can be taken "
          "during a storm."),

 dict(q="A community downwind of a coal-burning power plant reports acidified lakes, "
        "damaged building stone, and falling soil pH. How do these reports relate to the "
        "framework's statements?",
      choices=[
        "They correspond to the three effects the framework lists for acid deposition "
        "and to the downwind position it identifies",
        "They correspond to the effects of indoor air pollutants",
        "They correspond to the effects of thermal inversion trapping pollution",
        "They correspond to the effects of stratospheric ozone depletion",
        "They correspond to the effects of noise pollution on ecological systems"],
      ans=0,
      why="Acidified water, corroded structures and acidified soils are exactly the "
          "three effects the framework lists, and the community's downwind position is "
          "the pattern it gives. The other options belong to different topics with "
          "different effects."),

 dict(q="Which summary best captures the framework's account of acid deposition?",
      choices=[
        "Nitrogen oxides and sulfur oxides from human and natural sources produce acid "
        "deposition that mainly affects downwind communities, where it acidifies soils "
        "and water and corrodes structures, with the local bedrock affecting how severe "
        "the impact is",
        "Carbon dioxide from vehicles produces acid deposition that mainly affects "
        "upwind communities and has no effect on soils",
        "Acid deposition is a purely natural process that human activity does not "
        "influence",
        "Acid deposition affects only human-made structures and never the natural "
        "environment",
        "Acid deposition is caused by limestone bedrock releasing acid into lakes and "
        "ponds"],
      ans=0,
      why="Each clause of the keyed summary is one of the framework's statements: the "
          "oxides and their sources, the downwind communities, the three effects, and "
          "the regional differences in soils and bedrock. Every rejected summary "
          "contradicts at least one of them."),
]
