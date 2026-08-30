# AP COMPARATIVE GOVERNMENT AND POLITICS 1.1 The Practice of Political Scientists
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding MPA-1; learning objective MPA-1.A (explain how political
# scientists construct knowledge and communicate inferences and explanations
# about political systems, institutional interactions, and behavior).
# Suggested skill 3.B, describe patterns and trends in data.
#
# Essential knowledge relied on, in the framework's own terms:
#   MPA-1.A.1  analysis of quantitative AND qualitative information -- charts,
#              tables, graphs, speeches, foundational documents, political
#              cartoons, maps, political commentaries -- is a way to make
#              comparisons between and inferences about course countries
#   MPA-1.A.2  analysing empirical data with quantitative methods facilitates
#              comparisons among and inferences about course countries
#   MPA-1.A.3  causation is DIFFICULT TO DETERMINE WITH CERTAINTY in comparative
#              politics: numerous variables potentially influence policies and
#              regime stability with no way to isolate which produces the change
#   MPA-1.A.4  correlation exists when there is an association between two or
#              more variables
#   MPA-1.A.5  research requires differentiating empirical (factual/objective)
#              from normative (value) statements
#   MPA-1.A.6  empirical information is most often used to apply concepts,
#              support generalisations, or make arguments
#   MPA-1.A.7  comparative political scientists compare different political
#              systems to derive conclusions about politics
#   MPA-1.A.8  the seven named data collection resources: Human Development
#              Index; GDP and GDP per capita; GDP growth rate; Gini index
#              (coefficient); Freedom House; Transparency International;
#              Failed States Index
#
# ON THE DATA IN THE TABLES. The framework names the seven resources but prints
# no country values, and any real figure would be a current-events fact that
# dates. Every table in this bank is therefore labelled HYPOTHETICAL in the stem
# and every keyed conclusion is recoverable from the table itself -- which is
# also how the real exam's quantitative sets work, since the stimulus carries its
# own data. Nothing here asks a student to remember a number.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md. The CED's own sample questions print
# four; see AP_COMP_GOV_CED.md for that discrepancy.
TOPIC = ("1.1", "The Practice of Political Scientists", 1)

_T_HDI = dict(
    headers=["Country", "GDP per capita (hypothetical, US$)",
             "Human Development Index (hypothetical, 0-1)"],
    rows=[["China", "12,500", "0.768"],
          ["Mexico", "10,200", "0.758"],
          ["Nigeria", "2,300", "0.535"],
          ["United Kingdom", "46,000", "0.929"]])

_T_FH = dict(
    headers=["Country", "2010 score", "2015 score", "2020 score"],
    rows=[["Mexico", "66", "61", "62"],
          ["Nigeria", "48", "45", "47"],
          ["Russia", "31", "24", "20"]])

_T_GINI = dict(
    headers=["Country", "Gini index (hypothetical; 0 = perfect equality, 100 = perfect inequality)"],
    rows=[["China", "38"],
          ["Mexico", "45"],
          ["Nigeria", "35"],
          ["Russia", "36"],
          ["United Kingdom", "33"]])

QUESTIONS = [
 dict(q="A researcher finds that, across a large sample of states, countries with higher per capita gross domestic product tend to score higher on measures of democracy. On the basis of this finding alone, the relationship between wealth and democracy is best described as",
   choices=[
     "a correlation, because the two variables are associated but neither has been shown to produce the other",
     "a causal relationship, because wealth is measured before the democracy score is assigned",
     "a normative relationship, because it expresses a preference for wealthy democracies",
     "a qualitative relationship, because democracy scores are assigned by expert judgement",
     "an experimental result, because a large sample was used"], ans=0,
   why="EK MPA-1.A.4 defines correlation as an association between two or more variables, and EK MPA-1.A.3 says causation cannot be determined with certainty in comparative politics because numerous variables may be producing the change. An observed association is all this finding contains."),
 dict(q="Which of the following statements is empirical rather than normative?",
   choices=[
     "Nigeria and Mexico both elect a president who serves as head of state and head of government",
     "Nigeria ought to reduce the powers of its president",
     "The United Kingdom would govern more justly if it abolished the House of Lords",
     "Russia's leaders should permit greater competition in national elections",
     "China's government has a duty to allow independent civil society organizations"], ans=0,
   why="EK MPA-1.A.5 requires distinguishing empirical (factual and objective) statements from normative (value) statements. Only the first reports an institutional arrangement that can be checked against evidence; the other four each turn on 'ought', 'should' or 'duty'."),
 dict(q="A student writes: 'Iran's Guardian Council vets candidates for the Majles, and this practice is unjust.' The sentence is best described as",
   choices=[
     "an empirical claim joined to a normative claim",
     "two empirical claims",
     "two normative claims",
     "a causal claim supported by data",
     "a correlation between vetting and injustice"], ans=0,
   why="EK MPA-1.A.5 turns on separating factual from value statements. The first clause reports a practice that can be checked; the second applies a standard of justice to it, which no observation can settle. The sentence therefore contains one of each."),
 dict(q="A political scientist reports that regime stability and economic growth rise together across the six course countries but declines to say that growth produces stability. The best justification for that caution is that",
   choices=[
     "many variables can influence regime stability at once and there is no way to isolate which one produced the change",
     "economic growth is a normative concept and therefore cannot cause anything",
     "correlations reported across six countries are always statistically insignificant",
     "comparative politics prohibits the use of quantitative evidence",
     "stability can only be measured qualitatively, so it cannot be paired with a quantitative variable"], ans=0,
   why="EK MPA-1.A.3 states the reason in these terms: causation is difficult to determine with certainty because numerous variables potentially influence policies and regime stability, with no way to isolate and demonstrate which is producing the change."),
 dict(q="Of the data collection resources named in the course framework, which is best suited to comparing overall living standards across countries?",
   choices=[
     "The Human Development Index",
     "Gross domestic product",
     "The GDP growth rate",
     "The Gini index",
     "Transparency International's corruption measure"], ans=0,
   why="The HDI combines income with health and education attainment, so it reports how people live rather than how much a country produces. Total GDP scales with population, the growth rate reports change rather than level, the Gini index reports distribution, and the corruption measure reports governance."),
 dict(q="A comparative politics class wants a single figure showing how unequally income is distributed within each course country. Which resource named in the framework is designed for that purpose?",
   choices=[
     "The Gini index",
     "GDP per capita",
     "The GDP growth rate",
     "The Human Development Index",
     "Freedom House scores"], ans=0,
   why="The Gini index is a measure of the distribution of income within a population, which is exactly the question asked. GDP per capita is an average and hides distribution entirely; the other three measure growth, development and political freedom."),
 dict(q="Two countries report identical gross domestic product, but one has ten times the population of the other. Which comparison is most misleading if total GDP is used rather than GDP per capita?",
   choices=[
     "A comparison of how much output is available on average to each resident",
     "A comparison of the total size of the two economies",
     "A comparison of the two countries' land areas",
     "A comparison of the number of political parties in each country",
     "A comparison of the two countries' constitutional structures"], ans=0,
   why="Total GDP scales with population, so two economies of equal total size can offer very different amounts per resident. Dividing by population is what makes the per-resident comparison meaningful; the size of the economies is precisely what total GDP does report."),
 dict(q="A country's GDP growth rate rises from 2 percent to 6 percent while its GDP per capita remains among the lowest in a comparison group. The most accurate reading of these two figures together is that",
   choices=[
     "the economy is expanding quickly from a low starting level",
     "the country now has one of the highest living standards in the group",
     "income is being distributed more equally than in the other countries",
     "the growth rate figure contradicts the per capita figure, so one must be an error",
     "the country's political system must have become more democratic"], ans=0,
   why="A growth rate reports the speed of change and a per capita figure reports the level, so the two answer different questions and cannot contradict each other. Fast growth from a low base leaves the level low, which is what the pair of figures shows."),
 dict(q="Which of the following is a qualitative source of the kind the framework expects students to analyse?",
   choices=[
     "A political cartoon commenting on an election result",
     "A table of voter turnout percentages",
     "A line graph of GDP per capita over twenty years",
     "A bar chart of seats won by each party",
     "A map shaded by income quintile"], ans=0,
   why="EK MPA-1.A.1 lists political cartoons, speeches, foundational documents and political commentaries as qualitative material alongside charts, tables, graphs and maps as quantitative material. Only the cartoon is on the qualitative side of that list."),
 dict(q="A researcher assembles the text of a head of government's speech, a newspaper commentary on it, and the country's foundational constitutional document. According to the framework, this material is most useful for",
   choices=[
     "making comparisons between and inferences about course countries",
     "establishing with certainty that one institution caused a policy change",
     "calculating a Gini index for each country",
     "eliminating the need for quantitative evidence",
     "proving that a normative claim is factually true"], ans=0,
   why="EK MPA-1.A.1 names speeches, commentaries and foundational documents among the qualitative sources whose analysis supports comparison and inference across course countries. It does not license certainty about causation, which EK MPA-1.A.3 expressly denies."),
 dict(q="Why does the study of comparative politics require examining more than one political system?",
   choices=[
     "Conclusions about politics are derived by comparing different political systems with one another",
     "A single country cannot generate any empirical data",
     "Normative statements can only be made about groups of countries",
     "Correlation requires at least six variables to be measured",
     "Causation can be demonstrated with certainty once three countries are compared"], ans=0,
   why="EK MPA-1.A.7 states that comparative political scientists compare different political systems to derive conclusions about politics. A single case supplies no variation, so nothing about what distinguishes systems can be drawn from it."),
 dict(q="A political scientist uses turnout figures from five countries to support the generalization that competitive elections raise participation. This use of data is best described as",
   choices=[
     "using empirical information to support a generalization",
     "using normative information to establish a value",
     "using qualitative information to calculate a rate",
     "demonstrating causation with certainty",
     "replacing comparison with description"], ans=0,
   why="EK MPA-1.A.6 says political scientists most often use empirical information to apply concepts, support generalizations, or make arguments. Turnout figures are empirical and the claim they back is a generalization across cases."),
 dict(q="Which resource named in the framework would a researcher consult first to compare how freely citizens of two countries may organize and express political views?",
   choices=[
     "Freedom House",
     "The Gini index",
     "GDP per capita",
     "The GDP growth rate",
     "The Human Development Index"], ans=0,
   why="Freedom House rates political rights and civil liberties, which is the subject of the question. The other four measure income distribution, average output, the speed of economic change and human development respectively, none of which reports on rights."),
 dict(q="A journalist wants to compare the extent of perceived corruption in the public sectors of Nigeria and Russia. Which of the framework's named resources is designed for that comparison?",
   choices=[
     "Transparency International",
     "The Human Development Index",
     "The Gini index",
     "Gross domestic product",
     "The GDP growth rate"], ans=0,
   why="Transparency International's work is the corruption measure among the seven resources EK MPA-1.A.8 names. The others report human development, income distribution, economic size and economic change, none of which is a corruption measure."),
 dict(q="Which question is a comparative political scientist best equipped to answer with the methods described in the framework?",
   choices=[
     "How do the legislative powers of two countries differ, and what follows from that difference?",
     "Which of two countries has the morally superior form of government?",
     "Whether a country's citizens ought to obey their government",
     "Which political ideology is objectively correct",
     "Whether a constitution is beautiful"], ans=0,
   why="EK MPA-1.A.7 frames the discipline as comparing political systems to derive conclusions about politics, and EK MPA-1.A.5 sets value questions outside what evidence can settle. Only the first question can be answered by observation and comparison."),
 dict(q="The table presents hypothetical figures for four course countries. Which statement is accurate according to the table?",
   table=_T_HDI,
   choices=[
     "China's GDP per capita and Human Development Index are both higher than Mexico's",
     "Nigeria's GDP per capita is roughly half of Mexico's",
     "The United Kingdom's Human Development Index is more than twice Nigeria's",
     "Mexico has a higher Human Development Index than China but a lower GDP per capita",
     "Every country with GDP per capita above 10,000 dollars has a Human Development Index below 0.75"], ans=0,
   why="Reading the table: China's 12,500 exceeds Mexico's 10,200 and China's 0.768 exceeds Mexico's 0.758, so both comparisons run the same way. Each other option asserts a magnitude the table's own numbers contradict."),
 dict(q="Using the same hypothetical figures, which inference about the relationship between the two indicators is best supported?",
   table=_T_HDI,
   choices=[
     "Across these four countries the two indicators rise and fall together, but the table cannot show that one produces the other",
     "The table demonstrates that raising GDP per capita causes the Human Development Index to rise",
     "The table shows no association between the two indicators",
     "The table shows that the Human Development Index falls as GDP per capita rises",
     "The table proves that the four countries have similar living standards"], ans=0,
   why="Ranking the countries by either column produces the same order, which is an association and nothing more. EK MPA-1.A.3 is the reason the stronger reading is unavailable: with numerous variables in play, four observations cannot isolate which produces the change."),
 dict(q="The table gives hypothetical political-freedom scores, on a 0-100 scale where higher is freer, for three course countries. Which description of the data is accurate?",
   table=_T_FH,
   choices=[
     "Russia's score falls in both periods, while Mexico's and Nigeria's fall and then partially recover",
     "All three countries' scores fall in both periods",
     "All three countries' scores rise between 2015 and 2020",
     "Nigeria's score is the lowest in every year shown",
     "Mexico's score changes by more than Russia's across the full period"], ans=0,
   why="Russia moves 31 to 24 to 20, down twice; Mexico moves 66 to 61 to 62 and Nigeria 48 to 45 to 47, each down then up. Russia's full-period change of 11 points exceeds Mexico's 4, and Russia rather than Nigeria holds the lowest score in every year."),
 dict(q="A student concludes from the same hypothetical scores that political freedom is declining in every country in the world. The clearest problem with that conclusion is that",
   table=_T_FH,
   choices=[
     "the table reports three countries, and two of them rose in the most recent period",
     "the scale used runs from 0 to 100 rather than from 0 to 1",
     "a score cannot be compared across years",
     "the data are quantitative, so no conclusion may be drawn from them",
     "political freedom is a normative concept and cannot be measured at all"], ans=0,
   why="The conclusion generalizes beyond the three cases shown, and it is also contradicted inside them: Mexico rises from 61 to 62 and Nigeria from 45 to 47 in the final period. A description of data must stay within what the data covers."),
 dict(q="The table reports hypothetical Gini index values. Which country's income is most unequally distributed according to the table?",
   table=_T_GINI,
   choices=[
     "Mexico",
     "China",
     "Nigeria",
     "Russia",
     "The United Kingdom"], ans=0,
   why="The header states that a higher value means greater inequality, and Mexico's 45 is the largest of the five values. The country with the lowest value shown, at 33, is the United Kingdom, which is the most equal on this measure rather than the least."),
 dict(q="Two researchers examine the same hypothetical Gini values. One writes 'Mexico's index is 12 points above the United Kingdom's'; the other writes 'Mexico should adopt redistributive taxation.' The difference between the two statements is that",
   table=_T_GINI,
   choices=[
     "the first is empirical and the second is normative",
     "the first is normative and the second is empirical",
     "both are empirical, but only the second uses the table",
     "both are normative, because both mention inequality",
     "neither can be assessed, because the data are hypothetical"], ans=0,
   why="EK MPA-1.A.5's distinction applies directly. Mexico's 45 less the United Kingdom's 33 is 12, a figure the table settles; whether Mexico ought to tax differently is a value judgement no table can settle."),
 dict(q="A researcher observes that countries with more independent judiciaries also report lower perceived corruption, and concludes that judicial independence reduces corruption. The weakest point in the argument is that",
   choices=[
     "lower corruption may itself make judicial independence easier to sustain, and the data cannot distinguish the two directions",
     "perceived corruption is a normative concept and cannot be measured",
     "judicial independence cannot be compared across countries",
     "a correlation between two variables is impossible when both are measured by an index",
     "the conclusion is normative and therefore requires no evidence"], ans=0,
   why="EK MPA-1.A.3's difficulty is exactly this: an association is symmetric, so the same data fit the reverse account, and other variables may be producing both. Nothing in the observation isolates the direction the conclusion asserts."),
 dict(q="Which additional finding would most weaken the claim that a country's rising GDP growth rate caused its improvement on a democracy index?",
   choices=[
     "The democracy index began improving several years before the growth rate rose",
     "The country's GDP per capita is below the average for its region",
     "The democracy index and the growth rate are reported by different organizations",
     "The country has a federal rather than a unitary system",
     "The country's Gini index is unchanged over the period"], ans=0,
   why="A cause cannot follow its effect. If the democracy score was already improving before growth accelerated, the proposed cause was not yet present when the change began, which the other findings leave untouched."),
 dict(q="A researcher compares only the United Kingdom and Russia and concludes that parliamentary systems produce higher political-freedom scores than semi-presidential systems. The principal weakness of the design is that",
   choices=[
     "two cases differ in many respects besides the one named, so the difference cannot be attributed to system type",
     "the United Kingdom and Russia are not course countries",
     "political-freedom scores are qualitative and cannot be compared",
     "a conclusion about politics may never be drawn from a comparison",
     "parliamentary and semi-presidential systems cannot be compared with each other"], ans=0,
   why="EK MPA-1.A.3 names the problem: numerous variables potentially influence the outcome and none can be isolated. Two countries differ in history, wealth, cleavage structure and much else, so any one of those differences fits the result as well as system type does."),
 dict(q="Which of the following best describes what a comparative political scientist does with a map shaded to show regional variation in a country's election results?",
   choices=[
     "Treats it as quantitative material that supports description of a pattern and inference about the political system",
     "Treats it as a normative statement about which region is governed best",
     "Treats it as proof that the regional pattern was caused by ethnicity",
     "Discards it, because maps are not a recognized source in the discipline",
     "Uses it to calculate the country's Human Development Index"], ans=0,
   why="EK MPA-1.A.1 names maps among the quantitative material whose analysis supports comparison and inference. Reading a pattern from it is legitimate; attributing a cause to it is what EK MPA-1.A.3 warns against."),
 dict(q="'Voter turnout in the most recent national election was 63 percent' and 'Voter turnout in that election was disgracefully low' differ in that only the second",
   choices=[
     "applies a standard of value that observation cannot settle",
     "reports a figure that can be checked against records",
     "concerns political participation",
     "refers to a national rather than a local election",
     "could be included in a research report"], ans=0,
   why="EK MPA-1.A.5's distinction: the first is empirical, checkable against the record; the second calls the same figure disgraceful, which is a judgement about what turnout ought to be. Both concern the same election, so the other contrasts do not separate them."),
 dict(q="A researcher has ranked the six course countries on a corruption measure and on a measure of political rights. Which further step would most strengthen an argument that the two are related?",
   choices=[
     "Showing that the relationship also holds across a much larger set of countries and over several time periods",
     "Restating the ranking as a normative claim about which country governs best",
     "Removing the two countries that fit the pattern least well",
     "Replacing both measures with a single country's national statistics",
     "Declaring the relationship causal because the rankings match"], ans=0,
   why="EK MPA-1.A.2 treats quantitative analysis as the route to defensible comparisons and inferences, and a pattern that survives more cases and more time periods is harder to attribute to the particular six chosen. Dropping the countries that fit worst does the reverse: it manufactures the pattern."),
 dict(q="Describing a trend and explaining a trend differ in that an explanation",
   choices=[
     "offers a reason that political systems, institutions or behaviour supply for the movement in the data",
     "restates the direction of the movement in different words",
     "converts the figures into percentages",
     "identifies the highest and lowest values in the series",
     "reports the source and date of the data"], ans=0,
   why="The framework's data skills run from describing data through describing patterns to explaining what the data implies about political systems, institutions, processes, policies and behaviors. Only the first option supplies a reason; the rest are further description."),
 dict(q="Which of the following is the best reason for a comparativist to use several of the framework's named data resources together rather than relying on one?",
   choices=[
     "Each resource measures a different aspect of a country, so several together support a fuller comparison than any one alone",
     "Using several resources makes a causal claim certain",
     "The framework requires that all seven be cited in every study",
     "A single resource cannot produce a number",
     "Combining resources converts normative statements into empirical ones"], ans=0,
   why="EK MPA-1.A.8's list is deliberately varied: development, output, growth, distribution, political rights, corruption and state pressure are separate properties, and a country can rank high on one and low on another. Nothing about using several of them overcomes the causal limit in EK MPA-1.A.3."),
 dict(q="A comparative politics essay claims that a course country's regime is stable and supports the claim with the country's twenty-year record of uninterrupted elections, its GDP growth figures, and a passage from a national leader's speech. This combination of evidence is best described as",
   choices=[
     "quantitative and qualitative material used together to support an argument",
     "purely quantitative material, because two of the three sources contain numbers",
     "purely normative material, because stability is a value",
     "a demonstration that elections caused the growth",
     "a description of data with no argument attached"], ans=0,
   why="EK MPA-1.A.1 pairs the two kinds of material, and EK MPA-1.A.6 names supporting an argument as a principal use of empirical information. The election record and growth figures are quantitative, the speech is qualitative, and all three are marshalled behind a claim."),
]
