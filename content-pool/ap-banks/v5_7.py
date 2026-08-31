# AP U.S. GOVERNMENT AND POLITICS 5.7 Groups Influencing Policy Outcomes
# -- 30 questions
# CED V.1 (c) 2026, Unit 5 Political Participation.
# Learning objective 5.7.A: explain how VARIOUS POLITICAL ACTORS influence PUBLIC
# POLICY OUTCOMES.
# Suggested skill for this topic (CED p. 116): 1.E, concept application --
# explain how political principles, institutions, processes, policies, and
# behaviors apply to different scenarios in context.
#
# Essential knowledge relied on:
#   EK 5.7.A.1 -- "SINGLE-ISSUE GROUPS, IDEOLOGICAL OR SOCIAL MOVEMENTS, and
#     PROTEST MOVEMENTS form with the goal of AFFECTING SOCIETY AND
#     POLICYMAKING."
#   EK 5.7.A.2 -- "COMPETING ACTORS such as INTEREST GROUPS, PROFESSIONAL
#     ORGANIZATIONS, SOCIAL MOVEMENTS, THE MILITARY, and BUREAUCRATIC AGENCIES
#     influence policymaking, such as the FEDERAL BUDGET PROCESS, AT KEY STAGES
#     and TO VARYING DEGREES."
#   EK 5.7.A.3 -- "ELECTIONS AND POLITICAL PARTIES are related to MAJOR POLICY
#     SHIFTS OR INITIATIVES, OCCASIONALLY leading to POLITICAL REALIGNMENTS of
#     voting constituencies."
#
# EK 5.7.A.2'S LIST CROSSES THE LINE BETWEEN GOVERNMENT AND SOCIETY, and that is
# the thing to notice about it. Interest groups, professional organizations and
# social movements are outside government; THE MILITARY and BUREAUCRATIC
# AGENCIES are inside it. The framework calls all five COMPETING ACTORS in one
# breath, so the topic is not "how outside groups pressure government" -- it is
# how a set of actors, some of them parts of the government itself, compete over
# policy. A module that quietly dropped the two governmental actors would be
# answering a different and easier question. Items 8 to 15 carry all five, and
# the first table gives bureaucratic agencies and the military their own columns.
#
# TWO QUALIFIERS DO REAL WORK IN EK 5.7.A.2: AT KEY STAGES and TO VARYING
# DEGREES. Influence is not spread evenly across a process or across actors, and
# both phrases are droppable. The budget table is built so that the leading actor
# CHANGES from stage to stage, which is what "at key stages" means when it is
# turned into data, and item 27 makes that the correction.
#
# EK 5.7.A.3'S HEDGE IS "OCCASIONALLY". Elections and parties are RELATED TO
# major policy shifts, and only OCCASIONALLY lead to realignments of voting
# constituencies. The relation is stated flatly; the realignment is not. Turning
# the hedge into a rule -- every consequential election realigns the electorate
# -- is the error, and the second table is built with realignment following one
# election of four while policy initiatives follow all four.
#
# Documents the CED attaches to 5.7.A (p. 27): Federalist No. 10 (attached to
# 5.3.A through 5.7.A) and "Letter from a Birmingham Jail". Items 21 and 22
# quote them verbatim.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. No LaTeX:
# this is a prose subject and export_units.py no longer typesets US_GOV.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("5.7", "Groups Influencing Policy Outcomes", 5)

_BUDGET = ("A hypothetical study asked participants in the federal budget process which actor "
           "had the most influence at each stage. The table reports the share naming each.")
_BUDGET_TABLE = dict(
    headers=["Stage of the budget process", "Interest groups (%)",
             "Professional organizations (%)", "Bureaucratic agencies (%)", "The military (%)"],
    rows=[["Agency requests", "14", "9", "58", "19"],
          ["Executive proposal", "21", "12", "40", "27"],
          ["Committee markup", "44", "26", "18", "12"],
          ["Final passage", "38", "31", "17", "14"]])

_SHIFTS = ("A hypothetical study followed four elections, counting the major policy initiatives "
           "enacted in the two years after each and recording whether a realignment of voting "
           "constituencies was observed.")
_SHIFTS_TABLE = dict(
    headers=["Election", "Major policy initiatives enacted in the next two years",
             "Realignment of voting constituencies observed"],
    rows=[["Election 1", "7", "No"],
          ["Election 2", "3", "No"],
          ["Election 3", "9", "Yes"],
          ["Election 4", "5", "No"]])

QUESTIONS = [
 dict(q="According to the course framework, which three kinds of group form with the goal of affecting society and policymaking?",
   choices=[
     "Single-issue groups, ideological or social movements, and protest movements",
     "Political parties, interest groups, and elections",
     "Committees, agencies, and courts",
     "Professional organizations, the military, and bureaucratic agencies",
     "Primaries, caucuses, and conventions"], ans=0,
   why="EK 5.7.A.1 names exactly these three. The second option lists linkage institutions from EK 5.3.A.1 and the fourth lists three of the competing actors from EK 5.7.A.2, which is a different statement."),

 dict(q="According to EK 5.7.A.1, what goal do those groups form with?",
   choices=[
     "Affecting society and policymaking",
     "Winning control of a legislature",
     "Nominating candidates for office",
     "Raising money for political parties",
     "Filing amicus curiae briefs"], ans=0,
   why="EK 5.7.A.1's phrase is 'form with the goal of affecting society and policymaking', and both objects matter. A group aiming at society as well as at policy is not simply a smaller political party."),

 dict(q="Why does it matter that EK 5.7.A.1 names SOCIETY as well as policymaking among the goals?",
   choices=[
     "Because a movement may aim to change how people think and behave as well as to change what government does",
     "Because society and policymaking are the same thing",
     "Because the framework says such groups avoid policymaking",
     "Because it means these groups may not contact legislators",
     "Because it limits the groups to local activity"], ans=0,
   why="EK 5.7.A.1 lists two objects for the same goal, so a group on this list may pursue either or both. That is what distinguishes a social or protest movement from an organization whose entire object is a legislative outcome."),

 dict(q="What is a SINGLE-ISSUE GROUP, as EK 5.7.A.1 uses the term?",
   choices=[
     "A group organized around one question rather than a broad programme",
     "A group that supports only one candidate",
     "A group that exists for only one election",
     "A group with only one member",
     "A group that may act only once"], ans=0,
   why="EK 5.7.A.1 lists single-issue groups alongside broader ideological and social movements, so the contrast the term draws is one of scope. EK 5.6.A.1 makes the same distinction when it says interest groups may represent very specific or more general interests."),

 dict(q="How does EK 5.7.A.1's list relate to EK 5.6.A.1's account of interest groups?",
   choices=[
     "Both describe organized efforts to affect policy, and EK 5.6.A.1's very specific interests correspond closely to EK 5.7.A.1's single-issue groups",
     "The two statements describe unrelated phenomena",
     "EK 5.7.A.1 concerns government actors and EK 5.6.A.1 concerns private ones",
     "EK 5.6.A.1 says interest groups do not affect policy",
     "EK 5.7.A.1 replaces EK 5.6.A.1"], ans=0,
   why="EK 5.6.A.1 says interest groups may represent very specific or more general interests, and EK 5.7.A.1 names single-issue groups alongside broader movements. The two statements describe overlapping territory from different starting points."),

 dict(q="A movement organizes marches and public demonstrations to draw attention to a grievance and to press for a change in law. Which kind of group in EK 5.7.A.1 does this describe?",
   choices=[
     "A protest movement, which the framework lists among groups forming to affect society and policymaking",
     "A bureaucratic agency",
     "A professional organization",
     "A political party",
     "None of them, since demonstrations are not policymaking"], ans=0,
   why="EK 5.7.A.1 names protest movements among the three kinds of group, and the framework's stated goal covers affecting society and policymaking, which is what drawing attention and pressing for a change in law amount to."),

 dict(q="Which of the following does EK 5.7.A.1 NOT state?",
   choices=[
     "Which of the three kinds of group is most effective",
     "That single-issue groups form with the goal of affecting society and policymaking",
     "That ideological or social movements form with that goal",
     "That protest movements form with that goal",
     "That the goal includes affecting society"], ans=0,
   why="EK 5.7.A.1 names three kinds of group and one goal, and compares none of them. Every other option restates part of its single sentence."),

 dict(q="Which five COMPETING ACTORS does EK 5.7.A.2 name as influencing policymaking?",
   choices=[
     "Interest groups, professional organizations, social movements, the military, and bureaucratic agencies",
     "Interest groups, political parties, elections, media, and voters",
     "Single-issue groups, ideological movements, protest movements, parties, and elections",
     "Congress, the president, the courts, the states, and the people",
     "Primaries, caucuses, conventions, general elections, and the Electoral College"], ans=0,
   why="EK 5.7.A.2 lists exactly these five. The second option lists EK 5.3.A.1's linkage institutions and the third lists EK 5.7.A.1's three kinds of group, which is a separate statement in the same topic."),

 dict(q="What is notable about EK 5.7.A.2's list of competing actors?",
   choices=[
     "It includes actors inside government, the military and bureaucratic agencies, alongside actors outside it",
     "It includes only actors outside government",
     "It includes only actors inside government",
     "It includes only elected officials",
     "It includes only organizations with dues-paying members"], ans=0,
   why="Interest groups, professional organizations and social movements are outside government while the military and bureaucratic agencies are parts of it, and EK 5.7.A.2 calls all five competing actors in one sentence. The topic is therefore about competition over policy rather than about outside pressure on government."),

 dict(q="Why does it matter that EK 5.7.A.2 includes BUREAUCRATIC AGENCIES among the competing actors?",
   choices=[
     "Because it means parts of the government compete over policy alongside outside groups, rather than simply carrying out what others decide",
     "Because it means agencies are private organizations",
     "Because it means agencies do not implement policy",
     "Because it means only agencies influence policymaking",
     "Because it means agencies are a kind of interest group"], ans=0,
   why="EK 5.7.A.2 places agencies among actors that INFLUENCE policymaking, which is a role beyond implementation. EK 5.6.A.2's iron triangles describe one arrangement in which an agency, a committee and an interest group work together on a policy area."),

 dict(q="What example of policymaking does EK 5.7.A.2 itself name?",
   choices=[
     "The federal budget process",
     "The confirmation of judges",
     "The ratification of treaties",
     "The redrawing of legislative districts",
     "The certification of election results"], ans=0,
   why="EK 5.7.A.2 says these actors influence policymaking, 'such as the federal budget process'. Naming a process with identifiable stages is what makes the framework's next phrase, AT KEY STAGES, meaningful."),

 dict(q="According to EK 5.7.A.2, at what points and to what extent do these actors influence policymaking?",
   choices=[
     "At key stages and to varying degrees",
     "At every stage and to the same degree",
     "Only at the final stage and equally",
     "Only at the first stage and unequally",
     "The framework does not say"], ans=0,
   why="EK 5.7.A.2's own phrase is 'at key stages and to varying degrees'. Both qualifiers say influence is uneven, one across the process and one across the actors."),

 dict(q="What does the phrase AT KEY STAGES indicate about how influence operates in a process like the federal budget?",
   choices=[
     "That an actor may matter greatly at one point in the process and little at another",
     "That every actor matters equally throughout",
     "That only one stage of the process exists",
     "That influence is exercised only after a policy is adopted",
     "That the stages occur simultaneously"], ans=0,
   why="A process with stages allows an actor's influence to be concentrated rather than spread, which is what EK 5.7.A.2's phrase records. The budget table in this module shows the leading actor changing from stage to stage."),

dict(
   q="What does the phrase TO VARYING DEGREES add that AT KEY STAGES does not?",
   choices=[
     "That the actors differ from one another in how much influence they have, not only in when they have it",
     "That the stages occur in a fixed order",
     "That every actor is involved at every stage",
     "That influence cannot be measured",
     "That the framework ranks the five actors"], ans=0,
   why="AT KEY STAGES is about WHEN influence is exercised and TO VARYING DEGREES about HOW MUCH, so the two qualifiers describe unevenness along different dimensions. The framework states that the degrees vary without saying which actor has most."),

 dict(q="A federal agency, an interest group, and a professional organization all press for different provisions in one bill. Which framework statement does this illustrate?",
   choices=[
     "EK 5.7.A.2's competing actors influencing policymaking",
     "EK 5.7.A.1's three kinds of group forming to affect society and policymaking",
     "EK 5.7.A.3's relation between elections and major policy shifts",
     "EK 5.3.A.1's definition of a linkage institution",
     "EK 5.5.A.1's winner-take-all voting districts"], ans=0,
   why="Three of EK 5.7.A.2's five named actors are pressing in different directions on one measure, which is the competition the statement describes. The framework's word COMPETING is what the scenario supplies."),

 dict(q="According to EK 5.7.A.3, what are elections and political parties related to?",
   choices=[
     "Major policy shifts or initiatives",
     "The rules governing voter registration",
     "The structure of the federal courts",
     "The number of seats in the House",
     "The dates on which agencies publish regulations"], ans=0,
   why="EK 5.7.A.3 states this directly. The relation to policy shifts is stated flatly, unlike the realignment clause that follows it."),

 dict(q="According to EK 5.7.A.3, how often do elections and parties lead to political realignments of voting constituencies?",
   choices=[
     "Occasionally",
     "Always",
     "In every presidential election",
     "Never",
     "The framework does not say"], ans=0,
   why="EK 5.7.A.3's own word is OCCASIONALLY. It hedges the realignment clause while leaving the relation to major policy shifts unhedged, so the two halves of the sentence are not equally strong."),

 dict(q="Why does the difference between EK 5.7.A.3's two halves matter?",
   choices=[
     "Because the relation to major policy shifts is stated flatly while the realignment is stated as occasional, so evidence of a policy shift is not evidence of a realignment",
     "Because the two halves contradict each other",
     "Because realignments occur more often than policy shifts",
     "Because the framework says elections have no effect",
     "Because policy shifts and realignments are the same event"], ans=0,
   why="EK 5.7.A.3 says elections and parties ARE RELATED TO major policy shifts and only OCCASIONALLY lead to realignments, so the second is rarer than the first by the framework's own wording. Treating a policy shift as a realignment collapses a distinction the sentence draws."),

 dict(q="What is a POLITICAL REALIGNMENT of voting constituencies?",
   choices=[
     "A change in which groups of voters support which party",
     "A change in the boundaries of legislative districts",
     "A change in the number of parties on the ballot",
     "A change in the date of an election",
     "A change in the rules for registering to vote"], ans=0,
   why="EK 5.7.A.3 refers to realignments of voting CONSTITUENCIES, and EK 5.4.A.3.i defines a critical election as one in which there is a realignment of political party support among voters. Redistricting changes boundaries rather than which groups support which party."),

 dict(q="How does EK 5.7.A.3 relate to EK 5.4.A.3.i's account of critical elections?",
   choices=[
     "Both concern a realignment of party support among voters, one as an occasional consequence of elections and the other as what defines a critical election",
     "The two statements describe unrelated events",
     "EK 5.4.A.3.i says realignments never occur",
     "EK 5.7.A.3 defines a critical election",
     "EK 5.4.A.3.i concerns districts rather than voters"], ans=0,
   why="EK 5.4.A.3.i defines a critical election by a realignment of political party support among voters, and EK 5.7.A.3 says elections occasionally lead to political realignments of voting constituencies. The same phenomenon appears in two statements with different jobs."),

 dict(q="Read the following excerpt.\n\n“The most common and durable source of factions has been the various and unequal distribution of property. Those who hold and those who are without property have ever formed distinct interests in society.”\n—James Madison, Federalist No. 10, 1787\n\nHow does this passage relate to EK 5.7.A.2's competing actors?",
   choices=[
     "It treats competition among distinct interests as a permanent feature of society, which is the condition in which the framework's competing actors operate",
     "It argues that only one interest should be represented in policymaking",
     "It states that competing actors should be prohibited",
     "It concerns the military and bureaucratic agencies specifically",
     "It has no bearing on policymaking"], ans=0,
   why="Madison identifies distinct and durable interests arising from the distribution of property, and EK 5.7.A.2 describes actors competing over policy. The CED attaches Federalist No. 10 to 5.7.A, and the essay supplies the background condition for the competition the framework describes."),

 dict(q="Read the following excerpt.\n\n“We know through painful experience that freedom is never voluntarily given by the oppressor; it must be demanded by the oppressed.”\n—Martin Luther King, Jr., “Letter from a Birmingham Jail,” 1963\n\nWhich of EK 5.7.A.1's three kinds of group does this argument most directly speak for?",
   choices=[
     "Protest movements, which form with the goal of affecting society and policymaking",
     "Professional organizations",
     "Bureaucratic agencies",
     "Political parties",
     "The military"], ans=0,
   why="The passage argues that change follows demand from those seeking it, which is the premise of organized protest, and EK 5.7.A.1 names protest movements among groups forming to affect society and policymaking. The CED attaches the Letter to 5.7.A."),

 dict(q="A professional organization of licensed practitioners submits technical comments on a proposed regulation, and a federal agency revises the regulation in response. Which framework statement does this illustrate?",
   choices=[
     "EK 5.7.A.2's competing actors, with a professional organization and a bureaucratic agency both named on its list",
     "EK 5.7.A.1's protest movements",
     "EK 5.7.A.3's relation between elections and policy shifts",
     "EK 5.5.A.2's incorporation of third-party agendas",
     "EK 5.1.B.1's models of voting behavior"], ans=0,
   why="Professional organizations and bureaucratic agencies are two of the five actors EK 5.7.A.2 names, and the scenario has one influencing the other's decision. Nothing here involves an election, a protest or a party platform."),

 dict(q="Which statement best summarizes what LO 5.7.A asks students to explain?",
   choices=[
     "How a range of actors, some inside government and some outside it, shape what policy is finally adopted",
     "How voters decide which candidate to support",
     "How states administer their elections",
     "How the Supreme Court decides constitutional questions",
     "How campaign finance law is enforced"], ans=0,
   why="LO 5.7.A's own phrase is how VARIOUS POLITICAL ACTORS influence PUBLIC POLICY OUTCOMES, and EK 5.7.A.2's list spans government and society. The other four options describe subjects of other topics in this unit and in Unit 2."),

 dict(q=_BUDGET + " Which conclusion is best supported by the data?",
   table=_BUDGET_TABLE,
   choices=[
     "Bureaucratic agencies are named most often at the first two stages and interest groups at the last two, so the leading actor changes across the process",
     "Interest groups are named most often at every stage",
     "Bureaucratic agencies are named most often at every stage",
     "The four actors are named by similar shares at every stage",
     "The military is named most often at the final stage"], ans=0,
   why="Agencies lead at 58 and 40 percent in the first two rows and interest groups at 44 and 38 in the last two. The military peaks at 27 percent in the executive proposal stage and leads nowhere."),

 dict(q=_BUDGET + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_BUDGET_TABLE,
   choices=[
     "EK 5.7.A.2's competing actors influencing policymaking, such as the federal budget process, at key stages and to varying degrees",
     "EK 5.7.A.1's three kinds of group forming to affect society and policymaking",
     "EK 5.7.A.3's relation between elections and major policy shifts",
     "EK 5.6.B.1's inequality of interest group resources",
     "EK 5.3.B.1's functions of political parties"], ans=0,
   why="The table's rows are stages of the federal budget process, which EK 5.7.A.2 names as its own example, and its columns are four of the five actors that statement lists. The changing leader across rows is the phrase AT KEY STAGES in observable form."),

 dict(q=_BUDGET + " A student concludes from this table that one actor dominates the federal budget process. What is the most important correction?",
   table=_BUDGET_TABLE,
   choices=[
     "Which actor is named most often changes from stage to stage, which is what the framework's phrase AT KEY STAGES describes",
     "The same actor is named most often at every stage",
     "The table reports no figures for bureaucratic agencies",
     "The four actors are named by equal shares at every stage",
     "The table covers a single stage, so no comparison is possible"], ans=0,
   why="Bureaucratic agencies lead the first two rows and interest groups the last two, so no actor leads throughout. EK 5.7.A.2's two qualifiers say influence is uneven across stages and across actors, which is precisely what a claim of domination misses."),

 dict(q=_SHIFTS + " Which conclusion is best supported by the data?",
   table=_SHIFTS_TABLE,
   choices=[
     "Major policy initiatives followed every election in the table, while a realignment was observed after only one of the four",
     "A realignment was observed after every election",
     "No election was followed by any major policy initiative",
     "The election followed by the fewest initiatives is the one after which a realignment was observed",
     "Realignments were observed after three of the four elections"], ans=0,
   why="The initiative counts are 7, 3, 9 and 5, all above zero, and the realignment column reads No, No, Yes, No. The election followed by a realignment is the one with the most initiatives at 9, not the fewest."),

 dict(q=_SHIFTS + " Which statement in the course framework does this pattern most directly illustrate?",
   table=_SHIFTS_TABLE,
   choices=[
     "EK 5.7.A.3's statement that elections and parties are related to major policy shifts, occasionally leading to political realignments",
     "EK 5.7.A.2's competing actors at key stages",
     "EK 5.7.A.1's three kinds of group",
     "EK 5.6.A.1's activities of interest groups",
     "EK 5.2.A.2's influences on voter turnout"], ans=0,
   why="The table's two data columns are exactly the two halves of EK 5.7.A.3: policy initiatives following elections, and realignment occurring occasionally. Their different frequencies are the difference between the sentence's flat clause and its hedged one."),

 dict(q=_SHIFTS + " A student concludes that an election producing major policy initiatives has thereby produced a realignment. What is the most important correction?",
   table=_SHIFTS_TABLE,
   choices=[
     "All four elections were followed by initiatives and only one by a realignment, which is why the framework says elections lead to realignments only occasionally",
     "No election in the table was followed by any initiative",
     "Every election in the table was followed by a realignment",
     "The table does not report realignments",
     "The table covers a single election, so no comparison is possible"], ans=0,
   why="Three of the four elections produced initiatives without a realignment, so the first does not imply the second. EK 5.7.A.3 states the relation to policy shifts flatly and hedges the realignment with OCCASIONALLY, and the table separates the two."),
]
