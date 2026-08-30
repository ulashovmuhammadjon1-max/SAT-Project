# AP HUMAN GEOGRAPHY 3.5 Historical Causes of Diffusion -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding SPS-3, "Cultural
# ideas, practices, and innovations change or disappear over time." Learning
# objective SPS-3.A, "Explain how historical processes impact current cultural
# patterns."
#
# Essential knowledge for THIS topic (SPS-3.A.3 and A.4 belong to 3.6):
#   SPS-3.A.1  Interactions between and among culture traits and larger global
#              forces can lead to new forms of cultural expression; for example,
#              creolization and lingua franca.
#   SPS-3.A.2  Colonialism, imperialism, and trade helped to shape patterns and
#              practices of culture.
#
# SPS-3.A.1 makes a claim students routinely miss: contact does not only spread
# traits, it CREATES NEW ONES. The two examples the CED gives are both
# linguistic, and both are the product of contact rather than of either parent
# on its own. Items 1-9, 13, 17, 21, 26 and 27 are keyed to it.
#
# The two named examples, defined here since the CED defines neither:
#   creolization   the blending of two or more languages or cultural systems
#                  into a new form that belongs entirely to neither parent. In
#                  the linguistic case a PIDGIN is a simplified contact language
#                  with no native speakers; when a generation grows up speaking
#                  it as a first language it has become a CREOLE. That
#                  transition -- acquiring native speakers -- is the standard
#                  test and items 4, 8 and 27 turn on it.
#   lingua franca  a language used between speakers of different first
#                  languages, most often for trade and administration. It is
#                  defined by its FUNCTION, not by any property of the language
#                  itself, so the same language can be a lingua franca in one
#                  place and a first language in another. Items 5, 9 and 26
#                  turn on that.
#
# SPS-3.A.2 names three historical processes -- colonialism, imperialism, trade
# -- and says they HELPED TO SHAPE patterns and practices of culture. Note the
# verb: helped to shape, not determined. Items 10-12, 14-16, 18-20, 22-25 and
# 28-30 are keyed to it, and several of them turn on the fact that the resulting
# patterns outlive the political arrangements that produced them.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_5.py. FIVE choices (A-E).
TOPIC = ("3.5", "Historical Causes of Diffusion", 3)

QUESTIONS = [
 dict(q="According to the framework, what can interaction between culture traits and larger global forces produce?",
   choices=[
     "New forms of cultural expression that belong to neither original culture alone",
     "The disappearance of all local culture",
     "The preservation of every culture unchanged",
     "A single global culture identical everywhere",
     "Nothing, since culture traits do not interact"],
   ans=0,
   why="EK SPS-3.A.1 states that interactions between and among culture traits and larger global forces can lead to new forms of cultural expression. The key word is NEW: contact is generative rather than merely a matter of one trait replacing another."),

 dict(q="Which two examples does the framework name for new forms of cultural expression arising from interaction?",
   choices=[
     "Creolization and lingua franca",
     "Colonialism and imperialism",
     "Urbanization and globalization",
     "Assimilation and acculturation",
     "Relocation and expansion"],
   ans=0,
   why="EK SPS-3.A.1 names creolization and lingua franca as its two examples. Colonialism and imperialism belong to the next statement, urbanization and globalization to Topic 3.6, and assimilation and acculturation to Topic 3.8."),

 dict(q="Creolization is best described as",
   choices=[
     "The blending of two or more languages or cultural systems into a new form belonging entirely to neither parent",
     "The replacement of one language by another",
     "The disappearance of a language without a successor",
     "The use of one language for trade between groups",
     "The invention of a language with no prior influences"],
   ans=0,
   why="EK SPS-3.A.1 names creolization as an example of a new form of cultural expression arising from interaction. The defining feature is that the result is a new system rather than a version of either contributing one."),

 dict(q="A simplified contact language used between traders has no native speakers. A generation later, children in the port are growing up speaking it as their first language. What has happened?",
   choices=[
     "A pidgin has become a creole, since the contact language has acquired native speakers",
     "A creole has become a pidgin",
     "A lingua franca has disappeared",
     "One parent language has replaced the other",
     "Nothing has changed, since the vocabulary is the same"],
   ans=0,
   why="EK SPS-3.A.1 names creolization without defining it, and the standard test is exactly this transition. A contact language with no native speakers is a pidgin; once a generation acquires it as a mother tongue it becomes a creole with a full grammar and expressive range."),

 dict(q="A lingua franca is defined by",
   choices=[
     "Its function as a language used between speakers of different first languages, not by any property of the language itself",
     "The number of people who speak it as a first language",
     "The country in which it originated",
     "Its grammatical simplicity",
     "Its being written rather than spoken"],
   ans=0,
   why="EK SPS-3.A.1 names lingua franca as an example of a new form of cultural expression arising from interaction, and the term is functional. Any language becomes one where it is used to bridge groups with different mother tongues, which is why the same language can be a lingua franca in one region and a first language in another."),

 dict(q="A cuisine in a port city combines ingredients, techniques, and dishes from three continents into a body of cooking recognized as local and belonging to no one of the three. Which framework concept does this illustrate?",
   choices=[
     "Creolization, since interaction has produced a new form rather than a version of any contributing culture",
     "The emergence of a lingua franca",
     "The disappearance of local cuisine",
     "Colonialism operating directly",
     "The complete replacement of one cuisine by another"],
   ans=0,
   why="EK SPS-3.A.1 speaks of interactions among culture traits producing new forms of cultural expression, and creolization is its example of that process. The concept is not confined to language: any cultural system can blend into something that belongs to neither parent."),

 dict(q="Why does the framework treat cultural contact as generative rather than only as replacement?",
   choices=[
     "Because contact regularly produces forms that existed in none of the participating cultures beforehand",
     "Because contact never changes any culture",
     "Because contact always destroys the weaker culture",
     "Because contact only occurs through trade",
     "Because contact is a modern phenomenon"],
   ans=0,
   why="EK SPS-3.A.1's phrase is 'can lead to NEW FORMS of cultural expression', and its two examples are both things that did not exist before the contact that made them. A replacement account has no way to explain where a creole or a shared trade language came from."),

 dict(q="Which observation would best distinguish a creole from a pidgin?",
   choices=[
     "Whether there are people who speak it as a first language and can express anything in it",
     "Whether it is used in trade",
     "Whether it borrows words from more than one language",
     "Whether it is written down",
     "Whether it is spoken in a port"],
   ans=0,
   why="Both arise from contact and both draw on more than one source, so vocabulary and setting cannot separate them. The transition EK SPS-3.A.1's creolization names is the acquisition of native speakers, which is what turns a limited contact code into a full language."),

 dict(q="A language is the mother tongue of one country and is used across a region of many languages for business, higher education, and diplomacy. How should it be described in each role?",
   choices=[
     "A first language in the one country and a lingua franca across the region, since the term describes a function rather than a language",
     "A lingua franca in both, since it is used in more than one country",
     "A creole in the region, since speakers there mix it with their own languages",
     "A pidgin in the region, since it is used for business",
     "Neither, since a language can have only one status"],
   ans=0,
   why="EK SPS-3.A.1's lingua franca is defined by use between speakers of different first languages. Whether a language holds that status therefore depends on where you are asking, and the same language can be a mother tongue in one place and a bridge in another."),

 dict(q="Which three historical processes does the framework name as having helped shape patterns and practices of culture?",
   choices=[
     "Colonialism, imperialism, and trade",
     "Migration, urbanization, and industrialization",
     "Colonialism, war, and religion",
     "Trade, agriculture, and settlement",
     "Imperialism, technology, and education"],
   ans=0,
   why="EK SPS-3.A.2 names exactly these three. Migration, urbanization, industrialization and technology all shape culture too, but they are treated under other statements and other topics rather than this one."),

 dict(q="A country's official language, legal system, and school curriculum resemble those of a state that governed it a century ago and no longer does. What does this show?",
   choices=[
     "Cultural patterns established under colonial rule can outlive the political arrangement that created them",
     "The country is still governed by the former colonial power",
     "The similarity must be coincidental",
     "Colonialism has no cultural effects",
     "The country has recently adopted these institutions by free choice alone"],
   ans=0,
   why="EK SPS-3.A.2 says colonialism, imperialism and trade HELPED TO SHAPE patterns and practices of culture, and shaping is durable in a way that governing is not. Institutions once established have their own momentum, since they train the people who then run them."),

 dict(q="What is the most accurate way to state colonialism's cultural effect, given the framework's wording?",
   choices=[
     "It helped to shape cultural patterns, alongside the practices already present and those developed since",
     "It determined every feature of the cultures it touched",
     "It had no cultural effect",
     "It affected only language",
     "It affected only the colonizing society"],
   ans=0,
   why="EK SPS-3.A.2's verb is 'helped to shape' rather than determined, and taking the verb seriously is what separates an accurate claim from an overstatement. Colonized societies retained, adapted and created culture throughout, which is why the resulting patterns are blends rather than impositions."),

 dict(q="Which is the best example of trade shaping cultural practice over centuries?",
   choices=[
     "Crops, techniques, faiths, and vocabulary travelling along the same routes as goods, and taking hold at the ports and market towns along them",
     "A country closing its borders to all foreign contact",
     "Two societies with no contact developing similar tools",
     "A government banning imports",
     "A society deciding to preserve its traditions unchanged"],
   ans=0,
   why="EK SPS-3.A.2 names trade among the processes that helped shape patterns and practices of culture. A trade route is a repeated, durable channel of contact, so whatever travels with merchants -- seeds, gods, words, techniques -- diffuses along it."),

 dict(q="A distinctive musical form emerges among a population displaced by the transatlantic slave trade, drawing on instruments and rhythms from several African traditions together with European forms. This is best described as",
   choices=[
     "Creolization arising from forced contact, since the result is a new form belonging to none of its sources",
     "Relocation diffusion with no cultural change",
     "The disappearance of the original traditions",
     "A lingua franca in musical form",
     "Independent invention with no external influence"],
   ans=0,
   why="EK SPS-3.A.1 makes new forms of cultural expression the product of interaction among culture traits, and EK SPS-3.A.2 names the historical processes that forced the interaction. Nothing in the concept requires that the contact be voluntary."),

 dict(q="Why do the world's major lingua francas correspond closely to the reach of past empires and trade networks?",
   choices=[
     "A language becomes a bridge where administration, commerce, and schooling once required it, and that requirement leaves a durable pool of speakers",
     "Empires deliberately created lingua francas as their main goal",
     "The correspondence is coincidental",
     "Lingua francas can only arise from empires",
     "Lingua francas have no historical origins"],
   ans=0,
   why="EK SPS-3.A.2 names colonialism, imperialism and trade among the processes shaping cultural patterns, and EK SPS-3.A.1 names lingua franca among the resulting forms. The mechanism is practical: whoever must be dealt with sets the language of dealing, and that outlasts the dealing."),

 dict(q="A colonial administration drew its officials from one region of a colonized territory and excluded another. What long-term cultural consequence is most likely?",
   choices=[
     "A durable difference in education, language use, and access to state employment between the two regions",
     "No consequence, since administration is a political matter",
     "The two regions becoming culturally identical",
     "The immediate disappearance of both regions' cultures",
     "A consequence lasting only as long as the administration"],
   ans=0,
   why="EK SPS-3.A.2 says colonialism helped shape patterns AND PRACTICES of culture, and a recruitment rule is a practice with compounding effects. Schooling follows employment and employment follows schooling, so a difference created once reproduces itself for generations."),

 dict(q="Which statement about creolization is most accurate?",
   choices=[
     "It produces something new rather than a mixture in which the parents remain separable",
     "It is a temporary stage before one parent language wins",
     "It occurs only in language and never in other cultural forms",
     "It requires exactly two contributing cultures",
     "It occurs only where contact is voluntary"],
   ans=0,
   why="EK SPS-3.A.1 names creolization as an example of a NEW FORM of cultural expression. A blend that could be sorted back into its ingredients would not be a new form, which is what distinguishes creolization from simple borrowing."),

 dict(q="A trading city's population has for centuries included merchants from many origins, and its architecture, cuisine, festivals, and everyday speech all show multiple influences fused together. Which pair of framework processes best explains this?",
   choices=[
     "Trade as the historical process and creolization as the resulting new form of cultural expression",
     "Colonialism as the process and assimilation as the result",
     "Imperialism as the process and independent invention as the result",
     "Migration as the process and a lingua franca as the only result",
     "No framework process, since cities always change"],
   ans=0,
   why="EK SPS-3.A.2 names trade among the historical processes shaping cultural patterns and EK SPS-3.A.1 names creolization among the new forms interaction produces. Pairing a process with the form it generated is what a complete answer to this topic requires."),

 dict(q="Which of these best distinguishes colonialism from trade as a cause of cultural diffusion?",
   choices=[
     "Colonialism combines contact with political control, so it can impose institutions as well as offer practices",
     "Trade involves contact and colonialism does not",
     "Colonialism affects only language and trade only goods",
     "Trade is always more consequential than colonialism",
     "There is no difference between the two"],
   ans=0,
   why="EK SPS-3.A.2 names colonialism, imperialism and trade separately, and the distinction is the presence of coercive authority. Trade creates opportunities to adopt while colonial rule can also compel a school system, a legal code and an official language."),

 dict(q="A crop domesticated on one continent becomes a staple on another after centuries of trade and colonial agriculture. Which framework claim does this support?",
   choices=[
     "That colonialism, imperialism, and trade helped shape patterns and practices of culture, including food preferences",
     "That crops diffuse without human agency",
     "That food preferences are not culture traits",
     "That trade has no cultural effects",
     "That agricultural practices never change"],
   ans=0,
   why="EK SPS-3.A.2 names all three processes, and a staple crop's transfer runs through every one of them. EK PSO-3.A.2 from Topic 3.1 makes food preferences a culture trait, so the transfer changed culture and not only agriculture."),

 dict(q="What does the framework's phrase 'larger global forces' add to an account of cultural change?",
   choices=[
     "It places local cultural interaction inside processes such as empire and long-distance trade that operate at a much larger scale",
     "It means only global-scale processes matter",
     "It means local cultures do not interact",
     "It restricts the statement to the present day",
     "It has no particular meaning"],
   ans=0,
   why="EK SPS-3.A.1 speaks of interactions between and among culture traits AND larger global forces, which is a scale claim. A creole arises in one port and exists because of a trading system spanning oceans, so the local form cannot be explained at the local scale alone."),

 dict(q="A geographer says that colonialism's cultural legacy is 'still being written'. What is the strongest justification?",
   choices=[
     "The institutions, languages, and boundaries it established continue to shape decisions long after the rule itself ended",
     "Colonial rule has not actually ended anywhere",
     "Cultural legacies never change",
     "The claim cannot be justified, since colonialism is historical",
     "Only colonizing societies were affected"],
   ans=0,
   why="EK SPS-3.A.2 says these processes HELPED TO SHAPE patterns and practices of culture, which is a claim about durable structure. An official language or a school system keeps producing effects each year it operates, so the shaping continues after the shaper has gone."),

 dict(q="Which of the following would be evidence AGAINST a purely one-way account of colonial cultural influence?",
   choices=[
     "Foods, words, textiles, and religious practices from colonized regions becoming ordinary parts of life in the colonizing society",
     "A colonized society adopting the colonizer's official language",
     "A colonized society adopting the colonizer's legal system",
     "A colonized society adopting the colonizer's school curriculum",
     "A colonizing society having a large empire"],
   ans=0,
   why="EK SPS-3.A.1's interactions run between and among culture traits rather than in one direction only. Influence travelling back along the same routes is what shows contact to be a relationship rather than a transmission, however unequal the power in it."),

 dict(q="Why does the framework place this topic under an enduring understanding about cultural ideas CHANGING OR DISAPPEARING over time?",
   choices=[
     "Historical contact both creates new forms and ends existing ones, and the same processes do both",
     "Because all cultures eventually disappear",
     "Because no cultural idea ever changes",
     "Because change occurs only through trade",
     "Because disappearance is more common than change"],
   ans=0,
   why="SPS-3's enduring understanding names change AND disappearance, and EK SPS-3.A.1 and A.2 supply the mechanisms for both. The same colonial encounter that produced a creole also ended languages, and an honest account of the topic records both outcomes."),

 dict(q="Which is the strongest reason a lingua franca can persist long after the power that spread it has gone?",
   choices=[
     "Once enough people in a region use it to reach one another, each new learner has a practical reason to learn it regardless of its origin",
     "Because former colonies are required to keep it",
     "Because the language is easier than the alternatives",
     "Because no other language is available",
     "Because its origin is quickly forgotten"],
   ans=0,
   why="EK SPS-3.A.1's lingua franca is defined by function, and a functional advantage is self-reinforcing: the value of learning a bridge language rises with the number of people already using it. That mechanism is independent of how the first speakers came to it."),

 dict(q="Language use in four cities of one multilingual region is recorded. Using the table, which language functions as the region's lingua franca?",
   table=dict(
     headers=["City", "Most common first language", "Language used in interethnic business (%)"],
     rows=[
       ["City 1", "Language A", "Language D, 84"],
       ["City 2", "Language B", "Language D, 79"],
       ["City 3", "Language C", "Language D, 88"],
       ["City 4", "Language D", "Language D, 91"]]),
   choices=[
     "Language D, since it is used for business between groups in all four cities although it is the first language of only one",
     "Language A, since it appears first in the table",
     "Language B, since it is a first language somewhere",
     "Language C, since it is used in one city",
     "No language, since each city has a different first language"],
   ans=0,
   why="One language is named for interethnic business in all four cities, at 79 to 91 percent, while being the most common first language in only one of them. EK SPS-3.A.1's lingua franca is a functional category, and use between groups rather than first-language status is what defines it."),

 dict(q="Speaker data for a contact language are recorded across three generations. Using the table, in which generation did creolization occur?",
   table=dict(
     headers=["Generation", "Speakers using it as a second language", "Speakers using it as a first language"],
     rows=[
       ["Generation 1", "12,000", "0"],
       ["Generation 2", "26,000", "0"],
       ["Generation 3", "31,000", "9,400"]]),
   choices=[
     "Generation 3, since a contact language becomes a creole when a generation acquires it as a first language",
     "Generation 1, since the language already existed",
     "Generation 2, since second-language speakers more than doubled",
     "Generation 3, since second-language speakers were highest then",
     "No generation, since second-language speakers always outnumber first-language speakers"],
   ans=0,
   why="First-language speakers stand at zero for two generations and then reach 9,400, which is the transition from pidgin to creole. The second-language column rises throughout and therefore cannot mark the change, which is why the largest rise in that column is offered as a distractor."),

 dict(q="Official languages are recorded for a set of countries alongside their colonial histories. Using the table, what is the clearest pattern?",
   table=dict(
     headers=["Former administering power", "Countries", "Countries whose official language is that power's language"],
     rows=[
       ["Power 1", "18", "17"],
       ["Power 2", "11", "10"],
       ["Power 3", "9", "7"],
       ["Never administered by an outside power", "6", "0"]]),
   choices=[
     "34 of the 38 formerly administered countries use the administering power's language officially, against none of the six never administered",
     "All 44 countries use a former administering power's language",
     "Colonial history has no relationship to official language",
     "The six never administered countries use the most common colonial language",
     "Only Power 1's former territories show the pattern"],
   ans=0,
   why="Adding the first three rows gives 34 of 38 formerly administered countries, or 89 percent, against zero of six never administered. EK SPS-3.A.2 says colonialism and imperialism helped shape cultural patterns, and an official language is one of the most durable of those patterns."),

 dict(q="Vocabulary sources in one creole language are recorded. Using the table, what does the composition show?",
   table=dict(
     headers=["Source of vocabulary", "Share of core vocabulary (%)"],
     rows=[
       ["European lexifier language", "58"],
       ["West African languages", "27"],
       ["Indigenous American languages", "9"],
       ["Formed within the creole itself", "6"]]),
   choices=[
     "The language draws on at least three sources and has coined vocabulary of its own, so it is a new system rather than a dialect of any parent",
     "The language is simply a dialect of the European language",
     "The language is simply a dialect of the West African languages",
     "The language has no vocabulary of its own",
     "The shares cannot be compared, since the sources differ"],
   ans=0,
   why="The four shares sum to 100, with three separate donor families represented and 6 percent formed inside the language itself. EK SPS-3.A.1 names creolization as a NEW form of cultural expression, and a system with its own coinages is not reducible to any contributor."),

 dict(q="Cultural traits present in a port city are recorded by their period and route of arrival. Using the table, what is the best conclusion?",
   table=dict(
     headers=["Trait", "Period of arrival", "Route of arrival"],
     rows=[
       ["Staple crop", "1500s", "Trade"],
       ["Legal code", "1800s", "Colonial administration"],
       ["Musical form", "1700s-1800s", "Forced migration"],
       ["Official language", "1800s", "Colonial administration"],
       ["Spice trade cuisine", "1400s-1600s", "Trade"]]),
   choices=[
     "The city's present culture was shaped over four centuries by trade, colonial administration, and forced migration together, which are the processes the framework names",
     "The city's culture was shaped entirely by colonial administration",
     "The city's culture was shaped entirely by trade",
     "The city's culture arrived in a single period",
     "None of the traits listed is cultural"],
   ans=0,
   why="Five traits arrive by three different routes across four centuries, with two by trade, two by colonial administration and one by forced migration. EK SPS-3.A.2 names colonialism, imperialism and trade as processes that HELPED shape culture, and the plural is what the table demonstrates."),
]
