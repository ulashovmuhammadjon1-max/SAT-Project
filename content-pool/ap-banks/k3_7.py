# AP COMPARATIVE GOVERNMENT AND POLITICS 3.7 Civil Rights and Civil Liberties
# CED effective Fall 2026, Unit 3 Political Culture and Participation. Enduring
# understanding DEM-1; learning objective DEM-1.C (explain the extent to which
# civil rights and civil liberties are protected or restricted in different
# regimes). Suggested skill 4.A, Source Analysis.
#
# Essential knowledge relied on:
#   DEM-1.C.1  PROTECTION OF KEY CIVIL LIBERTIES DIFFERS ACROSS THE SIX COURSE
#              COUNTRIES
#   DEM-1.C.2  BOTH democratic and authoritarian regimes impose constraints on the
#              media TO PROTECT CITIZENS AND MAINTAIN ORDER, but democratic regimes
#              generally tolerate a HIGH DEGREE OF MEDIA FREEDOM to encourage citizen
#              control of the political agenda and check political power and
#              corruption
#   DEM-1.C.3  STRONGER AUTHORITARIAN REGIMES MONITOR AND RESTRICT CITIZENS' MEDIA
#              ACCESS to a greater degree to MAINTAIN POLITICAL CONTROL:
#     .a China's GREAT FIREWALL, limiting POLITICAL CRITICISM ON SOCIAL MEDIA
#     .b the IRANIAN COURT's SUSPENSION OR REVOCATION OF MEDIA LICENSES WHEN A JURY
#        FINDS OWNERS GUILTY of publishing ANTI-RELIGIOUS MATERIAL or INFORMATION
#        DETRIMENTAL TO THE NATIONAL INTEREST
#     .c the RUSSIAN government's NATIONALIZATION OF MOST BROADCAST MEDIA and RIGID
#        CONTROLS ON OPPOSITION NEWS SEGMENTS
#   DEM-1.C.4  a government is TRANSPARENT when it allows information about
#              government and policy making to CIRCULATE OPENLY; authoritarian
#              regimes tend to prefer SECRET OR CLOSED PROCEEDINGS TO MAXIMIZE ORDER
#   DEM-1.C.5  COMPETITIVE AUTHORITARIAN regimes act as a HYBRID; RUSSIA is
#              characterized as a competitive authoritarian regime OR ILLIBERAL
#              DEMOCRACY, holding CONTESTED ELECTIONS with LIMITED COMPETITIVENESS
#              and providing MINIMAL CIVIL LIBERTY PROTECTIONS and GOVERNMENTAL
#              TRANSPARENCY
#   DEM-1.C.6  comparing data showing how far governments protect or restrict CIVIL
#              LIBERTIES OVER TIME can determine REGIME PLACEMENT ON AN
#              AUTHORITARIAN/DEMOCRATIC SCALE
#
# Supporting statements, named in the verifier's claims: PAU-1.C.1.e (protected
# civil rights and liberties among democratization's aims), IEF-1.B.3 (restrictions
# on NGOs highlight violations of civil liberties protected under foundational
# documents), PAU-3.G.1.i (a Supreme Court protecting human and civil rights and
# liberties), LEG-1.C.3 (reform pressure creating institutions that protect civil
# liberties), DEM-2.B.4.a (a vetting body reducing electoral competition and
# representation).
#
# Topic 1.3 also draws on DEM-1.C.2 through DEM-1.C.6 for the democratic-
# authoritarian scale. This module deliberately keys the OTHER halves of those
# statements -- the stated PURPOSE of media constraint in both regime types, the
# detail of each of the three country mechanisms, transparency as applied rather
# than defined, and the over-time method of DEM-1.C.6 -- so the two topics test
# different things from the same sentences.
#
# Table figures and cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("3.7", "Civil Rights and Civil Liberties", 3)

_T_LIB = dict(
    headers=["Country (hypothetical)", "Civil liberties protection score, 2010 (0 to 100)",
             "Civil liberties protection score, 2020 (0 to 100)",
             "Independent news outlets operating in 2020"],
    rows=[["Country A", "78", "81", "240"],
          ["Country B", "44", "22", "31"],
          ["Country C", "61", "58", "96"]])

_T_MECH = dict(
    headers=["Restriction described (hypothetical case)", "Mechanism used"],
    rows=[["Case 1", "a national filtering system that limits political criticism on social media"],
          ["Case 2", "courts suspending or revoking media licences after a jury finds owners guilty of publishing certain material"],
          ["Case 3", "state ownership of most broadcast outlets, with rigid control of opposition news segments"],
          ["Case 4", "an independent regulator fining an outlet for breaching a published accuracy code"]])

_T_TRANS = dict(
    headers=["Government (hypothetical)", "Cabinet decisions published within a month (percent)",
             "Freedom-of-information requests granted (percent)",
             "Legislative committee sessions held in public (percent)"],
    rows=[["Government D", "86", "74", "91"],
          ["Government E", "9", "12", "6"]])

QUESTIONS = [
 dict(q="What does the framework say about the protection of key civil liberties among the six course countries?",
   choices=[
     "it differs across the six",
     "it is identical in all six",
     "it exists only in the three that are federal",
     "it exists only in the three that are unitary",
     "the framework makes no comparison among the six on this point"], ans=0,
   why="EK DEM-1.C.1 states that protection of key civil liberties differs across the six course countries, which is why the rest of the learning objective proceeds country by country rather than by a single rule."),
 dict(q="What purpose does the framework attribute to the media constraints imposed in BOTH democratic and authoritarian regimes?",
   choices=[
     "to protect citizens and maintain order",
     "to increase the profitability of state-owned outlets",
     "to satisfy the requirements of a supranational organization",
     "to raise turnout at national elections",
     "to reduce the number of political parties"], ans=0,
   why="EK DEM-1.C.2 states that both democratic and authoritarian regimes impose constraints on the media to protect citizens and maintain order. The purpose clause is the framework's own and applies to both types, which is why the presence of a constraint identifies neither."),
 dict(q="How does the framework describe China's Great Firewall?",
   choices=[
     "a use of the firewall to limit political criticism on social media",
     "a system of court-ordered licence suspensions following jury verdicts",
     "state ownership of most broadcast outlets",
     "an independent regulator enforcing an accuracy code",
     "a ban on all foreign-owned newspapers"], ans=0,
   why="EK DEM-1.C.3.a describes the Chinese Communist Party's use of the Great Firewall to limit political criticism on social media. The rejected mechanisms are the framework's descriptions of Iran and Russia, and two that appear nowhere in it."),
 dict(q="How does the framework describe media restriction in Iran?",
   choices=[
     "courts suspending or revoking media licences when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest",
     "a national filtering system limiting political criticism on social media",
     "state ownership of most broadcast outlets with control of opposition news segments",
     "a licensing body appointed by an independent commission",
     "a constitutional prohibition on privately owned media"], ans=0,
   why="EK DEM-1.C.3.b describes the Iranian court's suspension or revocation of media licenses when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest. Both the jury step and the two grounds are the framework's."),
 dict(q="How does the framework describe media restriction in Russia?",
   choices=[
     "nationalization of most broadcast media and rigid controls on opposition news segments",
     "a national filtering system limiting political criticism on social media",
     "court-ordered licence revocation following a jury verdict",
     "a requirement that every outlet be owned by a registered political party",
     "an independent regulator enforcing an accuracy code"], ans=0,
   why="EK DEM-1.C.3.c describes the Russian government's nationalization of most broadcast media and rigid controls on opposition news segments. The rejected mechanisms belong to China and Iran or appear nowhere in the framework."),
 dict(q="Which comparison of the framework's three media-restriction examples is accurate?",
   choices=[
     "One works through network filtering, one through court-ordered licensing decisions, and one through state ownership of broadcasters",
     "All three work through state ownership of broadcasters",
     "All three work through court-ordered licensing decisions",
     "All three work through network filtering",
     "The framework describes only one media-restriction mechanism"], ans=0,
   why="EK DEM-1.C.3.a, .b and .c describe three different instruments: a firewall limiting political criticism on social media, courts suspending or revoking licences after a jury verdict, and nationalization of most broadcast media with control of opposition news segments."),
 dict(q="What does the framework say stronger authoritarian regimes do, and why?",
   choices=[
     "they monitor and restrict citizens' media access to a greater degree, in order to maintain political control",
     "they withdraw entirely from the regulation of media",
     "they transfer media regulation to an independent commission",
     "they subsidize opposition outlets to demonstrate tolerance",
     "they abolish state ownership of broadcasters"], ans=0,
   why="EK DEM-1.C.3 introduces its three country examples with the statement that stronger authoritarian regimes monitor and restrict citizens' media access to a greater degree to maintain political control. The comparison is one of degree, since EK DEM-1.C.2 has both regime types constraining media."),
 dict(q="A government publishes the analyses behind its decisions, holds committee sessions in public, and answers requests for official records. In the framework's terms this government is",
   choices=[
     "transparent, since it allows information about government and policy making to circulate openly",
     "legitimate, since its constituents must accept its right to rule",
     "sovereign, since it exercises legal authority over its territory",
     "federal, since it distributes power among levels of government",
     "consolidated, since it is unlikely to revert to authoritarianism"], ans=0,
   why="EK DEM-1.C.4 defines a transparent government as one that allows information about government and policy making to circulate openly. The rejected terms are EK LEG-1.A.1's legitimacy, EK PAU-1.A.4's sovereignty, EK PAU-2.A.1's federalism and EK PAU-1.C.5's consolidation."),
 dict(q="A second government takes its decisions in unminuted meetings, refuses requests for official records, and publishes only outcomes. What does the framework say about regimes that prefer such proceedings?",
   choices=[
     "authoritarian regimes tend to prefer secret or closed proceedings in order to maximize order",
     "democratic regimes tend to prefer secret or closed proceedings in order to maximize order",
     "both regime types prefer closed proceedings equally",
     "no regime prefers closed proceedings",
     "closed proceedings are required by supranational organizations"], ans=0,
   why="EK DEM-1.C.4 states that authoritarian regimes tend to prefer secret or closed proceedings to maximize order, having defined transparency as the open circulation of information about government and policy making. The word 'tend' keeps the claim a tendency rather than a rule."),
 dict(q="Besides 'competitive authoritarian regime', what alternative description does the framework give for the same regime?",
   choices=[
     "illiberal democracy",
     "consolidated democracy",
     "one-party state",
     "military regime",
     "theocracy"], ans=0,
   why="EK DEM-1.C.5 states that Russia is characterized as a competitive authoritarian regime or illiberal democracy, offering the two labels for the same case. The rejected terms are separate types on EK PAU-1.B.3's list."),
 dict(q="Which feature of a competitive authoritarian regime does the framework name that bears directly on this topic?",
   choices=[
     "it provides minimal civil liberty protections",
     "it holds no elections of any kind",
     "it guarantees a high degree of media freedom",
     "it transfers civil liberties questions to a supranational court",
     "it has no written constitution"], ans=0,
   why="EK DEM-1.C.5 states that such a regime holds contested elections with limited degrees of competitiveness while providing minimal civil liberty protections and governmental transparency. The civil liberties clause is what connects the classification to this learning objective."),
 dict(q="What kind of comparison does the framework say can determine a regime's placement on an authoritarian-democratic scale?",
   choices=[
     "comparing data on the extent to which governments protect or restrict civil liberties over time",
     "comparing the number of political parties registered in each country",
     "comparing the size of each country's legislature",
     "comparing the length of each country's constitution",
     "comparing each country's rate of economic growth"], ans=0,
   why="EK DEM-1.C.6 states that comparing data showing the extent to which governments protect or restrict civil liberties over time can determine regime placement on an authoritarian/democratic scale. Party counts, chamber sizes and growth rates are not offered for this purpose."),
 dict(q="Why does the framework's method for placing regimes require data OVER TIME rather than a single reading?",
   choices=[
     "because placement on a scale is a matter of degree that can move, and a single reading shows a level without showing direction",
     "because civil liberties cannot be measured at any single moment",
     "because the framework compares only countries that have changed regime type",
     "because a single reading is always inaccurate",
     "because the scale applies only to regimes that are democratizing"], ans=0,
   why="EK DEM-1.C.6 specifies comparing data over time, and EK PAU-1.B.1 treats the democratic-authoritarian classification as a matter of degree along several indicators. EK PAU-1.C.4's warning that democratization can stall or be reversed is why direction matters as well as level."),
 dict(q="Which of democratization's aims does the framework state in terms of civil rights and liberties?",
   choices=[
     "protected civil rights and liberties",
     "a larger legislature",
     "a longer term for the head of government",
     "a unitary rather than a federal structure",
     "a higher rate of economic growth"], ans=0,
   why="EK PAU-1.C.1.e names protected civil rights and liberties among the outcomes democratization aims at over time, alongside universal suffrage, greater transparency, equal treatment and the establishment of the rule of law."),
 dict(q="What does the framework say the placing of restrictions on NGOs and civil society tends to do?",
   choices=[
     "it tends to highlight violations of civil liberties protected under foundational documents",
     "it tends to increase the protection of civil liberties",
     "it tends to be invisible to citizens and outside observers",
     "it tends to occur only where no foundational document exists",
     "it tends to raise the number of civil society organizations"], ans=0,
   why="EK IEF-1.B.3 states that across course countries, restrictions on NGOs and civil society tend to highlight violations of civil liberties protected under foundational documents. The restriction draws attention to the protection it cuts against."),
 dict(q="Which court function does the framework name that bears directly on civil liberties?",
   choices=[
     "protecting human and civil rights and liberties, among the major functions of the United Kingdom's Supreme Court",
     "vetting candidates for the legislature",
     "approving budget legislation and troop deployment",
     "assuming the legislature's duties between sessions",
     "confirming presidential appointments to the cabinet"], ans=0,
   why="EK PAU-3.G.1.i names serving as the final court of appeals, protecting human and civil rights and liberties, and ruling on devolution disputes among the major functions of the United Kingdom's Supreme Court. The rejected functions belong to Iran's Guardian Council, Russia's Federation Council, China's NPC Standing Committee and Iran's Majles."),
 dict(q="How does the framework connect civil society pressure to civil liberties?",
   choices=[
     "internal reform pressure from citizen protest groups and civil society can lead to new institutions or policies that protect civil liberties",
     "civil society organizations enact civil liberties protections themselves",
     "civil society pressure has no bearing on civil liberties",
     "civil liberties protections are created only by supranational organizations",
     "civil liberties protections are created only where a state is federal"], ans=0,
   why="EK LEG-1.C.3 states that internal reform pressure from citizen protest groups and civil society can lead to the creation of new political institutions or policies to protect civil liberties, improve transparency, address election fairness and media bias, limit corruption and ensure equality under law."),
 dict(q="The framework describes a vetting body excluding reform-minded candidates and those who do not support a state religion. What consequence does it attribute to that exclusion?",
   choices=[
     "it limits the number of candidates and reduces electoral competition and representation",
     "it increases the number of parties represented in the legislature",
     "it guarantees that the winning candidate holds an absolute majority",
     "it transfers the conduct of elections to the courts",
     "it has no effect on representation"], ans=0,
   why="EK DEM-2.B.4.a states that Iran's Guardian Council excludes reform-minded candidates or those who do not support Islamic values, which limits the number of candidates and reduces electoral competition and representation. Representation is the civil and political rights dimension of that restriction."),
 dict(q="Which comparison of the framework's Iranian and Russian media examples is accurate?",
   choices=[
     "One operates through court decisions about licences and the other through state ownership of broadcast outlets",
     "Both operate through state ownership of broadcast outlets",
     "Both operate through court decisions about licences",
     "One operates through a national filtering system and the other through an independent regulator",
     "Neither is described by the framework"], ans=0,
   why="EK DEM-1.C.3.b describes Iranian courts suspending or revoking media licences after a jury verdict, and EK DEM-1.C.3.c describes the Russian government's nationalization of most broadcast media with rigid controls on opposition news segments. The instruments are different in kind."),
 dict(q="The table reports hypothetical civil liberties data for three countries. Which country's record best illustrates the framework's method of using over-time data to place a regime on the authoritarian-democratic scale?",
   table=_T_LIB,
   choices=[
     "Country B, whose score fell 22 points over the decade and which has the fewest independent news outlets",
     "Country A, whose score rose 3 points",
     "Country C, whose score fell 3 points",
     "None of the three, since a single score cannot place a regime",
     "All three equally, since each score changed"], ans=0,
   why="EK DEM-1.C.6 states that comparing data on how far governments protect or restrict civil liberties OVER TIME can determine regime placement on an authoritarian/democratic scale, so the clearest case is the largest movement. EK DEM-1.C.3's media restrictions are why the outlet count points the same way."),
 dict(q="Using the same table, which country's record best supports a claim of stable and comparatively strong protection of civil liberties?",
   table=_T_LIB,
   choices=[
     "Country A, whose score is highest in both years, rose slightly, and which has the most independent news outlets",
     "Country B, whose score changed most",
     "Country C, whose score is second highest in both years",
     "None of the three, since stability cannot be observed in two readings",
     "Both Country A and Country C, since neither fell by more than a few points"], ans=0,
   why="EK DEM-1.C.6 makes protection over time the measure, so a claim of stable strong protection needs a high level in both years and little movement between them. EK DEM-1.C.2 connects a large independent press to the high degree of media freedom democratic regimes generally tolerate."),
 dict(q="According to the same table, the largest change in a country's civil liberties score over the decade was",
   table=_T_LIB,
   choices=[
     "22 points",
     "3 points",
     "19 points",
     "34 points",
     "81 points"], ans=0,
   why="Subtracting each country's earlier score from its later one and comparing the sizes of the changes identifies the largest. The alternatives are a smaller change, the difference between two changes, a gap between two countries in the same year, and the largest single score."),
 dict(q="The table describes four hypothetical media restrictions. Which one matches the framework's example from China?",
   table=_T_MECH,
   choices=[
     "Case 1, a national filtering system that limits political criticism on social media",
     "Case 2, courts suspending or revoking licences after a jury verdict",
     "Case 3, state ownership of most broadcast outlets",
     "Case 4, an independent regulator enforcing a published accuracy code",
     "None of the four, since the framework gives no example from that country"], ans=0,
   why="EK DEM-1.C.3.a describes the Chinese Communist Party's use of the Great Firewall to limit political criticism on social media, and only one row states a filtering system with that purpose. The fourth row matches nothing in EK DEM-1.C.3."),
 dict(q="Using the same table, which case matches the framework's example from Iran?",
   table=_T_MECH,
   choices=[
     "Case 2, courts suspending or revoking media licences after a jury finds owners guilty of publishing certain material",
     "Case 1, a national filtering system limiting political criticism",
     "Case 3, state ownership of most broadcast outlets",
     "Case 4, an independent regulator enforcing an accuracy code",
     "None of the four, since the framework describes no judicial mechanism"], ans=0,
   why="EK DEM-1.C.3.b describes the Iranian court's suspension or revocation of media licenses when a jury finds owners guilty of publishing anti-religious material or information detrimental to the national interest. Only one row involves courts and a jury."),
 dict(q="Using the same table, which case matches the framework's example from Russia?",
   table=_T_MECH,
   choices=[
     "Case 3, state ownership of most broadcast outlets with rigid control of opposition news segments",
     "Case 1, a national filtering system limiting political criticism",
     "Case 2, courts suspending licences after a jury verdict",
     "Case 4, an independent regulator enforcing an accuracy code",
     "None of the four, since the framework describes no ownership-based mechanism"], ans=0,
   why="EK DEM-1.C.3.c describes the Russian government's nationalization of most broadcast media and rigid controls on opposition news segments, and only one row states ownership together with control of opposition coverage."),
 dict(q="The table reports hypothetical transparency figures for two governments. Which one does the framework's definition of transparency fit?",
   table=_T_TRANS,
   choices=[
     "Government D, which publishes most cabinet decisions, grants most information requests, and holds most committee sessions in public",
     "Government E, which publishes fewer than one decision in ten within a month",
     "Neither, since transparency cannot be measured",
     "Both equally, since each publishes some decisions",
     "Government E, because closed proceedings maximize order"], ans=0,
   why="EK DEM-1.C.4 defines a transparent government as one that allows information about government and policy making to circulate openly, and all three columns measure that circulation. That closed proceedings may maximize order is the framework's account of why some regimes prefer them, not a reason to call them transparent."),
 dict(q="According to the same table, the average of the second government's three transparency figures is",
   table=_T_TRANS,
   choices=[
     "9 percent",
     "27 percent",
     "12 percent",
     "84 percent",
     "6 percent"], ans=0,
   why="Adding that government's three figures and dividing by three gives the average. The alternatives offer the sum rather than the average, two of the individual figures, and the corresponding average for the other row."),
 dict(q="Which finding would most strongly indicate that a country's protection of civil liberties has improved?",
   choices=[
     "Over a decade, restrictions on publishing and assembly were repealed, independent outlets multiplied, and prosecutions for criticism fell to near zero",
     "Over a decade, the legislature passed more statutes each year",
     "Over a decade, turnout at national elections rose",
     "Over a decade, the number of government ministries increased",
     "Over a decade, the head of government gave more public speeches"], ans=0,
   why="EK DEM-1.C.6 makes protection or restriction of civil liberties over time the relevant measure, and EK DEM-1.C.2 connects media freedom to citizen control of the political agenda. Statute counts, turnout, ministries and speeches measure none of that."),
 dict(q="Which finding would most strongly place a regime further toward the authoritarian end of the framework's scale?",
   choices=[
     "Most broadcast outlets were brought into state ownership, online criticism was filtered, and cabinet proceedings were closed to the public",
     "The governing party's majority in the legislature increased",
     "A new ministry was created to coordinate economic policy",
     "The state joined an additional international organization",
     "The head of government was replaced by a colleague from the same party"], ans=0,
   why="EK DEM-1.C.3 makes monitoring and restricting media access the mark of stronger authoritarian regimes, EK DEM-1.C.3.a and .c give filtering and nationalization as its instances, and EK DEM-1.C.4 makes closed proceedings the authoritarian preference. The keyed finding combines all three."),
 dict(q="Taking the framework's statements on civil rights and civil liberties together, which summary is most accurate?",
   choices=[
     "Protection differs across the six countries; both regime types constrain media to protect citizens and maintain order while democracies generally tolerate a high degree of media freedom; stronger authoritarian regimes restrict media access further by named means; transparency is the open circulation of information; and civil liberties data over time can place a regime on the scale",
     "Protection is identical across the six countries and does not change over time",
     "Only authoritarian regimes constrain the media, and only democracies restrict civil liberties",
     "Transparency and legitimacy are the same thing",
     "Civil liberties cannot be compared across countries or over time"], ans=0,
   why="EK DEM-1.C.1 supplies the variation across the six, EK DEM-1.C.2 the shared constraint and its purpose alongside democratic media freedom, EK DEM-1.C.3 the further restriction by stronger authoritarian regimes with three named instruments, EK DEM-1.C.4 transparency, and EK DEM-1.C.6 the over-time method."),
]
