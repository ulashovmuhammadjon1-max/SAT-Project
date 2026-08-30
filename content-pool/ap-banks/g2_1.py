# AP HUMAN GEOGRAPHY 2.1 Population Distribution -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding PSO-2, "Understanding
# where and how people live is essential to understanding global cultural,
# political, and economic patterns."
#
# Three learning objectives and four essential knowledge statements:
#   PSO-2.A.1  Physical factors (e.g., climate, landforms, water bodies) and
#              human factors (e.g., culture, economics, history, politics)
#              influence the distribution of population.
#   PSO-2.A.2  Factors that illustrate patterns of population distribution vary
#              according to the scale of analysis.
#   PSO-2.B.1  The three methods for calculating population density are
#              arithmetic, physiological, and agricultural.
#   PSO-2.C.1  The method used to calculate population density reveals different
#              information about the pressure the population exerts on the land.
#
# PSO-2.B.1 is a closed list of three and PSO-2.C.1 says what the list is FOR:
# the three methods are not three ways of computing the same thing, they answer
# three different questions about pressure on land. The definitions the module
# holds itself to, stated once so every key is auditable:
#
#   arithmetic density     total population / total land area
#                          -- how crowded the country is on paper
#   physiological density  total population / area of ARABLE land
#                          -- how many people each unit of farmable land feeds
#   agricultural density   number of FARMERS / area of arable land
#                          -- how much labour is applied per unit of farmland,
#                             so a LOW value indicates mechanized, high-output
#                             agriculture rather than empty land
#
# The last of those is the one students reverse, and items 9, 19, 20 and 29 are
# built on it.
#
# PSO-2.A.1's two lists (physical: climate, landforms, water bodies; human:
# culture, economics, history, politics) are exemplary, not exhaustive -- the CED
# writes "e.g." -- so items keyed to the physical/human split cite the statement
# while items naming a factor not on either list are keyed to the classification
# rather than to the example.
#
# Six items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_1.py. FIVE choices (A-E).
TOPIC = ("2.1", "Population Distribution", 2)

QUESTIONS = [
 dict(q="Which pairing correctly separates a physical from a human influence on where people live?",
   choices=[
     "Growing-season length is physical; the location of a colonial-era port is human",
     "Growing-season length is human; the location of a colonial-era port is physical",
     "Both are physical, since both can be mapped",
     "Both are human, since both affect people",
     "Neither is a factor in population distribution"],
   ans=0,
   why="EK PSO-2.A.1 divides the influences into physical factors such as climate and landforms and human factors such as history, economics and politics. A growing season is set by climate, while a port sited by an imperial administration is a historical and political decision."),

 dict(q="Population in a dry country is concentrated in a narrow strip along one river. The best explanation is that",
   choices=[
     "A physical factor, the availability of water for irrigation and settlement, concentrates people where the river makes agriculture possible",
     "A human factor alone explains it, since governments decide where people live",
     "Rivers repel settlement because of flood risk",
     "Population distribution has no relationship to physical geography",
     "The pattern must be an artefact of the map projection"],
   ans=0,
   why="EK PSO-2.A.1 names water bodies among the physical factors influencing distribution. Where rainfall cannot support cultivation, the river is the only place agriculture and dense settlement are possible, so the population narrows to the strip the water reaches."),

 dict(q="A country's largest cities are all coastal, and each began as a colonial trading post. Which kind of factor best explains this distribution?",
   choices=[
     "A historical factor, since the sites were chosen to serve an export economy and the settlements persisted",
     "A climatic factor, since coasts are always more temperate",
     "A landform factor, since coasts are always flat",
     "A purely contemporary economic factor, since history does not affect present distributions",
     "No identifiable factor, since city sites are chosen at random"],
   ans=0,
   why="EK PSO-2.A.1 lists history among the human factors influencing population distribution. Ports founded to move goods outward acquired infrastructure, administration and population that outlasted the trade that created them."),

 dict(q="At the global scale, climate explains much of the pattern of human settlement. At the scale of one city, climate explains almost none of it. This contrast illustrates which statement?",
   choices=[
     "That the factors illustrating patterns of population distribution vary according to the scale of analysis",
     "That climate is not a real influence on settlement",
     "That only global-scale analysis is valid",
     "That cities have no internal population pattern",
     "That physical factors never operate at the local scale"],
   ans=0,
   why="EK PSO-2.A.2 states exactly this: the factors that illustrate patterns of population distribution vary according to the scale of analysis. Climate barely varies across one city, so it cannot explain variation there, while it varies enormously across the globe."),

 dict(q="Which calculation gives a country's arithmetic population density?",
   choices=[
     "Total population divided by total land area",
     "Total population divided by arable land area",
     "Number of farmers divided by arable land area",
     "Arable land area divided by total population",
     "Total population divided by the number of settlements"],
   ans=0,
   why="EK PSO-2.B.1 names arithmetic as one of the three methods, and it is the simplest of them: everyone divided by all the land. It says how crowded a territory is on paper and nothing about the quality of the land being shared."),

 dict(q="Physiological density is calculated as total population divided by arable land. What does a high value tell a geographer?",
   choices=[
     "That each unit of farmable land must support many people, indicating pressure on the food-producing resource",
     "That the country has a large total land area",
     "That the country's farmers are numerous relative to its farmland",
     "That the country's population is growing quickly",
     "That the country's cities are densely built"],
   ans=0,
   why="EK PSO-2.C.1 states that the method used reveals different information about the pressure the population exerts on the land. Dividing by arable land rather than by all land isolates the resource that actually produces food, so the ratio measures demand on it."),

 dict(q="Agricultural density is the number of farmers divided by the area of arable land. A country with a very LOW agricultural density most likely has",
   choices=[
     "Highly mechanized agriculture in which few workers cultivate a large area",
     "Widespread subsistence farming worked by hand",
     "Almost no arable land at all",
     "A very large total population",
     "An unusually high physiological density"],
   ans=0,
   why="With farmers in the numerator and farmland in the denominator, a low ratio means few workers per unit of land, which is what machinery and capital substitution produce. The measure describes how labour-intensive the farming is, not how much food is grown."),

 dict(q="Two countries have identical arithmetic densities, but one has a physiological density four times the other's. What must be true?",
   choices=[
     "The country with the higher physiological density has a much smaller share of its land in arable use",
     "The country with the higher physiological density has a larger total population",
     "The country with the higher physiological density has more farmers",
     "The two countries have different total land areas",
     "One of the two figures must have been calculated incorrectly"],
   ans=0,
   why="Equal arithmetic densities fix population against total area, so any difference in physiological density has to come from the denominator that changed, which is arable land. EK PSO-2.C.1's point is precisely that the choice of denominator is what the different methods reveal."),

 dict(q="Which question is agricultural density best suited to answer?",
   choices=[
     "How much human labour is applied to each unit of farmland in this country?",
     "How many people must each hectare of farmland feed?",
     "How crowded is the country overall?",
     "How fast is the country's population growing?",
     "What share of the country's land is arable?"],
   ans=0,
   why="EK PSO-2.C.1 says each method reveals different information about pressure on the land, and agricultural density puts farmers over farmland. That ratio is a statement about labour intensity, while the number of mouths per hectare is what physiological density measures."),

 dict(q="A mountainous country reports a low arithmetic density but one of the highest physiological densities in the world. The most likely explanation is that",
   choices=[
     "Most of its territory is unfarmable, so its population is concentrated on a small area of cultivable land",
     "Its population is very small",
     "Its farmers are unusually numerous",
     "Its total land area was measured incorrectly",
     "It has more arable land than any comparable country"],
   ans=0,
   why="A low arithmetic figure means few people per unit of all land, while a high physiological figure means many people per unit of arable land, and only a small arable share can produce both at once. EK PSO-2.C.1 treats that divergence as informative rather than contradictory."),

 dict(q="Which physical factor best explains why very few people live in the interior of a large desert?",
   choices=[
     "Aridity, which makes both cultivation and reliable water supply impossible without imported infrastructure",
     "Latitude, since deserts occur only near the poles",
     "Elevation, since all deserts are high",
     "Political history, since deserts have never been colonized",
     "Soil colour, which absorbs heat"],
   ans=0,
   why="EK PSO-2.A.1 lists climate among the physical factors influencing distribution. Where precipitation cannot support crops or households, settlement depends on transported water and energy, which is why desert interiors hold isolated points rather than a spread of population."),

 dict(q="A national government builds a new capital city in a sparsely settled interior region and moves its ministries there. Which factor from the framework is at work?",
   choices=[
     "A political factor, since a state decision redirected population toward a chosen site",
     "A climatic factor, since interiors are drier",
     "A landform factor, since interiors are flatter",
     "No factor from the framework, since capitals are symbolic rather than demographic",
     "A physical factor, since the site had to be habitable"],
   ans=0,
   why="EK PSO-2.A.1 names politics among the human factors influencing the distribution of population. Relocating the machinery of government carries employment, services and migrants with it, which is how a deliberate siting decision becomes a demographic fact."),

 dict(q="A geographer says a country's national population density figure is 'true but nearly useless.' The strongest justification is that",
   choices=[
     "One figure for the whole country conceals extreme internal concentration, which is the pattern the analysis is actually about",
     "Density cannot be calculated for large countries",
     "National statistics are never accurate",
     "Density figures are meaningful only for cities",
     "Arithmetic density is calculated incorrectly by most governments"],
   ans=0,
   why="EK PSO-2.A.2 makes the informative factors depend on the scale of analysis, and a single national ratio is the coarsest possible scale. Averaging a crowded delta with an empty desert produces a number no part of the country resembles."),

 dict(q="Which of the following would RAISE a country's physiological density without any change in its population?",
   choices=[
     "Salinization and urban expansion removing land from cultivation",
     "An increase in the country's total land area",
     "A rise in the number of people working as farmers",
     "The mechanization of its agriculture",
     "An increase in crop yields per hectare"],
   ans=0,
   why="Physiological density is population over arable land, so with population fixed only a fall in the denominator can raise it. Yields, mechanization and the size of the farm workforce affect output and labour intensity but not the amount of land classified as arable."),

 dict(q="Which statement correctly distinguishes population distribution from population density?",
   choices=[
     "Distribution describes where people are arranged across an area; density is a ratio of people to a unit of area",
     "Distribution and density are two names for the same measurement",
     "Distribution is a ratio and density is a pattern",
     "Distribution applies only to countries and density only to cities",
     "Density can be mapped but distribution cannot"],
   ans=0,
   why="A distribution is a pattern -- clustered, dispersed, linear -- while a density is a single computed value for a defined unit. Two countries can share a density and have entirely different distributions, which is why the framework treats them in separate learning objectives."),

 dict(q="At the local scale within one city, which factor most often explains where population density is highest?",
   choices=[
     "The type of housing permitted and built, since apartment blocks hold far more people per hectare than detached houses",
     "The city's latitude",
     "The country's colonial history",
     "The continent the city is on",
     "The city's average annual rainfall"],
   ans=0,
   why="EK PSO-2.A.2 makes the explanatory factor depend on the scale, and within one city climate, latitude and continent are constants that cannot explain variation. Building form varies block by block and is what actually determines residents per hectare."),

 dict(q="Which combination of density figures best fits a country with intensive subsistence agriculture?",
   choices=[
     "High physiological density and high agricultural density",
     "Low physiological density and low agricultural density",
     "High physiological density and low agricultural density",
     "Low physiological density and high agricultural density",
     "Density measures cannot describe subsistence agriculture"],
   ans=0,
   why="Intensive subsistence farming means many people fed from limited farmland, which is a high physiological figure, worked by large numbers of hand labourers, which is a high agricultural figure. The pair together is the signature the two measures were designed to produce."),

 dict(q="Which combination of density figures best fits a highly commercialized farming country such as one where a few percent of workers farm large mechanized holdings?",
   choices=[
     "Low agricultural density with a moderate physiological density",
     "High agricultural density with a very high physiological density",
     "High agricultural density with a very low physiological density",
     "Agricultural density equal to arithmetic density",
     "No combination, since commercial agriculture has no density signature"],
   ans=0,
   why="Few farmers spread over a large cultivated area gives a low farmers-per-hectare ratio, while a moderate population divided by ample arable land keeps the people-per-hectare ratio unremarkable. The low labour ratio is the diagnostic figure for mechanization."),

 dict(q="A country reclassifies marginal grazing land as arable. Assuming nothing else changes, what happens to its density measures?",
   choices=[
     "Physiological and agricultural densities both fall, while arithmetic density is unchanged",
     "All three densities fall",
     "All three densities rise",
     "Arithmetic density falls and the other two are unchanged",
     "Only agricultural density changes"],
   ans=0,
   why="Arable land is the denominator of two of the three measures and appears in neither the numerator nor the denominator of the third. Enlarging it therefore lowers both ratios that use it and leaves population over total land exactly where it was."),

 dict(q="Which is the strongest reason a planner concerned with food self-sufficiency would prefer physiological to arithmetic density?",
   choices=[
     "It relates the population to the land that can actually produce food rather than to land in general",
     "It is easier to calculate",
     "It always produces a smaller number",
     "It counts only the farming population",
     "It is the only measure recognized internationally"],
   ans=0,
   why="EK PSO-2.C.1 is explicit that different methods reveal different information about pressure on the land. A food-supply question is about the productive resource, and dividing by deserts and ice sheets tells the planner nothing about it."),

 dict(q="Two neighboring provinces have the same population and the same total area, but one is largely floodplain and the other largely rock. What will differ, and why?",
   choices=[
     "Their physiological densities will differ, because the share of land that is arable differs while population and total area do not",
     "Their arithmetic densities will differ, because terrain affects total area",
     "Nothing will differ, because population and area are the same",
     "Their agricultural densities will be identical, because farmer counts follow population",
     "Only their population distributions can differ, not any density measure"],
   ans=0,
   why="Arithmetic density is fixed by the two quantities the provinces share, so it must be identical. The arable denominator is what the terrain changes, and it appears only in the physiological and agricultural measures."),

 dict(q="Which of the following is a HUMAN factor influencing where people live, as the framework classifies factors?",
   choices=[
     "The location of employment created by an industrial economy",
     "The elevation of a mountain range",
     "The path of a major river",
     "The mean January temperature",
     "The depth of a natural harbour"],
   ans=0,
   why="EK PSO-2.A.1 lists economics among the human factors influencing the distribution of population. Elevation, rivers, temperature and harbour depth are landforms, water bodies and climate, which the same statement places on the physical side."),

 dict(q="Why do the world's largest population clusters lie in midlatitude and subtropical lowlands near coasts and major rivers?",
   choices=[
     "Those areas combine cultivable climate, workable terrain, and access to water transport, so both physical and human advantages coincide",
     "Governments have required people to settle there",
     "Those areas have the largest total land area",
     "Those areas were settled most recently",
     "Those areas have the lowest disease burdens"],
   ans=0,
   why="EK PSO-2.A.1 lists physical and human factors side by side without ranking them, and the great clusters are where the two reinforce each other. Climate permits agriculture, flat land permits farming and building, and navigable water permits the trade that supports cities."),

 dict(q="A student concludes from a country's low arithmetic density that 'there is plenty of room for more people there.' What is the flaw?",
   choices=[
     "Arithmetic density averages over land that may be uninhabitable, so a low figure can coexist with severe pressure on the small usable area",
     "Arithmetic density is not a real measure",
     "The conclusion is correct for every country",
     "Arithmetic density counts only rural residents",
     "The flaw is that population is in the denominator"],
   ans=0,
   why="EK PSO-2.C.1 exists because the three methods answer different questions, and the arithmetic figure divides by every square kilometre whether it is farmable, frozen or vertical. Judging capacity requires the measure whose denominator is the usable land."),

 dict(q="Which statement about the three density methods is correct?",
   choices=[
     "They use the same population data with different denominators, or a different numerator, and therefore answer different questions",
     "They are three names for the same calculation",
     "They always rank countries in the same order",
     "Only arithmetic density is used by geographers today",
     "They differ only in the units in which the answer is reported"],
   ans=0,
   why="EK PSO-2.B.1 names three methods and EK PSO-2.C.1 says the method chosen reveals different information about pressure on the land. Two of the three change the denominator to arable land and one also replaces the numerator with the farming population."),

 dict(q="Two countries' land and population figures are shown. Using the table, which country has the higher arithmetic density, and which has the higher physiological density?",
   table=dict(
     headers=["Country", "Population (millions)", "Total land area (thousand km2)", "Arable land (thousand km2)"],
     rows=[
       ["Country A", "40", "400", "160"],
       ["Country B", "24", "300", "30"]]),
   choices=[
     "Country A has the higher arithmetic density at 100 per km2, while Country B has the higher physiological density at 800 per km2",
     "Country A is higher on both measures",
     "Country B is higher on both measures",
     "Country B has the higher arithmetic density and Country A the higher physiological density",
     "The two countries have equal densities on both measures"],
   ans=0,
   why="Arithmetic densities are 40 million over 400 thousand square kilometres, or 100 per square kilometre, against 80 for the other country, while physiological densities are 250 and 800. Changing the denominator to arable land reverses which country looks crowded, which is what the two measures are for."),

 dict(q="Farming data for three countries are shown. Using the table, which country's agriculture is most likely to be mechanized?",
   table=dict(
     headers=["Country", "Farmers (thousands)", "Arable land (thousand km2)"],
     rows=[
       ["Country P", "12,000", "600"],
       ["Country Q", "900", "450"],
       ["Country R", "4,500", "300"]]),
   choices=[
     "Country Q, with 2 farmers per square kilometre of arable land",
     "Country P, with the largest number of farmers",
     "Country R, with 15 farmers per square kilometre of arable land",
     "Country P, with 20 farmers per square kilometre of arable land",
     "All three, since every country uses machinery"],
   ans=0,
   why="Dividing farmers by arable land gives 20, 2 and 15 thousand farmers per thousand square kilometres, so the country applying least labour per unit of land is the one with the fewest farmers, not the one with the most land. Low labour intensity is the signature of capital substitution."),

 dict(q="A country's population and land are reported for four regions. Using the table, which region exerts the greatest pressure on its farmland?",
   table=dict(
     headers=["Region", "Population (thousands)", "Arable land (km2)"],
     rows=[
       ["Region 1", "4,800", "6,000"],
       ["Region 2", "2,100", "1,400"],
       ["Region 3", "9,000", "15,000"],
       ["Region 4", "1,200", "3,000"]]),
   choices=[
     "Region 2, at 1,500 people per square kilometre of arable land",
     "Region 3, which has the largest population in the table",
     "Region 1, at 800 people per square kilometre of arable land",
     "Region 4, which has the least arable land",
     "Region 3, which has the most arable land"],
   ans=0,
   why="Physiological densities are 800, 1,500, 600 and 400 people per square kilometre of arable land, so the most populous region is not the one under most pressure. The region with the least arable land is also not the answer, because its population is small in proportion."),

 dict(q="Land and settlement data for one country are shown by zone. Using the table, what share of the country's population lives on what share of its land?",
   table=dict(
     headers=["Zone", "Population (millions)", "Land area (thousand km2)"],
     rows=[
       ["River valley", "72", "40"],
       ["Coastal plain", "18", "60"],
       ["Desert interior", "10", "900"]]),
   choices=[
     "72 percent of the population lives on 4 percent of the land",
     "72 percent of the population lives on 40 percent of the land",
     "18 percent of the population lives on 4 percent of the land",
     "The population is spread evenly across the three zones",
     "10 percent of the population lives on 90 percent of the land, so the desert is the most crowded zone"],
   ans=0,
   why="The valley holds 72 of the country's 100 million people on 40 of its 1,000 thousand square kilometres, which is 72 percent of the population on 4 percent of the land. The national arithmetic density of 100 per square kilometre describes no zone in the table."),

 dict(q="A country's arable area changes over three decades while its population grows. Using the table, what has happened to the pressure on its farmland?",
   table=dict(
     headers=["Year", "Population (millions)", "Arable land (thousand km2)"],
     rows=[
       ["1990", "30", "120"],
       ["2005", "42", "105"],
       ["2020", "54", "90"]]),
   choices=[
     "Physiological density has doubled, from 250 to 600 people per square kilometre of arable land",
     "Physiological density has fallen, because farming has become more efficient",
     "Physiological density is unchanged, since both figures moved",
     "Physiological density rose only because the population rose",
     "Physiological density cannot be compared across years"],
   ans=0,
   why="Dividing each year's population by that year's arable land gives 250, 400 and 600 people per square kilometre, so the ratio has more than doubled. Both terms moved and they moved in opposite directions, which is why the population figure alone does not account for the rise."),
]
