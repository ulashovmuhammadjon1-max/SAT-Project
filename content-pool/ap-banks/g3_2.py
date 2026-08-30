# AP HUMAN GEOGRAPHY 3.2 Cultural Landscapes -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding PSO-3; two learning
# objectives.
#
# Essential knowledge, in full:
#   PSO-3.B.1  Cultural landscapes are combinations of physical features,
#              agricultural and industrial practices, religious and linguistic
#              characteristics, evidence of sequent occupance, and other
#              expressions of culture including traditional and postmodern
#              architecture and land-use patterns.
#   PSO-3.C.1  Attitudes toward ethnicity and gender, including the role of
#              women in the workforce; ethnic neighborhoods; and indigenous
#              communities and lands help shape the use of space in a given
#              society.
#
# PSO-3.B.1 is a long sentence and it is doing one thing: naming the ingredients
# a cultural landscape is a COMBINATION of. The list is
#   physical features
#   agricultural and industrial practices
#   religious and linguistic characteristics
#   evidence of SEQUENT OCCUPANCE
#   other expressions of culture, including traditional and postmodern
#     architecture and land-use patterns
# Items 1-4, 7, 9, 11, 15, 18 and 26 are keyed to membership in that list. The
# word COMBINATION is itself examinable: a landscape is not a single trait but
# the accumulated result of many, which is why item 2 asks about it.
#
# SEQUENT OCCUPANCE is the only technical term the statement names and the CED
# does not define it. As used throughout this module: the successive occupation
# of a place by different cultural groups, each leaving marks that survive into
# the next occupation, so the landscape holds several eras at once. Items 5, 12,
# 19, 22 and 27 turn on it, and item 12 asks for the definition directly.
#
# PSO-3.C.1 is the other half of the topic and it is easy to under-teach. It
# names three things that shape the USE OF SPACE: attitudes toward ethnicity and
# gender including women's role in the workforce, ethnic neighborhoods, and
# indigenous communities and lands. Items 13, 14, 16, 20, 21, 23, 24, 25, 28, 29
# and 30 are keyed to it. Its claim is spatial: an attitude is legible in where
# things are put and who can be where, not only in what people say.
#
# A NOTE ON VISUAL SOURCES. The suggested skill for this topic is 4.B, describe
# spatial patterns presented in VISUAL sources, and this bank carries no images.
# No stem here says "the photograph shows"; where a landscape must be examined,
# it is supplied as a real inventory table of what is present and in what
# quantity. CLAUDE.md's standing rule is that a prose description may never
# stand in for a figure, and an inventory is data rather than a description.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_2.py. FIVE choices (A-E).
TOPIC = ("3.2", "Cultural Landscapes", 3)

QUESTIONS = [
 dict(q="How does the framework describe a cultural landscape?",
   choices=[
     "A combination of physical features, agricultural and industrial practices, religious and linguistic characteristics, evidence of sequent occupance, and other expressions of culture",
     "The natural environment of a region before human settlement",
     "The artistic representation of a place in painting and photography",
     "The legal boundaries dividing a region into properties",
     "The climate and vegetation of a region"],
   ans=0,
   why="EK PSO-3.B.1 gives this list, and the operative word is combination: a cultural landscape is the accumulated result of many kinds of human activity on a physical base rather than any single feature of it."),

 dict(q="Why does the framework describe a cultural landscape as a COMBINATION rather than as a single feature?",
   choices=[
     "Any given landscape carries many different expressions of culture at once, laid over one another and over the physical base",
     "Because geographers cannot agree which feature matters most",
     "Because only combinations can be photographed",
     "Because a single feature is never visible",
     "Because the word has no particular significance"],
   ans=0,
   why="EK PSO-3.B.1 lists at least five kinds of ingredient in one sentence. Reading a landscape means separating those layers, which is only possible if they are understood to be present together rather than as alternatives."),

 dict(q="A geographer notes a region's terraced fields, its grain mills, its minarets, its bilingual road signs, and the ruined walls of an earlier settlement. Which framework category does each of the last two belong to?",
   choices=[
     "The signs are a linguistic characteristic and the ruined walls are evidence of sequent occupance",
     "Both are religious characteristics",
     "Both are physical features",
     "The signs are physical features and the walls are industrial practices",
     "Neither belongs to the framework's list"],
   ans=0,
   why="EK PSO-3.B.1 names religious and linguistic characteristics and evidence of sequent occupance as separate ingredients of a cultural landscape. Bilingual signage records what languages are used and by whom, while surviving walls record who was there before."),

 dict(q="Which of the following is a PHYSICAL feature contributing to a cultural landscape rather than an expression of culture?",
   choices=[
     "The ridge line along which a settlement is strung",
     "The style of the settlement's roofs",
     "The language of the settlement's shop signs",
     "The pattern of the settlement's field boundaries",
     "The location of the settlement's place of worship"],
   ans=0,
   why="EK PSO-3.B.1 includes physical features among the ingredients a landscape combines, and the ridge is there whether or not anyone builds on it. Roofs, signs, boundaries and places of worship are all human works placed on that base."),

 dict(q="A town shows a Roman street grid, a medieval cathedral, nineteenth-century industrial terraces, and a late twentieth-century shopping centre, all in use. This is the clearest example of",
   choices=[
     "Sequent occupance, since successive groups have each left marks that survive into the present landscape",
     "A physical feature of the site",
     "A purely postmodern landscape",
     "An indigenous cultural landscape",
     "An ethnic neighbourhood"],
   ans=0,
   why="EK PSO-3.B.1 names evidence of sequent occupance among the ingredients of a cultural landscape. What makes this the clearest case is that four eras are legible at once rather than the earlier ones having been erased."),

 dict(q="Which pairing correctly matches a landscape feature to the framework category it belongs to?",
   choices=[
     "Rows of blast furnaces and rail sidings, matched to industrial practices",
     "A river's floodplain, matched to religious characteristics",
     "A cemetery's headstone inscriptions, matched to physical features",
     "A hedge-bounded field system, matched to linguistic characteristics",
     "A shopping mall's glass facade, matched to sequent occupance"],
   ans=0,
   why="EK PSO-3.B.1 names agricultural and industrial practices among the ingredients of a cultural landscape, and furnaces with rail sidings are the industrial case. Each of the other pairings attaches a feature to a category it does not belong to."),

 dict(q="Why can a place of worship be read as evidence about a cultural landscape even by someone who does not share the religion?",
   choices=[
     "Its size, site, orientation, and prominence record what the society that built it considered important enough to organize space around",
     "Religious buildings are the only features that survive",
     "Religious buildings are physical rather than cultural features",
     "Its meaning can only be understood by adherents",
     "It carries no information about the surrounding landscape"],
   ans=0,
   why="EK PSO-3.B.1 names religious characteristics among the ingredients of a cultural landscape, and what a landscape records is the decision rather than the belief. Where a building is placed and how much of the settlement defers to it are observable facts."),

 dict(q="A region's landscape contains grain silos, irrigation canals, and machinery sheds. Which framework category do these belong to?",
   choices=[
     "Agricultural practices, one of the ingredients the framework lists",
     "Religious characteristics",
     "Sequent occupance",
     "Physical features",
     "Linguistic characteristics"],
   ans=0,
   why="EK PSO-3.B.1 names agricultural and industrial practices together as one of the ingredients a cultural landscape combines. Silos, canals and sheds are the physical apparatus of a way of farming, and they record which way that is."),

 dict(q="What does the framework mean by including 'traditional and postmodern architecture' among expressions of culture?",
   choices=[
     "Both inherited building forms and deliberately contemporary ones are cultural expressions and appear in the same landscape",
     "Only traditional architecture counts as cultural",
     "Only postmodern architecture counts as cultural",
     "Architecture is a physical rather than a cultural feature",
     "The two styles cannot appear in the same place"],
   ans=0,
   why="EK PSO-3.B.1 names both explicitly and puts them in one clause. A landscape is not made cultural by being old, and a glass tower records the values of its moment exactly as a courtyard house records those of its own."),

 dict(q="Which observation would best indicate sequent occupance in a rural landscape?",
   choices=[
     "Field boundaries following one survey system overlaid by roads following an entirely different one",
     "A single uniform field pattern across the whole district",
     "A river running through the district",
     "A recently built grain store",
     "A district in which every farm is the same size"],
   ans=0,
   why="Sequent occupance shows as incongruity: two organizing systems present at once because a later group imposed its own without erasing the earlier one. A uniform pattern is evidence of one occupation rather than several."),

 dict(q="Which framework statement covers the observation that a neighbourhood's shops, signage, and places of worship all serve one migrant-origin community?",
   choices=[
     "That ethnic neighbourhoods help shape the use of space in a given society",
     "That cultural landscapes contain physical features",
     "That landscapes show evidence of sequent occupance",
     "That agricultural practices are part of a landscape",
     "That architecture may be traditional or postmodern"],
   ans=0,
   why="EK PSO-3.C.1 names ethnic neighborhoods explicitly among the things that shape the use of space. The concentration is not merely demographic: it reorganizes what businesses, institutions and signage occupy a district."),

 dict(q="Sequent occupance is best defined as",
   choices=[
     "The successive occupation of a place by different cultural groups, each leaving marks that persist into later periods",
     "The migration of a single group between several places",
     "The replacement of one landscape by a completely new one",
     "The natural succession of vegetation on abandoned land",
     "The division of a landscape among several owners at one time"],
   ans=0,
   why="EK PSO-3.B.1 names evidence of sequent occupance without defining it, and the standard definition turns on persistence. If each occupation erased the last there would be nothing to observe; what makes it visible is that the earlier layers survive."),

 dict(q="A society in which few women work outside the home builds most of its shops within walking distance of housing, while one with high female employment builds larger stores near workplaces and transport. Which framework statement does this illustrate?",
   choices=[
     "That attitudes toward gender, including the role of women in the workforce, help shape the use of space",
     "That agricultural practices shape landscapes",
     "That sequent occupance shapes landscapes",
     "That physical features shape landscapes",
     "That linguistic characteristics shape landscapes"],
   ans=0,
   why="EK PSO-3.C.1 names attitudes toward gender and the role of women in the workforce among the things shaping the use of space. Where shops are put follows from when and how people can reach them, which follows from who is working where."),

 dict(q="A state recognizes an indigenous community's title to a large area and its right to govern land use there. What is the geographic consequence?",
   choices=[
     "The use of that space is organized by the community's own priorities rather than by the surrounding society's, producing a visibly different landscape",
     "The area's physical geography changes",
     "The area ceases to be part of the country",
     "The area's landscape becomes identical to the surrounding one",
     "There is no geographic consequence, since recognition is a legal matter"],
   ans=0,
   why="EK PSO-3.C.1 names indigenous communities and lands among the things shaping the use of space in a society. Who decides how land is used is what determines what appears on it, so a change in that authority is a change in the landscape over time."),

 dict(q="Which of these features would tell a geographer most about a region's LINGUISTIC characteristics?",
   choices=[
     "The languages appearing on shop fronts, street signs, and gravestones",
     "The pitch of the region's roofs",
     "The size of the region's fields",
     "The elevation of the region's settlements",
     "The number of factories in the region"],
   ans=0,
   why="EK PSO-3.B.1 names linguistic characteristics among the ingredients of a cultural landscape. Public writing is where language becomes visible in space, and the choice of which language appears where records status as well as usage."),

 dict(q="A city's older districts have wide sidewalks, corner shops, and mixed housing, while newer districts have cul-de-sacs, garages, and separate commercial zones. What does the contrast most directly record?",
   choices=[
     "Different assumptions about how households move, work, and shop, expressed as land-use patterns",
     "A change in the region's physical geography",
     "A change in the region's religion",
     "A change in the region's language",
     "Nothing cultural, since layouts are engineering decisions"],
   ans=0,
   why="EK PSO-3.B.1 names land-use patterns among the expressions of culture a landscape combines. A street layout encodes what its designers assumed about cars, work and daily life, which is why layouts change when those assumptions do."),

 dict(q="Why is a cultural landscape sometimes described as a record that no one set out to write?",
   choices=[
     "It accumulates from countless separate decisions, each made for its own reasons, and preserves them together",
     "Because landscapes are made only by governments",
     "Because landscapes are natural rather than human",
     "Because it is written down in documents",
     "Because only one group ever shapes a landscape"],
   ans=0,
   why="EK PSO-3.B.1 makes a landscape a combination of many ingredients, and nobody combines them deliberately. Each field boundary, roof and sign was placed by someone pursuing their own end, and the assemblage records a society that no one intended to describe."),

 dict(q="Which framework category do abandoned mine headframes, spoil heaps, and a disused rail line belong to?",
   choices=[
     "Industrial practices, and also evidence of sequent occupance if a later use has been built around them",
     "Physical features only",
     "Religious characteristics",
     "Linguistic characteristics",
     "None of the framework's categories"],
   ans=0,
   why="EK PSO-3.B.1 names industrial practices and evidence of sequent occupance as separate ingredients, and disused industrial works can be both at once. A single feature belonging to two categories is what the word combination in that statement allows for."),

 dict(q="A district's landscape is largely unchanged for two centuries and then substantially rebuilt within a decade. Which reading is best supported?",
   choices=[
     "A change in who holds the resources and authority to reshape space, since landscapes change at the speed of the decisions behind them",
     "A change in the district's physical geography",
     "A change in the district's climate",
     "That landscapes change at a constant rate everywhere",
     "That the earlier landscape was not cultural"],
   ans=0,
   why="EK PSO-3.B.1 makes the landscape an expression of culture, and expressions change when the people making them change or acquire new means. Two centuries of stability followed by a decade of rebuilding is a statement about power and capital rather than about geology."),

 dict(q="Which of the following best shows attitudes toward ETHNICITY shaping the use of space?",
   choices=[
     "Rules, whether legal or informal, that determined which groups could buy property in which districts of a city",
     "A river dividing a city into two halves",
     "A change in the city's average rainfall",
     "The construction of a new bridge",
     "An increase in the city's total population"],
   ans=0,
   why="EK PSO-3.C.1 names attitudes toward ethnicity among the things shaping the use of space. A rule about who may live where converts an attitude directly into a map, and the resulting pattern outlasts the rule by decades."),

 dict(q="A city plans a new district assuming that most adults will commute by car to a workplace and that someone will be home during the day. If female labour force participation then rises sharply, what happens?",
   choices=[
     "The district's design fits its residents' lives less well, since the layout embodies an assumption about gender roles that no longer holds",
     "The district's physical geography changes",
     "The district automatically redesigns itself",
     "Nothing changes, since layouts are independent of who lives in them",
     "The district's language changes"],
   ans=0,
   why="EK PSO-3.C.1 names the role of women in the workforce among the things shaping the use of space. A built layout is durable while the assumptions behind it are not, so a change in participation leaves the district organized around a household that has stopped existing."),

 dict(q="Which observation would best distinguish a landscape shaped by sequent occupance from one shaped by a single culture over a long period?",
   choices=[
     "The presence of features organized on different and incompatible principles, dated to different periods",
     "The presence of very old features",
     "The presence of features made from local materials",
     "The presence of a large number of buildings",
     "The presence of features in good repair"],
   ans=0,
   why="Age alone shows duration rather than succession, since one culture can build over centuries. What identifies sequent occupance is incongruity: two organizing logics present at once because different groups imposed them at different times."),

 dict(q="An indigenous community's land is managed for seasonal hunting, gathering, and ceremony rather than for continuous cultivation. A visiting official records it as 'unused'. What is the error?",
   choices=[
     "The official is applying one society's categories of land use to another's, and mistaking a different use for no use",
     "The official is correct, since the land is not cultivated",
     "The land is a physical feature rather than a cultural landscape",
     "The error is only that the official did not measure the area",
     "There is no error, since land use is objectively defined"],
   ans=0,
   why="EK PSO-3.C.1 names indigenous communities and lands among the things shaping the use of space, and EK PSO-3.A.3's ethnocentrism is the attitude on display. A category built for one system of land use fails to register a different one and reports it as absence."),

 dict(q="Which is the strongest reason a geographer would examine a cemetery when studying a cultural landscape?",
   choices=[
     "Its inscriptions, symbols, languages, and spatial arrangement record religion, language, ethnicity, and status together in one place",
     "Cemeteries are the largest features in most landscapes",
     "Cemeteries are physical rather than cultural features",
     "Cemeteries are the only features that survive",
     "Cemeteries reveal nothing about the living population"],
   ans=0,
   why="EK PSO-3.B.1 names religious and linguistic characteristics among a landscape's ingredients, and a cemetery carries both at once along with dated evidence of who was there. Concentrating several categories in one readable place is what makes it efficient evidence."),

 dict(q="What does the framework's phrase 'the use of space in a given society' add to the study of cultural landscapes?",
   choices=[
     "It makes attitudes examinable through where things are placed and who may be where, rather than only through what people say",
     "It restricts the study of landscapes to urban areas",
     "It means only governments shape space",
     "It means space cannot be studied",
     "It replaces the idea of a cultural landscape entirely"],
   ans=0,
   why="EK PSO-3.C.1's claim is spatial by construction: attitudes toward ethnicity and gender shape the USE of space. That is what makes a belief a geographic object -- it can be found in a map of who lives where and what is built for whom."),

 dict(q="An inventory of visible features in one district is shown. Using the table, which framework category is best represented in this landscape?",
   table=dict(
     headers=["Feature type", "Count"],
     rows=[
       ["Places of worship of two denominations", "6"],
       ["Bilingual street signs", "42"],
       ["Grain silos and machinery sheds", "3"],
       ["Buildings dated before 1850", "11"],
       ["Buildings dated 1990 or later", "58"]]),
   choices=[
     "Linguistic characteristics, since 42 bilingual signs is the largest count of any culturally specific feature type",
     "Agricultural practices, since silos and sheds are present",
     "Religious characteristics, since two denominations are represented",
     "Physical features, since the district has a site",
     "No category, since the counts are of different kinds of thing"],
   ans=0,
   why="EK PSO-3.B.1 lists linguistic characteristics among the ingredients of a cultural landscape, and 42 bilingual signs exceeds every other culturally specific count in the table. The buildings dated by period are evidence of sequent occupance rather than of one category's prominence."),

 dict(q="Dated structures in one town are recorded by period and by whether they remain in use. Using the table, what does the pattern show?",
   table=dict(
     headers=["Period of construction", "Structures surviving", "Still in use"],
     rows=[
       ["Before 1500", "14", "9"],
       ["1500-1799", "38", "31"],
       ["1800-1939", "126", "104"],
       ["1940-2019", "310", "298"]]),
   choices=[
     "Sequent occupance, since structures from all four periods survive and most of them remain in active use",
     "A single occupation, since most structures are recent",
     "Complete replacement of each period's landscape by the next",
     "That the town was abandoned before 1500",
     "That older structures are never reused"],
   ans=0,
   why="All four periods are represented, and the share still in use runs 64, 82, 83 and 96 percent, so the earlier layers have neither been erased nor left as ruins. A landscape holding four eras simultaneously in working use is what sequent occupance produces."),

 dict(q="Retail floor space and its location are recorded for one city at two dates alongside female labour force participation. Using the table, which relationship is best supported?",
   table=dict(
     headers=["Year", "Female labour force participation (%)", "Retail floor space within 400 m of housing (%)", "Retail floor space at transport nodes and out of town (%)"],
     rows=[
       ["1970", "31", "78", "22"],
       ["2020", "67", "34", "66"]]),
   choices=[
     "As participation more than doubled, retail shifted from near housing to transport nodes, which is a gendered attitude toward space changing with the workforce",
     "Retail shifted toward housing as participation rose",
     "Participation fell while retail moved out of town",
     "Retail location and participation are unrelated in the table",
     "Both retail categories rose between the two dates"],
   ans=0,
   why="Participation rises from 31 to 67 percent while retail near housing falls from 78 to 34 and retail at transport nodes rises from 22 to 66, and each year's two retail shares sum to 100. EK PSO-3.C.1 names the role of women in the workforce among the things shaping the use of space."),

 dict(q="Business types are recorded for two adjacent districts of one city. Using the table, which district is best described as an ethnic neighbourhood?",
   table=dict(
     headers=["Business type", "District 1", "District 2"],
     rows=[
       ["Serving one origin community in its own language", "9", "84"],
       ["General retail with no community-specific signage", "121", "26"],
       ["Places of worship of the community's tradition", "1", "7"],
       ["Community associations and language schools", "0", "11"]]),
   choices=[
     "District 2, where 84 of its 128 businesses serve one community in its own language and where community institutions are concentrated",
     "District 1, which has the larger number of businesses in total",
     "District 1, because general retail is the largest single category there",
     "District 2, because it has fewer businesses than District 1",
     "Neither, since both districts contain general retail"],
   ans=0,
   why="One district records 84 of 128 businesses serving a single community in its own language, with seven places of worship and eleven community institutions, against nine, one and zero in the other. EK PSO-3.C.1 names ethnic neighborhoods among the things shaping the use of space, and this is what that shaping looks like counted."),

 dict(q="Land management on an area returned to indigenous title is compared with adjacent land under other ownership. Using the table, what is the clearest difference?",
   table=dict(
     headers=["Land use", "Indigenous-titled area (% of land)", "Adjacent freehold area (% of land)"],
     rows=[
       ["Continuous cultivation", "6", "71"],
       ["Managed burning and seasonal harvest", "58", "0"],
       ["Protected ceremonial and habitat areas", "31", "4"],
       ["Built and fenced", "5", "25"]]),
   choices=[
     "The indigenous-titled area is dominated by seasonal and protected uses that are almost absent next door, so authority over land produces a visibly different landscape",
     "The two areas are used identically",
     "The indigenous-titled area is unused",
     "The adjacent area has more protected land",
     "The difference is caused by differences in soil and climate"],
   ans=0,
   why="Both columns sum to 100, so only composition is comparable: seasonal management and protected areas hold 89 percent of one area against 4 percent of the other, while continuous cultivation runs 6 against 71. EK PSO-3.C.1 names indigenous communities and lands among the things shaping the use of space."),
]
