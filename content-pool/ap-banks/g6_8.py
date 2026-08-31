# AP HUMAN GEOGRAPHY 6.8 Urban Sustainability -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding IMP-6, "The attitudes
# and values of a population, as well as the balance of power within that
# population, are reflected in the built landscape." Two learning objectives:
#   IMP-6.C  Identify the different urban design initiatives and practices.
#   IMP-6.D  Explain the effects of different urban design initiatives and
#            practices.
#
# Essential knowledge -- one statement each:
#   IMP-6.C.1  Sustainable design initiatives and zoning practices include mixed
#              land use, walkability, transportation-oriented development, and
#              smart-growth policies, including New Urbanism, greenbelts, and
#              slow-growth cities.
#   IMP-6.D.1  Praise for urban design initiatives includes the reduction of
#              sprawl, improved walkability and transportation, improved and
#              diverse housing options, improved livability and promotion of
#              sustainable options. Criticisms include increased housing costs,
#              possible de facto segregation, and the potential loss of
#              historical or place character.
#
# IMP-6.D.1 IS THE MOST EXPLICITLY TWO-SIDED STATEMENT IN THE COURSE. It gives a
# list of praise and then a list of criticisms, in one statement, and it hedges
# the second list twice -- "POSSIBLE de facto segregation" and "POTENTIAL loss of
# historical or place character". A module teaching only the praise would be
# teaching half the statement, and a module asserting the criticisms as
# established outcomes would be overstating the other half. So:
#   - items 10 and 11 take the two lists,
#   - items 12 to 15 take the four kinds of praise,
#   - items 16, 17 and 18 take the three criticisms, each keyed to the MECHANISM
#     by which the criticism arises rather than to a verdict on it,
#   - item 19 keys directly on the fact that the CED supplies both, and item 30's
#     distractors are the two one-sided readings.
# Item 17 is the most carefully written in the module: the CED's phrase is
# "possible de facto segregation", meaning separation that results in practice
# rather than by rule, and the key states the price mechanism that produces it
# without attributing an intention to anyone.
#
# THE SEVEN THINGS IMP-6.C.1 NAMES, with the working descriptions used here
# because the CED defines none of them:
#   mixed land use        homes, shops, workplaces and services in the same
#                         district instead of separated into zones
#   walkability           an environment in which ordinary destinations can be
#                         reached on foot safely and pleasantly
#   transportation-       concentrating housing and jobs around transit stops so
#     oriented development that the service has riders and the residents a service
#   smart growth          directing growth into already-served areas rather than
#                         outward onto new land
#   New Urbanism          designing new districts on traditional-town principles:
#                         streets in a connected grid, mixed uses, short blocks
#   greenbelt             a ring of land around a city on which building is
#                         restricted
#   slow-growth city      a city that deliberately limits the rate at which it
#                         adds housing and population
# Items 2 to 8 take them in turn and item 24 requires them to be told apart.
#
# ZONING IS THE INSTRUMENT and item 9 keys on it: IMP-6.C.1 calls these design
# initiatives AND ZONING PRACTICES, so most of them work by changing what is
# legally permitted on a piece of land rather than by building anything.
#
# SYNONYM CARE. `geo_check` treats {"transportation-oriented development",
# "transit-oriented development"} as one construct, so every item uses the CED's
# own wording and never both forms in one choice list.
#
# NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.8", "Urban Sustainability", 6)

QUESTIONS = [
 dict(q="Which set of sustainable design initiatives and zoning practices does the framework name?", choices=[
   "Mixed land use, walkability, transportation-oriented development, and smart-growth policies including New Urbanism, greenbelts and slow-growth cities",
   "Redlining, blockbusting, and urban renewal",
   "The concentric zone, sector and multiple nuclei models",
   "Site, situation, and infilling",
   "Megacities, metacities, edge cities and boomburbs"], ans=0,
   why="EK IMP-6.C.1 names exactly this set. Redlining and blockbusting are housing discrimination practices in EK SPS-6.A.1, the models belong to EK PSO-6.D.1, and the settlement forms to EK PSO-6.A.4, so each rejected option is drawn from a different statement."),

 dict(q="What is mixed land use?", choices=[
   "Placing homes, shops, workplaces and services in the same district rather than separating them into single-purpose zones",
   "Using the same building material throughout a district",
   "Mixing high-rise and low-rise buildings in a single block",
   "Allowing agriculture within a city boundary",
   "Combining public and private ownership of one building"], ans=0,
   why="EK IMP-6.C.1 names mixed land use among the sustainable design initiatives and zoning practices. Separating uses by zone is what puts every destination beyond walking distance, so mixing them again is the precondition for most of the other initiatives on the list."),

 dict(q="What does walkability describe?", choices=[
   "An environment in which everyday destinations can be reached on foot safely, directly and pleasantly",
   "The total length of footpaths in a city",
   "The number of people who own no car",
   "The average distance residents walk for exercise",
   "A rule requiring residents to walk rather than drive"], ans=0,
   why="EK IMP-6.C.1 names walkability among the sustainable design initiatives. It is a property of the environment rather than of the residents: whether a destination is close, whether the route is safe and whether the walk is worth making are all facts about the place."),

 dict(q="What is transportation-oriented development?", choices=[
   "Concentrating housing, jobs and services around transit stops so that the service has riders and the residents have a service",
   "Building roads before any housing is constructed",
   "Locating housing as far as possible from transport routes",
   "Providing every household with a private vehicle",
   "Designing a city entirely around freight movement"], ans=0,
   why="EK IMP-6.C.1 names transportation-oriented development among the sustainable design initiatives and zoning practices. It works on both sides of the transit problem at once, since a service needs density within walking distance and density needs a service to be worth living at."),

 dict(q="What do smart-growth policies aim to do?", choices=[
   "Direct new development into areas already served by infrastructure rather than outward onto new land",
   "Prevent any new development of any kind",
   "Encourage development to spread as widely as possible",
   "Increase the size of individual house plots",
   "Remove all planning rules from a city"], ans=0,
   why="EK IMP-6.C.1 names smart-growth policies among the sustainable design initiatives and zoning practices. The word 'growth' is in the name: the aim is to direct where growth happens rather than to stop it, which is what distinguishes smart growth from a slow-growth policy."),

 dict(q="What does New Urbanism propose?", choices=[
   "Designing new districts on traditional-town principles -- connected street grids, short blocks, mixed uses and a walkable centre",
   "Building only high-rise towers in new districts",
   "Abolishing streets in favour of pedestrian decks",
   "Designing districts exclusively for car access",
   "Preserving existing districts without any new building"], ans=0,
   why="EK IMP-6.C.1 names New Urbanism among the smart-growth policies. It is a design movement rather than a regulatory one, and its content is a return to the street pattern and mixture of uses that pre-automobile towns had."),

 dict(q="What is a greenbelt?", choices=[
   "A ring of land around a city on which building is restricted, limiting the city's outward expansion",
   "A park at the centre of a city",
   "A strip of trees planted along a motorway",
   "A district reserved for environmentally friendly industry",
   "A route reserved for cyclists across a city"], ans=0,
   why="EK IMP-6.C.1 names greenbelts among the smart-growth policies. The instrument is a restriction on where building may occur rather than a construction project, which is why it belongs among the ZONING practices the statement names."),

 dict(q="What is a slow-growth city?", choices=[
   "A city that deliberately limits the rate at which it adds housing and population",
   "A city whose population happens to be falling",
   "A city with a weak economy",
   "A city that grows only in its central district",
   "A city that has run out of developable land"], ans=0,
   why="EK IMP-6.C.1 names slow-growth cities among the smart-growth policies. The key word is deliberate: a slow-growth city is one whose growth rate is a policy choice, which distinguishes it from a city that is simply not growing."),

 dict(q="Why does the framework describe these initiatives as ZONING PRACTICES as well as design initiatives?", choices=[
   "Most of them work by changing what may legally be built on a piece of land, so the instrument is a rule rather than a building",
   "Because each of them requires a new building to be constructed",
   "Because zoning is the only subject of urban geography",
   "Because they apply only to land already zoned for agriculture",
   "Because they have no legal dimension at all"], ans=0,
   why="EK IMP-6.C.1 calls them sustainable design initiatives AND ZONING PRACTICES. Separated single-use zoning is what produced the pattern these initiatives address, so permitting a shop on a residential street is itself the reform in most cases."),

 dict(q="Which set does the framework list as PRAISE for urban design initiatives?", choices=[
   "Reduction of sprawl, improved walkability and transportation, improved and diverse housing options, and improved livability and promotion of sustainable options",
   "Increased housing costs, de facto segregation, and loss of place character",
   "Redlining, blockbusting, and disamenity zones",
   "Rank-size distributions, primacy, and gravity",
   "Site, situation, and cycles of development"], ans=0,
   why="EK IMP-6.D.1 names exactly this set as praise. The second option is that statement's list of CRITICISMS, and the framework gives both in the same sentence, so telling the two lists apart is the whole of this topic's second half."),

 dict(q="Which set does the framework list as CRITICISMS of urban design initiatives?", choices=[
   "Increased housing costs, possible de facto segregation, and the potential loss of historical or place character",
   "Reduction of sprawl, improved walkability, and improved livability",
   "Suburbanization, sprawl, and decentralization",
   "Threshold, range, and central place hierarchy",
   "Infilling, cycles of development, and technological capabilities"], ans=0,
   why="EK IMP-6.D.1 names exactly these three criticisms and hedges two of them -- POSSIBLE de facto segregation and POTENTIAL loss of character. Those hedges are the framework's own and are part of what the statement asserts."),

 dict(q="How do the framework's design initiatives reduce sprawl?", choices=[
   "By directing new building into already-built and already-served areas and restricting it at the edge, so the same growth occupies less new land",
   "By preventing any new households from forming",
   "By moving existing residents out of the city",
   "By lowering the density of new development",
   "By expanding the area available for building"], ans=0,
   why="EK IMP-6.D.1 names the reduction of sprawl first among the things praised. Sprawl is low-density outward expansion, so the counter-measure is to raise the density of new building and to restrict where it may occur, which is what greenbelts and smart growth do together."),

 dict(q="How do mixed land use and transportation-oriented development improve walkability and transportation together?", choices=[
   "Putting destinations within walking distance makes walking useful, and concentrating people near stops gives a transit service the riders it needs",
   "They improve transport by widening roads for cars",
   "They improve walking by lengthening the distance between destinations",
   "They affect transport but have no bearing on walking",
   "They work only where no transit service exists"], ans=0,
   why="EK IMP-6.D.1 names improved walkability and transportation among the things praised and EK IMP-6.C.1 names both initiatives. The two problems have one solution, since the density that supports a bus route is also the density that puts a shop within a five-minute walk."),

 dict(q="What does the framework mean by praising improved and DIVERSE housing options?", choices=[
   "A district containing several housing types -- apartments, townhouses and detached houses -- can accommodate households at different stages and incomes",
   "That every dwelling in a district should be identical",
   "That housing should be built only for high-income households",
   "That housing should be built only at very low density",
   "That the number of dwellings should be kept fixed"], ans=0,
   why="EK IMP-6.D.1 names improved and diverse housing options among the things praised. A district built to a single housing type serves a single kind of household, so the criticism it answers is that single-use, single-type zoning sorts people by what they can afford."),

 dict(q="What does the framework mean by praising improved LIVABILITY and the promotion of sustainable options?", choices=[
   "Streets that are pleasant to be in, destinations within reach, and travel choices that consume less land and energy",
   "The construction of the tallest possible buildings",
   "The removal of all vegetation from a city",
   "An increase in the average length of commuting trips",
   "The provision of more parking spaces per household"], ans=0,
   why="EK IMP-6.D.1 names improved livability and promotion of sustainable options among the things praised. Livability concerns the daily experience of a place while sustainability concerns its resource consumption, and the same design changes are credited with both."),

 dict(q="By what mechanism can urban design initiatives raise housing costs?", choices=[
   "Restricting where and how much may be built limits supply, and making a district more desirable raises demand for it, so prices rise from both directions",
   "Because building at higher density always costs more per dwelling",
   "Because such initiatives require every house to be rebuilt",
   "Because they increase the number of dwellings available",
   "Because governments set house prices directly"], ans=0,
   why="EK IMP-6.D.1 names increased housing costs among the criticisms. The mechanism is the awkward one: the same measures that make a district worth living in and limit outward expansion act on demand and supply in the directions that both raise price."),

 dict(q="What does the framework's criticism of POSSIBLE DE FACTO SEGREGATION refer to?", choices=[
   "Separation that results in practice rather than by rule, since rising prices in an improved district can put it out of reach of lower-income households",
   "A law requiring different groups to live in different districts",
   "The voluntary clustering of households with shared interests",
   "The physical division of a district by a motorway",
   "The separation of residential from industrial land uses"], ans=0,
   why="EK IMP-6.D.1 names POSSIBLE de facto segregation among the criticisms, and both qualifiers matter. 'De facto' means in fact rather than in law, and 'possible' marks it as an outcome the framework treats as a risk rather than as an established result."),

 dict(q="What does the criticism about POTENTIAL LOSS OF HISTORICAL OR PLACE CHARACTER mean?", choices=[
   "Redevelopment can replace the particular buildings, businesses and uses that made a district distinctive with a pattern that could be anywhere",
   "That new buildings are always physically weaker than old ones",
   "That a district's population must remain unchanged",
   "That historical buildings cannot legally be altered",
   "That new districts have no character of any kind"], ans=0,
   why="EK IMP-6.D.1 names the POTENTIAL loss of historical or place character among the criticisms. What distinguishes one district from another is often accumulated and irreplaceable, so a design applied uniformly can improve a place by its own criteria while removing what made it that place."),

 dict(q="Why does the framework supply both praise and criticisms in the same statement?", choices=[
   "The same measures produce the benefits and the costs, so an honest account of their effects has to include both",
   "Because geographers cannot agree on any of the effects",
   "Because the criticisms have all been shown to be false",
   "Because the praise applies to some cities and the criticisms to others entirely",
   "Because the framework takes no position on urban design"], ans=0,
   why="EK IMP-6.D.1 puts both lists in one statement, and the items on them are connected rather than independent. Making a district more desirable is simultaneously the achievement being praised and the first step in the price rise being criticized."),

 dict(q="Why can a greenbelt raise house prices inside the boundary it draws?", choices=[
   "It fixes the supply of developable land inside the ring while demand for the city continues to grow",
   "It reduces the desirability of the land it encloses",
   "It requires all new houses to be built to a higher standard",
   "It has no effect on the market for land",
   "It increases the amount of land available for housing"], ans=0,
   why="EK IMP-6.C.1 names greenbelts among the smart-growth policies and EK IMP-6.D.1 names increased housing costs among the criticisms. A greenbelt is a restriction on quantity, and where demand keeps rising against a fixed quantity the adjustment has to come through price."),

 dict(q="What is the practical difference between a mixed-use district and one built under single-use zoning?", choices=[
   "In one, homes, shops and workplaces stand on the same street; in the other each is in a separate area, so every trip between them must be made by vehicle",
   "The two are identical in daily practice",
   "Single-use zoning places all activities within walking distance",
   "Mixed use requires all buildings to serve the same purpose",
   "Single-use zoning is used only in dense districts"], ans=0,
   why="EK IMP-6.C.1 names mixed land use among the sustainable design initiatives and zoning practices. Separation of uses is a rule about what may be built where, and its unavoidable consequence is distance between the things a household needs in a day."),

 dict(q="Why does transportation-oriented development require the transit service and the density to be planned together?", choices=[
   "Density without a service gives residents nothing to use, and a service without density has too few riders to justify running frequently",
   "Because transit vehicles cannot operate in dense districts",
   "Because density and transit are unrelated to one another",
   "Because the service must always be built decades after the housing",
   "Because residents will use transit regardless of how frequent it is"], ans=0,
   why="EK IMP-6.C.1 names transportation-oriented development among the sustainable design initiatives. Each half of the arrangement is what makes the other worthwhile, which is why the initiative is defined by the pairing rather than by either element alone."),

 dict(q="At which two scales do the framework's initiatives operate?", choices=[
   "The scale of a single district, where street layout and land uses are designed, and the metropolitan scale, where a greenbelt or growth boundary directs where the whole region may expand",
   "Only the district scale, since design concerns buildings",
   "Only the metropolitan scale, since planning is region-wide",
   "The national scale only, since governments make the rules",
   "No scale, since urban design is not a spatial subject"], ans=0,
   why="EK IMP-6.C.1's list mixes the two: mixed land use, walkability and New Urbanism are district-scale design, while greenbelts and slow-growth policies act on a whole region. An initiative at one scale cannot achieve what one at the other does."),

 dict(q="What evidence would best test the claim that a redevelopment improved walkability?", choices=[
   "The number of everyday destinations within a short walk and the share of local trips actually made on foot, measured before and after",
   "The total population of the city before and after",
   "The number of parking spaces provided in the district",
   "The height of the tallest building in the district",
   "The average income of the district's residents"], ans=0,
   why="EK IMP-6.D.1 names improved walkability among the things praised, and walkability is a property of the environment measured by what it makes possible. Destinations within range measure the opportunity and trips on foot measure the take-up, so the two together test the claim."),

 dict(q="Which pairing of an initiative with the problem it most directly addresses is CORRECT?", choices=[
   "A greenbelt, matched to limiting a city's outward expansion",
   "A greenbelt, matched to increasing the variety of housing types in a district",
   "Mixed land use, matched to limiting a city's outward expansion",
   "New Urbanism, matched to restricting the rate at which a city adds population",
   "A slow-growth policy, matched to putting shops within walking distance of homes"], ans=0,
   why="EK IMP-6.C.1 names seven initiatives that act on different problems at different scales. Only one pairing here matches an initiative to what it actually does; each of the others attaches an initiative to the purpose of a different one on the same list."),

 dict(q="One district is recorded before and after redevelopment on New Urbanist principles. Using the accompanying figures, what changed?",
   table=dict(headers=["Measure", "Before", "After"],
     rows=[["Dwellings per hectare", "18", "47"],
           ["Shops and services within 400 metres", "3", "21"],
           ["Share of local trips on foot or by transit (%)", "14", "46"],
           ["Share of local trips by car (%)", "86", "54"]]),
   choices=[
   "Density and nearby destinations both rose sharply and the share of local trips made on foot or by transit rose from 14 to 46 percent while the car share fell to 54",
   "Density rose but the share of trips by car rose with it",
   "Nearby destinations fell while density rose",
   "The two trip-share rows do not sum to 100 in either period",
   "No change in travel behaviour accompanied the change in density"], ans=0,
   why="Dwellings per hectare rise from 18 to 47 and destinations within 400 metres from 3 to 21, while the two trip shares sum to 100 in both periods and the non-car share rises from 14 to 46 percent. EK IMP-6.D.1 names improved walkability and transportation among the things praised, and this is that claim expressed as measurements."),

 dict(q="House prices in a city with a growth boundary and in a comparable city without one are recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Year", "City with a growth boundary (index, 2000 = 100)", "Comparable city without one (index, 2000 = 100)"],
     rows=[["2000", "100", "100"],
           ["2010", "158", "126"],
           ["2020", "231", "149"]]),
   choices=[
   "Prices rose in both cities but far faster where the boundary applies, reaching an index of 231 against 149 by 2020",
   "Prices rose faster in the city without a boundary",
   "Prices fell in the city with a growth boundary",
   "The two cities' prices rose by identical amounts",
   "The record shows nothing about prices in either city"], ans=0,
   why="Both indices start at 100 and both rise, but the city with a boundary reaches 231 against 149, so its prices rose by 131 points against 49. EK IMP-6.D.1 names increased housing costs among the criticisms of urban design initiatives, and a comparison against a city without the policy is what makes the difference attributable rather than merely observed."),

 dict(q="Two scenarios for accommodating 40,000 new dwellings in one region are recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Scenario", "Land newly built on (hectares)", "New road required (kilometres)", "Infrastructure cost per dwelling (currency units)"],
     rows=[["Low-density expansion", "2,400", "620", "48,000"],
           ["Compact development", "640", "165", "26,000"]]),
   choices=[
   "The compact scenario houses the same 40,000 dwellings on 640 hectares against 2,400, with 165 kilometres of new road against 620 and about 46 percent less cost per dwelling",
   "The compact scenario houses fewer dwellings than the low-density one",
   "The compact scenario requires more new road than the low-density one",
   "Infrastructure cost per dwelling is the same in both scenarios",
   "The low-density scenario consumes less land per dwelling"], ans=0,
   why="Both scenarios house 40,000 dwellings, and the compact one uses 640 hectares against 2,400, 165 kilometres of road against 620, and 26,000 currency units per dwelling against 48,000, a saving of about 46 percent. EK IMP-6.D.1 names the reduction of sprawl among the things praised, and holding the dwelling count constant is what makes the comparison a fair one."),

 dict(q="What limitation should be stated when comparing house prices in a city with a growth boundary against a city without one?", choices=[
   "The two cities may differ in income growth, migration and land supply as well as in the policy, so the comparison narrows the explanation without isolating it",
   "House price indices cannot be constructed for any city",
   "Two indices starting at 100 can never be compared",
   "A difference between two cities always establishes its own cause",
   "The framework forbids the quantitative study of housing costs"], ans=0,
   why="EK IMP-6.D.1 names increased housing costs among the CRITICISMS of urban design initiatives, which is a claim about an effect. A city chosen for comparison is never identical in every other respect, so a difference is consistent with the criticism rather than a demonstration of it."),

 dict(q="A planning committee is told what the framework says about these initiatives. Which account gives it both halves of what the framework records?", choices=[
   "The framework names a set of design and zoning practices intended to make cities more sustainable, and records both the benefits claimed for them and the criticisms made of them",
   "The framework names a set of practices and records only their benefits",
   "The framework names a set of practices and records only the criticisms of them",
   "The framework describes the internal structure of cities using six models",
   "The framework describes how cities are distributed and sized within a country"], ans=0,
   why="EK IMP-6.C.1 supplies the list of initiatives and EK IMP-6.D.1 supplies both the praise and the criticisms in one statement. The two one-sided summaries each drop half of the second statement, and the last two describe EK PSO-6.D.1 and EK PSO-6.C.1 instead."),
]
