# AP HUMAN GEOGRAPHY 6.4 The Size and Distribution of Cities -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding PSO-6, "The presence
# and growth of cities vary across geographical locations because of physical
# geography and resources." Learning objective PSO-6.C, "Identify the different
# urban concepts such as hierarchy, interdependence, relative size, and spacing
# that are useful for explaining the distribution, size, and interaction of
# cities."
#
# Essential knowledge -- ONE statement, and it is a list of four principles:
#   PSO-6.C.1  Principles that are useful for explaining the distribution and
#              size of cities include rank-size rule, the primate city, gravity,
#              and Christaller's central place theory.
#
# THE FOUR PRINCIPLES ANSWER DIFFERENT QUESTIONS, and sorting them by question
# is what the topic actually tests. Item 18 asks for it directly:
#
#   rank-size rule        how do the SIZES of a country's cities relate to one
#                         another? (the nth city is about 1/n of the largest)
#   the primate city      what does it mean when the largest city is far bigger
#                         than the rank-size rule would predict?
#   gravity               how much INTERACTION should two places have? (it rises
#                         with the product of their populations and falls with
#                         the square of the distance between them)
#   central place theory  why are settlements of different sizes SPACED as they
#                         are, and which services will each support?
#
# The first two describe a size distribution, the third predicts a flow, and the
# fourth explains a spatial arrangement. A student who has learned them as four
# interchangeable "urban models" will pick the wrong one every time.
#
# THE ARITHMETIC EACH ONE ACTUALLY REQUIRES, stated because the CED names the
# principles without stating any of them:
#   rank-size   expected population of the nth city = population of the largest
#               divided by n. Items 3 and 26 compute it.
#   gravity     interaction is proportional to (P1 x P2) divided by the SQUARE
#               of the distance. Squaring the distance is the part students drop,
#               and items 8 and 27 are built on it -- doubling the distance
#               quarters the predicted interaction rather than halving it.
#   central     THRESHOLD is the minimum market a service needs to survive;
#     place     RANGE is the greatest distance a customer will travel for it. A
#               service exists where the range encloses enough people to meet the
#               threshold, which is why both numbers are needed and neither is
#               enough alone (items 10, 11, 12, 28).
#
# WHAT ALL FOUR ARE FOR. The CED calls them principles "useful for explaining",
# which is the same hedge Topic 5.8 attaches to von Thunen. None is a law, each
# rests on assumptions no real country satisfies, and items 19, 20, 21 and 29
# key on the limits of each in turn. A departure from a prediction is information
# about the country, not a refutation of the principle.
#
# SYNONYM CARE. `geo_check` treats {"central place theory", "christaller's
# model"} as one construct, so each item names that theory in exactly one way.
#
# NO REAL COUNTRY OR CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.4", "The Size and Distribution of Cities", 6)

QUESTIONS = [
 dict(q="Which four principles does the framework name as useful for explaining the distribution and size of cities?", choices=[
   "The rank-size rule, the primate city, gravity, and central place theory",
   "The concentric zone, sector, multiple nuclei, and galactic city models",
   "Site, situation, suburbanization, and sprawl",
   "Megacities, metacities, edge cities, and exurbs",
   "The rank-size rule, bid-rent theory, gravity, and the demographic transition model"], ans=0,
   why="EK PSO-6.C.1 names exactly these four. The urban structure models belong to EK PSO-6.D.1 and describe what is inside a city, whereas these four describe how cities relate to one another in size, spacing and interaction."),

 dict(q="What does the rank-size rule state?", choices=[
   "The nth largest city in a system has about one nth of the largest city's population",
   "Every city in a system has the same population",
   "The largest city has at least twice the population of the second largest",
   "Interaction between two cities falls with the square of the distance between them",
   "Cities are spaced evenly across a uniform plain"], ans=0,
   why="EK PSO-6.C.1 names the rank-size rule among the principles explaining the distribution and size of cities. It describes a regular relationship across a whole set of cities rather than a fact about any single one."),

 dict(q="In a country whose largest city has 9 million residents and whose city sizes follow the rank-size rule, what population would the third largest city have?", choices=[
   "About 3 million",
   "About 4.5 million",
   "About 6 million",
   "About 1.5 million",
   "About 9 million"], ans=0,
   why="The rule gives the nth city the largest city's population divided by n, so the third city is 9 million divided by 3. EK PSO-6.C.1 names the rank-size rule among the principles explaining the size of cities, and dividing by the rank is the whole of the arithmetic."),

 dict(q="What is a primate city?", choices=[
   "A country's largest city, disproportionately larger than the second largest and dominant in its economy, politics and culture",
   "The oldest city in a country",
   "A city that follows the rank-size rule exactly",
   "The capital city of any country",
   "A city with more than ten million residents"], ans=0,
   why="EK PSO-6.C.1 names the primate city among the principles explaining the distribution and size of cities. The definition is comparative -- what matters is the ratio to the next city down, not the absolute population."),

 dict(q="A country's four largest cities have 12, 2, 1.6 and 1.2 million residents. What does this distribution show?", choices=[
   "Primacy, since the largest city is six times the second rather than about twice it as the rank-size rule would predict",
   "A rank-size distribution, since city sizes fall as rank rises",
   "That the country has no urban hierarchy",
   "That the gravity model does not apply to this country",
   "That the four cities are equal in importance"], ans=0,
   why="The rank-size rule would put the second city near 6 million, and it is 2 million, so the largest city is far larger than the distribution predicts. EK PSO-6.C.1 names both the rank-size rule and the primate city, and the second is identified precisely by departure from the first."),

 dict(q="What does a strongly primate urban system usually indicate about a country?", choices=[
   "Political, economic and cultural functions are concentrated in one place, so opportunity and investment are as well",
   "The country has an unusually even distribution of opportunity",
   "The country has no capital city",
   "The country's second city must also be very large",
   "The country's population is evenly spread across its territory"], ans=0,
   why="EK PSO-6.C.1 names the primate city among the principles explaining the distribution and size of cities. A city becomes disproportionate because functions accumulate in it, and each function it holds gives people another reason to go there rather than anywhere else."),

 dict(q="What does the gravity model predict?", choices=[
   "That interaction between two places rises with the product of their populations and falls with the square of the distance between them",
   "That the largest city in a system will be twice the size of the second",
   "That settlements are arranged in hexagonal market areas",
   "That land rent falls with distance from a city centre",
   "That interaction depends only on distance and not on population"], ans=0,
   why="EK PSO-6.C.1 names gravity among the principles explaining the distribution and size of cities. It is the only one of the four that predicts a FLOW between two places rather than describing a pattern among many."),

 dict(q="Two cities' populations are unchanged but the distance between them doubles. What does the gravity model predict for the interaction between them?", choices=[
   "It falls to about one quarter of its previous level, since distance enters the prediction squared",
   "It falls to about one half of its previous level",
   "It is unchanged, since the populations are unchanged",
   "It doubles, since the cities are further apart",
   "It falls to about one eighth of its previous level"], ans=0,
   why="EK PSO-6.C.1 names gravity among the principles explaining the interaction of cities, and the distance term is squared. Squaring is the step students drop, and it is the difference between a prediction that halves and one that falls to a quarter."),

 dict(q="One of two cities doubles in population while the distance between them stays the same. What does the gravity model predict?", choices=[
   "Interaction roughly doubles, since it rises with the product of the two populations",
   "Interaction roughly quadruples",
   "Interaction is unchanged",
   "Interaction falls by half",
   "Interaction cannot be predicted without knowing the cities' areas"], ans=0,
   why="EK PSO-6.C.1 names gravity among the principles explaining the interaction of cities. The populations enter as a product and are not squared, so doubling one of them doubles the numerator and therefore the prediction."),

 dict(q="In central place theory, what is the THRESHOLD of a service?", choices=[
   "The minimum number of customers needed for the service to survive",
   "The greatest distance a customer will travel to reach the service",
   "The size of the building the service occupies",
   "The number of competing services in the same town",
   "The distance between two settlements offering the service"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities. Threshold is a claim about the market a service needs, which is why a service with a large threshold appears in few places."),

 dict(q="In central place theory, what is the RANGE of a service?", choices=[
   "The greatest distance a customer is willing to travel to obtain it",
   "The minimum number of customers it needs to survive",
   "The number of different goods it sells",
   "The area of land it occupies",
   "The number of settlements in the region"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities. Range describes how far the service's market extends, so it is a claim about the customer's willingness to travel rather than about the business's requirements."),

 dict(q="What condition must hold for a service to be viable at a given location, in central place theory's terms?", choices=[
   "The area within its range must contain at least enough people to meet its threshold",
   "Its range must be smaller than its threshold",
   "Its threshold must equal the population of the settlement exactly",
   "Its range must extend to the national border",
   "It must be the only such service in the country"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and the two concepts have to be used together. Threshold states the customers required and range states how far they can be drawn from, so viability is a comparison between the two."),

 dict(q="Why do higher-order goods and services appear in fewer settlements than lower-order ones?", choices=[
   "They have larger thresholds, so only a settlement drawing on a large enough surrounding population can support them",
   "They are physically larger and need more land",
   "They are prohibited in small settlements",
   "Customers refuse to travel for them",
   "They have smaller ranges than lower-order services"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and threshold is what sorts services into orders. A specialist service needs a large market, and only a few places can assemble one."),

 dict(q="Why does central place theory represent market areas as hexagons?", choices=[
   "Hexagons tile a plain completely without overlaps or gaps, which circles of equal size cannot do",
   "Because settlements are physically hexagonal in shape",
   "Because hexagons have the largest possible area for their perimeter",
   "Because roads always meet at six-way junctions",
   "Because hexagons are easier to draw than circles"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution of cities. A market area is naturally a circle around a centre, but circles either overlap or leave gaps, and hexagons are the closest shape to a circle that covers a plain exactly once."),

 dict(q="What does central place theory predict about the SPACING of settlements of different orders?", choices=[
   "Higher-order centres are fewer and further apart, while lower-order centres are more numerous and closer together",
   "All settlements are spaced identically regardless of order",
   "Higher-order centres are more numerous and closer together",
   "Spacing is random and cannot be predicted",
   "All settlements cluster at the edge of the region"], ans=0,
   why="Learning objective PSO-6.C names spacing among the concepts useful for explaining the distribution of cities, and EK PSO-6.C.1 names central place theory. A large threshold requires a large market area, and a large market area occupies more ground, so fewer such centres fit into a region."),

 dict(q="What does the framework's concept of INTERDEPENDENCE among cities refer to?", choices=[
   "Cities in a system rely on one another, with smaller places using services in larger ones and larger places drawing customers, labour and supplies from smaller ones",
   "Cities are entirely self-sufficient and independent of one another",
   "Every city in a system has the same population",
   "Cities compete without ever exchanging anything",
   "Interdependence applies only between cities in different countries"], ans=0,
   why="Learning objective PSO-6.C names interdependence among the concepts useful for explaining the distribution, size and interaction of cities. A settlement system works as a system precisely because no single place supplies everything its residents need."),

 dict(q="What does the concept of RELATIVE SIZE add to knowing a city's population?", choices=[
   "It compares a city with the others in its system, which is what makes a distribution rank-size or primate",
   "It measures the city's land area rather than its population",
   "It measures the height of the city's buildings",
   "It measures the city's population density",
   "It measures the city's distance from the capital"], ans=0,
   why="Learning objective PSO-6.C names relative size among the concepts useful for explaining the distribution and size of cities. A population of four million means one thing beside a city of eight million and something quite different beside a city of forty."),

 dict(q="Which principle would you use to predict how many trips people make between two particular cities?", choices=[
   "Gravity, since it predicts interaction between a specific pair of places",
   "The rank-size rule, since it describes city sizes",
   "The primate city, since it describes dominance",
   "Central place theory, since it describes market areas",
   "None of the four, since interaction cannot be predicted"], ans=0,
   why="EK PSO-6.C.1 names four principles and they answer different questions. Only one of them takes two specific places and returns an expected flow between them, which is what a question about trips requires."),

 dict(q="A country's city sizes depart substantially from the rank-size rule. What is the most defensible conclusion?", choices=[
   "The departure is information about that country's history and geography, since the rule is a regularity rather than a law",
   "The rule has been disproved and should not be used",
   "The country's population figures must be wrong",
   "The country has no cities",
   "Every country departs from the rule by the same amount"], ans=0,
   why="EK PSO-6.C.1 calls these principles USEFUL FOR EXPLAINING the distribution and size of cities, which is weaker than calling them laws. A colonial history, a recently redrawn border or a single dominant capital all produce recognizable departures, and the departure is what points to the cause."),

 dict(q="What is the main limitation of the gravity model as a predictor of interaction?", choices=[
   "Population and distance are not the only things that matter -- a border, a language difference or a poor transport link can cut interaction the model would predict",
   "The model cannot be calculated without a computer",
   "The model applies only to cities of identical size",
   "The model ignores population entirely",
   "The model has no limitations"], ans=0,
   why="EK PSO-6.C.1 names gravity among the principles USEFUL FOR EXPLAINING the interaction of cities. Two places of given sizes at a given distance can be separated by a closed border or joined by a fast rail link, and the model as stated sees neither."),

 dict(q="Which assumption of central place theory is least likely to hold in a real region?", choices=[
   "That the region is a flat plain of uniform fertility with population and purchasing power spread evenly across it",
   "That customers prefer to travel a shorter distance than a longer one",
   "That services need a minimum number of customers",
   "That some services are more specialized than others",
   "That settlements provide services to surrounding areas"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution of cities, and its hexagonal geometry follows from a uniform surface. Terrain, soils, rivers and unequal incomes all distort the pattern, while the behavioural assumptions in the other options are far more robust."),

 dict(q="At which scale is central place theory most usefully applied?", choices=[
   "The regional scale, where a set of settlements of different sizes serves a surrounding area",
   "The global scale, comparing continents",
   "The scale of a single building",
   "The household scale",
   "No scale, since the theory is purely abstract"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and its subject is a settlement system with its market areas. That is a regional object: it needs several settlements of different orders and the countryside they serve."),

 dict(q="Can a primate city also be a world city?", choices=[
   "Yes, since primacy describes dominance within a national system and world-city status describes function in the global hierarchy",
   "No, the two categories are mutually exclusive",
   "Only if the country is a core country",
   "Only if the city has more than twenty million residents",
   "Yes, but only if the country has exactly one city"], ans=0,
   why="EK PSO-6.C.1 names the primate city among the principles explaining size within a system, while EK PSO-6.B.1 places world cities at the top of the WORLD'S urban hierarchy. The two answer different questions, so a city can satisfy either, both, or neither."),

 dict(q="A resident of a small town buys bread locally but travels ninety kilometres to a large city for specialist medical treatment. Which principle explains this pattern?", choices=[
   "Central place theory, since a low-threshold service is available locally and a high-threshold one requires a larger centre further away",
   "The rank-size rule, since the two settlements differ in size",
   "The primate city, since one settlement is larger",
   "Gravity, since the resident travelled a distance",
   "None of the four principles applies to individual behaviour"], ans=0,
   why="EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and this is its characteristic prediction. Bread has a small threshold and a short range while specialist treatment has a large threshold and a long range, so the two are obtained at different levels of the hierarchy."),

 dict(q="Which pairing of a question with the principle that answers it is CORRECT?", choices=[
   "How much travel should occur between two named cities, answered by gravity",
   "How much travel should occur between two named cities, answered by the rank-size rule",
   "Which services a town of 3,000 can support, answered by the primate city",
   "Whether a country's largest city is disproportionate, answered by central place theory",
   "How city sizes in a country relate to one another, answered by gravity"], ans=0,
   why="EK PSO-6.C.1 names four principles that answer four different questions. Only one pairing here matches a question to the principle designed for it, and each of the others attaches a question to a principle that has nothing to say about it."),

 dict(q="A country's five largest cities are recorded below. Using the accompanying figures, what kind of distribution is this?",
   table=dict(headers=["Rank", "Population (millions)", "Population the rank-size rule predicts (millions)"],
     rows=[["1", "8.0", "8.00"],
           ["2", "4.1", "4.00"],
           ["3", "2.6", "2.67"],
           ["4", "2.1", "2.00"],
           ["5", "1.6", "1.60"]]),
   choices=[
   "A rank-size distribution, since every observed population is within about 0.1 million of what the rule predicts",
   "A primate distribution, since the largest city is the biggest",
   "A distribution that contradicts the rank-size rule entirely",
   "A distribution in which all five cities are the same size",
   "A distribution that the rank-size rule cannot be applied to"], ans=0,
   why="Each predicted value is the largest city's 8.0 million divided by the rank, and every observed figure is within 0.1 million of it. EK PSO-6.C.1 names the rank-size rule among the principles explaining the size of cities, and this is what a country that follows it closely looks like."),

 dict(q="Four pairs of cities are recorded below. Using the accompanying figures, which pair should have the greatest interaction according to the gravity model?",
   table=dict(headers=["Pair", "Population of first city (thousands)", "Population of second city (thousands)", "Distance apart (kilometres)"],
     rows=[["Pair A", "800", "400", "40"],
           ["Pair B", "1,600", "400", "80"],
           ["Pair C", "800", "800", "40"],
           ["Pair D", "400", "400", "25"]]),
   choices=[
   "Pair C, whose predicted interaction of 400 exceeds Pair D's 256, Pair A's 200 and Pair B's 100",
   "Pair B, since it contains the largest single city",
   "Pair D, since its cities are the closest together",
   "Pair A, since it is first in the record",
   "All four are equal, since each contains two cities"], ans=0,
   why="Multiplying the two populations and dividing by the square of the distance gives 200, 100, 400 and 256, so the pair with the largest product at the shorter distance wins. The pair containing the single largest city ranks last, because doubling its distance divides the prediction by four while doubling one population only doubles it."),

 dict(q="Five services are recorded below with their threshold and range. Using the accompanying figures, which will be found in the greatest number of settlements?",
   table=dict(headers=["Service", "Threshold (customers needed)", "Range (kilometres customers will travel)"],
     rows=[["Convenience store", "500", "3"],
           ["Primary school", "1,200", "5"],
           ["Supermarket", "8,000", "15"],
           ["Regional hospital", "120,000", "90"],
           ["Opera house", "900,000", "250"]]),
   choices=[
   "The convenience store, whose threshold of 500 customers is the lowest, so the largest number of settlements can support one",
   "The opera house, whose range of 250 kilometres is the greatest",
   "The regional hospital, since health care is essential",
   "The supermarket, since it is intermediate in both columns",
   "All five will be found in the same number of settlements"], ans=0,
   why="Threshold and range rise together across the five services, from 500 customers and 3 kilometres to 900,000 and 250, and the number of places able to support a service falls as its threshold rises. EK PSO-6.C.1 names central place theory among the principles explaining the distribution and size of cities, and this ordering is its central prediction."),

 dict(q="What limitation should be stated when using the gravity model with only populations and distances?", choices=[
   "The model treats every kilometre as equally costly to cross, so it cannot see a closed border, a mountain range or a fast rail link between the two places",
   "Populations and distances cannot be measured",
   "The model cannot be calculated for more than two cities",
   "Any prediction the model makes must be exactly correct",
   "The framework forbids the use of the gravity model"], ans=0,
   why="EK PSO-6.C.1 names gravity among the principles USEFUL FOR EXPLAINING the interaction of cities, which concedes that it is not complete. Distance in the formula is physical, and the friction that actually governs movement is political and infrastructural as well."),

 dict(q="A student is asked what the four principles in this topic have in common. Which answer is accurate?", choices=[
   "Each is a simplification that makes one aspect of a settlement system predictable, and each is useful partly because real systems depart from it in informative ways",
   "Each predicts the internal land-use pattern of a single city",
   "Each has been proved to hold exactly in every country",
   "Each concerns only the largest city in a country",
   "Each describes the physical site on which a city was founded"], ans=0,
   why="EK PSO-6.C.1 calls all four principles USEFUL FOR EXPLAINING the distribution and size of cities, which is the same hedge the CED attaches to von Thunen's model. The internal structure of a city belongs to EK PSO-6.D.1 and site belongs to EK PSO-6.A.1."),
]
