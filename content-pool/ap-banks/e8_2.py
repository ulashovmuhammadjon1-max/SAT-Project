# AP ENVIRONMENTAL SCIENCE 8.2 Human Impacts on Ecosystems
# CED effective Fall 2026, Unit 8 Aquatic and Terrestrial Pollution. Enduring
# understanding STB-3. Learning objective STB-3.B: describe the impacts of human
# activities on aquatic ecosystems. Suggested skill 6.B, apply appropriate mathematical
# relationships to solve a problem, with work shown.
#
# Essential knowledge relied on, in the framework's own words:
#   STB-3.B.1   Organisms have a range of tolerance for various pollutants. Organisms
#               have an optimum range for each factor where they can maintain
#               homeostasis. Outside of this range, organisms may experience
#               physiological stress, limited growth, reduced reproduction, and in
#               extreme cases, death.
#   STB-3.B.2   Coral reefs have been suffering damage due to a variety of factors,
#               including increasing ocean temperature, sediment runoff, and
#               destructive fishing practices.
#   STB-3.B.3   Oil spills in marine waters cause organisms to die from the
#               hydrocarbons in oil. Oil that floats on the surface of water can coat
#               the feathers of birds and fur of marine mammals. Some components of oil
#               sink to the ocean floor, killing some bottom-dwelling organisms.
#   STB-3.B.4   Oil that washes up on the beach can have economic consequences on the
#               fishing and tourism industries.
#   STB-3.B.5   Oceanic dead zones are areas of low oxygen in the world's oceans caused
#               by increased nutrient pollution.
#   STB-3.B.6   An oxygen sag curve is a plot of dissolved oxygen levels versus the
#               distance from a source of pollution, usually excess nutrients and
#               biological refuse.
#   STB-3.B.7   Heavy metals used for industry, especially mining and burning of fossil
#               fuels, can reach the groundwater, impacting the drinking water supply.
#   STB-3.B.8   Litter that reaches aquatic ecosystems, besides being unsightly, can
#               create intestinal blockage and choking hazards for wildlife and
#               introduce toxic substances to the food chain.
#   STB-3.B.9   Increased sediment in waterways can reduce light infiltration, which can
#               affect primary producers and visual predators. Sediment can also settle,
#               disrupting habitats.
#   STB-3.B.10  When elemental sources of mercury enter aquatic environments, bacteria
#               in the water convert it to highly toxic methylmercury.
#
# ON SCOPE. The eutrophication mechanism itself belongs to 8.5, thermal pollution to
# 8.6, biomagnification to 8.8 and coral bleaching by warming to 9.6. This topic keys
# the framework's own statements above: the dead zone is keyed as an area of low oxygen
# caused by nutrient pollution, not by the algal-decomposition sequence of STB-3.F.2,
# and mercury is keyed as far as its conversion to methylmercury, not up the food chain.
#
# ON THE ARITHMETIC. Suggested skill 6.B is a mathematical routine, so several items
# are quantitative. Every one of them carries its numbers in a table, is answerable in
# one or two steps without a calculator, and is recomputed in verify_e8_2.py from that
# table alone.
#
# FIVE choices (A-E). No LaTeX and no non-ASCII.
TOPIC = ("8.2", "Human Impacts on Ecosystems", 8)

_T_TOLERANCE = dict(
    headers=["Concentration of a pollutant in the tank (milligrams per liter)",
             "Fish surviving after 30 days (out of 40)",
             "Eggs laid per surviving female"],
    rows=[["0.0", "39", "620"],
          ["0.5", "38", "590"],
          ["2.0", "31", "240"],
          ["5.0", "12", "40"],
          ["10.0", "0", "0"]])

_T_SAG = dict(
    headers=["Distance downstream from the outfall (kilometers)",
             "Dissolved oxygen (milligrams per liter)"],
    rows=[["0", "8.2"],
          ["2", "4.1"],
          ["5", "1.6"],
          ["12", "4.4"],
          ["25", "7.9"]])

_T_DEADZONE = dict(
    headers=["Year", "Nitrogen carried down the river in spring (thousand tons)",
             "Area of the low-oxygen zone that summer (square kilometers)"],
    rows=[["Year 1", "60", "4,000"],
          ["Year 2", "95", "9,000"],
          ["Year 3", "140", "16,000"],
          ["Year 4", "45", "3,000"]])

_T_LIGHT = dict(
    headers=["Suspended sediment (milligrams per liter)",
             "Depth reached by 1 percent of surface light (meters)",
             "Algal growth measured on plates at 3 meters (milligrams per day)"],
    rows=[["5", "9.0", "18"],
          ["25", "4.5", "11"],
          ["60", "2.0", "4"],
          ["120", "0.8", "1"]])

_T_SPILL = dict(
    headers=["Quantity recorded for one spill", "Value"],
    rows=[["Volume of oil released (barrels)", "4,000"],
          ["Volume of one barrel (liters)", "160"],
          ["Area of the slick after two days (square kilometers)", "80"]])

_T_LOAD = dict(
    headers=["Quantity recorded for one river", "Value"],
    rows=[["Water flowing past the town each day (million liters)", "200"],
          ["Dissolved metal concentration (milligrams per liter)", "3"]])

_T_MERCURY = dict(
    headers=["Sampling site", "Distance from the abandoned mine (kilometers)",
             "Mercury in the water (nanograms per liter)",
             "Methylmercury in the water (nanograms per liter)"],
    rows=[["Site 1", "1", "48", "6.0"],
          ["Site 2", "6", "26", "3.1"],
          ["Site 3", "20", "9", "1.0"],
          ["Reference site on another stream", "40", "2", "0.2"]])

_T_REEF = dict(
    headers=["Reef section", "Sediment reaching the reef (grams per square meter per day)",
             "Live coral cover (percent)"],
    rows=[["Section 1", "2", "56"],
          ["Section 2", "9", "38"],
          ["Section 3", "21", "19"],
          ["Section 4", "40", "7"]])

QUESTIONS = [

 dict(q="What does the framework mean when it says organisms have a range of tolerance "
        "for a pollutant?",
      choices=[
        "There is an optimum range in which the organism can maintain homeostasis, and "
        "outside it the organism may suffer stress, limited growth, reduced reproduction "
        "or death",
        "The organism is unaffected by the pollutant at any concentration",
        "The organism dies immediately at any concentration above zero",
        "The organism can tolerate every pollutant equally well",
        "The organism's tolerance is fixed by the season rather than by the pollutant"],
      ans=0,
      why="The framework describes an optimum range for each factor where homeostasis "
          "can be maintained, and lists physiological stress, limited growth, reduced "
          "reproduction and, in extreme cases, death for conditions outside it. Neither "
          "complete immunity nor immediate death at any exposure is what it states."),

 dict(q="Results from a controlled exposure study are shown.",
      table=_T_TOLERANCE,
      choices=[
        "Survival and egg production both stay near their highest values at the lowest "
        "concentrations and fall as the concentration rises, reaching zero at the "
        "highest concentration",
        "Survival falls as the concentration rises but egg production is unaffected",
        "Both survival and egg production rise as the concentration rises",
        "Neither survival nor egg production changes across the concentrations tested",
        "Egg production is highest at the highest concentration tested"],
      ans=0,
      why="Both columns decrease as the concentration increases and both reach zero in "
          "the strongest treatment. Reduced reproduction and death outside the range of "
          "tolerance are two of the outcomes the framework names."),

 dict(q="Which factors does the framework name as damaging coral reefs?",
      choices=[
        "Increasing ocean temperature, sediment runoff, and destructive fishing practices",
        "Falling ocean temperature and rising dissolved oxygen",
        "Excess sunlight and low salinity only",
        "Noise from shipping and light from coastal cities",
        "Volcanic ash settling on the reef surface"],
      ans=0,
      why="Those three are the factors the framework lists for reef damage. Cooling "
          "water, rising oxygen, and the remaining options are not among the causes it "
          "names in this statement."),

 dict(q="Measurements across four sections of one reef are shown.",
      table=_T_REEF,
      choices=[
        "Live coral cover falls as the sediment reaching the reef rises",
        "Live coral cover rises as the sediment reaching the reef rises",
        "Live coral cover is the same in all four sections",
        "The section receiving the most sediment holds the most live coral",
        "Sediment and coral cover are unrelated in these data"],
      ans=0,
      why="Ordering the sections by sediment delivery puts the coral cover in "
          "decreasing order, so the two move in opposite directions. Sediment runoff is "
          "one of the factors the framework names as damaging coral reefs."),

 dict(q="How does the framework describe the harm oil spills do to organisms in marine "
        "waters?",
      choices=[
        "Organisms die from the hydrocarbons in the oil, floating oil coats the feathers "
        "of birds and the fur of marine mammals, and sinking components kill some "
        "bottom-dwelling organisms",
        "The oil raises the temperature of the water until organisms die of heat",
        "The oil dissolves completely and has no effect on any organism",
        "The oil is consumed by fish as food and improves their growth",
        "The oil affects only organisms living on the shoreline"],
      ans=0,
      why="The framework gives all three of those effects: death from the hydrocarbons, "
          "coating of feathers and fur by floating oil, and the killing of bottom "
          "dwellers by components that sink. None of the rejected descriptions appears "
          "in it."),

 dict(q="Records from one spill are shown.",
      table=_T_SPILL,
      choices=[
        "The spill released 640,000 liters of oil",
        "The spill released 64,000 liters of oil",
        "The spill released 6,400,000 liters of oil",
        "The spill released 4,160 liters of oil",
        "The volume released cannot be found from these records"],
      ans=0,
      why="Multiplying the number of barrels by the volume of one barrel gives the "
          "volume released, which is four thousand times one hundred and sixty. The two "
          "rejected magnitudes differ from that product by a factor of ten and the "
          "fourth adds the two quantities instead of multiplying them."),

 dict(q="What economic consequences does the framework attach to oil that washes up on a "
        "beach?",
      choices=[
        "Consequences for the fishing and tourism industries",
        "Consequences for the mining and forestry industries",
        "Consequences for the electricity generating industry only",
        "No economic consequences, since the oil is on land rather than in water",
        "Consequences for agriculture through reduced rainfall"],
      ans=0,
      why="The framework states that oil washing up on the beach can have economic "
          "consequences on the fishing and tourism industries. It attaches no such "
          "consequence to mining, forestry, electricity generation or rainfall."),

 dict(q="What does the framework say an oceanic dead zone is?",
      choices=[
        "An area of low oxygen in the world's oceans caused by increased nutrient "
        "pollution",
        "An area of the ocean where no sunlight reaches because of depth",
        "An area of the ocean that has been closed to fishing by law",
        "An area of the ocean covered by a floating oil slick",
        "An area of the ocean where the water is too cold for any organism"],
      ans=0,
      why="The framework defines oceanic dead zones as areas of low oxygen in the "
          "world's oceans caused by increased nutrient pollution. Depth, legal closure, "
          "oil cover and temperature are not what the definition names."),

 dict(q="River nitrogen and low-oxygen zone area are recorded for four years.",
      table=_T_DEADZONE,
      choices=[
        "The area of the low-oxygen zone was largest in the year the river carried the "
        "most nitrogen and smallest in the year it carried the least",
        "The area of the low-oxygen zone was largest in the year the river carried the "
        "least nitrogen",
        "The area of the low-oxygen zone was the same in all four years",
        "The area of the low-oxygen zone fell as the nitrogen load rose",
        "Nitrogen load and zone area are unrelated in these data"],
      ans=0,
      why="Ranking the years by nitrogen carried gives the same order as ranking them by "
          "zone area, so the largest and smallest of each fall in the same years. The "
          "framework attributes oceanic dead zones to increased nutrient pollution."),

 dict(q="What is an oxygen sag curve, as the framework defines it?",
      choices=[
        "A plot of dissolved oxygen levels against distance from a source of pollution",
        "A plot of water temperature against depth in a lake",
        "A plot of the number of fish caught against the year",
        "A plot of nutrient concentration against the time of day",
        "A plot of oxygen in the atmosphere against altitude"],
      ans=0,
      why="The framework defines an oxygen sag curve as a plot of dissolved oxygen "
          "levels versus the distance from a source of pollution, usually excess "
          "nutrients and biological refuse. The rejected options plot other quantities "
          "against other variables."),

 dict(q="Dissolved oxygen measured downstream of a wastewater outfall is shown.",
      table=_T_SAG,
      choices=[
        "Dissolved oxygen falls to a minimum a few kilometers below the outfall and then "
        "recovers farther downstream",
        "Dissolved oxygen rises steadily with distance below the outfall",
        "Dissolved oxygen is lowest at the outfall itself",
        "Dissolved oxygen falls steadily with distance and never recovers",
        "Dissolved oxygen is the same at every distance measured"],
      ans=0,
      why="The values fall from the outfall to a minimum several kilometers downstream "
          "and then rise again toward the starting level. That shape is the oxygen sag "
          "the framework describes as a plot of dissolved oxygen against distance from a "
          "source of pollution."),

 dict(q="Which sources does the framework name for the heavy metals that can reach "
        "groundwater?",
      choices=[
        "Industry, especially mining and the burning of fossil fuels",
        "Rainfall and snowmelt in unpolluted watersheds",
        "Photosynthesis by aquatic plants",
        "Decomposition of leaf litter in forests",
        "Evaporation from the surface of the ocean"],
      ans=0,
      why="The framework states that heavy metals used for industry, especially mining "
          "and burning of fossil fuels, can reach the groundwater and impact the "
          "drinking water supply. Natural water movement and biological processes are "
          "not given as their source here."),

 dict(q="Why does the framework treat heavy metals reaching groundwater as a human "
        "health concern rather than only an ecological one?",
      choices=[
        "Groundwater is a drinking water supply, so contamination reaches the people who "
        "use it",
        "Heavy metals become harmless once they are dissolved in groundwater",
        "Groundwater cannot reach the surface, so the metals stay underground",
        "Heavy metals in groundwater cause the water table to fall",
        "Groundwater is used only for irrigation and never for drinking"],
      ans=0,
      why="The framework's own wording is that the metals can reach the groundwater, "
          "impacting the drinking water supply. That is a route from an industrial "
          "source to people, and it does not depend on the metals being altered "
          "underground."),

 dict(q="Which harms does the framework attribute to litter that reaches aquatic "
        "ecosystems?",
      choices=[
        "Intestinal blockage and choking hazards for wildlife, and the introduction of "
        "toxic substances to the food chain",
        "An increase in dissolved oxygen that harms fish",
        "A rise in water temperature that kills bottom dwellers",
        "The neutralization of acid in the water",
        "An increase in the amount of light reaching submerged plants"],
      ans=0,
      why="Besides being unsightly, litter can create intestinal blockage and choking "
          "hazards for wildlife and introduce toxic substances to the food chain, which "
          "is exactly what the framework lists. None of the rejected effects is "
          "attributed to litter."),

 dict(q="What does the framework say increased sediment in waterways does?",
      choices=[
        "It reduces light infiltration, affecting primary producers and visual predators, "
        "and it can settle and disrupt habitats",
        "It increases light infiltration and so increases plant growth",
        "It raises the dissolved oxygen of the water",
        "It converts mercury into a less toxic form",
        "It has no effect on organisms because it is not a chemical pollutant"],
      ans=0,
      why="The framework states both effects: reduced light infiltration, which affects "
          "primary producers and visual predators, and settling that disrupts habitats. "
          "The rejected options reverse the light effect or assign sediment a role the "
          "framework gives to other processes."),

 dict(q="Measurements from four stretches of one river are shown.",
      table=_T_LIGHT,
      choices=[
        "As suspended sediment rises, light penetrates less deeply and the algal growth "
        "measured at a fixed depth falls",
        "As suspended sediment rises, light penetrates more deeply",
        "Algal growth rises as suspended sediment rises",
        "Light penetration and algal growth are unchanged across the four stretches",
        "The stretch with the most sediment shows the deepest light penetration"],
      ans=0,
      why="Both the depth reached by light and the algal growth fall at every step as "
          "sediment rises. Reduced light infiltration affecting primary producers is the "
          "effect of increased sediment the framework names."),

 dict(q="What does the framework say happens when elemental sources of mercury enter "
        "aquatic environments?",
      choices=[
        "Bacteria in the water convert the mercury to highly toxic methylmercury",
        "The mercury evaporates immediately and leaves the water",
        "The mercury settles permanently and becomes chemically inert",
        "Plants absorb the mercury and convert it into oxygen",
        "The mercury neutralizes other pollutants in the water"],
      ans=0,
      why="The framework states that when elemental sources of mercury enter aquatic "
          "environments, bacteria in the water convert it to highly toxic methylmercury. "
          "No evaporation, permanent settling or neutralizing role is described for it."),

 dict(q="Water samples from a stream below an abandoned mine are shown.",
      table=_T_MERCURY,
      choices=[
        "Both mercury and methylmercury are highest nearest the mine and fall with "
        "distance, and methylmercury is present wherever mercury is",
        "Methylmercury is present only at the reference site",
        "Mercury falls with distance while methylmercury rises",
        "Both measurements are highest at the reference site",
        "Methylmercury is absent from every sample"],
      ans=0,
      why="Both columns take their largest values at the site nearest the mine and fall "
          "at every step with distance, and every sample carries some methylmercury. The "
          "framework has bacteria in the water convert mercury entering an aquatic "
          "environment into methylmercury."),

 dict(q="Records for one river are shown.",
      table=_T_LOAD,
      choices=[
        "The river carries 600 kilograms of the dissolved metal past the town each day",
        "The river carries 60 kilograms of the dissolved metal past the town each day",
        "The river carries 6,000 kilograms of the dissolved metal past the town each day",
        "The river carries 203 kilograms of the dissolved metal past the town each day",
        "The daily load cannot be found from these records"],
      ans=0,
      why="Multiplying the daily volume by the concentration gives the daily mass: two "
          "hundred million liters times three milligrams per liter is six hundred "
          "million milligrams, which is six hundred kilograms. The rejected values are "
          "off by a factor of ten or add the two quantities."),

 dict(q="A species is kept at several temperatures and grows well only within a narrow "
        "band, with stress and reduced reproduction on either side. Which framework "
        "concept does this illustrate?",
      choices=[
        "A range of tolerance with an optimum range in which homeostasis can be "
        "maintained",
        "An oxygen sag curve measured with distance from a source",
        "The conversion of mercury to methylmercury by bacteria",
        "The economic consequence of oil washing onto a beach",
        "The formation of an oceanic dead zone from nutrient pollution"],
      ans=0,
      why="The framework describes an optimum range for each factor where homeostasis "
          "can be maintained, with physiological stress, limited growth and reduced "
          "reproduction outside it. The other options name unrelated statements from the "
          "same topic."),

 dict(q="Why does the framework describe both floating oil and sinking oil components as "
        "harmful after a spill?",
      choices=[
        "Floating oil coats the feathers of birds and the fur of marine mammals, while "
        "components that sink kill some bottom-dwelling organisms",
        "Floating oil is harmless and only the sinking components matter",
        "Sinking oil is harmless and only the floating oil matters",
        "Both float and neither reaches the sea floor",
        "Both sink and neither remains at the surface"],
      ans=0,
      why="The framework describes harm at both levels of the water column, assigning "
          "the coating of feathers and fur to oil at the surface and the killing of "
          "bottom dwellers to components that sink. Neither part is described as "
          "harmless."),

 dict(q="A coastal town reports lost income from both its fishing fleet and its hotels "
        "after a spill reaches its beaches. Which framework statement does this "
        "illustrate?",
      choices=[
        "Oil that washes up on the beach can have economic consequences on the fishing "
        "and tourism industries",
        "Oil spills cause organisms to die from the hydrocarbons in oil",
        "Litter introduces toxic substances to the food chain",
        "Heavy metals from industry can reach the groundwater",
        "Increased sediment reduces light infiltration in waterways"],
      ans=0,
      why="The town's losses are economic and fall on fishing and tourism, which is "
          "exactly the consequence the framework attaches to oil washing up on a beach. "
          "The other statements describe ecological or health effects rather than "
          "economic ones."),

 dict(q="Which change would a scientist expect to shrink an oceanic dead zone, based on "
        "the framework's account of its cause?",
      choices=[
        "A reduction in the nutrient pollution reaching that part of the ocean",
        "An increase in the nutrient pollution reaching that part of the ocean",
        "An increase in the amount of litter entering the ocean",
        "An increase in the mercury entering the ocean",
        "A reduction in the light reaching the ocean surface"],
      ans=0,
      why="The framework attributes oceanic dead zones to increased nutrient pollution, "
          "so reducing that pollution addresses the stated cause. Litter, mercury and "
          "light are given other effects and are not the cause of the low oxygen."),

 dict(q="Why is the oxygen sag curve plotted against distance from the source rather "
        "than against time?",
      choices=[
        "It shows how dissolved oxygen changes with position downstream of the "
        "pollution, which is what the framework defines it to plot",
        "Time cannot be measured in a river",
        "Dissolved oxygen does not change over time anywhere",
        "The curve is plotted against depth rather than distance",
        "The curve plots nutrient concentration rather than oxygen"],
      ans=0,
      why="The framework's definition is a plot of dissolved oxygen levels versus the "
          "distance from a source of pollution, so distance is the variable it is "
          "defined against. The rejected options change the quantity plotted or deny "
          "that oxygen varies."),

 dict(q="Which of the following best explains why sediment can harm a visual predator "
        "even though sediment is not toxic?",
      choices=[
        "Sediment reduces the light in the water, and a visual predator depends on being "
        "able to see its prey",
        "Sediment poisons the predator directly through its gills",
        "Sediment raises the water temperature beyond the predator's tolerance",
        "Sediment converts to methylmercury inside the predator",
        "Sediment increases the oxygen the predator needs"],
      ans=0,
      why="The framework attributes to increased sediment a reduction in light "
          "infiltration that affects primary producers and visual predators, so the harm "
          "runs through the loss of light rather than through toxicity."),

 dict(q="A study finds that fish in a river below a smelter carry a form of mercury that "
        "is more toxic than the mercury measured entering the river. Which framework "
        "statement accounts for this?",
      choices=[
        "Bacteria in the water convert elemental mercury entering an aquatic environment "
        "into highly toxic methylmercury",
        "Mercury becomes more toxic simply by being diluted",
        "Fish manufacture mercury in their own tissues",
        "Sediment converts mercury into a heavier metal",
        "Sunlight breaks mercury into a more toxic gas"],
      ans=0,
      why="The framework has bacteria in the water convert elemental mercury to highly "
          "toxic methylmercury once it enters an aquatic environment, which is a change "
          "in chemical form rather than in concentration. No other conversion route is "
          "given."),

 dict(q="Which of the following best describes what happens to an organism held just "
        "outside its optimum range for a pollutant but well below a lethal "
        "concentration?",
      choices=[
        "It may experience physiological stress, limited growth and reduced "
        "reproduction while remaining alive",
        "It is unaffected until the lethal concentration is reached",
        "It dies immediately, since any departure from the optimum is fatal",
        "Its reproduction increases to compensate for the stress",
        "It converts the pollutant into a harmless substance"],
      ans=0,
      why="The framework lists physiological stress, limited growth and reduced "
          "reproduction for conditions outside the optimum range, and reserves death for "
          "extreme cases. So sublethal harm is exactly what it predicts there."),

 dict(q="A reef is exposed to warmer water, heavier sediment runoff and destructive "
        "fishing at the same time. How does the framework describe such a case?",
      choices=[
        "Reefs suffer damage due to a variety of factors, and all three of these are "
        "among them",
        "Only one factor can damage a reef at a time",
        "Sediment runoff protects reefs from the other two factors",
        "Destructive fishing is the only factor the framework recognizes",
        "None of these three is a recognized cause of reef damage"],
      ans=0,
      why="The framework's statement is that coral reefs have been suffering damage due "
          "to a variety of factors, and it names increasing ocean temperature, sediment "
          "runoff and destructive fishing practices among them. It does not rank them or "
          "limit the number acting at once."),

 dict(q="A town's well water is found to contain a heavy metal, and the town lies "
        "downgradient of an old mine. Which framework statement is most directly "
        "relevant?",
      choices=[
        "Heavy metals used for industry, especially mining, can reach the groundwater and "
        "impact the drinking water supply",
        "Litter can create choking hazards for wildlife",
        "Oil that washes up on a beach affects fishing and tourism",
        "Increased sediment reduces light infiltration in waterways",
        "Oceanic dead zones are caused by increased nutrient pollution"],
      ans=0,
      why="The pollutant is a heavy metal, the setting is groundwater used for drinking, "
          "and mining is one of the industrial sources the framework names. The other "
          "statements concern different pollutants in different settings."),

 dict(q="Which summary best captures the range of impacts this topic attributes to human "
        "activity in aquatic ecosystems?",
      choices=[
        "Organisms are pushed outside their ranges of tolerance, reefs are damaged, oil "
        "spills kill organisms and damage coastal economies, nutrient pollution creates "
        "low-oxygen zones, metals reach drinking water, litter and sediment harm "
        "wildlife and habitat, and mercury is converted to a more toxic form",
        "The only impact is a change in water temperature",
        "The impacts are limited to the economic losses suffered by coastal industries",
        "The impacts fall on individual organisms but never on habitats or people",
        "The impacts are confined to the open ocean and never reach fresh water"],
      ans=0,
      why="Each clause of the keyed summary is one of the framework's ten statements for "
          "this topic, which cover organisms, habitats, economies and drinking water "
          "alike. Every rejected summary omits or denies most of them."),
]
