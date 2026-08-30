# AP HUMAN GEOGRAPHY 1.2 Geographic Data -- 30 questions
# CED Course Framework V.1, Unit 1. Enduring understanding IMP-1; learning
# objective IMP-1.B, "Identify different methods of geographic data collection."
#
# Essential knowledge this module rests on:
#   IMP-1.B.1  Data may be gathered in the field by organizations or by
#              individuals.
#   IMP-1.B.2  Geospatial technologies include geographic information systems
#              (GIS), satellite navigation systems, remote sensing, and online
#              mapping and visualization.
#   IMP-1.B.3  Spatial information can come from written accounts in the form of
#              field observations, media reports, travel narratives, policy
#              documents, personal interviews, landscape analysis, and
#              photographic interpretation.
#
# Note what IMP-1.B.3 does and does not say, because it is easy to over-read.
# It lists the SOURCES of spatial information; it does not classify them as
# "qualitative" or rank their reliability. Items about the strengths and limits
# of a source are keyed to what that source can and cannot record -- a matter of
# reasoning -- rather than to a framework sentence. Items 1, 2, 5-12 and 21-24,
# which turn on the CED's own lists, cite the EK.
#
# Six items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_2.py. FIVE choices (A-E).
TOPIC = ("1.2", "Geographic Data", 1)

QUESTIONS = [
 dict(q="A university team walks every block of a commercial district and records, on a standard form, whether each storefront is occupied, vacant or under renovation. What kind of data collection is this?",
   choices=[
     "Field observation, since the data are generated on site by the people recording them",
     "Remote sensing, since the team is observing without altering the district",
     "Satellite navigation, since the team must know where each block is",
     "Online mapping, since the results will be published on the web",
     "Photographic interpretation, since the storefronts are being looked at"],
   ans=0,
   why="EK IMP-1.B.1 says data may be gathered in the field, and IMP-1.B.3 lists field observations among the written accounts spatial information comes from. The defining feature is first-hand recording on the ground, not the technology used afterward."),

 dict(q="Which statement correctly distinguishes a satellite navigation system from a geographic information system?",
   choices=[
     "Satellite navigation fixes a position on Earth; a geographic information system stores, layers and analyzes spatial data",
     "Satellite navigation analyzes layers of data; a geographic information system fixes a position",
     "Both fix positions, but only satellite navigation works indoors",
     "Both analyze layers, but only a geographic information system uses satellites",
     "Satellite navigation is a form of remote sensing and a geographic information system is not"],
   ans=0,
   why="EK IMP-1.B.2 lists the two as separate geospatial technologies with separate jobs. A receiver reports where it is; the analytical work of combining, querying and mapping many layers is what a GIS does with data once it exists."),

 dict(q="An agency needs to know how much of a river basin's forest cover was lost between 1990 and 2020 across an area with almost no roads. Which technology is best suited, and why?",
   choices=[
     "Remote sensing, because imagery can measure land cover over inaccessible ground and over past decades",
     "Personal interviews, because residents remember the forest",
     "Satellite navigation, because coordinates can be recorded at each clearing",
     "A policy document review, because logging is regulated",
     "Field observation, because ground truth is always more accurate"],
   ans=0,
   why="Remote sensing acquires data without contact, so roadlessness is no obstacle, and archived imagery lets a present-day analyst measure a past condition that no one thought to survey at the time. That combination is what the other four cannot offer."),

 dict(q="A county wants to site a new health clinic. Analysts combine a layer of population by census block, a layer of existing clinic locations, a layer of bus routes and a layer of parcels zoned for institutional use, then look for parcels that satisfy all four conditions at once. This is an example of",
   choices=[
     "Overlay analysis in a geographic information system",
     "Remote sensing of the built environment",
     "Photographic interpretation of the parcels",
     "A travel narrative of the county",
     "Satellite navigation of the bus fleet"],
   ans=0,
   why="EK IMP-1.B.2 names GIS as a geospatial technology, and stacking independent layers so that a question can be asked of all of them at once is the operation a GIS exists to perform. None of the other tools can relate four different datasets to one another."),

 dict(q="A planner asks a geographic information system to shade every area within 400 meters of a rail station so she can see how much housing is within walking distance. Which capability of the system is she using?",
   choices=[
     "Buffering, which builds a zone of specified distance around a feature",
     "Georeferencing, which assigns coordinates to a scanned map",
     "Remote sensing, which measures the ground from a distance",
     "Interpolation, which estimates values between measured points",
     "Classification, which sorts values into map categories"],
   ans=0,
   why="A distance zone drawn around a point, line or polygon is a buffer, and the reason to draw one is to convert a proximity question into an area that other layers can be intersected with. The other operations do different jobs on the same data."),

 dict(q="After a major earthquake, thousands of volunteers around the world trace collapsed buildings and passable roads from fresh satellite imagery into a free, publicly editable web map that relief agencies then use. Which pair of items from the framework's list of geospatial technologies does this combine?",
   choices=[
     "Remote sensing and online mapping and visualization",
     "Satellite navigation and photographic interpretation",
     "A geographic information system and a policy document",
     "Field observation and a media report",
     "Satellite navigation and a travel narrative"],
   ans=0,
   why="EK IMP-1.B.2's list contains both halves of this workflow: the imagery is remote sensing, and the shared editable map that many contributors build and agencies consult is online mapping and visualization."),

 dict(q="Which is the most important reason a national census is treated as a foundational source of geographic data despite being expensive and slow?",
   choices=[
     "It attempts to count everyone, so results can be reported for very small areas rather than estimated from a sample",
     "It is collected by satellite and so avoids human error",
     "It is repeated every year, so it is always current",
     "It records opinions as well as counts, so it is qualitative",
     "It is produced by private firms and so is independent of government"],
   ans=0,
   why="A complete enumeration supports reporting at fine geographic detail; a sample large enough to do the same everywhere would be nearly as costly. That fine-grained coverage, not currency or objectivity, is what makes a census irreplaceable."),

 dict(q="Census takers in a large city report that recent immigrants, people without fixed addresses, and residents of informal housing are the hardest households to enumerate. What is the geographic consequence for a choropleth map built from those returns?",
   choices=[
     "Neighborhoods with those populations will appear less populous than they are, and any per-capita rate mapped there will be distorted",
     "The map will be unaffected, because undercounts cancel out across a city",
     "The map will overstate population in the affected neighborhoods",
     "Only the total for the city will be wrong; every neighborhood will be correct",
     "The map will be accurate but at too small a cartographic scale to use"],
   ans=0,
   why="Undercounting is spatially concentrated rather than random, so the error attaches to particular tracts. Because the count sits in the denominator of most mapped rates, an undercount inflates every per-capita figure calculated for the same area."),

 dict(q="A geographer studying how nineteenth-century Europeans understood the interior of Africa reads explorers' published journals. Which item from the framework's list of written accounts is she using, and what is its characteristic limitation?",
   choices=[
     "Travel narratives, which record the author's perceptions and purposes as much as the place",
     "Policy documents, which record only what a government intended to do",
     "Media reports, which are written for a mass audience under deadline",
     "Field observations, which capture only what is visible on one day",
     "Personal interviews, which depend on what a respondent chooses to say"],
   ans=0,
   why="EK IMP-1.B.3 lists travel narratives among the sources of spatial information. A journal is evidence of a place and equally of the traveller's frame of reference, which is precisely why it is useful for a study of how outsiders understood a region."),

 dict(q="A researcher wants to know what a national government intended when it redrew its provincial boundaries. Which source from the framework's list speaks most directly to intent?",
   choices=[
     "Policy documents, because they state the reasoning a government put on the record",
     "Remote sensing imagery, because it shows the new boundaries on the ground",
     "A dot distribution map of population, because boundaries follow people",
     "Satellite navigation traces, because they show where officials travelled",
     "A cartogram of provincial budgets, because money follows policy"],
   ans=0,
   why="EK IMP-1.B.3 lists policy documents among the written sources. Intent is a stated thing, and only a document in which the state gives its reasons records it; imagery and coordinates capture outcomes, from which intent can only be guessed."),

 dict(q="A study of why families left a drought-stricken district relies on recorded conversations with sixty households. What does this source provide that a table of out-migration counts cannot?",
   choices=[
     "The reasons people give for moving, which a count of movers never contains",
     "A more precise total number of migrants",
     "The exact destinations of every migrant household",
     "A measurement of the drought's severity",
     "A basis for mapping the district at a large cartographic scale"],
   ans=0,
   why="EK IMP-1.B.3 lists personal interviews among the sources of spatial information. A count establishes that movement happened and how much; only testimony supplies motive, which is what a study of causes needs."),

 dict(q="Reading the built environment of a neighborhood -- the ages and styles of its buildings, its signage, its places of worship, its land uses -- to infer who has lived there and when is which method?",
   choices=[
     "Landscape analysis, since the visible fabric of a place is read as evidence of the people who made it",
     "Remote sensing, since the neighborhood is being observed rather than surveyed",
     "A media report, since the neighborhood's history has been written about",
     "Satellite navigation, since each building has a location",
     "A census, since the question is about who lives there"],
   ans=0,
   why="EK IMP-1.B.3 lists landscape analysis among the written accounts geographers draw on. The landscape is treated as an accumulated record of past occupance, which is exactly the inference the question describes."),

 dict(q="A geographer compares aerial photographs of the same suburban fringe taken in 1955, 1980 and 2015 to date the arrival of subdivisions, a highway and a shopping center. Which method is this, and what makes it powerful here?",
   choices=[
     "Photographic interpretation, because a sequence of images fixes when each change occurred",
     "A personal interview, because the photographs were taken by residents",
     "A policy document review, because zoning decisions caused the changes",
     "Buffer analysis, because the highway has a corridor",
     "A travel narrative, because the photographer moved through the area"],
   ans=0,
   why="EK IMP-1.B.3 lists photographic interpretation. A single image shows a state; a dated series turns those states into a chronology, which is the only way to establish sequence when no one recorded the changes at the time."),

 dict(q="Which research question could NOT be answered by quantitative geographic data alone, and would require one of the framework's written or spoken sources?",
   choices=[
     "Why residents of a gentrifying district describe their neighborhood as no longer theirs",
     "How many housing units were built in the district last year",
     "What share of district households own a car",
     "How the district's median rent compares with the city's",
     "How far the average resident lives from a transit stop"],
   ans=0,
   why="Four of these are counts, shares, comparisons and distances -- all measurable. Meaning and self-understanding are not measurements, and EK IMP-1.B.3's interviews and written accounts exist precisely to supply what a table cannot."),

 dict(q="A national statistics office publishes unemployment only at the province level. A researcher wants to know whether unemployment is concentrated in particular city neighborhoods. What is the problem?",
   choices=[
     "Data reported for large units cannot be disaggregated back to the smaller units inside them",
     "Provinces are not enumeration units, so the data cannot be mapped",
     "Unemployment is qualitative and therefore cannot be mapped at any scale",
     "The data must first be converted to a cartogram before neighborhoods appear",
     "Province-level data is always less accurate than neighborhood-level data"],
   ans=0,
   why="Aggregation destroys internal variation: a single provincial figure is consistent with a smooth distribution and with extreme concentration alike, and nothing in the published number distinguishes them. The remedy is data collected at the finer unit, not arithmetic on the coarser one."),

 dict(q="A hiker's handheld receiver reports her position as 39.7392 degrees north, 104.9903 degrees west. Which kind of information is this, and which technology produced it?",
   choices=[
     "Absolute location, produced by a satellite navigation system",
     "Relative location, produced by a satellite navigation system",
     "Absolute location, produced by remote sensing",
     "Relative location, produced by a geographic information system",
     "Elevation, produced by online mapping and visualization"],
   ans=0,
   why="EK IMP-1.B.2 lists satellite navigation systems among the geospatial technologies, and a latitude-longitude pair is location stated in a fixed global reference frame, which is what makes it absolute rather than described against something else."),

 dict(q="A city uses census figures from 2010 to plan school capacity for 2026 in a district that has been redeveloping rapidly. What is the main weakness of this decision?",
   choices=[
     "The data may no longer describe the population it is being used to plan for",
     "Census data cannot be used for planning of any kind",
     "The data were collected by a government and are therefore biased",
     "The data are at too large a cartographic scale for a school district",
     "The data are qualitative and cannot support a numerical projection"],
   ans=0,
   why="A census is a snapshot, and its usefulness decays as the place changes. In a district that has redeveloped, the households counted may largely have been replaced, so the source is not wrong so much as out of date for this purpose."),

 dict(q="Why do national governments generally use a complete census for apportioning legislative seats but a monthly sample survey for tracking unemployment?",
   choices=[
     "Apportionment needs exact counts for fixed small areas; unemployment needs frequent national estimates, which a sample can deliver cheaply",
     "Samples cannot measure employment, and censuses cannot measure population",
     "A census is more accurate for every purpose but is illegal to run monthly",
     "Unemployment is a qualitative variable and population is a quantitative one",
     "Sample surveys report only at the national scale because they use satellites"],
   ans=0,
   why="The choice of instrument follows the purpose. Legal apportionment requires defensible counts for each district, which only enumeration gives; a labour-market indicator needs timeliness far more than small-area precision, which is what a repeated sample is good at."),

 dict(q="Thousands of cyclists' phone apps upload their routes, and a city uses the aggregated traces to decide where to build bike lanes. Which is the most serious geographic limitation of this data source?",
   choices=[
     "It records the trips of people who already ride and own the app, so demand from people who do not yet ride is invisible",
     "It cannot record location accurately enough to identify a street",
     "It is a form of remote sensing and therefore cannot show movement",
     "It is a policy document and therefore reflects only official intentions",
     "It reports only at the national scale"],
   ans=0,
   why="Volunteered data describes its contributors, not the population. Routes are dense where cycling is already comfortable, so the evidence systematically argues for investment where investment is least needed -- a self-selection problem that better positioning cannot fix."),

 dict(q="An international organization and a village cooperative both map the same set of wells, the first from a regional office and the second by walking to each well. Which framework statement covers both efforts?",
   choices=[
     "That data may be gathered in the field by organizations or by individuals",
     "That geospatial technologies include remote sensing",
     "That all maps are selective in information",
     "That scales of analysis include global, regional, national, and local",
     "That regions are defined on the basis of unifying characteristics"],
   ans=0,
   why="EK IMP-1.B.1 explicitly admits both collectors, organizations and individuals, into the definition of field data. The other four statements are real framework sentences from elsewhere in Unit 1, offered so the item tests which one is on point."),

 dict(q="Cloud cover over an equatorial region during the rainy season prevents an optical satellite from imaging the ground for weeks. This illustrates which general point about geographic data?",
   choices=[
     "Every collection method has conditions under which it fails, so sources are often combined",
     "Remote sensing is less accurate than field observation in all settings",
     "Optical imagery is not a geospatial technology",
     "Equatorial regions cannot be mapped",
     "Cloud cover distorts area the way a projection does"],
   ans=0,
   why="The failure is specific and physical -- optical sensors need a clear line of sight -- not evidence that the method is generally inferior. Recognising the failure conditions of each method is what leads geographers to triangulate across sources."),

 dict(q="A study of a contested urban redevelopment uses council minutes, newspaper coverage, interviews with displaced tenants and a series of aerial photographs. What is the strongest justification for using four sources rather than the single best one?",
   choices=[
     "Each source records something the others cannot, and agreement among them makes a conclusion harder to dismiss",
     "Four sources produce four maps, which is more than one map",
     "Using more sources always increases the cartographic scale of the result",
     "Qualitative sources are unreliable, so several are needed to equal one count",
     "The framework requires that every study use at least four sources"],
   ans=0,
   why="Minutes give official reasoning, press coverage gives contemporaneous public framing, interviews give the experience of those affected, and imagery gives the physical outcome. Their independence is the point: an account they all support is not an artefact of any one of them."),

 dict(q="Which pairing of a research need with a data source is the weakest match?",
   choices=[
     "Measuring how residents feel about a new mosque, using remote sensing imagery",
     "Measuring the growth of irrigated cropland, using satellite imagery",
     "Establishing when a highway interchange was built, using dated aerial photographs",
     "Establishing a government's stated reason for a resettlement, using policy documents",
     "Establishing why one family left a village, using a personal interview"],
   ans=0,
   why="Sensors record reflected energy, so they can show that a building exists and cannot record an attitude toward it. The other four match a source to a question the source is physically or evidentially capable of answering."),

 dict(q="A geographer says that a map produced from a geographic information system 'is only as good as the layers behind it.' What is the substance of that warning?",
   choices=[
     "A polished map inherits every error, omission and out-of-date value in the data it was built from",
     "A geographic information system cannot combine more than a few layers at once",
     "Maps made by software cannot be projected correctly",
     "Layers must all come from the same organization to be combined",
     "A geographic information system cannot display qualitative information"],
   ans=0,
   why="Processing does not improve source data; it only makes the result look authoritative. A misclassified land-cover layer or a stale address file produces a clean, confident and wrong map, and nothing on the page signals it."),

 dict(q="Which of the following is the clearest example of geographic data being gathered by individuals rather than by an organization?",
   choices=[
     "Residents of a flood-prone street logging high-water marks after every storm on a shared spreadsheet",
     "A national weather service operating a network of automated rain gauges",
     "A census bureau conducting a decennial enumeration",
     "A satellite operator distributing imagery to subscribers",
     "A transport ministry publishing traffic counts from roadside sensors"],
   ans=0,
   why="EK IMP-1.B.1 distinguishes the two collectors. Four of these are institutional programmes with staff and instruments; only the street's own residents are individuals generating the record themselves."),

 dict(q="Satellite imagery of a district is classified into land-cover types for three years. Using the table, which conclusion is supported?",
   table=dict(
     headers=["Land cover", "1990 (hectares)", "2005 (hectares)", "2020 (hectares)"],
     rows=[
       ["Forest", "42,000", "33,600", "25,200"],
       ["Cropland", "18,000", "20,000", "19,000"],
       ["Built-up", "4,000", "10,400", "19,800"],
       ["Water", "2,000", "2,000", "2,000"]]),
   choices=[
     "Forest fell by 40 percent over the thirty years while built-up land grew nearly fivefold",
     "Forest and cropland fell by the same proportion between 1990 and 2020",
     "Built-up land grew by 40 percent over the thirty years",
     "Water area fell as built-up land expanded",
     "The district's total mapped area fell by half between 1990 and 2020"],
   ans=0,
   why="Forest goes from 42,000 to 25,200 hectares, a loss of 16,800 or exactly 40 percent, while built-up land goes from 4,000 to 19,800, a factor of 4.95. Cropland barely moves and water does not move at all, so the two large opposite changes are the story the imagery tells."),

 dict(q="A census bureau publishes an independent estimate of how badly each group was undercounted. Using the table, which group's published count most understates its true size in percentage terms?",
   table=dict(
     headers=["Group", "Published count", "Estimated true count"],
     rows=[
       ["Group W", "1,960,000", "2,000,000"],
       ["Group X", "570,000", "600,000"],
       ["Group Y", "294,000", "300,000"],
       ["Group Z", "1,455,000", "1,500,000"]]),
   choices=[
     "Group X, whose published count falls 5 percent short of the estimated true count",
     "Group W, whose published count falls 40,000 short and so is the worst affected",
     "Group Y, because its counts are the smallest in the table",
     "Group Z, whose published count falls 3 percent short of the estimated true count",
     "All four groups are understated by the same percentage"],
   ans=0,
   why="Shortfalls of 40,000, 30,000, 6,000 and 45,000 rank quite differently once divided by the true counts: 2, 5, 2 and 3 percent. The largest absolute gap belongs to the largest group, which is why an undercount has to be judged as a rate."),

 dict(q="A mail survey on housing conditions returns the results below. In which district should the published estimate be treated with the most caution, and why?",
   table=dict(
     headers=["District", "Surveys mailed", "Surveys returned"],
     rows=[
       ["Ashcroft", "2,000", "1,240"],
       ["Brambly", "1,500", "300"],
       ["Colworth", "800", "520"],
       ["Dunhaven", "2,500", "1,750"]]),
   choices=[
     "Brambly, where only 20 percent of surveys came back, so the respondents may differ systematically from the district",
     "Dunhaven, where the most surveys were mailed and so the most were lost",
     "Colworth, where the fewest surveys were mailed",
     "Ashcroft, where 62 percent came back, the lowest rate in the table",
     "All four are equally reliable, since each returned several hundred surveys"],
   ans=0,
   why="Response rates are 62, 20, 65 and 70 percent, so Brambly is far below the rest. A low rate matters because the households that answer are not a random subset of those that do not, and 300 returns cannot repair that bias by being numerous."),

 dict(q="Four sites are evaluated in a geographic information system against three requirements for a new clinic. Using the table, which site does the overlay identify?",
   table=dict(
     headers=["Site", "Within 400 m of a bus stop", "Zoned institutional", "Outside the 100-year floodplain"],
     rows=[
       ["Site 1", "Yes", "Yes", "No"],
       ["Site 2", "Yes", "No", "Yes"],
       ["Site 3", "Yes", "Yes", "Yes"],
       ["Site 4", "No", "Yes", "Yes"]]),
   choices=[
     "Site 3, the only site that satisfies all three requirements at once",
     "Site 1, because transit access and zoning outrank flood risk",
     "Site 2, because it is the only site outside the floodplain",
     "Site 4, because two of three requirements is the best available",
     "No site qualifies, because no site satisfies more than two requirements"],
   ans=0,
   why="An overlay keeps only the area where every layer's condition holds. Three of the four sites fail exactly one requirement each, which is what makes the surviving site unique rather than merely best on points."),

 dict(q="Four data sources describing the same city are compared below. Which source is best suited to a study of how the city's built-up area expanded between 1985 and 2020?",
   table=dict(
     headers=["Source", "Earliest year available", "Latest year available", "Reporting unit"],
     rows=[
       ["Satellite imagery archive", "1984", "2023", "30-metre pixel"],
       ["Municipal building permits", "2004", "2023", "Individual parcel"],
       ["National census", "1991", "2021", "Census tract"],
       ["Resident interviews", "n/a", "2023", "Individual account"]]),
   choices=[
     "The satellite imagery archive, the only source whose record begins before 1985 and resolves changes below the tract",
     "The municipal building permits, because a parcel is the finest reporting unit in the table",
     "The national census, because it is the only official source covering the whole period",
     "The resident interviews, because residents observed the expansion directly",
     "None of them, because no source in the table covers 1985"],
   ans=0,
   why="Only two candidates reach back before 1985 -- imagery from 1984 and nothing else, since the census begins in 1991 and permits in 2004 -- and of those the imagery alone resolves change at 30 metres rather than at the tract. Coverage in time and resolution in space both have to be satisfied, and only one source does both."),
]
