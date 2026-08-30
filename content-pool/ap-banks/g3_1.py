# AP HUMAN GEOGRAPHY 3.1 Introduction to Culture -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding PSO-3, "Cultural
# practices vary across geographical locations because of physical geography and
# available resources." Learning objective PSO-3.A, "Define the characteristics,
# attitudes, and traits that influence geographers when they study culture."
#
# Essential knowledge, in full -- three statements:
#   PSO-3.A.1  Culture comprises the shared practices, technologies, attitudes,
#              and behaviors transmitted by a society.
#   PSO-3.A.2  Culture traits include such things as food preferences,
#              architecture, and land use.
#   PSO-3.A.3  Cultural relativism and ethnocentrism are different attitudes
#              toward cultural difference.
#
# PSO-3.A.1 is a definition and every word of it is doing work. SHARED rules out
# an individual's habit; TRANSMITTED rules out anything biological or invented
# afresh each generation; and the four nouns -- practices, technologies,
# attitudes, behaviors -- are broad enough to cover tools and beliefs alike.
# Items 1, 2, 3, 5, 9, 13 and 19 turn on one of those three words, because a
# student who can quote the sentence and not apply it has learned nothing.
#
# PSO-3.A.2's three examples are introduced with "such things as", so the list
# is ILLUSTRATIVE rather than closed. Items keyed to it say a trait is a trait
# because it is a shared, transmitted element of culture, not because it appears
# on the CED's list of three; asserting a closed list would misread the
# sentence.
#
# PSO-3.A.3 names the two attitudes and does not define them, so the definitions
# every key rests on are:
#   ethnocentrism        judging another culture by the standards of one's own,
#                        and usually finding it inferior
#   cultural relativism  understanding a practice in the context of the culture
#                        it belongs to, on that culture's own terms
# The pair is an axis of ATTITUDE, not of fact: neither is a claim about what a
# culture is, and item 21 makes that explicit because students reliably read
# relativism as "all practices are equally good", which is a different and much
# stronger claim the CED does not make.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_1.py. FIVE choices (A-E).
TOPIC = ("3.1", "Introduction to Culture", 3)

QUESTIONS = [
 dict(q="How does the framework define culture?",
   choices=[
     "The shared practices, technologies, attitudes, and behaviors transmitted by a society",
     "The artistic achievements of a society, such as its literature and music",
     "The physical environment in which a society lives",
     "The genetic inheritance shared by members of a group",
     "The government and legal system of a country"],
   ans=0,
   why="EK PSO-3.A.1 gives this definition word for word. It is deliberately broad, covering tools and beliefs alike, and its two load-bearing words are shared and transmitted, which exclude an individual's private habit and anything inherited biologically."),

 dict(q="A geographer says that a practice is cultural only if it is TRANSMITTED. What does this exclude?",
   choices=[
     "Anything inherited biologically or reinvented independently by each generation without being taught",
     "Anything practised by more than one person",
     "Anything that changes over time",
     "Anything involving technology",
     "Anything found in more than one country"],
   ans=0,
   why="EK PSO-3.A.1 makes transmission part of the definition of culture. What passes from one generation to the next by teaching, imitation and participation is cultural; what each individual arrives at unaided, or inherits in their body, is not."),

 dict(q="Which of the following is NOT a culture trait in the framework's sense?",
   choices=[
     "An individual's private preference that they have never told anyone about and no one else holds",
     "A regional preference for a particular staple grain",
     "A characteristic style of roof construction in a district",
     "A customary way of dividing farmland among heirs",
     "A widely observed festival marking the end of the harvest"],
   ans=0,
   why="EK PSO-3.A.1 makes culture the SHARED practices, technologies, attitudes and behaviors of a society. A preference held by one person and communicated to no one fails the sharing test, while the other four are held in common and passed on."),

 dict(q="The framework introduces its examples of culture traits with the words 'such things as'. What follows from that phrasing?",
   choices=[
     "The list of food preferences, architecture, and land use is illustrative rather than exhaustive",
     "Only those three things count as culture traits",
     "Those three things are the most important culture traits",
     "The list applies only to rural societies",
     "The phrase has no significance"],
   ans=0,
   why="EK PSO-3.A.2 writes 'include such things as', which introduces examples rather than a definition by enumeration. Language, dress, kinship, music and burial practice are all culture traits although none of them appears in the sentence."),

 dict(q="Which of the following best illustrates a culture trait expressed in LAND USE?",
   choices=[
     "A region's characteristic pattern of terraced hillside fields worked by extended families",
     "A region's annual rainfall total",
     "A region's elevation above sea level",
     "A region's underlying rock type",
     "A region's latitude"],
   ans=0,
   why="EK PSO-3.A.2 names land use among its examples of culture traits, and what makes it cultural is that it records a society's decisions about how to work the land. Rainfall, elevation, geology and latitude are physical conditions those decisions respond to rather than traits themselves."),

 dict(q="A visitor describes a society's funeral customs as 'strange and backward' by comparison with their own. This attitude is",
   choices=[
     "Ethnocentrism, since another culture is being judged by the standards of the visitor's own",
     "Cultural relativism, since the visitor has noticed a difference",
     "A culture trait of the society being described",
     "A neutral geographic observation",
     "Cultural transmission, since the visitor will report what they saw"],
   ans=0,
   why="EK PSO-3.A.3 names ethnocentrism and cultural relativism as two attitudes toward cultural difference. Applying one's own standards to another society's practice and finding it wanting is exactly what the first of the two names."),

 dict(q="A researcher explains a society's funeral customs by reference to that society's own beliefs about death, kinship, and obligation, without ranking them against her own. This approach is",
   choices=[
     "Cultural relativism, since the practice is understood in the context of the culture it belongs to",
     "Ethnocentrism, since the researcher has her own culture",
     "Cultural transmission, since beliefs are passed on",
     "A culture trait of the researcher's society",
     "An economic rather than a cultural analysis"],
   ans=0,
   why="EK PSO-3.A.3 pairs cultural relativism with ethnocentrism as attitudes toward difference. Relativism is a method of understanding: it asks what a practice means inside the system it belongs to before any judgement is made about it."),

 dict(q="Which statement about cultural relativism is most accurate?",
   choices=[
     "It is an approach to understanding practices in their own context, not a claim that every practice is equally desirable",
     "It is the claim that all cultural practices are equally good",
     "It is the claim that cultures never change",
     "It is the same attitude as ethnocentrism under a different name",
     "It is the claim that no culture can be studied by an outsider"],
   ans=0,
   why="EK PSO-3.A.3 calls it an ATTITUDE toward cultural difference, which is a stance toward understanding rather than a moral verdict. Reading it as the stronger claim that nothing can be criticized is the most common misunderstanding of the term."),

 dict(q="A society's tools, techniques, and machinery are included in the framework's definition of culture. Why?",
   choices=[
     "The definition names technologies alongside practices, attitudes, and behaviors as things a society shares and transmits",
     "Technology is the only part of culture that can be observed",
     "Technology determines all other parts of culture",
     "Technology is a physical rather than a cultural feature",
     "Technology is included only when it is traditional"],
   ans=0,
   why="EK PSO-3.A.1 lists technologies as one of the four things culture comprises. A tool is knowledge made physical: it must be learned, taught and maintained, which is exactly what makes it shared and transmitted."),

 dict(q="Two neighbouring valleys with almost identical climates and soils grow different staple crops and build houses of different materials. What does this show?",
   choices=[
     "Physical conditions constrain what is possible without determining what a society chooses, so culture varies where environment does not",
     "One of the two valleys must have a different climate after all",
     "Culture is determined entirely by the physical environment",
     "The two valleys have identical cultures",
     "Crops and building materials are not culture traits"],
   ans=0,
   why="PSO-3's enduring understanding says cultural practices vary because of physical geography and available resources, which is a claim about influence rather than about determination. Identical environments producing different traits is what shows the remaining variation is cultural."),

 dict(q="A geographer catalogues a region's dietary staples, house forms, field patterns, dialect, and festival calendar. She is compiling",
   choices=[
     "A set of culture traits, each of which is a shared and transmitted element of that society's way of life",
     "A physical geography of the region",
     "A demographic profile of the region",
     "An economic account of the region",
     "A political history of the region"],
   ans=0,
   why="EK PSO-3.A.2 offers food preferences, architecture and land use as examples of culture traits, and every item on the list is a shared practice passed between generations. That is what makes the catalogue cultural rather than physical or demographic."),

 dict(q="Why does the framework treat attitudes as part of culture rather than as a separate matter?",
   choices=[
     "Attitudes are learned from other members of a society and passed on, which is what makes them cultural rather than individual",
     "Attitudes cannot be observed and are therefore assumed",
     "Attitudes are the only part of culture that changes",
     "Attitudes are biological in origin",
     "Attitudes are included only when a society writes them down"],
   ans=0,
   why="EK PSO-3.A.1 names attitudes alongside practices, technologies and behaviors as things a society shares and transmits. A belief about what is respectful, edible or shameful is taught in exactly the way a technique is."),

 dict(q="A visitor refuses food offered by a host because they consider the host's cuisine unclean, without asking what it is or how it is prepared. This is best described as",
   choices=[
     "Ethnocentrism operating through a food preference, which the framework names as an example of a culture trait",
     "Cultural relativism, since the visitor recognized a difference",
     "A physical rather than a cultural response",
     "Cultural transmission from host to visitor",
     "A neutral personal preference with no cultural content"],
   ans=0,
   why="EK PSO-3.A.2 names food preferences among culture traits and EK PSO-3.A.3 names ethnocentrism as an attitude toward difference. Judging without inquiry is what distinguishes the ethnocentric response from a personal dislike."),

 dict(q="A society's building styles change as new materials become available but continue to follow inherited rules about which rooms face which direction. What does this illustrate?",
   choices=[
     "Culture traits can change in their material form while the transmitted rules organizing them persist",
     "Culture never changes once established",
     "Architecture is not a culture trait",
     "Only new buildings count as cultural",
     "The society has abandoned its culture"],
   ans=0,
   why="EK PSO-3.A.1 makes transmission the defining mechanism, and what is transmitted here is the rule rather than the material. EK PSO-3.A.2 names architecture as a culture trait, and the trait survives a change in the substance it is built from."),

 dict(q="Which of the following is the clearest example of a culture trait expressed in ARCHITECTURE?",
   choices=[
     "Courtyard houses built inward around a private central space, repeated across a region for centuries",
     "The height above sea level at which a town is built",
     "The number of people living in a town",
     "The distance between a town and the nearest river",
     "The average temperature of a town in July"],
   ans=0,
   why="EK PSO-3.A.2 names architecture among its examples of culture traits. A repeated building form embodies shared ideas about privacy, family and the relationship between household and street, and it is taught from builder to builder."),

 dict(q="Which pair of terms names attitudes rather than describing what a culture contains?",
   choices=[
     "Ethnocentrism and cultural relativism",
     "Food preferences and architecture",
     "Practices and technologies",
     "Land use and behaviors",
     "Attitudes and transmission"],
   ans=0,
   why="EK PSO-3.A.3 introduces ethnocentrism and cultural relativism as different attitudes toward cultural DIFFERENCE, which makes them stances an observer takes. The other options name components of culture itself, which is a different kind of thing."),

 dict(q="A textbook describes one society's agricultural methods as 'primitive' and another's as 'advanced' without stating the criterion. What is the problem?",
   choices=[
     "The ranking imports the writer's own standards as though they were universal, which is ethnocentrism",
     "The two societies cannot be compared at all",
     "Agricultural methods are not culture traits",
     "The problem is only that the writer did not use enough examples",
     "There is no problem, since some methods really are more advanced"],
   ans=0,
   why="EK PSO-3.A.3 names ethnocentrism as an attitude toward difference, and an unstated criterion is what makes a comparison ethnocentric rather than merely evaluative. A method well adapted to one environment may fail in another, so 'advanced' has to be advanced FOR something."),

 dict(q="Which is the strongest reason culture cannot be explained by the physical environment alone?",
   choices=[
     "Societies in similar environments make different choices, and societies in different environments sometimes make similar ones",
     "The physical environment has no influence on culture",
     "Cultures are entirely invented rather than transmitted",
     "The physical environment is too difficult to measure",
     "Cultures change and environments do not"],
   ans=0,
   why="PSO-3 makes physical geography and available resources sources of cultural variation without making them the only ones, which is the possibilist position from Unit 1 applied to culture. Both halves of the evidence are needed: constant environments with varying culture and varying environments with shared culture."),

 dict(q="Two groups living side by side speak different languages, keep different holidays, and eat different foods, but use the same tools and farm in the same way. How should this be described?",
   choices=[
     "They share some culture traits and differ in others, since culture is a bundle of traits rather than a single indivisible thing",
     "They have identical cultures",
     "They have entirely separate cultures with nothing in common",
     "Only the tools count as culture",
     "Only the language counts as culture"],
   ans=0,
   why="EK PSO-3.A.1's definition is a list of components and EK PSO-3.A.2 speaks of traits in the plural, so a culture is an assemblage rather than a unit. Groups can therefore overlap on some traits and diverge on others, which is the ordinary situation."),

 dict(q="A geographer studying a region's culture examines its cemeteries, field boundaries, kitchen equipment, and place names. What justifies treating such ordinary things as evidence?",
   choices=[
     "Culture is the shared, transmitted practices of everyday life, so ordinary objects and arrangements record it directly",
     "Only extraordinary objects can reveal culture",
     "These objects are the only ones that survive",
     "Culture is defined as the study of material objects",
     "These objects are physical rather than cultural features"],
   ans=0,
   why="EK PSO-3.A.1 defines culture as shared practices, technologies, attitudes and behaviors rather than as high art or ceremony. What people do every day, and the things they make to do it with, is where a definition that broad actually lives."),

 dict(q="Which statement best expresses the difference between the two attitudes the framework names?",
   choices=[
     "Ethnocentrism evaluates another culture by one's own standards; relativism seeks to understand it by its own",
     "Ethnocentrism is held by outsiders and relativism by insiders",
     "Ethnocentrism concerns religion and relativism concerns language",
     "Ethnocentrism is a culture trait and relativism is not",
     "The two attitudes are the same in practice"],
   ans=0,
   why="EK PSO-3.A.3 presents the two as different attitudes toward cultural difference, and the difference is whose standards supply the frame of reference. Both are available to any observer, insider or outsider, which is why the distinction is about method rather than position."),

 dict(q="A national campaign promotes one region's cuisine as the country's authentic national food. Which framework concepts are involved?",
   choices=[
     "Food preferences as a culture trait, promoted in a way that treats one region's traits as the standard for all",
     "Land use only, since food is grown",
     "Architecture only, since restaurants are buildings",
     "Neither, since national campaigns are political rather than cultural",
     "Cultural relativism, since the campaign celebrates a culture"],
   ans=0,
   why="EK PSO-3.A.2 names food preferences among culture traits, and elevating one region's traits to the national standard applies the standards of one group to everyone. That move is the ethnocentric structure operating inside a country rather than across a border."),

 dict(q="Why is the framework's definition of culture deliberately broad?",
   choices=[
     "Because a narrower definition would exclude the ordinary practices, tools, and attitudes that account for most of what varies between societies",
     "Because geographers cannot agree on a definition",
     "Because culture is impossible to define precisely",
     "Because the definition applies only to small societies",
     "Because a broad definition makes culture easier to measure"],
   ans=0,
   why="EK PSO-3.A.1 names four different kinds of thing in a single sentence, which is a choice rather than an accident. Restricting culture to art or to belief would leave a geographer unable to discuss the field patterns, house forms and diets that make regions visibly different."),

 dict(q="Which of the following would be evidence that a practice is genuinely SHARED rather than idiosyncratic?",
   choices=[
     "It is followed by most households in a community, expected of newcomers, and taught to children",
     "It is very old",
     "It is written down somewhere",
     "It is unusual compared with neighbouring communities",
     "It is performed in public"],
   ans=0,
   why="EK PSO-3.A.1's definition turns on sharing and transmission, so the evidence has to show both. Prevalence, an expectation applied to newcomers, and deliberate teaching are exactly the marks of a practice held in common rather than by an individual."),

 dict(q="A geographer argues that studying culture requires suspending judgement first and evaluating afterwards, if at all. Which framework concept is she applying?",
   choices=[
     "Cultural relativism, as an attitude adopted in order to understand a practice before assessing it",
     "Ethnocentrism, since she has her own standards",
     "Cultural transmission, since she will teach her findings",
     "A culture trait of the society she studies",
     "The definition of a culture trait"],
   ans=0,
   why="EK PSO-3.A.3 names relativism as an attitude toward cultural difference, and the sequence she describes is what the attitude amounts to in practice. Understanding first does not forbid judgement later; it forbids judgement in place of understanding."),

 dict(q="Survey responses on the staple grain eaten at the main meal are shown for four regions of one country. Using the table, what do the data show?",
   table=dict(
     headers=["Region", "Rice (%)", "Wheat (%)", "Maize (%)", "Other (%)"],
     rows=[
       ["Region 1", "82", "9", "5", "4"],
       ["Region 2", "11", "76", "8", "5"],
       ["Region 3", "6", "14", "74", "6"],
       ["Region 4", "38", "35", "21", "6"]]),
   choices=[
     "Three regions have a clear staple exceeding 70 percent while one is mixed, so food preference varies regionally within a single country",
     "All four regions share the same staple grain",
     "Food preference is uniform across the country",
     "Only one region has an identifiable staple",
     "The regions cannot be compared, since the percentages differ"],
   ans=0,
   why="Each row sums to 100, so the columns are shares of one region's households: three regions record a staple above 70 percent and the fourth has no category above 38. EK PSO-3.A.2 names food preferences among culture traits, and a trait varying between regions of one country is the pattern the table shows."),

 dict(q="House forms recorded in one region across four periods are shown. Using the table, what has happened to the region's architecture?",
   table=dict(
     headers=["Period", "Traditional courtyard form (%)", "Adapted courtyard with new materials (%)", "Imported style (%)"],
     rows=[
       ["1900-1939", "94", "2", "4"],
       ["1940-1979", "61", "27", "12"],
       ["1980-2019", "22", "51", "27"]]),
   choices=[
     "The inherited plan survives in most new houses even as materials and styles change, since the two courtyard categories together still account for 73 percent",
     "The inherited plan has disappeared entirely",
     "Imported styles now account for most new houses",
     "Nothing has changed since 1900",
     "The traditional form has grown as a share of new building"],
   ans=0,
   why="Each row sums to 100, and the two courtyard categories fall from 96 to 88 to 73 percent while the purely traditional form falls from 94 to 22. EK PSO-3.A.1 makes transmission the defining mechanism, and what is transmitted here is the plan rather than the material."),

 dict(q="Responses to a question about an unfamiliar cultural practice are shown for two survey groups. Using the table, which group's responses are more consistent with cultural relativism?",
   table=dict(
     headers=["Response given", "Group A (%)", "Group B (%)"],
     rows=[
       ["Asked what the practice means to those who follow it", "14", "58"],
       ["Judged it inferior to their own equivalent practice", "63", "17"],
       ["Said the practice should be abandoned", "18", "9"],
       ["Gave no opinion", "5", "16"]]),
   choices=[
     "Group B, where 58 percent sought the practice's meaning against 14 percent in the other group",
     "Group A, where 63 percent formed a clear judgement",
     "Group B, because it had the most respondents giving no opinion",
     "Group A, because it had the fewest respondents giving no opinion",
     "Neither, since attitudes cannot be measured by survey"],
   ans=0,
   why="Both columns sum to 100, so only shares are comparable, and the response asking what a practice means to its own practitioners is the relativist one while judging it against one's own equivalent is the ethnocentric one. The two groups are close to reversed on exactly that pair."),

 dict(q="Land-use patterns recorded in two districts settled by different groups are shown. Using the table, what is the best conclusion?",
   table=dict(
     headers=["Feature", "District 1", "District 2"],
     rows=[
       ["Mean field size (hectares)", "0.4", "36.0"],
       ["Field boundaries", "Stone walls and hedges", "Wire fencing"],
       ["Inheritance custom", "Divided among all heirs", "Passed to a single heir"],
       ["Soil type", "Loam", "Loam"],
       ["Mean annual rainfall (mm)", "780", "790"]]),
   choices=[
     "The two districts share their physical conditions almost exactly, so the ninetyfold difference in field size must reflect the different inheritance customs",
     "The difference in field size is explained by the difference in rainfall",
     "The difference in field size is explained by the difference in soil type",
     "The two districts have identical land-use patterns",
     "Field size is a physical rather than a cultural feature"],
   ans=0,
   why="Soil is identical and rainfall differs by 10 millimetres in 780, about one percent, while mean field size differs by a factor of ninety. A near-constant physical variable cannot explain an outcome that varies that widely, so the transmitted inheritance rule is what remains."),

 dict(q="A survey asked residents of four districts which traits they regard as central to their community's identity. Using the table, which trait is most widely shared across the four?",
   table=dict(
     headers=["Trait named as central", "District A (%)", "District B (%)", "District C (%)", "District D (%)"],
     rows=[
       ["Language spoken at home", "88", "91", "84", "90"],
       ["Religious observance", "71", "34", "62", "19"],
       ["Festival calendar", "45", "77", "38", "81"],
       ["Style of house building", "12", "18", "9", "22"]]),
   choices=[
     "Language, named by at least 84 percent in every district and with the smallest range across them",
     "Religious observance, which is named by a majority in two districts",
     "Festival calendar, which is named by more than three quarters of residents in two districts",
     "Style of house building, which is named least often everywhere",
     "No trait is shared, since the percentages differ between districts"],
   ans=0,
   why="Language runs 88, 91, 84 and 90 percent, a range of 7 points and the lowest figure in the table above 84, while religion ranges 19 to 71 and festivals 38 to 81. A trait that is both high and consistent across districts is the one most widely shared, which is a different question from which single figure is largest."),
]
