# AP HUMAN GEOGRAPHY 5.8 Von Thunen Model -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding PSO-5, "Availability
# of resources and cultural practices influence agricultural practices and
# land-use patterns." Learning objective PSO-5.D, "Describe how the von Thunen
# model is used to explain patterns of agricultural production at various
# scales." Suggested skill 5.B, scale analysis.
#
# Essential knowledge -- ONE statement, and it carries its own caveat:
#   PSO-5.D.1  Von Thunen's model helps to explain rural land use by emphasizing
#              the importance of transportation costs associated with distance
#              from the market; however, regions of specialty farming do not
#              always conform to von Thunen's concentric rings.
#
# THE SEMICOLON IS THE POINT. The CED states the model and then limits it in one
# sentence, and a module that taught only the first half would be teaching half
# the statement. Items 10, 22, 28 and 30 key on the caveat, and item 28's table
# is built so that the non-conforming zone is a SPECIALTY farming region, which
# is the exact exception the CED names rather than a generic failure.
#
# WHAT THE MODEL ACTUALLY EMPHASIZES, in the CED's own words, is TRANSPORTATION
# COSTS ASSOCIATED WITH DISTANCE FROM THE MARKET. That is the whole engine. A
# product whose transport cost rises steeply with distance -- because it is
# perishable, bulky or heavy relative to its value -- loses more by being far
# away, so it outbids others for near land. A product that travels cheaply can
# afford distance. Items 4 to 8, 15, 24 and 27 all run that single argument on
# different products, and item 8 gives the case where the transport cost is
# nearly zero because the product walks.
#
# THE RINGS THEMSELVES are not listed in the CED, so this module derives their
# ORDER from transport cost rather than asserting it: intensive dairying and
# market gardening nearest, then forest, then field crops, then grazing. The
# forest ring is the one students find odd and it is the clearest illustration of
# the mechanism -- in the world von Thunen was describing, fuel and timber were
# heavy, bulky and needed constantly, so their transport cost per unit of value
# was very high. Item 5 keys on that reasoning, not on the ring number.
#
# THE ASSUMPTIONS of the isolated state -- one market, a flat featureless plain,
# uniform soil and climate, transport equally easy in every direction, and
# producers seeking the best return -- are what produce circles rather than some
# other shape. Items 2, 3, 12, 13, 17, 19 and 25 work with them, and the
# consistent line is that the assumptions are the METHOD and not an error:
# holding everything else constant is how the effect of distance alone becomes
# visible.
#
# SCALE, which the learning objective names explicitly: the same reasoning
# applies around one town, around a metropolitan region, and at the global scale
# where perishable produce is grown near wealthy markets and grain and livestock
# far from them. Items 14, 23 and 26 are the scale items.
#
# SYNONYM CARE. `geo_check` treats {"least cost theory", "weber's model"} as one
# construct and {"central place theory", "christaller's model"} as another, so
# item 20 names each rival model in exactly one way.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.8", "Von Thünen Model", 5)

QUESTIONS = [
 dict(q="According to the framework, what does von Thunen's model emphasize in explaining rural land use?", choices=[
   "The importance of transportation costs associated with distance from the market",
   "The importance of soil fertility differences between districts",
   "The importance of climate in determining which crops can be grown",
   "The importance of government subsidies to farmers",
   "The importance of the survey method used to divide the land"], ans=0,
   why="EK PSO-5.D.1 says the model helps explain rural land use by emphasizing the importance of transportation costs associated with distance from the market. Soil and climate matter to agriculture, but the model deliberately holds them constant so that the effect of distance alone can be seen."),

 dict(q="Which set of conditions does the model assume in order to produce concentric rings?", choices=[
   "A single market on a flat plain with uniform soil and climate, transport equally easy in every direction, and producers seeking the best return",
   "Several competing markets in mountainous terrain with varied soils",
   "No market at all, with all output consumed on the farm",
   "A single market reachable only by one river",
   "Uniform soils but a different climate in each ring"], ans=0,
   why="EK PSO-5.D.1 describes the model's concentric rings, and rings are what those assumptions produce. If transport is equally easy in every direction from one point, then equal distances are equally costly and the resulting bands are circles."),

 dict(q="A navigable river runs across the plain, making transport along it far cheaper than transport overland. What happens to the model's prediction?", choices=[
   "The rings stretch outward along the river, because the cost of distance is lower in that direction",
   "The rings disappear entirely and no pattern remains",
   "The rings contract toward the market on all sides",
   "The rings become perfect circles of a larger radius",
   "Nothing changes, since rivers are not part of transport"], ans=0,
   why="EK PSO-5.D.1 makes transportation cost the model's central variable, so anything that changes the cost of distance changes the shape of the result. A direction in which distance is cheap can support a given use further out, which pulls the boundary of that band outward along the route."),

 dict(q="Why does intensive production of fresh milk and vegetables occupy the land nearest the market in the model?", choices=[
   "These products lose value quickly and cost a great deal to move, so being far from the market costs them more than it costs anything else",
   "These products require the deepest soils, which are always found near cities",
   "These products cannot be grown further than a few kilometres from a city",
   "These products are the least valuable per hectare",
   "These products are the cheapest of all to transport"], ans=0,
   why="EK PSO-5.D.1 identifies transportation costs associated with distance as the model's emphasis. A perishable product carries a steep penalty for every extra kilometre, so it gains most from a near site and can outbid other uses for it."),

 dict(q="In von Thunen's original arrangement, forest occupied a ring close to the market. What reasoning explains that placement?", choices=[
   "Fuel and timber were heavy and bulky in relation to their value and were needed constantly, so moving them any distance was expensive",
   "Trees will not grow more than a few kilometres from a city",
   "Forest was the most valuable product per hectare",
   "Forest required daily attention from many workers",
   "Forest could not be transported at all by any method"], ans=0,
   why="EK PSO-5.D.1 makes transportation cost the model's organizing variable, and this ring is the clearest illustration of it. In the economy von Thunen was describing, wood was the fuel as well as the building material, so its weight and constant demand put a heavy cost on distance."),

 dict(q="Why do field crops such as grain occupy a ring beyond the intensive and forest rings?", choices=[
   "Grain stores well and travels cheaply for its value, so distance costs it comparatively little",
   "Grain is the most perishable of all farm products",
   "Grain yields more per hectare than any other product",
   "Grain requires the most labour per hectare",
   "Grain can be grown only on distant land"], ans=0,
   why="EK PSO-5.D.1 emphasizes transportation costs associated with distance from the market. A dry, durable product loses little by being carried, so it is outbid for near land and does not need it, which places it in a middle band."),

 dict(q="Why does livestock grazing occupy the outermost ring in the model?", choices=[
   "It earns the least from each hectare, so it can bid only for the cheapest land, which is the land furthest from the market",
   "It earns the most from each hectare and can afford distant land",
   "Livestock cannot survive near a market",
   "Grazing requires the deepest soils, found only at a distance",
   "Grazing produces the most perishable product"], ans=0,
   why="EK PSO-5.D.1 explains rural land use through transportation costs and distance from the market. An extensive use earning little per hectare cannot win an auction for near land, and it does not need to, because the low rent of distant land is what makes it viable."),

 dict(q="Which feature of live animals reinforces their position in the outer ring of the model?", choices=[
   "They can be walked to market under their own power, which makes their transport cost per unit of distance unusually low",
   "They spoil faster than any other product",
   "They weigh more per unit of value than firewood",
   "They must be sold within hours of leaving the farm",
   "They cannot be moved at all once mature"], ans=0,
   why="EK PSO-5.D.1 makes transport cost the model's engine, and in the world it describes an animal moved itself. A product that supplies its own locomotion has almost the flattest cost-distance relationship of anything a farm produces, which puts it furthest out."),

 dict(q="How does von Thunen's model relate to bid-rent theory?", choices=[
   "The rings are the outcome of competitive bidding, since at each distance the use that can pay most for the land obtains it",
   "The two are unrelated ideas about different subjects",
   "Bid-rent theory contradicts the model's predictions",
   "The model assigns land uses by government decision rather than by bidding",
   "Bid-rent theory applies only to land that is not farmed"], ans=0,
   why="EK PSO-5.C.2 names bid-rent theory as the account of how land costs shape intensity and EK PSO-5.D.1 gives the model as the explanation of rural land use through transport cost and distance. The rings are what a rent gradient looks like once several uses bid against one another around one market."),

 dict(q="What caveat does the framework attach to von Thunen's model in the same sentence in which it states it?", choices=[
   "Regions of specialty farming do not always conform to the concentric rings",
   "The model applies only to livestock production",
   "The model has been shown to be entirely wrong",
   "The model applies only at the global scale",
   "The model cannot be applied to any real landscape"], ans=0,
   why="EK PSO-5.D.1 states the model and then limits it in the same sentence, saying that regions of specialty farming do not always conform to the rings. The caveat names a particular exception rather than dismissing the model, which is why both halves have to be learned together."),

 dict(q="How did refrigerated transport change the pattern the model predicts?", choices=[
   "It lowered the distance penalty on perishable products, so they can now be produced far from the markets that consume them",
   "It raised the distance penalty on perishable products",
   "It removed the need for any agricultural production",
   "It made grain more perishable than milk",
   "It had no effect, since the model concerns only rent"], ans=0,
   why="EK PSO-5.D.1 identifies transportation costs associated with distance as what the model emphasizes, so a technology that changes those costs changes the prediction. Perishability was the reason milk and vegetables had to be near, and refrigeration is precisely an attack on that reason."),

 dict(q="A region contains three large cities rather than one. What does the model predict for its land use?", choices=[
   "Each city generates its own set of bands, which overlap and interrupt one another where the cities are close together",
   "The model cannot be applied and predicts nothing",
   "One perfect set of rings forms around the largest city and the others have no effect",
   "All agricultural land becomes equally intensive",
   "The bands become squares rather than circles"], ans=0,
   why="EK PSO-5.D.1 explains land use by distance from THE market, and the assumption of a single market is what produces one set of circles. Adding markets does not remove the mechanism; it superimposes several gradients, which is why real landscapes show interrupted bands rather than clean rings."),

 dict(q="A district within the plain has thin, stony soil unsuitable for cultivation. How should a geographer treat this when applying the model?", choices=[
   "As a departure from the model's assumption of uniform land quality, which distorts the ring the district falls in without disproving the mechanism",
   "As proof that transport costs do not affect land use",
   "As a reason to abandon the model entirely",
   "As evidence that the district must lie in the innermost ring",
   "As irrelevant, since soil forms no part of any land-use decision"], ans=0,
   why="EK PSO-5.D.1 says the model HELPS TO EXPLAIN rural land use, which is a claim about a contributing factor rather than a complete account. The assumptions isolate distance, so where an assumption fails the local pattern departs from the prediction while the underlying pressure remains."),

 dict(q="How is the model applied at the GLOBAL scale?", choices=[
   "Perishable and high-value produce is grown relatively near wealthy consuming markets, while grain and livestock come from far more distant regions",
   "It cannot be applied above the scale of a single town",
   "Every country produces exactly the same goods",
   "The global pattern is the exact reverse of the local one",
   "At the global scale transport costs cease to exist"], ans=0,
   why="Learning objective PSO-5.D asks students to describe how the model explains patterns of agricultural production AT VARIOUS SCALES. The mechanism of EK PSO-5.D.1 is transport cost against distance, which operates whether the market is a town or a continent's worth of consumers."),

 dict(q="Two products earn the same amount at the market gate. One costs four times as much to move each kilometre. What does the model predict?", choices=[
   "The costlier product to move will be produced nearer the market and will outbid the other for near land",
   "The costlier product to move will be produced further from the market",
   "Both will be produced at the same distance, since their market prices are equal",
   "Neither will be produced at all",
   "The cheaper product to move will be produced nearest the market"], ans=0,
   why="EK PSO-5.D.1 emphasizes transportation costs associated with distance from the market, and equal gate prices leave transport cost as the only difference. The product losing more per kilometre gains more from a near site, so it is willing to pay more for one."),

 dict(q="What is von Thunen's model FOR, according to the framework's wording?", choices=[
   "Helping to explain rural land use by isolating one variable, rather than predicting exactly which crop will grow in a given place",
   "Predicting with certainty which crop will be grown at every location",
   "Determining the fertility of soil in each ring",
   "Setting the prices farmers receive for their products",
   "Deciding where governments should build roads"], ans=0,
   why="EK PSO-5.D.1 says the model HELPS TO EXPLAIN rural land use, and it attaches a caveat about specialty regions in the same sentence. A model that helped to explain would be judged by whether it makes a pattern intelligible, not by whether every case matches it."),

 dict(q="Why are the model's unrealistic assumptions a feature of its method rather than a defect?", choices=[
   "Holding soil, climate and terrain constant is the only way to see what distance from the market does on its own",
   "The assumptions were believed to be literally true when the model was written",
   "The assumptions make the model impossible to test",
   "The assumptions are required by the framework for every model",
   "The assumptions have no effect on the model's conclusions"], ans=0,
   why="EK PSO-5.D.1 credits the model with emphasizing transportation costs associated with distance from the market. Emphasis requires suppression: everything else has to be held still for the one variable's effect to become visible, which is why the plain is featureless."),

 dict(q="A government pays a subsidy that makes a low-value crop profitable on land far from any market. What does this show about the model?", choices=[
   "Policy can override the cost gradient the model isolates, which is one of the things the model deliberately excludes",
   "The model has been proved wrong in all cases",
   "Transport costs do not exist where subsidies are paid",
   "The crop must in fact be highly perishable",
   "Subsidies always reinforce the model's predictions"], ans=0,
   why="EK PSO-5.D.1 says the model helps to explain rural land use by emphasizing transport costs, which is a claim about one force among several. A payment that alters the return on distant land changes the outcome without touching the mechanism the model describes."),

 dict(q="Why do geographers still use a model whose assumptions no landscape satisfies?", choices=[
   "The departures from its prediction are themselves informative, since each one points to whichever assumption the real landscape breaks",
   "Because no better explanation of any kind exists",
   "Because the assumptions are actually satisfied in most regions",
   "Because the framework requires the model to be used",
   "Because the model makes no predictions that could fail"], ans=0,
   why="EK PSO-5.D.1 pairs the model with an explicit exception, which is the framework itself treating a mismatch as information. A prediction that fails in a stated way tells a geographer where to look, which a description with no prediction never does."),

 dict(q="Which model explains the location of MANUFACTURING rather than of agriculture?", choices=[
   "Weber's least cost theory",
   "Von Thunen's model of rural land use",
   "The demographic transition model",
   "The concentric zone model of urban structure",
   "The rank-size rule"], ans=0,
   why="EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing, while EK PSO-5.D.1 gives von Thunen's model as the explanation of rural land use. The two share a logic of transport cost and differ in what they locate."),

 dict(q="What does the model predict about the value of farmland as distance from the market increases?", choices=[
   "It falls, because the return a producer can obtain there is reduced by the cost of reaching the market",
   "It rises, because distant land is scarcer",
   "It remains constant in every ring",
   "It falls at first and then rises again beyond the outer ring",
   "It depends only on the soil and not on the location"], ans=0,
   why="EK PSO-5.D.1 explains rural land use through transportation costs associated with distance from the market. What a producer will pay for a site is what the site can earn, and every kilometre of distance subtracts transport cost from that earning."),

 dict(q="A region of vineyards and olive groves lies far outside the ring the model would place it in, and it thrives. Which part of the framework's statement covers this?", choices=[
   "The caveat that regions of specialty farming do not always conform to the concentric rings",
   "The claim that transportation costs are unimportant",
   "The claim that the model applies only at the global scale",
   "The claim that the model explains all rural land use exactly",
   "Nothing in the statement covers it"], ans=0,
   why="EK PSO-5.D.1 names specialty farming regions as the exception in the same sentence that states the model. Where a product is tied to a particular climate or soil, or sells on the reputation of its place, the value of that specific location can outweigh the penalty of distance."),

 dict(q="How does the model's logic apply WITHIN a single large farm?", choices=[
   "The fields nearest the farmstead receive the most attention and the most intensive use, because the cost of reaching them is lowest",
   "It does not apply below the scale of a whole region",
   "The most distant fields receive the most intensive use",
   "All fields on one farm are worked identically",
   "The logic applies only to fields that grow perishable crops"], ans=0,
   why="Learning objective PSO-5.D asks how the model explains agricultural production at various scales, and the mechanism of EK PSO-5.D.1 is the cost of covering distance. A farmyard is a market for labour and manure in the same way a town is a market for produce."),

 dict(q="Perishability and weight both raise transport cost. How do they differ in their effect?", choices=[
   "Perishability limits the TIME a product can spend travelling while weight raises the cost of each kilometre, so the two can place different products at the same distance for different reasons",
   "They are the same property under two names",
   "Weight limits time and perishability raises cost per kilometre",
   "Neither affects where a product is produced",
   "Perishability affects only livestock and weight only crops"], ans=0,
   why="EK PSO-5.D.1 emphasizes transportation costs associated with distance, and distance imposes both a bill and a delay. A product that spoils in a day and a product too heavy to be worth carrying both end up near the market, but a technology that solves one does not solve the other."),

 dict(q="A fast road is built outward from the market in one direction only. What does the model predict for land use along it?", choices=[
   "Uses that were confined near the market extend outward along the road, producing a lobe rather than a circle",
   "Land use along the road becomes less intensive than elsewhere at the same distance",
   "The rings remain perfect circles",
   "Farming ceases along the road",
   "The road has no effect, since the model concerns only soil"], ans=0,
   why="EK PSO-5.D.1 makes transportation cost the model's central variable, so the geometry of the result follows the geography of transport. Where the cost of distance is reduced along one line, the effective distance shrinks in that direction and the bands stretch to match."),

 dict(q="Net profit per hectare for three land uses at different distances from a market is recorded below. Using the accompanying figures, which use occupies the land 40 kilometres from the market?",
   table=dict(headers=["Distance from market (kilometres)", "Dairying (currency units per hectare)", "Grain (currency units per hectare)", "Ranching (currency units per hectare)"],
     rows=[["0", "800", "350", "150"],
           ["20", "480", "270", "130"],
           ["40", "160", "190", "110"],
           ["60", "-160", "110", "90"],
           ["80", "-480", "30", "70"]]),
   choices=[
   "Grain, which returns 190 there against 160 for dairying and 110 for ranching",
   "Dairying, which returns most at every distance shown",
   "Ranching, which declines most slowly and so returns most at 40 kilometres",
   "None of the three, since all returns are negative at 40 kilometres",
   "All three equally, since each returns a positive amount"], ans=0,
   why="At forty kilometres the three returns are 160, 190 and 110 currency units, so the middle use returns most there, although it is beaten nearer the market and overtaken further out. EK PSO-5.D.1 explains rural land use by transportation costs associated with distance, and a use that wins only in a middle band is what that produces."),

 dict(q="Transport cost per tonne-kilometre for five farm products is recorded below. Using the accompanying figures, what order does the model predict from the market outward?",
   table=dict(headers=["Product", "Transport cost (currency units per tonne-kilometre)"],
     rows=[["Fresh vegetables", "1.20"],
           ["Fresh milk", "0.90"],
           ["Firewood and timber", "0.60"],
           ["Wheat", "0.10"],
           ["Live cattle", "0.03"]]),
   choices=[
   "Fresh vegetables nearest at 1.20 and live cattle furthest at 0.03, with the others in falling order of transport cost between them",
   "Live cattle nearest and fresh vegetables furthest",
   "Wheat nearest, since it is the most widely grown",
   "All five at the same distance, since all can be transported",
   "Firewood furthest, since it is the heaviest product listed"], ans=0,
   why="The five costs fall from 1.20 to 0.03 currency units per tonne-kilometre, and the model places the product that suffers most per kilometre nearest the market. EK PSO-5.D.1 emphasizes transportation costs associated with distance, so the predicted order outward is simply the cost ranking reversed."),

 dict(q="Predicted and observed land uses in four zones around one market are recorded below. Using the accompanying record, what does the comparison show?",
   table=dict(headers=["Zone", "Distance from market (kilometres)", "Use the model predicts", "Use observed"],
     rows=[["Zone 1", "12", "Market gardening", "Market gardening"],
           ["Zone 2", "45", "Field crops", "Field crops"],
           ["Zone 3", "70", "Grazing", "Vineyards and olive groves"],
           ["Zone 4", "95", "Grazing", "Grazing"]]),
   choices=[
   "Three of the four zones match the prediction and the one that does not is a specialty farming region, which is the exception the framework itself names",
   "None of the four zones matches the prediction",
   "All four zones match the prediction exactly",
   "The zone that does not match lies nearest the market",
   "The record shows the model failing for grazing in particular"], ans=0,
   why="Three zones record the predicted use and the fourth records vineyards and olive groves where grazing was predicted, which is a specialty farming region rather than a random mismatch. EK PSO-5.D.1 states the model and then says in the same sentence that regions of specialty farming do not always conform to the concentric rings."),

 dict(q="What limitation should be stated when using a single market's observed land uses to test the model?", choices=[
   "One market's landscape cannot separate the effect of distance from the effects of soil, terrain and policy, since all of them vary across the same ground",
   "Observed land uses cannot be recorded accurately anywhere",
   "The model makes no predictions that could be compared with observation",
   "A single agreement between prediction and observation proves the model",
   "The framework forbids testing models against observation"], ans=0,
   why="EK PSO-5.D.1 says the model HELPS TO EXPLAIN rural land use, which concedes that other influences are present. The model's assumptions hold soil, terrain and policy constant, and a real landscape does not, so agreement and disagreement are each consistent with more than one cause."),

 dict(q="Which sentence states both halves of what the framework says about this model?", choices=[
   "Transportation cost rising with distance from the market explains much of the arrangement of rural land use, but specialty farming regions do not always fit the concentric rings",
   "Transportation cost explains the arrangement of rural land use completely and without exception",
   "The model has been superseded and explains nothing about rural land use",
   "The model concerns soil fertility rather than transportation cost",
   "Specialty farming regions are the only land uses the model explains"], ans=0,
   why="EK PSO-5.D.1 makes exactly these two claims in one sentence, joined by 'however'. Dropping either half misstates the framework, and the exception it names is specific -- specialty farming regions -- rather than a general disclaimer."),
]
