# AP COMPARATIVE GOVERNMENT AND POLITICS 1.8 Political Legitimacy
# CED effective Fall 2026, Unit 1 Political Systems, Regimes, and Governments.
# Enduring understanding LEG-1 (political legitimacy reinforces the sovereignty of
# the state); learning objective LEG-1.A. Suggested skill 3.C, DATA ANALYSIS --
# which is why this module carries three quantitative sets rather than one.
#
# Essential knowledge relied on:
#   LEG-1.A.1  LEGITIMACY refers to whether a government's constituents BELIEVE
#              their government has the right to use power in the way they do.
#              Legitimacy confers authority on and can increase the power of a
#              regime and government.
#   LEG-1.A.2  sources of legitimacy for BOTH democratic and authoritarian regimes
#              can include POPULAR ELECTIONS and CONSTITUTIONAL PROVISIONS; other
#              sources include NATIONALISM, TRADITION, GOVERNMENTAL EFFECTIVENESS,
#              ECONOMIC GROWTH, IDEOLOGY, RELIGIOUS HERITAGE AND ORGANIZATIONS,
#              and THE DOMINANT POLITICAL PARTY'S ENDORSEMENT
#
# Supporting statements, each named in the verifier's claim where used:
#   PAU-1.A.4  sovereignty is a state's independent legal authority over a
#              population and territory, free of outside interference
#   PAU-1.A.2  international recognition is an element of statehood
#   PAU-1.D.1b Iran's theocracy based on Islamic Sharia law after 1979
#   PAU-3.C.2f the United Kingdom's monarch serves ceremonially as head of state
#   PAU-4.A.2  China allows only the Communist Party of China to control governing
#              power, to maintain the values of centralism and order
#   DEM-1.C.5  Russia holds contested elections with limited competitiveness
#   MPA-1.A.3  causation cannot be isolated and demonstrated with certainty
#
# THE DISTINCTION EVERY ITEM HERE TURNS ON: legitimacy is a matter of BELIEF among
# a government's own constituents. It is not sovereignty (a legal standing), not
# international recognition (other states' acceptance), and not turnout (a
# behavior). Items 3, 4, 22 and 29 key that separately, because a student who
# conflates them can answer most of the topic wrongly in a consistent way.
#
# Table figures are HYPOTHETICAL and labelled so in every stem; the framework
# prints no survey or growth figures for any country.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("1.8", "Political Legitimacy", 1)

_T_TRUST = dict(
    headers=["Country (hypothetical)",
             "Share agreeing the government has the right to use power as it does, 2010",
             "Share agreeing the government has the right to use power as it does, 2020",
             "Share reporting that they voted at the last national election"],
    rows=[["Country L", "74", "61", "68"],
          ["Country M", "52", "58", "41"],
          ["Country N", "39", "35", "83"]])

_T_SOURCES = dict(
    headers=["Source named by respondents as the main reason the government has the right to rule",
             "Country P (hypothetical, percent)", "Country Q (hypothetical, percent)"],
    rows=[["Free elections", "46", "7"],
          ["Constitutional provisions", "21", "12"],
          ["Economic growth", "14", "33"],
          ["Religious heritage", "5", "31"],
          ["The governing party's endorsement", "14", "17"]])

_T_GROWTH = dict(
    headers=["Year", "Annual economic growth (hypothetical, percent)",
             "Share agreeing the government has the right to use power as it does (percent)"],
    rows=[["2014", "6.1", "72"],
          ["2016", "2.3", "64"],
          ["2018", "-1.4", "51"],
          ["2020", "3.0", "57"]])

QUESTIONS = [
 dict(q="The framework defines political legitimacy as",
   choices=[
     "whether a government's constituents believe their government has the right to use power in the way it does",
     "a state's independent legal authority over a population in a particular territory",
     "recognition of a state's government by other states",
     "the share of eligible citizens who vote at national elections",
     "the constitutional rules controlling access to and exercise of political power"], ans=0,
   why="EK LEG-1.A.1 gives exactly this definition. The rejected options are EK PAU-1.A.4's sovereignty, EK PAU-1.A.2's international recognition, a measure of behavior, and EK PAU-1.A.2's regime, each of which is a different concept in the framework."),
 dict(q="What does the framework say legitimacy does for a regime and government?",
   choices=[
     "it confers authority on them and can increase their power",
     "it guarantees that they will win the next election",
     "it substitutes for a written constitution",
     "it transfers sovereignty to them from other states",
     "it removes the need for any use of power at all"], ans=0,
   why="EK LEG-1.A.1 states that legitimacy confers authority on and can increase the power of a regime and government, which is why EK PAU-1.D.2 can say democratic regimes maintain sovereignty using less power. Belief in a government's right to act does part of the work coercion would otherwise have to do."),
 dict(q="Which comparison of legitimacy and sovereignty is consistent with the framework?",
   choices=[
     "Legitimacy is a belief held by a government's own constituents, whereas sovereignty is a state's independent legal authority over a population and territory",
     "Legitimacy is a state's independent legal authority, whereas sovereignty is a belief held by citizens",
     "Both terms refer to a government's recognition by other states",
     "Both terms refer to the constitutional rules controlling access to power",
     "Legitimacy applies only to democracies and sovereignty only to authoritarian regimes"], ans=0,
   why="EK LEG-1.A.1 locates legitimacy in what constituents believe and EK PAU-1.A.4 locates sovereignty in independent legal authority free of outside interference. A state can hold the second while a government struggles for the first, which is why the framework keeps them apart."),
 dict(q="A newly independent state is admitted to international organizations and its borders are accepted by its neighbours, but most of its own citizens deny that its government has any right to rule them. Applying the framework, the state has",
   choices=[
     "the international recognition an element of statehood requires, but a government whose legitimacy is in doubt",
     "legitimacy, since other states have recognized its government",
     "neither statehood nor legitimacy, since recognition is what legitimacy means",
     "legitimacy but not sovereignty, since its citizens are divided",
     "sovereignty only if a majority of its citizens vote in its elections"], ans=0,
   why="EK PAU-1.A.2 makes international recognition an element of statehood, while EK LEG-1.A.1 makes legitimacy a matter of what a government's own constituents believe. Recognition by outsiders cannot supply a belief held by insiders, so the two can come apart exactly as described."),
 dict(q="Which statement about sources of legitimacy is consistent with the framework?",
   choices=[
     "Popular elections and constitutional provisions can be sources of legitimacy for both democratic and authoritarian regimes",
     "Popular elections can be a source of legitimacy only for democratic regimes",
     "Constitutional provisions can be a source of legitimacy only for authoritarian regimes",
     "Authoritarian regimes have no sources of legitimacy",
     "Legitimacy has exactly one source in any given regime"], ans=0,
   why="EK LEG-1.A.2 states that sources of legitimacy for both democratic and authoritarian regimes can include popular elections as well as constitutional provisions. The framework deliberately makes these available to both, which is why holding an election is not by itself evidence that a regime is democratic."),
 dict(q="Besides popular elections and constitutional provisions, which set of sources of legitimacy does the framework name?",
   choices=[
     "nationalism, tradition, governmental effectiveness, economic growth, ideology, religious heritage and organizations, and the dominant political party's endorsement",
     "population size, territorial extent, and international recognition",
     "federalism, devolution, and supranational membership",
     "the independence of the judiciary and the separation of powers",
     "turnout, the number of registered parties, and the length of the electoral term"], ans=0,
   why="EK LEG-1.A.2 lists exactly these as the other sources of legitimacy. The rejected lists are the elements of statehood, territorial structure, features of institutional design, and electoral statistics, none of which the framework offers under this heading."),
 dict(q="A government presents itself as the defender of a shared national identity and history, and its supporters say it has the right to rule because it embodies the nation. Which source of legitimacy named by the framework is at work?",
   choices=[
     "nationalism",
     "tradition",
     "economic growth",
     "constitutional provisions",
     "the dominant political party's endorsement"], ans=0,
   why="EK LEG-1.A.2 names nationalism among the sources of legitimacy. An appeal to a shared national identity rather than to a founding text, a customary practice, economic performance or a party's approval is that source and no other."),
 dict(q="In one state, the head of state's office has been filled by the same hereditary line for centuries, and citizens accept its authority on the ground that it has always been so. Which source of legitimacy is at work?",
   choices=[
     "tradition",
     "ideology",
     "economic growth",
     "governmental effectiveness",
     "popular elections"], ans=0,
   why="EK LEG-1.A.2 names tradition among the sources of legitimacy. EK PAU-3.C.2.f describes the United Kingdom's monarch serving ceremonially as head of state, an office whose claim rests on continuity rather than on election, ideology or performance."),
 dict(q="Citizens of one state say their government has the right to rule because it delivers reliable public services, secure streets and a functioning administration. Which source of legitimacy is at work?",
   choices=[
     "governmental effectiveness",
     "nationalism",
     "religious heritage",
     "tradition",
     "constitutional provisions"], ans=0,
   why="EK LEG-1.A.2 names governmental effectiveness among the sources of legitimacy, and EK LEG-1.B.1 repeats policy effectiveness among the things through which governments maintain legitimacy. What is being credited is performance rather than identity, faith, custom or a founding text."),
 dict(q="A government's support rises through years of rapidly rising incomes and falls sharply when incomes stagnate. Which source of legitimacy does this pattern most directly implicate?",
   choices=[
     "economic growth",
     "religious heritage",
     "tradition",
     "constitutional provisions",
     "nationalism"], ans=0,
   why="EK LEG-1.A.2 names economic growth among the sources of legitimacy, and EK LEG-1.B.3 adds that serious problems such as a poor economy can undermine it. A source that rises and falls with incomes is that one; the others do not move with the business cycle."),
 dict(q="A ruling group justifies its authority by reference to a comprehensive doctrine about how society should be organized, and treats fidelity to that doctrine as the test of who may govern. Which source of legitimacy is at work?",
   choices=[
     "ideology",
     "tradition",
     "governmental effectiveness",
     "economic growth",
     "popular elections"], ans=0,
   why="EK LEG-1.A.2 names ideology among the sources of legitimacy, and EK PAU-4.A.2 describes China's rules reserving governing power to one party to maintain the values of centralism and order, which is a doctrine functioning in this way. Custom, performance, incomes and elections make different claims."),
 dict(q="In one state, religious authorities certify that the government's laws conform to a sacred legal code, and citizens who accept that code accept the government's right to rule on that basis. Which source of legitimacy is at work?",
   choices=[
     "religious heritage and organizations",
     "nationalism",
     "tradition considered apart from any religious claim",
     "governmental effectiveness",
     "the dominant political party's endorsement"], ans=0,
   why="EK LEG-1.A.2 names religious heritage and organizations among the sources of legitimacy, and EK PAU-1.D.1.b describes a theocracy based on Islamic Sharia law as the framework's instance of religion supplying the basis of rule. The claim runs through the religious code, not through custom, performance or a party."),
 dict(q="In one state, an official's authority is widely accepted because the governing party has selected and endorsed that official, and citizens treat the party's approval as settling the question. Which source of legitimacy is at work?",
   choices=[
     "the dominant political party's endorsement",
     "popular elections",
     "constitutional provisions",
     "nationalism",
     "economic growth"], ans=0,
   why="EK LEG-1.A.2 names the dominant political party's endorsement among the sources of legitimacy, and EK PAU-4.A.2 describes a system in which only one party may control governing power. What confers the right to rule in such a case is the party's choice rather than a vote, a text, an identity or a growth rate."),
 dict(q="Which source of legitimacy does the framework's account of Iran most directly illustrate?",
   choices=[
     "religious heritage and organizations",
     "economic growth",
     "tradition unconnected with religion",
     "the endorsement of a dominant secular party",
     "nationalism unconnected with religion"], ans=0,
   why="EK PAU-1.D.1.b describes the transition of power in Iran from dictatorial rule to a theocracy based on Islamic Sharia law, and EK PAU-3.G.1.b adds that the judiciary's major function is to ensure the legal system is based on religious law. EK LEG-1.A.2 names religious heritage and organizations as the corresponding source of legitimacy."),
 dict(q="Which pair of sources of legitimacy does the framework's account of China most directly illustrate?",
   choices=[
     "ideology and the dominant political party's endorsement",
     "popular elections and constitutional provisions considered alone",
     "tradition and religious heritage",
     "nationalism and free elections",
     "economic growth and judicial independence"], ans=0,
   why="EK PAU-4.A.2 states that China's rules allow only the Communist Party of China to control governing power in order to maintain the values of centralism and order, which pairs a doctrine with a party's exclusive endorsement. EK LEG-1.A.2 names both ideology and the dominant political party's endorsement among the sources of legitimacy."),
 dict(q="The United Kingdom's monarch serves ceremonially as head of state while the prime minister exercises executive power. In the framework's terms this arrangement most clearly shows",
   choices=[
     "tradition operating as a source of legitimacy alongside the elected institutions that actually govern",
     "religious heritage replacing elections as the basis of governing authority",
     "ideology supplying the sole basis of the government's right to rule",
     "economic growth conferring authority on the head of state",
     "a dominant party's endorsement determining who occupies the office of head of state"], ans=0,
   why="EK PAU-3.C.2.f describes the monarch serving ceremonially as head of state and formally appointing as prime minister the leader of the largest party in the Commons, so the two claims to authority sit side by side. EK LEG-1.A.2 names tradition among the sources of legitimacy, and EK LEG-1.A.2 also allows a regime more than one source at once."),
 dict(q="Russia holds contested elections with limited degrees of competitiveness. What does the framework's account of legitimacy imply about such elections?",
   choices=[
     "They can still serve as a source of legitimacy, because the framework makes popular elections available to authoritarian as well as democratic regimes",
     "They cannot serve as a source of legitimacy, because only fully competitive elections can",
     "They convert the regime into a consolidated democracy",
     "They are irrelevant to legitimacy, which depends only on economic growth",
     "They show that legitimacy is conferred by other states rather than by citizens"], ans=0,
   why="EK LEG-1.A.2 states that popular elections can be a source of legitimacy for both democratic and authoritarian regimes, and EK DEM-1.C.5 describes Russia as holding contested elections with limited competitiveness. The framework separates what an election contributes to legitimacy from what it shows about regime type."),
 dict(q="Mexico and Nigeria both became multiparty republics with written constitutions and independent election commissions. Which sources of legitimacy does that combination most directly supply?",
   choices=[
     "popular elections and constitutional provisions",
     "religious heritage and tradition",
     "ideology and the endorsement of a dominant party",
     "nationalism and military force",
     "economic growth alone"], ans=0,
   why="EK LEG-1.A.2 names popular elections and constitutional provisions as sources available to both regime types, EK PAU-1.D.1.c records both countries' transitions to multiparty republics, and EK DEM-2.B.4.b records the independent commissions created to reduce fraud and enhance competition. Those institutions are the electoral and constitutional sources in operation."),
 dict(q="Two governments each claim the right to rule: one points to its victory at a competitive election, the other to a religious code its laws are certified to satisfy. What does the framework's account imply about this contrast?",
   choices=[
     "Both are drawing on sources of legitimacy the framework names, so the contrast is between which sources are relied on rather than between having legitimacy and lacking it",
     "Only the first government can have legitimacy, since elections are the only genuine source",
     "Only the second government can have legitimacy, since tradition outweighs elections",
     "Neither can have legitimacy, since legitimacy is conferred by other states",
     "The contrast shows that the two governments must belong to the same regime type"], ans=0,
   why="EK LEG-1.A.2 lists popular elections and religious heritage and organizations among the sources of legitimacy without ranking them, and EK LEG-1.A.1 makes legitimacy a matter of what constituents believe. Which source a government relies on is therefore a separate question from whether its constituents accept its right to rule."),
 dict(q="The table reports hypothetical survey figures for three countries. Which column measures legitimacy as the framework defines it?",
   table=_T_TRUST,
   choices=[
     "the share agreeing the government has the right to use power as it does",
     "the share reporting that they voted at the last national election",
     "both columns equally, since voting and belief are the same thing",
     "neither column, since legitimacy cannot be measured by survey",
     "the difference between the two columns"], ans=0,
   why="EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power in the way it does, which is a belief rather than a behavior. Turnout records what people did, and the framework treats participation separately under EK DEM-1.A and EK DEM-1.B."),
 dict(q="Using the same table, which country's agreement figure fell the most between the two years shown?",
   table=_T_TRUST,
   choices=[
     "Country L, by 13 percentage points",
     "Country M, by 6 percentage points",
     "Country N, by 4 percentage points",
     "Country N, by 44 percentage points",
     "No country's figure fell"], ans=0,
   why="Subtracting each country's earlier figure from its later one gives the change, and only two of the three are negative. The largest of the figures offered against the key is a comparison across columns that measure different things rather than a change over time."),
 dict(q="One country in the table combines the highest reported turnout with the lowest agreement figure in both years. Which conclusion does this best support?",
   table=_T_TRUST,
   choices=[
     "High participation does not by itself establish that constituents believe the government has the right to use power as it does",
     "High participation always indicates high legitimacy",
     "Low agreement always produces low participation",
     "Turnout and legitimacy are two names for the same quantity",
     "The country with the highest turnout must be a consolidated democracy"], ans=0,
   why="EK LEG-1.A.1 makes legitimacy a belief about the government's right to use power, while EK DEM-1.A.4 notes that formal participation can be encouraged across regime types, including to give an illusion of influence. A row that pairs the highest turnout with the lowest agreement is exactly what those two statements together allow."),
 dict(q="The table reports the source respondents in two hypothetical countries name as the main reason their government has the right to rule. Which conclusion does it support?",
   table=_T_SOURCES,
   choices=[
     "Both countries draw on several of the sources the framework names, but the leading source differs between them",
     "Only one of the two countries draws on any source the framework names",
     "Both countries rely on a single source to the exclusion of all others",
     "Neither country's respondents name a source the framework lists",
     "The two countries name the sources in the same order of importance"], ans=0,
   why="EK LEG-1.A.2 lists popular elections, constitutional provisions, economic growth, religious heritage and organizations, and the dominant political party's endorsement among the sources of legitimacy, and every row of the table names one of them. Reading down each column shows support spread across several rows in both cases, with different rows leading."),
 dict(q="Using the same table, the source on which the two countries differ most is",
   table=_T_SOURCES,
   choices=[
     "free elections, a difference of 39 percentage points",
     "religious heritage, a difference of 26 percentage points",
     "economic growth, a difference of 19 percentage points",
     "constitutional provisions, a difference of 9 percentage points",
     "the governing party's endorsement, a difference of 3 percentage points"], ans=0,
   why="Taking the absolute difference between the two columns in each row and comparing them identifies the largest gap. Each of the alternatives states the correct gap for a different row, so the item turns on comparing the five differences rather than on computing any one of them."),
 dict(q="A student concludes from the same table that the country whose respondents rarely name free elections has no legitimacy at all. The best objection is that",
   table=_T_SOURCES,
   choices=[
     "the framework names several sources besides elections, and that country's respondents concentrate on two of them",
     "the framework names elections as the only source of legitimacy",
     "the table reports no information about that country",
     "legitimacy is conferred by other states rather than by a government's own constituents",
     "the two countries' figures cannot be compared because both are hypothetical"], ans=0,
   why="EK LEG-1.A.2 names nationalism, tradition, governmental effectiveness, economic growth, ideology, religious heritage and organizations, and a dominant party's endorsement alongside elections and constitutional provisions. Two of those rows carry most of that country's column, so the conclusion mistakes one source for the whole list."),
 dict(q="The table reports hypothetical annual growth and agreement figures for one country across four years. Which conclusion does it support?",
   table=_T_GROWTH,
   choices=[
     "Agreement fell in each year that growth slowed and rose in the year growth recovered, which is consistent with economic growth acting as a source of legitimacy",
     "Agreement rose in every year regardless of growth",
     "Agreement was unrelated to growth across the four years",
     "Growth was negative in every year shown",
     "Agreement was at its highest in the year growth was lowest"], ans=0,
   why="EK LEG-1.A.2 names economic growth among the sources of legitimacy and EK LEG-1.B.3 says a poor economy can undermine legitimacy. Reading the two columns year by year, they move in the same direction at every step, which is what those statements would lead a student to expect."),
 dict(q="A commentator uses the same four years of data to argue that slowing growth caused the fall in agreement. Which objection does the framework most directly support?",
   table=_T_GROWTH,
   choices=[
     "Four paired observations show an association, and the framework denies that causation can be isolated and demonstrated with certainty from such evidence",
     "The two columns do not in fact move together, so there is nothing to explain",
     "Economic growth is not one of the sources of legitimacy the framework names",
     "Causation can be established only where the data cover more than one country",
     "Survey data can never be used to study legitimacy"], ans=0,
   why="EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls an observed co-movement an association. The columns do move together, so what fails is the causal step rather than the reading of the data."),
 dict(q="Which finding would most strongly indicate that a government's legitimacy is weakening in the framework's sense?",
   choices=[
     "A growing share of citizens say the government has no right to make the decisions it is making",
     "The government has lost seats at a regional election",
     "The government has been criticized by another country's foreign ministry",
     "The government has reorganized two ministries",
     "The governing party has changed its leader"], ans=0,
   why="EK LEG-1.A.1 makes legitimacy a matter of whether a government's constituents believe it has the right to use power in the way it does, so evidence about it must be evidence about that belief. Seat losses, foreign criticism, reorganization and a leadership change are all compatible with citizens continuing to accept the government's right to act."),
 dict(q="Two governments deliver equally effective public services, but in one country most citizens accept the government's right to make the decisions it makes and in the other most do not. What does the framework's definition imply?",
   choices=[
     "The first government has greater legitimacy, since legitimacy is constituted by the belief rather than by the performance that may produce it",
     "Both have equal legitimacy, since their performance is equal",
     "The second has greater legitimacy, since dissatisfaction shows citizens are engaged",
     "Neither has legitimacy, since legitimacy requires a competitive election",
     "Legitimacy cannot differ between two governments with the same level of effectiveness"], ans=0,
   why="EK LEG-1.A.1 defines legitimacy as the belief of a government's constituents, while EK LEG-1.A.2 lists governmental effectiveness as one of several possible SOURCES of that belief. A source may be present without producing the belief, which is why performance and legitimacy can come apart."),
 dict(q="Taking the framework's two statements on legitimacy together, which summary is most accurate?",
   choices=[
     "Legitimacy is a belief among a government's constituents that it has the right to use power as it does, it confers authority and can increase a regime's power, and it can be drawn from any of several named sources available to democratic and authoritarian regimes alike",
     "Legitimacy is a legal standing conferred by other states, and only democratic regimes possess it",
     "Legitimacy is identical to sovereignty and has a single source, the constitution",
     "Legitimacy is measured by turnout and has no bearing on a regime's power",
     "Legitimacy is available only to regimes that hold fully competitive elections"], ans=0,
   why="EK LEG-1.A.1 supplies the definition and the consequence, that legitimacy confers authority on and can increase the power of a regime and government, while EK LEG-1.A.2 supplies the plural sources and says they are available to both regime types. The summary keeps all three parts rather than collapsing them."),
]
