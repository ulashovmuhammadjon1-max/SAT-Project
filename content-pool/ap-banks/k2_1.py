# AP COMPARATIVE GOVERNMENT AND POLITICS 2.1 Parliamentary, Presidential, and
# Semi-Presidential Systems
# CED effective Fall 2026, Unit 2 Political Institutions. Enduring understanding
# PAU-3 (the structure and function of political institutions reflect the
# allocation of power within a political system); learning objective PAU-3.A.
# Suggested skill 1.B.
#
# Essential knowledge relied on:
#   PAU-3.A.1  PARLIAMENTARY systems, SUCH AS THE UNITED KINGDOM, combine the
#              lawmaking and executive functions, which allows the national
#              legislature to SELECT AND REMOVE the head of government and cabinet
#   PAU-3.A.2  PRESIDENTIAL systems, SUCH AS MEXICO AND NIGERIA, feature a cabinet
#              mostly responsible to the ELECTED EXECUTIVE, with a legislature that
#              can only remove cabinet members THROUGH IMPEACHMENT; separate
#              FIXED-TERM popular elections for the national legislature; and a top
#              executive leader serving as BOTH HEAD OF STATE AND HEAD OF
#              GOVERNMENT
#   PAU-3.A.3  SEMI-PRESIDENTIAL systems, SUCH AS RUSSIA, feature separate popular
#              elections for the president and for the national legislature,
#              allowing the president to NOMINATE A PRIME MINISTER who must be
#              APPROVED BY THE LEGISLATURE; cabinet members are held accountable by
#              BOTH the president and the legislature
#
# Supporting statements, each named in the verifier's claim:
#   PAU-3.C.2c Mexico's elected president is both head of state and head of
#              government, commander in chief and leader of the bureaucracy
#   PAU-3.C.2d Nigeria's elected president is both head of state and head of
#              government, chief executive, commander in chief, head of civil
#              service
#   PAU-3.C.2e Russia's prime minister is head of government and oversees the civil
#              service; the elected president is head of state and commander in
#              chief and appoints top ministers
#   PAU-3.C.2f the United Kingdom's monarch serves ceremonially as head of state and
#              formally appoints as prime minister the leader of the party or
#              coalition holding the largest number of seats in the Commons
#
# THE TRAP THIS TOPIC MUST NOT FALL INTO: PAU-3.A assigns a system type to FOUR
# course countries only -- the United Kingdom, Mexico, Nigeria and Russia. CHINA
# AND IRAN ARE GIVEN NO SUCH LABEL ANYWHERE IN THE FRAMEWORK. No item asks a
# student to classify either, because the framework supports no answer and the
# plausible one is wrong on the substance. Item 12 keys that absence directly.
# See AP_COMP_GOV_CED.md note 2.
#
# Table figures and cases are HYPOTHETICAL and labelled so.
#
# FIVE choices (A-E) per SOCIAL_BRIEF.md.
TOPIC = ("2.1", "Parliamentary, Presidential, and Semi-Presidential Systems", 2)

_T_CAB = dict(
    headers=["Case (hypothetical)", "Cabinet ministers removed by the legislature, 2000-2020",
             "Cabinet ministers removed by the chief executive, 2000-2020",
             "Heads of government removed by the legislature, 2000-2020"],
    rows=[["Case 1", "2", "18", "3"],
          ["Case 2", "0", "24", "0"],
          ["Case 3", "5", "11", "0"]])

_T_SEL = dict(
    headers=["Case (hypothetical)", "Separate popular election for the head of state",
             "Separate popular election for the national legislature",
             "How the head of government takes office"],
    rows=[["Case 4", "yes", "yes", "nominated by the president and approved by the legislature"],
          ["Case 5", "no", "yes", "selected by the legislature, which may also remove the officeholder"],
          ["Case 6", "yes", "yes", "the same person is elected as head of state and head of government"]])

QUESTIONS = [
 dict(q="How does the framework describe a parliamentary system?",
   choices=[
     "It combines the lawmaking and executive functions, which allows the national legislature to select and remove the head of government and cabinet",
     "It separates the lawmaking and executive functions, so that neither may remove the other",
     "It holds separate popular elections for the head of state and for the legislature",
     "It vests lawmaking in a council appointed by the head of state",
     "It requires the head of government to be elected directly by voters"], ans=0,
   why="EK PAU-3.A.1 states that parliamentary systems combine the lawmaking and executive functions, which allows the national legislature to select and remove the head of government and cabinet. Selection and removal by the same body is what the combination of functions makes possible."),
 dict(q="Which course country does the framework name as its example of a parliamentary system?",
   choices=[
     "the United Kingdom",
     "Mexico",
     "Nigeria",
     "Russia",
     "China"], ans=0,
   why="EK PAU-3.A.1 names the United Kingdom as its example of a parliamentary system. EK PAU-3.A.2 names Mexico and Nigeria as presidential and EK PAU-3.A.3 names Russia as semi-presidential, while China is given no such label anywhere in the framework."),
 dict(q="How does the framework describe a presidential system?",
   choices=[
     "The cabinet is mostly responsible to the elected executive, and the legislature can remove cabinet members only through impeachment",
     "The cabinet is responsible to the legislature, which may remove it by an ordinary vote",
     "The head of government is nominated by the head of state and approved by the legislature",
     "Lawmaking and executive functions are combined in a single body",
     "The legislature selects the head of government from among its own members"], ans=0,
   why="EK PAU-3.A.2 states that presidential systems feature a cabinet mostly responsible to the elected executive, with a legislature that can only remove cabinet members through impeachment. The rejected options describe the parliamentary and semi-presidential arrangements of EK PAU-3.A.1 and EK PAU-3.A.3."),
 dict(q="Which course countries does the framework name as its examples of presidential systems?",
   choices=[
     "Mexico and Nigeria",
     "the United Kingdom and Russia",
     "China and Iran",
     "Russia and Nigeria",
     "Mexico and the United Kingdom"], ans=0,
   why="EK PAU-3.A.2 names Mexico and Nigeria as its examples of presidential systems. EK PAU-3.C.2.c and EK PAU-3.C.2.d confirm that each has an elected president serving as both head of state and head of government, which is the feature EK PAU-3.A.2 makes definitive."),
 dict(q="In a presidential system as the framework describes it, by what means may the legislature remove a member of the cabinet?",
   choices=[
     "only through impeachment",
     "by an ordinary majority vote of no confidence at any time",
     "by requesting the head of state to dismiss the minister",
     "it may not remove a cabinet member by any means",
     "by refusing to approve the minister's nomination after appointment"], ans=0,
   why="EK PAU-3.A.2 states that in presidential systems the legislature can only remove cabinet members through impeachment. That restriction is what makes the cabinet mostly responsible to the elected executive rather than to the legislature."),
 dict(q="Which feature of the elections in a presidential system does the framework specify?",
   choices=[
     "separate fixed-term popular elections for the national legislature",
     "elections for the legislature held only when the executive calls them",
     "elections for the legislature conducted by the cabinet",
     "a single election that chooses the legislature and the executive together as one slate",
     "no popular election for the legislature at all"], ans=0,
   why="EK PAU-3.A.2 states that presidential systems have separate fixed-term popular elections for the national legislature. The fixed term is part of the definition, since it is what prevents the executive from timing a legislative election to suit itself."),
 dict(q="What does the framework say about the top executive leader in a presidential system?",
   choices=[
     "the same leader serves as both head of state and head of government",
     "one person serves as head of state while a separate prime minister serves as head of government",
     "the head of state is ceremonial and the head of government exercises executive power",
     "the head of government is chosen by the head of state and confirmed by the legislature",
     "the office of head of state is left vacant"], ans=0,
   why="EK PAU-3.A.2 specifies a top executive leader serving as both head of state and head of government, and EK PAU-3.C.2.c and EK PAU-3.C.2.d repeat that formula for Mexico and Nigeria. The split of the two roles belongs to the parliamentary and semi-presidential cases instead."),
 dict(q="How does the framework describe a semi-presidential system?",
   choices=[
     "It holds separate popular elections for the president and for the legislature, and the president nominates a prime minister who must be approved by the legislature",
     "It combines the lawmaking and executive functions in a single body",
     "It gives one elected leader the roles of both head of state and head of government",
     "It allows the legislature to remove cabinet members only through impeachment",
     "It leaves the selection of the prime minister entirely to the legislature"], ans=0,
   why="EK PAU-3.A.3 states that semi-presidential systems feature separate popular elections for the president and for the national legislature, allowing the president to nominate a prime minister who must be approved by the legislature. Both halves of that sentence are needed to separate the type from the other two."),
 dict(q="Which course country does the framework name as its example of a semi-presidential system?",
   choices=[
     "Russia",
     "the United Kingdom",
     "Mexico",
     "Nigeria",
     "Iran"], ans=0,
   why="EK PAU-3.A.3 names Russia as its example of a semi-presidential system. EK PAU-3.C.2.e matches the description, giving Russia an elected president as head of state and commander in chief alongside a prime minister who is head of government and oversees the civil service."),
 dict(q="In a semi-presidential system as the framework describes it, how does a prime minister take office?",
   choices=[
     "the president nominates the prime minister, who must then be approved by the legislature",
     "the legislature elects the prime minister without any presidential involvement",
     "the prime minister is elected directly by voters at a separate national election",
     "the president appoints the prime minister with no legislative involvement",
     "the outgoing prime minister designates a successor"], ans=0,
   why="EK PAU-3.A.3 states that the president nominates a prime minister who must be approved by the legislature, and EK PAU-3.E.1.e adds that Russia's elected state Duma confirms the prime minister. Both the nomination and the approval are required, which is what makes the arrangement a hybrid."),
 dict(q="In a semi-presidential system, to whom are cabinet members accountable on the framework's account?",
   choices=[
     "to both the president and the legislature",
     "to the president alone",
     "to the legislature alone",
     "to the head of state, who is a separate person from the president",
     "to the judiciary, which reviews their conduct"], ans=0,
   why="EK PAU-3.A.3 states that members of the cabinet are held accountable by both the president and the legislature. That dual accountability is the difference from EK PAU-3.A.2's presidential cabinet, which is mostly responsible to the elected executive."),
 dict(q="Which statement about how the framework classifies the six course countries by executive-legislative type is accurate?",
   choices=[
     "It assigns a type to four of them and gives China and Iran no such label",
     "It assigns a type to all six",
     "It classifies China as presidential because it has a president",
     "It classifies Iran as semi-presidential because it has both a president and a supreme leader",
     "It classifies all six as parliamentary"], ans=0,
   why="EK PAU-3.A.1 names the United Kingdom, EK PAU-3.A.2 names Mexico and Nigeria, and EK PAU-3.A.3 names Russia, and no essential knowledge statement assigns either of the remaining two a parliamentary, presidential or semi-presidential label. Reasoning from the existence of a presidential office to the label is exactly what the framework's silence forbids."),
 dict(q="In one country the national legislature chooses the head of government from among its members, may dismiss that officeholder by a vote, and the same body makes law and sustains the executive. Which type does this describe?",
   choices=[
     "a parliamentary system",
     "a presidential system",
     "a semi-presidential system",
     "a system with no executive branch",
     "a system in which the head of state is directly elected"], ans=0,
   why="EK PAU-3.A.1 defines parliamentary systems by the combination of lawmaking and executive functions, which allows the national legislature to select and remove the head of government and cabinet. Selection and removal by the legislature is the distinguishing pair."),
 dict(q="In a second country, voters elect the legislature to a fixed term and separately elect a president who serves as head of state and head of government; the legislature may reach the president's ministers only by impeachment. Which type does this describe?",
   choices=[
     "a presidential system",
     "a parliamentary system",
     "a semi-presidential system",
     "a system in which the head of state is ceremonial",
     "a system in which the cabinet is accountable to both elected branches"], ans=0,
   why="EK PAU-3.A.2 defines presidential systems by a cabinet mostly responsible to the elected executive, removal of cabinet members by the legislature only through impeachment, separate fixed-term popular elections for the legislature, and one leader serving as head of state and head of government. All four features appear in the scenario."),
 dict(q="In a third country, voters separately elect a president and a legislature; the president names a prime minister whom the legislature must approve, and ministers answer to both. Which type does this describe?",
   choices=[
     "a semi-presidential system",
     "a parliamentary system",
     "a presidential system",
     "a system with a ceremonial head of state and no elected president",
     "a system in which lawmaking and executive functions are combined"], ans=0,
   why="EK PAU-3.A.3 defines semi-presidential systems by separate popular elections for president and legislature, presidential nomination of a prime minister subject to legislative approval, and cabinet accountability to both. All three features appear in the scenario."),
 dict(q="Which comparison of how the head of government reaches office in the United Kingdom and in Mexico is consistent with the framework?",
   choices=[
     "In one, the leader of the largest party in the elected chamber is formally appointed by a ceremonial head of state; in the other, the head of government is elected directly by voters as head of state as well",
     "In both, the head of government is elected directly by voters",
     "In both, the head of government is chosen by the legislature",
     "In one, the head of government is nominated by a president and approved by the legislature; in the other, the legislature elects the head of government",
     "In both, the head of state and head of government are different people"], ans=0,
   why="EK PAU-3.C.2.f describes the monarch formally appointing as prime minister the leader of the party or coalition holding the largest number of seats in the Commons, and EK PAU-3.C.2.c describes Mexico's elected president as both head of state and head of government. EK PAU-3.A.1 and EK PAU-3.A.2 make those the defining routes for the two types."),
 dict(q="Which comparison of cabinet accountability in Mexico and Russia is consistent with the framework?",
   choices=[
     "In one the cabinet is mostly responsible to the elected executive, while in the other cabinet members are held accountable by both the president and the legislature",
     "In both the cabinet is responsible only to the legislature",
     "In both the cabinet is responsible only to the president",
     "In one the cabinet is selected by the judiciary and in the other by the legislature",
     "Neither system provides any means of removing a cabinet member"], ans=0,
   why="EK PAU-3.A.2 makes a presidential cabinet mostly responsible to the elected executive, with legislative removal only by impeachment, and EK PAU-3.A.3 makes a semi-presidential cabinet accountable to both the president and the legislature. That difference is the main institutional consequence of the hybrid form."),
 dict(q="Which comparison of how a prime minister takes office in the United Kingdom and in Russia is consistent with the framework?",
   choices=[
     "In one the officeholder is the leader of the largest party in the elected chamber and is formally appointed by a ceremonial head of state; in the other the officeholder is nominated by an elected president and confirmed by the elected chamber",
     "In both the officeholder is nominated by an elected president and confirmed by the legislature",
     "In both the officeholder is elected directly by voters",
     "In one the officeholder is appointed by the judiciary and in the other by the armed forces",
     "Neither system has a prime minister"], ans=0,
   why="EK PAU-3.C.2.f describes the monarch formally appointing the leader of the largest Commons party, while EK PAU-3.A.3 and EK PAU-3.E.1.e describe presidential nomination of a prime minister confirmed by the elected Duma. The elected chamber matters in both, but through different mechanisms."),
 dict(q="The United Kingdom's monarch is head of state and its prime minister is head of government. How does this compare with the presidential systems the framework describes?",
   choices=[
     "In presidential systems one leader holds both roles, whereas here they are held by different people",
     "In presidential systems the two roles are also held by different people",
     "In presidential systems the head of state is always ceremonial",
     "In presidential systems the head of government is appointed by the head of state",
     "The framework does not identify who holds either role in presidential systems"], ans=0,
   why="EK PAU-3.A.2 specifies a top executive leader serving as both head of state and head of government in presidential systems, while EK PAU-3.C.2.f gives the United Kingdom a ceremonial head of state distinct from the prime minister. The two arrangements differ precisely on whether the roles are fused."),
 dict(q="The table reports hypothetical removals over two decades in three cases. Which case is most consistent with a parliamentary system as the framework describes it?",
   table=_T_CAB,
   choices=[
     "Case 1, where the legislature removed three heads of government as well as some cabinet ministers",
     "Case 2, where the legislature removed neither a cabinet minister nor a head of government",
     "Case 3, where the legislature removed cabinet ministers but no head of government",
     "All three equally, since each records removals of some kind",
     "None, because the framework supplies no removal counts for any country"], ans=0,
   why="EK PAU-3.A.1 defines a parliamentary system by the legislature's power to select and remove the head of government and cabinet, so a record of the legislature actually removing heads of government is the distinguishing evidence. Only one row shows that happening."),
 dict(q="Using the same table, which case is most consistent with a presidential system as the framework describes it?",
   table=_T_CAB,
   choices=[
     "Case 2, where the legislature removed no minister and no head of government while the chief executive removed the most ministers",
     "Case 1, where the legislature removed three heads of government",
     "Case 3, where the legislature removed five ministers",
     "All three equally, since each has a chief executive who removed ministers",
     "None, since a presidential legislature can never remove a cabinet member"], ans=0,
   why="EK PAU-3.A.2 makes the cabinet mostly responsible to the elected executive and allows legislative removal of cabinet members only through impeachment, a rare route. A row in which the executive does nearly all the removing and the legislature none fits that description; the rejected final option overstates the rule, since impeachment does exist."),
 dict(q="According to the same table, the total number of cabinet ministers removed by chief executives across the three cases is",
   table=_T_CAB,
   choices=[
     "53",
     "42",
     "60",
     "24",
     "29"], ans=0,
   why="Adding the three figures in the column recording removals by the chief executive gives the total. The alternatives arise from omitting a row, from adding the wrong column into the sum, from reading the largest single row, and from adding the two smaller rows only."),
 dict(q="The table describes three hypothetical cases by how each fills its offices. Which case matches the framework's description of a semi-presidential system?",
   table=_T_SEL,
   choices=[
     "Case 4, which elects a head of state and a legislature separately and has the head of government nominated by the president and approved by the legislature",
     "Case 5, whose head of government is selected by the legislature",
     "Case 6, where one elected person is both head of state and head of government",
     "None of the three, since a semi-presidential system holds no popular elections",
     "All three, since each holds a popular election of some kind"], ans=0,
   why="EK PAU-3.A.3 requires separate popular elections for the president and the legislature together with presidential nomination of a prime minister approved by the legislature. Only one row has all three features in the same case."),
 dict(q="Using the same table, which case matches the framework's description of a parliamentary system?",
   table=_T_SEL,
   choices=[
     "Case 5, which holds no separate popular election for the head of state and whose head of government is selected and removable by the legislature",
     "Case 4, whose head of government is nominated by the president",
     "Case 6, whose head of state and head of government are the same elected person",
     "None of the three, since a parliamentary system has no head of state",
     "All three, since each has a head of government"], ans=0,
   why="EK PAU-3.A.1 defines a parliamentary system by the combination of lawmaking and executive functions, which lets the national legislature select and remove the head of government. Only one row places both selection and removal in the legislature, and EK PAU-3.C.2.f shows that a parliamentary system does have a head of state, a ceremonial one."),
 dict(q="Using the same table, which case matches the framework's description of a presidential system?",
   table=_T_SEL,
   choices=[
     "Case 6, where the same elected person serves as head of state and head of government",
     "Case 4, where a president nominates the head of government",
     "Case 5, where the legislature selects the head of government",
     "None of the three, since a presidential system holds no election for the legislature",
     "Case 5, because its head of state is not popularly elected"], ans=0,
   why="EK PAU-3.A.2 specifies a top executive leader serving as both head of state and head of government alongside separate popular elections for the national legislature, and only one row fuses the two offices in a single elected person. The rejected final option is false of the framework, which requires separate legislative elections in this type."),
 dict(q="Which feature most sharply distinguishes a presidential from a semi-presidential system on the framework's account?",
   choices=[
     "whether the cabinet answers to the elected executive alone or to both the executive and the legislature",
     "whether the legislature is popularly elected",
     "whether the country holds elections at all",
     "whether the state is federal or unitary",
     "whether the head of state is called a president"], ans=0,
   why="EK PAU-3.A.2 and EK PAU-3.A.3 both provide separate popular elections and both use the title president, so neither of those separates the types. The framework's difference is that a presidential cabinet is mostly responsible to the elected executive while a semi-presidential cabinet is accountable to both branches."),
 dict(q="Which feature most sharply distinguishes a parliamentary from a semi-presidential system on the framework's account?",
   choices=[
     "whether the head of government owes office to the legislature alone or to a nomination by a separately elected president that the legislature then approves",
     "whether the legislature may pass laws",
     "whether the country has a written constitution",
     "whether the state is federal or unitary",
     "whether the cabinet has more than ten members"], ans=0,
   why="EK PAU-3.A.1 gives the legislature the power to select and remove the head of government, while EK PAU-3.A.3 inserts a separately elected president who nominates and a legislature that approves. The route to office is what the two definitions differ on."),
 dict(q="Which description of Nigeria's president is consistent with the framework?",
   choices=[
     "an elected leader serving as both head of state and head of government, chief executive, commander in chief and head of the civil service",
     "a ceremonial head of state who appoints the head of government",
     "a head of government nominated by a head of state and approved by the legislature",
     "a head of state chosen indirectly by the national legislature",
     "an appointed official responsible to a supreme leader"], ans=0,
   why="EK PAU-3.C.2.d describes Nigeria's elected president as both head of state and head of government, serving as chief executive, commander in chief and head of civil service, and able to approve domestic legislation and conduct foreign policy. EK PAU-3.A.2 names Nigeria among its presidential examples on exactly this basis."),
 dict(q="Which description of Mexico's president is consistent with the framework?",
   choices=[
     "an elected leader who is both head of state and head of government, serves as commander in chief and leader of the bureaucracy, and can approve domestic legislation and lead foreign policy",
     "a ceremonial head of state whose appointment of a prime minister is formal only",
     "a head of government who must be approved by the upper chamber before taking office",
     "an official selected by the largest party in the lower chamber",
     "a head of state without any role in legislation"], ans=0,
   why="EK PAU-3.C.2.c describes Mexico's elected president in exactly these terms. EK PAU-3.A.2 names Mexico among its presidential examples, and the fusion of head of state and head of government is the feature that definition turns on."),
 dict(q="Taking the framework's three definitions together, which summary is most accurate?",
   choices=[
     "The three types differ in how the head of government reaches office and to whom the cabinet answers, and the framework assigns a type to only four of the six course countries",
     "The three types differ only in what the head of state is called, and the framework assigns a type to all six course countries",
     "The three types differ in whether the state is federal or unitary",
     "The three types are alternative names for the same arrangement",
     "The three types differ in whether the legislature is elected"], ans=0,
   why="EK PAU-3.A.1, EK PAU-3.A.2 and EK PAU-3.A.3 differ on the route to the head of government's office and on the cabinet's lines of accountability, and each names its examples: the United Kingdom, Mexico and Nigeria, and Russia. No statement assigns a type to the remaining two course countries."),
]
