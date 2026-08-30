# AP COMPARATIVE GOVERNMENT AND POLITICS 3.2 Political Culture
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding IEF-1; learning objective IEF-1.C (explain how political culture
# relates to citizen behavior and the role of the state). Suggested skill 2.C,
# Country Comparison.
#
# Essential knowledge relied on:
#   IEF-1.C.1  POLITICAL CULTURE is the COLLECTIVE ATTITUDES, VALUES AND BELIEFS of
#              the citizenry and the NORMS OF BEHAVIOR in the political system; it
#              SETS EXPECTATIONS ABOUT THE EXERCISE OF POWER to establish a BALANCE
#              BETWEEN SOCIAL ORDER AND INDIVIDUAL LIBERTY
#   IEF-1.C.2  political culture is INFLUENCED BY factors of GEOGRAPHY, RELIGIOUS
#              TRADITIONS and HISTORY, forming a population's values and beliefs
#              about the ROLE OF GOVERNMENT, the RIGHTS OF THE INDIVIDUAL, and the
#              EXTENT AND ROLE OF CITIZENS IN CONTROLLING GOVERNMENT POLICY MAKING
#   IEF-1.C.3  political culture is transmitted through POLITICAL SOCIALIZATION, the
#              LIFELONG PROCESS of acquiring one's beliefs, values and orientations
#              toward the political system
#   IEF-1.C.4  FAMILY, SCHOOLS, PEERS, RELIGIOUS INSTITUTIONS, MEDIA and SOCIAL
#              ENVIRONMENTS INCLUDING CIVIC ORGANIZATIONS play a crucial role in
#              socialization and help develop political attitudes and values
#   IEF-1.C.5  though many agents of socialization are SIMILAR ACROSS REGIME TYPES,
#              AUTHORITARIAN REGIMES APPLY MORE CONCERTED GOVERNMENTAL PRESSURES to
#              socialize their citizens around conforming beliefs than do democratic
#              regimes
#
# IEF-1.C.5 is another of the framework's difference-OF-DEGREE claims, like
# DEM-1.C.2 on media and DEM-1.B.3 on participation: the AGENTS are similar in both
# regime types and the GOVERNMENTAL PRESSURE differs. Items 13, 15 and 25 key that,
# because the intuitive reading -- that socialization is something only
# authoritarian regimes do -- is not the framework's.
#
# Supporting statements used: LEG-1.A.2 (tradition and ideology among the sources of
# legitimacy), IEF-1.C.6 (political ideology, for the contrast in item 16),
# MPA-1.A.3 (causation cannot be isolated).
#
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.2", "Political Culture", 3)

_T_ORDER = dict(
    headers=["Country (hypothetical)",
             "Share agreeing that maintaining order should take priority over individual liberty (percent)",
             "Share agreeing that citizens should have a say in policy between elections (percent)",
             "Share saying they learned their political views mainly from family (percent)"],
    rows=[["Country A", "71", "28", "54"],
          ["Country B", "34", "69", "31"],
          ["Country C", "52", "47", "42"]])

_T_AGENT = dict(
    headers=["Agent of socialization (hypothetical survey)",
             "Share naming it as their main influence in Country D (percent)",
             "Share naming it as their main influence in Country E (percent)"],
    rows=[["Family", "46", "39"],
          ["Schools", "18", "34"],
          ["Peers", "11", "7"],
          ["Religious institutions", "14", "6"],
          ["Media", "11", "14"]])

QUESTIONS = [
 dict(q="How does the framework define political culture?",
   choices=[
     "the collective attitudes, values and beliefs of the citizenry and the norms of behavior in the political system",
     "the set of institutions legally empowered to make binding decisions for a state",
     "the rules controlling access to and the exercise of political power",
     "a set of values and beliefs about the goals of government held by an organized movement",
     "the share of citizens who vote at national elections"], ans=0,
   why="EK IEF-1.C.1 gives exactly this definition. The rejected options describe EK PAU-1.A.4's government, EK PAU-1.A.2's regime, EK IEF-1.C.6's political ideology and a measure of behavior."),
 dict(q="What does the framework say political culture sets expectations about?",
   choices=[
     "the exercise of power, so as to establish a balance between social order and individual liberty",
     "the number of political parties permitted to compete",
     "the territorial structure of the state",
     "the length of the head of government's term",
     "the qualifications required of judges"], ans=0,
   why="EK IEF-1.C.1 states that political culture sets expectations about the exercise of power to establish a balance between social order and individual liberty. That tension is the enduring understanding IEF-1 names in its own wording."),
 dict(q="Which factors does the framework say influence political culture?",
   choices=[
     "geography, religious traditions and history",
     "the number of chambers in the legislature and the length of its terms",
     "the rate of economic growth and the level of foreign investment",
     "the electoral system and the threshold for representation",
     "the size of the civil service and the number of ministries"], ans=0,
   why="EK IEF-1.C.2 names factors of geography, religious traditions and history as the influences on political culture. Institutional and economic features appear elsewhere in the framework and are not offered under this heading."),
 dict(q="According to the framework, what do those influences form in a population?",
   choices=[
     "values and beliefs about the role of government, the rights of the individual, and the extent and role of citizens in controlling government policy making",
     "the constitutional rules by which power is transferred",
     "the boundaries of electoral districts",
     "the composition of the cabinet",
     "the state's international recognition"], ans=0,
   why="EK IEF-1.C.2 states that geography, religious traditions and history form a population's values and beliefs about the role of government, the rights of the individual, and the extent and role of citizens in controlling government policy making. All three are beliefs, not institutions."),
 dict(q="How does the framework define political socialization?",
   choices=[
     "the lifelong process of acquiring one's beliefs, values and orientations toward the political system",
     "the process by which a government registers voters before an election",
     "the process by which a party recruits candidates for office",
     "the transfer of power from one government to the next",
     "the process by which a state grants citizenship to residents"], ans=0,
   why="EK IEF-1.C.3 defines political socialization as the lifelong process of acquiring one's beliefs, values and orientations toward the political system, and states that political culture is transmitted through it."),
 dict(q="Which feature of political socialization does the framework's definition emphasize?",
   choices=[
     "that it lasts a lifetime rather than ending in childhood",
     "that it is completed before a citizen first votes",
     "that it occurs only through formal schooling",
     "that it is directed by the state in every regime",
     "that it applies only to citizens who join a political party"], ans=0,
   why="EK IEF-1.C.3 calls socialization the LIFELONG process of acquiring one's beliefs, values and orientations toward the political system, and EK IEF-1.C.4 names agents that operate at different stages of life. Confining it to childhood or to schooling contradicts both."),
 dict(q="Which set of agents does the framework name as playing a crucial role in political socialization?",
   choices=[
     "family, schools, peers, religious institutions, media, and social environments including civic organizations",
     "the legislature, the executive and the judiciary",
     "electoral commissions, party headquarters and polling firms",
     "supranational organizations and foreign governments",
     "the armed forces and the police alone"], ans=0,
   why="EK IEF-1.C.4 names exactly these agents and says they play a crucial role in the socialization process and help develop political attitudes and values. State institutions and foreign bodies are not on that list."),
 dict(q="A child grows up hearing parents discuss elections and absorbs their assumptions about what government is for. Which agent of socialization does this illustrate?",
   choices=[
     "family",
     "schools",
     "peers",
     "religious institutions",
     "media"], ans=0,
   why="EK IEF-1.C.4 names family first among the agents that play a crucial role in the socialization process. EK IEF-1.C.3's description of socialization as lifelong is why the process does not end when the child leaves home."),
 dict(q="A national curriculum requires every pupil to study the state's founding narrative and its constitutional arrangements. Which agent of socialization does this illustrate?",
   choices=[
     "schools",
     "family",
     "peers",
     "media",
     "civic organizations"], ans=0,
   why="EK IEF-1.C.4 names schools among the agents of socialization, and EK IEF-1.C.5 adds that authoritarian regimes apply more concerted governmental pressures to socialize citizens around conforming beliefs, of which a mandated curriculum is one possible instrument."),
 dict(q="A student's political views shift after joining a circle of friends who argue about policy every week. Which agent of socialization does this illustrate?",
   choices=[
     "peers",
     "family",
     "schools",
     "religious institutions",
     "media"], ans=0,
   why="EK IEF-1.C.4 names peers among the agents that play a crucial role in socialization. EK IEF-1.C.3's lifelong framing is why an adult's views can still move under such influence."),
 dict(q="A congregation's teaching about obligations to the poor shapes members' expectations of what the state should provide. Which agent of socialization does this illustrate?",
   choices=[
     "religious institutions",
     "peers",
     "schools",
     "media",
     "family"], ans=0,
   why="EK IEF-1.C.4 names religious institutions among the agents of socialization, and EK IEF-1.C.2 names religious traditions among the influences on political culture. The two statements point at the same source from different angles."),
 dict(q="Regular exposure to news coverage and to a neighborhood association's campaigns shapes a citizen's view of what government should do. Which agents of socialization does this illustrate?",
   choices=[
     "media and social environments including civic organizations",
     "family and peers",
     "schools and religious institutions",
     "the legislature and the courts",
     "an electoral commission and a political party"], ans=0,
   why="EK IEF-1.C.4 names media and social environments including civic organizations among the agents of socialization, and EK IEF-1.A.1 places news media and neighborhood organizations within civil society, autonomous from the state."),
 dict(q="What does the framework say about the agents of socialization across regime types?",
   choices=[
     "many of them are similar across regime types",
     "they are entirely different in authoritarian and democratic regimes",
     "they exist only in democratic regimes",
     "they exist only in authoritarian regimes",
     "the framework does not compare them across regime types"], ans=0,
   why="EK IEF-1.C.5 states that many agents of socialization, such as family, school, peers, media and government, are similar across regime types. The difference the statement then draws is about governmental pressure, not about which agents exist."),
 dict(q="What difference between regime types does the framework draw about socialization?",
   choices=[
     "authoritarian regimes apply more concerted governmental pressures to socialize their citizens around conforming beliefs than democratic regimes do",
     "democratic regimes apply more concerted governmental pressures than authoritarian regimes do",
     "neither regime type applies any governmental pressure",
     "both regime types apply exactly the same governmental pressure",
     "the difference lies in which agents exist rather than in how they are used"], ans=0,
   why="EK IEF-1.C.5 states that authoritarian regimes apply more concerted governmental pressures to socialize their citizens around conforming beliefs than do democratic regimes, while the agents themselves are largely similar. The difference is one of degree in the pressure applied."),
 dict(q="A student concludes that political socialization is something only authoritarian regimes carry out. The best correction is that",
   choices=[
     "socialization occurs in every regime through largely similar agents, and what differs is how concerted the governmental pressure is",
     "socialization occurs only where the state controls the school curriculum",
     "socialization occurs only in democratic regimes, where citizens are free to form views",
     "socialization is not discussed by the framework at all",
     "socialization ends once a citizen reaches voting age in every regime"], ans=0,
   why="EK IEF-1.C.5 states that many agents of socialization are similar across regime types before drawing its difference about the concertedness of governmental pressure, and EK IEF-1.C.3 makes socialization the process by which any political culture is transmitted. This follows the same pattern as EK DEM-1.C.2 and EK DEM-1.B.3."),
 dict(q="Which comparison of political culture and political ideology is consistent with the framework?",
   choices=[
     "Political culture is the collective attitudes, values and beliefs of a citizenry, whereas a political ideology is a set of values and beliefs about the goals of government, public policy or politics",
     "Political culture is a set of beliefs about the goals of government, whereas an ideology is the collective attitudes of a whole citizenry",
     "The two terms mean the same thing",
     "Political culture applies only to democracies and ideology only to authoritarian regimes",
     "Political ideology is transmitted through socialization and political culture is not"], ans=0,
   why="EK IEF-1.C.1 defines political culture as the collective attitudes, values and beliefs of the citizenry and the norms of behavior in the political system, while EK IEF-1.C.6 defines a political ideology as a set of values and beliefs about the goals of government, public policy or politics. One describes a population, the other a programme."),
 dict(q="Why is a single opinion poll about one policy a poor measure of a country's political culture?",
   choices=[
     "because political culture is the collective attitudes, values and beliefs of a citizenry and the norms of behavior in the political system, which is broader than a view on one question",
     "because opinion polls are never accurate",
     "because political culture concerns only institutions and not beliefs",
     "because political culture cannot be measured in any way",
     "because political culture changes daily"], ans=0,
   why="EK IEF-1.C.1 defines political culture as collective attitudes, values and beliefs together with the norms of behavior in the political system, and EK IEF-1.C.2 has it forming views about the role of government, individual rights and citizens' part in policy making. A single issue reaches none of that breadth."),
 dict(q="A country whose settlements are dispersed across remote and difficult terrain develops strong expectations of local self-management. Which of the framework's named influences on political culture does this illustrate?",
   choices=[
     "geography",
     "religious traditions",
     "history",
     "the electoral system",
     "the structure of the legislature"], ans=0,
   why="EK IEF-1.C.2 names geography among the factors influencing political culture, alongside religious traditions and history. Institutional design appears elsewhere in the framework and is not among these three influences."),
 dict(q="A country in which a shared religious tradition has long framed public argument about obligations to others develops distinctive expectations of what the state should provide. Which influence does this illustrate?",
   choices=[
     "religious traditions",
     "geography",
     "the number of political parties",
     "the length of judicial terms",
     "the level of foreign investment"], ans=0,
   why="EK IEF-1.C.2 names religious traditions among the factors influencing political culture, and EK IEF-1.C.4 separately names religious institutions among the agents of socialization through which political culture is transmitted."),
 dict(q="The table reports hypothetical survey figures for three countries. Which country's political culture places the greatest weight on social order relative to individual liberty?",
   table=_T_ORDER,
   choices=[
     "Country A, where 71 percent give order priority and only 28 percent expect a say in policy between elections",
     "Country B, where 34 percent give order priority",
     "Country C, where 52 percent give order priority",
     "None of the three, since the balance between order and liberty cannot be surveyed",
     "All three equally, since a majority in each names one of the two"], ans=0,
   why="EK IEF-1.C.1 states that political culture sets expectations about the exercise of power to establish a balance between social order and individual liberty, so the row with the highest priority for order and the lowest expectation of influence between elections sits furthest toward the order end."),
 dict(q="Using the same table, which country's figures place it furthest toward the liberty and participation end of that balance?",
   table=_T_ORDER,
   choices=[
     "Country B, which has the lowest share giving order priority and the highest share expecting a say between elections",
     "Country A, which has the highest share giving order priority",
     "Country C, whose two figures are closest to each other",
     "None of the three, since expectations of influence are unrelated to political culture",
     "Both Country B and Country C, since neither gives order a share above 60 percent"], ans=0,
   why="EK IEF-1.C.1 makes the balance between social order and individual liberty the thing political culture sets expectations about, and EK IEF-1.C.2 includes the extent and role of citizens in controlling government policy making among the beliefs it forms. One row is lowest on order and highest on expected influence at once."),
 dict(q="According to the same table, the gap between the highest and the lowest share giving order priority over individual liberty is",
   table=_T_ORDER,
   choices=[
     "37 percentage points",
     "19 percentage points",
     "18 percentage points",
     "41 percentage points",
     "71 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the gap. The alternatives are the gaps between other pairs in the same column, the corresponding gap in a different column, and the largest single value read as a difference."),
 dict(q="The table reports which agent of socialization respondents in two hypothetical countries name as their main influence. On which agent do the two countries differ most?",
   table=_T_AGENT,
   choices=[
     "schools, by 16 percentage points",
     "family, by 7 percentage points",
     "religious institutions, by 8 percentage points",
     "peers, by 4 percentage points",
     "media, by 3 percentage points"], ans=0,
   why="EK IEF-1.C.4 names all five of the table's rows among the agents of socialization, so the item is a comparison within the framework's own list. Taking the absolute difference in each row and comparing them identifies the largest, and each alternative states the correct difference for a different row."),
 dict(q="Which conclusion does the same table best support?",
   table=_T_AGENT,
   choices=[
     "Both countries name the same set of agents, all of which the framework lists, but in different proportions",
     "The two countries name entirely different agents from one another",
     "Only one of the two countries names any agent the framework lists",
     "Every respondent in both countries named the same agent",
     "Neither country's respondents named family among their influences"], ans=0,
   why="EK IEF-1.C.5 states that many agents of socialization are similar across regime types, and every row of the table is one of the agents EK IEF-1.C.4 names, with both columns non-zero throughout. The proportions differ, which is what the item's key reports."),
 dict(q="A student concludes from the same table that the second country's government must be applying concerted pressure through its schools. What is the strongest objection?",
   table=_T_AGENT,
   choices=[
     "a larger share naming schools is consistent with that explanation but does not establish it, since the table measures which agent respondents name rather than how much governmental pressure is applied",
     "the table reports nothing about schools",
     "the framework says schools are never an agent of socialization",
     "the framework says only authoritarian regimes have schools",
     "no difference between the two columns is large enough to notice"], ans=0,
   why="EK IEF-1.C.5's claim is about the CONCERTEDNESS OF GOVERNMENTAL PRESSURE, which a survey of named influences does not measure, and EK MPA-1.A.3 denies that causation can be isolated and demonstrated with certainty from such evidence. A larger role for schools could arise from many sources."),
 dict(q="A country's political expectations were formed partly by a long period of foreign rule followed by a struggle for independence. Which of the framework's named influences on political culture does this illustrate?",
   choices=[
     "history",
     "geography",
     "religious traditions",
     "the current electoral system",
     "the current level of economic growth"], ans=0,
   why="EK IEF-1.C.2 names history among the factors influencing political culture, alongside geography and religious traditions, and says these form beliefs about the role of government, individual rights and citizens' part in policy making."),
 dict(q="Which finding would most strongly indicate that a country's political culture has changed rather than merely that one government has become unpopular?",
   choices=[
     "Across a generation, expectations about the proper balance between order and liberty and about citizens' part in policy making have shifted in the same direction",
     "The governing party's support has fallen by ten points since the last election",
     "A single ministry has been reorganized",
     "A new head of government has taken office",
     "Turnout at the most recent election was lower than at the previous one"], ans=0,
   why="EK IEF-1.C.1 makes political culture the collective attitudes, values and beliefs of a citizenry and EK IEF-1.C.2 makes beliefs about the role of government and citizens' part in policy making its content, while EK IEF-1.C.3 makes its transmission a lifelong process. A shift across a generation in those beliefs is a change of culture; a swing against one government is not."),
 dict(q="Two countries hold competitive elections, but in one citizens expect to influence policy continuously and in the other they expect to do so only at elections. What does the framework's account attribute this difference to?",
   choices=[
     "differences in political culture, which forms beliefs about the extent and role of citizens in controlling government policy making",
     "differences in the number of chambers in their legislatures",
     "differences in the length of their judicial terms",
     "differences in their international recognition",
     "differences in whether they hold elections at all"], ans=0,
   why="EK IEF-1.C.2 states that political culture forms a population's values and beliefs about the role of government, the rights of the individual, and the extent and role of citizens in controlling government policy making. Both countries hold competitive elections, so the institutional fact does not separate them."),
 dict(q="How does the framework's account of political culture connect to its account of legitimacy?",
   choices=[
     "it names tradition and ideology among the sources of legitimacy, and political culture is where a population's traditions and beliefs about government reside",
     "it states that legitimacy is conferred by other states rather than by a population's beliefs",
     "it states that political culture and legitimacy are the same thing",
     "it states that legitimacy depends only on economic growth",
     "it states that political culture has no bearing on a government's right to rule"], ans=0,
   why="EK LEG-1.A.2 names nationalism, tradition, governmental effectiveness, economic growth, ideology, religious heritage and organizations, and a dominant party's endorsement among the sources of legitimacy, and EK LEG-1.A.1 makes legitimacy a belief of a government's constituents. EK IEF-1.C.1's collective attitudes, values and beliefs are where such beliefs live."),
 dict(q="Taking the framework's statements on political culture together, which summary is most accurate?",
   choices=[
     "Political culture is a citizenry's collective attitudes, values and beliefs and the norms of its political system; geography, religious traditions and history shape it; it is transmitted through lifelong socialization by family, schools, peers, religious institutions, media and social environments; and those agents are similar across regime types while governmental pressure on them is not",
     "Political culture is the set of institutions through which a state governs, and it does not vary between countries",
     "Political culture is acquired entirely in childhood and cannot change afterwards",
     "Political culture exists only in democratic regimes, where citizens may form their own views",
     "Political culture is transmitted only by the state, through schools and official media"], ans=0,
   why="EK IEF-1.C.1 supplies the definition, EK IEF-1.C.2 the influences and what they form, EK IEF-1.C.3 the lifelong transmission through socialization, EK IEF-1.C.4 the agents, and EK IEF-1.C.5 the similarity of agents across regime types alongside the difference in governmental pressure."),
]
