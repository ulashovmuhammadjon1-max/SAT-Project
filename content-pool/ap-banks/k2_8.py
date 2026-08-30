# AP COMPARATIVE GOVERNMENT AND POLITICS 2.8 Judicial Systems
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.G (describe the structure and functions of
# judiciaries). Suggested skill 1.E, Concept Application.
#
# Essential knowledge relied on -- PAU-3.G.1, judiciaries in course countries have
# different functions and use various methods to appoint judges:
#   .a CHINA -- RULE BY LAW (INSTEAD OF RULE OF LAW) means the judicial system is
#      SUBSERVIENT to the decisions of the Chinese Communist Party, WHICH CONTROLS
#      MOST JUDICIAL APPOINTMENTS
#   .b IRAN -- the judiciary's MAJOR FUNCTION is to ensure the legal system is BASED
#      ON RELIGIOUS LAW, so judges must be TRAINED IN ISLAMIC SHARIA LAW; the head
#      of the judiciary is APPOINTED BY THE SUPREME LEADER and can NOMINATE HALF OF
#      THE GUARDIAN COUNCIL with approval by the Majles
#   .c MEXICO -- the judiciary is IN TRANSITION; the Supreme Court has the POWER OF
#      JUDICIAL REVIEW and subsequent constitutional amendments have been
#      implemented WITH THE INTENT to make the system more independent and effective
#   .d MEXICO -- Supreme Court magistrates are NOMINATED BY THE PRESIDENT and
#      APPROVED BY THE SENATE for a term of 15 YEARS
#   .e NIGERIA -- the judiciary has the POWER OF JUDICIAL REVIEW, an effort has been
#      made to REESTABLISH ITS LEGITIMACY AND INDEPENDENCE BY REDUCING CORRUPTION,
#      and under the system of FEDERALISM Islamic Sharia Courts have been
#      established in the north
#   .f NIGERIA -- Supreme Court judges are RECOMMENDED BY A JUDICIAL COUNCIL and
#      APPOINTED BY THE PRESIDENT with CONFIRMATION BY THE SENATE
#   .g RUSSIA -- the government USES THE JUDICIAL SYSTEM TO TARGET OPPOSITION, and
#      although CONSTITUTIONALLY the courts have the power of judicial review, this
#      power HAS NOT BEEN USED to limit the authority of the governing branches
#   .h RUSSIA -- judges are NOMINATED BY THE PRESIDENT and APPROVED BY THE
#      FEDERATION COUNCIL
#   .i UNITED KINGDOM -- the judicial system uses COMMON LAW to enforce the RULE OF
#      LAW; major functions of the Supreme Court include serving as the FINAL COURT
#      OF APPEALS, PROTECTING HUMAN AND CIVIL RIGHTS AND LIBERTIES, and RULING ON
#      DEVOLUTION DISPUTES
#
# TWO DISTINCTIONS THE FRAMEWORK DRAWS AND THE ITEMS KEEP
#   1. RULE BY LAW is not RULE OF LAW. PAU-3.G.1.a says so in parentheses, and
#      PAU-1.B.1.a defines the rule of law as governance by law rather than by
#      arbitrary decisions of individual officials. Item 1 keys the difference.
#   2. Russia's courts HOLD the power of judicial review constitutionally and have
#      NOT USED it against the governing branches. PAU-3.G.1.g states both halves,
#      so an item asking simply whether Russian courts have judicial review would
#      have two defensible answers. Items 12 and 27 ask which half is meant.
#
# Mexico's 15-year Supreme Court term is one of very few precise numbers in Units
# 1-3 (AP_COMP_GOV_CED.md note 9); item 7 keys it and item 26 keys its rarity.
#
# Table cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.8", "Judicial Systems", 2)

_T_JREV = dict(
    headers=["Court (hypothetical)", "Laws or executive acts struck down, 2000-2020",
             "Cases brought against the government, 2000-2020",
             "Share of those cases decided against the government (percent)"],
    rows=[["Court I", "41", "310", "28"],
          ["Court II", "0", "96", "2"],
          ["Court III", "17", "204", "19"]])

_T_APPT = dict(
    headers=["Court (hypothetical)", "How members reach the bench"],
    rows=[["Court W", "nominated by the head of state and approved by the elected upper chamber for a term of 15 years"],
          ["Court X", "recommended by a judicial council, appointed by the head of state, and confirmed by the elected upper chamber"],
          ["Court Y", "nominated by the head of state and approved by an appointed upper chamber"],
          ["Court Z", "most appointments controlled by the single governing party"]])

QUESTIONS = [
 dict(q="The framework describes one course country's system as resting on rule BY law instead of rule OF law. What does it say that means there?",
   choices=[
     "the judicial system is subservient to the decisions of the governing party",
     "the courts may strike down any law the legislature passes",
     "judges are elected by the population they serve",
     "the courts apply religious law rather than statute",
     "the courts serve as the final court of appeals for the whole state"], ans=0,
   why="EK PAU-3.G.1.a states that in China rule by law, instead of rule of law, means the judicial system is subservient to the decisions of the Chinese Communist Party. EK PAU-1.B.1.a defines the rule of law as governance by law rather than by arbitrary decisions of individual officials, which is the contrast the parenthesis draws."),
 dict(q="Who does the framework say controls most judicial appointments in China?",
   choices=[
     "the Chinese Communist Party",
     "the National People's Congress in full session",
     "the premier, subject to confirmation by the legislature",
     "a judicial council independent of the party",
     "the head of the judiciary, appointed for a fixed term"], ans=0,
   why="EK PAU-3.G.1.a states that the Chinese Communist Party controls most judicial appointments, alongside the judicial system's subservience to the party's decisions. EK PAU-4.A.2 explains that only that party may control governing power."),
 dict(q="What does the framework identify as the major function of Iran's judiciary?",
   choices=[
     "ensuring that the legal system is based on religious law",
     "serving as the final court of appeals for devolution disputes",
     "striking down laws that conflict with the constitution",
     "supervising the conduct of national elections",
     "confirming the appointment of cabinet ministers"], ans=0,
   why="EK PAU-3.G.1.b states that the Iranian judiciary's major function is to ensure that the legal system is based on religious law. Devolution disputes belong to the United Kingdom's Supreme Court under EK PAU-3.G.1.i, and confirming ministers to the Majles under EK PAU-3.E.1.b."),
 dict(q="What qualification does the framework say Iranian judges must have?",
   choices=[
     "training in Islamic Sharia law",
     "election by the population of their district",
     "recommendation by an independent judicial council",
     "prior service in the legislature",
     "approval by an appointed upper chamber"], ans=0,
   why="EK PAU-3.G.1.b states that because the judiciary's major function is to ensure the legal system is based on religious law, judges must be trained in Islamic Sharia law. The rejected qualifications describe the appointment routes of other course countries."),
 dict(q="What does the framework say about the head of Iran's judiciary?",
   choices=[
     "the officeholder is appointed by the Supreme Leader and can nominate half of the Guardian Council with approval by the Majles",
     "the officeholder is elected by the Majles for a fixed term",
     "the officeholder appoints the Supreme Leader",
     "the officeholder is recommended by a judicial council and confirmed by an upper chamber",
     "the officeholder nominates the whole Guardian Council without any approval"], ans=0,
   why="EK PAU-3.G.1.b states that the head of the judiciary is appointed by the Supreme Leader and can nominate half of the Guardian Council with approval by the Majles, and EK PAU-3.C.2.b has the Supreme Leader appointing the other half. Half in both places, never the whole body."),
 dict(q="How does the framework characterize Mexico's judiciary?",
   choices=[
     "in transition, with a Supreme Court holding the power of judicial review and constitutional amendments intended to make the system more independent and effective",
     "fully subservient to the governing party, which controls most appointments",
     "constitutionally empowered to review but never using that power against the governing branches",
     "required to ensure that the legal system rests on religious law",
     "organized around common law and serving as the final court of appeals"], ans=0,
   why="EK PAU-3.G.1.c states that the Mexican judiciary is in transition, that the Supreme Court has the power of judicial review, and that subsequent constitutional amendments have been implemented with the intent to make the system more independent and effective. The rejected descriptions belong to China, Russia, Iran and the United Kingdom."),
 dict(q="How does the framework describe the selection and tenure of Mexico's Supreme Court magistrates?",
   choices=[
     "nominated by the president and approved by the Senate for a term of 15 years",
     "recommended by a judicial council and confirmed by the Senate for life",
     "nominated by the president and approved by an appointed upper chamber",
     "appointed by the governing party without confirmation",
     "elected directly by voters for a term of six years"], ans=0,
   why="EK PAU-3.G.1.d states that Mexican Supreme Court magistrates are nominated by the president and approved by the Senate for a term of 15 years. The judicial council route is Nigeria's under EK PAU-3.G.1.f and the appointed upper chamber is Russia's under EK PAU-3.G.1.h."),
 dict(q="What does the framework say about the independence of Nigeria's judiciary?",
   choices=[
     "it holds the power of judicial review, and an effort has been made to reestablish its legitimacy and independence by reducing corruption",
     "it is subservient to the decisions of the governing party",
     "it holds no power of judicial review",
     "it exists to ensure that the legal system rests on religious law throughout the country",
     "it has never been regarded as lacking legitimacy or independence"], ans=0,
   why="EK PAU-3.G.1.e states that the Nigerian judiciary has the power of judicial review and that an effort has been made to reestablish its legitimacy and independence by reducing corruption. EK PAU-1.C.3 supplies the connection, that independent judiciaries can reduce corruption while protecting liberties and civil rights."),
 dict(q="Under what arrangement does the framework say Islamic Sharia Courts have been established in the north of Nigeria?",
   choices=[
     "under the country's system of federalism",
     "under a treaty with a supranational organization",
     "under a constitutional amendment abolishing judicial review",
     "under the supervision of a national vetting council",
     "under the direct control of the president"], ans=0,
   why="EK PAU-3.G.1.e states that under the system of federalism, Islamic Sharia Courts have been established in the north of Nigeria, and EK PAU-2.A.1 lists Nigeria among the federal states. A legal order differing by region is what dividing power among levels of government makes possible."),
 dict(q="How does the framework describe the appointment of Nigeria's Supreme Court judges?",
   choices=[
     "recommended by a judicial council, appointed by the president, and confirmed by the Senate",
     "nominated by the president and approved by the Senate for a term of 15 years",
     "nominated by the president and approved by an appointed upper chamber",
     "appointed by the head of the judiciary with approval by the legislature",
     "controlled for the most part by the governing party"], ans=0,
   why="EK PAU-3.G.1.f states that Nigeria's Supreme Court judges are recommended by a judicial council and appointed by the president with confirmation by the Senate. The three-step route is what distinguishes it from Mexico's two-step route at EK PAU-3.G.1.d."),
 dict(q="What does the framework say about how Russia's government uses the judicial system?",
   choices=[
     "it uses the judicial system to target opposition",
     "it uses the judicial system to review its own legislation for constitutionality",
     "it has abolished the courts' power of judicial review by amendment",
     "it requires the courts to apply religious law",
     "it allows a judicial council to recommend all appointments"], ans=0,
   why="EK PAU-3.G.1.g states that Russia's government uses the judicial system to target opposition. The same statement retains the courts' constitutional power of judicial review, so the framework is not describing the abolition of that power."),
 dict(q="Which statement about judicial review in Russia is consistent with the framework?",
   choices=[
     "the courts hold the power constitutionally, but it has not been used to limit the authority of the governing branches",
     "the courts have no such power under the constitution",
     "the courts have used the power repeatedly to limit the governing branches",
     "the power belongs to the Federation Council rather than to the courts",
     "the power was transferred to the president by amendment"], ans=0,
   why="EK PAU-3.G.1.g states both halves in one sentence: although constitutionally the courts have the power of judicial review, this power has not been used to limit the authority of the governing branches. An item asking only whether the courts have judicial review would therefore have two defensible answers."),
 dict(q="How does the framework describe the appointment of judges in Russia?",
   choices=[
     "nominated by the president and approved by the Federation Council",
     "nominated by the president and approved by the state Duma",
     "recommended by a judicial council and confirmed by an elected upper chamber",
     "appointed by regional governors and regional legislatures",
     "controlled for the most part by the governing party"], ans=0,
   why="EK PAU-3.G.1.h states that Russia's judges are nominated by the president and approved by the Federation Council, which EK PAU-3.E.1.e describes as appointed rather than elected. Confirming the prime minister, not judges, is the Duma's role."),
 dict(q="What does the framework say the United Kingdom's judicial system uses, and to what end?",
   choices=[
     "common law, to enforce the rule of law",
     "religious law, to ensure the legal system rests on scripture",
     "party directives, to keep the courts aligned with the governing party",
     "regional codes, to allow each nation of the state its own legal order",
     "a written constitution, to permit the annulment of any statute"], ans=0,
   why="EK PAU-3.G.1.i states that the United Kingdom's judicial system uses common law to enforce the rule of law. EK PAU-1.B.1.a makes adherence to the rule of law one of the framework's indicators of a regime's place on the democratic-authoritarian scale."),
 dict(q="Which set of functions does the framework assign to the United Kingdom's Supreme Court?",
   choices=[
     "serving as the final court of appeals, protecting human and civil rights and liberties, and ruling on devolution disputes",
     "striking down statutes passed by the elected chamber and appointing members of the upper chamber",
     "vetting candidates for the legislature and reviewing its laws",
     "approving treaties and troop deployment",
     "nominating half of a constitutional vetting council"], ans=0,
   why="EK PAU-3.G.1.i names these three as major functions of the United Kingdom's Supreme Court. The rejected sets belong to Iran's Guardian Council, Russia's Federation Council and Iran's head of the judiciary."),
 dict(q="Which comparison of the judiciaries of Mexico, Nigeria and Russia is consistent with the framework?",
   choices=[
     "All three are described as holding a power of judicial review, but only in the third is that power described as not having been used against the governing branches",
     "None of the three is described as holding a power of judicial review",
     "Only the first is described as holding a power of judicial review",
     "All three are described as having used judicial review to limit the governing branches",
     "All three are described as applying religious law"], ans=0,
   why="EK PAU-3.G.1.c gives Mexico's Supreme Court the power of judicial review, EK PAU-3.G.1.e gives Nigeria's judiciary the same power, and EK PAU-3.G.1.g gives Russia's courts the power constitutionally while stating that it has not been used to limit the authority of the governing branches."),
 dict(q="Which comparison of how Mexico and Nigeria fill their highest courts is consistent with the framework?",
   choices=[
     "Both involve the president and an elected Senate, but only one inserts a judicial council's recommendation before the president acts",
     "Both involve a judicial council's recommendation before the president acts",
     "Neither involves the legislature at any stage",
     "One involves an appointed upper chamber and the other an elected one",
     "Both give the president the power to appoint without any confirmation"], ans=0,
   why="EK PAU-3.G.1.d has Mexico's magistrates nominated by the president and approved by the Senate, while EK PAU-3.G.1.f has Nigeria's judges recommended by a judicial council, appointed by the president and confirmed by the Senate. EK PAU-3.E.1.c and EK PAU-3.E.1.d describe both Senates as elected."),
 dict(q="Which comparison of how Mexico and Russia fill their highest courts is consistent with the framework?",
   choices=[
     "In both the head of state nominates and an upper chamber approves, but one of those chambers is elected and the other appointed",
     "In both the head of state appoints without any confirmation",
     "In both a judicial council recommends candidates first",
     "In both the upper chamber is elected",
     "In both judges are elected directly by voters"], ans=0,
   why="EK PAU-3.G.1.d has Mexico's president nominating and the Senate approving, and EK PAU-3.G.1.h has Russia's president nominating and the Federation Council approving. EK PAU-3.E.1.c calls Mexico's Senate elected and EK PAU-3.E.1.e calls the Federation Council appointed, which is where the two routes part."),
 dict(q="Which comparison of what the judiciaries of China and Iran are subordinate to is consistent with the framework?",
   choices=[
     "One is described as subservient to the decisions of the governing party, while the other exists chiefly to ensure the legal system rests on religious law",
     "Both are described as subservient to the decisions of a governing party",
     "Both are described as ensuring the legal system rests on religious law",
     "One is subordinate to an elected legislature and the other to an appointed upper chamber",
     "Neither is described as subordinate to any other institution"], ans=0,
   why="EK PAU-3.G.1.a states that China's judicial system is subservient to the decisions of the Chinese Communist Party, and EK PAU-3.G.1.b states that the Iranian judiciary's major function is to ensure the legal system is based on religious law. Both are constrained, and by different things."),
 dict(q="The table reports hypothetical records for three high courts. Which court's record best matches the framework's description of a court holding the power of judicial review constitutionally without using it against the governing branches?",
   table=_T_JREV,
   choices=[
     "Court II, which struck down nothing in twenty years and decided two percent of cases against the government",
     "Court I, which struck down forty-one laws or acts",
     "Court III, which struck down seventeen laws or acts",
     "None of the three, since a court that never strikes anything down cannot hold the power",
     "All three equally, since each heard cases against the government"], ans=0,
   why="EK PAU-3.G.1.g states that although constitutionally the courts have the power of judicial review, this power has not been used to limit the authority of the governing branches. A court that hears such cases and never decides against the government is that description in data, and holding a power is not the same as exercising it."),
 dict(q="Using the same table, which court's record best matches the framework's description of a judiciary that both holds and exercises the power of judicial review?",
   table=_T_JREV,
   choices=[
     "Court I, which struck down the most laws or acts and decided the largest share of cases against the government",
     "Court II, which struck down none",
     "Court III, which decided the smallest share of cases against the government among those that struck anything down",
     "None of the three, since exercising judicial review cannot be observed",
     "All three, since each has the power under its constitution"], ans=0,
   why="EK PAU-3.G.1.c and EK PAU-3.G.1.e describe judiciaries holding the power of judicial review, and exercising it means deciding against the government at least sometimes. One row leads both on the count of laws struck down and on the share of cases decided against the government."),
 dict(q="According to the same table, the total number of laws or executive acts struck down across the three courts is",
   table=_T_JREV,
   choices=[
     "58",
     "41",
     "17",
     "24",
     "610"], ans=0,
   why="Adding the first numeric column across the three rows gives the total. The alternatives arise from reading a single row, from subtracting one row from another, and from adding a different column altogether."),
 dict(q="The table describes how members reach four hypothetical high courts. Which one matches the framework's description of Mexico's Supreme Court?",
   table=_T_APPT,
   choices=[
     "Court W, whose members are nominated by the head of state and approved by the elected upper chamber for a term of 15 years",
     "Court X, whose members are recommended by a judicial council first",
     "Court Y, whose approving chamber is appointed",
     "Court Z, whose appointments are controlled by a single governing party",
     "None of the four, since the framework states no term length for any court"], ans=0,
   why="EK PAU-3.G.1.d states that Mexican Supreme Court magistrates are nominated by the president and approved by the Senate for a term of 15 years, and EK PAU-3.E.1.c describes that Senate as elected. The framework does state this term length, which is why the last option fails."),
 dict(q="Using the same table, which court matches the framework's description of Nigeria's Supreme Court?",
   table=_T_APPT,
   choices=[
     "Court X, whose members are recommended by a judicial council, appointed by the head of state, and confirmed by the elected upper chamber",
     "Court W, whose members are nominated by the head of state and approved for a fixed term of years",
     "Court Y, whose approving chamber is appointed rather than elected",
     "Court Z, whose appointments are controlled by a single governing party",
     "None of the four, since the framework describes no confirmation stage there"], ans=0,
   why="EK PAU-3.G.1.f states that Nigeria's Supreme Court judges are recommended by a judicial council and appointed by the president with confirmation by the Senate, and EK PAU-3.E.1.d describes that Senate as elected. The judicial council step is what separates this route from Mexico's."),
 dict(q="Using the same table, which court matches the framework's description of Russia's judiciary?",
   table=_T_APPT,
   choices=[
     "Court Y, whose members are nominated by the head of state and approved by an appointed upper chamber",
     "Court W, whose approving chamber is elected",
     "Court X, whose members are recommended by a judicial council first",
     "Court Z, whose appointments are controlled by a single governing party",
     "None of the four, since Russian judges are elected"], ans=0,
   why="EK PAU-3.G.1.h states that Russia's judges are nominated by the president and approved by the Federation Council, and EK PAU-3.E.1.e describes the Federation Council as appointed. The appointed approving chamber is what distinguishes this route from Mexico's and Nigeria's."),
 dict(q="Mexico's 15-year Supreme Court term is unusual in the framework's account of Units 1 through 3 because",
   choices=[
     "the framework states very few precise numbers about the course countries' institutions",
     "no other course country has a judiciary",
     "the framework states a term length for every court in every course country",
     "it is the only number of any kind printed anywhere in the framework",
     "it is stated only in an optional instructional activity rather than in the course content"], ans=0,
   why="EK PAU-3.G.1.d prints the 15-year figure, and the framework's other precise numbers in these units are few: Iran's two 4-year presidential terms, China's at least 55 recognized ethnic minorities, Nigeria's more than 250 ethnic groups and 36 states, and ethnic Russians at more than 80 percent. It is course content, not an optional activity."),
 dict(q="A student asks whether Russia's courts have the power of judicial review. Why does the question need to be made more precise before it can be answered from the framework?",
   choices=[
     "because the framework says the courts hold that power constitutionally and also says it has not been used to limit the governing branches, so the answer depends on which is being asked",
     "because the framework says nothing about judicial review in Russia",
     "because the framework says the power was abolished by amendment",
     "because judicial review exists only in federal states",
     "because the framework describes judicial review only in common law systems"], ans=0,
   why="EK PAU-3.G.1.g states both halves in one sentence, so a question about the power on paper and a question about the power in practice have different answers. This is the same form-against-practice split EK PAU-3.E.1.a and EK PAU-3.F.1.a draw for China's legislature."),
 dict(q="What does the judicial council step in Nigeria's appointment process add, compared with a route in which the head of state nominates directly?",
   choices=[
     "a recommendation stage that precedes the head of state's appointment, in addition to the legislature's confirmation",
     "a power for the legislature to appoint judges without the head of state",
     "a requirement that judges be trained in religious law",
     "a fixed term of 15 years for each judge",
     "a right for voters to elect judges directly"], ans=0,
   why="EK PAU-3.G.1.f states that Nigeria's Supreme Court judges are recommended by a judicial council and appointed by the president with confirmation by the Senate, so the council acts before the president rather than replacing any stage. EK PAU-3.G.1.e connects that structure to the effort to reestablish the judiciary's legitimacy and independence."),
 dict(q="Which of the framework's descriptions shows a judiciary whose composition is controlled by an institution outside the courts and outside the legislature?",
   choices=[
     "a system in which the governing party controls most judicial appointments",
     "a system in which the head of state nominates and an elected chamber approves",
     "a system in which a judicial council recommends and an elected chamber confirms",
     "a system in which the highest court serves as the final court of appeals",
     "a system in which the highest court rules on devolution disputes"], ans=0,
   why="EK PAU-3.G.1.a states that the Chinese Communist Party controls most judicial appointments, and EK PAU-4.A.2 makes that party the only one permitted to control governing power. The rejected descriptions run through a head of state, a legislature or a judicial council, which are state institutions."),
 dict(q="Taking the framework's account of the six judiciaries together, which summary is most accurate?",
   choices=[
     "Judiciaries differ in function and in how judges are appointed, and the framework describes some as constrained by a party or by religious law and others as exercising judicial review or enforcing the rule of law",
     "All six judiciaries have identical functions and appointment methods",
     "None of the six judiciaries holds any power of judicial review",
     "All six judiciaries are described as fully independent of the other branches",
     "The framework describes only the appointment of judges and not their functions"], ans=0,
   why="EK PAU-3.G.1 opens by saying judiciaries in course countries have different functions and use various methods to appoint judges, and its nine sub-points range from subservience to a party, through a religious mission, to judicial review and common law enforcement of the rule of law."),
]
