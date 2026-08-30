# AP COMPARATIVE GOVERNMENT AND POLITICS 2.9 Independent Judiciaries
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.H (explain the importance of independent
# judiciaries relative to other political institutions). Suggested skill 5.B,
# Argumentation (support the argument using relevant evidence) -- which is why
# several items here ask which evidence would support or weaken a claim.
#
# Essential knowledge relied on:
#   PAU-3.H.1  the DEGREE of a judiciary's independence from other branches depends
#              on FIVE things:
#                1 the amount of AUTHORITY the courts have to OVERRULE EXECUTIVE
#                  AND LEGISLATIVE ACTIONS
#                2 the PROCESS BY WHICH JUDICIAL OFFICIALS ACQUIRE THEIR JOBS
#                3 the LENGTH OF JUDICIAL TERMS
#                4 the PROFESSIONAL AND ACADEMIC BACKGROUNDS judicial officials are
#                  expected to have
#                5 the PROCESSES USED TO REMOVE JUDGES FROM THEIR POSTS
#   PAU-3.H.2  independent judiciaries can STRENGTHEN DEMOCRACY by MAINTAINING
#              CHECKS AND BALANCES, PROTECTING RIGHTS AND LIBERTIES, ESTABLISHING
#              THE RULE OF LAW, and MAINTAINING SEPARATION OF POWERS
#
# Country applications are held to PAU-3.G.1, cited in each claim: party control of
# most appointments in China (.a), Sharia training for Iranian judges (.b), Mexico's
# 15-year term and its nomination-and-approval route (.c, .d), Nigeria's judicial
# council and the effort to reestablish independence by reducing corruption (.e,
# .f), and Russia's constitutional review power that has not been used against the
# governing branches (.g, .h). PAU-1.C.3 supplies the corruption link and PAU-1.B.2
# the general point about independence among branches.
#
# AN HONEST GAP, KEYED RATHER THAN PAPERED OVER: PAU-3.H.1 names the PROCESSES USED
# TO REMOVE JUDGES as one of its five factors, and the framework gives NO country
# illustration of a removal process anywhere in PAU-3.G.1 or elsewhere. Item 18
# keys that absence instead of inventing one.
#
# Table cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.9", "Independent Judiciaries", 2)

_T_FACT = dict(
    headers=["Judiciary (hypothetical)", "Stated length of a judicial term",
             "Authority to overrule executive and legislative acts",
             "Who decides the removal of a judge"],
    rows=[["Judiciary 1", "15 years", "held and regularly exercised",
           "the legislature, by a two-thirds vote after a formal proceeding"],
          ["Judiciary 2", "4 years", "held on paper but never exercised",
           "the head of government alone"],
          ["Judiciary 3", "20 years", "held and regularly exercised",
           "a panel of senior judges"]])

_T_OVER = dict(
    headers=["Court (hypothetical)", "Executive acts reviewed, 2000-2020",
             "Executive acts overruled, 2000-2020",
             "Judges removed by the executive, 2000-2020"],
    rows=[["Court A", "240", "64", "0"],
          ["Court B", "180", "3", "11"],
          ["Court C", "95", "22", "2"]])

QUESTIONS = [
 dict(q="On what does the framework say the degree of a judiciary's independence from the other branches depends?",
   choices=[
     "the courts' authority to overrule executive and legislative actions, how judicial officials acquire their jobs, the length of judicial terms, the backgrounds judicial officials are expected to have, and the processes used to remove judges",
     "the number of cases the courts hear each year",
     "whether the state is federal or unitary",
     "the size of the highest court and the age of its members",
     "whether the country uses common law or a written constitution"], ans=0,
   why="EK PAU-3.H.1 names exactly these five determinants of the degree of judicial independence. Caseload, territorial structure, court size and legal tradition are not among them, though EK PAU-3.G.1.i does describe one country's use of common law to enforce the rule of law."),
 dict(q="In one country the highest court may set aside a statute or an executive order it finds unlawful; in another it may not. Which of the framework's five determinants of judicial independence does this difference concern?",
   choices=[
     "the amount of authority the courts have to overrule executive and legislative actions",
     "the process by which judicial officials acquire their jobs",
     "the length of judicial terms",
     "the backgrounds judicial officials are expected to have",
     "the processes used to remove judges from their posts"], ans=0,
   why="EK PAU-3.H.1 names the amount of authority the courts have to overrule executive and legislative actions as the first of its five determinants. The other four concern how judges arrive, how long they stay, what they must have studied, and how they can be made to leave."),
 dict(q="In one country judges are chosen by the governing party, and in another by a council that recommends candidates to an elected head of state for confirmation by an elected chamber. Which determinant does this difference concern?",
   choices=[
     "the process by which judicial officials acquire their jobs",
     "the amount of authority the courts have to overrule other branches",
     "the length of judicial terms",
     "the backgrounds judicial officials are expected to have",
     "the processes used to remove judges from their posts"], ans=0,
   why="EK PAU-3.H.1 names the process by which judicial officials acquire their jobs among its five determinants, and EK PAU-3.G.1.a and EK PAU-3.G.1.f supply the two contrasting routes described in the item."),
 dict(q="Which determinant of judicial independence does a fixed fifteen-year appointment, as against a renewable two-year one, most directly concern?",
   choices=[
     "the length of judicial terms",
     "the amount of authority the courts have to overrule other branches",
     "the process by which judicial officials acquire their jobs",
     "the backgrounds judicial officials are expected to have",
     "the processes used to remove judges from their posts"], ans=0,
   why="EK PAU-3.H.1 names the length of judicial terms among its five determinants, and EK PAU-3.G.1.d prints one: Mexico's Supreme Court magistrates serve a term of 15 years. A judge whose reappointment is soon and frequent depends on whoever grants it."),
 dict(q="A state requires every judge to have completed a particular course of legal study before appointment. Which determinant does this concern?",
   choices=[
     "the professional and academic backgrounds judicial officials are expected to have",
     "the length of judicial terms",
     "the processes used to remove judges from their posts",
     "the amount of authority the courts have to overrule other branches",
     "the process by which judicial officials acquire their jobs"], ans=0,
   why="EK PAU-3.H.1 names the professional and academic backgrounds that judicial officials are expected to have among its five determinants, and EK PAU-3.G.1.b gives the framework's instance: Iranian judges must be trained in Islamic Sharia law because the judiciary's major function is to ensure the legal system rests on religious law."),
 dict(q="In one state a judge may be dismissed by the head of government alone; in another only by a formal proceeding before the legislature. Which determinant does this concern?",
   choices=[
     "the processes used to remove judges from their posts",
     "the length of judicial terms",
     "the backgrounds judicial officials are expected to have",
     "the process by which judicial officials acquire their jobs",
     "the amount of authority the courts have to overrule other branches"], ans=0,
   why="EK PAU-3.H.1 names the processes used to remove judges from their posts among its five determinants. Removal is separate from appointment and from term length: a fixed term means little if the officeholder can be dismissed at will inside it."),
 dict(q="According to the framework, how can independent judiciaries strengthen democracy?",
   choices=[
     "by maintaining checks and balances, protecting rights and liberties, establishing the rule of law, and maintaining separation of powers",
     "by increasing the number of cases heard each year",
     "by ensuring that the governing party's programme is enacted quickly",
     "by certifying election results and registering political parties",
     "by appointing members of the upper chamber of the legislature"], ans=0,
   why="EK PAU-3.H.2 names exactly these four contributions. Each is a way of limiting or structuring power rather than of exercising it, which is why the framework attaches them to INDEPENDENT judiciaries specifically."),
 dict(q="A constitutional court annuls an executive decree that exceeded the powers the legislature had delegated. Which of the framework's four contributions of an independent judiciary does this most directly illustrate?",
   choices=[
     "maintaining checks and balances",
     "protecting rights and liberties",
     "establishing the rule of law in commercial disputes",
     "maintaining the separation of powers between levels of government",
     "reducing corruption among electoral officials"], ans=0,
   why="EK PAU-3.H.2 names maintaining checks and balances among the ways independent judiciaries strengthen democracy, and EK PAU-1.B.2 explains why that matters, since independence can prevent any one branch from controlling all governmental power."),
 dict(q="A court strikes down a law banning peaceful assembly. Which of the framework's four contributions does this most directly illustrate?",
   choices=[
     "protecting rights and liberties",
     "maintaining checks and balances between levels of government",
     "establishing the rule of law by publishing its procedures",
     "maintaining separation of powers within the executive branch",
     "certifying the outcome of an election"], ans=0,
   why="EK PAU-3.H.2 names protecting rights and liberties among the ways independent judiciaries strengthen democracy, and EK PAU-1.C.3 adds that independent judiciaries protect individual liberties and civil rights while reducing corruption. EK PAU-3.G.1.i gives one country's Supreme Court that function explicitly."),
 dict(q="A judiciary consistently applies published rules to officials and citizens alike, so that outcomes do not depend on who a party is. Which of the framework's four contributions does this most directly illustrate?",
   choices=[
     "establishing the rule of law",
     "maintaining checks and balances between the chambers of the legislature",
     "protecting rights and liberties of minorities only",
     "maintaining separation of powers among levels of government",
     "reducing the number of cases brought against the government"], ans=0,
   why="EK PAU-3.H.2 names establishing the rule of law among the ways independent judiciaries strengthen democracy, and EK PAU-1.B.1.a describes the rule of law as governance by law rather than by arbitrary decisions of individual officials. Applying the same published rules to everyone is that principle in operation."),
 dict(q="A court refuses to let the executive exercise a power the constitution assigns to the legislature. Which of the framework's four contributions does this most directly illustrate?",
   choices=[
     "maintaining separation of powers",
     "protecting rights and liberties",
     "establishing the rule of law in criminal cases",
     "maintaining checks and balances between the state and its regions",
     "reducing corruption in the civil service"], ans=0,
   why="EK PAU-3.H.2 names maintaining separation of powers among the ways independent judiciaries strengthen democracy, and EK PAU-1.B.2 states that branch independence can prevent any one branch from controlling all governmental power. Returning a power to the branch the constitution assigned it to is that function."),
 dict(q="Which further contribution does the framework attribute to independent judiciaries outside this learning objective?",
   choices=[
     "reducing political corruption, which the framework says inhibits democratization",
     "increasing the number of political parties in the legislature",
     "raising the rate of economic growth",
     "shortening the time an executive spends in office",
     "certifying the results of national elections"], ans=0,
   why="EK PAU-1.C.3 states that political corruption inhibits democratization and that independent judiciaries can reduce such corruption while protecting individual liberties and civil rights. EK PAU-3.G.1.e connects this to Nigeria's effort to reestablish its judiciary's legitimacy and independence by reducing corruption."),
 dict(q="Applying the framework's first determinant to Russia, what does its account imply?",
   choices=[
     "the courts hold the authority constitutionally, but the framework says it has not been used to limit the authority of the governing branches",
     "the courts hold no such authority under the constitution",
     "the courts have used the authority repeatedly against the governing branches",
     "the authority belongs to the Federation Council rather than to the courts",
     "the framework says nothing about that authority in Russia"], ans=0,
   why="EK PAU-3.H.1 makes the amount of authority to overrule executive and legislative actions a determinant of independence, and EK PAU-3.G.1.g states both that Russia's courts constitutionally hold the power of judicial review and that it has not been used to limit the authority of the governing branches. Both halves belong to the assessment."),
 dict(q="Applying the framework's second determinant to China, what does its account imply?",
   choices=[
     "the governing party controls most judicial appointments, so the acquisition process points away from independence",
     "an independent judicial council controls most appointments",
     "judges are elected by the population they serve",
     "judges are appointed by an elected upper chamber alone",
     "the framework does not describe how judges are appointed there"], ans=0,
   why="EK PAU-3.H.1 makes the process by which judicial officials acquire their jobs a determinant of independence, and EK PAU-3.G.1.a states that the Chinese Communist Party controls most judicial appointments and that the judicial system is subservient to its decisions."),
 dict(q="Applying the framework's second determinant to Nigeria, which feature of its appointment process bears on independence?",
   choices=[
     "a judicial council recommends candidates before the head of state appoints and the elected Senate confirms",
     "the governing party controls most appointments",
     "the head of state appoints without any confirmation",
     "judges are appointed by an appointed upper chamber alone",
     "judges are appointed for a term of 15 years"], ans=0,
   why="EK PAU-3.G.1.f states that Nigeria's Supreme Court judges are recommended by a judicial council and appointed by the president with confirmation by the Senate, and EK PAU-3.G.1.e records an effort to reestablish the judiciary's legitimacy and independence. The 15-year term belongs to Mexico under EK PAU-3.G.1.d."),
 dict(q="Which course country's judiciary supplies the framework's only stated figure for the third determinant, the length of judicial terms?",
   choices=[
     "Mexico",
     "Nigeria",
     "Russia",
     "Iran",
     "the United Kingdom"], ans=0,
   why="EK PAU-3.G.1.d states that Mexican Supreme Court magistrates are nominated by the president and approved by the Senate for a term of 15 years, and no other statement in the framework gives a judicial term length for any course country."),
 dict(q="Which course country's judiciary supplies the framework's clearest instance of the fourth determinant, the backgrounds judicial officials are expected to have?",
   choices=[
     "Iran, whose judges must be trained in Islamic Sharia law",
     "Mexico, whose magistrates serve for fifteen years",
     "Nigeria, whose judges are recommended by a judicial council",
     "Russia, whose judges are approved by an appointed chamber",
     "the United Kingdom, whose Supreme Court rules on devolution disputes"], ans=0,
   why="EK PAU-3.H.1 names the professional and academic backgrounds judicial officials are expected to have among its determinants, and EK PAU-3.G.1.b states that Iranian judges must be trained in Islamic Sharia law because the judiciary's major function is to ensure the legal system is based on religious law. The rejected options bear on other determinants."),
 dict(q="The framework names the processes used to remove judges among its determinants of judicial independence. What does it go on to say about removal processes in the course countries?",
   choices=[
     "it gives no country illustration of a judicial removal process anywhere in the course content",
     "it states that judges may be removed only by the legislature in every course country",
     "it states that no judge may be removed in any course country",
     "it states that removal is decided by a supranational court in every course country",
     "it states that every course country uses the same removal process"], ans=0,
   why="EK PAU-3.H.1 lists the processes used to remove judges from their posts as a determinant, but none of the nine sub-points of EK PAU-3.G.1 describes a removal process for any course country, and no other statement supplies one. Asserting a rule about removal in any of the six would go beyond the framework."),
 dict(q="Which evidence would most strongly support a claim that a particular judiciary is independent, on the framework's determinants?",
   choices=[
     "Its judges hold long fixed terms, are chosen through a process no single branch controls, and have repeatedly set aside executive and legislative acts",
     "Its judges hear a large number of cases each year",
     "Its judges are widely respected by the public",
     "Its highest court sits in a purpose-built building",
     "Its judges are drawn from many regions of the country"], ans=0,
   why="EK PAU-3.H.1's determinants are the authority to overrule other branches, the acquisition process, term length, expected backgrounds and removal processes, and the keyed finding reports three of the five at once. Caseload, reputation, premises and geographic origin bear on none of them."),
 dict(q="The table describes three hypothetical judiciaries on the framework's determinants. Which appears LEAST independent?",
   table=_T_FACT,
   choices=[
     "Judiciary 2, which has the shortest stated term, an overruling power never exercised, and judges removable by the head of government alone",
     "Judiciary 1, whose judges may be removed by a legislative proceeding",
     "Judiciary 3, whose judges serve twenty-year terms",
     "None of the three, since independence cannot be judged from a table",
     "All three equally, since each has some authority to overrule"], ans=0,
   why="EK PAU-3.H.1 makes the authority to overrule, the length of terms and the removal process three of its five determinants, and one row is worst on all three at once. EK PAU-3.G.1.g shows the framework treating an unexercised constitutional power as the weaker case."),
 dict(q="Using the same table, which judiciary appears MOST independent on the framework's determinants?",
   table=_T_FACT,
   choices=[
     "Judiciary 3, which has the longest stated term, an overruling power regularly exercised, and removal decided by senior judges rather than by another branch",
     "Judiciary 1, which has a shorter stated term and removal decided by the legislature",
     "Judiciary 2, whose power is held on paper",
     "None of the three, since every judiciary is subordinate to the executive",
     "Both Judiciary 1 and Judiciary 3, since neither is removable by the head of government"], ans=0,
   why="EK PAU-3.H.1's determinants include term length, the authority to overrule and the removal process, and one row leads on all three: the longest term, a power actually used, and a removal decision kept inside the judiciary. Removal by the legislature is a formal process but still one another branch controls."),
 dict(q="According to the same table, the difference between the longest and the shortest stated judicial term is",
   table=_T_FACT,
   choices=[
     "16 years",
     "11 years",
     "5 years",
     "4 years",
     "20 years"], ans=0,
   why="Subtracting the smallest stated term from the largest gives the difference. The alternatives are the gaps between other pairs of rows, one row's term read as though it were a difference, and the largest single value."),
 dict(q="The table reports hypothetical review records for three courts. Which court's record best supports a claim of judicial independence on the framework's determinants?",
   table=_T_OVER,
   choices=[
     "Court A, which overruled the largest share of the executive acts it reviewed and had no judge removed by the executive",
     "Court B, which reviewed the second largest number of executive acts",
     "Court C, which had the fewest executive acts to review",
     "None of the three, since overruling an executive act is not evidence of independence",
     "All three equally, since each overruled at least one executive act"], ans=0,
   why="EK PAU-3.H.1 makes the authority to overrule executive and legislative actions and the processes used to remove judges two of its five determinants. Reading the table as proportions, one row leads on the first and shows nothing at all on the second, which is the combination the determinants point to."),
 dict(q="Using the same table, which court's record most strongly WEAKENS a claim of judicial independence?",
   table=_T_OVER,
   choices=[
     "Court B, which overruled under two percent of the acts it reviewed while eleven of its judges were removed by the executive",
     "Court A, which overruled the largest share of acts reviewed",
     "Court C, which reviewed the fewest acts",
     "None of the three, since removal of judges is irrelevant to independence",
     "All three, since each had at least one judge removed by the executive"], ans=0,
   why="EK PAU-3.H.1 names the processes used to remove judges from their posts among its determinants, so removals by the executive bear directly on the claim. One row combines the smallest share of acts overruled with by far the most such removals, and one row shows none at all."),
 dict(q="According to the same table, the share of reviewed executive acts that the third court overruled was closest to",
   table=_T_OVER,
   choices=[
     "23 percent",
     "27 percent",
     "2 percent",
     "77 percent",
     "95 percent"], ans=0,
   why="Dividing that court's overruled acts by the acts it reviewed gives the share. The alternatives offer another row's share, a third row's share, the complementary share, and the number of acts reviewed read as a percentage."),
 dict(q="Which evidence would most strongly WEAKEN a claim that a particular judiciary is independent?",
   choices=[
     "Judges who ruled against the government were removed shortly afterwards by the officials whose acts they had annulled",
     "The judiciary decided fewer cases last year than the year before",
     "The highest court's decisions are published in full",
     "Judges are required to hold a law degree",
     "The highest court sits in the capital city"], ans=0,
   why="EK PAU-3.H.1 names the processes used to remove judges from their posts among its five determinants, so removal by the very officials a judge ruled against strikes at independence directly. Caseload, publication, a qualification requirement and location bear on none of the five."),
 dict(q="Why does the framework treat judicial independence as a matter of degree resting on five determinants rather than a single yes-or-no property?",
   choices=[
     "because a judiciary can be strong on one determinant and weak on another, as when a court holds a constitutional power it does not use",
     "because independence cannot be assessed at all",
     "because only federal states have independent judiciaries",
     "because the framework treats all five determinants as equivalent to one another",
     "because independence depends solely on the length of judicial terms"], ans=0,
   why="EK PAU-3.H.1 speaks of the DEGREE of independence and lists five separate things it depends on, and EK PAU-3.G.1.g supplies exactly the mixed case, a court with constitutional review authority that has not used it against the governing branches."),
 dict(q="Which comparison of the judiciaries of Mexico and Russia on the framework's determinants is supported?",
   choices=[
     "Both have judges nominated by a president and approved by an upper chamber, but only one of those chambers is elected and only one of the two judiciaries is described as in transition toward greater independence",
     "Both have judges recommended by an independent judicial council",
     "Neither judiciary is described as holding any power of judicial review",
     "Both are described as having used judicial review against the governing branches",
     "Both are described as requiring judges to be trained in religious law"], ans=0,
   why="EK PAU-3.G.1.d has Mexico's magistrates nominated by the president and approved by the elected Senate, EK PAU-3.G.1.h has Russia's judges nominated by the president and approved by the appointed Federation Council, EK PAU-3.G.1.c calls Mexico's judiciary in transition toward independence and effectiveness, and EK PAU-3.G.1.g says Russia's review power has not been used against the governing branches."),
 dict(q="How does the framework's account of judicial independence connect to its account of the branches of government generally?",
   choices=[
     "it states that the branches are more likely to be independent of one another in democratic regimes, and that such independence can prevent any one branch from controlling all governmental power",
     "it states that the judiciary alone can be independent, and that the other branches never are",
     "it states that branch independence exists only in federal states",
     "it states that independence among branches has no bearing on regime type",
     "it states that the judiciary must be subordinate to the legislature in every regime"], ans=0,
   why="EK PAU-1.B.2 states that the branches of national government in democratic regimes are more likely to be independent of one another than in authoritarian regimes, and that independence can serve to prevent any one branch from controlling all governmental power. EK PAU-3.H.2's checks and balances and separation of powers are that idea applied to courts."),
 dict(q="Which summary best combines what the framework says makes a judiciary independent with what it says independence contributes?",
   choices=[
     "How independent a judiciary is depends on five separate features of its powers, its personnel and its tenure, and an independent judiciary strengthens democracy in four named ways",
     "Judicial independence is a single property a judiciary either has or lacks, and it has no bearing on democracy",
     "Judicial independence depends only on how judges are appointed, and it guarantees democracy",
     "Judicial independence is a feature only of common law systems",
     "The framework describes what makes a judiciary independent but says nothing about what independence contributes"], ans=0,
   why="EK PAU-3.H.1 supplies five determinants of the DEGREE of independence and EK PAU-3.H.2 the four ways an independent judiciary can strengthen democracy, namely checks and balances, protection of rights and liberties, establishment of the rule of law, and separation of powers."),
]
