# AP HUMAN GEOGRAPHY 6.9 Urban Data -- 30 questions
# CED Course Framework V.1, Unit 6. Enduring understanding IMP-6, "The attitudes
# and values of a population, as well as the balance of power within that
# population, are reflected in the built landscape." Learning objective IMP-6.E,
# "Explain how qualitative and quantitative data are used to show the causes and
# effects of geographic change within urban areas." Suggested skill 3.E, explain
# what maps or data imply or illustrate about geographic principles, processes
# and outcomes.
#
# Essential knowledge -- two statements, and they divide the evidence in two:
#   IMP-6.E.1  Quantitative data from census and survey data provide information
#              about changes in population composition and size in urban areas.
#   IMP-6.E.2  Qualitative data from field studies and narratives provide
#              information about individual attitudes toward urban change.
#
# THE TWO STATEMENTS ANSWER DIFFERENT QUESTIONS, and the whole topic is knowing
# which question each can answer:
#
#   QUANTITATIVE (census, survey)   HOW MANY, and WHO -- the size and composition
#                                   of a population, and how both changed
#   QUALITATIVE (field studies,     HOW IT IS REGARDED -- what individuals think
#     narratives)                   about the change, and why they say so
#
# A census can establish that a district's median income doubled and its renting
# households fell by a third. It cannot say whether the people who left chose to
# or had to, or what the change meant to anyone. That is the boundary items 13,
# 14 and 15 are built on, and item 15 is the one the learning objective actually
# asks for, since CAUSES and EFFECTS of urban change generally need both kinds
# of evidence at once.
#
# THE CED'S OWN WORDS ARE SPECIFIC and the module keys on them:
#   - IMP-6.E.1 says composition AND SIZE. Composition is who the population
#     consists of, size is how many there are, and the two move independently
#     (items 6, 7, 26).
#   - IMP-6.E.2 says INDIVIDUAL attitudes. The claim is deliberately about
#     individuals, which is exactly why qualitative evidence is strong on
#     meaning and weak on generalization (items 11, 12, 21).
#
# THE OVERLAP WITH TOPIC 1.2 is deliberate and bounded. Topic 1.2's EK IIM-1.B.1
# covers geographic data in general -- field observation, remote sensing,
# geographic information systems, travel narratives, policy documents. This
# module keeps to the four sources THIS statement names and to what they show
# about URBAN change specifically, so that the two topics do not become the same
# module twice.
#
# THE LIMITATIONS ARE PART OF THE TOPIC, not an appendix, because the suggested
# skill is explaining what data imply. Items 17 to 21 and 29 cover the four that
# matter in urban work: an area figure is not a statement about any individual in
# it, hard-to-count populations are undercounted where they are most
# concentrated, a census is old the moment it is published, and a sample is only
# as good as who answered it.
#
# NO REAL CITY IS NAMED ANYWHERE IN THIS MODULE.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("6.9", "Urban Data", 6)

QUESTIONS = [
 dict(q="According to the framework, what do quantitative data from censuses and surveys provide?", choices=[
   "Information about changes in population composition and size in urban areas",
   "Information about individual attitudes toward urban change",
   "Information about the physical structure of buildings",
   "Information about the intentions of city governments",
   "Information about the climate of urban areas"], ans=0,
   why="EK IMP-6.E.1 states that quantitative data from census and survey data provide information about changes in population composition and size in urban areas. Attitudes belong to EK IMP-6.E.2's qualitative sources, which is the division this topic rests on."),

 dict(q="According to the framework, what do qualitative data from field studies and narratives provide?", choices=[
   "Information about individual attitudes toward urban change",
   "Precise counts of a district's population",
   "The exact median income of a neighbourhood",
   "The number of dwellings built in a given year",
   "The boundaries of a city's administrative districts"], ans=0,
   why="EK IMP-6.E.2 states that qualitative data from field studies and narratives provide information about individual attitudes toward urban change. Counts and medians are what EK IMP-6.E.1's quantitative sources supply."),

 dict(q="Why does the framework name both kinds of data rather than one?", choices=[
   "Each answers a question the other cannot -- how many and who, against how the change is regarded and why",
   "Because the two kinds always produce the same findings",
   "Because qualitative data are more accurate than quantitative data",
   "Because quantitative data cannot be collected in urban areas",
   "Because the framework treats the two as interchangeable"], ans=0,
   why="EK IMP-6.E.1 and EK IMP-6.E.2 assign the two kinds of data to different subjects, and learning objective IMP-6.E asks how both are used to show causes and effects of urban change. A count establishes that something happened; an account establishes what it meant to the people it happened to."),

 dict(q="What can census data show about a single neighbourhood over two decades?", choices=[
   "How its population size and its composition by age, household type, tenure and income changed between the two counts",
   "Why individual residents chose to move away",
   "What residents thought about the changes",
   "Which buildings residents considered attractive",
   "How the local council intended the district to develop"], ans=0,
   why="EK IMP-6.E.1 says quantitative data from census and survey data provide information about changes in population composition and size in urban areas. A census counts everyone and records characteristics, so comparing two counts measures both what changed and by how much."),

 dict(q="What does a sample survey add to a census in urban research?", choices=[
   "It can be run far more often and can ask questions a census does not, at the cost of covering only a sample rather than everyone",
   "It counts every household more accurately than a census does",
   "It replaces the need for a census entirely",
   "It measures physical structures rather than people",
   "It can only be conducted once a decade"], ans=0,
   why="EK IMP-6.E.1 names census AND survey data together as quantitative sources. A census is complete and infrequent while a survey is partial and frequent, so the two answer questions at different resolutions in time and in space."),

 dict(q="What does POPULATION COMPOSITION mean in the framework's statement?", choices=[
   "What the population consists of -- its distribution by age, household type, income, tenure and other characteristics",
   "The total number of people in an area",
   "The physical materials used to build an area's housing",
   "The area of land a population occupies",
   "The rate at which a population grows"], ans=0,
   why="EK IMP-6.E.1 names changes in population composition AND size as what quantitative data reveal. Composition is the internal make-up of a population, which is a different thing from its total and can change while the total does not."),

 dict(q="A district's population is unchanged in size over ten years while its median age falls by twelve years and its share of households renting rises by thirty points. What has occurred?", choices=[
   "Its composition has changed substantially while its size has not, which is why the framework names the two separately",
   "Nothing has changed, since the population total is the same",
   "Its size has changed but its composition has not",
   "The data must be inaccurate, since composition cannot change without size",
   "Only qualitative data could detect any change here"], ans=0,
   why="EK IMP-6.E.1 names changes in population composition AND size as two things quantitative data reveal. A district can replace much of its population without changing its total, and a study reporting only the total would record no change at all."),

 dict(q="Which combination of census measures would most strongly suggest that a district has been through gentrification?", choices=[
   "Rising median income and rents alongside a falling share of households renting and a falling share of long-tenure residents",
   "Falling median income alongside rising vacancy",
   "An unchanged population with unchanged income and rents",
   "A rising population with unchanged income and tenure",
   "A falling population with falling rents"], ans=0,
   why="EK IMP-6.E.1 says quantitative data show changes in population composition and size in urban areas. Gentrification is a change in composition and price together, so the signature is several measures moving in a consistent direction rather than any one of them alone."),

 dict(q="What can census figures NOT establish about a district whose lower-income households have declined in number?", choices=[
   "Whether those households moved by choice or were pushed out, since a count records the outcome and not the reason",
   "How many such households there were at each count",
   "What share of all households they represented",
   "How the district's median income changed",
   "How the district's population total changed"], ans=0,
   why="EK IMP-6.E.1 confines quantitative data to changes in composition and size, and EK IMP-6.E.2 assigns attitudes and accounts to qualitative sources. A difference between two counts is compatible with many different stories about how it came about."),

 dict(q="What is a field study in urban research?", choices=[
   "Direct observation and interviewing carried out in the place being studied, recording what is there and what people say about it",
   "A statistical analysis of census returns",
   "A survey mailed to a random sample of households",
   "A review of a city's planning documents",
   "An analysis of satellite imagery of a city"], ans=0,
   why="EK IMP-6.E.2 names field studies among the qualitative sources providing information about individual attitudes toward urban change. Being present is the method: what is observed and what people say in the place itself is evidence a returned form cannot supply."),

 dict(q="What is a narrative as a source of urban data?", choices=[
   "A first-person account -- an interview, an oral history, a written recollection -- of how a person experienced a place and its change",
   "A statistical summary of a district's population",
   "A map showing changes in land use",
   "A table of housing prices over time",
   "An official statement of a government's intentions"], ans=0,
   why="EK IMP-6.E.2 names narratives alongside field studies as qualitative sources on individual attitudes toward urban change. What a narrative supplies is a person's own account, including the reasons and meanings that no count records."),

 dict(q="Why do residents' attitudes toward urban change matter to a geographer studying a city?", choices=[
   "Attitudes shape whether change is supported, resisted or reversed, so they are part of what determines how a place actually develops",
   "Attitudes have no bearing on what happens in a city",
   "Attitudes can be measured precisely by a census",
   "Attitudes matter only to historians rather than geographers",
   "Attitudes determine a city's physical site"], ans=0,
   why="EK IMP-6.E.2 names individual attitudes toward urban change as the subject of qualitative data, and enduring understanding IMP-6 says the attitudes and values of a population are reflected in the built landscape. What residents accept or oppose feeds back into what is built."),

 dict(q="Which research question can ONLY be answered with qualitative data?", choices=[
   "Why long-term residents describe a redeveloped district as no longer theirs",
   "How many households moved out of the district last year",
   "What share of the district's households rent their homes",
   "How the district's median rent compares with the city's",
   "How the district's population changed between two censuses"], ans=0,
   why="EK IMP-6.E.2 assigns individual attitudes toward urban change to qualitative sources, and a question beginning with why a person describes something a particular way is a question about meaning. The other four are counts and comparisons of counts, which EK IMP-6.E.1 assigns to quantitative sources."),

 dict(q="Which research question can ONLY be answered with quantitative data?", choices=[
   "By how much the district's share of households renting fell between two censuses",
   "How residents feel about the change in the district",
   "Why some residents chose to stay when others left",
   "What the district means to the people who grew up there",
   "How residents describe the district's atmosphere"], ans=0,
   why="EK IMP-6.E.1 says quantitative data from census and survey data provide information about changes in population composition and size. A magnitude is what a count supplies, and no number of interviews can establish by how much a share changed across a whole district."),

 dict(q="How are the two kinds of data used together to explain a change in an urban area?", choices=[
   "The quantitative data establish what changed and by how much, and the qualitative data supply the reasons people give and the effects they report",
   "The two are used separately and their findings are never combined",
   "The qualitative data are used to check the arithmetic of the quantitative data",
   "The quantitative data explain attitudes and the qualitative data supply counts",
   "Only one kind of data may be used in any single study"], ans=0,
   why="Learning objective IMP-6.E asks how qualitative AND quantitative data are used to show the causes and effects of geographic change within urban areas. Cause and effect are the joint product: one source locates and sizes the change and the other accounts for it."),

 dict(q="At which scales are urban census data usually published, and why does the choice matter?", choices=[
   "At small area units such as tracts as well as for whole cities, and a city-wide figure can conceal opposite changes in different districts",
   "Only for whole cities, since districts are too small to measure",
   "Only for individual households, since that is who is counted",
   "Only at the national scale, since censuses are national",
   "Scale makes no difference to what a census shows"], ans=0,
   why="EK IMP-6.E.1 says quantitative data provide information about changes in population composition and size IN URBAN AREAS, and the suggested skill for this topic is explaining what data imply. A city whose median income is flat may contain districts that doubled and districts that halved."),

 dict(q="Why can a statistic for a district not be applied to any individual living in it?", choices=[
   "An area figure is an average or a total over many households, and individuals within the area vary around it",
   "Because district statistics are always inaccurate",
   "Because individuals are not counted in a census",
   "Because districts contain no individuals",
   "It can be applied directly, since a district figure describes each resident"], ans=0,
   why="The suggested skill for this topic is explaining what data imply, and this is the commonest fallacy in reading area data. A district with a high median income contains poor households, and inferring an individual's characteristics from an area's is a mistake the aggregation itself creates."),

 dict(q="Which urban populations are most likely to be undercounted in a census, and why does it matter?", choices=[
   "People without fixed addresses, in informal or subdivided housing, and recent arrivals -- and they are concentrated in particular districts, so the undercount is spatially uneven",
   "Wealthy households, because they are away from home more often",
   "Everyone is counted equally, so no undercount occurs",
   "Only people living in the city centre",
   "Households with several generations living together, who are counted twice"], ans=0,
   why="EK IMP-6.E.1 makes the census a source on population composition and size, so a systematic undercount distorts both. Because the hard-to-count groups cluster geographically, the error falls hardest on the districts whose numbers most need to be right."),

 dict(q="What is the main practical limitation of using census data to study a rapidly changing district?", choices=[
   "A census describes the moment it was taken and is published later still, so it can be years out of date for a district that is changing fast",
   "A census cannot record income or tenure",
   "A census covers only rural areas",
   "A census records attitudes rather than counts",
   "A census cannot be compared with an earlier census"], ans=0,
   why="EK IMP-6.E.1 names census data as a quantitative source on changes in composition and size. A complete enumeration is expensive, so it is infrequent, and the price of completeness is that the picture is always of a past moment."),

 dict(q="What determines whether a sample survey's findings can be applied to a whole district?", choices=[
   "Whether the people who responded resemble the district's population, since a sample that over-represents some groups will misdescribe it",
   "The number of questions on the survey form",
   "Whether the survey was conducted in person or by post",
   "The length of time the survey took to complete",
   "Whether the survey was funded publicly or privately"], ans=0,
   why="EK IMP-6.E.1 names survey data among the quantitative sources on population composition and size. A sample stands in for a population only if it resembles it, so who did not answer matters as much as who did."),

 dict(q="What is the characteristic limitation of qualitative data in urban research?", choices=[
   "A small number of accounts, however rich, cannot establish how widely a view is held across a district",
   "Qualitative data cannot record what people say",
   "Qualitative data are always collected from too many people",
   "Qualitative data give exact magnitudes but no meanings",
   "Qualitative data have no limitations"], ans=0,
   why="EK IMP-6.E.2 says qualitative data provide information about INDIVIDUAL attitudes toward urban change, and the word individual is doing the work. Depth and generalization trade against each other, which is precisely why the framework pairs the qualitative statement with a quantitative one."),

 dict(q="Why is comparing two censuses more informative about urban change than reading one?", choices=[
   "A single count describes a state, while two counts of the same area describe a change and allow its direction and size to be measured",
   "Two censuses are more accurate than one",
   "A single census cannot record any characteristics",
   "Two censuses remove the need for any survey data",
   "A single census is always out of date and a pair is not"], ans=0,
   why="EK IMP-6.E.1 says quantitative data provide information about CHANGES in population composition and size. A change is a difference between two observations, so the comparison rather than either count is what carries the information."),

 dict(q="A geographer maps the change in median household income by census tract across a city. What does that map show that a map of income levels does not?", choices=[
   "Which districts are changing and in which direction, rather than which are currently rich or poor",
   "The exact income of each household",
   "The attitudes of residents toward the change",
   "The physical condition of the housing stock",
   "Nothing that a map of income levels does not already show"], ans=0,
   why="EK IMP-6.E.1 makes CHANGES in population composition the subject of quantitative urban data, and the suggested skill for this topic is explaining what maps or data imply. A level map and a change map can look nothing alike, since a poor district rising fast and a wealthy district standing still are opposite on one and similar on the other."),

 dict(q="What should a researcher conducting a field study keep in mind about their own presence?", choices=[
   "Who they are and how they ask affects what people are willing to say, so the account produced is shaped by the encounter as well as by the place",
   "A researcher's presence has no effect on what respondents say",
   "Field studies should be conducted without speaking to anyone",
   "Only residents may conduct field studies in their own district",
   "A researcher's presence guarantees accurate responses"], ans=0,
   why="EK IMP-6.E.2 names field studies among the qualitative sources on individual attitudes toward urban change. An attitude is elicited rather than measured, so the circumstances of the asking are part of what produced the answer and belong in the account of it."),

 dict(q="Which pairing of a research question with the kind of data that answers it is CORRECT?", choices=[
   "How many households left the district between two censuses, answered by quantitative data",
   "How many households left the district between two censuses, answered by qualitative data",
   "What leaving the district meant to the households that left, answered by quantitative data",
   "How residents describe the district's changing atmosphere, answered by quantitative data",
   "By how much the district's median rent rose, answered by qualitative data"], ans=0,
   why="EK IMP-6.E.1 assigns changes in composition and size to quantitative sources and EK IMP-6.E.2 assigns individual attitudes to qualitative ones. Only one pairing here matches a question to the kind of data the framework says can answer it."),

 dict(q="One census tract is recorded at two censuses below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Measure", "First census", "Second census"],
     rows=[["Population", "4,200", "5,100"],
           ["Median household income (thousands)", "31", "68"],
           ["Share of households renting (%)", "71", "44"],
           ["Median monthly rent", "640", "1,780"]]),
   choices=[
   "Population rose by about 21 percent while median income more than doubled, rents nearly tripled and the renting share fell by 27 points, so the tract's composition changed far more than its size",
   "Population and income both fell across the two censuses",
   "The renting share rose while rents fell",
   "The tract's size changed more than its composition",
   "No conclusion is possible, since the two censuses used different units"], ans=0,
   why="Population rises from 4,200 to 5,100, about 21 percent, while income rises from 31 to 68 and rent from 640 to 1,780, and the renting share falls 27 points. EK IMP-6.E.1 names changes in composition AND size as two separate things quantitative data reveal, and here they move at very different rates."),

 dict(q="Survey responses to a proposed redevelopment are recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Respondent group", "Approve (%)", "Oppose (%)", "Unsure (%)"],
     rows=[["Homeowners", "68", "22", "10"],
           ["Renters", "24", "64", "12"]]),
   choices=[
   "Approval and opposition are almost exactly reversed between the two groups, with 68 percent of owners approving against 24 percent of renters",
   "Both groups approve in similar proportions",
   "Renters approve more strongly than owners",
   "Neither group has a majority view",
   "The percentages in each row do not sum to 100"], ans=0,
   why="Each row sums to 100, and approval runs 68 percent among owners against 24 among renters while opposition runs 22 against 64, so the two groups' positions are close to mirror images. EK IMP-6.E.1 names survey data among the quantitative sources, and disaggregating by tenure is what turns an ambiguous city-wide figure into a readable one."),

 dict(q="A mixed-methods study of one district is recorded below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Finding", "Count"],
     rows=[["Households surveyed", "480"],
           ["Said the neighbourhood had improved", "312"],
           ["Said the neighbourhood had worsened", "168"],
           ["Of those saying it had worsened, number who rent", "141"]]),
   choices=[
   "About 65 percent said the neighbourhood had improved, but 84 percent of those saying it had worsened were renters, so a single overall figure would conceal who was affected",
   "A majority of those surveyed said the neighbourhood had worsened",
   "Renters made up a minority of those saying the neighbourhood had worsened",
   "Every household surveyed gave the same answer",
   "The counts of improved and worsened do not sum to the number surveyed"], ans=0,
   why="The two answers sum to the 480 households surveyed, 312 of them about 65 percent, while 141 of the 168 negative answers, about 84 percent, came from renters. Learning objective IMP-6.E asks how data are used to show the causes and effects of urban change, and a majority verdict concealing a concentrated minority experience is exactly why both readings are needed."),

 dict(q="What limitation should be stated when reporting that most surveyed households said a district had improved?", choices=[
   "The households that had already left the district cannot be surveyed in it, so the people most affected by the change may be missing from the sample altogether",
   "Survey responses cannot be counted",
   "Percentages cannot be reported alongside counts",
   "A majority finding always settles a question",
   "The framework forbids surveying residents about urban change"], ans=0,
   why="EK IMP-6.E.1 names survey data among the quantitative sources on urban change, and a survey reaches whoever is present to answer it. Where the change under study is one that moved people out, the sample is selected by the very process being measured."),

 dict(q="A methods section must state what this topic's two statements establish. Which statement is accurate?", choices=[
   "Censuses and surveys measure how an urban population's size and composition changed, while field studies and narratives record what individuals think about the change, and explaining causes and effects generally requires both",
   "Censuses and surveys record attitudes while field studies produce counts",
   "Quantitative data alone are sufficient to explain urban change",
   "Qualitative data alone are sufficient to explain urban change",
   "The two kinds of data answer the same question in different formats"], ans=0,
   why="EK IMP-6.E.1 assigns size and composition to quantitative sources, EK IMP-6.E.2 assigns individual attitudes to qualitative ones, and learning objective IMP-6.E asks how both are used to show causes and effects. Each rejected summary either swaps the two assignments or discards one of them."),
]
