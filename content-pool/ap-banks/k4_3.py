# AP COMPARATIVE GOVERNMENT AND POLITICS 4.3 Political Party Systems
# CED effective Fall 2026, Unit 4 Party and Electoral Systems and Citizen
# Organizations. Enduring understanding PAU-4 (the power, influence and strength
# of political parties and the degree of competition between parties reflect the
# values of the regime or type of government); learning objective PAU-4.A.
# Suggested skill 3.B, Data Analysis (describe patterns and trends in data).
#
# Essential knowledge relied on:
#   PAU-4.A.1  party systems and membership DIFFER among course countries, RANGING
#              FROM DOMINANT PARTY SYSTEMS TO MULTIPARTY SYSTEMS
#   PAU-4.A.2  CHINA has rules allowing ONLY ONE PARTY, the Communist Party of
#              China, to control governing power TO MAINTAIN THE VALUES OF
#              CENTRALISM AND ORDER, while ALLOWING EIGHT OTHER PARTIES TO EXIST to
#              BROADEN DISCUSSION AND CONSULTATION
#   PAU-4.A.3  rules ensuring ONE-PARTY DOMINANCE IN RUSSIA include INCREASING PARTY
#              REGISTRATION REQUIREMENTS, allowing ONLY LEGALLY REGISTERED PARTIES
#              TO RUN, USING SELECTIVE COURT DECISIONS TO DISQUALIFY CANDIDATES,
#              LIMITING THE OPPOSITION'S ABILITY TO PRESENT VIEWPOINTS IN THE MEDIA,
#              INCREASING THRESHOLD RULES to limit ballot access, and ELIMINATING
#              GUBERNATORIAL ELECTIONS
#   PAU-4.A.4  rules facilitating MEXICO's transition away from one-party dominance
#              include ELIMINATING EL DEDAZO, PRIVATIZING STATE-OWNED CORPORATIONS
#              TO DECREASE PATRONAGE, DECENTRALIZING AND REDUCING ONE-PARTY POWER AT
#              THE SUBNATIONAL LEVEL, and ESTABLISHING AND STRENGTHENING THE
#              NATIONAL ELECTORAL INSTITUTE
#   PAU-4.A.5  the DEGREE OF COMPETITION within multiparty systems can influence
#              REPRESENTATION and FORMAL POLITICAL PARTICIPATION by citizens:
#     .a NIGERIA's multiparty system includes 30 REGISTERED POLITICAL PARTIES, with
#        TWO STRONG PARTIES, the People's Democratic Party and the All Progressives
#        Congress, AND A THIRD PARTY HAVING A DEGREE OF ELECTORAL SUCCESS
#     .b the UNITED KINGDOM's party system features competition primarily between
#        TWO MAJOR PARTIES, Conservative and Labour, which CONTROL THE LEGISLATURE
#        AND EXECUTIVE, with FIRST-PAST-THE-POST rules FAVORING THE MAJOR PARTIES;
#        BUT MINOR PARTIES WITH REGIONAL REPRESENTATION ARE ALSO ABLE TO WIN SOME
#        LEGISLATIVE REPRESENTATION
#   PAU-4.A.6  CATCH-ALL political parties can earn support from GROUPS WITH
#              DIFFERENT CHARACTERISTICS, attracting popular support with
#              IDEOLOGICALLY DIVERSE PLATFORMS
#   PAU-4.A.7  some legislatures, SUCH AS THE UNITED KINGDOM'S HOUSE OF COMMONS, are
#              HIGHLY ORGANIZED BY POLITICAL PARTIES, with voting based on STRICT
#              PARTY DISCIPLINE that influences policy making
#
# THE HALF OF PAU-4.A.5.b STUDENTS DROP: after saying two major parties dominate
# and first-past-the-post favors them, the statement adds 'BUT minor parties with
# regional representation are also able to win some legislative representation'.
# Item 10 keys the whole sentence and item 17 keys the concession alone, because a
# two-party summary that omits it contradicts the framework.
#
# Table figures are HYPOTHETICAL and labelled so; the framework's own numbers here
# are Nigeria's 30 registered parties and China's eight permitted parties, and only
# those are asserted about a country.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("4.3", "Political Party Systems", 4)

_T_PARTY = dict(
    headers=["Country (hypothetical)", "Registered political parties",
             "Parties winning more than 5 percent of the seats",
             "Share of seats held by the largest party (percent)"],
    rows=[["Country A", "9", "1", "94"],
          ["Country B", "30", "3", "41"],
          ["Country C", "12", "2", "48"]])

_T_THRESH = dict(
    headers=["Election (hypothetical)", "Threshold for representation (percent of the vote)",
             "Parties clearing the threshold",
             "Share of votes cast for parties that won no seats (percent)"],
    rows=[["Election 1", "3", "7", "4"],
          ["Election 2", "5", "5", "11"],
          ["Election 3", "7", "3", "19"]])

_T_DISC = dict(
    headers=["Legislature (hypothetical)",
             "Share of divisions in which members voted with their own party (percent)",
             "Bills amended against the government's wishes in a session"],
    rows=[["Legislature P", "98", "2"],
          ["Legislature Q", "71", "44"]])

QUESTIONS = [
 dict(q="What range does the framework give for party systems across the course countries?",
   choices=[
     "from dominant party systems to multiparty systems",
     "from unitary systems to federal systems",
     "from parliamentary systems to presidential systems",
     "from rule by law to rule of law",
     "from limited social protections to a welfare state"], ans=0,
   why="EK PAU-4.A.1 states that party systems and membership differ among course countries, ranging from dominant party systems to multiparty systems. The rejected ranges belong to EK PAU-2.A.1, EK PAU-3.A, EK IEF-1.D.1 and EK IEF-1.D.2."),
 dict(q="What does the framework say about the eight parties permitted to exist alongside China's governing party?",
   choices=[
     "they exist to broaden discussion and consultation, while only the governing party controls governing power",
     "they may form a coalition government if they win a majority between them",
     "they are allocated seats in proportion to their share of the vote",
     "they nominate candidates for the presidency at each election",
     "they exist to contest control of the government at each election"], ans=0,
   why="EK PAU-4.A.2 states that China has rules allowing only the Communist Party of China to control governing power, to maintain the values of centralism and order, while allowing eight other parties to exist to broaden discussion and consultation. Control of government is reserved to one party throughout."),
 dict(q="Which values does the framework say China's one-party rules are meant to maintain?",
   choices=[
     "centralism and order",
     "pluralism and competition",
     "transparency and accountability",
     "federalism and local autonomy",
     "individualism and free trade"], ans=0,
   why="EK PAU-4.A.2 states that the rules reserving governing power to one party are there to maintain the values of centralism and order. The rejected values appear elsewhere in the framework and not in this statement."),
 dict(q="Which set of rules does the framework name as ensuring one-party dominance in Russia?",
   choices=[
     "increasing party registration requirements, allowing only legally registered parties to run, using selective court decisions to disqualify candidates, limiting the opposition's media access, increasing threshold rules, and eliminating gubernatorial elections",
     "eliminating a nomination practice, privatizing state-owned corporations, decentralizing party power, and strengthening an electoral institute",
     "permitting eight parties to exist to broaden discussion and consultation",
     "adopting ethnic quotas for representation in the federal legislature",
     "allowing parties to form coalitions to nominate joint candidates"], ans=0,
   why="EK PAU-4.A.3 lists exactly these six rules as ensuring one-party dominance in Russia. The first rejected option is EK PAU-4.A.4's list for Mexico, which points the opposite way, and the remaining three are the framework's descriptions of China, Nigeria and Mexico."),
 dict(q="Which of the framework's Russian rules works by narrowing who may appear on a ballot at all?",
   choices=[
     "allowing only legally registered parties to run for office, alongside increased registration requirements",
     "limiting the opposition's ability to present viewpoints in the media",
     "eliminating gubernatorial elections",
     "using selective court decisions to settle disputes between chambers",
     "permitting eight minor parties to exist"], ans=0,
   why="EK PAU-4.A.3 names increasing party registration requirements and allowing only legally registered parties to run for office, which together decide who may stand. Media limits shape the campaign rather than the ballot, and eliminating gubernatorial elections removes a contest rather than narrowing one."),
 dict(q="Which of the framework's Russian rules removes an entire category of elected office?",
   choices=[
     "eliminating gubernatorial elections",
     "increasing threshold rules to limit party access to the ballot",
     "using selective court decisions to disqualify candidates",
     "increasing party registration requirements",
     "limiting the opposition's ability to present viewpoints in the media"], ans=0,
   why="EK PAU-4.A.3 names eliminating gubernatorial elections among the rules ensuring one-party dominance, and EK DEM-2.B.5.c describes regional legislatures appointing a governor from a list approved by the president. The other rules restrict who may contest an election that still occurs."),
 dict(q="Which set of rules does the framework credit with facilitating a transition AWAY from one-party dominance?",
   choices=[
     "eliminating a nomination practice, privatizing state-owned corporations to decrease patronage, decentralizing and reducing one-party power at the subnational level, and establishing and strengthening a national electoral institute",
     "increasing party registration requirements and threshold rules",
     "using selective court decisions to disqualify candidates",
     "permitting minor parties to exist to broaden discussion",
     "eliminating gubernatorial elections"], ans=0,
   why="EK PAU-4.A.4 names exactly these rules as facilitating Mexico's transition away from one-party dominance. The rejected options come from EK PAU-4.A.3's list for Russia and EK PAU-4.A.2's description of China, which run the other way."),
 dict(q="What does the framework say the degree of competition within a multiparty system can influence?",
   choices=[
     "representation and formal political participation by citizens",
     "whether the state is federal or unitary",
     "the length of judicial terms",
     "the number of chambers in the legislature",
     "a state's international recognition"], ans=0,
   why="EK PAU-4.A.5 states that the degree of competition within multiparty systems can influence representation and formal political participation by citizens. Territorial structure, judicial tenure, chamber counts and recognition are treated under other statements."),
 dict(q="How does the framework describe Nigeria's party system?",
   choices=[
     "a multiparty system of 30 registered parties, with two strong parties and a third having a degree of electoral success",
     "a system in which only one party may control governing power",
     "a two-party system in which no third party wins any seats",
     "a system with no formal political party structures",
     "a system in which parties are allocated seats in proportion to their vote"], ans=0,
   why="EK PAU-4.A.5.a states that Nigeria's multiparty system includes 30 registered political parties, with two strong parties, the People's Democratic Party and the All Progressives Congress, and a third party having a degree of electoral success. All three elements are the framework's."),
 dict(q="How does the framework describe the United Kingdom's party system?",
   choices=[
     "competition primarily between two major parties that control the legislature and executive under first-past-the-post rules favoring them, but with minor parties holding regional representation still able to win some seats",
     "competition primarily between two major parties, with no other party winning any seats",
     "a multiparty system of 30 registered parties",
     "a system in which one party alone may control governing power",
     "a system without formal political party structures"], ans=0,
   why="EK PAU-4.A.5.b states that the United Kingdom's party system features competition primarily between the Conservative and Labour parties, which control the legislature and executive, with first-past-the-post rules favoring the major parties, BUT that minor parties with regional representation are also able to win some legislative representation. The concession is part of the statement."),
 dict(q="How does the framework define a catch-all political party?",
   choices=[
     "one that can earn support from groups with different characteristics, attracting popular support with ideologically diverse platforms",
     "one that represents a single ethnic or religious community",
     "one that exists only to contest local elections",
     "one that is permitted to exist but not to control governing power",
     "one that is formed as a temporary alliance to nominate a joint candidate"], ans=0,
   why="EK PAU-4.A.6 states that catch-all political parties can earn support from groups with different characteristics, attracting popular support with ideologically diverse platforms. The breadth of the platform and the breadth of the coalition are two halves of the same definition."),
 dict(q="What does the framework say about legislatures that are highly organized by political parties?",
   choices=[
     "voting in them is based on strict party discipline, which influences policy making",
     "their members vote without regard to party position",
     "they are found only in presidential systems",
     "their members are appointed rather than elected",
     "they have no committee structure"], ans=0,
   why="EK PAU-4.A.7 states that some legislatures, such as the United Kingdom's House of Commons, are highly organized by political parties, with voting based on strict party discipline that influences policy making."),
 dict(q="Which comparison of China's and Russia's party arrangements is consistent with the framework?",
   choices=[
     "In one, rules reserve governing power to a single party while permitting others to exist for discussion; in the other, a set of registration, threshold, court and media rules secures one party's dominance within contested elections",
     "In both, a single party is the only one permitted to exist",
     "In both, parties are allocated seats in proportion to their votes",
     "In one, parties are barred entirely; in the other, every party is guaranteed representation",
     "Neither country's party arrangements are described by the framework"], ans=0,
   why="EK PAU-4.A.2 describes rules reserving governing power to one party while allowing eight others to exist to broaden discussion and consultation, and EK PAU-4.A.3 lists six rules ensuring one-party dominance in Russia. EK DEM-1.C.5 adds that Russia holds contested elections with limited competitiveness, which is why the two arrangements are not the same."),
 dict(q="Which comparison of Mexico's and Russia's party rules is consistent with the framework?",
   choices=[
     "One set is credited with facilitating a transition away from one-party dominance, and the other with ensuring one-party dominance",
     "Both sets are credited with facilitating transitions away from one-party dominance",
     "Both sets are credited with ensuring one-party dominance",
     "Neither set concerns party dominance",
     "One set abolished political parties and the other created them"], ans=0,
   why="EK PAU-4.A.4 credits its list with facilitating Mexico's transition away from one-party dominance and EK PAU-4.A.3 credits its list with ensuring one-party dominance in Russia. The framework describes rule changes running in opposite directions."),
 dict(q="Which comparison of Nigeria's and the United Kingdom's party systems is consistent with the framework?",
   choices=[
     "Both have two leading parties, but the framework records 30 registered parties and a third with some electoral success in one, and minor parties with regional representation winning some seats in the other",
     "Both are dominant party systems in which one party controls governing power",
     "Neither has any party beyond its two leading ones winning representation",
     "One has no formal party structures and the other has 30 registered parties",
     "Both allocate seats to parties in proportion to their national vote"], ans=0,
   why="EK PAU-4.A.5.a gives Nigeria 30 registered parties with two strong ones and a third having a degree of electoral success, and EK PAU-4.A.5.b gives the United Kingdom two major parties alongside minor parties with regional representation winning some seats. Both systems have more than two parties represented."),
 dict(q="Which course country does the framework describe as lacking formal political party structures?",
   choices=[
     "Iran",
     "Nigeria",
     "Mexico",
     "Russia",
     "the United Kingdom"], ans=0,
   why="EK PAU-4.B.1.b states that Iran lacks formal political party structures and that parties operate as loosely formed political alliances with questionable linkage to constituents, and EK DEM-2.A.1.b repeats that the Majles lacks formal political party structures."),
 dict(q="A student summarizes the United Kingdom's party system as one in which only two parties ever win seats. Which part of the framework's statement does this omit?",
   choices=[
     "that minor parties with regional representation are also able to win some legislative representation",
     "that first-past-the-post rules favor the major parties",
     "that two major parties control the legislature and executive",
     "that the party system features competition primarily between two parties",
     "that the House of Commons is highly organized by political parties"], ans=0,
   why="EK PAU-4.A.5.b ends with the concession that minor parties with regional representation are also able to win some legislative representation, and EK PAU-4.B.1.h adds that single-member districts allow regional parties to win legislative seats. The other options are parts of the statement the summary keeps."),
 dict(q="Why, on the framework's account, do single-member district plurality rules in the United Kingdom both diminish minor-party representation and allow some regional parties to win seats?",
   choices=[
     "because a party whose support is spread thinly wins no districts, while a party whose support is concentrated in one region can win the districts there",
     "because minor parties are barred from contesting districts outside their region",
     "because regional parties are allocated a fixed number of seats by law",
     "because the electoral system allocates seats in proportion to the national vote",
     "because the two major parties do not contest seats in every region"], ans=0,
   why="EK PAU-4.B.1.g states that single-member district plurality elections diminish minor-party representation and EK PAU-4.B.1.h that single-member districts allow regional parties to win legislative seats, and EK DEM-2.B.2 explains the mechanism, since only the leading candidate in each district converts votes into a seat."),
 dict(q="Which framework claim best explains why a party might deliberately adopt an ideologically diverse platform?",
   choices=[
     "that catch-all parties can earn support from groups with different characteristics, attracting popular support with such platforms",
     "that party systems range from dominant party systems to multiparty systems",
     "that some legislatures are highly organized by political parties",
     "that one party may be permitted to control governing power",
     "that party registration requirements can be raised"], ans=0,
   why="EK PAU-4.A.6 states that catch-all political parties can earn support from groups with different characteristics, attracting popular support with ideologically diverse platforms. Breadth of platform is the means and breadth of support the end."),
 dict(q="The table reports hypothetical party figures for three countries. Which country's data best fits the dominant party end of the framework's range?",
   table=_T_PARTY,
   choices=[
     "Country A, where one party holds 94 percent of the seats and no other party wins more than 5 percent of them",
     "Country B, where three parties win more than 5 percent of the seats",
     "Country C, where the largest party holds fewer than half the seats",
     "None of the three, since a dominant party system cannot be seen in seat data",
     "All three equally, since each has a largest party"], ans=0,
   why="EK PAU-4.A.1 gives the range from dominant party systems to multiparty systems, so the dominant end is a single party holding almost all the seats with no significant rival. One row shows both features at once."),
 dict(q="Using the same table, which country's data best fits the framework's description of Nigeria's party system?",
   table=_T_PARTY,
   choices=[
     "Country B, with 30 registered parties and three winning more than 5 percent of the seats",
     "Country A, with nine registered parties and one winning seats",
     "Country C, with twelve registered parties and two winning seats",
     "None of the three, since the framework gives no party figures for that country",
     "All three, since each has more than one registered party"], ans=0,
   why="EK PAU-4.A.5.a states that Nigeria's multiparty system includes 30 registered political parties, with two strong parties and a third having a degree of electoral success, so the matching row needs both the party count and three parties winning meaningful representation."),
 dict(q="According to the same table, the total number of registered political parties across the three countries is",
   table=_T_PARTY,
   choices=[
     "51",
     "42",
     "39",
     "21",
     "30"], ans=0,
   why="Adding the registered-party column across the three rows gives the total. The alternatives arise from dropping a row, from adding only two rows, and from reading the largest single row as though it were the total."),
 dict(q="The table reports hypothetical results from three elections held under different thresholds. Which pattern does it show?",
   table=_T_THRESH,
   choices=[
     "As the threshold rises, fewer parties clear it and a larger share of votes goes to parties that win no seats",
     "As the threshold rises, more parties clear it and fewer votes are wasted",
     "The threshold has no relationship to the number of parties represented",
     "The share of wasted votes is the same at every threshold",
     "Every party cleared the threshold at each election"], ans=0,
   why="EK PAU-4.A.3 names increasing threshold rules among the devices limiting party access to the ballot and EK PAU-4.B.1.e records diminished representation of smaller parties in Russia because of changing threshold rules. Reading the three rows in order, both columns move as those statements predict."),
 dict(q="According to the same table, the difference between the largest and smallest shares of votes cast for parties that won no seats is",
   table=_T_THRESH,
   choices=[
     "15 percentage points",
     "8 percentage points",
     "7 percentage points",
     "4 percentage points",
     "19 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the difference. The alternatives are the gaps between other pairs in the same column, a figure from the threshold column, and the largest single value read as a difference."),
 dict(q="Which framework claim does the same table most directly illustrate?",
   table=_T_THRESH,
   choices=[
     "that changing threshold rules can diminish the representation of smaller parties",
     "that catch-all parties attract support with ideologically diverse platforms",
     "that some legislatures are highly organized by political parties",
     "that one party may be permitted to control governing power while others exist for consultation",
     "that party systems range from dominant party systems to multiparty systems"], ans=0,
   why="EK PAU-4.B.1.e states that diminished representation of smaller parties occurs because of changing threshold rules, and EK PAU-4.A.3 lists increasing threshold rules among the devices ensuring one-party dominance. The table's two columns move exactly as that account describes."),
 dict(q="The table reports hypothetical voting behavior in two legislatures. Which one matches the framework's description of a legislature highly organized by political parties?",
   table=_T_DISC,
   choices=[
     "Legislature P, where members voted with their own party in 98 percent of divisions and only two bills were amended against the government's wishes",
     "Legislature Q, where members voted with their own party in 71 percent of divisions",
     "Neither, since party discipline cannot be observed in voting records",
     "Both equally, since members in each voted with their party most of the time",
     "Legislature Q, because more bills were amended there"], ans=0,
   why="EK PAU-4.A.7 states that some legislatures, such as the United Kingdom's House of Commons, are highly organized by political parties, with voting based on strict party discipline that influences policy making. Near-unanimous party voting alongside almost no successful amendments against the government is that description in data."),
 dict(q="According to the same table, the difference between the two legislatures in the share of divisions in which members voted with their own party is",
   table=_T_DISC,
   choices=[
     "27 percentage points",
     "42 percentage points",
     "29 percentage points",
     "44 percentage points",
     "98 percentage points"], ans=0,
   why="Subtracting the smaller share from the larger gives the difference. The alternatives are the gap in the other column, a near miss produced by subtracting the smaller share from 100, a raw count from the amendments column, and the larger share read as a difference."),
 dict(q="Which finding would most strongly support a claim that a country's party system has moved away from one-party dominance?",
   choices=[
     "A nomination practice controlled by the outgoing leadership was abolished, state firms that supplied patronage were privatized, party power at the subnational level was reduced, and an independent electoral institute was established and strengthened",
     "The governing party increased its majority at the last election",
     "The number of registered parties was reduced",
     "The threshold for representation was raised",
     "Gubernatorial elections were replaced by appointments"], ans=0,
   why="EK PAU-4.A.4 names exactly these four measures as facilitating Mexico's transition away from one-party dominance. Each rejected option is either the opposite result or one of EK PAU-4.A.3's devices for ensuring dominance."),
 dict(q="Which finding would most strongly support a claim that a country's rules are being used to secure one party's dominance?",
   choices=[
     "Registration requirements and thresholds have been raised, courts have disqualified opposition candidates selectively, and the opposition's access to media has been curtailed",
     "The governing party has adopted an ideologically diverse platform",
     "Two major parties dominate the legislature under first-past-the-post rules",
     "Thirty parties are registered and three win meaningful representation",
     "Minor parties with regional support win some legislative seats"], ans=0,
   why="EK PAU-4.A.3 lists increasing party registration requirements, increasing threshold rules, selective court decisions disqualifying candidates and limiting the opposition's media access among the rules ensuring one-party dominance. The rejected findings describe EK PAU-4.A.6's catch-all party and EK PAU-4.A.5's competitive multiparty systems."),
 dict(q="Taking the framework's account of party systems together, which summary is most accurate?",
   choices=[
     "Party systems run from dominant party to multiparty, rules can be arranged to entrench or to loosen one party's hold, the degree of competition shapes representation and participation, and parties themselves differ in how broadly they appeal and how tightly they discipline their legislators",
     "Every course country has a two-party system with identical rules",
     "Party systems are identical across the six course countries",
     "Only the number of registered parties matters to how a party system works",
     "The framework describes party rules but says nothing about their effects"], ans=0,
   why="EK PAU-4.A.1 supplies the range, EK PAU-4.A.2 to EK PAU-4.A.4 the rules that entrench or loosen dominance, EK PAU-4.A.5 the effect of competition on representation and participation, EK PAU-4.A.6 the catch-all party and EK PAU-4.A.7 strict party discipline in some legislatures."),
]
