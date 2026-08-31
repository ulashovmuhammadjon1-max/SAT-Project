# AP COMPARATIVE GOVERNMENT AND POLITICS 5.1 Impact of Global Economic and
# Technological Forces
# CED effective Fall 2026, Unit 5 Political and Economic Changes and Development.
# Enduring understanding IEF-3 (economic globalization and economic
# liberalization have positively and negatively affected political policies and
# behaviors); learning objective IEF-3.A. Suggested skill 3.A, Data Analysis
# (describe the data presented).
#
# Essential knowledge relied on:
#   IEF-3.A.1  ECONOMIC GLOBALIZATION -- including ECONOMIC NETWORKS THAT ARE
#              GROWING MORE INTERCONNECTED, a WORLDWIDE MARKET WITH ACTORS
#              UNCONSTRAINED BY POLITICAL BORDERS, and a REDUCTION IN STATE CONTROL
#              OVER ECONOMIES -- has DEEPENED CROSS-NATIONAL CONNECTIONS AMONG
#              WORKERS, GOODS, AND CAPITAL and has CAUSED CHALLENGES FOR REGIME AND
#              CULTURAL STABILITY
#   IEF-3.A.2  STATE MEMBERSHIP IN the INTERNATIONAL MONETARY FUND, the WORLD BANK
#              and the WORLD TRADE ORGANIZATION HAS PROMOTED ECONOMIC
#              LIBERALIZATION POLICIES
#     .a CHINA AND NIGERIA have enacted economic liberalization policies and A
#        MAJORITY OF RESPONDENTS IN RECENT STUDIES have said they EXPECT CHILDREN IN
#        THEIR COUNTRIES TO BE BETTER OFF THAN THEIR PARENTS
#     .b in MEXICO, IN PART AS A RESULT OF THESE POLICIES, the NUMBER OF PEOPLE IN
#        THE MIDDLE CLASS HAS GROWN
#   IEF-3.A.3  MULTINATIONAL CORPORATIONS INCREASINGLY DOMINATE GLOBAL MARKETS and
#              POSE CHALLENGES TO, AND SOMETIMES CONFLICT WITH, DOMESTIC ECONOMIC
#              POLICIES REGARDING LABOR, THE ENVIRONMENT, LAND RIGHTS, TAXATION, AND
#              THE BUDGET
#   IEF-3.A.4  GLOBALIZATION AND NEOLIBERALISM CAN PROVOKE CONFLICTS WITHIN STATES,
#              including:
#     .a INCREASED DEMANDS BEING PLACED ON GOVERNMENTS BY CIVIL SOCIETY GROUPS
#     .b PROTESTS BY STUDENTS AND DISENFRANCHISED GROUPS
#     .c ARRESTS OF PROTESTERS AND IMPOSITION OF SOCIAL MEDIA RESTRICTIONS
#     .d EMPOWERMENT OF ONCE-MARGINAL, NATIONALIST, AND POPULIST GROUPS THAT BLAME
#        THE GOVERNMENT FOR CHANGES IN CULTURE AND ECONOMIC CONDITIONS
#
# THE WORD THE FRAMEWORK CHOOSES, AND THE ITEMS THAT REST ON IT: IEF-3.A.4 says
# conflicts WITHIN states. The whole statement is about domestic politics, not
# about disputes between governments, and its four items run in a recognizable
# sequence -- demands, then protest, then repression of protest, then the rise of
# groups that blame the government. Items 10 to 13, 18 and the third table follow
# that sequence, which is also why the table's four columns must move together
# for its key to hold.
#
# WHAT IS DELIBERATELY NOT ASSERTED: this is the unit the SOCIAL_BRIEF warns about,
# because public policy and economic change move with events. Nothing here turns
# on a growth rate, an exchange rate, an election, or any figure that could be
# out of date. The only country-specific claims made are the three the framework
# itself states -- China and Nigeria enacting liberalization policies with a
# majority of survey respondents expecting children to be better off than their
# parents (IEF-3.A.2.a), and Mexico's middle class having grown in part as a
# result of those policies (IEF-3.A.2.b). Every number in every table is
# HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("5.1", "Impact of Global Economic and Technological Forces", 5)

_T_OPTIMISM = dict(
    headers=["Country (hypothetical)",
             "Respondents expecting children to be better off than their parents (percent)",
             "Economic liberalization policies enacted"],
    rows=[["Country 1", "64", "Yes"],
          ["Country 2", "58", "Yes"],
          ["Country 3", "41", "No"],
          ["Country 4", "29", "No"]])

_T_MNC = dict(
    headers=["Domestic policy area",
             "Disputes recorded between the government and multinational corporations (hypothetical)"],
    rows=[["Labor", "14"],
          ["The environment", "22"],
          ["Land rights", "9"],
          ["Taxation", "31"],
          ["The budget", "6"]])

_T_CONFLICT = dict(
    headers=["Year (hypothetical)", "Demands submitted to the government by civil society groups",
             "Protest events led by students and other groups", "Protesters arrested",
             "Days on which social media services were restricted"],
    rows=[["Year 1", "120", "14", "60", "0"],
          ["Year 2", "260", "39", "410", "6"],
          ["Year 3", "515", "72", "990", "21"]])

QUESTIONS = [
 dict(q="Which three features does the framework include in its description of economic globalization?",
   choices=[
     "economic networks growing more interconnected, a worldwide market with actors unconstrained by political borders, and a reduction in state control over economies",
     "rising tariffs, currency controls, and the nationalization of banks",
     "the creation of ethnic quotas, the raising of thresholds, and the redrawing of districts",
     "an expansion of state ownership, the end of foreign investment, and the closing of borders",
     "the growth of political parties, the widening of the franchise, and the strengthening of legislatures"], ans=0,
   why="EK IEF-3.A.1 names economic networks that are growing more interconnected, a worldwide market with actors unconstrained by political borders, and a reduction in state control over economies as the content of economic globalization. The rejected sets run the opposite way or belong to other units."),
 dict(q="What does the framework say economic globalization has deepened?",
   choices=[
     "cross-national connections among workers, goods, and capital",
     "the authority of national regulators over prices",
     "the separation of national economies from one another",
     "the number of state-owned enterprises in each country",
     "the powers of regional legislatures over trade"], ans=0,
   why="EK IEF-3.A.1 states that economic globalization has deepened cross-national connections among workers, goods, and capital, so the three things it connects are people, products and money rather than institutions."),
 dict(q="What kinds of challenge does the framework say economic globalization has caused?",
   choices=[
     "challenges for regime and cultural stability",
     "challenges only to a country's balance of trade",
     "challenges only to the independence of its courts",
     "challenges only to the size of its armed forces",
     "no challenges, since it deepens connections"], ans=0,
   why="EK IEF-3.A.1 states that economic globalization has caused challenges for regime and cultural stability, so the framework's concern extends beyond economic measures to how a regime holds and how a culture changes."),
 dict(q="Membership in which three organizations does the framework say has promoted economic liberalization policies?",
   choices=[
     "the International Monetary Fund, the World Bank, and the World Trade Organization",
     "the Economic Community of West African States, the European Union, and the United Nations",
     "the World Health Organization, the World Bank, and the International Court of Justice",
     "the United Nations, the World Trade Organization, and the International Labour Organization",
     "the European Union, the International Monetary Fund, and the African Union"], ans=0,
   why="EK IEF-3.A.2 names state membership in the International Monetary Fund, the World Bank, and the World Trade Organization as having promoted economic liberalization policies. The supranational bodies in the rejected sets are treated under EK LEG-3.A.3 instead."),
 dict(q="What does the framework say membership in those organizations has promoted?",
   choices=[
     "economic liberalization policies",
     "the nationalization of key industries",
     "the imposition of higher tariffs on imports",
     "the creation of ethnic quotas in legislatures",
     "the extension of executive term limits"], ans=0,
   why="EK IEF-3.A.2 states that state membership in the International Monetary Fund, the World Bank and the World Trade Organization has promoted economic liberalization policies, which is a claim about the direction those memberships push policy."),
 dict(q="Which two course countries does the framework name as having enacted economic liberalization policies alongside a survey finding about expectations for the next generation?",
   choices=[
     "China and Nigeria",
     "Russia and Iran",
     "Mexico and the United Kingdom",
     "Iran and Nigeria",
     "China and Russia"], ans=0,
   why="EK IEF-3.A.2.a names China and Nigeria as having enacted economic liberalization policies and records that a majority of respondents in recent studies said they expect children in their countries to be better off than their parents."),
 dict(q="What did a majority of respondents in the studies the framework cites say about the countries named in EK IEF-3.A.2.a?",
   choices=[
     "that they expect children in their countries to be better off than their parents",
     "that they expect their governments to nationalize key industries",
     "that they oppose membership in international financial organizations",
     "that they expect emigration to rise sharply",
     "that they regard their courts as independent"], ans=0,
   why="EK IEF-3.A.2.a records that a majority of respondents in recent studies said they expect children in their countries to be better off than their parents, which is a statement about expectations rather than about measured incomes."),
 dict(q="What change does the framework record in Mexico, in part as a result of economic liberalization policies?",
   choices=[
     "the number of people in the middle class has grown",
     "the number of registered political parties has fallen",
     "state ownership of industry has expanded",
     "tariffs on imported goods have risen",
     "membership in international financial organizations has ended"], ans=0,
   why="EK IEF-3.A.2.b states that in Mexico, in part as a result of these policies, the number of people in the middle class has grown, and the qualifier in part is the framework's own."),
 dict(q="What does the framework say about the position of multinational corporations in global markets?",
   choices=[
     "they increasingly dominate global markets",
     "they are steadily losing ground to state-owned firms",
     "they operate only in countries that are not members of international financial organizations",
     "they are confined to the countries in which they were founded",
     "they have no bearing on domestic economic policy"], ans=0,
   why="EK IEF-3.A.3 states that multinational corporations increasingly dominate global markets and pose challenges to, and sometimes conflict with, domestic economic policies."),
 dict(q="Which domestic policy areas does the framework name as the ones multinational corporations challenge and sometimes conflict with?",
   choices=[
     "labor, the environment, land rights, taxation, and the budget",
     "elections, party registration, and campaign finance",
     "judicial appointments, court jurisdiction, and criminal procedure",
     "defense, foreign affairs, and treaty ratification",
     "education, health care, and gender equity"], ans=0,
   why="EK IEF-3.A.3 names domestic economic policies regarding labor, the environment, land rights, taxation, and the budget as the areas multinational corporations pose challenges to and sometimes conflict with."),
 dict(q="Where does the framework locate the conflicts that globalization and neoliberalism can provoke?",
   choices=[
     "within states",
     "between states and supranational organizations only",
     "between neighboring states only",
     "between international financial organizations",
     "within multinational corporations"], ans=0,
   why="EK IEF-3.A.4 states that globalization and neoliberalism can provoke conflicts within states, and each of the four items it lists concerns domestic actors rather than relations between governments."),
 dict(q="Which of the following does the framework list among the conflicts globalization and neoliberalism can provoke within a state?",
   choices=[
     "increased demands being placed on governments by civil society groups",
     "the transfer of sovereignty to a supranational body",
     "the abolition of a country's currency",
     "the redrawing of a country's international boundaries",
     "the merger of political parties into a single party"], ans=0,
   why="EK IEF-3.A.4.a names increased demands being placed on governments by civil society groups as one of the conflicts globalization and neoliberalism can provoke within states."),
 dict(q="Which pair does the framework list together as one of those conflicts?",
   choices=[
     "arrests of protesters and imposition of social media restrictions",
     "the raising of tariffs and the closing of borders",
     "the nationalization of banks and the abolition of parties",
     "the extension of term limits and the appointment of governors",
     "the creation of ethnic quotas and the raising of thresholds"], ans=0,
   why="EK IEF-3.A.4.c pairs arrests of protesters with the imposition of social media restrictions in a single item, so the framework treats the physical and the informational responses as one kind of conflict."),
 dict(q="How does the framework describe the groups that gain from the conflicts globalization can provoke?",
   choices=[
     "once-marginal, nationalist, and populist groups that blame the government for changes in culture and economic conditions",
     "state-sanctioned peak associations representing labor and business",
     "multinational corporations seeking lower taxes",
     "international financial organizations setting loan conditions",
     "regional parties seeking seats in single-member districts"], ans=0,
   why="EK IEF-3.A.4.d names the empowerment of once-marginal, nationalist, and populist groups that blame the government for changes in culture and economic conditions, so the framework's account joins a cultural grievance to an economic one."),
 dict(q="Which element of the framework's account of economic globalization bears most directly on a government's ability to steer its own economy?",
   choices=[
     "a reduction in state control over economies",
     "the deepening of connections among workers, goods, and capital",
     "the growth of interconnected economic networks",
     "membership in international financial organizations",
     "the empowerment of once-marginal groups"], ans=0,
   why="EK IEF-3.A.1 names a reduction in state control over economies as one of the three components of economic globalization, which is the component stated in terms of what a government can and cannot do."),
 dict(q="A government finds that investment funds enter and leave its financial markets faster than its regulators can respond, and that the firms involved answer to no single jurisdiction. Which part of the framework's account does this best illustrate?",
   choices=[
     "a worldwide market with actors unconstrained by political borders",
     "the imposition of social media restrictions",
     "the growth of a middle class",
     "the dominance of state-sanctioned peak associations",
     "membership in a supranational organization with sovereign powers"], ans=0,
   why="EK IEF-3.A.1 names a worldwide market with actors unconstrained by political borders among the features of economic globalization, and actors answering to no single jurisdiction is that feature described in operation."),
 dict(q="A large foreign-owned firm disputes the tax it owes and the size of the payment it makes toward a government's spending plans. Which framework claim does this most directly illustrate?",
   choices=[
     "that multinational corporations pose challenges to, and sometimes conflict with, domestic economic policies regarding taxation and the budget",
     "that civil society groups place increased demands on governments",
     "that membership in international financial organizations promotes liberalization",
     "that once-marginal groups blame the government for cultural change",
     "that economic networks are growing more interconnected"], ans=0,
   why="EK IEF-3.A.3 names taxation and the budget among the domestic economic policy areas that multinational corporations pose challenges to and sometimes conflict with."),
 dict(q="During a wave of demonstrations against an economic reform, a government detains demonstrators and restricts access to social media platforms. Which item in the framework's list does this match?",
   choices=[
     "arrests of protesters and imposition of social media restrictions",
     "increased demands being placed on governments by civil society groups",
     "protests by students and disenfranchised groups",
     "empowerment of once-marginal, nationalist, and populist groups",
     "a reduction in state control over economies"], ans=0,
   why="EK IEF-3.A.4.c names arrests of protesters and imposition of social media restrictions as one of the conflicts globalization and neoliberalism can provoke within states, and the scenario contains both halves of that item."),
 dict(q="Why does the framework treat globalization as a challenge to cultural stability and not only to economic conditions?",
   choices=[
     "because it records groups gaining influence by blaming the government for changes in culture as well as in economic conditions",
     "because it states that culture determines a country's rate of economic growth",
     "because it states that multinational corporations set cultural policy",
     "because it states that international financial organizations require cultural change as a loan condition",
     "because it states that cultural change occurs only where economies are closed"], ans=0,
   why="EK IEF-3.A.1 states that economic globalization has caused challenges for regime and cultural stability, and EK IEF-3.A.4.d gives the political form that takes, since the groups it names blame the government for changes in culture and economic conditions together."),
 dict(q="Read in order, the four items in EK IEF-3.A.4 describe a sequence. Which description of that sequence is most accurate?",
   choices=[
     "demands are placed on the government, protests follow, the state responds by arresting protesters and restricting communications, and groups that blame the government gain ground",
     "a government liberalizes, foreign investment rises, and incomes converge",
     "a government raises tariffs, imports fall, and domestic industry expands",
     "an international organization imposes conditions, a government complies, and the conditions are lifted",
     "a movement forms locally, spreads regionally, and then dissolves"], ans=0,
   why="EK IEF-3.A.4 lists increased civil society demands, protests by students and disenfranchised groups, arrests of protesters together with social media restrictions, and the empowerment of groups that blame the government, in that order."),
 dict(q="The table reports hypothetical survey results alongside each country's policy record. Which rows show the combination the framework records for the two countries it names in EK IEF-3.A.2.a?",
   table=_T_OPTIMISM,
   choices=[
     "the first two rows, where a majority expect children to be better off and liberalization policies have been enacted",
     "the last two rows, where fewer than half expect children to be better off",
     "the first and last rows only",
     "all four rows, since each reports a survey figure",
     "none of the rows, since the framework reports no survey findings"], ans=0,
   why="EK IEF-3.A.2.a states that China and Nigeria have enacted economic liberalization policies and that a majority of respondents in recent studies said they expect children in their countries to be better off than their parents, so the matching rows need both a majority above half and a record of liberalization."),
 dict(q="According to the same table, the number of countries in which more than half of respondents expect children to be better off than their parents is",
   table=_T_OPTIMISM,
   choices=[
     "2",
     "4",
     "3",
     "1",
     "0"], ans=0,
   why="Counting the rows whose survey figure exceeds half gives the answer. The alternatives are the number of rows in the table, the count obtained by including a row below half, a count that omits one qualifying row, and a claim that none qualifies."),
 dict(q="Using the same table, the gap between the highest and lowest shares expecting children to be better off is",
   table=_T_OPTIMISM,
   choices=[
     "35 percentage points",
     "23 percentage points",
     "12 percentage points",
     "6 percentage points",
     "64 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the gap. The alternatives are the gaps between other pairs in the same column and the largest single figure read as though it were a gap."),
 dict(q="The table records hypothetical disputes between one government and multinational corporations, by policy area. Which area accounts for the most disputes?",
   table=_T_MNC,
   choices=[
     "taxation, with 31 disputes",
     "the environment, with 22 disputes",
     "labor, with 14 disputes",
     "land rights, with 9 disputes",
     "the budget, with 6 disputes"], ans=0,
   why="EK IEF-3.A.3 names labor, the environment, land rights, taxation, and the budget as the domestic economic policy areas multinational corporations challenge, and the table reports those five areas, so the comparison stays inside the framework's own list."),
 dict(q="According to the same table of disputes, the total number recorded across all five policy areas is",
   table=_T_MNC,
   choices=[
     "82",
     "76",
     "67",
     "51",
     "31"], ans=0,
   why="Adding the dispute column across the five rows gives the total. The alternatives are the total with the smallest row omitted, the total of the three largest rows, the total with the largest row omitted, and the largest single row."),
 dict(q="Using the same table of disputes, the difference between the policy area with the most disputes and the one with the fewest is",
   table=_T_MNC,
   choices=[
     "25",
     "22",
     "17",
     "9",
     "37"], ans=0,
   why="Subtracting the smallest row from the largest gives the difference. The alternatives are other rows and gaps within the same column, and the two extreme rows added together instead of subtracted."),
 dict(q="The table records four measures of political conflict in one hypothetical country across three years. Which conclusion does it support?",
   table=_T_CONFLICT,
   choices=[
     "Civil society demands, protest events, arrests, and days of social media restriction all rose together across the three years",
     "Demands rose while protests, arrests, and restrictions all fell",
     "Arrests rose while every other column fell",
     "None of the four columns changed across the three years",
     "Restrictions were imposed in every year of the period"], ans=0,
   why="EK IEF-3.A.4 lists increased civil society demands, protests by students and disenfranchised groups, arrests of protesters and social media restrictions among the conflicts globalization and neoliberalism can provoke within states, and every column in the table rises across the period."),
 dict(q="According to the same table of three years, the increase in the number of protesters arrested between the first year and the third is",
   table=_T_CONFLICT,
   choices=[
     "930",
     "580",
     "350",
     "990",
     "1050"], ans=0,
   why="Subtracting the first year's figure from the third year's gives the increase. The alternatives are the increases across the other pairs of years, the third year's own figure, and the first and third years added together instead of subtracted."),
 dict(q="Using the same table of three years, the total number of days on which social media services were restricted is",
   table=_T_CONFLICT,
   choices=[
     "27",
     "21",
     "6",
     "48",
     "125"], ans=0,
   why="Adding that column across the three years gives the total. The alternatives are the largest single year, the middle year, the total counted twice against its largest year, and the total of a different column."),
 dict(q="Taking EK IEF-3.A as a whole, which summary is most accurate?",
   choices=[
     "Globalization has knitted economies together while reducing what states control, membership in international financial organizations has pushed governments toward liberalization, multinational firms increasingly contest domestic economic policy, and the resulting strains show up inside states as demands, protest, repression, and the rise of groups that blame the government",
     "Globalization has affected economies without any political consequences",
     "Globalization has increased state control over national economies",
     "Globalization produces conflicts only between governments and never inside them",
     "Globalization has had identical effects in every course country"], ans=0,
   why="EK IEF-3.A.1 supplies the description of globalization and its challenges to regime and cultural stability, EK IEF-3.A.2 the push toward liberalization from membership in international financial organizations, EK IEF-3.A.3 the challenge from multinational corporations, and EK IEF-3.A.4 the four conflicts within states."),
]
