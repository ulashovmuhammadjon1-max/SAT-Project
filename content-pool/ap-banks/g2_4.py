# AP HUMAN GEOGRAPHY 2.4 Population Dynamics -- 30 questions
# CED Course Framework V.1, Unit 2. Enduring understanding IMP-2, "Changes in
# population are due to mortality, fertility, and migration, which are
# influenced by the interplay of environmental, economic, cultural, and
# political factors."
#
# Learning objective IMP-2.A, "Explain factors that account for contemporary and
# historical trends in population growth and decline."
#   IMP-2.A.1  Demographic factors that determine a population's growth and
#              decline are fertility, mortality, and migration.
#   IMP-2.A.2  Geographers use the rate of natural increase and
#              population-doubling time to explain population growth and decline.
#   IMP-2.A.3  Social, cultural, political, and economic factors influence
#              fertility, mortality, and migration rates.
#
# IMP-2.A.1 gives a closed list of THREE components, and the most common student
# error is dropping the third: natural increase is births minus deaths and says
# nothing about migration, so a country can have positive natural increase and a
# falling population, or the reverse. Items 3, 9, 14, 21 and 28 turn on exactly
# that.
#
# IMP-2.A.2 names two measures by name, and this module uses their standard
# definitions. The CED does not print the formulas, so items computing them
# argue from the arithmetic rather than citing a code:
#   crude birth rate      births per 1,000 people per year
#   crude death rate      deaths per 1,000 people per year
#   rate of natural increase (percent) = (crude birth rate - crude death rate) / 10
#   doubling time (years) = 70 / rate of natural increase in percent
#   total fertility rate  average births per woman over a lifetime; about 2.1 is
#                         the replacement level in a low-mortality country
#   net migration rate    immigrants minus emigrants, per 1,000 people
#   overall growth rate   rate of natural increase plus net migration rate
#
# IMP-2.A.3 is the sentence that makes this a geography topic rather than an
# arithmetic one: rates are outcomes of social, cultural, political and economic
# conditions, not brute facts. Items 5, 11, 15, 17, 22, 24 and 25 are keyed to
# it.
#
# The doubling-time rule of 70 is an approximation and every item using it says
# so, because presenting an approximation as exact is its own kind of wrong key.
#
# Five items carry a real `table=`; each one's arithmetic is recomputed from the
# table in verify_g2_4.py. FIVE choices (A-E).
TOPIC = ("2.4", "Population Dynamics", 2)

QUESTIONS = [
 dict(q="Which three demographic processes together determine whether a country's population grows or declines?",
   choices=[
     "Fertility, mortality, and migration",
     "Fertility, mortality, and urbanization",
     "Birth rate, literacy, and life expectancy",
     "Migration, industrialization, and mortality",
     "Fertility, migration, and population density"],
   ans=0,
   why="EK IMP-2.A.1 names exactly these three as the demographic factors determining growth and decline. Urbanization, literacy, industrialization and density may influence those three, but none of them adds or removes a person from a national total by itself."),

 dict(q="A country records 22 births and 8 deaths per 1,000 people in a year. What is its rate of natural increase?",
   choices=[
     "1.4 percent",
     "14 percent",
     "0.14 percent",
     "30 percent",
     "It cannot be found without the migration figures"],
   ans=0,
   why="Natural increase is births minus deaths, so 22 minus 8 leaves 14 per 1,000, and 14 per 1,000 is 1.4 percent. Migration is excluded by definition, which is why the figure can be computed from the two rates alone."),

 dict(q="A country's rate of natural increase is positive, yet its total population fell last year. What must be true?",
   choices=[
     "Net out-migration exceeded the surplus of births over deaths",
     "The rate of natural increase was miscalculated",
     "Deaths exceeded births",
     "The country's fertility rate is zero",
     "This situation is impossible"],
   ans=0,
   why="EK IMP-2.A.1 lists migration alongside fertility and mortality, and natural increase measures only the first two. A larger outflow than the natural surplus is the one way the total can fall while natural increase stays positive."),

 dict(q="Using the rule of 70, roughly how long would a population growing at 2 percent a year take to double?",
   choices=[
     "About 35 years",
     "About 70 years",
     "About 140 years",
     "About 20 years",
     "About 2 years"],
   ans=0,
   why="EK IMP-2.A.2 names population-doubling time as a measure geographers use, and the standard approximation divides 70 by the growth rate expressed as a percent. Seventy over two is thirty-five, and the rule is an approximation rather than an exact result."),

 dict(q="Which explanation for falling fertility best matches the framework's claim that social and economic factors influence demographic rates?",
   choices=[
     "As education and paid employment for women expand and children become costly to raise, families choose to have fewer of them",
     "Fertility falls automatically once a country reaches a certain population",
     "Fertility is fixed by climate",
     "Fertility falls only where governments prohibit large families",
     "Fertility is unrelated to economic conditions"],
   ans=0,
   why="EK IMP-2.A.3 states that social, cultural, political and economic factors influence fertility, mortality and migration rates. Education, employment and the cost of raising a child are exactly such factors, and they act through household decisions rather than by decree."),

 dict(q="Two countries have the same rate of natural increase, but one is growing rapidly and the other is shrinking. The difference must lie in",
   choices=[
     "Net migration, the third component of population change",
     "Their total land areas",
     "Their population densities",
     "The accuracy of their censuses",
     "Their crude birth rates, which must differ"],
   ans=0,
   why="EK IMP-2.A.1 makes population change the sum of three components, and two of them are held equal by the premise. With natural increase identical, only the migration term can produce opposite outcomes."),

 dict(q="A country's crude death rate is higher than that of a poorer country with worse health care. What is the most likely explanation?",
   choices=[
     "The richer country has a much older age structure, and crude death rates are not adjusted for age",
     "The richer country's health care is worse than reported",
     "The poorer country has stopped recording deaths",
     "Crude death rates cannot be compared between countries",
     "The richer country must have a higher birth rate as well"],
   ans=0,
   why="A crude rate divides events by the whole population without regard to its composition, so a population concentrated in the old ages produces many deaths per thousand however good its medicine. Comparing crude rates between differently aged populations is the classic trap."),

 dict(q="Total fertility rate is best described as",
   choices=[
     "The average number of children a woman would bear over her lifetime at current age-specific rates",
     "The number of births per 1,000 people in a year",
     "The share of women who have at least one child",
     "The number of children currently alive per household",
     "The number of births minus deaths per 1,000 people"],
   ans=0,
   why="The measure is constructed by applying this year's fertility at each age to a hypothetical woman passing through all of them, which is why it is stated per woman rather than per thousand people. That construction is what makes it comparable between countries with different age structures."),

 dict(q="A country's total fertility rate has been 1.4 for twenty years, yet its population has continued to grow. Which explanation is most likely?",
   choices=[
     "Immigration and population momentum from large earlier cohorts have outweighed below-replacement fertility",
     "A fertility rate of 1.4 is above replacement",
     "The fertility rate must have been recorded incorrectly",
     "Deaths have fallen to zero",
     "Fertility rates do not affect population size"],
   ans=0,
   why="EK IMP-2.A.1 makes migration a component of change alongside fertility and mortality, and a large cohort already in the childbearing ages produces many births even at a low rate. Both mechanisms can sustain growth well after fertility falls below replacement."),

 dict(q="Which change would raise a country's rate of natural increase without any change in its birth rate?",
   choices=[
     "A fall in the death rate produced by improved sanitation and vaccination",
     "An increase in immigration",
     "An increase in emigration",
     "An increase in the country's land area",
     "A rise in the average age at marriage"],
   ans=0,
   why="Natural increase is births minus deaths, so with births fixed only the death term can move it, and it moves the rate up when it falls. Migration changes total population without entering the natural increase calculation at all."),

 dict(q="A government's expansion of childhood vaccination is followed by a sharp fall in the death rate and, for two decades, faster population growth. Which framework statement explains the link?",
   choices=[
     "Political and economic factors influence mortality rates, and mortality is one of the three components of population change",
     "Vaccination raises fertility directly",
     "Vaccination is a form of migration",
     "Population growth is unrelated to mortality",
     "Only fertility can change a population's size"],
   ans=0,
   why="EK IMP-2.A.3 makes political and economic factors act on mortality, and EK IMP-2.A.1 makes mortality one of the three determinants of growth. A programme that saves lives widens the gap between births and deaths without touching births."),

 dict(q="Which figure would tell a geographer most about how quickly a rapidly growing population will strain existing schools and clinics?",
   choices=[
     "The doubling time implied by the current growth rate",
     "The country's total land area",
     "The country's arithmetic population density",
     "The number of years since the last census",
     "The country's sex ratio"],
   ans=0,
   why="EK IMP-2.A.2 names population-doubling time as one of the measures geographers use to explain growth. Expressing a growth rate as the number of years until the population is twice its present size converts an abstract percentage into a planning horizon."),

 dict(q="Population A grows at 0.5 percent a year and Population B at 3.5 percent. Using the rule of 70, how do their doubling times compare?",
   choices=[
     "About 140 years against about 20 years, so B doubles seven times faster",
     "About 20 years against about 140 years, so A doubles faster",
     "Both double in about 70 years",
     "Neither will ever double",
     "The doubling times cannot be compared across countries"],
   ans=0,
   why="Seventy divided by 0.5 is 140 and seventy divided by 3.5 is 20, and the ratio of the two doubling times is the inverse of the ratio of the growth rates. Small differences in an annual percentage produce very large differences over a human lifetime."),

 dict(q="Which of the following is NOT a component of population change as the framework defines it?",
   choices=[
     "Urbanization",
     "Fertility",
     "Mortality",
     "Immigration",
     "Emigration"],
   ans=0,
   why="EK IMP-2.A.1 names fertility, mortality and migration, and migration covers movement in both directions. Moving from a rural district to a city inside the same country redistributes a national population without changing its size."),

 dict(q="A country's fertility falls sharply within a single generation. Which combination of causes best matches the framework's account?",
   choices=[
     "Rising female education and employment, later marriage, urban living costs, and wider access to contraception acting together",
     "A change in the country's climate",
     "A fall in the country's population density",
     "An increase in the country's total land area",
     "A change in the method used to count births"],
   ans=0,
   why="EK IMP-2.A.3 attributes fertility rates to social, cultural, political and economic factors. Fertility declines of that speed are consistently associated with the same cluster of household-level changes rather than with any single cause."),

 dict(q="Why is the crude birth rate a poorer measure than the total fertility rate for comparing two countries' childbearing?",
   choices=[
     "The crude rate depends on how many women of childbearing age the population happens to contain, while the fertility rate does not",
     "The crude rate is measured over a longer period",
     "The crude rate counts only first births",
     "The crude rate cannot be calculated for large countries",
     "The two measures always give the same ranking"],
   ans=0,
   why="Dividing births by the whole population makes the result depend on age structure, so a young population records a high crude rate even at moderate fertility. The lifetime measure removes that dependence, which is why it travels better between countries."),

 dict(q="A war reduces a country's population by 4 percent in three years. Which components of population change are involved?",
   choices=[
     "Mortality directly, and migration as refugees leave, with fertility usually falling as well",
     "Only mortality, since war causes deaths",
     "Only migration, since people flee",
     "Neither mortality nor migration, since war is a political event",
     "Only fertility, since births are postponed"],
   ans=0,
   why="EK IMP-2.A.1's three components are not mutually exclusive, and a war moves all of them: it raises deaths, drives departures, and separates or impoverishes couples so that births are postponed. EK IMP-2.A.3 makes the political factor the common cause."),

 dict(q="A country's population is projected to double in about 23 years. What is its approximate annual growth rate under the rule of 70?",
   choices=[
     "About 3 percent",
     "About 0.3 percent",
     "About 23 percent",
     "About 47 percent",
     "About 1 percent"],
   ans=0,
   why="The rule of 70 relates doubling time and growth rate reciprocally, so a doubling time of about 23 years implies a rate of about 70 divided by 23, which is close to 3 percent. The approximation runs in both directions."),

 dict(q="Which statement about the relationship between fertility and mortality decline is best supported?",
   choices=[
     "Mortality usually falls before fertility does, and the gap between them is when population grows fastest",
     "Fertility always falls before mortality",
     "The two always fall together at the same speed",
     "Neither falls without government action",
     "A fall in mortality causes an immediate fall in fertility"],
   ans=0,
   why="Death rates respond quickly to public health, sanitation and food supply, while birth rates respond to household decisions that shift over a generation. The interval in which deaths have fallen and births have not is arithmetically the period of maximum natural increase."),

 dict(q="Which of these is the strongest reason a national growth rate can conceal very different local trends?",
   choices=[
     "Internal migration moves people between regions without changing the national total, so growing and shrinking places can sum to a stable country",
     "National growth rates are always inaccurate",
     "Local populations are not counted",
     "Growth rates apply only at the national scale",
     "Local trends always match the national one"],
   ans=0,
   why="EK IMP-2.A.1 makes migration one of the three components, and internal moves are additions in one place and subtractions in another. The national figure nets them to zero while the local figures record the full movement."),

 dict(q="A country records a crude birth rate of 11, a crude death rate of 10, and a net migration rate of plus 6 per 1,000. What is its approximate annual growth rate?",
   choices=[
     "0.7 percent, since natural increase of 0.1 percent and net migration of 0.6 percent are added",
     "0.1 percent, since only natural increase counts",
     "1.7 percent, since all three rates are added",
     "0.6 percent, since migration outweighs natural increase entirely",
     "Minus 0.5 percent, since the death rate is close to the birth rate"],
   ans=0,
   why="Natural increase is 11 minus 10, or 1 per 1,000, and net migration adds a further 6 per 1,000, giving 7 per 1,000 in total, which is 0.7 percent. Adding the death rate as though it were a third positive term is the error the largest distractor represents."),

 dict(q="A government offers cash payments and extended parental leave to families having a third child, and fertility rises modestly. This illustrates which framework claim?",
   choices=[
     "That political and economic factors influence fertility rates",
     "That fertility rates cannot be changed",
     "That migration determines fertility",
     "That fertility is determined by mortality",
     "That fertility responds only to cultural factors"],
   ans=0,
   why="EK IMP-2.A.3 names political and economic factors among those influencing fertility, and a subsidy is both. The modest size of the response is itself informative, since it shows the policy acting on one input among many."),

 dict(q="Which comparison correctly distinguishes the rate of natural increase from the overall population growth rate?",
   choices=[
     "Natural increase counts only births and deaths, while the growth rate also includes net migration",
     "Natural increase includes migration and the growth rate does not",
     "The two are always identical",
     "Natural increase applies to regions and the growth rate to countries",
     "The growth rate counts only births"],
   ans=0,
   why="EK IMP-2.A.2 names the rate of natural increase specifically, and EK IMP-2.A.1 makes migration a separate component of change. The two measures coincide only where net migration happens to be zero."),

 dict(q="Which pairing of a demographic rate with a plausible cause best matches the framework's account of what shapes rates?",
   choices=[
     "A falling infant mortality rate paired with expanded prenatal care and clean water supply",
     "A falling infant mortality rate paired with an increase in national land area",
     "A rising birth rate paired with a change in map projection",
     "A rising death rate paired with an increase in literacy",
     "A falling migration rate paired with a change in the census date"],
   ans=0,
   why="EK IMP-2.A.3 attributes demographic rates to social, cultural, political and economic factors, and prenatal care and water supply are exactly such conditions acting on infant survival. The other pairings connect a rate to something with no mechanism linking them."),

 dict(q="A country's emigration is concentrated among young adults. Beyond the immediate loss of people, what is the most important demographic consequence?",
   choices=[
     "Births fall in later years because many of the people who would have had children are no longer there",
     "The death rate falls to zero",
     "The country's land area shrinks",
     "The total fertility rate rises automatically",
     "Emigration has no effect beyond the year it occurs"],
   ans=0,
   why="EK IMP-2.A.1's three components interact: removing people of childbearing age removes their future births as well as themselves. The effect on the birth count persists for decades even if the fertility rate per woman does not change at all."),

 dict(q="Four countries' vital rates are shown. Using the table, which country has the highest rate of natural increase?",
   table=dict(
     headers=["Country", "Crude birth rate (per 1,000)", "Crude death rate (per 1,000)"],
     rows=[
       ["Country A", "34", "9"],
       ["Country B", "38", "16"],
       ["Country C", "12", "11"],
       ["Country D", "19", "5"]]),
   choices=[
     "Country A, at 2.5 percent",
     "Country B, at 3.8 percent, because it has the highest birth rate",
     "Country D, at 1.4 percent",
     "Country C, at 0.1 percent",
     "Country B, at 2.2 percent"],
   ans=0,
   why="Subtracting deaths from births gives 25, 22, 1 and 14 per 1,000, which are 2.5, 2.2, 0.1 and 1.4 percent. The country with the highest birth rate also has the highest death rate, so it does not have the highest natural increase."),

 dict(q="Growth rates for four countries are shown. Using the table and the rule of 70, which country has the shortest doubling time, and roughly how long is it?",
   table=dict(
     headers=["Country", "Annual growth rate (%)"],
     rows=[
       ["Country W", "0.7"],
       ["Country X", "3.5"],
       ["Country Y", "1.4"],
       ["Country Z", "2.0"]]),
   choices=[
     "Country X, at about 20 years",
     "Country W, at about 20 years",
     "Country Z, at about 14 years",
     "Country Y, at about 70 years",
     "Country X, at about 35 years"],
   ans=0,
   why="Dividing 70 by each rate gives about 100, 20, 50 and 35 years, so the fastest-growing country doubles in roughly two decades. The rule of 70 is an approximation, which is why every figure here is given as about rather than exactly."),

 dict(q="Components of population change are shown for four countries, all rates per 1,000. Using the table, which country's population is shrinking?",
   table=dict(
     headers=["Country", "Crude birth rate", "Crude death rate", "Net migration rate"],
     rows=[
       ["Country J", "9", "13", "+7"],
       ["Country K", "10", "9", "-6"],
       ["Country L", "16", "7", "-4"],
       ["Country M", "8", "12", "+7"]]),
   choices=[
     "Country K, whose net loss to migration exceeds its positive natural increase",
     "Country J, whose birth rate is below its death rate",
     "Country L, which is losing people to emigration",
     "Country M, whose death rate exceeds its birth rate",
     "All four, since none has a birth rate above 20"],
   ans=0,
   why="Adding all three components gives plus 3, minus 5, plus 5 and plus 3 per 1,000, so exactly one country is shrinking, and it is one whose births exceed its deaths. A birth rate below a death rate is not by itself enough, because net immigration can more than compensate for it."),

 dict(q="Fertility measures for four countries are shown. Using the table, which country is furthest below the replacement level of about 2.1 children per woman?",
   table=dict(
     headers=["Country", "Total fertility rate", "Crude birth rate (per 1,000)"],
     rows=[
       ["Country P", "1.1", "7"],
       ["Country Q", "1.8", "11"],
       ["Country R", "2.4", "18"],
       ["Country S", "1.3", "14"]]),
   choices=[
     "Country P, at 1.1 children per woman",
     "Country S, at 1.3 children per woman, since it has a higher birth rate than Country Q",
     "Country Q, at 1.8 children per woman",
     "Country R, at 2.4 children per woman",
     "Country S, because its crude birth rate is second highest in the table"],
   ans=0,
   why="Only the lifetime measure can be compared with the replacement level, and 1.1 is the lowest of the four. One country pairs the second-lowest fertility with a relatively high crude birth rate, which shows the two measures ranking countries differently because age structures differ."),

 dict(q="A country's vital rates are shown for three decades. Using the table, what has happened to its rate of natural increase, and why?",
   table=dict(
     headers=["Year", "Crude birth rate (per 1,000)", "Crude death rate (per 1,000)"],
     rows=[
       ["1980", "44", "20"],
       ["2000", "38", "10"],
       ["2020", "24", "8"]]),
   choices=[
     "It rose from 2.4 to 2.8 percent and then fell to 1.6 percent, because deaths fell first and births fell later",
     "It fell steadily throughout, because the birth rate fell throughout",
     "It rose steadily throughout, because the death rate fell throughout",
     "It was unchanged, because both rates fell",
     "It cannot be determined without migration figures"],
   ans=0,
   why="Natural increase runs 24, 28 and 16 per 1,000, which is 2.4, 2.8 and 1.6 percent, so it rises before it falls. The death rate halves between the first two dates while the birth rate barely moves, and only in the last period does the birth rate fall faster."),
]
