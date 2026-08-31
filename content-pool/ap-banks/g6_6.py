# AP HUMAN GEOGRAPHY 6.6 Density and Land Use -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding IMP-6, "The attitudes
# and values of a population, as well as the balance of power within that
# population, are reflected in the built landscape." Learning objective IMP-6.A,
# "Explain how low-, medium-, and high-density housing characteristics represent
# different patterns of residential land use." Suggested skill 3.D, compare
# patterns and trends in quantitative and geospatial data.
#
# Essential knowledge -- ONE statement, and it is dense:
#   IMP-6.A.1  Residential buildings and patterns of land use reflect and shape
#              the city's culture, technological capabilities, cycles of
#              development, and infilling.
#
# "REFLECT AND SHAPE" IS THE WHOLE ARCHITECTURE OF THIS STATEMENT and item 1
# keys on it. The relationship runs BOTH WAYS. Buildings reflect the culture,
# technology and moment that produced them -- so a district's housing is
# evidence about the period it was built in. And buildings then shape what the
# people living in them can do, because a street of detached houses on large lots
# cannot support a tram line or a corner shop however much its residents might
# later want one. Items 12, 13, 14 and 24 run the second direction, which is the
# half students drop.
#
# THE FOUR THINGS THE STATEMENT NAMES, and what each contributes:
#   culture                 what households want and expect -- privacy, a yard,
#                           room for an extended family, a street to walk on
#   technological           what is physically possible -- an elevator and a
#     capabilities          steel frame permit height; piped water and sewerage
#                           permit density at all
#   cycles of development   a district's buildings mostly date from the boom that
#                           built it, so density is set for decades at a stroke
#   infilling               new building on vacant or underused land INSIDE the
#                           already-built area, which raises density without
#                           extending the city outward
# Items 6 to 11 take them in turn, and items 18, 26, 27 and 28 read each off
# data.
#
# THE THREE DENSITY BANDS the learning objective names, with the working
# descriptions used throughout, since the CED supplies no thresholds:
#   low      detached houses on their own plots, few dwellings per hectare
#   medium   townhouses, terraces, duplexes and low-rise apartment blocks
#   high     mid-rise and high-rise apartment buildings
# The bands are a continuum with no fixed cut-points, and item 20 keys on the
# measurement question the CED's own suggested skill implies: density means
# nothing until the denominator is stated, and GROSS density (everything inside
# the boundary, roads and parks included) and NET density (residential land only)
# can differ by a factor of two on the same ground. Item 29 makes that the data
# limitation.
#
# NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.6", "Density and Land Use", 6)

QUESTIONS = [
 dict(q="According to the framework, what is the relationship between a city's residential buildings and its culture, technology and development history?", choices=[
   "Buildings and land-use patterns both reflect those things and shape them in turn",
   "Buildings reflect them but have no influence of their own",
   "Buildings shape them but reflect nothing about the past",
   "There is no relationship between buildings and culture",
   "Buildings reflect climate alone"], ans=0,
   why="EK IMP-6.A.1 says residential buildings and patterns of land use REFLECT AND SHAPE the city's culture, technological capabilities, cycles of development and infilling. Both verbs are in the sentence, and the second is the one students overlook."),

 dict(q="What characterizes LOW-density residential land use?", choices=[
   "Detached houses standing on their own plots, so few dwellings occupy each hectare",
   "Mid-rise and high-rise apartment buildings",
   "Terraced houses and low-rise apartment blocks",
   "Land used entirely for offices and retail",
   "Land with no buildings on it at all"], ans=0,
   why="Learning objective IMP-6.A asks how low-, medium- and high-density housing characteristics represent different patterns of residential land use. Low density is defined by how much land each dwelling occupies, which is what makes it a land-use category rather than an architectural one."),

 dict(q="What characterizes MEDIUM-density residential land use?", choices=[
   "Townhouses, terraces, duplexes and low-rise apartment blocks, sharing walls or stacked a few storeys high",
   "Detached houses on large individual plots",
   "Towers of twenty storeys and above",
   "Warehousing and light industry",
   "Farmland at the metropolitan edge"], ans=0,
   why="Learning objective IMP-6.A names low, medium and high density as the three patterns of residential land use. The medium band is where dwellings begin to share walls or stack, which raises the number per hectare without requiring the technology a tower needs."),

 dict(q="What characterizes HIGH-density residential land use?", choices=[
   "Mid-rise and high-rise apartment buildings housing many dwellings on a small footprint",
   "Detached houses on quarter-hectare plots",
   "Single-storey terraces with private gardens",
   "Land held vacant for future development",
   "Low-rise buildings spread across a wide area"], ans=0,
   why="Learning objective IMP-6.A names high density among the three patterns of residential land use. Stacking dwellings vertically is what allows a small footprint to hold many households, which is why high density and building height are so closely associated."),

 dict(q="Roughly how does the land each dwelling occupies change across the three density bands?", choices=[
   "It falls sharply, so a high-density district can hold tens of times as many dwellings per hectare as a low-density one",
   "It stays about the same across all three",
   "It rises as density rises",
   "It falls only slightly, by around a tenth at each step",
   "It cannot be compared between the bands"], ans=0,
   why="Learning objective IMP-6.A distinguishes the three bands by their housing characteristics, and the land per dwelling is what those characteristics amount to spatially. The range from a detached house on its own plot to an apartment tower is an order of magnitude or more, not a marginal difference."),

 dict(q="How can a city's residential buildings REFLECT its culture?", choices=[
   "What households expect -- privacy, a garden, space for an extended family, a street life -- is built into the housing they choose and can afford",
   "Culture has no expression in the built environment",
   "Buildings reflect only the climate of the region",
   "Buildings reflect only the wealth of their owners",
   "Culture determines building height directly and nothing else"], ans=0,
   why="EK IMP-6.A.1 names culture first among the things residential buildings and land-use patterns reflect and shape. Housing is the most expensive purchase most households make, so what they want out of a dwelling is visible in what gets built."),

 dict(q="This topic's enduring understanding says the built landscape reflects the balance of power within a population as well as its attitudes and values. How does residential density show that?", choices=[
   "Whose preferences get built depends on who owns land, who lends, and who sets the rules, so the housing that exists records which groups' wishes prevailed",
   "Every household's preferences are built in equal measure",
   "The balance of power affects public buildings but never housing",
   "Housing reflects only the preferences of the people currently living in it",
   "Power has no expression in the physical form of a city"], ans=0,
   why="Enduring understanding IMP-6 states that the attitudes and values of a population AND the balance of power within it are reflected in the built landscape, and EK IMP-6.A.1 applies that to residential buildings. A dwelling is built by whoever can assemble the land, the finance and the permission, so the stock that exists is a record of who could do those things."),

 dict(q="Which technological capabilities made high-density residential development possible?", choices=[
   "The safety elevator and the steel frame, which made buildings usable and buildable above a few storeys",
   "The private car, which allowed people to live further apart",
   "The telephone, which removed the need to live near work",
   "Refrigeration, which allowed food to be stored at home",
   "The pneumatic tyre, which improved road surfaces"], ans=0,
   why="EK IMP-6.A.1 names technological capabilities among the things residential buildings reflect and shape. Height is the route to density on a small footprint, and it is impossible in practice without a way to move people up and a structure that carries the load."),

 dict(q="Why is piped water and sewerage a precondition for dense residential settlement?", choices=[
   "Concentrating thousands of people on a small area requires water to be brought in and waste taken away, which cannot be done by wells and pits at that density",
   "Because dense districts use less water per person",
   "Because pipes are required by law in all buildings",
   "Because piped water makes buildings physically stronger",
   "Because dense districts have no need for sanitation"], ans=0,
   why="EK IMP-6.A.1 names technological capabilities among the things that shape residential land use. Density is limited by whatever supporting system fails first, and before piped networks existed that was sanitation rather than construction."),

 dict(q="What does the framework mean by CYCLES OF DEVELOPMENT?", choices=[
   "A district is largely built during one period of building activity, so its housing type and density record the practice of that period",
   "The daily movement of commuters into and out of a city",
   "The seasonal variation in construction activity",
   "The rotation of land between agricultural and urban use",
   "The regular replacement of every building every twenty years"], ans=0,
   why="EK IMP-6.A.1 names cycles of development among the things residential buildings and land use reflect and shape. Building happens in waves, and what a wave puts up stands for generations, so a district's density is largely fixed by the moment it was built out."),

 dict(q="What is infilling?", choices=[
   "New building on vacant or underused sites inside the already-built area rather than at the city's edge",
   "The outward extension of a city onto farmland",
   "The demolition of an entire district",
   "The filling of a harbour to create new land",
   "The conversion of housing into offices"], ans=0,
   why="EK IMP-6.A.1 names infilling among the things residential buildings and patterns of land use reflect and shape. The defining feature is the location of the site: inside the existing built-up area rather than beyond its edge."),

 dict(q="Why does infilling raise a city's density without expanding its area?", choices=[
   "The additional dwellings are built on land already inside the city, so population rises while the built-up area does not",
   "Because infill dwellings are always taller than existing ones",
   "Because infilling requires demolishing more than it builds",
   "Because infill sites lie outside the city boundary",
   "Because infilling reduces the number of dwellings overall"], ans=0,
   why="EK IMP-6.A.1 names infilling alongside cycles of development. Density is population divided by area, so adding to the numerator while holding the denominator fixed is exactly what building on interior sites does."),

 dict(q="How do residential buildings SHAPE the behaviour of the people who live among them, rather than merely reflecting it?", choices=[
   "The density and layout fix how far ordinary destinations are, which determines whether walking, transit or driving is practical for decades afterward",
   "Buildings have no influence on how residents travel or shop",
   "Buildings determine residents' incomes directly",
   "Buildings shape only the appearance of a district",
   "Residents can change a district's density whenever they choose"], ans=0,
   why="EK IMP-6.A.1 says residential buildings and land-use patterns reflect AND SHAPE the city's culture and development. A street laid out at four dwellings per hectare puts every shop beyond walking distance, and that constraint outlives whoever chose the layout."),

 dict(q="Why does residential density largely determine whether frequent public transport is viable?", choices=[
   "A route needs enough potential passengers within walking distance of each stop, and low density does not supply them",
   "Because low-density districts are legally barred from having transit",
   "Because vehicles cannot operate on suburban roads",
   "Because dense districts have fewer people who need to travel",
   "Because transit costs the same to run regardless of ridership"], ans=0,
   why="EK IMP-6.A.1 says residential buildings and land-use patterns shape as well as reflect the city. Transit economics is a ratio of riders to route length, and dwellings per hectare is the numerator, which is why the housing decision effectively makes the transport decision."),

 dict(q="Why does low-density residential land use raise the per-household cost of municipal services?", choices=[
   "Pipes, wires, roads and collection routes are paid for by length, and low density means more length serving each household",
   "Because low-density households consume more of every service",
   "Because materials cost more in suburban areas",
   "Because low-density districts have more residents in total",
   "Because services are provided free in dense districts"], ans=0,
   why="EK IMP-6.A.1 says patterns of land use shape the city, and infrastructure cost is one of the clearest routes by which they do. A kilometre of water main costs about the same whether it serves twenty households or two hundred."),

 dict(q="How is residential density connected to land value in a city?", choices=[
   "Expensive land is built on more intensively, since a developer must earn more from each square metre to justify the price paid for it",
   "Expensive land is always built on least intensively",
   "Land value and density are unrelated",
   "Density determines land value entirely, with no other influence",
   "Land value falls as density rises in every case"], ans=0,
   why="EK IMP-6.A.1 names technological capabilities among the things shaping residential land use, and bid-rent theory in EK PSO-6.D.1 supplies the economic half. Height is the way to spread an expensive site across more saleable floor area, so the density gradient tracks the land-value gradient."),

 dict(q="What does a district of detached houses on large plots imply about daily life there?", choices=[
   "Most destinations are too far to walk to, so nearly all trips are made by car and services must be reached rather than encountered",
   "Residents can reach shops and schools on foot in a few minutes",
   "The district supports frequent bus service easily",
   "The district has the lowest infrastructure cost per household",
   "The district's residents make fewer trips than others"], ans=0,
   why="EK IMP-6.A.1 says residential buildings and land-use patterns shape the city. Low density spreads destinations out, and a distance too great to walk converts every errand into a vehicle trip, which is the practical meaning of the housing pattern."),

 dict(q="What does a district of mid-rise apartment buildings imply about daily life there?", choices=[
   "Enough people live within a short distance to support shops, schools and frequent transit within walking range",
   "Residents must drive to reach every service",
   "The district cannot support any retail",
   "Each household occupies more land than in a suburban district",
   "The district costs more per household to service"], ans=0,
   why="EK IMP-6.A.1 says residential buildings and land use shape the city as well as reflecting it. A shop needs a threshold of customers within its range, and stacking households is how a small area assembles one, which is why dense districts have street-level retail and low-density ones do not."),

 dict(q="A geographer records the median construction date of the housing in each ring of a metropolitan area and finds it rises steadily with distance from the centre. What does this record?", choices=[
   "Cycles of development, since each ring was built out in a later wave than the one inside it",
   "Infilling, since new building has occurred throughout",
   "That the outer rings are older than the inner ones",
   "That construction dates are unrelated to location",
   "That the city grew inward from its edges"], ans=0,
   why="EK IMP-6.A.1 names cycles of development among the things residential buildings and patterns of land use reflect. A city that grew outward built each ring in a later period, so building age is a direct record of the sequence of growth."),

 dict(q="At which scales can residential density be measured, and why does the choice matter?", choices=[
   "At the parcel, the district or the whole metropolitan area, and the figure changes greatly between them because each includes different amounts of non-residential land",
   "Only at the metropolitan scale, since density is a city-wide measure",
   "Only at the parcel scale, since buildings occupy parcels",
   "Density does not vary with the scale at which it is measured",
   "Density can be measured only for an entire country"], ans=0,
   why="The suggested skill for this topic is comparing patterns and trends in quantitative data, and a density is a ratio whose denominator has to be stated. A metropolitan figure averages farmland and parkland in with apartment blocks, so it can be a tenth of the density of the districts inside it."),

 dict(q="What is the difference between gross and net residential density?", choices=[
   "Gross density divides population by all the land inside a boundary, while net density divides it by the residential land only, so net is always the larger figure",
   "Gross density counts only apartments and net density counts only houses",
   "Net density divides by all land and gross density by residential land only",
   "The two always give the same figure",
   "Gross density is measured at night and net density during the day"], ans=0,
   why="The suggested skill for this topic is comparing patterns and trends in quantitative data, and this is the commonest ambiguity in a density figure. Roads, schools, parks and industry are inside the boundary and hold no residents, so excluding them raises the figure, sometimes by a factor of two."),

 dict(q="Two cities with the same technology and similar incomes have very different residential densities. What does the framework's statement suggest?", choices=[
   "Culture and the cycles in which each city was built also shape residential land use, so technology alone does not determine density",
   "One of the two cities must have measured its density incorrectly",
   "Technology fully determines density, so the observation is impossible",
   "Density is unrelated to anything a geographer can study",
   "The two cities must have different climates"], ans=0,
   why="EK IMP-6.A.1 names culture, technological capabilities, cycles of development and infilling together. Technology sets what is possible rather than what is chosen, so two cities with the same possibilities can differ because of what their residents wanted and when their housing was built."),

 dict(q="How does building on an infill site differ from building on a greenfield site at the metropolitan edge?", choices=[
   "The infill site is already served by existing roads and pipes, while the edge site requires new infrastructure and converts land not previously built on",
   "The infill site requires more new infrastructure than the edge site",
   "The two are identical in every respect except location",
   "The edge site is always inside the existing built-up area",
   "The infill site consumes more farmland"], ans=0,
   why="EK IMP-6.A.1 names infilling among the things residential buildings and patterns of land use reflect and shape. Building inside the served area uses capacity already paid for, which is the reason infill and outward expansion have such different consequences for a city's finances and its footprint."),

 dict(q="Why is a district's density difficult to change once it has been built?", choices=[
   "The buildings are durable and are owned by many separate parties, so raising density requires assembling sites and replacing structures that still have decades of life",
   "Because density is fixed permanently by law in every city",
   "Because buildings cannot be demolished for any reason",
   "Because residents have no interest in their surroundings",
   "Because a district's density is set by its climate"], ans=0,
   why="EK IMP-6.A.1 names cycles of development among the things residential land use reflects and shapes. A wave of building fixes a density in physical form, and the cost and coordination required to undo it are what make the resulting pattern outlast the era that produced it."),

 dict(q="Which pairing of an observation with what the framework says it reflects is CORRECT?", choices=[
   "New apartments built on a disused rail yard inside the city, matched to infilling",
   "New apartments built on a disused rail yard inside the city, matched to cycles of development",
   "A ring of housing all built within one decade, matched to infilling",
   "Elevators and steel frames permitting tall buildings, matched to culture",
   "A preference for a private garden, matched to technological capabilities"], ans=0,
   why="EK IMP-6.A.1 names culture, technological capabilities, cycles of development and infilling as four distinct things. Only one pairing here matches an observation to the one it actually illustrates; each of the others swaps two of the statement's own categories."),

 dict(q="Five residential forms are recorded below. Using the accompanying figures, what do they show?",
   table=dict(headers=["Residential form", "Dwellings per hectare", "Persons per square kilometre"],
     rows=[["Detached houses, large plots", "6", "1,400"],
           ["Detached houses, small plots", "14", "3,300"],
           ["Townhouses", "38", "8,700"],
           ["Low-rise apartments", "85", "19,000"],
           ["High-rise apartments", "240", "52,000"]]),
   choices=[
   "The densest form holds 240 dwellings per hectare against 6 for the least dense, a fortyfold difference, and both columns rise together",
   "The two columns move in opposite directions",
   "The densest form holds about twice as many dwellings per hectare as the least dense",
   "Dwellings per hectare rises while persons per square kilometre falls",
   "All five forms have the same density"], ans=0,
   why="Dwellings per hectare rises at every step from 6 to 240, a factor of forty, and persons per square kilometre rises with it from 1,400 to 52,000. Learning objective IMP-6.A asks how low-, medium- and high-density housing represent different patterns of residential land use, and the spread between the bands is what that difference amounts to."),

 dict(q="The housing of one metropolitan area by distance band is recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Distance from the centre (kilometres)", "Median year of construction", "Dominant housing form"],
     rows=[["0 to 2", "1908", "Mid-rise apartments"],
           ["2 to 6", "1936", "Townhouses and duplexes"],
           ["6 to 12", "1965", "Detached houses, small plots"],
           ["12 to 25", "1994", "Detached houses, large plots"]]),
   choices=[
   "Median construction year rises from 1908 to 1994 with distance while density falls, so each ring records the building practice of a later period",
   "The outermost ring contains the oldest housing",
   "Median construction year falls with distance from the centre",
   "All four rings were built in the same decade",
   "Housing form is unrelated to when a ring was built"], ans=0,
   why="The median construction year rises at every step from 1908 to 1994 while the dominant form moves from mid-rise apartments to detached houses on large plots. EK IMP-6.A.1 names cycles of development among the things residential buildings reflect, and a district built later was built to the practice of a later and less dense period."),

 dict(q="New housing in one city by site type is recorded below. Using the accompanying figures, what has occurred?",
   table=dict(headers=["Year", "New dwellings on infill sites", "New dwellings on greenfield sites", "Land newly built on (hectares)"],
     rows=[["2000", "1,200", "4,800", "620"],
           ["2010", "2,600", "3,900", "480"],
           ["2020", "5,100", "2,400", "260"]]),
   choices=[
   "The infill share of new dwellings rose from 20 to 68 percent while total new dwellings rose from 6,000 to 7,500 and land newly built on fell from 620 to 260 hectares",
   "The infill share fell across the period",
   "Total new dwellings fell across the period",
   "Land newly built on rose as infill increased",
   "Greenfield building rose while infill fell"], ans=0,
   why="Adding the two columns gives 6,000, 6,500 and 7,500 new dwellings, of which the infill share is 20, 40 and 68 percent, while land newly built on falls from 620 to 260 hectares. EK IMP-6.A.1 names infilling among the things residential land use reflects and shapes, and building more homes on less new land is exactly what a shift toward infill produces."),

 dict(q="What limitation should be stated when comparing residential densities between two cities?", choices=[
   "The figures are comparable only if both use the same denominator, since a gross density including parks and industry is not comparable with a net density covering residential land alone",
   "Densities cannot be measured in any city",
   "Dwellings and persons can never appear in the same record",
   "Any two density figures are directly comparable",
   "The framework forbids comparing cities quantitatively"], ans=0,
   why="The suggested skill for this topic is comparing patterns and trends in quantitative data, and a ratio is only as clear as its denominator. Two cities can appear to differ by a factor of two purely because one figure includes non-residential land and the other does not."),

 dict(q="A revision guide must state what this topic's essential knowledge establishes. Which statement is accurate?", choices=[
   "Housing at different densities represents different patterns of land use, and those buildings both record the culture, technology and period that produced them and constrain how the district can be used afterward",
   "Housing density is determined by technology alone",
   "Buildings record the past but have no effect on the present",
   "Residential density has no relationship to land use",
   "Infilling extends a city outward onto new land"], ans=0,
   why="EK IMP-6.A.1 says residential buildings and patterns of land use REFLECT AND SHAPE the city's culture, technological capabilities, cycles of development and infilling. Each rejected summary drops one of the two verbs, reduces the four influences to one, or reverses what infilling means."),
]
