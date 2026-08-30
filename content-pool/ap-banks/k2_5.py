# AP COMPARATIVE GOVERNMENT AND POLITICS 2.5 Removal of Executives
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.D (describe procedures for the removal of
# executive leadership by other institutions). Suggested skill 4.B, Source
# Analysis.
#
# Essential knowledge relied on -- and this topic has only ONE statement:
#   PAU-3.D.1  across the course countries, executive leaders can be removed by the
#              LEGISLATIVE BRANCH through DIFFERENT PROCEDURES that CONTROL THE
#              ABUSE OF POWER
#
# Because one sentence cannot carry thirty items, the procedures themselves are
# taken from the statements that describe them, each named in the verifier's
# claim:
#   PAU-3.A.1  a parliamentary legislature SELECTS AND REMOVES the head of
#              government and cabinet
#   PAU-3.A.2  a presidential legislature can remove cabinet members ONLY THROUGH
#              IMPEACHMENT
#   PAU-3.A.3  in a semi-presidential system cabinet members are accountable to
#              BOTH the president and the legislature
#   PAU-3.B.2  parliaments may CENSURE cabinet ministers -- a check that is not a
#              removal
#   PAU-3.C.2a changes in China's top leadership are accomplished BEHIND CLOSED
#              DOORS
#   PAU-3.E.1d Nigeria's Senate possesses UNIQUE IMPEACHMENT AND CONFIRMATION
#              POWERS
#   PAU-1.D.4  governments change peacefully by elections, appointments and lines of
#              succession, and by more violent means such as revolutions or coups,
#              represented by such transitions in IRAN AND NIGERIA
#   LEG-1.B.2  peaceful transfer of power reinforces legitimacy
#
# THE CED'S SCORING GUIDELINES supply three removal facts the framework's own
# essential knowledge does not spell out, and they are course content in the same
# document (Scoring Guideline for sample free-response Question 3, on legislative
# independence):
#   * in IRAN the Majles has power over the budget, CONFIRMS AND IMPEACHES
#     MINISTERS, and may issue formal questions the government must answer
#   * in NIGERIA the constitution gives the legislature the power to IMPEACH THE
#     PRESIDENT as well as oversight
#   * in MEXICO the constitution gives the legislature the power to IMPEACH THE
#     PRESIDENT
#   * in the UNITED KINGDOM members question the prime minister during Question
#     Time and use that power to hold the prime minister accountable
# Items keyed to these say so in the claim, so a reader can check the source.
#
# NOTHING is asserted about removing Iran's Supreme Leader, because the framework
# and its scoring guidelines say nothing about it, and an item resting on that
# silence would have no defensible key.
#
# Table cases and figures are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.5", "Removal of Executives", 2)

_T_REM = dict(
    headers=["Case (hypothetical)", "Route by which the chamber may remove the head of government",
             "Route by which the chamber may reach an individual minister",
             "Times either route was used, 1990-2020"],
    rows=[["Case G", "an ordinary vote of the chamber that selected the officeholder",
           "the same ordinary vote", "6"],
          ["Case H", "impeachment only", "impeachment only", "1"],
          ["Case J", "impeachment only", "refusal of confirmation, and impeachment", "3"]])

_T_IMP = dict(
    headers=["Group of cases (hypothetical)", "Impeachment attempts initiated, 1990-2020",
             "Attempts that removed the officeholder",
             "Executives leaving office at a scheduled date (percent)"],
    rows=[["Group 1", "9", "2", "91"],
          ["Group 2", "2", "0", "97"],
          ["Group 3", "14", "6", "72"]])

QUESTIONS = [
 dict(q="Which branch does the framework identify as able to remove executive leaders across the course countries?",
   choices=[
     "the legislative branch",
     "the judiciary",
     "the armed forces",
     "an independent electoral commission",
     "a supranational organization"], ans=0,
   why="EK PAU-3.D.1 states that across the course countries, executive leaders can be removed by the legislative branch through different procedures that control the abuse of power. Courts, armies, commissions and international bodies are treated elsewhere and not under this heading."),
 dict(q="What does the framework say about the procedures by which executives are removed in the six course countries?",
   choices=[
     "they differ from country to country",
     "they are identical in all six countries",
     "they exist in only one of the six countries",
     "they are set by a supranational organization common to the six",
     "they are described nowhere in the framework"], ans=0,
   why="EK PAU-3.D.1 states that executive leaders can be removed by the legislative branch through DIFFERENT procedures. That word is why a student must know which route belongs to which system rather than one general rule."),
 dict(q="What purpose does the framework attach to these removal procedures?",
   choices=[
     "they control the abuse of power",
     "they shorten the time an executive spends in office",
     "they transfer the executive's powers to the judiciary",
     "they guarantee that a new party will take office",
     "they determine which party wins the next election"], ans=0,
   why="EK PAU-3.D.1 states that the procedures control the abuse of power, which places removal alongside EK PAU-1.B.2's independence of branches as a device preventing one branch from controlling all governmental power."),
 dict(q="A head of government in one course country can be turned out by a vote of the same chamber that put that officeholder in place. Which of the framework's system types does this route belong to?",
   choices=[
     "the parliamentary type",
     "the presidential type",
     "the semi-presidential type",
     "no type, since no legislature may remove a head of government",
     "every type equally"], ans=0,
   why="EK PAU-3.A.1 states that parliamentary systems combine the lawmaking and executive functions, which allows the national legislature to select and remove the head of government and cabinet. Selection and removal by the same chamber is the parliamentary route."),
 dict(q="In one of the framework's system types, a legislature that wants a cabinet minister out has only one route available. What is it?",
   choices=[
     "impeachment",
     "an ordinary vote of no confidence",
     "a request to the head of state",
     "refusal to pass the minister's budget",
     "dissolution of the cabinet by the courts"], ans=0,
   why="EK PAU-3.A.2 states that in presidential systems the legislature can only remove cabinet members through impeachment, which is what makes the cabinet mostly responsible to the elected executive rather than to the legislature."),
 dict(q="In a semi-presidential system, which institutions hold cabinet ministers to account on the framework's account?",
   choices=[
     "both the president and the legislature",
     "the president alone",
     "the legislature alone",
     "the judiciary alone",
     "an electoral commission"], ans=0,
   why="EK PAU-3.A.3 states that in semi-presidential systems members of the cabinet are held accountable by both the president and the legislature, which distinguishes the type from the presidential cabinet of EK PAU-3.A.2."),
 dict(q="Which powers does the framework describe as unique to Nigeria's Senate within its own legislature?",
   choices=[
     "impeachment and confirmation powers",
     "the power to approve treaties and troop deployment",
     "the power to select and remove the head of government",
     "the power to review and amend bills, delaying their implementation",
     "the power to nominate half the members of a vetting body"], ans=0,
   why="EK PAU-3.E.1.d states that both chambers of Nigeria's National Assembly hold the power to approve legislation and that the Senate possesses unique impeachment and confirmation powers. The rejected options describe Russia's Federation Council, a parliamentary legislature, the House of Lords and Iran's judiciary."),
 dict(q="According to the CED's scoring guidance on legislative independence, what power does Nigeria's constitution give its legislature over the president?",
   choices=[
     "the power to impeach the president, alongside oversight",
     "the power to remove the president by an ordinary majority vote",
     "the power to appoint the president",
     "the power to shorten the president's term",
     "no power over the president at all"], ans=0,
   why="The CED's scoring guidelines for its sample comparative-analysis question accept that in Nigeria the constitution gives the legislature the power to impeach the president as well as oversight, and that it uses both powers to remain independent and check the executive branch. EK PAU-3.E.1.d places the impeachment power in the Senate."),
 dict(q="According to the same CED scoring guidance, what power does Mexico's constitution give its legislature over the president?",
   choices=[
     "the power to impeach the president",
     "the power to dismiss the president by a vote of no confidence",
     "the power to nominate the president's successor",
     "the power to extend the president's single term",
     "the power to appoint the cabinet directly"], ans=0,
   why="The CED's scoring guidelines accept that in Mexico the constitution gives the legislature the power to impeach the president and that it uses this power to check the executive branch. EK PAU-3.A.2 makes impeachment the presidential system's route, and EK PAU-3.A.2 places Mexico in that type."),
 dict(q="According to the same CED scoring guidance, which powers does Iran's Majles hold over ministers?",
   choices=[
     "it confirms and impeaches them",
     "it appoints them without any executive involvement",
     "it may only censure them",
     "it has no power over ministers at all",
     "it selects them from among its own members"], ans=0,
   why="The CED's scoring guidelines accept that in Iran the Majles has power over the budget, confirms and impeaches ministers, and may issue formal questions the government must answer, using these powers to check the executive branch. EK PAU-3.E.1.b adds that the Majles confirms presidential nominees to the Cabinet."),
 dict(q="Besides its powers over the budget and over ministers, what further power does the CED's scoring guidance attribute to Iran's Majles?",
   choices=[
     "it may issue formal questions that the government must answer",
     "it may dissolve the Guardian Council",
     "it may appoint the head of the judiciary",
     "it may call a national referendum",
     "it may amend the constitution without any other body's approval"], ans=0,
   why="The CED's scoring guidelines accept that the Majles may issue formal questions that the government must answer, alongside its budget power and its confirmation and impeachment of ministers. EK PAU-3.C.2.b assigns the appointment of the head of the judiciary to the Supreme Leader instead."),
 dict(q="The CED's scoring guidance describes Question Time in the United Kingdom as a power members use to",
   choices=[
     "hold the prime minister accountable and open debate",
     "remove the prime minister from office immediately",
     "appoint members of the upper chamber",
     "impeach the head of state",
     "dissolve the government's majority"], ans=0,
   why="The CED's scoring guidelines accept that during Question Time members of the United Kingdom legislature can question the prime minister about various policies and use that power to hold the prime minister accountable and open debate. EK PAU-3.B.2 lists questioning the executive among the parliamentary checks, and it is a check short of removal."),
 dict(q="How does censure of a cabinet minister differ from removal in the framework's account?",
   choices=[
     "censure is a formal check the framework lists among parliamentary powers, whereas removal ends the officeholder's tenure",
     "censure ends the officeholder's tenure, whereas removal is only a formal condemnation",
     "the framework treats the two as the same act under different names",
     "censure is available only in presidential systems",
     "removal is available only where the state is federal"], ans=0,
   why="EK PAU-3.B.2 lists censuring cabinet ministers among the parliamentary checks on the executive, alongside refusal of legislation, questioning and election deadlines, while EK PAU-3.D.1 concerns procedures that remove executive leaders. A condemnation and a removal are different outcomes."),
 dict(q="Which comparison of the legislatures of Mexico and Nigeria is supported by the CED and its scoring guidance?",
   choices=[
     "The constitution of each gives its legislature the power to impeach the president",
     "The legislature of each may remove the president by an ordinary majority vote",
     "Neither legislature has any power over its president",
     "One legislature may impeach the president and the other may only censure ministers",
     "One legislature selects the president and the other impeaches the president"], ans=0,
   why="The CED's scoring guidelines accept the impeachment power for both countries' legislatures, and EK PAU-3.A.2 makes impeachment the presidential system's route while placing both countries in that type. Neither is described as removing a president by ordinary vote."),
 dict(q="Which comparison of the removal powers of Iran's and Nigeria's legislatures is supported by the CED and its scoring guidance?",
   choices=[
     "One is described as impeaching ministers and the other as impeaching the president",
     "Both are described as impeaching the head of state",
     "Neither is described as impeaching anyone",
     "One is described as selecting the head of government and the other as impeaching ministers",
     "Both are described as removing officeholders by an ordinary majority vote"], ans=0,
   why="The CED's scoring guidelines accept that Iran's Majles confirms and impeaches MINISTERS and that Nigeria's legislature may impeach the PRESIDENT. Neither the framework nor its scoring guidelines describes any procedure for removing Iran's Supreme Leader, so nothing here rests on that silence."),
 dict(q="Which comparison of how an executive may be turned out in the United Kingdom and in Mexico follows from the framework's system types?",
   choices=[
     "In one the chamber that selected the head of government may also remove that officeholder, whereas in the other the legislature's route to the chief executive is impeachment",
     "In both the legislature may remove the chief executive by an ordinary vote",
     "In both the only route is impeachment",
     "In neither may the legislature remove any member of the executive",
     "In one the head of state removes the head of government and in the other the courts do"], ans=0,
   why="EK PAU-3.A.1 gives a parliamentary legislature the power to select and remove the head of government, and EK PAU-3.A.2 restricts a presidential legislature to impeachment, with the CED's scoring guidelines confirming the impeachment power over Mexico's president. EK PAU-3.A.1 and EK PAU-3.A.2 place the two countries in those types."),
 dict(q="What does the framework say about how changes in China's top leadership occur, and what follows for this topic?",
   choices=[
     "they are accomplished behind closed doors, so the framework describes no public legislative removal procedure there",
     "they are accomplished by an impeachment vote of the National People's Congress",
     "they are accomplished by a national referendum",
     "they are accomplished by the head of the judiciary",
     "they are accomplished by an ordinary vote of the eight permitted parties"], ans=0,
   why="EK PAU-3.C.2.a states that changes in China's top leadership are accomplished behind closed doors, and EK PAU-1.D.1.a locates that regime's stability in the Communist Party's control. EK PAU-3.F.1.a adds that the Politburo Standing Committee is the actual center of power, which is not a legislative body."),
 dict(q="The framework notes that governments can also change by more violent means. In which two course countries does it locate such transitions?",
   choices=[
     "Iran and Nigeria",
     "China and Russia",
     "Mexico and the United Kingdom",
     "Russia and Nigeria",
     "China and Iran"], ans=0,
   why="EK PAU-1.D.4 states that governments also change by more violent means such as revolutions or coups, represented by such violent transitions in Iran and Nigeria, and contrasts those with the relatively peaceful process of elections, appointments and lines of succession."),
 dict(q="Why does a peaceful, procedurally regular removal of an executive matter for legitimacy on the framework's account?",
   choices=[
     "because peaceful transfer of power is named among the things that reinforce legitimacy",
     "because international recognition depends on it",
     "because it converts an authoritarian regime into a democratic one",
     "because it lengthens the successor's term",
     "because it transfers sovereignty from the state to the legislature"], ans=0,
   why="EK LEG-1.B.2 names peaceful resolution of conflicts and peaceful transfer of power among the things that reinforce legitimacy, and EK LEG-1.A.1 defines legitimacy as whether constituents believe the government has the right to use power as it does. A removal conducted by the stated procedure demonstrates that the rules hold."),
 dict(q="The table describes three hypothetical cases by the routes available to the chamber. Which case matches the framework's account of a parliamentary system?",
   table=_T_REM,
   choices=[
     "Case G, where an ordinary vote of the chamber that selected the head of government may also remove that officeholder and reach ministers by the same route",
     "Case H, where impeachment is the only route to either the head of government or a minister",
     "Case J, where ministers may also be reached by refusal of confirmation",
     "None of the three, since a parliamentary chamber cannot remove a head of government",
     "All three equally, since each names a route"], ans=0,
   why="EK PAU-3.A.1 states that a parliamentary legislature selects and removes the head of government and cabinet, so the matching case is the one where an ordinary vote of the selecting chamber reaches both. Impeachment-only routes belong to EK PAU-3.A.2's presidential type."),
 dict(q="Using the same table, which case matches the framework's account of a presidential system most closely?",
   table=_T_REM,
   choices=[
     "Case H, where impeachment is the only route to the head of government and to individual ministers",
     "Case G, where an ordinary vote reaches both",
     "Case J, where ministers may be reached by refusal of confirmation as well as impeachment",
     "None of the three, since a presidential legislature has no route to a minister",
     "Both Case G and Case H, since each names a single route"], ans=0,
   why="EK PAU-3.A.2 states that a presidential legislature can only remove cabinet members through impeachment, so the closest match is the case in which impeachment is the sole route. The rejected option denying any route contradicts the same statement, which supplies impeachment."),
 dict(q="According to the same table, the total number of times either route was used across the three cases is",
   table=_T_REM,
   choices=[
     "10",
     "9",
     "7",
     "6",
     "4"], ans=0,
   why="Adding the final column across all three rows gives the total. The alternatives arise from omitting one row, from adding only two of the three, and from reading the largest single row as though it were the total."),
 dict(q="The table reports hypothetical impeachment records for three groups of cases. In which group did the largest SHARE of impeachment attempts actually remove the officeholder?",
   table=_T_IMP,
   choices=[
     "Group 3, where six of fourteen attempts removed the officeholder",
     "Group 1, where nine attempts were initiated",
     "Group 1, where two attempts removed the officeholder",
     "Group 2, where the fewest attempts were initiated",
     "The table does not report how many attempts succeeded"], ans=0,
   why="The question asks for a share, so each group's successful removals must be divided by its attempts rather than compared as counts. EK PAU-3.D.1 presents removal procedures as controlling the abuse of power, and a procedure that reaches its object is that control operating."),
 dict(q="According to the same table, the total number of impeachment attempts initiated across the three groups is",
   table=_T_IMP,
   choices=[
     "25",
     "23",
     "8",
     "14",
     "11"], ans=0,
   why="Adding the attempts column across the three groups gives the total. The alternatives arise from dropping the smallest group, from adding the successful removals instead, from reading the largest single group, and from adding only two groups."),
 dict(q="A student concludes from the same table that the group with the most impeachment attempts must be the least stable. Which objection is best supported?",
   table=_T_IMP,
   choices=[
     "The framework presents removal procedures as controlling the abuse of power, so their use is the constitutional mechanism working, and that group still records most executives leaving at a scheduled date",
     "The framework presents impeachment as a sign that a constitution has failed",
     "The table reports nothing about how executives left office",
     "The group with the most attempts also records the fewest scheduled departures, at zero",
     "Impeachment attempts cannot be counted"], ans=0,
   why="EK PAU-3.D.1 states that executive leaders can be removed by the legislative branch through different procedures that CONTROL THE ABUSE OF POWER, so using the procedure is the framework's picture of a check operating. The same row still shows a large majority of executives leaving at a scheduled date."),
 dict(q="Which finding would most strongly support a claim that a legislature's impeachment power is real rather than nominal?",
   choices=[
     "Impeachment proceedings have been brought against sitting executives and have on occasion resulted in removal",
     "The constitution contains an article describing impeachment",
     "The legislature has debated the meaning of the impeachment article",
     "The executive has publicly said that impeachment would be inappropriate",
     "The legislature meets for more days each year than it used to"], ans=0,
   why="EK PAU-3.D.1 concerns procedures by which executive leaders CAN BE REMOVED, and the CED's scoring guidelines accept that Nigeria's and Mexico's legislatures USE their impeachment powers to check the executive. A written article that has never been applied does not show the same thing."),
 dict(q="In one country the cabinet falls when the chamber that installed it withdraws its support, and no separate proceeding is required. Which of the framework's types does this describe, and what follows about the head of government's position?",
   choices=[
     "the parliamentary type, in which the head of government's tenure depends continuously on the chamber's support",
     "the presidential type, in which the head of government serves a fixed term regardless of the chamber",
     "the semi-presidential type, in which the head of government is nominated by a separately elected president",
     "a type in which the head of state removes the head of government at will",
     "a type in which the courts remove the head of government"], ans=0,
   why="EK PAU-3.A.1 states that combining the lawmaking and executive functions allows the national legislature to select and remove the head of government and cabinet. If withdrawal of support is sufficient and no separate proceeding is needed, tenure depends on that support continuously."),
 dict(q="In a second country, a chief executive elected separately to a fixed term can be reached by the legislature only through a formal proceeding brought on stated grounds. Which of the framework's types does this describe?",
   choices=[
     "the presidential type",
     "the parliamentary type",
     "a type in which the legislature selects the chief executive",
     "a type in which the chief executive is appointed by the head of the judiciary",
     "a type in which no removal is possible by any institution"], ans=0,
   why="EK PAU-3.A.2 gives presidential systems separate fixed-term popular elections and restricts the legislature to impeachment as its route to members of the executive. A formal proceeding on stated grounds against a separately elected officeholder is that arrangement."),
 dict(q="Why does the framework describe removal procedures as controlling the abuse of power rather than simply as ways of changing leaders?",
   choices=[
     "because the availability of a procedure constrains an officeholder while still in office, which is the same function the framework assigns to independence among branches",
     "because removal always follows an election defeat",
     "because removal transfers the executive's powers to the judiciary",
     "because removal is the only way any government ever changes",
     "because removal converts a unitary state into a federal one"], ans=0,
   why="EK PAU-3.D.1 attaches the phrase 'control the abuse of power' to these procedures, and EK PAU-1.B.2 assigns the same function to independence among branches, which can prevent any one branch from controlling all governmental power. EK PAU-1.D.4 makes clear that elections, appointments and succession are separate routes of change."),
 dict(q="Taking the framework's statement on removal together with the system types, which summary is most accurate?",
   choices=[
     "Legislatures across the course countries can remove executive leaders, but by different routes -- an ordinary vote where lawmaking and executive functions are combined, and impeachment where the branches are separately elected",
     "Legislatures across the course countries remove executive leaders by an identical procedure",
     "No legislature among the course countries can remove any member of the executive",
     "Only the courts may remove an executive in any of the course countries",
     "Removal procedures exist only where the state is federal"], ans=0,
   why="EK PAU-3.D.1 supplies the general claim and the word 'different', EK PAU-3.A.1 supplies the parliamentary route and EK PAU-3.A.2 the impeachment route, with EK PAU-3.A.3 adding dual accountability in the hybrid case. The summary keeps the general claim and the variation it insists on."),
]
