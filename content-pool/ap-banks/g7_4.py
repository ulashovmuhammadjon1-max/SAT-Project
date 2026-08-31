# AP HUMAN GEOGRAPHY 7.4 Women and Economic Development -- 30 questions
# CED Course Framework V.1, Unit 7. Enduring understanding SPS-7,
# "Industrialization, past and present, has facilitated improvements in
# standards of living, but it has also contributed to geographically uneven
# development." Learning objective SPS-7.D, "Explain how and TO WHAT EXTENT
# changes in economic development have contributed to gender parity." Suggested
# skill 3.D, compare patterns and trends in quantitative and geospatial data.
#
# Essential knowledge -- three statements:
#   SPS-7.D.1  The roles of women change as countries develop economically.
#   SPS-7.D.2  Although there are more women in the workforce, they do not have
#              equity in wages or employment opportunities.
#   SPS-7.D.3  Microloans have provided opportunities for women to create small
#              local businesses, which have improved standards of living.
#
# THE OBJECTIVE'S PHRASE IS "AND TO WHAT EXTENT", and it is the most important
# wording in the topic. SPS-7.D does not ask whether development produces gender
# parity; it asks HOW and HOW FAR. That is a question with a partial answer, and
# SPS-7.D.2 supplies it in the CED's own sentence structure: ALTHOUGH there are
# more women in the workforce, they do not have equity in wages or employment
# opportunities. Items 2, 3, 14 and 24 are built on that concession, and item 3
# asks for the structure of the sentence directly, because a student who
# remembers only the first clause has learned the opposite of what it says.
#
# SPS-7.D.2 NAMES TWO KINDS OF INEQUITY, not one, and they are different things:
#   wages                  unequal pay, whether for the same work or through the
#                          lower pay attached to work women predominantly do
#   employment opportunity unequal access to particular occupations and to
#                          advancement within them
# Items 4, 5, 18 and 28 keep them apart, because a table showing near-equal
# workforce participation can conceal a completely uneven distribution ACROSS
# occupations, which is what item 28's record is built to show.
#
# SPS-7.D.3 IS A POSITIVE CLAIM AND THE MODULE REPORTS IT AS ONE. The CED says
# microloans HAVE PROVIDED opportunities and the businesses HAVE IMPROVED
# standards of living. No item here contradicts that. What items 13 and 29 do
# instead is what the objective licenses: ask how FAR the instrument reaches,
# since a loan addresses the absence of capital and not the other constraints the
# same topic names. That is a question about extent, not a denial of the claim.
#
# WHAT THIS MODULE WILL NOT ASSERT: that development produces parity
# automatically (item 22), that participation rises steadily with income (item
# 26's record deliberately does not), or any claim about a named country. NO REAL
# COUNTRY IS NAMED ANYWHERE IN THIS MODULE, the three data items included.
#
# SYNONYM CARE. `geo_check` treats {"gender inequality index", "gii"} as one
# construct, so item 9 names it in exactly one way.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("7.4", "Women and Economic Development", 7)

QUESTIONS = [
 dict(q="What does the framework say happens to the roles of women as countries develop economically?", choices=[
   "They change",
   "They remain fixed regardless of development",
   "They become identical in every country",
   "They revert to what they were before development",
   "They are determined entirely by climate"], ans=0,
   why="EK SPS-7.D.1 states simply that the roles of women change as countries develop economically. The claim is that the roles are a function of the economy rather than a fixed feature of a society, which is the same move EK IMP-5.C.1 makes for agriculture."),

 dict(q="What does the framework say about women in the workforce and about equity?", choices=[
   "There are more women in the workforce, and they do not have equity in wages or employment opportunities",
   "There are more women in the workforce, and they have achieved equity in wages",
   "There are fewer women in the workforce than previously",
   "Women have equity in wages but not in employment opportunities",
   "The framework makes no claim about women in the workforce"], ans=0,
   why="EK SPS-7.D.2 states that ALTHOUGH there are more women in the workforce, they do not have equity in wages or employment opportunities. Both halves are in one sentence, and reporting either alone misstates it."),

 dict(q="What does the word ALTHOUGH do in the framework's statement about women in the workforce?", choices=[
   "It marks the first clause as a real gain and the second as a limit on it, so the sentence records progress and its incompleteness together",
   "It indicates that the first clause is false",
   "It indicates that the second clause is uncertain",
   "It joins two unrelated observations",
   "It has no effect on the meaning of the sentence"], ans=0,
   why="EK SPS-7.D.2 begins with ALTHOUGH there are more women in the workforce. A concession asserts both halves while marking the second as the one that qualifies the first, which is exactly the structure learning objective SPS-7.D's phrase 'to what extent' asks students to handle."),

 dict(q="What does a lack of equity in WAGES refer to?", choices=[
   "Women earning less than men, whether for comparable work or because the occupations they predominantly hold are paid less",
   "Women being unable to open a bank account",
   "Women working fewer total hours than men",
   "Women being employed only in agriculture",
   "Women receiving identical pay to men"], ans=0,
   why="EK SPS-7.D.2 names equity in wages as one of the two things not achieved. The gap has two components -- different pay within a job and different pay between the jobs each group predominantly holds -- and a measure that captures only the first understates it."),

 dict(q="What does a lack of equity in EMPLOYMENT OPPORTUNITIES refer to?", choices=[
   "Unequal access to particular occupations and to advancement within them, so the two groups are distributed differently across the labour market",
   "Unequal pay for identical work",
   "A difference in the total number of hours worked",
   "A difference in the age at which people retire",
   "The absence of any employment for women"], ans=0,
   why="EK SPS-7.D.2 names equity in employment opportunities separately from equity in wages. Opportunity concerns which jobs are reachable and which promotions are available, which is a claim about the SHAPE of employment rather than about its price."),

 dict(q="Why has the share of women in the workforce risen as economies have developed?", choices=[
   "Falling fertility, rising education and the growth of service and office employment together made paid work outside the home both possible and available",
   "Because governments require equal numbers of each sex in every workplace",
   "Because agricultural work disappeared entirely",
   "Because men left the workforce in equal numbers",
   "Because paid work became compulsory"], ans=0,
   why="EK SPS-7.D.1 says the roles of women change as countries develop economically and EK SPS-7.D.2 records that there are more women in the workforce. Fewer years of childbearing, more schooling and a shift toward sectors that hire on credentials are the three changes that route runs through."),

 dict(q="Through what mechanisms does economic development change the roles of women?", choices=[
   "Schooling extends, fertility falls, employment shifts toward sectors hiring on qualifications, and household work is partly commercialized",
   "Development changes cultural attitudes and nothing else",
   "Development changes the climate in which people live",
   "Development changes the total population and nothing else",
   "There are no identifiable mechanisms"], ans=0,
   why="EK SPS-7.D.1 states that the roles of women change as countries develop economically without specifying how, and learning objective SPS-7.D asks HOW as well as to what extent. Each of these is a change in what is possible or required rather than a change of opinion."),

 dict(q="How does this topic connect to the framework's statement about women in agriculture?", choices=[
   "Both make women's economic role a function of the system they work within, so the role changes when the system does",
   "The two statements contradict each other",
   "The agricultural statement concerns men rather than women",
   "There is no connection between the two",
   "Both assert that women's roles are fixed"], ans=0,
   why="EK IMP-5.C.1 says the role of females in food production varies depending on the type of production involved, and EK SPS-7.D.1 says the roles of women change as countries develop economically. Both locate the explanation in the surrounding economy rather than in any fixed characteristic."),

 dict(q="How does the framework's measure of gender inequality relate to this topic's claims?", choices=[
   "The Gender Inequality Index measures reproductive health, empowerment and labour-market participation, so it puts numbers on exactly the inequity this topic describes",
   "The index measures national income rather than inequality",
   "The index has no components relating to employment",
   "The index measures only fertility",
   "The index and this topic concern unrelated subjects"], ans=0,
   why="EK SPS-7.C.2 names reproductive health, indices of empowerment and labor-market participation as the components of that measure, and EK SPS-7.D.2 says women lack equity in wages and employment opportunities. The measure and the claim are about the same conditions."),

 dict(q="What does the framework say microloans have done?", choices=[
   "Provided opportunities for women to create small local businesses, which have improved standards of living",
   "Replaced the need for any other form of finance",
   "Eliminated gender inequality in wages",
   "Reduced the number of women in the workforce",
   "Provided large loans to established companies"], ans=0,
   why="EK SPS-7.D.3 states that microloans have provided opportunities for women to create small local businesses, which have improved standards of living. The chain has three steps -- the loan, the business, the improvement -- and the framework asserts all three."),

 dict(q="Why does a very small loan reach borrowers whom conventional bank lending does not?", choices=[
   "The amounts are too small for a bank's costs to be worth incurring, and the borrowers usually have no property to offer as security",
   "Because small loans carry no risk of any kind",
   "Because banks are legally forbidden to make small loans",
   "Because small borrowers do not want bank accounts",
   "Because small loans are always repaid automatically"], ans=0,
   why="EK SPS-7.D.3 says microloans have PROVIDED OPPORTUNITIES, which implies an opportunity that did not previously exist. Assessing and administering a loan costs roughly the same whatever its size, and collateral is what a lender falls back on, so both obstacles bear hardest on the smallest borrowers."),

 dict(q="By what chain does the framework say microloans improve standards of living?", choices=[
   "The loan funds a small local business, and the income the business earns is what raises the household's standard of living",
   "The loan itself is the improvement in living standards",
   "The loan replaces the need for the household to work",
   "The loan is spent directly on consumption",
   "The framework does not say how the improvement occurs"], ans=0,
   why="EK SPS-7.D.3 says microloans provided opportunities to CREATE SMALL LOCAL BUSINESSES, WHICH have improved standards of living. The relative pronoun does the work: the businesses are what improved living standards, and the loan is what made the businesses possible."),

 dict(q="To what extent can a microloan address the inequities this topic describes?", choices=[
   "It addresses the absence of capital, and leaves untouched the wage gap and the unequal access to occupations that the framework names separately",
   "It resolves every inequity the framework names",
   "It addresses the wage gap but not the absence of capital",
   "It addresses nothing at all",
   "It addresses inequity only in wealthy countries"], ans=0,
   why="EK SPS-7.D.3 credits microloans with providing opportunities and improving standards of living, and EK SPS-7.D.2 names a lack of equity in wages and employment opportunities. Learning objective SPS-7.D asks TO WHAT EXTENT, and an instrument that supplies capital is answering one of the constraints the topic names."),

 dict(q="What does the learning objective's phrase 'and to what extent' require a student to do?", choices=[
   "Say how far economic development has contributed to gender parity, rather than only whether it has contributed at all",
   "Decide whether gender parity is desirable",
   "Establish that development has produced complete parity",
   "Establish that development has produced no parity whatever",
   "Avoid making any judgement about the evidence"], ans=0,
   why="Learning objective SPS-7.D asks students to explain how AND TO WHAT EXTENT changes in economic development have contributed to gender parity. A yes-or-no answer does not address the second half, and EK SPS-7.D.2's concession is the framework's own indication that the answer is partial."),

 dict(q="Which combination of indicators would best measure progress toward gender parity in employment?", choices=[
   "Labour force participation, the ratio of women's to men's earnings, and the distribution of each group across occupations and levels of seniority",
   "Labour force participation alone",
   "The total population of each sex",
   "The number of laws mentioning employment",
   "The average number of hours in a working week"], ans=0,
   why="EK SPS-7.D.2 names both wages and employment opportunities as areas without equity, so a measure of one does not stand in for the other. Participation says who is in the labour market, earnings say what they receive and the occupational distribution says where in it they are."),

 dict(q="Why can an unadjusted wage gap and a like-for-like wage gap give very different figures?", choices=[
   "The unadjusted gap compares all earnings and so includes the effect of women being concentrated in lower-paid occupations, which a like-for-like comparison holds constant",
   "The two measures always give identical figures",
   "The like-for-like gap is always the larger of the two",
   "Neither figure can be calculated in practice",
   "The unadjusted gap excludes women's earnings"], ans=0,
   why="EK SPS-7.D.2 names inequity in wages AND in employment opportunities as two things. Comparing like with like removes the second from the measurement, which is useful for one purpose and understates the total difference in earnings that the two together produce."),

 dict(q="Why does unpaid household and care work matter to this topic?", choices=[
   "It is work that must be done and is not counted as employment, so a group carrying more of it has less time available for paid work and for advancement in it",
   "It appears in national accounts as ordinary employment",
   "It has no bearing on paid employment",
   "It is distributed equally in every society",
   "It is counted in the wage gap already"], ans=0,
   why="EK SPS-7.D.2 says women lack equity in employment opportunities, and time is one of the constraints on opportunity. Suggested skill 3.F in the neighbouring topic makes the same point about measurement: work that is not paid for is not counted, which does not make it absent."),

 dict(q="What is occupational segregation, and why does it matter for wage equity?", choices=[
   "The concentration of each group in different occupations, which matters because those occupations are paid differently",
   "The physical separation of workers within a building",
   "A legal prohibition on certain groups holding jobs",
   "The tendency of all workers to hold the same occupation",
   "A difference in the hours worked by each group"], ans=0,
   why="EK SPS-7.D.2 names inequity in wages and in employment opportunities in the same clause, and occupational segregation is the mechanism joining them. If the two groups hold different jobs and the jobs pay differently, an earnings gap follows without any employer paying two people differently for the same work."),

 dict(q="How does the shift of employment toward the service and information sectors bear on women's participation?", choices=[
   "It expanded employment in occupations hiring on schooling and credentials, which widened the range of paid work available",
   "It reduced the total number of jobs available",
   "It confined employment to physically demanding work",
   "It had no effect on the composition of the workforce",
   "It applied only to agricultural employment"], ans=0,
   why="EK SPS-7.D.1 says the roles of women change as countries develop economically, and EK SPS-7.B.1 says the sectors are characterized by distinct development patterns. A change in which sectors are hiring is a change in what qualifications the labour market rewards."),

 dict(q="Why are education and fertility so closely bound up with changes in women's economic roles?", choices=[
   "More schooling raises what a person can earn and tends to accompany later and fewer births, which together lengthen the period available for paid work",
   "Education and fertility are unrelated to employment",
   "More schooling raises fertility rates",
   "Fertility is fixed and cannot change with development",
   "Education affects men's employment only"], ans=0,
   why="EK SPS-7.D.1 says the roles of women change as countries develop economically, and EK SPS-7.C.1 names both fertility rates and literacy among the measures of development. The two move together with development, and both bear directly on how much of a life is available for paid work."),

 dict(q="At which two scales must the framework's claims in this topic be examined?", choices=[
   "The household, where time and income are allocated between its members, and the national labour market, where wages and occupational access are set",
   "Only the national scale, since statistics are national",
   "Only the household scale, since work is divided within households",
   "The global scale only, since development is a world process",
   "No scale, since gender parity is not a spatial question"], ans=0,
   why="EK SPS-7.D.2 concerns wages and employment opportunities, which are properties of a labour market, while EK SPS-7.D.3 concerns a household business. The suggested skill for this topic is comparing quantitative data, and the two scales require different data to answer different halves of the objective."),

 dict(q="Does economic development produce gender parity automatically, on the framework's account?", choices=[
   "No -- development changes women's roles and brings more women into the workforce, and the framework states in the same breath that equity in wages and opportunities has not followed",
   "Yes, parity follows automatically once a country develops",
   "No, because development has no effect on women's roles",
   "Yes, because more women in the workforce is what parity means",
   "The framework takes no position on the question"], ans=0,
   why="EK SPS-7.D.1 says roles change with development and EK SPS-7.D.2 says that although there are more women in the workforce, equity in wages and employment opportunities has not been reached. The two statements together are the framework's answer to its own objective's 'to what extent'."),

 dict(q="Why does the distinction between formal and informal employment matter for this topic?", choices=[
   "Work outside the registered economy carries no legal protection, no recorded earnings and no career ladder, so a group concentrated in it is disadvantaged in ways a participation figure does not show",
   "Informal work pays better than formal work",
   "Informal work is fully recorded in official statistics",
   "The distinction applies only to men's employment",
   "There is no difference between the two"], ans=0,
   why="EK SPS-7.D.2 names inequity in wages and employment opportunities, and EK SPS-7.C.1 names sectoral structure BOTH FORMAL AND INFORMAL among the measures of development. Being in the labour market and being in its protected part are different things, and only the first shows in a participation rate."),

 dict(q="How can the number of women in the workforce rise substantially while equity does not follow?", choices=[
   "Entry into the labour market and position within it are different things, so a group can be well represented in employment and poorly represented in its best-paid parts",
   "It cannot; more participation necessarily produces equity",
   "Only if the total workforce shrinks",
   "Only if wages fall for everyone",
   "Only in countries that are not developing"], ans=0,
   why="EK SPS-7.D.2 states exactly this combination: ALTHOUGH there are more women in the workforce, they do not have equity in wages or employment opportunities. Counting who is in the labour market and examining where in it they are are two different questions, and the sentence answers both."),

 dict(q="Which pairing of an observation with the framework statement covering it is CORRECT?", choices=[
   "A woman borrowing a small sum to start a market stall, matched to microloans creating small local businesses",
   "A woman borrowing a small sum to start a market stall, matched to the absence of equity in wages",
   "Women earning less than men in comparable work, matched to changing roles with development",
   "Women's share of employment rising over fifty years, matched to microloans",
   "Women concentrated in lower-paid occupations, matched to microloans"], ans=0,
   why="EK SPS-7.D.1, EK SPS-7.D.2 and EK SPS-7.D.3 cover changing roles, the absence of equity, and microloans respectively. Only one pairing here places an observation under the statement that actually covers it."),

 dict(q="Four countries at different income levels are compared below. Using the accompanying figures, which conclusion is best supported?",
   table=dict(headers=["Country", "Gross National Income per person", "Female labour force participation (%)", "Ratio of women's to men's median earnings"],
     rows=[["Country 1", "1,200", "62", "0.58"],
           ["Country 2", "5,000", "45", "0.66"],
           ["Country 3", "18,000", "58", "0.78"],
           ["Country 4", "46,000", "69", "0.84"]]),
   choices=[
   "The earnings ratio rises at every step from 0.58 to 0.84 without reaching parity, while participation falls and then rises rather than tracking income",
   "Both participation and the earnings ratio rise steadily with income",
   "The earnings ratio reaches parity in the richest country",
   "Participation falls steadily as income rises",
   "Neither measure changes with income"], ans=0,
   why="The earnings ratio rises at every step from 0.58 to 0.84 and stops short of 1.00, while participation goes 62, 45, 58, 69 and so does not move with income at all. Learning objective SPS-7.D asks how and TO WHAT EXTENT development has contributed to gender parity, and a measure that improves without arriving is what a partial answer looks like."),

 dict(q="A microloan programme's outcomes are recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Measure", "Value"],
     rows=[["Borrowers", "4,200"],
           ["Share of borrowers who are women (%)", "88"],
           ["Average loan (currency units)", "220"],
           ["Businesses still operating after three years (%)", "71"],
           ["Median change in borrower household income (%)", "34"]]),
   choices=[
   "About 3,700 of the 4,200 borrowers are women, most of the businesses survive three years, and median household income rose 34 percent, which is the chain the framework describes",
   "Fewer than half the borrowers are women",
   "The average loan is large enough to fund a substantial factory",
   "Most of the businesses had closed within three years",
   "Household income fell among borrowers"], ans=0,
   why="Eighty-eight percent of 4,200 borrowers is about 3,700, the survival rate of 71 percent is a majority, and median household income rose 34 percent. EK SPS-7.D.3 says microloans provided opportunities for women to create small local businesses which have improved standards of living, and the record follows that chain from lender to household."),

 dict(q="The distribution of two groups across occupations in one country is recorded below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Occupation group", "Women (%)", "Men (%)"],
     rows=[["Senior management", "24", "76"],
           ["Professional and technical", "51", "49"],
           ["Clerical and service", "68", "32"],
           ["Craft and machine operation", "12", "88"]]),
   choices=[
   "Women are near half of professional and technical employment but only 24 percent of senior management and 12 percent of craft and machine work, so participation overall conceals a very uneven distribution across occupations",
   "Women and men are evenly distributed across all four occupation groups",
   "Women are a majority in every occupation group",
   "Men are a majority in every occupation group",
   "The rows do not sum to 100 in any occupation group"], ans=0,
   why="Each row sums to 100, and women's share runs from 68 percent in clerical and service work down to 24 in senior management and 12 in craft and machine operation. EK SPS-7.D.2 names inequity in EMPLOYMENT OPPORTUNITIES separately from wages, and an uneven distribution across occupations is what that phrase describes."),

 dict(q="What limitation should be stated when using a microloan programme's own outcome figures?", choices=[
   "The record covers borrowers who were selected or self-selected into the programme, so it cannot show what would have happened to comparable households without it",
   "Loan amounts and survival rates cannot be measured",
   "Counts and percentages can never appear in one record",
   "A programme's reported outcomes settle the question of its effect",
   "The framework forbids evaluating microloan programmes"], ans=0,
   why="EK SPS-7.D.3 credits microloans with providing opportunities and improving standards of living, and learning objective SPS-7.D asks TO WHAT EXTENT. Households that sought and obtained a loan may differ from those that did not in ways that also affect their incomes, which is a limitation of the comparison rather than of the programme."),

 dict(q="A report must state what this topic's three statements establish together. Which statement is accurate?", choices=[
   "Development changes women's economic roles and has brought more women into paid work, equity in wages and occupational access has not followed, and microloans have opened one route to a small business and a better standard of living",
   "Development has produced full gender parity in wages and employment",
   "Development has had no effect on women's economic roles",
   "Microloans have resolved the inequities in wages and employment opportunities",
   "The framework records more women in the workforce and nothing further"], ans=0,
   why="EK SPS-7.D.1 supplies the changing roles, EK SPS-7.D.2 the gain and its limit in one sentence, and EK SPS-7.D.3 the microloan route. Each rejected summary either claims a parity the framework denies, denies a change the framework asserts, or drops the concession that answers the objective's 'to what extent'."),
]
