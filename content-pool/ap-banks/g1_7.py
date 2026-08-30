# AP HUMAN GEOGRAPHY 1.7 Regional Analysis -- 30 questions
# CED Course Framework V.1, Unit 1. Enduring understanding SPS-1; learning
# objective SPS-1.A, "Describe different ways that geographers define regions."
#
# Essential knowledge, in full -- four statements, and this module uses all four:
#   SPS-1.A.1  Regions are defined on the basis of one or more unifying
#              characteristics or on patterns of activity.
#   SPS-1.A.2  Types of regions include formal, functional, and
#              perceptual/vernacular.
#   SPS-1.A.3  Regional boundaries are transitional and often contested and
#              overlapping.
#   SPS-1.A.4  Geographers apply regional analysis at local, national, and
#              global scales.
#
# SPS-1.A.1 is doing more work than it looks. It gives TWO grounds on which a
# region may be built -- a shared characteristic, or a pattern of ACTIVITY --
# and that is exactly the formal/functional split of SPS-1.A.2 stated in
# advance. A formal region is unified by a trait its members share; a functional
# region is unified by the activity organized around a node; a
# perceptual/vernacular region is unified by what people believe about it, which
# is why its boundary is the most contested of the three.
#
# SPS-1.A.3 is the sentence students most often skip, and several items here are
# built on it alone: a regional boundary is a transition, not a line, and one
# place can belong to several regions at once. Items 9, 12, 17, 20, 24, 28 and 29
# turn on it.
#
# SPS-1.A.4 makes regional analysis scale-independent -- local, national and
# global -- which is why items 6, 15 and 23 apply the same three region types at
# three different extents.
#
# A note on the terminology, because the checker enforces it: this course treats
# "perceptual" and "vernacular" as two names for one type, so no question offers
# them as two separate options.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_7.py. FIVE choices (A-E).
TOPIC = ("1.7", "Regional Analysis", 1)

QUESTIONS = [
 dict(q="A geographer delimits an area within which more than 80 percent of the population speaks the same language. What type of region has she defined?",
   choices=[
     "A formal region, since it is bounded by a measurable characteristic its members share",
     "A functional region, since language is used to communicate",
     "A perceptual region, since speakers feel a shared identity",
     "A region defined by a node and its hinterland",
     "No region at all, since language is not a geographic variable"],
   ans=0,
   why="EK SPS-1.A.1 allows a region to rest on one or more unifying characteristics, and EK SPS-1.A.2 names formal as the type built that way. A measurable trait shared across an area is the defining structure of a formal region."),

 dict(q="A newspaper's delivery area, defined as everywhere its vans reach before 7 a.m. each morning, is best classified as",
   choices=[
     "A functional region, organized around a node by an activity radiating from it",
     "A formal region, since the boundary can be drawn precisely",
     "A perceptual region, since readers feel loyal to the paper",
     "A formal region, since every household inside it receives the same paper",
     "Not a region, since it changes if a van breaks down"],
   ans=0,
   why="EK SPS-1.A.1's second ground for a region is a pattern of activity, and EK SPS-1.A.2 names functional as that type. The area is held together by the operation of a single center rather than by a trait its residents share."),

 dict(q="Residents of several states argue about whether their state 'is really part of the Midwest.' The disputed area is best described as",
   choices=[
     "A perceptual region, whose extent depends on what people believe rather than on a measured trait",
     "A formal region, since states have precise boundaries",
     "A functional region, since the Midwest has an economic center",
     "A region that does not exist, since people disagree about it",
     "A formal region, since the argument concerns states"],
   ans=0,
   why="EK SPS-1.A.2 names perceptual and vernacular as one type, and EK SPS-1.A.3 says regional boundaries are often contested. A region whose limits vary with who is asked is by definition built out of belief rather than measurement."),

 dict(q="Which statement most accurately describes the boundary of a functional region?",
   choices=[
     "It marks the point where the influence of one node gives way to that of another, and it usually fades rather than snapping",
     "It is the legal border of the jurisdiction containing the node",
     "It is fixed permanently once the node is established",
     "It is wherever residents say the region ends",
     "It cannot be mapped at all"],
   ans=0,
   why="EK SPS-1.A.3 states that regional boundaries are transitional. Interaction with a node weakens with distance, so between two nodes there is a zone of divided allegiance rather than a line, which is what a commuting or trade-area boundary really is."),

 dict(q="A geographer defines a coffee-growing region using elevation, rainfall, and the crop actually planted. This is",
   choices=[
     "A formal region defined by more than one unifying characteristic at once",
     "A functional region, since coffee is exported through a port",
     "A perceptual region, since growers identify with the crop",
     "Not a region, since three criteria cannot define one area",
     "A functional region, since the three criteria interact"],
   ans=0,
   why="EK SPS-1.A.1 explicitly permits a region built on one OR MORE unifying characteristics. Combining criteria narrows the area without changing the type, since all three are traits the area possesses rather than activities organized from a center."),

 dict(q="Which set correctly matches a region to the scale at which it is being analyzed?",
   choices=[
     "A neighborhood historic district is local; the Corn Belt is national; the Sahel is global in reach across a continent",
     "All three examples are local, since each has a boundary",
     "All three examples are global, since regions are worldwide",
     "Only the Sahel is a region; the other two are administrative units",
     "Scale cannot be assigned to a region"],
   ans=0,
   why="EK SPS-1.A.4 states that geographers apply regional analysis at local, national and global scales. The same three region types recur at every extent, and the scale is set by the extent of the area analyzed rather than by the type."),

 dict(q="A transit authority maps the area from which more than 30 percent of workers commute into the central city. The result is",
   choices=[
     "A functional region, since commuting is the activity that organizes it",
     "A formal region, since 30 percent is a precise threshold",
     "A perceptual region, since commuters identify with the city",
     "A formal region, since every place inside shares the same commuting share",
     "Not a region at all, since the commuting share changes from year to year"],
   ans=0,
   why="A threshold makes the boundary crisp but does not change what unifies the area, and what unifies it here is daily movement toward one center. EK SPS-1.A.1's pattern of activity and EK SPS-1.A.2's functional type are the operative statements."),

 dict(q="Which of these is the best example of a formal region?",
   choices=[
     "The area of a country in which annual rainfall exceeds 1,000 millimetres",
     "The area served by a metropolitan water utility",
     "The area people call 'the South'",
     "The catchment of a regional airport",
     "The delivery zone of a pizza chain"],
   ans=0,
   why="EK SPS-1.A.2's formal type rests on a shared measurable characteristic, which a rainfall threshold is. The other four are held together by activity organized from a center or by popular belief, which makes them functional or perceptual."),

 dict(q="A place lies inside a national forest region, a river basin region, a metropolitan commuting region, and an area many residents call 'the high country.' What does this illustrate?",
   choices=[
     "Regions overlap, and one place can belong to several defined on different criteria at once",
     "Only one of the four classifications can be correct",
     "The place is in a contested territory",
     "Regional analysis is possible only at the national scale",
     "The four regions must share the same boundary"],
   ans=0,
   why="EK SPS-1.A.3 says regional boundaries are often overlapping. Because each region is built on a different unifying criterion, membership in one implies nothing about membership in another, and a single location can satisfy them all."),

 dict(q="Which is the strongest reason a perceptual region is difficult to map with a single line?",
   choices=[
     "Different people place its edge differently, so any single line represents one view among many",
     "Perceptual regions are always very large",
     "Perceptual regions have no names",
     "Perceptual regions change location each year",
     "Perceptual regions cannot be studied by geographers"],
   ans=0,
   why="EK SPS-1.A.3 states that regional boundaries are transitional and often contested, and a region built on belief is the extreme case. Mapping it honestly means showing a gradient of agreement rather than a single boundary."),

 dict(q="A geographer studies the area within which a hospital treats most emergency patients. To classify the region she should ask",
   choices=[
     "Whether the area is unified by movement toward one center or by a trait its parts share",
     "Whether the hospital is publicly or privately owned",
     "Whether the area has a legal boundary",
     "Whether local residents can name the region",
     "Whether the area is larger than a county"],
   ans=0,
   why="EK SPS-1.A.1 gives exactly two grounds for defining a region, a unifying characteristic or a pattern of activity, and EK SPS-1.A.2 attaches a type to each. Ownership, legal status, popular naming and size do not distinguish the types."),

 dict(q="Two adjacent metropolitan areas are growing toward each other, and a belt of towns between them now sends about half its commuters each way. In regional terms this belt is",
   choices=[
     "A transition zone in which the two functional regions overlap rather than meet at a line",
     "Part of neither region, since it is divided",
     "A formal region defined by its intermediate position",
     "A perceptual region, since residents are uncertain where they belong",
     "Evidence that functional regions cannot be mapped"],
   ans=0,
   why="EK SPS-1.A.3's claim that regional boundaries are transitional and overlapping describes this exactly. A split commuting field is not a failure of the classification; it is what the edge of a functional region actually looks like."),

 dict(q="Which of the following would change the boundary of a functional region without any change in the physical landscape?",
   choices=[
     "A new expressway that lets people commute to the node from twice as far away",
     "A drought that lowers crop yields in the region",
     "A rise in the average age of the region's population",
     "A change in the name residents use for the region",
     "A new soil survey with more accurate maps"],
   ans=0,
   why="A functional region is bounded by how far the node's activity effectively reaches, so anything that extends that reach moves the boundary outward. Yields, age structure, naming and survey accuracy do not alter where commuting stops."),

 dict(q="A geographer describes 'the Rust Belt' using deindustrialization, population loss, and a shared sense among residents of having been left behind. Which classification is most defensible?",
   choices=[
     "It combines formal criteria with a perceptual identity, which is common for widely used regional names",
     "It is purely formal, since deindustrialization can be measured",
     "It is purely functional, since the region once had industrial centers",
     "It is purely perceptual, since the name is informal",
     "It is not a region, since it mixes criteria"],
   ans=0,
   why="EK SPS-1.A.1 permits one or more unifying characteristics and EK SPS-1.A.2 names three types without forbidding a region from having features of more than one. Measurable decline and shared identity are both real here, and the honest classification says so."),

 dict(q="At which scale is regional analysis appropriate, according to the framework?",
   choices=[
     "At local, national, and global scales alike",
     "Only at the national scale, since regions are subdivisions of countries",
     "Only at the global scale, since world regions are the standard units",
     "Only at the local scale, since regions must be observed directly",
     "At no scale, since regions are informal constructs"],
   ans=0,
   why="EK SPS-1.A.4 states in so many words that geographers apply regional analysis at local, national and global scales. Nothing in the definition of a region ties it to a particular extent, only to a unifying criterion."),

 dict(q="Which question would best distinguish a formal region from a functional one in a case a student finds ambiguous?",
   choices=[
     "Is every part of the area alike in some measured respect, or is every part connected to the same center?",
     "Does the area have a name that people use?",
     "Is the area larger than a province?",
     "Was the area defined by a government or by a researcher?",
     "Does the area appear on a published map?"],
   ans=0,
   why="EK SPS-1.A.1's two grounds -- a unifying characteristic and a pattern of activity -- are exactly the two halves of this question. Naming, size, authorship and publication cut across the distinction and settle nothing."),

 dict(q="A survey asks residents of 40 counties whether they consider themselves part of a named region. Support falls from 95 percent in the core to 10 percent at the far edge. The best conclusion is that",
   choices=[
     "The region's boundary is a gradient of agreement, which is what a perceptual boundary looks like when measured",
     "The region does not exist, since agreement is not universal",
     "The boundary should be drawn where support first drops below 95 percent",
     "The survey was poorly designed, since a region must have a definite edge",
     "The counties with low support belong to no region at all"],
   ans=0,
   why="EK SPS-1.A.3 states that regional boundaries are transitional. Measured agreement declining smoothly from a core is the empirical form that transition takes, and choosing any single cut-off is a decision by the analyst rather than a discovery."),

 dict(q="Which of these is a functional region at the GLOBAL scale?",
   choices=[
     "The network of airports and routes served by a single alliance of airlines",
     "The set of countries where more than half the population is under 25",
     "The area people call 'the West'",
     "The countries with a Mediterranean climate",
     "The continent of Africa"],
   ans=0,
   why="EK SPS-1.A.4 allows regional analysis at the global scale, and EK SPS-1.A.2's functional type is defined by activity organized through nodes. An airline network is exactly a set of nodes and the flows connecting them, spread worldwide."),

 dict(q="A student says a region 'must have the same characteristics throughout to count as a region.' The best correction is that",
   choices=[
     "Uniformity is what defines a formal region only; functional and perceptual regions are unified by activity or by belief instead",
     "Uniformity is required of every region without exception",
     "Uniformity is never required, since all regions are informal",
     "Regions require uniformity only at the global scale",
     "The student is right, and functional regions are not regions"],
   ans=0,
   why="EK SPS-1.A.2 names three types, and only one of them is built on a shared trait. EK SPS-1.A.1's alternative ground, a pattern of activity, is precisely a way of unifying an area that is internally varied."),

 dict(q="Two governments disagree about where a resource-rich region begins, and each publishes a map showing it inside its own territory. This illustrates which statement in the framework?",
   choices=[
     "That regional boundaries are often contested",
     "That regions must be defined at the global scale",
     "That formal regions cannot be mapped",
     "That perceptual regions are the only contested type",
     "That regions are defined by patterns of activity alone"],
   ans=0,
   why="EK SPS-1.A.3 states that regional boundaries are transitional and often contested and overlapping. A dispute in which each party's map favors its own claim is the political form of that contest, and it can occur for a formal region as easily as a perceptual one."),

 dict(q="A retailer wants to know which stores compete with one another. Which regional concept is most useful?",
   choices=[
     "Functional regions, since each store's trade area is the zone from which it actually draws customers",
     "Formal regions, since stores in the same climate zone compete",
     "Perceptual regions, since customers have opinions about neighborhoods",
     "Political regions, since stores lie in different jurisdictions",
     "No regional concept, since competition is an economic question"],
   ans=0,
   why="A trade area is defined by where customers come from, which is a pattern of activity organized around a node exactly as EK SPS-1.A.1 and EK SPS-1.A.2 describe. Stores compete where their trade areas overlap, which the functional concept makes visible."),

 dict(q="Which is the most accurate statement about the relationship between a region and the criterion used to define it?",
   choices=[
     "Changing the criterion changes the region, so the boundary is a consequence of the analyst's choice as much as of the world",
     "A region exists independently of any criterion and is simply discovered",
     "Only governments may set the criterion for a region",
     "Every criterion yields the same boundary if applied carefully",
     "A region can be defined by only one criterion"],
   ans=0,
   why="EK SPS-1.A.1 makes the unifying characteristic or the pattern of activity the basis of the region, which means the region follows from the choice. Different thresholds and different traits give different boundaries from the same underlying reality."),

 dict(q="At the local scale, which of the following is best analyzed as a perceptual region?",
   choices=[
     "The area residents call 'the old quarter,' whose extent no two residents agree on exactly",
     "The catchment of the neighborhood elementary school",
     "The census tracts with median incomes above the city median",
     "The blocks served by a single water main",
     "The area within 500 metres of the tram line"],
   ans=0,
   why="EK SPS-1.A.4 puts regional analysis at the local scale as well, and EK SPS-1.A.2's perceptual type is built on shared belief. A named district whose limits vary from resident to resident is that type at neighborhood extent."),

 dict(q="A geographer argues that world regions such as 'Latin America' or 'Sub-Saharan Africa' should be used carefully. Which reason is strongest?",
   choices=[
     "Each groups very different countries under one label, and the boundary drawn depends on which criterion is chosen",
     "World regions are too small to be useful",
     "World regions have no names in common use",
     "World regions can only be functional",
     "World regions were abolished by the framework"],
   ans=0,
   why="EK SPS-1.A.1 makes a region a consequence of its defining criterion and EK SPS-1.A.3 warns that boundaries are transitional and contested. A continental label conceals both the internal variety it contains and the arbitrariness of where it was cut."),

 dict(q="Which of the following best captures why the framework groups 'perceptual' and 'vernacular' as a single type?",
   choices=[
     "Both names describe a region that exists because people name and believe in it rather than because a measurement defines it",
     "Both names describe regions defined by a central node",
     "Both names describe regions defined by climate",
     "The two names describe different types that happen to be studied together",
     "The two names refer to regions at different scales"],
   ans=0,
   why="EK SPS-1.A.2 prints the type as 'perceptual/vernacular', treating the pair as one category. What both words point at is a region constituted by common usage and belief, which is why it has no measurable criterion to appeal to."),

 dict(q="Four counties are surveyed for the characteristics below. Using the table, which counties belong to a formal region defined as areas where wheat exceeds half the cropped area AND rainfall is under 600 millimetres?",
   table=dict(
     headers=["County", "Wheat share of cropped area (%)", "Annual rainfall (mm)"],
     rows=[
       ["County 1", "62", "540"],
       ["County 2", "48", "520"],
       ["County 3", "71", "580"],
       ["County 4", "55", "690"]]),
   choices=[
     "Counties 1 and 3, the only counties meeting both criteria",
     "Counties 1, 3, and 4, since all three exceed half their cropped area in wheat",
     "Counties 1, 2, and 3, since all three receive under 600 millimetres",
     "All four counties, since each meets at least one criterion",
     "No county, since no county exceeds 75 percent wheat"],
   ans=0,
   why="Two criteria applied together admit only the counties satisfying both, and 62 with 540 and 71 with 580 are the pairs that do. Applying either criterion alone would admit three counties, which is why a multi-criterion formal region is smaller than the union of its parts."),

 dict(q="Commuting into a central city is recorded for five surrounding towns. Using the table, which towns fall inside a functional region defined by at least 25 percent of workers commuting to the center?",
   table=dict(
     headers=["Town", "Workers", "Commuting to central city"],
     rows=[
       ["Town A", "8,000", "3,200"],
       ["Town B", "5,000", "1,000"],
       ["Town C", "12,000", "3,600"],
       ["Town D", "4,000", "1,400"],
       ["Town E", "10,000", "1,900"]]),
   choices=[
     "Towns A, C, and D, whose commuting shares are 40, 30, and 35 percent",
     "Towns A and D only, since they have the highest shares",
     "Towns A, C, D, and E, since only Town B falls below the threshold",
     "Town C alone, since it sends the largest number of commuters",
     "All five towns, since each sends commuters to the center"],
   ans=0,
   why="Dividing commuters by workers gives 40, 20, 30, 35 and 19 percent, so three towns clear the 25 percent line. The town sending the most commuters in absolute terms is not the one with the highest share, which is why a functional boundary is drawn on the ratio."),

 dict(q="Residents of six counties were asked whether their county is part of a named vernacular region. Using the table, what does the pattern of responses show about the region's boundary?",
   table=dict(
     headers=["County", "Distance from core (km)", "Residents answering yes (%)"],
     rows=[
       ["Core county", "0", "96"],
       ["County V", "40", "88"],
       ["County W", "90", "74"],
       ["County X", "140", "55"],
       ["County Y", "200", "31"],
       ["County Z", "260", "9"]]),
   choices=[
     "Agreement declines steadily with distance from the core, so the boundary is a transition zone rather than a line",
     "Agreement is uniform, so the boundary is sharp and easy to draw",
     "Agreement rises with distance, so the region has no core",
     "Exactly half the counties agree, so the boundary lies between the third and fourth",
     "The responses show that the region does not exist"],
   ans=0,
   why="Agreement falls from 96 percent to 9 percent as distance rises from zero to 260 kilometres, with no jump anywhere in the sequence. A monotonic decline is the measured form of the transitional boundary the framework describes."),

 dict(q="One district's membership in four differently defined regions is recorded below. Using the table, which conclusion is supported?",
   table=dict(
     headers=["Region", "Basis of definition", "District included?"],
     rows=[
       ["Upland farming belt", "Shared elevation and crop", "Yes"],
       ["Port city commuter field", "Journey to work", "Yes"],
       ["The 'lake country'", "Local usage", "No"],
       ["River basin authority area", "Drainage", "Yes"]]),
   choices=[
     "The district belongs to three overlapping regions defined on three different bases and to a fourth not at all",
     "The district belongs to all four regions listed",
     "The district belongs to only one region, since a place can have only one",
     "The four regions must therefore share a common boundary",
     "The district belongs to no region, since the four disagree"],
   ans=0,
   why="Three rows record inclusion and one records exclusion, and the bases named are a shared trait, a journey-to-work pattern, local usage and drainage. Overlapping membership on different criteria is exactly what the framework's statement about boundaries predicts."),

 dict(q="A world region is defined three different ways and the resulting country lists are compared. Using the table, which statement is best supported?",
   table=dict(
     headers=["Defining criterion", "Countries included", "Countries also in all three lists"],
     rows=[
       ["Shared colonial language", "21", "12"],
       ["Membership of the regional trade bloc", "15", "12"],
       ["Popular usage in the media", "26", "12"]]),
   choices=[
     "Only 12 countries appear on all three lists, so the region's extent depends on which criterion is chosen",
     "All three criteria produce the same region",
     "The largest list is the correct definition of the region",
     "The smallest list is the correct definition of the region",
     "No country appears on more than one list"],
   ans=0,
   why="The three criteria admit 21, 15 and 26 countries while only 12 are common to all of them, so at least three countries in even the smallest list fall outside the shared core. A region is a consequence of its criterion, and different criteria genuinely disagree."),
]
