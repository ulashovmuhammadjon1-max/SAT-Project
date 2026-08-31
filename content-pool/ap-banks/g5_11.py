# AP HUMAN GEOGRAPHY 5.11 Challenges of Contemporary Agriculture -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding IMP-5, "Agricultural
# production and consumption patterns vary in different locations, presenting
# different environmental, social, economic, and cultural opportunities and
# challenges." Learning objective IMP-5.B, "Explain challenges and debates
# related to the changing nature of contemporary agriculture and food-production
# practices."
#
# Essential knowledge -- four statements, and this is the largest topic in the
# unit:
#   IMP-5.B.1  Agricultural innovations such as biotechnology, genetically
#              modified organisms, and aquaculture have been accompanied by
#              debates over sustainability, soil and water usage, reductions in
#              biodiversity, and extensive fertilizer and pesticide use.
#   IMP-5.B.2  Patterns of food production and consumption are influenced by
#              movements relating to individual food choice, such as urban
#              farming, community-supported agriculture (CSA), organic farming,
#              value-added specialty crops, fair trade, local-food movements,
#              and dietary shifts.
#   IMP-5.B.3  Challenges of feeding a global population include lack of food
#              access, as in cases of food insecurity and food deserts; problems
#              with distribution systems; adverse weather; and land use lost to
#              suburbanization.
#   IMP-5.B.4  The location of food-processing facilities and markets, economies
#              of scale, distribution systems, and government policies all have
#              economic effects on food-production practices.
#
# THE OBJECTIVE'S WORD IS "DEBATES" AND IMP-5.B.1 SAYS "ACCOMPANIED BY". Neither
# the CED nor this module takes a side on biotechnology, genetically modified
# organisms or aquaculture. Every item on that statement is keyed either to what
# the innovation IS or to what the recorded debate is ABOUT -- never to whether
# the innovation is good. Items 3, 4 and 6 are written that way deliberately, and
# a key asserting that a contested technology is safe or harmful would be
# teaching a position the framework does not hold.
#
# IMP-5.B.3'S FIRST CHALLENGE IS THE ONE STUDENTS MISREAD. It is LACK OF FOOD
# ACCESS, not lack of food. The statement's own examples -- food insecurity and
# food deserts -- are both about people who cannot reach or afford food that
# exists, and the statement names problems with DISTRIBUTION SYSTEMS separately
# from any shortfall in production. Items 17, 18, 19 and 26 all rest on that
# distinction, which is also why item 26's data item measures distance and
# vehicle access rather than the size of a harvest.
#
# IMP-5.B.2 IS THE DEMAND SIDE and its qualifier matters: these are movements
# relating to INDIVIDUAL FOOD CHOICE. They work by changing what people buy, so
# they alter production through the market rather than through regulation. Item
# 15 keys on that, and items 8 to 14 walk the CED's own list of seven.
#
# IMP-5.B.4 IS THE SUPPLY SIDE, and it is a list of four economic forces acting
# on production practices: where processing and markets are, economies of scale,
# distribution systems, and government policy. Items 22 to 24 and 25 separate
# them.
#
# SYNONYM CARE. `geo_check` treats {"genetically modified organisms", "gmos"} as
# one construct and {"community-supported agriculture", "csa"} as another. The
# CED pairs each abbreviation with its expansion, so where the statement is
# quoted both appear inside a SINGLE choice and never as two competing options.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.11", "Challenges of Contemporary Agriculture", 5)

QUESTIONS = [
 dict(q="Which agricultural innovations does the framework name as having been accompanied by debate?", choices=[
   "Biotechnology, genetically modified organisms (GMOs), and aquaculture",
   "Terraces, irrigation, and draining wetlands",
   "Urban farming, fair trade, and local-food movements",
   "Metes and bounds, township and range, and long lot",
   "Food insecurity, food deserts, and adverse weather"], ans=0,
   why="EK IMP-5.B.1 names exactly biotechnology, genetically modified organisms and aquaculture. Terraces and irrigation are landscape-altering practices in EK IMP-5.A.2, urban farming and fair trade are food-choice movements in EK IMP-5.B.2, and food deserts are challenges in EK IMP-5.B.3."),

 dict(q="Which set of debates does the framework say has accompanied those innovations?", choices=[
   "Sustainability, soil and water usage, reductions in biodiversity, and extensive fertilizer and pesticide use",
   "Settlement patterns, survey methods, and land tenure",
   "Rank-size rule, primate cities, and central place theory",
   "Tariffs, subsidies, and trade agreements",
   "Sustainability, urban farming, and dietary shifts"], ans=0,
   why="EK IMP-5.B.1 names exactly these four areas of debate. Urban farming and dietary shifts belong to EK IMP-5.B.2's list of food-choice movements rather than to the debates over innovation, which is what the last option confuses."),

 dict(q="What is a genetically modified organism in agriculture, and what does the framework say about it?", choices=[
   "An organism whose genetic material has been altered by direct intervention, which the framework records as an innovation accompanied by debate rather than as settled",
   "An organism produced by ordinary selective breeding over many generations",
   "An organism the framework identifies as unsafe",
   "An organism the framework identifies as entirely safe",
   "An organism that cannot be used in farming"], ans=0,
   why="EK IMP-5.B.1 lists genetically modified organisms among the innovations that have been ACCOMPANIED BY debates. The framework records the existence of the debate rather than resolving it, so a key asserting either verdict would go beyond the statement."),

 dict(q="What is aquaculture, and why does the framework place it among contested innovations?", choices=[
   "The farming of fish and other aquatic organisms in controlled conditions, which raises questions about water quality, feed sources and the surrounding environment",
   "The catching of wild fish from open water",
   "The irrigation of crops using seawater",
   "The draining of wetlands for cultivation",
   "The use of water to transport agricultural products"], ans=0,
   why="EK IMP-5.B.1 names aquaculture among the innovations accompanied by debates over sustainability, soil and water usage and biodiversity. Farming aquatic species concentrates feed, waste and stock in one place, which is what connects the practice to each of the debates the statement lists."),

 dict(q="How do contemporary agricultural innovations contribute to reductions in biodiversity?", choices=[
   "Planting a narrow set of high-performing varieties over very large areas displaces the many local varieties and the habitats that were there before",
   "Innovations create new species, which reduces the number of existing ones",
   "Reductions in biodiversity occur only in oceans",
   "Biodiversity falls because fewer farmers are employed",
   "The framework denies that biodiversity has been affected"], ans=0,
   why="EK IMP-5.B.1 names reductions in biodiversity among the debates accompanying agricultural innovation. Uniformity is what a high-performing variety spreads, and uniformity across a landscape is the opposite of the diversity the debate is about."),

 dict(q="Why does the framework list soil and water usage as a subject of debate about agricultural innovation?", choices=[
   "Higher-output systems generally draw more heavily on soil and water, so whether the gain can be sustained at that draw is genuinely disputed",
   "Because innovation removes the need for soil and water entirely",
   "Because soil and water are unaffected by farming methods",
   "Because the framework has settled the question against innovation",
   "Because soil and water usage concerns only aquaculture"], ans=0,
   why="EK IMP-5.B.1 names soil and water usage among the debates accompanying innovations such as biotechnology and aquaculture. The word 'debates' is the framework's own, so the item is keyed to what is contested rather than to a verdict on it."),

 dict(q="Which movements does the framework name as relating to individual food choice?", choices=[
   "Urban farming, community-supported agriculture (CSA), organic farming, value-added specialty crops, fair trade, local-food movements, and dietary shifts",
   "Biotechnology, genetically modified organisms, and aquaculture",
   "Food insecurity, food deserts, and adverse weather",
   "Economies of scale, distribution systems, and government policies",
   "Slash and burn, terraces, and pastoral nomadism"], ans=0,
   why="EK IMP-5.B.2 names exactly these seven movements. Each of the other options is drawn from a different statement in this topic or from EK IMP-5.A.2, and telling the four lists apart is most of what this topic asks."),

 dict(q="What is urban farming, and why does it appear on the framework's list?", choices=[
   "Growing food within a city, on rooftops, vacant lots and community plots, which shortens the distance between production and consumption",
   "Farming carried out only in rural districts near cities",
   "The purchase of rural farmland by city residents",
   "The construction of food-processing plants inside cities",
   "The sale of farm products in urban markets"], ans=0,
   why="EK IMP-5.B.2 names urban farming among the movements relating to individual food choice that influence patterns of food production and consumption. Producing inside the place of consumption is a direct reversal of the long chains described in EK PSO-5.E.1."),

 dict(q="How does community-supported agriculture change the relationship between a farm and its customers?", choices=[
   "Customers buy a share of a season's harvest in advance, so they take on part of the risk and the farm has income before the crop exists",
   "Customers buy produce at a supermarket owned by the farm",
   "Customers work full-time on the farm without payment",
   "Customers lend the farm money at interest",
   "Customers vote on which crops the government will subsidize"], ans=0,
   why="EK IMP-5.B.2 names community-supported agriculture among the movements relating to individual food choice. Paying before the harvest moves both the risk and the cash flow, which is what distinguishes the arrangement from simply buying local produce."),

 dict(q="What does organic farming's place on the framework's list indicate about how such movements work?", choices=[
   "They change what is produced by changing what consumers choose to buy, rather than by regulation",
   "They change what is produced by government order",
   "They have no effect on production patterns",
   "They apply only to food that is exported",
   "They operate by reducing the total food supply"], ans=0,
   why="EK IMP-5.B.2 describes these as movements relating to INDIVIDUAL FOOD CHOICE that influence patterns of food production and consumption. The route from the movement to the field runs through the market, which is what makes them demand-side rather than policy changes."),

 dict(q="What is a value-added specialty crop?", choices=[
   "A crop grown or processed for a particular quality that commands a higher price than the ordinary commodity version of it",
   "A crop grown in the largest possible volume at the lowest possible cost",
   "A crop that cannot be sold at any price",
   "A crop grown only for the household's own consumption",
   "A crop whose price is fixed by government"], ans=0,
   why="EK IMP-5.B.2 names value-added specialty crops among the movements relating to individual food choice. The strategy is the direct opposite of competing on cost per tonne, which is why it is a route by which a small producer survives beside a large one."),

 dict(q="What does fair trade attempt to change about a commodity chain?", choices=[
   "The share of the final price that reaches the producer, and the conditions under which the crop is grown",
   "The physical route the product takes to market",
   "The climate in which the crop is grown",
   "The number of crops a farm may grow",
   "The tariff a government charges on imports"], ans=0,
   why="EK IMP-5.B.2 names fair trade among the movements relating to individual food choice, and EK PSO-5.E.1 places agricultural products in a global supply chain. The movement works on how the value in that chain is divided, using the willingness of buyers to pay more as its lever."),

 dict(q="What is the central claim of a local-food movement?", choices=[
   "That food produced nearer to where it is eaten carries advantages in freshness, transport impact and support for the local economy",
   "That imported food is unsafe to eat",
   "That all agriculture should be subsistence agriculture",
   "That farms should grow only a single crop",
   "That food should be distributed by government rather than sold"], ans=0,
   why="EK IMP-5.B.2 names local-food movements among the movements relating to individual food choice. The claim is comparative rather than absolute, and it is what makes the movement a counter-current to the long chains of EK PSO-5.E.1."),

 dict(q="How can dietary shifts change agricultural production patterns across whole regions?", choices=[
   "A change in what people choose to eat changes what is worth growing, and the land, water and feed requirements of the new diet may be quite different",
   "Dietary shifts affect consumers only and never producers",
   "Dietary shifts change the climate of producing regions",
   "Dietary shifts affect only imported foods",
   "Dietary shifts have no effect until governments act"], ans=0,
   why="EK IMP-5.B.2 names dietary shifts among the movements influencing patterns of food production AND consumption. Demand is what makes a crop worth planting, so a sustained change in diet reorganizes production wherever the market reaches."),

 dict(q="What do all seven of the framework's food-choice movements have in common?", choices=[
   "Each works by changing what individuals decide to buy or eat, and reaches production through that demand",
   "Each is imposed by national legislation",
   "Each reduces the total quantity of food produced",
   "Each applies only to grain crops",
   "Each operates only in low-income countries"], ans=0,
   why="EK IMP-5.B.2 describes them as movements relating to individual food choice that influence patterns of food production and consumption. That common mechanism is what puts them on one list despite their differences in aim and scale."),

 dict(q="Which challenges of feeding a global population does the framework name?", choices=[
   "Lack of food access, problems with distribution systems, adverse weather, and land use lost to suburbanization",
   "Biotechnology, genetically modified organisms, and aquaculture",
   "Urban farming, fair trade, and organic farming",
   "Economies of scale and the location of processing facilities",
   "Terraces, irrigation, and shifting cultivation"], ans=0,
   why="EK IMP-5.B.3 names exactly these four challenges. The other options belong to EK IMP-5.B.1's innovations, EK IMP-5.B.2's movements, EK IMP-5.B.4's economic forces and EK IMP-5.A.2's landscape practices respectively."),

 dict(q="What is food insecurity?", choices=[
   "Not having reliable access to enough safe and nutritious food, which can occur in a country whose farms produce a surplus",
   "A national shortage of food caused by crop failure alone",
   "The absence of any agriculture in a region",
   "A dislike of the food available locally",
   "The export of more food than a country produces"], ans=0,
   why="EK IMP-5.B.3 names lack of food access, as in cases of food insecurity and food deserts, among the challenges of feeding a global population. The framework's word is ACCESS, so the condition is about reach and affordability rather than about the size of the harvest."),

 dict(q="What is a food desert?", choices=[
   "An area whose residents have little practical access to affordable fresh food, usually because the nearest full grocer is far away and transport is limited",
   "An arid region where no crops can be grown",
   "A district where farming has been abandoned",
   "A country that imports all of its food",
   "A neighbourhood where residents choose not to cook"], ans=0,
   why="EK IMP-5.B.3 gives food deserts as an example of lack of food access. The word 'desert' refers to the absence of food retail rather than to any physical aridity, which is why food deserts occur in the middle of well-supplied cities."),

 dict(q="Why does the framework list problems with distribution systems separately from any shortfall in production?", choices=[
   "Food can exist in quantity and still not reach the people who need it, so a distribution failure is a distinct cause of hunger",
   "Because distribution systems affect only exports",
   "Because production shortfalls never occur",
   "Because distribution and production are the same thing",
   "Because distribution problems affect only wealthy countries"], ans=0,
   why="EK IMP-5.B.3 names problems with distribution systems alongside lack of food access as challenges of feeding a global population. Listing them separately from the harvest is the framework distinguishing between food that does not exist and food that does not arrive."),

 dict(q="Why does the framework name adverse weather among the challenges of feeding a global population?", choices=[
   "Drought, flood, heat and storm reduce harvests in particular places and particular years, and a specialized global system transmits that shortfall to prices everywhere",
   "Because weather affects only local subsistence farming",
   "Because weather is entirely predictable and can be planned for",
   "Because weather affects consumption but not production",
   "Because weather has become uniform across the world"], ans=0,
   why="EK IMP-5.B.3 names adverse weather among the challenges, and EK PSO-5.E.1 places food in a global supply chain. A harvest is a biological outcome exposed to conditions no one controls, and a chain that links producers to distant buyers passes the shortfall along."),

 dict(q="Why does the framework count land use lost to suburbanization as a challenge of feeding a global population?", choices=[
   "Cities expand onto the flat, well-watered land near them, which is often the best farmland, and the conversion is effectively permanent",
   "Because suburbs consume more food than cities",
   "Because suburban residents refuse to buy farm products",
   "Because farmland is lost only to forest regrowth",
   "Because suburbanization occurs only in regions with poor soil"], ans=0,
   why="EK IMP-5.B.3 names land use lost to suburbanization among the challenges of feeding a global population. Cities were founded where farming was good, so expansion takes the best available land first, and building on soil is one of the few land-use changes that cannot readily be reversed."),

 dict(q="Which economic forces does the framework say have effects on food-production practices?", choices=[
   "The location of food-processing facilities and markets, economies of scale, distribution systems, and government policies",
   "Urban farming, fair trade, and dietary shifts",
   "Food insecurity, food deserts, and adverse weather",
   "Biotechnology, genetically modified organisms, and aquaculture",
   "Clustered, dispersed, and linear settlement patterns"], ans=0,
   why="EK IMP-5.B.4 names exactly these four. Distinguishing this list from the food-choice movements of EK IMP-5.B.2 is the point: those work through what consumers buy, while these work through the cost and organization of producing."),

 dict(q="How does the location of a food-processing facility affect what farmers around it grow?", choices=[
   "A crop that must be processed soon after harvest can be grown profitably only within reach of a plant, so the plant's location concentrates that crop around it",
   "Processing facilities have no effect on planting decisions",
   "Farmers grow whatever the facility processes regardless of distance",
   "The facility determines the climate of the surrounding district",
   "Processing facilities affect only the price of machinery"], ans=0,
   why="EK IMP-5.B.4 names the location of food-processing facilities and markets among the economic influences on food-production practices. Where a crop must reach a plant within hours, the plant's catchment is a hard boundary on where planting that crop makes sense."),

 dict(q="How can government policy change food-production practices without ordering any farmer to do anything?", choices=[
   "A subsidy, a tariff or a standard changes what is profitable, and farmers respond to the altered returns",
   "Government policy affects only imported food",
   "Government policy has no economic effect on farming",
   "Government policy works only by direct command",
   "Government policy applies only to food processing"], ans=0,
   why="EK IMP-5.B.4 names government policies among the economic forces bearing on food-production practices. Policy that works on prices leaves the decision with the farmer while changing which decision pays, which is why its effects appear as a shift in what is grown."),

 dict(q="Which pairing of a case with the framework statement it belongs to is CORRECT?", choices=[
   "A neighbourhood five kilometres from the nearest grocer, matched to lack of food access",
   "A subsidy that makes one crop more profitable, matched to individual food choice",
   "A household buying a share of a farm's harvest in advance, matched to adverse weather",
   "Debate over the water use of a fish farm, matched to distribution systems",
   "Suburban housing built on prime farmland, matched to agricultural innovation"], ans=0,
   why="EK IMP-5.B.1 to EK IMP-5.B.4 divide this topic into innovations and their debates, food-choice movements, challenges of feeding a global population, and economic forces on production. Only one pairing here places its case under the statement that actually covers it."),

 dict(q="Four neighbourhoods in one city are recorded below. Using the accompanying figures, which best fits the framework's description of a food desert?",
   table=dict(headers=["Neighbourhood", "Distance to nearest full grocery store (kilometres)", "Households with a vehicle (%)", "Households below the poverty line (%)"],
     rows=[["Neighbourhood 1", "0.4", "78", "9"],
           ["Neighbourhood 2", "3.8", "31", "34"],
           ["Neighbourhood 3", "0.9", "66", "15"],
           ["Neighbourhood 4", "4.6", "24", "41"]]),
   choices=[
   "Neighbourhood 4, which is 4.6 kilometres from a full grocery store with only 24 percent of households holding a vehicle",
   "Neighbourhood 1, which is nearest to a grocery store",
   "Neighbourhood 3, which has an intermediate poverty rate",
   "Neighbourhood 2, because 3.8 kilometres is the greatest distance recorded",
   "All four equally, since each contains households below the poverty line"], ans=0,
   why="One neighbourhood records both the greatest distance to a full grocery store and the lowest rate of vehicle access, and it also has the highest poverty rate, so distance and the means to cover it point the same way. EK IMP-5.B.3 gives food deserts as an example of lack of food ACCESS, which is what those three columns together measure."),

 dict(q="The sources of one country's fish supply are recorded below. Using the accompanying figures, what has occurred?",
   table=dict(headers=["Year", "Share from aquaculture (%)", "Share from wild capture (%)"],
     rows=[["1990", "13", "87"],
           ["2000", "26", "74"],
           ["2010", "40", "60"],
           ["2020", "49", "51"]]),
   choices=[
   "The aquaculture share rose from 13 to 49 percent while wild capture fell from 87 to 51, so farmed fish has grown from a small fraction to nearly half the supply",
   "The aquaculture share fell across the period",
   "Wild capture rose while aquaculture fell",
   "Aquaculture exceeded half of the supply by 2020",
   "The two shares were equal in every year recorded"], ans=0,
   why="The two columns sum to 100 in every year, so the record is about composition, and the farmed share rises at every step from 13 to 49 percent without passing half. EK IMP-5.B.1 names aquaculture among the agricultural innovations accompanied by debate, and a share approaching half is why those debates matter."),

 dict(q="Farmland converted to developed use in one region is recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Decade", "Farmland converted to developed use (hectares)", "Share of the region's prime farmland converted (%)"],
     rows=[["1980s", "210,000", "2.1"],
           ["1990s", "340,000", "3.5"],
           ["2000s", "290,000", "3.1"],
           ["2010s", "250,000", "2.8"]]),
   choices=[
   "About 1,090,000 hectares were converted across the four decades, amounting to 11.5 percent of the region's prime farmland",
   "Conversion rose in every decade recorded",
   "Conversion stopped entirely after the 1990s",
   "Less than 1 percent of prime farmland was converted in total",
   "The 1980s recorded the largest conversion of the four decades"], ans=0,
   why="The four decadal figures sum to 1,090,000 hectares and the four shares sum to 11.5 percent, while the largest single decade is the 1990s rather than the 1980s and conversion continues in every decade shown. EK IMP-5.B.3 names land use lost to suburbanization among the challenges of feeding a global population, and a cumulative total is how that loss is properly stated."),

 dict(q="What limitation should be stated when using distance to a grocery store to identify food deserts?", choices=[
   "Distance alone does not settle access, since transport, income, opening hours and what the nearest store actually stocks all bear on whether food can be obtained",
   "Distances between places cannot be measured",
   "Kilometres and percentages can never appear in the same record",
   "A neighbourhood far from a store is by definition a food desert",
   "The framework forbids quantitative work on food access"], ans=0,
   why="EK IMP-5.B.3 names food deserts as a case of lack of food ACCESS rather than of distance. A short walk without money and a long drive with a car are different situations, so a distance figure is one input to the judgement rather than the judgement itself."),

 dict(q="A revision guide must distinguish this topic's four statements in one sentence each. Which set of descriptions is accurate?", choices=[
   "Innovations and the debates accompanying them; movements working through individual food choice; challenges of feeding a global population; and economic forces acting on production practices",
   "Four separate lists of environmental damage caused by farming",
   "Four descriptions of rural settlement patterns",
   "Four accounts of the Green Revolution's consequences",
   "Innovations, survey methods, settlement patterns, and climate regions"], ans=0,
   why="EK IMP-5.B.1 covers innovations and their debates, EK IMP-5.B.2 the demand-side movements, EK IMP-5.B.3 the challenges of feeding a global population, and EK IMP-5.B.4 the economic forces on production. Keeping the four apart is what the topic's structure asks a student to be able to do."),
]
