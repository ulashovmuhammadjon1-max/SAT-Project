# AP COMPARATIVE GOVERNMENT AND POLITICS 2.7 Independent Legislatures
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.F (explain how legislative powers are
# constrained by other institutions and/or processes, which can affect legislative
# independence). Suggested skill 4.C, Source Analysis.
#
# Essential knowledge relied on:
#   PAU-3.F.1  legislative powers can be CONSTRAINED BY OTHER GOVERNMENTAL
#              INSTITUTIONS, including:
#     .a China's POLITBURO STANDING COMMITTEE, which is the ACTUAL CENTER OF POWER
#        in the Chinese state
#     .b China's STANDING COMMITTEE OF THE NATIONAL PEOPLE'S CONGRESS, which
#        ASSUMES LEGISLATIVE DUTIES most of the year when the NPC is not in
#        session, SETS THE NPC LEGISLATIVE AGENDA, SUPERVISES NPC MEMBER ELECTIONS,
#        and INTERPRETS THE CONSTITUTION AND LAWS
#     .c Iran's EXPEDIENCY COUNCIL, selected by the Supreme Leader as an ADVISORY
#        COMMITTEE TO RESOLVE DISPUTES between the Majles and the Guardian Council
#     .d Iran's GUARDIAN COUNCIL, which VETS CANDIDATES and OVERSEES THE MAJLES to
#        make sure laws comply with Islamic law
#   PAU-3.F.2  legislatures have the potential to REINFORCE LEGITIMACY AND STABILITY
#              by RESPONDING TO PUBLIC DEMAND, OPENLY DEBATING POLICY, FACILITATING
#              COMPROMISE BETWEEN FACTIONS, EXTENDING CIVIL LIBERTIES, and
#              RESTRICTING THE POWER OF THE EXECUTIVE
#
# THE CED'S SCORING GUIDELINES for its sample comparative-analysis question define
# the term this topic turns on and give reasons a regime constrains a legislature:
#   * LEGISLATIVE INDEPENDENCE is "the degree to which a legislature is free to
#     exercise its powers without influence from other branches/institutions"
#   * the Iranian government constrains the Majles TO GIVE THE SUPREME LEADER MORE
#     POWER and to make sure all institutions abide by THEOCRATIC RULES
#   * in the United Kingdom the legislature is CONSTRAINED BY ELECTIONS, with all
#     members of the House of Commons up for election every 5 years, which
#     constrains lawmakers to work for their constituents
#   * in Nigeria the House of Representatives is CONSTRAINED BY THE EXECUTIVE
#     BRANCH, because the president wants more concentrated power
#   * in Mexico the legislature is CONSTRAINED BY ELECTIONS as a way to maintain
#     stability and prevent corruption
# Every item keyed to one of these says so in the verifier's claim.
#
# Note that PAU-3.F.1's four examples come from only TWO course countries, China
# and Iran. Item 29 keys that, because a student who assumes the framework
# distributes its examples evenly will look for a third.
#
# Table cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.7", "Independent Legislatures", 2)

_T_IND = dict(
    headers=["Legislature (hypothetical)", "Executive bills amended before passage (percent)",
             "Bills initiated by members rather than by the executive (percent)",
             "Days in session per year"],
    rows=[["Legislature P", "62", "41", "118"],
          ["Legislature Q", "9", "4", "12"],
          ["Legislature R", "38", "23", "74"]])

_T_CONSTR = dict(
    headers=["Constraining body (hypothetical case)", "Function as described"],
    rows=[["Body 1", "vets candidates for the legislature and oversees it to ensure its laws comply with religious law"],
          ["Body 2", "exercises the legislature's duties for most of the year while it is not in session, sets its agenda, supervises the election of its members, and interprets the constitution and laws"],
          ["Body 3", "an advisory committee that resolves disputes between the legislature and the body that vets candidates"],
          ["Body 4", "the actual center of power in the state, standing outside the legislature altogether"]])

QUESTIONS = [
 dict(q="How do the CED's scoring guidelines define legislative independence?",
   choices=[
     "the degree to which a legislature is free to exercise its powers without influence from other branches or institutions",
     "the number of bills a legislature passes each year",
     "whether a legislature is elected rather than appointed",
     "whether a legislature has one chamber or two",
     "the length of time a legislature sits before an election must be held"], ans=0,
   why="The CED's scoring guidelines for its sample comparative-analysis question accept exactly this definition. It makes independence a matter of freedom from outside influence rather than of output, selection method, structure or timetable."),
 dict(q="What does the framework say can constrain legislative powers?",
   choices=[
     "other governmental institutions",
     "only the electorate at a general election",
     "only a supranational organization",
     "only the courts",
     "nothing, since a legislature's powers are absolute"], ans=0,
   why="EK PAU-3.F.1 states that legislative powers can be constrained by other governmental institutions, and then names four such bodies. The CED's scoring guidelines add elections and the executive branch as further sources of constraint."),
 dict(q="Which body does the framework describe as the actual center of power in the Chinese state?",
   choices=[
     "the Politburo Standing Committee",
     "the National People's Congress meeting in full session",
     "the Standing Committee that acts for the Congress between its sessions",
     "the office of the premier",
     "the Military Commission"], ans=0,
   why="EK PAU-3.F.1.a states that China's Politburo Standing Committee is the actual center of power in the Chinese state. EK PAU-3.E.1.a separately states what the constitution RECOGNIZES about the National People's Congress, which is a claim about the text rather than about actual power."),
 dict(q="Which set of functions does the framework assign to the Standing Committee of China's National People's Congress?",
   choices=[
     "assuming legislative duties most of the year when the Congress is not in session, setting its legislative agenda, supervising the election of its members, and interpreting the Constitution and laws",
     "vetting candidates and reviewing laws for compliance with religious law",
     "resolving disputes between the legislature and a vetting body",
     "approving budget legislation, treaties, judicial nominees and troop deployment",
     "reviewing and amending bills and delaying their implementation"], ans=0,
   why="EK PAU-3.F.1.b lists exactly these four functions. The rejected sets belong to Iran's Guardian Council, Iran's Expediency Council, Russia's Federation Council and the United Kingdom's House of Lords."),
 dict(q="Why does the framework treat the Standing Committee's assumption of legislative duties as a constraint on the legislature?",
   choices=[
     "because it exercises those duties for most of the year, when the full body is not in session",
     "because it may dissolve the full body at will",
     "because it appoints every member of the full body",
     "because it may veto laws the full body has passed",
     "because it replaces the full body permanently"], ans=0,
   why="EK PAU-3.F.1.b states that the Standing Committee assumes legislative duties most of the year when the National People's Congress is not in session. A body that acts for most of the year is exercising the legislature's own powers for most of the year, which is what EK PAU-3.F.1 means by a constraint."),
 dict(q="Which of the Standing Committee's functions bears most directly on who sits in the National People's Congress?",
   choices=[
     "supervising the election of its members",
     "setting its legislative agenda",
     "interpreting the Constitution and laws",
     "assuming its duties between sessions",
     "approving the premier"], ans=0,
   why="EK PAU-3.F.1.b names supervising National People's Congress member elections among the Standing Committee's functions. Agenda setting, interpretation and acting between sessions all concern what the body does rather than who belongs to it, and approving the premier is the full Congress's function under EK PAU-3.E.1.a."),
 dict(q="Which of the Standing Committee's functions gives it authority over the meaning of the law itself?",
   choices=[
     "interpreting the Constitution and laws",
     "supervising the election of members",
     "setting the legislative agenda",
     "assuming legislative duties between sessions",
     "legitimizing policies of the executive"], ans=0,
   why="EK PAU-3.F.1.b names interpreting the Constitution and laws among the Standing Committee's functions, which is authority over what the law means rather than over who makes it or when. Legitimizing executive policies is assigned to the full Congress at EK PAU-3.E.1.a."),
 dict(q="How does the framework describe Iran's Expediency Council?",
   choices=[
     "an advisory committee selected by the Supreme Leader to resolve disputes between the Majles and the Guardian Council",
     "a body that vets candidates and oversees the Majles for compliance with Islamic law",
     "a chamber that reviews and amends the Majles's bills",
     "a court that hears appeals from the Majles",
     "an elected chamber that confirms Cabinet nominees"], ans=0,
   why="EK PAU-3.F.1.c states that Iran's Expediency Council is selected by the Supreme Leader as an advisory committee to resolve disputes between the Majles and the Guardian Council, and EK PAU-3.C.2.b lists the Council among the Supreme Leader's appointments."),
 dict(q="How does the framework describe the functions of Iran's Guardian Council in relation to the Majles?",
   choices=[
     "it vets candidates and oversees the Majles to make sure laws comply with Islamic law",
     "it resolves disputes between the Majles and another body",
     "it assumes the Majles's duties when that body is not in session",
     "it approves the budget the Majles has passed",
     "it appoints the members of the Majles directly"], ans=0,
   why="EK PAU-3.F.1.d states that Iran's Guardian Council vets candidates and oversees the Majles to make sure laws comply with Islamic law, and EK PAU-3.E.1.b adds that the Majles acts under its supervision for compatibility with Islam and Sharia law. Dispute resolution belongs to the Expediency Council."),
 dict(q="Which comparison of the two Chinese bodies the framework names as constraints is accurate?",
   choices=[
     "One is described as the actual center of power in the state, while the other exercises the legislature's own duties between sessions and sets its agenda",
     "One vets candidates for the legislature while the other resolves disputes about its laws",
     "Both are described as the actual center of power in the state",
     "Both are chambers of the legislature with equal powers",
     "Neither has any role in the legislature's work"], ans=0,
   why="EK PAU-3.F.1.a identifies the Politburo Standing Committee as the actual center of power in the Chinese state, while EK PAU-3.F.1.b describes the Standing Committee of the National People's Congress acting for the legislature between sessions, setting its agenda, supervising its member elections and interpreting the law. Vetting and dispute resolution are the Iranian bodies' functions."),
 dict(q="Which comparison of the two Iranian bodies the framework names as constraints is accurate?",
   choices=[
     "One vets candidates and checks laws against religious law, while the other advises on disputes between the legislature and that vetting body",
     "One assumes the legislature's duties between sessions while the other interprets the constitution",
     "Both vet candidates for the legislature",
     "Both are elected by the legislature from among its own members",
     "Neither is connected to the Supreme Leader in any way"], ans=0,
   why="EK PAU-3.F.1.d gives the Guardian Council the vetting and compliance role and EK PAU-3.F.1.c gives the Expediency Council the advisory dispute-resolving role. EK PAU-3.C.2.b has the Supreme Leader appointing the Expediency Council and half the Guardian Council, so neither is separate from that office."),
 dict(q="According to the framework, legislatures have the potential to reinforce legitimacy and stability by",
   choices=[
     "responding to public demand, openly debating policy, facilitating compromise between factions, extending civil liberties, and restricting the power of the executive",
     "deferring to the executive on questions of policy and meeting in closed session",
     "delegating their lawmaking powers to a smaller committee",
     "extending the term of the head of government",
     "certifying election results and drawing constituency boundaries"], ans=0,
   why="EK PAU-3.F.2 lists exactly these five. The last of them, restricting the power of the executive, is the same function EK PAU-3.B.1 and EK PAU-3.B.2 describe from the comparative side."),
 dict(q="A legislature holds televised debates in which rival positions on a proposed law are argued at length. Which of the framework's five routes to reinforcing legitimacy and stability does this illustrate?",
   choices=[
     "openly debating policy",
     "extending civil liberties",
     "facilitating compromise between factions",
     "restricting the power of the executive",
     "responding to public demand"], ans=0,
   why="EK PAU-3.F.2 names openly debating policy among the ways legislatures can reinforce legitimacy and stability, and EK DEM-1.C.4 treats the open circulation of information about policy making as transparency. Debate itself, rather than its outcome, is what this route consists of."),
 dict(q="A legislature brokers an agreement between two blocs whose demands had blocked a budget for months. Which of the framework's five routes does this illustrate?",
   choices=[
     "facilitating compromise between factions",
     "openly debating policy",
     "extending civil liberties",
     "responding to public demand",
     "restricting the power of the executive"], ans=0,
   why="EK PAU-3.F.2 names facilitating compromise between factions among the ways legislatures reinforce legitimacy and stability. EK LEG-1.B.2 adds that peaceful resolution of conflicts reinforces legitimacy, which is what a brokered agreement between rival blocs supplies."),
 dict(q="A legislature enacts statutory protections for freedom of assembly and of the press. Which of the framework's five routes does this illustrate?",
   choices=[
     "extending civil liberties",
     "facilitating compromise between factions",
     "openly debating policy",
     "responding to public demand",
     "restricting the power of the executive"], ans=0,
   why="EK PAU-3.F.2 names extending civil liberties among the ways legislatures reinforce legitimacy and stability, and EK LEG-1.C.3 describes reform pressure producing institutions or policies that protect civil liberties. Enacting the protection is that route."),
 dict(q="A legislature refuses the executive's request for emergency powers and requires ministers to seek approval for each measure. Which of the framework's five routes does this illustrate?",
   choices=[
     "restricting the power of the executive",
     "responding to public demand",
     "extending civil liberties",
     "openly debating policy",
     "facilitating compromise between factions"], ans=0,
   why="EK PAU-3.F.2 names restricting the power of the executive among the ways legislatures reinforce legitimacy and stability, and EK PAU-3.B.2 lists refusing to pass executive-proposed legislation among the parliamentary checks. Withholding a delegated power is that restriction in operation."),
 dict(q="According to the CED's scoring guidance, why does the Iranian government constrain the Majles?",
   choices=[
     "to give the Supreme Leader more power and to make sure all institutions abide by theocratic rules",
     "to reduce the cost of legislative sessions",
     "to satisfy the requirements of a supranational organization",
     "to increase the number of parties represented in the chamber",
     "to transfer lawmaking to an elected upper chamber"], ans=0,
   why="The CED's scoring guidelines accept both of these explanations, and add that the Expediency Council, selected by the Supreme Leader, can constrain the Majles to reduce its power. EK PAU-3.F.1.c and EK PAU-3.F.1.d supply the institutional mechanisms."),
 dict(q="According to the same scoring guidance, what constrains the United Kingdom's legislature, and with what effect?",
   choices=[
     "elections, with all members of the House of Commons up for election every five years, which constrains lawmakers to work for their constituents",
     "an appointed upper chamber that may veto any bill permanently",
     "a vetting body that reviews candidates before each election",
     "a supranational court that reviews every statute",
     "the monarch's power to refuse assent to legislation"], ans=0,
   why="The CED's scoring guidelines accept that in the United Kingdom the legislature is constrained by elections, that all members of the House of Commons are up for election every 5 years, and that this constrains lawmakers to work for their constituents. EK PAU-3.E.1.f gives the Lords a delaying rather than a veto role."),
 dict(q="According to the same scoring guidance, what constrains Nigeria's House of Representatives, and why?",
   choices=[
     "the executive branch, because the president wants to have more concentrated power",
     "a religious vetting body, because laws must comply with religious law",
     "an appointed upper chamber, because it may delay implementation",
     "a supranational organization, because of treaty obligations",
     "the judiciary, because it may dissolve the chamber"], ans=0,
   why="The CED's scoring guidelines accept that in Nigeria the House of Representatives is constrained by the executive branch because the president wants to have more concentrated power. The vetting body and the delaying chamber described against it belong to Iran and the United Kingdom."),
 dict(q="The table reports hypothetical figures for three legislatures. Which one appears most independent on the definition the CED's scoring guidelines give?",
   table=_T_IND,
   choices=[
     "Legislature P, which amends the largest share of executive bills, originates the largest share of bills itself, and sits on the most days",
     "Legislature Q, which sits on the fewest days",
     "Legislature R, which is second on every measure",
     "None of the three, since independence cannot be observed in data",
     "All three equally, since each amends some executive bills"], ans=0,
   why="The CED's scoring guidelines define legislative independence as the degree to which a legislature is free to exercise its powers without influence from other branches or institutions. Amending the executive's bills, originating its own, and sitting often are all exercises of its own powers, and all three columns point to the same row."),
 dict(q="Using the same table, which legislature's record is most consistent with the framework's description of a body whose duties are exercised elsewhere for most of the year?",
   table=_T_IND,
   choices=[
     "Legislature Q, which sits on twelve days a year and amends nine percent of executive bills",
     "Legislature P, which sits on the most days",
     "Legislature R, which sits on seventy-four days",
     "None of the three, since a legislature always exercises its own duties",
     "All three, since each sits for part of the year"], ans=0,
   why="EK PAU-3.F.1.b describes a standing committee that assumes legislative duties most of the year when the full body is not in session, so the matching record is a chamber that sits rarely and changes little when it does. The other two rows sit far more often and amend far more."),
 dict(q="According to the same table, the gap between the highest and lowest shares of executive bills amended before passage is",
   table=_T_IND,
   choices=[
     "53 percentage points",
     "24 percentage points",
     "29 percentage points",
     "37 percentage points",
     "62 percentage points"], ans=0,
   why="Subtracting the smallest figure in that column from the largest gives the gap. The alternatives are the gaps between other pairs in the same column, the corresponding gap in a different column, and the largest single value read as though it were a difference."),
 dict(q="The table describes four hypothetical constraining bodies. Which one matches the framework's description of Iran's Guardian Council?",
   table=_T_CONSTR,
   choices=[
     "Body 1, which vets candidates for the legislature and oversees it to ensure its laws comply with religious law",
     "Body 2, which exercises the legislature's duties between sessions",
     "Body 3, which advises on disputes",
     "Body 4, which stands outside the legislature as the actual center of power",
     "None of the four, since the Guardian Council does not constrain the legislature"], ans=0,
   why="EK PAU-3.F.1.d states that Iran's Guardian Council vets candidates and oversees the Majles to make sure laws comply with Islamic law, and EK PAU-3.E.1.b confirms that the Majles acts under its supervision. Only one row carries both the vetting and the compliance function."),
 dict(q="Using the same table, which body matches the framework's description of the Standing Committee of China's National People's Congress?",
   table=_T_CONSTR,
   choices=[
     "Body 2, which exercises the legislature's duties for most of the year, sets its agenda, supervises the election of its members, and interprets the constitution and laws",
     "Body 1, which vets candidates for the legislature",
     "Body 3, which resolves disputes between two other bodies",
     "Body 4, which stands outside the legislature altogether",
     "None of the four, since that committee is part of the legislature and so cannot constrain it"], ans=0,
   why="EK PAU-3.F.1.b lists all four of these functions for the Standing Committee of the National People's Congress, and EK PAU-3.F.1 places it among the institutions that constrain legislative powers. Being part of the same institution does not remove it from that list."),
 dict(q="Using the same table, which body matches the framework's description of Iran's Expediency Council?",
   table=_T_CONSTR,
   choices=[
     "Body 3, an advisory committee that resolves disputes between the legislature and the body that vets candidates",
     "Body 1, which vets candidates itself",
     "Body 2, which exercises the legislature's duties between sessions",
     "Body 4, the actual center of power in the state",
     "None of the four, since the Expediency Council has no role in legislation"], ans=0,
   why="EK PAU-3.F.1.c states that Iran's Expediency Council is selected by the Supreme Leader as an advisory committee to resolve disputes between the Majles and the Guardian Council. Only one row is advisory and describes resolving disputes between the legislature and the vetting body."),
 dict(q="According to the CED's scoring guidance, what constrains Mexico's legislature, and for what stated purpose?",
   choices=[
     "elections, as a way to maintain stability and prevent corruption",
     "a religious vetting body, to ensure laws comply with religious law",
     "a standing committee that acts between sessions",
     "an appointed upper chamber that may delay implementation",
     "the judiciary, which may annul any statute"], ans=0,
   why="The CED's scoring guidelines accept that in Mexico the legislature is constrained by elections as a way to maintain stability and prevent corruption. The same guidelines give a parallel explanation for the United Kingdom, where elections constrain lawmakers to work for their constituents."),
 dict(q="Which of the constraints the framework names operates from INSIDE the legislature it constrains rather than from outside it?",
   choices=[
     "the standing committee that assumes the legislature's duties between sessions and sets its agenda",
     "the body that vets candidates for the legislature",
     "the advisory committee that resolves disputes about the legislature's laws",
     "the body described as the actual center of power in the state",
     "the executive branch of the government"], ans=0,
   why="EK PAU-3.F.1.b describes a committee OF the National People's Congress exercising that body's duties, setting its agenda, supervising its member elections and interpreting the law, so the constraint runs from within. EK PAU-3.F.1.a, .c and .d name bodies outside the legislature they affect."),
 dict(q="Which finding would most strongly support a claim that a legislature is independent, on the definition the CED's scoring guidelines give?",
   choices=[
     "The chamber has repeatedly rejected or rewritten the executive's proposals and has set its own agenda without outside approval",
     "The chamber passes every bill the executive introduces",
     "The chamber has a large number of members",
     "The chamber meets in a purpose-built building",
     "The chamber's members belong to many different parties"], ans=0,
   why="The CED's scoring guidelines define legislative independence as freedom to exercise the legislature's powers without influence from other branches or institutions, so evidence for it must be evidence of powers exercised against or apart from outside preference. Size, premises and party count say nothing about that freedom."),
 dict(q="From how many of the six course countries does the framework draw the four constraining bodies it names under this learning objective?",
   choices=[
     "two",
     "three",
     "four",
     "five",
     "all six"], ans=0,
   why="EK PAU-3.F.1.a and .b name two Chinese bodies and EK PAU-3.F.1.c and .d name two Iranian ones, so the four examples come from two countries. Constraints on the legislatures of the other course countries appear in the CED's scoring guidelines rather than in this statement."),
 dict(q="Taking the framework's two statements in this topic together, which summary is most accurate?",
   choices=[
     "Other governmental institutions can limit what a legislature is free to do, and a legislature that is free to act can reinforce legitimacy and stability in five named ways",
     "Legislatures cannot be constrained by any other institution, and their only function is to pass laws",
     "Legislatures are constrained only by elections, and constraint has no bearing on legitimacy",
     "Constraints on legislatures exist only in authoritarian regimes, where legislatures cannot reinforce legitimacy",
     "The framework treats legislative independence as identical to the number of chambers a legislature has"], ans=0,
   why="EK PAU-3.F.1 supplies the constraints and EK PAU-3.F.2 the five ways a legislature can reinforce legitimacy and stability, so the two statements describe what limits a legislature and what it contributes when unlimited. The CED's scoring guidelines add elections and the executive as further constraints, in democratic cases included."),
]
