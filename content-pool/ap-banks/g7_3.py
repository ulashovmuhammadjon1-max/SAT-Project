# AP HUMAN GEOGRAPHY 7.3 Measures of Development -- 30 questions
# CED Course Framework V.1, Unit 7. Enduring understanding SPS-7,
# "Industrialization, past and present, has facilitated improvements in
# standards of living, but it has also contributed to geographically uneven
# development." Learning objective SPS-7.C, "Describe social and economic
# measures of development." Suggested skill 3.F, "Explain possible limitations
# of the data provided."
#
# Essential knowledge -- three statements:
#   SPS-7.C.1  Measures of social and economic development include Gross
#              Domestic Product (GDP); Gross National Product (GNP); and Gross
#              National Income (GNI) per capita; sectoral structure of an
#              economy, both formal and informal; income distribution; fertility
#              rates; infant mortality rates; access to health care; use of
#              fossil fuels and renewable energy; and literacy rates.
#   SPS-7.C.2  Measures of gender inequality, such as the Gender Inequality Index
#              (GII), include reproductive health, indices of empowerment, and
#              labor-market participation.
#   SPS-7.C.3  The Human Development Index (HDI) is a composite measure used to
#              show spatial variation among states in levels of development.
#
# THE SUGGESTED SKILL IS THE TOPIC. Skill 3.F is "explain possible LIMITATIONS of
# the data provided", and it is the only topic in the course whose suggested
# skill is about what evidence cannot do. So roughly a third of this module is
# limitation items -- 20 to 24 and 29 -- and they are not an appendix. A student
# who can recite ten measures and cannot say what any of them misses has not met
# what SPS-7.C actually asks.
#
# THE THREE DISTINCTIONS THAT DO THE WORK:
#   GDP against GNP     GDP counts what is produced INSIDE a country's borders;
#                       GNP counts what is produced by its residents WHEREVER
#                       they are. The two diverge wherever profits or wages cross
#                       borders (items 2, 3).
#   TOTAL against       A total measures the size of an economy; a per-capita
#     PER CAPITA        figure measures what it amounts to for each person. Item 4
#                       keys on this and item 20 on what per capita still hides.
#   AVERAGE against     A mean says nothing about spread, so two countries with
#     DISTRIBUTION      identical GNI per capita can be entirely different places
#                       to live. That is why SPS-7.C.1 lists income distribution
#                       as its own measure (items 8, 20, 27).
#
# WHAT IS SAFE TO ASSERT ABOUT THE TWO INDICES. The CED names the Gender
# Inequality Index and gives its three components -- reproductive health, indices
# of empowerment, and labor-market participation -- so item 14 keys on the CED's
# own list. For the Human Development Index the CED says only that it is a
# COMPOSITE measure used to show spatial variation among states, so item 16 keys
# on that word and item 17 states the three standard dimensions -- a long and
# healthy life, knowledge, and a decent standard of living -- as the conventional
# composition rather than as the framework's own words. No numerical threshold is
# attached to either index anywhere in this module, because neither statement
# supplies one.
#
# NO REAL COUNTRY IS NAMED ANYWHERE IN THIS MODULE, the three data items
# included. Development indicators are revised and rebased, so a figure true when
# written can be wrong when read, and a lettered country carries the reasoning
# just as well.
#
# SYNONYM CARE. `geo_check` treats {"human development index", "hdi"}, {"gender
# inequality index", "gii"} and {"gross national income per capita", "gni per
# capita"} as three constructs, so no choice list names any of them in two ways.
#
# Three items carry a real `table=`. FIVE choices (A-E).
TOPIC = ("7.3", "Measures of Development", 7)

QUESTIONS = [
 dict(q="Which of the following does the framework NOT name among its measures of social and economic development?", choices=[
   "The rank-size rule",
   "Infant mortality rates",
   "Literacy rates",
   "Income distribution",
   "Access to health care"], ans=0,
   why="EK SPS-7.C.1 names infant mortality, literacy, income distribution and access to health care among its measures, along with the national accounts and energy use. The rank-size rule belongs to EK PSO-6.C.1 and describes the size distribution of a country's cities."),

 dict(q="What does Gross Domestic Product measure?", choices=[
   "The value of goods and services produced inside a country's borders in a given period",
   "The value of goods and services produced by a country's residents wherever they are",
   "The total income received by a country's households after taxes",
   "The total wealth a country has accumulated over its history",
   "The value of a country's exports minus its imports"], ans=0,
   why="EK SPS-7.C.1 names Gross Domestic Product among the measures of social and economic development. The word domestic marks the boundary: what counts is where production happened, not who owned the operation that carried it out."),

 dict(q="How does Gross National Product differ from Gross Domestic Product?", choices=[
   "It counts what a country's residents produce wherever they are, so it includes their earnings abroad and excludes foreign-owned production at home",
   "It counts only production inside the country's borders",
   "It measures wealth rather than annual production",
   "It excludes all services and counts only goods",
   "The two measure exactly the same thing"], ans=0,
   why="EK SPS-7.C.1 names both Gross Domestic Product and Gross National Product among its measures, which implies they differ. One is bounded by territory and the other by who the producer belongs to, and the gap between them is largest where profits and wages cross borders heavily."),

 dict(q="Why is Gross National Income usually reported PER CAPITA rather than as a total?", choices=[
   "A total measures the size of an economy while dividing by population measures what it amounts to for each person, which is what a development comparison needs",
   "Totals cannot be calculated accurately",
   "Per-capita figures are always larger than totals",
   "Population figures are more reliable than income figures",
   "The two figures always give the same country ranking"], ans=0,
   why="EK SPS-7.C.1 names Gross National Income PER CAPITA specifically. A populous country can have an enormous total and a modest figure per person, so the total ranks economies by size and the per-capita figure ranks them by what an average resident has."),

 dict(q="Why are income figures often adjusted for purchasing power when countries are compared?", choices=[
   "The same sum of money buys different amounts in different countries, so an unadjusted comparison overstates the gap where prices are low",
   "Because exchange rates are never published",
   "Because income cannot be measured in any currency",
   "Because the adjustment makes all countries appear identical",
   "Because prices are the same in every country"], ans=0,
   why="EK SPS-7.C.1 names Gross National Income per capita among the measures and suggested skill 3.F asks for the limitations of data. A figure converted at a market exchange rate measures what a resident could buy abroad rather than what they can buy at home."),

 dict(q="Why does the framework name the SECTORAL STRUCTURE of an economy among its development measures?", choices=[
   "The shares of employment in the primary, secondary and higher sectors shift as an economy develops, so the composition itself indicates a level",
   "Because every economy has an identical sectoral structure",
   "Because sectoral structure measures the total size of an economy",
   "Because only the primary sector matters for development",
   "Because sectoral structure is unrelated to development"], ans=0,
   why="EK SPS-7.C.1 names sectoral structure among the measures of development and EK SPS-7.B.1 says the sectors are characterized by distinct development patterns. The second statement is what makes the first a measure rather than a description."),

 dict(q="Why does the framework specify sectoral structure BOTH FORMAL AND INFORMAL?", choices=[
   "Much economic activity is unregistered and untaxed, so a measure counting only the formal sector understates output and employment, sometimes greatly",
   "Because the informal sector does not exist in most countries",
   "Because formal and informal activity are identical in size everywhere",
   "Because only informal activity contributes to development",
   "Because the two are two names for the same thing"], ans=0,
   why="EK SPS-7.C.1 names sectoral structure of an economy, BOTH FORMAL AND INFORMAL. The qualification is a warning built into the statement: where a large share of work is unregistered, a measure that sees only registered activity describes a different economy from the one people live in."),

 dict(q="Why does the framework list INCOME DISTRIBUTION as a measure separate from income per person?", choices=[
   "An average says nothing about spread, so two countries with the same income per person can differ enormously in what most of their residents actually receive",
   "Income distribution is another name for income per person",
   "Distribution matters only in wealthy countries",
   "An average already accounts for how income is shared",
   "Income distribution cannot be measured"], ans=0,
   why="EK SPS-7.C.1 names income distribution alongside Gross National Income per capita, and listing both means neither substitutes for the other. A mean is a single number about a whole distribution, and a distribution is what it is a single number about."),

 dict(q="Why is the fertility rate treated as a development measure?", choices=[
   "It falls as incomes, education and access to health care rise, so it moves with development even though it measures births",
   "Because a high fertility rate indicates a high level of development",
   "Because fertility is fixed by climate",
   "Because fertility rates are the same in every country",
   "Because fertility measures economic output directly"], ans=0,
   why="EK SPS-7.C.1 names fertility rates among the measures of social and economic development. What makes a demographic figure a development indicator is that it responds reliably to the same changes development consists of, which is the logic of the demographic transition model in Unit 2."),

 dict(q="Why is infant mortality an unusually sensitive measure of development?", choices=[
   "Infant survival depends on nutrition, clean water, sanitation and health care at once, so the rate responds to whether a whole set of basic conditions is being met",
   "Because infants are the largest group in any population",
   "Because infant mortality is unrelated to health care",
   "Because it measures economic output more precisely than income does",
   "Because it is identical in every country"], ans=0,
   why="EK SPS-7.C.1 names infant mortality rates among the measures of social and economic development. A measure sensitive to several conditions at once is a good summary indicator precisely because failure in any one of them shows up in it."),

 dict(q="What does ACCESS TO HEALTH CARE measure that a count of doctors alone would not?", choices=[
   "Whether people can actually reach and afford care, which depends on distance, cost and availability as well as on how many practitioners exist",
   "The total number of hospitals in a country",
   "The average lifespan of a country's population",
   "The number of medical schools in a country",
   "The proportion of national income spent on medicine"], ans=0,
   why="EK SPS-7.C.1 names access to health care among the measures of development, and access is a relationship rather than a stock. A country can have practitioners concentrated where a minority of its population lives and still leave most people without reachable care."),

 dict(q="Why does the framework include the use of fossil fuels and renewable energy among development measures?", choices=[
   "Energy consumption per person rises with industrial activity and living standards, and the mix between the two sources indicates how that energy is obtained",
   "Because energy use is unrelated to economic activity",
   "Because only renewable energy indicates development",
   "Because energy use measures a country's total population",
   "Because all countries use energy in identical proportions"], ans=0,
   why="EK SPS-7.C.1 names use of fossil fuels AND renewable energy among the measures. Naming both is what makes it two measures in one: how much energy a population commands, and what kind, which are separate facts about a country."),

 dict(q="Why is the literacy rate a development measure rather than merely an education statistic?", choices=[
   "Literacy is the precondition for most further schooling and most skilled work, so the rate indicates what a population is able to do as well as what it has been taught",
   "Because literacy rates are the same in every country",
   "Because literacy measures national income directly",
   "Because literacy has no relationship to employment",
   "Because it counts the number of schools in a country"], ans=0,
   why="EK SPS-7.C.1 names literacy rates among the measures of social and economic development. Reading is the gateway skill: it conditions access to further training, to information and to most work above the least skilled, which is why the rate summarizes more than schooling."),

 dict(q="Which three components does the framework name for its measure of gender inequality?", choices=[
   "Reproductive health, indices of empowerment, and labour-market participation",
   "Literacy, life expectancy, and income per person",
   "Fertility, infant mortality, and access to health care",
   "Formal and informal sectoral structure",
   "Fossil fuel use, renewable energy use, and income distribution"], ans=0,
   why="EK SPS-7.C.2 says measures of gender inequality, such as the Gender Inequality Index, include reproductive health, indices of empowerment and labor-market participation. The other options are drawn from EK SPS-7.C.1's general list of development measures."),

 dict(q="Why is gender inequality measured separately rather than being read off general development measures?", choices=[
   "A national figure averages across the whole population, so a country can score well on income or literacy overall while a large gap persists within it",
   "Because gender inequality does not affect development",
   "Because general measures already report every group separately",
   "Because gender inequality exists only in poor countries",
   "Because the two kinds of measure always give the same ranking"], ans=0,
   why="EK SPS-7.C.2 names measures of gender inequality as a category of their own alongside EK SPS-7.C.1's general measures. An average conceals the composition of the population it averages, which is the same reason income distribution is listed separately from income per person."),

 dict(q="What does the framework say the Human Development Index is, and what is it used for?", choices=[
   "A composite measure used to show spatial variation among states in levels of development",
   "A single measure of national income per person",
   "A measure of gender inequality within a country",
   "A count of the services a government provides",
   "A measure of a country's total economic output"], ans=0,
   why="EK SPS-7.C.3 states that the Human Development Index is a composite measure used to show spatial variation among states in levels of development. Both halves matter: it combines several indicators, and its purpose is comparison across places."),

 dict(q="Which three dimensions does the Human Development Index conventionally combine?", choices=[
   "A long and healthy life, knowledge, and a decent standard of living",
   "Reproductive health, empowerment, and labour-market participation",
   "Fossil fuel use, renewable energy use, and literacy",
   "Gross Domestic Product, Gross National Product, and exports",
   "Fertility, migration, and population density"], ans=0,
   why="EK SPS-7.C.3 calls the index a composite measure without listing its parts, and these are its conventional three dimensions. The second option is EK SPS-7.C.2's list for the gender inequality measure, which is the composite most easily confused with this one."),

 dict(q="What does combining several indicators into one composite index gain, and what does it cost?", choices=[
   "It gives a single comparable figure for each country, and it conceals which of the underlying components is high or low",
   "It gains accuracy and costs nothing",
   "It costs comparability and gains detail",
   "It neither gains nor costs anything relative to a single indicator",
   "It removes the need for any underlying data"], ans=0,
   why="EK SPS-7.C.3 describes the index as a COMPOSITE measure used to show spatial variation among states, and suggested skill 3.F asks for the limitations of data. Two countries can reach the same composite score by entirely different routes, which is exactly what a single number cannot report."),

 dict(q="How do the framework's ECONOMIC and SOCIAL measures of development differ?", choices=[
   "Economic measures record output and income, while social measures record the conditions of people's lives such as health, education and survival",
   "Economic measures are accurate and social measures are not",
   "Social measures record output and economic measures record health",
   "The two kinds always give the same country ranking",
   "The framework recognizes only economic measures"], ans=0,
   why="Learning objective SPS-7.C asks students to describe SOCIAL AND ECONOMIC measures of development, and EK SPS-7.C.1's list contains both kinds. Naming both is a claim that development is not exhausted by output, which is also why the composite index of EK SPS-7.C.3 combines them."),

 dict(q="What does income per person fail to show, however accurately it is measured?", choices=[
   "How the income is shared, so a country with a high average can still have most of its population on very little",
   "The total size of a country's economy",
   "The population of the country",
   "The currency in which income is denominated",
   "Nothing; a per-person figure captures everything relevant"], ans=0,
   why="EK SPS-7.C.1 lists income distribution as a measure separate from Gross National Income per capita, and suggested skill 3.F asks for the limitations of the data provided. A mean is compatible with any distribution, which is precisely why the framework lists both."),

 dict(q="Why can official statistics understate economic activity in a country with a large informal sector?", choices=[
   "Unregistered work is not captured by the systems that produce national accounts, so real output and employment exceed the recorded figures",
   "Because informal work produces nothing of value",
   "Because informal work is counted twice",
   "Because official statistics are always deliberately falsified",
   "Because the informal sector is the same size everywhere"], ans=0,
   why="EK SPS-7.C.1 names sectoral structure BOTH FORMAL AND INFORMAL among its measures, and suggested skill 3.F asks for the limitations of data. What is unregistered is largely uncounted, so the recorded economy and the actual economy diverge by more where the informal share is larger."),

 dict(q="Why can a national development figure be misleading about the country it describes?", choices=[
   "A national figure is an average over regions that may differ enormously, so it can describe no actual part of the country well",
   "National figures are always more accurate than regional ones",
   "Regional variation does not exist within countries",
   "A national figure automatically reports its own regional range",
   "National figures are collected only in wealthy countries"], ans=0,
   why="EK SPS-7.C.3 says the Human Development Index shows spatial variation AMONG STATES, which is a comparison at one scale. Suggested skill 3.F asks for the limitations of the data, and a figure computed for a whole state conceals whatever variation exists inside it."),

 dict(q="What limitation should be recognized about the timeliness and comparability of development data?", choices=[
   "Countries collect data at different intervals with different definitions and different reliability, so a table of figures may not be measuring quite the same thing in each row",
   "All countries collect identical data in the same year",
   "Development data are never revised once published",
   "Definitions of every indicator are fixed internationally and never differ",
   "Data quality is identical in every country"], ans=0,
   why="Suggested skill 3.F for this topic is explaining possible limitations of the data provided. A cross-country table looks uniform on the page and is assembled from national collections that differ in date, method and coverage, which is a limitation of the comparison rather than of any one figure."),

 dict(q="Which important aspect of an economy do the framework's standard measures largely omit?", choices=[
   "Unpaid work in households and the depletion of natural resources, neither of which appears in output figures",
   "Manufacturing output, which no measure records",
   "Population size, which no measure records",
   "Literacy, which no measure records",
   "Nothing is omitted by the standard measures"], ans=0,
   why="Suggested skill 3.F asks for the limitations of the data, and EK SPS-7.C.1's list is built around recorded output and recorded social outcomes. Work that is never paid for and resources that are drawn down without being priced fall outside what those systems count."),

 dict(q="Which pairing of a measure with what it captures is CORRECT?", choices=[
   "Infant mortality rate, matched to the effect of nutrition, water, sanitation and health care on the youngest",
   "Infant mortality rate, matched to the total output of an economy",
   "Gross Domestic Product, matched to how income is shared among households",
   "Literacy rate, matched to the mix of fossil fuel and renewable energy use",
   "Income distribution, matched to the value of production inside a country's borders"], ans=0,
   why="EK SPS-7.C.1 lists these measures for different things, and the list is only useful if the measures are kept apart. Only one pairing here matches a measure to what it actually captures; each of the others attaches a measure to the subject of a different one on the same list."),

 dict(q="Four countries are compared below. Using the accompanying record, which conclusion is best supported?",
   table=dict(headers=["Country", "Gross National Income per person", "Infant mortality per 1,000 births", "Literacy rate (%)", "Composite development index"],
     rows=[["Country 1", "48,000", "4", "99", "0.92"],
           ["Country 2", "12,000", "21", "94", "0.74"],
           ["Country 3", "4,200", "44", "78", "0.58"],
           ["Country 4", "1,100", "68", "51", "0.42"]]),
   choices=[
   "Income, literacy and the composite index all fall together while infant mortality rises from 4 to 68, so four independent measures rank the countries in the same order",
   "The four measures disagree about the ranking of the countries",
   "Infant mortality falls as income falls",
   "Literacy rises as income falls",
   "The composite index is unrelated to the other three measures"], ans=0,
   why="Income falls from 48,000 to 1,100, literacy from 99 to 51 percent and the composite index from 0.92 to 0.42, while infant mortality rises from 4 to 68 at every step. EK SPS-7.C.1 names all four kinds of measure, and their agreeing is what makes any one of them usable as a summary."),

 dict(q="Two countries with the same income per person are compared below. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Measure", "Country X", "Country Y"],
     rows=[["Gross National Income per person", "14,000", "14,000"],
           ["Share of national income received by the poorest fifth (%)", "3", "9"],
           ["Share of national income received by the richest fifth (%)", "62", "38"]]),
   choices=[
   "Income per person is identical while the richest fifth receives about 21 times the poorest fifth's share in one country and about 4 times in the other, so the average conceals two very different distributions",
   "The two countries have identical income distributions",
   "The country with the more equal distribution has the higher income per person",
   "The poorest fifth receives the same share in both countries",
   "Income per person differs between the two countries"], ans=0,
   why="Both countries record 14,000 per person, while the ratio of the richest fifth's share to the poorest fifth's is about 20.7 in one and about 4.2 in the other. EK SPS-7.C.1 lists income distribution separately from income per capita, and this record is why the framework treats them as two measures."),

 dict(q="The components of a composite development index are recorded below for three countries. Using the accompanying figures, which conclusion is supported?",
   table=dict(headers=["Country", "Life expectancy at birth (years)", "Expected years of schooling", "Gross National Income per person", "Composite index"],
     rows=[["Country A", "82", "17.5", "46,000", "0.93"],
           ["Country B", "71", "13.2", "11,500", "0.72"],
           ["Country C", "62", "9.8", "2,900", "0.53"]]),
   choices=[
   "All three components fall together from Country A to Country C and the composite index falls with them, so the index summarizes measures that agree rather than averaging measures that conflict",
   "The three components move in different directions",
   "The composite index rises as its components fall",
   "Life expectancy and schooling rise while income falls",
   "The composite index is unrelated to its three components"], ans=0,
   why="Life expectancy falls from 82 to 62, expected schooling from 17.5 to 9.8 years and income from 46,000 to 2,900, while the composite index falls from 0.93 to 0.53. EK SPS-7.C.3 calls the index a composite measure of spatial variation among states, and a case where the components agree is the easy case, which is exactly why the hard case has to be stated separately."),

 dict(q="What limitation should be stated when a composite index summarizes several components in one number?", choices=[
   "Two countries can reach the same score by different combinations of the components, so the index has to be read alongside the parts it is built from",
   "A composite index cannot be calculated at all",
   "Components and an index can never appear in one record",
   "A single composite score reports its own components",
   "The framework forbids the use of composite indices"], ans=0,
   why="EK SPS-7.C.3 describes the Human Development Index as a COMPOSITE measure, and suggested skill 3.F asks for the limitations of the data provided. Compression is what makes a composite comparable and it is the same operation that discards the information about which component is weak."),

 dict(q="A report must state what this topic's three statements establish together. Which statement is accurate?", choices=[
   "Development is measured by economic and social indicators of several kinds, gender inequality is measured separately by its own components, and a composite index combines indicators to compare states -- and every one of these measures has limits",
   "Development is measured entirely by income per person",
   "The framework names only social measures of development",
   "A composite index makes all other measures unnecessary",
   "Gender inequality is measured by the same indicators as general development"], ans=0,
   why="EK SPS-7.C.1 supplies the general measures, EK SPS-7.C.2 the gender inequality components and EK SPS-7.C.3 the composite index, while suggested skill 3.F makes limitations part of the topic. Each rejected summary reduces the three statements to one or removes the qualification the skill supplies."),
]
