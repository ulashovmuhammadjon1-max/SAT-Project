# AP COMPARATIVE GOVERNMENT AND POLITICS 2.6 Legislative Systems
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3; learning objective PAU-3.E (describe legislative structures and functions
# in course countries). Suggested skill 2.A, Country Comparison.
#
# Essential knowledge relied on:
#   PAU-3.E.1  legislative institutions of course countries include:
#     .a CHINA -- a PARTY-CONTROLLED, UNICAMERAL system consisting of an elected
#        National People's Congress that THE CONSTITUTION RECOGNIZES as the
#        government's most powerful institution, which ELECTS THE PRESIDENT,
#        APPROVES THE PREMIER, and LEGITIMIZES POLICIES of the executive
#     .b IRAN -- UNICAMERAL; the Majles is elected and holds the power to APPROVE
#        LEGISLATION, OVERSEE THE BUDGET, and CONFIRM PRESIDENTIAL NOMINEES TO THE
#        CABINET, acting UNDER THE SUPERVISION OF THE GUARDIAN COUNCIL to ensure
#        compatibility with Islam and Sharia law
#     .c MEXICO -- a congressional-presidential system, BICAMERAL: the elected
#        Chamber of Deputies APPROVES LEGISLATION, LEVIES TAXES and VERIFIES
#        OUTCOMES OF ELECTIONS; the elected Senate holds the UNIQUE power to
#        CONFIRM PRESIDENTIAL APPOINTMENTS TO THE SUPREME COURT, APPROVE TREATIES,
#        and APPROVE FEDERAL INTERVENTION IN STATE MATTERS
#     .d NIGERIA -- congressional-presidential, BICAMERAL, with an elected Senate
#        and House of Representatives; BOTH chambers approve legislation and the
#        Senate possesses UNIQUE IMPEACHMENT AND CONFIRMATION powers
#     .e RUSSIA -- a parliamentary-hybrid system, BICAMERAL: an elected state Duma
#        PASSES LEGISLATION and CONFIRMS THE PRIME MINISTER; an APPOINTED
#        Federation Council approves BUDGET LEGISLATION, TREATIES, JUDICIAL
#        NOMINEES and TROOP DEPLOYMENT
#     .f UNITED KINGDOM -- a parliamentary system, BICAMERAL: an elected House of
#        Commons approves legislation, and an APPOINTED House of Lords REVIEWS AND
#        AMENDS bills from the Commons, EFFECTIVELY DELAYING IMPLEMENTATION AS A
#        POWER CHECK
#
# How members reach these chambers is EK DEM-2.A.1.a-f, cited where used:
#   .a China's NPC selects members INDIRECTLY through local and regional elections
#   .b Iran's Majles is directly elected in single-member and multimember districts,
#      sometimes requiring a second round; candidates are vetted by the Guardian
#      Council; the body LACKS FORMAL POLITICAL PARTY STRUCTURES; a small number of
#      the 290 SEATS are reserved for non-Muslim minorities
#   .c Mexico: 300 deputies in single-member districts by plurality plus 200 by
#      party-list proportional representation; 96 senators in three-seat
#      constituencies plus 32 by proportional representation
#   .d Nigeria: House members in single-member districts, seats per state by
#      population size; the Senate has three members from each of Nigeria's 36 states
#   .e Russia: half the Duma directly elected in single-member districts, half by
#      proportional representation with a threshold
#   .f the United Kingdom's Commons is elected under single-member district,
#      first-past-the-post rules
#
# PAU-3.E.1.a is a statement about what CHINA'S CONSTITUTION RECOGNIZES; PAU-3.F.1.a
# says the Politburo Standing Committee is the ACTUAL center of power. Items here
# say which of the two is being asked about, because an item that blurred them
# would have no defensible key (AP_COMP_GOV_CED.md note 5).
#
# Table cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.6", "Legislative Systems", 2)

_T_SEATS = dict(
    headers=["Chamber (hypothetical)", "Seats filled in single-member districts",
             "Seats filled by proportional representation", "Total seats"],
    rows=[["Chamber 1", "300", "200", "500"],
          ["Chamber 2", "225", "225", "450"],
          ["Chamber 3", "650", "0", "650"]])

_T_UP = dict(
    headers=["Upper chamber (hypothetical)", "How members reach the chamber",
             "Powers the chamber holds"],
    rows=[["Upper chamber X", "elected",
           "confirming appointments to the highest court, approving treaties, and approving intervention in the affairs of a constituent unit"],
          ["Upper chamber Y", "appointed",
           "approving budget legislation, treaties, judicial nominees, and troop deployment"],
          ["Upper chamber Z", "appointed",
           "reviewing and amending bills from the lower chamber, delaying their implementation"]])

QUESTIONS = [
 dict(q="Which course countries does the framework describe as having unicameral legislatures?",
   choices=[
     "China and Iran",
     "Mexico and Nigeria",
     "Russia and the United Kingdom",
     "China and the United Kingdom",
     "all six course countries"], ans=0,
   why="EK PAU-3.E.1.a calls China's system unicameral and EK PAU-3.E.1.b calls Iran's theocracy unicameral, while EK PAU-3.E.1.c through .f describe Mexico, Nigeria, Russia and the United Kingdom as bicameral."),
 dict(q="What does the framework say China's constitution recognizes the National People's Congress as?",
   choices=[
     "the government's most powerful institution, which elects the president, approves the premier, and legitimizes policies of the executive",
     "an advisory body with no power over the executive",
     "the actual center of power in the Chinese state",
     "a chamber that reviews and amends bills, delaying their implementation",
     "an appointed body whose members are chosen by regional governors"], ans=0,
   why="EK PAU-3.E.1.a states that the constitution recognizes the National People's Congress as the government's most powerful institution that elects the president, approves the premier and legitimizes policies of the executive. EK PAU-3.F.1.a separately identifies the Politburo Standing Committee as the ACTUAL center of power, which is a different claim."),
 dict(q="How does the framework say members of China's National People's Congress are selected?",
   choices=[
     "indirectly, through a series of local and regional elections",
     "directly, in single-member districts by plurality",
     "by appointment from regional governors and regional legislatures",
     "half in single-member districts and half by proportional representation",
     "by the premier, subject to the president's approval"], ans=0,
   why="EK DEM-2.A.1.a states that the National People's Congress of China selects members indirectly through a series of local and regional elections. The rejected methods are those the framework assigns to the United Kingdom, Russia's Federation Council and Russia's Duma."),
 dict(q="Which powers does the framework assign to Iran's Majles?",
   choices=[
     "approving legislation, overseeing the budget, and confirming presidential nominees to the Cabinet",
     "electing the president and approving the premier",
     "approving budget legislation, treaties, judicial nominees, and troop deployment",
     "confirming appointments to the highest court and approving federal intervention in state matters",
     "reviewing and amending bills from a lower chamber"], ans=0,
   why="EK PAU-3.E.1.b states that Iran's Majles is elected and holds the power to approve legislation, oversee the budget, and confirm presidential nominees to the Cabinet. The rejected lists describe China's National People's Congress, Russia's Federation Council, Mexico's Senate and the United Kingdom's House of Lords."),
 dict(q="Under whose supervision does the framework say Iran's Majles acts, and to what end?",
   choices=[
     "the Guardian Council, to ensure that laws are compatible with Islam and Sharia law",
     "the Expediency Council, to ensure that the budget is balanced",
     "the president, to ensure that the cabinet is confirmed",
     "the head of the judiciary, to ensure that trials are conducted correctly",
     "an independent election commission, to ensure that seats are fairly allocated"], ans=0,
   why="EK PAU-3.E.1.b states that the Majles acts under the supervision of the Guardian Council to ensure compatibility with Islam and Sharia law, and EK PAU-3.F.1.d adds that the Guardian Council vets candidates and oversees the Majles for that purpose. The Expediency Council's role under EK PAU-3.F.1.c is to resolve disputes between the two."),
 dict(q="What does the framework say about the composition of Iran's Majles?",
   choices=[
     "a small number of its 290 seats are reserved for non-Muslim minorities, and the body lacks formal political party structures",
     "all of its seats are allocated by proportional representation among registered parties",
     "half of its seats are filled in single-member districts and half by proportional representation",
     "its members are appointed by the Supreme Leader",
     "its seats are divided equally among the country's provinces"], ans=0,
   why="EK DEM-2.A.1.b states that Iran's Majles members are directly elected in single-member and multimember districts, that the body lacks formal political party structures, and that a small number of the 290 seats are reserved for non-Muslim minorities such as Christians, Jews and Zoroastrians."),
 dict(q="Which powers does the framework assign to Mexico's Chamber of Deputies?",
   choices=[
     "approving legislation, levying taxes, and verifying outcomes of elections",
     "confirming presidential appointments to the Supreme Court and approving treaties",
     "approving federal intervention in state matters",
     "confirming the prime minister",
     "reviewing and amending bills from the upper chamber"], ans=0,
   why="EK PAU-3.E.1.c states that Mexico's elected Chamber of Deputies approves legislation, levies taxes, and verifies outcomes of elections. The first three rejected options are powers the same statement assigns to the Senate, and the last two belong to Russia's Duma and the House of Lords."),
 dict(q="Which powers does the framework describe as unique to Mexico's Senate?",
   choices=[
     "confirming presidential appointments to the Supreme Court, approving treaties, and approving federal intervention in state matters",
     "levying taxes and verifying outcomes of elections",
     "impeaching the president and confirming appointments generally",
     "approving budget legislation and troop deployment",
     "reviewing and amending bills and delaying their implementation"], ans=0,
   why="EK PAU-3.E.1.c gives Mexico's elected Senate the unique power to confirm presidential appointments to the Supreme Court, approve treaties, and approve federal intervention in state matters. The rejected lists belong to the Chamber of Deputies, Nigeria's Senate, Russia's Federation Council and the House of Lords."),
 dict(q="How does the framework describe the composition of Mexico's two chambers?",
   choices=[
     "300 deputies elected in single-member districts by plurality plus 200 by party-list proportional representation, and 96 senators elected in three-seat constituencies plus 32 by proportional representation",
     "500 deputies all elected by proportional representation and 128 senators all elected in single-member districts",
     "300 deputies and 200 senators, all elected in single-member districts",
     "half the deputies elected in single-member districts and half by proportional representation with a threshold",
     "three senators from each of the country's states and no deputies"], ans=0,
   why="EK DEM-2.A.1.c gives these figures for Mexico's Congress of the Union and adds that gender quotas in the party list system have helped increase female representation. The half-and-half arrangement described against it is Russia's Duma under EK DEM-2.A.1.e, and three senators per state is Nigeria's under EK DEM-2.A.1.d."),
 dict(q="How does the framework describe the legislative powers of Nigeria's two chambers?",
   choices=[
     "both chambers hold the power to approve legislation, and the Senate possesses unique impeachment and confirmation powers",
     "only the lower chamber may approve legislation, and the upper chamber may only delay it",
     "only the upper chamber may approve legislation, and the lower chamber levies taxes",
     "neither chamber may approve legislation without the approval of a vetting body",
     "the upper chamber confirms the prime minister and the lower chamber passes legislation"], ans=0,
   why="EK PAU-3.E.1.d states that both chambers of Nigeria's bicameral system hold the power to approve legislation and that the Senate possesses unique impeachment and confirmation powers. The rejected descriptions belong to the United Kingdom, Mexico, Iran and Russia."),
 dict(q="How does the framework describe the composition of Nigeria's two chambers?",
   choices=[
     "House members are directly elected in single-member districts with the number from each state based on population size, while the Senate has three members directly elected from each of the country's 36 states",
     "both chambers are elected by proportional representation from national party lists",
     "the House is elected and the Senate is appointed by state governors",
     "the House has three members from each state and the Senate is elected by population",
     "both chambers are elected in three-seat constituencies"], ans=0,
   why="EK DEM-2.A.1.d states that Nigerian House members are directly elected in single-member districts with representation from each state based on population size, and that the Senate has three members directly elected from each of Nigeria's 36 states. Both chambers are elected."),
 dict(q="Which powers does the framework assign to Russia's state Duma?",
   choices=[
     "passing legislation and confirming the prime minister",
     "approving budget legislation, treaties, judicial nominees, and troop deployment",
     "electing the president and legitimizing policies of the executive",
     "levying taxes and verifying outcomes of elections",
     "reviewing and amending bills from the upper chamber"], ans=0,
   why="EK PAU-3.E.1.e states that Russia's elected state Duma passes legislation and confirms the prime minister, which is also the approval step EK PAU-3.A.3's semi-presidential definition requires. The rejected lists belong to the Federation Council, China's National People's Congress, Mexico's Chamber of Deputies and the House of Lords."),
 dict(q="Which powers does the framework assign to Russia's Federation Council, and how do its members reach it?",
   choices=[
     "it is appointed, and it approves budget legislation, treaties, judicial nominees, and troop deployment",
     "it is elected, and it confirms the prime minister",
     "it is appointed, and it reviews and amends bills from the lower chamber",
     "it is elected, and it approves federal intervention in the affairs of the regions",
     "it is appointed, and it elects the president"], ans=0,
   why="EK PAU-3.E.1.e describes an appointed Federation Council approving budget legislation, treaties, judicial nominees and troop deployment, and EK DEM-2.B.5.c adds that its appointments are made by regional governors and the regional legislature. Confirming the prime minister belongs to the elected Duma under the same statement."),
 dict(q="How does the framework describe the way Russia's state Duma is elected?",
   choices=[
     "half of the representatives directly elected from single-member districts and the other half through proportional representation with a threshold",
     "all representatives directly elected from single-member districts by plurality",
     "all representatives elected by proportional representation with no threshold",
     "representatives appointed by regional governors and regional legislatures",
     "representatives selected indirectly through local and regional elections"], ans=0,
   why="EK DEM-2.A.1.e states that changes to state Duma elections have returned it to a system in which half of the representatives are directly elected from single-member districts and the other half are chosen through elections using proportional representation with a threshold."),
 dict(q="Which chamber does the framework describe as approving legislation in the United Kingdom, and how is it chosen?",
   choices=[
     "the elected House of Commons, chosen under single-member district, first-past-the-post rules",
     "the appointed House of Lords, chosen on the recommendation of the prime minister",
     "the elected House of Commons, chosen by proportional representation with a threshold",
     "the appointed House of Lords, chosen by regional governors",
     "a single elected chamber, since the United Kingdom is unicameral"], ans=0,
   why="EK PAU-3.E.1.f states that the United Kingdom's parliamentary system is bicameral with an elected House of Commons that approves legislation, and EK DEM-2.A.1.f states that Commons members are directly elected under single-member district, first-past-the-post rules."),
 dict(q="What role does the framework assign to the United Kingdom's House of Lords?",
   choices=[
     "reviewing and amending bills from the lower chamber, effectively delaying implementation as a power check",
     "approving all legislation before the lower chamber may consider it",
     "confirming the prime minister after the monarch's appointment",
     "approving treaties and troop deployment",
     "levying taxes and verifying outcomes of elections"], ans=0,
   why="EK PAU-3.E.1.f states that the appointed House of Lords reviews and amends bills from the Commons, effectively delaying implementation as a power check. The rejected powers belong to Russia's Duma and Federation Council and to Mexico's Chamber of Deputies."),
 dict(q="Which two of the course countries does the framework describe as having an APPOINTED upper chamber?",
   choices=[
     "Russia and the United Kingdom",
     "Mexico and Nigeria",
     "China and Iran",
     "Mexico and Russia",
     "Nigeria and the United Kingdom"], ans=0,
   why="EK PAU-3.E.1.e calls Russia's Federation Council appointed and EK PAU-3.E.1.f calls the House of Lords appointed, while EK PAU-3.E.1.c and EK PAU-3.E.1.d describe Mexico's Senate and Nigeria's Senate as elected. China and Iran have no upper chamber at all."),
 dict(q="Which comparison of the two elected upper chambers among the course countries is consistent with the framework?",
   choices=[
     "One holds unique powers over Supreme Court appointments, treaties and federal intervention, while the other holds unique impeachment and confirmation powers",
     "Both hold unique impeachment powers and nothing else",
     "Both are appointed rather than elected",
     "Neither has any power over appointments",
     "One approves troop deployment and the other reviews and amends bills"], ans=0,
   why="EK PAU-3.E.1.c gives Mexico's elected Senate unique power over Supreme Court appointments, treaties and federal intervention in state matters, and EK PAU-3.E.1.d gives Nigeria's elected Senate unique impeachment and confirmation powers. Troop deployment and bill delay belong to the two appointed chambers instead."),
 dict(q="Which two upper chambers does the framework describe as approving treaties?",
   choices=[
     "Mexico's Senate and Russia's Federation Council",
     "Nigeria's Senate and the United Kingdom's House of Lords",
     "China's National People's Congress and Iran's Majles",
     "Mexico's Chamber of Deputies and Russia's state Duma",
     "Nigeria's House of Representatives and Iran's Majles"], ans=0,
   why="EK PAU-3.E.1.c gives Mexico's Senate the power to approve treaties and EK PAU-3.E.1.e gives Russia's Federation Council the power to approve treaties alongside budget legislation, judicial nominees and troop deployment. No other chamber is described as holding that power."),
 dict(q="The table reports hypothetical chamber compositions. Which chamber's composition matches the framework's description of Mexico's Chamber of Deputies?",
   table=_T_SEATS,
   choices=[
     "Chamber 1, with 300 district seats and 200 proportional seats",
     "Chamber 2, with 225 district seats and 225 proportional seats",
     "Chamber 3, with 650 district seats and none filled proportionally",
     "None of the three, since the framework gives no seat figures",
     "All three, since each fills some seats in districts"], ans=0,
   why="EK DEM-2.A.1.c states that Mexico's Chamber of Deputies has 300 members directly elected in single-member districts by plurality and an additional 200 elected by a proportional representation party list system. Only one row carries both figures."),
 dict(q="Using the same table, which chamber's composition matches the framework's description of Russia's state Duma?",
   table=_T_SEATS,
   choices=[
     "Chamber 2, which fills exactly half its seats in districts and half proportionally",
     "Chamber 1, which fills more seats in districts than proportionally",
     "Chamber 3, which fills every seat in districts",
     "None of the three, since the Duma is appointed",
     "Both Chamber 1 and Chamber 2, since each fills some seats proportionally"], ans=0,
   why="EK DEM-2.A.1.e states that half of the state Duma's representatives are directly elected from single-member districts and the other half through proportional representation with a threshold. Only one row divides its seats exactly in half, and the Duma is elected rather than appointed."),
 dict(q="According to the same table, the share of the first chamber's seats filled by proportional representation is",
   table=_T_SEATS,
   choices=[
     "40 percent",
     "60 percent",
     "50 percent",
     "20 percent",
     "0 percent"], ans=0,
   why="Dividing that chamber's proportional seats by its total gives the share. The alternatives offer the complementary district share, the share for a different row, a misplaced decimal, and the share for the row that fills no seats proportionally."),
 dict(q="The table describes three hypothetical upper chambers. Which one matches the framework's description of Mexico's Senate?",
   table=_T_UP,
   choices=[
     "Upper chamber X, elected, with powers over appointments to the highest court, treaties, and intervention in a constituent unit",
     "Upper chamber Y, appointed, with powers over the budget, treaties, judicial nominees and troop deployment",
     "Upper chamber Z, appointed, reviewing and amending bills from the lower chamber",
     "None of the three, since Mexico's Senate is appointed",
     "Both Upper chamber X and Upper chamber Y, since each approves treaties"], ans=0,
   why="EK PAU-3.E.1.c describes Mexico's ELECTED Senate as holding the unique power to confirm presidential appointments to the Supreme Court, approve treaties, and approve federal intervention in state matters. Only one row is elected and carries all three powers."),
 dict(q="Using the same table, which chamber matches the framework's description of Russia's Federation Council?",
   table=_T_UP,
   choices=[
     "Upper chamber Y, appointed, with powers over budget legislation, treaties, judicial nominees and troop deployment",
     "Upper chamber X, elected, with powers over court appointments and treaties",
     "Upper chamber Z, appointed, reviewing and amending bills",
     "None of the three, since the Federation Council is elected",
     "Both Upper chamber Y and Upper chamber Z, since both are appointed"], ans=0,
   why="EK PAU-3.E.1.e describes an APPOINTED Federation Council approving budget legislation, treaties, judicial nominees and troop deployment. Two rows are appointed, so the powers column is what separates them."),
 dict(q="Using the same table, which chamber matches the framework's description of the United Kingdom's House of Lords?",
   table=_T_UP,
   choices=[
     "Upper chamber Z, appointed, reviewing and amending bills from the lower chamber and delaying their implementation",
     "Upper chamber X, elected, with powers over court appointments",
     "Upper chamber Y, appointed, with powers over troop deployment",
     "None of the three, since the House of Lords is elected",
     "Both Upper chamber X and Upper chamber Z, since neither approves troop deployment"], ans=0,
   why="EK PAU-3.E.1.f describes the APPOINTED House of Lords as reviewing and amending bills from the Commons, effectively delaying implementation as a power check. Only one row pairs appointment with that reviewing and delaying role."),
 dict(q="Which comparison of how the head of government is confirmed in China and in Russia is consistent with the framework?",
   choices=[
     "One legislature is described by its constitution as approving the premier, while the other is described as confirming the prime minister",
     "Both legislatures elect the head of government directly from among their own members",
     "Neither legislature has any role in the selection of the head of government",
     "One legislature appoints the head of government and the other impeaches that officeholder",
     "Both legislatures are appointed rather than elected"], ans=0,
   why="EK PAU-3.E.1.a states that China's constitution recognizes the National People's Congress as electing the president and approving the premier, and EK PAU-3.E.1.e states that Russia's elected state Duma confirms the prime minister. Both chambers are elected, in Russia directly and in China indirectly under EK DEM-2.A.1.a."),
 dict(q="Which legislature does the framework describe as verifying the outcomes of elections?",
   choices=[
     "Mexico's Chamber of Deputies",
     "Russia's Federation Council",
     "the United Kingdom's House of Lords",
     "Nigeria's Senate",
     "China's National People's Congress"], ans=0,
   why="EK PAU-3.E.1.c states that Mexico's elected Chamber of Deputies approves legislation, levies taxes, and verifies outcomes of elections. No other legislative chamber in the framework is given that function."),
 dict(q="A question asks which body is the actual center of power in the Chinese state. Which answer does the framework support, and why is the National People's Congress not it?",
   choices=[
     "the Politburo Standing Committee, because the framework's claim about the National People's Congress is a claim about what the constitution recognizes",
     "the National People's Congress, because the constitution recognizes it as the most powerful institution",
     "neither, because the framework identifies no center of power in that state",
     "the premier, because that officeholder oversees the civil service",
     "the Standing Committee of the National People's Congress, because it sets the legislative agenda"], ans=0,
   why="EK PAU-3.F.1.a states that China's Politburo Standing Committee is the actual center of power in the Chinese state, while EK PAU-3.E.1.a states only what the constitution RECOGNIZES about the National People's Congress. Both sentences are the framework's, and they answer different questions."),
 dict(q="Which statement about how the six legislatures are chosen is consistent with the framework?",
   choices=[
     "Members reach these chambers by several different routes, including direct election in districts, proportional representation, indirect election, and appointment",
     "Every chamber among the six is directly elected",
     "Every chamber among the six is appointed",
     "Every chamber among the six is elected entirely by proportional representation",
     "The framework does not describe how members of these chambers are chosen"], ans=0,
   why="EK DEM-2.A.1.a through .f describe indirect selection in China, districts with a possible second round in Iran, a mixed system in Mexico, districts in Nigeria, a half-and-half system in Russia and first-past-the-post in the United Kingdom, while EK PAU-3.E.1.e and .f describe two appointed upper chambers."),
 dict(q="Taking the framework's account of the six legislatures together, which summary is most accurate?",
   choices=[
     "Two are unicameral and four bicameral, the powers assigned to each chamber differ, and two of the four upper chambers are appointed rather than elected",
     "All six are bicameral with identical powers in each chamber",
     "All six are unicameral",
     "All six upper chambers are elected",
     "The framework assigns the same set of powers to every legislature among the six"], ans=0,
   why="EK PAU-3.E.1.a and .b describe unicameral systems, .c through .f bicameral ones, and .e and .f identify the two appointed upper chambers. The powers listed differ chamber by chamber throughout the statement."),
]
