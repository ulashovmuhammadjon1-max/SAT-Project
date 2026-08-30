# AP HUMAN GEOGRAPHY 2.2 Consequences of Population Distribution -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding PSO-2; learning
# objective PSO-2.D, "Explain how population distribution and density affect
# society and the environment."
#
# Essential knowledge, in full -- the topic has exactly two statements:
#   PSO-2.D.1  Population distribution and density affect political, economic,
#              and social processes, including the provision of services such as
#              medical care.
#   PSO-2.D.2  Population distribution and density affect the environment and
#              natural resources; this is known as carrying capacity.
#
# PSO-2.D.1 names three domains -- political, economic, social -- and singles
# out ONE example, the provision of services such as medical care. The module
# treats those three domains as the classification axis (which kind of
# consequence is this?) and the service-provision example as the case the CED
# has explicitly authorized, which is why items 3, 6, 11, 17 and 26 are built on
# it.
#
# PSO-2.D.2 attaches the term CARRYING CAPACITY to the environmental
# consequence, and the definition the module holds itself to is the one the
# sentence implies: the population an area's resources can support at a given
# level of consumption and technology. Two corollaries follow and several items
# turn on them -- carrying capacity is not a fixed number, since technology and
# consumption per person move it, and exceeding it does not simply stop growth,
# it degrades the resource base so that future capacity is LOWER.
#
# Two things this topic is NOT, kept out on purpose: it is not Malthus (2.6
# owns that), and it is not the density METHODS (2.1 owns those). Density is
# used here as an input to a consequence, never as a calculation to be named.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_2.py. FIVE choices (A-E).
TOPIC = ("2.2", "Consequences of Population Distribution", 2)

QUESTIONS = [
 dict(q="Why does it cost far more per household to deliver piped water in a sparsely settled rural district than in a dense city neighborhood?",
   choices=[
     "The same length of pipe serves far fewer households, so the fixed cost of the network is divided among fewer payers",
     "Rural water is inherently more expensive to treat",
     "Rural households use much more water than urban ones",
     "Cities receive subsidies that rural districts do not",
     "Pipe is more expensive to buy in rural areas"],
   ans=0,
   why="EK PSO-2.D.1 states that distribution and density affect economic and social processes including service provision. Network infrastructure has a cost proportional to distance and a benefit proportional to the households connected, so low density raises the cost per connection directly."),

 dict(q="A country's constitution guarantees each province a minimum number of legislative seats regardless of population. What is the geographic consequence?",
   choices=[
     "Voters in sparsely populated provinces have more representation per person than voters in dense ones",
     "Every voter has exactly equal influence, since seats are guaranteed",
     "Dense provinces gain influence, since they have more people",
     "Representation becomes independent of geography altogether",
     "The rule has no effect unless provinces differ in area"],
   ans=0,
   why="EK PSO-2.D.1 names political processes among those affected by population distribution. A floor on seats decouples representation from population, so the same seat is bought with fewer voters where population is thin."),

 dict(q="A rural region has one hospital serving an area in which the average resident lives 90 minutes away. Which consequence is most directly predicted by the framework?",
   choices=[
     "Medical care is provided less accessibly because the population is too dispersed to support facilities close to everyone",
     "The region's residents are healthier because they live in the countryside",
     "Population density has no bearing on where hospitals are built",
     "The hospital will relocate to the geographic center of the region",
     "Residents will use the hospital more often than urban residents do"],
   ans=0,
   why="EK PSO-2.D.1 singles out the provision of services such as medical care as the example of a process affected by distribution and density. A facility needs a threshold population to sustain it, so dispersal forces long travel times whatever the site chosen."),

 dict(q="Carrying capacity, as the framework uses the term, is best defined as",
   choices=[
     "The population an area's resources can support at a given level of consumption and technology",
     "The total number of people who could physically stand in an area",
     "The maximum population a government will permit",
     "The population an area held at its historical peak",
     "The number of people an area's arable land could feed regardless of technology"],
   ans=0,
   why="EK PSO-2.D.2 attaches carrying capacity to the effect of population distribution and density on the environment and natural resources. The concept is a relationship between people, resources, and how much each person consumes, not a fixed physical count."),

 dict(q="Which observation would best show that a pastoral region has exceeded its carrying capacity?",
   choices=[
     "Herd sizes have risen while grass cover, soil depth, and per-animal yields have all declined year after year",
     "The region's population has grown for a decade",
     "The region imports some of its food",
     "The region has more livestock than its neighbors",
     "The region's rainfall varies from year to year"],
   ans=0,
   why="Exceeding carrying capacity is diagnosed by degradation of the resource base rather than by the size of the population alone. Rising demand alongside falling productivity per unit is the signature that the stock supporting the system is being consumed."),

 dict(q="A sparsely populated district cannot keep a full-time pediatrician in practice. Which explanation fits the framework's account of service provision?",
   choices=[
     "The district's population is below the threshold needed to generate enough demand to support the specialty",
     "Pediatricians prefer cities for cultural reasons alone",
     "The district's residents have no children",
     "Rural populations are healthier and need no specialists",
     "The government forbids specialists from practising outside cities"],
   ans=0,
   why="EK PSO-2.D.1 names service provision as a process shaped by distribution and density. A specialized service needs a minimum number of users within reach to be viable, and thin population puts that number out of reach without changing anyone's need."),

 dict(q="A rapidly growing city draws its water from an aquifer that is being pumped faster than it recharges. Which framework concept is most directly involved?",
   choices=[
     "Carrying capacity, since the concentration of population is drawing down the natural resource that sustains it",
     "The demographic transition, since the city is growing",
     "Physiological density, since water is not arable land",
     "Distance decay, since water is piped from a distance",
     "Political representation, since the city is governed"],
   ans=0,
   why="EK PSO-2.D.2 states that population distribution and density affect the environment and natural resources, and names that relationship carrying capacity. Withdrawal exceeding recharge is the resource being consumed rather than used, which is the definition in operation."),

 dict(q="Which statement about carrying capacity is correct?",
   choices=[
     "It can be raised by technology that increases output per unit of resource and lowered by rising consumption per person",
     "It is a fixed number determined by an area's size",
     "It applies only to non-human populations",
     "It is the same for every region of comparable area",
     "It cannot be exceeded, by definition"],
   ans=0,
   why="EK PSO-2.D.2 ties carrying capacity to the resources an area supplies, and how far those resources go depends on the technology applied to them and the consumption of each person. Both terms move, which is why the same land supports different numbers at different times."),

 dict(q="A dense urban district and a dispersed rural district have the same total population. Which pair of consequences is most likely?",
   choices=[
     "The urban district delivers services more cheaply per person; the rural district exerts less pressure per unit of area on local land",
     "Both districts face identical service costs and identical environmental pressure",
     "The rural district delivers services more cheaply per person",
     "The urban district exerts less environmental pressure per unit of area",
     "Neither density nor distribution affects services or environment"],
   ans=0,
   why="EK PSO-2.D.1 and PSO-2.D.2 make both consequences follow from the same arrangement. Concentration shortens the networks that services run on while intensifying demand on the immediate area, and dispersal does the opposite on both counts."),

 dict(q="A national government proposes closing small rural schools and busing students to larger consolidated ones. Which trade-off does population distribution create here?",
   choices=[
     "Cost per student falls with consolidation, but travel time rises and the school stops being a local institution",
     "Both cost and travel time fall with consolidation",
     "Both cost and travel time rise with consolidation",
     "Consolidation has no effect on cost, only on travel",
     "Population distribution is irrelevant to school siting"],
   ans=0,
   why="EK PSO-2.D.1 covers the social and economic processes shaped by distribution, and a threshold service in a thin population forces exactly this choice. Fixed costs per school fall when pupils are pooled, and the price is paid in distance."),

 dict(q="Which is the clearest example of population distribution affecting a POLITICAL process?",
   choices=[
     "Electoral districts must be redrawn after a census because population has shifted between regions",
     "A city's water main bursts during a cold spell",
     "A rural clinic closes for lack of patients",
     "A forest is cleared for cropland",
     "A supermarket opens in a growing suburb"],
   ans=0,
   why="EK PSO-2.D.1 names political processes explicitly. Redistricting exists precisely because representation is tied to population and population moves, so the map of power has to be redrawn when the map of people changes."),

 dict(q="A coastal strip holds most of a country's population, and it is also the country's most productive fishery and its main wetland. Which consequence follows most directly?",
   choices=[
     "Competition between settlement and the ecosystems that occupy the same narrow zone, so pressure on those resources is far higher than a national average would suggest",
     "The wetland will expand as population grows",
     "Fish stocks will be unaffected, since fishing is offshore",
     "The country's carrying capacity is set by its interior",
     "Population concentration reduces pressure on coastal resources"],
   ans=0,
   why="EK PSO-2.D.2 ties environmental pressure to where people are, not merely to how many there are. When the concentration of people coincides spatially with the resource, the local pressure is far above what a country-wide figure would imply."),

 dict(q="Which of these best explains why a national average of environmental pressure can be misleading?",
   choices=[
     "Pressure is exerted where people actually are, so a country with an empty interior can still be straining the resources of the strip that is settled",
     "National averages are always calculated incorrectly",
     "Environmental pressure cannot be measured at any scale",
     "Only global figures are meaningful for the environment",
     "Averages overstate pressure in every case"],
   ans=0,
   why="EK PSO-2.D.2 makes distribution as well as density the driver of environmental consequence. An average spreads demand evenly across territory that the population does not occupy evenly, which understates the load exactly where it falls."),

 dict(q="A city of eight million must build a new landfill, a new water treatment plant, and a new power station within twenty years. Which framework statement covers this?",
   choices=[
     "That population distribution and density affect the environment and natural resources",
     "That population distribution affects only political processes",
     "That carrying capacity applies only to agricultural societies",
     "That density has no effect on infrastructure",
     "That environmental effects arise only from rural populations"],
   ans=0,
   why="EK PSO-2.D.2 states the relationship directly, and the three facilities are the physical form it takes: concentrated population generates concentrated waste, water demand and energy demand that the surrounding environment has to absorb or supply."),

 dict(q="A district's population falls by a third over twenty years. Which consequence is most likely for its public services?",
   choices=[
     "Per-user costs rise because the fixed costs of existing networks and buildings are shared among fewer people",
     "Per-user costs fall proportionally with the population",
     "Service quality automatically improves because there are fewer users",
     "Services are unaffected, since infrastructure is already built",
     "The district will receive additional infrastructure to compensate"],
   ans=0,
   why="EK PSO-2.D.1 makes provision of services depend on distribution and density. A pipe network, a school building and a bus route cost nearly the same to maintain whether they are used heavily or lightly, so depopulation raises the cost each remaining user must cover."),

 dict(q="Which action would RAISE a region's carrying capacity, as the framework uses the term?",
   choices=[
     "Introducing irrigation and higher-yielding crops that increase food produced per hectare",
     "Increasing average meat consumption per person",
     "Increasing the region's population",
     "Redrawing the region's boundaries to include more desert",
     "Recording the population more accurately"],
   ans=0,
   why="EK PSO-2.D.2's carrying capacity is a relation between resources, technology and consumption. Raising output per unit of land increases the number of people the same area can support, while raising consumption per person lowers it and counting people changes neither term."),

 dict(q="Two provinces have equal populations. Province A is one dense metropolitan area; Province B is a hundred scattered villages. Which service is relatively HARDER to provide in Province A?",
   choices=[
     "Affordable housing, because demand is concentrated on a small and expensive land supply",
     "Public transit, because riders are close together",
     "Piped sewerage, because households are adjacent",
     "Emergency response, because distances are short",
     "Primary schooling, because children are numerous in each catchment"],
   ans=0,
   why="EK PSO-2.D.1 makes distribution shape economic and social processes in both directions. Concentration makes network services cheap and land-consuming goods expensive, because everyone is bidding for the same limited central area."),

 dict(q="A geographer argues that carrying capacity is 'a moving target rather than a ceiling.' Which evidence best supports that claim?",
   choices=[
     "The same land supported far fewer people before mechanized farming and supports more now, while a richer diet would reverse the gain",
     "The world's population has grown continuously",
     "Some regions have more resources than others",
     "Population density can be measured in three different ways",
     "Governments set population targets"],
   ans=0,
   why="EK PSO-2.D.2 defines the environmental limit in terms of the resources an area supplies, and both the yield obtained from those resources and the amount each person takes are variable. Evidence that the same land has supported different numbers under different technologies makes the point directly."),

 dict(q="Which is the strongest reason a very dispersed population can be as environmentally consequential as a concentrated one?",
   choices=[
     "Dispersal spreads roads, clearing, and infrastructure over a far larger area, fragmenting habitat that a compact settlement would leave intact",
     "Dispersed populations always consume more per person",
     "Dispersed populations are always larger",
     "Concentrated populations have no environmental effect",
     "Dispersal has no measurable environmental consequence"],
   ans=0,
   why="EK PSO-2.D.2 names distribution as well as density as the driver of environmental effect. Compact settlement concentrates its damage into a small footprint, while the same number of people spread thinly requires far more road, line and clearing per person."),

 dict(q="A country's population is concentrated in one metropolitan region containing the capital, the main port, and the largest universities. Which political consequence is most likely?",
   choices=[
     "National decisions tend to reflect the interests of that region, and other regions perceive themselves as peripheral",
     "The concentration guarantees that all regions receive equal attention",
     "Political power will move to the least populated region",
     "Concentration removes the need for a national government",
     "Political processes are unaffected by where population is concentrated"],
   ans=0,
   why="EK PSO-2.D.1 lists political processes among those distribution affects. Where population, government and economy coincide, votes, media, expertise and lobbying are all concentrated in the same place, and the sense of being peripheral elsewhere is the standard result."),

 dict(q="Which of these is the best example of a SOCIAL consequence of population distribution, as distinct from a political or economic one?",
   choices=[
     "Young people leaving thinly populated districts because there are too few peers, services, and opportunities to stay for",
     "A district losing a legislative seat after a census",
     "A supermarket chain closing an unprofitable rural branch",
     "A tax rate rising to fund a rural road",
     "A national election being held on a single day"],
   ans=0,
   why="EK PSO-2.D.1 names political, economic and social processes as three separate domains. Losing a seat is political and a closed branch or a tax rate is economic, whereas the thinning of the social world a young person can participate in is the social case."),

 dict(q="An island's population has grown while its fresh water, soil, and fisheries have all deteriorated. Which conclusion is best supported?",
   choices=[
     "The island appears to be at or beyond its carrying capacity at current consumption and technology",
     "The island's population must be reduced to zero for the resources to recover",
     "Carrying capacity does not apply to islands",
     "The deterioration must have a cause unrelated to population",
     "The island's carrying capacity has risen"],
   ans=0,
   why="EK PSO-2.D.2 names carrying capacity as the concept covering the effect of population on environment and resources. Simultaneous deterioration of several independent resource systems as population rises is the pattern the concept describes, stated with the qualifier the definition requires."),

 dict(q="Why does the framework mention 'the provision of services such as medical care' specifically when discussing density?",
   choices=[
     "Because a service with a high threshold population makes the effect of density on access unusually visible",
     "Because medical care is the only service affected by density",
     "Because medical care is provided only in cities",
     "Because density has no effect on other services",
     "Because medical care is a political rather than a social process"],
   ans=0,
   why="EK PSO-2.D.1 offers medical care as an example rather than an exhaustive claim, and it is a good example because hospitals and specialties need large catchments. Where the threshold is high, thin population converts directly into distance and delay."),

 dict(q="A city expands outward at very low density, adding roads, sewers, and power lines across former farmland. Which pair of consequences does the framework predict?",
   choices=[
     "Higher per-household infrastructure cost and greater conversion of productive land",
     "Lower per-household infrastructure cost and less land conversion",
     "Lower per-household cost but greater land conversion",
     "Higher per-household cost but less land conversion",
     "Neither cost nor land use is affected by the density of expansion"],
   ans=0,
   why="EK PSO-2.D.1 and PSO-2.D.2 are both engaged: spreading a given number of households over more ground lengthens every network serving them and takes more land out of its previous use. The two consequences move together because they have the same cause."),

 dict(q="Which of the following would most reduce the environmental pressure a given population exerts, without changing the number of people?",
   choices=[
     "Falling consumption of resources per person and more efficient technology",
     "Spreading the same population over a larger area",
     "Concentrating the same population into a smaller area",
     "Recalculating the population's density by a different method",
     "Redrawing the region's administrative boundaries"],
   ans=0,
   why="EK PSO-2.D.2 makes the environmental effect a function of the population and the resources it draws on, and the draw per person is the term that is not the headcount. Rearranging people or recomputing a statistic changes where the pressure falls or how it is described, not its total."),

 dict(q="A health ministry compares the cost of running a clinic in four districts. Using the table, which district has the highest cost per resident served, and why?",
   table=dict(
     headers=["District", "Residents served", "Annual clinic cost (thousand $)"],
     rows=[
       ["District 1", "40,000", "1,200"],
       ["District 2", "6,000", "900"],
       ["District 3", "25,000", "1,000"],
       ["District 4", "12,000", "720"]]),
   choices=[
     "District 2, at $150 per resident, because a clinic's fixed costs are spread over the fewest people",
     "District 1, at $30 per resident, because it has the largest total cost",
     "District 3, at $40 per resident, because it serves a middling population",
     "District 4, at $60 per resident, because its total cost is lowest",
     "All four are equal, since each district has one clinic"],
   ans=0,
   why="Dividing cost by residents gives $30, $150, $40 and $60 per person, so the district with the largest budget is the cheapest per head and the district with the smallest population is the dearest. A facility's cost does not fall in proportion to the population it serves."),

 dict(q="Four grazing districts are assessed against their estimated carrying capacities. Using the table, which district is most severely overstocked in proportional terms?",
   table=dict(
     headers=["District", "Estimated carrying capacity (animals)", "Current herd (animals)"],
     rows=[
       ["District A", "20,000", "23,000"],
       ["District B", "4,000", "7,000"],
       ["District C", "50,000", "58,000"],
       ["District D", "9,000", "9,000"]]),
   choices=[
     "District B, whose herd is 75 percent above its estimated capacity",
     "District C, whose herd exceeds capacity by the largest number of animals",
     "District A, whose herd exceeds capacity by 15 percent",
     "District D, whose herd exactly equals its capacity",
     "None, because carrying capacity cannot be estimated"],
   ans=0,
   why="Overshoot as a share of capacity is 15, 75, 16 and 0 percent, so the district exceeding capacity by the most animals is not the one under the greatest proportional strain. A small resource base is overwhelmed by a much smaller absolute excess."),

 dict(q="A regional authority reports the length of water main needed to reach the households in four settlements. Using the table, which settlement is cheapest to serve per household?",
   table=dict(
     headers=["Settlement", "Households", "Water main required (km)"],
     rows=[
       ["Settlement W", "5,000", "25"],
       ["Settlement X", "800", "40"],
       ["Settlement Y", "2,000", "20"],
       ["Settlement Z", "300", "30"]]),
   choices=[
     "Settlement W, needing 5 metres of main per household",
     "Settlement Y, needing 10 metres of main per household",
     "Settlement X, needing the most main of any settlement in total",
     "Settlement Z, needing the fewest households to be connected",
     "Settlement X, needing 50 metres of main per household"],
   ans=0,
   why="Dividing metres of main by households gives 5, 50, 10 and 100 metres each, so the settlement requiring the least pipe in total is not the cheapest to serve. Density, not total network length, determines what each connection costs."),

 dict(q="Legislative seats and populations are shown for four provinces. Using the table, which province's voters are best represented per person?",
   table=dict(
     headers=["Province", "Population (thousands)", "Seats"],
     rows=[
       ["Province I", "3,600", "12"],
       ["Province II", "450", "3"],
       ["Province III", "1,200", "6"],
       ["Province IV", "2,400", "6"]]),
   choices=[
     "Province II, with one seat for every 150,000 people",
     "Province I, with the most seats in the table",
     "Province IV, with one seat for every 400,000 people",
     "Province III, with one seat for every 200,000 people",
     "All four are equally represented, since each has seats"],
   ans=0,
   why="People per seat are 300,000, 150,000, 200,000 and 400,000, so the province with the fewest people needs the fewest of them to elect a member. Holding a large number of seats is not the same as being well represented per voter."),

 dict(q="Water withdrawals and renewable supply are shown for four basins with different settlement patterns. Using the table, which basin is drawing most heavily on its renewable supply relative to what is available?",
   table=dict(
     headers=["Basin", "Population (thousands)", "Renewable supply (million m3/yr)", "Withdrawal (million m3/yr)"],
     rows=[
       ["Basin K", "900", "600", "300"],
       ["Basin L", "150", "80", "72"],
       ["Basin M", "2,400", "1,500", "1,050"],
       ["Basin N", "400", "500", "150"]]),
   choices=[
     "Basin L, which withdraws 90 percent of its renewable supply",
     "Basin M, which withdraws the largest volume of water",
     "Basin K, which withdraws 50 percent of its renewable supply",
     "Basin N, which has the smallest renewable supply",
     "Basin M, which has the largest population"],
   ans=0,
   why="Withdrawal as a share of renewable supply is 50, 90, 70 and 30 percent, so the basin taking the most water in volume is not the basin closest to its limit. Basin N does not have the smallest supply either, which the table shows directly."),
]
