# AP HUMAN GEOGRAPHY 6.7 Infrastructure -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding IMP-6, "The attitudes
# and values of a population, as well as the balance of power within that
# population, are reflected in the built landscape." Learning objective IMP-6.B,
# "Explain how a city's infrastructure relates to local politics, society, and
# the environment." Suggested skill 3.C, explain patterns and trends in maps and
# in quantitative and geospatial data.
#
# Essential knowledge -- ONE statement:
#   IMP-6.B.1  The location and quality of a city's infrastructure directly
#              affects its spatial patterns of economic and social development.
#
# THE STATEMENT HAS TWO INPUTS AND TWO OUTPUTS, and every item in the module is
# placed on that grid:
#
#                        ECONOMIC development     SOCIAL development
#   LOCATION of it       where firms, offices     which neighbourhoods can
#                        and housing get built    reach schools, clinics, work
#   QUALITY of it        whether a business can   whether a household has safe
#                        operate reliably         water, light and sanitation
#
# LOCATION and QUALITY are different variables and the CED names both. A district
# can be crossed by a trunk road it has no junction onto, and a district can have
# a water main that runs six hours a day. Items 3, 4 and 5 separate them and item
# 5 puts them together, because a single item asking only "does infrastructure
# matter" would test nothing.
#
# THE LEARNING OBJECTIVE ADDS THREE RELATIONSHIPS the essential knowledge does
# not: infrastructure and local POLITICS, SOCIETY and the ENVIRONMENT. Items 8,
# 9, 10, 11, 19, 23 and 24 cover them, and the politics items key on the
# mechanism -- infrastructure is expensive, durable and publicly decided, so the
# question of where a line goes is settled by whoever is in the room -- rather
# than attributing motives to any named party.
#
# WHAT COUNTS AS INFRASTRUCTURE, since the CED does not enumerate it: the
# transport network (roads, transit, ports, airports), the utility networks
# (water, sewerage, electricity, telecommunications) and the social facilities
# built to serve a population (schools, clinics, parks). Item 2 keys on the
# breadth of the category, because a student who hears only "roads" will miss
# most of what the statement covers.
#
# THE PROPERTY THAT MAKES INFRASTRUCTURE GEOGRAPHIC is that it is fixed in place
# and lasts for generations. A pipe laid once determines who has water for fifty
# years; a motorway cut through a neighbourhood divides it permanently. Items 12,
# 13, 15 and 22 rest on that durability, and item 15 supplies the reason
# infrastructure gaps persist: investment follows the districts that already
# generate revenue and demand, which is a loop rather than a decision.
#
# NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.7", "Infrastructure", 6)

QUESTIONS = [
 dict(q="What does the framework say about a city's infrastructure?", choices=[
   "Its location and quality directly affect the city's spatial patterns of economic and social development",
   "Its quality matters but its location does not",
   "Its location matters but its quality does not",
   "It has no effect on where development occurs",
   "It affects economic development but not social development"], ans=0,
   why="EK IMP-6.B.1 states that the location AND quality of a city's infrastructure directly affects its spatial patterns of economic AND social development. All four terms are in the sentence, and each rejected option removes one of them."),

 dict(q="Which set best captures what counts as a city's infrastructure?", choices=[
   "Transport networks, utility networks such as water, sewerage, power and telecommunications, and social facilities such as schools and clinics",
   "Roads and highways only",
   "Privately owned office buildings only",
   "The natural landforms on which the city is built",
   "The city's population and its age structure"], ans=0,
   why="EK IMP-6.B.1 refers to a city's infrastructure without enumerating it, and the category covers the built systems that make urban life possible. A student who hears only roads will miss the utility and social networks that most directly shape who can live and work where."),

 dict(q="How does the LOCATION of infrastructure affect a city's development pattern?", choices=[
   "Development concentrates where the network can be reached, so a station or an interchange pulls building toward it and land away from it is passed over",
   "Location has no effect, since infrastructure serves a whole city equally",
   "Development avoids places that are well served",
   "Location affects only the appearance of a district",
   "Location matters only for privately owned infrastructure"], ans=0,
   why="EK IMP-6.B.1 says the LOCATION of infrastructure directly affects spatial patterns of development. A network is reachable only at particular points, so its geography decides which sites are usable and which are not."),

 dict(q="How does the QUALITY of infrastructure affect development, independently of its location?", choices=[
   "A connection that is unreliable or unsafe cannot support the activity a reliable one would, so a district can be nominally served and still unable to attract investment",
   "Quality and location are the same variable under two names",
   "Quality affects appearance but not economic activity",
   "A connection either exists or does not, with no intermediate condition",
   "Quality matters only in rural areas"], ans=0,
   why="EK IMP-6.B.1 names QUALITY alongside location as a determinant of spatial patterns of development. A water main running six hours a day and a power supply failing daily are both present on a map and absent in practice, which is precisely the distinction the second term captures."),

 dict(q="A district lies beside a major rail line but has no station, and its electricity supply fails most evenings. What does the framework's statement predict?", choices=[
   "Weak economic and social development, since the district is poorly served on both the location and the quality dimensions the statement names",
   "Strong development, since the rail line passes through it",
   "No effect, since infrastructure does not influence development",
   "Strong development, since undeveloped land is cheap",
   "An effect on social development but none on economic development"], ans=0,
   why="EK IMP-6.B.1 names location and quality together as determinants of spatial patterns of economic and social development. Proximity without access is a failure of location, since a network is reachable only where it opens, and unreliable power is a failure of quality."),

 dict(q="What does the framework mean by a spatial pattern of ECONOMIC development?", choices=[
   "The uneven distribution of firms, jobs and investment across a city's districts",
   "The total value of a city's economy",
   "The average income of a city's residents",
   "The number of businesses registered in a country",
   "The rate at which a city's economy grows over time"], ans=0,
   why="EK IMP-6.B.1 says infrastructure affects a city's SPATIAL PATTERNS of economic and social development. The word spatial makes the claim about distribution within the city rather than about any city-wide total or growth rate."),

 dict(q="What does the framework mean by a spatial pattern of SOCIAL development?", choices=[
   "The uneven distribution across a city's districts of access to schooling, health care, safe water and the conditions of a decent life",
   "The total population of the city",
   "The number of social organizations in a city",
   "The average age of a city's residents",
   "The rate at which a city's population grows"], ans=0,
   why="EK IMP-6.B.1 names social development alongside economic development as something whose SPATIAL pattern infrastructure affects. Reading it as a city-wide measure loses the claim, which is about the differences between one district and another."),

 dict(q="How does a city's infrastructure relate to local politics?", choices=[
   "Infrastructure is expensive, long-lived and publicly decided, so where a line or a plant goes is settled through a political process rather than by the network's own logic",
   "Infrastructure decisions are made purely by engineers on technical grounds",
   "Infrastructure has no relationship to politics",
   "Infrastructure is decided by residents voting on each pipe individually",
   "Politics affects only privately financed infrastructure"], ans=0,
   why="Learning objective IMP-6.B asks how a city's infrastructure relates to local politics, society and the environment. A route can usually serve several alignments about equally well on technical grounds, and choosing among them distributes benefit and disruption, which is what makes it political."),

 dict(q="How does the distribution of infrastructure relate to a city's society?", choices=[
   "Districts with reliable networks can reach work, schooling and services that districts without them cannot, so the pattern of provision becomes a pattern of opportunity",
   "Infrastructure is distributed equally in every city",
   "Infrastructure affects buildings but not the people in them",
   "Only households that own vehicles are affected by infrastructure",
   "Social outcomes are unrelated to physical networks"], ans=0,
   why="EK IMP-6.B.1 says infrastructure directly affects spatial patterns of SOCIAL development. Access is what a network delivers, so where it reaches and how well it works determines what a household can get to on an ordinary day."),

 dict(q="How does a city's infrastructure relate to the environment through its surfaces?", choices=[
   "Roads, roofs and paving prevent rain from soaking into the ground, so more of it runs off quickly and flooding downstream becomes more likely",
   "Paved surfaces absorb more water than soil does",
   "Impervious surfaces have no effect on how water moves",
   "Paving reduces the total rainfall a city receives",
   "Runoff is determined only by the amount of rain that falls"], ans=0,
   why="Learning objective IMP-6.B asks how a city's infrastructure relates to the environment. Replacing soil and vegetation with sealed surfaces changes the path water takes rather than the amount that arrives, and a faster path means a higher peak flow."),

 dict(q="How does water and sanitation infrastructure relate to the environment and to public health at once?", choices=[
   "Collecting and treating waste keeps it out of the water people drink, so the same system protects the receiving rivers and the population's health together",
   "Sanitation affects health but has no environmental consequence",
   "Sanitation affects rivers but has no consequence for health",
   "Waste treatment increases contamination of drinking water",
   "Neither health nor the environment is affected by sanitation"], ans=0,
   why="Learning objective IMP-6.B asks how infrastructure relates to society and the environment, and EK IMP-6.B.1 makes its quality a determinant of social development. Untreated waste reaching a watercourse is simultaneously an environmental discharge and a route by which disease returns to the population."),

 dict(q="An elevated motorway is cut through the middle of an existing residential district. What is the most likely local effect?", choices=[
   "The district is physically divided, so journeys within it lengthen and the land beside the structure becomes less desirable",
   "The district becomes more unified because it is now accessible",
   "The district's property values rise uniformly",
   "Nothing changes locally, since the traffic passes through",
   "The district gains a new local street network"], ans=0,
   why="EK IMP-6.B.1 says the location of infrastructure directly affects spatial patterns of economic and social development. A route designed to move traffic through a place rather than to it is a barrier at ground level, and the benefit accrues to the through traveller while the disruption stays local."),

 dict(q="Why does an infrastructure decision commit a city for far longer than most other public decisions?", choices=[
   "The assets are physically fixed and last for decades, so a route or a network laid out once determines what is possible long after the decision is forgotten",
   "Because infrastructure decisions cannot legally be revisited",
   "Because infrastructure is rebuilt every few years",
   "Because infrastructure has no effect until decades have passed",
   "Because infrastructure can be moved easily when needs change"], ans=0,
   why="EK IMP-6.B.1 makes the LOCATION of infrastructure a determinant of spatial patterns of development. Durability is what converts a decision into a geography: the network of a century ago is still the network today in most cities, and everything built since has been fitted to it."),

 dict(q="Why do rapidly growing informal settlements often lack basic networks?", choices=[
   "They are built faster than networks can be extended and often on land whose occupation is not formally recognized, which makes public investment in it difficult",
   "Their residents do not want water or electricity",
   "Networks are physically impossible to build in such settlements",
   "Such settlements are always located outside city boundaries",
   "Their residents have already been served by another network"], ans=0,
   why="EK IMP-6.B.1 says the location and quality of infrastructure directly affects spatial patterns of social development. Networks are planned, financed and laid over years while settlement can happen in months, and an unrecognized tenure makes the investment harder to justify and to recover."),

 dict(q="Why does infrastructure provision tend to reinforce existing differences between districts?", choices=[
   "Investment tends to follow the districts that already generate demand and revenue, so well-served districts attract the activity that justifies further investment",
   "Because engineers prefer to work in wealthy districts",
   "Because poorly served districts refuse new infrastructure",
   "Because infrastructure costs more to build in poor districts in every case",
   "Because differences between districts are fixed and cannot change"], ans=0,
   why="EK IMP-6.B.1 says infrastructure directly affects spatial patterns of economic and social development, and the relationship runs in both directions over time. A district with reliable service attracts firms and households, whose activity then supplies the case for the next investment there."),

 dict(q="Why is maintenance of existing infrastructure often neglected in favour of new construction?", choices=[
   "A new line or plant is visible and attributable while maintenance prevents a failure that nobody sees, so the political return on the two is very different",
   "Maintenance is more expensive than new construction in every case",
   "Existing infrastructure does not deteriorate",
   "Maintenance produces no benefit of any kind",
   "New construction requires no political decision"], ans=0,
   why="Learning objective IMP-6.B asks how a city's infrastructure relates to local politics, and this is one of the clearest instances. EK IMP-6.B.1 makes QUALITY a determinant of development, and deferred maintenance is exactly how quality falls while the map still shows a network."),

 dict(q="At which two scales must a city's infrastructure be examined to understand its effects?", choices=[
   "The neighbourhood, where a household either has a working connection or does not, and the metropolitan area, where the network's overall shape determines which districts are connected to which",
   "Only the metropolitan scale, since networks are city-wide",
   "Only the household scale, since services are consumed by households",
   "Neither scale, since infrastructure is not a spatial subject",
   "Only the national scale, since governments fund infrastructure"], ans=0,
   why="EK IMP-6.B.1 says infrastructure affects SPATIAL PATTERNS of economic and social development, and a pattern exists only when districts are compared. The metropolitan network decides what is reachable and the local connection decides whether a particular household can use it."),

 dict(q="Which measure would best capture the QUALITY rather than merely the presence of a city's water supply?", choices=[
   "The number of hours per day the supply runs and whether the water meets safety standards",
   "The total length of water mains in the city",
   "The number of districts the network passes through",
   "The year the network was first built",
   "The number of people employed by the water utility"], ans=0,
   why="EK IMP-6.B.1 names location and quality as two separate determinants, so a measure of one is not a measure of the other. Pipe length and coverage describe where the network goes, while hours of service and water safety describe whether it does what it exists to do."),

 dict(q="What is green infrastructure, and how does it relate to the framework's account?", choices=[
   "Vegetated and permeable features -- parks, street trees, wetlands, permeable paving -- built to manage water and heat alongside conventional networks",
   "Any infrastructure painted green",
   "Infrastructure built entirely without public money",
   "The removal of all built infrastructure from a city",
   "Infrastructure that serves only agricultural land"], ans=0,
   why="Learning objective IMP-6.B asks how a city's infrastructure relates to the environment. Sealed surfaces speed runoff and store heat, and vegetated permeable features work on the same problems by restoring the processes the sealed surfaces removed."),

 dict(q="Why did piped water and sewerage produce such large improvements in urban health?", choices=[
   "They separated drinking water from human waste, which interrupted the transmission of the diseases that had spread most readily in dense settlement",
   "They increased the total amount of water available for drinking",
   "They eliminated all disease from cities",
   "They allowed cities to be built at lower densities",
   "They reduced the cost of housing construction"], ans=0,
   why="EK IMP-6.B.1 makes the quality of infrastructure a determinant of spatial patterns of social development. Density concentrates people and their waste in the same place, so the network that keeps the two apart is what makes dense settlement survivable."),

 dict(q="Why is telecommunications capacity now treated as infrastructure in the same sense as roads and water?", choices=[
   "Access to a reliable connection determines what work, schooling and services a household or firm can obtain, so its distribution shapes development the way a physical network does",
   "Because cables are buried in the ground like pipes",
   "Because telecommunications is provided free everywhere",
   "Because it replaces the need for transport entirely",
   "Because it has no effect on economic activity"], ans=0,
   why="EK IMP-6.B.1 says the location and quality of a city's infrastructure directly affects spatial patterns of economic and social development. What makes something infrastructure is that access to it conditions what everything else can do, which is a functional test rather than a physical one."),

 dict(q="Why does new transport infrastructure usually raise land values near it?", choices=[
   "Access is part of what a site is worth, so improving the access improves the site without anything changing on the land itself",
   "Because construction physically improves the soil",
   "Because land near infrastructure is always scarcer",
   "Because governments set land values directly",
   "Land values are unaffected by transport provision"], ans=0,
   why="EK IMP-6.B.1 says the location of infrastructure directly affects spatial patterns of economic development, and land value is where that effect is first registered. What a site can be used for depends on what can reach it, so a new connection changes the site's possible uses and therefore its price."),

 dict(q="A metropolitan area is divided among many small municipalities, each responsible for its own networks. What difficulty does this create?", choices=[
   "A network that must cross many boundaries requires agreement among authorities whose interests differ, so provision can be uneven or stall entirely",
   "Fragmentation makes network construction cheaper and faster",
   "Fragmentation has no effect on infrastructure",
   "Each municipality automatically builds identical networks",
   "Networks do not cross municipal boundaries in any city"], ans=0,
   why="Learning objective IMP-6.B asks how a city's infrastructure relates to local politics. A network's logic is metropolitan while the authority to build it may be divided a dozen ways, and EK IMP-6.B.1's location variable is exactly what such a division determines."),

 dict(q="Why is deciding who pays for a piece of urban infrastructure a political question and not only a financial one?", choices=[
   "The people who pay and the people who benefit are often in different places, so any method of raising the money distributes the cost across districts",
   "Because the total cost is unknowable",
   "Because infrastructure is always paid for by its direct users",
   "Because financing has no relationship to who benefits",
   "Because every district benefits equally from every project"], ans=0,
   why="Learning objective IMP-6.B asks how infrastructure relates to local politics, and EK IMP-6.B.1 makes its location a determinant of spatial patterns of development. A project in one district paid for city-wide, or paid for locally and used regionally, is a transfer between places however it is described."),

 dict(q="Which pairing of an observation with the relationship it illustrates is CORRECT?", choices=[
   "Storm runoff rising as a catchment is paved over, matched to infrastructure and the environment",
   "Storm runoff rising as a catchment is paved over, matched to infrastructure and local politics",
   "A council choosing between two alignments for a new rail line, matched to infrastructure and the environment",
   "Households in one district lacking a safe water connection, matched to infrastructure and the environment",
   "A wetland restored to absorb floodwater, matched to infrastructure and local politics"], ans=0,
   why="Learning objective IMP-6.B names politics, society and the environment as three relationships. Only one pairing here matches an observation to the relationship it actually illustrates, and each of the others attaches an observation to one of the other two."),

 dict(q="Four districts of one city are recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["District", "Households with a piped water connection (%)", "Hours of electricity supply per day", "Paved road share (%)", "Deaths before age five per 1,000 births"],
     rows=[["District 1", "98", "24", "96", "6"],
           ["District 2", "71", "19", "62", "18"],
           ["District 3", "44", "11", "28", "41"],
           ["District 4", "22", "6", "9", "63"]]),
   choices=[
   "All three infrastructure measures fall together from District 1 to District 4 while child mortality rises from 6 to 63 per 1,000, so provision and outcome move in opposite directions",
   "Infrastructure provision and child mortality rise together",
   "Child mortality is highest in the best-served district",
   "The three infrastructure measures disagree about which district is best served",
   "No pattern can be read, since four different units appear"], ans=0,
   why="Water coverage, electricity hours and paved road share all fall at every step across the four districts while deaths before age five rise from 6 to 63 per thousand. EK IMP-6.B.1 says the location and quality of infrastructure directly affects spatial patterns of social development, and three independent measures agreeing is what makes the pattern readable."),

 dict(q="New construction near a rail station opened ten years earlier is recorded below. Using the accompanying figures, what does the record show?",
   table=dict(headers=["Distance from the station (metres)", "New floor area built in the decade (thousand square metres)"],
     rows=[["0 to 400", "640"],
           ["400 to 800", "310"],
           ["800 to 1,600", "120"],
           ["1,600 to 3,200", "45"]]),
   choices=[
   "New building falls steeply with distance from the station, from 640 thousand square metres in the nearest band to 45 in the furthest",
   "New building rises with distance from the station",
   "New building is spread evenly across the four bands",
   "The furthest band received the most new floor area",
   "No relationship to distance can be read from the record"], ans=0,
   why="Floor area falls at every step from 640 to 310 to 120 to 45 thousand square metres as distance from the station rises. EK IMP-6.B.1 says the LOCATION of infrastructure directly affects spatial patterns of economic development, and a network reachable only at particular points concentrates building around those points."),

 dict(q="Storm runoff in four catchments of one city is recorded below. Using the accompanying figures, what does the record show?",
   table=dict(headers=["Catchment", "Impervious surface (% of catchment)", "Peak storm runoff (cubic metres per second)"],
     rows=[["Catchment W", "12", "4.1"],
           ["Catchment X", "28", "9.8"],
           ["Catchment Y", "51", "19.6"],
           ["Catchment Z", "74", "31.5"]]),
   choices=[
   "Peak runoff rises from 4.1 to 31.5 cubic metres per second as impervious surface rises from 12 to 74 percent, so sealing the surface raises the flood peak",
   "Peak runoff falls as impervious surface rises",
   "Peak runoff is unrelated to impervious surface",
   "The catchment with the least paving has the highest peak runoff",
   "The two measures cannot be compared, since they use different units"], ans=0,
   why="Impervious surface rises at every step from 12 to 74 percent and peak runoff rises with it from 4.1 to 31.5 cubic metres per second, more than a sevenfold increase. Learning objective IMP-6.B asks how a city's infrastructure relates to the environment, and sealed surfaces sending rain to the drain instead of into the ground is the mechanism."),

 dict(q="What limitation should be stated when using district-level infrastructure and health figures together?", choices=[
   "Districts differ in income, crowding and other conditions as well as in infrastructure, so the record shows provision and outcome moving together without isolating the cause",
   "Infrastructure coverage cannot be measured by district",
   "Percentages and rates can never appear in the same record",
   "A consistent pattern across four districts proves its own cause",
   "The framework forbids linking infrastructure to health outcomes"], ans=0,
   why="EK IMP-6.B.1 says infrastructure DIRECTLY AFFECTS spatial patterns of social development, but a table of districts cannot by itself separate that effect from everything else that varies between them. Poorly served districts are usually poorer in other respects too, which is why the pattern is consistent with the claim rather than a demonstration of it."),

 dict(q="Which sentence states what this topic establishes, using both of the framework's input terms and both of its outputs?", choices=[
   "Where a city's networks run and how well they work together determine which districts get investment and jobs and which households can reach services",
   "The quality of a city's networks determines its total economic output",
   "The location of a city's networks affects appearance but not opportunity",
   "A city's infrastructure affects its economy but not its society",
   "Infrastructure is distributed evenly within cities and so explains nothing"], ans=0,
   why="EK IMP-6.B.1 names location AND quality as the inputs and spatial patterns of economic AND social development as the outputs. Each rejected summary drops one of those four terms, and the last denies the unevenness that makes the statement a claim about pattern at all."),
]
