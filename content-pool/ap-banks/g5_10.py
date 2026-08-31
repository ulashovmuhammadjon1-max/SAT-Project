# AP HUMAN GEOGRAPHY 5.10 Consequences of Agricultural Practices -- 30 questions
# CED Course Framework V.1, Unit 5. Enduring understanding IMP-5, "Agricultural
# production and consumption patterns vary in different locations, presenting
# different environmental, social, economic, and cultural opportunities and
# challenges." Learning objective IMP-5.A, "Explain how agricultural practices
# have environmental and societal consequences."
#
# Essential knowledge -- three statements, and all three are lists:
#   IMP-5.A.1  Environmental effects of agricultural land use include pollution,
#              land cover change, desertification, soil salinization, and
#              conservation efforts.
#   IMP-5.A.2  Agricultural practices -- including slash and burn, terraces,
#              irrigation, deforestation, draining wetlands, shifting
#              cultivation, and pastoral nomadism -- alter the landscape.
#   IMP-5.A.3  Societal effects of agricultural practices include changing diets,
#              role of women in agricultural production, and economic purpose.
#
# THE ODD ENTRY ON THE FIRST LIST IS "CONSERVATION EFFORTS", and it is the
# feature of this topic most worth noticing. Pollution, land cover change,
# desertification and salinization are damage; conservation is a response. The
# CED puts all five under one heading because the statement is about the
# EFFECTS OF AGRICULTURAL LAND USE on the environment, and organized effort to
# protect soil and water is as much a consequence of farming as the erosion is.
# Items 8, 22 and 24 rest on this, and item 24 asks for it directly, because a
# student who reads the list as five kinds of damage will be baffled by the
# fifth.
#
# IMP-5.A.2 IS ABOUT THE LANDSCAPE, not about yields or economics. Its verb is
# ALTER THE LANDSCAPE, so every item keyed to it asks what a practice leaves
# visible on the ground -- terraces cut into a slope, canals and field geometry,
# a forest edge that has moved, a drained wetland's ditches, a mosaic of plots at
# different stages of regrowth, wells and tracks converging on water. Items 9 to
# 15 walk the CED's own list of seven practices, and item 20 reverses the
# reasoning by reading a practice off a landscape.
#
# IMP-5.A.3'S THIRD ENTRY, "economic purpose", is the one that needs unpacking:
# it means the purpose FOR WHICH a society farms -- to feed itself, or to sell --
# and a shift between those changes what is grown, who grows it and what happens
# to it. Item 18 keys on that. The second entry, the role of women, is Topic
# 5.12's whole subject; item 17 keys only on what IMP-5.A.3 itself asserts, which
# is that the role changes with the practice, and leaves the detail there.
#
# WHAT NO ITEM ASSERTS: that any practice is universally destructive, or that
# desertification and salinization are inevitable results of farming dry land.
# Both are outcomes of particular practices in particular conditions, and items
# 6, 7 and 23 key on the mechanism so that the conditions are part of the answer.
#
# SYNONYM CARE. `geo_check` treats {"shifting cultivation", "slash-and-burn
# agriculture", "swidden agriculture"} as one construct and {"pastoral nomadism",
# "nomadic herding"} as another. The CED's own list names slash and burn AND
# shifting cultivation separately, so where the statement is quoted they appear
# together inside a SINGLE choice rather than as two competing options.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("5.10", "Consequences of Agricultural Practices", 5)

QUESTIONS = [
 dict(q="Which set of environmental effects does the framework attribute to agricultural land use?", choices=[
   "Pollution, land cover change, desertification, soil salinization, and conservation efforts",
   "Changing diets, the role of women, and economic purpose",
   "Clustered, dispersed, and linear settlement",
   "High-yield seeds, chemicals, and mechanization",
   "Metes and bounds, township and range, and long lot"], ans=0,
   why="EK IMP-5.A.1 names exactly these five. Changing diets and economic purpose belong to EK IMP-5.A.3's societal list, and the other sets are drawn from settlement, the Green Revolution and survey methods, which are separate topics."),

 dict(q="Which set of practices does the framework name as altering the landscape?", choices=[
   "Slash and burn, terraces, irrigation, deforestation, draining wetlands, shifting cultivation, and pastoral nomadism",
   "Pollution, desertification, and soil salinization",
   "Changing diets, the role of women, and economic purpose",
   "Rank-size rule, primate city, and central place theory",
   "Market gardening, plantation agriculture, and ranching"], ans=0,
   why="EK IMP-5.A.2 names exactly this list of practices and says they alter the landscape. The second option names effects rather than practices, and the others belong to different statements in the course."),

 dict(q="Which three societal effects of agricultural practices does the framework name?", choices=[
   "Changing diets, the role of women in agricultural production, and economic purpose",
   "Pollution, desertification, and soil salinization",
   "Terraces, irrigation, and draining wetlands",
   "Land cover change, conservation efforts, and salinization",
   "Changing diets, rising rents, and falling birth rates"], ans=0,
   why="EK IMP-5.A.3 names exactly these three societal effects. The environmental effects belong to EK IMP-5.A.1 and the landscape-altering practices to EK IMP-5.A.2, so this statement is the only one of the three concerned with people rather than with land."),

 dict(q="By what route does farming most commonly pollute water?", choices=[
   "Fertilizer and pesticide applied to fields is carried off them by rain and irrigation water into streams and groundwater",
   "Farm machinery is washed in rivers",
   "Crops absorb clean water and release polluted water",
   "Farms discharge treated sewage directly into rivers",
   "Farming affects only air quality and never water"], ans=0,
   why="EK IMP-5.A.1 names pollution first among the environmental effects of agricultural land use. What makes agricultural pollution distinctive is that it is diffuse: it leaves a whole surface rather than a pipe, which is why it is so hard to regulate or trace."),

 dict(q="What does the framework mean by land cover change as an effect of agricultural land use?", choices=[
   "The vegetation covering an area is replaced -- forest or grassland becomes cropland or pasture -- which changes the surface over large areas",
   "The ownership of the land changes hands",
   "The land's political boundaries are redrawn",
   "The land is surveyed by a different method",
   "The land's elevation is altered"], ans=0,
   why="EK IMP-5.A.1 names land cover change among the environmental effects of agricultural land use. Cover is what is physically on the surface, which is why the change is visible from satellites and why it affects water, soil and habitat together."),

 dict(q="What is desertification, and how do agricultural practices contribute to it?", choices=[
   "The degradation of dry land until it can no longer support the vegetation it once did, driven partly by overgrazing and cultivation beyond what the land can sustain",
   "The natural expansion of deserts, to which farming contributes nothing",
   "The conversion of desert into farmland by irrigation",
   "The salting of soil by irrigation water",
   "The replacement of grassland with forest"], ans=0,
   why="EK IMP-5.A.1 names desertification among the environmental effects of agricultural land use, which attributes a role to farming without making it the only cause. Removing vegetation faster than dry land can regrow it exposes the soil, and the soil then blows or washes away."),

 dict(q="How does agricultural practice produce soil salinization?", choices=[
   "Irrigation water carries dissolved salts, and where it evaporates rather than draining away the salt is left behind and accumulates",
   "Fertilizer is manufactured from common salt",
   "Salt is blown onto fields from the sea in all inland regions",
   "Crops excrete salt into the soil as they grow",
   "Ploughing brings buried salt deposits to the surface everywhere"], ans=0,
   why="EK IMP-5.A.1 names soil salinization among the environmental effects of agricultural land use. The salt is already dissolved in the water applied; what farming supplies is the repeated evaporation that concentrates it in the root zone until crops fail."),

 dict(q="Why does the framework list CONSERVATION EFFORTS alongside pollution, land cover change, desertification and salinization?", choices=[
   "Because the statement covers the effects of agricultural land use on the environment, and organized effort to protect soil and water is as much a consequence of farming as the damage is",
   "Because conservation efforts are a form of pollution",
   "Because conservation efforts have never actually occurred",
   "Because the list was intended to contain only harms and this entry is an error",
   "Because conservation is the only environmental effect that matters"], ans=0,
   why="EK IMP-5.A.1 puts all five under one heading, and four of them are damage while the fifth is a response to it. Reading the statement as a list of harms makes the last entry incomprehensible; reading it as a list of consequences makes it obvious."),

 dict(q="How do terraces alter a landscape, and what problem do they solve?", choices=[
   "They cut a slope into a stair of level platforms, which slows runoff and holds soil that would otherwise wash downhill",
   "They raise the elevation of a hillside",
   "They drain water away from a slope as fast as possible",
   "They convert a slope into a single flat field",
   "They have no visible effect on a landscape"], ans=0,
   why="EK IMP-5.A.2 names terraces among the practices that alter the landscape. A level surface holds water long enough for it to soak in rather than run off, which is why terracing is both a landscape alteration and a soil-conservation practice."),

 dict(q="How does irrigation alter a landscape beyond the fields it waters?", choices=[
   "Canals, ditches, reservoirs and the geometry of fields laid out to receive water become permanent features, and the river or aquifer supplying them is drawn down",
   "It has effects only within the irrigated field itself",
   "It changes the region's underlying geology",
   "It removes the need for any field boundaries",
   "It leaves no trace once the season ends"], ans=0,
   why="EK IMP-5.A.2 names irrigation among the practices that alter the landscape. Delivering water requires a built network that outlasts any one crop, and taking water from a river or an aquifer alters the place the water came from as well as the place it goes."),

 dict(q="A forest edge in a farming district moves steadily outward over forty years. Which practice from the framework's list does this record?", choices=[
   "Deforestation, since land under forest is being converted to agricultural use",
   "Terracing, since the slope is being modified",
   "Salinization, since the soil is changing",
   "Pastoral nomadism, since the land is being used",
   "Conservation, since the forest is being managed"], ans=0,
   why="EK IMP-5.A.2 names deforestation among the practices that alter the landscape and EK IMP-5.A.1 names land cover change among the environmental effects. A moving forest edge is the visible boundary between the two land covers, which is why it can be measured from imagery."),

 dict(q="What does draining a wetland for agriculture change beyond making the land cultivable?", choices=[
   "The area loses its capacity to store floodwater and to support the species that depended on standing water",
   "The area's climate becomes tropical",
   "The area's soil becomes permanently saline",
   "Nothing else changes, since only the water is removed",
   "The area becomes unsuitable for any crop"], ans=0,
   why="EK IMP-5.A.2 names draining wetlands among the practices that alter the landscape. A wetland performs functions besides occupying space -- holding water back, filtering it, supporting particular species -- and draining it ends all of them at once."),

 dict(q="What visible pattern does shifting cultivation leave on a landscape?", choices=[
   "A mosaic of plots at different stages of clearing, cropping and regrowth, changing position over the years",
   "A permanent grid of identical rectangular fields",
   "A single continuously cropped field of great size",
   "Terraced slopes rising in steps",
   "No visible pattern of any kind"], ans=0,
   why="EK IMP-5.A.2 names shifting cultivation among the practices that alter the landscape. Because plots are used and rested in rotation, at any moment the district holds ground at every stage of the cycle at once, which is what makes the pattern a mosaic rather than a field."),

 dict(q="How does pastoral nomadism alter the landscape it moves across?", choices=[
   "Grazing pressure, tracks and the wells and watering points herds converge on leave a visible imprint even though no field is cultivated",
   "It leaves no imprint at all, since no ground is broken",
   "It terraces the slopes the herds cross",
   "It converts grassland permanently into forest",
   "It drains the wetlands the herds pass through"], ans=0,
   why="EK IMP-5.A.2 names pastoral nomadism among the practices that alter the landscape, which is a claim worth noticing because the practice grows nothing. Water is the scarce thing in the environments where it occurs, so the imprint concentrates wherever the herds must come to drink."),

 dict(q="What does a slash-and-burn clearing do to the soil in the first seasons after it is made?", choices=[
   "The ash returns nutrients to the surface, which raises fertility briefly before rain and cropping remove it again",
   "It permanently enriches the soil for many decades",
   "It makes the soil saline",
   "It has no effect on soil fertility",
   "It converts the soil to bare rock immediately"], ans=0,
   why="EK IMP-5.A.2 names slash and burn among the practices that alter the landscape. Burning transfers nutrients held in standing vegetation onto the ground, and where rainfall leaches heavily that transfer is short-lived, which is what makes the practice a cycle rather than a settlement."),

 dict(q="A society's diet shifts over two generations from mostly cereals and roots toward more meat, dairy, oils and processed foods. Which framework statement covers this?", choices=[
   "That the societal effects of agricultural practices include changing diets",
   "That agricultural practices alter the landscape",
   "That environmental effects include soil salinization",
   "That rural settlement patterns are clustered, dispersed, or linear",
   "That agricultural production regions are defined by climate"], ans=0,
   why="EK IMP-5.A.3 names changing diets first among the societal effects of agricultural practices. What a society eats follows from what its agriculture produces and buys, so a change in production reaches the table as surely as it reaches the market."),

 dict(q="What does the framework assert about the role of women in agricultural production?", choices=[
   "That it is among the societal effects of agricultural practices, so it changes as those practices change",
   "That it is identical in every society and every period",
   "That women take no part in agricultural production",
   "That it is an environmental rather than a societal effect",
   "That it depends only on climate"], ans=0,
   why="EK IMP-5.A.3 names the role of women in agricultural production among the societal effects of agricultural practices. Placing it on that list is itself the claim: the role is a consequence of how a society farms rather than a fixed feature of it."),

 dict(q="What does the framework's societal effect called ECONOMIC PURPOSE refer to?", choices=[
   "The purpose for which a society farms -- to feed itself or to sell -- which changes what is grown, who grows it, and where the output goes",
   "The total value of a country's agricultural exports",
   "The price a farmer receives for a crop",
   "The cost of agricultural machinery",
   "The area of land under cultivation"], ans=0,
   why="EK IMP-5.A.3 names economic purpose among the societal effects of agricultural practices. A shift from growing food to eat toward growing crops to sell reorganizes the household's labour, its diet and its exposure to prices, which is why the CED counts it as a societal effect rather than a merely economic one."),

 dict(q="At which two scales must the environmental effects the framework names be examined?", choices=[
   "At the field or district scale, where a terrace or a salinized plot is visible, and at the regional or global scale, where land cover change is measured across whole basins",
   "At the global scale only, since the environment is global",
   "At the field scale only, since farming happens in fields",
   "At no scale, since environmental effects are not spatial",
   "At the household scale only, since households farm"], ans=0,
   why="EK IMP-5.A.1 names effects that range from a salinized field to land cover change across a region. The same practice repeated across thousands of holdings becomes a regional change, so the two scales record the same process at different resolutions."),

 dict(q="A geographer sees stepped platforms cut into steep hillsides, stone-lined channels running along the contours, and small level plots. What does this landscape record?", choices=[
   "Terracing and irrigation, practices the framework names among those that alter the landscape",
   "Pastoral nomadism and shifting cultivation",
   "Deforestation and the draining of wetlands",
   "Salinization and desertification",
   "A township and range survey"], ans=0,
   why="EK IMP-5.A.2 names terraces and irrigation among the practices that alter the landscape, and both leave permanent constructed features. Reading a practice from what it built is the reverse of the reasoning the statement sets out, and it is what a cultural landscape allows."),

 dict(q="Which of the framework's environmental effects is hardest to reverse once it has occurred, and why?", choices=[
   "Desertification, because the vegetation and the soil that supported it are both lost, and rebuilding soil takes far longer than removing it",
   "Pollution, because water can never be cleaned",
   "Land cover change, because forests cannot be replanted at all",
   "Conservation efforts, because they cannot be undone",
   "All four are equally and immediately reversible"], ans=0,
   why="EK IMP-5.A.1 names desertification among the environmental effects of agricultural land use. Soil forms over centuries and can be lost in years, so a degraded dry landscape cannot be restored on the timescale over which it was damaged."),

 dict(q="Which set of practices would count as conservation efforts in the framework's sense?", choices=[
   "Contour ploughing, cover crops, reduced tillage, and vegetated buffer strips beside watercourses",
   "Deep ploughing of steep slopes and removal of hedgerows",
   "Increasing fertilizer application above what the crop can use",
   "Draining remaining wetlands for cultivation",
   "Grazing dry rangeland beyond what its grass can support"], ans=0,
   why="EK IMP-5.A.1 names conservation efforts among the environmental effects of agricultural land use. Each of the practices in the keyed set works by keeping soil and water where they are, which is the direct answer to the erosion, runoff and pollution the same statement lists."),

 dict(q="Describe the sequence by which grazing pressure can lead to desertification in a dry region.", choices=[
   "Vegetation is removed faster than it regrows, bare soil is exposed to wind and rain, the soil is lost, and the land can no longer support the plants that held it",
   "Grazing adds nutrients, which causes plants to grow too quickly and die",
   "Herds compact the soil, which raises the water table until the land floods",
   "Grazing has no relationship to desertification of any kind",
   "Animals eat the soil directly, leaving bare rock"], ans=0,
   why="EK IMP-5.A.1 names desertification among the environmental effects of agricultural land use. Each step in the chain follows from the one before, and the important feature is that the last step makes the first step's damage permanent, since without plants there is nothing to hold the soil."),

 dict(q="A student says the framework's environmental list is a list of five kinds of damage. What is the correction?", choices=[
   "Four of the five are damage and the fifth, conservation efforts, is a response to it, since the statement lists effects rather than harms",
   "All five are indeed kinds of damage",
   "None of the five is damage",
   "The list contains six items rather than five",
   "The list concerns societal rather than environmental effects"], ans=0,
   why="EK IMP-5.A.1 lists pollution, land cover change, desertification, soil salinization AND conservation efforts under one heading. The heading is environmental effects of agricultural land use, and a deliberate effort to protect soil and water is an effect of farming in exactly the same sense."),

 dict(q="Which pairing of a practice with what it leaves on the landscape is CORRECT?", choices=[
   "Draining wetlands, matched to a network of ditches across formerly waterlogged ground",
   "Terracing, matched to a mosaic of plots at different stages of regrowth",
   "Shifting cultivation, matched to stone platforms cut into a slope",
   "Irrigation, matched to a forest edge that has moved outward",
   "Deforestation, matched to salt crusts on the soil surface"], ans=0,
   why="EK IMP-5.A.2 names seven practices and says they alter the landscape, each in its own way. Only one pairing here matches a practice to the feature it actually produces; the others swap the traces of two of the CED's own listed practices."),

 dict(q="Land cover in one river basin is recorded below. Using the accompanying figures, what has occurred?",
   table=dict(headers=["Land cover", "Share of the basin in 1985 (%)", "Share of the basin in 2020 (%)"],
     rows=[["Forest", "62", "31"],
           ["Cropland", "21", "48"],
           ["Pasture", "12", "17"],
           ["Other", "5", "4"]]),
   choices=[
   "Forest fell from 62 to 31 percent of the basin while cropland and pasture together rose from 33 to 65 percent, which is land cover change driven by agricultural expansion",
   "Forest and cropland both fell across the period",
   "The basin's total area halved between the two dates",
   "Pasture fell while forest rose",
   "No change occurred, since the shares still sum to 100"], ans=0,
   why="Both columns sum to 100, so the record is about composition, and forest halves from 62 to 31 percent while cropland and pasture together rise from 33 to 65. EK IMP-5.A.1 names land cover change among the environmental effects of agricultural land use, and this is that effect measured directly."),

 dict(q="Water quality at four points along one river is recorded below. Using the accompanying figures, what does the record support?",
   table=dict(headers=["Sampling point", "Position", "Nitrate (milligrams per litre)", "Dissolved oxygen (milligrams per litre)"],
     rows=[["Point 1", "Above all farmland", "1.2", "9.1"],
           ["Point 2", "Below scattered farms", "6.8", "7.2"],
           ["Point 3", "Below intensively farmed land", "14.5", "4.3"],
           ["Point 4", "In the estuary", "11.9", "3.8"]]),
   choices=[
   "Nitrate rises more than tenfold from above the farmland to below the intensively farmed land while dissolved oxygen more than halves, which is the pollution the framework attributes to agricultural land use",
   "Nitrate and dissolved oxygen rise together downstream",
   "Nitrate is highest above all farmland",
   "Dissolved oxygen is lowest at the point above the farmland",
   "The record shows no change along the river"], ans=0,
   why="Nitrate rises from 1.2 to 14.5 milligrams per litre between the point above the farmland and the point below the intensively farmed land, more than a tenfold increase, while dissolved oxygen falls from 9.1 to 4.3. EK IMP-5.A.1 names pollution among the environmental effects of agricultural land use, and the two columns move in the pattern nutrient enrichment produces."),

 dict(q="The composition of one country's food energy supply at two dates is recorded below. Using the accompanying figures, which of the framework's societal effects does this record?",
   table=dict(headers=["Food group", "Share of food energy in 1970 (%)", "Share of food energy in 2020 (%)"],
     rows=[["Cereals and roots", "74", "51"],
           ["Animal products", "9", "22"],
           ["Oils and sugars", "12", "21"],
           ["Other", "5", "6"]]),
   choices=[
   "Changing diets, since cereals and roots fall from 74 to 51 percent of food energy while animal products and oils and sugars together rise from 21 to 43 percent",
   "Soil salinization, since agriculture has intensified",
   "Land cover change, since more food is being produced",
   "Desertification, since diets have altered",
   "No effect the framework names, since diet is a personal matter"], ans=0,
   why="Both columns sum to 100, so this is a change in composition, and the staple share falls by 23 points while animal products and oils and sugars together gain 22. EK IMP-5.A.3 names changing diets first among the societal effects of agricultural practices, and it is the only one of the framework's categories the record measures."),

 dict(q="What limitation should be stated when using water-quality readings along one river to demonstrate agricultural pollution?", choices=[
   "The readings show where concentrations rise but not that farming alone caused it, since settlements and industry may also discharge along the same reach",
   "Water quality cannot be measured in a river",
   "Concentrations and positions cannot appear in one record",
   "A rise between two points always proves its own cause",
   "The framework forbids the use of measurements in this topic"], ans=0,
   why="EK IMP-5.A.1 names pollution among the environmental effects of agricultural land use without claiming farming is the only source. Diffuse agricultural runoff is genuinely hard to separate from other discharges along the same stretch, which is exactly why the reading has to be stated as consistent rather than conclusive."),

 dict(q="A revision guide must state what this topic's three statements establish between them. Which statement does so accurately?", choices=[
   "Farming changes the environment, including through conservation as well as damage; named practices leave visible marks on the landscape; and it changes diets, the role of women, and the purpose for which a society farms",
   "Farming changes the environment but has no societal consequences",
   "Farming changes society but leaves the landscape unaltered",
   "The framework lists only harmful environmental effects of farming",
   "Agricultural practices affect only the fields on which they are carried out"], ans=0,
   why="EK IMP-5.A.1 supplies the environmental effects including conservation, EK IMP-5.A.2 the practices that alter the landscape, and EK IMP-5.A.3 the three societal effects. Each rejected summary drops one of the three statements or reads the first list as containing damage alone."),
]
