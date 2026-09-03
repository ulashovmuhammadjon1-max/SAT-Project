# AP ENVIRONMENTAL SCIENCE 1.3 Aquatic Biomes
# CED effective Fall 2026, Unit 1 The Living World: Ecosystems.
# Enduring understanding ERT-1: Ecosystems are the result of biotic and abiotic
# interactions.
# Learning objective ERT-1.C: describe the global distribution and principal
# environmental aspects of aquatic biomes. Suggested skill 1.B.
#
# Essential knowledge relied on, in the framework's own words:
#   ERT-1.C.1  Freshwater biomes include streams, rivers, ponds, and lakes. These
#              freshwater biomes are a vital resource for drinking water.
#   ERT-1.C.2  Marine biomes include oceans, coral reefs, marshland, and estuaries.
#              Algae in marine biomes supply a large portion of the Earth's oxygen, and
#              also take in carbon dioxide from the atmosphere.
#   ERT-1.C.3  The global distribution of nonmineral marine natural resources, such as
#              different types of fish, varies because of some combination of salinity,
#              depth, turbidity, nutrient availability, and temperature.
#
# WHAT IS DELIBERATELY NOT ASKED. The framework NAMES the freshwater and marine biomes
# and does not define any of them. So no item asks what an estuary or a coral reef IS;
# items that use one of those names use it only as a member of the list it appears in.
# Where a salinity or temperature gradient matters, the numbers are given in the table so
# that nothing has to be assumed about the place.
#
# BOUNDARIES WITH NEIGHBOURING TOPICS. Light penetration with depth belongs to ENG-1.A.5
# in topic 1.8 and is NOT used here; depth and turbidity appear only as two of the five
# factors ERT-1.C.3 lists. The six-factor terrestrial list of ERT-1.B.3 belongs to topic
# 1.2; the only item here that touches it (item 20) does so to mark what the marine list
# does NOT contain.
#
# FIVE choices (A-E) per SCIENCE_BRIEF.md. No LaTeX: export_units.py does not typeset
# Environmental Science.
TOPIC = ("1.3", "Aquatic Biomes", 1)

_T_SALINITY = dict(
    headers=["Sampling station", "Salinity (grams of salt per kilogram of water)",
             "Number of fish species recorded"],
    rows=[["Station 1", "1", "9"],
          ["Station 2", "8", "14"],
          ["Station 3", "19", "21"],
          ["Station 4", "31", "17"]])

_T_DEPTH = dict(
    headers=["Depth band sampled (meters)", "Number of fish species recorded",
             "Percent of the recorded species found only in this band"],
    rows=[["0 to 50", "46", "52"],
          ["50 to 200", "38", "39"],
          ["200 to 600", "21", "62"],
          ["600 to 1200", "11", "82"]])

_T_TURBID = dict(
    headers=["Coastal site", "Turbidity (nephelometric turbidity units)",
             "Algal cover on the seabed (percent)"],
    rows=[["Site 1", "2", "58"],
          ["Site 2", "9", "37"],
          ["Site 3", "24", "12"],
          ["Site 4", "51", "3"]])

_T_NUTRIENT = dict(
    headers=["Fishing ground", "Surface nitrate concentration (micromoles per liter)",
             "Mean annual fish catch (thousands of tonnes)"],
    rows=[["Ground A", "0.4", "12"],
          ["Ground B", "3.1", "48"],
          ["Ground C", "7.6", "121"],
          ["Ground D", "11.9", "165"]])

_T_TEMPWATER = dict(
    headers=["Coastal survey block", "Mean sea surface temperature (degrees Celsius)",
             "Percent of catch made up of cold-water species",
             "Percent of catch made up of warm-water species"],
    rows=[["Block 1", "6", "88", "4"],
          ["Block 2", "12", "61", "27"],
          ["Block 3", "19", "22", "70"],
          ["Block 4", "26", "3", "94"]])

_T_BOTTLE = dict(
    headers=["Bottle of seawater containing algae", "Light supplied",
             "Change in dissolved oxygen after six hours (milligrams per liter)"],
    rows=[["Bottle 1", "Full daylight", "4.8"],
          ["Bottle 2", "Half daylight", "2.1"],
          ["Bottle 3", "Complete darkness", "-1.6"]])

_T_DIEL = dict(
    headers=["Time of day above an algal bed", "Dissolved carbon dioxide (milligrams per liter)"],
    rows=[["Two hours after sunrise", "9.4"],
          ["Midday", "5.1"],
          ["Two hours before sunset", "4.2"],
          ["Middle of the night", "10.8"]])

_T_SUPPLY = dict(
    headers=["Source of one city's drinking water", "Share of the annual supply (percent)"],
    rows=[["Reservoir on a river", "54"],
          ["Lake", "29"],
          ["Groundwater well", "17"]])

_T_TWOLAKES = dict(
    headers=["Lake", "Mean turbidity (nephelometric turbidity units)",
             "Mass of algae per square meter of lake bed (grams)"],
    rows=[["Lake M", "3", "410"],
          ["Lake N", "38", "45"]])

QUESTIONS = [

 dict(q="Which of the following does the framework name as a freshwater biome?",
      choices=[
        "A pond",
        "A coral reef",
        "An estuary",
        "Marshland",
        "The open ocean"],
      ans=0,
      why="ERT-1.C.1 lists streams, rivers, ponds and lakes as freshwater biomes. Each "
          "rejected option appears instead in the list of marine biomes given in "
          "ERT-1.C.2."),

 dict(q="Which of the following does the framework name as a marine biome?",
      choices=[
        "An estuary",
        "A stream",
        "A river",
        "A pond",
        "A lake"],
      ans=0,
      why="ERT-1.C.2 lists oceans, coral reefs, marshland and estuaries as marine biomes. "
          "Every rejected option belongs to the freshwater list in ERT-1.C.1."),

 dict(q="Why does the framework single out freshwater biomes as important to people?",
      choices=[
        "Because they are a vital resource for drinking water.",
        "Because they supply most of the salt used by people.",
        "Because they hold the largest share of the world's fish catch.",
        "Because they supply a large portion of the Earth's oxygen.",
        "Because they contain the world's mineral ore deposits."],
      ans=0,
      why="ERT-1.C.1 states that freshwater biomes are a vital resource for drinking "
          "water. The oxygen claim belongs to algae in marine biomes under ERT-1.C.2, "
          "and the framework makes no fish-catch or ore claim about fresh water."),

 dict(q="What does the framework state about algae living in marine biomes?",
      choices=[
        "They supply a large portion of the Earth's oxygen and take in carbon dioxide "
        "from the atmosphere.",
        "They supply a large portion of the Earth's carbon dioxide and take in oxygen "
        "from the atmosphere.",
        "They supply drinking water to coastal human populations.",
        "They have no measurable effect on the composition of the atmosphere.",
        "They release nitrogen gas that becomes the largest atmospheric reservoir."],
      ans=0,
      why="ERT-1.C.2 states that algae in marine biomes supply a large portion of the "
          "Earth's oxygen and also take in carbon dioxide from the atmosphere. The "
          "rejected options reverse the two gases or attach claims the statement does "
          "not make."),

 dict(q="Two ocean areas at similar latitudes support very different kinds of fish. "
        "Which set of conditions does the framework identify as accounting for "
        "differences of that kind?",
      choices=[
        "Salinity, depth, turbidity, nutrient availability, and temperature.",
        "Soil type, parent rock, and the length of the growing season.",
        "Latitude and altitude only.",
        "The total human population living on the nearest coast.",
        "The number of mineral deposits on the seafloor beneath each area."],
      ans=0,
      why="ERT-1.C.3 states that the global distribution of nonmineral marine natural "
          "resources, such as different types of fish, varies because of some combination "
          "of salinity, depth, turbidity, nutrient availability, and temperature."),

 dict(q="The table gives salinity and fish species counts at four stations along a single "
        "coastal transect. Which conclusion is best supported?",
      table=_T_SALINITY,
      choices=[
        "Salinity varies widely across the transect, and the species count is not the "
        "same at any two salinities recorded.",
        "Salinity is nearly constant across the transect, so it cannot influence which "
        "species are present.",
        "The station with the lowest salinity records the highest species count.",
        "Species count rises steadily from the first station to the last.",
        "Every station records the same number of fish species."],
      ans=0,
      why="The salinity column spans a thirtyfold range and no two stations share a "
          "species count, so the transect is a gradient rather than a uniform stretch. "
          "ERT-1.C.3 names salinity as one factor behind where marine species are found."),

 dict(q="A survey recorded fish species in four depth bands at one site, as shown. Which "
        "statement is best supported by the table?",
      table=_T_DEPTH,
      choices=[
        "Fewer species were recorded in the deeper bands, and a larger share of the "
        "species in the deepest band were found in no other band.",
        "More species were recorded in the deeper bands than in the shallow bands.",
        "The same number of species was recorded in every band.",
        "Every species recorded in the deepest band was also recorded in a shallower "
        "band.",
        "The shallowest band contained the largest share of species found in no other "
        "band."],
      ans=0,
      why="The species count falls from the shallowest band to the deepest while the "
          "share unique to a band is greatest in the deepest. ERT-1.C.3 names depth as "
          "one of the factors behind the distribution of marine species."),

 dict(q="Turbidity and algal cover were measured at four coastal sites, as shown. Which "
        "relationship do the data support?",
      table=_T_TURBID,
      choices=[
        "Algal cover falls as turbidity rises across the four sites.",
        "Algal cover rises as turbidity rises across the four sites.",
        "Algal cover is the same at every level of turbidity recorded.",
        "The site with the highest turbidity also has the highest algal cover.",
        "Turbidity is the same at all four sites, so no relationship can be examined."],
      ans=0,
      why="Sorting the sites by turbidity leaves the algal cover strictly decreasing. "
          "ERT-1.C.3 names turbidity among the factors behind the distribution of marine "
          "resources, and this table shows the direction of that relationship at one "
          "coast."),

 dict(q="Nitrate concentration and fish catch were recorded for four fishing grounds, as "
        "shown. Which conclusion is best supported?",
      table=_T_NUTRIENT,
      choices=[
        "The grounds with more nitrate available yielded the larger catches.",
        "The grounds with more nitrate available yielded the smaller catches.",
        "Catch is unrelated to the nitrate concentration recorded.",
        "The ground with the lowest nitrate concentration yielded the largest catch.",
        "All four grounds yielded catches within ten thousand tonnes of each other."],
      ans=0,
      why="Sorting the grounds by nitrate concentration leaves the catch strictly "
          "increasing. ERT-1.C.3 names nutrient availability among the factors behind "
          "the distribution of nonmineral marine resources such as fish."),

 dict(q="Sea surface temperature and the composition of the catch were recorded in four "
        "coastal blocks, as shown. Which statement is best supported?",
      table=_T_TEMPWATER,
      choices=[
        "The share of the catch made up of cold-water species falls as temperature "
        "rises, while the warm-water share rises.",
        "The share of the catch made up of cold-water species rises as temperature "
        "rises, while the warm-water share falls.",
        "Both shares rise together as temperature rises.",
        "Both shares are unchanged across the four blocks.",
        "The warmest block has the largest cold-water share of the four."],
      ans=0,
      why="Reading down the two composition columns as temperature increases, one falls "
          "and the other rises. ERT-1.C.3 names temperature among the factors behind the "
          "distribution of marine species."),

 dict(q="Three sealed bottles of seawater containing algae were held for six hours under "
        "the conditions shown. Which conclusion about the algae is best supported?",
      table=_T_BOTTLE,
      choices=[
        "The algae added oxygen to the water when light was supplied and did not do so "
        "in darkness.",
        "The algae added oxygen to the water in darkness and removed it in the light.",
        "The algae had the same effect on dissolved oxygen in all three bottles.",
        "The bottle held in complete darkness gained the most dissolved oxygen.",
        "The bottle in half daylight gained more dissolved oxygen than the bottle in "
        "full daylight."],
      ans=0,
      why="Dissolved oxygen rose in both lit bottles and fell in the dark bottle, and the "
          "larger rise came with the greater light supply. ERT-1.C.2 states that algae in "
          "marine biomes supply a large portion of the Earth's oxygen."),

 dict(q="Dissolved carbon dioxide was measured in the water above an algal bed at four "
        "times, as shown. Which conclusion is best supported?",
      table=_T_DIEL,
      choices=[
        "Dissolved carbon dioxide is lower during daylight than at night, which is "
        "consistent with algae taking carbon dioxide in.",
        "Dissolved carbon dioxide is higher during daylight than at night, which is "
        "consistent with algae releasing carbon dioxide in the light.",
        "Dissolved carbon dioxide is the same at every time recorded.",
        "The highest carbon dioxide reading was taken at midday.",
        "The lowest carbon dioxide reading was taken in the middle of the night."],
      ans=0,
      why="The two daylight readings are the two lowest and the night reading is the "
          "highest. ERT-1.C.2 states that algae in marine biomes take in carbon dioxide "
          "from the atmosphere, which is what a daytime drawdown reflects."),

 dict(q="A river carries water into a coastal bay, and salinity was measured at intervals "
        "from the river mouth out to open water. Why does the framework treat this "
        "gradient as important for the fish found there?",
      choices=[
        "Because salinity is one of the conditions it names as accounting for where "
        "different types of fish occur.",
        "Because salinity determines the total volume of water in the bay.",
        "Because salinity is the only condition that affects marine life.",
        "Because salinity determines the mineral resources of the seafloor.",
        "Because a change in salinity converts a marine biome into a terrestrial biome."],
      ans=0,
      why="ERT-1.C.3 lists salinity first among the conditions whose combination accounts "
          "for the varying distribution of nonmineral marine resources such as different "
          "types of fish. It is one contributing factor rather than the only one."),

 dict(q="ERT-1.C.3 concerns nonmineral marine natural resources. Which of the following "
        "is the example the framework itself gives?",
      choices=[
        "Different types of fish.",
        "Manganese nodules lying on the deep seafloor.",
        "Offshore petroleum reservoirs.",
        "Sand and gravel dredged from the seabed.",
        "Salt evaporated from seawater."],
      ans=0,
      why="ERT-1.C.3 names different types of fish as its example of a nonmineral marine "
          "natural resource. Every rejected option is a mineral or fossil deposit, which "
          "the word nonmineral excludes."),

 dict(q="The table shows where one city's drinking water comes from. Which statement "
        "about the city's supply is best supported by the table together with the "
        "framework?",
      table=_T_SUPPLY,
      choices=[
        "More than three quarters of the supply comes from the freshwater biomes the "
        "framework names as a vital drinking-water resource.",
        "The whole of the supply comes from marine biomes.",
        "None of the supply comes from a freshwater biome.",
        "The single largest share comes from the groundwater well.",
        "The lake and the well together supply more than the river reservoir does."],
      ans=0,
      why="ERT-1.C.1 names rivers and lakes among the freshwater biomes and calls them a "
          "vital resource for drinking water. Adding the two tabulated shares that come "
          "from those biomes gives more than three quarters of the supply."),

 dict(q="A student groups coral reefs together with estuaries and marshland. What "
        "justifies putting these three in one group?",
      choices=[
        "The framework names all three as marine biomes.",
        "The framework names all three as freshwater biomes.",
        "All three are found only in the deepest parts of the ocean.",
        "All three are terrestrial biomes shaped by their climate.",
        "All three are named as sources of drinking water."],
      ans=0,
      why="ERT-1.C.2 lists oceans, coral reefs, marshland and estuaries together as "
          "marine biomes, which is the grouping the framework itself makes."),

 dict(q="If marine algae were greatly reduced worldwide, which pair of consequences does "
        "the framework most directly support predicting?",
      choices=[
        "Less oxygen supplied to the Earth and less carbon dioxide taken in from the "
        "atmosphere.",
        "More oxygen supplied to the Earth and more carbon dioxide taken in from the "
        "atmosphere.",
        "Less oxygen supplied to the Earth and more carbon dioxide taken in from the "
        "atmosphere.",
        "No change in either gas, since algae affect only the water they live in.",
        "Less drinking water available and more salt in the oceans."],
      ans=0,
      why="ERT-1.C.2 assigns algae in marine biomes two roles at once, supplying a large "
          "portion of the Earth's oxygen and taking in carbon dioxide from the "
          "atmosphere, so reducing the algae reduces both."),

 dict(q="A researcher wants to test whether turbidity is what limits algae in a coastal "
        "bay. Which comparison would give the most direct evidence?",
      choices=[
        "Compare algal growth at sites that differ in turbidity while salinity, depth, "
        "nutrients and temperature are held similar.",
        "Compare algal growth at sites that differ in every one of the five conditions at "
        "once.",
        "Compare the number of fish species at sites that differ in turbidity.",
        "Compare algal growth in the bay with algal growth in a freshwater pond.",
        "Compare the total volume of water at sites that differ in turbidity."],
      ans=0,
      why="ERT-1.C.3 names five conditions whose combination accounts for distribution, "
          "so isolating one of them requires holding the other four similar. A comparison "
          "in which everything varies cannot attribute a difference to any single factor."),

 dict(q="Two areas of seabed lie at the same latitude, have the same salinity, the same "
        "turbidity, the same nutrient supply and the same temperature, but hold very "
        "different fish. Which of the framework's listed conditions remains as the likely "
        "explanation?",
      choices=[
        "Depth.",
        "Salinity.",
        "Turbidity.",
        "Nutrient availability.",
        "Temperature."],
      ans=0,
      why="ERT-1.C.3 lists salinity, depth, turbidity, nutrient availability and "
          "temperature. The stem holds four of the five equal, so the one it does not "
          "mention is the only listed candidate left."),

 dict(q="Which of the following is NOT one of the conditions the framework names as "
        "accounting for the distribution of nonmineral marine natural resources?",
      choices=[
        "Soil type.",
        "Salinity.",
        "Turbidity.",
        "Nutrient availability.",
        "Temperature."],
      ans=0,
      why="ERT-1.C.3 lists salinity, depth, turbidity, nutrient availability and "
          "temperature. Soil belongs to the terrestrial list in ERT-1.B.3 and does not "
          "appear in the marine one."),

 dict(q="Why is the world's fish supply not spread evenly through the oceans?",
      choices=[
        "Because the conditions fish depend on vary from place to place, in some "
        "combination of salinity, depth, turbidity, nutrients and temperature.",
        "Because fishing fleets have removed fish evenly from every part of the ocean.",
        "Because fish are a mineral resource and follow the seafloor ore deposits.",
        "Because temperature is the only condition that varies within an ocean.",
        "Because the ocean is a single biome with uniform conditions throughout."],
      ans=0,
      why="ERT-1.C.3 names different types of fish as its example of a nonmineral marine "
          "natural resource and attributes their uneven distribution to some combination "
          "of the five conditions it lists."),

 dict(q="A student writes that all aquatic biomes are essentially the same. Which "
        "distinction does the framework itself draw?",
      choices=[
        "It separates freshwater biomes such as streams and lakes from marine biomes such "
        "as oceans and coral reefs.",
        "It separates aquatic biomes by the season in which they are studied.",
        "It separates aquatic biomes by the country in whose waters they lie.",
        "It separates aquatic biomes into exactly two named lakes and two named rivers.",
        "It treats every body of water as one undivided biome."],
      ans=0,
      why="ERT-1.C.1 and ERT-1.C.2 give two separate lists, one of freshwater biomes and "
          "one of marine biomes, which is the division the framework makes."),

 dict(q="Turbidity and algal mass were measured in two lakes, as shown. Which statement "
        "is best supported by the table?",
      table=_T_TWOLAKES,
      choices=[
        "The clearer lake holds far more algae per square meter of lake bed.",
        "The murkier lake holds far more algae per square meter of lake bed.",
        "The two lakes hold about the same mass of algae per square meter.",
        "Turbidity is the same in the two lakes.",
        "Neither lake contains any algae."],
      ans=0,
      why="The lake with the lower turbidity reading carries an algal mass about nine "
          "times that of the murkier lake. Turbidity is one of the conditions ERT-1.C.3 "
          "names, and the table shows which direction the relationship runs here."),

 dict(q="Which finding would most directly support the claim that nutrient availability "
        "is influencing the size of a fishery?",
      choices=[
        "Catches at a set of grounds rise and fall together with the measured nutrient "
        "concentration of their surface waters over many years.",
        "The grounds with the largest catches are the ones nearest to a major port.",
        "The grounds with the largest catches are fished by the largest number of boats.",
        "Catches at every ground fell in one year when a storm damaged the fleet.",
        "The grounds with the largest catches lie at the greatest distance from land."],
      ans=0,
      why="ERT-1.C.3 names nutrient availability as one factor behind the distribution of "
          "fish, so the finding that bears on it is a measured association between "
          "nutrient concentration and catch. Port distance and fleet size are properties "
          "of the fishing effort, not of the water."),

 dict(q="A coastal wetland is drained and the algae living there are lost. Which effect "
        "does ERT-1.C.2 most directly support attributing to that loss?",
      choices=[
        "A reduction in the amount of carbon dioxide taken in from the atmosphere at that "
        "place.",
        "An increase in the amount of carbon dioxide taken in from the atmosphere at that "
        "place.",
        "An increase in the drinking water available from that place.",
        "A rise in the salinity of the open ocean worldwide.",
        "A change in the mineral resources of the seabed beneath the wetland."],
      ans=0,
      why="ERT-1.C.2 states that algae in marine biomes take in carbon dioxide from the "
          "atmosphere, so removing the algae removes that uptake at the place where they "
          "lived."),

 dict(q="Which statement correctly compares the two lists the framework gives for aquatic "
        "biomes?",
      choices=[
        "Streams, rivers, ponds and lakes are the freshwater list; oceans, coral reefs, "
        "marshland and estuaries are the marine list.",
        "Streams, rivers, ponds and lakes are the marine list; oceans, coral reefs, "
        "marshland and estuaries are the freshwater list.",
        "Both lists contain the same four entries under different names.",
        "The freshwater list contains nine entries and the marine list contains four.",
        "Only the marine list is given; the framework names no freshwater biomes."],
      ans=0,
      why="ERT-1.C.1 gives streams, rivers, ponds and lakes as freshwater biomes and "
          "ERT-1.C.2 gives oceans, coral reefs, marshland and estuaries as marine biomes, "
          "which is exactly the pairing in the keyed option."),

 dict(q="Using the four depth bands surveyed earlier, a student argues that the deepest "
        "band is the least distinctive part of the site. Which feature of those data most "
        "directly weakens that argument?",
      table=_T_DEPTH,
      choices=[
        "The deepest band has the largest share of species recorded in no other band.",
        "The deepest band has the largest number of species of any band.",
        "The deepest band and the shallowest band have equal species counts.",
        "The deepest band has the smallest share of species recorded in no other band.",
        "Every band has the same share of species recorded in no other band."],
      ans=0,
      why="Distinctiveness here is measured by the share of species found nowhere else, "
          "and that column reaches its maximum in the deepest band, so the data point the "
          "opposite way from the student's argument."),

 dict(q="Two fishing grounds have the same temperature, depth and turbidity, but one lies "
        "where a current brings up nutrient-rich water. Which prediction does the "
        "framework support?",
      choices=[
        "The ground receiving the nutrient-rich water is likely to support the larger "
        "fish resource.",
        "The two grounds must support identical fish resources, since three conditions "
        "match.",
        "The ground receiving the nutrient-rich water is likely to support the smaller "
        "fish resource.",
        "Nutrient supply cannot affect fish, because fish do not take up nitrate.",
        "Nutrient supply matters only in freshwater biomes."],
      ans=0,
      why="ERT-1.C.3 names nutrient availability among the conditions whose combination "
          "accounts for the distribution of nonmineral marine resources such as fish, and "
          "the stem holds the other tabulated conditions equal between the two grounds."),

 dict(q="Which of the following best explains why the framework calls the marine "
        "contribution to atmospheric oxygen large?",
      choices=[
        "Because algae living in marine biomes supply a large portion of the Earth's "
        "oxygen.",
        "Because seawater dissolves oxygen out of the atmosphere and returns it later.",
        "Because marine biomes cover a small fraction of the Earth's surface.",
        "Because fish release oxygen as they respire in seawater.",
        "Because coral reefs release oxygen from the minerals in their skeletons."],
      ans=0,
      why="ERT-1.C.2 attributes the supply of a large portion of the Earth's oxygen "
          "specifically to algae in marine biomes. The framework makes no such claim "
          "about dissolution, about fish respiration or about reef minerals."),

 dict(q="A town proposes to draw its drinking water from a nearby lake rather than from "
        "the sea. Which framework statement most directly supports that choice?",
      choices=[
        "Freshwater biomes, which include lakes, are a vital resource for drinking water.",
        "Marine biomes include oceans, coral reefs, marshland and estuaries.",
        "Algae in marine biomes supply a large portion of the Earth's oxygen.",
        "The distribution of fish varies with salinity, depth and temperature.",
        "The worldwide distribution of biomes is dynamic and may shift."],
      ans=0,
      why="ERT-1.C.1 names lakes among the freshwater biomes and states that those "
          "biomes are a vital resource for drinking water, which is precisely the use the "
          "town proposes."),
]
