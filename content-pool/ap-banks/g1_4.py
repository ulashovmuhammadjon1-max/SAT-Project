# AP HUMAN GEOGRAPHY 1.4 Spatial Concepts -- 30 questions
# CED Course Framework V.1, Unit 1. Enduring understanding PSO-1; learning
# objective PSO-1.A, "Define major geographic concepts that illustrate spatial
# relationships."
#
# Essential knowledge, in full -- the topic has exactly one statement:
#   PSO-1.A.1  Spatial concepts include absolute and relative location, space,
#              place, flows, distance decay, time-space compression, and pattern.
#
# That is a closed list of eight concepts and it is the whole topic. It supplies
# the NAMES and nothing else: the CED does not define distance decay, does not
# say how place differs from space, and does not state that time-space
# compression is unevenly distributed. So a key here can rest on membership in
# the list (which concept is this?) or on what the concept actually picks out
# (what does distance decay predict?), and the second kind is reasoning rather
# than citation. Items keyed to list membership cite PSO-1.A.1; the rest cite
# nothing, because inventing a code for them would be a fabricated citation.
#
# The distinctions the module is built on, stated once so the keys are auditable:
#   absolute location  position in a fixed global reference frame; it does not
#                      change when the world around a place changes
#   relative location  position described against other places, and therefore
#                      alterable by a new road, a closed border, a new airline
#   space              extent, measured and abstract
#   place              a location with meaning, character and identity attached
#   flows              movement of people, goods, capital, or information
#   distance decay     interaction falls as separation rises
#   time-space compression  travel and communication times collapse while
#                      absolute distances stay exactly what they were
#   pattern            the arrangement of phenomena -- clustered, dispersed,
#                      linear, random
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_4.py. FIVE choices (A-E).
TOPIC = ("1.4", "Spatial Concepts", 1)

QUESTIONS = [
 dict(q="A shipping manifest records a port as 1 degree 17 minutes north, 103 degrees 51 minutes east. Which spatial concept from the framework's list is being used?",
   choices=[
     "Absolute location, because the position is stated in a fixed global reference frame",
     "Relative location, because the port is described by reference to the equator",
     "Place, because the port has a distinctive character",
     "Space, because the port occupies an area of the Earth's surface",
     "Pattern, because ports are arranged along coastlines"],
   ans=0,
   why="PSO-1.A.1 lists absolute and relative location as separate concepts. A latitude-longitude pair fixes a point in a coordinate system that does not depend on any other place, which is what makes it absolute rather than described against something."),

 dict(q="A shop's website says it is 'two blocks east of the cathedral, opposite the tram stop.' This description uses",
   choices=[
     "Relative location, since the shop is fixed by its position with respect to other features",
     "Absolute location, since blocks and stops can be measured precisely",
     "Place, since the cathedral gives the district its identity",
     "Flows, since trams move people past the shop",
     "Distance decay, since customers come from nearby"],
   ans=0,
   why="PSO-1.A.1 pairs relative with absolute location. A description that depends on knowing where the cathedral and the tram stop are is relative by construction, and it would fail entirely for a reader who did not know those landmarks."),

 dict(q="Which statement best captures the difference between space and place as the framework distinguishes them?",
   choices=[
     "Space is measurable extent; place is a location invested with meaning, character, and identity",
     "Space is small and place is large",
     "Space refers to outer space and place refers to Earth",
     "Space is a modern idea and place is a historical one",
     "Space applies to rural areas and place applies to urban ones"],
   ans=0,
   why="PSO-1.A.1 lists space and place as separate spatial concepts. The working distinction geographers draw is between abstract extent, which can be measured and divided, and a particular location made meaningful by what people have done and felt there."),

 dict(q="A tourist board's slogan describes a town as a place 'where the mountains meet the sea and the fishing families still mend their nets on the quay.' The slogan is trading on",
   choices=[
     "A sense of place, built out of the meanings and associations attached to a particular location",
     "Absolute location, since the town's coordinates are unique",
     "Distance decay, since visitors come from a limited catchment",
     "Time-space compression, since the town is now easy to reach",
     "Pattern, since fishing towns line the coast"],
   ans=0,
   why="Place in PSO-1.A.1's sense is location plus meaning, and a slogan of this kind is an attempt to sell exactly that surplus. Nothing in it depends on where the town sits in a coordinate system or on how far its visitors travel."),

 dict(q="A study finds that the number of visitors to a museum falls steadily as the distance from their home to the museum increases. This relationship is",
   choices=[
     "Distance decay, the decline of interaction with increasing separation",
     "Time-space compression, since visitors travel faster than before",
     "Relative location, since the museum is central",
     "A flow reversal, since some visitors return home",
     "Pattern, since museums are located in city centers"],
   ans=0,
   why="PSO-1.A.1 names distance decay. The concept is precisely that interaction between two places weakens as the separation between them grows, because distance imposes costs in money, time and effort that rise with it."),

 dict(q="Between 1850 and today, the fastest travel time from London to Sydney fell from about three months to about a day, while the kilometers between them did not change at all. This is the standard illustration of",
   choices=[
     "Time-space compression, in which relative distance collapses while absolute distance is unchanged",
     "Distance decay, since fewer people made the journey in 1850",
     "Relative location, since Sydney moved closer to London",
     "A change in absolute location produced by improved surveying",
     "Pattern, since air routes form a network"],
   ans=0,
   why="PSO-1.A.1 lists time-space compression. The concept turns on the gap between two measures of separation: kilometers are fixed by geometry, while hours and dollars are set by technology and can fall dramatically without the Earth changing shape."),

 dict(q="Remittances sent home by migrant workers, containerized cargo crossing an ocean, and news spreading through a social network are all examples of which concept from the framework's list?",
   choices=[
     "Flows, the movement of people, goods, capital, or information between places",
     "Patterns, the arrangement of phenomena across an area",
     "Places, locations to which meaning is attached",
     "Absolute locations, since each has a starting point",
     "Distance decay, since each weakens with distance"],
   ans=0,
   why="PSO-1.A.1 lists flows as a spatial concept in its own right. What unites money, cargo and news here is that each is something moving between places rather than something sitting in one, which is the definition of a flow."),

 dict(q="A map of farmsteads in a newly surveyed district shows one dwelling near the center of each square parcel, spread evenly across the whole area. The arrangement is best described as",
   choices=[
     "A dispersed pattern, since the dwellings are spread evenly rather than concentrated",
     "A clustered pattern, since every dwelling sits inside a parcel",
     "A linear pattern, since the parcels form rows",
     "A random pattern, since no dwelling is at a parcel corner",
     "A radial pattern, since roads reach every parcel"],
   ans=0,
   why="PSO-1.A.1 lists pattern among the spatial concepts, and the standard descriptions are clustered, dispersed, linear and random. Even spacing produced by a survey system is the clearest possible case of dispersal, since concentration is exactly what the layout prevents."),

 dict(q="A new bridge opens across a river, cutting the driving time between two towns from ninety minutes to fifteen. Which statement is correct?",
   choices=[
     "Their relative location with respect to each other has changed while their absolute locations have not",
     "Both their absolute and their relative locations have changed",
     "Their absolute locations have changed but their relative locations have not",
     "Neither location has changed, since the towns did not move",
     "Only their sense of place has changed"],
   ans=0,
   why="Absolute location is a coordinate and nothing a bridge does can alter it, while relative location is a statement about position with respect to other places and is exactly what a new connection rewrites. The distinction is the point of listing the two concepts separately."),

 dict(q="Which of the following would most weaken the distance decay effect for a particular good or service?",
   choices=[
     "The good is high in value, rare, and cheap to ship relative to its price",
     "The good is heavy, bulky, and low in value per tonne",
     "The good is perishable within a few hours",
     "Close substitutes for the good are available in every town",
     "Transport costs per kilometer rise sharply"],
   ans=0,
   why="Distance decay is strong when separation imposes a large penalty relative to the value of the interaction. A rare, valuable, easily shipped good makes the transport cost trivial as a share of price and gives buyers a reason to reach far, which flattens the decline."),

 dict(q="A geographer argues that time-space compression has been experienced very unevenly. Which observation supports that argument most directly?",
   choices=[
     "A financial trader reaches counterparties on three continents in milliseconds while a farmer in the same country is a day's walk from a paved road",
     "Air travel has become cheaper in every country",
     "The Earth's circumference has not changed",
     "The internet is used in every country in the world",
     "Shipping containers are a standard size worldwide"],
   ans=0,
   why="The claim is about the distribution of the effect, not its existence, so the evidence has to be a contrast within one setting. A trader and a farmer in the same country inhabit different relative geographies despite sharing an absolute one."),

 dict(q="Which pairing correctly matches a measurement to the kind of distance it expresses?",
   choices=[
     "Forty minutes by train expresses relative distance; forty kilometers expresses absolute distance",
     "Forty minutes by train expresses absolute distance; forty kilometers expresses relative distance",
     "Both expressions state absolute distance, since both are numbers",
     "Both expressions state relative distance, since both depend on the route",
     "Neither expression states a distance, since distance must be measured in a straight line"],
   ans=0,
   why="A duration depends on the mode, the timetable and the congestion of the day, so it describes separation as experienced rather than as measured on the ground. Kilometers are fixed by the geometry of the Earth's surface and do not move with the traffic."),

 dict(q="Migrants leave a rural region for the capital, and each year they send part of their wages home. A geographer describing this as two linked flows would say that",
   choices=[
     "People flow toward the capital while money flows back toward the region of origin",
     "Only the movement of people counts as a flow, since money is not physical",
     "Both flows move in the same direction, toward the capital",
     "Neither is a flow, because the migrants intend to return",
     "The money is a pattern rather than a flow"],
   ans=0,
   why="PSO-1.A.1 includes capital among the things that move between places, so remittances are a flow in the same sense that migration is. The pair runs in opposite directions, which is what makes the relationship between origin and destination a two-way one."),

 dict(q="Settlements in a valley are strung out one after another along a single river and its road. The arrangement is best described as",
   choices=[
     "A linear pattern, because the settlements follow a single axis",
     "A dispersed pattern, because the settlements are separated from one another",
     "A clustered pattern, because every settlement is in the same valley",
     "A random pattern, because the spacing between settlements varies",
     "A radial pattern, because roads run out from each settlement"],
   ans=0,
   why="Pattern in PSO-1.A.1 is a description of arrangement, and an arrangement organized along one axis is linear regardless of how evenly spaced its members are. The river and the road supply the axis and the reason for it."),

 dict(q="Which of the following is the best evidence that a set of towns is CLUSTERED rather than dispersed at the regional scale?",
   choices=[
     "Most of the towns fall within one small part of the region, leaving large areas with none",
     "Every town has approximately the same population",
     "The towns are connected by a well-developed road network",
     "The towns are all more than 20 kilometers apart",
     "The region's total population is large"],
   ans=0,
   why="Clustering is a statement about concentration in part of an area, so the diagnostic evidence is the coexistence of a dense subarea and large empty ones. Equal populations, good roads, wide spacing and a large total are all compatible with either arrangement."),

 dict(q="A resident says that a park 'is not just green space, it is where my parents met and where the neighborhood holds its summer festival.' The distinction she is drawing is between",
   choices=[
     "Undifferentiated space and a place made meaningful by what has happened there",
     "Absolute location and relative location",
     "A flow and a pattern",
     "Distance decay and time-space compression",
     "A local scale and a regional scale"],
   ans=0,
   why="The park's measurable extent is the same either way; what she adds is the accumulated meaning that turns extent into a particular place. That is exactly the space-place distinction PSO-1.A.1's two separate entries point to."),

 dict(q="A telephone company finds that the number of calls between pairs of cities falls sharply with the distance between them, but that the fall is much gentler for calls placed over the internet than for those placed on the old metered network. The best explanation is that",
   choices=[
     "Distance decay weakens when the cost of interaction stops rising with distance",
     "Distance decay does not apply to communication of any kind",
     "The internet abolished absolute distance between the cities",
     "The cities' relative locations changed when the internet arrived",
     "Calls over the internet follow a random pattern"],
   ans=0,
   why="Distance decay reflects the friction that separation imposes, and a metered network makes that friction explicit in the price. Flat-rate transmission removes the cost gradient while leaving other reasons for local interaction intact, so the curve flattens without disappearing."),

 dict(q="Which of the following changes would be an example of time-space compression at the scale of a single metropolitan area?",
   choices=[
     "A new express rail line cuts the trip from an outer suburb to the center from 70 minutes to 25",
     "The metropolitan area annexes an adjacent town",
     "A census reveals the metropolitan population is larger than expected",
     "A new coordinate system is adopted for the city's survey records",
     "The city renames several of its neighborhoods"],
   ans=0,
   why="Time-space compression is a collapse in the time or cost of moving between places without any change in the distance between them, and it can occur at any scale. Annexation, recounting, resurveying and renaming leave travel times exactly where they were."),

 dict(q="An analyst says that a shopping center's trade area is 'bounded by distance decay rather than by a line on a map.' What does she mean?",
   choices=[
     "The probability that a household shops there falls off gradually with distance, so the edge of the trade area is a fading gradient rather than a border",
     "The trade area has no edge and extends to the whole country",
     "The trade area is defined by the municipal boundary",
     "Only households within a fixed radius may shop there",
     "The trade area moves as the shopping center is rebuilt"],
   ans=0,
   why="Distance decay describes a continuous decline rather than a threshold, so patronage thins with distance instead of stopping at a particular ring. That is why trade areas are drawn as probability surfaces and why two centers' trade areas can overlap."),

 dict(q="Two islands are 40 kilometers apart. A ferry runs once a week, takes six hours, and costs a day's wages. A geographer would say that the islands are",
   choices=[
     "Close in absolute distance but far apart in relative terms",
     "Far apart in absolute distance and close in relative terms",
     "Close by both measures, since 40 kilometers is a short distance",
     "Far apart by both measures, since the ferry is slow",
     "Neither close nor far, since distance cannot be compared across measures"],
   ans=0,
   why="Forty kilometers is a small separation in the fixed measure, while a weekly six-hour crossing costing a day's pay is a large one in time, money and effort. Holding the two measures apart is exactly why the framework lists absolute and relative separately."),

 dict(q="Which research question is most directly about FLOWS rather than about pattern?",
   choices=[
     "How many tonnes of wheat move each year from the prairie provinces to Pacific ports",
     "Whether wheat farms are evenly spread across the prairie provinces",
     "Where the boundary of the wheat-growing region lies",
     "How wheat farming gives the prairies their regional identity",
     "What the latitude and longitude of the largest grain elevator are"],
   ans=0,
   why="A flow question asks about movement between places over a period, and tonnes per year moving from one region to another is exactly that. The other four ask about arrangement, extent, meaning and position, which are the other concepts on PSO-1.A.1's list."),

 dict(q="A student claims that because two cities are now four hours apart by high-speed train instead of nine by car, 'they are closer together than they used to be.' The most precise correction is that",
   choices=[
     "They are closer in travel time, which is relative distance, while the kilometers between them are unchanged",
     "They are closer in every sense, since travel time is the only real measure",
     "They are no closer at all, since travel time is not a measure of distance",
     "Their absolute locations have shifted toward each other",
     "The claim cannot be evaluated without knowing the fare"],
   ans=0,
   why="The student's observation is right and the vocabulary is loose: what has fallen is one relative measure of separation. Saying so precisely is what allows time-space compression to be stated as a claim about the gap between the two measures."),

 dict(q="Which statement about absolute location is correct?",
   choices=[
     "A place's coordinates remain the same even as the roads, borders, and cities around it change",
     "A place's coordinates change whenever a new transport link is built",
     "Coordinates can be assigned only to settlements, not to unpopulated points",
     "Coordinates describe how far a place is from the nearest city",
     "Coordinates change when a country adopts a new name for the place"],
   ans=0,
   why="An absolute location is a position in a fixed reference frame, so it is indifferent to everything that happens around the point. That stability is what makes it useful as a common register when every relative description is shifting."),

 dict(q="A geographer maps the origins of everyone who attended a regional hospital and finds patients from far away only for one rare surgical specialty. Which spatial concept explains the contrast between that specialty and routine care?",
   choices=[
     "Distance decay is weaker for a service that few facilities provide, because patients have no nearer alternative",
     "Time-space compression applies only to surgical patients",
     "Rare specialties have a different absolute location from routine care",
     "Routine care produces flows and specialty care does not",
     "Specialty patients form a linear pattern"],
   ans=0,
   why="The steepness of distance decay depends on how easily an interaction can be satisfied nearby. Routine care is available in every town so the curve is steep; a service offered at one site in the region leaves distant patients no substitute, so they travel."),

 dict(q="Which of these best explains why geographers treat 'pattern' as a spatial concept worth naming separately from location?",
   choices=[
     "A set of locations has properties, such as clustering or dispersal, that no single location possesses",
     "Patterns can be measured but locations cannot",
     "Patterns apply only at the global scale",
     "A pattern is simply a list of absolute locations",
     "Locations change over time and patterns do not"],
   ans=0,
   why="Arrangement is a property of a collection rather than of any member of it, so it cannot be read off one coordinate no matter how precise. That is why PSO-1.A.1 lists pattern alongside location instead of treating it as a kind of location."),

 dict(q="Visitor counts at a national park are recorded by the distance band of the visitor's home. Using the table, which conclusion is best supported?",
   table=dict(
     headers=["Distance band (km)", "Visitors per 10,000 residents"],
     rows=[
       ["0-50", "820"],
       ["51-100", "410"],
       ["101-200", "205"],
       ["201-400", "96"],
       ["401-800", "44"]]),
   choices=[
     "Visits per 10,000 residents roughly halve with each step outward, a clear case of distance decay",
     "Visits per 10,000 residents fall by a constant 200 with each step outward",
     "Visits per 10,000 residents are unrelated to distance",
     "Visits per 10,000 residents rise with distance beyond 200 km",
     "The nearest band supplies fewer visits per 10,000 residents than the farthest"],
   ans=0,
   why="Successive ratios are 0.50, 0.50, 0.47 and 0.46, so each band gets roughly half the visitation rate of the one inside it. A constant subtraction would not fit, because the absolute drop shrinks from 410 to 52 as the rate itself falls."),

 dict(q="The table records the fastest scheduled travel time between the same two cities in three different years. Using the table, which statement is correct?",
   table=dict(
     headers=["Year", "Fastest travel time (hours)", "Straight-line distance (km)"],
     rows=[
       ["1900", "60", "1,200"],
       ["1960", "12", "1,200"],
       ["2020", "3", "1,200"]]),
   choices=[
     "Travel time fell to one twentieth of its 1900 value while the distance stayed at 1,200 km, which is time-space compression",
     "Both the travel time and the distance fell by the same proportion",
     "The distance fell while the travel time stayed the same",
     "Travel time fell by a constant number of hours in each period",
     "The cities' absolute locations changed between 1900 and 2020"],
   ans=0,
   why="Sixty hours to three is a reduction to one twentieth, and the distance column is identical in all three rows. The two columns behaving differently is the entire content of the concept: relative separation collapsed and absolute separation did not."),

 dict(q="The table records migration between two regions over one year. Using the table, which statement about the flows is correct?",
   table=dict(
     headers=["Direction", "Migrants"],
     rows=[
       ["Region North to Region South", "48,000"],
       ["Region South to Region North", "31,000"]]),
   choices=[
     "The net flow is 17,000 toward Region South, although substantial movement occurs in both directions",
     "The net flow is 79,000 toward Region South",
     "Movement occurs in one direction only, from Region North to Region South",
     "The net flow is 17,000 toward Region North",
     "The two regions exchanged equal numbers of migrants"],
   ans=0,
   why="Subtracting the smaller stream from the larger gives a net of 17,000 in the direction of the larger one, while adding them would give the gross exchange of 79,000. Both numbers are real and they answer different questions, which is why counterflows matter."),

 dict(q="Four districts of equal area are surveyed for shops. Using the table, which district's shops are most clustered, and on what evidence?",
   table=dict(
     headers=["District", "Shops", "Quadrats with no shop (of 16)"],
     rows=[
       ["District P", "48", "2"],
       ["District Q", "48", "11"],
       ["District R", "48", "5"],
       ["District S", "48", "0"]]),
   choices=[
     "District Q, where 11 of 16 quadrats are empty even though it has the same 48 shops as the others",
     "District S, because every quadrat contains at least one shop",
     "District P, because it has the fewest empty quadrats after District S",
     "District R, because its number of empty quadrats is closest to the average",
     "All four are equally clustered, because each contains 48 shops"],
   ans=0,
   why="Holding the count and the area constant, clustering shows up as empty quadrats: the more of the area that has nothing in it, the more concentrated the shops must be where they do occur. Equal totals are exactly why the empty-quadrat column is the discriminating evidence."),

 dict(q="A central bank records remittances between one country and four partners. Using the table, which partner has the largest net outflow to the recording country?",
   table=dict(
     headers=["Partner", "Sent to recording country (millions)", "Received from recording country (millions)"],
     rows=[
       ["Partner 1", "900", "150"],
       ["Partner 2", "1,200", "700"],
       ["Partner 3", "400", "60"],
       ["Partner 4", "1,500", "1,100"]]),
   choices=[
     "Partner 1, with a net of 750 million",
     "Partner 4, with the largest gross amount sent",
     "Partner 2, with a net of 700 million",
     "Partner 3, with the largest ratio of sent to received",
     "Partner 4, with a net of 750 million"],
   ans=0,
   why="Netting each pair gives 750, 500, 340 and 400 million, so the partner sending the most in gross terms is not the partner with the largest net position. Capital flows in both directions between the same pair of countries, and only the difference measures the transfer."),
]
