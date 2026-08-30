# AP U.S. GOVERNMENT AND POLITICS 2.14 Holding the Bureaucracy Accountable -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# TWO learning objectives, one for each branch that controls the bureaucracy:
#   LO 2.14.A -- explain how CONGRESS uses its oversight power in its
#     relationship with the executive branch.
#   LO 2.14.B -- explain how the PRESIDENT ensures that executive branch
#     agencies and departments carry out their responsibilities in concert with
#     the goals of the administration.
# Suggested skill for this topic (CED p. 74): 3.C, EXPLAIN PATTERNS AND TRENDS
# IN DATA TO DRAW CONCLUSIONS. This module carries nine data items across three
# tables, weighted to explanation rather than description, because 3.C asks a
# student to say what a pattern MEANS and not merely what it is.
#
# Essential knowledge relied on:
#   EK 2.14.A.1 -- "Congressional oversight of the bureaucracy to ensure that
#     legislation is IMPLEMENTED AS INTENDED includes:
#       i.   Review, monitoring, and supervision of bureaucratic agencies
#       ii.  Investigation and committee hearings of bureaucratic activity
#       iii. POWER OF THE PURSE (the ability of Congress to check the
#            bureaucracy by APPROPRIATING OR WITHHOLDING FUNDS)"
#   EK 2.14.A.2 -- "As a means to curtail the use of presidential power,
#     congressional oversight serves as a CHECK OF EXECUTIVE AUTHORIZATION."
#   EK 2.14.B.1 -- "PRESIDENTIAL IDEOLOGY, AUTHORITY, AND INFLUENCE affect how
#     executive branch agencies carry out the goals of the administration."
#   EK 2.14.B.2 -- "COMPLIANCE MONITORING ensures that funds are being used
#     properly and regulations are being followed. Compliance monitoring CAN
#     POSE A CHALLENGE TO POLICY IMPLEMENTATION."
#
# THE TWO OBJECTIVES DESCRIBE A CONTEST, NOT TWO SEPARATE SUBJECTS. Congress
# oversees the agencies to ensure ITS legislation is implemented as intended;
# the president directs the same agencies toward the ADMINISTRATION's goals.
# Both are aimed at the same officials at the same time, which is why the CED
# puts them in one topic and why items 21 to 24 and 28 to 30 are about the
# collision rather than about either side alone.
#
# EK 2.14.B.2 IS THE STATEMENT MOST OFTEN HALF-READ, and item 17 exists for it.
# Compliance monitoring does two things in the CED's own sentence: it ENSURES
# funds are used properly and regulations followed, AND it CAN POSE A CHALLENGE
# TO POLICY IMPLEMENTATION. It is both the safeguard and a cost of the
# safeguard. A bank that reports only the first half teaches that monitoring is
# free; a bank that reports only the second teaches that it is waste.
#
# THE CED'S OWN PARENTHESIS defines the power of the purse as appropriating OR
# WITHHOLDING funds. Withholding is the half students forget, and it is the half
# that makes the power a check rather than a routine budgeting function. Items 7
# to 9 turn on it.
#
# Documents the CED attaches to 2.14.A (p. 26-27): Federalist No. 51,
# Federalist No. 70.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: Federalist No. 51 and constitutional
# text are quoted verbatim. The CED's illustrative examples for this topic are
# marked NOT REQUIRED and none is named. All three tables are labelled
# hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.14", "Holding the Bureaucracy Accountable", 2)

_OVERSIGHT = ("In a hypothetical legislature, the table reports oversight activity directed at "
              "executive agencies in years of unified and of divided party control.")
_OVERSIGHT_TABLE = dict(
    headers=["Year", "Party control", "Oversight hearings held", "Agencies whose funds were reduced"],
    rows=[["Year 1", "Unified", "112", "3"],
          ["Year 2", "Unified", "128", "5"],
          ["Year 3", "Divided", "294", "17"],
          ["Year 4", "Divided", "331", "21"]])

_MONITORING = ("In a hypothetical study of one grant program, the table reports the share of "
               "funds accounted for and the average months from award to first service "
               "delivered, at four levels of compliance monitoring.")
_MONITORING_TABLE = dict(
    headers=["Level of compliance monitoring", "Funds fully accounted for (%)", "Months from award to first service"],
    rows=[["Minimal", "71", "4"],
          ["Moderate", "88", "7"],
          ["Extensive", "96", "13"],
          ["Very extensive", "98", "22"]])

_DIRECTION = ("In a hypothetical study, the table reports how closely agency regulatory output "
              "matched the stated priorities of the sitting administration, by the share of an "
              "agency's senior positions filled by that administration's appointees.")
_DIRECTION_TABLE = dict(
    headers=["Share of senior positions filled by the administration (%)", "Number of agencies", "Regulatory output matching administration priorities (%)"],
    rows=[["Under 25", "7", "38"],
          ["25 to 49", "9", "52"],
          ["50 to 74", "11", "69"],
          ["75 and above", "6", "81"]])

QUESTIONS = [
 dict(q="According to the course framework, the purpose of congressional oversight of the bureaucracy is to ensure that",
   choices=[
     "legislation is implemented as intended",
     "agencies employ officials of the majority party",
     "the president's agenda is carried out promptly",
     "the courts have an opportunity to review each regulation",
     "agencies spend their entire appropriation each year"], ans=0,
   why="EK 2.14.A.1 states the purpose in exactly these words. Oversight is Congress checking the implementation of ITS OWN legislation, which is what distinguishes it from presidential direction."),

 dict(q="Which of the following does the course framework list as a form of congressional oversight?",
   choices=[
     "Review, monitoring, and supervision of bureaucratic agencies",
     "Appointing the heads of executive agencies",
     "Issuing regulations that agencies must follow",
     "Removing agency officials for poor performance",
     "Reviewing the constitutionality of agency rules"], ans=0,
   why="EK 2.14.A.1.i names review, monitoring and supervision. Appointment is executive, rulemaking is the agency's own, removal is executive, and constitutional review belongs to the courts."),

 dict(q="A congressional committee summons agency officials to explain why a program has fallen behind schedule. Which form of oversight is this?",
   choices=[
     "Investigation and committee hearings of bureaucratic activity",
     "Review, monitoring, and supervision, which requires no appearance by officials",
     "The power of the purse, since the program involves spending",
     "Compliance monitoring, which is an executive function",
     "Judicial review of the agency's performance"], ans=0,
   why="EK 2.14.A.1.ii names investigation and committee hearings, and a summons to testify is the characteristic form. EK 2.12.A.1.iii records the same event from the agency's side."),

 dict(q="According to the course framework, the power of the purse is",
   choices=[
     "the ability of Congress to check the bureaucracy by appropriating or withholding funds",
     "the president's authority to direct how agencies spend their appropriations",
     "the courts' authority to order an agency to spend money",
     "an agency's authority to raise its own revenue",
     "the Senate's authority to confirm the officials who manage a budget"], ans=0,
   why="EK 2.14.A.1.iii gives this definition in its own parenthesis, and the two verbs -- APPROPRIATING OR WITHHOLDING -- are both part of it."),

 dict(q="Which half of the power of the purse makes it a CHECK rather than a routine budgeting function?",
   choices=[
     "Withholding funds, since the possibility of losing an appropriation is what gives an agency reason to answer to Congress",
     "Appropriating funds, since agencies could not operate without them",
     "Neither, since the power of the purse is not a check",
     "Both equally, since appropriating and withholding are the same act",
     "Neither, since only the president may withhold funds"], ans=0,
   why="EK 2.14.A.1.iii names both verbs, and it is the credible threat of withholding that converts an annual appropriation into leverage. Appropriating alone is what any legislature does."),

 dict(q="A committee informs an agency that its next appropriation will be reduced unless it changes how it administers a program, and the agency changes. Which form of oversight has operated?",
   choices=[
     "The power of the purse, exercised through the threat of withholding funds",
     "Investigation and committee hearings, since the committee communicated with the agency",
     "Review, monitoring and supervision, since the committee examined the program",
     "Compliance monitoring, since the agency's administration was at issue",
     "Judicial review, since the agency was required to change its conduct"], ans=0,
   why="EK 2.14.A.1.iii's power of the purse works by appropriating OR WITHHOLDING, and the change here was produced by the prospect of a reduction rather than by a hearing or a rule."),

 dict(q="According to the course framework, congressional oversight serves as a check of executive authorization as a means to",
   choices=[
     "curtail the use of presidential power",
     "increase the number of agencies in the executive branch",
     "transfer rulemaking authority to the courts",
     "shorten the president's term of office",
     "require the Senate to confirm additional officials"], ans=0,
   why="EK 2.14.A.2 states this in exactly these words: oversight curtails the use of presidential power by checking executive authorization."),

 dict(q="Why does overseeing AGENCIES amount to a check on the PRESIDENT, as EK 2.14.A.2 asserts?",
   choices=[
     "Agencies are the instrument through which a president's priorities become action, so limiting what they may do limits what the president can accomplish",
     "Agencies are part of the legislative branch",
     "Agency heads may be removed by a vote of Congress",
     "The president is required to attend congressional hearings",
     "Agencies report to Congress rather than to the president"], ans=0,
   why="EK 2.14.B.1 makes agencies the vehicle for the administration's goals, so EK 2.14.A.2's check on their authorization reaches the president indirectly. Agencies remain within the executive branch."),

 dict(q="Read the following excerpt.\n\n“Ambition must be made to counteract ambition. The interest of the man must be connected with the constitutional rights of the place.”\n—James Madison, Federalist No. 51, 1788\n\nHow does congressional oversight of the bureaucracy fit Madison's design?",
   choices=[
     "Members of Congress defend the legislature's institutional stake in how its statutes are carried out, whichever party holds the presidency",
     "Members of Congress are required to support a president of their own party",
     "Oversight is conducted by the executive branch over itself",
     "Oversight requires the agreement of all three branches before it may begin",
     "Oversight replaces the separation of powers with a single chain of command"], ans=0,
   why="Madison's design gives an institution a power and its members a motive to use it, and Congress's stake in seeing its own statutes implemented as intended is exactly such a motive."),

 dict(q="According to the course framework, what affects how executive branch agencies carry out the goals of the administration?",
   choices=[
     "Presidential ideology, authority, and influence",
     "The seniority of the committee chairs overseeing them",
     "The number of federal courts with jurisdiction over them",
     "The length of the president's remaining term alone",
     "The size of the federal budget deficit"], ans=0,
   why="EK 2.14.B.1 names exactly these three: presidential ideology, authority and influence. The list is the framework's own and the other options are not on it."),

 dict(q="A new administration's appointees direct an agency to prioritize a category of enforcement the previous administration had de-emphasized, using the same statute. Which claim from the course framework does this illustrate?",
   choices=[
     "That presidential ideology, authority and influence affect how agencies carry out the goals of the administration",
     "That agencies may disregard statutes they consider unwise",
     "That Congress must approve each change in enforcement priorities",
     "That the courts set enforcement priorities for agencies",
     "That agency priorities are fixed by statute and cannot change"], ans=0,
   why="EK 2.14.B.1 is precisely this, and EK 2.13.A.1's delegated discretion is the room in which it operates: where a statute leaves a choice open, a change of administration can change the answer."),

 dict(q="Which of the president's three levers named by EK 2.14.B.1 operates through the FORMAL powers of the office rather than through persuasion or outlook?",
   choices=[
     "Authority, which includes appointment and the direction of subordinate officials",
     "Ideology, which shapes which goals the administration pursues",
     "Influence, which operates through relationships and public standing",
     "None of the three, since all are informal",
     "All three equally, since the framework does not distinguish them"], ans=0,
   why="EK 2.14.B.1 lists ideology, authority and influence as three distinct things. Authority is the formal one; ideology supplies the direction and influence the persuasion, which EK 2.4.A.2.iii classifies as informal."),

 dict(q="According to the course framework, what does compliance monitoring ensure?",
   choices=[
     "That funds are being used properly and regulations are being followed",
     "That agencies spend their full appropriation each year",
     "That Congress approves each regulation before it takes effect",
     "That the courts review each grant award",
     "That agency officials are appointed on merit"], ans=0,
   why="EK 2.14.B.2 states both objects in exactly these words. Monitoring is about the proper use of funds and adherence to regulations rather than about the volume of spending."),

 dict(q="The course framework says something further about compliance monitoring, beyond what it ensures. What is it?",
   choices=[
     "That it can pose a challenge to policy implementation",
     "That it is prohibited in programs administered by the states",
     "That it may be conducted only by the courts",
     "That it guarantees a policy will succeed",
     "That it applies only to programs costing more than a set amount"], ans=0,
   why="EK 2.14.B.2's second sentence is that compliance monitoring 'can pose a challenge to policy implementation.' The statement gives both the benefit and its cost, and reading only one half misstates it."),

 dict(q="Why can compliance monitoring pose a challenge to policy implementation?",
   choices=[
     "The reporting and verification it requires consume time and staff that would otherwise go to delivering the program",
     "It transfers the program to a different agency",
     "It makes the underlying statute unenforceable",
     "It requires congressional approval before any funds may be spent",
     "It prevents an agency from issuing any regulations"], ans=0,
   why="EK 2.14.B.2 pairs the assurance with the challenge, and the mechanism is the ordinary one: verification is itself work. The other options describe consequences monitoring does not have."),

 dict(q="A program administrator argues that monitoring requirements should be reduced. A second argues they should be increased. Which framing of the disagreement is most consistent with the course framework?",
   choices=[
     "Both are describing real effects of the same practice, since EK 2.14.B.2 says monitoring both ensures proper use of funds and can challenge implementation",
     "The first is right, since the framework says monitoring serves no purpose",
     "The second is right, since the framework says monitoring has no costs",
     "Neither is right, since the framework does not mention compliance monitoring",
     "The disagreement cannot be resolved, since the framework treats monitoring as purely political"], ans=0,
   why="EK 2.14.B.2 contains both halves in two sentences, so the disagreement is about where to set a level rather than about which effect is real."),

 dict(q="Which pairing correctly matches a form of accountability with the branch that exercises it?",
   choices=[
     "Committee hearings, with Congress; compliance monitoring, with the executive branch",
     "Committee hearings, with the executive branch; compliance monitoring, with Congress",
     "Both, with Congress",
     "Both, with the executive branch",
     "Both, with the federal courts"], ans=0,
   why="EK 2.14.A.1.ii places hearings under congressional oversight, and EK 2.14.B.2 places compliance monitoring under the president's assurance that agencies act in concert with the administration's goals."),

 dict(q="An agency finds itself directed by a congressional committee to do one thing and by the administration to do another, both within the statute's terms. What does this situation illustrate?",
   choices=[
     "The bureaucracy answers to two principals at once, which is the structure this topic describes",
     "The agency must follow whichever instruction arrived first",
     "The agency must refer the conflict to the Supreme Court",
     "The agency is free to disregard both instructions",
     "The conflict shows that one of the two instructions must be unconstitutional"], ans=0,
   why="LO 2.14.A and LO 2.14.B describe two branches directing the same agencies at the same time, which is why the CED puts them in one topic. Nothing in the framework resolves the conflict by priority or by referral."),

 dict(q="Which of the following would most strengthen a claim that congressional oversight is effective?",
   choices=[
     "Agencies changed how they administered programs after hearings identified problems, and the changes persisted",
     "Congress held more hearings this year than last year",
     "More committees claimed jurisdiction over the same agency",
     "Hearings received extensive news coverage",
     "Agency officials appeared promptly when summoned"], ans=0,
   why="EK 2.14.A.1's stated purpose is ensuring legislation is implemented as intended, so effectiveness must be measured by changed implementation. Counts of hearings and coverage measure activity."),

 dict(q="Which of the following would most strengthen a claim that a president has succeeded in directing agencies toward the administration's goals?",
   choices=[
     "Agency regulatory output shifted toward the administration's stated priorities after its appointees took office",
     "The president gave several speeches about the agencies' work",
     "The number of federal employees increased",
     "Congress held fewer hearings than in the previous year",
     "The agencies' budgets increased"], ans=0,
   why="EK 2.14.B.1's claim is about how agencies CARRY OUT the administration's goals, so the evidence must be a change in what the agencies actually did. Speeches, staffing and budgets measure inputs."),

 dict(q=_OVERSIGHT + " Which pattern is best supported by the data, and what does it suggest?",
   table=_OVERSIGHT_TABLE,
   choices=[
     "Both hearings and funding reductions rose sharply under divided control, which suggests oversight intensifies when the opposing party holds a chamber",
     "Both fell under divided control, which suggests oversight depends on cooperation",
     "Hearings rose but funding reductions fell under divided control",
     "Hearings and funding reductions were roughly equal across all four years",
     "Oversight activity was highest in the first year of the term"], ans=0,
   why="Hearings run 112, 128, 294 and 331 and reductions run 3, 5, 17 and 21, both roughly tripling between the unified and divided years. The lowest figures are in Year 1."),

 dict(q=_OVERSIGHT + " Which claim from the course framework does the pattern most directly illustrate?",
   table=_OVERSIGHT_TABLE,
   choices=[
     "That congressional oversight serves as a check of executive authorization, curtailing the use of presidential power",
     "That compliance monitoring ensures funds are used properly",
     "That presidential ideology affects how agencies carry out administration goals",
     "That the civil service uses a merit system",
     "That agencies exercise discretion delegated by Congress"], ans=0,
   why="EK 2.14.A.2 casts oversight as a check on presidential power, and oversight rising precisely when the opposing party controls Congress is that function operating. The other options name statements the table does not measure."),

 dict(q=_OVERSIGHT + " A student concludes that divided control CAUSES more oversight. Which limitation of the data most undercuts that conclusion?",
   table=_OVERSIGHT_TABLE,
   choices=[
     "The divided years are also the later years of the term, so party control and time in office cannot be separated here",
     "The table omits the number of hearings held, so no comparison is possible",
     "The table reports only years of divided control",
     "The table gives percentages rather than counts",
     "The two series move in opposite directions"], ans=0,
   why="Unified control occupies Years 1 and 2 and divided control Years 3 and 4, so the two explanations are perfectly confounded, exactly as in the executive-order table of topic 2.5. Both series and four years are plainly present."),

 dict(q=_MONITORING + " Which pattern is best supported by the data?",
   table=_MONITORING_TABLE,
   choices=[
     "Accountability rises with monitoring but so does delay, and the gain in accountability shrinks while the delay keeps growing",
     "Both accountability and speed improve as monitoring increases",
     "Accountability falls as monitoring increases",
     "Delay is unrelated to the level of monitoring",
     "Accountability reaches one hundred percent at the highest level of monitoring"], ans=0,
   why="Accounting runs 71, 88, 96 and 98 -- gains of 17, 8 and 2 -- while months run 4, 7, 13 and 22, rising by 3, 6 and 9. The last level reaches 98, not 100."),

 dict(q=_MONITORING + " Which claim from the course framework do these data most directly illustrate?",
   table=_MONITORING_TABLE,
   choices=[
     "That compliance monitoring ensures funds are used properly and can pose a challenge to policy implementation",
     "That compliance monitoring has no effect on how funds are used",
     "That compliance monitoring speeds policy implementation",
     "That congressional oversight includes committee hearings",
     "That agencies exercise discretion delegated by Congress"], ans=0,
   why="EK 2.14.B.2's two sentences are the two columns: accountability rises, and time to first service rises with it. A table showing only one column could not illustrate the statement."),

 dict(q=_MONITORING + " A program manager must choose a level of monitoring. Which conclusion do the data best support?",
   table=_MONITORING_TABLE,
   choices=[
     "Moving beyond extensive monitoring buys two additional points of accounting at the cost of nine additional months",
     "Moving from minimal to moderate monitoring is the costliest step in delay",
     "Every increase in monitoring produces an equal gain in accounting",
     "The highest level of monitoring is best on both measures",
     "The data show no basis for choosing among the levels"], ans=0,
   why="The step from extensive to very extensive raises accounting from 96 to 98 and months from 13 to 22. The steps in delay grow rather than shrink, so the first step is the cheapest, not the costliest."),

 dict(q=_DIRECTION + " Which pattern is best supported by the data?",
   table=_DIRECTION_TABLE,
   choices=[
     "The more senior positions an administration has filled, the more closely regulatory output matches its priorities",
     "The relationship runs the other way, with fewer appointees producing closer matching",
     "Matching is the same at every level of appointment",
     "Most agencies in the study had three quarters or more of their senior positions filled",
     "Matching exceeds ninety percent in at least one group"], ans=0,
   why="Matching runs 38, 52, 69 and 81 percent as the appointment share rises. The largest group is the eleven agencies in the third band, and no group exceeds 81 percent."),

 dict(q=_DIRECTION + " Which claim from the course framework do these data most directly illustrate?",
   table=_DIRECTION_TABLE,
   choices=[
     "That presidential authority, exercised through appointments, affects how agencies carry out administration goals",
     "That congressional oversight ensures legislation is implemented as intended",
     "That the power of the purse checks the bureaucracy",
     "That compliance monitoring can challenge implementation",
     "That agencies form iron triangles with committees and interest groups"], ans=0,
   why="EK 2.14.B.1 names authority among the three things affecting how agencies carry out the administration's goals, and appointments are how authority reaches an agency's decisions."),

 dict(q=_DIRECTION + " Which limitation of these data most complicates the conclusion that appointments cause the matching?",
   table=_DIRECTION_TABLE,
   choices=[
     "Administrations may appoint more heavily at agencies whose work they care most about, so the priority may drive the appointments rather than the reverse",
     "The table omits the share of senior positions filled, so no comparison is possible",
     "The table covers a single agency, so no comparison is possible",
     "The table reports counts rather than percentages, so no rate can be computed",
     "The table shows no relationship between the two variables"], ans=0,
   why="Reverse causation is the live alternative here: an administration that cares about a policy area invests in both appointments and priorities there. All four bands, the agency counts and both percentages are plainly present."),

 dict(q="Which statement best captures the relationship between the two learning objectives in this topic?",
   choices=[
     "Congress and the president direct the same agencies toward partly different ends, so accountability runs in two directions at once",
     "Congress controls agencies entirely and the president has no role",
     "The president controls agencies entirely and Congress has no role",
     "Agencies are accountable only to the federal courts",
     "Agencies are accountable to no institution once a statute has been enacted"], ans=0,
   why="LO 2.14.A gives Congress oversight to ensure ITS legislation is implemented as intended, and LO 2.14.B gives the president the task of aligning agencies with the ADMINISTRATION's goals. Both reach the same officials at once."),
]
