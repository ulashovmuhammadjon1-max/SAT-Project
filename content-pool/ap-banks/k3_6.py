# AP COMPARATIVE GOVERNMENT AND POLITICS 3.6 Forces that Impact Political
# Participation
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding DEM-1; learning objective DEM-1.B (explain how political
# participation affects and is affected by democratic or authoritarian regime
# types). Suggested skill 5.B, Argumentation.
#
# Essential knowledge relied on:
#   DEM-1.B.1  authoritarian and democratic regimes SUPPORT SIMILAR FORMS of
#              participation to influence policy making, including casting votes in
#              public elections, but DIFFER IN HOW MUCH IMPACT CITIZENS HAVE based on
#              HOW OPEN AND COMPETITIVE ELECTIONS ARE. In many elections in
#              authoritarian regimes there are FEW IF ANY OPPOSITION CANDIDATES --
#              those ADVOCATING DIFFERING VIEWS FROM THAT OF THE CONTROLLING
#              PARTY/ELITE -- allowed to run, and THE GOVERNMENT OFTEN INTERVENES to
#              ensure its preferred candidates and parties win
#   DEM-1.B.2  INFORMAL participation, such as PROTESTS and POLITICAL CRITICISM
#              EXPRESSED THROUGH SOCIAL MEDIA, is treated differently across regime
#              types; in authoritarian systems there is LESS TOLERANCE OF CRITICAL
#              VIEWPOINTS that may challenge authoritarian regimes
#   DEM-1.B.3  BOTH authoritarian and democratic regimes REGULATE formal political
#              participation by placing RESTRICTIONS ON VOTING ACCESS and
#              DISALLOWING DISRUPTIVE AND VIOLENT PROTESTS, but authoritarian regimes
#              manage and limit citizen participation TO A MUCH GREATER EXTENT
#   DEM-1.B.4  authoritarian regimes TOLERATE MASS POLITICAL PROTESTS AND MOVEMENTS
#              LESS than democratic regimes do, VALUING PUBLIC ORDER MORE THAN
#              INDIVIDUAL LIBERTIES AND CIVIL RIGHTS
#
# DEM-1.B.3 IS THE FRAMEWORK'S OWN TRAP. The CED's sample multiple-choice set is
# built on it: three of that question's four distractors are 'only authoritarian
# regimes...' statements, and the key is the one recognizing that BOTH types
# regulate formal participation and differ in degree (AP_COMP_GOV_CED.md note 13).
# Items 7, 10 and 23 key that reading, and no item here treats the existence of a
# restriction as evidence of regime type on its own.
#
# Suggested skill 5.B is Argumentation, so items 17, 18, 22, 28 and 29 ask which
# evidence would support or weaken a claim rather than what the framework says.
#
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.6", "Forces that Impact Political Participation", 3)

_T_OPP = dict(
    headers=["Country (hypothetical)", "Candidates on the ballot per seat",
             "Share of candidates advocating views differing from the governing party (percent)",
             "Share of contests won by the governing party (percent)"],
    rows=[["Country S", "1.2", "6", "97"],
          ["Country T", "3.8", "71", "44"],
          ["Country U", "2.4", "48", "58"]])

_T_REG = dict(
    headers=["Regulation of participation (hypothetical sample of cases)",
             "Number of democratic cases applying it", "Number of authoritarian cases applying it"],
    rows=[["Restrictions on voting access", "14", "19"],
          ["Disallowing disruptive and violent protests", "20", "20"],
          ["Banning peaceful mass demonstrations", "1", "17"],
          ["Prosecuting online criticism of officials", "2", "18"]])

_T_PROT = dict(
    headers=["Country (hypothetical)", "Mass demonstrations permitted to proceed, 2015-2020",
             "Mass demonstrations dispersed by force, 2015-2020",
             "Share of demonstrators prosecuted (percent)"],
    rows=[["Country V", "308", "12", "1"],
          ["Country W", "24", "96", "37"]])

QUESTIONS = [
 dict(q="What does the framework say about the forms of participation supported in authoritarian and democratic regimes?",
   choices=[
     "both support similar forms of participation, including casting votes in public elections",
     "authoritarian regimes support no form of participation",
     "democratic regimes support no form of participation other than voting",
     "the two support entirely different forms of participation",
     "the framework does not compare the forms supported in the two regime types"], ans=0,
   why="EK DEM-1.B.1 states that authoritarian and democratic regimes support similar forms of participation to influence policy making, including casting votes in public elections. The difference it then draws is about the impact citizens have, not about which forms exist."),
 dict(q="On what does the framework say the difference in citizens' impact depends?",
   choices=[
     "how open and competitive elections are",
     "how many citizens are eligible to vote",
     "whether the state is federal or unitary",
     "how many chambers the legislature has",
     "the length of the head of government's term"], ans=0,
   why="EK DEM-1.B.1 states that the two regime types differ in how much impact citizens have on policies and policy making based on how open and competitive elections are. Eligibility, territorial structure and institutional design are treated under other statements."),
 dict(q="How does the framework define an opposition candidate?",
   choices=[
     "one advocating differing views from that of the controlling party or elite",
     "one who has previously held office",
     "one nominated by a registered party rather than standing independently",
     "one who is not a member of the legislature",
     "one who has been vetted by an electoral commission"], ans=0,
   why="EK DEM-1.B.1 defines opposition candidates parenthetically as those advocating differing views from that of the controlling party/elite. The definition turns on the views advanced rather than on the candidate's history or affiliation."),
 dict(q="What does the framework say governments in many authoritarian elections often do?",
   choices=[
     "intervene in those elections to ensure that their preferred candidates and parties win",
     "withdraw entirely from the conduct of elections",
     "transfer the conduct of elections to a supranational body",
     "guarantee opposition candidates a fixed share of the seats",
     "cancel the elections rather than hold them"], ans=0,
   why="EK DEM-1.B.1 states that the government often intervenes in these elections to ensure that its preferred candidates and parties win, in the same statement that notes there are few if any opposition candidates allowed to run. The elections still take place, which is the point."),
 dict(q="Which examples does the framework give of informal political participation?",
   choices=[
     "protests and political criticism expressed through social media",
     "casting ballots in national elections and registering to vote",
     "standing for office and joining a political party",
     "serving on a jury and paying taxes",
     "signing a treaty and ratifying a constitution"], ans=0,
   why="EK DEM-1.B.2 gives protests and political criticism expressed through social media as its examples of informal participation. Casting ballots belongs to the FORMAL participation of EK DEM-1.A.4 and EK DEM-1.B.3."),
 dict(q="What does the framework say about how authoritarian systems treat critical viewpoints?",
   choices=[
     "there is less tolerance of critical viewpoints that may challenge authoritarian regimes",
     "critical viewpoints are treated identically to supportive ones",
     "there is greater tolerance of critical viewpoints than in democratic regimes",
     "critical viewpoints are encouraged in order to gather input",
     "the framework does not compare the treatment of critical viewpoints"], ans=0,
   why="EK DEM-1.B.2 states that informal participation is treated differently across regime types and that in authoritarian systems there is less tolerance of critical viewpoints that may challenge authoritarian regimes. EK DEM-1.C.3 gives the framework's instances of media restriction."),
 dict(q="Which statement about the regulation of formal political participation is consistent with the framework?",
   choices=[
     "both authoritarian and democratic regimes regulate it, though authoritarian regimes manage and limit participation to a much greater extent",
     "only authoritarian regimes regulate it",
     "only democratic regimes regulate it",
     "neither regime type regulates it",
     "both regulate it to exactly the same extent"], ans=0,
   why="EK DEM-1.B.3 states that both authoritarian and democratic regimes regulate formal political participation and that authoritarian regimes manage and limit citizen participation to a much greater extent. The framework's difference is one of degree, and the CED's own sample question is built on that reading."),
 dict(q="Which two forms of regulation does the framework name as common to both regime types?",
   choices=[
     "placing restrictions on voting access and disallowing disruptive and violent protests",
     "banning all public assembly and prosecuting all criticism",
     "vetting candidates and dissolving opposition parties",
     "nationalizing the media and closing the courts",
     "abolishing elections and appointing legislators"], ans=0,
   why="EK DEM-1.B.3 names restrictions on voting access and the disallowing of disruptive and violent protests as regulations both regime types apply. The rejected options describe measures the framework attributes to particular regimes rather than to both."),
 dict(q="What phrase does the framework use to describe how far authoritarian regimes go in managing participation?",
   choices=[
     "to a much greater extent",
     "to the same extent",
     "to a slightly greater extent",
     "to a lesser extent",
     "the framework gives no comparison"], ans=0,
   why="EK DEM-1.B.3 states that authoritarian regimes manage and limit citizen participation to a much greater extent, which fixes both the direction and the size of the difference while keeping the practice common to both types."),
 dict(q="A student writes that restrictions on voting access show a regime must be authoritarian. What does the framework say?",
   choices=[
     "both regime types place restrictions on voting access, so the existence of a restriction does not by itself identify the regime type",
     "only authoritarian regimes place restrictions on voting access",
     "only democratic regimes place restrictions on voting access",
     "no regime places restrictions on voting access",
     "restrictions on voting access are not discussed by the framework"], ans=0,
   why="EK DEM-1.B.3 states that both authoritarian and democratic regimes regulate formal political participation by placing restrictions on voting access, differing in degree rather than in kind. The CED's own sample multiple-choice question is built on rejecting the exclusive reading."),
 dict(q="What does the framework say about mass political protests and movements across regime types?",
   choices=[
     "authoritarian regimes tolerate them less than democratic regimes do",
     "authoritarian regimes tolerate them more than democratic regimes do",
     "both regime types tolerate them equally",
     "neither regime type tolerates them at all",
     "the framework does not compare their treatment"], ans=0,
   why="EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less than democratic regimes do. EK DEM-1.B.3 has already established that both types disallow disruptive and violent protests, so this is a further difference of degree."),
 dict(q="What reason does the framework give for that difference in tolerance?",
   choices=[
     "authoritarian regimes value public order more than individual liberties and civil rights",
     "authoritarian regimes lack the police capacity to manage large gatherings",
     "authoritarian regimes are required to do so by supranational organizations",
     "authoritarian regimes have no legal provision for assembly",
     "the framework gives no reason"], ans=0,
   why="EK DEM-1.B.4 states that authoritarian regimes tolerate mass protests less, valuing public order more than individual liberties and civil rights. The reason offered is a matter of what the regime values, which EK IEF-1.C.1 makes the axis political culture sets expectations along."),
 dict(q="Which comparison of the framework's statements on informal criticism and on mass protest is accurate?",
   choices=[
     "One concerns tolerance of critical viewpoints including those expressed through social media, and the other concerns tolerance of mass protests and movements, and both find authoritarian regimes less tolerant",
     "One finds authoritarian regimes more tolerant and the other finds them less tolerant",
     "Both concern only the regulation of voting access",
     "Both concern only violent protest",
     "Neither draws any comparison between regime types"], ans=0,
   why="EK DEM-1.B.2 concerns informal participation including political criticism through social media and EK DEM-1.B.4 concerns mass political protests and movements, and both state that authoritarian regimes are less tolerant. They are separate statements pointing the same way."),
 dict(q="In one country an election is held on schedule, but the only candidates permitted to stand endorse the governing party's programme, and it wins almost every contest. Which framework description does this best match?",
   choices=[
     "an election with few if any opposition candidates, in which the government has intervened to ensure its preferred candidates win",
     "an open and competitive election in which citizens control policy making",
     "a referendum on a policy question",
     "an instance of informal political participation",
     "an example of a regime declining to regulate participation"], ans=0,
   why="EK DEM-1.B.1 describes many elections in authoritarian regimes as having few if any opposition candidates, defined as those advocating differing views from the controlling party or elite, with the government often intervening to ensure its preferred candidates and parties win. Both features appear in the scenario."),
 dict(q="In a second country, people are prosecuted for posts criticizing ministers, while supportive posts circulate freely. Which framework statement does this most directly illustrate?",
   choices=[
     "that in authoritarian systems there is less tolerance of critical viewpoints, including political criticism expressed through social media",
     "that both regime types disallow disruptive and violent protests",
     "that both regime types place restrictions on voting access",
     "that elections are held to allow citizen control of the policy-making process",
     "that referenda allow citizens to vote directly on policy questions"], ans=0,
   why="EK DEM-1.B.2 names political criticism expressed through social media among the forms of informal participation and states that authoritarian systems show less tolerance of critical viewpoints that may challenge them. The asymmetry between critical and supportive posts is that intolerance made visible."),
 dict(q="In a third country, a democracy, a march that blocks a motorway is dispersed and its organizers are fined. Which framework statement does this most directly illustrate?",
   choices=[
     "that both regime types regulate formal participation by disallowing disruptive and violent protests",
     "that authoritarian regimes tolerate mass protests less than democratic regimes",
     "that authoritarian systems show less tolerance of critical viewpoints",
     "that governments often intervene in elections to ensure preferred candidates win",
     "that the regime must in fact be authoritarian"], ans=0,
   why="EK DEM-1.B.3 states that both authoritarian and democratic regimes regulate formal political participation by placing restrictions on voting access and disallowing disruptive and violent protests. A disruptive march dispersed in a democracy is that statement's democratic half."),
 dict(q="Which evidence would most strongly support a claim that a country's elections give citizens little impact on policy?",
   choices=[
     "Almost no candidates advocating views differing from the governing party appear on the ballot, and the governing party wins nearly every contest",
     "Turnout at the most recent election was very high",
     "The election was held on the date fixed by law",
     "The legislature met soon after the election",
     "Results were published within a week of the vote"], ans=0,
   why="EK DEM-1.B.1 makes citizens' impact depend on how open and competitive elections are and describes many authoritarian elections as having few if any opposition candidates with the government intervening to secure its preferred results. Turnout, timing, sitting dates and prompt publication bear on none of that."),
 dict(q="Which evidence would most strongly WEAKEN a claim that a regime tolerates mass political protest?",
   choices=[
     "Most large demonstrations in recent years were dispersed by force and a substantial share of participants were prosecuted",
     "Some demonstrations were smaller than their organizers had hoped",
     "Demonstrations were reported in the national press",
     "Demonstrations required advance notice to the police",
     "Demonstrations were held on weekends rather than working days"], ans=0,
   why="EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less than democratic regimes, valuing public order more than individual liberties and civil rights. Dispersal and prosecution measure tolerance; a notice requirement is the ordinary regulation EK DEM-1.B.3 attributes to both regime types."),
 dict(q="Why does the framework's account imply that the mere holding of elections says little about a regime type?",
   choices=[
     "because both regime types support similar forms of participation, and the difference lies in how open and competitive those elections are",
     "because elections are held only in democratic regimes",
     "because elections are held only in authoritarian regimes",
     "because the framework treats elections as irrelevant to regime type",
     "because elections in every country are equally competitive"], ans=0,
   why="EK DEM-1.B.1 states that authoritarian and democratic regimes support similar forms of participation, including voting, and differ in how much impact citizens have based on how open and competitive elections are. EK LEG-1.A.2 adds that popular elections can be a source of legitimacy for both."),
 dict(q="The table reports hypothetical election figures for three countries. Which record best matches the framework's description of many elections in authoritarian regimes?",
   table=_T_OPP,
   choices=[
     "Country S, with barely more than one candidate per seat, almost no candidates advocating differing views, and the governing party winning nearly every contest",
     "Country T, with the most candidates per seat",
     "Country U, which is between the other two on every measure",
     "None of the three, since the framework describes no such elections",
     "All three equally, since each held an election"], ans=0,
   why="EK DEM-1.B.1 describes many elections in authoritarian regimes as having few if any opposition candidates, those advocating differing views from the controlling party or elite, with the government often intervening to ensure its preferred candidates win. One row shows all three features together."),
 dict(q="Using the same table, which record best matches the framework's description of open and competitive elections?",
   table=_T_OPP,
   choices=[
     "Country T, with the most candidates per seat, the largest share advocating differing views, and the governing party winning fewer than half the contests",
     "Country S, where the governing party wins nearly every contest",
     "Country U, where the governing party wins a majority of contests",
     "None of the three, since competitiveness cannot be measured",
     "Both Country T and Country U, since neither governing party wins every contest"], ans=0,
   why="EK DEM-1.B.1 makes citizens' impact depend on how open and competitive elections are, so the record to look for combines a crowded ballot, many candidates advocating differing views, and a governing party that can lose. One row shows all three."),
 dict(q="According to the same table, the difference between the largest and smallest shares of contests won by the governing party is",
   table=_T_OPP,
   choices=[
     "53 percentage points",
     "39 percentage points",
     "14 percentage points",
     "65 percentage points",
     "97 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the difference. The alternatives are the gaps between other pairs in the same column, the corresponding gap in the differing-views column, and the largest single value read as a difference."),
 dict(q="The table reports how often four regulations appear among hypothetical democratic and authoritarian cases. Which conclusion does it support?",
   table=_T_REG,
   choices=[
     "The two regulations the framework names as common to both regime types appear in substantial numbers of both, while the other two appear almost only among authoritarian cases",
     "Every regulation in the table appears only among authoritarian cases",
     "Every regulation in the table appears equally often in both groups",
     "No regulation in the table appears among democratic cases",
     "Restrictions on voting access appear only among democratic cases"], ans=0,
   why="EK DEM-1.B.3 names restrictions on voting access and the disallowing of disruptive and violent protests as regulations BOTH regime types apply, and those two rows carry double-figure counts in both columns. The other two rows describe measures EK DEM-1.B.2 and EK DEM-1.B.4 associate with authoritarian intolerance."),
 dict(q="Using the same table, which two rows diverge most sharply between the two groups, and which framework claims does that divergence match?",
   table=_T_REG,
   choices=[
     "banning peaceful mass demonstrations and prosecuting online criticism, matching the claims that authoritarian regimes tolerate mass protest less and show less tolerance of critical viewpoints",
     "restrictions on voting access and disallowing disruptive protests, matching the claim that both regime types regulate participation",
     "restrictions on voting access and prosecuting online criticism, matching the claim that elections are open and competitive",
     "disallowing disruptive protests and banning peaceful demonstrations, matching the claim that governments intervene in elections",
     "no two rows diverge between the groups"], ans=0,
   why="EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less, and EK DEM-1.B.2 that they show less tolerance of critical viewpoints including criticism through social media. Those are the two rows whose counts differ most between the columns."),
 dict(q="According to the same table, the total number of authoritarian cases applying any of the four regulations is",
   table=_T_REG,
   choices=[
     "74",
     "37",
     "57",
     "39",
     "20"], ans=0,
   why="Adding the authoritarian column across all four rows gives the total. The alternatives arise from adding the democratic column instead, from dropping a row, from adding only two rows, and from reading a single row."),
 dict(q="The table reports hypothetical protest records for two countries. Which record best matches the framework's account of how authoritarian regimes treat mass political protest?",
   table=_T_PROT,
   choices=[
     "Country W, where far more demonstrations were dispersed by force than were permitted to proceed and more than a third of demonstrators were prosecuted",
     "Country V, where a small number of demonstrations were dispersed by force",
     "Neither, since the framework says no regime permits mass demonstrations",
     "Both equally, since each dispersed some demonstrations",
     "Country V, because it recorded more demonstrations in total"], ans=0,
   why="EK DEM-1.B.4 states that authoritarian regimes tolerate mass political protests and movements less than democratic regimes do, valuing public order more than individual liberties and civil rights. A record in which dispersal outnumbers permission and prosecution is common is that intolerance in data."),
 dict(q="According to the same table, the share of that country's mass demonstrations that were dispersed by force was closest to",
   table=_T_PROT,
   choices=[
     "80 percent",
     "20 percent",
     "37 percent",
     "4 percent",
     "96 percent"], ans=0,
   why="Dividing the demonstrations dispersed by force by the total of those permitted and those dispersed gives the share. The alternatives offer the complementary share, the prosecution figure, the other country's dispersal share, and the raw count read as a percentage."),
 dict(q="Which finding would most strongly support a claim that a regime's tolerance of informal participation has narrowed?",
   choices=[
     "Prosecutions for online criticism of officials have risen sharply while prosecutions for other offences have not",
     "The number of social media users in the country has risen",
     "The government has opened an official account on a social media platform",
     "A minister has replied publicly to a critical post",
     "The national press has increased its coverage of parliament"], ans=0,
   why="EK DEM-1.B.2 names political criticism expressed through social media among the forms of informal participation and states that authoritarian systems show less tolerance of critical viewpoints. A rise in prosecutions specific to criticism, against a flat background, is evidence about tolerance rather than about usage."),
 dict(q="Which finding would most strongly WEAKEN a claim that a country's elections are open and competitive?",
   choices=[
     "Candidates advocating views differing from the governing party were removed from the ballot before voting began",
     "Turnout fell slightly compared with the previous election",
     "The governing party's vote share was higher than the polls had predicted",
     "Several small parties chose not to contest the election",
     "The count took longer than expected"], ans=0,
   why="EK DEM-1.B.1 defines opposition candidates as those advocating differing views from the controlling party or elite and makes their presence part of what open and competitive means. Turnout, polling error, voluntary abstention and a slow count are all compatible with a free contest."),
 dict(q="Taking the framework's statements in this topic together, which summary is most accurate?",
   choices=[
     "Both regime types support similar forms of participation and both regulate them, but authoritarian regimes limit participation to a much greater extent, tolerate critical viewpoints and mass protest less, and often intervene in elections to secure their preferred results",
     "Only democratic regimes support any form of political participation",
     "Only authoritarian regimes regulate political participation",
     "The two regime types treat every form of participation identically",
     "The framework compares the two regime types only on the number of parties permitted"], ans=0,
   why="EK DEM-1.B.1 supplies the similar forms and the difference in impact, EK DEM-1.B.2 the treatment of informal criticism, EK DEM-1.B.3 the regulation both types apply and the much greater extent in one, and EK DEM-1.B.4 the lower tolerance of mass protest and the reason for it."),
]
