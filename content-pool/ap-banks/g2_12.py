# AP HUMAN GEOGRAPHY 2.12 Effects of Migration -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding IMP-2; learning
# objective IMP-2.E, "Explain historical and contemporary geographic effects of
# migration."
#
# Essential knowledge -- one statement, and it is a bare list of three:
#   IMP-2.E.1  Migration has political, economic, and cultural effects.
#
# Three domains, no examples, no definitions. So the citable content of this
# topic is the CLASSIFICATION -- which of the three domains an effect belongs to
# -- and everything else is reasoning that the claims below argue rather than
# cite. Items 1, 4, 7, 11, 15, 19, 23 and 27 ask for the domain directly, which
# is the part a citation can support.
#
# The second axis the module uses throughout, because the exam does: an effect
# falls on the ORIGIN, on the DESTINATION, or on both, and the same migration
# usually produces opposite effects at the two ends. Remittances are income at
# the origin and a wage bill at the destination; the loss of a trained nurse is
# a shortage at the origin and a filled vacancy at the destination. Items 3, 5,
# 9, 14, 18, 22, 26 and 28 are built on that pairing.
#
# Terms this module uses, defined here since the CED defines none of them:
#   remittance     money sent home by a migrant working abroad
#   brain drain    the emigration of highly trained people from a country that
#                  paid to train them
#   brain gain     the reverse, including skills and capital returning with a
#                  migrant, and the incentive effect on those who stay
#   ethnic enclave a district where a migrant-origin group is concentrated,
#                  supporting language, food, worship and business networks
#   diaspora       a dispersed population maintaining ties to a homeland
#
# A discipline the module holds to, and the reason several items are worded
# carefully: migration's effects are contested politically, so an item must ask
# what an effect IS rather than whether it is good. Items 16 and 24 make the
# trade-offs explicit instead of hiding them behind a preferred answer.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_12.py. FIVE choices (A-E).
TOPIC = ("2.12", "Effects of Migration", 2)

QUESTIONS = [
 dict(q="Which three kinds of effect does the framework attribute to migration?",
   choices=[
     "Political, economic, and cultural",
     "Political, environmental, and demographic",
     "Economic, environmental, and technological",
     "Cultural, demographic, and environmental",
     "Political, economic, and environmental"],
   ans=0,
   why="EK IMP-2.E.1 states that migration has political, economic and cultural effects, and the list is exactly three. Environmental, demographic and technological consequences certainly follow from migration, but they are not the three the statement names."),

 dict(q="Migrant workers abroad send home money that amounts to a fifth of their country's national income. What kind of effect is this, and where does it fall?",
   choices=[
     "An economic effect at the origin, since the money is income to households in the country the migrants left",
     "An economic effect at the destination, since the money is earned there",
     "A cultural effect at the origin, since families are separated",
     "A political effect at the destination, since transfers cross borders",
     "No effect, since the money is simply moved from one place to another"],
   ans=0,
   why="EK IMP-2.E.1 names economic effects, and remittances are the clearest of them. The wages are earned at the destination and spent at the origin, which is why the effect on household income falls on the country the migrants left."),

 dict(q="A country trains doctors at public expense and half of each graduating class emigrates. What is the effect on the origin, and what is it called?",
   choices=[
     "An economic loss known as brain drain, since the country bears the training cost and another country receives the benefit",
     "An economic gain known as brain gain, since the doctors send money home",
     "A cultural effect only, since medicine is a profession",
     "A political effect, since medical training is regulated",
     "No effect, since the doctors may return"],
   ans=0,
   why="EK IMP-2.E.1 names economic effects, and this is the standard case in which the effect at the origin and the effect at the destination run in opposite directions. The public investment is made in one country and the return on it is collected in another."),

 dict(q="A migrant-origin community establishes places of worship, shops, and a newspaper in its own language in one district of a destination city. Which effect is this?",
   choices=[
     "A cultural effect at the destination, visible in the district's landscape and institutions",
     "An economic effect, since shops are businesses",
     "A political effect, since newspapers report on politics",
     "A cultural effect at the origin, since the community came from elsewhere",
     "No effect, since districts change constantly"],
   ans=0,
   why="EK IMP-2.E.1 names cultural effects, and the visible institutions of a community are how those effects show up on the ground. That the shops are also businesses does not make the effect economic, since the question asks what the change principally is."),

 dict(q="Which pairing correctly describes the SAME migration having opposite effects at its two ends?",
   choices=[
     "A shortage of trained nurses at the origin and a filled vacancy at the destination",
     "A shortage of trained nurses at both ends",
     "A gain in population at both ends",
     "A cultural effect at the origin and no effect at the destination",
     "A political effect at the destination and no effect at the origin"],
   ans=0,
   why="A migrant is subtracted from one labour market and added to another, so a single move produces a deficit in one place and a surplus in the other. EK IMP-2.E.1's economic effects are frequently of this kind, which is why the origin and the destination have to be considered separately."),

 dict(q="Migrants in a destination country organize to lobby for changes in visa rules and campaign in local elections once naturalized. This is",
   choices=[
     "A political effect of migration at the destination",
     "An economic effect at the destination",
     "A cultural effect at the origin",
     "An economic effect at the origin",
     "Not an effect of migration, since campaigning is a normal political activity"],
   ans=0,
   why="EK IMP-2.E.1 names political effects, and the arrival of a population that can organize and eventually vote changes what a destination's politics is about. That the activity itself is ordinary is what makes the effect political rather than exceptional."),

 dict(q="A diaspora community funds political parties and civil society organizations in its country of origin and lobbies its host government on that country's behalf. Which effect is this?",
   choices=[
     "A political effect at the origin, produced by people who are no longer resident there",
     "An economic effect at the destination",
     "A cultural effect at the destination",
     "No effect, since the community has left",
     "A political effect at the destination only"],
   ans=0,
   why="EK IMP-2.E.1 names political effects without confining them to the receiving country. A diaspora retains an interest in the politics of the place it left and often has resources the residents do not, so its influence there can be considerable."),

 dict(q="A rural district loses most of its young adults to the cities over thirty years. Which combination of effects follows?",
   choices=[
     "An economic effect as the labour force shrinks and a cultural effect as institutions and traditions lose the people who sustained them",
     "Only an economic effect, since the district loses workers",
     "Only a cultural effect, since traditions change",
     "A political effect only, since the district loses representation",
     "No effect, since the population is simply redistributed"],
   ans=0,
   why="EK IMP-2.E.1 names three kinds of effect and nothing prevents one migration from producing more than one. A school, a festival and a football club all require people of particular ages, so a selective loss reaches the culture as directly as it reaches the labour market."),

 dict(q="Which is the strongest reason a destination country's population can grow younger as a result of immigration?",
   choices=[
     "Migrants are concentrated in the young working ages, so their arrival adds disproportionately to those cohorts",
     "Migrants have lower mortality than residents at every age",
     "Migrants are usually retired",
     "Immigration reduces the number of older residents",
     "Immigration changes the way a population is counted"],
   ans=0,
   why="Migration is strongly selective by age, so a receiving country imports a slice of the pyramid rather than a cross-section of it. The effect on age structure follows from who moves rather than from anything happening to the resident population."),

 dict(q="Remittances make up a large share of a country's foreign exchange earnings. What is the principal risk this creates?",
   choices=[
     "The country's income becomes dependent on labour markets and immigration policies it does not control",
     "The country's population will fall to zero",
     "Remittances cannot be spent domestically",
     "Remittances reduce household income",
     "There is no risk, since remittances are always stable"],
   ans=0,
   why="EK IMP-2.E.1's economic effects include the structure of an economy as well as the flow of money. A recession or a rule change in a destination country transmits directly into the origin's household income, which is a dependence rather than a benefit or a cost."),

 dict(q="A destination city's cuisine, music, and festivals come to include elements brought by successive migrant groups. This is best described as",
   choices=[
     "A cultural effect at the destination, in which the receiving society itself is changed by the people it receives",
     "An economic effect, since restaurants are businesses",
     "A political effect, since festivals require permits",
     "A cultural effect at the origin, since the practices came from there",
     "Not an effect of migration, since cultures always change"],
   ans=0,
   why="EK IMP-2.E.1 names cultural effects, and this is the reciprocal case: the receiving society is not a fixed container that migrants enter. That cultures change anyway does not make a specific change caused by specific arrivals uncaused."),

 dict(q="Which of the following is an ECONOMIC effect of immigration on a destination country?",
   choices=[
     "Sectors that depend on migrant labour can expand, while wages in those occupations face downward pressure",
     "The destination country's language changes over generations",
     "Naturalized migrants become a constituency in elections",
     "New places of worship appear in particular neighbourhoods",
     "The country's total land area increases"],
   ans=0,
   why="EK IMP-2.E.1 separates economic from political and cultural effects, and this option is about labour supply and wages. Language and worship are cultural, an electoral constituency is political, and land area does not change at all."),

 dict(q="Why do geographers describe some effects of migration as running in BOTH directions between origin and destination?",
   choices=[
     "Migrants send money, ideas, and expectations home while carrying practices and skills abroad, so influence flows along the same route in both directions",
     "Migrants always return to their origin eventually",
     "Effects at the origin cancel effects at the destination",
     "The origin and destination are the same place",
     "Only economic effects can run in two directions"],
   ans=0,
   why="EK IMP-2.E.1's three kinds of effect are not confined to one end of a migration, and a migration route is a channel rather than a one-way pipe. Remittances, return visits, and changed expectations about schooling or marriage all travel back along it."),

 dict(q="A country's government negotiates agreements with several destination states to protect its citizens working abroad. This shows that",
   choices=[
     "Emigration produces political effects at the origin, since the state acquires interests and obligations outside its own territory",
     "Emigration has no political consequences",
     "Emigration is a purely cultural process",
     "The origin state has become part of the destination state",
     "The agreements are economic rather than political"],
   ans=0,
   why="EK IMP-2.E.1 names political effects, and one of the least obvious is that a state with a large emigrant population must conduct a foreign policy about them. That obligation exists whether or not the migrants ever return."),

 dict(q="A destination country debates whether immigration raises or lowers wages for existing workers. What is the most defensible summary of what geographers can say?",
   choices=[
     "The effect differs by occupation, skill level, and time period, so a single answer for a whole country conceals opposite effects inside it",
     "Immigration always lowers wages for everyone",
     "Immigration always raises wages for everyone",
     "Wages are unaffected by immigration under any circumstances",
     "The question cannot be studied because wages are not measured"],
   ans=0,
   why="EK IMP-2.E.1 names economic effects without asserting their sign, and the evidence supports a disaggregated answer rather than a single one. Workers who compete directly with arrivals and workers whose services arrivals buy are affected in opposite directions."),

 dict(q="Which is an example of BRAIN GAIN rather than brain drain?",
   choices=[
     "Engineers who trained and worked abroad returning to found firms and train others at home",
     "Nurses emigrating after their training is paid for at home",
     "Students leaving for university abroad and remaining there",
     "Doctors recruited from a country facing a shortage",
     "Researchers accepting permanent posts overseas"],
   ans=0,
   why="Brain gain is the return of skills and capital to an origin country, including through people who left and came back with more than they took. The other four options are all movements of trained people away from the country that trained them."),

 dict(q="What is the most important reason remittances are often considered a more reliable source of income for a household than foreign aid is for a government?",
   choices=[
     "They go directly to the household that needs them, and migrants often increase them precisely when conditions at home worsen",
     "They are larger than all aid combined in every country",
     "They are paid by governments rather than by individuals",
     "They cannot be spent on consumption",
     "They are guaranteed by international agreement"],
   ans=0,
   why="EK IMP-2.E.1's economic effects include the channel through which money reaches people, and remittances bypass the institutions aid must pass through. The countercyclical behaviour is what distinguishes them: a family sends more, not less, after a bad harvest."),

 dict(q="A destination country's schools must add classes in a second language and hire staff who speak it. Which effects are involved?",
   choices=[
     "A cultural effect, since the language of a public institution changes, and an economic effect, since the change has a cost",
     "Only a cultural effect, since language is culture",
     "Only an economic effect, since staff must be paid",
     "A political effect only, since schools are public",
     "No effect, since schools change their staffing regularly"],
   ans=0,
   why="EK IMP-2.E.1 names three domains and a single consequence can fall into more than one of them. The change in what language a public institution operates in is cultural, and the budget line it creates is economic."),

 dict(q="Which of these is best described as a POLITICAL effect of migration at the destination?",
   choices=[
     "Immigration becoming a central issue in national elections and a determinant of how people vote",
     "Restaurants serving new cuisines opening in a city centre",
     "Money being sent from the destination to migrants' families",
     "A shortage of workers appearing in the origin country",
     "New places of worship being built"],
   ans=0,
   why="EK IMP-2.E.1 separates political from economic and cultural effects. Cuisine and worship are cultural, remittances and labour shortages are economic, and what an election is fought about is political by definition."),

 dict(q="A village's population halves and its school, clinic, and bus service close for lack of users. What is the most complete description?",
   choices=[
     "An economic effect, since services need a threshold population, with cultural consequences as the institutions that held the village together disappear",
     "A purely cultural effect",
     "A purely political effect",
     "No effect, since the services could reopen",
     "An environmental effect, since fewer people use the land"],
   ans=0,
   why="EK IMP-2.E.1 names economic and cultural effects among the three, and both are present: services close because too few people remain to sustain them, and their closure removes the places where the community met. Naming both is what makes the description complete."),

 dict(q="Why can the same immigration produce a labour shortage in one country and a labour surplus in another at the same time?",
   choices=[
     "Migration subtracts workers from the origin's labour market and adds them to the destination's, so one market tightens as the other loosens",
     "Labour markets are unaffected by migration",
     "Both countries experience shortages",
     "Both countries experience surpluses",
     "The effect depends only on the total world population"],
   ans=0,
   why="EK IMP-2.E.1's economic effects operate on two labour markets rather than one, and a migrant leaves a gap behind exactly as surely as they fill one ahead. Whether either market notices depends on how large the flow is relative to each."),

 dict(q="Second-generation members of a migrant community speak the destination's language at school and their parents' language at home, and identify with both. This illustrates",
   choices=[
     "A cultural effect that continues after the migration itself has ended, since identity is renegotiated across generations",
     "An economic effect, since schooling has a cost",
     "A political effect, since language policy is legislated",
     "No effect, since the second generation did not migrate",
     "A cultural effect at the origin only"],
   ans=0,
   why="EK IMP-2.E.1 names cultural effects without limiting them to the migrants themselves. The consequences of a migration are worked out over generations, which is why a community's cultural geography keeps changing long after arrivals stop."),

 dict(q="Which statement about the effects of migration is most defensible as a general claim?",
   choices=[
     "Effects fall on origins and destinations alike, differ by domain, and are frequently opposite in sign at the two ends",
     "All effects of migration fall on the destination",
     "All effects of migration fall on the origin",
     "The effects of migration are always positive",
     "The effects of migration are always negative"],
   ans=0,
   why="EK IMP-2.E.1 names three domains without assigning a sign or a location to any of them. A general claim that survives is therefore structural -- where the effects fall and how they differ -- rather than an evaluation."),

 dict(q="A country with heavy emigration finds that villages with the most migrants abroad also have the best housing and the highest school enrolment, but the fewest working-age adults. What is the most accurate reading?",
   choices=[
     "Remittances have raised living standards while the absence of the people who send them has hollowed out the local workforce, which is the same migration producing opposite effects",
     "Emigration has had no effect on these villages",
     "The housing and schooling must have other causes entirely",
     "The villages are better off in every respect",
     "The villages are worse off in every respect"],
   ans=0,
   why="EK IMP-2.E.1's economic effects can run in both directions at the same place, and this is the standard case. The money and the missing people arrive from the same decision, so an honest account records the improvement and the loss together."),

 dict(q="Which of the following would be the best evidence that a destination district has become an ethnic enclave?",
   choices=[
     "A large share of residents share one origin, and businesses, worship, and signage in the district serve that community in its own language",
     "The district has a high population density",
     "The district's residents have lower incomes than the city average",
     "The district is close to the city centre",
     "The district has grown rapidly in the last decade"],
   ans=0,
   why="An enclave is defined by concentration of one origin group together with the institutions that concentration supports, which is EK IMP-2.E.1's cultural effect made visible on the landscape. Density, income, location and growth rate are true of many districts that are not enclaves."),

 dict(q="Remittances are shown for four countries alongside their national income. Using the table, which country depends most heavily on money sent home by migrants?",
   table=dict(
     headers=["Country", "Remittances received (US$ billions)", "GDP (US$ billions)"],
     rows=[
       ["Country A", "24.0", "480.0"],
       ["Country B", "8.4", "28.0"],
       ["Country C", "31.0", "1,240.0"],
       ["Country D", "3.6", "36.0"]]),
   choices=[
     "Country B, where remittances equal 30 percent of national income",
     "Country C, which receives the largest amount of remittances",
     "Country A, where remittances equal 5 percent of national income",
     "Country D, where remittances equal 10 percent of national income",
     "Country C, because the largest economy must be the most dependent"],
   ans=0,
   why="Remittances as a share of national income are 5, 30, 2.5 and 10 percent, so the country receiving the largest amount in dollars is the least dependent of the four. Dependence is a ratio and the dollar total is a size, which is why they rank the countries differently."),

 dict(q="Emigration of trained professionals is shown for four countries. Using the table, which country faces the most severe brain drain?",
   table=dict(
     headers=["Country", "Physicians trained (per year)", "Physicians emigrating within five years"],
     rows=[
       ["Country P", "1,800", "360"],
       ["Country Q", "240", "168"],
       ["Country R", "5,000", "500"],
       ["Country S", "900", "270"]]),
   choices=[
     "Country Q, which loses 70 percent of each cohort it trains",
     "Country R, which loses the largest number of physicians",
     "Country P, which loses 20 percent of each cohort it trains",
     "Country S, which loses 30 percent of each cohort it trains",
     "Country R, because the largest training programme must lose the most"],
   ans=0,
   why="Emigration rates are 20, 70, 10 and 30 percent of each trained cohort, so the country losing the most doctors in absolute terms has the lowest loss rate of the four. A small training programme losing seven in ten graduates is the severe case."),

 dict(q="A destination country's workforce is broken down by sector. Using the table, in which sector would a halt to immigration be felt most sharply?",
   table=dict(
     headers=["Sector", "Total workers (thousands)", "Foreign-born workers (thousands)"],
     rows=[
       ["Agriculture and food processing", "400", "260"],
       ["Construction", "900", "315"],
       ["Health and social care", "1,200", "360"],
       ["Public administration", "700", "70"]]),
   choices=[
     "Agriculture and food processing, where 65 percent of workers are foreign-born",
     "Health and social care, which employs the most foreign-born workers",
     "Construction, where 35 percent of workers are foreign-born",
     "Public administration, where 10 percent of workers are foreign-born",
     "Health and social care, because it is the largest sector listed"],
   ans=0,
   why="Foreign-born shares are 65, 35, 30 and 10 percent, so the sector employing the most foreign-born workers in absolute terms is not the most exposed to a halt. Exposure is the share of a sector's workforce that would be missing, not the headcount."),

 dict(q="Languages spoken at home are shown for one city district across three censuses. Using the table, what has happened?",
   table=dict(
     headers=["Census", "National language only (%)", "National language and another (%)", "Another language only (%)"],
     rows=[
       ["1990", "88", "9", "3"],
       ["2005", "61", "27", "12"],
       ["2020", "44", "42", "14"]]),
   choices=[
     "The share speaking only the national language fell by 44 points while bilingual households rose from 9 to 42 percent, the largest single change in the table",
     "The share speaking only another language became the largest category",
     "All three categories fell between 1990 and 2020",
     "The district became less linguistically diverse",
     "Bilingual households fell while monolingual households rose"],
   ans=0,
   why="Each row sums to 100, so only composition can be read: the national-language-only share falls from 88 to 44 and bilingual households rise from 9 to 42, a gain of 33 points against the other-language-only category's 11. Bilingualism rather than replacement is what the numbers show."),

 dict(q="Net migration and age structure are shown for two districts of one country. Using the table, which statement is best supported?",
   table=dict(
     headers=["District", "Net migration rate (per 1,000)", "Share aged 20-39 (%)", "Share aged 65+ (%)"],
     rows=[
       ["Interior district", "-18", "17", "29"],
       ["Coastal district", "+21", "34", "12"]]),
   choices=[
     "The same internal migration has aged one district and rejuvenated the other, since young adults are leaving one and arriving in the other",
     "Both districts are aging at the same rate",
     "The coastal district is older than the interior district",
     "Migration has had no effect on either district's age structure",
     "The interior district has more young adults than the coastal district"],
   ans=0,
   why="One district loses 18 per 1,000 and holds 17 percent aged 20 to 39 against 29 percent over 65, while the other gains 21 per 1,000 with 34 percent young adults and 12 percent elderly. Internal migration nets to zero nationally, so the same flow produces exactly opposite age effects at its two ends."),
]
