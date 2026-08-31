# AP HUMAN GEOGRAPHY 5.2 Settlement Patterns and Survey Methods -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding PSO-5, "Availability
# of resources and cultural practices influence agricultural practices and
# land-use patterns." Learning objective PSO-5.B, "Identify different rural
# settlement patterns and methods of surveying rural settlements."
#
# Essential knowledge -- three statements:
#   PSO-5.B.1  Specific agricultural practices shape different rural land-use
#              patterns.
#   PSO-5.B.2  Rural settlement patterns are classified as clustered, dispersed,
#              or linear.
#   PSO-5.B.3  Rural survey methods include metes and bounds, township and
#              range, and long lot.
#
# TWO SEPARATE CLASSIFICATIONS, and keeping them apart is most of the work.
# A SETTLEMENT PATTERN describes where the DWELLINGS are relative to one
# another. A SURVEY METHOD describes how the LAND was divided into parcels.
# They are related but not the same question, and an item that confuses them is
# the commonest way this topic is got wrong. Items 1, 2, 16, 24 and 30 keep the
# two lists explicitly distinct.
#
# WHAT THE CED DOES NOT DEFINE: any of the six terms. The definitions used
# throughout, and repeated in the claims, are the standard ones:
#   clustered          dwellings grouped together, with the fields worked from
#                      the group and lying around it
#   dispersed          each farmstead stands separately on the land it works
#   linear             dwellings strung along a line -- a road, a river, a
#                      levee, a canal
#   metes and bounds   boundaries described by natural features, directions and
#                      distances, producing irregular parcels
#   township and range a rectangular grid laid out from surveyed base lines and
#                      meridians, producing square parcels
#   long lot           narrow parcels running back from a river or road, so that
#                      every holding has frontage on it
#
# THE ONE ARITHMETIC FACT this module uses is the geometry of the township and
# range grid: a section is one square mile, which is 640 acres, so a quarter
# section is 160 acres and a quarter of a quarter is 40. That is a property of
# the survey system itself, not a claim about any country's land law, and item 28
# recomputes it from its own table rather than asserting it.
#
# PSO-5.B.1 IS THE CAUSAL STATEMENT and it is easy to skip past. Practices shape
# patterns: a system needing many hands at once on the same water source pulls
# dwellings together, while a system in which each household works a large block
# of land alone pushes them apart. Items 12, 13, 14, 15, 21 and 25 run that
# argument in both directions, because the exam asks it both ways.
#
# NO REAL PLACE IS NAMED. The CED names none in these three statements, survey
# systems are attached to particular national histories that are easy to get
# subtly wrong, and describing a landscape tests the same reading.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.2", "Settlement Patterns and Survey Methods", 5)

QUESTIONS = [
 dict(q="Into which three categories does the framework classify rural settlement patterns?", choices=[
   "Clustered, dispersed, and linear",
   "Metes and bounds, township and range, and long lot",
   "Intensive, extensive, and subsistence",
   "Primary, secondary, and tertiary",
   "Formal, functional, and perceptual"], ans=0,
   why="EK PSO-5.B.2 names exactly clustered, dispersed and linear. The three survey methods are a separate list in EK PSO-5.B.3 and answer a different question, namely how the land was divided rather than where the houses stand."),

 dict(q="Which three rural SURVEY methods does the framework name?", choices=[
   "Metes and bounds, township and range, and long lot",
   "Clustered, dispersed, and linear",
   "Contour, transect, and quadrat",
   "Concentric, sector, and multiple nuclei",
   "Arithmetic, physiological, and agricultural"], ans=0,
   why="EK PSO-5.B.3 names exactly these three. A survey method is a way of dividing land into parcels, which is a different classification from EK PSO-5.B.2's account of where dwellings stand relative to one another."),

 dict(q="In one district almost every farmhouse stands in a single village, with the fields worked out from it in every direction. Which settlement pattern is this?", choices=[
   "Clustered, since the dwellings are grouped and the fields surround the group",
   "Dispersed, since the fields are spread out",
   "Linear, since the roads leave the village",
   "Long lot, since fields extend outward",
   "Township and range, since the fields are divided"], ans=0,
   why="EK PSO-5.B.2 classifies settlement patterns as clustered, dispersed or linear, and the clustered case is defined by dwellings grouped together with their land around them. Long lot and township and range are survey methods rather than settlement patterns."),

 dict(q="In another district each farmhouse stands alone in the middle of the land it works, more than a kilometre from its nearest neighbour. Which settlement pattern is this?", choices=[
   "Dispersed, since each dwelling sits separately on its own holding",
   "Clustered, since each farm is a unit",
   "Linear, since the farms are connected by a road",
   "Metes and bounds, since the holdings are separate",
   "Long lot, since each holding is large"], ans=0,
   why="EK PSO-5.B.2 names dispersed among its three settlement patterns, and the defining feature is that dwellings stand apart on the land each one works. Metes and bounds and long lot describe how parcels were laid out, not where houses were built."),

 dict(q="Along one bank of a river, farmhouses stand in a nearly continuous ribbon a few hundred metres apart, each with its land running back from the water. Which settlement pattern is this?", choices=[
   "Linear, since the dwellings follow the line of the river",
   "Clustered, since the dwellings are close together",
   "Dispersed, since each dwelling has its own land",
   "Township and range, since the land is divided regularly",
   "Metes and bounds, since the river is a boundary"], ans=0,
   why="EK PSO-5.B.2 names linear among its three settlement patterns. The dwellings are close together, but they are strung out along a line rather than gathered around a centre, which is what separates the linear case from the clustered one."),

 dict(q="A deed describes a boundary as running 'from the great oak north-east 140 paces to the stone wall, thence along the wall to the creek'. Which survey method produced this parcel?", choices=[
   "Metes and bounds, which fixes boundaries by natural features, directions, and distances",
   "Township and range, which lays out a rectangular grid",
   "Long lot, which gives every holding river frontage",
   "A clustered settlement pattern",
   "A dispersed settlement pattern"], ans=0,
   why="EK PSO-5.B.3 names metes and bounds among the rural survey methods. Describing a boundary by the features it passes is the defining method, and it is why parcels laid out this way have irregular shapes that follow the ground."),

 dict(q="A region's farmland is divided into squares one mile on a side, its roads meet at right angles a mile apart, and parcels are described by their position in a numbered grid. Which survey method is this?", choices=[
   "Township and range, a rectangular survey laid out from base lines and meridians",
   "Metes and bounds, since parcels are described precisely",
   "Long lot, since parcels are regular",
   "A linear settlement pattern",
   "A clustered settlement pattern"], ans=0,
   why="EK PSO-5.B.3 names township and range among the rural survey methods. A grid surveyed from fixed reference lines produces square parcels and a road network on the same right angles, which is why the pattern is visible from the air."),

 dict(q="Parcels along a waterway are each about 200 metres wide and four kilometres deep, running back from the water in parallel strips. Which survey method is this?", choices=[
   "Long lot, which gives each holding a share of the frontage",
   "Township and range, which produces square parcels",
   "Metes and bounds, which produces irregular parcels",
   "A dispersed settlement pattern",
   "A clustered settlement pattern"], ans=0,
   why="EK PSO-5.B.3 names long lot among the rural survey methods. Narrow strips running back from a waterway exist so that every holding touches the water, which in a pre-road landscape is the transport route, the water supply and the best soil at once."),

 dict(q="Why were long lots laid out narrow and deep rather than as compact blocks?", choices=[
   "So that every holding would touch the river or road that supplied transport, water, and the best land",
   "Because narrow parcels are easier to plough than wide ones",
   "Because the surveyors could not measure long distances",
   "To ensure every holding had exactly the same soil type throughout",
   "Because narrow parcels prevent settlement altogether"], ans=0,
   why="EK PSO-5.B.3 names long lot among the survey methods, and the shape is a solution to a distribution problem. Frontage on the waterway is the scarce and valuable thing, so dividing it into many narrow shares gives every holding access to it."),

 dict(q="Why does a township and range survey tend to be associated with a DISPERSED settlement pattern?", choices=[
   "Each household received a compact block of land and built on its own block, which places dwellings apart by construction",
   "Because the grid forbids villages by law",
   "Because square parcels cannot be farmed from a village",
   "Because the grid is always laid out in mountainous country",
   "Because the survey assigns each household several scattered strips"], ans=0,
   why="EK PSO-5.B.1 says specific agricultural practices shape different rural land-use patterns, and the way land is handed out is part of that. When a household's land arrives as one square block, the shortest distance to all of it is the middle of the block, so that is where the house goes."),

 dict(q="Why do metes and bounds parcels typically look irregular on a map?", choices=[
   "Their boundaries follow features on the ground -- streams, ridges, walls, trees -- and the ground is not rectangular",
   "Because surveyors using the method worked without instruments of any kind",
   "Because the method requires every parcel to be a different size",
   "Because the method was used only on steep slopes",
   "Because the method divides land by population rather than by area"], ans=0,
   why="EK PSO-5.B.3 names metes and bounds among the survey methods, and the irregularity follows from what the method uses as references. A boundary defined by a creek takes the shape of the creek, which is exactly what a rectangular survey avoids."),

 dict(q="A farming system requires many households to flood, plant and harvest the same fields within a few days of one another, using one shared water source. What settlement pattern would you expect, and why?", choices=[
   "Clustered, because a practice needing many hands and one water source at the same moment pulls dwellings together",
   "Dispersed, because water is available everywhere",
   "Linear, because water always runs in a line",
   "Dispersed, because shared work requires privacy",
   "No particular pattern, since practice does not affect settlement"], ans=0,
   why="EK PSO-5.B.1 states that specific agricultural practices shape different rural land-use patterns. Where the work is simultaneous and the water is common, living apart imposes a daily cost on every household, and living together removes it."),

 dict(q="Cattle are grazed on holdings of several thousand hectares each, worked by one household. Which settlement pattern follows most directly from that practice?", choices=[
   "Dispersed, since a holding that large places its neighbours many kilometres away",
   "Clustered, since ranchers need company",
   "Linear, since cattle move along tracks",
   "Clustered, since livestock require shared labour",
   "Linear, since fences run in straight lines"], ans=0,
   why="EK PSO-5.B.1 says agricultural practices shape rural land-use patterns, and holding size is the most direct route from practice to pattern. If each household needs thousands of hectares, the arithmetic of area puts the next household a long way off."),

 dict(q="A village stands at the centre of a district, and the households living in it cultivate plots scattered at varying distances around it, resting some of them for years at a time. Which combination is this?", choices=[
   "A clustered settlement pattern with land use organized outward from the village",
   "A dispersed settlement pattern with land use organized in strips",
   "A linear settlement pattern with a rectangular survey",
   "A dispersed settlement pattern with a long lot survey",
   "A linear settlement pattern with land use organized in squares"], ans=0,
   why="EK PSO-5.B.2 classifies the settlement itself as clustered, while EK PSO-5.B.1 accounts for the land-use pattern that grows out of the practice. Plots worked from one settlement and rested in rotation produce a ring of land at different stages around a single centre."),

 dict(q="Houses in a flood-prone delta stand along a raised natural levee, the only ground that stays dry, with fields on the wet land behind. Which settlement pattern is this, and what has produced it?", choices=[
   "Linear, produced by a physical feature that offers a narrow strip of usable building land",
   "Clustered, produced by the need for defence",
   "Dispersed, produced by large holdings",
   "Clustered, produced by a rectangular survey",
   "Dispersed, produced by flooding"], ans=0,
   why="EK PSO-5.B.2 names linear among the settlement patterns, and a levee is one of the standard causes of it. Where only a narrow ribbon of ground is dry, buildable land is itself a line, and the settlement takes the shape of the resource."),

 dict(q="A geographer studying an aerial view of farmland can identify the survey method but not the settlement pattern. Which feature of that aerial view would tell her the survey method?", choices=[
   "The shapes of the field and property boundaries",
   "The number of people in each household",
   "The crops growing in each field",
   "The nationality of the landowners",
   "The distance to the nearest city"], ans=0,
   why="EK PSO-5.B.3 names three methods that differ in the geometry they impose -- irregular, rectangular and narrow-strip. Boundary shape is the visible trace of that geometry, whereas EK PSO-5.B.2's settlement categories are read from where the buildings are."),

 dict(q="What is the principal disadvantage of a clustered rural settlement for the farmers who live in it?", choices=[
   "Time and effort are spent travelling to fields that may lie some distance from the village",
   "Farmers cannot share equipment or labour",
   "The village cannot support a school or a place of worship",
   "The land cannot be divided into parcels",
   "The settlement cannot be reached by road"], ans=0,
   why="EK PSO-5.B.2 names clustered among the three patterns, and every arrangement trades one cost against another. Living together makes shared labour, services and defence easy and puts a daily journey between the household and the far edge of its land."),

 dict(q="What is the principal disadvantage of a dispersed rural settlement?", choices=[
   "Households are far from one another, so services and shared labour are harder to organize",
   "Farmers must walk a long way to their own fields",
   "The land cannot be surveyed",
   "Dwellings must be rebuilt every season",
   "Crops cannot be sold commercially"], ans=0,
   why="EK PSO-5.B.2 names dispersed among the three patterns. Living on one's own land removes the journey to the fields and adds distance to everything else, which is why schools, clinics and shops in dispersed districts serve very large areas."),

 dict(q="Why does a township and range survey leave such a distinctive mark on a region's road network?", choices=[
   "Roads were built along the survey lines, so they run north-south and east-west and meet at right angles at regular intervals",
   "Because the survey required roads to curve around each parcel",
   "Because roads were forbidden inside surveyed townships",
   "Because the survey placed all roads along rivers",
   "Because roads under the system are always unpaved"], ans=0,
   why="EK PSO-5.B.3 names township and range as a rural survey method, and the grid is laid out before the roads. Building along the parcel lines is the cheapest option because it uses land nobody is farming, which is why the survey geometry is still legible from the air a century later."),

 dict(q="What is the most serious practical weakness of describing boundaries by metes and bounds?", choices=[
   "The features named as references can move, be cut down, or disappear, leaving the boundary uncertain",
   "The method cannot describe a boundary of any kind",
   "The method requires every parcel to be square",
   "The method can be used only on public land",
   "The method produces parcels that are all identical in size"], ans=0,
   why="EK PSO-5.B.3 names metes and bounds among the survey methods, and its references are physical objects rather than coordinates. A boundary running to a named tree is exact only for as long as the tree stands, which is why such boundaries generate disputes generations later."),

 dict(q="A long lot survey and a linear settlement pattern very often occur together. What connects them?", choices=[
   "Each long lot touches the waterway at one narrow end, so the natural place to build is on that frontage, which strings the dwellings along the water",
   "Long lots are required by law to be settled in villages",
   "The connection is coincidental and has no cause",
   "Linear settlement forces surveyors to use square parcels",
   "Long lots are always laid out far from any waterway"], ans=0,
   why="EK PSO-5.B.2 names linear as a settlement pattern and EK PSO-5.B.3 names long lot as a survey method, and the two are joined by where the value of the parcel sits. If a holding's transport, water and best land are all at one end, every household builds at that end."),

 dict(q="At which scale of analysis does the framework's classification of settlement patterns operate?", choices=[
   "The local scale, since the categories describe how dwellings are arranged relative to one another within a district",
   "The global scale, since the categories describe world population distribution",
   "The state scale, since governments choose settlement patterns",
   "The continental scale, since climate zones cross continents",
   "No scale, since settlement patterns are not spatial"], ans=0,
   why="EK PSO-5.B.2 classifies patterns by the arrangement of dwellings, which is something a person can see by walking or by looking at one aerial photograph. National population distribution is a different measurement made at a different scale."),

 dict(q="A flat, forested plain is to be surveyed for settlement, and it contains almost no distinctive natural landmarks. Which survey method is best suited, and why?", choices=[
   "Township and range, because a rectangular grid can be laid out from astronomical reference lines without needing landmarks at all",
   "Metes and bounds, because the trees provide markers",
   "Long lot, because the plain is flat",
   "Metes and bounds, because a flat plain has no rivers",
   "None of the three, since flat land cannot be surveyed"], ans=0,
   why="EK PSO-5.B.3 names all three methods, and they differ in what they take as their references. A rectangular survey needs only a base line and a meridian, which makes it usable exactly where a boundary-by-landmark description would have nothing to name."),

 dict(q="Which pairing of a term with the correct classification is CORRECT?", choices=[
   "Long lot with survey method, and dispersed with settlement pattern",
   "Long lot with settlement pattern, and dispersed with survey method",
   "Metes and bounds with settlement pattern, and linear with survey method",
   "Township and range with settlement pattern, and clustered with survey method",
   "Clustered with survey method, and linear with survey method"], ans=0,
   why="EK PSO-5.B.2 supplies clustered, dispersed and linear as settlement patterns while EK PSO-5.B.3 supplies metes and bounds, township and range and long lot as survey methods. Only one pairing here puts both terms in the list the framework puts them in."),

 dict(q="Two districts in the same climate grow the same crop. One is worked as a few very large estates and the other as many small family holdings. What does the framework predict about their rural land-use patterns?", choices=[
   "They will differ, since the framework says specific agricultural practices shape different rural land-use patterns",
   "They will be identical, since climate and crop are the same",
   "Neither will have a land-use pattern at all",
   "The estates will produce a linear pattern and the smallholdings a grid",
   "Land-use pattern depends only on the survey method used"], ans=0,
   why="EK PSO-5.B.1 states that specific agricultural practices shape different rural land-use patterns, and how land is held and worked is part of the practice. Field size, the number and placing of dwellings and the road density all follow from whether the ground is farmed in blocks of a thousand hectares or of five."),

 dict(q="Parcels along one bank of a river are recorded below. Using the accompanying figures, which survey method do they represent?",
   table=dict(headers=["Parcel", "Frontage on the river (metres)", "Depth back from the river (metres)"],
     rows=[["Parcel 1", "180", "4,200"],
           ["Parcel 2", "190", "3,900"],
           ["Parcel 3", "165", "4,500"],
           ["Parcel 4", "175", "4,100"]]),
   choices=[
   "Long lot, since every parcel is more than twenty times as deep as it is wide and every one touches the river",
   "Township and range, since the parcels are regular in shape",
   "Metes and bounds, since the river is used as a reference",
   "Long lot, since the parcels are square",
   "Township and range, since each parcel is one mile across"], ans=0,
   why="Every parcel's depth exceeds its frontage by a factor of more than twenty, and each one has frontage on the river, which is the geometry EK PSO-5.B.3 attaches to the long lot. Regularity alone would not distinguish this from a rectangular survey; the extreme ratio and the shared frontage do."),

 dict(q="Four rural districts with the same number of dwellings are recorded below. Using the accompanying figures, which two are clustered?",
   table=dict(headers=["District", "Farm dwellings", "Dwellings in the largest single settlement", "Mean distance to the nearest dwelling (metres)"],
     rows=[["District A", "240", "221", "30"],
           ["District B", "240", "6", "900"],
           ["District C", "240", "196", "45"],
           ["District D", "240", "11", "750"]]),
   choices=[
   "Districts A and C, where almost all dwellings stand in one settlement and the nearest neighbour is tens of metres away",
   "Districts B and D, where dwellings are furthest apart",
   "Districts A and B, since they head the record",
   "All four, since each has the same number of dwellings",
   "None of them, since a clustered pattern requires more dwellings"], ans=0,
   why="Two districts hold more than four fifths of their dwellings in a single settlement with neighbours within 50 metres, while the other two hold under five percent in their largest settlement and average more than 700 metres between dwellings. EK PSO-5.B.2 separates clustered from dispersed on exactly that arrangement, and the equal dwelling counts remove population size as an explanation."),

 dict(q="The standard divisions of a rectangular survey are recorded below. Using the accompanying figures, how large is a parcel described as the north-west quarter of the north-east quarter of a section?",
   table=dict(headers=["Land description", "Share of a section", "Area (acres)"],
     rows=[["Section", "One whole", "640"],
           ["Half section", "One half", "320"],
           ["Quarter section", "One quarter", "160"],
           ["Quarter of a quarter section", "One sixteenth", "40"]]),
   choices=[
   "40 acres, since a quarter of a quarter is one sixteenth of a section",
   "160 acres, since a quarter of a section is described",
   "320 acres, since two quarters are named",
   "640 acres, since the parcel lies within one section",
   "80 acres, since one eighth of a section is described"], ans=0,
   why="A quarter of a quarter is one sixteenth, and one sixteenth of the 640 acres in a section is 40. The record's own rows confirm the proportion at each step, and the description names two successive quarterings rather than adding two quarters together."),

 dict(q="Why can the survey method used to divide a region two centuries ago still be visible in its landscape today?", choices=[
   "Property boundaries are expensive and legally difficult to move, so later fields, roads and field boundaries were fitted to the lines already drawn",
   "Because survey lines are physically painted on the ground and repainted each year",
   "Because farming methods have not changed in two centuries",
   "Because governments require the original survey to be preserved",
   "It cannot; survey methods leave no lasting trace"], ans=0,
   why="EK PSO-5.B.3 names three survey methods, and each imposes a geometry on ownership rather than on any crop. Ownership boundaries outlast the people who drew them because changing one requires agreement and money, so subsequent building follows the lines rather than replacing them."),

 dict(q="A student must state in one sentence what this topic's three essential knowledge statements establish. Which sentence stays inside what the framework claims?", choices=[
   "Agricultural practices shape rural land-use patterns; settlements are classified as clustered, dispersed or linear; and land is surveyed by metes and bounds, township and range, or long lot",
   "Settlement patterns and survey methods are two names for the same classification",
   "Rural settlement patterns are determined entirely by the survey method used",
   "Survey methods are classified as clustered, dispersed and linear",
   "Agricultural practice has no effect on rural land use"], ans=0,
   why="EK PSO-5.B.1, EK PSO-5.B.2 and EK PSO-5.B.3 make exactly these three claims, and the two classifications are separate lists answering different questions. Survey method and settlement pattern are strongly associated in practice without either determining the other."),
]
