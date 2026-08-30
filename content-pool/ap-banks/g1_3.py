# AP HUMAN GEOGRAPHY 1.3 The Power of Geographic Data -- 30 questions
# CED Course Framework V.1, Unit 1. Enduring understanding IMP-1; learning
# objective IMP-1.C, "Explain the geographical effects of decisions made using
# geographical information."
#
# Essential knowledge, in full -- the topic has exactly one statement:
#   IMP-1.C.1  Geospatial and geographical data, including census data and
#              satellite imagery, are used at all scales for personal, business
#              and organizational, and governmental decision-making purposes.
#
# Read that sentence carefully, because it fixes what this topic is about and
# what it is not. It names two exemplar data sources (census data, satellite
# imagery), it asserts the range of scales ("at all scales"), and it lists three
# classes of decision maker: personal, business and organizational, and
# governmental. The learning objective adds the part the exam actually tests --
# the geographical EFFECTS of those decisions, meaning what changes on the
# ground once a decision has been made from the data.
#
# So every item here is built on one of three moves:
#   (a) classify the decision maker (items 1-4, 13, 17, 20, 25),
#   (b) trace the geographic consequence of a decision made from data
#       (items 5-12, 14-16, 18, 19, 21-24), and
#   (c) read a real data table the way a decision maker would (26-30).
# Items whose key is a matter of course content cite IMP-1.C.1; items whose key
# is a matter of reasoning about consequences cite nothing, because inventing an
# EK code for them would be a fabricated citation.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_3.py. FIVE choices (A-E).
TOPIC = ("1.3", "The Power of Geographic Data", 1)

QUESTIONS = [
 dict(q="A driver opens a navigation app before leaving home, sees that the usual highway is congested, and takes a different route. Under the framework's classification of who uses geographic data, this is a decision at which level?",
   choices=[
     "Personal, since an individual is using the data to make a choice about her own movement",
     "Governmental, since the highway is publicly built and maintained",
     "Business, since a private company supplies the application",
     "Organizational, since traffic data are aggregated from many users",
     "Governmental, since traffic laws determine which routes are legal"],
   ans=0,
   why="EK IMP-1.C.1 names personal decision making as one of the three classes of use. Who owns the data or the road does not determine the class; the class is fixed by whose decision the data is informing, and here it is the individual driver's."),

 dict(q="A supermarket chain compares census figures on household size and income with the locations of its competitors before choosing between two possible store sites. This is best described as",
   choices=[
     "A business decision made with census data, one of the uses the framework names explicitly",
     "A governmental decision, because census data are collected by a government",
     "A personal decision, because a manager makes the final call",
     "A decision that census data cannot support, because a census does not record shopping",
     "An organizational decision that could equally have been made without any spatial data"],
   ans=0,
   why="EK IMP-1.C.1 lists census data among the geographic data used for business decision making. The collector of a dataset and the user of it are different things, and site selection is a commercial judgement about where customers are."),

 dict(q="A relief agency working in a country with no reliable address system uses recent satellite imagery to count shelters in a rapidly growing displacement camp and to plan where water points should go. Which of the framework's classes of use does this illustrate?",
   choices=[
     "Organizational decision making using satellite imagery",
     "Personal decision making using satellite imagery",
     "Business decision making using census data",
     "Governmental decision making using a national census",
     "A use outside the framework's three classes"],
   ans=0,
   why="EK IMP-1.C.1 pairs satellite imagery with organizational decision making and asserts that such data are used at all scales. An agency is neither an individual nor a state, and no census exists for a camp that formed in weeks."),

 dict(q="A national government uses census counts to decide how many seats each region receives in the legislature. What makes this a particularly consequential use of geographic data?",
   choices=[
     "The count is converted directly into political representation, so an error in the data becomes an error in who governs",
     "The count is expensive, so an error wastes public money",
     "The count is published, so an error damages the statistical office's reputation",
     "The count is spatial, so an error produces a distorted map",
     "The count is decennial, so an error is corrected within a year"],
   ans=0,
   why="Apportionment is a rule that mechanically transforms population figures into seats, so the data are not advisory but determinative. That direct conversion is why census accuracy is contested politically rather than only technically."),

 dict(q="In the mid-twentieth century, lenders in some countries used maps that graded neighborhoods by perceived lending risk, with the lowest grades assigned largely on the basis of the residents' race or ethnicity. Loans were then refused in the lowest-graded areas. What is the geographic effect this illustrates?",
   choices=[
     "A map made from biased categories directed investment away from particular neighborhoods and so helped produce the decline it claimed to predict",
     "A map made from biased categories had no effect, because lending decisions are made loan by loan",
     "The map improved lending accuracy, since the graded areas did decline",
     "The map's effect was limited to the year in which it was drawn",
     "The map affected only the lenders who drew it, not the neighborhoods themselves"],
   ans=0,
   why="A decision rule applied through a map redistributes real resources across space, and withheld credit degrades housing stock over decades. The apparent confirmation is circular: the map's own consequences became the evidence offered for its accuracy."),

 dict(q="A national funding formula distributes money to local governments in proportion to their census populations. A city with a substantial undercount will",
   choices=[
     "Receive less funding than its actual population warrants for as long as the flawed count governs the formula",
     "Receive extra funding, because undercounted places are compensated automatically",
     "Be unaffected, because funding formulas use estimates rather than the census",
     "Lose funding only in the year the census is taken",
     "Receive the same funding, because formulas are set by negotiation rather than by data"],
   ans=0,
   why="Where a formula takes population as its input, an undercount propagates directly into the allocation and persists until the next count replaces it. The effect is geographic because undercount is concentrated in particular kinds of places rather than spread evenly."),

 dict(q="A police department directs extra patrols to the areas where past arrest records are densest. Officers in those areas then make more arrests, which are added to the dataset. What is the geographic problem with this arrangement?",
   choices=[
     "The data record where police have looked as much as where offenses occur, so the system reinforces its own initial pattern",
     "The data are too coarse to identify individual streets",
     "The data cannot be mapped because arrests are points rather than areas",
     "The data are collected by a government and are therefore unusable for planning",
     "The data would be valid only if collected by satellite"],
   ans=0,
   why="Arrest counts are a record of enforcement activity, not an independent measure of offending, so deploying on them creates a feedback loop in which attention manufactures the evidence for more attention. The pattern becomes self-confirming regardless of the underlying distribution."),

 dict(q="An insurer redraws its flood-risk zones using new elevation data and raises premiums sharply inside the revised high-risk zone. Which set of geographic effects is most likely?",
   choices=[
     "Property values and new construction inside the zone fall relative to just outside it, and the boundary itself becomes economically visible",
     "Property values change uniformly across the whole city, since insurance is a citywide market",
     "Nothing changes on the ground, because a risk zone is only a line on a map",
     "Construction increases inside the zone, because insured properties are safer",
     "The zone boundary disappears, because insurers do not publish their maps"],
   ans=0,
   why="A line that changes the cost of holding property in one place and not the next creates a discontinuity in price and in building decisions across it. The map does not merely describe the landscape; it becomes one of the forces shaping it."),

 dict(q="Two days after a hurricane, an emergency management agency compares imagery taken before and after the storm to decide where to send search teams first. What does the imagery provide that ground reports could not at that moment?",
   choices=[
     "A consistent view of the whole affected area at once, including places no one can currently reach",
     "The names of the residents who need help",
     "A legally binding assessment of damage for insurance purposes",
     "A record of what the buildings were worth before the storm",
     "A measure of how frightened residents were"],
   ans=0,
   why="Immediately after a disaster the roads and communications that ground reporting depends on are the very things that have failed, so coverage is patchy exactly where damage is worst. Imagery is uniform over the whole scene and does not require access."),

 dict(q="A grain farmer uses a yield map from last season's harvest, combined with soil sampling, to apply more fertilizer to the low-yielding corners of a field and less to the rest. This is an example of",
   choices=[
     "Geospatial data changing a decision at the sub-field scale, where the same field is treated as several different places",
     "Geospatial data being used only for record keeping rather than for decisions",
     "A decision that could not be made without a national census",
     "A governmental decision, because agriculture is regulated",
     "A decision made at the global scale, because commodity prices are global"],
   ans=0,
   why="EK IMP-1.C.1 asserts that geospatial data are used at all scales, and the finest of them is within a single holding. Treating one field as an internally varied surface rather than as a uniform unit is exactly what the yield map makes possible."),

 dict(q="A public health office maps confirmed cases of a waterborne illness and finds them tightly clustered around one section of the distribution network. What is the most defensible decision to make from this map?",
   choices=[
     "Test and, if necessary, isolate that section of the network, because the spatial clustering points to a shared source",
     "Conclude that residents of that section are less hygienic than others",
     "Close the entire city's water system until every case is resolved",
     "Ignore the pattern, because disease maps show only where people were tested",
     "Rebuild the distribution network across the whole city immediately"],
   ans=0,
   why="A cluster tight around one piece of shared infrastructure is evidence about that infrastructure, and testing it is both the cheapest and the most direct response. The blaming and the citywide responses go far beyond what the spatial pattern supports."),

 dict(q="A county selects a landfill site by combining layers for land cost, distance to housing, and soil suitability. The site chosen turns out to be adjacent to the county's poorest and least politically organized community. What does this case illustrate about decisions made with geographic data?",
   choices=[
     "The criteria written into an analysis carry values, and cheap land is not a neutral variable when land is cheap where poor people live",
     "Geographic information systems remove human judgement from siting decisions",
     "The result proves the analysis was performed incorrectly",
     "Soil suitability is the only criterion that should ever be used",
     "The outcome would have been identical under any set of criteria"],
   ans=0,
   why="An analysis returns what its criteria ask for, and land price is correlated with the wealth and political weight of nearby residents. The apparent objectivity of the output conceals the choice of inputs, which is where the distributional consequence was decided."),

 dict(q="Fine-grained data on residents' party registration, street by street, allow a legislature to draw district boundaries that produce a durable majority for one party. This shows that",
   choices=[
     "Better spatial data can make a political manipulation more precise rather than less possible",
     "Better spatial data always make district boundaries fairer",
     "District boundaries cannot be drawn without such data",
     "Party registration is not geographic information",
     "The effect would be identical if the data were available only at the state level"],
   ans=0,
   why="Precision is a capability, not a value: the same resolution that allows a fair line to be verified allows an unfair one to be optimized. Coarse data limits how finely a boundary can be tuned, which is why resolution and manipulability rise together here."),

 dict(q="A phone application records its users' locations continuously and sells the aggregated traces to advertisers. Which concern is specifically geographic rather than general to any personal data?",
   choices=[
     "A person's home, workplace, place of worship, and clinic visits can be inferred from where the device sits and when",
     "The company may be hacked and lose the records",
     "Users may not have read the terms of service",
     "The data may be stored on servers in another country",
     "Advertising may be annoying to users"],
   ans=0,
   why="A location trace is not just an identifier but a record of participation in particular places, and the sensitive facts follow from the places themselves. The other concerns attach equally to any dataset regardless of whether it has coordinates."),

 dict(q="A power utility maps outage frequency by circuit and prioritizes rebuilding on the circuits with the longest cumulative outage times. Which criticism of this decision rule is strongest?",
   choices=[
     "Outages are recorded only where customers report them, so under-reporting neighborhoods will appear reliable and stay last in line",
     "Circuits are lines and therefore cannot be mapped",
     "Cumulative outage time is a quantitative measure and quantitative measures cannot guide decisions",
     "The utility should use a national census instead of its own records",
     "Prioritizing by need is never appropriate for infrastructure"],
   ans=0,
   why="The dataset measures reported outages rather than experienced ones, so a systematic difference in reporting becomes a systematic difference in investment. That is the same reporting bias that makes crime and complaint data hazardous as an allocation rule."),

 dict(q="A national ministry uses province-level poverty rates to decide where to build clinics, and places one clinic in the geographic center of each of the poorest provinces. What is the likely geographic effect?",
   choices=[
     "Clinics may end up far from the actual concentrations of poor households inside each province, because the data were too coarse for the decision",
     "Clinics will automatically be placed where the poorest households live, because the provinces were correctly chosen",
     "The decision cannot be evaluated, since poverty is not a spatial variable",
     "Every household in each province will be equally well served, since the center is equidistant from all points",
     "The clinics will be unused, since poverty rates do not predict health need"],
   ans=0,
   why="Choosing the right province and choosing the right site within it are different questions, and a provincial average says nothing about the internal distribution. The mismatch between the scale of the data and the scale of the decision is where the error enters."),

 dict(q="Which of the following is the clearest example of geographic data being used for a personal decision rather than an organizational one?",
   choices=[
     "A family comparing school catchment maps and commute times before deciding which neighborhood to rent in",
     "A charity allocating food aid among districts using malnutrition surveys",
     "A ministry deciding where to widen a highway using traffic counts",
     "A bank deciding which branches to close using account-holder addresses",
     "A hospital network deciding where to open a clinic using patient origin data"],
   ans=0,
   why="EK IMP-1.C.1 separates personal from business, organizational and governmental use. Four of these decisions are made by institutions on behalf of populations; only the household is choosing for itself."),

 dict(q="An informal settlement of 40,000 people does not appear on the municipal base map, so it is not included in the layers used for planning water and refuse services. What is the geographic effect of that omission?",
   choices=[
     "The settlement is passed over in service planning, and its absence from the data is mistaken for an absence of need",
     "The settlement receives extra services, because unmapped areas are surveyed first",
     "The omission affects the map's appearance but not any allocation of services",
     "The omission will be corrected automatically by satellite imagery",
     "The settlement's residents will be counted twice in the census instead"],
   ans=0,
   why="A decision process that reads its world from a dataset can only act on what the dataset contains, so an unmapped population is invisible to every step that follows. Being left off the map is therefore a material harm rather than a cartographic detail."),

 dict(q="A delivery company reroutes its vans each morning using live road-speed data and the day's order addresses. Which statement best captures why this is a geographic decision and not merely a logistical one?",
   choices=[
     "The cost of the route depends on the arrangement of the stops in space and on conditions that vary from place to place",
     "The vans are physical objects and physical objects occupy space",
     "The company employs drivers who live in different places",
     "Delivery is regulated differently in different countries",
     "The orders were placed using devices that report their location"],
   ans=0,
   why="What makes the problem geographic is that the objective function is built out of distances, adjacencies and locally varying travel times. The other statements are true of the company but do not make the routing decision itself spatial."),

 dict(q="A coastal city publishes an evacuation-zone map built from storm-surge modeling and elevation data. Beyond guiding evacuations, what is a likely secondary geographic effect of publishing it?",
   choices=[
     "Property markets, insurers, and developers begin treating the zone boundary as a real line, changing what gets built where",
     "The map has no effect outside emergencies, because it is only used during storms",
     "Elevation inside the zone will gradually rise as sediment accumulates",
     "The city will be legally prevented from ever revising the boundary",
     "Residents outside the zone will evacuate first"],
   ans=0,
   why="Once an authoritative line is published, actors with money at stake incorporate it into decisions that outlast any single storm. The map's influence on ordinary land and credit markets is a larger long-run effect than its use during the few days of an emergency."),

 dict(q="A government uses satellite imagery to identify cultivated parcels that lack formal title, then issues titles to the occupants. Which pair of effects is most plausible?",
   choices=[
     "Occupants gain security and access to credit, while households whose fields the imagery misread or missed are left more vulnerable than before",
     "Every occupant gains title, since imagery records all cultivation without error",
     "No occupant gains anything, since imagery cannot show who farms a parcel",
     "Only the government benefits, since titling produces tax records and nothing else",
     "Titles are issued to the owners of the satellites"],
   ans=0,
   why="A titling programme converts a data product into a durable legal right, so both the accuracy and the omissions of the imagery become permanent. Formalization is rarely uniformly good or bad; it redistributes security toward those the data captured correctly."),

 dict(q="A retail analyst maps the drive-time catchment of each existing store and finds that a proposed new store's catchment would overlap two of them by more than half. The most likely business conclusion is that",
   choices=[
     "The new store would mostly draw customers away from the company's own stores rather than add sales",
     "The new store should be built because overlap indicates strong demand",
     "The existing stores should close because the catchments overlap",
     "Catchment overlap has no bearing on a siting decision",
     "The overlap proves the drive-time data were computed incorrectly"],
   ans=0,
   why="Overlapping catchments mean the same households are being served twice by one firm, so the added revenue is largely transferred rather than new. Recognising cannibalization is precisely what the spatial analysis is for."),

 dict(q="Which statement best expresses the framework's point that geographic data are used at all scales?",
   choices=[
     "The same kinds of data inform an individual choosing a route, a firm choosing a site, and a state allocating seats",
     "Geographic data are only meaningful at the national scale, where censuses are conducted",
     "Geographic data are only meaningful at the local scale, where they are collected",
     "Global data are always more reliable than local data",
     "A dataset can be used at exactly one scale"],
   ans=0,
   why="EK IMP-1.C.1 states the range explicitly by naming personal, business and organizational, and governmental users in a single sentence about all scales. The distinguishing feature is the decision being made, not a scale at which the data become valid."),

 dict(q="A city releases a public dataset of reported crimes at the individual address level. Which is the most serious foreseeable consequence of that decision?",
   choices=[
     "Victims may be identifiable from address and offense type, and property values on named streets may fall on the basis of a handful of reports",
     "The dataset will be too large for the public to download",
     "Crime will increase because offenders will read the data",
     "The city will lose the ability to map crime internally",
     "The data will become inaccurate as soon as they are published"],
   ans=0,
   why="Publishing at the finest spatial unit both erodes the anonymity that aggregation provides and lets a small number of incidents stigmatize a specific block. Both harms follow from the resolution of the release rather than from the decision to be transparent."),

 dict(q="A ministry of education, a private tutoring company, and a parent all consult the same published map of school performance. What does this show about geographic data?",
   choices=[
     "One dataset can serve governmental, business, and personal decisions at once, and each user pursues a different end with it",
     "A dataset serves whichever user first obtained it and no other",
     "Only the ministry's use counts as a decision, since it made the data",
     "The parent's use is not a decision, since no money changes hands",
     "The company's use invalidates the ministry's use"],
   ans=0,
   why="EK IMP-1.C.1 lists the three classes of user side by side, and nothing in the data restricts it to one of them. The ministry may reallocate teachers, the firm may site a branch, and the parent may choose a house, all from the same map."),

 dict(q="A chain uses the figures below to choose one of four sites for a store aimed at large households. Using the table, which site does the analysis identify, and on what grounds?",
   table=dict(
     headers=["Site", "Households within 3 km", "Average household size", "Nearest competitor (km)"],
     rows=[
       ["Site 1", "9,000", "2.1", "1.0"],
       ["Site 2", "6,000", "4.0", "5.0"],
       ["Site 3", "11,000", "2.0", "0.5"],
       ["Site 4", "5,000", "3.0", "4.0"]]),
   choices=[
     "Site 2, which serves 24,000 people within 3 km and whose nearest competitor is the most distant in the table",
     "Site 3, because it counts the most households within 3 km",
     "Site 1, because it counts the second most households within 3 km",
     "Site 4, because its average household size is above the median for the table",
     "Site 3, because a competitor half a kilometer away indicates a proven market"],
   ans=0,
   why="Multiplying households by average household size gives populations of 18,900, 24,000, 22,000 and 15,000, so the site with the most households is not the site serving the most people. The largest served population also happens to be the furthest from a competitor, which is why the two criteria agree here."),

 dict(q="A county must decide which parcels to place inside a new mandatory flood-insurance zone, defined as land below 4 metres of elevation. Using the table, how many of the listed parcels fall inside the zone, and what does that imply for the county?",
   table=dict(
     headers=["Parcel", "Elevation (m)", "Assessed value (thousands)", "Households"],
     rows=[
       ["Parcel A", "2.5", "180", "12"],
       ["Parcel B", "6.0", "240", "9"],
       ["Parcel C", "3.2", "150", "20"],
       ["Parcel D", "4.5", "300", "7"],
       ["Parcel E", "1.8", "220", "15"]]),
   choices=[
     "Three parcels, holding 47 of the 63 households listed, so most of the affected residents live on the lowest ground",
     "Two parcels, holding 27 households, since only the two lowest parcels qualify",
     "Four parcels, holding 54 households, since only the highest parcel is excluded",
     "Three parcels, holding the three highest assessed values in the table",
     "One parcel, since a threshold rule can apply to only one parcel at a time"],
   ans=0,
   why="Parcels at 2.5, 3.2 and 1.8 metres sit below the four-metre threshold and together hold 12, 20 and 15 households, which is 47 of the 63 in the table. A rule stated in metres has its real bite in the number of households it reaches."),

 dict(q="A national grant programme pays local governments a fixed amount per resident counted. Using the table, which city loses the most grant money to its undercount?",
   table=dict(
     headers=["City", "Counted population", "Estimated true population", "Grant per resident"],
     rows=[
       ["Ashvale", "200,000", "215,000", "$20"],
       ["Brightmoor", "150,000", "162,000", "$40"],
       ["Calder", "400,000", "408,000", "$30"],
       ["Dunmore", "90,000", "99,000", "$45"]]),
   choices=[
     "Brightmoor, which forgoes $480,000",
     "Ashvale, which forgoes $300,000 despite the largest missed count in the table",
     "Calder, which forgoes the most because it is by far the largest city listed",
     "Dunmore, which forgoes the most because its undercount rate is the highest listed",
     "All four forgo the same amount, since every city is paid at a per-resident rate"],
   ans=0,
   why="The loss is the missed count times that city's rate: 15,000 at $20 is $300,000, 12,000 at $40 is $480,000, 8,000 at $30 is $240,000 and 9,000 at $45 is $405,000. The largest missed count, the highest undercount rate and the largest population all belong to different cities, and none of them is the answer."),

 dict(q="A regional authority will fund broadband construction in the district with the greatest number of unserved households. Using the table, which district should be funded?",
   table=dict(
     headers=["District", "Households", "Share with broadband access"],
     rows=[
       ["District J", "40,000", "90%"],
       ["District K", "12,000", "55%"],
       ["District L", "25,000", "60%"],
       ["District M", "8,000", "30%"]]),
   choices=[
     "District L, with 10,000 unserved households",
     "District M, with the lowest share of households connected",
     "District J, with the largest number of households",
     "District K, with 5,400 unserved households",
     "District M, with 5,600 unserved households"],
   ans=0,
   why="Unserved counts are 4,000, 5,400, 10,000 and 5,600, so the district with the worst connection rate is not the district with the most unserved households. Which measure the rule names decides where the money goes."),

 dict(q="A farmer will apply extra fertilizer to any management zone whose yield fell more than 15 percent below the field average. Using the table, which zones receive the extra application?",
   table=dict(
     headers=["Zone", "Area (hectares)", "Yield (tonnes per hectare)"],
     rows=[
       ["Zone 1", "10", "9.0"],
       ["Zone 2", "10", "5.6"],
       ["Zone 3", "10", "8.4"],
       ["Zone 4", "10", "5.0"]]),
   choices=[
     "Zones 2 and 4, the only zones under the 5.95 tonne cutoff that 15 percent below the 7.0 field average sets",
     "Zone 4 only, since it alone records the lowest yield anywhere in the field",
     "Zones 2, 3, and 4, since each of the three yields less than the best zone does",
     "All four zones, since no single zone reaches the highest yield recorded here",
     "No zone at all, because the threshold is measured against the highest yield rather than the mean"],
   ans=0,
   why="The four equal-area zones average exactly 7.0 tonnes per hectare, so the cutoff is 5.95, and yields of 5.6 and 5.0 fall under it while 8.4 and 9.0 sit well above the mean. Two zones qualify, not the single worst zone and not every zone below average."),
]
