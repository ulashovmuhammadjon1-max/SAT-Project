# AP COMPARATIVE GOVERNMENT AND POLITICS 3.9 Challenges from Political and Social
# Cleavages
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding LEG-2; learning objective LEG-2.B. Suggested skill 5.C,
# Argumentation (use reasoning to organize and analyze evidence, explaining its
# significance to justify the claim or thesis).
#
# Essential knowledge relied on -- this topic has ONE statement:
#   LEG-2.B.5  challenges governments face in SECURING STABILITY IN MULTINATIONAL
#              STATES include:
#     .a CONFLICTING INTERESTS AND COMPETITION AMONG GROUPS AND POLITICAL PARTIES
#     .b PERCEIVED LACK OF GOVERNMENTAL AUTHORITY AND LEGITIMACY
#     .c PRESSURE FOR AUTONOMY/SECESSION, INTERGROUP CONFLICT, TERRORISM, and CIVIL
#        WAR
#     .d ENCROACHMENT OF NEIGHBORING STATES THAT SENSE GOVERNMENT WEAKNESS AND
#        VULNERABILITY
#
# THREE OF THE FOUR ARE INTERNAL AND THE FOURTH IS EXTERNAL. That asymmetry is the
# most testable feature of the statement and items 6 and 25 key it, because a
# student who treats the list as uniformly internal misses that the framework makes
# a government's perceived weakness an invitation to outside pressure.
#
# One sentence cannot carry thirty items, so the surrounding statements supply the
# rest, each named in the verifier's claim:
#   LEG-2.B.2.b  responses ranging from BRUTE REPRESSION to RECOGNITION, AUTONOMOUS
#                REGIONS and REPRESENTATION IN GOVERNMENTAL INSTITUTIONS
#   LEG-2.B.3    cleavages used to STRENGTHEN LEGITIMACY AND HOLD ONTO POWER in all
#                course countries, and able to UNDERMINE LEGITIMACY
#   LEG-2.B.4.a-b  separatist movements in five course countries; autonomy-without-
#                independence groups in two
#   LEG-1.A.1    legitimacy is whether constituents BELIEVE the government has the
#                right to use power as it does
#   LEG-1.B.3    serious problems such as social conflicts can UNDERMINE legitimacy
#   LEG-1.C.1.b  state responses to SEPARATIST GROUP VIOLENCE, drug trafficking and
#                discrimination in IRAN, MEXICO and NIGERIA
#   LEG-1.C.2    states limit DIVISIVE AND VIOLENT ACTORS to attract private capital
#                and foreign direct investment
#   PAU-2.A.2    the degree of centralization often reflects a response to ETHNIC
#                CLEAVAGES and to SUPRANATIONAL ORGANIZATIONS AND OTHER COUNTRIES
#   DEM-1.A.3    violent political behavior is likelier when conventional options
#                are felt ineffective or unavailable
#   MPA-1.A.3    causation cannot be isolated and demonstrated with certainty
#
# Topic 1.10 keys LEG-2.B.5's list as a single recall item. This module instead
# works through the four sub-points one at a time, keys the internal/external
# asymmetry, and puts the list into a matrix and a data set.
#
# Table figures and cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.9", "Challenges from Political and Social Cleavages", 3)

_T_CHAL = dict(
    headers=["Reported challenge (hypothetical sample of multinational states)",
             "Number of states reporting it",
             "Number of those states in which the government's approval fell in the same period"],
    rows=[["Conflicting interests and competition among groups and political parties", "31", "12"],
          ["Perceived lack of governmental authority and legitimacy", "18", "17"],
          ["Pressure for autonomy or secession", "22", "14"],
          ["Encroachment by a neighboring state", "6", "5"]])

_T_SCEN = dict(
    headers=["Case (hypothetical)", "What is reported"],
    rows=[["Case 1", "two parties representing different groups each refuse to govern with the other, and no budget passes for a year"],
          ["Case 2", "citizens across several regions say the national government has no right to make decisions for them"],
          ["Case 3", "an armed movement in one province declares independence and fighting spreads"],
          ["Case 4", "a neighboring state moves troops to the border after judging the government unable to control its territory"]])

_T_STAB = dict(
    headers=["Country (hypothetical)", "Number of the framework's four challenges reported",
             "Government approval (percent)"],
    rows=[["Country N", "1", "62"],
          ["Country P", "3", "34"],
          ["Country Q", "4", "19"]])

QUESTIONS = [
 dict(q="The framework's list of challenges in this topic is introduced as a list of challenges to what?",
   choices=[
     "securing stability in multinational states",
     "securing international recognition for a new state",
     "conducting elections in federal systems",
     "appointing an independent judiciary",
     "joining a supranational organization"], ans=0,
   why="EK LEG-2.B.5 introduces its four items as challenges governments face in securing stability in multinational states, which is why every one of them concerns divisions inside a society rather than the machinery of elections, courts or treaties."),
 dict(q="Which challenge does the framework name that concerns rivalry among organized political actors?",
   choices=[
     "conflicting interests and competition among groups and political parties",
     "perceived lack of governmental authority and legitimacy",
     "pressure for autonomy or secession",
     "encroachment of neighboring states",
     "the absence of a written constitution"], ans=0,
   why="EK LEG-2.B.5.a names conflicting interests and competition among groups and political parties. The other options are the framework's other three challenges and one that appears nowhere in the statement."),
 dict(q="Which challenge does the framework name that concerns what citizens believe about their government?",
   choices=[
     "perceived lack of governmental authority and legitimacy",
     "conflicting interests among political parties",
     "terrorism and civil war",
     "encroachment of neighboring states",
     "competition for natural resources"], ans=0,
   why="EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy, and EK LEG-1.A.1 makes legitimacy a matter of whether constituents believe their government has the right to use power in the way it does. The word 'perceived' is what places this challenge in the realm of belief."),
 dict(q="Which set of difficulties does the framework group together in the third of its four challenges?",
   choices=[
     "pressure for autonomy or secession, intergroup conflict, terrorism, and civil war",
     "inflation, unemployment, and falling exports",
     "low turnout, weak parties, and infrequent elections",
     "judicial delay, prison overcrowding, and police shortages",
     "treaty obligations and supranational regulation"], ans=0,
   why="EK LEG-2.B.5.c groups pressure for autonomy or secession, intergroup conflict, terrorism and civil war in a single item, which runs from a political demand through to organized violence."),
 dict(q="Which challenge does the framework describe as arising outside the state?",
   choices=[
     "encroachment of neighboring states that sense government weakness and vulnerability",
     "conflicting interests among groups and political parties",
     "a perceived lack of governmental authority and legitimacy",
     "pressure for autonomy or secession",
     "intergroup conflict and terrorism"], ans=0,
   why="EK LEG-2.B.5.d is the only one of the four that names an actor outside the state, describing neighboring states that sense government weakness and vulnerability. The other three arise among a state's own groups, parties and citizens."),
 dict(q="What is the relationship the framework draws between a government's internal difficulties and the behavior of its neighbors?",
   choices=[
     "neighboring states may encroach when they sense that the government is weak and vulnerable",
     "neighboring states withdraw from contact when a government is weak",
     "neighboring states are required to assist a weakened government",
     "the framework describes no connection between the two",
     "neighboring states encroach only where a government is strong"], ans=0,
   why="EK LEG-2.B.5.d states that encroachment comes from neighboring states that SENSE GOVERNMENT WEAKNESS AND VULNERABILITY, so the external challenge is triggered by the internal ones. That is why the list mixes three internal items with one external one."),
 dict(q="Two parties, each representing a different national group, refuse to serve in government together, and no budget is passed for a year. Which of the framework's challenges does this illustrate?",
   choices=[
     "conflicting interests and competition among groups and political parties",
     "a perceived lack of governmental authority and legitimacy",
     "pressure for autonomy or secession",
     "encroachment of a neighboring state",
     "terrorism and civil war"], ans=0,
   why="EK LEG-2.B.5.a names conflicting interests and competition among groups and political parties, and EK LEG-2.B.1 states that cleavages affect party systems as well as voting behavior. Deadlock between two group-based parties is that challenge operating."),
 dict(q="Across several regions, citizens say the national government has no right to make decisions for them. Which of the framework's challenges does this illustrate?",
   choices=[
     "a perceived lack of governmental authority and legitimacy",
     "conflicting interests among political parties",
     "encroachment of a neighboring state",
     "civil war",
     "competition for natural resources between regions"], ans=0,
   why="EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy, and EK LEG-1.A.1 defines legitimacy as whether constituents believe their government has the right to use power as it does. Denial of that right is the challenge stated directly."),
 dict(q="An armed movement in one province proclaims independence and fighting spreads to neighbouring districts. Which of the framework's challenges does this illustrate?",
   choices=[
     "pressure for secession together with intergroup conflict and, if it continues, civil war",
     "conflicting interests among political parties",
     "a perceived lack of governmental authority alone",
     "encroachment of a neighboring state",
     "competition among groups for representation in the cabinet"], ans=0,
   why="EK LEG-2.B.5.c groups pressure for autonomy or secession with intergroup conflict, terrorism and civil war, and the scenario moves along that same sequence. EK LEG-2.B.4.a records that separatist movements have emerged in five of the six course countries."),
 dict(q="A neighboring state moves troops to the border after concluding that the government cannot control its own territory. Which of the framework's challenges does this illustrate?",
   choices=[
     "encroachment of a neighboring state that senses government weakness and vulnerability",
     "a perceived lack of governmental authority among the state's own citizens",
     "conflicting interests among the state's political parties",
     "pressure for autonomy from a regional movement",
     "the state's withdrawal from a supranational organization"], ans=0,
   why="EK LEG-2.B.5.d names encroachment of neighboring states that sense government weakness and vulnerability. The judgement that the government cannot control its territory is the sensed weakness the statement describes."),
 dict(q="A state facing all four of the framework's challenges at once would be experiencing",
   choices=[
     "three difficulties arising among its own groups, parties and citizens, and one arising from outside its borders",
     "four difficulties all arising from outside its borders",
     "four difficulties all arising among its own citizens",
     "two internal and two external difficulties",
     "one internal and three external difficulties"], ans=0,
   why="EK LEG-2.B.5.a, .b and .c concern a state's own parties, citizens and movements, while EK LEG-2.B.5.d names neighboring states. Three internal and one external is the composition of the framework's list."),
 dict(q="Why does the framework use the word 'perceived' in naming a lack of governmental authority and legitimacy as a challenge?",
   choices=[
     "because legitimacy is a matter of whether constituents believe the government has the right to use power as it does",
     "because governments in multinational states have no legal authority",
     "because the framework doubts that any government is legitimate",
     "because authority is conferred by other states rather than by citizens",
     "because the challenge arises only where a constitution is unwritten"], ans=0,
   why="EK LEG-1.A.1 defines legitimacy as whether a government's constituents believe it has the right to use power in the way they do, so a shortfall in legitimacy is by definition a matter of perception. EK PAU-1.A.4's sovereignty, by contrast, is a legal standing."),
 dict(q="A government facing pressure for autonomy from a national minority responds by creating an autonomous region with authority over language and education. Where does that response sit on the range the framework describes?",
   choices=[
     "at the recognition end, since creating autonomous regions is one of the framework's named accommodating measures",
     "at the brute repression end",
     "outside the framework's range of responses",
     "at the midpoint, since autonomy is neither recognition nor repression",
     "outside the range, since the framework describes only responses to violence"], ans=0,
   why="EK LEG-2.B.2.b states that state responses range from brute repression to recognition of ethnic and religious minorities and the creation of autonomous regions and/or representation of minorities in governmental institutions. The scenario names the framework's own accommodating measure."),
 dict(q="What does the framework say about the effect of cleavages on legitimacy?",
   choices=[
     "they can be used to strengthen legitimacy and hold onto power, and they may also lead to conflict and undermine legitimacy",
     "they always undermine legitimacy",
     "they always strengthen legitimacy",
     "they have no effect on legitimacy",
     "they affect legitimacy only in authoritarian regimes"], ans=0,
   why="EK LEG-2.B.3 states both halves in one statement: examples of the use of cleavages to strengthen legitimacy and hold onto power can be found in all course countries, and such cleavages may also lead to conflict and undermine legitimacy. EK LEG-1.B.3 adds that social conflicts can undermine legitimacy."),
 dict(q="In how many of the six course countries does the framework record that separatist movements have emerged?",
   choices=[
     "five",
     "two",
     "three",
     "four",
     "all six"], ans=0,
   why="EK LEG-2.B.4.a names China, Iran, Nigeria, Russia and the United Kingdom, which is five of the six. EK LEG-2.B.5.c makes pressure for autonomy or secession one of the challenges to stability in multinational states, so the two statements bear on each other directly."),
 dict(q="A government has closed the courts to a minority's grievances and barred its candidates from the ballot, and some of its members turn to violence. Which framework claim best explains that turn?",
   choices=[
     "violent political behavior becomes more likely when citizens feel that more conventional options for participation are ineffective or unavailable",
     "violent political behavior occurs only where a state is federal",
     "violent political behavior is unrelated to the availability of other options",
     "violent political behavior occurs only where neighboring states intervene",
     "violent political behavior always precedes a demand for autonomy"], ans=0,
   why="EK DEM-1.A.3 names citizens feeling that more conventional options for political participation are ineffective or unavailable among the conditions making violent political behavior more likely, and EK LEG-2.B.5.c places intergroup conflict and terrorism among the challenges to stability."),
 dict(q="In which three course countries does the framework describe state responses to separatist group violence, drug trafficking and discrimination based on gender or religious differences?",
   choices=[
     "Iran, Mexico and Nigeria",
     "China, Russia and the United Kingdom",
     "China, Iran and Russia",
     "Mexico, Nigeria and the United Kingdom",
     "all six course countries"], ans=0,
   why="EK LEG-1.C.1.b names state responses to separatist group violence, drug trafficking and discrimination based on gender or religious differences in Iran, Mexico and Nigeria. Both the trio of challenges and the trio of countries are the framework's."),
 dict(q="Why, on the framework's account, do state authorities try to limit the influence of divisive and violent actors?",
   choices=[
     "to attract more private capital and foreign direct investment and to improve economic growth",
     "to satisfy an obligation imposed by a neighboring state",
     "to increase the number of parties represented in the legislature",
     "to secure international recognition of their statehood",
     "to transfer authority from the national to the regional level"], ans=0,
   why="EK LEG-1.C.2 states that state authorities of different regime types attempt to limit the influence of divisive and violent actors in their countries to attract more private capital and foreign direct investment and to improve economic growth. The motive the framework gives is economic."),
 dict(q="How does the framework connect cleavages to a state's territorial arrangements?",
   choices=[
     "the degree to which power is centralized or decentralized often reflects a state's response to internal and external actors including ethnic cleavages",
     "cleavages have no bearing on how power is distributed among levels of government",
     "cleavages determine whether a state is recognized internationally",
     "cleavages determine the length of judicial terms",
     "cleavages determine whether a legislature has one chamber or two"], ans=0,
   why="EK PAU-2.A.2 states that the degree to which power is centralized or decentralized can change over time and in many cases reflects a state response to internal and external actors that include ethnic cleavages and the operations of supranational organizations and other countries."),
 dict(q="The table reports how often four challenges were recorded in a hypothetical sample of multinational states. Which challenge was reported by the largest number of states?",
   table=_T_CHAL,
   choices=[
     "conflicting interests and competition among groups and political parties, in 31 states",
     "pressure for autonomy or secession, in 22 states",
     "a perceived lack of governmental authority and legitimacy, in 18 states",
     "encroachment by a neighboring state, in 6 states",
     "the table does not report how many states reported each challenge"], ans=0,
   why="EK LEG-2.B.5 names all four of the table's rows as challenges to securing stability in multinational states, so the comparison stays inside the framework's own list. The first column reports the count directly, and each alternative states the true count for a different row."),
 dict(q="Using the same table, which challenge coincided with a fall in the government's approval in the largest SHARE of the states reporting it?",
   table=_T_CHAL,
   choices=[
     "a perceived lack of governmental authority and legitimacy, in 17 of the 18 states reporting it",
     "conflicting interests and competition among groups and political parties, in 12 states",
     "pressure for autonomy or secession, in 14 states",
     "encroachment by a neighboring state, in 5 states",
     "all four challenges equally"], ans=0,
   why="The question asks for a share, so each row's second figure must be divided by its first rather than compared as a count. EK LEG-1.A.1's definition of legitimacy as a belief of a government's constituents is why the row about perception should track approval most closely."),
 dict(q="According to the same table, the total number of states reporting one or more of the four challenges cannot be read directly, but the total number of REPORTS across the four rows is",
   table=_T_CHAL,
   choices=[
     "77",
     "48",
     "71",
     "55",
     "31"], ans=0,
   why="Adding the first numeric column across the four rows gives the number of reports. The alternatives arise from adding the second column, from dropping a row, from adding only some rows, and from reading the largest single row as though it were the total."),
 dict(q="The table describes four hypothetical cases. Which one illustrates the framework's challenge of conflicting interests and competition among groups and political parties?",
   table=_T_SCEN,
   choices=[
     "Case 1, in which two parties representing different groups refuse to govern together and no budget passes",
     "Case 2, in which citizens deny the government's right to decide for them",
     "Case 3, in which an armed movement declares independence",
     "Case 4, in which a neighboring state moves troops to the border",
     "None of the four, since that challenge cannot be observed"], ans=0,
   why="EK LEG-2.B.5.a names conflicting interests and competition among groups and political parties, and only one row describes party competition producing deadlock. The other rows state the framework's other three challenges."),
 dict(q="Using the same table, which case illustrates a perceived lack of governmental authority and legitimacy?",
   table=_T_SCEN,
   choices=[
     "Case 2, in which citizens across several regions deny that the national government has the right to decide for them",
     "Case 1, in which two parties refuse to govern together",
     "Case 3, in which an armed movement declares independence",
     "Case 4, in which a neighboring state moves troops to the border",
     "None of the four, since legitimacy is a legal standing rather than a belief"], ans=0,
   why="EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy, and EK LEG-1.A.1 defines legitimacy as whether constituents believe the government has the right to use power as it does. The rejected final option confuses legitimacy with EK PAU-1.A.4's sovereignty."),
 dict(q="Using the same table, which case describes the only one of the framework's four challenges that originates outside the state?",
   table=_T_SCEN,
   choices=[
     "Case 4, in which a neighboring state moves troops to the border after judging the government unable to control its territory",
     "Case 1, in which two parties refuse to govern together",
     "Case 2, in which citizens deny the government's right to decide",
     "Case 3, in which an armed movement declares independence",
     "None of the four, since all of the framework's challenges are internal"], ans=0,
   why="EK LEG-2.B.5.d is the only one of the four to name an actor outside the state, and it specifies neighboring states that sense government weakness and vulnerability. The other three arise among a state's own parties, citizens and movements."),
 dict(q="The table reports, for three hypothetical countries, how many of the framework's four challenges were recorded and the government's approval. Which conclusion does it support?",
   table=_T_STAB,
   choices=[
     "The more of the framework's challenges a country records, the lower its government's approval in this sample",
     "The more challenges a country records, the higher its government's approval",
     "Approval is the same in all three countries",
     "No country in the table records more than two challenges",
     "The table reports nothing about government approval"], ans=0,
   why="EK LEG-2.B.5 lists the four challenges as obstacles to securing stability, and EK LEG-1.B.3 states that serious problems including social conflicts can undermine legitimacy. Reading the two columns together, they move in opposite directions at every step."),
 dict(q="A commentator uses the same three countries to argue that the challenges caused the fall in approval. Which objection does the framework most directly support?",
   table=_T_STAB,
   choices=[
     "three paired observations show an association, and the framework denies that causation can be isolated and demonstrated with certainty from such evidence",
     "the two columns do not in fact move together, so there is nothing to explain",
     "the framework says approval is unrelated to challenges of any kind",
     "causation can be established only where a sample includes more than one region",
     "government approval cannot be measured"], ans=0,
   why="EK MPA-1.A.3 states that numerous variables potentially influence political outcomes with no way to isolate and demonstrate which is producing the change, and EK MPA-1.A.4 calls a co-movement an association. A government already unpopular for other reasons might also attract more of these challenges."),
 dict(q="Which evidence would most strongly support a claim that a multinational state faces the framework's second challenge rather than its first?",
   choices=[
     "Surveys across several groups show a majority denying that the national government has the right to make decisions binding on them",
     "Two parties in the legislature have failed to agree on a budget",
     "A neighbouring state has increased its military spending",
     "An armed movement has been reported in one province",
     "The government has created an autonomous region"], ans=0,
   why="EK LEG-2.B.5.b names a perceived lack of governmental authority and legitimacy and EK LEG-1.A.1 makes legitimacy a belief of a government's constituents, so the evidence must be about that belief. Legislative deadlock is EK LEG-2.B.5.a's challenge, and the remaining options are EK LEG-2.B.5.d, EK LEG-2.B.5.c and EK LEG-2.B.2.b's accommodating response."),
 dict(q="Which evidence would most strongly support a claim that a government's internal weakness has begun to attract external pressure?",
   choices=[
     "A neighbouring state has taken control of territory after publicly describing the government as unable to police its own borders",
     "A neighbouring state has signed a trade agreement with the government",
     "The government has joined an additional international organization",
     "An opposition party has criticized the government's foreign policy",
     "The government has increased spending on its diplomatic service"], ans=0,
   why="EK LEG-2.B.5.d describes the encroachment of neighboring states that sense government weakness and vulnerability, so the evidence must show both the encroachment and the perception of weakness. A trade agreement, treaty membership, domestic criticism and diplomatic spending show neither."),
 dict(q="Taking the framework's statement on challenges in multinational states as a whole, which summary is most accurate?",
   choices=[
     "Stability is threatened by competition among groups and parties, by a perceived lack of authority and legitimacy, and by pressure for autonomy that can escalate into conflict, terrorism and civil war, and those internal weaknesses can in turn invite encroachment by neighbouring states",
     "Stability is threatened only by outside powers, and internal divisions are irrelevant",
     "Stability is threatened only by internal divisions, and outside powers play no part",
     "Stability is threatened only where a state has no written constitution",
     "The framework names no challenges to stability in multinational states"], ans=0,
   why="EK LEG-2.B.5 lists four challenges, three of which are internal and the fourth of which, encroachment by neighboring states, is triggered by their sensing government weakness and vulnerability. The summary keeps that dependence between the internal three and the external one."),
]
