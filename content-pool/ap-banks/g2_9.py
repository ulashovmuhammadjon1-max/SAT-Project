# AP HUMAN GEOGRAPHY 2.9 Aging Populations -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding SPS-2; learning
# objective SPS-2.C, "Explain the causes and consequences of an aging
# population."
#
# Essential knowledge, in full -- two statements, causes then consequences:
#   SPS-2.C.1  Population aging is determined by birth and death rates and life
#              expectancy.
#   SPS-2.C.2  An aging population has political, social, and economic
#              consequences, including the dependency ratio.
#
# SPS-2.C.1 names THREE determinants and the first is the one students omit.
# Aging is usually pictured as people living longer, but the larger driver is
# fewer births: a smaller cohort entering at the bottom raises the share of
# every older cohort without anyone living a day longer. Items 1, 2, 5, 11, 15
# and 26 turn on that, and item 2 asks about it directly.
#
# SPS-2.C.2 names three domains -- political, social, economic -- and singles
# out ONE measure, the dependency ratio. The definitions this module holds
# itself to, since the CED names the ratio without printing its formula:
#
#   total dependency ratio   = (population under 15 + population 65 and over)
#                              divided by population 15-64, times 100
#   youth dependency ratio   = population under 15 / population 15-64, times 100
#   elderly dependency ratio = population 65 and over / population 15-64,
#                              times 100
#
# Two consequences of that definition carry several items and are argued rather
# than cited. First, the TOTAL ratio can be identical in a very young country
# and a very old one while its composition is entirely different, so the ratio
# alone cannot tell you which kind of country you are looking at -- items 9, 17
# and 27 rest on this. Second, the ratio is an arithmetic construct with fixed
# age cut-offs, so a country in which many people work past 65 or study past 20
# has a measured ratio that misdescribes its real burden -- items 13 and 22.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_9.py. FIVE choices (A-E).
TOPIC = ("2.9", "Aging Populations", 2)

QUESTIONS = [
 dict(q="Which combination of demographic factors determines whether a population ages?",
   choices=[
     "Birth rates, death rates, and life expectancy",
     "Birth rates and land area",
     "Migration and population density",
     "Life expectancy alone",
     "Death rates and total population size"],
   ans=0,
   why="EK SPS-2.C.1 names exactly these three determinants of population aging. Aging is a change in the SHARE of a population that is old, so it depends on how many people are being added at the bottom as much as on how long those already alive survive."),

 dict(q="Which of the two main drivers usually contributes more to a country's population aging?",
   choices=[
     "Falling fertility, because a smaller cohort at the bottom raises every older cohort's share without anyone living longer",
     "Rising life expectancy, because aging means people living longer by definition",
     "Rising mortality, because more deaths mean an older population",
     "Immigration, because migrants are usually elderly",
     "Neither; aging occurs independently of birth and death rates"],
   ans=0,
   why="EK SPS-2.C.1 lists birth rates first among the determinants. Aging is measured as a proportion, and a proportion rises either because its numerator grows or because its denominator shrinks; sustained low fertility shrinks the denominator every year."),

 dict(q="The total dependency ratio is calculated as",
   choices=[
     "The population under 15 plus the population 65 and over, divided by the population aged 15 to 64, times 100",
     "The population 65 and over divided by the total population, times 100",
     "The population aged 15 to 64 divided by the total population, times 100",
     "The population under 15 divided by the population 65 and over, times 100",
     "The number of retired people divided by the number of employed people, times 100"],
   ans=0,
   why="EK SPS-2.C.2 names the dependency ratio as a consequence measure without printing its formula, and the standard construction puts both dependent age groups over the working ages. Using the total population as the denominator would give a share rather than a ratio of dependents to workers."),

 dict(q="A country reports 24 million people under 15, 60 million aged 15 to 64, and 16 million aged 65 and over. What is its total dependency ratio?",
   choices=[
     "About 67, since 40 million dependents are supported by 60 million people of working age",
     "About 40, since dependents are 40 percent of the population",
     "About 27, since 16 million of 60 million are elderly",
     "About 150, since 60 million divided by 40 million is 1.5",
     "About 100, since the dependent and working populations are equal"],
   ans=0,
   why="Adding 24 and 16 million gives 40 million dependents, and 40 over 60 is 0.667, or about 67 per hundred people of working age. The distractors compute a share of the total, one of the two component ratios, and the reciprocal."),

 dict(q="Two countries have the same total dependency ratio of 60. One has a ratio built almost entirely of children, the other almost entirely of people over 65. What follows?",
   choices=[
     "They face very different spending needs, since one ratio implies schools and the other implies pensions and health care",
     "They face identical spending needs, since the ratio is the same",
     "One of the two ratios must have been calculated incorrectly",
     "The younger country's ratio will fall faster",
     "The ratio cannot be the same for a young and an old population"],
   ans=0,
   why="The total ratio adds two very different groups into one figure, so an identical value is compatible with opposite compositions. EK SPS-2.C.2 names the ratio among the consequences of aging, and reading it without decomposing it is how a young country and an old one get mistaken for each other."),

 dict(q="An aging population raises which economic pressure most directly?",
   choices=[
     "The cost of pensions and health care falls on a working-age population that is not growing, so each worker supports more",
     "The cost of primary schooling rises sharply",
     "The demand for maternity services rises sharply",
     "The country's land area must be expanded",
     "The country's arithmetic density necessarily falls"],
   ans=0,
   why="EK SPS-2.C.2 names economic consequences among the effects of an aging population. Pension and health systems transfer resources from workers to the retired, so a rising elderly share and a flat working-age population raise the transfer required from each worker."),

 dict(q="Which is a SOCIAL rather than an economic or political consequence of an aging population?",
   choices=[
     "More households in which an adult child provides daily care for an aging parent, often alongside paid work",
     "A rise in the share of the national budget spent on pensions",
     "Older voters forming a larger share of the electorate",
     "A shortage of workers in physically demanding trades",
     "A fall in tax revenue from income"],
   ans=0,
   why="EK SPS-2.C.2 lists political, social and economic consequences as three separate domains. Budgets, tax revenue and labour shortages are economic and the composition of the electorate is political, while the reorganization of family life around care is social."),

 dict(q="Which is a POLITICAL consequence of an aging population?",
   choices=[
     "Policies favouring pensioners become harder to change because older voters turn out in large numbers",
     "The number of nursing home places must rise",
     "Health care spending rises as a share of output",
     "Families spend more time caring for elderly relatives",
     "The labour force shrinks relative to the population"],
   ans=0,
   why="EK SPS-2.C.2 names political consequences separately from social and economic ones. Where an age group is both large and reliably participating, the policies serving it acquire a constituency that makes reform electorally costly."),

 dict(q="Which policy response to an aging population acts on the DENOMINATOR of the dependency ratio?",
   choices=[
     "Raising the statutory retirement age, which moves people from the dependent group into the working-age group",
     "Increasing the size of pension payments",
     "Building more residential care facilities",
     "Extending the school leaving age",
     "Expanding home visits by nurses"],
   ans=0,
   why="The ratio's denominator is the population counted as of working age, so redefining where that band ends adds people to it and subtracts them from the numerator at the same time. Larger pensions, more care places and longer schooling change the cost or the numerator instead."),

 dict(q="A country facing labour shortages from aging adopts a selective immigration programme. Why does this work faster than pronatalist measures?",
   choices=[
     "Admitted adults enter the working-age population immediately, while a child born today joins it in about twenty years",
     "Immigrants have higher fertility than residents in every country",
     "Immigration reduces the number of elderly residents",
     "Pronatalist measures reduce the working-age population",
     "Immigration lowers life expectancy"],
   ans=0,
   why="Both instruments act on the working-age population but on completely different timescales, and an aging country's shortage is present rather than future. EK SPS-2.C.2's economic consequences are what the country is trying to relieve, and only one lever relieves them now."),

 dict(q="A country's life expectancy has been stable for twenty years while its fertility has fallen from 2.1 to 1.3. What will happen to its age structure?",
   choices=[
     "It will age substantially, because each entering cohort is smaller than the one before even though no one lives longer",
     "It will not age, since life expectancy has not risen",
     "It will become younger, since fewer old people are being added",
     "Nothing can be said without the mortality rate",
     "It will age only if immigration stops"],
   ans=0,
   why="EK SPS-2.C.1 makes birth rates a determinant of aging in their own right. A shrinking base raises the share held by every cohort above it, so a population can age rapidly with no change in how long its members live."),

 dict(q="Which measure would tell a government most about the burden its elderly population places on its workers specifically?",
   choices=[
     "The elderly dependency ratio, which relates the population 65 and over to the population aged 15 to 64",
     "The total dependency ratio, which combines the young and the old",
     "The share of the population under 15",
     "The country's crude birth rate",
     "The country's arithmetic population density"],
   ans=0,
   why="EK SPS-2.C.2 names the dependency ratio, and the elderly component is the part that isolates the group in question. The total ratio mixes in children, whose costs fall on different budgets and end at a known age."),

 dict(q="Why can a measured dependency ratio misstate the real economic burden a country carries?",
   choices=[
     "Its age cut-offs are fixed, so people working past 65 are counted as dependent and people studying past 20 are counted as workers",
     "The ratio cannot be calculated for large countries",
     "Population data are never accurate enough to compute it",
     "The ratio counts only people who are employed",
     "The ratio changes every day and cannot be compared"],
   ans=0,
   why="The construction assumes everyone between two ages works and no one outside them does, which is an approximation rather than a measurement. Where labour force participation departs from that assumption, the ratio and the real burden move apart."),

 dict(q="A country's population is stable in total but its median age has risen by twelve years in two decades. Which pair of causes is most likely?",
   choices=[
     "Sustained low fertility together with rising life expectancy",
     "Rising fertility together with falling life expectancy",
     "High immigration of young workers together with rising fertility",
     "A fall in life expectancy together with a rise in births",
     "An increase in the country's land area"],
   ans=0,
   why="EK SPS-2.C.1 names birth rates, death rates and life expectancy as the determinants, and only one combination of them raises median age while holding the total steady. Fewer entrants at the bottom and more survivors at the top both push the median upward."),

 dict(q="Which statement about aging and the labour force is most accurate?",
   choices=[
     "As large cohorts retire and smaller ones enter, the working-age population can shrink even while total population is stable",
     "The labour force always grows with the total population",
     "Aging has no effect on the size of the labour force",
     "The labour force shrinks only when total population shrinks",
     "Retirement has no effect on labour force size"],
   ans=0,
   why="The working-age band is fed at one end and drained at the other, so its size depends on the relative sizes of the entering and exiting cohorts rather than on the total. A large cohort leaving and a small one arriving shrinks it regardless of what the total does."),

 dict(q="A rural district's population is aging much faster than its country's. What is the most likely cause?",
   choices=[
     "Out-migration of young adults, which removes people from the base and takes their future children with them",
     "In-migration of young workers",
     "A rise in the district's birth rate",
     "A fall in the district's life expectancy",
     "An increase in the district's land area"],
   ans=0,
   why="At the subnational scale migration reshapes age structure faster than fertility or mortality can, and it is selective by age. The district loses the cohort that would have had children as well as the cohort itself, which ages it twice over."),

 dict(q="Two countries have total dependency ratios of 85 and 52. Which conclusion is NOT safe to draw?",
   choices=[
     "That the country with the ratio of 85 has an older population",
     "That the country with the ratio of 85 has more dependents per worker",
     "That both countries have some dependent population",
     "That the ratios can be compared only if both use the same age bands",
     "That the difference implies different fiscal pressures"],
   ans=0,
   why="A high total ratio can come from many children or many elderly people, so the total alone does not identify which. EK SPS-2.C.2 names the ratio as a consequence measure, and using it to infer age structure requires decomposing it first."),

 dict(q="Which of the following would reduce a country's total dependency ratio without changing anyone's age?",
   choices=[
     "Admitting a large number of working-age immigrants",
     "Raising pension payments",
     "Improving elderly health care",
     "Increasing the birth rate",
     "Extending life expectancy"],
   ans=0,
   why="The ratio compares two age groups, so adding people to the working-age band lowers it directly. Raising births adds to the numerator, extending life expectancy adds to the numerator later, and better care or larger pensions change costs without changing counts."),

 dict(q="Why does an aging population create pressure on a pay-as-you-go pension system in particular?",
   choices=[
     "Current workers' contributions fund current pensions, so a falling ratio of workers to pensioners must be met by higher contributions, lower benefits, or later retirement",
     "Such systems invest contributions and are unaffected by age structure",
     "Such systems pay only people under 65",
     "Such systems are funded entirely by the elderly themselves",
     "Aging populations pay more tax than young ones"],
   ans=0,
   why="EK SPS-2.C.2 names economic consequences including the dependency ratio, and a pay-as-you-go system makes that ratio the system's own arithmetic. When each pensioner is supported by fewer workers, one of the three terms has to give."),

 dict(q="Which observation would best indicate that a country is at an early stage of aging rather than an advanced one?",
   choices=[
     "Its share over 65 is still under 10 percent but its fertility has been below replacement for a decade",
     "Its share over 65 is above 25 percent",
     "Its median age is above 48",
     "Its working-age population has been shrinking for twenty years",
     "Its dependency ratio is dominated by the elderly"],
   ans=0,
   why="EK SPS-2.C.1 makes low fertility a determinant of aging that acts with a long lag, so the commitment to an older future is made years before the older population appears. A small elderly share with entrenched low fertility is the early stage of exactly that process."),

 dict(q="A geographer says an aging country's problem is 'not that people live too long but that too few were born.' Which framework statement does this restate?",
   choices=[
     "That population aging is determined by birth rates as well as by death rates and life expectancy",
     "That aging has political consequences",
     "That the dependency ratio measures aging",
     "That migration determines age structure",
     "That aging is unrelated to fertility"],
   ans=0,
   why="EK SPS-2.C.1 lists birth rates among the determinants of aging alongside death rates and life expectancy. The remark is a compressed statement of the first determinant, and it is worth making because the popular account leaves it out."),

 dict(q="A country with an aging population raises its retirement age from 62 to 67. Which pair of effects follows?",
   choices=[
     "The measured dependency ratio falls and the real burden falls too, provided older workers can actually find and keep work",
     "The measured ratio falls and the real burden necessarily falls with it",
     "The measured ratio rises",
     "Neither the measured ratio nor the real burden changes",
     "The measured ratio falls but the number of people over 65 also falls"],
   ans=0,
   why="Moving the age boundary is an arithmetic change to the ratio, and whether it changes the underlying economics depends on employment at those ages. Stating the condition is what separates an honest answer from one that confuses a definition with an outcome."),

 dict(q="Which of these best explains why aging is happening in nearly every world region, though at different speeds?",
   choices=[
     "Fertility has fallen and life expectancy has risen almost everywhere, though both began at different levels and moved at different times",
     "Every country has adopted the same population policy",
     "The world's total population has stopped growing",
     "Migration has ceased between world regions",
     "Aging is confined to wealthy countries"],
   ans=0,
   why="EK SPS-2.C.1's three determinants have all moved in the aging direction across most of the world, and the differences between regions are differences of timing and starting point rather than of direction. That is why the process is nearly universal but nowhere synchronized."),

 dict(q="A country's elderly dependency ratio is 12 while its youth dependency ratio is 68. What kind of country is this most likely to be?",
   choices=[
     "One with high fertility and a young population, facing pressure on schools rather than on pensions",
     "One with an aging population facing pension pressure",
     "One with a shrinking population",
     "One with very high life expectancy and low fertility",
     "One with equal numbers of children and elderly people"],
   ans=0,
   why="Decomposing the total ratio identifies the source of the burden, and a youth component nearly six times the elderly one places the country firmly at the young end. EK SPS-2.C.2 names the ratio as the measure, and reading its parts is what makes it informative."),

 dict(q="Which combination of responses to aging acts on all three of the framework's consequence domains?",
   choices=[
     "Raising the retirement age, funding home care so families can keep working, and reforming pension entitlements through legislation",
     "Building more roads and airports",
     "Redrawing the country's internal boundaries",
     "Publishing more detailed population statistics",
     "Increasing the country's total land area"],
   ans=0,
   why="EK SPS-2.C.2 names political, social and economic consequences, and the three measures listed address one of each: the labour supply, the burden on families, and the legislated entitlement. A response confined to one domain leaves the others untouched."),

 dict(q="A country's population by broad age group is shown. Using the table, what is its total dependency ratio?",
   table=dict(
     headers=["Age group", "Population (millions)"],
     rows=[
       ["Under 15", "9.0"],
       ["15-64", "40.0"],
       ["65 and over", "11.0"]]),
   choices=[
     "50, since 20 million dependents are supported by 40 million people of working age",
     "20, since there are 20 million dependents",
     "33, since 20 million is one third of the total population",
     "200, since 40 million divided by 20 million is 2",
     "27.5, since 11 million divided by 40 million is 0.275"],
   ans=0,
   why="Nine plus eleven gives 20 million dependents against 40 million of working age, which is 50 per hundred workers. The distractors report the raw count, the share of the total, the reciprocal, and the elderly component alone."),

 dict(q="Two countries' age structures are shown. Using the table, which statement is best supported?",
   table=dict(
     headers=["Age group", "Country A (millions)", "Country B (millions)"],
     rows=[
       ["Under 15", "18.0", "4.0"],
       ["15-64", "30.0", "30.0"],
       ["65 and over", "3.0", "17.0"]]),
   choices=[
     "Both have a total dependency ratio of 70, but one is driven by children and the other by people over 65",
     "Country A has the higher total dependency ratio",
     "Country B has the higher total dependency ratio",
     "The two countries have identical age structures",
     "Neither country's ratio can be calculated from the table"],
   ans=0,
   why="Both countries have 21 million dependents against 30 million of working age, which is 70 per hundred in each case, yet one has 18 million children to 3 million elderly and the other has the reverse. An identical total concealing opposite compositions is exactly why the ratio has to be decomposed."),

 dict(q="A country's age structure is projected forward. Using the table, what is happening to the elderly dependency ratio?",
   table=dict(
     headers=["Year", "Population 15-64 (millions)", "Population 65 and over (millions)"],
     rows=[
       ["2000", "50.0", "10.0"],
       ["2020", "48.0", "16.0"],
       ["2040", "40.0", "24.0"]]),
   choices=[
     "It rises from 20 to 60 per hundred workers, because the elderly population grows while the working-age population shrinks",
     "It falls, because the working-age population is shrinking",
     "It stays constant, because both figures change",
     "It rises from 10 to 24 per hundred workers",
     "It cannot be calculated without the number of children"],
   ans=0,
   why="Dividing the elderly by the working-age population gives 20, 33 and 60 per hundred, so the ratio triples over forty years. Both terms move in the directions that raise it, which is why the rise is far larger than the growth of the elderly population alone."),

 dict(q="Four countries' fertility histories and elderly shares are shown. Using the table, which country is aging fastest despite still having a small elderly share?",
   table=dict(
     headers=["Country", "Fertility 25 years ago", "Fertility now", "Share 65 and over now (%)"],
     rows=[
       ["Country P", "2.1", "2.0", "19"],
       ["Country Q", "5.9", "1.4", "8"],
       ["Country R", "1.9", "1.8", "22"],
       ["Country S", "6.2", "5.4", "3"]]),
   choices=[
     "Country Q, whose fertility fell by 4.5 children per woman in a generation while its elderly share is still only 8 percent",
     "Country R, which has the largest elderly share in the table",
     "Country P, whose fertility is closest to replacement",
     "Country S, whose fertility is the highest in the table",
     "None of them, since aging depends only on life expectancy"],
   ans=0,
   why="Falls of 0.1, 4.5, 0.1 and 0.8 children per woman make one country's fertility collapse an order of magnitude larger than any other's, and its small elderly share means the consequence is still ahead of it. EK SPS-2.C.1 makes birth rates a determinant of aging, and a fall of that size commits a country to a rapid rise in its elderly share."),

 dict(q="Public spending by category is shown for two countries with the same total population. Using the table, which country is the older one?",
   table=dict(
     headers=["Spending category", "Country X (% of budget)", "Country Y (% of budget)"],
     rows=[
       ["Primary and secondary education", "26", "11"],
       ["Pensions", "7", "31"],
       ["Health care for those over 65", "5", "22"],
       ["All other spending", "62", "36"]]),
   choices=[
     "Country Y, which devotes 53 percent of its budget to pensions and elderly health care against 12 percent in the other",
     "Country X, which spends more on education",
     "Country Y, because its other spending is lower",
     "Country X, because its pension spending is lower",
     "Neither, since budget shares say nothing about age structure"],
   ans=0,
   why="Both columns sum to 100 percent, so only composition is comparable, and 31 plus 22 gives 53 percent for the age-related categories against 7 plus 5 in the other country. EK SPS-2.C.2 names economic consequences of aging, and a budget is where those consequences become visible."),
]
