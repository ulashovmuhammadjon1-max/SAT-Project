# AP U.S. GOVERNMENT AND POLITICS 5.3 Political Parties -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# TWO learning objectives:
#   LO 5.3.A -- DESCRIBE LINKAGE INSTITUTIONS.
#   LO 5.3.B -- explain the FUNCTION AND IMPACT of political parties ON THE
#     ELECTORATE AND GOVERNMENT.
# Suggested skill for this topic (CED p. 116): 1.B, concept application --
# explain political principles, institutions, processes, policies, and behaviors.
#
# Essential knowledge relied on:
#   EK 5.3.A.1 -- "LINKAGE INSTITUTIONS are CHANNELS THAT ALLOW INDIVIDUALS TO
#     COMMUNICATE THEIR PREFERENCES TO POLICYMAKERS:
#       i. Political parties  ii. Interest groups  iii. Elections  iv. Media"
#   EK 5.3.B.1 -- "The functions and impact of political parties on the
#     electorate and government are represented by:
#       i.   Mobilization and education of voters
#       ii.  Party platforms
#       iii. Candidate recruitment
#       iv.  Campaign management, including fundraising and media strategy
#       v.   THE COMMITTEE AND PARTY LEADERSHIP SYSTEMS IN LEGISLATURES"
#
# THE DEFINITION OF A LINKAGE INSTITUTION HAS A DIRECTION, AND THE DIRECTION IS
# THE DEFINITION. EK 5.3.A.1's channels run FROM INDIVIDUALS TO POLICYMAKERS. A
# paraphrase that has institutions communicating to citizens -- informing them,
# reaching them, telling them what government is doing -- has reversed the
# framework's own arrow and described something else entirely. Media is where
# the reversal is most tempting, because the obvious thing media does is carry
# information outward; EK 5.3.A.1 lists it as a linkage institution for the
# opposite reason. Items 2, 3 and 8 turn on the direction and the verifier
# refuses any key that reverses it.
#
# FOUR LINKAGE INSTITUTIONS, AND THE LIST IS CLOSED AS THE FRAMEWORK GIVES IT.
# Parties, interest groups, elections, media. Note that three of the four are
# themselves topics later in this unit, which is why 5.3 sits where it does.
#
# EK 5.3.B.1'S FIFTH FUNCTION IS THE ONE THAT DISAPPEARS, and losing it costs
# half the objective. LO 5.3.B says parties act ON THE ELECTORATE AND GOVERNMENT;
# functions i to iv are directed at voters and candidates, and function v -- THE
# COMMITTEE AND PARTY LEADERSHIP SYSTEMS IN LEGISLATURES -- is the whole of the
# government half. A module that stopped at four would answer only half of what
# the objective asks. The second table is built to show exactly that split, four
# rows against one, and item 30 makes the single row the point.
#
# The CED attaches no foundational document and no required case to 5.3.A or
# 5.3.B. Its one illustrative example for this topic is marked NOT REQUIRED and
# is not used. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.3", "Political Parties", 5)

_CHANNELS = ("A hypothetical survey asked respondents which channels they had used in the past "
             "year to try to communicate their preferences to policymakers, and then which one "
             "they considered most effective.")
_CHANNELS_TABLE = dict(
    headers=["Channel", "Used it in the past year (%)", "Named it the most effective (%)"],
    rows=[["Political parties", "22", "14"],
          ["Interest groups", "17", "21"],
          ["Elections", "63", "48"],
          ["Media", "39", "17"]])

_ACTIVITIES = ("A hypothetical study recorded how one political party's organization divided its "
               "staff time across five activities during an election cycle, and whether each "
               "activity was directed mainly at the electorate or at government.")
_ACTIVITIES_TABLE = dict(
    headers=["Party activity", "Directed mainly at", "Share of staff time (%)"],
    rows=[["Mobilization and education of voters", "The electorate", "31"],
          ["Developing the party platform", "The electorate", "9"],
          ["Candidate recruitment", "The electorate", "18"],
          ["Campaign management, including fundraising and media strategy", "The electorate",
           "27"],
          ["Operating the committee and leadership systems in the legislature", "Government",
           "15"]])

QUESTIONS = [
 dict(q="According to the course framework, what are linkage institutions?",
   choices=[
     "Channels that allow individuals to communicate their preferences to policymakers",
     "Agencies that carry out the laws Congress passes",
     "Courts that resolve disputes between citizens and the government",
     "Channels through which government informs citizens of its decisions",
     "Organizations that draft and enact legislation"], ans=0,
   why="EK 5.3.A.1 defines linkage institutions in exactly these words. The direction of the channel is part of the definition: it runs from individuals to policymakers, not the other way."),

 dict(q="In which direction do the channels EK 5.3.A.1 describes run?",
   choices=[
     "From individuals to policymakers",
     "From policymakers to individuals",
     "Between one branch of government and another",
     "Between the national government and the states",
     "In no particular direction"], ans=0,
   why="EK 5.3.A.1's phrase is 'allow individuals to communicate their preferences to policymakers'. An institution that carries information outward from government to citizens is doing something the framework's definition does not describe."),

 dict(q="A student describes a linkage institution as a way for government to keep the public informed. What is the most important correction?",
   choices=[
     "The framework's definition runs the other way: a linkage institution carries individuals' preferences to policymakers",
     "The framework does not define linkage institutions",
     "The framework lists only two linkage institutions",
     "The framework says linkage institutions are part of government",
     "The framework says linkage institutions carry information in both directions equally"], ans=0,
   why="EK 5.3.A.1's channels allow individuals to communicate their preferences TO POLICYMAKERS, so the student has reversed the arrow. Informing the public is something several of these institutions also do, but it is not what makes them linkage institutions in the framework's sense."),

 dict(q="Which four linkage institutions does EK 5.3.A.1 name?",
   choices=[
     "Political parties, interest groups, elections, and media",
     "Political parties, courts, agencies, and elections",
     "Interest groups, lobbyists, campaigns, and conventions",
     "Elections, primaries, caucuses, and conventions",
     "Media, schools, families, and religious organizations"], ans=0,
   why="EK 5.3.A.1 lists exactly these four. The last option lists the contributors to political socialization from EK 5.2.A.1's companion statement in Unit 4, which is a different list serving a different purpose."),

 dict(q="Why is an ELECTION a linkage institution in the framework's sense?",
   choices=[
     "Because it is a channel through which individuals communicate a preference to those who will make policy",
     "Because it determines the boundaries of legislative districts",
     "Because it is administered by state governments",
     "Because it informs citizens about candidates",
     "Because it is required by the Constitution"], ans=0,
   why="EK 5.3.A.1's definition is about carrying individual preferences to policymakers, and a vote is the most direct form of that communication. That elections are state-administered and constitutionally required is true and is not what places them on this list."),

 dict(q="Why does EK 5.3.A.1 include MEDIA among linkage institutions?",
   choices=[
     "Because it serves as a channel through which the preferences of individuals reach policymakers",
     "Because it broadcasts government announcements to the public",
     "Because it is owned by political parties",
     "Because it is regulated by the federal government",
     "Because it employs professional journalists"], ans=0,
   why="EK 5.3.A.1's definition applies to every item on its list, media included, so media is listed for the same reason as the other three. The outward flow of information is the more obvious thing media does, which is exactly why this item is worth asking."),

 dict(q="Three of the four linkage institutions EK 5.3.A.1 names are the subjects of their own later topics in this unit. What does that indicate about the place of 5.3 in the unit?",
   choices=[
     "It introduces the category that the topics on parties, interest groups, and media then develop in detail",
     "It replaces those later topics",
     "It concerns institutions the later topics reject",
     "It is unrelated to the rest of the unit",
     "It is the last topic in the unit"], ans=0,
   why="EK 5.3.A.1's list names political parties, interest groups, elections and media, and later topics in Unit 5 take up parties, third parties, interest groups, elections and the media in turn. The topic supplies the category the rest of the unit fills in."),

 dict(q="An organization publishes analyses of pending legislation that its members send to their representatives. Which part of EK 5.3.A.1's definition does this activity satisfy?",
   choices=[
     "It is a channel carrying individuals' preferences to policymakers",
     "It is a channel carrying government's decisions to individuals",
     "It is an agency implementing a law",
     "It is a court resolving a dispute",
     "It satisfies no part of the definition, since the organization is private"], ans=0,
   why="What the activity accomplishes is getting members' views in front of representatives, which is EK 5.3.A.1's definition exactly. That the organization is private is what makes it a linkage institution rather than part of the government it is communicating with."),

 dict(q="According to the course framework, what do the functions and impact of political parties bear on?",
   choices=[
     "The electorate and government",
     "The electorate only",
     "Government only",
     "The courts and the bureaucracy",
     "The states and the national government"], ans=0,
   why="LO 5.3.B and EK 5.3.B.1 both name the electorate AND government. Four of the five functions the framework lists are directed at voters and candidates and the fifth is directed at legislatures, so both halves are needed to cover the list."),

 dict(q="Which five functions does EK 5.3.B.1 name?",
   choices=[
     "Mobilization and education of voters, party platforms, candidate recruitment, campaign management, and the committee and party leadership systems in legislatures",
     "Mobilization, platforms, recruitment, and campaign management only",
     "Lobbying, litigating, testifying, and drafting legislation",
     "Nominating, appointing, confirming, and impeaching",
     "Registering voters, counting ballots, certifying results, and seating members"], ans=0,
   why="EK 5.3.B.1 lists five, and the fifth is the committee and party leadership systems in legislatures. The second option is the same list with the fifth removed, which is the standard omission and which drops the government half of the objective."),

 dict(q="Which of EK 5.3.B.1's five functions operates inside government rather than among voters?",
   choices=[
     "The committee and party leadership systems in legislatures",
     "Mobilization and education of voters",
     "Party platforms",
     "Candidate recruitment",
     "Campaign management, including fundraising and media strategy"], ans=0,
   why="EK 5.3.B.1.v names the committee and party leadership systems in legislatures, which are structures within a legislature rather than activities directed at the electorate. It is the item that makes LO 5.3.B's phrase AND GOVERNMENT accurate."),

 dict(q="What does EK 5.3.B.1 include within CAMPAIGN MANAGEMENT?",
   choices=[
     "Fundraising and media strategy",
     "Drafting legislation and holding hearings",
     "Certifying election results",
     "Appointing judges",
     "Setting the rules for primaries in each state"], ans=0,
   why="EK 5.3.B.1.iv's own phrase is 'campaign management, including fundraising and media strategy'. Both named activities are things a party organization does for its candidates rather than things government does."),

 dict(q="A party organization identifies and persuades promising individuals to run for office. Which function does this illustrate?",
   choices=[
     "Candidate recruitment",
     "Mobilization and education of voters",
     "Party platforms",
     "Campaign management",
     "The committee and party leadership systems in legislatures"], ans=0,
   why="EK 5.3.B.1.iii names candidate recruitment, and finding people to run is that function. It is distinct from campaign management, which concerns supporting a candidacy once it exists."),

 dict(q="A party organization runs registration drives and distributes explanations of how and where to vote. Which function does this illustrate?",
   choices=[
     "Mobilization and education of voters",
     "Candidate recruitment",
     "Party platforms",
     "The committee systems in legislatures",
     "Campaign management"], ans=0,
   why="EK 5.3.B.1.i names mobilization and education of voters, and both halves of that phrase are present in the scenario. Neither activity concerns a particular candidate, which is what separates it from campaign management."),

 dict(q="A party adopts a document setting out the positions it commits to. Which function does this illustrate, and which topic elsewhere in the course describes the document?",
   choices=[
     "Party platforms, which EK 4.7.A.1 describes as generally aligning more closely with a set of ideological positions",
     "Candidate recruitment, which EK 5.3.B.1.iii describes",
     "Campaign management, which EK 5.3.B.1.iv describes",
     "Mobilization of voters, which EK 5.3.B.1.i describes",
     "The committee systems in legislatures, which EK 5.3.B.1.v describes"], ans=0,
   why="EK 5.3.B.1.ii names party platforms as a function, and EK 4.7.A.1 says each major party's platforms generally align more closely with a set of ideological positions. The two statements describe the same document from different angles."),

 dict(q="Two members of the same party hold leadership positions in a legislature and coordinate which bills reach the floor. Which function does this illustrate?",
   choices=[
     "The committee and party leadership systems in legislatures",
     "Campaign management",
     "Candidate recruitment",
     "Mobilization and education of voters",
     "Party platforms"], ans=0,
   why="EK 5.3.B.1.v names the committee and party leadership systems in legislatures, and coordinating a legislative agenda through those structures is that function operating. Nothing in the scenario involves voters or candidacies."),

 dict(q="Why would a module on political parties that covered only mobilization, platforms, recruitment, and campaign management be incomplete?",
   choices=[
     "Because it would leave out EK 5.3.B.1.v and with it the whole government half of LO 5.3.B",
     "Because those four functions are not in the framework",
     "Because the framework lists six functions",
     "Because platforms belong to a different topic",
     "Because campaign management is not a party function"], ans=0,
   why="The four named functions are all directed at the electorate, and EK 5.3.B.1.v is the only item on the list operating inside government. LO 5.3.B asks about the impact of parties on the electorate AND government, so dropping the fifth answers half the objective."),

 dict(q="How is a political party's role as a LINKAGE INSTITUTION related to its FUNCTIONS as EK 5.3.B.1 lists them?",
   choices=[
     "Several of the listed functions are the means by which the party carries individuals' preferences toward policymakers",
     "The two are unrelated aspects of parties",
     "The linkage role concerns government and the functions concern voters",
     "A party is a linkage institution only when it is out of power",
     "The framework treats the two as alternative descriptions of elections"], ans=0,
   why="EK 5.3.A.1 makes a party a channel from individuals to policymakers, and EK 5.3.B.1's functions -- mobilizing voters, writing a platform, recruiting candidates -- are the activities through which that channel operates. The two statements describe one institution at two levels."),

 dict(q="What distinguishes a political party from an interest group as linkage institutions, given that EK 5.3.A.1 lists both?",
   choices=[
     "Parties recruit and run candidates for office under their own label, which EK 5.3.B.1 lists among their functions",
     "Only parties communicate preferences to policymakers",
     "Only interest groups communicate preferences to policymakers",
     "Interest groups are part of government and parties are not",
     "The framework treats the two as identical"], ans=0,
   why="EK 5.3.A.1 assigns both the same channel role, so the difference has to come from elsewhere, and EK 5.3.B.1.iii and iv name candidate recruitment and campaign management as party functions. EK 5.6.A.1 describes what interest groups do instead, and running candidates under a label is not on that list."),

 dict(q="Which of the following does EK 5.3.A.1 NOT state?",
   choices=[
     "Which of the four linkage institutions is most effective",
     "That linkage institutions are channels for individuals to communicate preferences to policymakers",
     "That political parties are a linkage institution",
     "That elections are a linkage institution",
     "That media is a linkage institution"], ans=0,
   why="EK 5.3.A.1 supplies a definition and a list of four and ranks none of them. Every other option restates part of the statement."),

 dict(q="LO 5.3.A's verb is DESCRIBE and LO 5.3.B's is EXPLAIN. What does that difference indicate about what each asks for?",
   choices=[
     "The first asks what linkage institutions are, and the second asks how party functions produce effects on the electorate and government",
     "The first asks for an argument and the second for a definition",
     "The two verbs mean the same thing in the framework",
     "The first concerns data and the second concerns sources",
     "The second asks only for a list"], ans=0,
   why="A description states what something is, which is what EK 5.3.A.1's definition and list supply, while an explanation gives an account of how something works, which is what EK 5.3.B.1's functions and their impact call for. The framework's choice of verbs matches the content behind each objective."),

 dict(q="A citizen joins a party, attends its meetings, and helps write a resolution that the party later adopts into its platform. Which two things in the framework does this sequence illustrate?",
   choices=[
     "A party operating as a linkage institution, and the party platform function of EK 5.3.B.1.ii",
     "An interest group filing an amicus curiae brief, and candidate recruitment",
     "An election as a linkage institution, and campaign management",
     "Media agenda setting, and mobilization of voters",
     "The committee systems in legislatures, and voter education"], ans=0,
   why="The citizen's preference travels through the party toward the positions it commits to, which is EK 5.3.A.1's channel, and the document produced is EK 5.3.B.1.ii's party platform. Both statements describe the same episode at different levels."),

 dict(q="Why does the framework describe EK 5.3.B.1's items as the functions AND IMPACT of parties rather than as functions alone?",
   choices=[
     "Because each item names something a party does and also something that has an effect on the electorate or on government",
     "Because impact is measured only after an election",
     "Because the framework doubts that parties have functions",
     "Because impact is a synonym for function in the framework",
     "Because only the fifth item has any impact"], ans=0,
   why="EK 5.3.B.1's own phrase is 'the functions and impact of political parties on the electorate and government', and each listed item is both an activity and a way the party bears on someone. Mobilizing voters is a function; more voters mobilized is an impact."),

 dict(q="Which statement best summarizes what this topic establishes about political parties?",
   choices=[
     "They are one of four channels carrying individual preferences to policymakers, and they act on both the electorate and government through five named functions",
     "They are the only channel carrying preferences to policymakers",
     "They act on the electorate but not on government",
     "They act on government but not on the electorate",
     "They are agencies of the national government"], ans=0,
   why="EK 5.3.A.1 places parties among four linkage institutions and EK 5.3.B.1 lists five functions reaching both the electorate and government. Each of the other options drops one of those two statements or overstates it."),

 dict(q=_CHANNELS + " Which conclusion is best supported by the data?",
   table=_CHANNELS_TABLE,
   choices=[
     "Elections lead both columns, and interest groups are the only channel named most effective by a larger share than the share that used it",
     "Media leads both columns",
     "Every channel was named most effective by a larger share than used it",
     "Political parties were used by more respondents than elections",
     "No channel was used by more than a quarter of respondents"], ans=0,
   why="Elections stand at 63 percent used and 48 percent named most effective, the largest figure in each column. Interest groups run 17 used against 21 named most effective, while parties, elections and media all fall in the second column."),

 dict(q=_CHANNELS + " The four rows of this table correspond to which statement in the course framework?",
   table=_CHANNELS_TABLE,
   choices=[
     "EK 5.3.A.1's list of four linkage institutions",
     "EK 5.3.B.1's five functions of political parties",
     "EK 5.2.A.4's factors influencing voter choice",
     "EK 5.1.B.1's models of voting behavior",
     "EK 5.2.A.2's influences on turnout"], ans=0,
   why="The rows are political parties, interest groups, elections and media, which is EK 5.3.A.1's list exactly. The stem's description of the channels also matches the framework's definition, since respondents were asked about communicating preferences to policymakers."),

 dict(q=_CHANNELS + " A student concludes from the second column that media should not be counted as a linkage institution. What is the most important correction?",
   table=_CHANNELS_TABLE,
   choices=[
     "EK 5.3.A.1 lists media as one of the four, and how effective respondents consider a channel does not determine whether it meets the framework's definition",
     "The table shows media as the most effective channel",
     "The table reports no figure for media",
     "Media was used by fewer respondents than any other channel",
     "The framework lists five linkage institutions rather than four"], ans=0,
   why="Membership in EK 5.3.A.1's list follows from the definition, which is being a channel from individuals to policymakers, not from a rating. Media was in fact used by 39 percent, the second highest in that column, so it is not the least used either."),

 dict(q=_ACTIVITIES + " Which conclusion is best supported by the data?",
   table=_ACTIVITIES_TABLE,
   choices=[
     "Four of the five activities are directed mainly at the electorate and one at government, and the electorate-directed activities together take most of the staff time",
     "Every activity is directed mainly at government",
     "Every activity is directed mainly at the electorate",
     "The government-directed activity takes the largest share of staff time",
     "The five activities take equal shares of staff time"], ans=0,
   why="The second column reads electorate four times and government once, and the four electorate rows total 85 percent of staff time against 15 for the government row. Mobilization takes the largest single share at 31 percent."),

 dict(q=_ACTIVITIES + " The five rows of this table correspond to which statement in the course framework?",
   table=_ACTIVITIES_TABLE,
   choices=[
     "EK 5.3.B.1's five functions of political parties",
     "EK 5.3.A.1's four linkage institutions",
     "EK 5.2.A.4's factors influencing voter choice",
     "EK 5.1.A.1's amendments protecting voting rights",
     "EK 5.6.A.1's account of what interest groups do"], ans=0,
   why="The rows are mobilization and education of voters, party platforms, candidate recruitment, campaign management, and the committee and leadership systems in the legislature, which is EK 5.3.B.1's list in order. There are five rows because the framework names five functions."),

 dict(q=_ACTIVITIES + " A student concludes from this table that political parties act only on voters. What is the most important correction?",
   table=_ACTIVITIES_TABLE,
   choices=[
     "One row is directed at government and accounts for 15 percent of staff time, and it corresponds to EK 5.3.B.1.v, the government half of what LO 5.3.B asks about",
     "Every row in the table is directed at government",
     "The table reports no figure for the government-directed row",
     "The government-directed row takes the largest share of staff time",
     "The framework lists only four functions of political parties"], ans=0,
   why="The committee and leadership row is directed at government and is a real 15 percent of the party's staff time, so the conclusion overlooks a row rather than reading one wrongly. EK 5.3.B.1.v is the only item on the framework's list operating inside government, which is why dropping it costs half of LO 5.3.B."),
]
