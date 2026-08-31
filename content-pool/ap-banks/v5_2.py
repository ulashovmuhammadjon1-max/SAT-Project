# AP U.S. GOVERNMENT AND POLITICS 5.2 Voter Turnout -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.2.A: explain the roles that INDIVIDUAL CHOICE and STATE
# LAWS play in voter turnout in elections.
# Suggested skill for this topic (CED p. 116): 3.C, data analysis -- EXPLAIN
# PATTERNS AND TRENDS IN DATA TO DRAW CONCLUSIONS.
#
# Essential knowledge relied on. Four statements, and the fourth is about a
# DIFFERENT QUESTION from the first three:
#   EK 5.2.A.1 -- "STRUCTURAL BARRIERS (such as polling hours, availability of
#     absentee ballots, etc.), POLITICAL EFFICACY (THE BELIEF THAT AN
#     INDIVIDUAL'S PARTICIPATION IN THE POLITICAL PROCESS WILL MAKE A
#     DIFFERENCE), and DEMOGRAPHICS can influence differences in voter turnout."
#   EK 5.2.A.2 -- three things that can influence turnout:
#       i.   "Differences in STATE-CONTROLLED ELECTIONS (the hours polls are
#            open, Voter ID laws, variations in funding for polling places and
#            workers, variations in types of voting allowed, such as voting by
#            mail, absentee voting, and early voting)"
#       ii.  "Variations in VOTER REGISTRATION laws and procedures (registering
#            in-person, online, or automatically)"
#       iii. "ELECTION TYPE (MORE TURNOUT FOR PRESIDENTIAL ELECTIONS THAN MIDTERM
#            ELECTIONS)"
#   EK 5.2.A.3 -- "Demographic characteristics and political efficacy or
#     engagement are used to PREDICT THE LIKELIHOOD of whether an individual will
#     vote."
#   EK 5.2.A.4 -- "Factors influencing VOTER CHOICE include:
#       i.   Party identification and ideological orientation
#       ii.  Candidate characteristics
#       iii. Contemporary political issues
#       iv.  Religious beliefs or affiliation, age, gender, race and ethnicity,
#            and other demographic characteristics"
#
# TURNOUT AND VOTER CHOICE ARE TWO DIFFERENT QUESTIONS, AND THIS TOPIC ANSWERS
# BOTH. EK 5.2.A.1 to 3 are about WHETHER a person votes; EK 5.2.A.4 is about
# WHOM they vote for. The two lists even share an item -- demographics appears in
# both -- which is exactly what makes them easy to run together, and running them
# together is the error this module is built against. Evidence about turnout says
# nothing about choice and evidence about choice says nothing about turnout.
# Items 16 to 21 and item 30 turn on it, and the verifier refuses any key that
# offers a turnout factor as an explanation of choice or the reverse.
#
# LO 5.2.A NAMES TWO ROLES: INDIVIDUAL CHOICE AND STATE LAWS. That pairing maps
# onto the essential knowledge cleanly -- political efficacy is the individual
# side and EK 5.2.A.2.i and ii are the state side -- and it is why a module on
# this topic cannot be only about laws or only about attitudes.
#
# POLITICAL EFFICACY HAS A DEFINITION AND IT IS A BELIEF. EK 5.2.A.1's
# parenthesis is "the belief that an individual's participation in the political
# process will make a difference". It is not interest, not knowledge, and not
# actual influence -- a person may have high efficacy and little influence, or
# the reverse. Item 4 makes the definition the question.
#
# THE ONE DIRECTIONAL FACT THE FRAMEWORK STATES OUTRIGHT is in EK 5.2.A.2.iii:
# more turnout for presidential elections than midterm elections. Almost
# everything else in this topic is a list of things that CAN influence turnout,
# without a direction. The first table carries the stated fact in every row.
#
# The CED attaches no foundational document and no required case to 5.2.A. All
# three tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.2", "Voter Turnout", 5)

_AGE = ("A hypothetical study reports turnout among eligible voters in one state, by age group, "
        "in a presidential election year and in the midterm election that followed.")
_AGE_TABLE = dict(
    headers=["Age group", "Presidential election turnout (%)", "Midterm election turnout (%)"],
    rows=[["Ages 18 to 24", "43", "20"],
          ["Ages 25 to 44", "57", "35"],
          ["Ages 45 to 64", "69", "52"],
          ["Age 65 and older", "74", "61"]])

_LAWS = ("A hypothetical study reports four states' election rules alongside turnout in the same "
         "election.")
_LAWS_TABLE = dict(
    headers=["State", "Days of early voting offered", "Online registration available",
             "Turnout (%)"],
    rows=[["State A", "0", "No", "54"],
          ["State B", "10", "No", "61"],
          ["State C", "14", "Yes", "68"],
          ["State D", "21", "Yes", "66"]])

_EFFICACY = ("A hypothetical survey grouped respondents by how strongly they reported believing "
             "that their own participation makes a difference, and then recorded whether each "
             "voted.")
_EFFICACY_TABLE = dict(
    headers=["Reported level of political efficacy", "Share of the sample (%)",
             "Share of the group who voted (%)"],
    rows=[["High", "28", "83"],
          ["Moderate", "41", "62"],
          ["Low", "31", "34"]])

QUESTIONS = [
 dict(q="According to the course framework, which three things can influence differences in voter turnout in the United States?",
   choices=[
     "Structural barriers, political efficacy, and demographics",
     "Party platforms, campaign spending, and media coverage",
     "Judicial decisions, executive orders, and treaties",
     "Interest groups, lobbyists, and political action committees",
     "Federalism, separation of powers, and checks and balances"], ans=0,
   why="EK 5.2.A.1 names exactly these three. Two of them are features of the system a voter encounters and one, political efficacy, is a belief the voter holds, which is why LO 5.2.A pairs state laws with individual choice."),

 dict(q="What examples does EK 5.2.A.1 give of STRUCTURAL BARRIERS?",
   choices=[
     "Polling hours and the availability of absentee ballots",
     "Party identification and ideological orientation",
     "Candidate characteristics and contemporary issues",
     "Religious affiliation and age",
     "Campaign advertising and media endorsements"], ans=0,
   why="EK 5.2.A.1's parenthesis names polling hours and the availability of absentee ballots. The other options list factors the framework assigns to voter CHOICE in EK 5.2.A.4, which is a different question."),

 dict(q="According to the course framework, what is POLITICAL EFFICACY?",
   choices=[
     "The belief that an individual's participation in the political process will make a difference",
     "The amount of influence an individual actually has over policy",
     "The level of a person's knowledge about government",
     "The degree of a person's interest in following the news",
     "The number of elections in which a person has voted"], ans=0,
   why="EK 5.2.A.1 defines political efficacy in exactly these words, and the framework's noun is a BELIEF. It is not actual influence, not knowledge and not interest, so a person may hold the belief strongly while having little influence, or the reverse."),

 dict(q="Why does it matter that the framework defines political efficacy as a BELIEF rather than as actual influence?",
   choices=[
     "Because what drives a person's decision to participate is what they believe about their participation, whatever their actual influence turns out to be",
     "Because beliefs are easier to measure than influence",
     "Because the framework says individuals have no actual influence",
     "Because efficacy applies only to people who already vote",
     "Because actual influence is fixed by law"], ans=0,
   why="EK 5.2.A.1's parenthesis makes efficacy a belief about whether participation will make a difference, and EK 5.2.A.3 uses it to predict whether an individual will vote. A belief can motivate an action whether or not it is accurate."),

 dict(q="Which of the three influences EK 5.2.A.1 names corresponds to the INDIVIDUAL CHOICE half of LO 5.2.A?",
   choices=[
     "Political efficacy, since it is a belief the individual holds",
     "Structural barriers, since individuals encounter them",
     "Demographics, since they describe individuals",
     "None of the three, since the objective concerns only state laws",
     "All three equally, since each concerns individuals"], ans=0,
   why="LO 5.2.A names individual choice and state laws as the two roles, and EK 5.2.A.1's political efficacy is the item defined as a belief a person holds. Structural barriers are features of how elections are run, and demographics are characteristics rather than choices."),

 dict(q="Which of the influences EK 5.2.A.1 and EK 5.2.A.2 name corresponds most closely to the STATE LAWS half of LO 5.2.A?",
   choices=[
     "Differences in state-controlled elections and variations in voter registration laws and procedures",
     "Political efficacy and engagement",
     "Demographic characteristics",
     "Party identification and ideological orientation",
     "Candidate characteristics"], ans=0,
   why="EK 5.2.A.2.i and EK 5.2.A.2.ii both describe rules a state sets, which is the state laws half of the objective. Party identification and candidate characteristics belong to EK 5.2.A.4's list of factors influencing voter choice."),

 dict(q="What does EK 5.2.A.2 name as examples of differences in STATE-CONTROLLED ELECTIONS?",
   choices=[
     "The hours polls are open, Voter ID laws, funding for polling places and workers, and the types of voting allowed",
     "The party affiliation of the governor and the size of the legislature",
     "The number of candidates on the ballot and the length of the campaign",
     "Party identification and ideological orientation",
     "Religious affiliation, age, and gender"], ans=0,
   why="EK 5.2.A.2.i's parenthesis names all four, and its examples of types of voting allowed are voting by mail, absentee voting and early voting. Each is something a state decides rather than something a voter brings."),

 dict(q="What three types of voting does EK 5.2.A.2.i give as examples of variations a state may allow?",
   choices=[
     "Voting by mail, absentee voting, and early voting",
     "Straight ticket, split ticket, and write-in voting",
     "Primary, caucus, and general election voting",
     "Retrospective, prospective, and rational choice voting",
     "In-person, online, and automatic voting"], ans=0,
   why="EK 5.2.A.2.i names voting by mail, absentee voting and early voting. The last option names EK 5.2.A.2.ii's registration methods rather than types of voting, and the fourth names EK 5.1.B.1's models of voting behavior."),

 dict(q="What three registration methods does EK 5.2.A.2.ii name?",
   choices=[
     "Registering in person, online, or automatically",
     "Registering by mail, by telephone, or in person",
     "Registering at a polling place, at a school, or at a courthouse",
     "Registering with a party, as an independent, or as unaffiliated",
     "Voting by mail, absentee voting, and early voting"], ans=0,
   why="EK 5.2.A.2.ii's parenthesis names registering in person, online, or automatically. The last option names the types of voting from EK 5.2.A.2.i, which is a separate item in the same list."),

 dict(q="According to EK 5.2.A.2, how does turnout differ by election type?",
   choices=[
     "There is more turnout for presidential elections than for midterm elections",
     "There is more turnout for midterm elections than for presidential elections",
     "Turnout is the same in both types of election",
     "Turnout depends only on the state and not on the election type",
     "The framework does not compare election types"], ans=0,
   why="EK 5.2.A.2.iii states the comparison directly, and it is one of the few directional facts the framework states outright in this topic. Almost everything else in EK 5.2.A.1 and EK 5.2.A.2 is a list of things that CAN influence turnout without a stated direction."),

 dict(q="Most of the items EK 5.2.A.1 and EK 5.2.A.2 list are described as things that CAN influence turnout. What does that wording indicate?",
   choices=[
     "That the framework identifies possible influences without stating how much each matters or in which direction",
     "That none of the listed items actually influences turnout",
     "That each item always increases turnout",
     "That each item always decreases turnout",
     "That the items influence voter choice rather than turnout"], ans=0,
   why="The framework's verb is CAN INFLUENCE, which is a claim about possibility rather than magnitude or direction. EK 5.2.A.2.iii is the exception that proves it, since that is the one item where a direction is stated."),

 dict(q="A state extends the hours its polls are open and begins allowing registration online. Which two items in EK 5.2.A.2 do these changes correspond to?",
   choices=[
     "Differences in state-controlled elections, and variations in voter registration laws and procedures",
     "Election type, and demographic characteristics",
     "Political efficacy, and party identification",
     "Candidate characteristics, and contemporary political issues",
     "Both correspond to election type"], ans=0,
   why="Polling hours appear in EK 5.2.A.2.i's parenthesis and online registration in EK 5.2.A.2.ii's, so the two changes fall under two different items of the framework's own list. Election type concerns whether the election is presidential or midterm."),

 dict(q="According to EK 5.2.A.3, what are demographic characteristics and political efficacy or engagement used to do?",
   choices=[
     "Predict the likelihood of whether an individual will vote",
     "Determine which candidate an individual will support",
     "Set the rules a state uses to run its elections",
     "Measure how much influence an individual has over policy",
     "Decide whether an election is presidential or midterm"], ans=0,
   why="EK 5.2.A.3 states this in exactly these words. Its object is whether a person will vote at all, which is turnout, and not whom they will vote for, which EK 5.2.A.4 treats separately."),

 dict(q="EK 5.2.A.3 says these characteristics are used to PREDICT A LIKELIHOOD. What does that phrasing indicate about the claim?",
   choices=[
     "That the characteristics support a probabilistic expectation about an individual rather than a certainty",
     "That the characteristics determine with certainty whether a person votes",
     "That the characteristics are used only after an election",
     "That the characteristics apply only to people who have already voted",
     "That prediction is prohibited by the framework"], ans=0,
   why="A likelihood is a probability, so EK 5.2.A.3 supports an expectation rather than a rule about any individual. A person with characteristics associated with low turnout may vote, which the wording accommodates."),

 dict(q="What does EK 5.2.A.3 add that EK 5.2.A.1 does not already say?",
   choices=[
     "That the same characteristics can be used to predict an individual's likelihood of voting, not only to explain differences in turnout across groups",
     "That structural barriers do not influence turnout",
     "That demographics are irrelevant to turnout",
     "That political efficacy is a state law",
     "That turnout is the same in every election"], ans=0,
   why="EK 5.2.A.1 says the three influences can explain DIFFERENCES in turnout, which is a claim about variation across people, while EK 5.2.A.3 turns the same factors toward an individual-level prediction. The second is a use of the first."),

 dict(q="According to EK 5.2.A.4, what do the factors it lists influence?",
   choices=[
     "Voter choice",
     "Voter turnout",
     "The rules a state sets for its elections",
     "The date on which an election is held",
     "The number of candidates on a ballot"], ans=0,
   why="EK 5.2.A.4's own words are 'Factors influencing voter choice include'. Choice is whom a person votes for, which is a different question from whether they vote at all, and EK 5.2.A.1 to 3 answer that other question."),

 dict(q="Which four factors does EK 5.2.A.4 list as influencing voter choice?",
   choices=[
     "Party identification and ideological orientation, candidate characteristics, contemporary political issues, and demographic characteristics",
     "Polling hours, Voter ID laws, registration methods, and election type",
     "Structural barriers, political efficacy, demographics, and state laws",
     "Rational choice, retrospective, prospective, and straight ticket voting",
     "Mobilization, party platforms, candidate recruitment, and campaign management"], ans=0,
   why="EK 5.2.A.4's four items are exactly these. The second and third options list turnout influences from EK 5.2.A.1 and EK 5.2.A.2, the fourth lists EK 5.1.B.1's models of voting behavior, and the fifth lists EK 5.3.B.1's party functions."),

 dict(q="Which factor appears in BOTH the framework's account of turnout and its list of factors influencing voter choice?",
   choices=[
     "Demographic characteristics",
     "Political efficacy",
     "Structural barriers",
     "Election type",
     "Registration procedures"], ans=0,
   why="EK 5.2.A.1 names demographics among the influences on turnout and EK 5.2.A.4.iv names demographic characteristics among the influences on choice. That overlap is exactly what makes the two questions easy to run together, since one factor bears on both."),

 dict(q="A researcher shows that a demographic group votes at a lower rate than others. What does this finding bear on, in the framework's terms?",
   choices=[
     "Turnout, since it concerns whether members of the group vote, and it says nothing about whom those who vote support",
     "Voter choice, since it concerns a demographic group",
     "Both equally, since demographics appear in both lists",
     "Neither, since the framework does not discuss demographic groups",
     "Voter choice, since a lower rate implies a preference"], ans=0,
   why="A rate of voting is a turnout measure, which EK 5.2.A.1 and EK 5.2.A.3 address. That demographics also appear in EK 5.2.A.4 does not make a turnout finding a finding about choice, because the two statements ask different questions of the same characteristic."),

 dict(q="A researcher shows that voters who identify with a party overwhelmingly support that party's candidate. What does this finding bear on, in the framework's terms?",
   choices=[
     "Voter choice, since it concerns whom voters support rather than whether they turn out",
     "Turnout, since party identifiers vote more often",
     "Both equally, since party identification appears in both lists",
     "Neither, since party identification is not in the framework",
     "Turnout, since the finding concerns an election"], ans=0,
   why="EK 5.2.A.4.i names party identification among the factors influencing voter choice, and the finding is about whom voters supported. Party identification does not appear in EK 5.2.A.1 to 3, so the framework does not offer it here as a turnout factor."),

 dict(q="Why does the framework treat turnout and voter choice as separate questions within one topic?",
   choices=[
     "Because whether a person votes and whom they vote for are different decisions that different factors bear on",
     "Because the two questions are answered by the same list of factors",
     "Because turnout concerns states and choice concerns the national government",
     "Because voter choice is not part of the course",
     "Because turnout is measured before an election and choice afterward"], ans=0,
   why="EK 5.2.A.1 to 3 concern whether an individual will vote and EK 5.2.A.4 concerns what influences the vote itself, and the framework gives them separate statements with mostly different items. Evidence about one is not evidence about the other."),

 dict(q=_AGE + " Which conclusion is best supported by the data?",
   table=_AGE_TABLE,
   choices=[
     "Turnout rises with age in both elections, and every age group turned out at a higher rate in the presidential election than in the midterm",
     "Turnout falls with age in both elections",
     "Midterm turnout exceeded presidential turnout in at least one age group",
     "The youngest and oldest groups turned out at similar rates",
     "Turnout was identical across the four age groups in the midterm election"], ans=0,
   why="Reading down each column gives 43, 57, 69, 74 and 20, 35, 52, 61, both rising with age. Every presidential figure exceeds the midterm figure in the same row, and the youngest and oldest groups differ by 31 points in the presidential election."),

 dict(q=_AGE + " Which statements in the course framework does this pattern most directly illustrate?",
   table=_AGE_TABLE,
   choices=[
     "EK 5.2.A.2.iii's greater turnout in presidential than midterm elections, together with EK 5.2.A.1's inclusion of demographics among the influences on turnout",
     "EK 5.2.A.4's factors influencing voter choice",
     "EK 5.1.B.1's four models of voting behavior",
     "EK 5.3.A.1's list of linkage institutions",
     "EK 5.2.A.2.ii's variations in registration procedures"], ans=0,
   why="Two patterns are present and each corresponds to a framework statement: the gap between the columns is EK 5.2.A.2.iii's stated comparison, and the gradient down each column is a demographic difference of the kind EK 5.2.A.1 names. Nothing here concerns whom anyone voted for."),

 dict(q=_AGE + " A candidate's campaign is deciding how much attention to give issues favored mainly by the youngest age group. Which conclusion does the data best support?",
   table=_AGE_TABLE,
   choices=[
     "The youngest group casts the smallest share of the votes actually cast, so a campaign has less electoral incentive to prioritize its issues, especially in a midterm year",
     "The youngest group turns out at the highest rate, so its issues should be prioritized",
     "Turnout rates give no information relevant to a campaign's decisions",
     "The oldest group turns out at the lowest rate in midterm elections",
     "The data show which issues each age group favors"], ans=0,
   why="The youngest group turns out at 43 percent in the presidential election and 20 percent in the midterm, the lowest in both columns and less than a third of the oldest group's midterm rate. The table reports turnout only, so the reasoning runs through how many votes a group casts rather than through what it wants."),

 dict(q=_LAWS + " Which conclusion is best supported by the data?",
   table=_LAWS_TABLE,
   choices=[
     "Both states offering online registration had higher turnout than either state without it, while more days of early voting did not always mean higher turnout",
     "Turnout rose with every additional day of early voting",
     "The state with the most early voting days had the highest turnout",
     "Online registration made no difference to turnout in this table",
     "All four states reported the same turnout"], ans=0,
   why="The two states with online registration report 68 and 66 percent against 54 and 61 for the two without. The state offering 21 days of early voting reports 66 percent, below the state offering 14 days at 68, so days alone do not order turnout."),

 dict(q=_LAWS + " Which statements in the course framework do the first two columns of this table correspond to?",
   table=_LAWS_TABLE,
   choices=[
     "EK 5.2.A.2.i's variations in types of voting allowed, and EK 5.2.A.2.ii's variations in registration procedures",
     "EK 5.2.A.4's factors influencing voter choice",
     "EK 5.2.A.1's definition of political efficacy",
     "EK 5.1.A.1's amendments protecting voting rights",
     "EK 5.3.B.1's functions of political parties"], ans=0,
   why="Early voting is named in EK 5.2.A.2.i's list of types of voting a state may allow, and online registration in EK 5.2.A.2.ii's list of registration procedures. Both are things a state decides, which is the state laws half of LO 5.2.A."),

 dict(q=_LAWS + " What is the most important limitation of this data as evidence about which policy raises turnout?",
   table=_LAWS_TABLE,
   choices=[
     "The two policies vary together across these states, and the states differ in other ways the table does not report, so no single policy's effect can be isolated",
     "The table does not report turnout",
     "The table reports only one state",
     "The table shows identical turnout in all four states",
     "The table reports registration but not early voting"], ans=0,
   why="Both states with online registration also offer more early voting days than the state with none, so the two policies are not separated in this data. Four states also differ in population, politics and much else that the table does not measure."),

 dict(q=_EFFICACY + " Which conclusion is best supported by the data?",
   table=_EFFICACY_TABLE,
   choices=[
     "The share of a group who voted rises with its reported level of political efficacy, from 34 percent to 83 percent",
     "The share who voted falls as reported efficacy rises",
     "Every group voted at a similar rate",
     "The largest group in the sample voted at the highest rate",
     "No group voted at a rate above half"], ans=0,
   why="The voting shares are 83, 62 and 34 percent for high, moderate and low efficacy, a range of 49 points. The largest group in the sample is the moderate one at 41 percent, which voted at 62 percent rather than the highest rate."),

 dict(q=_EFFICACY + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_EFFICACY_TABLE,
   choices=[
     "EK 5.2.A.3's use of political efficacy to predict the likelihood of whether an individual will vote",
     "EK 5.2.A.4's factors influencing voter choice",
     "EK 5.2.A.2.iii's comparison of presidential and midterm turnout",
     "EK 5.1.A.1's amendments protecting voting rights",
     "EK 5.3.A.1's list of linkage institutions"], ans=0,
   why="The table pairs a reported level of efficacy with whether people voted, which is the prediction EK 5.2.A.3 describes. The stem's description of efficacy also matches EK 5.2.A.1's definition, a belief that one's own participation makes a difference."),

 dict(q=_EFFICACY + " A student uses this table to explain which candidate the respondents supported. What is the most important correction?",
   table=_EFFICACY_TABLE,
   choices=[
     "The table measures whether people voted, which is turnout, and the framework treats the factors influencing voter choice separately in EK 5.2.A.4",
     "The table reports which candidate each group supported",
     "The table shows that efficacy has no relationship to voting",
     "The table covers a single respondent, so no share can be computed",
     "Political efficacy appears in the framework's list of factors influencing choice"], ans=0,
   why="Both of the table's data columns concern participation and neither records a preference between candidates. EK 5.2.A.4's list of factors influencing voter choice does not include political efficacy, so the framework offers no route from this table to a conclusion about choice."),
]
