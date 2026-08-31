# AP HUMAN GEOGRAPHY 5.1 Introduction to Agriculture -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding PSO-5, "Availability
# of resources and cultural practices influence agricultural practices and
# land-use patterns." Learning objective PSO-5.A, "Explain the connection
# between physical geography and agricultural practices."
#
# Essential knowledge -- three statements:
#   PSO-5.A.1  Agricultural practices are influenced by the physical environment
#              and climatic conditions, such as the Mediterranean climate and
#              tropical climates.
#   PSO-5.A.2  Intensive farming practices include market gardening, plantation
#              agriculture, and mixed crop-livestock systems.
#   PSO-5.A.3  Extensive farming practices include shifting cultivation, nomadic
#              herding, and ranching.
#
# THE ONE DEFINITION THE CED DOES NOT SUPPLY is what makes a practice intensive
# or extensive. It gives two lists and no criterion. The criterion used
# throughout this module, and stated in the claims, is the standard one:
#
#   INTENSIVE   high inputs of labour and/or capital per unit of LAND, so a
#               small area is worked hard
#   EXTENSIVE   low inputs of labour and capital per unit of LAND, so a large
#               area is worked lightly
#
# It is a ratio to AREA, not to output and not to the worker. That is why
# plantation agriculture -- which occupies very large estates -- is on the
# INTENSIVE list: what is measured is how much labour and capital each hectare
# receives, not how many hectares there are. Items 4, 5, 14, 21 and 26 rest on
# this, and item 14 asks for it directly, because the plantation case is where
# every student's intuition breaks.
#
# THE SECOND TRAP is reading PSO-5.A.1 as environmental determinism. The CED's
# verb is INFLUENCED BY, and the same statement's own examples show why: a
# Mediterranean climate occurs in several widely separated parts of the world
# and supports a recognisable but not identical set of practices, while tropical
# climates carry both plantation agriculture and shifting cultivation, which
# could hardly be less alike. Climate sets limits and costs; it does not choose
# the farm. Items 2, 17, 24, 25 and 29 are built on that distinction.
#
# WHAT IS SAFE TO ASSERT ABOUT CLIMATE. Only what follows from the physical
# facts: a Mediterranean climate has hot dry summers and mild wet winters, so
# summer crops need irrigation or must be drought-tolerant; a wet tropical
# climate is warm year-round with heavy rainfall and heavily leached soils; arid
# and semi-arid land grows grass unreliably and cannot support continuous
# cropping without water. No claim is made here about which country grows what.
#
# SYNONYM CARE. `geo_check` treats "shifting cultivation" and "slash-and-burn
# agriculture" as one construct, and "nomadic herding" and "pastoral nomadism"
# as another, so no choice list offers two names for one practice.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.1", "Introduction to Agriculture", 5)

QUESTIONS = [
 dict(q="According to the framework, what is the relationship between physical geography and agricultural practices?", choices=[
   "Agricultural practices are influenced by the physical environment and climatic conditions",
   "Agricultural practices are determined entirely by climate",
   "Agricultural practices are unrelated to the physical environment",
   "Physical geography is determined by agricultural practices",
   "Only soil, and not climate, influences agricultural practices"], ans=0,
   why="EK PSO-5.A.1 states that agricultural practices are influenced by the physical environment and climatic conditions. The verb is deliberate: the environment sets what is possible and what is costly, while what is actually farmed also reflects markets, technology and culture."),

 dict(q="A region has hot, dry summers and mild, wet winters. What does that combination imply for the crops grown there without irrigation?", choices=[
   "They must either be drought-tolerant through the summer or complete their growth during the wet season",
   "They may be any crop at all, since temperature is the only constraint",
   "They must be crops that require standing water all year",
   "They cannot include tree or vine crops of any kind",
   "They must be crops adapted to a short frost-free season"], ans=0,
   why="EK PSO-5.A.1 names the Mediterranean climate as one of its examples of climatic influence. The defining feature of that climate is that its rain and its warmth arrive in different seasons, so an unirrigated crop must be able to survive the dry warm months or finish before them."),

 dict(q="Which farming practice from the framework's lists is most associated with warm, wet tropical lowlands and the production of a single crop for export?", choices=[
   "Plantation agriculture",
   "Nomadic herding",
   "Ranching",
   "Market gardening",
   "Mixed crop-livestock systems"], ans=0,
   why="EK PSO-5.A.2 names plantation agriculture among the intensive practices and EK PSO-5.A.1 names tropical climates among the climatic conditions that influence practice. Year-round warmth and rainfall allow perennial export crops that cannot survive a frost."),

 dict(q="What does it mean to call a farming practice INTENSIVE?", choices=[
   "A large amount of labour and capital is applied to each unit of land, so a small area is worked hard",
   "A large area of land is farmed by each worker",
   "The farm produces a large total output regardless of its area",
   "The farm uses no machinery",
   "The farm is located far from any market"], ans=0,
   why="Intensity is a ratio of inputs to AREA, which is why a small market garden receiving heavy labour and capital is intensive. Total output and output per worker are different measures and can point the opposite way."),

 dict(q="What does it mean to call a farming practice EXTENSIVE?", choices=[
   "Relatively little labour and capital is applied to each unit of land, so a large area is needed",
   "The farm is highly productive per hectare",
   "The farm is close to its market",
   "The farm grows only export crops",
   "The farm employs many workers on a small holding"], ans=0,
   why="EK PSO-5.A.3 names shifting cultivation, nomadic herding and ranching as extensive practices, and all three spread modest inputs over a wide area. Land substitutes for labour and capital, which is why extensive systems appear where land is cheap relative to both."),

 dict(q="A grower on eleven hectares just outside a city produces salad greens, herbs and strawberries under plastic tunnels, harvesting several times a week for city shops. Which practice from the framework's lists is this?", choices=[
   "Market gardening, an intensive practice",
   "Ranching, an extensive practice",
   "Shifting cultivation, an extensive practice",
   "Nomadic herding, an extensive practice",
   "Plantation agriculture, since the crops are sold commercially"], ans=0,
   why="EK PSO-5.A.2 names market gardening among the intensive practices. A small acreage worked continuously for perishable, high-value produce sold nearby is the defining case, and the perishability is what ties the farm to a market it can reach quickly."),

 dict(q="Which three practices does the framework name as INTENSIVE?", choices=[
   "Market gardening, plantation agriculture, and mixed crop-livestock systems",
   "Shifting cultivation, nomadic herding, and ranching",
   "Ranching, market gardening, and shifting cultivation",
   "Plantation agriculture, ranching, and nomadic herding",
   "Mixed crop-livestock systems, ranching, and shifting cultivation"], ans=0,
   why="EK PSO-5.A.2 names exactly these three. The list is worth memorizing precisely because plantation agriculture occupies large estates, which makes it the member students most often move to the other list."),

 dict(q="Which three practices does the framework name as EXTENSIVE?", choices=[
   "Shifting cultivation, nomadic herding, and ranching",
   "Market gardening, plantation agriculture, and mixed crop-livestock systems",
   "Ranching, plantation agriculture, and market gardening",
   "Shifting cultivation, market gardening, and mixed crop-livestock systems",
   "Nomadic herding, plantation agriculture, and mixed crop-livestock systems"], ans=0,
   why="EK PSO-5.A.3 names exactly these three. All three apply modest labour and capital across a wide area, which is the property the category records."),

 dict(q="A family clears a small plot in tropical forest, burns the cut vegetation, crops the plot for three or four years, then abandons it to regrow and clears another. Which practice is this, and why is it classified as it is?", choices=[
   "Shifting cultivation, extensive because the household needs a large area of land over time even though each plot is small",
   "Market gardening, intensive because the plot is small",
   "Plantation agriculture, intensive because the forest is tropical",
   "Ranching, extensive because the land is not permanently cropped",
   "Mixed crop-livestock, intensive because both crops and forest are used"], ans=0,
   why="EK PSO-5.A.3 names shifting cultivation among the extensive practices. The plot in use is small, but the fallow land regenerating around it is part of the system, so the land requirement per household over a full cycle is large."),

 dict(q="Herders move livestock between seasonal pastures across dry grassland and semi-desert, never cropping the land. Which practice is this, and what physical condition explains it?", choices=[
   "Nomadic herding, an extensive practice suited to land too dry or too variable for reliable cropping",
   "Ranching, since livestock are involved and the land is dry",
   "Mixed crop-livestock, since animals are raised",
   "Market gardening, since the herders sell animals",
   "Plantation agriculture, since one product is specialized in"], ans=0,
   why="EK PSO-5.A.3 names nomadic herding among the extensive practices and EK PSO-5.A.1 connects practice to the physical environment. Where rainfall is too low and too erratic for a crop, moving animals to wherever grass has grown converts an unreliable resource into food."),

 dict(q="Cattle graze on a fenced holding of 14,000 hectares with two workers, and are trucked to a distant processing plant. Which practice is this?", choices=[
   "Ranching, an extensive practice",
   "Nomadic herding, since animals graze",
   "Mixed crop-livestock, since livestock are raised commercially",
   "Market gardening, since the product is sold",
   "Plantation agriculture, since the holding is very large"], ans=0,
   why="EK PSO-5.A.3 names ranching among the extensive practices. The land is held permanently and worked with very little labour or capital per hectare, which distinguishes it from herding that moves across land nobody fences and from systems that crop the same ground."),

 dict(q="A farm grows grain and fodder and keeps dairy cattle on the same holding, feeding the fodder to the animals and returning manure to the fields. Which practice is this, and why is it intensive?", choices=[
   "A mixed crop-livestock system, intensive because the same land supports two enterprises and receives labour and nutrients continuously",
   "Ranching, extensive because livestock are kept",
   "Shifting cultivation, extensive because fields are rotated",
   "Plantation agriculture, intensive because it is commercial",
   "Nomadic herding, extensive because animals are fed"], ans=0,
   why="EK PSO-5.A.2 names mixed crop-livestock systems among the intensive practices. Linking the two enterprises means each hectare is producing through more of the year and the nutrient cycle is closed on the farm, which is a high level of management per unit of land."),

 dict(q="Why does the framework classify plantation agriculture as INTENSIVE even though plantations occupy very large estates?", choices=[
   "Intensity measures labour and capital per unit of land, and a plantation's processing, planting and harvesting demands are high on every hectare it holds",
   "Because plantations are always smaller than ranches",
   "Because plantations produce food rather than fibre",
   "Because the estate is owned by one company",
   "Because plantations occur only in tropical climates"], ans=0,
   why="EK PSO-5.A.2 places plantation agriculture on the intensive list. Total estate size is not the criterion; the labour and capital each hectare absorbs is, and a perennial export crop harvested and processed on site absorbs a great deal of both."),

 dict(q="Two farms produce the same total tonnage. One works 8 hectares with 40 workers and the other works 900 hectares with 4. Which comparison is correct?", choices=[
   "The 8-hectare farm is far more intensive, since intensity compares inputs with land area rather than with output",
   "Both are equally intensive, since their output is the same",
   "The 900-hectare farm is more intensive, since it produces the same on more land",
   "Neither can be classified without knowing the crop",
   "The 900-hectare farm is more intensive, since it uses more machinery per worker"], ans=0,
   why="Intensity is the ratio of labour and capital to AREA, so equal output tells a geographer nothing about it. Five workers per hectare against one worker per 225 hectares is the comparison the category is built on."),

 dict(q="Which is the strongest reason the same climate can support several different agricultural practices?", choices=[
   "Climate sets the limits and the costs, while what is actually grown also depends on markets, technology, land ownership and culture",
   "Climate has no measurable effect on farming",
   "Every climate supports exactly one practice",
   "Farmers ignore climate when it is inconvenient",
   "Practices are assigned to climates by governments"], ans=0,
   why="EK PSO-5.A.1 says practices are INFLUENCED by the physical environment and climatic conditions rather than determined by them. Tropical climates carry both plantation agriculture and shifting cultivation, which are about as different as two systems in the framework's lists can be."),

 dict(q="Beyond climate, which set of physical conditions most directly shapes what a piece of land can be used for?", choices=[
   "Soil depth and fertility, slope, and the availability of water",
   "Distance to the nearest national border",
   "The political party governing the region",
   "The number of languages spoken locally",
   "The age structure of the national population"], ans=0,
   why="EK PSO-5.A.1 names the physical environment as well as climatic conditions. Steep slopes, thin soils and absent water restrict what can be grown and how, which is why terraces, irrigation and grazing appear where they do."),

 dict(q="A tropical rainforest region has heavy rainfall year-round and soils whose nutrients are quickly washed downward. How does this help explain shifting cultivation?", choices=[
   "Burning returns nutrients to the surface for a few seasons, after which the plot must be rested, which is why the practice moves",
   "The soils are so fertile that a plot never needs to be rested",
   "Heavy rain makes any cultivation impossible",
   "The practice is chosen because the climate is cool",
   "Nutrients accumulate at the surface, so plots improve with use"], ans=0,
   why="EK PSO-5.A.1 connects practice to the physical environment and EK PSO-5.A.3 names shifting cultivation as an extensive practice. Where continuous rainfall leaches the soil, fertility is held in the vegetation rather than the ground, so the cycle of clearing, cropping and fallow follows directly from the physical facts."),

 dict(q="A government offers subsidised irrigation in a region with hot dry summers, and farmers begin growing summer vegetables where they previously grew only winter grain and drought-tolerant tree crops. What does this show?", choices=[
   "Technology can relax a climatic constraint, which is why the framework says practice is influenced by climate rather than fixed by it",
   "The region's climate has changed",
   "Climate never constrained the region in the first place",
   "Irrigation proves that the physical environment is irrelevant to farming",
   "Winter grain cannot be grown in a Mediterranean climate"], ans=0,
   why="EK PSO-5.A.1 uses the word 'influenced', and irrigation is the clearest illustration of why. The dry summer is still a physical fact; what has changed is the cost of working around it, which is the kind of change that shifts a practice without changing the climate."),

 dict(q="Which pairing of a practice with its category is CORRECT?", choices=[
   "Ranching with extensive practice",
   "Market gardening with extensive practice",
   "Shifting cultivation with intensive practice",
   "Mixed crop-livestock systems with extensive practice",
   "Nomadic herding with intensive practice"], ans=0,
   why="EK PSO-5.A.2 lists market gardening, plantation agriculture and mixed crop-livestock systems as intensive, and EK PSO-5.A.3 lists shifting cultivation, nomadic herding and ranching as extensive. Only one pairing here places a practice on the list the framework puts it on."),

 dict(q="Why does the intensity of a farming system tend to fall as distance from a city increases, all else equal?", choices=[
   "Land is cheaper further out, so it becomes rational to substitute more land for labour and capital",
   "Soils are always poorer further from cities",
   "Rainfall always decreases with distance from cities",
   "Governments forbid intensive farming outside cities",
   "Distance has no effect on how land is farmed"], ans=0,
   why="EK PSO-5.A.2 and EK PSO-5.A.3 divide practices by how hard each hectare is worked, and the price of a hectare is what makes working it hard worthwhile. Where land is dear a farmer economizes on land; where land is cheap a farmer economizes on labour and capital instead."),

 dict(q="A student says that extensive farming means low productivity. What is the most accurate correction?", choices=[
   "Extensive means low inputs per hectare, and output per WORKER on a mechanized extensive farm can be extremely high",
   "Extensive means high inputs per hectare, so the student has it backwards",
   "The student is correct, since extensive farms always produce little",
   "Extensive refers to the distance to market rather than to inputs",
   "Extensive and intensive both describe output per hectare only"], ans=0,
   why="Extensive systems yield little per hectare by construction, but a grain farm with large machinery and two operators can produce enormous quantities per person. Confusing the two denominators is the commonest error in this part of the course."),

 dict(q="Which practice on the framework's lists would be most difficult to sustain if the land it uses were fenced and subdivided into permanent private holdings?", choices=[
   "Nomadic herding, which depends on moving animals across wide areas to wherever forage is available",
   "Market gardening, which uses a small fixed plot",
   "Plantation agriculture, which occupies a defined estate",
   "Mixed crop-livestock systems, which operate on one holding",
   "Ranching, which is already conducted on fenced land"], ans=0,
   why="EK PSO-5.A.3 names nomadic herding as an extensive practice, and its extensiveness is precisely a matter of mobility across a large area. The other four are conducted on land held in one place, so partition does not remove the basis of the system."),

 dict(q="Two regions share a Mediterranean climate but lie on opposite sides of the world. What does the framework's wording lead a geographer to expect?", choices=[
   "Similar physical opportunities and constraints, and therefore some recognisably similar crops, without the two regions farming identically",
   "Identical agricultural systems, since climate determines practice",
   "No similarity at all, since climate is irrelevant",
   "Similar crops only if the two regions trade with each other",
   "Similar practices only if the two regions have the same government"], ans=0,
   why="EK PSO-5.A.1 says practice is influenced by climatic conditions and names the Mediterranean climate as an example. Shared climate narrows the range of sensible crops in both places, while market access, landholding and technology account for the differences that remain."),

 dict(q="Why is a warm climate with reliable year-round rainfall favourable to a perennial export crop grown on plantations?", choices=[
   "A tree or shrub crop can grow and be harvested through much of the year without a frost that would kill it",
   "Because year-round rain removes the need for any labour",
   "Because such climates have the world's deepest soils",
   "Because perennial crops require a cold dormant season",
   "Because plantations can only be established where rainfall is unreliable"], ans=0,
   why="EK PSO-5.A.1 names tropical climates as an example of climatic influence and EK PSO-5.A.2 names plantation agriculture as an intensive practice. A perennial crop represents years of investment before the first harvest, which a frost-free climate protects and a temperate one would not."),

 dict(q="A geographer describes intensity as a spectrum rather than two boxes. What is the best support for that description?", choices=[
   "Inputs per hectare vary continuously, and the same practice can be conducted more or less intensively in different places",
   "The framework says there are exactly two possible farming systems",
   "Every farm applies exactly the same inputs per hectare",
   "Intensity cannot be measured at all",
   "The two categories are defined by crop type rather than by inputs"], ans=0,
   why="EK PSO-5.A.2 and EK PSO-5.A.3 give lists rather than a threshold, and no boundary value appears anywhere in the framework. Cattle raised on unimproved range and cattle raised on fertilized, irrigated pasture are the same enterprise at very different intensities."),

 dict(q="Labour applied to four farming systems is recorded below. Using the accompanying figures, which system is the most intensive and which the most extensive?",
   table=dict(headers=["System", "Area (hectares)", "Labour (worker-days per year)"],
     rows=[["System 1", "6", "1,800"],
           ["System 2", "120", "900"],
           ["System 3", "2,400", "480"],
           ["System 4", "40", "600"]]),
   choices=[
   "System 1 is the most intensive at 300 worker-days per hectare and System 3 the most extensive at 0.2",
   "System 3 is the most intensive because it uses the most land",
   "System 2 is the most intensive, since it applies more labour than every holding larger than it",
   "System 4 is the most extensive because it has the fewest workers",
   "All four are equally intensive, since each is farmed"], ans=0,
   why="Dividing labour by area gives 300, 7.5, 0.2 and 15 worker-days per hectare, so the smallest holding is worked hardest and the largest most lightly. Intensity compares inputs with area rather than with total labour, which is why the system using the second-largest labour force is not the most intensive."),

 dict(q="Monthly conditions at one station are recorded below. Using the accompanying figures, which agricultural constraint does this climate impose?",
   table=dict(headers=["Season", "Mean temperature (degrees Celsius)", "Rainfall (millimetres)"],
     rows=[["December to February", "11", "310"],
           ["March to May", "16", "120"],
           ["June to August", "27", "15"],
           ["September to November", "19", "95"]]),
   choices=[
   "The warmest season is also the driest, receiving only 15 millimetres, so a summer crop needs irrigation or drought tolerance",
   "The warmest season is also the wettest, so any crop can be grown in summer",
   "The station is frost-bound all year, so no crop can be grown",
   "Rainfall is evenly distributed, so season does not matter",
   "The coldest season is the driest, so winter cropping is impossible"], ans=0,
   why="The hottest quarter at 27 degrees receives 15 millimetres while the coolest at 11 degrees receives 310, so warmth and water arrive in different seasons. EK PSO-5.A.1 names the Mediterranean climate among its examples, and this seasonal mismatch is its defining agricultural consequence."),

 dict(q="Four holdings are recorded below. Using the accompanying figures, which is best described as an extensive system?",
   table=dict(headers=["Holding", "Area (hectares)", "Workers", "Capital spending per hectare (currency units)"],
     rows=[["Holding W", "3", "9", "4,200"],
           ["Holding X", "60", "14", "1,100"],
           ["Holding Y", "3,000", "3", "12"],
           ["Holding Z", "25", "7", "900"]]),
   choices=[
   "Holding Y, with one worker per 1,000 hectares and 12 currency units of capital per hectare",
   "Holding W, because it has the fewest hectares",
   "Holding X, because it has the most workers",
   "Holding Z, because its capital spending is lowest of the small holdings",
   "All four, since every farm uses land"], ans=0,
   why="One holding records a thousand hectares per worker and twelve currency units of capital per hectare, against three hectares for nine workers and 4,200 units per hectare at the other end. EK PSO-5.A.3 groups practices that spread modest labour and capital over a wide area, and both of this holding's ratios are two orders of magnitude below the rest."),

 dict(q="Which of these would be the strongest single piece of evidence that a farming system is extensive rather than intensive?", choices=[
   "A very low figure for labour and capital applied per hectare",
   "A very large total output",
   "A very large number of employees",
   "A location far from the nearest port",
   "A crop that is exported rather than consumed locally"], ans=0,
   why="EK PSO-5.A.2 and EK PSO-5.A.3 divide the practices by how heavily each unit of land is worked. Total output, workforce size, location and destination of the crop are all compatible with either category, so only the ratio to area settles the question."),

 dict(q="A student is asked what the three essential knowledge statements of this topic establish together. Which answer stays inside what the framework claims?", choices=[
   "That the physical environment and climate influence what farming is practised, and that practices divide into intensive and extensive groups the framework lists by name",
   "That climate determines exactly which crop is grown in each place",
   "That all tropical farming is extensive and all temperate farming is intensive",
   "That intensity is measured by the total size of a holding",
   "That agricultural practice is unrelated to physical geography"], ans=0,
   why="EK PSO-5.A.1 supplies the influence of environment and climate, while EK PSO-5.A.2 and EK PSO-5.A.3 supply the two named lists. Tropical climates carry plantation agriculture from the intensive list and shifting cultivation from the extensive one, which is why no climate maps onto one category."),
]
