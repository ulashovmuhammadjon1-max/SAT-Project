# AP HUMAN GEOGRAPHY 3.6 Contemporary Causes of Diffusion -- 30 questions
# CED Course Framework V.1, Unit 3. Enduring understanding SPS-3; learning
# objective SPS-3.A, "Explain how historical processes impact current cultural
# patterns."
#
# Essential knowledge for THIS topic (A.1 and A.2 belong to 3.5):
#   SPS-3.A.3  Cultural ideas and practices are socially constructed and change
#              through both small-scale and large-scale processes such as
#              urbanization and globalization. These processes come to bear on
#              culture through media, technological change, politics, economics,
#              and social relationships.
#   SPS-3.A.4  Communication technologies, such as the internet and the
#              time-space convergence, are reshaping and accelerating
#              interactions among people; changing cultural practices, as in the
#              increasing use of English and the loss of indigenous languages;
#              and creating cultural convergence and divergence.
#
# SPS-3.A.3 contains three separate claims and all three are examinable:
#   1. Cultural ideas and practices are SOCIALLY CONSTRUCTED -- they are made
#      and maintained by people rather than given by nature. Items 1, 4, 11 and
#      19 turn on this.
#   2. Change runs through BOTH SMALL-SCALE AND LARGE-SCALE processes, with
#      urbanization and globalization named as the large-scale examples. Items
#      2, 5, 9, 14 and 22 turn on the scale pairing, which students collapse
#      into "globalization changes everything".
#   3. Those processes reach culture through FIVE named channels -- media,
#      technological change, politics, economics, and social relationships.
#      That list is closed and items 3, 8, 12, 17, 21 and 26 use it.
#
# SPS-3.A.4 names three consequences of communication technology and the third
# is the one students drop:
#   -- reshaping and ACCELERATING interactions among people
#   -- CHANGING CULTURAL PRACTICES, with two examples given: the increasing use
#      of English and the loss of indigenous languages
#   -- creating cultural CONVERGENCE AND DIVERGENCE
# The pairing in the third is deliberate. The same technologies that make places
# more alike also let dispersed minorities sustain and revive practices that
# proximity alone could never have kept going. Items 15, 18, 23, 25, 29 and 30
# are built on that, because a module teaching only convergence would be
# teaching half the sentence.
#
# TIME-SPACE CONVERGENCE, named in SPS-3.A.4 and undefined by the CED, is used
# here as: the reduction in the time needed to connect two places as transport
# and communication improve, so that places grow functionally closer while the
# distance between them is unchanged. It is the same phenomenon Topic 1.4 calls
# time-space compression, seen from the side of the places rather than the
# experience, and item 7 says so rather than pretending the two terms are
# unrelated.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g3_6.py. FIVE choices (A-E).
TOPIC = ("3.6", "Contemporary Causes of Diffusion", 3)

QUESTIONS = [
 dict(q="What does the framework mean by saying cultural ideas and practices are 'socially constructed'?",
   choices=[
     "They are made, maintained, and changed by people rather than given by nature or fixed for all time",
     "They are invented by governments",
     "They are determined by the physical environment",
     "They cannot be studied scientifically",
     "They are the same in every society"],
   ans=0,
   why="EK SPS-3.A.3 states that cultural ideas and practices are socially constructed. The point of the phrase is that a practice persists because people keep doing it and teaching it, which is also why it can change when they stop."),

 dict(q="Which two large-scale processes does the framework name as changing cultural ideas and practices?",
   choices=[
     "Urbanization and globalization",
     "Colonialism and imperialism",
     "Migration and industrialization",
     "Relocation and expansion",
     "Convergence and divergence"],
   ans=0,
   why="EK SPS-3.A.3 names urbanization and globalization as its examples of large-scale processes. Colonialism and imperialism belong to the previous topic's statement, and convergence and divergence are outcomes named in SPS-3.A.4 rather than processes."),

 dict(q="Through which five channels does the framework say these processes come to bear on culture?",
   choices=[
     "Media, technological change, politics, economics, and social relationships",
     "Media, education, religion, politics, and language",
     "Technology, migration, trade, war, and religion",
     "Politics, economics, geography, history, and language",
     "Media, transport, agriculture, industry, and government"],
   ans=0,
   why="EK SPS-3.A.3 prints exactly this list of five. Each distractor substitutes a plausible channel the statement does not name, and the list is closed rather than illustrative here."),

 dict(q="A geographer says that because a practice is socially constructed, it 'could have been otherwise'. What does this claim commit her to?",
   choices=[
     "That the practice arose from particular decisions and circumstances rather than from necessity, so it can be examined and can change",
     "That the practice is unimportant",
     "That the practice is false",
     "That the practice has no effects",
     "That every society will eventually abandon the practice"],
   ans=0,
   why="EK SPS-3.A.3's social construction claim is about origin and maintenance rather than about value. Recognising contingency is what makes a practice a subject for explanation instead of something taken as given."),

 dict(q="Why does the framework name BOTH small-scale and large-scale processes?",
   choices=[
     "Cultural change is produced by household and neighbourhood processes as well as by worldwide ones, and the two operate at once",
     "Only large-scale processes matter",
     "Only small-scale processes matter",
     "Small-scale and large-scale processes are the same thing",
     "The two never occur in the same place"],
   ans=0,
   why="EK SPS-3.A.3 writes 'both small-scale and large-scale processes', which is a deliberate pairing. A family deciding which language to speak at home and a global media industry are both changing culture, and neither account is complete without the other."),

 dict(q="Which of the following is the clearest example of URBANIZATION changing cultural practice?",
   choices=[
     "Households moving to cities adopting smaller family sizes, new work rhythms, and different food-buying habits",
     "A country's population growing",
     "A new international trade agreement",
     "A change in a country's climate",
     "A rise in the price of a commodity"],
   ans=0,
   why="EK SPS-3.A.3 names urbanization among the large-scale processes changing cultural ideas and practices. Moving to a city changes the cost of children, the structure of the working day and the way food is obtained, and each of those reshapes daily practice."),

 dict(q="Time-space convergence, as SPS-3.A.4 uses the term, refers to",
   choices=[
     "The falling time needed to connect two places as transport and communication improve, so places grow functionally closer while the distance between them is unchanged",
     "Two places physically moving toward each other",
     "The disappearance of distance from geography",
     "The convergence of two cultures into one",
     "The synchronization of clocks between countries"],
   ans=0,
   why="EK SPS-3.A.4 names time-space convergence among the communication technologies reshaping interaction, without defining it. It is the same phenomenon Topic 1.4 calls time-space compression, described from the side of the places rather than of the person experiencing the journey."),

 dict(q="A television and streaming industry concentrated in a few countries supplies much of the world's entertainment. Which of the framework's five channels is most directly at work?",
   choices=[
     "Media, one of the five channels through which large-scale processes reach culture",
     "Politics",
     "Economics only, since the industry is commercial",
     "Social relationships only, since people watch together",
     "None of the five, since entertainment is not culture"],
   ans=0,
   why="EK SPS-3.A.3 names media first among the five channels through which urbanization and globalization come to bear on culture. That the industry is also commercial does not displace the channel, since the question asks how the influence reaches people."),

 dict(q="Which of the following is best described as a SMALL-SCALE process changing culture?",
   choices=[
     "A neighbourhood's families deciding together to hold a weekly market that becomes a fixture of local life",
     "The worldwide expansion of a retail chain",
     "The growth of internet access across a continent",
     "A change in international trade rules",
     "The urbanization of a whole country"],
   ans=0,
   why="EK SPS-3.A.3 pairs small-scale with large-scale processes, and a neighbourhood establishing a durable practice is the small-scale case. The other four options operate at national or global extent, which is the other half of the pairing."),

 dict(q="What does SPS-3.A.4 identify as consequences of communication technologies?",
   choices=[
     "Accelerated interaction, changed cultural practices, and both cultural convergence and divergence",
     "Accelerated interaction only",
     "Cultural convergence only",
     "The disappearance of all local culture",
     "No cultural consequences at all"],
   ans=0,
   why="EK SPS-3.A.4 names three consequences in one sentence, and the third is a pair rather than a single outcome. A reading that stops at convergence omits half of what the statement asserts."),

 dict(q="A practice widely believed to be 'natural' turns out to have begun in a particular period, spread through particular channels, and to be absent in other societies. Which framework claim does this support?",
   choices=[
     "That cultural ideas and practices are socially constructed",
     "That cultural practices are determined by climate",
     "That cultural practices never change",
     "That only large-scale processes change culture",
     "That the practice is therefore worthless"],
   ans=0,
   why="EK SPS-3.A.3 asserts that cultural ideas and practices are socially constructed, and datable origins together with absence elsewhere are the standard evidence for it. Neither observation says anything about whether the practice is good."),

 dict(q="A government mandates a single language of instruction in all schools, and within two generations a minority language has few young speakers. Which channel from the framework's list is operating?",
   choices=[
     "Politics, since a state decision reached culture through the school system",
     "Media",
     "Economics",
     "Technological change",
     "None, since language change is natural"],
   ans=0,
   why="EK SPS-3.A.3 names politics among the five channels through which processes come to bear on culture, and EK SPS-3.A.4 names the loss of indigenous languages among the practices that change. A curriculum rule is politics acting on culture directly."),

 dict(q="Which pair of outcomes does SPS-3.A.4 say communication technologies create?",
   choices=[
     "Cultural convergence and cultural divergence, together rather than as alternatives",
     "Cultural convergence only",
     "Cultural divergence only",
     "Cultural convergence followed inevitably by divergence",
     "Neither, since technology has no cultural effects"],
   ans=0,
   why="EK SPS-3.A.4 ends by naming convergence AND divergence, which is a claim that both occur. The same networks that spread one set of practices everywhere also let dispersed communities find one another and sustain practices proximity could not."),

 dict(q="A rural district's young people adopt urban speech, dress, and music after gaining reliable mobile internet, while their grandparents' practices continue at home. What does this illustrate?",
   choices=[
     "Communication technology accelerating interaction and changing practices unevenly within one population",
     "The complete disappearance of the district's culture",
     "That technology has no cultural effect",
     "That the district has urbanized",
     "That cultural change is always uniform across a population"],
   ans=0,
   why="EK SPS-3.A.4 says communication technologies are reshaping and accelerating interactions and changing cultural practices, and nothing in that requires the change to be uniform. Access and receptiveness both vary by age, which is why one household can contain two patterns."),

 dict(q="Which observation is the best evidence for cultural DIVERGENCE produced by communication technology?",
   choices=[
     "A scattered minority using online networks to teach its language and coordinate observances it could not sustain locally",
     "A global brand opening outlets in many countries",
     "A film released simultaneously worldwide",
     "The same social platform being used everywhere",
     "A single language spreading in international business"],
   ans=0,
   why="EK SPS-3.A.4 names both convergence and divergence as effects of communication technology. Divergence appears where the technology sustains distinctiveness rather than dissolving it, which is exactly what a dispersed community's network does."),

 dict(q="What is the most accurate statement about English's role, given SPS-3.A.4's wording?",
   choices=[
     "Its use is increasing, which the framework names as an example of communication technologies changing cultural practices",
     "It has replaced all other languages",
     "Its use is decreasing worldwide",
     "It is unaffected by communication technology",
     "It is the only language used online"],
   ans=0,
   why="EK SPS-3.A.4 names the increasing use of English as one of its two examples of changed cultural practice. The statement is about a trend rather than about replacement, and overstating it would make a defensible claim into a false one."),

 dict(q="A multinational firm's hiring, pay, and promotion practices become the norm in an industry across several countries. Which of the five channels is most directly involved?",
   choices=[
     "Economics, since the influence travels through employment and markets",
     "Media",
     "Politics",
     "Technological change",
     "Social relationships"],
   ans=0,
   why="EK SPS-3.A.3 names economics among the five channels through which large-scale processes reach culture. Workplace norms spread because employment is where most adults spend their days and because firms compete for the same workers."),

 dict(q="Why does the framework pair convergence with divergence rather than naming only convergence?",
   choices=[
     "Because the same technologies simultaneously make distant places more alike and allow dispersed groups to maintain distinctiveness",
     "Because convergence and divergence mean the same thing",
     "Because divergence is more common than convergence",
     "Because convergence has been disproved",
     "Because the two occur in different centuries"],
   ans=0,
   why="EK SPS-3.A.4 names both outcomes in the same clause, which asserts that a single cause produces both. A network that carries a global product to a village also carries a minority's language lessons to its diaspora, and both effects are real."),

 dict(q="A student writes that globalization is 'erasing local culture everywhere'. What is the strongest correction available from the framework?",
   choices=[
     "The framework names divergence alongside convergence, and local practices are frequently adapted, revived, or asserted rather than erased",
     "Globalization has no cultural effects",
     "Local culture is unchanging",
     "The student is right, and the framework says so",
     "Only urbanization affects local culture"],
   ans=0,
   why="EK SPS-3.A.4 names cultural convergence AND divergence as effects, and EK SPS-3.A.3 makes culture something people construct rather than something passively received. The erasure claim assumes an audience with no agency, which is what both statements deny."),

 dict(q="A minority language loses its last fluent speakers over three generations as schooling, employment, and media all operate in a national language. Which framework statement covers this?",
   choices=[
     "That communication technologies and the processes reaching culture through media, politics, and economics change cultural practices, including the loss of indigenous languages",
     "That cultural practices never change",
     "That only politics affects language",
     "That language loss is unrelated to media or economics",
     "That the language was never socially constructed"],
   ans=0,
   why="EK SPS-3.A.4 names the loss of indigenous languages as an example of changing cultural practice, and EK SPS-3.A.3's five channels are how the pressure is applied. Naming several channels together is more accurate than isolating one, since a language dies when it stops being useful in all of them."),

 dict(q="Friendships, family ties, and community networks are named by the framework as one of the five channels. Why do they belong there?",
   choices=[
     "Most people adopt a new practice because someone they know and trust already has, which makes personal ties a channel of cultural change",
     "Because friendships are unaffected by culture",
     "Because social ties are the only channel that matters",
     "Because social relationships are a physical feature",
     "Because friendships cannot be studied"],
   ans=0,
   why="EK SPS-3.A.3 names social relationships among the five channels through which processes come to bear on culture. It is also the mechanism behind contagious diffusion from Topic 3.4: adoption travels along the links people actually have."),

 dict(q="Which is the strongest reason cultural change through the internet does not follow the distance-ordered pattern of contagious diffusion?",
   choices=[
     "Online contact does not require proximity, so the ordering falls to interest, language, and prominence instead of to distance",
     "The internet does not transmit culture",
     "Distance has ceased to exist",
     "Only cities have internet access",
     "Contagious diffusion never applied to any medium"],
   ans=0,
   why="EK SPS-3.A.4 says communication technologies are reshaping and accelerating interactions among people, and the reshaping is exactly this. Contact by proximity produces distance decay; contact by network produces ordering by connection instead."),

 dict(q="A national broadcaster's evening bulletin, watched by most households for decades, gives way to individually chosen feeds. What cultural consequence does the framework's convergence-and-divergence pairing predict?",
   choices=[
     "Both: some content reaches audiences worldwide while shared national reference points weaken and audiences fragment",
     "Convergence only, since content is now global",
     "Divergence only, since audiences fragment",
     "No change, since people still watch television",
     "The disappearance of all media influence"],
   ans=0,
   why="EK SPS-3.A.4 names convergence and divergence together, and this is a case where one change produces both at once. The same shift that lets a video reach a hundred countries also removes the single bulletin that gave one country a common evening."),

 dict(q="Which pairing correctly matches a case to the framework channel carrying it?",
   choices=[
     "A worldwide music genre reaching listeners through streaming platforms, matched to media",
     "A school curriculum law, matched to media",
     "A change in employment practices, matched to technological change",
     "A friend recommending a practice, matched to politics",
     "A new device changing daily routines, matched to social relationships"],
   ans=0,
   why="EK SPS-3.A.3's five channels are media, technological change, politics, economics and social relationships, and a streaming platform delivering music is the media case. Each other pairing attaches a case to a channel that does not carry it."),

 dict(q="What is the most defensible summary of contemporary cultural change, given both essential knowledge statements?",
   choices=[
     "Processes at several scales reach culture through media, technology, politics, economics, and social ties, producing both greater similarity between places and new forms of distinctiveness",
     "Globalization is making all places culturally identical",
     "Culture is unaffected by contemporary processes",
     "Only technology changes culture",
     "Local culture is always destroyed by global culture"],
   ans=0,
   why="EK SPS-3.A.3 supplies the scales and the five channels while EK SPS-3.A.4 supplies the paired outcome of convergence and divergence. A summary that keeps both halves is what the two statements together assert, and dropping either produces a claim the CED does not make."),

 dict(q="Survey responses on where respondents first encountered a newly adopted practice are shown. Using the table, which framework channel accounted for the most first encounters?",
   table=dict(
     headers=["Channel of first encounter", "Respondents"],
     rows=[
       ["Online video and social platforms", "1,940"],
       ["A friend or family member", "1,180"],
       ["At work or through an employer", "640"],
       ["A government campaign or school", "310"],
       ["A new device or application itself", "430"]]),
   choices=[
     "Media, at 1,940 of 4,500 respondents, more than any other single channel",
     "Social relationships, at 1,180 respondents",
     "Economics, at 640 respondents",
     "Politics, at 310 respondents",
     "Technological change, at 430 respondents"],
   ans=0,
   why="The five response categories map one to one onto EK SPS-3.A.3's five channels, and 1,940 of the 4,500 responses fall in the media one against 1,180 for the next largest. Every option names a real channel, so only the counts separate them."),

 dict(q="Internet access and the share of respondents reporting daily contact with people in other countries are shown for four years. Using the table, what relationship do the data show?",
   table=dict(
     headers=["Year", "Households with internet access (%)", "Reporting daily contact abroad (%)"],
     rows=[
       ["2000", "14", "3"],
       ["2010", "41", "17"],
       ["2020", "78", "49"],
       ["2024", "86", "58"]]),
   choices=[
     "Daily international contact rose from 3 to 58 percent as access rose from 14 to 86, which is interaction being accelerated by communication technology",
     "Daily international contact fell as access rose",
     "The two measures are unrelated",
     "Access rose faster than contact in every period",
     "Contact reached 100 percent by 2024"],
   ans=0,
   why="Access runs 14, 41, 78 and 86 percent while contact runs 3, 17, 49 and 58, rising together at every step with contact multiplying more than nineteenfold. EK SPS-3.A.4 says communication technologies are reshaping and accelerating interactions among people, which is what the pairing shows."),

 dict(q="Languages spoken in one country are recorded by number of speakers at two dates. Using the table, which pattern does the framework's account of language change predict and the data confirm?",
   table=dict(
     headers=["Language", "Speakers in 1980", "Speakers in 2020"],
     rows=[
       ["National language", "22,000,000", "38,000,000"],
       ["Indigenous language 1", "410,000", "96,000"],
       ["Indigenous language 2", "88,000", "9,000"],
       ["Indigenous language 3", "31,000", "2,100"]]),
   choices=[
     "The national language gained speakers while all three indigenous languages lost more than three quarters of theirs",
     "All four languages gained speakers",
     "All four languages lost speakers",
     "The indigenous languages gained speakers while the national language lost them",
     "The changes were the same size for every language"],
   ans=0,
   why="The national language rises from 22 to 38 million while the three indigenous languages fall by 77, 90 and 93 percent respectively. EK SPS-3.A.4 names the loss of indigenous languages among the practices communication technologies and related processes change."),

 dict(q="Online activity of a dispersed minority community is recorded over a decade. Using the table, which framework outcome do these data illustrate?",
   table=dict(
     headers=["Year", "Online language classes offered", "Members participating in coordinated observances", "Countries with participating members"],
     rows=[
       ["2014", "3", "420", "6"],
       ["2019", "27", "3,100", "19"],
       ["2024", "64", "9,800", "31"]]),
   choices=[
     "Cultural divergence, since the technology is sustaining a distinct practice across a community too scattered to maintain it locally",
     "Cultural convergence, since the community uses the same platforms as everyone else",
     "The loss of an indigenous language",
     "Urbanization changing cultural practice",
     "No framework outcome, since the numbers are small"],
   ans=0,
   why="Classes rise from 3 to 64, participants from 420 to 9,800 and participating countries from 6 to 31, so a community spread across more countries is sustaining more shared practice rather than less. EK SPS-3.A.4 names divergence alongside convergence, and this is the divergence case."),

 dict(q="Two measures of cultural change are recorded for one country across three decades. Using the table, what does the pair of trends show?",
   table=dict(
     headers=["Decade", "Households consuming internationally produced media weekly (%)", "Registered local cultural associations"],
     rows=[
       ["1990s", "18", "340"],
       ["2000s", "52", "610"],
       ["2010s", "84", "1,180"]]),
   choices=[
     "Convergence and divergence occurring together, since international media consumption and local cultural organizing both rose sharply",
     "Convergence only, since international media consumption rose",
     "Divergence only, since local associations rose",
     "Neither, since the two measures contradict each other",
     "That local associations caused the rise in media consumption"],
   ans=0,
   why="International media consumption rises from 18 to 84 percent while registered local associations rise from 340 to 1,180, so both curves move upward together. EK SPS-3.A.4 names convergence and divergence as effects of the same technologies, and two rising trends is what that pairing looks like in data."),
]
