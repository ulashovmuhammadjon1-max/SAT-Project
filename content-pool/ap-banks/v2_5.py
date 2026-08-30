# AP U.S. GOVERNMENT AND POLITICS 2.5 Checks on the Presidency -- 30 questions
# CED V.1 (c) 2026, Unit 2 Interactions Among Branches of Government.
# Learning objective 2.5.A: explain how the president's agenda can create
# tension and frequent confrontations with Congress.
# Suggested skill for this topic (CED p. 65): 1.E, explain how political
# principles, institutions, processes, policies and behaviors apply to different
# SCENARIOS IN CONTEXT. So this module is weighted to scenario items: most stems
# describe a situation and ask what it illustrates or what follows from it.
#
# Essential knowledge relied on:
#   EK 2.5.A.1 -- "Senate confirmation is an important check on appointment
#     powers but there can be a potential for conflict based on who is chosen by
#     the president for appointments, including:
#       i.   Cabinet members
#       ii.  Ambassadors
#       iii. Some positions within the Executive Office of the President
#       iv.  Supreme Court Justices, Court of Appeals judges, and District Court
#            judges"
#   EK 2.5.A.2 -- "Senate confirmation is an important check on appointment
#     powers, but the president's LONGEST LASTING INFLUENCE lies in LIFE-TENURED
#     JUDICIAL APPOINTMENTS."
#   EK 2.5.A.3 -- "Policy conflicts with the CONGRESSIONAL AGENDA (the formal
#     list of policies Congress is considering at any given time) can lead the
#     president to use EXECUTIVE ORDERS AND DIRECTIVES TO THE BUREAUCRACY to
#     address the president's own agenda items."
#
# THE WORD "SOME" IN EK 2.5.A.1.iii IS LOAD-BEARING and item 5 is built on it.
# The framework says SOME positions within the Executive Office of the President
# require confirmation, not all of them. A student who generalises to "every
# White House official must be confirmed" has learned something false, and the
# framework's own list is careful in a way a paraphrase usually is not.
#
# THE CLAIM AT EK 2.5.A.2 IS COMPARATIVE, not absolute, and items 11 to 15 keep
# it that way. The framework does not say judicial appointments are the
# president's most important power; it says they are the LONGEST LASTING
# INFLUENCE, and the reason is life tenure -- a judge outlasts the president who
# appointed him. Every item here that touches EK 2.5.A.2 turns on DURATION.
#
# EK 2.5.A.3 SUPPLIES THE CED'S OWN DEFINITION of the congressional agenda: "the
# formal list of policies Congress is considering at any given time." That
# parenthesis is examinable text and item 16 quotes it.
#
# Documents the CED attaches to 2.5.A (p. 26-27): the Emancipation Proclamation,
# Federalist No. 51, Federalist No. 70.
#
# QUOTATION POLICY, per SOCIAL_BRIEF.md: constitutional text and Federalist
# No. 51 are quoted verbatim; the Federalist No. 70 excerpt is the one the CED
# itself quotes at EK 2.6.A.1. Both tables are labelled hypothetical.
#
# NOTATION: no digit-hyphen-digit and no digit-slash-digit anywhere. The
# verifier enforces it.
#
# FIVE choices (A-E); key written first throughout.
TOPIC = ("2.5", "Checks on the Presidency", 2)

_CONFIRM = ("In a hypothetical presidency, the table reports how the Senate disposed of "
            "nominations in four categories over a four-year term.")
_CONFIRM_TABLE = dict(
    headers=["Category of nominee", "Confirmed", "Rejected or withdrawn", "No action taken"],
    rows=[["Cabinet members", "21", "2", "0"],
          ["Ambassadors", "148", "9", "37"],
          ["Court of Appeals judges", "31", "4", "19"],
          ["District Court judges", "96", "5", "44"]])

_ORDERS = ("In a hypothetical study, the table reports the number of executive orders a "
           "president issued in years of unified and of divided party control of Congress.")
_ORDERS_TABLE = dict(
    headers=["Year", "Party control of Congress", "Executive orders issued"],
    rows=[["Year 1", "Unified", "29"],
          ["Year 2", "Unified", "34"],
          ["Year 3", "Divided", "58"],
          ["Year 4", "Divided", "66"]])

QUESTIONS = [
 dict(q="According to the course framework, Senate confirmation is best described as",
   choices=[
     "an important check on the president's appointment powers",
     "a formality that has no effect on who serves in the executive branch",
     "a power the Senate shares equally with the House of Representatives",
     "a requirement that applies only to judicial nominations",
     "a procedure by which the Senate selects nominees for the president to appoint"], ans=0,
   why="EK 2.5.A.1 and EK 2.5.A.2 both open with the same phrase: Senate confirmation is an important check on appointment powers. The House has no role, and the president nominates."),

 dict(q="Which of the following categories of appointment does the course framework NOT list as subject to Senate confirmation?",
   choices=[
     "Members of the president's personal household staff",
     "Cabinet members",
     "Ambassadors",
     "Supreme Court Justices",
     "District Court judges"], ans=0,
   why="EK 2.5.A.1 lists Cabinet members, ambassadors, some positions within the Executive Office of the President, and Supreme Court, Court of Appeals and District Court judges. Household staff appear nowhere on the list."),

 dict(q="The Senate rejects a president's nominee for a Cabinet department after hearings reveal disagreement about the nominee's policy views. According to the course framework, this episode illustrates",
   choices=[
     "Senate confirmation operating as a check, with conflict arising from who was chosen",
     "the president's power to appoint without any legislative involvement",
     "the House of Representatives exercising its confirmation power",
     "an executive order being blocked by the Senate",
     "a pocket veto of a nomination"], ans=0,
   why="EK 2.5.A.1 says confirmation is an important check but that conflict can arise 'based on who is chosen by the president for appointments,' which is exactly a rejection on the nominee's views."),

 dict(q="Which statement about the confirmation of judicial nominees is accurate under the course framework?",
   choices=[
     "Supreme Court Justices, Court of Appeals judges and District Court judges are all subject to Senate confirmation",
     "Only Supreme Court Justices are subject to Senate confirmation",
     "Judicial nominees are confirmed by both chambers of Congress",
     "Judicial nominees take office without confirmation and may be removed by the Senate later",
     "District Court judges are appointed by state governors"], ans=0,
   why="EK 2.5.A.1.iv names all three levels of the federal judiciary in one item, so the check reaches the whole federal bench rather than the Supreme Court alone."),

 dict(q="What does the course framework say about positions within the Executive Office of the President?",
   choices=[
     "Some of them are subject to Senate confirmation",
     "All of them are subject to Senate confirmation",
     "None of them is subject to Senate confirmation",
     "They are filled by the Senate rather than by the president",
     "They are subject to confirmation only during a president's first year in office"], ans=0,
   why="EK 2.5.A.1.iii says SOME positions within the Executive Office of the President, and the word is deliberate. Generalizing it in either direction misstates the framework."),

 dict(q="A president's nominee for an ambassadorship is never brought to a vote, and the nomination expires at the end of the Congress. Which observation about the confirmation check does this best illustrate?",
   choices=[
     "The Senate can defeat a nomination by inaction as effectively as by a vote against it",
     "A nomination becomes effective automatically if the Senate takes no action",
     "The president may install the nominee without Senate involvement once a year has passed",
     "Only a formal vote against a nominee counts as an exercise of the confirmation check",
     "The House may confirm a nominee the Senate has ignored"], ans=0,
   why="EK 2.5.A.1 makes confirmation a check on the appointment power, and a check operates whenever it prevents the appointment, whether by rejection or by never scheduling the vote."),

 dict(q="Read the following excerpt.\n\n“He shall nominate, and by and with the Advice and Consent of the Senate, shall appoint Ambassadors, other public Ministers and Consuls, Judges of the supreme Court, and all other Officers of the United States, whose Appointments are not herein otherwise provided for.”\n—U.S. Constitution, Article II, Section 2\n\nWhich division of responsibility does this passage establish?",
   choices=[
     "The president chooses the nominee and the Senate decides whether the appointment is made",
     "The Senate chooses the nominee and the president decides whether the appointment is made",
     "The president appoints without any role for the Senate",
     "The Senate appoints without any role for the president",
     "Both chambers of Congress must consent before an appointment is made"], ans=0,
   why="The clause separates nomination, which is the president's, from appointment, which requires the Senate's advice and consent. That separation is what makes confirmation the check EK 2.5.A.1 describes."),

 dict(q="Read the following excerpt.\n\n“Ambition must be made to counteract ambition. The interest of the man must be connected with the constitutional rights of the place.”\n—James Madison, Federalist No. 51, 1788\n\nHow does the Senate's confirmation power illustrate Madison's principle?",
   choices=[
     "Senators defend the Senate's institutional prerogative even when doing so obstructs a president of their own party",
     "Senators are required by the Constitution to defer to a president of their own party",
     "The president and the Senate are prevented from disagreeing about appointments",
     "Confirmation ensures that only nominees with no political views are appointed",
     "The Senate's power over appointments makes the president's nomination power meaningless"], ans=0,
   why="Madison's design gives each institution a power and its officeholders a motive to use it, and a confirmation fight inside a party is the clearest case of institutional interest asserting itself over partisan convenience."),

 dict(q="A president complains that the Senate has confirmed few of her nominees and that agencies are operating with acting officials. Which trade-off in the constitutional design does this situation reflect?",
   choices=[
     "The check that prevents unsuitable appointments also slows the staffing of the executive branch",
     "The check applies only to nominees the president's own party opposes",
     "The Senate is constitutionally required to act on every nomination within one session",
     "Acting officials may not exercise any authority of the office they occupy",
     "The president may fill any vacancy permanently once the Senate has delayed"], ans=0,
   why="EK 2.5.A.1 presents confirmation as a check with a potential for conflict built into it, and delay is that conflict's ordinary cost. Nothing requires the Senate to act within a set period."),

 dict(q="According to the course framework, where does a president's longest lasting influence lie?",
   choices=[
     "In life-tenured judicial appointments",
     "In executive orders, which remain in force indefinitely",
     "In treaties, which bind future presidents",
     "In Cabinet appointments, which shape a department for decades",
     "In signing statements, which control how courts read a statute"], ans=0,
   why="EK 2.5.A.2 says the president's longest lasting influence lies in life-tenured judicial appointments. The claim is about DURATION, and the reason is the tenure, not the importance of the office."),

 dict(q="Why does the course framework single out judicial appointments as the president's longest lasting influence?",
   choices=[
     "Federal judges hold office during good behavior, so an appointee may serve for decades after the appointing president has left office",
     "Federal judges may be removed only by the president who appointed them",
     "Judicial appointments do not require Senate confirmation and so are easier to make",
     "Federal judges are elected to fixed terms that outlast a presidential term",
     "Judicial decisions may not be changed by any later act of government"], ans=0,
   why="EK 2.5.A.2's reason is life tenure, which U.S. Constitution Article III Section 1 supplies as office held during good behavior. Judicial appointments do require confirmation, per EK 2.5.A.1.iv."),

 dict(q="A president serves one term and appoints two Supreme Court Justices and forty lower court judges. Twenty years later, most of the president's executive orders have been revoked but most of the judges are still serving. Which claim from the course framework does this best illustrate?",
   choices=[
     "That the president's longest lasting influence lies in life-tenured judicial appointments",
     "That executive orders are the president's most powerful instrument",
     "That Senate confirmation has no effect on who becomes a judge",
     "That a president's agenda ends when the term ends",
     "That judicial appointments require no Senate action"], ans=0,
   why="EK 2.5.A.2's claim is comparative and about duration, and the contrast between revoked orders and sitting judges is exactly the comparison the statement makes."),

 dict(q="A commentator argues that a president's judicial appointments matter more than his legislative record. Which qualification does the course framework support?",
   choices=[
     "The framework claims only that judicial appointments last longest, which is a claim about duration rather than about importance",
     "The framework claims that judicial appointments are the only influence a president has",
     "The framework claims that legislative records have no lasting effect",
     "The framework claims that judicial appointments are unimportant compared with executive orders",
     "The framework makes no claim about the duration of any presidential influence"], ans=0,
   why="EK 2.5.A.2 says longest LASTING influence, which is a statement about how long an effect persists. Reading it as a ranking of importance imports a claim the framework does not make."),

 dict(q="Which feature of judicial appointments makes the Senate's confirmation check especially consequential?",
   choices=[
     "Because the appointment is for life, an error cannot be corrected at the next election",
     "Because judges serve fixed terms, the Senate may reconsider each appointment periodically",
     "Because the president may remove a judge at will, confirmation is largely symbolic",
     "Because judicial nominees are confirmed by a two-thirds vote, rejection is common",
     "Because the House also votes on judicial nominees, agreement is rare"], ans=0,
   why="EK 2.5.A.1 makes confirmation a check and EK 2.5.A.2 supplies the life tenure, and the two together mean the Senate's decision is close to final. The House has no role and no supermajority is required."),

 dict(q="According to the course framework, the congressional agenda is",
   choices=[
     "the formal list of policies Congress is considering at any given time",
     "the president's list of legislative priorities for the coming year",
     "the schedule of committee hearings for a single week",
     "the party platform adopted at a national convention",
     "the list of nominations awaiting Senate action"], ans=0,
   why="EK 2.5.A.3 defines the congressional agenda in exactly these words, in its own parenthesis. It is Congress's list rather than the president's."),

 dict(q="According to the course framework, what can a president do when policy conflicts with the congressional agenda block the president's own priorities?",
   choices=[
     "Use executive orders and directives to the bureaucracy to address the president's agenda items",
     "Enact the proposals directly as statutes without congressional action",
     "Dissolve Congress and call new elections",
     "Direct the Supreme Court to rule on the disputed policy",
     "Suspend the congressional agenda until the dispute is resolved"], ans=0,
   why="EK 2.5.A.3 names executive orders and directives to the bureaucracy as the response to policy conflicts with the congressional agenda. The other four options describe powers no branch holds."),

 dict(q="A president unable to persuade Congress to fund a program instead directs the relevant department to reprioritize its existing appropriations toward the same goal. Which limit on that strategy is most important?",
   choices=[
     "The directive can reach only what existing law and existing appropriations already permit",
     "The directive requires Senate confirmation before the department may act",
     "The directive must be approved by a two-thirds vote of both chambers",
     "The directive automatically expires after ninety days",
     "The directive may be issued only if Congress has formally adjourned"], ans=0,
   why="EK 2.5.A.3's instruments are directives to the bureaucracy, and EK 2.4.A.2.iv grounds executive orders in vested or delegated power, so neither can create authority or money that Congress has not supplied."),

 dict(q="A president issues an executive order on an issue Congress has debated for two years without acting. Which description of the situation is most consistent with the course framework?",
   choices=[
     "A policy conflict with the congressional agenda has led the president to act through the bureaucracy instead",
     "The president has amended the congressional agenda by executive action",
     "Congress has delegated its legislative power to the president",
     "The executive order becomes a statute once Congress fails to act for two years",
     "The president has exercised the pocket veto"], ans=0,
   why="EK 2.5.A.3 describes exactly this sequence: conflict with what Congress is considering, followed by executive orders and directives to address the president's own agenda items. An order does not become a statute."),

 dict(q="Which of the following is the strongest congressional response to a president who governs extensively through executive orders?",
   choices=[
     "Enacting a statute that removes or narrows the authority the orders rest on",
     "Passing a resolution expressing disapproval of the orders",
     "Refusing to confirm judicial nominees until the orders are withdrawn",
     "Asking the Supreme Court for an advisory opinion on the orders",
     "Adjourning so that the president may issue no further orders"], ans=0,
   why="EK 2.4.A.2.iv grounds executive orders in vested or delegated power, so legislation withdrawing the delegation strikes at the source. Federal courts do not issue advisory opinions, and adjournment does not suspend the executive power."),

 dict(q="Read the following excerpt.\n\n“A feeble Executive implies a feeble execution of the government. A feeble execution is but another phrase for a bad execution; and a government ill executed, whatever it may be in theory, must be, in practice, a bad government.”\n—Alexander Hamilton, Federalist No. 70, 1788\n\nHow would a president most likely use this passage in a confrontation with Congress?",
   choices=[
     "To argue that an executive able to act decisively is a requirement of good government, not a threat to it",
     "To argue that the executive should be subject to no check by the legislature",
     "To argue that executive power should be divided among several officials",
     "To argue that Congress rather than the president should administer the laws",
     "To argue that the president may disregard statutes he considers unwise"], ans=0,
   why="Federalist No. 70 argues for a single energetic executive as a component of good government; Hamilton opposes a plural executive, which is why the third option states his adversary's position rather than his."),

 dict(q=_CONFIRM + " Which conclusion is best supported by the data?",
   table=_CONFIRM_TABLE,
   choices=[
     "Cabinet nominations were the only category on which the Senate always acted",
     "Every category shows more nominations rejected or withdrawn than left without action",
     "Court of Appeals judges were confirmed more often than District Court judges",
     "No nomination in any category was rejected or withdrawn",
     "Ambassadorial nominations were the most likely to be rejected outright"], ans=0,
   why="The Cabinet row is the only one with zero in the no-action column. In the other three rows inaction outnumbers rejection, and 31 Court of Appeals confirmations is fewer than 96 District Court confirmations."),

 dict(q=_CONFIRM + " Which conclusion about the confirmation check is best supported by the data?",
   table=_CONFIRM_TABLE,
   choices=[
     "Inaction, not rejection, is the Senate's most common way of defeating a nomination",
     "Rejection is the Senate's most common way of defeating a nomination",
     "The Senate confirms every judicial nominee it considers",
     "The Senate treats Cabinet and judicial nominations identically",
     "The Senate rejects more nominees than it confirms in every category"], ans=0,
   why="Across the four rows, 100 nominations lapsed without action against 20 rejected or withdrawn, so inaction defeats five times as many nominees as rejection. Confirmations outnumber both in every row."),

 dict(q=_CONFIRM + " A student concludes that the Senate is hostile to judicial nominees in particular. Which limitation of the data most undercuts that conclusion?",
   table=_CONFIRM_TABLE,
   choices=[
     "The table reports a single presidency, so it cannot show whether this pattern is unusual or typical",
     "The table omits judicial nominees entirely, so no comparison is possible",
     "The table reports percentages that do not sum to one hundred",
     "The table gives no information about how many nominees were confirmed",
     "The table covers a single year, so no pattern can be observed"], ans=0,
   why="One administration's record supplies no baseline against which to call a pattern hostile, which is the standard limitation of a single-case table. Two judicial rows, a confirmed column and a four-year term are all plainly present."),

 dict(q=_ORDERS + " Which conclusion is best supported by the data?",
   table=_ORDERS_TABLE,
   choices=[
     "The president issued more executive orders in each divided-control year than in either unified-control year",
     "The president issued more executive orders in each unified-control year than in either divided-control year",
     "The number of executive orders was the same in every year",
     "The president issued fewer executive orders in the final year than in the first",
     "Party control of Congress was divided in every year shown"], ans=0,
   why="The two unified years show 29 and 34 orders and the two divided years 58 and 66, so every divided year exceeds every unified year. The final year is the highest of the four."),

 dict(q=_ORDERS + " Which claim from the course framework do these data most directly illustrate?",
   table=_ORDERS_TABLE,
   choices=[
     "That policy conflicts with the congressional agenda can lead a president to use executive orders to address his own agenda items",
     "That Senate confirmation is an important check on appointment powers",
     "That the president's longest lasting influence lies in life-tenured judicial appointments",
     "That vetoes can be overridden while pocket vetoes cannot",
     "That the congressional agenda is the formal list of policies Congress is considering"], ans=0,
   why="EK 2.5.A.3 links policy conflict with the congressional agenda to the use of executive orders, and divided control is the condition under which such conflict is most likely. The other options name statements these columns do not measure."),

 dict(q=_ORDERS + " A student concludes that divided government CAUSES presidents to issue more executive orders. Which limitation of the data most undercuts that conclusion?",
   table=_ORDERS_TABLE,
   choices=[
     "The divided-control years are also the later years of the term, so time in office and party control cannot be separated here",
     "The table omits the number of executive orders issued, so no comparison is possible",
     "The table reports only years of unified control, so no comparison is possible",
     "The table gives percentages rather than counts, so no total can be computed",
     "The table covers a single year, so no pattern can be observed"], ans=0,
   why="Unified control occupies Years 1 and 2 and divided control Years 3 and 4, so the two explanations are perfectly confounded in this table. Both variables and four years are plainly present."),

 dict(q="A president's party holds a majority in both chambers, yet several of the president's nominees still face difficulty. Which explanation is most consistent with the course framework?",
   choices=[
     "Conflict can arise from who is chosen, and senators of the president's own party may object to a particular nominee",
     "Senate confirmation applies only during periods of divided government",
     "A nominee opposed by any senator cannot be confirmed",
     "The Senate must reject at least one nominee in each category each year",
     "Confirmation votes are taken by the House when the Senate is controlled by the president's party"], ans=0,
   why="EK 2.5.A.1 locates the potential for conflict in WHO IS CHOSEN rather than in which party controls the chamber, so a unified Senate can still balk at a particular nomination."),

 dict(q="Which question would best test the framework's claim that policy conflict pushes presidents toward executive action?",
   choices=[
     "Do presidents issue more executive orders on subjects where their legislative proposals have failed than on subjects where they have passed?",
     "Do presidents issue more executive orders in their first year than in later years?",
     "Do presidents who issue many executive orders have higher approval ratings?",
     "Do presidents issue more executive orders than their predecessors did?",
     "Do executive orders run longer than the statutes on the same subject?"], ans=0,
   why="EK 2.5.A.3's claim links a specific conflict to a specific response, so the test has to compare executive action across subjects where the legislative route succeeded and failed. Totals and trends over time do not isolate the mechanism."),

 dict(q="A senator argues that the confirmation power should be used to shape policy, not merely to screen for competence. Which feature of the framework's account best supports her position?",
   choices=[
     "The framework locates the potential for conflict in who is chosen, which makes a nominee's views a legitimate subject of the check",
     "The framework says confirmation applies only to nominees whose competence is in doubt",
     "The framework gives the Senate the power to nominate as well as to confirm",
     "The framework says a president must consult the Senate before selecting a nominee",
     "The framework says confirmation votes must be unanimous"], ans=0,
   why="EK 2.5.A.1 says the potential for conflict arises 'based on who is chosen by the president,' which is a statement about the identity and views of the nominee rather than about qualifications alone."),

 dict(q="Which pair of powers, taken together, best explains why a president and a Senate controlled by the other party come into frequent confrontation?",
   choices=[
     "The president's power to nominate and the Senate's power to withhold consent, which give each side a decision the other cannot make alone",
     "The president's power to veto and the Senate's power to veto",
     "The Senate's power to nominate and the president's power to confirm",
     "The president's power to adjourn Congress and the Senate's power to convene it",
     "The Senate's power to issue executive orders and the president's power to repeal them"], ans=0,
   why="U.S. Constitution Article II Section 2 splits the appointment between nomination and consent, and EK 2.5.A.1 makes that split the site of conflict. The other options assign powers to institutions that do not hold them."),
]
