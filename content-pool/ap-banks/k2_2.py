# AP COMPARATIVE GOVERNMENT AND POLITICS 2.2 Comparing Parliamentary,
# Presidential, and Semi-Presidential Systems
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.B (compare institutional relations among
# parliamentary, presidential, and semi-presidential systems). Suggested skill
# 2.C, Country Comparison.
#
# Essential knowledge relied on:
#   PAU-3.B.1  ALTHOUGH parliamentary systems have FEWER INSTITUTIONAL OBSTACLES to
#              enact policy than presidential systems (presidential systems have
#              DIVIDED BRANCH POWERS), parliamentary systems HAVE THEIR OWN CHECKS
#              ON THE EXECUTIVE BRANCH
#   PAU-3.B.2  parliaments may CENSURE CABINET MINISTERS, REFUSE TO PASS EXECUTIVE
#              PROPOSED LEGISLATION, QUESTION the executive and cabinet ministers,
#              and IMPOSE TIME DEADLINES ON CALLING NEW ELECTIONS
#
# The second clause of PAU-3.B.1 is the half students drop, and the framework
# writes it as a concession ('although ... have their own checks'). Items 3, 9, 22
# and 26 key that clause rather than the headline comparison, because a student
# who keeps only the first half concludes that a parliamentary executive is
# unchecked, which the sentence expressly denies (AP_COMP_GOV_CED.md note 11).
#
# Supporting statements, each named in the verifier's claim:
#   PAU-3.A.1-3 the three definitions, for the routes to office and removal
#   PAU-3.D.1  across the course countries, executive leaders can be removed by the
#              legislative branch through different procedures that control the
#              abuse of power
#   PAU-3.E.1c Mexico's Senate confirms Supreme Court appointments, approves
#              treaties, and approves federal intervention in state matters
#   PAU-3.E.1d Nigeria's Senate possesses unique impeachment and confirmation powers
#   PAU-3.E.1e Russia's Duma passes legislation and confirms the prime minister; an
#              appointed Federation Council approves budget legislation, treaties,
#              judicial nominees and troop deployment
#   PAU-3.E.1f the United Kingdom's appointed House of Lords reviews and amends
#              Commons bills, effectively delaying implementation as a power check
#   PAU-3.F.2  legislatures can reinforce legitimacy and stability by responding to
#              public demand, openly debating policy, facilitating compromise
#              between factions, extending civil liberties, and restricting the
#              power of the executive
#
# Table figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.2", "Comparing Parliamentary, Presidential, and Semi-Presidential Systems", 2)

_T_OBST = dict(
    headers=["System type (hypothetical sample of cases)",
             "Executive-proposed bills that became law (percent)",
             "Median months from proposal to enactment",
             "Executive-proposed bills defeated by the legislature (percent)"],
    rows=[["Parliamentary cases", "88", "7", "6"],
          ["Presidential cases", "54", "19", "24"],
          ["Semi-presidential cases", "67", "13", "15"]])

_T_CHECK = dict(
    headers=["Parliamentary check on the executive", "Episodes recorded (hypothetical)",
             "Episodes in which the executive afterwards changed its position"],
    rows=[["Censure of a cabinet minister", "12", "7"],
          ["Refusal to pass executive-proposed legislation", "31", "22"],
          ["Questioning of the executive and cabinet ministers", "210", "18"],
          ["Imposition of a time deadline for calling new elections", "5", "4"]])

QUESTIONS = [
 dict(q="What does the framework say about the institutional obstacles to enacting policy in parliamentary and presidential systems?",
   choices=[
     "Parliamentary systems have fewer institutional obstacles to enacting policy than presidential systems",
     "Presidential systems have fewer institutional obstacles to enacting policy than parliamentary systems",
     "The two types face identical institutional obstacles",
     "Neither type faces any institutional obstacle to enacting policy",
     "The framework declines to compare the two types on this point"], ans=0,
   why="EK PAU-3.B.1 states that parliamentary systems have fewer institutional obstacles to enact policy than presidential systems. The comparison runs in that direction, and reversing it is the most common misreading of the sentence."),
 dict(q="What reason does the framework give, in the same sentence, for presidential systems facing more institutional obstacles?",
   choices=[
     "presidential systems have divided branch powers",
     "presidential systems hold elections more frequently",
     "presidential legislatures are always bicameral",
     "presidential systems lack a written constitution",
     "presidential systems have larger cabinets"], ans=0,
   why="EK PAU-3.B.1 supplies the reason parenthetically: presidential systems have divided branch powers. EK PAU-3.A.2's separate fixed-term elections and a cabinet responsible to the executive rather than the legislature are what that division consists of."),
 dict(q="Which clause completes the framework's comparison of the two types?",
   choices=[
     "parliamentary systems have their own checks on the executive branch",
     "parliamentary systems place no checks at all on the executive branch",
     "presidential systems place no checks on the executive branch",
     "neither type places any check on the executive branch",
     "checks on the executive exist only where the state is federal"], ans=0,
   why="EK PAU-3.B.1 is written as a concession: although parliamentary systems have fewer institutional obstacles, they have their own checks on the executive branch. Dropping that clause turns the sentence into a claim the framework explicitly refuses to make."),
 dict(q="Which set of powers does the framework name as parliamentary checks on the executive?",
   choices=[
     "censuring cabinet ministers, refusing to pass executive-proposed legislation, questioning the executive and ministers, and imposing time deadlines on calling new elections",
     "impeaching the head of state and appointing the judiciary",
     "vetoing legislation and dissolving the courts",
     "certifying election results and drawing constituency boundaries",
     "declaring war and ratifying treaties"], ans=0,
   why="EK PAU-3.B.2 lists exactly these four. They are the content of EK PAU-3.B.1's claim that parliamentary systems have their own checks, and none of them requires the separation of branches that a presidential system supplies."),
 dict(q="A parliament passes a motion formally condemning a minister's conduct in office. Which of the framework's named parliamentary checks does this illustrate?",
   choices=[
     "censure of a cabinet minister",
     "refusal to pass executive-proposed legislation",
     "questioning of the executive and cabinet ministers",
     "imposition of a time deadline for calling new elections",
     "impeachment of the head of state"], ans=0,
   why="EK PAU-3.B.2 names censuring cabinet ministers among the parliamentary checks on the executive. A formal motion of condemnation is that check; the other named checks concern legislation, interrogation and the election timetable."),
 dict(q="A governing executive's flagship bill is voted down by the chamber that sustains it in office. Which of the framework's named parliamentary checks does this illustrate?",
   choices=[
     "refusal to pass executive-proposed legislation",
     "censure of a cabinet minister",
     "questioning of the executive and cabinet ministers",
     "imposition of a time deadline for calling new elections",
     "impeachment of a cabinet minister"], ans=0,
   why="EK PAU-3.B.2 names refusing to pass executive-proposed legislation among the parliamentary checks. EK PAU-3.B.1's concession is precisely that a system with fewer institutional obstacles still contains checks of this kind."),
 dict(q="Ministers are required to appear before the chamber at fixed intervals and answer members' questions on the record. Which of the framework's named parliamentary checks does this illustrate?",
   choices=[
     "questioning of the executive and cabinet ministers",
     "censure of a cabinet minister",
     "refusal to pass executive-proposed legislation",
     "imposition of a time deadline for calling new elections",
     "judicial review of executive action"], ans=0,
   why="EK PAU-3.B.2 names questioning the executive and cabinet ministers among the parliamentary checks on the executive. EK PAU-3.F.2 adds openly debating policy among the ways legislatures reinforce legitimacy and stability, which such questioning serves."),
 dict(q="A parliament sets a fixed period within which the executive must call the next general election. Which of the framework's named parliamentary checks does this illustrate?",
   choices=[
     "imposition of a time deadline for calling new elections",
     "censure of a cabinet minister",
     "refusal to pass executive-proposed legislation",
     "questioning of the executive and cabinet ministers",
     "confirmation of judicial nominees"], ans=0,
   why="EK PAU-3.B.2 names imposing time deadlines on calling new elections among the parliamentary checks. The power matters because EK PAU-3.C.2.f gives a prime minister the ability to call elections, and a deadline limits the executive's freedom to time that decision."),
 dict(q="A student concludes from the framework that a parliamentary executive faces no checks because its own majority sustains it. The best correction is that",
   choices=[
     "the framework states in the same sentence that parliamentary systems have their own checks on the executive branch, and names four of them",
     "the framework states that parliamentary systems have more institutional obstacles than presidential systems",
     "the framework says checks on the executive exist only in presidential systems",
     "the framework says a parliamentary majority can never be divided",
     "the framework does not discuss checks on the executive at all"], ans=0,
   why="EK PAU-3.B.1 is a concession sentence whose second clause says parliamentary systems have their own checks on the executive branch, and EK PAU-3.B.2 lists censure, refusal of legislation, questioning and election deadlines. The student has kept the first clause and dropped the second."),
 dict(q="A second student concludes that presidential systems can enact policy more quickly because a single elected leader is both head of state and head of government. What is wrong with this?",
   choices=[
     "The framework says the opposite about obstacles, attributing FEWER of them to parliamentary systems because presidential systems have divided branch powers",
     "The framework says presidential systems have no head of government",
     "The framework says presidential legislatures cannot pass laws",
     "The framework says parliamentary systems have divided branch powers",
     "The framework does not identify who serves as head of government in presidential systems"], ans=0,
   why="EK PAU-3.B.1 assigns fewer institutional obstacles to parliamentary systems and attributes the presidential system's obstacles to divided branch powers. EK PAU-3.A.2's fusion of head of state and head of government does not remove the separation between the executive and a separately elected legislature."),
 dict(q="Which feature of presidential systems most directly produces the divided branch powers the framework names?",
   choices=[
     "the legislature is popularly elected to its own fixed term and the executive is elected separately, so neither owes its office to the other",
     "the legislature selects the executive from among its members",
     "the executive may dissolve the legislature at will",
     "the cabinet is accountable to the legislature by ordinary vote",
     "the head of state is ceremonial"], ans=0,
   why="EK PAU-3.A.2 gives presidential systems separate fixed-term popular elections for the national legislature alongside a separately chosen executive, which is what EK PAU-3.B.1 means by divided branch powers. The rejected options describe the parliamentary arrangement of EK PAU-3.A.1."),
 dict(q="Which feature of a semi-presidential system creates an institutional obstacle that a purely presidential system does not have?",
   choices=[
     "the president's nominee for prime minister must be approved by the legislature",
     "the legislature is popularly elected",
     "the president is popularly elected",
     "the cabinet exists at all",
     "the head of state and head of government are the same person"], ans=0,
   why="EK PAU-3.A.3 requires the president's nominee for prime minister to be approved by the legislature and makes cabinet members accountable to both branches, which is an approval step EK PAU-3.A.2's presidential type does not contain. Popular election of both branches is common to the two types."),
 dict(q="Which comparison of how an executive can be removed across the three types is consistent with the framework?",
   choices=[
     "In a parliamentary system the legislature may select and remove the head of government; in a presidential system the legislature may reach cabinet members only through impeachment; in a semi-presidential system the cabinet answers to both branches",
     "In all three types the legislature may remove the executive by ordinary vote",
     "In none of the three types may the legislature remove any member of the executive",
     "Only in presidential systems may the legislature remove the head of government",
     "Removal procedures are identical across the six course countries"], ans=0,
   why="EK PAU-3.A.1, EK PAU-3.A.2 and EK PAU-3.A.3 supply the three arrangements, and EK PAU-3.D.1 states that across the course countries executive leaders can be removed by the legislative branch through different procedures that control the abuse of power. The framework's word is 'different'."),
 dict(q="The framework describes the United Kingdom's appointed upper chamber as reviewing and amending bills from the elected chamber, effectively delaying implementation. This is best understood as",
   choices=[
     "a check on the executive operating inside a parliamentary system",
     "evidence that the United Kingdom is a presidential system",
     "a power to veto legislation permanently",
     "a power to remove the prime minister from office",
     "a form of judicial review of executive action"], ans=0,
   why="EK PAU-3.E.1.f states that the appointed House of Lords reviews and amends bills from the Commons, effectively delaying implementation as a power check, and EK PAU-3.B.1 says parliamentary systems have their own checks on the executive branch. Delay is not a veto, and the chamber does not remove the head of government."),
 dict(q="Mexico's Senate confirms presidential appointments to the Supreme Court and approves treaties. Within this topic's comparison, these powers are best described as",
   choices=[
     "checks arising from the divided branch powers the framework attributes to presidential systems",
     "checks of the kind the framework lists as distinctively parliamentary",
     "evidence that Mexico is a semi-presidential system",
     "powers that allow the Senate to remove the president by ordinary vote",
     "powers exercised by an appointed rather than an elected chamber"], ans=0,
   why="EK PAU-3.E.1.c gives Mexico's elected Senate the unique power to confirm presidential appointments to the Supreme Court, approve treaties and approve federal intervention in state matters, and EK PAU-3.B.1 attributes divided branch powers to presidential systems. EK PAU-3.A.2 places Mexico in that type."),
 dict(q="Which powers does the framework assign uniquely to Nigeria's Senate?",
   choices=[
     "impeachment and confirmation powers",
     "the power to select and remove the head of government",
     "the power to nominate the prime minister",
     "the power to review and amend bills only, delaying their implementation",
     "the power to approve troop deployment and judicial nominees"], ans=0,
   why="EK PAU-3.E.1.d states that both chambers of Nigeria's National Assembly hold the power to approve legislation and that the Senate possesses unique impeachment and confirmation powers. The rejected options describe the parliamentary route of EK PAU-3.A.1, the semi-presidential route of EK PAU-3.A.3, the Lords of EK PAU-3.E.1.f and the Federation Council of EK PAU-3.E.1.e."),
 dict(q="Which description of the two chambers of Russia's legislature is consistent with the framework?",
   choices=[
     "an elected Duma that passes legislation and confirms the prime minister, and an appointed Federation Council that approves budget legislation, treaties, judicial nominees and troop deployment",
     "an elected Duma that appoints the president, and an elected Federation Council that passes all legislation",
     "two appointed chambers, neither of which has any role in legislation",
     "a single elected chamber that both passes legislation and selects the head of government",
     "an appointed Duma and an elected Federation Council"], ans=0,
   why="EK PAU-3.E.1.e describes Russia's bicameral system in exactly these terms. The confirmation of the prime minister by the elected chamber is what EK PAU-3.A.3's semi-presidential definition requires, so the two statements fit together."),
 dict(q="According to the framework, legislatures have the potential to reinforce legitimacy and stability by",
   choices=[
     "responding to public demand, openly debating policy, facilitating compromise between factions, extending civil liberties, and restricting the power of the executive",
     "deferring to the executive on all questions of policy",
     "meeting in closed session to avoid public disagreement",
     "delegating their lawmaking power to the cabinet",
     "extending the term of the head of government"], ans=0,
   why="EK PAU-3.F.2 lists exactly these five ways in which legislatures can reinforce legitimacy and stability. The last of them, restricting the power of the executive, is the same function EK PAU-3.B.1 and EK PAU-3.B.2 describe from the comparative side."),
 dict(q="Which check on the executive belongs to the framework's presidential account rather than to its list of parliamentary checks?",
   choices=[
     "removal of cabinet members through impeachment",
     "censure of a cabinet minister",
     "refusal to pass executive-proposed legislation",
     "questioning of the executive and cabinet ministers",
     "imposition of a time deadline for calling new elections"], ans=0,
   why="EK PAU-3.A.2 makes impeachment the route by which a presidential legislature may remove cabinet members, while EK PAU-3.B.2's list of parliamentary checks comprises censure, refusal of legislation, questioning and election deadlines. The four rejected options are that list."),
 dict(q="The table reports hypothetical figures for three groups of cases. Which conclusion is most consistent with the framework's comparison of institutional obstacles?",
   table=_T_OBST,
   choices=[
     "The parliamentary cases enact the largest share of executive-proposed bills, do so in the shortest median time, and lose the smallest share to defeat",
     "The presidential cases enact the largest share of executive-proposed bills",
     "The three groups enact the same share of executive-proposed bills",
     "The semi-presidential cases take the longest median time from proposal to enactment",
     "No group defeats any executive-proposed bill"], ans=0,
   why="EK PAU-3.B.1 states that parliamentary systems have fewer institutional obstacles to enacting policy than presidential systems, and all three columns move together in the table. The group with fewest obstacles should lead on passage, on speed and on avoiding defeat, which is what one row does."),
 dict(q="Using the same table, the gap between the parliamentary and presidential groups in the share of executive-proposed bills that became law is",
   table=_T_OBST,
   choices=[
     "34 percentage points",
     "21 percentage points",
     "13 percentage points",
     "18 percentage points",
     "12 percentage points"], ans=0,
   why="Subtracting the presidential group's passage share from the parliamentary group's gives the gap. The alternatives are the gaps between other pairs of rows in the same column, or gaps taken from a different column, so the item turns on reading the right two cells."),
 dict(q="A student concludes from the same table that a parliamentary executive is not checked at all. Which objection combines the framework and the data most directly?",
   table=_T_OBST,
   choices=[
     "The framework says parliamentary systems have their own checks on the executive, and the table shows some executive-proposed bills being defeated even in the parliamentary cases",
     "The table shows no executive-proposed bills being defeated in the parliamentary cases",
     "The framework says parliamentary systems have more institutional obstacles than presidential systems",
     "The table reports nothing about the fate of executive-proposed bills",
     "Checks on the executive cannot be measured by any table"], ans=0,
   why="EK PAU-3.B.1's second clause states that parliamentary systems have their own checks on the executive branch, and EK PAU-3.B.2 names four. The parliamentary row's defeat share is small but not zero, so the data agree with the framework rather than with the student."),
 dict(q="The table reports hypothetical episodes of the four parliamentary checks the framework names. Which check was used most often?",
   table=_T_CHECK,
   choices=[
     "questioning of the executive and cabinet ministers, with 210 episodes",
     "refusal to pass executive-proposed legislation, with 31 episodes",
     "censure of a cabinet minister, with 12 episodes",
     "imposition of a time deadline for calling new elections, with 5 episodes",
     "the table does not report how often each check was used"], ans=0,
   why="EK PAU-3.B.2 names all four checks recorded in the table, and the episode column reports how often each was used. One row is larger than the other three combined, which is what makes it the most frequently used."),
 dict(q="Using the same table, which check was followed by a change in the executive's position in the largest SHARE of its episodes?",
   table=_T_CHECK,
   choices=[
     "imposition of a time deadline for calling new elections, in four of five episodes",
     "questioning of the executive and cabinet ministers, in 18 episodes",
     "refusal to pass executive-proposed legislation, in 22 episodes",
     "censure of a cabinet minister, in seven episodes",
     "all four checks equally, since each was followed by some change of position"], ans=0,
   why="The question asks for a share rather than a count, so each row's second figure must be divided by its first. The rejected options quote raw counts, two of which are larger than the keyed row's count while representing much smaller shares of their own totals."),
 dict(q="Which conclusion about the four checks does the same table support?",
   table=_T_CHECK,
   choices=[
     "The check used most often was followed by a change in the executive's position in the smallest share of its episodes, so how often a check is used is not a measure of how much it moves the executive",
     "The check used most often was also the one most often followed by a change of position",
     "The check used least often was never followed by a change of position",
     "Every episode of every check was followed by a change of position",
     "No episode of any check was followed by a change of position"], ans=0,
   why="EK PAU-3.B.2 lists the four checks without ranking them, and reading the table as proportions rather than counts separates frequency from effect. The most frequently recorded check has by far the lowest proportion of episodes followed by a change of position."),
 dict(q="Which statement best captures the trade-off the framework describes between the two types?",
   choices=[
     "A parliamentary executive faces fewer institutional obstacles to enacting policy but is subject to checks its own legislature exercises, whereas a presidential executive faces obstacles arising from divided branch powers",
     "A parliamentary executive faces more institutional obstacles and fewer checks than a presidential executive",
     "Both executives face identical obstacles and identical checks",
     "A presidential executive faces neither obstacles nor checks",
     "A parliamentary executive faces no obstacles and no checks"], ans=0,
   why="EK PAU-3.B.1 combines both halves in one sentence, fewer institutional obstacles for parliamentary systems because presidential systems have divided branch powers, and their own checks on the executive branch nonetheless. Keeping only one half produces each of the rejected options."),
 dict(q="An executive's legislative programme is blocked because the upper chamber, elected separately and controlled by a rival party, refuses to confirm the appointments needed to implement it. Which of the framework's descriptions does this best illustrate?",
   choices=[
     "the divided branch powers the framework attributes to presidential systems",
     "the parliamentary check of censuring a cabinet minister",
     "the parliamentary check of imposing a time deadline for calling new elections",
     "the combination of lawmaking and executive functions",
     "the accountability of the cabinet to both president and legislature"], ans=0,
   why="EK PAU-3.B.1 attributes divided branch powers to presidential systems, and EK PAU-3.A.2's separately elected fixed-term legislature is what allows a rival majority to sit opposite the executive. EK PAU-3.E.1.c and EK PAU-3.E.1.d give confirmation powers to the upper chambers of the framework's two presidential cases."),
 dict(q="Why does the power to impose a time deadline for calling new elections count as a check on the executive?",
   choices=[
     "because an executive that can choose when to face the voters gains an advantage that a deadline removes",
     "because it allows the legislature to remove the head of state",
     "because it transfers the conduct of elections to the courts",
     "because it prevents any election from being held",
     "because it requires the executive to resign after every election"], ans=0,
   why="EK PAU-3.B.2 names imposing time deadlines on calling new elections among the parliamentary checks, and EK PAU-3.C.2.f gives a prime minister the power to call elections. A deadline constrains the timing of that decision without touching the head of state, the courts or the holding of elections."),
 dict(q="Which finding would most strongly support a claim that a particular parliamentary executive is effectively checked by its legislature?",
   choices=[
     "Ministers have been censured, several executive bills have been defeated, and question sessions have repeatedly forced changes of policy",
     "The governing party holds a large majority in the chamber",
     "The executive has introduced a large number of bills",
     "The legislature meets for more days each year than it used to",
     "The head of state has made several official visits abroad"], ans=0,
   why="EK PAU-3.B.2 names censure, refusal to pass executive-proposed legislation and questioning among the parliamentary checks, and the keyed finding reports all three actually being used. A large majority, a heavy legislative programme, sitting days and ceremonial activity say nothing about whether the executive was constrained."),
 dict(q="Taking the framework's two statements in this topic together, which summary is most accurate?",
   choices=[
     "Parliamentary systems face fewer institutional obstacles than presidential systems, whose branch powers are divided, but parliaments check their executives through censure, refusal of legislation, questioning and deadlines on calling elections",
     "Parliamentary systems face more obstacles than presidential systems and check their executives in the same ways",
     "Neither type places checks on the executive, and the difference between them is only in how the head of state is titled",
     "Presidential systems face fewer obstacles because their branch powers are combined",
     "The framework compares the two types only by the number of chambers in their legislatures"], ans=0,
   why="EK PAU-3.B.1 supplies the comparison and its concession, and EK PAU-3.B.2 supplies the four checks that give the concession content. The summary keeps both halves, which is what the framework's 'although' construction requires."),
]
