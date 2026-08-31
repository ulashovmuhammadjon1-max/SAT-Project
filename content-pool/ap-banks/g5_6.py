# AP HUMAN GEOGRAPHY 5.6 Agricultural Production Regions -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding PSO-5, "Availability
# of resources and cultural practices influence agricultural practices and
# land-use patterns." Learning objective PSO-5.C, "Explain how economic forces
# influence agricultural practices."
#
# Essential knowledge -- the two statements assigned to this topic:
#   PSO-5.C.1  Agricultural production regions are defined by the extent to
#              which they reflect subsistence or commercial practices
#              (monocropping or monoculture).
#   PSO-5.C.2  Intensive and extensive farming practices are determined in part
#              by land costs (bid-rent theory).
#
# TWO HEDGES, AND THEY DECIDE THE MODULE.
#
# First, "THE EXTENT TO WHICH". PSO-5.C.1 does not sort regions into a
# subsistence box and a commercial box; it says regions are defined by the
# DEGREE to which they reflect one or the other. That makes the classification a
# spectrum with real cases in the middle -- a household that eats most of what
# it grows and sells a small surplus is neither purely one nor the other. Items
# 6, 17, 24 and 30 rest on this.
#
# Second, "DETERMINED IN PART BY". PSO-5.C.2 attributes intensity to land costs
# only partly, which is right: climate, soil, perishability, labour supply and
# government policy all bear on it too. An item keyed as though rent alone fixed
# the practice would be overstating the sentence, so items 11 and 21 key against
# that reading directly.
#
# BID-RENT THEORY, since the CED names it without explaining it. Land near a
# market is scarce and every user wants it, so its rent is bid up. A user who
# earns a great deal from each hectare -- because the crop is high-value, or
# perishable, or must reach the market daily -- can pay that rent and still
# profit; a user earning little per hectare cannot. So the land nearest the
# market goes to the most intensive use, and intensity falls with distance as
# rent falls. The mechanism is COMPETITIVE BIDDING, not a rule about where crops
# grow, and item 10 asks for exactly that.
#
# THE RELATIONSHIP TO TOPIC 5.8. Von Thunen's model is the application of this
# rent gradient to agricultural land use, and it is a separate topic with its own
# statement (PSO-5.D.1). This module keys on the rent mechanism itself and item
# 22 marks the boundary between the two rather than pretending there is none.
#
# SYNONYM CARE. `geo_check` treats {"monocropping", "monoculture"} as one
# construct. The CED's own parenthesis pairs them, so they appear together
# INSIDE a single choice where that is what the statement says, and never as two
# separate choices, which would make an item unanswerable.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.6", "Agricultural Production Regions", 5)

QUESTIONS = [
 dict(q="According to the framework, what defines agricultural production regions?", choices=[
   "The extent to which they reflect subsistence or commercial practices",
   "The climate zone in which they lie",
   "The number of people who live in them",
   "The survey method used to divide their land",
   "The political boundaries that enclose them"], ans=0,
   why="EK PSO-5.C.1 states that agricultural production regions are defined by the extent to which they reflect subsistence or commercial practices. Climate and land division influence what is farmed, but the framework's defining criterion here is economic: who the output is for."),

 dict(q="What is subsistence agriculture?", choices=[
   "Farming carried on primarily to feed the household and community that grows the food",
   "Farming carried on primarily to sell the output for money",
   "Farming that uses no labour at all",
   "Farming that occurs only in cold climates",
   "Farming that produces a single crop for export"], ans=0,
   why="EK PSO-5.C.1 contrasts subsistence with commercial practices as the two poles defining production regions. The distinction is about the destination of the output rather than about the technology used or the size of the holding."),

 dict(q="What is commercial agriculture?", choices=[
   "Farming carried on primarily to sell the output, so the household's income rather than its diet depends on the harvest",
   "Farming carried on primarily to feed the household that grows the food",
   "Farming that uses only hand tools",
   "Farming practised only near the equator",
   "Farming that produces many different crops on a small plot"], ans=0,
   why="EK PSO-5.C.1 names commercial practices as one of the two poles by which production regions are defined. Once output is sold rather than eaten, price, transport cost and market access begin to govern what is grown, which is why the economic forces of PSO-5.C are the subject of this topic."),

 dict(q="What does the framework's parenthesis 'monocropping or monoculture' describe?", choices=[
   "The growing of a single crop, or a very narrow range of crops, across a large area",
   "The growing of many different crops on one small plot",
   "The rearing of livestock without any crops",
   "The abandonment of farmland to natural vegetation",
   "The division of a farm into scattered strips"], ans=0,
   why="EK PSO-5.C.1 attaches the parenthesis to commercial practices, and both words name the same thing: one crop over a wide area. Specialization of that kind makes sense only when the crop is sold, since a household that ate only what it grew could not live on a single crop."),

 dict(q="Why does the framework attach monocropping to COMMERCIAL rather than to subsistence practice?", choices=[
   "A household that ate only what it grew would need a varied range of crops, while a farm selling its crop can specialize in whichever one pays best",
   "Because subsistence farmers are forbidden to grow more than one crop",
   "Because a single crop yields less than several crops",
   "Because commercial farms cannot grow more than one crop",
   "Because monocropping requires a cold climate"], ans=0,
   why="EK PSO-5.C.1 places the parenthesis beside commercial practices. Selling the harvest converts it into money that will buy anything, which removes the requirement that the farm itself supply a complete diet and allows specialization in whatever the land and market favour."),

 dict(q="What follows from the framework's phrase 'the EXTENT TO WHICH' regions reflect subsistence or commercial practices?", choices=[
   "The classification is a spectrum, so a region can be partly subsistence and partly commercial rather than wholly one or the other",
   "Every region is entirely subsistence or entirely commercial",
   "The classification applies only to regions that sell nothing",
   "Regions cannot be classified in these terms at all",
   "Only commercial regions count as production regions"], ans=0,
   why="EK PSO-5.C.1's wording is deliberately about degree rather than category. Households that eat most of what they grow and sell a modest surplus are extremely common, and a two-box classification would have nowhere to put them."),

 dict(q="What does bid-rent theory say about the price of land?", choices=[
   "Land nearer a market commands a higher rent, because more users compete for it, and rent falls with distance from the market",
   "Land far from a market commands a higher rent because it is more plentiful",
   "All agricultural land commands the same rent regardless of location",
   "Rent depends only on the fertility of the soil",
   "Rent rises with distance from the market at a constant rate"], ans=0,
   why="EK PSO-5.C.2 names bid-rent theory as the account of how land costs bear on farming practice. The theory is about competition: a site everyone wants goes to whoever will pay most for it, and proximity to a market is the quality being competed for."),

 dict(q="According to bid-rent reasoning, what kind of farming occupies land closest to a market?", choices=[
   "The most intensive uses, since only a high return per hectare can cover a high rent per hectare",
   "The most extensive uses, since they need the most land",
   "Whichever use arrived in the region first",
   "The use with the lowest labour requirement",
   "Land closest to a market is never farmed"], ans=0,
   why="EK PSO-5.C.2 says intensive and extensive practices are determined in part by land costs. A hectare that costs a great deal must earn a great deal, and only a use that works each hectare hard can do so, which is why intensity is highest where rent is highest."),

 dict(q="According to bid-rent reasoning, what kind of farming occupies land far from a market?", choices=[
   "Extensive uses, since low rents make it affordable to spread modest returns over a large area",
   "Intensive uses, since distance requires more labour",
   "Only market gardening, since it can be transported furthest",
   "No farming at all, since distant land has no value",
   "Whichever use pays the highest rent overall"], ans=0,
   why="EK PSO-5.C.2 attributes the intensive-extensive division in part to land costs. Where a hectare is cheap, a use earning little from each hectare is still viable, and land can substitute for the labour and capital an intensive system would require."),

 dict(q="What is the actual mechanism by which bid-rent produces a pattern of land uses around a market?", choices=[
   "Competing users each offer what a site is worth to them, and the site goes to the highest bidder, so uses sort themselves by how much each can pay at each distance",
   "A planning authority assigns each crop to a distance band",
   "Farmers choose their distance at random",
   "The most fertile land is always nearest the market",
   "Each crop can physically grow only at one particular distance"], ans=0,
   why="EK PSO-5.C.2 names bid-rent theory, and bidding is the process in the name. Nothing prevents wheat from growing beside a city; what happens is that a use earning more per hectare outbids it there, so the observed pattern is the outcome of an auction rather than of a rule."),

 dict(q="The framework says intensive and extensive practices are determined IN PART by land costs. What does that qualification concede?", choices=[
   "That other factors -- climate, soil, perishability, labour supply and policy -- also bear on how intensively land is farmed",
   "That land costs have no effect on farming practice",
   "That land costs are the only factor of any importance",
   "That the theory applies only to commercial regions",
   "That intensity cannot be explained at all"], ans=0,
   why="EK PSO-5.C.2's phrase 'in part' is a real hedge. A rent gradient explains a great deal about where intensity is found, but a frost-free winter, a deep soil or a subsidy can each move a practice away from what rent alone would predict."),

 dict(q="A dairy farm supplying fresh milk operates on expensive land ten kilometres from a large city rather than on cheap land two hundred kilometres away. Which reasoning explains this best?", choices=[
   "A perishable product that must reach the market quickly earns enough per hectare near the city to cover the higher rent",
   "Cheap land is always unsuitable for dairy cattle",
   "Dairy farming requires the same rent wherever it occurs",
   "Distant land is too fertile for dairying",
   "Dairy farms are assigned their locations by government"], ans=0,
   why="EK PSO-5.C.2 attributes the intensive-extensive pattern in part to land costs, and perishability is what makes proximity worth paying for. A product that spoils or loses value in transit has a transport cost that rises steeply with distance, which pushes the bid for near land up."),

 dict(q="Wheat is grown on very large holdings four hundred kilometres from the nearest large city. Which reasoning explains this best?", choices=[
   "Wheat earns little per hectare but stores and travels well, so it can afford distance and needs the cheap land that distance provides",
   "Wheat cannot be grown within four hundred kilometres of a city",
   "Wheat earns more per hectare than any other crop",
   "Wheat is the most perishable of crops",
   "Distant land is always more fertile than near land"], ans=0,
   why="EK PSO-5.C.2 says land costs partly determine whether a practice is intensive or extensive. A durable, low-value-per-hectare crop loses the bidding for near land and gains nothing from winning it, so it settles where rent is low enough for an extensive system to pay."),

 dict(q="Four uses bid for one site immediately outside a city. Which is most likely to obtain it, on bid-rent reasoning?", choices=[
   "A grower of perishable salad crops harvesting several times a week for city shops",
   "A cattle ranch running stock on unimproved grass",
   "A wheat farm harvesting once a year",
   "A forestry plantation harvested every thirty years",
   "Land left in permanent fallow"], ans=0,
   why="EK PSO-5.C.2 connects intensity to land costs through bid-rent theory. The use that earns the most from each hectare each year can offer the most for the site, and continuous harvesting of a high-value perishable crop is the highest-earning use of the five."),

 dict(q="Which combination of features is characteristic of a strongly SUBSISTENCE production region?", choices=[
   "A varied range of crops and animals on each holding, most of the output eaten by the household, and little dependence on purchased inputs",
   "A single crop across large holdings, almost all of it sold, and heavy use of purchased inputs",
   "No cultivation of any kind",
   "Farming carried out entirely by machinery with no household labour",
   "Production entirely for export to distant countries"], ans=0,
   why="EK PSO-5.C.1 defines production regions by the extent to which they reflect subsistence or commercial practices. A household eating what it grows must grow a range of things, and it has little cash with which to buy inputs, so diversity and low purchased inputs travel together."),

 dict(q="Which combination of features is characteristic of a strongly COMMERCIAL production region?", choices=[
   "Specialization in one or two crops over large areas, output sold rather than eaten, and reliance on purchased inputs and distant markets",
   "Many crops on each small holding, all of them eaten by the grower",
   "Farming without any connection to a market",
   "Production limited to what one family can consume",
   "Cultivation only of crops that cannot be transported"], ans=0,
   why="EK PSO-5.C.1 attaches monocropping and monoculture to commercial practices. Once the harvest is sold, the farm's own diet no longer constrains what it plants, and specialization plus purchased inputs is the arrangement that follows."),

 dict(q="A district's households eat about two thirds of what they grow and sell the remaining third at a weekly market. How should the district be classified?", choices=[
   "As lying between the two poles, since the framework classifies regions by the extent to which they reflect each kind of practice",
   "As purely subsistence, since some output is eaten",
   "As purely commercial, since some output is sold",
   "As unclassifiable, since the framework recognizes only two categories",
   "As commercial, because a market exists in the district"], ans=0,
   why="EK PSO-5.C.1's phrase 'the extent to which' makes the classification a matter of degree. A district selling a third of its output is doing both things, and forcing it into either pole would discard exactly the information the framework's wording preserves."),

 dict(q="What risk does a region running on monoculture carry that a diversified region does not?", choices=[
   "A single price fall or a single pest can affect the entire region's income at once, because everything depends on one crop",
   "A single crop cannot be sold at all",
   "Monoculture always produces lower yields per hectare",
   "Monoculture prevents the use of machinery",
   "A single crop requires more different kinds of equipment"], ans=0,
   why="EK PSO-5.C.1 names monocropping and monoculture as features of commercial regions, and concentration is what specialization means. Diversity spreads exposure across several markets and several biologies, so removing it raises the return in a good year and the loss in a bad one."),

 dict(q="Why do commercial farms specialize rather than growing a little of everything?", choices=[
   "Specialization allows the equipment, knowledge and marketing to be matched to one crop, which lowers cost per unit sold",
   "Because law requires commercial farms to grow one crop",
   "Because a commercial farm's soil supports only one crop",
   "Because growing several crops is physically impossible on a large farm",
   "Because specialization reduces the total output of the farm"], ans=0,
   why="EK PSO-5.C.1 associates monocropping with commercial practice, and the reason is economic rather than agronomic. A combine, a storage system and a buyer relationship built around one crop are all cheaper per tonne than five of each, which is exactly the pressure a farm selling its output faces."),

 dict(q="At which two scales does the framework's classification of production regions operate?", choices=[
   "At the regional or world scale, where whole areas are described as more subsistence or more commercial, and at the farm scale, where an individual holding sells more or less of what it grows",
   "Only at the global scale, since agriculture is traded internationally",
   "Only at the scale of a single field",
   "At no scale, since the classification is not spatial",
   "Only at the national scale, since governments collect the data"], ans=0,
   why="EK PSO-5.C.1 speaks of production REGIONS, which are areas, while the practice being measured is what an individual farm does with its harvest. A region is more commercial because more of its farms sell more of their output, so the two scales are connected by aggregation."),

 dict(q="A new motorway halves the cost of moving produce to a city. What does bid-rent reasoning predict?", choices=[
   "Distant land becomes more attractive for uses that had been confined to near land, so the pattern of uses stretches outward",
   "Land near the city becomes worthless",
   "No change occurs, since transport cost is unrelated to rent",
   "Every farm switches to subsistence production",
   "Rent rises equally at every distance from the city"], ans=0,
   why="EK PSO-5.C.2 attributes intensity in part to land costs, and land costs near a market reflect what distant land cannot do. Cheaper transport reduces the penalty of distance, which raises what distant land is worth to a use that had needed to be close."),

 dict(q="How does bid-rent theory relate to von Thunen's model of agricultural land use?", choices=[
   "Von Thunen's model is the application of the rent-and-distance relationship to agriculture, producing the concentric arrangement of uses that the model is known for",
   "The two are unrelated theories about different subjects",
   "Bid-rent theory contradicts von Thunen's model",
   "Von Thunen's model concerns industry rather than agriculture",
   "Bid-rent theory applies only to land that is not farmed"], ans=0,
   why="EK PSO-5.C.2 names bid-rent theory as the account of how land costs shape intensity, and EK PSO-5.D.1 gives von Thunen's model as the explanation of rural land use by transportation costs and distance from market. The second is the first worked out for a farming landscape."),

 dict(q="A student classifies production regions by climate zone. What is the objection from the framework?", choices=[
   "The framework defines production regions by the extent to which they reflect subsistence or commercial practices, which is an economic criterion rather than a climatic one",
   "Climate has no influence on agriculture at all",
   "The framework classifies production regions by political boundary",
   "Climate zones cannot be mapped",
   "There is no objection, since climate is the framework's criterion"], ans=0,
   why="EK PSO-5.C.1 supplies the defining criterion in its own words, and it concerns who the output is for. Climate governs what CAN be grown, which EK PSO-5.A.1 covers in a different topic, but it is not what the framework uses to define a production region."),

 dict(q="A household grows enough grain and vegetables to feed itself and sells a few baskets of tomatoes each week for cash to buy salt, cloth and schoolbooks. What is the most accurate reading?", choices=[
   "The household is largely subsistence with a small commercial element, and the cash income buys what the farm itself cannot produce",
   "The household is entirely commercial, since it sells something",
   "The household is entirely subsistence, since it grows most of its food",
   "The household is practising monoculture",
   "The household cannot be described in the framework's terms"], ans=0,
   why="EK PSO-5.C.1 classifies by the extent to which practices are subsistence or commercial, which allows a mixed reading. A small cash income is what converts a self-provisioning farm into a household that can obtain goods no farm produces."),

 dict(q="Why does a strongly commercial production region depend on conditions outside its own boundaries in a way a subsistence region does not?", choices=[
   "Its income depends on prices set elsewhere and on transport and buyers it does not control, so events far away can change what a harvest is worth",
   "Because commercial regions cannot grow their own food at all",
   "Because subsistence regions never trade with anyone",
   "Because commercial regions have no soil of their own",
   "Because prices are fixed permanently by the framework"], ans=0,
   why="EK PSO-5.C.1 defines the commercial pole by the practice of selling output, and a sale requires a buyer somewhere else. A subsistence household's harvest has the same value to it whatever a distant market does, which is the exposure specialization trades away for higher income."),

 dict(q="Rent that three land uses would offer per hectare at different distances from a market is recorded below. Using the accompanying figures, which use occupies the land at 20 kilometres?",
   table=dict(headers=["Distance from market (kilometres)", "Market gardening (currency units per hectare)", "Dairying (currency units per hectare)", "Grain (currency units per hectare)"],
     rows=[["0", "1,000", "700", "400"],
           ["10", "600", "540", "350"],
           ["20", "200", "380", "300"],
           ["30", "0", "220", "250"],
           ["40", "0", "60", "200"]]),
   choices=[
   "Dairying, which bids 380 there against 300 for grain and 200 for market gardening",
   "Market gardening, which bids highest at every distance",
   "Grain, because it bids 300 and nothing bids more",
   "None of the three, since no use bids anything at 20 kilometres",
   "All three equally, since each offers a positive amount"], ans=0,
   why="At twenty kilometres the three bids are 200, 380 and 300 currency units, so the middle use outbids the other two there even though it is outbid nearer the market and further from it. The land goes to whichever use values that particular site most, which is what EK PSO-5.C.2's bid-rent theory asserts."),

 dict(q="The destination of farm output in four regions is recorded below. Using the accompanying figures, which region is the most strongly commercial?",
   table=dict(headers=["Region", "Share of output consumed by the producing household (%)", "Share of output sold (%)"],
     rows=[["Region 1", "88", "12"],
           ["Region 2", "61", "39"],
           ["Region 3", "12", "88"],
           ["Region 4", "3", "97"]]),
   choices=[
   "Region 4, which sells 97 percent of its output and consumes 3 percent",
   "Region 1, which consumes 88 percent of its output",
   "Region 2, which is closest to an even split",
   "Region 3, which sells 88 percent of its output",
   "All four equally, since every region both sells and consumes"], ans=0,
   why="The shares in each row sum to 100, and the region selling 97 percent of its output sells more than any other, with the four forming a clear gradient from 12 to 97 percent sold. EK PSO-5.C.1 defines production regions by the extent to which they reflect subsistence or commercial practices, and the sold share is a direct measure of that extent."),

 dict(q="Crop diversity and market orientation in four regions are recorded below. Using the accompanying figures, what relationship do they show?",
   table=dict(headers=["Region", "Mean number of crops grown per farm", "Share of output sold (%)"],
     rows=[["Region A", "9", "15"],
           ["Region B", "6", "40"],
           ["Region C", "3", "82"],
           ["Region D", "1", "97"]]),
   choices=[
   "As the share of output sold rises from 15 to 97 percent, crops per farm fall from nine to one, which is the move toward monocropping the framework associates with commercial practice",
   "Crop diversity and the share sold rise together",
   "Crop diversity is the same in all four regions",
   "The most commercial region grows the most crops",
   "No relationship can be read, since the two measures use different units"], ans=0,
   why="The two columns move in opposite directions at every step: nine crops with 15 percent sold at one end, one crop with 97 percent sold at the other. EK PSO-5.C.1 attaches monocropping and monoculture to commercial practices, and this record is that association expressed as numbers."),

 dict(q="What limitation should be stated when using crops-per-farm figures as a measure of commercial orientation?", choices=[
   "The number of crops is a proxy rather than a definition, since the framework defines the distinction by whether output is eaten or sold and a diverse farm could still sell everything",
   "Counting crops is impossible in practice",
   "Crop counts and percentages can never appear in one record",
   "A pattern in a record always proves its own cause",
   "The framework forbids quantitative measures of production regions"], ans=0,
   why="EK PSO-5.C.1 defines production regions by the extent to which practices are subsistence or commercial, and puts monocropping in a parenthesis rather than in the definition. Diversity is strongly associated with subsistence without being what the term means, so a crop count supports the reading rather than establishing it."),

 dict(q="An examiner asks for the economic logic of this topic in a single sentence. Which sentence keeps both of the framework's qualifications?", choices=[
   "Production regions are placed on a subsistence-to-commercial spectrum, with specialization at the commercial end, and how intensively land is farmed depends partly on what that land costs",
   "Production regions are defined by climate, and land costs have no influence on farming",
   "Every production region is either wholly subsistence or wholly commercial",
   "Land costs alone determine whether farming is intensive or extensive",
   "Commercial regions always grow many different crops"], ans=0,
   why="EK PSO-5.C.1 supplies the spectrum and its association with monocropping, and EK PSO-5.C.2 supplies the partial role of land costs through bid-rent theory. The rejected summaries each drop one of the framework's two hedges -- 'the extent to which' and 'in part'."),
]
