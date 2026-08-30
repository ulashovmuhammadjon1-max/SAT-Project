# AP HUMAN GEOGRAPHY 1.1 Introduction to Maps -- 30 questions
# CED: Course Framework V.1 (2020, seven units), Unit 1 Thinking Geographically.
# Enduring understanding IMP-1: geographers use maps and data to depict
# relationships of time, space, and scale. Learning objective IMP-1.A.
#
# Essential knowledge this module rests on:
#   IMP-1.A.1  Types of maps include reference maps and thematic maps.
#   IMP-1.A.2  Types of spatial patterns represented on maps include absolute
#              and relative distance and direction, clustering, dispersal,
#              and elevation.
#   IMP-1.A.3  All maps are selective in information; map projections inevitably
#              distort spatial relationships in shape, area, distance,
#              and direction.
#
# The named thematic-map types (choropleth, dot distribution, graduated symbol,
# isoline, cartogram, flow-line) and the named projections (Mercator,
# Gall-Peters, Robinson, Goode's homolosine, azimuthal, conic) are NOT printed in
# IMP-1.A -- the EK gives the reference/thematic split and the four distortion
# properties. They are the standard operationalisation of that EK and are what
# the CED's own sample questions assume a student can read (sample MC 11 is a
# choropleth). Items that turn on one of them are keyed to what the map type or
# projection DOES -- a property that can be reasoned about -- not to a framework
# sentence that does not exist. Items keyed to a framework sentence cite it.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g1_1.py. FIVE choices (A-E), the real exam's format.
TOPIC = ("1.1", "Introduction to Maps", 1)

QUESTIONS = [
 dict(q="A county elections office needs a map that shows every precinct boundary and the streets inside it, with no statistical shading of any kind. Which type of map is being described?",
   choices=[
     "A reference map, because its purpose is to show where things are",
     "A choropleth map, because precincts are enumeration units",
     "A cartogram, because precincts differ in population",
     "A flow-line map, because voters travel to polling places",
     "An isoline map, because precinct boundaries are continuous lines"],
   ans=0,
   why="EK IMP-1.A.1 splits maps into reference and thematic. The office wants the base geography itself -- boundaries and streets -- which is exactly what a reference map supplies; every other option displays a variable laid over that geography, and no variable has been mentioned."),

 dict(q="What most fundamentally distinguishes a thematic map from a reference map?",
   choices=[
     "It is built to show the spatial pattern of one variable rather than to show where places are",
     "It is drawn at a larger cartographic scale",
     "It uses a projection that preserves area",
     "It shows physical features instead of political ones",
     "It covers a smaller portion of Earth's surface"],
   ans=0,
   why="EK IMP-1.A.1 names the two types, and the difference is one of purpose, not of scale, projection, subject matter or extent -- a thematic map exists to display the distribution of some attribute, and a reference map exists to locate things."),

 dict(q="A geographer wants to map median household income for all 3,143 U.S. counties so that regional differences in income level stand out at a glance. Which thematic map type fits the data?",
   choices=[
     "Choropleth, because income is already a rate-like value comparable across units of different size",
     "Dot distribution, because each dot could stand for one household",
     "Flow-line, because income moves between counties",
     "Cartogram, because counties differ in area",
     "Graduated symbol, because income is a point measurement"],
   ans=0,
   why="A choropleth shades enumeration units, so it is only valid for values already standardised for the size of the unit. A median is such a value; the other four either misrepresent a per-unit average as a count, as movement, or as a point observation."),

 dict(q="Why is it a cartographic error to make a choropleth map of the raw number of people living in each county?",
   choices=[
     "Shading an area by a raw count makes large counties look important simply because they are large",
     "Counts cannot be sorted into classes",
     "Counties are not enumeration units",
     "Raw counts require an equal-area projection to be mapped at all",
     "A choropleth cannot display more than four classes"],
   ans=0,
   why="Choropleth shading fills the whole polygon, so the eye reads area as quantity. Unless the value is normalised -- a rate, a density, a percentage -- a big sparsely settled county and a small crowded one can carry the same shade for opposite reasons."),

 dict(q="Each dot on a map of Australian sheep stands for 10,000 animals. What does the resulting pattern of dots communicate that a shaded map of sheep per state could not?",
   choices=[
     "Where within each state the animals actually are",
     "The exact number of sheep at any point",
     "The rate of change in the sheep population",
     "The direction sheep are moved between states",
     "The elevation of the grazing land"],
   ans=0,
   why="A dot distribution map places its dots at the locations of the phenomenon, so clustering and empty space inside a unit are visible; a choropleth flattens the whole state to one shade and hides all internal variation."),

 dict(q="A map of the Pacific Northwest draws lines connecting all points receiving the same mean annual rainfall. Which map type is this, and what property of the data makes it appropriate?",
   choices=[
     "Isoline, because rainfall varies continuously across space rather than by administrative unit",
     "Choropleth, because rainfall totals are averages",
     "Cartogram, because wetter areas matter more",
     "Dot distribution, because each storm can be plotted",
     "Flow-line, because moisture moves inland from the ocean"],
   ans=0,
   why="An isoline map is the one type built for a continuous surface: the variable has a value everywhere, not only where a boundary has been drawn, so lines of equal value are meaningful. Rainfall, elevation and temperature are the standard cases."),

 dict(q="A map of Europe redraws each country so that its area is proportional to the number of asylum applications it received, leaving the countries' true shapes badly distorted. What is the mapmaker deliberately trading away, and for what?",
   choices=[
     "True area and shape, in exchange for making the magnitude of the variable immediately readable",
     "True direction, in exchange for a larger cartographic scale",
     "Topological adjacency, in exchange for equal-area accuracy",
     "The ability to show any quantitative variable, in exchange for legibility",
     "Elevation information, in exchange for showing political boundaries"],
   ans=0,
   why="A cartogram is a value-by-area map: it discards the very geometry a projection normally tries to protect so that the size a reader sees is the quantity itself. Adjacency is usually preserved, which is what still makes the map recognisable."),

 dict(q="Arrows of varying thickness on a world map show the tonnage of soybeans shipped from Brazil to each of its main customers. Which map type is this?",
   choices=[
     "A flow-line map, since it depicts both the direction and the volume of movement",
     "A graduated symbol map, since symbol size varies",
     "An isoline map, since the arrows are lines",
     "A reference map, since it shows real ports",
     "A dot distribution map, since each shipment is a discrete event"],
   ans=0,
   why="Flow-line mapping is the technique for interaction between places: the line's path carries direction and its width carries magnitude, which no static-location map type can show at once."),

 dict(q="Circles of increasing size are placed on the capital city of each South American country, scaled to that country's annual coffee exports. What must a reader be careful about when comparing two of these circles?",
   choices=[
     "The eye judges circle area unreliably, so a circle twice as wide represents four times the value, not twice",
     "The circles show a rate, so they cannot be compared between countries",
     "The circles are placed at country centroids, so they misstate direction",
     "Graduated symbols can only be compared if the map is equal-area",
     "The circles must all fall inside the borders of the units they describe"],
   ans=0,
   why="Graduated symbol maps encode magnitude in a two-dimensional symbol, and area grows with the square of the radius. Readers systematically underestimate the large symbols, which is the standard caution about this map type."),

 dict(q="Two atlases print choropleth maps of the same six unemployment rates. One cuts the range into three equal-width classes; the other puts two counties in each of three classes. Which statement about the table is correct, and what does it illustrate?",
   table=dict(
     headers=["County", "Unemployment rate (%)"],
     rows=[
       ["Ashfield", "3.1"],
       ["Bellwood", "4.0"],
       ["Cranmere", "4.2"],
       ["Dunmore", "8.9"],
       ["Eastport", "9.0"],
       ["Fairholt", "15.2"]]),
   choices=[
     "Cranmere sits in the lowest class under equal-width breaks and the middle class under equal-count breaks, so the classification alone changes the map",
     "Fairholt sits in the highest class under both methods, which proves the two maps must look alike",
     "Every county keeps its class under both methods, so classification cannot matter",
     "The equal-width method is invalid because the rates are percentages",
     "Only a map with six classes, one per county, could be honest about these data"],
   ans=0,
   why="Equal-width breaks over the 3.1-to-15.2 range fall at 7.13 and 11.17, putting Ashfield, Bellwood and Cranmere together at the bottom; equal-count breaks put two counties per class, so Cranmere joins Dunmore in the middle. EK IMP-1.A.3's claim that all maps are selective covers this: identical numbers, two defensible methods, two different visual regions."),

 dict(q="A student says a world map showing only capital cities and international borders is 'objective, because it leaves out opinions.' What is the strongest geographic objection?",
   choices=[
     "Deciding which borders and which cities to draw is itself a selection, and contested borders have to be drawn one way or another",
     "The map is at too small a scale to be objective",
     "Reference maps are always less accurate than thematic maps",
     "Objectivity would require an equal-area projection",
     "Capital cities cannot be located precisely enough to map"],
   ans=0,
   why="EK IMP-1.A.3's claim that all maps are selective applies to reference maps too. Omission is a choice, and a map of borders necessarily takes a position wherever a border is disputed."),

 dict(q="The straight-line separation between Cairo and Khartoum is about 1,600 kilometers. Which term names that measurement?",
   choices=[
     "Absolute distance, because it is stated in a standard unit of length",
     "Relative distance, because it depends on the route taken",
     "Distance decay, because interaction falls off with separation",
     "Time-space compression, because travel is faster than it once was",
     "Absolute direction, because it is measured from a fixed reference"],
   ans=0,
   why="EK IMP-1.A.2 lists absolute and relative distance among the spatial patterns maps represent. Absolute distance is separation in standardised units; the alternatives describe how far apart places feel, how interaction weakens, and how connectivity changes."),

 dict(q="A commuter says her office is 'forty minutes away' while a colleague says it is 'eleven kilometers away.' Which pair of terms correctly labels the two statements, in that order?",
   choices=[
     "Relative distance, then absolute distance",
     "Absolute distance, then relative distance",
     "Relative direction, then absolute direction",
     "Distance decay, then time-space compression",
     "Site description, then situation description"],
   ans=0,
   why="Time, cost and effort are measures of relative distance, which changes with traffic, mode and infrastructure; kilometers are the standard unit, so the second statement is absolute distance."),

 dict(q="A geographer notes that Detroit is at roughly 42 degrees north latitude, and a Detroit resident says the city is 'up north.' The second statement is an example of",
   choices=[
     "Relative direction, since it is expressed with reference to the speaker's own frame",
     "Absolute direction, since north is a cardinal direction",
     "Absolute location, since a place is being named",
     "Elevation, since 'up' is a vertical term",
     "Dispersal, since the statement spreads a place out"],
   ans=0,
   why="EK IMP-1.A.2 pairs absolute and relative direction. A cardinal bearing measured from the pole is absolute; 'up north' is stated relative to where the speaker stands and to a cultural sense of the map, and would change for a speaker in Ontario."),

 dict(q="On a map of Nevada, gold-mining towns appear tightly packed along a single belt while the rest of the state is nearly empty of them. Which term describes this pattern?",
   choices=[
     "Clustering, because the phenomenon is concentrated in one part of the area mapped",
     "Dispersal, because much of the state has no towns",
     "Elevation, because mining follows the mountains",
     "Relative distance, because the towns are close together",
     "Selectivity, because the map omits other towns"],
   ans=0,
   why="EK IMP-1.A.2 names clustering and dispersal as spatial patterns. Concentration into a limited zone is clustering; the emptiness elsewhere is the same fact seen from the other side, not a second, separate pattern."),

 dict(q="Farmsteads in the American Midwest sit roughly evenly spaced across the countryside, one to each quarter-section, with no obvious concentrations. This pattern is best described as",
   choices=[
     "Dispersal, because the features are spread out at regular intervals rather than concentrated",
     "Clustering, because the farms all belong to one region",
     "Distance decay, because the farms thin out with distance",
     "Absolute location, because each farm has coordinates",
     "Time-space compression, because roads connect the farms"],
   ans=0,
   why="EK IMP-1.A.2's dispersal is the opposite of clustering: features occupy the whole area rather than concentrating in part of it. Regular spacing is the strongest form of it."),

 dict(q="A topographic map shows contour lines packed closely together along one side of a ridge and spread far apart on the other. What does the contrast tell a reader?",
   choices=[
     "The closely spaced side is much steeper, since the same interval of rise is crossed in a shorter horizontal distance",
     "The closely spaced side is higher above sea level",
     "The widely spaced side has been surveyed less carefully",
     "The two sides face different cardinal directions",
     "The map uses two different contour intervals"],
   ans=0,
   why="Contours are isolines of elevation drawn at a fixed vertical interval, so their horizontal spacing is a direct reading of slope: the same rise packed into less ground is a steeper gradient. EK IMP-1.A.2 lists elevation among the patterns maps portray."),

 dict(q="Why can no flat map preserve shape, area, distance and direction all at once?",
   choices=[
     "A curved surface cannot be flattened without stretching or tearing it somewhere",
     "Cartographers have not yet found the necessary mathematics",
     "Satellite data is not accurate enough at the poles",
     "Paper and screens have a fixed aspect ratio",
     "The four properties are only defined for small areas"],
   ans=0,
   why="EK IMP-1.A.3 states that projections inevitably distort spatial relationships. The reason is geometric rather than technical: a sphere is not developable, so every projection buys accuracy in one property with error in another."),

 dict(q="A navigator plotting a constant compass bearing across the Atlantic wants that course to appear as a straight line on the chart. Which projection serves that purpose, and at what cost?",
   choices=[
     "Mercator, at the cost of enormously exaggerated area toward the poles",
     "Gall-Peters, at the cost of exaggerated shape near the equator",
     "Robinson, at the cost of interrupted ocean basins",
     "Goode's homolosine, at the cost of distorted area",
     "A polar azimuthal projection, at the cost of distorted direction"],
   ans=0,
   why="Mercator is conformal and was designed so that a line of constant bearing is straight, which is why it survives on nautical charts; the same mathematics inflates high-latitude area, so Greenland is drawn near the size of Africa."),

 dict(q="On a Mercator world map, Greenland appears roughly as large as Africa. What is the correct explanation?",
   choices=[
     "Mercator stretches area increasingly with latitude, and Greenland lies far nearer the pole than Africa does",
     "Greenland is genuinely close to Africa in area once the ice sheet is included",
     "Mercator preserves area but distorts shape, which misleads the eye",
     "The two landmasses are drawn at different cartographic scales on the same sheet",
     "Africa is drawn smaller so that its interior detail will fit"],
   ans=0,
   why="Mercator's spacing of parallels grows toward the poles to keep angles true, so the areal exaggeration is a function of latitude. Africa straddles the equator, where the exaggeration is least, and Greenland sits above 60 degrees north, where it is extreme."),

 dict(q="An organisation mapping the global distribution of childhood vaccination coverage insists that the map must not overstate the size of any region. Which projection best meets that requirement?",
   choices=[
     "Gall-Peters, because it is an equal-area projection",
     "Mercator, because it is conformal",
     "A polar azimuthal projection, because it preserves direction from its center",
     "A conic projection, because it is accurate along its standard parallels",
     "Robinson, because it minimizes every kind of error at once"],
   ans=0,
   why="Comparing a distribution between regions requires that equal areas on the ground occupy equal areas on the page, which is what an equal-area projection guarantees; the price is visibly stretched shapes, and Robinson is a compromise that is exactly equal-area nowhere."),

 dict(q="Goode's homolosine projection is interrupted, splitting the oceans into lobes. What does this design buy the mapmaker?",
   choices=[
     "Land areas keep their true relative size with less shape distortion than an uninterrupted equal-area map",
     "Compass bearings become straight lines across the whole map",
     "The map becomes suitable for plotting sea routes",
     "Distance can be measured accurately between any two points",
     "The poles are shown as lines rather than points"],
   ans=0,
   why="Interruption pushes the unavoidable error into the oceans, where the map has nothing to say, so the continents come out equal-area and reasonably shaped. That is a good bargain for a distribution map and a bad one for navigation, which the interruptions cut across."),

 dict(q="The Robinson projection is often described as a compromise. What does that mean in practice?",
   choices=[
     "It distorts shape, area, distance and direction moderately rather than eliminating any one of them",
     "It preserves area at the equator and shape at the poles",
     "It alternates between two projections at a standard parallel",
     "It shows only the land and omits the oceans",
     "It preserves direction from a single central point"],
   ans=0,
   why="A compromise projection accepts a little error in every property instead of holding one exact, which makes it pleasant for a general reference wall map and unsuitable for any measurement that needs a property held true."),

 dict(q="An airline planning great-circle routes out of a hub at the North Pole wants a map on which the true bearing from the hub to any destination can be read directly. Which projection is designed for that?",
   choices=[
     "A polar azimuthal projection, which preserves direction outward from its central point",
     "Mercator, which preserves the shape of every landmass",
     "Gall-Peters, which preserves area everywhere",
     "Goode's homolosine, which preserves the outlines of the continents",
     "A conic projection, which preserves distance along every meridian"],
   ans=0,
   why="Azimuthal projections hold true direction from the point of tangency outward, which is exactly the property a hub-and-spoke route map needs; the distortion grows with distance from that center, which is acceptable when everything of interest radiates from it."),

 dict(q="A state highway department maps a single county at 1:24,000. Compared with a world map at 1:50,000,000, the county map is",
   choices=[
     "Larger in scale, and therefore able to show far more detail over far less ground",
     "Smaller in scale, because the county covers less of Earth's surface",
     "Larger in scale, and therefore able to show far more ground",
     "Identical in scale, since scale describes the ratio and not the area",
     "Smaller in scale, because the denominator of the fraction is smaller"],
   ans=0,
   why="A representative fraction is a ratio, so the smaller the denominator, the larger the fraction and the larger the scale. 1/24,000 is far larger than 1/50,000,000, and the payoff for that magnification is detail at the cost of extent."),

 dict(q="Which of the following would most likely be shown on a small-scale map rather than a large-scale one?",
   choices=[
     "The distribution of the world's major language families",
     "The layout of the fire hydrants on one city block",
     "The parcel boundaries of a residential subdivision",
     "The room plan of a university library",
     "The location of every tree along a single avenue"],
   ans=0,
   why="Small scale means a large denominator, a large extent and little detail. Only a worldwide distribution needs that extent; each of the other four is a task that requires magnification of a very small area."),

 dict(q="Five counties report the population and land area below. A planner argues that a dot distribution map and a choropleth map of population density would leave very different impressions of which county is the most crowded. Which county supports her point most sharply?",
   table=dict(
     headers=["County", "Population", "Land area (square miles)"],
     rows=[
       ["Alder", "480,000", "1,200"],
       ["Birch", "150,000", "150"],
       ["Cedar", "96,000", "480"],
       ["Dogwood", "210,000", "700"],
       ["Elm", "60,000", "1,500"]]),
   choices=[
     "Birch, which has far from the largest population but by far the highest density",
     "Alder, which has both the largest population and the highest density",
     "Elm, which has the smallest population and the highest density",
     "Cedar, whose density is the highest in the table",
     "Dogwood, which has the largest land area and the largest population"],
   ans=0,
   why="A dot map shows counts, so Alder's 480,000 dominates it; a choropleth of density shows Birch at 1,000 people per square mile against Alder's 400. The county that is largest by one measure is not the densest, which is exactly the divergence the planner is describing."),

 dict(q="A cartographer must choose one of the scales below for a map that will show every building footprint in a small town. Which representative fraction is the largest scale available, and therefore the right choice?",
   table=dict(
     headers=["Option", "Representative fraction"],
     rows=[
       ["W", "1:1,000,000"],
       ["X", "1:250,000"],
       ["Y", "1:12,000"],
       ["Z", "1:100,000"]]),
   choices=[
     "Y, because 1:12,000 has the smallest denominator and so is the largest scale",
     "W, because 1:1,000,000 has the largest denominator and so is the largest scale",
     "X, because 1:250,000 falls in the middle of the range",
     "Z, because 1:100,000 is a round number and a standard series",
     "None of them, because building footprints require an equal-area projection"],
   ans=0,
   why="Scale is the fraction, not the denominator, so the option with the smallest denominator magnifies the ground most. Building footprints are a few tens of meters across and survive only at that magnification."),

 dict(q="The table gives the straight-line distance and the scheduled travel time from a regional hub to four towns. Which pairing shows most clearly that absolute and relative distance can rank places differently?",
   table=dict(
     headers=["Town", "Straight-line distance (km)", "Scheduled travel time (min)"],
     rows=[
       ["Pinehill", "40", "75"],
       ["Quarry Bay", "95", "55"],
       ["Redford", "60", "90"],
       ["Stonebridge", "120", "70"]]),
   choices=[
     "Stonebridge and Redford: Stonebridge is twice as far in kilometers yet is reached sooner",
     "Pinehill and Redford: the nearer town also takes less time, as expected",
     "Quarry Bay and Stonebridge: the farther town also takes longer, as expected",
     "Pinehill and Quarry Bay: both are reached in under an hour",
     "Redford and Quarry Bay: the two towns are the same distance from the hub"],
   ans=0,
   why="Relative distance measured in time reverses the ranking that kilometers give whenever the transport network is uneven: Stonebridge is 120 km out but 70 minutes away, while Redford is 60 km out and 90 minutes away, so a highway to one and back roads to the other decide the outcome."),

 dict(q="A dot distribution map of a province uses one dot for every 5,000 residents. The table reports the number of dots falling in each district. Which conclusion does the map support?",
   table=dict(
     headers=["District", "Dots on map", "Land area (sq km)"],
     rows=[
       ["Northvale", "18", "9,000"],
       ["Eastmoor", "44", "2,200"],
       ["Southgate", "31", "6,200"],
       ["Westbrook", "7", "3,500"]]),
   choices=[
     "Eastmoor holds 220,000 residents, the largest population and the highest density in the province",
     "Northvale holds the largest population, since it has the largest land area",
     "Westbrook holds 35,000 residents and the highest density in the province",
     "Southgate and Eastmoor hold the same number of residents",
     "The map cannot be used to compare districts, because dots are not an enumeration unit"],
   ans=0,
   why="Each dot is a stated count, so the dots convert directly: 44 dots is 220,000 people, more than any other district, and 220,000 over 2,200 square kilometers is 100 per square kilometer, also the highest. The dot value is what makes a dot map quantitative rather than merely suggestive."),
]
