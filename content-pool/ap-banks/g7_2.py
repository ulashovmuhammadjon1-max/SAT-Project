# AP HUMAN GEOGRAPHY 7.2 Economic Sectors and Patterns -- 30 questions
# CED Course Framework V.1, Unit 7. Enduring understanding SPS-7,
# "Industrialization, past and present, has facilitated improvements in
# standards of living, but it has also contributed to geographically uneven
# development." Learning objective SPS-7.B, "Explain the spatial patterns of
# industrial production and development."
#
# Essential knowledge -- two statements:
#   SPS-7.B.1  The different economic sectors -- including primary, secondary,
#              tertiary, quaternary, and quinary -- are characterized by distinct
#              development patterns.
#   SPS-7.B.2  Labor, transportation (including shipping containers), the
#              break-of-bulk point, least cost theory, markets, and resources
#              influence the location of manufacturing such as core,
#              semiperiphery, and periphery locations.
#
# THE FIVE SECTORS, with the working definitions used throughout, since the CED
# names them and defines none:
#   primary     extraction from the earth -- farming, fishing, forestry, mining
#   secondary   turning those materials into goods -- manufacturing, processing,
#               construction
#   tertiary    services delivered to people -- retail, transport, hospitality,
#               personal and routine business services
#   quaternary  handling INFORMATION -- research, analysis, software, higher
#               education, the technical work of finance
#   quinary     the highest level of DECISION -- the small number of posts at
#               which the direction of large organizations and governments is set
# Items 2 to 6 take one each. The boundary students actually miss is tertiary
# against quaternary (item 8): both are "services", and what separates them is
# whether the work delivers a service to a customer or produces and interprets
# information. Item 9 marks the quaternary-quinary line, which is a matter of
# decision authority rather than of subject.
#
# "DISTINCT DEVELOPMENT PATTERNS" IS THE POINT OF SPS-7.B.1, not the list. The
# sectors do not merely differ; each dominates at a different stage, so the
# sectoral composition of employment is itself a measure of development. Items 7
# and 26 are built on that, and item 26's table is four economies at four
# positions on the same path rather than four unrelated cases.
#
# SPS-7.B.2 IS A LIST OF SIX LOCATION FACTORS, and the module keeps them
# separate: labour (11), transportation including shipping containers (12, 21,
# 28), the break-of-bulk point (13), least cost theory (14, 15, 16, 17, 27),
# markets (18) and resources (19). Item 25 requires them to be told apart.
#
# LEAST COST THEORY, since the CED names it without stating it: a manufacturer
# locates where the combined cost of moving materials in, moving the product out,
# and labour is lowest, with a further pull toward clustering with related firms.
# The consequence students are asked for is the bulk-reducing / bulk-gaining
# distinction -- an industry that loses weight in processing is pulled toward its
# materials, one that gains weight or bulk is pulled toward its market. Items 15
# and 16 are that pair and item 27 makes it arithmetic.
#
# SYNONYM CARE. `geo_check` treats {"least cost theory", "weber's model",
# "weber model"} as one construct, so every item names it in exactly one way.
#
# NO REAL COUNTRY OR FIRM IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("7.2", "Economic Sectors and Patterns", 7)

QUESTIONS = [
 dict(q="Which five economic sectors does the framework name?", choices=[
   "Primary, secondary, tertiary, quaternary, and quinary",
   "Agricultural, industrial, and post-industrial",
   "Core, semiperiphery, and periphery",
   "Formal, informal, and subsistence",
   "Extraction, manufacturing, and consumption"], ans=0,
   why="EK SPS-7.B.1 names exactly these five and says they are characterized by distinct development patterns. Core, semiperiphery and periphery are positions in the world economy named in EK SPS-7.B.2, which classify places rather than kinds of work."),

 dict(q="What kind of activity belongs to the PRIMARY sector?", choices=[
   "Taking materials directly from the earth -- farming, fishing, forestry and mining",
   "Turning raw materials into finished goods",
   "Selling goods to consumers in shops",
   "Analysing data and conducting research",
   "Setting the strategy of a large organization"], ans=0,
   why="EK SPS-7.B.1 names the primary sector first among the five. Everything else in an economy works on what this sector obtains, which is why it is first in the sequence as well as first in the list."),

 dict(q="What kind of activity belongs to the SECONDARY sector?", choices=[
   "Turning raw materials into finished or semi-finished goods -- manufacturing, processing and construction",
   "Extracting minerals from the ground",
   "Providing haircuts, meals and retail service",
   "Producing and interpreting information",
   "Making the highest-level decisions in government"], ans=0,
   why="EK SPS-7.B.1 names the secondary sector among the five, and EK SPS-7.B.2 is entirely about the location of MANUFACTURING, which is this sector. Adding value by transforming a material is what the category records."),

 dict(q="What kind of activity belongs to the TERTIARY sector?", choices=[
   "Providing services directly to people and businesses -- retail, transport, hospitality and routine office work",
   "Growing crops and catching fish",
   "Assembling components into finished products",
   "Conducting scientific research",
   "Deciding the direction of a national government"], ans=0,
   why="EK SPS-7.B.1 names the tertiary sector among the five. What distinguishes it is that the output is a service performed rather than an object produced, which is why it grows as incomes rise and households buy work as well as goods."),

 dict(q="What kind of activity belongs to the QUATERNARY sector?", choices=[
   "Producing, processing and interpreting information -- research, data analysis, software and higher education",
   "Selling goods in shops and restaurants",
   "Extracting coal and iron ore",
   "Assembling vehicles in a factory",
   "Chairing the board of a multinational firm"], ans=0,
   why="EK SPS-7.B.1 names the quaternary sector among the five. It is separated from the tertiary sector by its material: the work produces knowledge rather than delivering a service to a customer standing in front of it."),

 dict(q="What kind of activity belongs to the QUINARY sector?", choices=[
   "The highest-level decision-making in large organizations and governments, carried out by a very small number of people",
   "Routine clerical work in a large office",
   "Scientific research in a university laboratory",
   "Retail sales in a department store",
   "The mining of metal ores"], ans=0,
   why="EK SPS-7.B.1 names the quinary sector as the last of the five. What defines it is authority rather than subject: the work is deciding what an organization will do, which is why the sector is very small in employment and disproportionate in effect."),

 dict(q="What does the framework mean by saying the sectors are characterized by DISTINCT DEVELOPMENT PATTERNS?", choices=[
   "Each sector dominates employment at a different stage, so the sectoral composition of a workforce is itself a measure of development",
   "Each sector employs exactly the same share of workers everywhere",
   "The sectors developed simultaneously in every country",
   "Only the primary sector exists in any real economy",
   "The sectors are unrelated to a country's level of development"], ans=0,
   why="EK SPS-7.B.1 says the different economic sectors are characterized by distinct development patterns. That is a claim about sequence rather than about definition, and it is what makes a table of sector shares readable as a development measure."),

 dict(q="What distinguishes tertiary from quaternary work, given that both are commonly called services?", choices=[
   "Tertiary work delivers a service to a customer, while quaternary work produces and interprets information",
   "Tertiary work is paid and quaternary work is unpaid",
   "Tertiary work occurs in cities and quaternary work in rural areas",
   "Tertiary work uses machinery and quaternary work does not",
   "There is no difference between the two"], ans=0,
   why="EK SPS-7.B.1 lists tertiary and quaternary as separate sectors. Both sit outside extraction and manufacturing, so the line between them has to be drawn on what the work produces, and information is a different output from a service performed."),

 dict(q="What separates the quinary sector from the quaternary sector?", choices=[
   "Quinary work carries the authority to decide what an organization will do, while quaternary work supplies the analysis on which such decisions rest",
   "Quinary work is technical and quaternary work is managerial",
   "Quinary work occupies more people than quaternary work",
   "Quaternary work involves no information",
   "The two sectors are identical"], ans=0,
   why="EK SPS-7.B.1 names quaternary and quinary as the last two of five sectors. The distinction is one of authority rather than of subject matter, which is why the quinary sector is described as the smallest and highest rather than as a different field of work."),

 dict(q="Which set of factors does the framework say influences the location of manufacturing?", choices=[
   "Labour, transportation including shipping containers, the break-of-bulk point, least cost theory, markets, and resources",
   "Site, situation, and cycles of development",
   "Rank-size rule, primate city, gravity, and central place theory",
   "Mixed land use, walkability, and smart growth",
   "Redlining, blockbusting, and affordability"], ans=0,
   why="EK SPS-7.B.2 names exactly this set as influencing the location of manufacturing. The rejected sets belong to the urban topics of Unit 6 and describe where cities are, how they are sized and what is inside them rather than where a factory goes."),

 dict(q="In what two ways does LABOUR influence where manufacturing locates?", choices=[
   "Through what workers cost and through what skills they have, which pull in different directions for different products",
   "Only through what workers cost, since skill is the same everywhere",
   "Only through the number of workers available",
   "Labour has no influence on manufacturing location",
   "Only through the distance workers travel to work"], ans=0,
   why="EK SPS-7.B.2 names labor first among the influences on the location of manufacturing. Assembly requiring little training follows low wages, while production requiring particular expertise follows the places that have it, so a single word covers two opposite pulls."),

 dict(q="How did the shipping container change the geography of manufacturing?", choices=[
   "It cut the cost and time of moving goods so far that distant low-wage locations became viable suppliers to markets on other continents",
   "It raised the cost of long-distance shipping",
   "It made it necessary to manufacture goods near their markets",
   "It applied only to passenger travel",
   "It had no effect on where goods were produced"], ans=0,
   why="EK SPS-7.B.2 names transportation INCLUDING SHIPPING CONTAINERS among the influences on the location of manufacturing, which is an unusually specific mention. Standardizing the unit of cargo removed most of the handling cost from a sea journey, and what falls when transport falls is the penalty for distance."),

 dict(q="What is a break-of-bulk point?", choices=[
   "A place where goods are transferred from one mode of transport to another, such as a port where sea cargo moves to rail or road",
   "The point at which a machine breaks down in a factory",
   "The distance beyond which a product cannot be sold",
   "The moment at which a firm stops production",
   "A place where large orders are divided among several buyers"], ans=0,
   why="EK SPS-7.B.2 names the break-of-bulk point among the influences on the location of manufacturing. Handling costs money, so a place where cargo must be handled anyway is a place where processing it as well adds little to the total."),

 dict(q="What does least cost theory say determines where a manufacturer locates?", choices=[
   "The site where the combined cost of moving materials in, moving the product out, and labour is lowest",
   "The site with the largest available land area",
   "The site nearest the national capital",
   "The site with the most pleasant climate",
   "The site chosen at random among those available"], ans=0,
   why="EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing. It treats location as a minimization problem over costs that vary with place, which is why transport and labour are the terms it works with."),

 dict(q="A factory processes ore that loses most of its weight when refined. Where does least cost reasoning place it, and why?", choices=[
   "Near the ore, since moving the heavy raw material is far more expensive than moving the light refined product",
   "Near the market, since the finished product is more valuable",
   "Midway between the ore and the market in every case",
   "Wherever labour is cheapest, regardless of transport",
   "The theory makes no prediction for such an industry"], ans=0,
   why="EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing, and the weight lost in processing is what decides the pull. Carrying material that will be discarded is a cost avoided by discarding it before the journey."),

 dict(q="A factory makes a product that is far bulkier than the inputs it is assembled from. Where does least cost reasoning place it?", choices=[
   "Near the market, since the finished product is the expensive thing to move",
   "Near the raw materials, since inputs must be gathered",
   "At a break-of-bulk point regardless of the market",
   "Wherever land is cheapest",
   "The theory makes no prediction for such an industry"], ans=0,
   why="EK SPS-7.B.2 names least cost theory among the influences on manufacturing location, and the same logic that pulls a weight-losing industry to its materials pulls a weight-gaining one to its customers. What is expensive to move is what the location is arranged around."),

 dict(q="What is agglomeration, and why does it affect manufacturing location?", choices=[
   "The clustering of related firms in one place, which lets them share suppliers, skilled labour and infrastructure and lowers each one's costs",
   "The merging of several firms into one company",
   "The dispersal of a firm's plants across many regions",
   "The accumulation of unsold products in a warehouse",
   "The concentration of a firm's ownership in few hands"], ans=0,
   why="EK SPS-7.B.2 names least cost theory among the influences on the location of manufacturing, and the pull toward clustering is part of that account. A firm's costs depend on what is around it as well as on what it pays for transport and labour."),

 dict(q="How do MARKETS influence where manufacturing locates?", choices=[
   "Being near the buyers reduces the cost and time of delivery, which matters most for products that are bulky, fragile or urgently needed",
   "Markets have no influence on manufacturing location",
   "Being far from buyers reduces delivery costs",
   "Markets influence only the price of a product, never its production site",
   "Markets matter only for products that are exported"], ans=0,
   why="EK SPS-7.B.2 names markets among the influences on the location of manufacturing. The market is one end of the journey the product must make, so its position enters the location decision on exactly the same terms as the position of the materials."),

 dict(q="How do RESOURCES influence where manufacturing locates?", choices=[
   "An industry consuming large quantities of a bulky material is drawn toward its source, since moving it is a large share of total cost",
   "Resources determine the price of the finished product only",
   "Resources have no bearing on factory location",
   "Industries always locate as far from resources as possible",
   "Resources matter only in the primary sector"], ans=0,
   why="EK SPS-7.B.2 names resources among the influences on the location of manufacturing and EK SPS-7.A.1 says resource availability facilitated industrialization. The mechanism is the same in both statements: what is expensive to move is what a location is organized around."),

 dict(q="What do the terms core, semiperiphery and periphery describe in the framework's statement about manufacturing location?", choices=[
   "Positions in the world economy, so the statement is about which kinds of location attract which kinds of production",
   "Distances from the centre of a city",
   "The three shifts a factory operates in a day",
   "The stages of a product's assembly",
   "The zones of a von Thunen model"], ans=0,
   why="EK SPS-7.B.2 says these factors influence the location of manufacturing SUCH AS core, semiperiphery and periphery locations, and those categories come from the world-systems framework named in EK SPS-7.E.1. The statement is about a global division of production rather than about sites within one country."),

 dict(q="Why did cheaper container shipping tend to move assembly work toward peripheral and semiperipheral locations?", choices=[
   "Once distance costs little, the wage difference between locations outweighs the cost of shipping the product to its market",
   "Because containers can only be unloaded in peripheral countries",
   "Because core countries prohibited manufacturing",
   "Because peripheral locations have the largest markets",
   "Because shipping costs rose, forcing production to move"], ans=0,
   why="EK SPS-7.B.2 names transportation including shipping containers alongside labor and markets as influences on the location of manufacturing. Location is a comparison between costs, so reducing one of them to near nothing lets a different one decide the outcome."),

 dict(q="What is the principal limitation of least cost theory as an account of where factories go?", choices=[
   "It treats cost as the whole of the decision, so it does not capture government incentives, trade rules, exchange rates or the pull of existing supplier networks",
   "It cannot be applied to any real industry",
   "It ignores transport costs entirely",
   "It applies only to agricultural production",
   "It has no limitations, which is why the framework names it"], ans=0,
   why="EK SPS-7.B.2 lists least cost theory as one of six influences rather than as the explanation. A model that minimizes over transport and labour is a good account of the terms it contains, and the other five entries on the CED's own list are a reminder that it does not contain everything."),

 dict(q="At which two scales do the framework's location factors operate?", choices=[
   "The site scale, where a plant is placed relative to materials, market and a break-of-bulk point, and the global scale, where production is distributed among core, semiperipheral and peripheral locations",
   "Only the site scale, since factories occupy sites",
   "Only the global scale, since manufacturing is international",
   "Only the national scale, since governments regulate industry",
   "No scale, since location is an economic rather than a spatial question"], ans=0,
   why="EK SPS-7.B.2 names break-of-bulk points and resources, which are particular places, and core, semiperiphery and periphery, which are positions in the world economy. The same list of six factors answers a question about a site and a question about a continent."),

 dict(q="Which pairing of an activity with its sector is CORRECT?", choices=[
   "Writing software for a research institute, matched to the quaternary sector",
   "Writing software for a research institute, matched to the tertiary sector",
   "Catching fish at sea, matched to the secondary sector",
   "Assembling televisions in a factory, matched to the primary sector",
   "Serving meals in a restaurant, matched to the quaternary sector"], ans=0,
   why="EK SPS-7.B.1 names five sectors distinguished by what the work produces. Only one pairing here places an activity in the sector its output belongs to; each of the others moves an activity one or two steps along the CED's own sequence."),

 dict(q="Which pairing of a situation with the location factor it illustrates is CORRECT?", choices=[
   "A processing plant built at a port where cargo transfers from ship to rail, matched to the break-of-bulk point",
   "A processing plant built at a port where cargo transfers from ship to rail, matched to markets",
   "A firm moving assembly abroad to reduce wage costs, matched to resources",
   "A steel mill built beside an iron ore field, matched to shipping containers",
   "A bottling plant built near the city that drinks its output, matched to labour"], ans=0,
   why="EK SPS-7.B.2 names six distinct influences on the location of manufacturing. Only one pairing here matches a situation to the factor it actually illustrates, and each of the others attaches a case to a different factor on the same list."),

 dict(q="Employment by sector in four economies is recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Economy", "Primary (%)", "Secondary (%)", "Tertiary and above (%)"],
     rows=[["Economy 1", "58", "17", "25"],
           ["Economy 2", "31", "28", "41"],
           ["Economy 3", "12", "26", "62"],
           ["Economy 4", "2", "18", "80"]]),
   choices=[
   "The primary share falls from 58 to 2 percent while the tertiary and higher share rises from 25 to 80, and the secondary share rises and then falls, which is the pattern of a sequence rather than of unrelated cases",
   "All three shares rise together across the four economies",
   "The secondary share rises steadily across all four economies",
   "The primary share rises as the tertiary share rises",
   "The four economies have identical sectoral compositions"], ans=0,
   why="Each row sums to 100, the primary share falls at every step from 58 to 2 percent and the tertiary and higher share rises at every step from 25 to 80, while the secondary share rises from 17 to 28 and then falls back to 18. EK SPS-7.B.1 says the sectors are characterized by distinct development patterns, and a secondary share that peaks in the middle is what that pattern looks like."),

 dict(q="Three candidate sites for one factory are costed below. Using the accompanying figures, which does least cost reasoning select?",
   table=dict(headers=["Site", "Cost of moving materials in", "Cost of moving product out", "Labour cost"],
     rows=[["Site A", "40", "90", "50"],
           ["Site B", "70", "45", "55"],
           ["Site C", "95", "20", "70"]]),
   choices=[
   "Site B, whose total of 170 is below Site C's 185 and Site A's 180, even though it is cheapest on none of the three components",
   "Site A, because its materials cost is the lowest",
   "Site C, because its product transport cost is the lowest",
   "Site B, because it is cheapest on all three components",
   "All three sites are equally costly in total"], ans=0,
   why="Adding the three components gives 180, 170 and 185, so the lowest total belongs to a site that leads on none of them individually. EK SPS-7.B.2 names least cost theory among the influences on manufacturing location, and minimizing a SUM is what distinguishes it from choosing the cheapest single input."),

 dict(q="The cost and duration of moving a tonne of goods 8,000 kilometres by sea are recorded below. Using the accompanying figures, what has occurred?",
   table=dict(headers=["Period", "Cost per tonne (currency units)", "Days in transit"],
     rows=[["Before containerization", "78", "45"],
           ["Early containerization", "34", "26"],
           ["Mature container network", "12", "18"],
           ["Recent period", "6", "14"]]),
   choices=[
   "Cost per tonne fell from 78 to 6 and transit time from 45 days to 14, so distance became far less of an obstacle to sourcing goods from far away",
   "Cost per tonne fell while transit time rose",
   "Transit time fell while cost per tonne rose",
   "Neither cost nor transit time changed",
   "Cost fell by about half over the whole period"], ans=0,
   why="Cost falls at every step from 78 to 6 currency units, a factor of thirteen, and transit time from 45 to 14 days. EK SPS-7.B.2 names transportation including shipping containers among the influences on the location of manufacturing, and a cost falling by that much is what allows a distant wage difference to decide a location."),

 dict(q="What limitation should be stated when using shipping costs to explain where manufacturing has moved?", choices=[
   "Falling transport cost makes distant production possible without determining it, since wages, skills, trade rules and supplier networks all bear on the decision as well",
   "Shipping costs cannot be measured over time",
   "Costs and durations can never appear in the same record",
   "A falling cost establishes by itself where production will go",
   "The framework forbids the use of transport cost data"], ans=0,
   why="EK SPS-7.B.2 names transportation as one of SIX influences on the location of manufacturing. Cheap shipping removes an obstacle rather than supplying a destination, so the record explains why a distant location became possible and not why a particular one was chosen."),

 dict(q="A textbook must state what this topic's two statements establish. Which statement is accurate?", choices=[
   "Economies are made up of five sectors whose relative size shifts as development proceeds, and where manufacturing locates is decided by labour, transport, break-of-bulk points, cost minimization, markets and resources across core, semiperipheral and peripheral positions",
   "Economies are made up of three sectors and manufacturing locates wherever labour is cheapest",
   "The five sectors employ equal shares of workers in every economy",
   "Manufacturing location is determined by transport cost alone",
   "The sectors describe positions in the world economy rather than kinds of work"], ans=0,
   why="EK SPS-7.B.1 supplies the five sectors and their distinct development patterns, and EK SPS-7.B.2 supplies the six location influences and the three world-economy positions. Each rejected summary shortens one of the two lists or collapses the distinction between a kind of work and a kind of place."),
]
