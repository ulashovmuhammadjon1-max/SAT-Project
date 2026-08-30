# AP U.S. GOVERNMENT AND POLITICS 2.2 Structures, Powers, and Functions of Congress -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.2.A: explain how the structure, powers, and functions of
# both houses of Congress affect the policymaking process.
# Suggested skill for this topic (CED p. 60): 3.A, DESCRIBE THE DATA PRESENTED.
# This module carries nine data items across three tables rather than the usual
# six, because the framework's own suggested skill for the topic is data
# description and the budget claim at EK 2.2.A.4.ii is a claim about numbers.
#
# Essential knowledge relied on:
#   EK 2.2.A.1 -- "The structures and powers of the Senate and House are
#     different BY DESIGN. This difference directly affects the legislative
#     process."
#   EK 2.2.A.2 -- both chambers refer bills to committees, which hold hearings,
#     debate and mark up bills; "Leadership in committees is determined by the
#     majority political party."
#   EK 2.2.A.3 -- chamber-specific rules:
#     i.  HOUSE: the Speaker is elected by a majority of members and presides;
#         all revenue bills must originate in the House; rules for debate on a
#         bill are established by the RULES COMMITTEE; the House can form a
#         COMMITTEE OF THE WHOLE to expedite debate; an individual
#         representative can file a DISCHARGE PETITION to bring a bill to the
#         floor, "but it is rarely done."
#     ii. SENATE: bills are typically brought to the floor by UNANIMOUS CONSENT,
#         but a senator may request a HOLD to prevent a bill from reaching the
#         floor; during debate a senator may FILIBUSTER (prolong debate to delay
#         or prevent a vote) or move for CLOTURE (a procedure to end debate).
#     iii. a CONFERENCE COMMITTEE reconciles differences when the two chambers
#         pass versions of the same bill with variation in wording.
#   EK 2.2.A.4 -- the budget must address both kinds of spending:
#     i.  MANDATORY spending is required by law for entitlement programs such as
#         Social Security, Medicare and Medicaid.
#     ii. DISCRETIONARY spending is approved annually for defense, education and
#         infrastructure. "As entitlement costs grow, discretionary spending
#         opportunities will DECREASE UNLESS tax revenues increase, or the
#         budget deficit increases."
#   EK 2.2.A.5 -- PORK-BARREL legislation (funding for a local project inside a
#     larger appropriation bill) and LOGROLLING (exchange of political favors
#     among legislators, such as trading votes) affect the process in both
#     chambers.
#
# THE CONDITIONAL IN EK 2.2.A.4.ii IS THE HARDEST SENTENCE IN THIS TOPIC, and
# items 16 to 18 and 27 to 29 are built on it. It is not "entitlements crowd out
# discretionary spending." It is a claim with TWO stated escape routes: the
# squeeze happens UNLESS revenues rise OR the deficit grows. A student who drops
# the "unless" clause gets the data items wrong, because a table can show
# entitlements growing while discretionary spending holds steady -- and that is
# not a counterexample to the framework, it is the framework's second branch.
#
# THE DISCHARGE PETITION, worded carefully. EK 2.2.A.3.i says "an individual
# representative in the House can file a discharge petition," and adds "but it
# is rarely done." The chamber rule requires 218 signatures to succeed; the
# CED's sentence describes who FILES it. See AP_US_GOV_CED.md note 11. Items
# here are worded to be true of both readings: they say a representative may
# file one and that success is rare, and none asserts that one member's
# signature suffices to discharge a bill.
#
# Required cases the CED attaches to 2.2.A (p. 31-32): Shaw v. Reno.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text verbatim; the
# budget tables are labelled hypothetical, because real outlay figures could not
# be verified here and would date the module.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere; the
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.2", "Structures, Powers, and Functions of Congress", 2)

_BUDGET = ("In a hypothetical national budget, the table reports outlays in billions of "
           "dollars in three consecutive years.")
_BUDGET_TABLE = dict(
    headers=["Category", "Year 1", "Year 2", "Year 3"],
    rows=[["Mandatory spending", "2,400", "2,700", "3,050"],
          ["Discretionary spending", "1,300", "1,280", "1,240"],
          ["Total outlays", "3,700", "3,980", "4,290"],
          ["Total revenues", "3,300", "3,430", "3,540"]])

_RULES = ("The table lists five congressional procedures and identifies the chamber in which "
          "each operates and what it does.")
_RULES_TABLE = dict(
    headers=["Procedure", "Chamber", "Effect on a bill"],
    rows=[["Rules Committee", "House", "Sets the terms of floor debate"],
          ["Committee of the Whole", "House", "Expedites debate"],
          ["Discharge petition", "House", "Can bring a bill to the floor from committee"],
          ["Filibuster", "Senate", "Prolongs debate to delay or prevent a vote"],
          ["Cloture", "Senate", "Ends debate"]])

_STAGE = ("In a hypothetical two-year Congress, the table reports how many bills introduced "
          "in the larger chamber survived each successive stage of the legislative process.")
_STAGE_TABLE = dict(
    headers=["Stage", "Bills remaining"],
    rows=[["Introduced", "6,400"],
          ["Reported out of committee", "1,050"],
          ["Passed the chamber of origin", "620"],
          ["Passed both chambers", "340"],
          ["Signed into law", "310"]])

QUESTIONS = [
 dict(q="According to the course framework, the different structures and powers of the Senate and House are best understood as",
   choices=[
     "a deliberate feature of the design, which directly affects the legislative process",
     "an accident of history that the framers did not anticipate",
     "identical in practice, since both chambers must pass the same bill",
     "a defect that the Seventeenth Amendment was adopted to correct",
     "irrelevant to how legislation is actually made"], ans=0,
   why="EK 2.2.A.1 says the structures and powers are different BY DESIGN and that the difference directly affects the legislative process, which is the premise of the whole topic."),

 dict(q="According to the course framework, leadership of congressional committees is determined by",
   choices=[
     "the majority political party in the chamber",
     "seniority alone, regardless of party",
     "a vote of the whole chamber taken by secret ballot",
     "the president, subject to Senate confirmation",
     "the party that holds the presidency"], ans=0,
   why="EK 2.2.A.2 states that leadership in committees is determined by the majority political party. That is why control of a chamber matters even when the same members remain in office."),

 dict(q="Which sequence describes what the course framework says committees do with a bill?",
   choices=[
     "Receive it on referral, conduct hearings, debate it, and mark it up with revisions and additions",
     "Receive it after floor passage and decide whether to send it to the president",
     "Draft it, pass it, and transmit it directly to the other chamber",
     "Receive it from the president and decide whether to introduce it",
     "Reconcile differences between two chambers' versions of the same bill"], ans=0,
   why="EK 2.2.A.2 lists referral, hearings, debate and markup with revisions and additions. Reconciling two chambers' versions is the conference committee's job under EK 2.2.A.3.iii, which is a different stage."),

 dict(q="A committee chair schedules no hearing on a bill referred to her committee, and the bill goes no further. Which feature of the legislative process does this illustrate?",
   choices=[
     "Committees are a gatekeeping stage, and the majority party's control of chairs gives it control of that gate",
     "The Constitution requires that every bill receive a committee hearing",
     "A bill that receives no hearing automatically reaches the floor after one year",
     "Committee chairs are chosen by the minority party to protect its interests",
     "Only the president may withdraw a bill from consideration"], ans=0,
   why="EK 2.2.A.2 puts referral and hearings at the front of the process and assigns committee leadership to the majority party, so a chair's inaction is a decision with force. Nothing in the Constitution requires a hearing."),

 dict(q="In the House, the terms on which a bill will be debated on the floor are established by",
   choices=[
     "the Rules Committee",
     "the Committee of the Whole",
     "unanimous consent of the members present",
     "a conference committee",
     "the Senate majority leader"], ans=0,
   why="EK 2.2.A.3.i names the Rules Committee as the body that establishes rules for debate on a bill in the House. Unanimous consent is the Senate's ordinary route to the floor under EK 2.2.A.3.ii."),

 dict(q="What is the purpose of the House's Committee of the Whole, according to the course framework?",
   choices=[
     "To expedite debate on bills",
     "To reconcile differences between House and Senate versions of a bill",
     "To set the rules under which a bill will be debated",
     "To end debate when a minority is prolonging it",
     "To elect the Speaker at the opening of each Congress"], ans=0,
   why="EK 2.2.A.3.i says the House can form a Committee of the Whole in order to expedite debate on bills. Reconciliation is the conference committee, rule setting is the Rules Committee, and ending debate is the Senate's cloture."),

 dict(q="According to the course framework, a discharge petition is a procedure by which",
   choices=[
     "a representative can seek to bring a bill to the floor for debate, though it is rarely done",
     "a senator can prevent a bill from reaching the floor",
     "a committee chair can remove a bill from the calendar",
     "the Speaker can require the Senate to take up a House bill",
     "the president can compel a vote on a proposal"], ans=0,
   why="EK 2.2.A.3.i says an individual representative in the House can file a discharge petition to have a bill brought to the floor for debate, 'but it is rarely done.' The second option describes the Senate hold under EK 2.2.A.3.ii."),

 dict(q="Why does the course framework note that the discharge petition is rarely used successfully?",
   choices=[
     "It is a route around the committee system and the majority leadership, which normally control what reaches the floor",
     "The Constitution forbids its use more than once in each Congress",
     "It may be filed only by the Speaker, who has no reason to use it",
     "It applies only to revenue bills, which are rare",
     "It requires the approval of the Supreme Court"], ans=0,
   why="EK 2.2.A.2 gives the majority party control of committees and EK 2.2.A.3.i gives the Rules Committee control of floor debate, so a procedure that bypasses both runs against the chamber's ordinary power structure."),

 dict(q="In the Senate, bills are typically brought to the floor by",
   choices=[
     "unanimous consent",
     "a resolution reported by the Rules Committee",
     "a discharge petition filed by an individual senator",
     "a majority vote of the Committee of the Whole",
     "an order of the vice president"], ans=0,
   why="EK 2.2.A.3.ii states that bills are typically brought to the floor by unanimous consent in the Senate. The Rules Committee, the discharge petition and the Committee of the Whole are all House procedures under EK 2.2.A.3.i."),

 dict(q="A senator informs the majority leader that she objects to bringing a particular bill to the floor, and the bill is not scheduled. According to the course framework, this action is",
   choices=[
     "a hold, a request that prevents a bill from getting to the floor for a vote",
     "a filibuster, a tactic to prolong debate once a bill has reached the floor",
     "cloture, a procedure to end debate on a bill",
     "a discharge petition, a request to bring a bill out of committee",
     "a markup, a revision of a bill's text in committee"], ans=0,
   why="EK 2.2.A.3.ii defines a hold as a senator's request to prevent a bill from getting to the floor for a vote, which is what happened here. A filibuster operates during debate, after the bill has reached the floor."),

 dict(q="What is the relationship between the filibuster and cloture as the course framework defines them?",
   choices=[
     "The filibuster prolongs debate to delay or prevent a vote, and cloture is the procedure for ending that debate",
     "Cloture prolongs debate and the filibuster ends it",
     "Both are procedures for ending debate, used in different chambers",
     "Both are procedures for prolonging debate, used at different stages",
     "The filibuster is a House procedure and cloture is a Senate procedure"], ans=0,
   why="EK 2.2.A.3.ii defines the filibuster as a tactic to prolong debate and delay or prevent a vote, and cloture as a procedure to end a debate. Both are Senate procedures, which is why the last option fails."),

 dict(q="Which pairing of a procedure with its chamber is correct?",
   choices=[
     "Cloture with the Senate and the Committee of the Whole with the House",
     "Cloture with the House and the Rules Committee with the Senate",
     "The filibuster with the House and the discharge petition with the Senate",
     "Unanimous consent with the House and the hold with the House",
     "The Rules Committee with the Senate and the Committee of the Whole with the Senate"], ans=0,
   why="EK 2.2.A.3.ii assigns cloture, the filibuster, the hold and unanimous consent to the Senate; EK 2.2.A.3.i assigns the Rules Committee, the Committee of the Whole and the discharge petition to the House."),

 dict(q="The House and the Senate each pass a bill on the same subject, but the two texts differ in wording. According to the course framework, what happens next?",
   choices=[
     "A conference committee meets to reconcile the differences",
     "The version passed by the larger chamber automatically prevails",
     "The bill is sent to the president, who chooses between the two versions",
     "The bill returns to the committees of origin in both chambers for a new markup",
     "The Supreme Court determines which version conforms to the Constitution"], ans=0,
   why="EK 2.2.A.3.iii states that a conference committee meets to reconcile differences when a bill passed by both chambers on the same topic varies in its wording."),

 dict(q="According to the course framework, mandatory spending is",
   choices=[
     "required by law for entitlement programs such as Social Security, Medicare, and Medicaid",
     "approved on an annual basis for defense, education, and infrastructure",
     "the portion of the budget the president may spend without congressional approval",
     "spending that Congress may reduce at any time by a simple majority vote",
     "the portion of the budget devoted to servicing the national debt alone"], ans=0,
   why="EK 2.2.A.4.i defines mandatory spending in exactly these terms and names those three programs. The second option is the framework's definition of discretionary spending."),

 dict(q="According to the course framework, discretionary spending is",
   choices=[
     "approved on an annual basis for purposes such as defense, education, and infrastructure",
     "required by law for entitlement programs",
     "spending that occurs automatically without any congressional action",
     "the difference between total outlays and total revenues in a fiscal year",
     "spending authorized permanently and reviewed only once a decade"], ans=0,
   why="EK 2.2.A.4.ii defines discretionary spending as approved annually and names defense, education and infrastructure. The fourth option describes the deficit, which is a different quantity."),

 dict(q="The course framework says that as entitlement costs grow, discretionary spending opportunities will decrease. Under what stated conditions does that consequence NOT follow?",
   choices=[
     "If tax revenues increase, or if the budget deficit increases",
     "If Congress passes an annual budget on time",
     "If the president requests a reduction in defense spending",
     "If the Senate invokes cloture on the appropriations bill",
     "If the House Rules Committee reports a closed rule"], ans=0,
   why="EK 2.2.A.4.ii states the squeeze with an explicit 'unless' carrying exactly two escapes: unless tax revenues increase, or the budget deficit increases. Dropping that clause is the most common misreading of this statement."),

 dict(q="A budget analyst observes that entitlement costs rose sharply over a decade while spending on defense, education and infrastructure held roughly steady. Which explanation is most consistent with the course framework?",
   choices=[
     "Revenues rose or the deficit grew, either of which the framework identifies as a way to avoid the squeeze",
     "The framework's claim about entitlements and discretionary spending has been disproved",
     "Entitlement spending must in fact have fallen, since discretionary spending did not decline",
     "Congress reclassified entitlement programs as discretionary",
     "Mandatory and discretionary spending are unrelated to one another in any budget"], ans=0,
   why="EK 2.2.A.4.ii's conditional has two escape routes, so steady discretionary spending alongside rising entitlements is what the statement predicts when one of them is operating, not a counterexample to it."),

 dict(q="Which of the following best explains why mandatory spending constrains congressional discretion more than discretionary spending does?",
   choices=[
     "Mandatory spending flows from standing law and continues unless Congress changes that law, while discretionary spending must be enacted each year",
     "Mandatory spending is controlled by the president rather than by Congress",
     "Discretionary spending is required by law and mandatory spending is optional",
     "Mandatory spending may not be altered by any act of Congress",
     "Discretionary spending is not subject to the appropriations process"], ans=0,
   why="EK 2.2.A.4 distinguishes the two by how each is authorized: mandatory is required by law for entitlement programs, discretionary is approved annually. The third option reverses the two definitions."),

 dict(q="According to the course framework, pork-barrel legislation is",
   choices=[
     "funding for a local project included in a larger appropriation bill",
     "an exchange of political favors among legislators, such as trading votes",
     "a procedure for ending debate in the Senate",
     "a bill that has been reported out of committee without amendment",
     "spending required by law for an entitlement program"], ans=0,
   why="EK 2.2.A.5 defines pork-barrel legislation as funding for a local project in a larger appropriation bill, and separately defines logrolling as the exchange of political favors, which is the second option."),

 dict(q="Two legislators agree that each will vote for the other's priority bill although neither cares about the other's subject. According to the course framework, this practice is",
   choices=[
     "logrolling, an exchange of political favors among legislators such as trading votes",
     "pork-barrel legislation, funding for a local project in a larger appropriation bill",
     "a markup, the revision of a bill's text in committee",
     "a hold, a request preventing a bill from reaching the floor",
     "cloture, a procedure to end debate"], ans=0,
   why="EK 2.2.A.5 defines logrolling as the exchange of political favors among legislators, such as trading votes, to gain support for legislation, which is exactly the arrangement described."),

 dict(q="In Shaw v. Reno (1993), the Supreme Court held that majority-minority districts created under the Voting Rights Act of 1965 may be constitutionally challenged by voters if race is the only factor used in creating the district. How does the case bear on the structure of Congress?",
   choices=[
     "It constrains how the districts that elect the House may be drawn, and district lines shape who serves and therefore how the chamber legislates",
     "It changed the number of senators each state may elect",
     "It transferred the drawing of congressional districts to the Senate",
     "It required that all House committees be chaired by the minority party",
     "It abolished the Rules Committee's control over floor debate"], ans=0,
   why="The CED attaches Shaw to 2.2.A, and the connection is that House districts determine the chamber's membership. The other options describe changes the holding does not make."),

 dict(q=_BUDGET + " Which conclusion is best supported by the data?",
   table=_BUDGET_TABLE,
   choices=[
     "Mandatory spending rose in each year while discretionary spending fell in each year",
     "Both categories of spending rose in each year",
     "Discretionary spending exceeded mandatory spending in at least one year",
     "Total revenues exceeded total outlays in each year",
     "Total outlays fell between Year 1 and Year 3"], ans=0,
   why="Mandatory runs 2,400 then 2,700 then 3,050, and discretionary runs 1,300 then 1,280 then 1,240. Outlays exceed revenues in every year, and mandatory is larger than discretionary throughout."),

 dict(q=_BUDGET + " Which statement in the course framework do these data most directly illustrate?",
   table=_BUDGET_TABLE,
   choices=[
     "That as entitlement costs grow, discretionary spending opportunities decrease unless revenues rise or the deficit grows",
     "That mandatory spending is approved on an annual basis",
     "That discretionary spending is required by law for entitlement programs",
     "That the budget must be balanced in each fiscal year",
     "That pork-barrel legislation determines the size of the budget"], ans=0,
   why="Rising mandatory outlays alongside falling discretionary outlays is EK 2.2.A.4.ii's squeeze. The second and third options swap the framework's two definitions."),

 dict(q=_BUDGET + " By how much did the gap between total outlays and total revenues change between Year 1 and Year 3?",
   table=_BUDGET_TABLE,
   choices=[
     "It grew by 350 billion dollars, from 400 billion to 750 billion",
     "It shrank by 350 billion dollars, from 750 billion to 400 billion",
     "It stayed the same at 400 billion dollars",
     "It grew by 750 billion dollars, from zero to 750 billion",
     "It cannot be determined, because the table reports no revenue figures"], ans=0,
   why="Year 1 outlays of 3,700 less revenues of 3,300 leaves 400; Year 3 outlays of 4,290 less revenues of 3,540 leaves 750; the increase is 350. The table's last row reports revenues directly."),

 dict(q=_RULES + " Which conclusion is best supported by the table?",
   table=_RULES_TABLE,
   choices=[
     "Three of the five procedures operate in the House and two in the Senate",
     "All five procedures operate in the same chamber",
     "The two Senate procedures both work to speed a bill toward a vote",
     "Every procedure listed makes it easier for a bill to reach a vote",
     "No procedure listed affects floor debate"], ans=0,
   why="The chamber column reads House three times and Senate twice. The two Senate entries pull in opposite directions, since the filibuster prolongs debate and cloture ends it."),

 dict(q=_RULES + " Which pair of procedures in the table work in opposite directions on the same bill?",
   table=_RULES_TABLE,
   choices=[
     "The filibuster, which prolongs debate, and cloture, which ends it",
     "The Rules Committee, which sets the terms of debate, and the Committee of the Whole, which expedites it",
     "The discharge petition, which brings a bill to the floor, and the Rules Committee, which sets terms of debate",
     "Cloture, which ends debate, and the Committee of the Whole, which expedites debate",
     "The filibuster, which prolongs debate, and the discharge petition, which brings a bill to the floor"], ans=0,
   why="EK 2.2.A.3.ii pairs the two Senate procedures as tactic and counter-tactic, and only that pair has one entry prolonging and the other ending the same debate. The other options pair procedures in different chambers or pointing the same way."),

 dict(q=_RULES + " A student concludes from the table that the House has more procedural tools than the Senate. Which limitation of the data most undercuts that conclusion?",
   table=_RULES_TABLE,
   choices=[
     "The table lists five selected procedures rather than all of them, so the count reflects which rows were chosen",
     "The table omits the Senate entirely, so no comparison is possible",
     "The table reports how often each procedure is used, which is not the same as how many exist",
     "The table covers only procedures used in a single Congress",
     "The table gives no information about what any procedure does"], ans=0,
   why="Counting rows in a curated list measures the list, not the institution, which is the data-limitation skill at CED 3.E. The table plainly names the Senate twice and carries an effect column."),

 dict(q=_STAGE + " Which conclusion is best supported by the data?",
   table=_STAGE_TABLE,
   choices=[
     "Fewer than one in five bills introduced were reported out of committee",
     "More than half of the bills introduced passed the chamber of origin",
     "Every bill that passed both chambers was signed into law",
     "The largest drop in the number of bills occurred after passage by both chambers",
     "More bills were signed into law than were reported out of committee"], ans=0,
   why="1,050 of 6,400 is about 16 percent, under one in five. The largest drop is the 5,350 lost at the committee stage, and 30 bills that passed both chambers were not signed."),

 dict(q=_STAGE + " Which feature of the legislative process do these data most directly illustrate?",
   table=_STAGE_TABLE,
   choices=[
     "That committees are the stage at which most bills die, which is why control of committee leadership matters",
     "That the president rejects most bills that reach his desk",
     "That the Senate is the chamber in which most bills fail",
     "That most bills introduced eventually become law",
     "That conference committees reject most bills sent to them"], ans=0,
   why="The count falls from 6,400 to 1,050 at the committee stage, a larger loss than every later stage combined, which is EK 2.2.A.2's committee gate. The table follows bills from one chamber and cannot single out the Senate."),

 dict(q=_STAGE + " A student concludes from the table that Congress is unproductive because so few bills become law. Which limitation of the data most undercuts that conclusion?",
   table=_STAGE_TABLE,
   choices=[
     "The table counts bills without regard to their contents, and a single enacted bill may carry the substance of many that died",
     "The table omits the number of bills introduced, so no rate can be computed",
     "The table reports percentages that do not sum to one hundred",
     "The table covers a single day of the legislative session",
     "The table gives no information about whether any bill became law"], ans=0,
   why="A raw survival rate treats every bill as equivalent, and omnibus and appropriation bills routinely absorb provisions from bills that never advanced on their own. The table plainly reports both the introduction count and the enactment count."),
]
